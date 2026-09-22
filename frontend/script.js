const socket = new WebSocket("ws://localhost:8000/ws");

const cameraButton = document.getElementById("start-camera-button");
const webcam = document.getElementById("webcam");
const info = document.getElementById("info");

const captureCanvas = document.createElement("canvas");
const captureCtx = captureCanvas.getContext("2d");

const annotatedStreamCanvas = document.getElementById("annotated-stream");
const annotatedCtx = annotatedStreamCanvas.getContext("2d");

let isCameraOn = false;
let cameraStream = null;
let isSendingFrames = false;

function startVideo() {
	if (isCameraOn === false) {
		navigator.mediaDevices.getUserMedia({ video: true })
		.then((stream) => {
			webcam.srcObject = stream;
			info.textContent = "Camera is on";
			cameraStream = stream;
			isCameraOn = true;
			cameraButton.textContent = "Turn Camera Off";	
			
			frameSending()
		})
		.catch(() => {
			info.textContent = "Please turn on camera";
			
		})
	
	} else {
		cameraStream.getTracks().forEach(track => {
			track.stop();
		});
		
		info.textContent = "Camera is off";
		isCameraOn = false;
		cameraButton.textContent = "Turn Camera On";
	}		
}

async function frameSending() {
	while (isCameraOn) {
		processFrame();
		
		await new Promise(resolve => setTimeout(resolve, 100))
	}
}

function processFrame() {
	
	if (webcam.videoWidth === 0 || webcam.videoHeight === 0) {
		return;
	}
	
	captureCanvas.width = webcam.videoWidth;
	captureCanvas.height = webcam.videoHeight;
	
	captureCtx.drawImage(
		webcam,
		0,
		0,
		captureCanvas.width,
		captureCanvas.height
	);
	
	
	captureCanvas.toBlob(blob => {
		if (blob && socket.readyState === WebSocket.OPEN) {
			socket.send(blob);
		}}, "image/jpeg", 0.8);
		
		
}		

cameraButton.onclick = startVideo;

socket.onopen = () => {	
	socket.send(JSON.stringify({
		"connection-message":"Frontend connecting to backend"
	}));
	
}

socket.binaryType = "blob";

socket.onmessage = async (event) => {	
	
	if (typeof event.data === "string") {
		const data = JSON.parse(event.data);
		console.log(data["connection-message"]);
		console.log("success!");
	} else if (event.data instanceof Blob) {
		const blob = event.data;
		const bitmap = await createImageBitmap(blob);
		
		annotatedStreamCanvas.width = bitmap.width;
		annotatedStreamCanvas.height = bitmap.height;
		
		annotatedCtx.drawImage(bitmap, 0, 0);
		bitmap.close();
	}
};


	
	