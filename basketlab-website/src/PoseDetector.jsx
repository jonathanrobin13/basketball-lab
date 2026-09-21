async function createObjectDetector {
	
	const vision = await FilesetResolver.forVisionTasks(
	"https://cdn.jsdelivr.net/npm/@mediapipe/tasks-vision@latest/wasm");
	
	// Create the detector 
	const poseLandmarker = poseLandmarker.createFromOptions(vision, {
		baseOptions: { modelAssetPath: "assets/models/pose_landmarker_lite.task"},
		runningMode: "VIDEO"
	});
	
	objectDetector.detect();
	
}

