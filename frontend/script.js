const video = document.getElementById("camera");
if (video) {
navigator.mediaDevices.getUserMedia({ video: true })
    .then(stream => {
        video.srcObject = stream;
    });
}

const button = document.getElementById("button");
const result = document.getElementById("result");
	
button.addEventListener("click", async () => {
    const response = await fetch("http://localhost:8000/tracking");

    const data = await response.json();

    result.textContent = data.message;
});