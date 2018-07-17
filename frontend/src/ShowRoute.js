import React from 'react';
import start from './image/start.png'

// function to show the user the route between stations with in between stations shown also
class ShowRoute extends React.Component {
	render() {
		return (
			<div className="show-route">
				<p><i className="fas fa-bus"></i><span className="start"> Bus Line: {this.props.routeid}</span></p>
				<p className="from-to">From <span className="stop-name">{this.props.start}</span></p>
				<p className="from-to">To <span className="stop-name">{this.props.end}</span></p>
				<p className="from-to">Depart At: 10.00 a.m</p>
				<p className="from-to">Estimated Arrive At: 10.30 a.m</p>
				<p className="from-to"><i className="far fa-clock"></i> &nbsp; Duration: {this.props.prediction.totalDuration} miniutes</p>
				<hr/>
				<p className="from-to"><span className="stops-num">{this.props.prediction.stopsNum} Stops</span></p>
				<ul>
					{this.props.prediction.stopInfo.map(each => (
						<p key={each.stop_id} className="from-to">· {each.stop_name}</p>
					))}
				</ul>

			</div>
		)
	}
}

export default ShowRoute
