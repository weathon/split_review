# MeMo: Meaningful, Modular Controllers Via Information Bottlenecks

- Decision: Reject
- Scores: 3, 5, 6, 5

## Abstract
Robots are often built from standardized assemblies, (e.g. arms, legs, or fingers), but each robot must be trained from scratch to control all the actuators of all the parts together. In this paper we demonstrate a new approach that takes a single robot and its controller as input and produces a set of modular controllers for each of these assemblies such that when a new robot is built from the same parts, its control can be quickly learned by reusing the modular controllers. We achieve this with a framework called MeMo which learns (Me)aningful, (Mo)dular controllers. Specifically, MeMo pretrains a modular architecture that assigns separate neural networks to physical substructures and uses an information bottleneck to learn an appropriate division of control information between the modules. We benchmark our framework in locomotion and grasping environments on challenging simple to complex robot morphology transfer. We also show that the modules help in task transfer. On both structure and task transfer, MeMo achieves improved training efficiency to pretrained graph neural network baselines. In particular, MeMo significantly improves training efficiency on structure transfer, often achieving 2x the training efficiency of the strongest baseline.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a modular policy learning approach for modularly designed robots. The approach learns separate modules for each actuator of the robot, along with a master controller. The master controller provides higher-level information to each actuator module, which then uses this information along with actuator-specific information to output the torques that are executed at each actuator. The paper uses an information bottleneck technique to learn appropriate modular behaviors. The proposed approach is evaluated on locomotion and manipulation tasks, and demonstrates good performance for both task and morphology transfer.

### Strengths
The overall paper focuses on an important problem of learning modular controllers such that they can be transferred from one morphology to another.

### Weaknesses
It is really unclear to me why the proposed approach will surely learn modular controllers. Specifically, the approach this paper proposes is to use reinforcement learning to train a monolithic policy (here done via PPO). This learned policy is then used to generate data which is used in an imitation learning setup. 

Specifically, the authors say 

“The goal of Imitation Learning …. train models that are transferable to variety of context (e.g. robot structures and tasks). This requires modules to represent meaningful behavior, which we enforce by imposing an information bottleneck on the master controller.”

But a fundamental problem with this approach is that the RL policy  has been trained on one task alone. Using an asymmetric approach to train the modular policy (with noise) does not in any way guarantee that the policies learned by individual modules will transfer to new tasks or morphologies. It is only because the task being considered here are too simplistic and almost within domain that we see positive transfer. Specifically, the robot manipulation example uses 4 fingers to train and 5 fingers to evaluate. However, the grasping policy in each of these settings is very similar basically, each finger basically has to push into the object. Further, grasping with greater than 2 fingers is anyways quite easy. Hence, it is really unclear if there is any modular structure. It would be interesting and make the paper much better if more challenging tasks are considered. Specifically, tasks where modularity is well defined. 

Can the authors provide any reason why this method will learn truly modular policies? Also, would this approach work if I define each joint of a 7dof robot as a separate module and then try to transfer to a 6-dof robot or another 7-dof robot with very different morphology? 

**train models that are transferable to variety of context (e.g. robot structures and tasks)**: Is there any limitation on the kind of tasks that this approach transfers or would this work across all different kinds of tasks? I think these above statements which form the crux of the paper are quite vague and do not precisely tell the reader where this approach can work and what are its failure modes.

**More Manipulation Experiments:** The paper argues that this is a general approach. However, most experiments are in walking domains (e.g. centipedes and worms). Can more manipulation tasks be considered for this approach? For instance, I am wondering whether a task (e.g. opening an oven) when done in slightly different configurations or with objects of different sizes still allows modular controllers to be learned from *a single task instance* (as done here).

### Questions
please see above.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, the authors show the benefits of a hierarchical network structure, trained via Imitation Learning and a gaussian-noise induced 'bottleneck', when transferring learned policies between robots with different morphologies. The network is composed of a 'master' network followed by many modules, which correspond to a grouping of similar actuators (one per joint). The authors show that by using the hierarchical network they can achieve sample efficiency and transfer policies between different structures and tasks. The network is compared to hierarchical/non-hierarchical RL agents that starts from scratch as well as to a state-of-the-art transfer approach called Nerve-Net.

### Strengths
The authors introduce a very important problem for actual robotics, that of transferring learned policies between robots (with different morphologies, assuming shared actuators/joint structures). The method chosen also looks interesting and several simulation examples are shown to support the claim that the hierarchical network can achieve knowledge/policy transfer between robots (and tasks, although the motivation is for different morphologies).

### Weaknesses
However, I found the contribution to be lacking in several key aspects:

* The proposed method was not sufficiently / rigorously analyzed. It is not clear why certain choices were made: the Gaussian-noise induced 'bottleneck' for instance performed better than L1-regularization, but it would be nice to analyze this more mathematically and study how it induces modularity during training. Specifically, the authors should provide a more detailed analysis of the information bottleneck created by the Gaussian noise. The paper lacks a theoretical justification for why this specific type of noise leads to better modularity than L1 regularization, beyond empirical results. For example, an analysis of the mutual information between the master network's output and the inputs to the modules could provide insight into how the bottleneck is shaping the learned representation. It is unclear what the variance of the noise was, and how this affects the performance.

* It is also not clear why Imitation Learning is necessary to train the hierarchical network with bottleneck, I believe if the authors focus on this problem, it can lead them to more rigorously understand the approach and suggest improvements for RL training. The authors should investigate why directly training the hierarchical network with RL fails. Is it a problem of exploration, or is there something about the non-stationarity of the RL data distribution that prevents the modules from learning meaningful features? A more detailed discussion of the challenges of training with RL, and why imitation learning is a necessary workaround, would strengthen the paper.

* It is very difficult to convincingly show knowledge/policy transfer between different 'robots', when these are only in simulation. The robots used in simulation, moreover, have very similar structures, for a more convincing argument I would show more experiments between quite different morphologies and tasks. Even without real robot experiments, it would go a long way to consider several difficulties that show up in real robot experiments: sensor noise, not having access to joint velocity measurements, actuator limits etc. The morphologies used are all variations of a centipede, and do not represent a significant change in robot structure. The authors should demonstrate transfer to robots with different kinematic structures, such as manipulators or quadrupeds, to truly validate the transfer capabilities. Moreover, the simulation should include more realistic sensor noise, actuator limits, and consider the challenge of not having access to perfect state information, such as joint velocities.

* It would be nice to show when and if the proposed method fails: this would help to understand how the method contributes to the literature better and also pave the way to more research. The authors should include examples of scenarios where the proposed method does not perform well, and discuss why these failures occur. This will help to identify the limitations of the approach and guide future research.

### Questions
* Shallow MLPs were used throughout the training as components, have the authors tried other architectures such as convolutional networks, transformers, or deeper MLPs?

* Are there other approaches to compare against besides Nerve-Net? The related work sections mentions many recent papers, some of which could be comparable.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper focuses on learning transferrable control policy for modular robots. To achieve this goal, the authors pretrain a modular architecture that assigns separate neural networks to robot substructures and uses an information bottleneck to learn an appropriate division of control information between the modules. They further benchmark the proposed framework in locomotion and grasping environments. The empirical results validate the effectiveness of the proposed method.

### Strengths
1. The problem this paper considers is important.
2. This paper is well-motivated. The idea of reusing control policy for similar modules of robots is easy to understand.
3. The proposed method is generally novel although there might be some works in multi-agent reinforcement learning that have similar network structures. 
4. This paper is well-written and easy to follow.
5. The empirical results in Figure 6 are significant compared with NeverNet. But more SOTA baselines should be considered.

### Weaknesses
1. The empirical results can be further improved. The authors only compared the proposed method with NerveNet, but ignored any recent works in the field of modular RL, such as SMP (One Policy to Control Them All: Shared Modular Policies for Agent-Agnostic Control), Amorpheus (My Body is a Cage: the Role of Morphology in Graph-Based Incompatible Control), METAMORPH: LEARNING UNIVERSAL CONTROLLERS WITH TRANSFORMERS, etc. The lack of comparison with these methods makes it difficult to assess the true performance of the proposed method relative to the state-of-the-art. Specifically, the paper should include comparisons with methods that also learn modular policies and can handle different robot morphologies. The current results only show an improvement over a single baseline, which is not sufficient to demonstrate the broad applicability of the approach.
2. The proposed method requires predefining the partition of robots. This reliance on predefined partitions limits the method's flexibility. In many real-world scenarios, the optimal partitioning of a robot into modules may not be known a priori and may even vary depending on the task. The requirement for manual partitioning could also introduce bias and limit the potential for the method to discover novel or more efficient modular control strategies. The paper should discuss how the performance of the method is affected by different partitioning strategies and how to choose an appropriate partitioning for a given robot and task.
3. This paper does not provide any discussions of limitations. The absence of a discussion on the limitations of the proposed method makes it difficult to understand the scope and applicability of the approach. The paper should include a discussion of the potential failure cases, the computational cost of the method, and the sensitivity of the method to hyperparameter settings. This discussion is crucial for a complete and balanced assessment of the proposed method.

### Questions
1. How does the MLP network in Figure 4 handle incompatible input and output?
2. Why does adding Gaussian noise can be regarded as an information bottleneck?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents MeMo, a hierarchical, modular architecture for robot controllers. It pretrains a modular architecture that assigns separate neural networks to physical substructures and uses an information bottleneck to learn an appropriate division of control information between the modules. The authors have conducted experiments to evaluate the generalization capability of MeMo for both structure and task transfer.

### Strengths
1. MeMo introduces an innovative hierarchical architecture for robot control that emphasizes modularity. The introduction of the information bottleneck adds a unique element that aids in generalization.

 2. The paper presents a thorough set of experiments in both structure and task transfer settings. The evaluation covers various robot morphologies and tasks, demonstrating the flexibility and effectiveness of MeMo.

 3. The paper is well-structured, and the key concepts are presented in a clear and understandable manner. Figures and plots help in visualizing the results and concepts.
 
4. The authors have benchmarked MeMo in challenging environments for robot morphology transfer. The results indicating improved training efficiency in both structure and task transfer are commendable. Moreover, the comparison with other methods, especially NerveNet, provides valuable insights into the advantages of MeMo.

### Weaknesses
1. The significance of the information bottleneck is mentioned, but a deeper exploration into its role and implications within the framework might enrich the paper's content. It might be helpful if the authors can clarify the choice of Gaussian noise as the information bottleneck and its specific advantages over other potential techniques, such as variational methods or adversarial training. Providing some theoretical underpinnings, such as an analysis of the mutual information between the master controller output and the module inputs, would enhance the paper's contribution.

2. While the paper mentions comparisons with other methods like NerveNet, a more exhaustive comparative analysis might accentuate MeMo's advantages more distinctly. It would be beneficial to provide more granularity on experimental setups, such as the specific reward functions used for each task, the range of hyperparameters explored, and perhaps even failed experiments to give readers a comprehensive understanding. Please consider extending experiments to more diverse robot morphologies, including those with closed kinematic chains, or even real-world robot applications to further validate the framework's robustness.

3. This article is not very innovative to the field.

### Questions
1.  I have concerns on extending this method to more complex tasks (environments). The authors should compare their methods with more strong baselines which learn universal controllers for modular robots.

2. Can and how MeMo transfer to the real world problem?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
