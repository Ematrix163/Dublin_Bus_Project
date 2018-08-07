
/* global google */

import React from 'react';
import Spinner from './image/spinner.svg'

const { compose, withProps, lifecycle } = require("recompose");
const { withScriptjs,} = require("react-google-maps");
const { StandaloneSearchBox } = require("react-google-maps/lib/components/places/StandaloneSearchBox");

const SearchBox = compose(
  withProps({
	  googleMapURL: "https://maps.googleapis.com/maps/api/js?v=3.exp&libraries=geometry,drawing,places&key=AIzaSyDjRsP2Z4JM86ag3hkbRMmfS1a72YBlD8w",
      loadingElement: <div style={{ height: `100%` }} />,
      containerElement: <div style={{ height: `400px` }} />,
  }),

  lifecycle({
    componentWillMount() {
      const refs = {}
      this.setState({
        places: [],
		bounds: new google.maps.LatLngBounds(
			new google.maps.LatLng(52.64,-6.6),
    		new google.maps.LatLng(53.65,-6.0)
		),
		useMyLoc: () => {
			// this.props.useMyLoc();
			this.setState({spinner: true});
			if ("geolocation" in navigator) {
				navigator.geolocation.getCurrentPosition(
					(position) => {
						this.setState({spinner: false});
						// for when getting location is a success
						const places = new google.maps.LatLng(position.coords.latitude.toFixed(4), position.coords.longitude.toFixed(4));
						this.setState({places, text: places});
						this.props.switchUserLoc(places);
	   				},
					(error_message) => {
						this.setState({spinner: false});
	   					console.error('An error has occured while retrieving location', error_message)
	 				}
			)};
		},
        onSearchBoxMounted: ref => {
          refs.searchBox = ref;
        },
        onPlacesChanged: () => {
          const places = refs.searchBox.getPlaces();
          this.setState({places,});
		  this.props.locChange(places);
        },
      })
    },
  }),
  withScriptjs
)(props =>
  <div data-standalone-searchbox="">
    <StandaloneSearchBox
      ref={props.onSearchBoxMounted}
      bounds={props.bounds}
      onPlacesChanged={props.onPlacesChanged}
    >
      <input
        type="text"
        placeholder= {props.text}
        style={{
          boxSizing: `border-box`,
          border: `1px solid transparent`,
          width: props.type === 'origin'? `85%`: `100%`,
          height: `32px`,
          padding: `0 12px`,
          borderRadius: `3px`,
          boxShadow: `0 2px 6px rgba(0, 0, 0, 0.3)`,
          fontSize: `14px`,
          outline: `none`,
          textOverflow: `ellipses`,
		  display: `inline`,
		  margin: `8px 10px 15px 0`
        }}

      />
    </StandaloneSearchBox>
	{props.type === 'origin'?
		props.spinner?
			<img style={{display :`inline`, width: `35 px`}} src={Spinner} alt="" />
			:<span>&nbsp;&nbsp;&nbsp;<i className="use-my-loc fas fa-location-arrow" onClick={props.useMyLoc}><span className="tooltiptext">Use My Location</span></i></span>
		: null
	}
  </div>
);

export default SearchBox
