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
        view: 'station',
        showroute: true,
        routes: [],
		station: [],
		selectedOption: '',
		start_stop: '',
		end_stop: '',
    }

    componentDidMount() {
		let temp = [];
		WebAPI.getAllRoute().then(r => r.map((each) => {
			temp.push({value:each, label:each})
		}))
		this.setState({routes: temp})
	}

	routeChange = (val) => {
		let temp = [];
		this.setState({selectedOption:val})
		WebAPI.getStation(val).then(s => {
			s.map(each => {temp.push({value:each.name, label:each.name})});
			this.setState({station: temp});
			console.log(temp);
		})
	}

	startChange = (val) => {
		this.setState({start_stop:val})
	}

	endChange = (val) => {
		this.setState({end_stop: val})
	}

    switchView = (value) => {
        this.setState({view: value})
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
							<Select className="selectbox" name="form-field-name" placeholder="Sstart Stop"
  								value={this.state.start_stop} options={this.state.station} onChange={this.startChange}/>
							<Select className="selectbox" name="form-field-name" placeholder="Destination stop"
								value={this.state.end_stop} options={this.state.station} onChange={this.endChange}/>
                            <button type="button" className="btn btn-primary btn-blocky">Search</button>
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
                        ? <ShowRoute/>
                        : ''
                }
            </div>

        </div>)
    }
}


export default SideBar;
