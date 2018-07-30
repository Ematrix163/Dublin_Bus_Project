import React from 'react';
import SideBar from './SideBar'
import Login from './Login'
import Map from './Map'
import './css/App.css';
import * as WebAPI from './WebAPI'
import moment from 'moment';

import SweetAlert from 'sweetalert2-react';
import { Link, Route } from 'react-router-dom'


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
		blink: '',
		prediction: {"stopInfo":[]},
		allDirections: [],
		direction: '',
		show: false,
		start_loc: '',
		dest_loc: '',
		alert: '',
		submitFlag: false
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
			this.setState({selectedOption:val, start_stop:'', end_stop:'', direction:''})
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
					data.map(each => {temp.push({value:each.true_stop_id, label:each.stop_name, lat:each.stop_lat, lng: each.stop_long, name: each.stop_name})});
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
    switchView = (value) => {
		this.setState({view: value, station:[]});
		//Clear the markers when user switch to another view
		if (value === 'station')
			this.setState({prediction:{"stopInfo":[]}});
	}
	// In route View, when user click submit button
	routeSubmit = () => {
		// Check all these fields are not blank
		if (this.state.selectedOption && this.state.start_stop && this.state.end_stop && this.state.time) {
			this.setState({view:'loading'});
			// Call the api to predict the time
			WebAPI.getTime(this.state.selectedOption.value, this.state.start_stop.value, this.state.end_stop.value, this.state.time, this.state.direction.value).then(r => {
				if (r.status === 'success') {
					this.setState({prediction: r.data, showroute:true, view:'result'});
				} else {
					this.setState({view:'route', show:'false', alert:'Sorry, the bus is not in service at that time!'})
				}
			});
		} else {
			this.setState({show:true, alert:'Please fill out the form!'})
		}
	}

	startLocChange = (places) => {
		this.setState({start_loc: places[0].geometry.location})
	}

	destLocChange = (places) => {
		this.setState({dest_loc: places[0].geometry.location})
	}

	handleOver = (id) => {
		this.setState({blink:id});
	}

	handleOut = () => {
		this.setState({blink:''});
	}

	stationSubmit = () => {
		this.setState({submitFlag:true});
		const start_loc = this.state.start_loc.lat();
		const start_lng = this.state.start_loc.lng();
		const end_loc = this.state.dest_loc.lat();
		const end_lng = this.state.dest_loc.lng();
		WebAPI.getGoogleDirection(start_loc, start_lng, end_loc, end_lng, 1532979801)
			.then(r => {
				this.setState({prediction: r.data});
			})
	}

	render() {
		return (
		<div>
			<Route exact path="/" render={() => (
				<div className="base-container">
					<SideBar
						search={this.state.search}
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
						startLocChange={this.startLocChange}
						destLocChange={this.destLocChange}
						handleOut={this.handleOut}
						handleOver={this.handleOver}
						stationSubmit={this.stationSubmit}
						/>

						<SweetAlert
							show={this.state.show}
							type='error'
							title= 'Oops!'
							text={this.state.alert}
							onConfirm={() => this.setState({ show: false })}
						/>
						<div className="main">
						<div className="header">
							<ul className="navigator">
								<Link to='/login'><li>Sign In</li></Link>
								<Link to='/'><li>About Us</li></Link>
							</ul>
						</div>
						<div id="map">
							<Map
								stops={this.state.prediction.stopInfo}
								station={this.state.station}
								startLoc={this.state.start_loc}
								destLoc={this.state.dest_loc}
								view={this.state.view}
								blink={this.state.blink}
								submitFlag={this.state.submitFlag}
								/>
						</div>
						</div>
					</div>
				)}/>

			<Route exact path="/login" render={() => (
					<Login/>
				)}/>
			</div>
		)
	}
}


export default App
