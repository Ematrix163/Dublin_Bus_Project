import React from 'react';

import './css/App.css';
import './css/signin.css'

import { Redirect, Link } from 'react-router-dom'

class SignUp extends React.Component {
	constructor(props) {
		super(props);
		this.state = {
			username: '',
			password: ''
		}
	}

	handlepwd = (val) => {
		this.setState({password: val.target.value});
	}

	handleuser = (val) => {
		this.setState({username: val.target.value});
	}


    render() {
        return (
			<div className="login">
				<div className="ribbon-wrapper h2 ribbon-red">
					<div className="ribbon-front">
						<h2>Sign Up Your Account</h2>
					</div>
					<div className="ribbon-edge-topleft2"></div>
					<div className="ribbon-edge-bottomleft"></div>
				</div>
				<form>
					<ul>
						<li>
							<input
								type="text"
								className="text"
								placeholder="Username"
								value={this.state.username}
								onChange={this.handleuser}/>
							<a href="#" className="icon user"></a>
						</li>
						 <li>
							<input
								type="password"
								value={this.state.password}
								placeholder="password"
								onChange={this.handlepwd}/>
							<a href="#" className="icon lock"></a>
						</li>
					</ul>
				</form>
				<div>Click here to sign up!</div>
				<div className="submit">
					<input
						type="submit"
						value="Log in"
					/>
				</div>
			</div>
		)
	}
}

export default SignUp
