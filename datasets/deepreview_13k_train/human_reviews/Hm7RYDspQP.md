# Network-based Active Inference for Adaptive and Cost-efficient Real-World Applications: A Benchmark Study of a Valve-turning Task Against Deep Reinforcement Learning

- Decision: Reject
- Scores: 3, 3, 3, 5

## Abstract
This paper introduces Network-based Active Inference (NetAIF), a novel approach that integrates Active Inference (AIF) principles with network dynamics to enable adaptive, cost-efficient real-world applications. In benchmark tests against Deep Reinforcement Learning (DRL), NetAIF outperforms DRL in both computational efficiency and task performance. Leveraging random attractor dynamics, NetAIF generates real-time trajectories, allowing robots to adapt to complex, dynamic environments without the need for extensive pre-training. We demonstrate NetAIF's superiority in industrial valve manipulation, achieving over 99\% accuracy in goal position and orientation in untrained dynamic environments, with a 45,000-fold reduction in computational costs. NetAIF is approximately 100,000 times more efficient in iteration count than DRL, making it a highly robust and efficient solution for industrial applications.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors propose an algorithm to address some of the shortcomings of Deep Reinforcement Learning (DRL) algorithms such as : generalizability to changing/dynamic environment and compute efficiency. They tackle the task of automated valve-turning by formulating the problem from an Active Inference (AI) perspective which is built on Free Energy Principle (FEP). The results show significant improvement in task accuracy and compute efficiency over several DRL baselines.

### Strengths
The paper is well motivated and proposes an interesting approach to tackle an important issue in robotics.

### Weaknesses
The biggest weakness in this paper is the lack of experimental details. My questions in the following paragraph are all primarily clarifying several missing information that might be very useful for a reader.

While the results comparing the task accuracy as well as compute efficiency to DRL methods seems very promising, In my opinion, several aspects of the paper needs to be improved. 

Starting with experimental details : The paper seems to lack sufficient details about the different experimental set-up for a reader to reproduce the results. For example, what is the state space of the robot for this task? I don’t recollect it ever being mentioned in the entire paper, neither in the supplementary material. 

What exactly is the prediction error for the valve turning task? For the target following task? Is it the difference between the current robot joint angles and the desired robot joint angles?

For the DRL baselines, what is the state and action space? What reward function is used? 
Section 2.2 mentions a “random attractor”, how does this fit into the Algorithm 1? 

The video supplement is helpful to gain context about the task and the robot motion is impressive. However, since the main goal of the approach was to show that it can adapt to changes in the environment, why not show valve turning for the different shapes or with different frictional properties? Are there any failure cases? If so, why? It might also be helpful to see how the DRL policies look like in real world, are they so bad that deploying them was not feasible? 

In figure 3, For the valve turning task, what are the external, internal and blanket states? Providing this information could give the reader some context and improve readability of the paper

### Questions
While the results comparing the task accuracy as well as compute efficiency to DRL methods seems very promising, In my opinion, several aspects of the paper needs to be improved. 

Starting with experimental details : The paper seems to lack sufficient details about the different experimental set-up for a reader to reproduce the results. For example, what is the state space of the robot for this task? I don’t recollect it ever being mentioned in the entire paper, neither in the supplementary material. 

What exactly is the prediction error for the valve turning task? For the target following task? Is it the difference between the current robot joint angles and the desired robot joint angles?

For the DRL baselines, what is the state and action space? What reward function is used? 
Section 2.2 mentions a “random attractor”, how does this fit into the Algorithm 1? 

The video supplement is helpful to gain context about the task and the robot motion is impressive. However, since the main goal of the approach was to show that it can adapt to changes in the environment, why not show valve turning for the different shapes or with different frictional properties? Are there any failure cases? If so, why? It might also be helpful to see how the DRL policies look like in real world, are they so bad that deploying them was not feasible? 

In figure 3, For the valve turning task, what are the external, internal and blanket states? Providing this information could give the reader some context and improve readability of the paper

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a novel method based on the active inference framework to solve a value-turning robotic manipulation task. They explain the active inference framework at a high-level, discuss their approach NetAIF, and compare it to a number of deep RL (DRL) approaches. They show an improvement in sample efficiency and performance compared to these competing methods on the considered task.

### Strengths
- Considering alternative algorithms to DRL which are more sample-efficient for specific applications is a timely and important problem.
- The evaluation does support the claims of sample efficiency and improved performance of the proposed algorithm.

### Weaknesses
 - While the proposed algorithm, NetAIF, appears very interesting, it is very difficult to ascertain how it works from the exposition in the text. There is an Algorithm box, but it is missing many critical pieces of information, including how the new weight values are set and over what the prediction errors are computed. The paper would be significantly strengthed if rewritten to include more information about the learning rule and what sets the network architecture apart from a linear RNN.
- While I know the point of the paper was to evaluate the algorithm on a specific task, it makes it very hard to determine if this approach is scalable to other problems. I greatly appreciate the inclusion of a real robotic platform. However, for a machine learning conference, the paper would be significantly strengthened by evaluating over more benchmarks to determine the generalizability of the proposed method.

### Questions
- What exactly is the network architecture? How does the learning rule work?
- How well does the proposed method work on alternative benchmark tasks?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper proposes Network-based Active Inference (NetAIF), a novel framework that integrates Active Inference (AIF) principles with network dynamics to create a real-time adaptive system for robotic tasks. Unlike reinforcement learning, which typically relies on learning from reward signals, NetAIF leverages feedback loops between hidden layers and actively learns by minimizing the difference between the current state and the desired state, enhancing the system's learning efficiency. The paper demonstrates the effectiveness of the proposed method through both simulation and real-world experiments, where NetAIF dramatically outperforms RL methods in terms of efficiency and accuracy.

### Strengths
1. The proposed method seems novel, NetAIF's ability to learn in real-time without requiring extensive pre-training offers a significant advantage over traditional RL methods.
2. The paper evaluates NetAIF on both simulated and real-world tasks, providing evidence of the method's practicality.

### Weaknesses
1. The paper is difficult to process, particularly for readers without a background in Active Inference. A major revision could improve the paper’s accessibility, especially for a general machine learning audience. For instance, a detailed explanation of how NetAIF differs from standard neural networks (particularly in weight updates compared to backpropagation) is necessary to help readers better understand the novel aspects of the framework. The current description lacks sufficient detail on the specific mechanisms of the feedback control loops and how they influence weight adjustments, making it hard to grasp the core innovation beyond a high-level concept.
2. There is no related work section, making it difficult to situate the contribution within existing literature. Adding a discussion on how NetAIF compares to other models, especially in terms of neural network architectures, reinforcement learning approaches, and AIF-based methods, would clarify the innovation. The absence of this section makes it challenging to understand how NetAIF builds upon or deviates from existing methods, particularly in areas like predictive coding networks or other biologically inspired control systems.
3. It is unclear whether NetAIF is leveraging additional information compared to model-free RL algorithms. The paper should clarify whether NetAIF has access to more privileged information (e.g., task-specific control laws or goal states) and whether the comparison with RL is fair. Are RL algorithms using the same input data for training and execution? The paper needs to explicitly state the input representation for both NetAIF and the RL baselines, ensuring that the comparison is not skewed by differences in the information available to each method. For example, if NetAIF has access to the goal state while RL only receives sparse rewards, the comparison is not valid.

### Questions
1. The first paragraph of the introduction feels disconnected from the core concept of the paper. It would benefit from a clearer link between the identified challenges and how NetAIF addresses these challenges specifically.
2. It would be helpful to add a summary of contribution at the end of the introduction.
3. The paper could benefit from a clear problem statement. Can the authors clarify what are the inputs to the proposed system? Additionally, can the authors confirm whether RL baselines in the paper are using equivalent input information to ensure a fair comparison?
4. In Table 1, adding noise and Hindsight Experience Replay (HER) appears to improve SAC's performance. Why were these enhancements not applied to PPO in Table 2? Since PPO seems to perform better in the experiments, why wasn't PPO tested in Table 1 for consistency?
5. What do the authors think about the comparison between the proposal and a model-based RL approach?

### Soundness
2

### Presentation
1

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
A Neural Network incorporating Active Inference principles is applied in robotic tasks. With the aid of random attractor dynamics, an interesting portion of the presented approach is that no pre-training is forcibly required. The adaptability in dynamic environments with minimal overhead makes it a scalable, cost-efficient solution for robotic control in unpredictable settings.

### Strengths
This is an application of NetAIF in robotic control. Two main advantages are illustrated. One is that the Time-consuming pre-training is no longer required, making it a cost-efficient solution. Another is the incorporation of feedback control law in the network model, which enables the system stable. Moreover, random pullback attractor is utilized to update the weights. From the results in the paper, the performance of this method is very good.

### Weaknesses
The literature research is not enough and the literature is so old. The expression of the paper is weak and the key issues are not explained clearly. For example, lack of detailed application description of NetAIF, like noise processing. In addition, the arranged experiments are too simple. The motion speed of the manipulator is low, which is not enough to verify the effectiveness of the method. Furthermore, the paper lacks a clear explanation of how the random pullback attractor is implemented and how it contributes to the network's learning process. The absence of a detailed description of the feedback controller's design and its parameters makes it difficult to assess the stability and robustness of the proposed system. The paper also fails to address the limitations of the proposed approach, such as its sensitivity to initial conditions or its performance in highly complex environments.

### Questions
1)	Please provide the related code;
2)	I wonder if this method is effective for learning highly dynamic systems like quadcopters?
3)	Provide more experimental details, such as network input, network output, neuron weights, and the design of feedback controller.

### Soundness
3

### Presentation
2

### Contribution
3
