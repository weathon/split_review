# SEABO: A Simple Search-Based Method for Offline Imitation Learning

- Decision: Accept
- Avg Score: 7.00
- Scores: 6, 8, 6, 8

## Abstract
Offline reinforcement learning (RL) has attracted much attention due to its ability in learning from static offline datasets and eliminating the need of interacting with the environment. Nevertheless, the success of offline RL relies heavily on the offline transitions annotated with reward labels. In practice, we often need to hand-craft the reward function, which is sometimes difficult, labor-intensive, or inefficient. To tackle this challenge, we set our focus on the offline imitation learning (IL) setting, and aim at getting a reward function based on the expert data and unlabeled data. To that end, we propose a simple yet effective search-based offline IL method, tagged SEABO. SEABO allocates a larger reward to the transition that is close to its closest neighbor in the expert demonstration, and a smaller reward otherwise, all in an unsupervised learning manner. Experimental results on a variety of D4RL datasets indicate that SEABO can achieve competitive performance to offline RL algorithms with ground-truth rewards, given only a single expert trajectory, and can outperform prior reward learning and offline IL methods across many tasks. Moreover, we demonstrate that SEABO also works well if the expert demonstrations contain only observations.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a method for Offline Imitation Learning (IL) that defines a reward function based on the Euclidean distance to the nearest neighbor expert state. The method, called SEABO, uses a KD-tree to efficiently query expert states and compute rewards for all transitions. The resulting problem can then be optimized using an arbitrary offline RL algorithm. The experimental results demonstrated improved performance in several tasks of the D4RL benchmark.

### Strengths
1. The proposed approach is both novel and simple, and its implementation is efficient due to the use of a KD-tree, without the need for training an extra discriminator.
2. This paper focuses on the context of single-expert-demonstration IL tasks, which is an area of growing interest in the field.
3. I find the discussion on using different search algorithms in Section 5.4 and Appendix Section C interesting.
4. The Limitations section in the appendix is highly appreciated, as it provides valuable guidance on tuning hyperparameters and applying SEABO on visual input.

### Weaknesses
1. I'm concerned about the use of Euclidean distance and would suggest that the authors include references justifying the use of this distance metric. This is crucial because there might be scenarios where states that are close in Euclidean distance are, in fact, far apart when accounting for the transitions within the Markov Decision Process (MDP). This particular challenge doesn't arise in discriminator-based methods, mainly due to the use of an additional neural network during training. Specifically, the Euclidean distance treats each state dimension independently, which may not capture the underlying manifold structure of the state space. For example, in a robotic arm manipulation task, a small change in joint angles might lead to a large change in end-effector position, and vice-versa. Thus, two states that are close in Euclidean space might require very different control sequences to reach, making the reward signal potentially misleading. A more suitable distance metric should consider the dynamic constraints of the MDP.
2. I believe that "(oracle)" should be omitted from Table 1-3 and 6. For instance, consider "IQL (oracle)": it utilizes the ground truth reward but doesn't rely on expert demonstrations. Removing the ground truth reward and integrating an additional expert demonstration does not necessarily make the task more challenging.
3. The experiments currently compare with only two Offline RL methods (IQL and TD3_BC). It would be better to include more recent baselines such as Trajectory Transformer [[1]], Diffuser [[2]], or other methods. The current evaluation lacks a comprehensive comparison with state-of-the-art offline RL algorithms, making it difficult to assess the true performance of the proposed method. Furthermore, the chosen baselines may not represent the strongest competitors in the field, potentially overestimating the relative performance of SEABO.

### Questions
1. Can SEABO utilize alternative distance metrics in place of the Euclidean distance? If so, how much modification is required?
2. The comparison between ground-truth rewards and the rewards obtained by SEABO (as in Figures 2 and 12) is intriguing. Have you also conducted similar reward comparisons in additional environments, such as AntMaze-v0 and Adroit-v0?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proses an approach for imitation learning using nearest-neighbor-based reward computation and offline RL. Given a dataset of unlabeled environment interactions and a single demonstration, they use a KD-tree to compute the distance of each transition to it's nearest neighbor in the demo (euclidean distance) and use this as a pseudo-reward which they can optimize with offline RL. The method is evaluated extensively in D4RL locomotion (and few manipulation) tasks and shows strong performance over prior works.

### Strengths
The idea is simple and well-explained in the paper. The empirical validation is thorough, with results across many D4RL locomotion tasks and a small number of manipulation tasks. A representative set of baselines is used and the method shows strong empirical performance. The simple proposed method beats more complex alternatives that need to use optimal transport etc.

### Weaknesses
I don't have many issues with the paper. The method has some limitations (see below), but I don't think this invalidates the contributions of the current paper. 

One minor weakness is that the approach is mostly evaluated on locomotion tasks for which precision is not the most critical. It could be great to evaluate it on a challenging, long-horizon manipulation task to test the limits of the method. For example the IKEA Furniture assembly benchmark could provide a nice test bed and I would be curious how well the proposed method performs.

Another minor point is that the paper lacks explanation how the euclidean distance is computed on the transition tuple. Do you compute euclidean distance on state, action and next state separately and then sum them? is there a weighting? Providing some details on this would be great!




### Questions
--

# Post Rebuttal Comments

Thank you for answering my review.

I appreciate the new experimental results -- performance on Kitchen seems strong and should be included in the paper.

Regarding the furniture assembly benchmark: if offline imitation algorithms struggle in this benchmark, would it be feasible to apply your algorithm in an online context? Also, note that there is a new version of the benchmark (IKEA Furniture Bench, https://clvrai.github.io/furniture-bench/) -- while its focus is on real-world manipulation, it also comes with a simulated counterpart and offline dataset -- you could check that one out as well!

In any case, thank you for adding the experiments and I maintain my recommendation of acceptance. I also skimmed the other reviews and it seems that all reviewers are in agreement that the paper should be accepted.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes the "SEABO" algorithm, which is an imitation learning algorithm that utilizes an expert dataset along with an unlabeled dataset. SEABO annotates the unlabeled dataset with rewards based on the distance between each state and the closest state in the expert dataset, and then runs an offline RL algorithm on the annotated dataset. The authors show improvements on the D4RL benchmark compared to prior baselines.

### Strengths
- This paper proposes a very simple algorithm that achieves good performance relative to more complex methods. I think this type of work has good value to the community in that it introduces easy-to-reproduce results and discourages over-engineering of methods.

- The paper is clear in presentation and mostly well written.

### Weaknesses
 - There is only empirical analysis of the proposed method. I believe there are certain tasks where SEABO would perform poorly, such as a cliff-walking type of task where there is a precise boundary between what is accetable and what is a failure. Specifically, in environments where the reward function is discontinuous or has sharp transitions, the assumption that proximity to an expert state implies near-optimal behavior may not hold. For example, consider a navigation task where a single step over a boundary results in a large negative reward; in such cases, the distance metric used by SEABO might incorrectly assign high rewards to states just before the boundary.

- I hypothesize that the approach will also only work in lower dimensional control environments. This is because the method relies heavily on a  distance function, and this could suffer from the curse of dimensionality in more complex environments. The performance of nearest-neighbor search, which is a core component of SEABO, degrades exponentially with increasing dimensionality. In high-dimensional state spaces, the notion of 'closeness' becomes less meaningful, and most states will be equidistant from the expert states. This could lead to the algorithm assigning similar rewards to vastly different states, hindering effective learning.

Minor:
Search in the context of RL and planning typically has a slightly different connotation, which is using some type of tree-based or trajectory-shooting method that optimizes some cost function. In this work search is only used to find states close to an expert. I'm not sure what can be done with this in the writing, but I was expecting a method in the former category after reading the abstract. It may be better to replace "search" with "nearest neighbors" to be more specific.

### Questions
"we hypothesize that the transition is near-optimal if it lies close to the expert trajectory" -> Is this strategy always good or does it have weaknesses? I would imagine that certain environments with discontinuities or discrete events (e.g. a car crash) would not favor this strategy.

There is another simple baseline commonly used in offline RL, which is sometimes referred to as percent-BC, which is to imitate the top N% of trajectories in the offline dataset (such as N=10 or N=25). As it is somewhat similar in spirit to SEABO, it would be good to see comparisons to this approach.

Is there any effect of the "curse of dimensionality" for higher dimensional states?

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors introduce an offline imitation learning algorithm called SEBO, which is centered on the task of learning a reward function from a dataset of expert demonstrations and applying it to unlabeled data to facilitate offline reinforcement learning.

The key innovation in SEBO lies in its use of a straightforward metric for generating the reward function, without the use of any neural networks. The algorithm employs search algorithms to determine the reward function. Specifically, SEBO constructs a KD-tree based on the expert demonstrations. For each unlabeled data point, the algorithm queries the KD-tree to identify its closest neighbor in the expert dataset and assesses the proximity between them. If the distance is minimal (indicating similarity to the expert trajectory), a high reward is assigned; conversely, if the distance is substantial (indicating deviation from the expert trajectory), a low reward is assigned.

The paper evaluates the SEBO algorithm across a range of MuJoCo environments and demonstrates its performance.

### Strengths
1. The paper is well written, and the algorithm is studied well on different MuJoCo environments. The authors also conduct a sensitivity analysis with respect to the two parameters $\alpha$ and $\beta$
2. SEBO is efficient, and easy to implement. It costs a minimal overhead over existing Offline RL algorithms, and does not involve training of a new neural network.  
3. The authors also evaluate it in a scenario where there is only access to observations, a case that might be of real world importance.

### Weaknesses
 **Evaluations restricted to deterministic environments**

All evaluations performed in this paper are conducted on deterministic environments (transitions in MuJoCo are completely deterministic), the claim that just one expert trajectory is sufficient might not be true if the environments are stochastic. For example, you may have a good (s,a,s’) pair in the dataset, but you may assign a lower reward to it as its not present in the expert demonstration.  I think there is an inherent correlation between the number of expert trajectories needed and the stochasticity of the environment. Specifically, in stochastic environments, a single expert trajectory may not adequately cover the state-action space, leading to inaccurate reward assignments by SEBO. The algorithm's reliance on nearest-neighbor matching in the expert trajectory could penalize valid transitions that are not directly represented in the single expert demonstration, even if those transitions are optimal or near-optimal.

**The paper lacks theoretical justifications, which makes understanding some parts a little difficult. For instance,**

This method might not work in situations where there are multiple ways to solve the same task. 
Consider the following example of a navigation problem, where the goal is to navigate to the destination from start position, and there are two ways to solve this task. One that goes left and reaches the goal, the other that goes right and reaches the goal.  Suppose the expert demonstrations takes the left path, and the unlabeled demonstrations (say from an expert policy as well) are from the right path, SEBO will assign low rewards to all transitions and not learn a good policy while BC will probably work. This highlights a critical limitation: SEBO's reward function is inherently biased towards the specific path taken by the expert, and it does not generalize well to alternative, equally valid solutions. The lack of theoretical analysis makes it difficult to predict the conditions under which SEBO will fail or succeed, and it also limits the ability to compare it with other offline imitation learning algorithms.

### Questions
1. Is there an inherent assumption being made between the distribution of state-action pairs in the expert demonstrations and the unlabeled dataset? 
2. Why are the experiments on D4RL restricted to medium level task and not conducted on expert and random versions of it? 
3. Does the stochasticity of environments affect the performance of SEBO? 
4. When using point wise matching to determine the reward are you making some inherent assumptions on the transition kernel?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
2 fair
