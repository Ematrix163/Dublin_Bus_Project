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
        locationArray: [{lat: 53.3454764728264, lng: -6.26620615548430000000}, {lat: 53.3469263969899, lng: -6.26207684589386000000},{lat: 53.3462448501457, lng: -6.25910057954255}, {lat: 53.3455062736618, lng: -6.256532266224},
        {lat: 53.34475116159920600000, lng: -6.25283825801258000000},
        {lat: 53.34261644427850000000, lng: -6.25621463756987000000},
        {lat: 53.33985341637740000000, lng: -6.24737682273898000000},
{lat: 53.34133589331870000000, lng: -6.25162625805016100000},
{lat: 53.34359131981290000000, lng: -6.24974670516903100000}],



    }),
    withScriptjs,
    withGoogleMap
	)((props) =>
	    <GoogleMap
	        defaultZoom={8}
	        defaultCenter={{ lat: 53.350140, lng: -6.266155 }}
	    >


     {/*This line below creates markers based on the props.LocationArray above */}
            {/*(currently hardcoded, but it will eventually take in the locations of the stops)*/}
            { props.isRouteShown && props.locationArray.map(marker => (
    <Marker
      position={{ lat: marker.lat, lng: marker.lng }}

    />
))}





	    </GoogleMap>
)


{/*Handling marker click so that when it is clicked it disappears*/}
class Map extends React.PureComponent {
    state = {
        isMarkerShown: false,
        isRouteShown: false
    }

    componentDidMount() {
        this.delayedShowMarker()
        this.showRouteMarkers()
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

     showRouteMarkers = () => {
        setTimeout(() => {
            this.setState({ isRouteShown: true })
        }, 3000)

    }

    render() {
        return (
            <MyMapComponent
                isMarkerShown={this.state.isMarkerShown}
                onMarkerClick={this.handleMarkerClick}
                isRouteShown={this.state.isRouteShown}
            />
        )
    }
}

export default Map;
