import React from 'react';

class MyFav extends React.Component {

	render() {
		return (
			<table className="fav-table">
				<tbody>
			    <tr>
				  <th>Journey</th>
			      <th>Line</th>
			      <th>Direction</th>
			      <th>Departure Stop</th>
			      <th>Destination Stop</th>
				  <th><i onClick={this.props.infowclose} className="info-close fas fa-window-close"></i></th>
			    </tr>
			    {this.props.favdata.data.map((j, index) => {
					return (
						<tr key={index}>
					      <td>{j.journeyname}</td>
						  <td>{j.routeid}</td>
					      <td>{j.direction_name}</td>
					      <td>{j.originstop_name}</td>
					      <td>{j.destinationstop_name}</td>
						  <td className="chose-journey" onClick={this.props.choose.bind(this, j)}>Choose</td>
					    </tr>
					)
				})}
			</tbody>
			</table>
		)
	}
}


export default MyFav
