import React, {Component} from 'react';
import {compose, withProps, lifecycle} from "recompose"
import {withScriptjs, withGoogleMap, GoogleMap, Marker, StandaloneSearchBox} from "react-google-maps"

// const { SearchBox } = require("react-google-maps/lib/components/places/StandaloneSearchBox");

//search box for station view for user to be able to search for stations
const SearchBox = compose(withProps({
    googleMapURL: "https://maps.googleapis.com/maps/api/js?v=3.exp&libraries=geometry,drawing,places&key=AIzaSyDjRsP2Z4JM86ag3hkbRMmfS1a72YBlD8w", loadingElement: <div style={{
            height: `100%`
        }}/>,
    containerElement: <div style={{
                height: `400px`
            }}/>
}), lifecycle({
    componentWillMount() {
        const refs = {}

        this.setState({
            places: [],
            onSearchBoxMounted: ref => {
                refs.searchBox = ref;
            },
            onPlacesChanged: () => {
                const places = refs.searchBox.getPlaces();
                this.setState({places});
            }
        })
    }
}), withScriptjs)(props => <div data-standalone-searchbox="">
    <StandaloneSearchBox ref={props.onSearchBoxMounted} bounds={props.bounds} onPlacesChanged={props.onPlacesChanged}>
        <input type="text" placeholder="Customized your placeholder" style={{
                boxSizing: `border-box`,
                border: `1px solid transparent`,
                width: `240px`,
                height: `32px`,
                padding: `0 12px`,
                borderRadius: `3px`,
                boxShadow: `0 2px 6px rgba(0, 0, 0, 0.3)`,
                fontSize: `14px`,
                outline: `none`,
                textOverflow: `ellipses`
            }}/>
    </StandaloneSearchBox>
    <ol>
        {
            props.places.map(({place_id, formatted_address, geometry: {
                    location
                }}) => <li key={place_id}>
                    {formatted_address}
                    {" at "}
                    ({location.lat()}, {location.lng()})
                </li>)
        }
    </ol>
</div>);

export default SearchBox
