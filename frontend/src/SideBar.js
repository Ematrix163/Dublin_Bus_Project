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


    render() {
        return (<div className="sidebar">
            <div className="logo">
                <img src={logo}/>
            </div>
            {/*function to allow user to switch between route and station view*/}
            <div className="view">
                <button className={this.props.view === "route"? "button-view": "button-view-activate"}
					onClick={this.props.switchView.bind(this, 'route')}>Route View</button>
				<button className={this.props.view === "route"? "button-view-activate": "button-view"}
					onClick={this.props.switchView.bind(this, 'station')}>Station View</button>
            </div>
            {/*container for user to input journey details depending on route/station view*/}
            <div className="sidebar-container">
                {
                    //Route view elements
                    //1.User selects route, 2. User selects departure stop, 3. User selects arrival stop
                    this.props.view === 'route'
                        ? <div className="input-container">
						  	<Select
								className="selectbox"
								name="form-field-name"
								placeholder="Please Select a bus line"
								value={this.props.selectedOption}
								options={this.props.routes}
								onChange={this.props.routeChange}/>

							<Select
								className="selectbox"
								name="form-field-name"
								placeholder="Please Choose A Direction"
								value={this.props.direction}
								options={this.props.allDirections}
								onChange={this.props.dirChange}/>

							<Select
								className="selectbox"
								name="form-field-name"
								placeholder="Start Stop"
  								value={this.props.startStop}
								options={this.props.station}
								onChange={this.props.startChange}/>

							<Select
								className="selectbox"
								name="form-field-name"
								placeholder="Destination stop"
								value={this.props.endStop}
								options={this.props.station}
								onChange={this.props.endChange}/>

							<div><Datetime className="timepicker" onChange={this.props.timeOnchange} inputProps={{ placeholder: 'Choose The Time' }}/></div>
                            <button type="button" className="route-button btn btn-primary btn-lg btn-block" onClick={this.props.routeSubmit}>Search</button>
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
                    this.props.showroute
                        ? <ShowRoute
							prediction={this.props.prediction}
							start={this.props.startStop.label}
							end={this.props.endStop.label}
							routeid={this.props.selectedOption.label}/>
                        : ''
                }
            </div>

        </div>)
    }
}


export default SideBar;
