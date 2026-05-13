# Value-aligned Behavior Cloning for Offline Reinforcement Learning via Bi-level Optimization

- Decision: Accept
- Scores: 6, 8, 8, 6

## Abstract
Offline reinforcement learning (RL) aims to optimize policies under pre-collected data, without requiring any further interactions with the environment. Derived from imitation learning, Behavior cloning (BC) is extensively utilized in offline RL for its simplicity and effectiveness. Although BC inherently avoids out-of-distribution deviations, it lacks the ability to discern between high and low-quality data, potentially leading to sub-optimal performance when facing with poor-quality data. Current offline RL algorithms attempt to enhance BC by incorporating value estimation, yet often struggle to effectively balance these two critical components, specifically the alignment between the behavior policy and the pre-trained value estimations under in-sample offline data. To address this challenge, we propose the Value-aligned Behavior Cloning via Bi-level Optimization (VACO), a novel bi-level framework that seamlessly integrates an inner loop for weighted supervised behavior cloning (BC) with an outer loop dedicated to value alignment. \textcolor{blue}{In this framework, the inner loop employs a meta-scoring network to evaluate and appropriately weight each training sample, while the outer loop maximizes value estimation for alignment with controlled noise to facilitate limited exploration.} This bi-level structure allows VACO to identify the optimal weighted BC policy, ultimately maximizing the expected estimated return conditioned on the learned value function. We conduct a comprehensive evaluation of VACO across a variety of continuous control benchmarks in offline RL, where it consistently achieves superior performance compared to existing state-of-the-art methods.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In offline RL, behavior constraints (BC objectives) and value estimation (Q-values) are commonly used strategies to train policies. However, when both strategies are applied together, they tend to interfere with each other, often resulting in sub-optimal performance. To address this issue, the paper proposes VACO, which first learns the value network (Q-function) and then employs a bi-level learning process: training a meta-score network in the outer loop, and updating the policy using a weighted BC objective in the inner loop. The proposed VACO method is compared with several baselines on tasks from the D4RL dataset. Experimental results demonstrate that VACO achieves superior performance across tasks and various data resource settings.

### Strengths
- **Paper Writing:** The paper has a coherent and concise narrative. The challenge is clearly described, the proposed method is easy to understand, and the figures and tables are well-designed, allowing readers to quickly grasp the key points.

- **Method Originality:** Although applying learnable models/parameters to dynamically adjust the weight of each training sample is not a new idea, the insight to develop bi-level optimization in the context of behavior constraints in offline RL is underexplored, lending sufficient originality to the method.

- **Reproducibility:** The inclusion of source code and detailed experimental information enhances the paper’s reproducibility.

### Weaknesses
 **Major Concerns**
- **Theroem Correctness:** While the proposed method seems to have enough originality, I have doubts about its supporting theorem, particularly the assumption on line 261, i.e. $\frac{\partial\phi_{t-1}}{\partial\alpha} \approx 0$. The paper indicates that this assumption is supported by the Markov property. However, if I understand correctly, the Markov property primarily concerns state transitions in a stochastic process, where the future state depends only on the current state (and action, in the case of an MDP) and not on past states. In this scenario, however, it involves dependencies between functions across iterations, not probabilistic state transitions. I believe the divergence of $\phi_t$ and $\phi_{t-1}$ should be evaluated to better determine whether this assumption is valid.
- **Evaluation Tasks:** The proposed method and baselines are only examined on simple tasks from one benchmark, i.e., D4RL, making it unclear whether the comparison results hold sufficient generalization. I recommend conducting the evaluation on Adroit tasks (also from D4RL) at least, or on more complex benchmarks such as Robomimic [R1], which also provides collected trajectories with different levels of expertise.
- **Ablation Studies:** The paper lacks in-depth ablations. While conducting the study on removing inputs of the meta-score network is a nice start, it is more basic. More comprehensive ablations, such as visualizing the relationship between assigned weights and the state-action pairs collected by different policies, could better demonstrate the effectiveness of the proposed method.
- **Baseline Details:** The paper lacks descriptions of the selected baselines. Although the paper categorizes baselines into four groups, there is no explanation of each baseline's key insights or features, raising concerns about whether the compared baselines are robust enough.

---

**Minor Concerns**
- **Task Setting:** While I acknowledge that offline RL is a critical area, especially considering safety and training efficiency, the setting studied in the paper is somewhat dated; the policy can only learn from a single collected dataset. Recent offline RL works have explored more diverse directions, such as auxiliary unlabeled data [R2, R3], primitive discovery [R4], or offline-to-online settings [R5], which may have the potential to create a greater impact.

- **Experimental Results:** As mentioned in the appendix, some results from previous works are copied. I suspect this is also the reason for some missing fields in Table 1. I suggest conducting experiments for all methods under the same conditions (same devices and random seeds) to better demonstrate the fairness of the comparison.

- **Typos:** While the paper is generally well-written, there are some typos that should be corrected. For instance:

  line 094, line 478: "In details" -> "In detail"

  line 227: "Gauss noise" -> "Gaussian noise"

  line 236: "square error" -> "squared error"

  line 239: "Through such bi-level optimization framework" -> "Through such a bi-level optimization framework"
  
  line 307: (1) classical methods: (1) Explicit regularization methods: -> This line needs clarification or correction.

Note: Addressing these concerns is highly encouraged, but they did not substantially affect my evaluation.

### Questions
1. Could you please clarify how the assumption on line 261 is derived? I believe the Markov property may not be an appropriate basis for this assumption.
2. Does the proposed VACO demonstrate sufficient generalization ability? Can it still achieve superior performance on more challenging tasks, such as those in the Adroit or Robomimic datasets?
3. Can the learned meta-score network assign low weights to state-action pairs collected by policies that exhibit poor performance? Any visualizations or discussions would be helpful.
4. Please provide more details about the compared baselines so we can better assess the superiority of the proposed method.
5. From line 748 to line 753, the paper states that any value estimation loss function and any behavior cloning-based policy extraction loss function can be used. Is this claim supported by any experiments?
6. Why is Gaussian noise used in Eq. 6? Additionally, why is the noise injected into the state rather than into the intermediate latent variables or the output logits?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
Summary:

This paper introduces a novel bi-level offline DRL framework called value-aligned behavior Closing via bi-level optimization (VACO).
The authors identify critical challenges in offline RL, particularly out-of-distribution (OOD) and value alignment issues.
To address these issues, the VACO framework employs a bi-level optimization strategy integrating a meta-scoring neural network to generate adaptive weights for behavior learning.
In the various tasks in the D4RL benchmark, VACO achieves state-of-the-art performance compared to other SOTA methods.

### Strengths
Strengths

1. This paper's writing is excellent. It utilizes illustrative figures to clearly demonstrate the out-of-distribution (OOD) and value alignment issues in offline DRL and effectively explains the motivation behind the method. The methodology and experimental setup are clearly presented, with an appendix and code provided for additional details.

2. This approach combines the maximization of the value estimation function with weighted behavioral cloning from a novel perspective, proposing a bi-level learning framework that simultaneously mitigates OOD issues and value alignment issues.

3. The method was tested across multiple tasks on the D4RL benchmark. The results are impressive, as the method, using a simple MLP, surpasses most other methods, including diffusion networks, and achieves the highest average performance.

### Weaknesses
Weaknesses

1. The name of the method may not be entirely appropriate. Although it includes "bi-level optimization," in lines 9 and 10 of the algorithm, the two networks are alternately trained without forming an outer and inner loop. This approach resembles adversarial training, similar to the generator and discriminator in GANs. A more suitable name might be "Adversarial/Complementary Value-Aligned Behavior Cloning". The current name implies a nested optimization structure that is not actually present in the algorithm, potentially misleading readers about the method's core mechanics.

2. Could the authors further explore the relationship between maximizing the value estimation function and weighted behavioral cloning in Equation 6? For instance, do they exhibit an adversarial relationship, or are they complementary? It would be helpful to provide training loss curves or other visualizations of the two losses to clarify this relationship. Specifically, it is unclear how the simultaneous optimization of these two objectives affects the overall learning process. Are there scenarios where maximizing the Q-function might conflict with the behavioral cloning objective, and how does the algorithm handle such situations? A deeper analysis of the interaction between these two loss terms is needed.

3. Could the authors provide additional results for tasks in the adroit and kitchen environments in D4RL, as well as learning curves for MuJoCo tasks? The current evaluation is limited to a subset of D4RL tasks, and expanding the evaluation to include more complex environments like adroit and kitchen would provide a more comprehensive assessment of the method's robustness and generalizability. Furthermore, learning curves for MuJoCo tasks are essential to understand the training dynamics and convergence behavior of the proposed approach.

4. I am very curious about the relationship between the meta-score and Q-value for a given state-action pair. Could you provide some statistical analysis? Do they exhibit a proportional relationship, such that a larger Q-value corresponds to a higher meta-score? If so, could the Q-value be used as a substitute for the meta-score? It's not clear how the meta-score is related to the value function, and whether it provides information beyond what is already captured by the Q-value. If the meta-score is highly correlated with the Q-value, it might be redundant and unnecessary.

### Questions
Please check the weakness section.

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This work proposes a novel algorithm, VACO, that combines two offline RL approaches: behavior cloning and value estimation, in a meta-learning framework. In particular, the outer loop uses value estimation to train the weights of behavioral cloning data samples. The approach is designed to balance common issues in offline reinforcement learning: namely, the over-estimation of the value of out-of-distribution state-action pairs, and convergence on sub-optimal actions in-distribution.

### Strengths
The motivation is clear: the issues with current offline RL methods are clearly established.

The approach is original: it combines two well-established methods in a novel way that produces better results than either method alone.

SOTA performance on an established benchmark.

### Weaknesses
The related works section (Section 5) is placed after the experiments (Section 4), despite describing the methods compared in the experiments. This made the experiments section much harder to parse through on the first pass. Placing this information somewhere before Section 3 could greatly improve the paper’s clarity on the first readthrough.

The writing is hard to parse in a few places. In the abstract (lines 25-26), the description of inner and outer loops appears to suggest that the outer loop only adds noise, rather than training the weighting, which it does according to the description in 3.3. This lack of clarity could lead to misinterpretations of the core algorithm.

There is no analysis on training costs (number of iterations required or wall time). Given the use of meta-learning, I would assume that the approach is generally more costly than most of the alternatives. Because of the competitive performance of the algorithm, it doesn’t need to be faster than other methods, but cost would be an important concern in determining when to use this approach versus a simpler one. Furthermore, the lack of discussion on computational resources used for the experiments makes it difficult to assess the practical scalability of the method.

### Questions
For the experiments, is the same value network used across all approaches in each environment? Or does each approach have a separately trained value network?

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes to address the issue of balancing the value estimation and behaviour cloning in face of data of a mixed quality. The proposed idea is to turn the policy learning and behaviour regression losses to a bi-level optimization. The core idea is to learn a score network to assign a weight to each datapoint in the inner loop such that the learning signal from low-quality data is downplayed. The score network is tuned in the outer loop with a form of policy learning loss with a regularization of adding Gaussian noise to the predicted action. The inner loop is expanded as a one-step update rule so the gradient can be derived. The approach is tested on Hopper, HalfCheetah, Walker2D and AntMaze environments, reporting improvements over a range of baselines with different behavior cloning regularizations.

### Strengths
* The idea is well motivated with the challenges of aligning trained behaviour and the one used for value estimation well elaborated. 

* The core idea of enforcing a weighted objectives through bi-level optimization is intuitive and easy to understand.

* The selected baselines seem relevant to the comparison and assessment.

### Weaknesses
 * Insufficient evaluation on more complicated task environments. The selected tasks look simple and could be expanded to cover tasks beyond locomotion. Test results on tasks relying on visual input and manipulation tasks such as Fetch could improve the soundness of the results.

* The results only contain ultimate performance on a limited set of tasks. There is no direct evidence or analysis that how the proposed learning scheme mitigate the alignment issue. A study that can explicitly attributes the improvement to a better alignment could lead to a stronger argument.

* The performance improvement seems diminished on more complicated AntMaze task. This raises the question whether the method can scale up to more complicated scenarios as suggested above.

* Part of the writing on the inner loop derivative is a bit unclear. See the questions below.

### Questions
* Can the method be demonstrated to work well on more comprehensive benchmarks including more diverse skills and sensory input?

* Can the observed improvement be linked to a better alignment that was identified as the root cause of inferior performance of previous approaches?

* Can the score network be used to evaluate data snippets to show they are indeed reflecting the optimality of the data?

* Eq. (6) indicates a noise perturbation to the state. Typo?

* Eq. (8) avoids second-order derivatives and it seems due to the assumed $\frac{\partial \phi_{t-1}}{\partial \alpha} \approx 0$. Why this can be valid and what is defined as the Markov process here?

### Soundness
3

### Presentation
3

### Contribution
2
