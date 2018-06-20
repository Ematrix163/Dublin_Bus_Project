import React, { Component } from 'react';
import './App.css';
import logo from './image/logo.jpg'




class SideBar extends React.Component {

	render() {
		return (
			<div className="sidebar">
				<div className="sidebar-container">
					<div className="logo">
						<img src={logo}/>
					</div>
					<div className="form">
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
		                            <input type="text" className="form-control"  id="date" />
		                        </div>
		                        <button type="submit" className="btn btn-block btn-primary">Submit</button>
		                    </form>
					</div>
				</div>
				<div className="route"></div>
			</div>
		)
	}
}


export default SideBar;
