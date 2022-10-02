#include <Servo.h> 
#include <ros.h>
#include <std_msgs/UInt16.h>
#include <std_msgs/String.h>

ros::NodeHandle  nh;

Servo servo;

int angles[] = {45,80,115,140};
int led[] = {24,26,28,30};
bool state[] = {0,0,0,0};

void open_cb(const std_msgs::UInt16& cmd_msg){
  if (cmd_msg.data >= 0 && cmd_msg.data <= 3) {
    bool newState = !(state[cmd_msg.data]);
    servo.write(angles[cmd_msg.data]); //set servo angle
    state[cmd_msg.data] = newState;
  }
}


ros::Subscriber<std_msgs::UInt16> sub("locker_open", open_cb);
std_msgs::String str_msg;
ros::Publisher chatter("locker_state", &str_msg);


void check_if_on(bool state[]){
   //checar q casilleros estan abiertos y publicarlo
   if (state[0]){
    str_msg.data = "Locker 0 is open";
    chatter.publish( &str_msg );
    digitalWrite(24, HIGH);
   }
   else{
    digitalWrite(24, LOW);
   }
   if (state[1]){
    str_msg.data = "Locker 1 is open";
    chatter.publish( &str_msg );
    digitalWrite(26, HIGH);
   }
   else{
    digitalWrite(26, LOW);
   }
   if (state[2]){
    str_msg.data = "Locker 2 is open";
    chatter.publish( &str_msg );
    digitalWrite(28, HIGH);
   }
   else{
    digitalWrite(28, LOW);
   }
   if (state[3]){
    str_msg.data = "Locker 3 is open";
    chatter.publish( &str_msg );
    digitalWrite(30, HIGH);
   }
   else{
    digitalWrite(30, LOW);
   }
}

void setup(){
  pinMode(24, OUTPUT);
  pinMode(26, OUTPUT);
  pinMode(28, OUTPUT);
  pinMode(30, OUTPUT);
  
  nh.initNode();
  nh.subscribe(sub);
  nh.advertise(chatter);
  servo.attach(9); //attach it to pin 9
}

void loop(){
  check_if_on(state);
  nh.spinOnce();
  delay(1);
}
