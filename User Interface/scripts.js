document.addEventListener("DOMContentLoaded", () => {
    const getPromptBtn = document.querySelector(".getPromptBtn");
    const promptDisplay = document.getElementById("promptDisplay");
    const recordStartDisplay = document.getElementById("recordButton");
    const recordStopDisplay = document.getElementById("stopRecordButton");

    let mediaRecorder;
    let audioChunks = [];

    getPromptBtn.addEventListener("click", async () => {
        getPromptBtn.parentNode.remove();

        const strtbtn = document.createElement("button");
        strtbtn.innerHTML = "Start Recording";
        recordStartDisplay.appendChild(strtbtn);

        const stpbtn = document.createElement("button");
        stpbtn.innerHTML = "Stop Recording";
        recordStopDisplay.appendChild(stpbtn);

        strtbtn.addEventListener("click", startRecording);
        stpbtn.addEventListener("click", stopRecording);

       
        function startRecording() {
            navigator.mediaDevices
                .getUserMedia({ audio: true })
                .then((stream) => {
                    mediaRecorder = new MediaRecorder(stream);
                    mediaRecorder.ondataavailable = (event) => {
                        if (event.data.size > 0) {
                            audioChunks.push(event.data);
                        }
                    };

                    mediaRecorder.onstop = () => {
                        // Do nothing here; handle audio data in ondataavailable
                    };

                    mediaRecorder.start();
                    strtbtn.disabled = true;
                    stpbtn.disabled = false;
                })
                .catch((error) => {
                    console.error("Error accessing microphone:", error);
                });
        }

        function stopRecording() {
            if (mediaRecorder && mediaRecorder.state === "recording") {
                mediaRecorder.stop();
                strtbtn.disabled = false;
                stpbtn.disabled = true;
                sendAudioToBackend(new Blob(audioChunks, { type: "audio/wav" }));
                console.log("Sent to backend");
            }
        }

        try {
            const response = await fetch("prompts.json");
            const data = await response.json();
            const promptsArray = data.interviewQuestions;

            if (promptsArray && promptsArray.length > 0) {
                const randomIndex = Math.floor(Math.random() * promptsArray.length);
                const randomPrompt = promptsArray[randomIndex];
                promptDisplay.innerText = "Q. " + randomPrompt;
            } else {
                promptDisplay.innerText = "No prompts available.";
            }
        } catch (error) {
            console.error("Error fetching or parsing prompts:", error);
            promptDisplay.innerText = "Error fetching or parsing prompts.";
        }

        function sendAudioToBackend(audioBlob) {
            const formData = new FormData();
            formData.append("audioFile", audioBlob, "recorded-speech.wav");

            fetch("/process_audio", {
                method: "POST",
                body: formData,
            })
                .then(response => response.json())
                .then(result => {
                    console.log("Backend response:", result);
                    // Handle the result from the backend
                })
                .catch(error => {
                    console.error("Error processing audio on the backend:", error);
                    // Handle the error, e.g., display an error message on the webpage
                });
        }
    });
});
