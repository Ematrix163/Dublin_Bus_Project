const api = 'url'


const headers = {
	'Access-Control-Allow-Origin': '*',
	'Accept': 'application/json'
}

export const getAllRoute = (route) => {
	fetch(`${api}`, {headers})
		.then(res => res.json())
}
