import React from 'react';

import './css/main.css';

import { Timeline } from 'react-twitter-widgets'


class TwitterDisplay extends React.Component {

// var Timeline = require('react-twitter-widgets').Timeline
    render() {
		return (
		    // use linkProps if you want to pass attributes to all links
			<div className="twitter-display">
				<Timeline
					dataSource={{
					  sourceType: 'profile',
					  screenName: 'aaroadwatch'
					}}
					options={{
					  username: 'TwitterDev',
					  height: 'calc(100vh - 100px)',

					}}
				/>
		</div>
        )
    }
}


export default TwitterDisplay;
