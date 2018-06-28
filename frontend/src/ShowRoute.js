import React from 'react';
import start from './image/start.png'

// function to show the user the route between stations with in between stations shown also
class ShowRoute extends React.Component {
	render() {
		return (
			<div className="show-route">
				<p><i className="fas fa-bus"></i><span className="start"> Bus Line: 46A</span></p>
				<hr/>
				<p>UCD</p>
				<ul>
					<li>Station 1</li>
					<li>Station 2</li>
					<li>Station 3</li>
				</ul>
				<p>TCD</p>
			</div>
		)
	}
}

export default ShowRoute
