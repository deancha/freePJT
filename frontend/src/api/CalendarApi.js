import BASE_URL from '../main'

const axios = require('axios');

const applyCounsel = (data,callback,errorCallback)=>{
    axios({
        method: 'post',
        url: BASE_URL + 'counsel/counselReservationinsert',
        data : data,
      })
      .then(function(response){
        callback(response.data);
      })
      .catch((error) => {
        errorCallback(error);
      })
}

const getCounsel = (data,callback,errorCallback)=>{
    axios({
      method: 'get',
      url: BASE_URL + 'counsel/getmycounsel/'+data,
    })
    .then(function(response){
      callback(response.data.data.listtwo);
      console.log(response.data.data.listtwo);
    })
    .catch((error) => {
      errorCallback(error);
    })
}

const CalendarApi = {
  applyCounsel:(data,callback,errorCallback)=>applyCounsel(data,callback,errorCallback),
  getCounsel:(data,callback,errorCallback)=>getCounsel(data,callback,errorCallback),
}

export default CalendarApi