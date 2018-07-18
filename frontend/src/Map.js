import React from 'react';
import { compose, withProps } from "recompose"
import { withScriptjs, withGoogleMap, GoogleMap, Marker, } from "react-google-maps"

{/*Loading map of Dublin onto page*/}
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
	    <GoogleMap defaultZoom={12} defaultCenter={{ lat: 53.350140, lng: -6.266155 }}>
     	{/*This line below creates markers based on the props.LocationArray above */}

        {/*(currently hardcoded, but it will eventually take in the locations of the stops)*/}
        {props.stops.map(marker => (
    		<Marker key={marker.stop_id} position={{ lat: parseFloat(marker.stop_lat), lng: parseFloat(marker.stop_long) }}/>
		))}
	    </GoogleMap>
)


{/*Handling marker click so that when it is clicked it disappears*/}
class Map extends React.PureComponent {
    state = {
        isMarkerShown: true,
        isRouteShown: false
    }

    componentDidMount() {
        // // this.delayedShowMarker()
        // this.showRouteMarkers()
    }

    // delayedShowMarker = () => {
    //     setTimeout(() => {
    //         this.setState({ isMarkerShown: true })
    //     }, 3000)
    // }

    handleMarkerClick = () => {
        this.setState({ isMarkerShown: false })
        this.delayedShowMarker()
    }

     // showRouteMarkers = () => {
     //    setTimeout(() => {
     //        this.setState({ isRouteShown: true })
     //    }, 3000)

    // }

    render() {
        return (
            <MyMapComponent
                isMarkerShown={this.state.isMarkerShown}
                onMarkerClick={this.handleMarkerClick}
                isRouteShown={this.state.isRouteShown}
				stops={this.props.stops}
            />
        )
    }
}

export default Map;
