import React from 'react';
import ShowRoute from './ShowRoute'
import logo from './image/logo.jpg'
import SearchBox from './StandaloneSearchBox'
import moment from 'moment';
import 'react-datepicker/dist/react-datepicker.css';
import Select from 'react-select';
import 'react-select/dist/react-select.css';
import * as Datetime from 'react-datetime';

//the side the webpage for user to enter journey details and to show route info

class SideBar extends React.Component {

    render() {
        let left_content;
        switch (this.props.view) {
            case 'route':
                left_content = <div className="sidebar">
                    <div className="logo">
                        <img src={logo}/>
                    </div>
                    <div className="view">
                        <button className="button-view" onClick={this.props.switchView.bind(this, 'route')}>Route View</button>
                        <button className="button-view-activate" onClick={this.props.switchView.bind(this, 'station')}>Station View</button>
                    </div>
                    <div className="sidebar-container">
                        <div className="input-container">
                            <Select className="selectbox" name="form-field-name" placeholder="Please Select a bus line" value={this.props.selectedOption} options={this.props.routes} onChange={this.props.routeChange}/>
                            <Select className="selectbox" name="form-field-name" placeholder="Please Choose A Direction" value={this.props.direction} options={this.props.allDirections} onChange={this.props.dirChange}/>
                            <Select className="selectbox" name="form-field-name" placeholder="Start Stop" value={this.props.startStop} options={this.props.station} onChange={this.props.startChange}/>
                            <Select className="selectbox" name="form-field-name" placeholder="Destination stop" value={this.props.endStop} options={this.props.station} onChange={this.props.endChange}/>
							<Datetime className="timepicker" onChange={this.props.timeOnchange} inputProps={{placeholder: '                        Choose The Time'}}/>
							<button type="button" className="route-button btn btn-primary btn-lg btn-block" onClick={this.props.routeSubmit}>Search</button>
                        </div>
                    </div>
                </div>;
                break;

            case 'station':
                left_content = <div className="sidebar">
                    <div className="logo">
                        <img src={logo}/>
                    </div>
                    <div className="view">
                        <button className="button-view" onClick={this.props.switchView.bind(this, 'route')}>Route View</button>
                        <button className="button-view-activate" onClick={this.props.switchView.bind(this, 'station')}>Station View</button>
                    </div>
                    <div className="sidebar-container">
                        <div className="form">
                            <SearchBox locChange={this.props.startLocChange} text='Please enter your location'/>
                            <SearchBox locChange={this.props.destLocChange} text='Please enter your destination'/>
                            <div><Datetime inputProps={{placeholder: 'Choose The Time'}}/></div>
                            <br/>
                            <button className="btn btn-block btn-primary" onClick={this.props.findRoute}>Submit</button>
                        </div>
                    </div>
                </div>;
                break;

            case 'result':
                left_content = <div className="sidebar">
					<div className="route-result"><i className="fas fa-arrow-left" onClick={this.props.switchView.bind(this,'route')}></i></div>
                    <div className="sidebar-container">
                        <ShowRoute
							prediction={this.props.prediction}
							start={this.props.startStop.label}
							end={this.props.endStop.label}
							routeid={this.props.selectedOption.label}
							handleOver={this.props.handleOver}
							handleOut={this.props.handleOut}
							time={this.props.time}/>
                    </div>
                </div>
                break;

			case 'loading':
				left_content =
							<div className="sidebar">
								<div className="cssload-thecube">
									<div className="cssload-cube cssload-c1"></div>
									<div className="cssload-cube cssload-c2"></div>
									<div className="cssload-cube cssload-c4"></div>
									<div className="cssload-cube cssload-c3"></div>
								</div>
							</div>

        }

        return (<div>{left_content}</div>)
    }
}

export default SideBar;
