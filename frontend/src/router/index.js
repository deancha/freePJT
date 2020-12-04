import Vue from 'vue'
import VueRouter from 'vue-router'
import WebMeeting from '../views/WebMeeting.vue'
import WebMeeting2 from '../views/WebMeeting2.vue'

import Home from '../views/HomePage.vue'
import ConsultantSchedule from '../views/ConsultantSchedule.vue'
import SignIn from '../views/SignInPage.vue'
import SignUp from '../views/SignUpPage.vue'
import SignUpCounselor from '../views/SignUpCounselorPage.vue'
import SearchConsultant from '../views/SearchConsultant.vue'
import KakaoCheck from '../views/KakaoCheckPage.vue'
import Survey from '../views/SurveyPage.vue'
import SelectUser from '../views/SelectUserPage.vue'
// import Maker from '../components/Home/Maker.vue'
import MyPage from '../views/MyPage.vue'
import Test from '../views/Test.vue'

import SelfDiagResult from '../views/SelfDiagResult.vue'

import UploadImg from '../components/User/UploadImg.vue'
import Chat from '../components/SeacrhConsultant/Chat.vue'

import CounselorUpdate from '../components/MyInfo/CounselorUpdate.vue'
import UserUpdate from '../components/MyInfo/UserUpdate.vue'


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/consultantSchedule',
    name: 'About',
    component: ConsultantSchedule
  },
  {
    path: '/signin',
    name: 'SignIn',
    component: SignIn
  },
  {
    path: '/signupcounselor',
    name: 'SignUpCounselor',
    component: SignUpCounselor
  },
  {
    path: '/signup',
    name: 'SignUp',
    component: SignUp
  },
  {
    path:'/webmeeting',
    name: 'WebMeeting',
    component: WebMeeting,
  },
  {
    path:'/searchConsultant',
    name: 'searchConsultant',
    component: SearchConsultant,
  },
  {
    path:'/kakaocheck',
    name: 'KakaoCheck',
    component: KakaoCheck,
  },
  {
    path:'/uploadimg',
    name:'UploadImg',
    component: UploadImg,
  },
  {
    path:'/chat',
    name:'Chat',
    component: Chat,
    
  },
  {
    path:'/survey',
    name: 'Survey',
    component: Survey,
  },
  {
    path:'/selectuser',
    name: 'SelectUser',
    component: SelectUser,
  },
  {
    path: '/selfDiagResult',
    name: 'SelfDiagResult',
    component: SelfDiagResult,
    props: true,
  },


  {
    path:'/uploadimg',
    name:'UploadImg',
    component: UploadImg,
  },
  {
    path:'/chat',
    name:'Chat',
    component: Chat,
  },
  {
    path: '/selfDiagResult',
    name: 'SelfDiagResult',
    component: SelfDiagResult,
  },
  {
    path: '/mypage',
    name: 'MyPage',
    component: MyPage,
    props: true,
  },
  {
    path: '/counselorupdate',
    name: 'CounselorUpdate',
    component: CounselorUpdate,
    props: true,
  },
  {
    path: '/userupdate',
    name: 'UserUpdate',
    component: UserUpdate,
    props: true,
  },
  {
    path: '/test',
    name: 'Test',
    component: Test,
  
  },
  {
    path:'/webmeeting2/',
    name: 'WebMeeting2',
    component: WebMeeting2,
  },
  
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
