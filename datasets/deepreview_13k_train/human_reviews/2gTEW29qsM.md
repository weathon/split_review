# Masked Generative Priors Improve World Models Sequence Modelling Capabilities

- Decision: Reject
- Scores: 6, 5, 6, 5

## Abstract
Deep Reinforcement Learning (RL) has become the leading approach for creating artificial agents in complex environments. Model-based approaches, which are RL methods with world models that predict environment dynamics, are among the most promising directions for improving data efficiency, forming a critical step toward bridging the gap between research and real-world deployment. In particular, world models enhance sample efficiency by learning in imagination, which involves training a generative sequence model of the environment in a self-supervised manner.
Recently, Masked Generative Modelling has emerged as a more efficient and superior inductive bias for modelling and generating token sequences. Building on the Efficient Stochastic Transformer-based World Models (STORM) architecture, we replace the traditional MLP prior with a Masked Generative Prior (e.g., MaskGIT Prior) and introduce GIT-STORM.
We evaluate our model on two downstream tasks: reinforcement learning and video prediction. GIT-STORM demonstrates substantial performance gains in RL tasks on the Atari 100k benchmark.
Moreover, we apply Categorical Transformer-based World Models to continuous action environments for the first time, addressing a significant gap in prior research. To achieve this, we employ a state mixer function that integrates latent state representations with actions, enabling our model to handle continuous control tasks. We validate this approach through qualitative and quantitative analyses on the DeepMind Control Suite, showcasing the effectiveness of Transformer-based World Models in this new domain.
Our results highlight the versatility and efficacy of the MaskGIT dynamics prior, paving the way for more accurate world models and effective RL policies.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper, Masked Generative Priors Improve World Models Sequence Modelling Capabilities, introduces GIT-STORM, an extension of the STORM architecture, incorporating MaskGIT as a dynamics prior to enhance sequence modeling in world models. The authors address two main gaps in previous research: the limitation of transformer-based world models in continuous action environments and the inadequacies of prior methods, like STORM, in capturing effective state representations. Through experiments on Atari 100k (discrete) and DeepMind Control Suite (continuous), GIT-STORM demonstrates improvements in RL and video prediction, suggesting that Masked Generative Priors could be a powerful inductive bias for world models, supporting broader applicability across diverse RL tasks and environments.

### Strengths
The empirical evaluation spans discrete and continuous action benchmarks, providing a robust assessment of GIT-STORM’s performance. The reported results demonstrate that GIT-STORM not only improves sample efficiency in RL tasks but also enhances video prediction quality, particularly in the Atari 100k benchmark, aligning well with the study's objectives. Moreover, the paper is well-written with a clear structure, providing a good experience as a reader. Extending the transformer-based world models to continuous action tasks also poses a sufficient novelty and broadens the utility of these models in RL and video prediction applications.

### Weaknesses
It remains unclear why GIT-STORM does not consistently outperform STORM across all benchmarks or why it fails to close the performance gap with DreamerV3 in environments beyond Atari 100k. The paper does not fully explain the conditions under which GIT-STORM’s improvements are more marginal, suggesting a need for clearer insights into the impact of individual architectural components. Specifically, the analysis lacks a detailed breakdown of performance across different environment characteristics, such as the complexity of the state space or the nature of the reward function, which could explain the variability in GIT-STORM's effectiveness. Furthermore, the paper does not address the potential for overfitting to the specific environments used in the study, which could limit the generalization capabilities of the model. 

The paper claims state-of-the-art results for GIT-STORM on select environments, yet Table 6 seems to indicate that DrQ-v2 outperforms GIT-STORM on two environments (where the authors claim they are better?). Clarifying the conditions under which GIT-STORM achieves these results or adjusting the claim would help ensure consistency and accuracy in presenting the model's achievements. The lack of a clear definition of what constitutes state-of-the-art performance in the context of this work makes it difficult to assess the validity of this claim. A more rigorous comparison, including statistical significance testing, would be necessary to support the claim of state-of-the-art performance.

The proposed approach for handling continuous action spaces is promising, yet lacks a comprehensive empirical analysis. Additional studies on more diverse continuous control tasks, including those with higher dimensionality and more complex dynamics, could provide stronger validation of the state mixer function's effectiveness and the broader applicability of the model in continuous settings. Most importantly, the modifications from STORM to GIT-STORM are extensive, involving MaskGIT, state mixer, policy adjustments from DreamerV3, and an observation module from STORM. The compounded modifications make it difficult to discern the exact contribution of each component to the reported performance improvements. A more focused ablation study is required to isolate the impact of each modification, for example, by systematically removing each component and evaluating the resulting performance changes.

### Questions
- Could the authors elaborate on why GIT-STORM occasionally does not surpass STORM and the conditions where improvements are only minor? Understanding this would clarify the contextual efficacy of the MaskGIT prior.
- Regarding the reported state-of-the-art claim, Table 6 suggests that DrQ-v2 outperforms GIT-STORM in some highlighted environments. Could the authors comment why they claim GIT-STORM provides SOTA results on these? It is not the case, right?
- What is the rationale for improving STORM over directly utilizing DreamerV3, which appears to perform better in many scenarios? Or put differently: why would one care to improve STORM with the proposed modifications when there is DreamerV3 and I could just use it or improve over DreamerV3? 

I am open to increase my score once there is clarity on these questions.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces GIT-STORM, which incorporates three modifications to the base algorithm STORM: a MaskGIT prior that replaces the MLP dynamics head, a draft-and-revise decoding scheme for enhanced consistency, and a state mixer for continuous action environments. Experimental results demonstrate that GIT-STORM surpasses STORM on both Atari 100K and DMC benchmarks. Video prediction results indicate that this improvement is attributed to more accurate representations.

### Strengths
- The motivation of incorporating a MaskGIT prior into the STORM architecture is clear.
- The proposed method is straightforward and easy to reproduce.
- MaskGIT can effectively improve the video prediction quality of STORM,  indicating applicability of GIT-STORM to more complicated tasks.

### Weaknesses
 - The paper contains a misstatement in its contributions. The authors claim that they "apply transformer-based world models to continuous action environments for the first time". This claim is inaccurate, as TransDreamer[1] can also be applied to continuous action environments. The authors are evidently aware of this paper, given that they have cited it in this work.
- The state-mixer design is not properly addressed. If the authors claim this part of their contribution, they should either elaborate on the design, or provide empirical results to show the superiority of this method. Based on the overlapping tasks, TransDreamer appears to have better performance than GIT-STORM+state-mixer on the continuous control benchmark DMC.
- The experimental results in Atari 100K only demonstrate marginal improvement. The gain over STORM seems to primarily originate from the gopher task alone, which contains inconsistent results, as detailed in the questions section.

### Questions
- Results on the Freeway task have very high variance according to Figure 10. How many out of the five runs does GIT-STORM actually achieve non-zero performance? 
- The most challenging aspect of learning the Freeway task is obtaining the first successful trajectory, which I believe is more related to the exploration strategy than state predictions, given the sparse rewards. How does GIT-STORM assist the agent in exploring more efficiently? Is this strategy stable, or are the successful trajectories obtained by random seeds?
- Why would the pendulum swingup task fail for both STORM and GIT-STORM? DreamerV2, DreamerV3 and TransDreamer can learn this task fairly easily.
- The experiment results in Table 5 and Figure 10 appear inconsistent. For instance, the Gopher score reported in Table 5 is 8562, but the last point in Figure 10 shows a performance of around 2500. Do these two results use different metrics?
- Could you add the learning curves of STORM or DreamerV3 to Figure 10 for a better comparison, considering that you have reproduced these results?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposed to replace the MLP head with MaskGIT prior in STORM to achieve a higher quality of latent generation, and therefore achieve better performance on the Atari100k benchmark.
This paper also bridges the gap of the lack of evaluation of transformer-based world models on continuous control tasks.

### Strengths
1. This paper clearly distinguishes itself from previous work, with good comparison and illustration.

2. One-hot categorical latent is widely used in recent model-based RL, yet the research on it is insufficient. This paper provides a novel view of it.

3. This paper bridges the gap of the lack of evaluation of transformer-based world models on continuous control tasks.

### Weaknesses
1. The motivation and effect of using MaskGIT head in world models are unclear.
Is there any evidence that the world models would have hallucinations, and how could a MaskGIT head mitigate such issues?
How to distinguish if the improved performance (both RL and FVD) comes from more parameters or the MaskGIT prior?

    There should be some further investigation into the mechanism of the MaskGIT head. Such as:

    (a) What's the difference between the latent variables (or distributions) generated with the MLP head and MaskGIT head?

    (b) This MaskGIT head looks like a skip/residual connection from $z_{t}$ to $\hat{z}_{t+1}$, would this reduce the KL divergence in the training or imagination?

    (c) These are sample questions. An investigation like this would improve the soundness and contribution of this paper.

2. Section 2.1 could be more concise, as these are not quite related to the key contributions and are frequently repeated in each of the model-based RL papers.

### Questions
1. On lines 307-309, I think STORM uses KV caching in both the conditioning phase and the imagination phase, see [here](https://github.com/weipu-zhang/STORM/blob/e0b3fd44320d7e213ec905c673ad3f35b61b89f4/sub_models/world_models.py#L363). The `predict_next()` uses `forward_with_kv_cache()` for decoding.

2. Missing comma on line 214?

3. What's new in the proposed state mixer compared to the STORM's action mixer?

4. `Freeway` is a hard exploration environment, as the agent has to repeat the `up` operation many times to get a first reward, which is a rare event for a random policy. Without the first reward, the value space is all zero and the policy would be further optimized as a uniform random policy. STORM, IRIS, and DIAMOND have different tricks that can mitigate such an issue. But what is the underlying reason for GIT-STORM to reach a non-zero result? I think this is not related to the improved decoding or world modelling quality since DreamerV3 and STORM (w/o traj) could also produce a nearly perfect reconstruction and prediction on `Freeway`.

5. For the `Quadruped Run` in Figure 6, I wonder if it's too small (compared to Figure 4 in [DreamerV3](https://arxiv.org/pdf/2301.04104)).

6. Lines 529-530, "Replacing...", the order is reversed.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes GIT-STORM, which utilizes a MaskGIT model instead of an MLP for the prior head in world models (based on STORM). It also makes minor modifications (a state mixer) to support continuous actions. Experiments are done on Atari100k and DMC benchmarks, considering both policy learning and video prediction performance. GIT-STORM outperforms its base method STORM.

### Strengths
To my knowledge, MaskGIT models, with their strong expressiveness, are not yet utilized for world models in the MBRL community.

### Weaknesses
1. The illustration and descriptions of the model are confusing. Can authors provide more insights for their specific designs?
   - In Figure 1 (left), it seems that GIT-STORM uses masked $z_t$ as inputs for reconstructing $z_{t+1}$. This is strange since, in the original MaskGIT, we mask and reconstruct masked target tokens. Similarly, I think it is more reasonable to mask $z_{t+1}$ as inputs. The iterative decoding process during inference, where the output $z_{t+1}$ is fed back as input, also creates a discrepancy with the training phase where the input is $z_t$. The paper needs to clarify how this iterative process aligns with the training procedure, where a masked version of $z_t$ is used as input to predict $z_{t+1}$.
   - In Figure 1 (left), there is no $\xi_t$ but only $\eta_t$. 
   - Also, the dot product seems to be a commonly used trick that ties weights for embedding and linear layer before Softmax. If so, relevant literature should be cited. Specifically, this weight tying strategy is widely used in language models and MaskGIT implementations, and the paper should acknowledge this connection and cite relevant works.
   - The Draft-and-Revise decoding scheme, if not proposed by this work, should be moved into a preliminary section. 
2. The contribution to supporting continuous actions is overclaimed (as 'for the first time'). In fact, concatenating or summating continuous inputs with hidden states is a too straightforward approach in current VLA models (e.g., OpenVLA for inputting continuous visual representations) and action-conditioned video prediction models (e.g., iVideoGPT for inputting continuous actions).
3. The performance of GIT-STORM on DMC is outperformed by its base method, DreamerV3.

### Questions
There are also some minor questions:

1. In Line 309, why KV cache can improve sample efficiency? Do you mean computational efficiency?
2. To my knowledge, perplexity is a metric whose lower values mean better. However, in Table 3, higher perplexity is marked as better.
3. In Figure 6, the quadruped agents are too small in the images. This work seems to have used an unusual camera setting for these tasks.

If the authors well address my concerns, I am willing to improve my rating.

### Soundness
2

### Presentation
2

### Contribution
3
