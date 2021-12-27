# Rubik's-Cube
Rubik's cube solver

Uses Herbert Kociemba's 2-phase algorithm. Connected to custom cube-manipulating rig fitted with an Arduino Uno and 6 stepper motors and color detecting webcam.

run start.py to start the program

U1, U2, U3, U4, U5, U6, U7, U8, U9, R1, R2,
R3, R4, R5, R6, R7, R8, R9, F1, F2, F3, F4, F5, F6, F7, F8, F9, D1, D2, D3, D4, D5, D6, D7, D8, D9, L1, L2, L3, L4,
L5, L6, L7, L8, L9, B1, B2, B3, B4, B5, B6, B7, B8, B9

The names of the facelet positions of the cube
                  |************|
                  |* 1** 2** 3*|
                  |************|
                  |* 4** Y** 6*|
                  |************|
                  |* 7** 8** 9*|
            camera|************|
     |************|************|************|************|
     |*37**38**39*|*19**20**21*|*10**11**12*|*46**47**48*|
     |************|************|************|************|
     |*40**O **42*|*22** B**24*|*13**R **15*|*49**G **51*|
     |************|************|************|************|
     |*43**44**45*|*25**26**27*|*16**17**18*|*52**53**54*|
     |************|************|************|************|
                  |************|
                  |*28**29**30*|
                  |************|
                  |*31**W **33*|
                  |************|
                  |*34**35**36*|
                  |************|

  4
0 1 2 3
  5
  
  Y
O B R G
  W

  U
L F R B
  D

