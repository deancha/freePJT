import BASE_URL from '../main'

const axios = require('axios');

const requestCounselorList = (callback,errorCallback)=>{
    axios({
        method: 'get',
        url: BASE_URL + 'counselor/counselorlist',
      })
      .then(function(response){
        console.log(response)
        callback(response.data.data);
      })
      .catch((error) => {
        errorCallback(error);
      })
}

const getreviewcounselor = (data,callback,errorCallback)=>{
  axios({
      method: 'get',
      url: BASE_URL + 'review/getreviewcounselor/'+data,
    })
    .then(function(response){
      console.log(response)
      callback(response.data.data);
    })
    .catch((error) => {
      errorCallback(error);
    })
}

const counselormajorlist = (data,callback,errorCallback)=>{
  axios({
      method: 'get',
      url: BASE_URL + 'counselor/counselormajor/'+data,
    })
    .then(function(response){
      console.log(response)
      callback(response.data.data);
    })
    .catch((error) => {
      errorCallback(error);
    })
}

const CounselorApi = {
    requestCounselorList:(callback,errorCallback)=>requestCounselorList(callback,errorCallback),
    getreviewcounselor:(data,callback,errorCallback)=>getreviewcounselor(data,callback,errorCallback),
    counselormajorlist:(data,callback,errorCallback)=>counselormajorlist(data,callback,errorCallback),
}

export default CounselorApi