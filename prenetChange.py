#!/usr/bin/env python
# coding: utf-8

# # Deep Q learning with Doom 🕹️
# In this notebook we'll implement an agent <b>that plays Doom by using a Deep Q learning architecture.</b> <br>
# Our agent playing Doom:
# 
# <img src="https://raw.githubusercontent.com/simoninithomas/Deep_reinforcement_learning_Course/master/DQN%20Doom/assets/doom.gif" style="max-width: 600px;" alt="Deep Q learning with Doom"/>
# 

# # This is a notebook from Deep Reinforcement Learning Course with Tensorflow
# <img src="https://simoninithomas.github.io/Deep_reinforcement_learning_Course/assets/img/preview.jpg" alt="Deep Reinforcement Course" style="width: 500px;"/>
# 
# <p>  Deep Reinforcement Learning Course is a free series of blog posts and videos 🆕 about Deep Reinforcement Learning, where we'll learn the main algorithms, and how to implement them with Tensorflow.
# 
# 📜The articles explain the concept from the big picture to the mathematical details behind it.
# 
# 📹 The videos explain how to create the agent with Tensorflow </b></p>
# 
# ## <a href="https://simoninithomas.github.io/Deep_reinforcement_learning_Course/">Syllabus</a><br>
# ### 📜 Part 1: Introduction to Reinforcement Learning [ARTICLE](https://medium.freecodecamp.org/an-introduction-to-reinforcement-learning-4339519de419) 
# 
# ### Part 2: Q-learning with FrozenLake 
# #### 📜 [ARTICLE](https://medium.freecodecamp.org/diving-deeper-into-reinforcement-learning-with-q-learning-c18d0db58efe) // [FROZENLAKE IMPLEMENTATION](https://github.com/simoninithomas/Deep_reinforcement_learning_Course/blob/master/Q%20learning/Q%20Learning%20with%20FrozenLake.ipynb)
# #### 📹 [Implementing a Q-learning agent that plays Taxi-v2 🚕](https://youtu.be/q2ZOEFAaaI0) 
# 
# ### Part 3: Deep Q-learning with Doom
# #### 📜 [ARTICLE](https://medium.freecodecamp.org/an-introduction-to-deep-q-learning-lets-play-doom-54d02d8017d8)  //  [DOOM IMPLEMENTATION](https://github.com/simoninithomas/Deep_reinforcement_learning_Course/blob/master/DQN%20Doom/Deep%20Q%20learning%20with%20Doom.ipynb)
# #### 📹 [Create a DQN Agent that learns to play Atari Space Invaders 👾 ](https://youtu.be/gCJyVX98KJ4)
# 
# ### Part 3+: Improvments in Deep Q-Learning
# #### 📜 [ARTICLE (📅 JUNE)] 
# #### 📹 [Create an Agent that learns to play Doom Deadly corridor (📅 06/20 )] 
# 
# ### Part 4: Policy Gradients with Doom 
# #### 📜 [ARTICLE](https://medium.freecodecamp.org/an-introduction-to-policy-gradients-with-cartpole-and-doom-495b5ef2207f) //  [CARTPOLE IMPLEMENTATION](https://github.com/simoninithomas/Deep_reinforcement_learning_Course/blob/master/Policy%20Gradients/Cartpole/Cartpole%20REINFORCE%20Monte%20Carlo%20Policy%20Gradients.ipynb) // [DOOM IMPLEMENTATION](https://github.com/simoninithomas/Deep_reinforcement_learning_Course/blob/master/Policy%20Gradients/Doom/Doom%20REINFORCE%20Monte%20Carlo%20Policy%20gradients.ipynb)
# #### 📹 [Create an Agent that learns to play Doom deathmatch (📅 06/27)] 
# 
# ### Part 5: Advantage Advantage Actor Critic (A2C) 
# #### 📜 [ARTICLE (📅 June)] 
# #### 📹 [Create an Agent that learns to play Outrun (📅 07/04)] 
# 
# ### Part 6: Asynchronous Advantage Actor Critic (A3C) 
# #### 📜 [ARTICLE (📅 July)] 
# #### 📹 [Create an Agent that learns to play Michael Jackson's Moonwalker (📅 07/11)] 
# 
# ### Part 7: Proximal Policy Gradients 
# #### 📜 [ARTICLE (📅 July)]
# #### 📹 [Create an Agent that learns to play walk with Mujoco (📅 07/18)]
# 
# ### Part 8: TBA 
# 
# ## Any questions 👨‍💻
# <p> If you have any questions, feel free to ask me: </p>
# <p> 📧: <a href="mailto:hello@simoninithomas.com">hello@simoninithomas.com</a>  </p>
# <p> Github: https://github.com/simoninithomas/Deep_reinforcement_learning_Course </p>
# <p> 🌐 : https://simoninithomas.github.io/Deep_reinforcement_learning_Course/ </p>
# <p> Twitter: <a href="https://twitter.com/ThomasSimonini">@ThomasSimonini</a> </p>
# <p> Don't forget to <b> follow me on <a href="https://twitter.com/ThomasSimonini">twitter</a>, <a href="https://github.com/simoninithomas/Deep_reinforcement_learning_Course">github</a> and <a href="https://medium.com/@thomassimonini">Medium</a> to be alerted of the new articles that I publish </b></p>
#     
# ## How to help  🙌
# 3 ways:
# - **Clap our articles and like our videos a lot**:Clapping in Medium means that you really like our articles. And the more claps we have, the more our article is shared Liking our videos help them to be much more visible to the deep learning community.
# - **Share and speak about our articles and videos**: By sharing our articles and videos you help us to spread the word. 
# - **Improve our notebooks**: if you found a bug or **a better implementation** you can send a pull request.
# <br>
# 
# ## Important note 🤔
# <b> You can run it on your computer but it's better to run it on GPU based services</b>, personally I use Microsoft Azure and their Deep Learning Virtual Machine (they offer 170$)
# https://azuremarketplace.microsoft.com/en-us/marketplace/apps/microsoft-ads.dsvm-deep-learning
# <br>
# ⚠️ I don't have any business relations with them. I just loved their excellent customer service.
# 
# If you have some troubles to use Microsoft Azure follow the explainations of this excellent article here (without last the part fast.ai): https://medium.com/@manikantayadunanda/setting-up-deeplearning-machine-and-fast-ai-on-azure-a22eb6bd6429

# ## Step 1: Import the libraries 📚

# In[1]:


import tensorflow as tf      # Deep Learning library
import numpy as np           # Handle matrices
import gym
#from vizdoom import *        # Doom Environment

import random                # Handling random number generation
import time                  # Handling time calculation
from skimage import transform# Help us to preprocess the frames

from skimage import color
from collections import deque# Ordered collection with ends
import matplotlib.pyplot as plt # Display graphs
from skimage.measure import block_reduce
import warnings # This ignore all the warning messages that are normally printed during the training because of skiimage
warnings.filterwarnings('ignore') 


# ## Step 2: Create our environment 🎮
# - Now that we imported the libraries/dependencies, we will create our environment.
# - Doom environment takes:
#     - A `configuration file` that **handle all the options** (size of the frame, possible actions...)
#     - A `scenario file`: that **generates the correct scenario** (in our case basic **but you're invited to try other scenarios**).
# - Note: We have 3 possible actions `[[0,0,1], [1,0,0], [0,1,0]]` so we don't need to do one hot encoding (thanks to < a href="https://stackoverflow.com/users/2237916/silgon">silgon</a> for figuring out. 
# 
# ### Our environment
# <img src="assets/doom.png" style="max-width:500px;" alt="Doom"/>
#                                     
# - A monster is spawned **randomly somewhere along the opposite wall**. 
# - Player can only go **left/right and shoot**. 
# - 1 hit is enough **to kill the monster**. 
# - Episode finishes when **monster is killed or on timeout (300)**.
# <br><br>
# REWARDS:
# 
# - +101 for killing the monster 
# - -5 for missing 
# - Episode ends after killing the monster or on timeout.
# - living reward = -1

# In[2]:


#"""
#Here we create our environment
#"""
#def create_environment():
    #game = DoomGame()
    
    # Load the correct configuration
    #game.load_config("basic.cfg")
    
    # Load the correct scenario (in our case basic scenario)
    #game.set_doom_scenario_path("basic.wad")
    
    #game.init()
    
    # Here our possible actions
    #left = [1, 0, 0]
    #right = [0, 1, 0]
    #shoot = [0, 0, 1]
    #possible_actions = [left, right, shoot]
    
    #return game, possible_actions
       
#"""
#Here we performing random action to test the environment
#"""
def test_environment():
    game = DoomGame()
    game.load_config("basic.cfg")
    game.set_doom_scenario_path("basic.wad")
    game.init()
    shoot = [0, 0, 1]
    left = [1, 0, 0]
    right = [0, 1, 0]
    actions = [shoot, left, right]

    episodes = 10
    for i in range(episodes):
        game.new_episode()
        while not game.is_episode_finished():
            state = game.get_state()
            img = state.screen_buffer
            misc = state.game_variables
            action = random.choice(actions)
            print(action)
            reward = game.make_action(action)
            print ("\treward:", reward)
            time.sleep(0.02)
        print ("Result:", game.get_total_reward())
        time.sleep(2)
    game.close()


# In[3]:

game= gym.make('Phoenix-v0')
possible_actions = np.array(np.identity(game.action_space.n,dtype=int).tolist())
#game, possible_actions = create_environment()


# ## Step 3: Define the preprocessing functions ⚙️
# ### preprocess_frame
# Preprocessing is an important step, <b>because we want to reduce the complexity of our states to reduce the computation time needed for training.</b>
# <br><br>
# Our steps:
# - Grayscale each of our frames (because <b> color does not add important information </b>). But this is already done by the config file.
# - Crop the screen (in our case we remove the roof because it contains no information)
# - We normalize pixel values
# - Finally we resize the preprocessed frame

# In[4]:


"""
    preprocess_frame:
    Take a frame.
    Resize it.
        __________________
        |                 |
        |                 |
        |                 |
        |                 |
        |_________________|
        
        to
        _____________
        |            |
        |            |
        |            |
        |____________|
    Normalize it.
    
    return preprocessed_frame
    
    """
def preprocess_frame(frame):
    # Greyscale frame already done in our vizdoom config
    # x = np.mean(frame,-1)
    gray=color.rgb2gray(frame) 
    cropped_frame = gray[22:-28,:]
    #print(cropped_frame.shape)
    downscale=block_reduce(cropped_frame,block_size=(2,2),func=np.mean)
    downscale[downscale<.1]=0
    downscale[downscale>=.1]=255
    
    # Normalize Pixel Values
    #normalized_frame = cropped_frame/255.0
    
    # Resize
    #preprocessed_frame = transform.resize(normalized_frame, [84,84])
    #plt.imshow(downscale,interpolation='nearest')
    #plt.show()
    return downscale


# ### stack_frames
# 👏 This part was made possible thanks to help of <a href="https://github.com/Miffyli">Anssi</a><br>
# 
# As explained in this really <a href="https://danieltakeshi.github.io/2016/11/25/frame-skipping-and-preprocessing-for-deep-q-networks-on-atari-2600-games/">  good article </a> we stack frames.
# 
# Stacking frames is really important because it helps us to **give have a sense of motion to our Neural Network.**
# 
# - First we preprocess frame
# - Then we append the frame to the deque that automatically **removes the oldest frame**
# - Finally we **build the stacked state**
# 
# This is how work stack:
# - For the first frame, we feed 4 frames
# - At each timestep, **we add the new frame to deque and then we stack them to form a new stacked frame**
# - And so on
# <img src="https://raw.githubusercontent.com/simoninithomas/Deep_reinforcement_learning_Course/master/DQN/Space%20Invaders/assets/stack_frames.png" alt="stack">

# In[5]:


stack_size = 4 # We stack 4 frames

# Initialize deque with zero-images one array for each image
stacked_frames  =  deque([np.zeros((80,80), dtype=np.int) for i in range(stack_size)], maxlen=4) 

def stack_frames(stacked_frames, state, is_new_episode):
    # Preprocess frame
    frame = preprocess_frame(state)
    
    if is_new_episode:
        # Clear our stacked_frames
        stacked_frames = deque([np.zeros((80,80), dtype=np.int) for i in range(stack_size)], maxlen=4)
        
        # Because we're in a new episode, copy the same frame 4x
        stacked_frames.append(frame)
        stacked_frames.append(frame)
        stacked_frames.append(frame)
        stacked_frames.append(frame)
        
        # Stack the frames
        stacked_state = np.stack(stacked_frames, axis=2)
        
    else:
        # Append frame to deque, automatically removes the oldest frame
        stacked_frames.append(frame)

        # Build the stacked state (first dimension specifies different frames)
        stacked_state = np.stack(stacked_frames, axis=2) 
    
    return stacked_state, stacked_frames


# ## Step 4: Set up our hyperparameters ⚗️
# In this part we'll set up our different hyperparameters. But when you implement a Neural Network by yourself you will **not implement hyperparamaters at once but progressively**.
# 
# - First, you begin by defining the neural networks hyperparameters when you implement the model.
# - Then, you'll add the training hyperparameters when you implement the training algorithm.

# In[6]:


### MODEL HYPERPARAMETERS
state_size = [80,80,4]      # Our input is a stack of 4 frames hence 84x84x4 (Width, height, channels) 
action_size = game.action_space.n              # 3 possible actions: left, right, shoot
learning_rate =  0.0002      # Alpha (aka learning rate)

### TRAINING HYPERPARAMETERS
total_episodes = 50000        # Total episodes for training
max_steps = 50000              # Max possible steps in an episode
batch_size = 64             

# Exploration parameters for epsilon greedy strategy
explore_start = 1.0            # exploration probability at start
explore_stop = 0.01            # minimum exploration probability 
decay_rate = 0.00001            # exponential decay rate for exploration prob

# Q learning hyperparameters
gamma = 0.95               # Discounting rate

### MEMORY HYPERPARAMETERS
pretrain_length = batch_size*100   # Number of experiences stored in the Memory when initialized for the first time
memory_size = 1000000          # Number of experiences the Memory can keep

### MODIFY THIS TO FALSE IF YOU JUST WANT TO SEE THE TRAINED AGENT
training = True

## TURN THIS TO TRUE IF YOU WANT TO RENDER THE ENVIRONMENT
episode_render = False


# ## Step 5: Create our Deep Q-learning Neural Network model 🧠
# <img src="https://raw.githubusercontent.com/simoninithomas/Deep_reinforcement_learning_Course/master/DQN/doom/assets/model.png" alt="Model" />
# This is our Deep Q-learning model:
# - We take a stack of 4 frames as input
# - It passes through 3 convnets
# - Then it is flatened
# - Finally it passes through 2 FC layers
# - It outputs a Q value for each actions

# In[7]:


class DQNetwork:
    def __init__(self, state_size, action_size, learning_rate, name='DQNetwork'):
        self.state_size = state_size
        self.action_size = action_size
        self.learning_rate = learning_rate
        
        with tf.variable_scope(name):
            # We create the placeholders
            # *state_size means that we take each elements of state_size in tuple hence is like if we wrote
            # [None, 84, 84, 4]
            self.inputs_ = tf.placeholder(tf.float32, [None, 80,80,4], name="inputs")
            self.actions_ = tf.placeholder(tf.float32, [None, 8], name="actions_")
            
            # Remember that target_Q is the R(s,a) + ymax Qhat(s', a')
            self.target_Q = tf.placeholder(tf.float32, [None], name="target")
            
            """
            First convnet:
            CNN
            BatchNormalization
            ELU
            """
            # Input is 84x84x4
            self.conv1 = tf.layers.conv2d(inputs = self.inputs_,
                                         filters = 32,
                                         kernel_size = [8,8],
                                         strides = [4,4],
                                         padding = "VALID",
                                          kernel_initializer=tf.contrib.layers.xavier_initializer_conv2d(),
                                         name = "conv1")
            
            self.conv1_batchnorm = tf.layers.batch_normalization(self.conv1,
                                                   training = True,
                                                   epsilon = 1e-5,
                                                     name = 'batch_norm1')
            
            self.conv1_out = tf.nn.elu(self.conv1_batchnorm, name="conv1_out")
            ## --> [20, 20, 32]
            
            
            """
            Second convnet:
            CNN
            BatchNormalization
            ELU
            """
            self.conv2 = tf.layers.conv2d(inputs = self.conv1_out,
                                 filters = 64,
                                 kernel_size = [4,4],
                                 strides = [2,2],
                                 padding = "VALID",
                                kernel_initializer=tf.contrib.layers.xavier_initializer_conv2d(),
                                 name = "conv2")
        
            self.conv2_batchnorm = tf.layers.batch_normalization(self.conv2,
                                                   training = True,
                                                   epsilon = 1e-5,
                                                     name = 'batch_norm2')

            self.conv2_out = tf.nn.elu(self.conv2_batchnorm, name="conv2_out")
            ## --> [9, 9, 64]
            
            
            """
            Third convnet:
            CNN
            BatchNormalization
            ELU
            """
            #self.conv3 = tf.layers.conv2d(inputs = self.conv2_out,
            #                     filters = 128,
            #                     kernel_size = [4,4],
            #                     strides = [2,2],
            #                     padding = "VALID",
            #                    kernel_initializer=tf.contrib.layers.xavier_initializer_conv2d(),
            #                     name = "conv3")
            #
            #self.conv3_batchnorm = tf.layers.batch_normalization(self.conv3,
            #                                       training = True,
            #                                       epsilon = 1e-5,
            #                                         name = 'batch_norm3')
            #
            #self.conv3_out = tf.nn.elu(self.conv3_batchnorm, name="conv3_out")
            ## --> [3, 3, 128]
            #
            # 
            self.flatten = tf.layers.flatten(self.conv2_out)
            # --> [1152]
            
            
            self.fc = tf.layers.dense(inputs = self.flatten,
                                  units = 512,
                                  activation = tf.nn.elu,
                                       kernel_initializer=tf.contrib.layers.xavier_initializer(),
                                name="fc1")
            
            
            self.output = tf.layers.dense(inputs = self.fc, 
                                           kernel_initializer=tf.contrib.layers.xavier_initializer(),
                                          units = 8, 
                                        activation=None)

  
            # Q is our predicted Q value.
            self.Q = tf.reduce_sum(tf.multiply(self.output, self.actions_), axis=1)
            
            
            # The loss is the difference between our predicted Q_values and the Q_target
            # Sum(Qtarget - Q)^2
            self.loss = tf.reduce_mean(tf.square(self.target_Q - self.Q))
            
            self.optimizer = tf.train.RMSPropOptimizer(self.learning_rate).minimize(self.loss)


# In[8]:


# Reset the graph
tf.reset_default_graph()

# Instantiate the DQNetwork
DQNetwork = DQNetwork(state_size, action_size, learning_rate)


# ## Step 6: Experience Replay 🔁
# Now that we create our Neural Network, **we need to implement the Experience Replay method.** <br><br>
# Here we'll create the Memory object that creates a deque.A deque (double ended queue) is a data type that **removes the oldest element each time that you add a new element.**
# 
# This part was taken from Udacity : <a href="https://github.com/udacity/deep-learning/blob/master/reinforcement/Q-learning-cart.ipynb" Cartpole DQN</a>

# In[9]:


class Memory():
    def __init__(self, max_size):
        self.buffer = deque(maxlen = max_size)
    
    def add(self, experience):
        self.buffer.append(experience)
    
    def sample(self, batch_size):
        buffer_size = len(self.buffer)
        index = np.random.choice(np.arange(buffer_size),
                                size = batch_size,
                                replace = False)
        
        return [self.buffer[i] for i in index]


# Here we'll **deal with the empty memory problem**: we pre-populate our memory by taking random actions and storing the experience (state, action, reward, new_state).

# In[10]:


# Instantiate memory
memory = Memory(max_size = memory_size)

# Render the environment
game.reset()

for i in range(pretrain_length):
    # If it's the first step
    if i == 0:
        # First we need a state
        state = game.reset()
        state, stacked_frames = stack_frames(stacked_frames, state, True)
    
    # Random action
    choice=random.randint(1,len(possible_actions))-1
    action= possible_actions[choice]
    #action = random.choice(possible_actions)

    next_state, reward,done,_ = game.step(choice)
    # Get the rewards
    
    #reward = game.make_action(action)
    
    # Look if the episode is finished
    #done = game.is_episode_finished()
    
    # If we're dead
    if done:
        # We finished the episode
        next_state = np.zeros(state.shape)
        
        # Add experience to memory
        memory.add((state, action, reward, next_state, done))
        
        # Start a new episode
        state=game.reset()
        
        # First we need a state
        #state = game.get_state().screen_buffer
        
        # Stack the frames
        state, stacked_frames = stack_frames(stacked_frames, state, True)
        
    else:
        # Get the next state
        #next_state = game.get_state().screen_buffer
        next_state, stacked_frames = stack_frames(stacked_frames, next_state, False)
        
        # Add experience to memory
        memory.add((state, action, reward, next_state, done))
        
        # Our state is now the next_state
        state = next_state
print("Memory Ready")
# ## Step 7: Set up Tensorboard 📊
# For more information about tensorboard, please watch this <a href="https://www.youtube.com/embed/eBbEDRsCmv4">excellent 30min tutorial</a> <br><br>
# To launch tensorboard : `tensorboard --logdir=/tensorboard/dqn/1`

# In[11]:


# Setup TensorBoard Writer
writer = tf.summary.FileWriter("tensorboard/dqn/2")

## Losses
tf.summary.scalar("Loss", DQNetwork.loss)

write_op = tf.summary.merge_all()


# ## Step 8: Train our Agent 🏃‍♂️
# 
# Our algorithm:
# <br>
# * Initialize the weights
# * Init the environment
# * Initialize the decay rate (that will use to reduce epsilon) 
# <br><br>
# * **For** episode to max_episode **do** 
#     * Make new episode
#     * Set step to 0
#     * Observe the first state $s_0$
#     <br><br>
#     * **While** step < max_steps **do**:
#         * Increase decay_rate
#         * With $\epsilon$ select a random action $a_t$, otherwise select $a_t = \mathrm{argmax}_a Q(s_t,a)$
#         * Execute action $a_t$ in simulator and observe reward $r_{t+1}$ and new state $s_{t+1}$
#         * Store transition $<s_t, a_t, r_{t+1}, s_{t+1}>$ in memory $D$
#         * Sample random mini-batch from $D$: $<s, a, r, s'>$
#         * Set $\hat{Q} = r$ if the episode ends at $+1$, otherwise set $\hat{Q} = r + \gamma \max_{a'}{Q(s', a')}$
#         * Make a gradient descent step with loss $(\hat{Q} - Q(s, a))^2$
#     * **endfor**
#     <br><br>
# * **endfor**
# 
#     

# In[12]:


"""
This function will do the part
With ϵ select a random action atat, otherwise select at=argmaxaQ(st,a)
"""
def predict_action(explore_start, explore_stop, decay_rate, decay_step, state, actions):
    ## EPSILON GREEDY STRATEGY
    # Choose action a from state s using epsilon greedy.
    ## First we randomize a number
    exp_exp_tradeoff = np.random.rand()

    # Here we'll use an improved version of our epsilon greedy strategy used in Q-learning notebook
    explore_probability = explore_stop + (explore_start - explore_stop) * np.exp(-decay_rate * decay_step)
    
    if (explore_probability > exp_exp_tradeoff):
        # Make a random action (exploration)
        action = random.choice(possible_actions)
        
    else:
        # Get action from Q-network (exploitation)
        # Estimate the Qs values state
        Qs = sess.run(DQNetwork.output, feed_dict = {DQNetwork.inputs_: state.reshape((1, 80,80,4))})
        
        # Take the biggest Q value (= the best action)
        choice = np.argmax(Qs)
        action = possible_actions[int(choice)]
                
    return action, explore_probability


# In[13]:


# Saver will help us to save our model
saver = tf.train.Saver()

if training == True:
    print("Training Started")
    with tf.Session() as sess:
        # Initialize the variables
        sess.run(tf.global_variables_initializer())
        
        # Initialize the decay rate (that will use to reduce epsilon) 
        decay_step = 0

        # Init the game
        game.reset()

        for episode in range(total_episodes):
            # Set step to 0
            step = 0
            
            # Initialize the rewards of the episode
            episode_rewards = []
            
            # Make a new episode and observe the first state
            state=game.reset()
            #state = game.get_state().screen_buffer
            
            # Remember that stack frame function also call our preprocess function.
            state, stacked_frames = stack_frames(stacked_frames, state, True)

            while step < max_steps:
                step += 1
                
                # Increase decay_step
                decay_step +=1
                
                # Predict the action to take and take it
                action, explore_probability = predict_action(explore_start, explore_stop, decay_rate, decay_step, state, possible_actions)
                choice=action.tolist().index(1)
                next_state,reward,done,_=game.step(choice)

                # Do the action
                #reward = game.make_action(action)
                
                # Look if the episode is finished
                #done = game.is_episode_finished()
                
                # Add the reward to total reward
                episode_rewards.append(reward)

                # If the game is finished
                if done:
                    # the episode ends so no next state
                    next_state = np.zeros((80,80), dtype=np.int)
                    next_state, stacked_frames = stack_frames(stacked_frames, next_state, False)

                    # Set step = max_steps to end the episode
                    step = max_steps

                    # Get the total reward of the episode
                    total_reward = np.sum(episode_rewards)

                    print('Episode: {}'.format(episode),
                              'Total reward: {}'.format(total_reward),
                              'Training loss: {:.4f}'.format(loss),
                              'Explore P: {:.4f}'.format(explore_probability))

                    memory.add((state, action, reward, next_state, done))

                else:
                    # Get the next state
                    #next_state = game.get_state().screen_buffer
                    
                    # Stack the frame of the next_state
                    next_state, stacked_frames = stack_frames(stacked_frames, next_state, False)
                    

                    # Add experience to memory
                    memory.add((state, action, reward, next_state, done))
                    
                    # st+1 is now our current state
                    state = next_state


                ### LEARNING PART            
                # Obtain random mini-batch from memory
                batch = memory.sample(batch_size)
                states_mb = np.array([each[0] for each in batch], ndmin=3)
                actions_mb = np.array([each[1] for each in batch])
                rewards_mb = np.array([each[2] for each in batch]) 
                next_states_mb = np.array([each[3] for each in batch], ndmin=3)
                dones_mb = np.array([each[4] for each in batch])

                target_Qs_batch = []

                 # Get Q values for next_state 
                Qs_next_state = sess.run(DQNetwork.output, feed_dict = {DQNetwork.inputs_: next_states_mb})
                
                # Set Q_target = r if the episode ends at s+1, otherwise set Q_target = r + gamma*maxQ(s', a')
                for i in range(0, len(batch)):
                    terminal = dones_mb[i]

                    # If we are in a terminal state, only equals reward
                    if terminal:
                        target_Qs_batch.append(rewards_mb[i])
                        
                    else:
                        target = rewards_mb[i] + gamma * np.max(Qs_next_state[i])
                        target_Qs_batch.append(target)
                        

                targets_mb = np.array([each for each in target_Qs_batch])

                loss, _ = sess.run([DQNetwork.loss, DQNetwork.optimizer],
                                    feed_dict={DQNetwork.inputs_: states_mb,
                                               DQNetwork.target_Q: targets_mb,
                                               DQNetwork.actions_: actions_mb})

                # Write TF Summaries
                summary = sess.run(write_op, feed_dict={DQNetwork.inputs_: states_mb,
                                                   DQNetwork.target_Q: targets_mb,
                                                   DQNetwork.actions_: actions_mb})
                writer.add_summary(summary, episode)
                writer.flush()

            # Save model every 5 episodes
            if episode % 5 == 0:
                save_path = saver.save(sess, "./models/model.ckpt")
                print("Model Saved")


# ## Step 9: Watch our Agent play 👀
# Now that we trained our agent, we can test it

# In[ ]:


with tf.Session() as sess:
    game = gym.make('Pheonix-v0')
    
    #game, possible_actions = create_environment()
    
    totalScore = 0
    
   
    # Load the model
    saver.restore(sess, "./models/model.ckpt")
    game.init()
    for i in range(1):
        
        game.new_episode()
        while not game.is_episode_finished():
            frame = game.get_state().screen_buffer
            state = stack_frames(stacked_frames, frame)
            # Take the biggest Q value (= the best action)
            Qs = sess.run(DQNetwork.output, feed_dict = {DQNetwork.inputs_: state.reshape((1, 80,80,4))})
            action = np.argmax(Qs)
            action = possible_actions[int(action)]
            game.make_action(action)        
            score = game.get_total_reward()
        print("Score: ", score)
        totalScore += score
    print("TOTAL_SCORE", totalScore/100.0)
    game.close()

