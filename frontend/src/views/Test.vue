<template>
<div id="videos">
    <video id="localVideo" muted autoplay playsinline></video>
    <video id="remoteVideo" autoplay playsinline></video>
</div>
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
// let roomId = null;

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
    created(){
        window.
        this.tt();
        this.openUserMedia();
        this.joinRoomById("YLcOPWsBUDSDavdnOZs3");
    },  
    methods:{
        tt(){
            console.log("222")
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
        async  joinRoomById(roomidid){
          const roomRef = db.collection('rooms').doc(roomidid);
          const roomSnapshot = await roomRef.get();
          console.log(roomidid)
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
    },

}
</script>

<style>

</style>