# Integration Challenge | RoBorregos Candidates 2022

## Development team

| Name                    | Email                                                               | Github                                                       | Role      |
| ----------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------ | --------- |
| José Cisneros | [A01283070@itesm.mx](mailto:A01283070@itesm.mx) | [@Josecisneros001](https://github.com/Josecisneros001) | PM & Programmer |
| Kevin Vega | [vegakevinrdz@gmail.com](mailto:vegakevinrdz@gmai.com) | [@KevinVegaTec](https://github.com/KevinVegaTec)   | PM & Programmer  |


## Env setup
1. Install ROS Noetic : [Reference](http://wiki.ros.org/noetic/Installation/Ubuntu)

## Installation

1. **IMPORTANT: Fork the repository into your account**

2. Clone the project repository on your local machine.

HTTP:
``` bash
$ git clone https://github.com/your-username/Candidates-2022.git
```

SSH:
``` bash 
$ git clone git@github.com:your-username/Candidates-2022.git
```
**Be sure to be in the Integration Challenge Branch**

GetObject and GetTarget services are done in the challenge_ws

<img src='Reto Integracion CD2022.jpg' width="1000"/>

The following system opens or closes a locker in a storing system. It does it by receiving an ID and checking if it matches one of the IDs of the stored objects. If it does it opens the corresponding locker.

Tasks:
1. Develop the Navigation ActionServer
2. Develop the Speech ActionServer
3. Develop the Vision ActionServer and the GetInfo service
4. Develop the Store ActionServer, the Linear Actuator Service and do the phisical implementation with a microcontroller

*For building the workspace, the catkin build command from sudo apt-get install python3-catkin-tools was used.
**The Arduino must be connected in the following way:

Guide to run:
1. Connect the Arduino with the servo_ros.ino to the "Port Name" port in the computer.
*in each terminal you have to run the source devel/setup.bash
2. Run rosrun manager getInfo.py
3. Run rosrun manager getObject.py
4. Run rosrun manager speech.py
5. Run rosrun manager getTarget.py
6. Run rosrun manager vision.py
7. Run rosrun manager navigation.py
8. rosrun rosserial_python serial_node.py /dev/"Port Name"
9. Run rosrun manager store.py
10. Run rosrun manager mainEngine.py

In the main engine, put 1 if you wish to open a locker and the id of the object you wish to obtain. 

  ID      Object
'12345': 'Arduino',
'22453': 'Puente H',
'31512': 'Motor',
'62232': 'LED',

Use "q" when asked if you want to open a locker for quitting the main engine.

## References
- [actionlib](http://wiki.ros.org/actionlib)
- [ROS Services](http://wiki.ros.org/Services)
- [rosserial](http://wiki.ros.org/rosserial)


