import React, { Component } from 'react';
import { compose, withProps } from "recompose"
import { withScriptjs, withGoogleMap, GoogleMap, Marker, } from "react-google-maps"


const MyMapComponent = compose(
    withProps({
        googleMapURL: "https://maps.googleapis.com/maps/api/js?v=3.exp&libraries=geometry,drawing,places&key=AIzaSyDjRsP2Z4JM86ag3hkbRMmfS1a72YBlD8w",
        loadingElement: <div style={{ height: `100%` }}/>,
		containerElement: <div style={{ height: `100%` }} />,
        mapElement: <div style={{ height: `100%` }} />,
    }),
    withScriptjs,
    withGoogleMap
	)((props) =>
	    <GoogleMap
	        defaultZoom={8}
	        defaultCenter={{ lat: 53.350140, lng: -6.266155 }}
	    >
	        {props.isMarkerShown && <Marker position={{ lat: 53.350140, lng: -6.266155 }} onClick={props.onMarkerClick} />}
	    </GoogleMap>
)



class Map extends React.PureComponent {
    state = {
        isMarkerShown: false,
    }

    componentDidMount() {
        this.delayedShowMarker()
    }

    delayedShowMarker = () => {
        setTimeout(() => {
            this.setState({ isMarkerShown: true })
        }, 3000)
    }

    handleMarkerClick = () => {
        this.setState({ isMarkerShown: false })
        this.delayedShowMarker()
    }

    render() {
        return (
            <MyMapComponent
                isMarkerShown={this.state.isMarkerShown}
                onMarkerClick={this.handleMarkerClick}
            />
        )
    }
}

export default Map;
