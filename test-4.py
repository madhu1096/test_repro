 def reward_function(params):
    ###############################################################################
    '''
    Example of using waypoints and heading to make the car in the right direction
    '''

    import math

    # Read input variables
    waypoints = params['waypoints']
    closest_waypoints = params['closest_waypoints']
    heading = params['heading']

    # Initialize the reward with typical value 
    reward = 1.0

    # Calculate the direction of the center line based on the closest waypoints
    next_point = waypoints[closest_waypoints[1]]
    prev_point = waypoints[closest_waypoints[0]]

    # Calculate the direction in radius, arctan2(dy, dx), the result is (-pi, pi) in radians
    track_direction = math.atan2(next_point[1] - prev_point[1], next_point[0] - prev_point[0]) 
    # Convert to degree
    track_direction = math.degrees(track_direction)

    # Calculate the difference between the track direction and the heading direction of the car
    direction_diff = abs(track_direction - heading)
    if direction_diff > 180:
        direction_diff = 360 - direction_diff

    # Penalize the reward if the difference is too large
    DIRECTION_THRESHOLD = 10.0
    if direction_diff > DIRECTION_THRESHOLD:
        reward *= 0.5

    return reward



Completion.. 19.4secs




def reward_function(params):  

 all_wheels_on_track = params['all_wheels_on_track']
 track_width = params['track_width']
 distance_from_center = params['distance_from_center']
 # Penalize if the car is too far away from the center
 marker_1 = 0.1 * track_width
 marker_2 = 0.25 * track_width
 marker_3 = 0.4 * track_width
 marker_4 = 0.65 * track_width
 speed = params['speed']
 SPEED_TRESHOLD = 2
 if distance_from_center <= marker_1:
	 reward = 1.0
 elif distance_from_center <= marker_2:
	 reward = 0.3
 elif distance_from_center <= marker_3:
	 reward = 0.8
 elif distance_from_center <= marker_4:
	 reward = 0.05
 else:
	 reward = 1e-3  

 if not (all_wheels_on_track):
        reward = 1e-3  

 return float(reward)
 
Speed = 2m/s
Granularity = 2

Completed around 15secs but not trained properly// getiing more offtrcak



def reward_function(params):  

 all_wheels_on_track = params['all_wheels_on_track']
 track_width = params['track_width']
 distance_from_center = params['distance_from_center']
 # Penalize if the car is too far away from the center
 marker_1 = 0.1 * track_width
 marker_2 = 0.25 * track_width
 marker_3 = 0.4 * track_width
 marker_4 = 0.65 * track_width
 is_left_of_center = params['is_left_of_center']
 progress = params['progress']
 if  is_left_of_center:
	 if distance_from_center <= marker_1:
		 reward = 1.0
	 elif distance_from_center <= marker_2:
		 reward = 0.8
	 elif distance_from_center <= marker_3:
		 reward = 0.2
	 elif distance_from_center <= marker_4:
		 reward = 0.01
	 else:
		 reward = 1e-3  
 else:
	 if distance_from_center <= marker_1:
		 reward = 1.0
	 elif distance_from_center <= marker_2:
		 reward = 0.9
	 elif distance_from_center <= marker_3:
		 reward = 0.3
	 elif distance_from_center <= marker_4:
		 reward = 0.01
	 else:
		 reward = 1e-5  

 if progress == 100:
        reward += 100


 if not (all_wheels_on_track):
        reward = 1e-5 

 return float(reward) 



Speed - 2m/s
Granul - 3

Performs good but no money
