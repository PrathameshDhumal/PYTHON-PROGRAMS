##############################################################
#
#Author:Prathamesh Dhumal
#Date:5/7/21
#About:Application of Reinforcement Machine Learning
#
##############################################################

import random
from typing import List

#Environment Class : Its a model of the world which is external to the agent.
                     #It provides observations and reqards to agent                        
class SampleEnvironment:
    def __init__(self):
        self.steps_left =20
    
    def get_observations(self)->List[float]:
        return[0.0,0.0,0.0]
    
    def get_actions(self)->List[int]:
        return[0,1]
    
    def is_done(self)->bool:
        return self.steps_left == 0

    def action(self,action :int)->float:
        if self.is_done():
            raise Exception("Game Over")
        self.steps_left -=1
        return random.random();

#Agent Class : A thing or person that tries to get rewards by interactions
#(Pie of code that implement some policy)
class Agent:
    def __init__(self):
        self.total_reward =0.0
    #Steps Function accept environment instance
        #1:Observe the environment 
        #2:Make decision about action based on observations
        #3:Submit the action to environment
        #4:Get the reward for current step
    def step(self,env : SampleEnvironment):
        current_obs = env.get_observations()
        print("Observations {}".format(current_obs))
        action = env.get_actions()
        print(action)
        reward = env.action(random.choice(action))
        self.total_reward += reward
        print("Total reward {}".format(self.total_reward))

def main():
    print("________________Reinforcement Machine Learning_____________")
    env =SampleEnvironment()
    agent=Agent()
    i=0

    while not env.is_done():
        i+=1
        print("Step no {}". format(i))
        agent.step(env)
    print("Total reward got : %.4f" %agent.total_reward)

if __name__ =="__main__":
    main()