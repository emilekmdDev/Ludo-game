<template>
 <div v-for="i in players.length" :key="i">
  <br>
  {{ players[i-1] }}
 </div>
  <div v-show="!showparty">
    <div>
      <form @submit.prevent="addplayer(playername)">
        <button type="submit">+</button>
        <input type="text"  v-model="playername">
      </form>

    </div>
    <Player v-for="(player,index) in players" :key="index" @del="deleteplayer(player.playername)" :players="players" :index="index" :colors="colors" :hide='false'></Player>
    <button @click="start">start a party width boot</button>
  </div>
<transition>
  <div v-show="showparty">
    <p>Les noms sont : {{ id }}</p>
  <div class="container">
    <div class="c1">
      <div class="p1color home">
        
        <div v-for="i in players.length" :key="i">
          <!-- gere l'affichage des pions en fonctions des couleurs selectionner -->
          <div class="subcontainer" v-if="players[i-1].color=='p1color'" id="home1">
            {{ players[i-1].playername}}
            {{ players[i-1].turn }}
            <div class="pion p1color" :class="{waiting:pionsp1[0].canmove && !pionsp1[0].finish}" ref="varpion1p1" @click="select(pionsp1[0],pionsp1)"></div>
            <div class="pion p1color" :class="{waiting:pionsp1[1].canmove && !pionsp1[1].finish}" ref="varpion2p1" @click="select(pionsp1[1],pionsp1)"></div>
            <div class="pion p1color" :class="{waiting:pionsp1[2].canmove && !pionsp1[2].finish}" ref="varpion3p1" @click="select(pionsp1[2],pionsp1)"></div>
            <div class="pion p1color" :class="{waiting:pionsp1[3].canmove && !pionsp1[3].finish}" ref="varpion4p1" @click="select(pionsp1[3],pionsp1)"></div>
          </div>
        </div>

      </div>    
      <div class="block1">
        <div v-for="i in 18" :key="i" :class="{box:true,p1color:i==2 ||i>7 && i<13 || i==15,imune:imune.includes(i)}" :id="i">{{ i }}</div>
      </div>
      <div class="p4color home" >
        <!-- gere l'affichage des pions en fonctions des couleurs selectionner -->
        <div v-for="i in players.length" :key="i">
          <div class="subcontainer" v-if="players[i-1].color=='p4color'" id="home4">
            {{ players[i-1].playername }}
            {{ players[i-1].turn }}
            <div class="pion p4color" :class="{waiting:pionsp4[0].canmove && !pionsp4[0].finish}" ref="varpion1p4" @click="select(pionsp4[0],pionsp4)"></div>
            <div class="pion p4color" :class="{waiting:pionsp4[1].canmove && !pionsp4[1].finish}" ref="varpion2p4" @click="select(pionsp4[1],pionsp4)"></div>
            <div class="pion p4color" :class="{waiting:pionsp4[2].canmove && !pionsp4[2].finish}" ref="varpion3p4" @click="select(pionsp4[2],pionsp4)"></div>
            <div class="pion p4color" :class="{waiting:pionsp4[3].canmove && !pionsp4[3].finish}" ref="varpion4p4" @click="select(pionsp4[3],pionsp4)"></div>
          </div>
        </div>

      </div>
    </div>

    <div class="c2">
      <div class="block1">
        <div v-for="(i,index) in col2row1" :key="index" :class="{box:true,p2color:col2row1_colored.includes(i),imune:imune.includes(i)}" :id="i">{{i}}</div>  
      </div>
      <div class="center" style="display: flex;align-items: center;justify-content: center;"><button @click="play">lancer le de</button> <span ref="dicedisplay">""</span></div>
      <div class="block2">
        <div v-for="(i,index) in col2row3" :key="index" :class="{box:true,p4color:col2row3_colored.includes(i),imune:imune.includes(i)}" :id="i">{{ i }}</div>
      </div>
    </div>

    <div class="c3">
      <div class="p2color home">
        <!-- gere l'affichage des pions en fonctions des couleurs selectionner -->
        <div v-for="i in players.length" :key="i">
          <div class="subcontainer" v-if="players[i-1].color=='p2color'" id="home2">
            {{ players[i-1].playername }}
            {{players[i-1].turn}}
            <div class="pion p2color" :class="{waiting:pionsp2[0].canmove && !pionsp2[0].finish}" ref="varpion1p2" @click="select(pionsp2[0],pionsp2)"></div>
            <div class="pion p2color" :class="{waiting:pionsp2[1].canmove && !pionsp2[1].finish}" ref="varpion2p2" @click="select(pionsp2[1],pionsp2)"></div>
            <div class="pion p2color" :class="{waiting:pionsp2[2].canmove && !pionsp2[2].finish}" ref="varpion3p2" @click="select(pionsp2[2],pionsp2)"></div>
            <div class="pion p2color" :class="{waiting:pionsp2[3].canmove && !pionsp2[3].finish}" ref="varpion4p2" @click="select(pionsp2[3],pionsp2)"></div>
          </div>
        </div>
      </div>
      <div class="block1">
        <div v-for="i in col3row2" :key="i" :class="{box:true,p3color:i==71 ||i>60 && i<66 || i==58,imune:imune.includes(i)}" :id="i">{{ i }}</div>
      </div>
      <div class="p3color home">
        <!-- gere l'affichage des pions en fonctions des couleurs selectionner -->
        <div v-for="i in players.length" :key="i">
          <div class="subcontainer" v-if="players[i-1].color=='p3color'" id="home3">
            {{ players[i-1].playername }}
            {{ players[i-1].turn }}
            <div class="pion p3color" :class="{waiting:pionsp3[0].canmove && !pionsp3[0].finish}" ref="varpion1p3" @click="select(pionsp3[0],pionsp3)"></div>
            <div class="pion p3color" :class="{waiting:pionsp3[1].canmove && !pionsp3[1].finish}" ref="varpion2p3" @click="select(pionsp3[1],pionsp3)"></div>
            <div class="pion p3color" :class="{waiting:pionsp3[2].canmove && !pionsp3[2].finish}" ref="varpion3p3" @click="select(pionsp3[2],pionsp3)"></div>
            <div class="pion p3color" :class="{waiting:pionsp3[3].canmove && !pionsp3[3].finish}" ref="varpion4p3" @click="select(pionsp3[3],pionsp3)"></div>
          </div>
        </div>
      </div>
    </div>
  </div>
  </div>
</transition>

</template>

<script>

import Player from './Player.vue';

import {Pion,Joueur, Partie} from '../js/class_.js'
import { onMounted,onUpdated,ref } from "vue";

export default {

  props:['id'],
  components:{Player},

  setup(){
    
    ////////////////////////////////////// variable
    
    let canmove=ref(false)
    let col2row1=ref([])
    let col2row3=ref([])
    let col3row2=ref([])

    let col2row1_colored=ref([])
    let col2row3_colored=ref([])
    let col3row2_colored=ref([])

    let imune=[2,15,25,24,48,49,71,58]

    ////////////////////////////////pions

    let varpion1p1=ref(null)
    let varpion2p1=ref(null)
    let varpion3p1=ref(null)
    let varpion4p1=ref(null)

    let pion1p1 = new Pion ()
    let pion2p1 = new Pion ()
    let pion3p1 = new Pion ()
    let pion4p1 = new Pion ()


    let varpion1p2=ref(null)
    let varpion2p2=ref(null)
    let varpion3p2=ref(null)
    let varpion4p2=ref(null)

    let pion1p2 = new Pion ()
    let pion2p2 = new Pion ()
    let pion3p2 = new Pion ()
    let pion4p2 = new Pion ()


    let varpion1p3=ref(null)
    let varpion2p3=ref(null)
    let varpion3p3=ref(null)
    let varpion4p3=ref(null)

    let pion1p3 = new Pion ()
    let pion2p3 = new Pion ()
    let pion3p3 = new Pion ()
    let pion4p3 = new Pion ()


    let varpion1p4=ref(null)
    let varpion2p4=ref(null)
    let varpion3p4=ref(null)
    let varpion4p4=ref(null)

    let pion1p4 = new Pion ()
    let pion2p4 = new Pion ()
    let pion3p4 = new Pion ()
    let pion4p4 = new Pion ()

    ///////////////////////////////////////////////

    //varible pour le stockage et l'affichage des valeurs de de
    let dicedisplay=ref(null)
    let dicevalue

    /////////////////////////////////////////////// listes contenant l'ensemble des pions de chaque joueurs
    let pionsp1=ref([pion1p1,pion2p1,pion3p1,pion4p1])
    let pionsp2=ref([pion1p2,pion2p2,pion3p2,pion4p2])
    let pionsp3=ref([pion1p3,pion2p3,pion3p3,pion4p3])
    let pionsp4=ref([pion1p4,pion2p4,pion3p4,pion4p4])
    

    /////////////////////////////////////////////// contient les id des case a parcourir pour chaque joueur
    let p1road=[2,3,4,5,6,34,31,28,25,22,19,20,21,24,27,30,33,36,55,56,57,58,59,60,66,72,71,70,
    69,68,67,39,42,45,48,51,54,53,52,49,46,43,40,37,18,17,16,15,14,13,7,8,9,10,11,12]

    let p2road=[24,27,30,33,36,55,56,57,58,59,60,66,72,71,70,69,68,67,39,42,45,48,51,54,53,52,49,
    46,43,40,37,18,17,16,15,14,13,7,1,2,3,4,5,6,34,31,28,25,22,19,20,23,26,29,32,35]
    
    let p3road=[71,70,69,68,67,39,42,45,48,51,54,53,52,49,46,43,40,37,18,17,16,15,14,13,7,1,2,3,
    4,5,6,34,31,28,25,22,19,20,21,24,27,30,33,36,55,56,57,58,59,60,66,65,64,63,62,61]
    
    let p4road=[49,46,43,40,37,18,17,16,15,14,13,7,1,2,3,4,5,6,34,31,28,25,22,19,20,21,24,27,30,
    33,36,55,56,57,58,59,60,66,72,71,70,69,68,67,39,42,45,48,51,54,53,50,57,55,41,38]

    
    /////////////////////////////////////////////// continent l'ensemeble des joueurs qui constituront la partie
    let names=['andre','thomas','Adam','Ego','Edison','Hans','Toshi','Belmont','emile','Jean']
    let players=ref([
      {playername:'player name',color:'p1color',turn:true,id:0,pions:null,road:null,pions_t:0,winner:false,type:'human'},
      {playername:names[Math.floor(Math.random() * 10)],color:'p2color',turn:false,id:0,pions:null,road:null,pions_t:0,winner:false,type:'bot'},
      {playername:names[Math.floor(Math.random() * 10)],color:'p3color',turn:false,id:0,pions:null,road:null,pions_t:0,winner:false,type:'bot'},
      {playername:names[Math.floor(Math.random() * 10)],color:'p4color',turn:false,id:0,pions:null,road:null,pions_t:0,winner:false,type:'bot'},
    ])

    let partie=new Partie()
    /////////////////////////////////////////////// continet tout les couleur dispo et permet de savoir ques couleur sont disponible lor de la selection des joueur
    let colors=ref([{color:'p1color',taked:true},{color:'p2color',taked:false},{color:'p3color',taked:false},{color:'p4color',taked:false}])

    //////////////////////////////// est dynamiquement associer a l'input permetant d'ajouter des joueur via leur noms
    let playername=ref('')
    //gerer l'affichage de la configuration de la partie et de la table de jeux
    let showparty=ref(false)

    /////////////// permet de savoir si un joueur est train de jouer
    let playing=false

    //////////////////////////////////////////////////////////////// function ////////////////////////////////////////////////////////////////

    ////////////////// ce lance lorque l'on click sur le boutton play
    function play(){      

      
      if (!playing) {
        playing=true

        //generation de la valeur du de
        dicevalue=Math.floor(Math.random() * 2) + 5
        dicedisplay.value.innerText=dicevalue
        

        let i
        //reinitialise la selections de l'ensemble des pions selectionner a false
        for (i = 0; i < players.value.length; i++) {
          reset_(players.value[i].pions)
        }
        
        //permet de savoir l'index du joeur dont c'est le tour
        for (i = 0; i < players.value.length; i++) {
          if (players.value[i].turn) break
        }

        // met en exergue tout les pions deplacable dans le code mais aussi visuellement dans l'html grace a une classe "waiting"
        movable_p(players.value[i],'activate',dicevalue)
        
        // patiente jusqu'a ce que le joueur selectionne le pion qu'il souhaite deplacer si possible
        const interval=setInterval(() => {

          //cas ou aucun pion n'est deplacable on passeras directement au jouerur suivant
              if (movable(dicevalue,players.value[i].pions)==false) { 
                  console.log('cant');
                  
                  clearInterval(interval)
                  nextplayers(players.value)  
                  end(players.value)
                  playing=false
                  
                  if (nextplayersisbot(players.value)) setTimeout(() => {play()}, 1000);
                  
                  return
              }
              
              if (players.value[i].type=='bot') {
                if (autoplay(dicevalue,players.value[i])==true) {
                  clearInterval(interval)
                  end(players.value)
                  playing=false
                  setTimeout(() => {play()}, 1000)
                  movable_p(players.value[i],'deactivate',dicevalue)
                  return   
                }else{
                  clearInterval(interval)
                  nextplayers(players.value)  
                  end(players.value)
                  playing=false
                  movable_p(players.value[i],'deactivate',dicevalue)

                  if (nextplayersisbot(players.value)) setTimeout(() => {play()}, 1000);

                  return 
                }
              }

              // gere le deplacement du pion selectionner automatiquement (cas ou il n'y a que un seul pions deplacable) ou par le joeur
              if (selectedpion(players.value[i].pions) || automovepion(players.value[i])!=null) {
                //desactive la mise en exergue des pions deplacable
                movable_p(players.value[i],'deactivate',dicevalue)
                
                //recupere le pion a selectionner suivant deux cas : l'auto et la selection effectuer par le joueus
                let pion
                if (automovepion(players.value[i])!=null) {
                  pion=automovepion(players.value[i])
                }else{
                  pion=selectedpion(players.value[i].pions)
                }
                
                //sortie d'un pion de la maison
                if (pion.athome() && dicevalue==6) {
                  move(pion,1,players.value[i].color)
                  clearInterval(interval)
                  // nextplayers(players.value)
                  end(players.value)
                  playing=false
                  
                  // if (nextplayersisbot(players.value)) setTimeout(() => {play()}, 1000);
                  
                  return
                }

                //deplacement d'un pion deja sortie de la maison
                if (pion.onroad()) {
                  let captureresponse=move(pion,dicevalue,players.value[i].color)
                  clearInterval(interval)
                  
                  if (!(dicevalue==6 || captureresponse==true)) {
                    nextplayers(players.value) 
                  }

                  end(players.value)
                  playing=false
                  if (nextplayersisbot(players.value)) setTimeout(() => {play()}, 1000);
                  return
                }
              }   
        }, 100);
      }
    }

    // si un seul pion est deplacable, le retourne 
    function autoplay(dicevalue,botplayer) {
      let nb={n:0,index:0}
      
      ///////////////////////////////////// priorite 1 l'autove
      //connaitre le nombre de pions deplacable
      for (let i = 0; i < botplayer.pions.length; i++) {
        if (botplayer.pions[i].canmove) {
          nb.n++
        }
      }

      if (nb.n==0) {
        return
      }

      //deplacemenent automatique s'il n'y a que un pion deplacable
      if (nb.n==1) {
        if (cancapture(botplayer.color,players.value,botplayer.pions[nb.index].current_position+dicevalue) || dicevalue==6) {
          move(botplayer.pions[nb.index],dicevalue,botplayer.color)
          return true 
        }
        move(botplayer.pions[nb.index],dicevalue,botplayer.color)
        return
      }
      
      ///////////////////////////////////// priorite 2 la capture
      
      for (let i = 0; i < botplayer.pions.length; i++) {       
        if (cancapture(botplayer.color,players.value,botplayer.pions[i].current_position+dicevalue)) {
          move(botplayer.pions[i],dicevalue,botplayer.color)
          return true
        }
      }

      ///////////////////////////////////// priorite 2 la sotie d'un pion ou son deplacement sur la route

      let rand_=Math.floor(Math.random() * 2)
      
      
      if (rand_==0) {

        for (let i = 0; i < botplayer.pions.length; i++) {
          //cas ou un pion est sortable de la maison
          if (botplayer.pions[i].athome() && dicevalue==6){
            move(botplayer.pions[i],1,botplayer.color)
            return true
          }
        }

        for (let i = 0; i < botplayer.pions.length; i++) {
          // cas ou un pion est en cours de route
          if (botplayer.pions[i].onroad() && botplayer.pions[i].current_position+dicevalue<=p1road.length){
            move(botplayer.pions[i],dicevalue,botplayer.color)  
            if (dicevalue==6) {return true}else{return false}
            }
        }
      }else{
        for (let i = 0; i < botplayer.pions.length; i++) {
          // cas ou un pion est en cours de route
          if (botplayer.pions[i].onroad() && botplayer.pions[i].current_position+dicevalue<=p1road.length){
            move(botplayer.pions[i],dicevalue,botplayer.color)  
            if (dicevalue==6) {return true}else{return false}
            }
        }

        for (let i = 0; i < botplayer.pions.length; i++) {
          //cas ou un pion est sortable de la maison
          if (botplayer.pions[i].athome() && dicevalue==6){
            move(botplayer.pions[i],1,botplayer.color)
            return true
          }
        } 
      }
    }

    function automovepion(player){
      let n=0,index=0

      for (let i = 0; i < player.pions.length; i++) {
        if (player.pions[i].canmove) {
          n++
          index=i
        }        
      }      
      
      if (n==1) {
        player.pions[index].selected=true
        return player.pions[index]
      }

      return null
    }
    
    // gere le deplacement d'un pion a parti de ce dernier la valeur de de et sa couleur 
    function move(pion,valeur,color) {
      let index=pion.current_position+valeur
      let road
      switch (color) {
        case 'p1color':
          road=p1road
          break;
      
        case 'p2color':
          road=p2road
          break;
        
        case 'p3color':
          road=p3road
          break;

        case 'p4color':
          road=p4road
          break;
        default:
          break;
      }

      if (index<road.length) {
        let target=document.getElementById(road[parseInt(index)])  
        pion.current_position=index
        
        // pion.domvar.style.transform = `translate(${target.offsetTop}px, ${target.offsetLeft}px)`;
        
        /////////////// capture retourne un bouleen si une capture a ete fait ou pas
        let response=capture(color,players.value,road[parseInt(index)])
        
        if (imune.includes(road[parseInt(index)])) {
          pion.imune=true
        }else{
          pion.imune=false
        }
        target.appendChild(pion.domvar)
        return response
      }else if(index==road.length){
        //cas ou le pion termine sont parcour
        for (let i = 0; i < players.value.length; i++) {
          if (players.value[i].color==color) {
            players.value[i].pions_t++
            if (players.value[i].pions_t==4) {
              players.value[i].winner=true
            }
          }
        }
        pion.finish=true

        document.getElementById('53').appendChild(pion.domvar)  
        console.log(players.value);
        
        return false
      }
    }

    function cancapture(color,players,position) {
      for (let i = 0; i < players.length; i++) {
        if (color==players[i].color) continue
        for (let j = 0; j < players[i].pions.length; j++) {
          let player=players[i]
            if(player.road[player.pions[j].current_position]==position && !player.pions[j].imune){
              return true
            }
        }
      }
      return false
    }
    // gere la capture d'un pion adverse (on verifie si la case vers la quel on vas contient un pion non imunise)
    function capture(color,players,position){ 
      for (let i = 0; i < players.length; i++) {
        if (color==players[i].color) continue
        for (let j = 0; j < players[i].pions.length; j++) {
          let player=players[i]
            if(player.road[players[i].pions[j].current_position]==position && !player.pions[j].imune){
              backhome(player.pions[j],player)
              return true
            }
        }
      }
      return false
    }

    // gere le reset et retour d'un pion a sa maison
    function backhome(pion,player){
      pion.current_position=-1
      pion.imune=false
      let tmp
      switch (player.color) {
          
          case 'p1color':
            tmp = document.getElementById('home1')
            tmp.appendChild(pion.domvar)
          break;
        
          case 'p2color':
            tmp = document.getElementById('home2')
            tmp.appendChild(pion.domvar)
          break;
          
          case 'p3color':
            tmp = document.getElementById('home3')
            tmp.appendChild(pion.domvar)
          break;
          
          case 'p4color':
            tmp = document.getElementById('home4')
            tmp.appendChild(pion.domvar)
          break;
      
        default:
          break;
      }
    }

    
    function nextplayersisbot(players){
      let tmp=['p1color','p2color','p3color','p4color'],index=0,j,k
      for (index = 0; index < players.length; index++) {
        if (players[index].turn) break
      }
      
      for (j = 0; j < tmp.length; j++) {
        if (players[index].color==tmp[j]) break
      }

      if (j<3) {
        for (k = 0; k < players.length; k++) {
          if (players[k].color==tmp[j+1]) {
            break
          }
        } 
      }else{
        for (k = 0; k < players.length; k++) {
          if (players[k].color==tmp[0]) {
            break
          }
        } 
      }
      // console.log(k,j);
      
      // le k-1 'cest pour palier au fait que j'apelle la fonctionne nextplayer() avant
      
      if (k==0) {
        // console.log(players[players.length-1]);
        
        return players[players.length-1].type=='bot'  
      }else{
        // console.log(players[k-1]);
        return players[k-1].type=='bot'  
      }
    }

    // permet de passer au joueur suivant en mettant le champ turn a jour de l'object player
    function nextplayers(players){
      
      let tmp=['p1color','p2color','p3color','p4color'],index=0,j,k=0
      for (index = 0; index < players.length; index++) {
        if (players[index].turn) {
          players[index].turn=false
          break
        }
      }
      
      for (j = 0; j < tmp.length; j++) {
        if (players[index].color==tmp[j]) {
          break
        }
      }
      console.log(k,players.length,j);
      if (j<3) {
        for (k = 0; k < players.length; k++) {
          if (players[k].color==tmp[j+1]) {
            break
          }
        } 
      }else{
        for (k = 0; k < players.length; k++) {
          if (players[k].color==tmp[0]) {
            break
          }
        } 
      }
      console.log(k,players.length,j);
      
      /////////////think
      if (k==players.length) {
        players[0].turn=true 
      }else{
        players[k].turn=true 
      }
      
    }

    // retourne un bool s'il existe un pion deplacable ou pas
    // recently update
    function movable(dice,pions) {
      for (let i = 0; i < pions.length; i++){
        //cas ou un pion est sortable de la maison
        if (pions[i].athome() && dice==6){
          return true
        }
        
        // cas ou un pion est en cours de route
        if (pions[i].onroad() && pions[i].current_position+dice <= p1road.length){
          return true  
        }
      }
      return false
    }

    /////////////// met en exergue l'ensemble des pions deplacable
    function movable_p(player,status,dice) {
      switch (status) {
        case 'activate':          
            for (let i = 0; i < player.pions.length; i++){
            //cas ou un pion est sortable de la maison
              if (!player.pions[i].finish && dice==6 && player.pions[i].current_position==-1 ||
               !player.pions[i].finish && player.pions[i].current_position!=-1 && player.road.length>=player.pions[i].current_position+dice){
                // console.log(player.road.length==player.pions[i].current_position+dice);
                player.pions[i].canmove=true  
              }
            }
          break;

        case 'deactivate':
          for (let i = 0; i < player.pions.length; i++){
            player.pions[i].canmove=false
          }
        break;

        default:
          break;
      }
      
    }

    //permet de selectionner un pion
    function select(pion,pions){
      for (let i = 0; i < pions.length; i++) {
        pions[i].selected=false
      }
      pion.selected=true
    }


    //reset la selection des pions
    function reset_(pions){
      for (let i = 0; i < pions.length; i++) {
        pions[i].selected=false
      }
    }

    //retourne le pion selectionner
    function selectedpion(pions) {
      for (let i = 0; i < 4; i++) {
        if (pions[i].selected) {          
          return pions[i]
        }
      }
      return null
    }

    //permet d'ajouter un player
    function addplayer(name){
      if (players.value.length<4 && name!='') {
        let color_=colors.value.find(elt=>!elt.taked)
        color_.taked=true
        // console.log(colors.value);
        players.value.push({playername:name,color:color_.color,turn:false,id:0,pions:null,road:null,pions_t:0,winner:false,type:'bot'})
      }
      playername.value=''
    }

    // permet de suprimer un player
    function deleteplayer(removename){
          
      if (players.value.length>2) {
        for (let i = 0; i < players.value.length; i++) {
          if (players.value[i].playername==removename) {
            for (let j = 0; j < colors.value.length; j++) {
              if (colors.value[j].color==players.value[i].color) {
                //libere sa couleur
                colors.value[j].taked=false
                break
              }
            }
            break
          } 
        }
        players.value=players.value.filter(obj=>obj.playername!=removename)
      }
    }

    // gere la fin de partie lorsque n-1 joueur on terminer
    function end(players) {
      let n
      for (let i = 0; i < players.length; i++) {
        if (players[i].winner) {
          n++
        }
      }

      if (players.length-1==n) {
        console.log('Partie terminer');
        
      }
    }
    
    //permet d'intialiser certainer variables au lancement de la partie
    function start(){
      ////////////////////////// domvar des pions

      try {
        pion1p1.domvar = varpion1p1.value['0']
        pion2p1.domvar = varpion2p1.value['0']
        pion3p1.domvar = varpion3p1.value['0']
        pion4p1.domvar = varpion4p1.value['0']   
      } catch (error) {
        pion1p1.domvar = varpion1p1.value
        pion2p1.domvar = varpion2p1.value
        pion3p1.domvar = varpion3p1.value
        pion4p1.domvar = varpion4p1.value
      }

      try {
        pion1p2.domvar = varpion1p2.value['0']
        pion2p2.domvar = varpion2p2.value['0']
        pion3p2.domvar = varpion3p2.value['0']
        pion4p2.domvar = varpion4p2.value['0']   
      } catch (error) {
        pion1p2.domvar = varpion1p2.value
        pion2p2.domvar = varpion2p2.value
        pion3p2.domvar = varpion3p2.value
        pion4p2.domvar = varpion4p2.value
      }

      try {
        pion1p3.domvar = varpion1p3.value['0']
        pion2p3.domvar = varpion2p3.value['0']
        pion3p3.domvar = varpion3p3.value['0']
        pion4p3.domvar = varpion4p3.value['0']   
      } catch (error) {
        pion1p3.domvar = varpion1p3.value
        pion2p3.domvar = varpion2p3.value
        pion3p3.domvar = varpion3p3.value
        pion4p3.domvar = varpion4p3.value
      }

      try {
        pion1p4.domvar = varpion1p4.value['0']
        pion2p4.domvar = varpion2p4.value['0']
        pion3p4.domvar = varpion3p4.value['0']
        pion4p4.domvar = varpion4p4.value['0']   
      } catch (error) {
        pion1p4.domvar = varpion1p4.value
        pion2p4.domvar = varpion2p4.value
        pion3p4.domvar = varpion3p4.value
        pion4p4.domvar = varpion4p4.value
      }

      // console.log(pion1p1.domvar);
      // console.log(pion1p2.domvar);
      // console.log(pion1p3.domvar);
      // console.log(pion1p4.domvar);
      // console.log(varpion2p1);
      // console.log(varpion1p2.value['0']);
      // console.log(varpion1p2.value);
            
      showparty.value=true
      
      /////////////// assignation des routes et pions de chaque joueur configurer
      
      for (let i = 0; i < players.value.length; i++) {
        if (players.value[i].type=='human') {
          players.value[i].turn=true 
        }
        players.value[i].id=i+1      
        
        switch (players.value[i].color) {
          case 'p1color':
            players.value[i].pions=pionsp1.value
            for (let j = 0; j < 4; j++) {
              players.value[i].pions[j].player_id=players.value[i].id
            }
            players.value[i].road=p1road
          break;
          
          case 'p2color':
            players.value[i].pions=pionsp2.value
            for (let j = 0; j < 4; j++) {
              players.value[i].pions[j].player_id=players.value[i].id
            }
            players.value[i].road=p2road
          break;

          case 'p3color':
            players.value[i].pions=pionsp3.value
            for (let j = 0; j < 4; j++) {
              players.value[i].pions[j].player_id=players.value[i].id
            }
            players.value[i].road=p3road
          break;
          
          case 'p4color':
            players.value[i].pions=pionsp4.value
            for (let j = 0; j < 4; j++) {
              players.value[i].pions[j].player_id=players.value[i].id
            }
            players.value[i].road=p4road
          break;
        
          default:
            break;
        }
      }
      partie.players=players.value
    }

    onMounted(() => {      
      
      /////////////////////// gere la construction du dom (case speciale,coloré..)
      let i
      ///////////////////////////////////c2 
      for (let i = 19; i <= 36; i++) {
        col2row1.value.push(i)
      }

      for (let i = 37; i <=54; i++) {
        col2row3.value.push(i)
      }

      i=23
      col2row1_colored.value.push(24 ,25)
      while (1) {
        col2row1_colored.value.push(i) 
        i+=3
        if (i>36) {
          break
        }
      }

      i=38
      col2row3_colored.value.push(49 ,48)
      while (1) {
        col2row3_colored.value.push(i) 
        i+=3
        if (i>50) {
          break
        }
      }
      
      ///////////////////////////////////c3

      for (let i = 55; i <= 72; i++) {
        col3row2.value.push(i)
      }

      i=61
      col3row2_colored.value.push(71 ,58)
      while (1) {
        col3row2_colored.value.push(i) 
        i++
        if (i>65) {
          break
        }
      }
    })
    
    return {col2row1,
            col2row1_colored,
            col2row3,
            col2row3_colored,
            col3row2,
            col3row2_colored,
            imune,
            
            pionsp1,pionsp2,pionsp3,pionsp4,
            varpion1p1,varpion2p1,varpion3p1,varpion4p1,
            varpion1p2,varpion2p2,varpion3p2,varpion4p2,
            varpion1p3,varpion2p3,varpion3p3,varpion4p3,
            varpion1p4,varpion2p4,varpion3p4,varpion4p4,
            
            play,
            dicedisplay,
            select,
            canmove,
            players,
            playername,
            showparty,
            deleteplayer,
            addplayer,
            start,
            colors,
          }
  },

}

</script>


<style scoped>
  :root {
  --p1_color: red;
  --p2_color: green;
  --p3_color: yellow;
  --p4_color: blue;

  --home_size:300px;
  --boxsize:50px;
  --col_size:150px;

  --rounded:50%;
  --token_size:40px
  }

  .move_:hover{
    transform: scale(1.1);
  }
  *{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
  }

  .container{
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
  }

  .p1color{
      background: var(--p1_color);
  }

  .p2color{
      background: var(--p2_color);
  }

  .p3color{
      background: var(--p3_color);
  }

  .p4color{
      background: var(--p4_color);
  }

  .home{
      width: var(--home_size);
      height: var(--home_size);
      display: flex;
      align-items: center;
      justify-content: center;
  }

  .subcontainer{
    width: calc(var(--home_size) / 2);;
    height: calc(var(--home_size)/2);
    display: grid;
    grid-template-columns: repeat(2, 1fr); 
    grid-template-rows: repeat(2, 1fr); 
    justify-items: center;
    align-items: center; 
  }

  .box{
      height: var(--boxsize);
      width: var(--boxsize);
      border: 1px solid black;
      display: flex;
      align-items: center;
      justify-content: center;
      color: rgba(0, 0, 0, 0.322);
  }

  .c1 .block1,.c3 .block1{
      display: grid;
      grid-template-columns: repeat(6,auto);
  }

  .c1{
      width: var(--home_size);
  }

  .c2{
    width: var(--col_size);  
  }

  .c2 .block1,.c2 .block2{
      display: grid;
      grid-template-columns: repeat(3,auto);
  }
  .center{
    width: var(--col_size);
    height: var(--col_size);
    background: gray;
  }

  .imune{
    background: rgb(180, 180, 180);
  }

  .pion{
    height: var(--token_size);
    width: var(--token_size);
    border-radius: var(--rounded);
    border: 3px solid black;
    text-align: center;
    transition-property: transform;
    transition: 1s;
  }

  .pion:hover{
    transform: scale(1.1);
  }

  .waiting{
    animation-name: example;
    animation-duration: 2s ;
    animation-iteration-count: infinite;
  }

  .v-enter-active,
  .v-leave-active {
    transition: opacity 0.5s ease;
  }

  .v-enter-from,
  .v-leave-to {
    opacity: 0;
}


  @keyframes example {
  0%   {background-color: red;}
  25%  {background-color: yellow;}
  50%  {background-color: blue;}
  100% {background-color: green;}
}

</style>