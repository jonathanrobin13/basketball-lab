import React, {useState} from 'react';


function Button() {
	
	const styles = {
		backgroundColor: "blue",
		color: "white",
		border: "none",
		borderRadius: "5px",
		padding: "5px 10px",
		margin: "5px 10px",
		boxShadow: "3px 3px 2px rgba(0, 0, 0, 0.25)",
		cursor: "pointer"
	};

	const [isCameraOn, setCamera] = useState(false);
	
	const turnCamera = (e) => {
		if (isCameraOn) {
			setCamera(false);
			e.target.textContent = "Turn Camera On";
		} else {
			setCamera(true);
			e.target.textContent = "Turn Camera off";
		}
	};

	return(
		<button style={styles} onClick={(e) => turnCamera(e)}>Turn Camera On</button>
	);
}

export default Button