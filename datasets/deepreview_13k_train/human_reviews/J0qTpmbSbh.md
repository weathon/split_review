# GenARM: Reward Guided Generation with Autoregressive Reward Model for Test-Time Alignment

- Decision: Accept
- Scores: 6, 6, 6, 8

## Abstract
Large Language Models (LLMs) exhibit impressive capabilities but require careful alignment with human preferences. Traditional training-time methods finetune LLMs using human preference datasets but incur significant training costs and require repeated training to handle diverse user preferences. Test-time alignment methods address this by using reward models (RMs) to guide frozen LLMs without retraining. However, existing test-time approaches rely on trajectory-level RMs which are designed to evaluate complete responses, making them unsuitable for autoregressive text generation that requires computing next-token rewards from partial responses. To address this, we introduce GenARM, a test-time alignment approach that leverages the Autoregressive Reward Model—a novel reward parametrization designed to predict next-token rewards for efficient and effective autoregressive generation. Theoretically, we demonstrate that this parametrization can provably guide frozen LLMs toward any distribution achievable by traditional RMs within the KL-regularized reinforcement learning framework. Experimental results show that GenARM significantly outperforms prior test-time alignment baselines and matches the performance of training-time methods. Additionally, GenARM enables efficient weak-to-strong guidance, aligning larger LLMs with smaller RMs without the high costs of training larger models. Furthermore, GenARM supports multi-objective alignment, allowing real-time trade-offs between preference dimensions and catering to diverse user preferences without retraining.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces GenARM, a testing-time alignment method that leverages the Autoregressive reward model, which is designed by the authors to predict next-token rewards for efficient and effective autoregressive generation. The authors show that this new design can allow us to efficiently guide frozen LLMs toward the target optimal distribution that is usually learned by training time alignment methods such as DPO or PPO. Experiments show that GenARM can outperform previous test-time alignment methods significantly without high costs of training larger models. Further, GenARM also supports multi-objective alignment, which allows users to balance trade-offs of different objectives without retraining.

### Strengths
- The GenARM's design is relatively simple and straightforward, which allows the model to learn the reward effectively. 
- Compared with previous testing time alignment methods that naively used trajectory-based RM to guide the frozen LLMs to generate samples of target distributions, GenARM can provide relatively more accurate token-level guidance and signals with only a small costs to train the GenARM model;
- Empirical experiments shows that GenARM achieves much better performance without training the larger model, while the performance is close to high cost training time-based methods such as DPO;
- The simplicity of the GenARM method also allows users to align the frozen LLMs with multiple objectives, which provide flexibility for real-world alignment problems.

### Weaknesses
 - Compared with training time-based method, there is still gap of the current methods and DPO, while theoretically the authors show that the method can approximate the target optimal distribution;
- The evaluation experiments are relatively simple, only conducted on simple benchmarks;
- It would be good to compare [1] since this is also closely related to testing-time alignment.
- It would be good to add some discussion of previous token-level reward methods or literature, e.g. [2]

### Questions
- There are two ways to predict or output token level rewards, one is to directly view the problem as token-level prediction, and another method is to use an additional head to predict the real-values of the reward, I wonder if authors tried and compare these two methods?

- Regarding the gap of training time methods, I wonder if we leverage more advanced sampling methods such as MCTS to generate more trajectories, will the gap be eliminated?

### Soundness
4

### Presentation
4

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
The paper looks at reward models for RLHF and suggests training a token-level reward model from human preferences by parametrizing it as a sum of log probabilities. They prove that although it constrains the reward models to belong to a specific model class, this class is rich enough to model any reward under the Bradley-Terry preference framework. Empirically, the authors use the token-level reward to perform inference-time alignment.

### Strengths
- The authors identify an important pain point of existing work, such as ARGS, that performs inference-time alignment on a token level without being trained for it.
- The theoretical analysis provides an important insight into the capacity of the parameterization the authors chose.
- The paper is written in a clear and easy-to-follow way.

### Weaknesses
 - While the focus on the downstream application of inference-time alignment is nice and leads to powerful results, I'm expecting work that suggests a new way to train a reward model to first evaluate how well the reward model itself is. Do the proposed reward models achieve better prediction capabilities than trajectory-level reward models? same level? I'm suggesting using rewardbench [1] for such evaluation, but even a classic train-test split on some preference dataset will be interesting.

- The author mentioned some prior work that distilled the reward function to a value function to be used in inference-time alignment [2]. Although these methods require an additional training step it is not a real downside, and I believe it should added as a baseline.



### Questions
- Can training-time alignment algorithms, like PPO, also benefit from the token-level reward? It makes credit assignment easier than trajectory-level rewards.

- [1] is another work that also deals with learning token-level information as part of the reward function. Although it uses different parameterizations, I believe it should be added to the related work section.

- Can you add confidence intervals to the results in Table 1? It will help the reader understand if something like a 48% win rate is significant or not.

[1] Nath, Vaskar, et al. "Learning Goal-Conditioned Representations for Language Reward Models." arXiv preprint arXiv:2407.13887 (2024).

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
Test time alignment, which guide frozen LLMs during test time text generation, can align LLMs with preference without incurring training cost.
To address the mismatch between trajectory-level RMs and autoregressive text generation, this paper proposes GenARM, a test-time alignment approach that leverages the Autoregressive Reward Model to predict next-token rewards for efficient and effective autoregressive generation.
Experimental results and theoretical arguments are provided to justify the proposed approach, especially compared to the prior test-time alignment baselines.

### Strengths
1. The idea of addressing the mismatch between trajectory-level RMs and autoregressive text generation is promising, and have been gaining attention in the community.
2. The proposed method is relatively versatile in experiments, allowing both standard generation, weak-to-strong guidance, and multi-objective alignment.

### Weaknesses
1. Autoregressive Reward Model, trained by aligning the accumulated token-level rewards over a full response with the ground truth preference ordering, has been clearly proposed in the literature, e.g., [1,2] and the reference therein. Further, the idea of per-step-reward guided generation has been presented in [3] and the reference therein. The authors ought to have a adequate citation, discussion, and ideally comparison with these prior works. Otherwise, the contribution of this work will be significantly impaired. In particular, I strongly suggest the authors to move part of the current Related Work to the appendix for discussing in details these prior efforts for dense rewards in LLMs' RLHF/generation.

2. The calculation of token sampling probability eq. (7) will roughly double the decoding time, especially compared to train-time alignment methods.

3. Source code seems not anonymously released for review purpose.

### Questions
1. How would the per-step reward parametrization, eq. (4), mitigate the length bias that longer responses have more term to be sum up, and hence may automatically have a higher aggregate sequence-level reward?
2. In Figure 3 right, why does the word "words" also receives a low reward?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper presents GenARM, a novel reward model parameterization for test-time alignment. Comparing with prior works in the domain of test-time alignment, this paper proposes to use the sum of auto-regressive log probability of each token to be the reward model for the entire trajectory. The training objective function and usage for constrained decoding remains the same. Theoretical analysis has been provided to justify this parameterization of the reward model. Empirically, strong performances have been observed for GenARM against other popular baselines such as ARGS and Transfer-Q over three different settings including human preference alignment, weak-to-strong guidance, and multi-objective alignment.

### Strengths
The clarity of the writing is worth mentioning, I enjoyed following the reading. Each component is properly motivated. And the insights from the experiments are properly organized.

The approach is, as far as I am aware of, novel. It also seems easy to train and does not incur too much additional computational overhead.

Theoretical analysis has been provided for completeness of the paper.

The effectiveness of the proposed method is validated thoroughly in the experiments section over three different settings including human preference alignment, weak-to-strong guidance, and multi-objective alignment. The section of weak-to-strong guidance is particularly informative.

### Weaknesses
The training objective of the reward model (Equation [5]) draws an interesting connection with DPO objective (Equation [7] in DPO). This might result in an unfair comparison with other test-time alighment methods such as ARGS because now that the training cost of the reward model is basically the same as training-time alignment methods like DPO. 

In order to provide a more fair comparison, it might be helpful to dedicate additional experiments/paragraphs illustrating the number of samples/training time comparison with other baselines such as ARGS and Transfer-Q

There is an inconsistency of baselines across different settings. In particular, why is BoN of included in Section 6.1 and Transfer-Q not included in Section 6.2?

### Questions
See weakness, it would be great if the authors can explain the connection of the proposed method with DPO objective

### Soundness
3

### Presentation
4

### Contribution
3
