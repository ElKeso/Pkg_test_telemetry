#include "ros/ros.h"
#include "geometry_msgs/Pose.h"
#include "math.h"

int flag_ver = 0;
int flag_hor = 0;
int flag_angle = 0;
int a=1;

int main(int argc, char **argv){
  ros::init(argc, argv, "virtual_fly_w");
  ros::NodeHandle nh;
  ros::Publisher fly_pub = nh.advertise<geometry_msgs::Pose>("/Drone/pose", 1000);
  ros::Rate loop_rate(2);
  geometry_msgs::Pose ref;
  ref.orientation.x = 0;
  while (ros::ok()){
    for(int i=0; i<=360; i=i+a){
      ref.orientation.w = i;
      if(i==0){
        a=1;
      }
      if(i==360){
        a=-1;
      }
      fly_pub.publish(ref);
      loop_rate.sleep();
    }
    ros::spinOnce();
    loop_rate.sleep();
    }   
  return 0;
}