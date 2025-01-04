const textContainer = document.getElementById('text-container');

// The text to display line by line
const lines = [
    "Line 1: Welcome to my portfolio!",
    "Line 2: I am an AI Engineer passionate about solving problems.",
    "Line 3: I specialize in Computer Vision and Intelligent Systems.",
    "Line 4: Let's create something amazing together!"
];

const typingSpeed = 50; // Typing speed (ms) per character
const lineDelay = 1000; // Delay (ms) between lines

// Function to simulate typing
function typeLine(line, callback) {
    let charIndex = 0;
    const interval = setInterval(() => {
        if (charIndex < line.length) {
            textContainer.innerHTML += line[charIndex];
            charIndex++;
        } else {
            clearInterval(interval);
            callback();
        }
    }, typingSpeed);
}

// Function to display lines one by one
function displayLines(index = 0) {
    if (index < lines.length) {
        typeLine(lines[index], () => {
            textContainer.innerHTML += '\n'; // Add a line break after each line
            setTimeout(() => displayLines(index + 1), lineDelay);
        });
    }
}

// Start the typing animation
displayLines();
