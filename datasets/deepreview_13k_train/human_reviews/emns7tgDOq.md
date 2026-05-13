# Beyond the Known: Decision Making with Counterfactual Reasoning Decision Transformer

- Decision: Reject
- Scores: 3, 5, 5, 3

## Abstract
Decision Transformer (DT) plays a crucial role in modern reinforcement learning, leveraging offline datasets to achieve impressive results across various domains. However, DT requires high-quality, comprehensive data to perform optimally. In real-world applications, such ideal data is often lacking, with the underrepresentation of optimal behaviours posing a significant challenge. This limitation highlights the difficulty of relying on offline datasets for training, as suboptimal data can hinder performance. To address this, we propose the Counterfactual Reasoning Decision Transformer (CRDT), a novel framework inspired by counterfactual reasoning. CRDT enhances DT’s ability to reason beyond known data by generating and utilizing counterfactual experiences, enabling improved decision-making in out-of-distribution scenarios. Extensive experiments across continuous and discrete action spaces, including environments with limited data, demonstrate that CRDT consistently outperforms conventional DT approaches. Additionally, reasoning counterfactually allows the DT agent to obtain stitching ability, allowing it to combine suboptimal trajectories. These results highlight the potential of counterfactual reasoning to enhance RL agents' performance and generalization capabilities.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The authors introduce a Counterfactual Reasoning Decision Transformer (CRDT) that integrates counterfactual actions into the training process. 

To create a counterfactual dataset, they select actions based on heuristic criteria—such as a selection probability threshold (e.g., less than $\delta$) and expected ranges for continuous actions. 

They then generate trajectories by executing these counterfactual actions, focusing on less confident, low-return-to-go trajectories for the counterfactual dataset. 
The Decision Transformer (DT) is trained using both this counterfactual dataset and the original offline dataset.

### Strengths
Novel Concept: To the best of my knowledge, this is the first attempt to incorporate counterfactual reasoning into DT training, which adds a novel approach to decision transformers.

### Weaknesses
 - Weak Connection to Causal Inference: Although inspired by causality, the method lacks a clear link to causal inference concepts, something like causal effects. The approach mainly introduces how to generate uncertain trajectories and incorporate them into DT training. The method does not explicitly model causal relationships between actions and outcomes, nor does it attempt to estimate any form of treatment effect. The connection to causality is therefore superficial, primarily serving as a motivation rather than a core methodological component.

- Marginal Novelty: The proposed method does not make a strong theoretical contribution beyond its counterfactual data generation process. And the proposed method is not novel. The core idea of generating counterfactual data by perturbing actions and observing the resulting trajectories is not entirely new; similar techniques have been explored in other contexts. The novelty is further diminished by the lack of a strong theoretical grounding for the counterfactual generation process.

- Ground-Truth Validity of Counterfactual Trajectories: There’s no clear guarantee that the generated counterfactual trajectories are really real within the ground-truth Markov Decision Process (MDP). This raises concerns about the reliability of using these trajectories in training. The method relies on learned models to generate these trajectories, which may not accurately reflect the true dynamics of the environment. Without a mechanism to ensure the validity of these counterfactual trajectories, there is a risk of introducing spurious data that could negatively impact the training process.

### Questions
How to count the number of the encountered input (h_t, s_t+1, g_t+1)?

N_enc is usually 1?

The expected range in (8) is not clear, could any negative value of an action qualify as a counterfactual action, or are there specific restrictions? 

The process for selecting candidate counterfactual actions in Lines 271–287 is not fully explained. Could you provide a more detailed description of how these actions are chosen?

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
3

### Summary
This paper proposes the Counterfactual Reasoning Decision Transformer (CRDT), an extension of the Decision Transformer inspired by the potential outcomes framework from causal inference. CRDT includes a treatment model and an outcome model to enable counterfactual reasoning, allowing the agent to consider hypothetical actions and their potential outcomes. Experiments on locomotion, ant tasks demonstrate that CRDT outperforms DT and traditional methods.

### Strengths
1. The paper identifies the limitation of DT that DTs can underperform when optimal trajectories are scarce or data is biased toward suboptimal trajectories.
2. CRDT enables the agent to reason beyond known data by generating counterfactual experiences by integrating the causal inference framework, particularly the potential outcomes approach, with reinforcement learning. CRDT shows better performance on standard benchmarks as compare to traditional methods and DT.

### Weaknesses
1. The CRDT framework introduces several new hyperparameters (e.g., number of counterfactual actions, uncertainty threshold, and the number of experiences), which may require extensive tuning for different environments, potentially hindering practical applicability. The paper does not provide sufficient guidance on how to choose these hyperparameters, and it is unclear how sensitive the performance is to their values. For instance, the optimal number of counterfactual actions likely depends on the complexity of the action space, and the uncertainty threshold may need to be adjusted based on the noise level in the environment. Without a systematic approach to hyperparameter selection, it is difficult to assess the robustness of the method.
2. It is unclear to me how the treatment and outcome models are utilized during inference at test time, as the sections before the experiment sections focus primarily on how to train them. Providing detailed explanations of the inference process (e.g.  through an algo box) would help readers understand the agent's operation in practice. Specifically, it is not clear how the counterfactual samples generated by the treatment and outcome models are integrated into the decision-making process of the agent during evaluation. The paper should clarify whether these models are used online during inference or if the counterfactual samples are pre-computed and stored.
3. The paper states: "In our framework, the model o is trained with dropout regularization layers. This allows us to run multiple forward passes during the inferencing process to check the uncertainty of the output." Typically, dropout is disabled during inference. The logic behind using dropout during inference for uncertainty estimation needs clarification. It is not clear how the uncertainty estimates obtained through dropout are used to guide the agent's behavior. The paper should explain the specific mechanism by which the uncertainty is quantified and how it affects the selection of counterfactual actions.
4. Introducing additional models may increase computational costs during inference compared to the standard DT, and the paper lacks a comparison of computational efficiency (e.g., FLOPs, inference time) between CRDT and DT. The paper should provide a quantitative analysis of the computational overhead introduced by the treatment and outcome models, including the time required for generating counterfactual samples and the inference time of the overall system. This analysis is crucial for assessing the practical feasibility of the approach.
5. A demonstration or visualization of what kind of counterfactual actions or states are encountered will help reader understand better how these counterfactual reasoning leads to better performance. The paper should include visualizations that show the distribution of counterfactual actions and states, as well as how they differ from the original actions and states. This would provide insights into the types of scenarios where counterfactual reasoning is most beneficial.

### Questions
please see weakness.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a novel algorithm named Counterfactual Reasoning Decision Transformer to leverage the counterfactual experiences to improve the performance of the Decision Transformer (DT) in offline reinforcement learning. The DT lacks the stitching ability which leads them to learn the sub-optimal trajectories. The authors address this limitation by introducing the counterfactual reasoning module to generate and filter the counterfactual trajectories with high accumulated return and high prediction confidence. The empirical study shows that the proposed method outperforms the existing DT methods in the D4RL benchmark and Atari games.

### Strengths
- The CRDT framework aims to address the limitations of the stitching ability of DT by leveraging counterfactual reasoning to generate and filter the counterfactual trajectories without changing the DT's architecture.
- The methodology is inspired by two criteria: high accumulated return and high prediction confidence, which ensures the generated counterfactual trajectories are meaningful and beneficial for the DT's training.
- The empirical results show that the proposed method outperforms the existing DT methods in the D4RL benchmark and Atari games, demonstrating the effectiveness of the CRDT framework.

### Weaknesses
 - The paper provides a detailed explanation of the CRDT framework but lacks theoretical analysis of the counterfactual reasoning and its impact on the DT's performance. Specifically, there is no formal proof or guarantee that the generated counterfactual trajectories will lead to improved policy learning, or under what conditions the counterfactual reasoning will be most effective. The paper would benefit from a more rigorous analysis of the convergence properties of the proposed method.
- The implementation of the CRDT framework involves training two separate transformer models (Treatment and Outcome models), which increases computational consumption and training costs. The paper does not provide a detailed analysis of the computational overhead, such as training time, memory usage, and inference time, compared to the standard DT. This makes it difficult to assess the practical applicability of the method, especially in resource-constrained environments. Furthermore, the paper does not discuss the sensitivity of the method to hyperparameter choices related to the training of these two models.
- Although this method outperforms existing baseline methods in the average score in the D4RL benchmark and Atari games, the improvements are not significant across all tasks and environments. In some cases, the performance is comparable to the standard DT, and in others, there is a noticeable drop in performance, such as in the Pong game. The paper does not provide a clear explanation for these inconsistencies, and it is unclear why the counterfactual reasoning approach is not universally effective.

### Questions
- Can you provide more insights into the counterfactual reasoning module and how the CRDT framework ensures that the generated counterfactual trajectories are beneficial for the DT's training? What is the motivation behind using counterfactual reasoning to improve the DT's performance? 
- Since this method uses high accumulated return as the criterion, why are actions leading to the lowest counterfactual returns-to-go chosen? 
- Since this method generates counterfactual trajectories of length T/2 in algorithm 2, how does the CRDT framework ensure that these trajectories are meaningful and do not deviate too much from the real trajectories? 
- Can you explain why this method performs very well on the medium-expert dataset but has similar performance to the DT on the medium and medium-replay datasets in the D4RL benchmark? What is the reason for this? 
- Can you explain why this method may show a significant drop in performance in the Pong game compared to the DT method?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
In this paper, a novel framework called the Counterfactual Reasoning Decision Transformer (CRDT) is proposed. Inspired by counterfactual reasoning, CRDT elevates DT's capacity to extrapolate beyond familiar data by creating and leveraging counterfactual experiences. This enhancement enables superior decision-making in unfamiliar scenarios. Experiments conducted on Atari and D4RL benchmarks, encompassing scenarios with limited data and modified dynamics, illustrate that CRDT surpasses traditional DT methods. Furthermore, engaging in counterfactual reasoning empowers the DT agent with stitching abilities, enabling the fusion of suboptimal trajectories without structural alterations.

### Strengths
The problem raised in this paper is important and the experiments are solid.

### Weaknesses
1) The basic idea in this paper is to encourage the agent to explore the counterfactual actions according to the training data. The authors realized this by a pretrained dynamics model (outcome model). However, the predictions of the dynamics model over these counterfactual actions would introduce large biases because these actions would not have enough data to support. Then the proposed method seems to be unreasonable.

2) The relationship between the proposed method in this paper and those model-based offline RL algorithms. The core problem is to solve the problem of learning from sub-optimal data by the stitching abilities (e.g. the example in Fig. 1), but, as far as we have known, the model-based offline RL algorithms such as MOPO [1] and MOBILE [2] may also have the abilities of stitching. We wish the authors to discuss the performance of model-based offline RL algorithms in the example of Fig. 1.

3) Lack of the discussion about the advantages over the currently stitching-enabled methods, such as [3], [4] and [5]. Why would they fail the task as is listed in Fig. 1?

4) A shortcoming of the proposed Counterfactual Action Filtering. If the true dynamics model is stochastic, then even the actions are safe to be taken, the sum of the variance of the trajectory would also be high and the U in Eq.(10) would also be large. In such case, such actions would be filtered, but in fact they may be safe to be taken.

5) This paper aims to research the topic of offline rl from sub-optimal dataset, then the 'random' datasets of D4RL may be important. So the authors are encouraged  to give some experimental results on 'random' datasets in Table 1.

6) Concerning the counterfactual action selection, how the selected action is related to the performance improvement should be further formulated and explained.

### Questions
see above

### Soundness
3

### Presentation
3

### Contribution
2
