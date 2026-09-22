import Header from './Header.jsx'
import Footer from './Footer.jsx'
import Card from './Card.jsx'
import Button from './Button.jsx'
import Counter from './Counter.jsx'
import Camera from './Camera.jsx'

function App() {
	return(
			<>
				<Header />
				<Button />
				<br></br>
				<Card heading="Improve your Shot!" text="This will help you have the best shooting form"/>
				<Card heading="No prices." text="No prices needed. Just sign up and your ready!"/>
				<br />
				<Counter />
				<Camera />
				<Footer />
			</>
	);
}

export default App
