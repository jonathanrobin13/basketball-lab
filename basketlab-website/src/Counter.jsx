import React, {useState} from 'react';

function Counter() {
	const buttonStyles = {
		backgroundColor: "blue",
		color: "white",
		border: "none",
		borderRadius: "5px",
		padding: "5px 10px",
		margin: "5px 10px",
		boxShadow: "3px 3px 2px rgba(0, 0, 0, 0.25)",
		cursor: "pointer"
	};
	
	const numberStyles = {
	
	};
	
	const [number, setNumber] = useState(0);
	
	const addOne = () => {
		setNumber(number + 1);
	}
	
	const reset = () => {
		setNumber(0);
	}
	
	const substractOne = () => {
		setNumber(number - 1);
	}
	
	
	return(
		<>
			<button style={buttonStyles} onClick={substractOne}>- 1</button>
			<button style={buttonStyles} onClick={reset}>Reset</button>
			<button style={buttonStyles} onClick={addOne}>+ 1</button>
			<p style={numberStyles}>{number}</p>
		</>
	);
}

export default Counter
