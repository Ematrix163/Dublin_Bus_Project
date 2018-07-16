/*
This is all api methods
*/

const api = "http://localhost:8000/api"

const headers = {
  'Accept': 'application/json',
}

export const getAllRoute = () =>
	fetch(`${api}/allroutes`, {headers})
		.then(res => res.json())


export const getStation = (routeid) =>
	fetch(`${api}/station?route=${routeid.value}`, {headers})
		.then(res => res.json())


//Get the predict time
export const getTime = (routeid, start_stop, end_stop) =>
	fetch(`${api}/routetime`, {
		methods: 'GET',
		body: {
			'routeid': routeid,
			'start_stop': start_stop,
			'end_stop': end_stop
		}
	}).then(res => res.json())
