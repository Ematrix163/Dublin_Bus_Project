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
		.then(res => res.route)


export const getStation = (routeid) =>
	fetch(`${api}/station`, {headers})
		.then(res => res.json())
		.then(res => res.station)
