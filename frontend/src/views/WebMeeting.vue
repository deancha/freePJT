<template>
<v-app>
        <h1> 
            여기는 WebMeeting.vue
        </h1>
      <div >
      
      <v-btn
        class="ma-2"
        color="secondary"
        id="cameraBtn" @click="openUserMedia"
      >
        비디오 시작
      </v-btn>

      <v-btn
        color="blue-grey"
        class="ma-2 white--text"
         id="createBtn" @click="createRoom"
      >
        방 생성
        <v-icon
          right
          dark
        >
          mdi-cloud-upload
        </v-icon>
      </v-btn>

      <!-- //////////////////////////-->
        <v-dialog
          v-model="dialog"
          persistent
          max-width="290"
        >
          <template v-slot:activator="{ on, attrs }">
            <v-btn
              color="primary"
              dark
              v-bind="attrs"
              v-on="on"
            >
              <!-- id="joinBtn" @click="joinRoom" -->
              방 들어가기

            </v-btn>
          </template>
          <v-card>
            <v-card-title class="headline">
              Room ID를 입력해주세요
            </v-card-title>

            <v-text-field
            v-model="room_id"
            label="Room ID"
            required
            outlined
            dense
          ></v-text-field>

            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn
                color="green darken-1"
                text
                @click="dialog = false"
              >
                취소
              </v-btn>
              <v-btn
                color="green darken-1"
                text
                id="confirmJoinBtn"
                @click="joinRoomById"
              >
                입장  
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>

      

      <v-btn
        class="ma-2"
        color="info"
        id="hangupBtn" @click="hangUp"
      >
        Hang Up
        
      </v-btn>

</div>
<div>
    <span id="currentRoom"></span>
</div>
<div id="videos">
    <video id="localVideo" muted autoplay playsinline></video>
    <video id="remoteVideo" autoplay playsinline></video>
</div>

        <!-- <video id="gum-local" autoplay playsinline></video> -->
        <!-- <v-btn id="showVideo" color="info" @click="getUserMedia">카메라</v-btn> -->
        <!-- <v-btn id="startButton" color="info" @click="shareScreen">화면공유</v-btn> -->

</v-app>
</template>

<script>
import adapter from 'webrtc-adapter'
import db from '../../firebaseInit'

if (adapter.browserDetails.browser == 'firefox') {
  adapter.browserShim.shimGetDisplayMedia(window, 'screen');
}

// mdc.ripple.MDCRipple.attachTo(document.querySelector('.mdc-button'));


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
// let roomDialog = null;
let roomId = null;

// roomDialog = new mdc.dialog.MDCDialog(document.querySelector('#room-dialog'));




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


export default {
    name : "",
    data(){
      return{
        dialog: false,
        room_id : "",
        isCameraBtnDisabled : false,
        isCreateBtnDisabled : false,
      }
    },
    methods :{
        

        // async shareScreen(){
        //   navigator.mediaDevices.getDisplayMedia({video: true})
        //   .then(handleSuccess, handleError);
        // },

        async createRoom() {
          document.querySelector('#createBtn').disabled = true;
          const roomRef = await db.collection('rooms').doc();
          console.log(roomRef)
          console.log('Create PeerConnection with configuration: ', configuration);
          peerConnection = new RTCPeerConnection(configuration);
          registerPeerConnectionListeners();

          localStream.getTracks().forEach(track => {
            peerConnection.addTrack(track, localStream);
          });

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
          document.querySelector(
              '#currentRoom').innerText = `Current room is ${roomRef.id} - You are the caller!`;
          // Code for creating a room above

          peerConnection.addEventListener('track', event => {
            console.log('Got remote track:', event.streams[0]);
            event.streams[0].getTracks().forEach(track => {
              console.log('Add a track to the remoteStream:', track);
              remoteStream.addTrack(track);
            });
          });

          // Listening for remote session description below
          roomRef.onSnapshot(async snapshot => {
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
              }
            });
          });
        },

        async  joinRoomById(){
          const roomRef = db.collection('rooms').doc(this.room_id);
          const roomSnapshot = await roomRef.get();
          console.log(this.room_id)
          console.log(roomRef)

          if (roomSnapshot.exists) {
            console.log('Create PeerConnection with configuration: ', configuration);
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

            // Listening for remote ICE candidates below
            roomRef.collection('callerCandidates').onSnapshot(snapshot => {
              snapshot.docChanges().forEach(async change => {
                if (change.type === 'added') {
                  let data = change.doc.data();
                  console.log(`Got new remote ICE candidate: ${JSON.stringify(data)}`);
                  await peerConnection.addIceCandidate(new RTCIceCandidate(data));
                }
              });
            });
            // Listening for remote ICE candidates above
          }
          this.dialog=false;

        },
        

        async openUserMedia(){
          const stream = await navigator.mediaDevices.getUserMedia(
            {
              video : true,
              audio : true
            }
          );

          document.querySelector('#localVideo').srcObject = stream;
          localStream = stream;
          remoteStream = new MediaStream();
          document.querySelector('#remoteVideo').srcObject = remoteStream;

          // document.querySelector('#cameraBtn').disabled = true;
          // document.querySelector('#joinBtn').disabled = false;
          // document.querySelector('#createBtn').disabled = false;
          // document.querySelector('#hangupBtn').disabled = false;
        },

        async hangUp(){
          const tracks = document.querySelector('#localVideo').srcObject.getTracks();
          tracks.forEach(track=>{
            track.stop();
          });

          if(remoteStream){
            remoteStream.getTracks().forEach(track => track.stop());
          }

          if(peerConnection){
            peerConnection.close();
          }

          document.querySelector('#localVideo').srcObject = null;
          document.querySelector('#remoteVideo').srcObject = null;
          // document.querySelector('#cameraBtn').disabled = false;
          // document.querySelector('#joinBtn').disabled = true;
          // document.querySelector('#createBtn').disabled = true;
          // document.querySelector('#hangupBtn').disabled = true;
          document.querySelector('#currentRoom').innerText = '';

          if(roomId){
            const roomRef = db.collection('rooms').doc(roomId);
            const calleeCandidates = await roomRef.collection('calleeCandidates').get();
            calleeCandidates.forEach(async candidate => {
              await candidate.delete();
            });

            const callerCandidates = await roomRef.collection('callerCandidates').get();
            callerCandidates.forEach(async candidate =>{
              await candidate.delete();
            });
            await roomRef.delete();
          }

          document.location.reload(true);
        },
        
    }

}
</script>

<style scoped>


</style>