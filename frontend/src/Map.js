/*global google*/

import React from 'react';
import { compose, withProps, lifecycle } from "recompose"
import { withScriptjs, withGoogleMap, GoogleMap, Marker, DirectionsRenderer} from "react-google-maps"

const MyMapComponent = compose(
    withProps({
        googleMapURL: "https://maps.googleapis.com/maps/api/js?v=3.exp&libraries=geometry,drawing,places&key=AIzaSyDjRsP2Z4JM86ag3hkbRMmfS1a72YBlD8w",
        loadingElement: <div style={{ height: `100%` }}/>,
		containerElement: <div style={{ height: `100%` }} />,
        mapElement: <div style={{ height: `100%` }} />,
    }),
    withScriptjs,
    withGoogleMap,
	lifecycle({
       componentDidUpdate   () {
		 if (this.props.station) {
			 const DirectionsService = new google.maps.DirectionsService();
			 let start_lat = this.props.station[0].lat;
			 let start_lng = this.props.station[0].lng;
			 let length = this.props.station.length
			 let end_lat = this.props.station[length-1].lat;
			 let end_lng = this.props.station[length-1].lng;
			  DirectionsService.route({
				origin: new google.maps.LatLng(start_lat, start_lng),
				destination: new google.maps.LatLng(end_lat, end_lng),
				travelMode: google.maps.TravelMode.TRANSIT,
			   	transitOptions: {
					modes: ['BUS'],
					routingPreference: 'FEWER_TRANSFERS',
					departureTime: new Date(2018, 7, 19, 16, 40, 0, 0)
				},
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
        	{props.stops.map(marker => (
    			<Marker key={marker.stop_id} position={{ lat: parseFloat(marker.stop_lat), lng: parseFloat(marker.stop_long) }}/>
			))}
		 	{props.directions &&
				<DirectionsRenderer
					directions={props.directions}
					options={{suppressMarkers: true}} />}
	    </GoogleMap>
)


{/*Handling marker click so that when it is clicked it disappears*/}
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
