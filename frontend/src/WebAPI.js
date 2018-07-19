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


export const getStation = (routeid, direction) =>
	fetch(`${api}/station?route=${routeid}&direction=${direction}`, {headers})
		.then(res => res.json())



//Get different directions
export const getDirection = (routeid) =>
	fetch(`${api}/direction?routeid=${routeid}`)
		.then(res => res.json())


//Get the predict time
export const getTime = (routeid, start_stop, end_stop, time, direction) =>
	fetch(`${api}/time?routeid=${routeid}&start_stop=${start_stop}&end_stop=${end_stop}&datetime=${time}&direction=${direction}`, {
		methods: 'GET',
		// body: {
		// 	'routeid': routeid,
		// 	'start_stop': start_stop,
		// 	'end_stop': end_stop,
		// 	'datetime': time
		// }
	}).then(res => res.json())
