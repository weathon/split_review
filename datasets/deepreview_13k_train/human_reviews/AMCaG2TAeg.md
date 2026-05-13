# Causal Influence-Aware Counterfactual Data Augmentation

- Decision: Reject
- Scores: 5, 5, 3

## Abstract
\looseness -1 Offline data are both valuable and practical resources for teaching robots complex behaviors.
Ideally, learning agents should not be constrained by the scarcity of available demonstrations, but rather generalize beyond the training distribution.
However, the complexity of real-world scenarios typically requires huge amounts of data to prevent neural network policies from picking up on spurious correlations and learning non-causal relationships. 
We propose \method, a data augmentation method that can create feasible synthetic transitions from a fixed dataset without having access to online environment interactions.
By utilizing principled methods for quantifying causal influence, we are able to perform counterfactual reasoning by swapping \emph{action}-unaffected parts of the state-space between independent trajectories in the dataset.
We empirically show that this leads to a substantial increase in robustness of offline learning algorithms against distributional shift.
Videos, code and data are available at \url{https://sites.google.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a method called Causal Influence Aware Counterfactual Data Augmentation (CAIAC) that addresses the challenge of generalizing robot behaviours to new situations using pre-recorded data and human-collected demonstrations. By swapping causally action-unaffected parts of the state-space from different observed trajectories in the dataset, CAIAC creates feasible synthetic samples without the need for new environment interactions. The experimental results demonstrate the generalization capabilities and sample efficiency of the proposed method.

### Strengths
- The paper proposes a data augmentation method called Causal Influence Aware Counterfactual Data Augmentation (CAIAC) that can create feasible synthetic samples from a fixed dataset without the need for new environmental interactions.

- The paper is well-written and easy to follow.

- The experiments on offline self-supervised skill learning and offline reinforcement learning showcase the effectiveness of the proposed method as some extent.

- The proposed approach is independent and can be used with any learning algorithm.

### Weaknesses
 - The novelty is limited, drawing heavily on the groundwork laid by Seitzer et al., 2021, for local causal graph estimation and CAI's influence measurement. The conceptual leap from the work of CoDA (Pitis et al., 2020), which also involves counterfactual generation through connected component swapping, to the present technique of swapping uncontrollable subgraphs, seems incremental rather than revolutionary.

- While the paper successfully argues the challenges and pitfalls of complete causal structure estimation, it only partially addresses the performance of CAIAC in high-dimensional, low data regime environments, leaving a gap in the analysis. A more exhaustive exploration of the method's computational demands and scalability would greatly enhance the reader's understanding.

- The experimental comparisons seem to lack a critical control condition — an alternative method that also augments counterfactual data through local causal structure estimation with CAI but swap the connected components to form new transitions given two transitions that share local causal structures. Including such a benchmark would provide a clearer picture of CAIAC's relative efficacy.

### Questions
- Could the authors provide more insight into CAIAC's performance in environments with abundant data? The discrepancy in performance between low and high data regimes in high-dimensional settings warrants further clarification.

- Moreover, could the authors elaborate on the computational complexity and scalability of the CAIAC method, especially in comparison to existing methods?

### Soundness
2 fair

### Presentation
3 good

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
This paper proposes CAIAC, a novel counterfactual data augmentation technique that generates additional data by swapping causally “action-unaffected” state dimensions of different transitions. CAIAC identifies action unaffected state dimensions using a Causal Action Influence (CAI) metric. Empirically, CAIAC outperforms other counterfactual data augmentation techniques (CoDA and CoDA-ACTION, sort of interpolation between CAIAC and CoDA) on offline Franka Kitchen tasks and a two-block FetchPush task.

### Strengths
1. The topic of counterfactual data augmentation is of general interest to the RL community, as many real-world tasks have local causal structures (as noted in the paper).
2. The paper is well-motivated, and I found the description of local causal models easy to follow.

### Weaknesses
1. There seems to be a fine distinction between CAIAC, CoDA, and CoDA-ACTION that that isn’t quite clear to me. My understanding is as follows:
* CoDA uses a learn local causal model (or a hard-coded heuristic) to identify locally independent state dimensions and then generates augmented transitions by swapping the locally independent state dimensions of observed transitions. The resulting augmented transitions.
* CAIAC is identical to CoDA but uses a CAI metric to identify locally independent state dimensions.
* I could not understand the difference between CoDA and CoDA-ACTION.

  I hope the authors can clear up my confusion on this matter. If my current understanding of CAIAC vs CoDA is correct, then algorithmic contribution of this work is limited. In any case, a figure that clearly illustrates the difference between CoDA, CODA-ACTION, and CAIAC would be immensely helpful towards understanding (1) the CAIAC algorithm and (2) the novelty of this work. It would also be helpful if the authors evaluated these algorithms on a simple, didactic toy task like the SpriteWorld task used CoDA.
    
2. Empirical results seem weak. In Table 1, CAIAC outperforms baselines with obvious significance in 3/6 tasks (Kettle, Microwave, Bottom-burner), and struggles in the remaining 3 tasks (Slide Cabinet, Light Switch, Hinge Cabinet). Since the algorithmic contribution seems limited, I would like to see CAIAC evaluated on additional tasks -- tasks that show some learning progress with CAIAC and in an online learning setting. Some possible tasks: FetchSlide, FetchPickAndPlace, FetchStack, or the analogous PandaGym tasks. 

3. The paper states that CoDA and CODA-ACTION are (1) unable to recover the correct causal graph and (2) create dynamically infeasible data which harms performance, but there is no empirical evidence to support this claim. Given a dataset of augmented transitions {(s, a, r, s')}, the authors might consider validating claim (2) by initializing simulation to s, taking action a, and then checking if s' equals the simulators true next state. Then we could compute the probability that each algorithm generates feasible data and see if CoDA and CoDA-ACTION are more likely to generate such data than CAIAC. Claim (1) would then follow immediately -- if an algorithm generates a relatively large amount of infeasible data, then it surely has the wrong causal model. 

4. It’s not immediately clear what CAIAC is doing from Figure 1. I suggest explicitly stating in caption or the figure itself what is being swapped and what augmented data is generated.

Other comments:

1. I found Figure 6 to be quite helpful in understanding the CAI scores. If possible, this figure would be a nice addition to the main paper.

2. When describing the local causal structure in the chosen benchmark tasks, it may be beneficial to concretely describe the structure. In particular, the agent's actions only affect an object if the agent is in contact with the object.

3. The authors may find the following references particularly relevant to this work:
* MoCoDA [1] is an extension of CoDA that enables a user to control the distribution of augmented data.
* GuDA [2] is a framework for generating expert-quality augmented data.

### Questions
1. In the weaknesses section, I suggested additional online RL experiments. CAIAC, like CoDA, can be used in online learning too, correct?

### Soundness
3 good

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper emphasizes the importance of allowing learning agents to generalize to various situations, rather than being constrained by limited demonstrations. In real-world scenarios, the combinatorial complexity necessitates a significant amount of data to prevent neural network policies from relying on non-causal factors. Therefore, the authors propose CAIAC, a data augmentation method that generates synthetic samples from a fixed dataset without requiring new interactions with the environment. This method is inspired by the idea that an agent can only change its environment through actions. Hence, parts of the state space that are unaffected by actions are swapped from different trajectories in the dataset. The paper utilizes Causal Action Influence" (CAI) to identify action-independent entities and then swap states of these entities from other observations in the dataset. The introduction highlights the potential of teaching robots using demonstrations and datasets, which is a promising approach for developing competent robotic assistants.

### Strengths
1. The idea of using local independence to do counterfactual data augmentation is neat and interesting. As there could exist many spurious correlations during the offline data collection process, counterfactual data augmentation is important for breaking the spurious correlation.

2. The paper is well-written and easy to follow. The formulation of the problem and the proposed method is clear.

### Weaknesses
1. If I understand correctly, a strong underlying assumption of the proposed method is that the swapped states are irrelevant to the goal state. In the experiment part, the authors mention that “we initialize all non-target entities (with p = 0.5) to a random state”, which is why I think there exists such an assumption. This assumption is required since local independence does not imply the dependency between the current state and the goal state. This assumption is fine if the task is simple and the horizon is short. However, if the task is long-horizon and the later sub-tasks require some pre-conditioned to be satisfied, the local independence may not always be true. The method's reliance on swapping states of entities deemed action-independent could lead to issues when these entities, while not directly influenced by the current action, are still crucial for achieving the overall goal, especially in long-horizon tasks where specific preconditions must be met. For example, in a complex manipulation task, the position of an object might not be directly changed by a specific action, but its initial placement is critical for the success of subsequent steps. 

2. Another assumption of the method is the fixed factorization of the state space, which may not be available in most real-world tasks. Determining which variable to be abstract from raw sensors may limit the usage of this method. The requirement for a predefined factorization of the state space into independent entities is a significant limitation. In many real-world scenarios, especially those involving raw sensor data, the underlying structure of the state space is not known a priori. The process of identifying and separating relevant entities from raw sensor data is a challenging problem in itself, and the method's reliance on a fixed factorization limits its applicability to tasks where this factorization is readily available or easily determined. This assumption also restricts the method's ability to generalize to more complex scenarios where the state space might not have a clear, fixed decomposition.

3. Missing related literature on causal reinforcement learning [1-11].

4. Using counterfactual data augmentation to improve RL algorithms has been investigated a lot in previous work. CoDA is an important work but cannot cover all existing baselines. The authors may need to add more baselines to show fair comparison, for example [1, 2, 4, 7, 9].

### Questions
1. The analysis of the failure cases in Table 1 is missing. The proposed method does not have an improvement in the last three tasks (i.e., Slide cabinet, Light switch, Hinge cabinet). I also observe such a performance drop in Figure 5. According to the design of the spurious correlation, I expect that the proposed method should generally work for all tasks. Could the authors explain the reasons for the failure?

2. In Section 5.2, the authors explore a goal-conditioned task. One question about the results is the statement “All methods perform similarly, given that there is enough coverage of the state space in the original dataset.”. It looks like the proposed method is the worst among all four methods. I don’t think the gap between CAIAC and No Aug. is caused by randomness. Usually, using data augmentation will not harm the performance. Could the authors provide some explanations? Is this related to the first point of the weakness part of my review?

3. Still in Section 5.2, the statement “the transformer model is able to discover the causal graph and creates realistic counterfactuals” is not supported by any evidence. 

4. Could the authors provide a detailed comparison between CAIAC and CoDA? I think these two methods have very similar ideas but with different implementations. CoDA may suffer the problem of data scarcity for training a good transformer, but generally, what is the main advantage of using CAI to identify local independence?

5. “For Fetch-Push we set θ = 0.1, and θ = 0.3 for Franka-Kitchen.” How do you select the parameter θ?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
