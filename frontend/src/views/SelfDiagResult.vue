<template>
    <div>
    <TopHeader></TopHeader>
    <Header></Header>

      <v-app>
        <v-card
          class="mx-auto my-12"
        >

          <v-card-title>당신의 우울증 점수는?</v-card-title>
          
          <div v-if="result<=15"> 
          <v-card-text class="text-center">


          <div style="margin-top:10px;"><span style="font-size:60px;color:#f57c00;"> {{result}}</span>점</div>
            <svg class="fine" width="44px" height="44px" viewBox="0 0 44 44" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                <g id="fine-emotion" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
                    <g id="fine">
                        <circle id="body" fill="#1988E3" cx="22" cy="22" r="22"></circle>
                        <g class="matrix" transform="translate(22.000000, 32.000000)">
                        <g class="face-container">
                        <g class="face" transform="translate(-9, -12)">
                            <g class="face-upAndDown">
                            <g class="eyes">
                            <ellipse class="right-eye" fill="#2C0E0F" cx="16.0941176" cy="1.75609756" rx="1.90588235" ry="1.75609756"></ellipse>
                            <ellipse class="left-eye" fill="#2C0E0F" cx="1.90588235" cy="1.75609756" rx="1.90588235" ry="1.75609756"></ellipse></g>
                            <path d="M6.18823529,4.90499997 C6.18823529,5.95249999 7.48721095,7 9.08957864,7 C10.6919463,7 11.990922,5.95249999 11.990922,4.90499997" id="mouth" stroke="#2C0E0F" stroke-linecap="round" stroke-linejoin="round"></path>
                            </g>
                        </g>
                        </g>
                    </g>
                    </g>
                </g>
            </svg>
          </v-card-text>

          <v-divider class="mx-4"></v-divider>
          
          <v-card-title >우울하지 않은 상태시군요!</v-card-title>

          <v-card-text class="text-center">

            
            일상생활을 담대하게 보내고 있는 당신!<br>
            전문의 상담은 필요없다고 느껴집니다.<br>
            다만, 우울한 때가 생길 때 가벼운 마음으로 상담을 받아 보시는 것도 좋을 것 같아요:)
            
          </v-card-text>

        </div> 
            
            

        
        <div v-else-if="result<=20"> 
          <v-card-text class="text-center">
          
          <div style="margin-top:10px;"><span style="font-size:60px;color:#f57c00;">{{result}}</span>점</div>
            <svg class="happy" width="44px" height="44px" viewBox="0 0 44 44" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                <g id="Happy" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd" transform="translate(0, 0)">
                    <circle id="Body" fill="#248C37" cx="22" cy="22" r="22"></circle>
                    <g class="scaleFace">
                    <g class="face">  
                        <ellipse id="Eye-right" fill="#2C0E0F" cx="29.0875" cy="21.75" rx="1.89926471" ry="1.75"></ellipse>
                        <ellipse id="Eye-left" fill="#2C0E0F" cx="14.8992647" cy="21.75" rx="1.89926471" ry="1.75"></ellipse>
                        <path d="M21.8941176,27.8819633 C24.8588235,27.8819632 25.4941176,25.5404999 25.4941176,24.5648901 C25.4941176,23.5892803 24.4352941,23.9795242 22.1058824,23.9795242 C19.7764706,23.9795242 18.2941176,23.5892803 18.2941176,24.5648901 C18.2941176,25.5404999 18.9294118,27.8819633 21.8941176,27.8819633 Z" id="Mouth" fill="#2C0E0F"></path>
                        <ellipse id="Tung" fill="#E23D18" cx="21.8941176" cy="26.4390244" rx="1.69411765" ry="0.780487805"></ellipse>
                    </g>  
                </g>
                </g>
            </svg>
          </v-card-text>
          <v-divider class="mx-4"></v-divider>
          <v-card-title >가벼운 우울상태입니다</v-card-title>

          <v-card-text class="text-center">            
            일생생활에 지장이 없는 우울함을 갖고 있습니다.<br/>
            살짝 우울한 마음이 보이기는 하지만 건강적으로는 괜찮은 것 같습니다.<br/>
            우울한 기분이 계속 지속된다면 상담을 받아보시는 것을 추천드립니다.
          </v-card-text>
        </div> 
        
        <div v-else-if="result<=24">
          <v-card-text class="text-center">
          
          <div style="margin-top:10px;"><span style="font-size:60px;color:#f57c00;"> {{result}}</span>점</div>
            
            <svg class="neutral" width="44px" height="44px" viewBox="0 0 44 44" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                <g>
                    <circle id="body" fill="#F9AC1B" cx="22" cy="22" r="22"></circle>
                    <g class="face">
                    <g transform="translate(13.000000, 20.000000)" fill="#2C0E0F">
                        <g class="mouth">
                            <g transform="translate(9, 5)" >
                            <rect x="-2" y="0" width="4" height="2" rx="2"></rect>
                            </g>
                        </g>
                        <ellipse class="right-eye" cx="16.0941176" cy="1.75" rx="1.90588235" ry="1.75"></ellipse>
                        <ellipse class="left-eye" cx="1.90588235" cy="1.75" rx="1.90588235" ry="1.75"></ellipse>
                    </g>
                    </g>
                </g>
            </svg>

          </v-card-text>
          
          <v-divider class="mx-4"></v-divider>

          <v-card-title >많이 우울한 상태입니다</v-card-title>

          <v-card-text class="text-center">            
            많이 우울한 상태시군요<br/>
            공허한 마음이 날이 시간이 지나도 풀리지 않는다면 전문의 상담받는 것을 추천드려요<br/>
            마음이 너무 불안하고 허전하다면 주저하지 마세요<br/>
            빠른 상담이 당신을 편안하게 해줄 수 있을지도 몰라요
          </v-card-text>
        </div> 
        
        <div v-else>

          <v-card-text class="text-center">
          
          <div style="margin-top:10px;"><span style="font-size:60px;color:#f57c00;"> {{result}}</span>점</div>
            
            <svg class="sad" width="44px" height="44px" viewBox="0 0 44 44" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                <g id="sad" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd" transform="translate(0, 0)">
                    <circle id="body" fill="#E23D18" cx="22" cy="22" r="22"></circle>
                    <g id="face" transform="translate(13.000000, 20.000000)">
                        <g class="face">
                        <path d="M7,4 C7,5.1045695 7.8954305,6 9,6 C10.1045695,6 11,5.1045695 11,4" class="mouth" stroke="#2C0E0F" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" transform="translate(9.000000, 5.000000) rotate(-180.000000) translate(-9.000000, -5.000000) "></path>
                        <ellipse class="right-eye" fill="#2C0E0F" cx="16.0941176" cy="1.75609756" rx="1.90588235" ry="1.75609756"></ellipse>
                        <ellipse class="left-eye" fill="#2C0E0F" cx="1.90588235" cy="1.75609756" rx="1.90588235" ry="1.75609756"></ellipse>
                    </g>
                    </g>
                </g>
            </svg>

         </v-card-text>
          
          <v-divider class="mx-4"></v-divider>

          <v-card-title >심한 우울상태입니다</v-card-title>

          <v-card-text class="text-center">           
            시간이 지나도 우울한 감정이 계속되고 있죠?<br/>
            전문의 상담이 필요한 때입니다!<br/>
            전문의 상담을 통해 고민을 공유하고 하루 빨리 우울증을 치료하세요.<br/>
            우울증은 빨리 치료하면 2개월이면 완치가 가능합니다!<br/>
          </v-card-text>
        </div>
          
        </v-card>
        
        
        <div class="text-center">
            <v-btn depressed class="ma-2" color="success" to = "/">메인화면</v-btn>
            <v-btn depressed class="ma-2 " color="primary" to = "/searchConsultant">심리상담 받아보실래요?</v-btn>

        </div>
        </v-app>
        <Footer></Footer>

    </div>
</template>

<script>
import TopHeader from '../components/Home/TopHeader.vue'
import Header from '../components/Home/Header.vue'
import Footer from '../components/Home/Footer.vue'

export default {
    props:{
      result:{
        type: Number,
        default: 0
    }},

    plugins: [
+   require('postcss-nested'),
    require('autoprefixer')
  ],
   components: {
    Header,
    TopHeader,
    // Count_Section,
    Footer
  },
}
</script>

<style scoped>

@use postcss-nested;
@use postcss-simple-vars;

html, body {
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}

svg {
  margin: 10px;
  width: 10em;
  height: 10em;
}

svg.happy {

  .face {
    animation: upAndDown 0.8s ease infinite;  
  }
  
  .scaleFace {
    transform-origin: 35px 20px;
    transform: rotate(12deg);
  }

}

svg.sad {
  width: 10em;
  height: 10em;
  
  .face {
    animation: leftToRight 0.4s linear infinite alternate-reverse;
  }
  
  .left-eye, .right-eye {
    opacity: 1;
    transform-origin: 0 1px;
    animation: 
      blink 3s linear infinite,
      blinkSqueeze 3s linear infinite;
  }
  
  .mouth {
    padding-top: 20px;
  }
}

svg.neutral {
  .face {
    animation: upAndDown 6s ease infinite; 
  }
  
  .left-eye, .right-eye {
    opacity: 1;
    transform-origin: 0 1px;
    animation: 
      blink 3s linear infinite,
      blinkSqueezeTwice 3s linear infinite;
    animation-delay: 1s;
  }
  .mouth {
    animation: scaleX 2s ease infinite alternate-reverse;
  }
}

svg.fine {
  .face-container {
    animation: rotateLeftToRight 3s infinite;
  }
  
  .face-upAndDown {
    animation: fineUpAndDown 3s infinite;
  }
  
  .left-eye, .right-eye {
    opacity: 1;
    transform-origin: 0 1px;
    animation: 
      blink 3s linear infinite,
      blinkSqueeze 3s linear infinite;
  }
}

@keyframes rotateLeftToRight {
  0% { transform: rotate(15deg); }
  50% { transform: rotate(-15deg); }
  100% { transform: rotate(15deg); }
}

@keyframes fineUpAndDown {
  0% { transform: translate(0, 0); }
  25% { transform: translate(0, -1px); }
  50% { transform: translate(0, 0); }
  75% { transform: translate(0, -1px); }
  100% { transform: translate(0, 0); }
}

@keyframes upAndDown {
  0% { transform: translate(0, -1px); }
  50% { transform: translate(0, 2px); }
  100% { transform: translate(0, -1px); }
}

@keyframes leftToRight {
  0% { transform: translate(-1px, 4px); }
  100% { transform: translate(1px, 4px); }
}

@keyframes leftToRightWide {
  0% { transform: translate(-5px, 1px); }
  100% { transform: translate(2px, 1px); }
}

@keyframes scaleX {
  0% { transform: translate(0, 0) scale(1, 1); }
  100% { transform: translate(-9px, 0) scale(2, 1); }
}

@keyframes scaleUpAndDown {
  0% { transform: scale(1, 1); }
  100% { transform: scale(1, 1.2); }
}

@keyframes blink {
  0% { opacity: 1; }
  45% { opacity: 1; }
  50% { opacity: 0; }
  55% { opacity: 1; }
  100% { opacity: 1; }
}

@keyframes blinkSqueeze {
  0% { transform: scale(1, 1); }
  45% { transform: scale(1, 1); }
  50% { transform: scale(1, 0); }
  55% { transform: scale(1, 1); }
  100% { transform: scale(1, 1); }
}

@keyframes blinkSqueezeTwice {
  0% { transform: scale(1, 1); }
  45% { transform: scale(1, 1); }
  50% { transform: scale(1, 0); }
  55% { transform: scale(1, 1); }
  60% { transform: scale(1, 0); }
  65% { transform: scale(1, 1); }
  100% { transform: scale(1, 1); }
}
</style>