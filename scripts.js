document.addEventListener("DOMContentLoaded", () => {
    const getPromptBtn = document.querySelector(".getPromptBtn");
    const promptDisplay = document.getElementById("promptDisplay");

    getPromptBtn.addEventListener("click", async () => {
        
        getPromptBtn.parentNode.remove();



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
