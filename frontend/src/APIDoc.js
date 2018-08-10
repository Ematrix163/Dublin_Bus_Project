import React from 'react'
import Markdown from 'react-markdown'

class APIDoc extends React.Component {
	constructor(props) {
		super(props);
		this.state = {
			text: ''
		}
	}

	componentDidMount() {
		fetch('http://localhost:8000/api/static')
		.then(res => res.json())
			.then(r => {
				this.setState({text: r});
			})
	}


	render() {
		return (
			<div className='api'>
				<div className='api-container'>
					<Markdown source={this.state.text}/>
				</div>
			</div>
		)
	}
}


export default APIDoc
