import React from 'react';
import './css/App.css';
import './css/signin.css'

class Login extends React.Component {
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
						<h2>User Login</h2>
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
							<i className="sign-icon user"></i>
						</li>
						 <li>
							<input
								type="password"
								value={this.state.password}
								placeholder="password"
								onChange={this.handlepwd}/>
							<i className="sign-icon lock"></i>
						</li>
					</ul>
				</form>
				<div style={{float: 'right'}}>Click to <span className='signup-alert' onClick={this.props.switchsignup}>sign up!</span></div>
				<div className="submit">
					<input
						type="submit"
						value="Log in"
						onClick={this.props.login.bind(this, this.state.username, this.state.password)}/>
				</div>
			</div>
		)
	}
}

export default Login
