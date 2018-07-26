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
		 if (this.props.station.length > 0 && this.props.view === 'route') {
			 const DirectionsServiceRoute = new window.google.maps.DirectionsService();
			 let length = this.props.station.length;
			 let waypts = [];
			 let start_lat = this.props.station[0].lat;
			 let start_lng = this.props.station[0].lng;
			 let end_lat = this.props.station[length-1].lat;
			 let end_lng = this.props.station[length-1].lng;
			 DirectionsServiceRoute.route({
				origin: new google.maps.LatLng(start_lat, start_lng),
				destination: new google.maps.LatLng(end_lat, end_lng),
				waypoints: waypts,
				travelMode: google.maps.TravelMode.TRANSIT,
			 }, (result, status) => {
				 if (status === google.maps.DirectionsStatus.OK) {
					 	 console.log(result);
				  this.setState({
					directions: result,
				  });
			  	  } else {
				  console.error(`error fetching directions ${result}`);
				}
			  });
		 } else if (this.props.view === 'station') {
			 console.log('1');
			 const DirectionsServiceStation = new google.maps.DirectionsService();
			 DirectionsServiceStation.route({
 			   origin: new google.maps.LatLng(this.props.startLoc.lat(),this.props.startLoc.lng()),
 			   destination: new google.maps.LatLng(this.props.destLoc.lat(),this.props.destLoc.lng()),
 			   travelMode: google.maps.TravelMode.TRANSIT,
 			}, (result, status) => {
 				if (status === google.maps.DirectionsStatus.OK) {
 						console.log(result);
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
			<div>
        	{props.stops.map(marker => (
    			<Marker key={marker.stop_id} position={{ lat: parseFloat(marker.stop_lat), lng: parseFloat(marker.stop_long) }} onClick={props.onToggleOpen}>
					  {props.isOpen && <InfoWindow onCloseClick={props.onToggleOpen.bind(this,marker.stop_id)}><div>{marker.stop_name}</div></InfoWindow>}
				</Marker>
			))}
		 	{props.directions &&<DirectionsRenderer directions={props.directions} options={{suppressMarkers: true}} />}
			</div>
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
            />
        )
    }
}

export default Map;
