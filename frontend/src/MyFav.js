import React from 'react';

class MyFav extends React.Component {

	render() {
		return (
			<table className="table">
			  <thead className="thead-dark">
			    <tr>
				  <th scope="col">Journey Name</th>
			      <th scope="col">Line ID</th>
			      <th scope="col">Direction</th>
			      <th scope="col">Departure Stop</th>
			      <th scope="col">Destination Stop</th>
				  <th scope="col"></th>
			    </tr>
			  </thead>
			  <tbody>
			    {this.props.favdata.data.map(j => {
					console.log(j);
					return (
						<tr key={j.journeyname}>
					      <th>{j.journeyname}</th>
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
