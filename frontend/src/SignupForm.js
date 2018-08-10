import React from 'react';
import PropTypes from 'prop-types';
import './css/main.css';
import './css/util.css';

class SignupForm extends React.Component {
  state = {
    username: '',
    password: ''
  };

  handle_change = e => {
    const name = e.target.name;
    const value = e.target.value;
    this.setState(prevstate => {
      const newState = { ...prevstate };
      newState[name] = value;
      return newState;
    });
  };

  render() {
    return (


         <div className="limiter">
      <div className="container-login100">
      <div className="wrap-login100">


      <form className="login100-form validate-form" onSubmit={e => this.props.handle_signup(e, this.state)}>
        <span className="login100-form-title">Sign Up</span>


        <label htmlFor="username">Username</label>

          <div className="wrap-input100 validate-input">
        <input
            className="input100"
          type="text"
          name="username"
          value={this.state.username}
          onChange={this.handle_change}
        />
              <span className="focus-input100"></span>


              </div>



                    <div className="wrap-input100 validate-input">

        <label htmlFor="password">Password</label>
        <input
            className="input100"
          type="password"
          name="password"
          value={this.state.password}
          onChange={this.handle_change}
        />

<span className="focus-input100"></span>
            <span className="symbol-input100">
              <i className="fa fa-lock" aria-hidden="true"></i>
            </span>



                        </div>

        <input type="submit" value="Sign Up" />
      </form>


               </div>
    </div>
  </div>


    );
  }
}

export default SignupForm;

SignupForm.propTypes = {
  handle_signup: PropTypes.func.isRequired
};