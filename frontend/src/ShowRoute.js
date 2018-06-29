import React from 'react';
import start from './image/start.png'

// function to show the user the route between stations with in between stations shown also
class ShowRoute extends React.Component {
	render() {
		return (
			<div className="show-route">
				<p><i className="fas fa-bus"></i><span className="start"> Bus Line: 46A</span></p>
				<p className="from-to">From <span className="stop-name">Crofton Road</span></p>
				<p className="from-to">To <span className="stop-name">Kill Lane Business Park</span></p>
				<p><i class="far fa-clock"></i> &nbsp; 20 miniutes</p>
				<hr/>
				<p>Crofton Road<span className="stops-num">9 Stops</span></p>
				<ul>
					<li>Marine Road	</li>
					<li>George's St</li>
					<li>York Road</li>
					<li>York Road</li>
					<li>Mounttown Rd</li>
					<li>Kill Avenue	Carriglea Avenue</li>
					<li>Kill Avenue	Kill O The Grange</li>
					<li>Kill Avenue	Church</li>
				</ul>
				<p>Kill Lane Business Park</p>
			</div>
		)
	}
}

export default ShowRoute
