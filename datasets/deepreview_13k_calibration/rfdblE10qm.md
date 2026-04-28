# Rethinking Reward Modeling in Preference-based Large Language Model Alignment

- Decision: Accept
- Avg Score: 8.00
- Scores: 8, 8, 8

## Abstract
The Bradley-Terry (BT) model is a common and successful practice in reward modeling for Large Language Model (LLM) alignment. However, it remains unclear *why* this model --- originally developed for multi-player stochastic game matching --- can be adopted to convert pairwise response comparisons to reward values and make predictions. Especially given the fact that only a limited number of prompt-response pairs are sparsely compared with others. 
In this paper, we first establish the convergence rate of BT reward models based on deep neural networks using embeddings, providing a theoretical foundation for their use.
Despite theoretically sound, we argue that the BT model is not a necessary choice from the perspective of downstream optimization, this is because a reward model only needs to preserve the correct ranking predictions through a monotonic transformation of the true reward. 
We highlight the critical concept of *order consistency* in reward modeling and demonstrate that the BT model possesses this property.
Moreover, we propose a simple and straightforward upper-bound algorithm, compatible with off-the-shelf binary classifiers, as an alternative order-consistent reward modeling objective. 
To offer practical insights, we empirically evaluate the performance of these different reward modeling approaches across more than 12,000 experimental setups, using $6$ base LLMs, $2$ datasets, and diverse annotation designs that vary in quantity, quality, and pairing choices in preference annotations.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper investigates the theoretical validity of employing the BT model in the reward modeling process. It also explores alternative reward modeling approaches and compares them with the BT model. Additionally, this work tests the feasibility and effectiveness of using a cross-prompt comparison method for reward modeling, thereby moving beyond the current reward data paradigm of utilizing the same prompt with different responses.

### Strengths
As BT model has been widely used as a  default paradigm in reward modeling, there are few work disscuss the validity for this pattern. This work gives a detailed theoretical analysis of using BT model in reward modeling and offers other alternative methods for reward modeling and  conducts rich ablation studies on them. The theoretical analysis reveals some very basic logics of reward modeling and BT model, which offers a deep explanation of how reward modeling and BT model works.

### Weaknesses
1. As illustrated in paper, the label of classifation is simply to  assign (1, 0) to the prefered answer. It is seemingly to be a very rough way for building classifation labels since there are pairs may both be, we say like, 'helpful'. One is labeled as 'chosen' in raw dataset just becase it is more helpful than the rejected one. But it does not mean the rejected one should be  classified in to 'not helpful'.  For example, chosen answer may get a 10/10 score in helpful, and rejected answer may get 9/10.  Can you disscuss this limitation and its potential impact on their results? And have you ever considered alternative labeling schemes that might better capture nuanced differences between responses?
2. The  experiment model size only ranges from 2B to 8B. It remains unknown weather CLF method still more effective when applied to larger models. Do you have any hypotheses about how these results would be if scale to larger models? Can you discuss this limitation and propose how future work could address it?

### Questions
1. In the ablation study of Annotation Error Rate, CLF method almost not decrease as Annotation Error Rate arises. This is not common for a  classification model. Can you give more  explanation of this unexpected robustness to annotation errors? And could you also discuss potential implications of this finding for practical applications?
2. Have you considered comparing your methods on existing benchmarks? And how the results in paper might compare to or complement existing benchmark results?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper investigates the theoretical and practical foundations of the BT model in LLM alignment, examining its common use in transforming pairwise comparisons into reward scores despite sparse data. The authors establish a convergence rate for BT reward models based on neural network embeddings, ensuring its theoretical validity, but argue that BT is not essential for downstream optimization, as any monotonic transformation of true reward suffices. They propose an order-consistent alternative using a binary classifier framework that simplifies reward modeling. Furthermore, the authors propose to utilize cross-prompt comparisons for improving the reward modeling performance.

### Strengths
1. Provides a thorough analysis of the BT model's application in LLM alignment, identifying unique challenges and offering theoretical justification, including the introduction of asymptotic theory for BT regression in preference-based reward modeling.  
2. Proposes `order consistency` as a core principle in reward modeling, leading to an alternative to the BT model. Additionally, the use of cross-prompt comparisons enhances training by expanding available comparisons, which further contributing to performance improvements.  
3. The paper is presented in a clear and coherent manner. The authors introduce the purpose behind each step before detailing the results, providing a helpful summary of expected outcomes. Despite the dense content, the writing remains accessible and easy to follow.
4. The experiment is thoughtfully designed to validate the proposed methods and offer valuable insights to readers.

### Weaknesses
I have no major concerns. I have only one minor suggestion: Figures 2 and 3 should include dataset names in each row for added clarity.

### Questions
- **Q1:** The results showing that $\\mathcal{L}_{\\textrm{clf}}$ outperforms the BT model in Figure 1 are somewhat counterintuitive to me, as the classification objective learns marginal probability while the BT model learns joint probability (line 305). The classification objective seems to use less information than the BT model, as the correspondence between $i$ and $j$ is missing. Could you elaborate on why the classification objective not only works but also performs better than the BT model?

- **Q2:** The idea of utilizing cross-prompt comparisons is interesting and shows significant improvements in experiments. Could you discuss any restrictions on using cross-prompt comparisons and describe scenarios where cross-prompt comparisons are particularly effective?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper addresses the prevalent use of the Bradley-Terry (BT) model for reward modeling in LLM alignment. It introduces an asymptotic theory for BT regression in LLM reward modeling, setting the first risk bound for BT model in LLM alignment, and propose order consistency as the central goal of reward modeling, which can inform both the BT model and an alternative classification-based approach. This approach is shown to be more flexible and efficient than the BT model, especially when dealing with varying levels of annotation quality and quantity. The paper supports its claims with extensive testing across different LLMs and annotation strategies. 

The proposed theoretical framework includes: 
- Argues that a reward model does not need to provide exact probabilities of preference; instead, it must maintain the correct order of preferences between prompt-response pairs.
- Establishes a bound on the prediction error of a reward model based on MLPs. This bound ensures that, under specific conditions, the model will predict preference probabilities with a controlled error margin.
- Shows that the predicted rewards will be close to the true rewards as long as the preference probabilities are well approximated.
- Provides a theoretical guarantee that the model will remain order-consistent even when dealing with noisy annotations.

### Strengths
- The paper provides a theoretical framework to justify the use of order consistency. 
- The authors conduct extensive experiments with diverse setups, support their claims about the classification-based model’s advantages over BT.
- The paper is well written.

### Weaknesses
 - The paper evaluates reward model performance primarily through BoN sampling improvements. While BoN results provide insights into relative ranking, they do not directly reflect the reward model’s prediction accuracy or error, which is central to the theoretical claims in Theorem 2.2. Including accuracy or error metrics in the evaluation could provide a more comprehensive validation of the theoretical bounds on prediction error, demonstrating that the model’s predictions align with the theoretical guarantees.
- In RL training (e.g., using PPO), the RM’s calibration is crucial: a well-calibrated RM should assign progressively higher rewards to better trajectories. Theorem 2.2 focuses on minimizing prediction error, which may not ensure adequate calibration for RL. To fully evaluate the proposed approach, an analysis of the reward model’s calibration or additional experiments using PPO (or other algorithms) would help determine if the model can effectively support RL tasks where calibration quality directly impacts learning stability and performance.

### Questions
- In RLHF, preferences may be non-transitive—such that if A > B and B > C, it doesn’t always imply A > C. Could this be consider as annotation errors? Or should this also be invested (as it might also reflect genuine complexities in human judgments, influenced by context or subjective factors)?

### Soundness
3

### Presentation
3

### Contribution
3
