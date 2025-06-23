# Ludo

## jeux offline  

[] jouer  
  [x] lancer le de  
  [x] deplacer le pion si c'est son tour  
[] ne pas pouvoir jouer alors qu'on est sur le point de terminer mais qu'on a pas la bonne valeur de de
[x] distinguer les pion deplacable

[] animation
  [] deplacement des pion case par case avec animation

[x] sortir un pion de la maison  
  [x] selectionner un pion
[] deplacer un pion  
  -si existe un pion deplacable
[x] configuration de la partie
  [x] choix du nom
  [x] choix de la couleur

[] jcb
  [] jouer automatiquement
[x] capturer un pion adverse  
[] lancer une partie  

## Etat de la partie

[]

## contraintes & test

### contraintes

[] on ne peut capturer un pion qui ce trouve sur une case imune  
[] la capture d'un pion offre la possibilite de rejouer  
[] jouer 6 permet de rejouer (on limiteras a 3 9 succesif)  
[] capturer un pion le ramene loin dans sa maisson  
[] deux pion de couleur differentes peuvent rester sur la meme case imune sinon l'autre pion devras attendre seras placer sur la case précédentes  

## jeux online  

- creation de compte de joueur
- pouvoir ce loger en tant que joueur

- afficher la liste des parties
- cree une partie
- joindre une partie
  - en tant que joueur
  - ent tant que spectateur

### containte

- c'est l'adminstrateur qui cree les tables (2player cout 500pts/4 player cout 100ponts)
- une fois que l'utilisateur est loger il peut choissir partie rapide/partie privee si c'est partie rapide on lui propose les partie rapide dispos
