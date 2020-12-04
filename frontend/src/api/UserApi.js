import BASE_URL from '../main'

const axios = require('axios');


const Logout = (data,callback,errorCallback) => {
    axios({
        method: 'get',
        url: BASE_URL + 'user/user/'+data,
    })
    .then(function(response){
      callback(response.data);
    })
    .catch((error) => {
      errorCallback(error);
      //에러시 사용자에게 알리기
    });
  }

const SignIn = (data,callback,errorCallback) =>{
    axios({
      method: 'post',
      url: BASE_URL + 'user/userlogin',
      data : data,
    })
    .then(function(response){
      callback(response.data);
    })
    .catch((error) => {
      errorCallback(error);
    })
}

const SignUp = (data,callback,errorCallback) =>{
  axios({
    method: 'post',
    url: BASE_URL + 'user/userlist',
    data : data,
  })
  .then(function(response){
    callback(response.data);
  })
  .catch((error) => {
    errorCallback(error);
  })
}
const SignUpCounselor = (data,callback,errorCallback) =>{
  axios({
    method: 'post',
    url: BASE_URL + 'counselor/counselorlist',
    data : data,
  })
  .then(function(response){
    callback(response.data);
  })
  .catch((error) => {
    errorCallback(error);
  })
}
const AddCounselPart = (data,callback,errorCallback) =>{
  axios({
    method: 'post',
    url: BASE_URL + 'counselor/counselormajorlist',
    data : data,
  })
  .then(function(response){
    callback(response.data);
  })
  .catch((error) => {
    errorCallback(error);
  })
}
const EmailValidation = (data,callback,errorCallback) =>{
  axios({
    method: 'post',
    url: BASE_URL + 'emailvalidation',
    data : data,
  })
  .then(function(response){
    callback(response.data);
  })
  .catch((error) => {
    errorCallback(error);
  })
}

const KakaoLogin = (callback,errorCallback) =>{
  axios({
    method: 'get',
    url: BASE_URL + 'account/login/kakao',

  })
  .then(function(response){
    callback(response.data);
  })
  .catch((error) => {
    errorCallback(error);
  })
}

const UserApi = {
  Logout:(data,callback,errorCallback)=>Logout(data,callback,errorCallback),
  SignIn:(data,callback,errorCallback)=>SignIn(data,callback,errorCallback),
  SignUp: (data, callback, errorCallback) => SignUp(data, callback, errorCallback),
  SignUpCounselor: (data, callback, errorCallback) => SignUpCounselor(data, callback, errorCallback),
  AddCounselPart:(data,callback,errorCallback)=>AddCounselPart(data,callback,errorCallback),
  KakaoLogin:(data,callback,errorCallback)=>KakaoLogin(data,callback,errorCallback),
  EmailValidation:(data,callback,errorCallback)=>EmailValidation(data,callback,errorCallback),


}

export default UserApi