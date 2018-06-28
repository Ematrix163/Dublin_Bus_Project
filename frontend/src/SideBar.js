import React, {Component} from 'react';
import SelectBox from './SelectBox'
import ShowRoute from './ShowRoute'
import * as API from './API'
import logo from './image/logo.jpg'


import DatePicker from 'react-datepicker';
import moment from 'moment';
import 'react-datepicker/dist/react-datepicker.css';


//the side the webpage for user to enter journey details and to show route info

class SideBar extends React.Component {

    state = {
        view: 'route',
        showroute: true,
        route: []
    }

    componentDidMount() {}

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
                <button className={this.state.view === "route"
                        ? "button-view"
                        : "button-view-activate"} onClick={this.switchView.bind(this, 'route')}>Route View</button>
                <button className={this.state.view === "route"
                        ? "button-view-activate"
                        : "button-view"} onClick={this.switchView.bind(this, 'station')}>Station View</button>
            </div>
            {/*container for user to input journey details depending on route/station view*/}
            <div className="sidebar-container">

                {
                    //Route view elements
                    //1.User selects route, 2. User selects departure stop, 3. User selects arrival stop

                    this.state.view === 'route'
                        ? <div className="input-container">
                                <SelectBox route={this.state.route}/>
                                <SelectBox/>
                                <SelectBox/>
                                <button type="button" className="btn btn-primary btn-blocky">Search</button>
                            </div>
                        //station view elements
                        // user chooses departure and arrival stop
                        : <div className="form">
                                <form>
                                    <div className="form-group">
                                        <label htmlFor="departure">Departing From:</label>
                                        <input type="text" className="form-control" id="departure" aria-describedby="emailHelp" placeholder="Departing From"/>
                                        <small id="emailHelp" className="form-text text-muted">Please enter your location.</small>
                                    </div>
                                    <div className="form-group">
                                        <label htmlFor="destination">Destination:</label>
                                        <input type="texts" className="form-control" id="destination" placeholder="Destination"/>
                                    </div>
                                    {/*Calender for user to choose date*/}
									<div><DatePicker /><i class="fas fa-table"></i></div>
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




// class to create calender for user to select the date of travel
class Example extends React.Component {
  constructor (props) {
    super(props)
    this.state = {
      startDate: moment()
    };
    this.handleChange = this.handleChange.bind(this);
  }

  handleChange(date) {
    this.setState({
      startDate: date
    });
  }

  render() {
    return <DatePicker
        selected={this.state.startDate}
        onChange={this.handleChange}
    />;
  }
}






export default SideBar;
