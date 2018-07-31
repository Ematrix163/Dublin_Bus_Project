
/* global google */

import React, {Component} from 'react';

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
        placeholder='Your Location'
        style={{
          boxSizing: `border-box`,
          border: `1px solid transparent`,
          width: `100%`,
          height: `32px`,
          padding: `0 12px`,
          borderRadius: `3px`,
          boxShadow: `0 2px 6px rgba(0, 0, 0, 0.3)`,
          fontSize: `14px`,
          outline: `none`,
          textOverflow: `ellipses`,
        }}
      />
    </StandaloneSearchBox>
    <ol>
    </ol>
  </div>
);

export default SearchBox
