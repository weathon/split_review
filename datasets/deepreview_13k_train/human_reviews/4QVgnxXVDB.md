# 3CIL: Causality-Inspired Contrastive Conditional Imitation Learning for Autonomous Driving

- Decision: Reject
- Scores: 3, 6, 6, 5

## Abstract
Imitation learning (IL) aims to recover an expert's strategy by performing supervised learning on the demonstration datasets. Incorporating IL in safety-crucial tasks like autonomous driving is promising as it requires less interaction with the actual environment than reinforcement learning approaches. However,  the robustness of IL methods is often questioned, as phenomena like causal confusion occur frequently and hinder it from practical use. In this paper, we conduct causal reasoning to investigate the crucial requirements for the ideal imitation generalization performance. With insights derived from modeled causalities, we propose causality-inspired contrastive conditional imitation learning (3CIL), a conditional imitation learning method equipped with contrastive learning and action residual prediction tasks, regularizing the imitator in causal and anti-causal directions. To mitigate the divergence with experts in unfamiliar scenarios, 3CIL introduces a sample-weighting term that transforms the prediction error into an emphasis on critical samples. Extensive experiments in the CARLA simulator show the proposed method significantly improves the driving capabilities of models.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors present a new imitation learning algorithm that aims to solve some causal confusion problems in previous imitation learning methods on self-driving tasks. Specifically, the authors propose to 1) learn a more representative state representation; 2) reduce the chance of learning spurious-correlation by inferring delta actions from latent states, and 3) weight training samples by the discrepancy between prediction and ground truth.

### Strengths
* The authors do a good job summarizing previous findings about causal confusion problems in self-driving tasks
* Proposed lots of interesting strategies to potentially solve or alleviate the causal confusion problems

### Weaknesses
 * Authors made lots of assumptions:
   * It's not sufficient to directly map ot to at
     * This remains an untested hypothesis 
   *  learning a decoder for \hat{s}t helps it match with expert st
      * on the contrary, learning a decoder for \hat{s}t could force the encoder to focus on every detail in the image, even the ones that do not directly contribute to ground st.
   *  Since delta(at) is inferred from (st), it doesn't learn the spurious correlation
      * This assumption can be wrong since st would contain information from a(t-1)
   * The proposed method is better than baselines in most scenarios, but is that because of the design choices or just better models or bigger capacities?
* Figure 2 could have more annotations
  *  It would be better if the authors could annotate the different colors and shapes of each node

### Questions
My main concern is that there are lots of assumptions made in this paper that are unsupported by evidence or experiments, I would change my opinion if the authors present more ablation experiments that carefully study each of their design decisions. I would also love to see more qualitative examples (instead of just descriptions). Lastly,  the authors should give more details when comparing the baselines. Are the performance gain simply caused by a better network architecture or a bigger network capacity?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes to solve causal confusion problem in imitation learning using supervised contrastive learning, residual prediction and sample weighting. It draws insights from causality that motivates to learn a representation of history observations without spurious correlations.
Experiments on CARLA shows solid improvements over baselines, such as CIL and Premier-TACO.

### Strengths
- Formulate the imitation learning problem from a causal perspective and tries to prevent confounding factors using representation learning.
- Proposes to use supervised contrastive learning to learn an image representation that aligns with expert actions.
- The improvements in the tested scenarios is promising.

### Weaknesses
 - Lack of comparisons with some related work, such as Wen et.al. Key-frame focused visual imitation learning, which proposes a weighting strategy based on action predictability.
- It would be nice to have more quantitative and qualitative analysis of the improvement. Can we attribute those to improvement in reducing spurious correlations?
- Lack of evaluation on CARLA benchmark instead of self-constructed scenarios.

### Questions
The improvements in those scenarios look promising. But, how to demonstrate it's coming from reducing the confounding factors as shown in previous sections?

### Soundness
3

### Presentation
3

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
To deal with the causal confusion problem in imitation learning, authors take the inspiration from causal learning and propose the 3CIL framework which integrates contrastive learning, action residual prediction, and importance weighting techniques together. Testing on autonomous driving benchmark CARLA, 3CIL achieves good performance with higher success rate and lower collision times than the baselines.

### Strengths
The proposed framework is well-motivated.

The experimental result looks good.

### Weaknesses
1.	For importance weighting, would you please intuitively or theoretically explain the motivation for using the errors of action residual prediction as weights, instead of other choices, e.g., AdaBoost or Keyframe? Or would you please compare with them?

2.	Why is it necessary to divide the imitating process into two separate stages? I suggest comparing with training the representation modules and the policy end-to-end.

3.	In Table 1, why is the performance of 3CIL in scenario 3 worst across all scenarios? Even worse than the unseen ones, i.e., 5 and 6.

4.	More ablation studies, analysis experiments, and visualizations are necessary. The current experimental results only contain the comparison with baselines and two simple ablation studies. I suggest having more experiments and visualizations to verify your arguments that 3CIL successfully removes the spurious correlation and importance weighting correctly finds the rare scenarios.

5.	Missing some important references [2,3,4].

### Questions
Please refer to the Weaknesses part.

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The authors propose to combine causal reasoning techniques to assist imitation for autonomous driving. Specifically, the paper presents a novel approach, causality-inspired contrastive conditional imitation learning (3CIL), which integrates contrastive learning and action residual prediction. The framework is based on POMDP, trying to mimic the scenarios when the expert and imitator share different views.

### Strengths
The idea of combining causality, contrastive learning and conditional imitation learning is quite interesting. The performance seems to be good for all scenarios. Fig. 1 is intuitive.

### Weaknesses
My major concerns lie in theoretical clarity, experimental design, and practical applicability. In the absence of strong theoretical guarantees, the paper would benefit greatly from robust experimental results. Additionally, it’s crucial to provide a clear rationale for the integration of causality, contrastive learning, and conditional imitation learning, explaining why this combination is necessary. I have outlined specific questions below.

### **Some high-level questions**
1. In "3CIL: Causality-Inspired Contrastive Conditional Imitation Learning," the abbreviation "CIL" is first defined in line 162. However, it’s unclear what the "C" stands for. Is it "Causality" or "Conditional"? Could you clarify this term for consistency?

2. Does the input for the VAE include all the past history observations $o_{1:t}$?

3. Some important details are in the appendix. The authors should consider move them to the major context, e.g., Fig. 4 and Fig. 5.

### **Some questions about theoretical guarantee**
1. As discussed in (Ruan et al., 2022; Ruan & Di, 2022; Kumor et al., 2021), unobserved confounders (UCs) often complicate causal identifiability, and certain variables must be considered to mitigate the influence of spurious correlations or shortcuts during the learning process. In your approach, which specific variables are crucial to achieving this objective? E.g., which variables are required to block all the backdoor paths.

2. Following up on the previous question, if all the past ground-truth states $s_{1:t}$ are unobserved (common in POMDPs), and $a_{t-1} \leftarrow s_{t-1} \rightarrow s_{t} \rightarrow a_{t}$ is active, in other words, there is an active backdoor path between $a_{t-1}$ and $a_{t}$ which can never be blocked. Given that this path cannot be blocked, is the policy learning process identifiable or robust? How do you ensure convergence in policy learning under these circumstances? 

3. The idea of training a representation model $G$ is not that novel. Especially, when $\hat{s}_{t}$ is unobserved, it is very hard to directly determine whether the representation model is good or not. While simulations may provide insights, evaluating the model’s practical effectiveness in real-world conditions can be significantly harder. What methods do you suggest to compare model performance outside of a simulation environment?

4. The proposed method appears to be a pipeline structure (i.e., representation model + policy model).
    
     4.1 IIf overall performance is not expected, what strategy would you recommend to isolate and improve the specific component responsible? How can one effectively determine whether limitations stem from the representation model or from the policy?
    
     4.2 Will there be any cascaded errors from upstream to downstream tasks? Could you elaborate on any mechanisms in place to mitigate such cascading errors?

### **Some questions about experiments**

1. In your experiments, does the imitator have access to the reward $R$? Additionally, are the expert demonstrations generated from RL algorithms that use the same reward function $R$?

2. For the observations, the expert is able to observe $s_{t}$, but the imitator is only able to observe $o_{t}$. Is that correct?

3. To what extent does the reward $R$ reflect real-world driving behaviors? How accurately does it capture the dynamics observed in actual driving scenarios?

4. Could the authors add more details to the reward $R$? Specifically, how are the four components $r$ defined? If the primary objective is to evaluate route adherence, is $r_{position}$ alone sufficient, or are the other rewards essential? Please clarify the role of each reward component.

5. Additional metrics could enhance the evaluation process, such as the RMSE between predicted positions and target routes. Would the authors consider including these metrics for a more comprehensive analysis?

### Questions
### **Some high-level questions**
1. In "3CIL: Causality-Inspired Contrastive Conditional Imitation Learning," the abbreviation "CIL" is first defined in line 162. However, it’s unclear what the "C" stands for. Is it "Causality" or "Conditional"? Could you clarify this term for consistency?

2. Does the input for the VAE include all the past history observations $o_{1:t}$?

3. Some important details are in the appendix. The authors should consider move them to the major context, e.g., Fig. 4 and Fig. 5. 

### **Some questions about theoretical guarantee**
1. As discussed in (Ruan et al., 2022; Ruan & Di, 2022; Kumor et al., 2021), unobserved confounders (UCs) often complicate causal identifiability, and certain variables must be considered to mitigate the influence of spurious correlations or shortcuts during the learning process. In your approach, which specific variables are crucial to achieving this objective? E.g., which variables are required to block all the backdoor paths.

2. Following up on the previous question, if all the past ground-truth states $s_{1:t}$ are unobserved (common in POMDPs), and $a_{t-1} \leftarrow s_{t-1} \rightarrow s_{t} \rightarrow a_{t}$ is active, in other words, there is an active backdoor path between $a_{t-1}$ and $a_{t}$ which can never be blocked. Given that this path cannot be blocked, is the policy learning process identifiable or robust? How do you ensure convergence in policy learning under these circumstances? 

3. The idea of training a representation model $G$ is not that novel. Especially, when $\hat{s}_{t}$ is unobserved, it is very hard to directly determine whether the representation model is good or not. While simulations may provide insights, evaluating the model’s practical effectiveness in real-world conditions can be significantly harder. What methods do you suggest to compare model performance outside of a simulation environment?

4. The proposed method appears to be a pipeline structure (i.e., representation model + policy model).
    
     4.1 IIf overall performance is not expected, what strategy would you recommend to isolate and improve the specific component responsible? How can one effectively determine whether limitations stem from the representation model or from the policy?
    
     4.2 Will there be any cascaded errors from upstream to downstream tasks? Could you elaborate on any mechanisms in place to mitigate such cascading errors?

### **Some questions about experiments**

1. In your experiments, does the imitator have access to the reward $R$? Additionally, are the expert demonstrations generated from RL algorithms that use the same reward function $R$? 

2. For the observations, the expert is able to observe $s_{t}$, but the imitator is only able to observe $o_{t}$. Is that correct?

3. To what extent does the reward $R$ reflect real-world driving behaviors? How accurately does it capture the dynamics observed in actual driving scenarios?

4. Could the authors add more details to the reward $R$? Specifically, how are the four components $r$ defined? If the primary objective is to evaluate route adherence, is $r_{position}$ alone sufficient, or are the other rewards essential? Please clarify the role of each reward component.

5. Additional metrics could enhance the evaluation process, such as the RMSE between predicted positions and target routes. Would the authors consider including these metrics for a more comprehensive analysis?

**Should the authors address these questions thoroughly, I would consider raising my evaluation score.**

---------

References:
- Pearl, Judea. Causality. Cambridge university press, 2009.
- Peters, Jonas, Dominik Janzing, and Bernhard Schölkopf. Elements of causal inference: foundations and learning algorithms. The MIT Press, 2017.
- Ruan, Kangrui, and Xuan Di. "Learning human driving behaviors with sequential causal imitation learning." Proceedings of the AAAI Conference on Artificial Intelligence. Vol. 36. No. 4. 2022.
- Ruan, Kangrui, et al. "Causal imitation learning via inverse reinforcement learning." The Eleventh International Conference on Learning Representations. 2023.
- Kumor, Daniel, Junzhe Zhang, and Elias Bareinboim. "Sequential causal imitation learning with unobserved confounders." Advances in Neural Information Processing Systems 34 (2021): 14669-14680.

### Soundness
2

### Presentation
2

### Contribution
3
