import React from 'react';
import 'react-select/dist/react-select.css';
import './css/main.css';

import { Timeline } from 'react-twitter-widgets'


class TwitterDisplay extends React.Component {

// var Timeline = require('react-twitter-widgets').Timeline

    render() {



		return (
		    // use linkProps if you want to pass attributes to all links

            <div className="TwitterDisplay">


  <Timeline
    dataSource={{
      sourceType: 'profile',
      screenName: 'aaroadwatch'
    }}
    options={{
      username: 'TwitterDev',
      height: '400',

    }}
    onLoad={() => console.log('Timeline is loaded!')}
  />

            </div>
        )

    }
}








export default TwitterDisplay;
