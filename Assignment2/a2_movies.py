import os,sys

#sys.path.append('/homex/binaree/lmgc90_dev_cluster_parallel/build')
#sys.path.append('/Users/Amjat/Documents/lmgc90_dev/build')

from pylmgc90.chipy import *

from numpy import *



#############

#############

#############

#############

# Parametres

#############

#

# ... de la simu

sigma_0           = 10000

dt                = 1.e-3  # pas de temps

theta             = 0.5    # Time integrator

nb_steps          = 40000

freq_display      = 5000

freq_outFiles     = 1000

freq_detect       = 1      # Frequence de detection des contacts

#

# ... du calcul

#       123456789012345678901234567890

type = 'Stored_Delassus_Loops         '

norm = 'QM/16'

tol = 0.1e-3

relax = 1.0

gs_it1 = 50                    # Nombre d iteration mini

gs_it2 = 501                   # Nombre d iteration max = gs_it2 * gs_it1

nlgs_SetWithQuickScramble()

#

#############

#############

#############

#############



checkDirectories()             # On test si tout les dossiers sont presents

SetDimension(2)                # Set dimension in chipy for dummies  ###

utilities_DisableLogMes()

#############

### lecture du modele ###

#############

### model reading ###

utilities_logMes('READ BODIES')

ReadBodies()



utilities_logMes('READ BEHAVIOURS')

ReadBehaviours()



utilities_logMes('LOAD BEHAVIOURS')

LoadBehaviours()



utilities_logMes('READ INI DOF')

ReadIniDof()



utilities_logMes('LOAD TACTORS')

LoadTactors()



utilities_logMes('READ INI Vloc Rloc')

ReadIniVlocRloc()



utilities_logMes('READ DRIVEN DOF')

ReadDrivenDof()

#############

### Fin de la lecture du modele ###

#############



#############

### Ecriture du modele ###

#############

utilities_logMes('WRITE BODIES')

WriteBodies()

utilities_logMes('WRITE BEHAVIOURS')

WriteBehaviours()

utilities_logMes('WRITE DRIVEN DOF')

WriteDrivenDof()

#############

### Fin de l ecriture du modele ###

#############



#############

### Calcul des diametres

#############

nb_rbdy2    = RBDY2_GetNbRBDY2()          # On recupere le nb de grains

Rmax        = 0.0

Rmin        = 100000000.

Rmax_temp   = 0.0

Rmin_temp   = 0.0

ref_radius  = 0.0

for k in range (1,nb_rbdy2-2):           # On boucle sur tout les corps - 2 (car parois)

  Rmax_temp = DISKx_GetRadius(k)

  Rmin_temp = DISKx_GetRadius(k)

  if (Rmax_temp > Rmax):

    Rmax = Rmax_temp

  if (Rmin_temp < Rmin):

    Rmin = Rmin_temp

ref_radius  = 0.5*(Rmax + Rmin)



#############

### definition des parametres du calcul ###

#############

utilities_logMes('INIT TIME STEPPING')

TimeEvolution_SetTimeStep(dt)

Integrator_InitTheta(theta)



### post2D ##

OpenDisplayFiles()

#OpenPostproFiles()



### COMPUTE MASS ###

ComputeMass()



#############

### DEBUT DU CALCUL ###

#############

print ("Sauvegarde donnees      = ", freq_outFiles)

print ("Sauvegarde visu         = ", freq_display)

body_down   = nb_rbdy2 - 3

body_up     = nb_rbdy2 - 2

body_left   = nb_rbdy2 - 1

body_right  = nb_rbdy2



for k in range(1, nb_steps, 1):

   #

   IncrementStep()

   ComputeFext()
   print ("Time step = ",k)
   #### Update of applied force on right and up wall #######

   vector = RBDY2_GetBodyVector("Coor_", body_down)

   ymin = vector[1] + Rmax

   vector = RBDY2_GetBodyVector("Coor_", body_up)

   ymax = vector[1] - Rmax

   vector = RBDY2_GetBodyVector("Coor_", body_left)

   xmin = vector[0] + Rmax

   vector = RBDY2_GetBodyVector("Coor_", body_right)

   xmax = vector[0] - Rmax



   Fwall_up    = sigma_0 * abs( xmax-xmin )

   Fwall_right = sigma_0 * abs( ymax-ymin )



   RBDY2_PutBodyVector("Fext_", body_up, [0,-Fwall_up,0])

   RBDY2_PutBodyVector("Fext_", body_right, [-Fwall_right,0,0])

   ########

   ComputeBulk()

   ComputeFreeVelocity()

   #

   SelectProxTactors(freq_detect)

   #

   RecupRloc()

   nlgs_ExSolver(type,norm,tol,relax,gs_it1,gs_it2)

   StockRloc()

   #

   ComputeDof()

   UpdateStep()

   #

   WriteOutDof(freq_outFiles)

   WriteOutVlocRloc(freq_outFiles)

   #

   ### post2D ###

   WriteDisplayFiles(freq_display,ref_radius)

   #WritePostproFiles()

#

#############

### FIN DU CALCUL ###

#############



CloseDisplayFiles()

#ClosePostproFiles()

