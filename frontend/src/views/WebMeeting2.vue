<template>
<div>
  <div id="content" style="margin-top: -10%;" class="wrap">
    <!-- <section id="enter-wrap">
      <div id="create-wrap">
        <p>영상회의를 시작하시겠습니까?</p>
        <button id="btn-start">Start</button>
      </div>
      <div id="wait-wrap"></div>
    </section> -->

    <section id="video-wrap">
      <div>
        <video id="screen-video" style="display:none" autoplay playsinline></video>

        <video id="local-video"  autoplay playsinline></video>
        <video id="remote-video" autoplay playsinline></video>  
      </div>

      <div></div>
    </section>
  </div>
<!-- 하단 버튼 바 -->
<v-app class="bottomBtns">
    <v-snackbar
        v-model="snackbar"
        :timeout="timeout"
        color="#8A9EEB"
        top
      >
        {{ snackbartext }}

      </v-snackbar>
      <v-row style="margin-top: 320px; width: 80%; margin-left: 11%">
          <div v-if="myStatus==1">
          <v-btn v-if="createdYes" class="mx-2"  dark style="background-color:#2196F3; outline: 0; vertical-align:center; margin-top:6px;" @click="createRoom">
            방 생성
          </v-btn>

          <v-btn v-else class="mx-2"  dark style="background-color:green;  outline: 0; margin-top:6px;" @click="setClipboard">
            주소공유
          </v-btn>
          
          </div>
          <v-spacer></v-spacer>
         <v-btn class="mx-2" fab dark style="background-color:green;  outline: 0;" @click="shareScreen">
            <v-icon dark>
              mdi-monitor-share
            </v-icon>
        </v-btn>

          <v-btn v-if="this.cameraOn" class="mx-2" fab dark  @click="offCamera" style=" outline: 0;">
            <v-icon dark>
              mdi-video-outline
            </v-icon>
          </v-btn>
          <v-btn v-else class="mx-2" fab dark style="background-color:#E91E63;  outline: 0;" @click="onCamera">
          <v-icon dark>
            mdi-video-off-outline
          </v-icon>
        </v-btn>
        <v-btn v-if="this.voiceOn"  class="mx-2" fab dark @click="offVoice" style=" outline: 0;">
          <v-icon dark>
            mdi-microphone-outline
          </v-icon>
        </v-btn>
          <v-btn  v-else class="mx-2" fab dark style="background-color:#E91E63;  outline: 0;" @click="onVoice" >
            <v-icon dark>
              mdi-microphone-off
            </v-icon>
          </v-btn>


        <v-btn v-if="myStatus==1" class="mx-2" fab dark style="background-color:#E91E63;  outline: 0;"  @click="EndMeeting">
          <v-icon dark>
            mdi-phone-hangup
          </v-icon>
        </v-btn>


        <v-spacer></v-spacer>

        <v-btn v-if="myStatus=='1'" class="mx-2" dark style="background-color:green;  outline: 0; margin-top:6px;" @click.stop="drawer = !drawer">
              상담 일지 작성
          </v-btn>
    <v-navigation-drawer
      v-model="drawer"
      absolute
      right
      style="margin-right: 50px; margin-top: -300px; height: 500px;"
    >
      <v-list-item>
        <v-list-item-content>
          <v-list-item-title>상담 일지</v-list-item-title>
          <v-textarea
          v-model="content"
          class="mt-3"
          solo
          label="작성해주세요"
          height="400px"
        ></v-textarea>
        </v-list-item-content>
      </v-list-item>

    </v-navigation-drawer>
      </v-row>
    <v-snackbar
      v-model="EndSnackbar"
      color="#8A9EEB"
      top
      timeout="-1"
    >
      저장되었습니다 
      <template v-slot:action="{ attrs }">
        <v-btn
          text
          v-bind="attrs"
          @click="move()"
          
        >
          닫기
        </v-btn>
      </template>
    </v-snackbar>
        
</v-app>


</div>
</template>

<script>
import adapter from 'webrtc-adapter'
import db from '../../firebaseInit'
import axios from "axios";
import firebase from "firebase";
// const functions = require('firebase-functions');
// const admin = require('firebase-admin');
// admin.initializeApp();
if (adapter.browserDetails.browser == 'firefox') {
  adapter.browserShim.shimGetDisplayMedia(window, 'screen');
}


const configuration = {
  iceServers: [
    {
      urls: [
        'stun:stun1.l.google.com:19302',
        'stun:stun2.l.google.com:19302',
      ],
    },
  ],
  iceCandidatePoolSize: 10,
};

let peerConnection = null;
let localStream = null;

let remoteStream = null;
// // let roomDialog = null;
let roomId = null;

function registerPeerConnectionListeners() {
  peerConnection.addEventListener('icegatheringstatechange', () => {
    console.log(
        `ICE gathering state changed: ${peerConnection.iceGatheringState}`);
  });

  peerConnection.addEventListener('connectionstatechange', () => {
    console.log(`Connection state change: ${peerConnection.connectionState}`);
  });

  peerConnection.addEventListener('signalingstatechange', () => {
    console.log(`Signaling state change: ${peerConnection.signalingState}`);
  });

  peerConnection.addEventListener('iceconnectionstatechange ', () => {
    console.log(
        `ICE connection state change: ${peerConnection.iceConnectionState}`);
  });
}

function isEmpty(str){
    
    if(typeof str == "undefined" || str == null || str == "")
        return true;
    else
        return false ;
}



export default {

  mounted(){
    this.openUserMedia();
    // setInterval(()=>{
    //   console.log(this.toggleSwitch)
    //   this.toggleSwitch = window.$cookies.get("temp")
    // }, 1000);

    if(!isEmpty(location.href.split('#')[1])){
      this.joinRoomById();
    }
    // this.setRoomToken("Aaaa");
  },
  data(){
    return{
      snackbar : false,
      snackbartext : "내담자에게 링크를 공유했습니다. 잠시 대기해 주세요.",
      timeout: 3700,
      cameraOn : true,
      voiceOn : true,
      createdYes : true,
      drawer: false,
      myStatus : 0,
      content : "",
      counseldata: [],
      EndSnackbar: false,
    }
  },
  created(){
    let cookies = window.$cookies.get("user");
    this.myStatus = cookies.data.isuser;
    this.counseldata = this.$store.state.counselmeetingData;
  },
  methods:{    
    EndMeeting(){
        axios.post(process.env.VUE_APP_API_URL+"counsel/counselinsert",{
            "counselReservation_pk" : this.counseldata.counselReservation_pk,
            "counsel_startdate": this.counseldata.counsel_startdate,
            "counsel_enddate" : this.counseldata.counsel_enddate,
            "user_pk" : this.counseldata.user_pk,
            "counselor_pk" : this.counseldata.counselor_pk,
            "counsel_fee" : this.counseldata.counsel_fee,
            "counsel_detail" : this.content
       }).then((data) => {
        this.detail = data.data.data
        this.EndSnackbar = true;

        
      }).catch((er)=>{
        console.log(er)
      });       
    },
    move(){
      this.EndSnackbar = false;
      this.$router.push("/");

    },
    onCamera(){
      this.cameraOn = true;
      localStream.getVideoTracks()[0].enabled = true;
    },
    offCamera(){
      this.cameraOn = false;
      localStream.getVideoTracks()[0].enabled = false;

    },
    onVoice(){
      this.voiceOn = true;
      localStream.getAudioTracks()[0].enabled = true;


    },
    offVoice(){
      this.voiceOn = false;
      localStream.getAudioTracks()[0].enabled = false;

    },
    setRoomToken(code){
      location.hash = '#' + code;
    },
    setClipboard(){
        const link = location.href + "  이 링크로 접속해 주세요.";
        console.log(link);
        let name = window.$cookies.get("user").data.counselor_name
        let room = this.$store.state.counselmeetingData.user_pk + "|" + window.$cookies.get("user").data.counselor_pk;
        const message = {
          text: link,
          username: name,
        };
        firebase
          .database()
          .ref("messages")
          .child(room)
          .push(message);
        this.snackbar = true;
        
    },

   async openUserMedia(){
    const stream = await navigator.mediaDevices.getUserMedia(
      {
        video : true,
        audio : true
      }
    );

    document.querySelector('#local-video').srcObject = stream;
    localStream = stream;

  
    remoteStream = new MediaStream();
    document.querySelector('#remote-video').srcObject = remoteStream;

   
  },
  async createRoom() {
    // document.querySelector('#createBtn').disabled = true;
    const roomRef = await db.collection('rooms').doc();
    // console.log(roomRef)
    // console.log('Create PeerConnection with configuration: ', configuration);
    peerConnection = new RTCPeerConnection(configuration);
    registerPeerConnectionListeners();

    localStream.getTracks().forEach(track => {
      peerConnection.addTrack(track, localStream);
    });
    
    this.createdYes = !this.createdYes


    // Code for collecting ICE candidates below
    const callerCandidatesCollection = roomRef.collection('callerCandidates');

    peerConnection.addEventListener('icecandidate', event => {
      if (!event.candidate) {
        console.log('Got final candidate!');
        return;
      }
      console.log('Got candidate: ', event.candidate);
      callerCandidatesCollection.add(event.candidate.toJSON());
    });
    // Code for collecting ICE candidates above

    // Code for creating a room below
    const offer = await peerConnection.createOffer();
    await peerConnection.setLocalDescription(offer);
    console.log('Created offer:', offer);

    const roomWithOffer = {
      'offer': {
        type: offer.type,
        sdp: offer.sdp,
      },
    };
    await roomRef.set(roomWithOffer);
    roomId = roomRef.id;
    console.log(`New room created with SDP offer. Room ID: ${roomRef.id}`);
    // document.querySelector('#currentRoom').innerText = `Current room is ${roomRef.id} - You are the caller!`;
    // Code for creating a room above

    await peerConnection.addEventListener('track', event => {
      console.log('Got remote track:', event.streams[0]);
      event.streams[0].getTracks().forEach(track => {
        console.log('Add a track to the remoteStream:', track);
        remoteStream.addTrack(track);
      });
    });

    // Listening for remote session description below
    await roomRef.onSnapshot(async snapshot => {
      const data = snapshot.data();
      if (!peerConnection.currentRemoteDescription && data && data.answer) {
        console.log('Got remote description: ', data.answer);
        const rtcSessionDescription = new RTCSessionDescription(data.answer);
        await peerConnection.setRemoteDescription(rtcSessionDescription);
      }
    });
    // Listening for remote session description above

    // Listen for remote ICE candidates below
    await roomRef.collection('calleeCandidates').onSnapshot(snapshot => {
      snapshot.docChanges().forEach(async change => {
        if (change.type === 'added') {
          let data = change.doc.data();
          console.log(`Got new remote ICE candidate: ${JSON.stringify(data)}`);
          await peerConnection.addIceCandidate(new RTCIceCandidate(data));
          document.querySelector('body').classList.add("connected");

        }
      });
    });
    console.log(roomId)
    this.setRoomToken(roomId);
    this.createdYes = false;
  },


  async joinRoomById(){
    setTimeout(async () => {

    const roomRef = db.collection('rooms').doc(location.href.split('#')[1]);
    const roomSnapshot = await roomRef.get();
    console.log(roomRef)

    if (roomSnapshot.exists) {
      console.log('Create PeerConnection with configuration: ',  );
      peerConnection = new RTCPeerConnection(configuration);
      registerPeerConnectionListeners();
      localStream.getTracks().forEach(track => {
        peerConnection.addTrack(track, localStream);
      });

      // Code for collecting ICE candidates below
      const calleeCandidatesCollection = await roomRef.collection('calleeCandidates');
      peerConnection.addEventListener('icecandidate', event => {
        if (!event.candidate) {
          console.log('Got final candidate!');
          return;
        }
        console.log('Got candidate: ', event.candidate);
        calleeCandidatesCollection.add(event.candidate.toJSON());
      });
      // Code for collecting ICE candidates above

      await peerConnection.addEventListener('track', event => {
        console.log('Got remote track:', event.streams[0]);
        event.streams[0].getTracks().forEach(track => {
          console.log('Add a track to the remoteStream:', track);
          remoteStream.addTrack(track);
        });
      });

      // Code for creating SDP answer below
      const offer = roomSnapshot.data().offer;
      console.log('Got offer:', offer);
      await peerConnection.setRemoteDescription(new RTCSessionDescription(offer));
      const answer = await peerConnection.createAnswer();
      console.log('Created answer:', answer);
      await peerConnection.setLocalDescription(answer);

      const roomWithAnswer = {
        answer: {
          type: answer.type,
          sdp: answer.sdp,
        },
      };
      await roomRef.update(roomWithAnswer);
      // Code for creating SDP answer above

      // Listening for remote ICE candidates below
      await roomRef.collection('callerCandidates').onSnapshot(snapshot => {
        snapshot.docChanges().forEach(async change => {
          if (change.type === 'added') {
            let data = change.doc.data();
            console.log(`Got new remote ICE candidate: ${JSON.stringify(data)}`);
            await peerConnection.addIceCandidate(new RTCIceCandidate(data));
            document.querySelector('body').classList.add("connected");

            // window.$cookies.set("temp","tempV")
            // this.toggleSwitch = window.$cookies.get("temp")
            // console.log(this.toggleSwitch)
          }
        });
      });
      // Listening for remote ICE candidates above
    }
    this.dialog=false;
    // document.querySelector('#remote-video').style.dispaly = 'block';
    }, 1000);
  },


  shareScreen(){
    navigator.mediaDevices.getDisplayMedia({
      video:true
    })
    .then(this.screenShareHandleSuccess)

  },

  
  async screenShareHandleSuccess(stream){

    const roomRef = db.collection('rooms').doc(location.href.split('#')[1]);
    const roomRef2 = await db.collection('rooms').doc();

    const roomSnapshot = await roomRef.get();
    console.log(roomRef)

    if (roomSnapshot.exists) {
      console.log('Create PeerConnection with configuration: ',  );
      peerConnection = new RTCPeerConnection(configuration);
      registerPeerConnectionListeners();
      localStream.getTracks().forEach(track => {
        peerConnection.addTrack(track, localStream);
      });

      // Code for collecting ICE candidates below
      const calleeCandidatesCollection = roomRef.collection('calleeCandidates');

      peerConnection.addEventListener('icecandidate', event => {
        if (!event.candidate) {
          console.log('Got final candidate!');
          return;
        }
        console.log('Got candidate: ', event.candidate);
        calleeCandidatesCollection.add(event.candidate.toJSON());

      });
      // Code for collecting ICE candidates above

      peerConnection.addEventListener('track', event => {
        console.log('Got remote track:', event.streams[0]);
        event.streams[0].getTracks().forEach(track => {
          console.log('Add a track to the remoteStream:', track);
          remoteStream.addTrack(track);
        });
      });

      // Code for creating SDP answer below
      const offer = roomSnapshot.data().offer;
      console.log('Got offer:', offer);
      await peerConnection.setRemoteDescription(new RTCSessionDescription(offer));
      const answer = await peerConnection.createAnswer();
      console.log('Created answer:', answer);
      await peerConnection.setLocalDescription(answer);

      const roomWithAnswer = {
        answer: {
          type: answer.type,
          sdp: answer.sdp,
        },
      };
      await roomRef.update(roomWithAnswer);
      // Code for creating SDP answer above
      await roomRef2.onSnapshot(async snapshot => {
        const data = snapshot.data();
        if (!peerConnection.currentRemoteDescription && data && data.answer) {
          console.log('Got remote description: ', data.answer);
          const rtcSessionDescription = new RTCSessionDescription(data.answer);
          await peerConnection.setRemoteDescription(rtcSessionDescription);
        }
      });
      // Listening for remote ICE candidates below
      // 
      // Listening for remote ICE candidates above
    
      await roomRef.collection('calleeCandidates').onSnapshot(snapshot => {
      snapshot.docChanges().forEach(async change => {
        if (change.type === 'added') {
          let data = change.doc.data();
          console.log(`Got new remote ICE candidate: ${JSON.stringify(data)}`);
          await peerConnection.addIceCandidate(new RTCIceCandidate(data));
          document.querySelector('#screen-video').srcObject = stream;
          document.querySelector('body').classList.add("shared");
          stream.getVideoTracks()[0].addEventListener('ended', () => {
            document.querySelector('body').classList.remove("shared");
          })
        }
      });
    });




  }



  },
  
  

}
}

</script>

<style scoped>
 /* body {overflow:hidden} */

.wrap {
  margin-top: 0;
  position: relative;
  font-size: 1.2em;
  text-align: center;
}

.wrap p {
  font-size: 1.25em;
}

.wrap button {
  margin-top: 20px;
  min-width: 80px;
  vertical-align: top;
}

.room-info {
  vertical-align: top;
}

/********************************************
  Below room style
*********************************************/
video {
  margin: 0 0 0 0;
  width: 100%;
  z-index: 1;
  background: #222;
  border: solid 1px #fff;
  transition: all 0.6s ease-out;
  height : 100%
}

video.effect {
  transform: scale(1, 1);
}

#video-wrap {
  /* display: none; */
  position: relative;
  margin: 0 auto;
  min-height: 620px;
}

#video-wrap .buttons {
  position: absolute;
  bottom: 0;
}

#local {
  position: absolute;
  top: 4%;
  right: 2%;
  width: 340px;
  height: 220px;
  border: solid 1px #fff;
}

#remote-video{
  display : none;

}

#screen-video{
  display: none;
}

.shared #local-video{
  top: 2px;
  left: 2px !important;
  width: 15% !important;
  height : 20% !important;
  border: solid 1px #fff;
  z-index: 2;
}
.shared #remote-video{
  top: 20% !important;
  left: 2px !important;
  width: 15% !important;
  height : 20% !important;
  border: solid 1px #fff;
  z-index: 2;
}
.shared #screen-video{
  display : block !important;
  position: absolute;
  top: 0;
  left: 0;
}

#local-video {
  position: absolute;
  top: 0;
  left: 0;
  /* height: 100%; */
}


#share-wrap {
  display: none;
  margin: 10px 0;
}

.room #enter-wrap,
.connected #create-wrap,
.connected #wait-wrap {
  display: none;
}
.connected #local-video {
  top: 2px;
  left: 2px !important;
  width: 15% !important;
  height : 20% !important;
  border: solid 1px #fff;
  z-index: 2;
}

.connected #remote-video{
  display : block !important;
  position: absolute;
  top: 0;
  left: 0;
}
.room #share-wrap {
  display: block;
}

.room #wait-wrap {
  display: none;
}

.room #video-wrap {
  display: block;
}

.room #content {
  padding-top: 30px;
}

.bottomBtns {
  bottom : 0;
  width : 100vw;
  height: 10%;
  position : fixed;
  background-color: #fff;
  align-items :center;
  text-align: center;
  margin-bottom: 0;
  border-top: 4px blue;
  z-index : 3;
}

.micandvoice{
  vertical-align : center;
  margin : 0 0;
  display: inline-block;
}
</style>