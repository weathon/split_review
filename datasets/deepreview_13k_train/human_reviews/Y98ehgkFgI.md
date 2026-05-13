# Network-based Active Inference and its Application in Robotics

- Decision: Reject
- Scores: 3, 6, 3, 1

## Abstract
This paper introduces Network-based Active Inference (NetAIF), a novel robotic framework that enables real-time learning and adaptability in dynamic, unstructured environments. NetAIF leverages random attractor dynamics and the Free Energy Principle (FEP) to simplify trajectory generation through network-topology-driven attractors that induce controlled instabilities and probabilistic sampling cycles. This approach allows robots to efficiently adapt to changing conditions without requiring extensive pre-training or pre-calculated trajectories. By integrating learning and control mechanisms within a compact model architecture, NetAIF facilitates seamless task execution, such as target tracking and valve manipulation. Extensive simulations and real-world experiments demonstrate NetAIF's capability to perform rapid and precise real-time adjustments, highlighting its suitability for applications requiring high adaptability and efficient control, such as robotics tasks in the energy and manufacturing sectors.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The work at first sight is very interesting as it seems to address some of the challenges in active inference for robotics, reads well, and showing its functioning in a real robot is very much appreciated. It also shows some novelty over previous approaches. However, there is plenty of explanations missing on the methodology used. For instance, where is the learning? Furthermore, results are not deeply analysed. Thus, it is complicated to understand the level of contribution of the approach.

### Strengths
* Easy to read
* Novelty of neural network active inference with pullback attractor.
* Interesting behaviour of unstable regions.
* Experiments with real robots

### Weaknesses
 * The introduction is to broad and to superficial in all three items selected. The energy transition seems to far away from this work. Also only Deep RL is mentioned. What about MPC with learning. In the active inference section survey is the only work reference. But it would be more informative how this work differs from previous robotics works. e.g., An empirical study of active inference on a humanoid robot, A novel adaptive controller for robot manipulators based on active inference, End-to-end pixel-based deep active inference for body perception and action, The Free Energy Principle for Perception and Action: A Deep Learning Perspective, etc.
Include a brief comparison table highlighting key differences between their approach and the cited active inference robotics works. This would give clearer guidance on how to improve the introduction and positioning of their work.

* Methods are unclear. What is the state, what is being minimized and learnt how it is performed. The diffusion process, etc. A lot of further explanation is needed. Provide
1.	A clear definition of the state space
2.	An explicit statement of what quantity is being minimized
3.	A step-by-step description of the learning process
4.	A more detailed explanation of how the diffusion process is implemented in their model
5.	Key methodological details you feel are missing, such as the objective function and learning algorithm equations

* Results analysis can be certainly improved. For instance, pose matching only shows 2-DOF results in joint angles not in the task space. This is not pose. Note that pose considers position and rotation of the end-effector.
Provide full 6-DOF pose results including end-effector position and orientation.

The tracking what is the input output of the NetAIF? Why you need a kalman filter? AIF can do filtering. so the NetAIF is only computing the controller? Improve the flow diagram with notation and input output and explanation.

The valve experiment. "manipulate valves of different shapes (triangle,
square, circle)" this is not shown. It is not clear what is the NetAIF computing and what is the engineering part. Provide analysis of valve manipulation for different shapes and a clear distinction between NetAIF computations and engineering components

Extra remark. Figures should be further explained, just the title is not enough.

### Questions
* Where is the learning? Algorithm 1 only shows execution of the net. Provide a separate algorithm or flowchart that explicitly shows the learning process, including weight updates and any optimization steps.
* What is the Free energy landscape (what is the equation? or what is x? how this affect the weights?) how is the diffusion coefficient being computed and  dW.
1.	Provide the explicit equation for the free energy landscape
2.	Clearly define all variables (e.g., x)
3.	Explain how these components relate to the network weights
4.	Detail how the diffusion coefficient is calculated
5.	Explain what dW represents in their implementation and how it is used

* Active inference agents explore when the model is unknown. But here authors express that the system is pushed into unstable regions due to the feedback loops. Provide an explanation of the potential advantages or disadvantages of this method compared to standard active inference exploration techniques.

References:
"For a comparison with DRL methods, see the companion paper (Anonymous, 2024)." This information should be in this paper. And it is marked as under review in ICRA but it can be found as under review in ICLR2025. Better to put all the info in one paper than split into two as it reduces its impact.

The High Road to Active Inference is a chapter. May be better to cite the book and refer to the chapter.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces Network-based Active Inference (NetAIF), a robotic framework that leverages active inference principles and network dynamics to enable robots to adapt in real-time to dynamic environments. Built upon the Free Energy Principle (FEP), NetAIF supposedly simplifies trajectory generation using network-driven attractors, which introduce controlled instabilities and probabilistic sampling. These design choices supposedly allow for efficient, rapid responses to environmental changes without extensive pre-training, contrasting with deep reinforcement learning (DRL) approaches that require complex reward structures.

### Strengths
I think active inference principles with network dynamics is a nice idea specifcially given that application of active inferecne has been a challenge without cumbersome approximations. So looks like your approach of integrating active inference with network dynamics is promising, potentially offering a fresh perspective in robotic control.

It is also interesting idea to diverge form optimization at every level and think of exploration and perturbations to converge towards good solutions.

The mode seems to be reduce computational overhead, making it suitable for resource-constrained cases like robots.

The authors provide thorough experimental validation, showcasing the framework's effectiveness across various tasks.

### Weaknesses
I do have some concerns regarding the work.

Lack of Structure in Descriptions: The initial sections of the paper, particularly the introduction, lack clear organization, making it difficult to follow the progression of ideas. A section on DRL is presented with no experiments on DRL later on in the paper.  The authors could reintroduce the problem of challenges of control more generally and issues with active inference that you are trying to address here.  start with the general challenges in robotic control, then introducing active inference and its limitations, followed by how NetAIF addresses these issues. Next would be related works and then a proper formulation of your methodology. This would provide a clearer progression of ideas for the readers to follow.

Relevant Literature : Also I dont feel the related works section is done well.  It doesn't cover earlier works that are compuationaly cheap and related such as PMP (https://link.springer.com/article/10.1007/s10514-016-9563-3) or other adaptive/neural control methods. Basically, refer to methods that are learable, adaptive and computationaly cheap to provide a relevant review and comparison.

Comparative Analysis: Then  paper does not sufficiently compare NetAIF against established approaches in terms of accuracy and efficacy, limiting the context of its contributions. I undersand there is another work by the authors submitted to ICLR 2025. I suggest to merge the works given the same underlying idea. I believe a combined paper would show a promising work with applications and comparisons making it stronger or more impactful.

Convergence Guarantees: The method’s ability to ensure convergence to high accuracy while incorporating constant perturbations is not adequately addressed, raising concerns about stability and reliability. You could provide theoretical guarantees or empirical evidence demonstrating the system's stability under various perturbation conditions.

Relevance to ICLR: The focus on robotic control, as opposed to learning and representation, may limit its appeal to broader ICLR community although this is not a limitation of the work per se.

### Questions
Comparative Metrics: What are the specific performance metrics used to evaluate NetAIF against existing methods, and how do these metrics support the claims of improved adaptability and efficiency?

Accuracy and Stability: How does the framework guarantee convergence to a high accuracy given the introduction of controlled instabilities and random perturbations? What mechanisms are in place to handle potential divergence?

Long-Term and Large system Performance: What measures are taken to evaluate the long-term performance and adaptability of NetAIF in highly variable environments or highly redundant robots as perturbations may make the system unstable.

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes a novel framework for robust learning of real-world robotics tasks in unstructured environments. The framework, called NetAIF, simplifies trajectory generation by relying on stochastic Random Dynamical Systems (RDS) and training model weights using the Free Energy Principle. Explicit feedback loops are introduced between hidden layers to control instabilities and enable real-time learning of three robotic tracking and interaction tasks.

### Strengths
- Interesting idea of using stable attractor dynamics for trajectory generation.
- Accompanying videos of tracking experiments suggest reasonable tracking performance.

### Weaknesses
 - Metrics and baselines are unclear. The only metric presented is average planning time in Section 3.6. However, no concrete comparisons with existing approaches like PRMs and Hybrid RRT-PRM as mentioned in the same section. Given the simplicity of the tasks evaluated, the paper also does not discuss why a simple PID tracking controller would not work, at least for the first 2 tasks.
- The tasks presented lack significant details to allow for a fair evaluation of the presented approach. For instance, the action space used in each of the tasks is not clear. Similarly, the type of robot controller used is also unclear and could have a significant bearing on the results of the experiment. Is the gripper state part of the system state?
- Sensory information here seems to be a direct measurement of the state. In general, this is only true for simple tasks. For instance, imagine a driverless car. Sensory information will generally be obtained through sensors like cameras without an explicit finite-sized state space. It is not clear how this approach would apply to a more general scenario where the relationship between sensory information and state information is not clearly defined.
- Paper lacks clarity on the data used for training. How are the weights trained for each task? Is Algorithm 1 used to train the network weights? If this is the case, how do the authors ensure that training on the robot like this is safe?

### Questions
Clarifications:
- What does weight resetting mean? How does resetting work and how does this affect the dynamics of the network?
- How do you validate performance in the presence of environmental disturbance? All the tasks investigated here seem to have little to no environmental disturbance.

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
This paper proposes an active-inference inspired neural network architecture that can be used for various tasks in robotics applications. It is claimed that the neural network architecture follows several biological and physical principles, such as the minimization of free energy, or the principle of least action. Several experiments show that the model can be used for pose matching, target tracking and a valve-turning task with a real 6-DOF robotic arm.

### Strengths
The idea to use active-inference or related biologically-inspired principles for robotics is interesting, and indeed, such methods can be much more sample-efficient than a standard application of Deep RL, which often tends to be sample-inefficient and have long-training cycles.

### Weaknesses
However, the paper is not written well. I was often puzzled throughout reading the paper, as the proposed model and architecture's properties are described without really introducing a method. The methodology seems very unclear, and the link to the literature is mostly not discussed, so that I was unable to form a clear idea of what the method is and what the contribution (with respect to the related work in the literature) is. Moreover in the experiments there were no comparisons with other methods, even though the method is claimed to improve significantly over deep RL baselines. Besides that, I was at least expecting a comparison with a more control-theoretic baseline, such as a (well-tuned) PD controller.

===== POST-REBUTTAL EDIT =====

I thank the authors for their rebuttal. I also removed the offending sentence, it was not meant as a personal/subjective comment, however I understand that it can be taken as such, for that I apologize. Overall my grade remains the same, and I strongly recommend the authors to introduce their method with clear mathematical notation. All the reviewers had trouble understanding the methodology, although it is agreed that Active Inference is a promising venue for robotics.

A few comments below on the rebuttal:

"The explanation of controlled instability (Section 2) is thoroughly detailed, describing the explicit bidirectional connections in the hidden layer and the external feedback loop that stabilizes the network. " However all the reviewers including me had trouble understanding the controlled instabilities introduced by the method, and the weight resetting.

"NetAIF is a novel framework that introduces a fundamentally new approach to trajectory generation and control, leveraging stochastic attractor dynamics and active inference principles. Due to its novelty, it has limited direct relevance to existing methods in the literature, which may contribute to a perceived gap in its contextualization. It is important to note that NetAIF’s approach represents a significant departure from traditional methodologies, making comparisons less straightforward." We're unable to appreciate perhaps the novelty of the approach because of (i) lack of clear understanding of the methodology, (ii) lack of clear comparisons, (iii) lack of detailed explanations of the algorithm and the implementation.

### Questions
I will list here some comments and questions that I had while reading the paper:

Section 1
- much more citations are needed in section 1. We're missing the connection to the literature.
- in what way is active inference 'advanced'?
- why is minimizing surprisal often impractical? 
- mention the relation/links to variational inference (Bayes) in section 1.3
- "By minimizing F, the agent balances accuracy (matching observations) and complexity (keeping the model simple)" 
This is not clear from the text. Characteristics of the method are often explained without really introducing the method, e.g., 
"NetAIF computes trajectories more efficiently than traditional AIF methods" How is this done? 
Section 2
- It is not clear what Figure 1 is, is it a fully connected network, or a convolutional neural network? or something else (RNN, etc.)?
- "NetAIF introduces explicit feedback loops between hidden layers, deliberately inducing controlled instabilities. Through extensive simulations and real-world experiments, we observe that these feedback mechanisms enable the network to explore the state space more thoroughly, leading to improved adaptability in dynamic environments."
What does it mean a controlled instability? what do you mean by 'thoroughly'? These claims are not supported by the experiments. I strongly recommend the authors to start from clear mathematical definitions.
- Figure 2 is not clear. What does red signify? what does blue signify for instance?
- "NetAIF actively manipulates network dynamics to push the system into unstable regions." How is this done? It does not seem to be discussed in the experiments adequately. And in general, instability is a huge problem in robotics. Or perhaps the authors mean something else? (see my comment above also, these points would be clarified by starting from mathematical definitions)
- "These feedback loops enhance oscillatory patterns, similar to neuron firing sequences, that persist even after training. This random bursts of node activity can be observed in the supplementary video, further highlighting the parallels with brain function." Again this seemed very vague to me (hence the comparison to a manual, rather than a clear scientific paper).
- Figure 3: "rendering the system open" What does open mean?
- What is a non-equilibrium steady state? Not clear from the text, is there a relation to Lyapunov stability?
- Algorithm 1 is not clear and not explained, not is it self-contained. How is desired state determined? What is new_weight? The algorithm seems to be missing a loop, given that there is feedback. Nor is the feedforward mapping of inputs to outputs properly introduced (unless there is only one hidden layer).
- What is the Free Energy in Algorithm 1? How is it playing a role?
- "By iteratively updating its local components based on prediction errors and external control laws, the system converges towards the desired states." -> How is this to be proved?

Section 3 (Experiments)
- How would you deal with constraints?
- How do you get the desired joint poise? Inverse Kinematics?
- There are no comparisons. The task seems especially easy, so I would expect a well-tuned PD controller to do equally well here.
section 3.4
- How is the network trained?

Section 4 (Discussions)
- "Moreover, this natural tendency aligns with the Least Action Principle (LAP) in classical mechanics" -> how?
- "The network dynamics appear to inherently seek the most efficient temporal path toward stabilization, regardless of initial conditions. This suggests that the network is optimizing its behavior by minimizing a functional analogous to action, thereby aligning with universal
optimization principles found in physics. " Appear and suggest are not rigorous enough, especially given that you're proposing a network structure whose novelty hinges on this explanation.

### Soundness
1

### Presentation
1

### Contribution
1
