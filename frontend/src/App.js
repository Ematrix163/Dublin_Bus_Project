import React from 'react';
import SideBar from './SideBar'
import Login from './Login'
import Map from './Map'
import './css/App.css';
import * as WebAPI from './WebAPI'
import moment from 'moment';
import TwitterDisplay from './TwitterDisplay';
import SweetAlert from 'sweetalert2-react';
import { Link, Route } from 'react-router-dom'
import Term from './Term'
import APIDoc from './APIDoc'
import SignUp from './SignUp'
import MyFav from './MyFav'
import * as Datetime from 'react-datetime';
import DatePicker from 'react-mobile-datepicker'

class App extends React.Component {

    state = {
        view: 'route',
        routes: [],
        station: [],
        selectedOption: '',
        start_stop: '',
        end_stop: '',
        time: '',
        blink: '',
        prediction: {},
        allDirections: [],
        direction: '',
        show: false,
        start_loc: '',
        dest_loc: '',
        alert: {
			type: 'success',
			title: '',
			text: ''
		},
        submitFlag: false,
        spinner: false,
        toggle: false,
        showsidebar: false,
        width: 0,
        height: 0,
        timepickerOpen: false,
        displayed_form: '',
        logged_in: localStorage.getItem('token')
            ? true
            : false,
        username: localStorage.getItem('token')
					? JSON.parse(atob(localStorage.getItem('token').split('.')[1]))['username']
					:'',
		mainView: 'Map',
		showfav: false,
		favdata: '',
		showTimePicker:false,
		infowtimeisOpen: true,
    };

    /* Get the window size */
    constructor(props) {
        super(props);
        this.updateWindowDimensions = this.updateWindowDimensions.bind(this);
    }

    componentWillUnmount() {
        window.removeEventListener('resize', this.updateWindowDimensions);
    }

    updateWindowDimensions() {
        this.setState({width: window.innerWidth, height: window.innerHeight});
    }

    componentDidMount() {
        this.setState({showsidebar: true});
        this.updateWindowDimensions();
        window.addEventListener('resize', this.updateWindowDimensions);
    } // end didMount

    // changes the toggle state from true to false
	toggleClick = () => {
		if (this.state.toggle) {
			this.setState({mainView: 'Map'});
		} else {
			this.setState({mainView: 'Twitter'})
		}
	    this.setState(prevState => ({toggle: !prevState.toggle}))
	  }

    // When user Choose different route, the directions should be updated
    routeChange = (val) => {
        if (val) {
            this.setState({selectedOption: val, start_stop: '', end_stop: '', direction: ''})
            WebAPI.getDirection(val.value).then(r => {
                this.setState({
                    allDirections: [
                        {
                            label: r.dir1,
                            value: 1
                        }, {
                            label: r.dir2,
                            value: 2
                        }
                    ]
                });
            })
        }
    }

    //When user choose different directions, will show all related stops
    dirChange = (val) => {
        if (val) {
            this.setState({direction: val})
            let temp = [];
            WebAPI.getStation(this.state.selectedOption.value, val.value).then(s => {
                if (s['status'] === "success") {
                    let data = s.data;
                    data.map(each => {
                        temp.push({value: each.true_stop_id, label: each.stop_name, lat: each.stop_lat, lng: each.stop_long, name: each.stop_name})
                    });
                    this.setState({station: temp});
                }
            })
        }
    }

    // If time change, modify the time state
    timeOnchange = (val) => {
        let time = val.format();
        let unixtime = moment(new Date(time)).format('x') / 1000;
        this.setState({time: unixtime});
    }

    // If the start stop change
    startChange = (val) => this.setState({start_stop: val})
    // If the end stop change
    endChange = (val) => this.setState({end_stop: val})
    // When user choose another view
    switchView = (value) => {
        this.setState({view: value, station: []});
        //Clear the markers when user switch to another view
        if (value === 'station')
            this.setState({prediction: {}});
        }
    // In route View, when user click submit button
    routeSubmit = () => {
        // Check all these fields are not blank
        if (this.state.selectedOption && this.state.start_stop && this.state.end_stop && this.state.time) {
            this.setState({view: 'loading', toggle: false});
            // Call the api to predict the time
            WebAPI.getTime(this.state.selectedOption.value, this.state.start_stop.value, this.state.end_stop.value, this.state.time, this.state.direction.value).then(r => {
                if (r.status === 'success') {
                    this.setState({prediction: r, view: 'result'});

                }
            });
        } else {
            this.setState({
				toggle: false,
				show: true,
				alert: {
					type: 'error',
					title: 'Oops!',
					text: 'Please finish the form!'
				}
			})
        }
    }

    startLocChange = (places) => {
        this.setState({start_loc: places[0].geometry.location})
    }

    destLocChange = (places) => {
        this.setState({dest_loc: places[0].geometry.location})
    }

    handleOver = (id) => {
        this.setState({blink: id});
    }

    handleOut = () => {
        this.setState({blink: ''});
    }

    //Get the google data
    stationSubmit = () => {
        this.setState({submitFlag: true});
        const start_loc = this.state.start_loc.lat();
        const start_lng = this.state.start_loc.lng();
        const end_loc = this.state.dest_loc.lat();
        const end_lng = this.state.dest_loc.lng();
		const time = this.state.time;


		if (start_loc && start_lng && end_loc && end_lng && time) {
			this.setState({view: 'loading'});
			WebAPI.getGoogleDirection(start_loc, start_lng, end_loc, end_lng, time).then(r => {
				if (r.status === 'success') {
					this.setState({prediction: r, view: 'station_result'});
				} else {
					this.setState({
						view: 'station',
						show: 'false',
						alert: {
							type: 'error',
							title: 'Oops!',
							text: 'Sorry, the bus is not running by dublin bus company!'
						}
					})
				}
			})
		} else {
			this.setState({
				show: true,
				alert: {
					type: 'error',
					title: 'Oops!',
					text: 'Please finish the form!'
				}
			})
		}

    }

    switchUserLoc = (place) => {
        this.setState({start_loc: place});
    }

    //Toggle the SideBar
    toggleSideBar = () => {
        this.setState({
            showsidebar: !this.state.showsidebar
        })
    }

    handleSelect = (val) => {
        const time = Math.floor(val.getTime() / 1000);
        this.setState({
			timepickerOpen: false,
			time: time,
		});
    }

	handleinfowSelect = (val) => {
		console.log(val);
		const time = Math.floor(val.getTime() / 1000);
		this.setState({
			infowtimeisOpen: false,
			showTimePicker: false,
			time: time,
			showsidebar: true
		}, () => this.routeSubmit());
	}

    openTimePicker = () => {
        this.setState({timepickerOpen: true});
    }

	login = (username, pwd) => {
		fetch('/api/login', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify(
				{
					"username": username,
					"password": pwd
				}
			)
		})
		.then(res => res.json())
		.then(data => {

			if (data.token) {
				localStorage.setItem('token', data.token);
				const detail = atob(data.token.split('.')[1]);
				const detail_json = JSON.parse(detail)
				this.setState({
						logged_in: true,
						mainView: 'Map',
						username: detail_json['username']
					});
			} else {
				this.setState({
					show: true,
					alert: {
						type: 'error',
						title: '',
						text: 'Incorrect username or password. Please try again!'
					}
				})
			}
		})

	}

	logout = () => {
		localStorage.removeItem('token');
		this.setState({logged_in: false, username: ''});
	}

	signup = (username, pwd) => {
		fetch('/api/signup', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json',
			},
			body: JSON.stringify({
				username: username,
				password: pwd
			})
		})
		.then(r => r.json())
		.then(r => {
			if (r.status === 'success') {
				this.setState({
					show: true,
					alert: {
						type: 'success',
						title: 'Success!',
						text: `You've succeed signed up a account!`
					},
					mainView: 'Map'
				})
			} else {
				this.setState({
					show: true,
					alert: {
						type: 'error',
						title: 'Oops!',
						text: `Sorry, your username has been taken by others, please choose another one.`
					}
				})
			}
		})

	}

	switchlogin = (val) => {
		this.setState({mainView: val});
	}

	showUserFav = () => {
		//fetch users' favourite places
		fetch('/api/userdata', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json',
				'Authorization': 'JWT ' + localStorage.getItem('token')
			},
		}).then(r => r.json())
		.then(data => {
			this.setState({showfav: true, favdata:data})
		});
	}

	chooseFav = (j) => {
		this.setState({
			showfav: false,
			showTimePicker: true,
			selectedOption: {
				value: j.routeid,
				label: j.routeid
			},
			start_stop:{
				value: j.originstop_id,
				label: j.originstop_name
			},
			end_stop: {
				value: j.destinationstop_id,
				label: j.destinationstop_name
			},
			direction: {
				value: j.direction_id,
				label: j.direction_name
			},
			showTimePicker: true
		});

		if (this.state.width < 700) {
			this.setState({infowtimeisOpen: true});
		}
	}

	deleteFav = (id) => {
		fetch('/api/deletejourney', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json',
				'Authorization': 'JWT ' + localStorage.getItem('token')
			},
			body: JSON.stringify({
				journey_id: id
			})
		})
		.then(r => r.json())
		.then(r => {
			if (r.status === "success") {
				// Delete successfully
			 	let temp  = this.state.favdata.data.filter(each => each.id != id);
				this.setState({favdata: {data: temp}});
			}
		})
	}

	handlesave = () => {
		// First decide whether the user is logged in or not
		if (this.state.logged_in) {
			if (this.state.selectedOption && this.state.start_stop && this.state.end_stop) {
				// Check whether the user has filled out all information then send the data
				fetch('/api/savedata', {
					method: 'POST',
					headers: {
						'Content-Type': 'application/json',
						'Authorization': 'JWT ' + localStorage.getItem('token')
					},
					body: JSON.stringify({
						routeid: this.state.selectedOption.value,
						dir_name: this.state.direction.label,
						dir_id: this.state.direction.value,
						origin_id: this.state.start_stop.value,
						origin_name: this.state.start_stop.label,
						dest_id: this.state.end_stop.value,
						dest_name: this.state.end_stop.label,
						jour: 'Journey'
					})
				}).then(this.setState({
					show: true,
					alert: {
						type: 'success',
						title: 'Success!',
						text: `You've saved this journey!`
					}
				}))
			} else {
				//Alert the user to finish the form
				this.setState({
					show: true,
					alert: {
						type: 'error',
						title: 'Oops!',
						text: 'Please finish the form!'
					},
				});
			}
		} else {
			//Alert the user to login first
			this.setState({
				show: true,
				alert: {
					type: 'error',
					title: 'Oops!',
					text: 'Please finish the from!'
				},
				mainView: 'login'
			});
		}
	}

    render() {
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
		let mainView;
		switch (this.state.mainView) {
			case 'Map':
				mainView = <Map
							stopsall={this.state.prediction}
							station={this.state.station}
							startLoc={this.state.start_loc}
							destLoc={this.state.dest_loc}
							view={this.state.view}
							blink={this.state.blink}
							submitFlag={this.state.submitFlag}
							/>
				break;
			case 'Twitter':
				mainView = <TwitterDisplay/>
				break;
			case 'login' :
				mainView = <Login
							login={this.login}
							switchsignup={()=>this.setState({mainView: 'signup'})}
							/>
				break;
			case 'signup':
				mainView = <SignUp
						   		signup={this.signup}
							/>
				break;
		}

        return (<div>
            <Route exact path="/" render={() => (<div className="base-container">
                    {this.state.showsidebar
                            ? <SideBar
								search={this.state.search}
								view={this.state.view}
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
								switchUserLoc={this.switchUserLoc}
								toggleSideBar={this.toggleSideBar}
								windowwidth={this.state.width}
								handleSelect={this.handleSelect}
								handleCancel={this.handleCancel}
								isOpen={this.state.timepickerOpen}
								openTimePicker={this.openTimePicker}
								handlesave={this.handlesave}/>
                            : null
                    }
                    <SweetAlert
						show={this.state.show}
						type={this.state.alert.type}
						title={this.state.alert.title}
					    text={this.state.alert.text}
						onConfirm={() => this.setState({show: false})}/>

					{(this.state.width <= 700 && !this.state.showsidebar) || this.state.width > 700
                            ? <div className="main">
                                    <div className="header">
                                        <ul className="navigator">
                                            {this.state.showsidebar
	                                            ? <i className="toggle fas fa-angle-double-left" onClick={this.toggleSideBar}></i>
	                                            : <i className="toggle fas fa-angle-double-right" onClick={this.toggleSideBar}></i>
                                            }
                                            <Link to='/apidoc'>
                                                <li>API</li>
                                            </Link>
                                            <li onClick={this.toggleClick}>
												{this.state.toggle? 'Map': 'Twitter'}
											</li>
												<li>
													{this.state.logged_in?
													<i className="fas fa-user dropdown">
														<div className="dropdown-content">
															<p className="log-options">Hi, {this.state.username}</p>
															<hr/>
															<p className="log-options" onClick={this.logout}>Log Out</p>
															<p className="log-options" onClick={this.showUserFav}>My Fav Places</p>
														</div>
													</i>
													:
													<i className="far fa-user dropdown">
														<div className="dropdown-content">
															<p className="log-options" onClick={this.switchlogin.bind(this, 'login')}>Log In</p>
															<p className="log-options" onClick={this.switchlogin.bind(this, 'signup')}>Sign Up</p>
														</div>
													</i>
													}
												</li>
                                        </ul>
                                    </div>
                                    <div id="map">
										{mainView}
									</div>

									{this.state.showfav?
										<div className="shadow-wrapper">
											<div className="infowindow">
											 	<MyFav
													favdata={this.state.favdata}
													choose={this.chooseFav}
													delete={this.deleteFav}
													infowclose={() => this.setState({showfav: false})}/>
											</div>
										</div>:
										null
									}

									{this.state.showTimePicker?
										<div className="shadow-wrapper">
											<div className="infowindow-small">
												{this.state.width <= 700 ?
													<DatePicker
														isOpen={this.state.infowtimeisOpen}
														dateFormat={['YYYY', ['MM', (month) => monthMap[month]], 'DD','hh', 'mm']}
														confirmText='Confrim'
														cancelText="Cancel"
														showFormat="YYYY/MM/DD/hh:mm"
														onSelect={this.handleinfowSelect}
				                    					onCancel={() => this.setState({infowtimeisOpen: false, showTimePicker: false})}
													/>
													:
													<div>
														<h2 className="time-note">Please select time:</h2>
														<Datetime
															className="timepicker"
															onChange={this.timeOnchange}
															inputProps={{placeholder: 'Choose The Time'}}
															value={new Date()}
														/>
														<button
															className="info-submit btn btn-primary"
															onClick={() => {
																this.routeSubmit();
																this.setState({showTimePicker: false});
															}}>
															Submit
														</button>
														<button
															className="info-submit btn btn-info"
															onClick={() => {
																this.setState({
																	showTimePicker: false,
																	showfav: true
																});
															}}>
															Back
														</button>

													</div>
												}
											</div>
										</div>
										: null
									}
                                </div>
                            : null
                    }
                </div>)}/>
            <Route exact path="/twitter" render={() => (<TwitterDisplay/>)}/>
            <Route exact path="/term" render={() => (<Term/>)}/>
            <Route exact path="/apidoc" render={() => (<APIDoc/>)}/>
        </div>)
    }
}

export default App
