/*global google*/

import React from 'react';
import { compose, withProps, lifecycle, withStateHandlers } from "recompose"
import { withScriptjs, withGoogleMap, GoogleMap, Marker, DirectionsRenderer, InfoWindow} from "react-google-maps"

const MyMapComponent = compose(
	withStateHandlers(() => ({isOpen: {},}),
	{
		onToggleOpen: ({ isOpen }) => () => ({isOpen: !isOpen,})
	}),
    withProps({
        googleMapURL: "https://maps.googleapis.com/maps/api/js?v=3.exp&libraries=geometry,drawing,places&key=AIzaSyDjRsP2Z4JM86ag3hkbRMmfS1a72YBlD8w",
        loadingElement: <div style={{ height: `100%` }}/>,
		containerElement: <div style={{ height: `100%` }} />,
        mapElement: <div style={{ height: `100%` }} />,
    }),
    withScriptjs,
    withGoogleMap,
	lifecycle({
       componentDidUpdate () {
		 if (this.props.view === 'station' && this.props.startLoc && this.props.destLoc && this.props.submitFlag) {
			 const DirectionsServiceStation = new google.maps.DirectionsService();
			 DirectionsServiceStation.route({
 			   origin: new google.maps.LatLng(this.props.startLoc.lat(),this.props.startLoc.lng()),
 			   destination: new google.maps.LatLng(this.props.destLoc.lat(),this.props.destLoc.lng()),
 			   travelMode: google.maps.TravelMode.TRANSIT,
 			}, (result, status) => {
 				if (status === google.maps.DirectionsStatus.OK) {
 				 this.setState({
 				   directions: result,
 				 });
 				 } else {
 				 console.error(`error fetching directions ${result}`);
 			   }
 			 });
		 }
       }
     })
	)((props) =>
	    <GoogleMap defaultZoom={12} defaultCenter={{ lat: 53.350140, lng: -6.266155 }}>
			{props.directions && <DirectionsRenderer directions={props.directions} />}
        	{props.stops.map(marker => (
    			<Marker
					key={marker.stop_id}
					position={{ lat: parseFloat(marker.stop_lat), lng: parseFloat(marker.stop_long) }}
					onClick={props.onToggleOpen}
					animation={marker.stop_id === props.blink? google.maps.Animation.BOUNCE: ""}
					>
				</Marker>
			))}
	    </GoogleMap>
	)

class Map extends React.PureComponent {
    state = {
        isMarkerShown: true,
        isRouteShown: true
    }

    componentDidMount() {

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
                isRouteShown={this.state.isRouteShown}
				stops={this.props.stops}
				station={this.props.station}
				blink={this.props.blink}
				view={this.props.view}
				startLoc={this.props.startLoc}
				destLoc={this.props.destLoc}
				submitFlag={this.props.submitFlag}
            />
        )
    }
}

export default Map;
