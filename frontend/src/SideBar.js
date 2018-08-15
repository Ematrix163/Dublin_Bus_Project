import React from 'react';
import ShowRoute from './ShowRoute'
import logo from './image/logo.png'
import SearchBox from './StandaloneSearchBox'
import 'react-datepicker/dist/react-datepicker.css';
import Select from 'react-select';
import * as Datetime from 'react-datetime';
import ShowStationResult from './ShowStationResult'
import DatePicker from 'react-mobile-datepicker'
import PowerGoogle from './image/powered_by_google.png'
import { Link } from 'react-router-dom'

//the side the webpage for user to enter journey details and to show route info
class SideBar extends React.Component {
	constructor(props) {
		super(props);
		this.SMALL_SCREEN_WIDTH = 700;
		this.state = {
			mobileTime: ''
		}
	}


	handleSelect = (val) => {
		this.props.handleSelect(val);
		this.setState({mobileTime: val});
	}

    render() {
        let left_content;
		const stops = [
			{value: "1", label: "1"},
			{value: "102", label: "102"},
			{value: "104", label: "104"},
			{value: "11", label: "11"},
			{value: "111", label: "111"},
			{value: "114", label: "114"},
			{value: "116", label: "116"},
			{value: "118", label: "118"},
			{value: "120", label: "120"},
			{value: "122", label: "122"},
			{value: "123", label: "123"},
			{value: "13", label: "13"},
			{value: "130", label: "130"},
			{value: "14", label: "14"},
			{value: "140", label: "140"},
			{value: "142", label: "142"},
			{value: "145", label: "145"},
			{value: "14C", label: "14C"},
			{value: "15", label: "15"},
			{value: "150", label: "150"},
			{value: "151", label: "151"},
			{value: "15A", label: "15A"},
			{value: "15B", label: "15B"},
			{value: "16", label: "16"},
			{value: "161", label: "161"},
			{value: "16C", label: "16C"},
			{value: "17", label: "17"},
			{value: "17A", label: "17A"},
			{value: "18", label: "18"},
			{value: "184", label: "184"},
			{value: "185", label: "185"},
			{value: "220", label: "220"},
			{value: "236", label: "236"},
			{value: "238", label: "238"},
			{value: "239", label: "239"},
			{value: "25", label: "25"},
			{value: "25A", label: "25A"},
			{value: "25B", label: "25B"},
			{value: "25D", label: "25D"},
			{value: "25X", label: "25X"},
			{value: "26", label: "26"},
			{value: "27", label: "27"},
			{value: "270", label: "270"},
			{value: "27A", label: "27A"},
			{value: "27B", label: "27B"},
			{value: "27X", label: "27X"},
			{value: "29A", label: "29A"},
			{value: "31", label: "31"},
			{value: "31A", label: "31A"},
			{value: "31B", label: "31B"},
			{value: "31D", label: "31D"},
			{value: "32", label: "32"},
			{value: "32X", label: "32X"},
			{value: "33", label: "33"},
			{value: "33A", label: "33A"},
			{value: "33B", label: "33B"},
			{value: "33X", label: "33X"},
			{value: "37", label: "37"},
			{value: "38", label: "38"},
			{value: "38A", label: "38A"},
			{value: "38B", label: "38B"},
			{value: "38D", label: "38D"},
			{value: "39", label: "39"},
			{value: "39A", label: "39A"},
			{value: "4", label: "4"},
			{value: "40", label: "40"},
			{value: "40B", label: "40B"},
			{value: "40D", label: "40D"},
			{value: "41", label: "41"},
			{value: "41A", label: "41A"},
			{value: "41B", label: "41B"},
			{value: "41C", label: "41C"},
			{value: "41X", label: "41X"},
			{value: "42", label: "42"},
			{value: "42D", label: "42D"},
			{value: "43", label: "43"},
			{value: "44", label: "44"},
			{value: "44B", label: "44B"},
			{value: "45A", label: "45A"},
			{value: "46A", label: "46A"},
			{value: "46E", label: "46E"},
			{value: "47", label: "47"},
			{value: "49", label: "49"},
			{value: "51D", label: "51D"},
			{value: "51X", label: "51X"},
			{value: "53", label: "53"},
			{value: "54A", label: "54A"},
			{value: "56A", label: "56A"},
			{value: "59", label: "59"},
			{value: "61", label: "61"},
			{value: "63", label: "63"},
			{value: "65", label: "65"},
			{value: "65B", label: "65B"},
			{value: "66", label: "66"},
			{value: "66A", label: "66A"},
			{value: "66B", label: "66B"},
			{value: "66X", label: "66X"},
			{value: "67", label: "67"},
			{value: "67X", label: "67X"},
			{value: "68", label: "68"},
			{value: "68A", label: "68A"},
			{value: "68X", label: "68X"},
			{value: "69", label: "69"},
			{value: "69X", label: "69X"},
			{value: "7", label: "7"},
			{value: "70", label: "70"},
			{value: "70D", label: "70D"},
			{value: "75", label: "75"},
			{value: "757", label: "757"},
			{value: "76", label: "76"},
			{value: "76A", label: "76A"},
			{value: "77A", label: "77A"},
			{value: "77X", label: "77X"},
			{value: "79", label: "79"},
			{value: "79A", label: "79A"},
			{value: "7A", label: "7A"},
			{value: "7B", label: "7B"},
			{value: "7D", label: "7D"},
			{value: "83", label: "83"},
			{value: "83A", label: "83A"},
			{value: "84", label: "84"},
			{value: "84A", label: "84A"},
			{value: "84X", label: "84X"},
			{value: "9", label: "9"}
		];
		const monthMap = {
		    '01': 'Jan',
		    '02': 'Feb',
		    '03': 'Mar',
		    '04': 'Apr',
		    '05': 'May',
		    '06': 'Jun',
		    '07': 'Jul',
		    '08': 'Aug',
		    '09': 'Sep',
		    '10': 'Oct',
		    '11': 'Nov',
		    '12': 'Dec',
		};

        switch (this.props.view) {
            case 'route':
                left_content = <div className="sidebar">
					{this.props.windowwidth <= this.SMALL_SCREEN_WIDTH?
						<i className="siderbar-toggle fas fa-angle-double-left" onClick={this.props.toggleSideBar}></i>
						: null
					}
                    <div className="logo">
                        <img src={logo} alt="logo" onClick={() => window.location.href='/'}/>
                    </div>

                    <div className="view">
                        <button
							className={this.props.view === "route"? "button-view-activate" : "button-view"}
							onClick={this.props.switchView.bind(this, 'route')}>
							By Bus Line
						</button>
						<button
							className={this.props.view === "station"? "button-view-activate" : "button-view"}
							onClick={this.props.switchView.bind(this, 'station')}>
							By Location
						</button>

                    </div>
                    <div className="sidebar-container">
                        <div className="input-container">
                            <Select
								className="selectbox"
								name="form-field-name"
								placeholder="Please Select a Bus Line"
								value={this.props.selectedOption}
								options={stops}
								onChange={this.props.routeChange}
								isSearchable={this.props.windowwidth > this.SMALL_SCREEN_WIDTH ? true: false}
							/>
                            <Select
								className="selectbox"
								name="form-field-name"
								placeholder="Please Choose a Direction"
								value={this.props.direction}
								options={this.props.allDirections}
								onChange={this.props.dirChange}
								isSearchable={this.props.windowwidth > this.SMALL_SCREEN_WIDTH ? true: false}
							/>
                            <Select
								className="selectbox"
								name="form-field-name"
								placeholder="Start Stop"
								value={this.props.startStop}
								options={this.props.startOption}
								onChange={this.props.startChange}
								isSearchable={this.props.windowwidth > this.SMALL_SCREEN_WIDTH ? true: false}
							/>
                            <Select
								className="selectbox"
								name="form-field-name"
								placeholder="Destination Stop"
								value={this.props.endStop}
								options={this.props.endOption}
								onChange={this.props.endChange}
								isSearchable={this.props.windowwidth > this.SMALL_SCREEN_WIDTH ? true: false}
							/>
							{this.props.windowwidth <= this.SMALL_SCREEN_WIDTH?
								<div className="time-select-container">
								 	<input className="time-select" value={this.state.mobileTime} disabled/>
									<i className="icon fas fa-calendar-alt" onClick={this.props.openTimePicker}></i>
									<DatePicker
										isOpen={this.props.isOpen}
										dateFormat={['YYYY', ['MM', (month) => monthMap[month]], 'DD','hh', 'mm']}
										confirmText='Confrim'
										cancelText="Cancel"
										showFormat="YYYY/MM/DD/hh:mm"
										onSelect={this.handleSelect}
                    					onCancel={this.props.handleCancel}
									/>
								</div>
								:
								<Datetime
									className="timepicker"
									onChange={this.props.timeOnchange}
									inputProps={{placeholder: 'Choose The Time'}}
								/>
							}
							<button
								type="button"
								className="route-button btn btn-info btn-lg btn-block"
								onClick={this.props.handlesave}
							   >Save My Journey
							 </button>
							<button
								type="button"
								className="route-button btn btn-primary btn-lg btn-block"
								onClick={this.props.routeSubmit}>Search
							 </button>
                        </div>
                    </div>
					<Link to='/term'><span className="term">Terms</span></Link>
                </div>;
                break;

            case 'station':
                left_content = <div className="sidebar">
					{this.props.windowwidth <= this.SMALL_SCREEN_WIDTH?
						<i className="siderbar-toggle fas fa-angle-double-left" onClick={this.props.toggleSideBar}></i>
						: null
					}
                    <div className="logo">
                        <img src={logo} alt="logo" onClick={() => window.location.href='/'}/>
                    </div>
                    <div className="view">
						<button className="button-view" onClick={this.props.switchView.bind(this, 'route')}>By Bus Line</button>
						<button className="button-view-activate" onClick={this.props.switchView.bind(this, 'station')}>By Location</button>
                    </div>
                    <div className="sidebar-container">
                        <div className="form">
                            <SearchBox
								 locChange={this.props.startLocChange}
								 text='Please Enter Your Departure Place'
								 type='origin'
								 switchUserLoc={this.props.switchUserLoc}
							/>
                            <SearchBox
								locChange={this.props.destLocChange}
								text='Please Enter Your Destination'
								type='dest'
							/>
							{this.props.windowwidth <= this.SMALL_SCREEN_WIDTH?
								<div className="time-select-container-station">
								 	<input className="time-select" value={this.state.mobileTime} disabled/>
									<i className="icon fas fa-calendar-alt" onClick={this.props.openTimePicker}></i>
									<DatePicker
										isOpen={this.props.isOpen}
										dateFormat={['YYYY', ['MM', (month) => monthMap[month]], 'DD','hh', 'mm']}
										confirmText='Confrim'
										cancelText="Cancel"
										showFormat="YYYY/MM/DD/hh:mm"
										onSelect={this.handleSelect}
                    					onCancel={this.props.handleCancel}
									/>
								</div>
								:
								<Datetime
									className="timepicker-station"
									onChange={this.props.timeOnchange}
									inputProps={{placeholder: 'Choose The Time'}}
								/>
							}
                            <br/>
                            <button className="btn btn-block btn-primary" onClick={this.props.stationSubmit}>Submit</button>
                        </div>
                    </div>
					<div className="blank"></div>
					<img src={PowerGoogle} className="google-logo" alt=""/>
					<Link to='/term'><span className="term">Terms</span></Link>
                </div>
                break;

            case 'result':
                left_content = <div className="sidebar">
					<div className="route-result">
						<i className="fas fa-arrow-left" onClick={this.props.switchView.bind(this,'route')}></i>
						{this.props.windowwidth <= this.SMALL_SCREEN_WIDTH?
							<i className="toggle-head fas fa-angle-double-left" onClick={this.props.toggleSideBar}></i>
							: null
						}
					</div>
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
				break;

			case 'station_result':
				left_content =
					<div className="sidebar">
						{this.props.windowwidth <= this.SMALL_SCREEN_WIDTH?
							<i className="toggle-head fas fa-angle-double-left" onClick={this.props.toggleSideBar}></i>
							: null
						}
						<div className="route-result"><i className="fas fa-arrow-left" onClick={this.props.switchView.bind(this,'station')}></i></div>
						<div className="sidebar-container">
							<ShowStationResult
								startName={this.props.startName}
								endName={this.props.endName}
								data={this.props.prediction}
								time={this.props.time}
							/>
						</div>
					</div>
				break;

        }
        return (<div>{left_content}</div>)
    }
}

export default SideBar;
