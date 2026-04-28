# Compositional Conservatism: A Transductive Approach in Offline Reinforcement Learning

- Decision: Accept
- Avg Score: 6.33
- Scores: 6, 8, 5

## Abstract
Offline reinforcement learning (RL) is a compelling framework for learning optimal policies from past experiences without additional interaction with the environment.
   Nevertheless, offline RL inevitably faces the problem of distributional shifts, where the states and actions encountered during policy execution may not be in the training dataset distribution.
   A common solution involves incorporating conservatism into the policy or the value function to safeguard against uncertainties and unknowns.
   In this work, we focus on achieving the same objectives of conservatism but from a different perspective.
   We propose COmpositional COnservatism with Anchor-seeking (COCOA) for offline RL, an approach that pursues conservatism in a \textit{compositional} manner on top of the transductive reparameterization \citep{transd_aviv2023}, which decomposes the input variable (the state in our case) into an anchor and its difference from the original input.
 Our  COCOA seeks both in-distribution anchors and differences by utilizing the learned reverse dynamics model, encouraging conservatism in the compositional input space for the policy or value function.
   Such compositional conservatism is independent of and agnostic to the prevalent \textit{behavioral} conservatism in offline RL.
   We apply COCOA to four state-of-the-art offline RL algorithms and evaluate them on the D4RL benchmark, where COCOA generally improves the performance of each algorithm.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presents an approach to enhance offline reinforcement learning by reparameterizing out-of-distribution states into two simpler components: an anchor and a difference from the anchor, leveraging bilinear transduction for better generalization. The proposed anchor-seeking policy, which utilizes reverse model rollouts, aims to identify these components from within the distribution seen during training, ensuring relevance and improving computational efficiency. The policy is complemented by a reverse dynamics model that diversifies the training data, allowing the model to generalize to new environments effectively. This novel method has been empirically shown to enhance the performance of several state-of-the-art offline RL algorithms.

### Strengths
Pros:
1. The paper is well-written and easy to follow.  The reproducibility is good as it provided code.
2. Introduce a novel perspective in finding conservatism in the compositional input space, different from the previous works in finding conservatism in the behavioral space.
3. COCOA can be used in-combination with other offline RL algorithms to improve the performance of previous model-free and model-based algorithms.
4. Good experimental results with SOTA performance on the D4RL benchmarks.
5. Ablation study in comparing with a baseline anchor selection process demonstrate that their anchor-seeking methods is crucial for their performance.

### Weaknesses
Cons:
1. Why not train a reverse policy but use a random divergent reverse policy? Is there an ablation study on this?
2. The evaluation is only limited to D4rl benchmarks and why in IQL, adding COCOA does not improve much among all the d4rl tasks, could you provide some insights into this?

### Questions
please see weakness

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a new form of conservatism in offline RL called COCOA, specifically with "anchor states" defined by a learned dynamics model. The use of anchor states is motivated by work transforming the out-of-support generalization problem to an out-of-combination problem in the offline RL context.

Experiments show that the addition of COCOA to common offline RL algorithms results in improved performance across the D4RL benchmark suite, and ablations show that the proposed anchor-seeking method is crucial for good performance across said domains.

### Strengths
Overall, the paper is very well written, and generally easy to follow. While I haven't worked in this area in RL research a lot, it is interesting to see the extension of a supervised learning approach for use in offline RL, and for it to work as well as it does seem to work here.

The performance results are very interesting, and show that anchor-seeking methods can improve performance especially in the medium-expert domains, where maybe excess conservatism leads to suboptimal performance for most offline RL algorithms. The experiments and ablations are generally solid and thorough, across many relevant benchmarks.

### Weaknesses
It seems that this model-based approach here is similar to those in forward model-based offline RL algorithms such as COMBO [1], where the goal is to use a larger coverage state-action distribution for offline RL through the use of a forward dynamics model. It would be interesting to see the comparison between this approach (combined with CQL) and COMBO (if COMBO results can be reproduced), as COMBO also shows significantly less conservatism when used with CQL compared to CQL on its own. I wouldn't say that this is a big weakness, but I feel like from a high level it would be worth it to do this comparison.

There has also been work showing that even synthetic experience replay [2] from strong generative models is useful for RL -- might be worth citing or comparing against as well, but I may be wrong here. Again, not a huge weakness in my eyes but would be interesting to see the comparison.

### Questions
No real big questions here actually -- very solid!

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Authors propose method COCOA for adapting bilinear transduction to offline RL setup with training environment dynamics and anchor-seeking policy.

### Strengths
Proposed approach may boost the performance of the offline RL algorithms and applicable to any actor-critic algorithm. Approach is tested on 4 different algorithms.

### Weaknesses
 * Training world models might be very time-consuming.

* Proposed approach lead to the improvement only in approximately 58% of cases. And performance might be decreased dramatically. I've also calculated the differences between "+ COCOA" and "Alone" in Table 1 and it appeared that COCOA decreases performance down by 0.8 points. This indicates that only specific algorithms are expected to benefit on average by COCOA. And for MOPO and MOBILE hyperparameters were heavily tuned for each dataset which might be the cause why they benefited.

* Evaluation is performed only on the Gym MuJoCo datasets which I think is not enough now and evaluation on D4RL AntMaze or Adroit is essential. As an alternative, offline-to-online setup might be tested.

### Questions
* What is the training time for algorithms with and without COCOA?

* What is hyperparameters sensitivity for MOPO and MOBILE when COCOA is added compared to the same algorithms without COCOA? EOP (https://arxiv.org/abs/2110.04156) can be used for this purpose.

* What are IQL scores on random datasets?

* Are there any thoughts why IQL suffer from COCOA?

* How would COCOA behave with offline RL algorithms which regularize policy? E.g. ReBRAC (https://arxiv.org/pdf/2305.09836.pdf) which is the state-of-the-art algorithm from this family.

* Could you please run experiments on AntMaze or Adroit domains or test your approach in offline-to-online setup? At least for IQL and MOBILE.

* Please add the average scores for each of the approaches in the Table 1 so it is clear what is actual impact of COCOA on algorithms?

Minor text issues: the second paragraph of section 2.1 duplicates information from the first one. Results section has  "**FFor** IQL,".

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
