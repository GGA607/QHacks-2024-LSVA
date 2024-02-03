
document.getElementById("getPromptBtn").addEventListener("click", async () => {
    const promptDisplay = document.getElementById("promptDisplay");

    try {
        
        const response = await fetch("prompts.json");
        const data = await response.json(); // Parse the JSON data
        const promptsArray = data.prompts; // Extract the array of prompts from the JSON data

        const randomIndex = Math.floor(Math.random() * promptsArray.length); // Generate a random index
        const randomPrompt = promptsArray[randomIndex]; // Select a random prompt from the array

        // Update the UI with the randomly selected prompt
        promptDisplay.innerText = randomPrompt;
    } catch (error) {
        console.error("Error fetching prompts:", error);
        promptDisplay.innerText = "Error fetching prompts.";
    }
});
