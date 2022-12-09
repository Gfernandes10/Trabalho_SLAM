# Instalação

Primeiro passo:

instalar os pacotes desse repositório no seu workspace

Segundo passo:

Compilar seu workspace 


Terceiro Passo:

Seguir as recomendações desse repositório para a instalação do orb-slam
https://github.com/thien94/orb_slam3_ros_wrapper


# Executar AR Drone 2.0

Se você possuir um controle de ps4, conecte a porta USB e execute os seguintes comandos:

roslaunch ardrone_gazebo single_ardrone_joy.launch 

Pressione X para decolar o drone e "bola" para pousar.

movimente o drone através dos joysticks.

Se você não possuir um controle de ps4 execute os seguintes comandos:

roslaunch ardrone_gazebo single_ardrone_joy.launch 

rostopic pub /ardrone/takeoff std_msgs/Empty "{}" 

rosrun teleop_twist_keyboard teleop_twist_keyboard.py

Controle o drone pelos botões indicados no terminal do teleop_twist_keyboard

# Executar ORB-SLAM3

roslaunch orb_slam3_ros_wrapper euroc_mono.launch 

Obs: Movimente o drone para começar o mapeamento no ORB-SLAM.
