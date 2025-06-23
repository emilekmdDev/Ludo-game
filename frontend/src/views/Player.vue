<template> 
    <div>
        <div v-if="hide==false || hide==true && index==0" >
        <input type="text"  maxlength="30" onfocus="this.value=''" v-model="players[index].playername" :placeholder="players[index].playername" required> 
        <div class="box" :class="players[index].color" @click="changecolor" :id="id_[index]"></div> 
        <div v-if="setting[index]">
            color setting 
            <div class="backdrop" @click.self="setting[index]=false">
                <div class="box selectable" :class="colors[0].color" @click="updatecolor(players[index],colors[0].color)"></div>
                <div class="box selectable" :class="colors[1].color" @click="updatecolor(players[index],colors[1].color)"></div>
                <div class="box selectable" :class="colors[2].color" @click="updatecolor(players[index],colors[2].color)"></div>
                <div class="box selectable" :class="colors[3].color" @click="updatecolor(players[index],colors[3].color)"></div>
                <div class="box close" @click="setting[index]=false">x</div>
            </div>
        </div>
          <div v-if="!hide">
            <button @click="del">-</button>
            <button @click="changetype">type</button>
            <p v-if="players[index].type=='bot'">bot</p>
            <p v-if="players[index].type=='human'">human</p>
          </div>
        </div>
    </div>
</template>

<script>


export default {
    props:{
        index:Number,
        players:Object,
        colors:Array,
        hide:Boolean,
    },
    data(){
        return{
            setting:[false,false,false,false],
            id_:['c1','c2','c3','c4']
        }
    },

    methods:{
        del(){            
            let n=0
            for (let i = 0; i < this.players.length; i++) { 
              if (this.players[i].type=='human') {
                n++
                //empeche une partie de boot
              }
            }
            
            if (n==1 &&this.players[this.index].type=='human') {
              return
            }
            this.$emit('del')
        },

        changecolor(){
            this.setting[this.index]=true
        },

        updatecolor(player,color){

          if (player.color==color) {
            return
          }

          if (this.hide) {
            if (player.color==color){
              return
            }

            for (let i = 0; i < this.colors.length; i++) {
              if (this.colors[i].color==player.color) {
                this.colors[i].taked=false 
              }

              if (this.colors[i].color==color) {
                this.colors[i].taked=true
              }
            }

            for (let i = 0; i < this.players.length; i++) {
              if (this.players[i].color==color) {
                this.players[i].color=player.color
                player.color=color
                break
              }
            }

            return
          }
          for (let i = 0; i < this.colors.length; i++) {
            ///cas ou la couleur est deja prise
            if (this.colors[i].color==color && this.colors[i].taked) {
              return
            }

            if (this.colors[i].color==color) {
              
              for (let j = 0; j < this.colors.length; j++) {
                if (this.colors[j].color==player.color) {
                  this.colors[j].taked=false
                }
                
              }
              player.color=color   
              this.colors[i].taked=true

              let target=document.getElementById(this.id_[this.index])
              for (let j = 0; j < this.colors.length; j++) {
                target.classList.remove(this.colors[j].color)
              }
              target.classList.add(this.colors[i].color)
              
              // console.log(document.getElementById(this.id_[this.index]).classList);
              
            }
          }

        },

        changetype(){
          let n=0
          for (let i = 0; i < this.players.length; i++) { 
            if (this.players[i].type=='human') {
              n++
              //empeche une partie de boot
            }
          }
          if (n==1 &&this.players[this.index].type=='human') {
            return
          }
          this.players[this.index].type=='bot'?this.players[this.index].type='human':this.players[this.index].type='bot'
        }
    }
}
</script>

<style>
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

  *{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
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

  .box{
      width: 20px;
      height: 20px;
  }

  .backdrop{
    position: relative;
    top: 0;
    left: 0;
    width: 300px;
    background: rgba(255, 0, 0, 0.274);
  }

  .selectable:hover{
    transform: scale(1.1);
  }

  .close:hover{
    cursor: pointer;
  }
</style>