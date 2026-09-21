import logo from './assets/react.svg'

function Card(props) {
	return(
		<div className="card">
			<img className="card-image" src={logo} alt="Logo for BasketLab"></img>
			<h2 className="card-heading">{props.heading}</h2>
			<p className="card-text">{props.text}</p>
		</div>
	);
}


export default Card