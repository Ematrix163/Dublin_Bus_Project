import React from 'react';

import Up from './image/up.png'
import Down from './image/down.png'

// function to show the user the route between stations with in between stations shown also
class ShowRoute extends React.Component {

	state = {
		show: false
	}

	toggle = () => {

		this.setState({
			show: !this.state.show,
		})
	}

	render() {

		const start_formattedTime = this.props.prediction.data[0].bustime[1]
		const end = Math.floor((this.props.prediction.data[0].bustime[0])) + this.props.prediction.data[0].totalDuration * 60;
		const end_hour = Math.floor(end / 3600)
		const end_min = ('00' + Math.floor((end - end_hour * 3600) / 60)).substr(-2)
		const end_formattedTime = end_hour + ':' + end_min + ':00'

		return (
			<div className="show-route">
				{this.props.prediction.data[0].flag? null:<div className="alert alert-danger" role="alert">Sorry, there is no serving bus after your picked datetime!</div>}
				<p><i className="fas fa-bus"></i><span className="start"> Bus Line: {this.props.routeid}</span></p>
				<p className="from-to">From <span className="stop-name">{this.props.start}</span></p>
				<p className="from-to">To <span className="stop-name">{this.props.end}</span></p>
				<p className="from-to">Bus Will Arrive At:&nbsp;{start_formattedTime}</p>
				<p className="from-to">Estimated Arrival Time: &nbsp;{end_formattedTime}</p>
				<p className="from-to">
					<i className="far fa-clock"></i> &nbsp; Duration:&nbsp;
						<span className="start">{this.props.prediction.data[0].totalDuration}</span> miniutes
						<span
							className="detail"
							onClick={()=>this.toggle()}>Deatils
							<img className="bracket" alt="" src={this.state.show? Up: Down}/>
						</span>
				</p>


				<hr/>
				{this.state.show?
					<div>
						<p className="from-to"><span className="stops-num">{this.props.prediction.data[0].stopsNum} Stops</span></p>
						<ul className='route-ul'>
							{this.props.prediction.data[0].stopInfo.map(each => (
								<li
									key={each.stop_id}
									className="stop-detail"
									onMouseOver={this.props.handleOver.bind(this, each.stop_id)}
									onMouseOut={this.props.handleOut}>· {each.stop_name}</li>
							))}
						</ul>
					</div>
					:
					null
				}

			</div>
		)
	}
}

export default ShowRoute
