import React from 'react';
import ShowRoute from './ShowRoute'
import * as WebAPI from './WebAPI'
import logo from './image/logo.jpg'

import SearchBox from './StandaloneSearchBox'
import DatePicker from 'react-datepicker';
import moment from 'moment';
import 'react-datepicker/dist/react-datepicker.css';

import Select from 'react-select';
import 'react-select/dist/react-select.css';

import * as Datetime from 'react-datetime';
//the side the webpage for user to enter journey details and to show route info

class SideBar extends React.Component {
    state = {
        view: 'route',
        showroute: false,
        routes: [],
		station: [],
		selectedOption: '',
		start_stop: '',
		end_stop: '',
		time: '',
		prediction: {}
    }
    componentDidMount() {
		let temp = [];
		WebAPI.getAllRoute().then(r => r.map((each) => {
			temp.push({value:each.routes, label:each.routes})
		}))
		this.setState({routes: temp})
	}
	// When user Choose different route, the stop should be updated
	routeChange = (val) => {
		if (val) {
			let temp = [];
			this.setState({selectedOption:val})
			WebAPI.getStation(val).then(s => {
					s.map(each => {temp.push({value:each.stop_name, label:each.stop_name, id: each.true_stop_id})});
					this.setState({station: temp});
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
			WebAPI.getTime(this.state.selectedOption.value, this.state.start_stop.id,this.state.end_stop.id, this.state.time).then(r => {
				console.log(r);
				if (r.status = 'success') {
					this.setState({showroute:true, prediction: r.data});
				} else {
					console.log('fail!');
				}
			});
		} else {
			console.log('error');
		}
	}

    render() {
        return (<div className="sidebar">
            <div className="logo">
                <img src={logo}/>
            </div>
            {/*function to allow user to switch between route and station view*/}
            <div className="view">
                <button className={this.state.view === "route"? "button-view": "button-view-activate"}
					onClick={this.switchView.bind(this, 'route')}>Route View</button>
                <button className={this.state.view === "route"? "button-view-activate": "button-view"}
					onClick={this.switchView.bind(this, 'station')}>Station View</button>
            </div>
            {/*container for user to input journey details depending on route/station view*/}
            <div className="sidebar-container">
                {
                    //Route view elements
                    //1.User selects route, 2. User selects departure stop, 3. User selects arrival stop
                    this.state.view === 'route'
                        ? <div className="input-container">
						  	<Select className="selectbox" name="form-field-name" placeholder="Please Select a bus line"
								value={this.state.selectedOption} options={this.state.routes} onChange={this.routeChange}/>
							<Select className="selectbox" name="form-field-name" placeholder="Start Stop"
  								value={this.state.start_stop} options={this.state.station} onChange={this.startChange}/>
							<Select className="selectbox" name="form-field-name" placeholder="Destination stop"
								value={this.state.end_stop} options={this.state.station} onChange={this.endChange}/>
							<div><Datetime onChange={this.timeOnchange} inputProps={{ placeholder: 'Choose The Time' }}/></div>
                            <button type="button" className="btn btn-primary btn-blocky" onClick={this.routeSubmit}>Search</button>

                          </div>
                        //station view elements
                        // user chooses departure and arrival stop
                        : <div className="form">
                                <form>
                                    <SearchBox text='Please enter your location'/>
                                    <SearchBox text='Please enter your destination'/>
                                    {/*Calender for user to choose date*/}
									<div><Datetime inputProps={{ placeholder: 'Choose The Time' }}/></div>
									<br/>
                                    <button type="submit" className="btn btn-block btn-primary">Submit</button>
                                </form>
                            </div>
                }
                {
                    //calls function show route to show the route details
                    this.state.showroute
                        ? <ShowRoute
							prediction={this.state.prediction}
							start={this.state.start_stop.label}
							end={this.state.end_stop.label}
							routeid={this.state.selectedOption.label}/>
                        : ''
                }
            </div>

        </div>)
    }
}


export default SideBar;
