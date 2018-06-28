import {StandaloneSearchBox} from "react-google-maps"
import React, {Component} from 'react';

import SelectBox from './SelectBox'
import * as API from './API'
import logo from './image/logo.jpg'

// import { Route, Link } from 'react-router-dom'

class SideBar extends React.Component {

    state = {
        view: 'route',
        route: []
    }

    componentDidMount() {}

	switchView = (value) => {
		this.setState({view: value})
	}

    render() {
        return (<div className="sidebar">
            <div className="sidebar-container">
                <div className="logo">
                    <img src={logo}/>
                </div>
                <div className="view">
                    <button className="button-view" onClick={this.switchView.bind(this, 'route')}>Route View</button>
                    <button className="button-view" onClick={this.switchView.bind(this, 'station')}>Station View</button>
                </div>
                {
                    this.state.view == 'route'
                        ? <div className="input-container">
                                <SelectBox route={this.state.route}/>
                                <SelectBox/>
                                <SelectBox/>
                                <button type="button" className="btn btn-primary">Primary</button>
                            </div>
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
                                    <div className="form-group">
                                        <label htmlFor="date">Date and Time:</label>
                                        <input type="text" className="form-control" id="date"/>
                                    </div>
                                    <button type="submit" className="btn btn-block btn-primary">Submit</button>
                                </form>
                            </div>
                }

            </div>
            <div className="route"></div>
        </div>)
    }
}

export default SideBar;
