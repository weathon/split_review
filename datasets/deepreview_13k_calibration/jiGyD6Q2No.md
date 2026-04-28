# UNIQ: Offline Inverse  Q-learning for Avoiding Undesirable Demonstrations

- Decision: Reject
- Avg Score: 4.25
- Scores: 8, 3, 3, 3

## Abstract
We address the problem of offline learning a policy that avoids undesirable demonstrations. Unlike conventional offline imitation learning approaches that aim to imitate expert or near-optimal demonstrations, our setting involves avoiding undesirable behavior (specified using undesirable demonstrations). To tackle this problem, unlike standard imitation learning where the aim is to minimize the distance between learning policy and expert demonstrations, we formulate the learning task as maximizing a statistical distance, in the space of state-action stationary distributions, between the learning policy and the undesirable policy. This significantly different approach results in a novel training objective that necessitates a new algorithm to address it. Our algorithm, UNIQ, tackles these challenges by building on the inverse Q-learning framework, framing the learning problem as a cooperative (non-adversarial) task. We then demonstrate how to efficiently leverage unlabeled data for practical training. Our method is evaluated on standard benchmark environments, where it consistently outperforms state-of-the-art baselines.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces a novel approach to learning from "undesirable" demonstrations. Instead of conventional imitation learning, which aims to imitate expert demonstrations, i.e. minimizing the distance with desired demonstrations, this method focuses on avoiding negative behaviors, i.e. maximizing the distance with undesired policy.

Based on MaxEnt RL framework and inverse Q-learning, the authors propose UNIQ, an offline inverse Q-learning algorithm designed to maximize the statistical distance between the target policy and undesirable policy. UNIQ utilizes both demonstrations of undesirable behavior and a broader pool of unlabeled data to develop a learning policy that effectively avoids unwanted actions.

### Strengths
Problem novelty - This paper tackles the distinct challenge of learning policies that actively avoid undesirable behaviors, rather than merely replicating expert behaviors. This approach is valuable in many applications where high-quality expert data might be scarce or unavailable.

Crisp and well-rounded introduction - Good summary of the problem space, the traditional approach, and the gap it's trying to address. Clearly explained frameworks that the algorithm is based on (inverse Q-learning).

Implementation details - The paper provides source code along with comprehensive details on hyper parameter settings and experimental configurations, improving both reproducibility and transparency.

### Weaknesses
Lack of validation using real-world data - While UNIQ is assessed on well-known benchmarks, evaluating it with real-world datasets from fields such as healthcare or autonomous driving could greatly enhance its value and demonstrate its applicability beyond simulated settings.

### Questions
Have you considered testing UNIQ in real-world domains? What specific challenges do you foresee in transferring the method from simulated benchmarks to real-world datasets?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This work tackles the challenge of offline learning in scenarios with undesirable demonstrations, aiming to train agents that avoid unsafe or undesired behaviors in environments where undesirable and mixed demonstrations are given.
The paper presents UNIQ (**UN**desirable demonstrations-driven **I**nverse **Q**-Learning), an approach built on an inverse Q-learning (IQ-Learn) framework. 
By exploiting IQ-Learn framework, the study aims to learn a reward function that penalizes actions similar to those in the undesirable dataset, effectively steering the policy away from risky behaviors.
Instead of directly optimizing within the policy and reward spaces, UNIQ operates in the Q-space, following a similar approach to IQ-Learn. 
The optimized Q-function is then used to derive the policy through weighted behavior cloning, with weights informed by an advantage function computed from the Q-values.
Through this approach, UNIQ efficiently learns a policy that emphasizes safety by penalizing actions aligned with undesirable demonstrations, making it a robust method for offline learning in risk-sensitive environments.

### Strengths
This work integrates the IQ-Learn framework into the problem setting of learning from undesirable demonstrations, addressing a challenge in safe offline imitation learning. 
By extending IQ-Learn to handle scenarios with undesired behaviors, the authors provide a novel application that moves beyond traditional offline imitation learning and into the realm of safe policy learning, which is important in real-world applications.

The study goes beyond merely applying IQ-Learn to this setting; it rigorously justifies the suitability of IQ-Learn for learning from undesirable demonstrations. 
Through in-depth analysis, the authors clarify how the proposed objective captures the characteristics needed to discourage unsafe behaviors, and this thorough justifications strengthen the reliability for applications of UNIQ.

Additionally, the authors propose a practical version of the UNIQ algorithm, making it applicable to real-world scenarios where undesirable demonstrations are given. 
This implementation, combined with theoretical insights, enables safe policy learning in some practical offline learning scenarios.

### Weaknesses
 **1. Questionable Design of Training Objective**

The training objective (Eq. 3) of UNIQ is focused solely on maximizing the discrepancy between the state-action distributions of non-preferred and imitator demonstrations. 
However, this objective lacks a mechanism to guide the policy toward with expert behaviors contained in mixed demonstration datasets. 
Consequently, the Q-function is primarily trained to penalize undesired demonstrations rather than to increase the Q-value of expert demonstrations.
This implies that when the unlabeled dataset contains a large number of safe yet non-optimal random actions in $D^{MIX} \setminus D^{UN}$, UNIQ may struggle to identify safe expert behaviors.

While this may result in a "safe" agent but it raises concerns regarding its usefulness for real-world applications. 
For instance, in an autonomous driving context, a policy that avoids non-preferred behaviors by simply stopping at the starting state could technically be safe,  yet it would lack the functional behaviors that essential for practical deployment.

**2. Limited Consideration of Experimental Scenarios** 

The experimental results also highlights a limitation of the current objective design, as UNIQ achieves relatively low costs and returns, indicating safety but at the expense of effectiveness.
These results appear insufficient to demonstrate that UNIQ is practically beneficial, as all evaluations are conducted on constrained RL benchmarks that primarily aim to maximize returns while keeping costs within predefined thresholds. 

As discussed in Section 1, the authors may argue that UNIQ is advantageous in certain scenarios — such as when expert demonstrations are entirely absent in the mixed dataset or when specific undesirable actions must be avoided by pretrained agents without compromising performance — the absence of experiments on these contexts weakens the argument for its applicability. 
The authors are encouraged to explore and present alternative scenarios and corresponding experiments that are suitable for applying the method's objectives and this would strengthen the justification of UNIQ’s approach and its practical relevance.


**3. Ambiguously Guided Safe Objective**

As noted by other reviewers as well, it still remains challenging to agree that the proposed objective is practically useful. 
The authors suggest that it could be beneficial when data is explicitly labeled as undesirable according to the learner's intention.
However, such a scenario seems to require more data points compared to standard IL problems. 
This is because, in many cases, the number of desirable actions per state is significantly smaller than the number of undesirable ones, especially with a deterministic expert. 
For example, if $|A|=4$ (e.g. navigation task) there is only one optimal action, while the other three are undesirable.

**4. Experimental Results on Mixed (Desirable+Random+Undesirable) Datasets**

Thank you for the additional experiment involving random demonstrations added to the dataset (included in Section C.6). 
However, as discussed by the authors, UNIQ demonstrates effectiveness only in the HalfCheetah task (one out of the two tasks tested).
Consequently, it is difficult to draw a strong conclusion about the effectiveness of UNIQ in mixed datasets.

### Questions
Q1. In line 220, the manuscript assumes that “$D^{MIX}$ may contain a mix of random, undesired, and expert demonstrations.” However, datasets used in experiments comprised with undesired and expert demonstrations. Could you provide additional exprimental results with mixing (safe) random demonstrations to the dataset?

Q2. Could you clarify what is meant by “the quality of the unlabeled dataset” in line 244? Does this refer to the proportion of preferred and non-preferred demonstrations in $D^{MIX}$? Additionally, why does UNIQ rely less on this compared to SafeDICE?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors present a new framework for training a desired policy using two datasets: one containing undesirable trajectories and another with unlabeled data. The goal is to train the policy without an explicit definition of optimal behavior, relying instead on a concept of behaviors to avoid. The authors argue that this approach is crucial in fields like autonomous driving and healthcare, where unsafe actions could lead to catastrophic outcomes.

### Strengths
- the concept is interesting and could indeed have important applications
- minor modification to existing approach, making application more straightforward
- the paper is well written

### Weaknesses
 - By merely avoiding certain behaviors, the resulting solution space appears vast and highly ambiguous.
- It seems that the undesired dataset needs to be quite large to effectively narrow the space of desired behaviors. The experiments suggest that a substantial number of trajectories were used.
- The experiments also indicate that the unlabeled dataset may actually contain safe trajectories rather than genuinely unlabeled data, implying a notion of optimality within the datasets. These safe trajectories could be viewed as an expert distribution to match, making them suitable for standard imitation learning methods. (see questions)
- I would argue that the datasets used in this paper are not truly unlabeled but instead consist of trained behaviors—one representing safe behavior and the other unsafe—leading to a narrow solution space. I doubt that this approach would scale effectively to settings with genuinely unlabeled data. It would be valuable for the authors to include an ablation study addressing this point. They could, for instance, test scalability by using a small set of undesired behaviors along with some of the untrained D4RL dataset to validate their approach.
- What is the divergence optimized here?
    -  [1] demonstrated that IQ-Learn minimizes the chi-squared divergence between the policy and a mixture distribution. Here, however, it seems that the approach maximizes the chi-squared divergence between a mixture distribution and another mixture distribution that includes both desired and undesired behaviors.
- How were the baselines trained, like BC-Mix and IQ-learn Mix? Where they trained to imitate only the Mix distribution? If yes, I would argue that this is an unfair since you actually have access to the dataset you would like to imitate (the safe trajectories), and IQ-learn and BC should rather try to imitate that one.

Minor Points:
- try to write more compactly:
    - huge tables should be in appendix, only a reduced version should be in the main paper
- many of the propositions are very trivial extension previous ones, and probably not worth to specifically include them in the actual paper.

### Questions
- What is the divergence optimized here?
    -  [1] demonstrated that IQ-Learn minimizes the chi-squared divergence between the policy and a mixture distribution. Here, however, it seems that the approach maximizes the chi-squared divergence between a mixture distribution and another mixture distribution that includes both desired and undesired behaviors.
- How were the baselines trained, like BC-Mix and IQ-learn Mix? Where they trained to imitate only the Mix distribution? If yes, I would argue that this is an unfair since you actually have access to the dataset you would like to imitate (the safe trajectories), and IQ-learn and BC should rather try to imitate that one.

[1] Al-Hafez et. al, LS-IQ: Implicit Reward Regularization for Inverse Reinforcement Learning

Minor Points:
- try to write more compactly:
    - huge tables should be in appendix, only a reduced version should be in the main paper
- many of the propositions are very trivial extension previous ones, and probably not worth to specifically include them in the actual paper.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes an offline IL method that can leverage both expert or near-optimal demonstrations, as well as a collection of undesirable (sub-optimal) demonstrations. The proposed method aims to imitate the expert behavior while avoiding the undesired behaviors. The proposed method can be seen as a flipped version of IQ-Learn, which instead of minimizing the reward gap, it enlarges the gap with the undesired data distribution. As the IQ-Learn is derived under the online setting, the authors also borrow ingredients from the DICE method to estimate the occupancy ratio as importance weights to enable sampling from the data distribution. Although the problem setting is meaningful, I also have some concerns with the paper. Please see the strengths and weaknesses for detailed comments.

### Strengths
- The proposed problem setting is meaningful in practice, which can enable IL policy learning to avoid certain undesirable behaviors.
- Using DICE to convert the IQ-Learn framework to an offline method is interesting.
- The paper is well-organized and easy to read.

### Weaknesses
 - The proposed method basically flipped the formulation in IQ-Learn, from minimizing the divergence with respect to expert distribution, to maximizing the divergence with respect to undesirable data distribution. Although it sounds reasonable, maximizing a divergence is often not a good idea, as it can produce ill-behaved optimization problems and should be avoided in most algorithm designs. Minimizing a statistical divergence may produce stable optimization towards a unique solution, but maximizing a divergence would encourage optimization in an arbitrary direction. Even under the exact same problem setting, SafeDICE still chooses to minimize some divergence to learn their policy. I have some concerns regarding the stability and solution quality of the proposed method in complex tasks.
- The technical novelty of this paper is incremental, as it is basically an offline, flipped version of IQ-Learn. One new item proposed by the paper is the use of DICE-based method to estimate the occupancy ratio, in order to turn the original IQ-Learn framework from online sampling to offline sampling, but this is still somewhat incremental.
- I also have concerns regarding the heavy dependency on the IQ-Learn framework, as based on my past empirical experience, as well as results reported in many recent IL works, IQ-Learn often performs poorly in many tasks. One reason for this is that the optimization procedure of IQ-Learn is overly complex, which often negatively impacts policy learning stability. The proposed method is even more complex than IQ-Learn (has additional occupancy ratio estimation steps).
- The experiments also have a number of problems.
  - First, the authors use a very strange way to construct the unsafe and safe data (one is collected by an unconstrained PPO policy, and the other is collected with SIM). I don't think this is reasonable as compared to most real-world scenarios. data generated from an RL policy typically have a very narrow data distribution. The datasets generated by the authors would create a data distribution that has two easily separable peaks in distribution, which favors discriminator learning, and also makes the problem easy to solve. The authors should consider evaluating on some more commonly used safe offline RL benchmark datasets, like DSRL[1], which could make the conclusion more convincing.
  - Some baselines are also problematic, which are different from the versions reported in their original paper. The authors need to explain and justify why these changes were made.
    - The original IQ-Learn is derived under the online setting, which is not compatible with the offline setting. In the original IQ-Learn paper, their authors did provide an offline version (see Section 5.1 in the IQ-Learn paper), which changed the way how advantage term is estimated, but this version has some theory-to-practice gaps. The authors mentioned that they use the official implementation of IQ-Learn, but modified the actor update part. I'm not sure if the right offline version of IQ-Learn is compared, since comparing with the online version is meaningless. 
    - The "DWBC" baseline is also far from the version reported in the original DWBC paper, with completely different weighting schemes for policy learning.

### Questions
- Can you provide theoretical or empirical evidence to demonstrate the stability of the proposed approach, particularly in complex tasks?
- How is the performance of the proposed method on DSRL benchmark datasets?
- What are the performances if you use the original offline-version IQ-Learn as well as the original DWBC learning objective as baselines?

### Soundness
2

### Presentation
3

### Contribution
2
