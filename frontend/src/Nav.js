import React from 'react';
import PropTypes from 'prop-types';

function Nav(props) {
  const logged_out_nav = (

<span>
      <li onClick={() => props.display_form('login')}>login</li>

       <li onClick={() => props.display_form('signup')}>signup</li>

</span>

  );

  const logged_in_nav = (

      <li onClick={props.handle_logout}>logout</li>

  );
  return <span>{props.logged_in ? logged_in_nav : logged_out_nav}</span>;
}

export default Nav;

Nav.propTypes = {
  logged_in: PropTypes.bool.isRequired,
  display_form: PropTypes.func.isRequired,
  handle_logout: PropTypes.func.isRequired
};



