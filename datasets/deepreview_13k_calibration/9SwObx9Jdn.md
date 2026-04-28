# Generation of Geodesics with Actor-Critic Reinforcement Learning to Predict Midpoints

- Decision: Reject
- Avg Score: 4.75
- Scores: 5, 6, 5, 3

## Abstract
To find the shortest paths for all pairs on manifolds with infinitesimally defined metrics, we propose to generate them by predicting midpoints recursively and an actor-critic method to learn midpoint prediction. We prove the soundness of our approach and show experimentally that the proposed method outperforms existing methods on both local and global path planning tasks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents a novel reinforcement learning framework, termed as 'midpoint tree', designed to recursively generate geodesics for path planning. The approach introduces an actor-critic learning method tailored to predict midpoint waypoints, facilitating the construction of paths in complex environments. The paper details both the theoretical underpinnings and the practical implications of the method, demonstrating its application to two distinct metrics, the Matsumoto metric and a car-like metric, and discussing its potential in fields such as image processing and physical systems modeling.

### Strengths
The paper presents a distinct approach to generating geodesics in reinforcement learning environments via a "midpoint tree" algorithm. The theoretical underpinnings are robust, complemented by a thorough experimental evaluation. The articulation is commendable, with the authors elucidating complex ideas succinctly. This work's originality and potential applicability are clear, indicating its prospective value in advancing research within reinforcement learning and robotics.

### Weaknesses
The paper lacks a broader range of examples to demonstrate the applicability of the method to more common robotic tasks like locomotion and manipulation planning. The experimental results, while encouraging, do not showcase a significant advantage over existing methods, raising questions about the practical benefits of the proposed approach. It requires certain assumptions that may not be present in typical robotic environments, such as the need for global coordinate systems and uniform sampling. The method might not be readily applicable to more complicated, dynamic environments.

More concretely:
- The algorithm requires additional assumptions that may not be readily available or applicable in common robotic tasks, such as locomotion and manipulation planning. These assumptions include the need for global coordinate systems, obstacle-free environments, and environment-specific policy learning. The method's effectiveness is contingent on these conditions, which are not always present in more complex or dynamically changing real-world scenarios. Additionally, the challenge of generating globally optimal paths and dealing with the complexity of Finsler geodesics further limits its applicability to standard reinforcement learning tasks.

- In the original wording, the paper mentions that the method "only works well locally since we assume that manifolds have global coordinate systems and the continuous midpoint property may be satisfied only locally. For the generation of globally minimizing geodesics, we may have to divide manifolds, train policies for each local region and connect locally generated geodesics." It also states that "the policy has to be learned for each environment. By modifying our method so that the actor and critic input information on environments, it may be possible to learn a policy applicable to different environments." These statements highlight the limitations regarding the need for specific geometric and topological assumptions that may not hold in typical RL tasks in robotics.

A line of work on quasimetric distance for goal-conditioned RL seems related, which could provide important context and benchmarking. I'd be curious whether the proposed approach is related to them.
- Tongzhou Wang et al., Optimal Goal-Reaching Reinforcement Learning via Quasimetric Learning, ICML 2023
- Tongzhou Wang et al., On the Learning and Learnability of Quasimetrics, ICLR 2022

### Questions
- Can the authors provide additional examples where their method might be applicable, specifically within the realm of robotics tasks like locomotion and manipulation?
- How does the proposed approach compare in terms of benefits and applicability to other realistic tasks, beyond what has been demonstrated in the paper?
- Could the authors discuss the relationship and distinctions between their work and recent research on quasimetric learning for goal-conditioned RL?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a modification of the sub-goal tree framework to use midpoints instead of arbitrary intermediate points and actor-critic instead of policy gradient for goal-conditioned reinforcement learning problems. With the two changes, the proposed method is able to generate equally divided waypoints and with better sample efficiency on deep trees. Theoretical proofs are given for the convergence of the proposed method. The proposed method shows comparable performance to baselines on several tasks with advantage of generating equally divided waypoints.

### Strengths
The paper is well-written and the method is well-motivated. The effectiveness of the proposed method is supported both theoretically and empirically. The generated waypoints with equal distances would be more useful than that of the previous method.

### Weaknesses
The novelty of the paper is not prominent compared to its base methods. 
The experimental setting is a bit simplified. In section 6, the authors propose a penalty term to be added to deal with obstacles. Wondering how easy is it to generalize the proposed method to environments with obstacles.
The experiment results do not show clear performance improvements of the proposed method.

### Questions
Can we add some more explanation and justification on why the midpoint is not just a trivial extension of the existing method using arbitrary waypoints?

Can we add more analysis on how the proposed method could be generalized to environments with obstacles?

In Figures 2 and 3, the proposed method does not show clear improvements compared to baselines. Is this expected? Can we add more explanations?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
1: You are unable to assess this paper and have alerted the ACs to seek an opinion from different reviewers.

### Summary
This work focuses on path planning to generate geodesics in some manifold. It extends sub-goal tree framework (Jurgenson et al., 2020) to generate midpoints (equal distances to two given points), instead of any intermediate points. They train an actor to predict the midpoints, and a critic to predict the distance of two given points (s,g). It is also shown to converge to a unique optimal solution,  where the distance is given by some continuous approximation. The method is evaluated on two toy tasks to showcase its effectiveness over RL and previous planning approach.

### Strengths
The overall writing is rigorous, principled and looks solid work. But I am not sure of its significance.

### Weaknesses
Perhaps the motivation of this work can be better written. As the authors pointed out in their experiments, generating geodesic (path planning) can be simply tackled by RL by specifying a reward function related to the difference in distance. But it may have instability or other issue compared to path planning approaches.

Could you give some explanation why Car-like task favors your approach, while Matsumoto task not?

The experiment scope is a bit narrow as only two toy tasks are evaluated.

Minor: The description of methods in the experiments can be more complete – add a line of “ours” using Eq. 8 before “the following variants of our methods”.  The name “sequential RL” is a bit confusing as RL is sequential in nature. Perhaps “vanilla RL” or just “RL”, because your approach uses a non-conventional actor loss.

### Questions
I’m not familiar with path planning and differential manifold, so some of these comments are my educational guess.

---- Post-rebuttal

After reading the authors' response and other reviews, I think this work still requires more empirical evaluation on their approach. Thus, I lower my rating.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, the authors study the problem of finding geodesics in general manifolds via reinforcement learning. The main idea is to divide the discovery task into smaller ones by predicting midpoints recursively. An actor-critic algorithm learns a policy to generate midpoints. Two empirical evaluations are provided to demonstrate the efficacy of the proposed algorithm.

### Strengths
1. Geodesics generation with reinforcement learning is a relatively under-explored research area. This work contributes by studying an actor-critic formulation and shows its effectiveness.

2. A few design choices are explored, such as different variants of the actor loss. These results help illustrate some properties of the proposed algorithm.

### Weaknesses
 1. The empirical evaluation environments are relatively artificial. I would expect some more practical tasks such as robotic motion planning to be more effective in demonstrating the significance of the contribution. 

 2. The current baselines are all RL based. I think some classical motion planning algorithms should be included too, such as RRT (RRT*) and A* search. 

 3. This is more of a clarification of the problem setting. It seems that the end goal of the learned policy is not necessarily finding the shortest path. The success criterion is stated as “all values of C(4) for two consecutive points are not greater than $\epsilon$”, which does not imply that a path is the shortest. Is this correct? If so, this should be stated more clearly.

### Questions
1. Please provide some motivations for the definition of $C$ (Equation (4)). Also please explain what $df_x$ is in this definition.

2. Why is Equation (5) hard to compute efficiently?

3. How does one decide the depth parameter $D$ on Line 18 of Algorithm 1?

4. In Equation (11), should the right-hand side be $d(x, y)$, the true distance rather than the local approximation? Either way, Equation (11) could use a more expanded explanation.

5. In Proposition 2, what is $V_i$?

6. In the Sequential Reinforcement Learning (Seq) baseline, why is the reward function (Equation (16)) scaled by $\epsilon$? How does this decision affect the learning?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
