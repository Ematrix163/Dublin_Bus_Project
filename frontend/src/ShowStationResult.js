import React from 'react';

// <div>
// 	<i class="fas fa-walking"></i>Walk to Dublin (UCD Stillorgan Rd Flyover) 5 mins
// 		<ul>
// 			<li>Head <b>northeast</b> 0.1 km </li>
// 			<li>Turn <b>right</b></li>
// 			<li>Turn <b>left</b></li>
// 			<li>Turn <b>right</b></li>
// 		</ul>
// </div>
// <div>
// 	<i class="fas fa-bus"></i>Bus towards Phoenix Pk
// </div>

class ShowStationResult extends React.Component {
	render() {
		const temp = this.props.google ? this.props.google.routes[0].legs[0].steps : [];
		let mode;
		return (
			<div className="station-result">
				{temp.map(step => (
					<div>
						{step.travel_mode === 'WALKING' ? <i className="fas fa-walking"></i>: <i className="fas fa-bus"></i>}{step.html_instructions}
						<ul>
							{step.travel_mode === 'WALKING' ? step.steps.map(detail => (<li>{detail.html_instructions}</li>))
								: null}
						</ul>
					</div>
				))}
			</div>
		)
	}
}

export default ShowStationResult
