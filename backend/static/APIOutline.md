# API Documentation


**1. All Line ID**

>   URL: https://www.dublinroute.com/api/allroutes
>

   Response Example:

   ```json
   [
       {
           "routes": "1"
       },
       {
           "routes": "102"
       },
       {
           "routes": "104"
       },
       {
           "routes": "11"
       },
   ]
   ```
    
   Returns all Dublin bus line id.



**2. Get directions of a line ID**

   > URL: https://www.dublinroute.com/api/direction?routeid=${your_line_id}

   

   > Request Example:
  https://www.dublinroute.com/api/direction?routeid=46A


   Response: 

   ```json
   {
       "dir1": "From Phoenix Park To Dun Laoghaire",
       "dir2": "From Dun Laoghaire To Phoenix Park "
   }
   ```

   Note: The routeid is not case sensitive. 

   

**3. Get the stations of a line id**  


   > URL: https://www.dublinroute.com/api/station?direction=\${direction}&route=\${routeid}

   Response:

   ```json
{
    "status": "success",
    "data": [
        {
            "stop_id": "8220DB000807",
            "stop_name": "Arbour Hill, Phoenix Park Gate",
            "stop_lat": "53.35155651211540000000",
            "stop_long": "-6.29770038608451000000",
            "true_stop_id": 807
        },
        {
            "stop_id": "8220DB000808",
            "stop_name": "Cabra East, North Circular Road (O'Devaney Gardens)",
            "stop_lat": "53.35399466951961000000",
            "stop_long": "-6.29534982649487100000",
            "true_stop_id": 808
        },
        {
            "stop_id": "8220DB000809",
            "stop_name": "Cabra East, North Circular Road (Oxmanstown Road)",
            "stop_lat": "53.35526073980500400000",
            "stop_long": "-6.29337634624951000000",
            "true_stop_id": 809
        },
        {
            "stop_id": "8220DB000810",
            "stop_name": "Cabra East, North Circular Road",
            "stop_lat": "53.35709986015710000000",
            "stop_long": "-6.28999764127673000000",
            "true_stop_id": 810
        },
        {
            "stop_id": "8220DB000811",
            "stop_name": "Cabra East, North Circular Road",
            "stop_lat": "53.35767214989720500000",
            "stop_long": "-6.28728544721744100000",
            "true_stop_id": 811
        },
        {
            "stop_id": "8220DB000812",
            "stop_name": "Cabra East, Grangegorman Hospital",
            "stop_lat": "53.35826636065229400000",
            "stop_long": "-6.28422674373800000000",
            "true_stop_id": 812
        },
        {
            "stop_id": "8220DB000813",
            "stop_name": "Cabra East, North Circular Road (Charleville Road)",
            "stop_lat": "53.35919004609720400000",
            "stop_long": "-6.28095937438322000000",
            "true_stop_id": 813
        },
        {
            "stop_id": "8220DB000814",
            "stop_name": "Phibsborough, North Circular Road (Cabra Road)",
            "stop_lat": "53.36054001513700000000",
            "stop_long": "-6.27609704929995100000",
            "true_stop_id": 814
        }
}
   ```

   

* `stop_id`: The full stop id of the stop.
* `stop_name`: The name of the stop.
* `stop_lat`: The latitude of the stop.
* `stop_lng`: The longitude of the stop.
* `true_stop_id`: The last four digit 

 

4. Predict Time

   > API CALL: `https://www.dublinroute.com/api/time?routeid=${routeid}&start_stop=${start_stop}&end_stop=${end_stop}&datetime=${datetime}&direction=${direction}`

   Request Parameters:

   `routeid`: The bus line id of the route.

   `start_stop`: The stop id of the departure stop.

   `end_stop`: The stop id of the destination stop.

   `datetime`: The unixtime

   `direction`: The direction of the bus. 1 or 2.

   ```json
   {
       "status": "success",
       "data": [
           {
               "detail": [
                   129.28838530737093,
                   82.1440770481716,
                   86.06053386938444,
                   79.33715190789118,
                   8.299953887039743,
                   218.5556833491369,
                   63.22767360619676,
                   110.06241558835553,
                   92.38577100195205,
                   182.2275161064153,
                   70.77476925591591,
                   40.81011969438985,
                   15.386551849757119,
                   70.01102715707745,
                   25.434120498926006
               ],
               "totalDuration": 21,
               "stopsNum": 16,
               "stopInfo": [
                   {
                       "stop_id": "8220DB007391",
                       "stop_name": "Merrion Square South",
                       "stop_lat": "53.33909074783990000000",
                       "stop_long": "-6.24991601709797000000",
                       "true_stop_id": 7391
                   },
                   {
                       "stop_id": "8220DB000493",
                       "stop_name": "Merrion Square, Holles Street",
                       "stop_lat": "53.33985341637740000000",
                       "stop_long": "-6.24737682273898000000",
                       "true_stop_id": 493
                   },
                   {
                       "stop_id": "8220DB000494",
                       "stop_name": "Clare Street",
                       "stop_lat": "53.34133589331870000000",
                       "stop_long": "-6.25162625805016100000",
                       "true_stop_id": 494
                   },
                   {
                       "stop_id": "8220DB000495",
                       "stop_name": "Pearse Station, Outside Train Station",
                       "stop_lat": "53.34359131981290000000",
                       "stop_long": "-6.24974670516903100000",
                       "true_stop_id": 495
                   },
                   {
                       "stop_id": "8220DB000400",
                       "stop_name": "Trinity College, Shaw Street",
                       "stop_lat": "53.34475116159920600000",
                       "stop_long": "-6.25283825801258000000",
                       "true_stop_id": 400
                   },
                   {
                       "stop_id": "8220DB007588",
                       "stop_name": "Pearse Street",
                       "stop_lat": "53.34502174308180000000",
                       "stop_long": "-6.25290229106650900000",
                       "true_stop_id": 7588
                   },
                   {
                       "stop_id": "8220DB007392",
                       "stop_name": "Temple Bar, Aston Quay",
                       "stop_lat": "53.34646041538011000000",
                       "stop_long": "-6.26093925922545050000",
                       "true_stop_id": 7392
                   },
                   {
                       "stop_id": "8220DB000312",
                       "stop_name": "Temple Bar, Wellington Quay",
                       "stop_lat": "53.34547647282640000000",
                       "stop_long": "-6.26620615548430000000",
                       "true_stop_id": 312
                   },
                   {
                       "stop_id": "8220DB001444",
                       "stop_name": "Dublin City South, Merchant's Quay",
                       "stop_lat": "53.34511841466180000000",
                       "stop_long": "-6.27374547145288900000",
                       "true_stop_id": 1444
                   },
                   {
                       "stop_id": "8220DB001445",
                       "stop_name": "James's Gate, Ushers Quay",
                       "stop_lat": "53.34567841025250000000",
                       "stop_long": "-6.27828883961720000000",
                       "true_stop_id": 1445
                   },
                   {
                       "stop_id": "8220DB007078",
                       "stop_name": "Phoenix Park, Sean Heuston Bridge",
                       "stop_lat": "53.34791030524820600000",
                       "stop_long": "-6.29287390375090000000",
                       "true_stop_id": 7078
                   },
                   {
                       "stop_id": "8220DB001449",
                       "stop_name": "Phoenix Park, Conyngham Road Bus Garage",
                       "stop_lat": "53.34815282999489500000",
                       "stop_long": "-6.29789609467721000000",
                       "true_stop_id": 1449
                   },
                   {
                       "stop_id": "8220DB001450",
                       "stop_name": "Phoenix Park, Wellington Monument",
                       "stop_lat": "53.34815540423440000000",
                       "stop_long": "-6.30186141311769000000",
                       "true_stop_id": 1450
                   },
                   {
                       "stop_id": "8220DB001451",
                       "stop_name": "Islandbridge, Bridgewater Business Centre",
                       "stop_lat": "53.34827827893530000000",
                       "stop_long": "-6.30544644496588000000",
                       "true_stop_id": 1451
                   },
                   {
                       "stop_id": "8220DB002191",
                       "stop_name": "Islandbridge, Sarah Place",
                       "stop_lat": "53.34802557187770000000",
                       "stop_long": "-6.31044326467113950000",
                       "true_stop_id": 2191
                   },
                   {
                       "stop_id": "8220DB002192",
                       "stop_name": "Islandbridge, U.C.D Boat Club",
                       "stop_lat": "53.34724562293600000000",
                       "stop_long": "-6.31567109288469100000",
                       "true_stop_id": 2192
                   }
               ],
               "bustime": [
                   43500,
                   "12:05:00"
               ],
               "flag": true
           }
       ]
   }
   ```

   ​

   * `status`: The response state of the data
   * `data`
     * `detail`: The duration (in seconds) for one stop to another. (In order)
     * `totalDuration`: The total time for this journey (in minutes)
     * `stopsNum` The total stop number of the journey.
     * `stopInfo`: The detail information of all stops. (In order)
     * `bustime`: The bus arrive time of the bus.
     * `flag`: Boolean Value. False means if there is no bus of that day after the user picked time,  otherwise true.