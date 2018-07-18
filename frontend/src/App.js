import React, { Component } from 'react';

import SideBar from './SideBar'
import Map from './Map'
import './css/App.css';

import * as WebAPI from './WebAPI'

import moment from 'moment';

class App extends React.Component {

	state = {
        view: 'route',
        showroute: false,
        routes: [],
		station: [],
		selectedOption: '',
		start_stop: '',
		end_stop: '',
		time: '',
		prediction: {},
		allDirections: [],
		direction: ''
    }


    componentDidMount() {
		let temp = [];
		WebAPI.getAllRoute().then(r => r.map((each) => {
			temp.push({value:each.routes, label:each.routes})
		}))
		this.setState({routes: temp})
	}

	// When user Choose different route, the directions should be updated
	routeChange = (val) => {
		if (val) {
			this.setState({selectedOption:val})
			WebAPI.getDirection(val.value).then(r => {
				this.setState({allDirections: [{label: r.dir1, value: 1},{label: r.dir2, value: 2}]});
			})
		}
	}


	//When user choose different directions, will show all related stops
	dirChange = (val) => {
		if (val) {
			this.setState({direction:val})
			let temp = [];
			WebAPI.getStation(this.state.selectedOption.value, val.value).then(s => {
				if (s['status'] === "success") {
					let data = s.data;
					data.map(each => {temp.push({value:each.true_stop_id, label:each.stop_name})});
					this.setState({station: temp});
				}

			})
		}
	}


	// If time change, modify the time state
	timeOnchange = (val) => {
		let time = val.format();
		let unixtime = moment(new Date(time)).format('x')/1000;
		this.setState({time: unixtime});
	}

	// If the start stop change
	startChange = (val,a) => this.setState({start_stop:val})

	// If the end stop change
	endChange = (val) => this.setState({end_stop: val})

	// When user choose another view
    switchView = (value) => this.setState({view: value})

	// In route View, when user click submit button
	routeSubmit = () => {
		// Check all these fields are not blank
		if (this.state.selectedOption && this.state.start_stop && this.state.end_stop && this.state.time) {
			// Call the api to predict the time
			WebAPI.getTime(this.state.selectedOption.value, this.state.start_stop.value, this.state.end_stop.value, this.state.time, this.state.direction.value).then(r => {
				if (r.status === 'success') {
					console.log(1111);
					this.setState({prediction: r.data, showroute:true});
				} else {
					console.log('fail!');
				}
			});
		} else {
			console.log('error');
		}
	}


	render() {
		return (
			<div className="base-container">
				<SideBar
					view={this.state.view}
					showroute={this.state.showroute}
					routes={this.state.routes}
					station={this.state.station}
					selectedOption={this.state.selectedOption}
					startStop={this.state.start_stop}
					endStop={this.state.end_stop}
					time={this.state.time}
					prediction={this.state.prediction}
					allDirections={this.state.allDirections}
					direction={this.state.direction}
					routeChange={this.routeChange}
					startChange={this.startChange}
					endChange={this.endChange}
					switchView={this.switchView}
					dirChange={this.dirChange}
					routeSubmit={this.routeSubmit}
					timeOnchange={this.timeOnchange}
					/>


				<div className="main">
					<div id="map">
						<Map/>
					</div>
				</div>
			</div>
		)
	}
}


export default App
