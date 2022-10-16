#include <pluginlib/class_list_macros.h>
#include <nodelet/nodelet.h>

#include <ros/ros.h>
#include <std_msgs/String.h>
#include <stdio.h>


namespace nodelet_exercise
{

class Hello : public nodelet::Nodelet
{

private:
	virtual void onInit()
	{
		ros::NodeHandle& private_nh = getPrivateNodeHandle();
		NODELET_DEBUG("Initialized the Nodelet");
		pub = private_nh.advertise<std_msgs::String>("msg_out",5);
		sub = private_nh.subscribe("msg_in",5, &Hello::callback, this);
	}
	
	void callback(const std_msgs::StringConstPtr input)
	{
		std_msgs::String output;
		output.data = input->data;

		NODELET_DEBUG("Message data = %s",output.data.c_str());
		ROS_INFO("Message data = %s",output.data.c_str());
		pub.publish(output);		
	}

  ros::Publisher pub;
  ros::Subscriber sub;

};

}

PLUGINLIB_EXPORT_CLASS(nodelet_exercise::Hello, nodelet::Nodelet);

