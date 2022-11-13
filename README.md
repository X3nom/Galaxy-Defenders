# Galaxy-Defenders
Simple game where you shoot down asteroids and dodge bullets.

This is a game I made back in 2021 using pygame. The code is pretty messy, because I was just starting to learn programming by that time.
## Gamerules
  - If asteroid gets all the way to the bottom of screen, the game is over.
  
  - Player has 5 lives, live decreases if bullet hits you, if you get to 0, game is also over
  
  - Player has "power", power percentage increases with asteroids destroyed. There are 3 abilities player can use, each of which needs some power percentage
  
    abilities:
  
    - machinegun - rapid fire, needs 100% power
  
    - shield - makes player invincible for some amount of time, needs 70% power
    
    - homing missile - shoots bullet, that automaticcaly finds its way to asteroids, needs 35% power
## Note
!!! For some reason game does not want to run from file explorer, but runs just fine from VScode

## Possible future updates

If I revisit this project someday (which I don't think will happen), possibilities are to implement:

  - highest score system - has been worked on in the past, but not finished.
  
  - dash ability - is implemented, but now working how it should
  
  - bosses - aliens, that would fly on the top portion on the screen, and shoot bullets at player
