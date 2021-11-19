# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 12:03:07 2021

@author: shalu
"""
import math
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d 

class LineFormation:
    
    
    def checkboundary(leader_goal: list):
        x_limits = [-1.8,1.8]
        y_limits = [-2.8,2.8]
        z_limits = [0.3,2.3]
        
        l = leader_goal 
        
        if ( (l[0] < x_limits[0] or l[0] > x_limits[1]) or
             (l[1] < y_limits[0] or l[1] > y_limits[1]) or 
             (l[2] < z_limits[0] or l[2] > z_limits[1]) ):
            return False
        else:
            return True
        c
    
    def form(min_dist_x: float, min_dist_y: float, min_dist_z: float, uav_pos: list) -> list:
        

        error = []
        #print("No of Drones: ", len(uav_pos))
        # first drone is used to drive
        
        number_of_drones = len(uav_pos)
        #print(number_of_drones)
        
        #leader Position
        x = uav_pos[0][0] + (number_of_drones-1) * min_dist_x 
        y = uav_pos[0][1] + (number_of_drones-1) * min_dist_y
        z = uav_pos[0][2] + (number_of_drones-1) * min_dist_z
    
        #print(x,y,z)    
        #go_ahead = LineFormation.checkboundary([x,y,z])
        go_ahead = True
        
        if go_ahead == False:
            
            print("The Formation is gonna hit the Walls")
            print("Choose within the boundary limits, flight area is about 4x6x2.5 m^3")
            
        elif go_ahead == True: 
            
            for i in range(len(uav_pos) - 1):
                
                uav_x = uav_pos[0][0] - uav_pos[i+1][0] + min_dist_x*(i+1)
                uav_y = uav_pos[0][1] - uav_pos[i+1][1] + min_dist_y*(i+1)
                uav_z = uav_pos[0][2] - uav_pos[i+1][2] + min_dist_z*(i+1)
                
                error.append([uav_x, uav_y, uav_z])
            return error
    
    
    
    
    def rotation(uav_pos: list, min_dist: float):
        # Returs the position of the leader drone on circumference
        midpoint = uav_pos[1] 
        #radius = min_dist
        
        original_dist = math.sqrt( (midpoint[0]-uav_pos[0][0])**2 + (midpoint[1]-uav_pos[0][1])**2 )
        print("Original Dist: ", original_dist)
        new_pos_x = uav_pos[0][0] + 0.1
        new_pos_y = uav_pos[0][1] + 0.1
        
        print("new_pos_x = ",new_pos_x )
        print("new_pos_y = ",new_pos_y )
        
        # Dist from Center
        dist = math.sqrt( (midpoint[0]-new_pos_x)**2 + (midpoint[1]-new_pos_y)**2 )
        print("adjacent: ", dist)

        dist_bw_pos = math.sqrt( 2*0.1**2 )
        
        print("step Dist: ", dist_bw_pos)
        theta = math.atan(dist_bw_pos/dist)
        print("theta: ", theta)
        relative_dist = min_dist - dist
        print("relative dist: ", relative_dist)

        add_x = math.sin(theta)*relative_dist
        add_y = math.cos(theta)*relative_dist
        
        print("after adding: ",new_pos_x+add_x)
        print("after addinng: ",new_pos_y+add_y)
        
        return [new_pos_x + add_x, new_pos_y + add_y, uav_pos[0][2]]
    
    def full_rotation(uav_pos: list, min_dist: float):
        
        
    # This method returns the trajectory of leader during the full rotation
    # i.e 360 degrees, given the starting position of all the drones
        theta = 1
        start_pos = uav_pos
        print("leader Pos: ",start_pos)
        traj = []
        while theta < 384:    
        #print(theta)
            tta = round(theta/60, 3)
            #print("theta: ", theta)
            #print(tta)
            add_x = round( math.sin(tta)*min_dist, 2)
            #print(add_x)
            add_y = round( math.cos(tta)*min_dist, 2)  
            #print(add_y)
            
            if tta < 1.5:   

                leader_pos = [start_pos[0] + add_x, start_pos[1] + min_dist - add_y, start_pos[2]]
                #print('1',leader_pos)
                traj.append(leader_pos)
            
            elif tta > 1.4 and tta < 3.1:

                leader_pos = [start_pos[0] + add_x, start_pos[1] + min_dist - add_y, start_pos[2]]
                #print('2',leader_pos)
                traj.append(leader_pos)
    
            elif tta > 3.0 and tta < 4.7:

                leader_pos = [start_pos[0] + add_x, start_pos[1] + min_dist - add_y, start_pos[2]]
                #print('3',leader_pos)
                traj.append(leader_pos)
            
            elif tta > 4.6 and tta < 6.4:

                leader_pos = [start_pos[0] + add_x, start_pos[1] + min_dist - add_y, start_pos[2]]
                #print('4',leader_pos)
                traj.append(leader_pos)
            
            theta += 1
        return traj
        
  
        

        
        
class Character:
    
    def __init__(self):
        
        self.x_limits = [-1.8,1.8]
        self.y_limits = [-2.8,2.8]
        self.z_limits = [0.3,2.3]
        
        
        x_limits = self.x_limits
        y_limits = self.y_limits
        z_limits = self.z_limits
        
    def final_positions(uav_pos: list, error: list):
        
        """
        Description:
            
            This method calculates the final positions of uav's
            based on the error calculated from shape vectors.
        """
        
        goal = []
        
        for i in range(len(error)):
            
            x = round((uav_pos[i+1][0] + error[i][0]), 3)
            y = round((uav_pos[i+1][1] + error[i][1]), 3)
            z = round((uav_pos[i+1][2] + error[i][2]), 3)
            
            goal.append([x,y,z])
          
        return goal
        

    def form_cross(uav_pos: list):
        
        """
        Description:range(len(
            
            This method returns the final position of the 
            drones of a formation shaped "cross" with exactly 
            6 drones.
            
            if you want to use more drones, update their shape vectors
        
        """
        if len(uav_pos) < 5:
            print("Need atleast 6 Drones to perform Cross formation")
            
        else:
            
            error = []
            shape_vect = [[0, 0.6, 0], [0, -0.6, 0], [0.5, 0, -0.3], [-0.4, 0, 0.5]] 
            for i in range(len(uav_pos) - 1):
                
                x = uav_pos[0][0] - uav_pos[i+1][0] - shape_vect[i][0]
                y = uav_pos[0][1] - uav_pos[i+1][1] - shape_vect[i][1]
                z = uav_pos[0][2] - uav_pos[i+1][2] - shape_vect[i][2]
                
                error.append([x,y,z])
            #print("Erro b/w shape: ",error)
            
            PID_Array = Character.final_positions(uav_pos, error)
            
            return PID_Array
    
    def form_A(uav_pos: list):
        
        if len(uav_pos) < 6:
            print("Insufficient number of Drones")
            
        else:
            leader = uav_pos[0]
            
            # Predefined Shape Vector
            shape_vector = [[-0.2,0.5,0.5], [0,0.2,0], [0.2,0,-0.5], [0,-0.2,0], [-0.2,-0.5,0.5]]
            
            error = []
            for i in range(len(shape_vector)):
                
                x = uav_pos[i][0] + shape_vector[i][0]
                y = uav_pos[i][1] + shape_vector[i][1]
                z = uav_pos[i][2] + shape_vector[i][2]
                error.append([x,y,z])
            return error
        
        
    def form_I(uav_pos: list, leader_pos: list, min_dist = [0.6,0.6,0.4]):
        
        if len(uav_pos) < 2:
            
            print("Atleast 2 drones are required to form shape I")
        
        else:
            
            shape_vect = []
            shape_vect.append(leader_pos)
            for i in range(len(uav_pos) - 1):
                
                uav_x = leader_pos[0] - min_dist[0]*(i+1)
                uav_y = leader_pos[1] 
                uav_z = leader_pos[2] + min_dist[2]*(i+1)
                
                shape_vect.append([uav_x,uav_y,uav_z])
                    
            #for g in range(len(uav_pos)):
            #print("Shape_Vect: ", shape_vect)
            goal_position = path_planning.give_position(uav_pos, shape_vect)            
            return goal_position
 
       
    def form_L(uav_pos: list, leader_pos: list, min_dist = [0.6,0.6,0.4]):
        
        if len(uav_pos) < 3:
            
            print("Atleast 3 drones are required to form shape I")
        
        else:
            
            shape_vect = []
            shape_vect.append(leader_pos)
            for i in range(len(uav_pos) - 2):
                
                uav_x = leader_pos[0] - min_dist[0]*(i+1)
                uav_y = leader_pos[1] 
                uav_z = leader_pos[2] + min_dist[2]*(i+1)
                
                shape_vect.append([uav_x,uav_y,uav_z])
            
            x = leader_pos[0] 
            y = leader_pos[1] + min_dist[2] + 0.1
            z = leader_pos[2] 
            shape_vect.append([x, y, z])
            #for g in range(len(uav_pos)):
            print("Shape_Vect: ", shape_vect)
            goal_position = path_planning.give_position(uav_pos, shape_vect)            
            return goal_position       
 
       
    def form_Square(uav_pos: list, leader_pos: list, min_dist = [0.6,0.6,0.45]):
        """

        
        """
        if len(uav_pos) < 4:
            
            print("Atleast 4 drones are required to form shape I")
        
        else:
            
            shape_vect = []
            shape_vect.append(leader_pos)
            #position1 = leader_pos
            position2 = [leader_pos[0] + 0.4, leader_pos[1], leader_pos[2]+ min_dist[2]*2]
            position3 = [leader_pos[0] + 0.4, leader_pos[1] + min_dist[1]+0.2, leader_pos[2]+ min_dist[2]*2]
            position4 = [leader_pos[0], leader_pos[1] + min_dist[1]+0.2, leader_pos[2]]

            shape_vect.append(position2)
            shape_vect.append(position3)
            shape_vect.append(position4)
            #for g in range(len(uav_pos)):
            print("Shape_Vect: ", shape_vect)
            goal_position = path_planning.give_position(uav_pos, shape_vect)            
            return goal_position        
        


class path_planning():

    def __init__(self):
        
        self.x_limits = [-1.8,1.8]
        self.y_limits = [-2.8,2.8]
        self.z_limits = [0.3,2.3]
        
        
        x_limits = self.x_limits
        y_limits = self.y_limits
        z_limits = self.z_limits
        
        
        
        
    def Hover(cur_pos:list, goal_pos: list):
        
        drone_list = []
        for d in goal_pos:
            if d[2] < 0.55 or d[2] > 1.5:
                pos = [round(d[0],3), round(d[1],3), 0.55]
            
            else:
                pos = [round(d[0],3), round(d[1],3), round(d[2],3)]
            
            drone_list.append(pos)
        goal_position = path_planning.give_position(cur_pos, drone_list) 
        
        return goal_position
    
    
    def give_position(current_pos: list, goal_pos: list):
        
        """
        This Function Calculates the distance between a drone 
        and the new positions in the formation for all the drones
        and returns the locations of min position to the corresponding
        drones in the list order.
        
        """
        min_dist = []
        for i in range(len(current_pos)):
            
            dist = []
            for j in range(len(goal_pos)):
                x_sq = (current_pos[i][0] - goal_pos[j][0])**2
                y_sq = (current_pos[i][1] - goal_pos[j][1])**2
                z_sq = (current_pos[i][2] - goal_pos[j][2])**2
                dist.append(math.sqrt(x_sq + y_sq + z_sq))
                
            min_dist.append(goal_pos[dist.index(min(dist))])
            goal_pos.pop(dist.index(min(dist)))
            
        return min_dist
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        


