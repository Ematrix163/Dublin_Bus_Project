import React, { Component } from 'react';

import SideBar from './SideBar'
import Map from './Map'
import './App.css';

class App extends React.Component {
	render() {
		return (
			<div className="base-container">
				<SideBar/>
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
