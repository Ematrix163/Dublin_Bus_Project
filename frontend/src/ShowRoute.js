import React from 'react';

// function to show the user the route between stations with in between stations shown also
class ShowRoute extends React.Component {

	render() {

		const start_formattedTime = this.props.prediction.bustime[1]
		const end = parseInt((this.props.prediction.bustime[0])) + this.props.prediction.totalDuration * 60;
		const end_hour = parseInt(end / 3600)
		const end_min = ('00' + parseInt((end - end_hour * 3600) / 60)).substr(-2)
		const end_formattedTime = end_hour + ':' + end_min + ':00'


		return (
			<div className="show-route">
				<p><i className="fas fa-bus"></i><span className="start"> Bus Line: {this.props.routeid}</span></p>
				<p className="from-to">From <span className="stop-name">{this.props.start}</span></p>
				<p className="from-to">To <span className="stop-name">{this.props.end}</span></p>
				<p className="from-to">Bus Arrive At:&nbsp;{start_formattedTime}</p>
				<p className="from-to">Estimated Arrive At: &nbsp;{end_formattedTime}</p>
				<p className="from-to"><i className="far fa-clock"></i> &nbsp; Duration: {this.props.prediction.totalDuration} miniutes</p>
				<hr/>
				<p className="from-to"><span className="stops-num">{this.props.prediction.stopsNum} Stops</span></p>
				<ul>
					{this.props.prediction.stopInfo.map(each => (
						<p
							key={each.stop_id}
							className="stop-detail"
							onMouseOver={this.props.handleOver.bind(this, each.stop_id)}
							onMouseOut={this.props.handleOut}>· {each.stop_name}</p>
					))}
				</ul>
			</div>
		)
	}
}

export default ShowRoute
