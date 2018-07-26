import React from 'react';

// function to show the user the route between stations with in between stations shown also
class ShowRoute extends React.Component {

	render() {
		let start_date = new Date(this.props.time*1000);
		let start_minutes = "0" + start_date.getMinutes();
		let start_hours = start_date.getHours();
		// Fix the Bug of timepicker
		if (start_hours === 0)
			start_hours = 12;
		else if (start_hours === 12)
			start_hours = 12;

		let start_formattedTime = start_hours + ':' + start_minutes.substr(-2)
		let end_date = new Date((this.props.time + this.props.prediction.totalDuration*60)*1000);
		let end_hours = start_date.getHours();

		// Fix the Bug of timepicker
		if (end_hours === 0)
			end_hours = 12;
		else if (end_hours === 12)
			end_hours = 12;
		let end_minutes = "0" + end_date.getMinutes();
		let end_formattedTime = end_hours + ':' + end_minutes.substr(-2)

		return (
			<div className="show-route">
				<p><i className="fas fa-bus"></i><span className="start"> Bus Line: {this.props.routeid}</span></p>
				<p className="from-to">From <span className="stop-name">{this.props.start}</span></p>
				<p className="from-to">To <span className="stop-name">{this.props.end}</span></p>
				<p className="from-to">Depart At:&nbsp;{start_formattedTime}</p>
				<p className="from-to">Estimated Arrive At: &nbsp;{end_formattedTime}</p>
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
