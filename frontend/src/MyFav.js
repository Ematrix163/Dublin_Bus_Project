import React from 'react';

class MyFav extends React.Component {

	render() {
		return (
			<table className="fav-table">
				<tbody>
			    <tr>
			      <th align="center">Line</th>
			      <th align="center">Direction</th>
			      <th align="center">Departure Stop</th>
			      <th>Destination Stop</th>
				  <th colspan="2"><i onClick={this.props.infowclose} className="info-close fas fa-window-close"></i></th>
			    </tr>
			    {this.props.favdata.data.map((j, index) => {
					return (
						<tr key={index}>
						  <td>{j.routeid}</td>
					      <td>{j.direction_name}</td>
					      <td>{j.originstop_name}</td>
					      <td>{j.destinationstop_name}</td>
						  <td>
							  <i className="far fa-check-square chose-journey"  onClick={this.props.choose.bind(this, j)}></i>
						  </td>
						  <td><i className="far fa-trash-alt chose-journey" onClick={this.props.delete.bind(this, j.id)}></i></td>
					    </tr>
					)
				})}
			</tbody>
			</table>
		)
	}
}


export default MyFav
