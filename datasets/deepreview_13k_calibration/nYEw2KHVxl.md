# Offline-to-online Reinforcement Learning for Image-based Grasping with Scarce Demonstrations

- Decision: Reject
- Avg Score: 4.75
- Scores: 3, 6, 5, 5

## Abstract
Offline-to-online reinforcement learning (O2O RL) aims to obtain a continually improving policy as it interacts with the environment, while ensuring the initial policy behaviour is satisficing.
   This satisficing behaviour is necessary for robotic manipulation where random exploration can be costly due to catastrophic failures and time.
   O2O RL is especially compelling when we can only obtain a scarce amount of (potentially suboptimal) demonstrations---a scenario where behavioural cloning (BC) is known to suffer from distribution shift.
   Previous works have outlined the challenges in applying O2O RL algorithms under the image-based environments.
   In this work, we propose a novel O2O RL algorithm that can learn in a real-life image-based robotic vacuum grasping task with a small number of demonstrations where BC fails majority of the time.
   The proposed algorithm replaces the target network in off-policy actor-critic algorithms with a regularization technique inspired by neural tangent kernel.
   We demonstrate that the proposed algorithm can reach above 90\% success rate in under two hours of interaction time, with only 50 human demonstrations, while BC and existing commonly-used RL algorithms fail to achieve similar performance.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper introduces a novel offline-to-online reinforcement learning (O2O RL) approach tailored for robotic grasping with limited image-based demonstrations. The authors tackle the challenge of scarce data by developing a method, called Simplified Q, which integrates a regularization technique inspired by neural tangent kernel (NTK) theory, aiming to stabilize Q-value estimates and reduce the risk of Q-divergence. This method eliminates the need for a target network, which is traditionally used in actor-critic frameworks, allowing the agent to learn effectively with only 50 demonstrations and minimal online interaction. The approach is tested on a robotic grasping task with a vacuum-based manipulator and achieves a high success rate (>90%) in less than two hours, significantly outperforming behavioral cloning (BC) and other standard RL baselines. The paper demonstrates the algorithm’s robustness through ablation studies and comparative experiments, highlighting its potential for real-world applications where exploration is costly and data is limited​.

### Strengths
The proposed technique demonstrates impressive sample efficiency, allowing reinforcement learning to succeed with a limited number of demonstrations.

The paper provides strong empirical support through real-world experiments on image-based robotic manipulation, highlighting the practical applicability of the approach.

### Weaknesses
This work appears to reframe concepts that are well-explored in the reinforcement learning from demonstrations (RLfD) literature. The setup of offline-to-online reinforcement learning (O2O RL), which involves pretraining a policy with approximately 50 demonstrations and then continuing online RL (with optional further use of the demonstrations), as detailed on page 4, closely mirrors standard practices in RLfD. Many RLfD approaches similarly involve pretraining on demonstrations followed by online refinement of the policy using both interaction data and demonstration experiences, in both continuous control domains, e.g. [1][3][4][5], and discrete domains, e.g. [2].

To strengthen the contribution, it would be beneficial for the authors to provide a theoretical discussion on the relationship between O2O RL and RLfD. Additionally, incorporating experimental comparisons with established RLfD approaches would offer a more robust evaluation and ensure that the proposed method’s performance is rigorously benchmarked against strong baselines.

### Questions
Do you have insights on the number of demonstration trajectories required for effective training?

### Soundness
2

### Presentation
4

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper presents a novel regularizer inspired by neural tangent kernel (NTK) literature that can decorrelate the latent representation of different state-action pairs, while maintaining reasonable Q-value estimates. This is presented as a novel offline-to-online reinforcement learning algorithm to learn image-based tasks with small number of demonstrations. The proposed algorithm replaces the target network in off-policy actor-critic algorithms and is shown to overperform alternative methods.

### Strengths
The paper is structured fairly well and evaluations are carried out with experiments and comparisons that demonstrate the proposed algorithm.
The method presented in well framed in relevant literature and presented and formulated in a sound way.
The work is well motivated and its application is relevant to the field, and especially interesting for real-robot applications.
The experimental setup is explained well and plots and graphs are clear.
The paper analyses different aspects of the proposed method, eg latent feature, Q-estimates, performance against BC and SAC.

### Weaknesses
The clarity of the paper can be improved in terms of readability and crispness of contributing statements. For example in Figure 3, it is not immediately clear from the figures why the three plots show performance of different algorithms, while the caption is very verbose and sometime vague (eg "various image encoder" could be more specific).
While it is nice to see comparisons with BC and SAC, it would be interesting to see performance of conservative Q learning as well, as this method is based on it.
Other experiments would have helped support the contribution, eg experiments on D4RL, robomimic, or other available data/tasks.

### Questions
- In which cases does your method stop outperforming others? for example, is there a dependency on the number or quality of demonstrations?
- Can you clarify what aspect in particular of the NTK helps most? could other kernel be used/compared? if not, why?
- Did you test your algorithms on other baselines/tasks?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes a variation on conservative Q-learning (CQL) to use when training a robot grasping policy in a low data regime.

Drawing inspiraction from the Neural Tangent Kernel line of work, the Q-function is parameterized as $Q(s,a) = w^T \phi(s,a)$ where $w$ are the weights at the last layer and $\phi(s,a)$ is some (potentially deep net based) featurizer. If we froze the weights of $\phi(s,a)$, then the kernel $\kappa(s,a,s',a')$ would be exactly $\phi(s',a')^T\phi(s,a)$, and this controls the amount of generalization occurring between state action pairs.

In this work, we do not freeze $\phi(s,a)$, but instead add an auxiliary loss to CQL to keep $\phi(s',a')^T\phi(s,a)$ close to 0 to reduce overgeneralization (a key challenge in offline RL). This is done with an mean squared loss, $E_D[ (\phi(s, a_u)^T \phi(s', a_\pi'))^2]$, encouraging decorrelation between a uniformly sampled action $a_u$ and the current policy's action $a_\pi$.

This method is studied in a real-life grasping task.

### Strengths
The paper does a good job of presenting the core change of their method, as well as motivating why it could help with overgeneralization. The model architectures used are well-defined

### Weaknesses
The method doesn't seem to meaningfully build on prior work.

* RL and BC have been applied to image-based grasping before, including in the low demonstration regime.
* Image-based RL has on occasionally been done before as well (with SAC)

The absolute performance numbers relative to the BC baseline seem quite low. The paper is correct in observing that the NTK objective from Kumar et al 2022 is partly ill-formed: minimizing $E_D[ \phi(s, a_u)^T \phi(s', a_\pi')]$ allows for a negative kernel value, which could let learning in one Q-value cause unlearning in another Q-value. However, the Ma et al 2023 citation is described as also doing this, which is incorrect. The Ma et al 2023 paper minimizes the absolute value $|\phi(s, a_u)^T \phi(s', a_\pi')|$, i.e. it uses an L1 loss. This paper does technically do something different (L2 loss instead), but the results of doing so aren't great.

In short I'm not very convinced on novelty or effectiveness. This combined with using a single hard-to-reproduce robot environment make me believe the paper is not good enough.

### Questions
Could the authors explain why they remove the target network when including the NTK regularizer? As far as I can tell, the target network is maintained in prior work that uses NTK regularization, I am not sure why it was removed.

### Soundness
3

### Presentation
3

### Contribution
1

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a regularization method for CQL, improving efficiency in the offline-to-online RL setting. Inspired by the neural tangent kernel (NTK) literature, the paper replaces the target Q network with an NTK regularization term. Experiments are conducted on an image-based grasping task using a vacuum. Results show that the method outperforms BC and RL baselines after online RL and does not rely on a pre-trained image encoder.

### Strengths
1. To my knowledge, the proposed NTK regularization for offline-to-online CQL is a novel approach that addresses the learning stability issues.
2. The paper demonstrates promising experimental settings on a real-world robotic grasping task, taking acceptable training time to improve the policy on the real robot.
3. The paper presents a detailed experimental analysis of the grasping task.

### Weaknesses
1. My main concern is that the proposed method appears to be a general approach for offline-to-online RL rather than designed for robotic grasping. The motivation behind the proposed regularization term does not seem related to the task of robotic grasping. However, the majority of the paper is written as if it is focused on robotic grasping.

2. Because of this, I suggest that the experiments should include various RL benchmarks, such as D4RL, to demonstrate the general effectiveness of the proposed algorithm, rather than focusing solely on a single vacuum grasping task.

3. Regarding the literature on robotic grasping, the use of a vacuum to grasp flat objects, as demonstrated in the paper, represents a relatively simple setup. It remains unclear whether the method would be effective with parallel grippers or in grasping more complex objects. If hardware devices are not available, conducting simulation experiments on these settings could strengthen the experimental results.

### Questions
Please see the Weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2
