class Joueur{
    constructor(id,turn,color,pions,road,pions_t,winner,type){
        this.id=id
        this.turn=turn
        this.color=color
        this.pions=pions
        this.road=road
        this.pions_t=pions_t
        this.winner=winner
        this.type=type
    }
}


class Pion {
    constructor(current_position = -1, player_id = 0, domvar = null, imune = false, selected=false,finish=false,canmove=false) {
        this.current_position = current_position;
        this.player_id = player_id;
        this.domvar = domvar;
        this.imune = imune;
        this.selected=selected
        this.finish=finish
        this.canmove=canmove
    }

    athome(){
        if (this.current_position==-1 && !this.finish) {
            return true
        }
        return false
    }

      //verifie si un pion est sur le chemin
    onroad(){
        if (this.current_position!=-1 && !this.finish) {
            return true
        }
        return false
    }
}

class Partie{
    constructor(playserturn=1,players=[]){
        this.playserturn=playserturn
        this.players=players
    }
    // permet de passer au joueur suivant en mettant le champ turn a jour de l'object player
    nextplayers(){
        for (let i = 0; i < this.players.length; i++) {
          if (this.players[i].turn && i!=this.players.length-1) {
            this.players[i].turn=false
            this.players[i+1].turn=true
            return
          }
          
          if (this.players[i].turn && i==this.players.length-1) {
            this.players[i].turn=false
            this.players[0].turn=true
            return
          }
  
        }
    }
}

export {Joueur,Pion,Partie}