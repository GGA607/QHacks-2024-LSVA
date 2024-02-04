document.addEventListener("DOMContentLoaded", () => {
    const getPromptBtn = document.querySelector(".getPromptBtn");
    const promptDisplay = document.getElementById("promptDisplay");
    const recordStartDisplay = document.getElementById("recordButton");
    const recordStopDisplay = document.getElementById("stopRecordButton");

    getPromptBtn.addEventListener("click", async () => {
        
        getPromptBtn.parentNode.remove();

        const strtbtn = document.createElement("button");
        strtbtn.innerHTML = "Start Recording";
        recordStartDisplay.appendChild(strtbtn);

        const stpbtn = document.createElement("button");
        stpbtn.innerHTML = "Stop Recording";
        recordStopDisplay.appendChild(stpbtn);

        let mediaRecorder;
        let audioChunks = [];

        strtbtn.addEventListener("click", startRecording);
        stpbtn.addEventListener("click", stopRecording);

        const downloadLink = document.getElementById("downloadLink");

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
                  const audioBlob = new Blob(audioChunks, { type: "audio/wav" });
                  const audioUrl = URL.createObjectURL(audioBlob);

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
            if (mediaRecorder.state === "recording") {
              mediaRecorder.stop();
              strtbtn.disabled = false;
              stpbtn.disabled = true;
            }
          }
    


        try {
            const response = await fetch("prompts.json");
            const data = await response.json();
            const promptsArray = data.interviewQuestions;

            if (promptsArray && promptsArray.length > 0) {
                const randomIndex = Math.floor(Math.random() * promptsArray.length);
                const randomPrompt = promptsArray[randomIndex];

                // Update the UI with the randomly selected prompt
                promptDisplay.innerText = "Q. " + randomPrompt;
            } else {
                promptDisplay.innerText = "No prompts available.";
            }
        } catch (error) {
            console.error("Error fetching or parsing prompts:", error);
            promptDisplay.innerText = "Error fetching or parsing prompts.";
        }
    });
});


