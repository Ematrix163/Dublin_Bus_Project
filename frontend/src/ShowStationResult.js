import React from 'react';

import Up from './image/up.png'
import Down from './image/down.png'


class ShowStationResult extends React.Component {
	state = {
		show: {},
		seq: {}
	}

	componentWillMount() {
		let temp = {};
		let num;
		if (this.props.data.google) {
			num = this.props.data.google.routes[0].legs[0].steps.length;
		}
		let count = 0;
		for (let i = 0; i < num; i++) {
			temp[i] = false;
			if (this.props.data.google.routes[0].legs[0].steps[i].travel_mode === 'TRANSIT') {
				let tempSeq = this.state.seq;
				tempSeq[i] = count;
				this.setState({seq: tempSeq});
				count ++;
			}
		}
		this.setState({show: temp});
	}

	// When user toggle the detail information
	toggle = (index)=>{
		let temp = this.state.show;
		temp[index] = !temp[index];
		this.setState({show: temp});
	}

	render() {
		const temp = this.props.data.google ? this.props.data.google.routes[0].legs[0].steps : [];

		return (
			<div className="station-result">
				{temp.map((step, index) => (
					<div key={index}>
						{step.travel_mode === 'WALKING'?
							<div>
							<div className="walk">
								<i className="fas fa-walking"></i>&nbsp;{step.html_instructions}
								<br/>
								<i className="far fa-clock"></i>
								<span className="time"> {step.duration.text}</span>
								<span className="detail" onClick={()=>this.toggle(index)}>Deatils<img className="bracket" alt="" src={this.state.show[index]? Up: Down}/></span>
									{this.state.show[index]?
										<ul className="inf-detail-walk">
											{step.steps.map((detail, index1)=> (
												<li key={index1} dangerouslySetInnerHTML={{__html:detail.html_instructions}}></li>
											))}
										</ul>
										: null}
							</div>
							<hr/>
							</div>
						:
							<div>
								<div className="bus">
									<i className="fas fa-bus"></i><span className="start"> Bus: {step.transit_details.line.short_name}&nbsp;</span><span className='dest-name'>{step.html_instructions}</span>
									<span className="stops-num">{this.props.data.data[this.state.seq[index]].stopsNum} stops</span>
									<br/>
									<i className="far fa-clock"></i>{this.props.data.data[this.state.seq[index]].totalDuration} mins<span className="detail" onClick={()=>this.toggle(index)}>Deatils
										<img className="bracket" alt=""  src={this.state.show[index]? Up: Down}/></span>
									{this.state.show[index]?
										<ul className="inf-detail-bus">
											{this.props.data.data[this.state.seq[index]].stopInfo.map(stop => (
												<li key={stop["stop_id"]}>· {stop.stop_name}</li>
											))}
										</ul>
									: null}
								</div>
								<hr/>
							</div>
					}
					</div>
				))}
			</div>
		)
	}
}

export default ShowStationResult
