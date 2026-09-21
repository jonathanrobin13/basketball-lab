import React, {useRef, useState} from 'react'


function Camera() {
	
	const videoRef = useRef(null);
	const facingModeRef = useRef("user");
	const switchCameraStyle = useRef();

	const [streamState, setStream] = useState(false);	
	const [cameraMessage, setCameraMessage] = useState("Camera is off");
	const [buttonText, setButton] = useState("Turn camera on");
	const [switchCameraAllowed, setSwitchCameraAllowed] = useState(false);

			
	const startCamera = (facingMode) => {
		navigator.mediaDevices.getUserMedia({audio: false, video: {facingMode: facingMode}})
		.then((stream) => {
			videoRef.current.srcObject = stream;
			setStream(true);
			
			setButton("Turn camera off");
			setCameraMessage("Camera is on.");
			setSwitchCameraAllowed(true);
			switchCameraStyle.current.style.backgroundColor = "blue";
			
		})
		.catch((error) => {
			if (error.name === "NotAllowedError") {
				setCameraMessage("Please allow permission to access camera.");
			}
		});
	};
		

	const stopCamera = () => {
		const tracks = videoRef.current.srcObject.getTracks();
		tracks.forEach(track => track.stop());
		videoRef.current.srcObject = null;
		
		setButton("Turn camera on");
		setStream(false);
		setCameraMessage("Camera is off.");
		setSwitchCameraAllowed(false);
		switchCameraStyle.current.style.backgroundColor = "rgb(0, 0, 0)"
		
	};
	
	const handleCamera = () => {
		if (!streamState) {
			startCamera(facingModeRef.current);
		} else {
			stopCamera();
		}

	};
	
	const switchCamera = () => {
		if (switchCameraAllowed) {		
			// stop camera
			stopCamera();
			
			facingModeRef.current = facingModeRef.current === "user" ? "environment" : "user";
			
			startCamera(facingModeRef.current);
		}
	
	};
		
		
		
	
	
	return(
		<>	
			<video ref={videoRef} autoPlay></video>
			<button className="button" onClick={handleCamera}>{buttonText}</button>
			<button className="button" onClick={switchCamera} ref={switchCameraStyle} id="switch-camera-btn">Switch Camera</button>
			<p>{cameraMessage}</p>
		</>
	);
}

export default Camera