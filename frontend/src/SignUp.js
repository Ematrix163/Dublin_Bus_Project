import React from 'react';
import './css/App.css';
import './css/signin.css'

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
						<h2>Create Your Account</h2>
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
				<div className="submit">
					<input
						type="submit"
						value="Sign Up"
						onClick={this.props.signup.bind(this, this.state.username, this.state.password)}/>
				</div>
			</div>
		)
	}
}

export default SignUp
