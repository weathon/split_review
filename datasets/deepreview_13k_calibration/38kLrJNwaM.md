# LEASE: Offline Preference-based Reinforcement Learning with High Sample Efficiency

- Decision: Reject
- Avg Score: 6.00
- Scores: 5, 5, 8

## Abstract
Offline preference-based reinforcement learning (PbRL) provides an effective way to overcome the challenges of designing reward and the high costs of online interaction. However, since labeling preference needs real-time human feedback, acquiring sufficient preference labels is challenging. To solve this, this paper proposes a offLine prEference-bAsed RL with high Sample Efficient (LEASE) algorithm, where a learned transition model is leveraged to generate unlabeled preference data. Considering the pretrained reward model may generate incorrect labels for unlabeled data, we design an uncertainty-aware mechanism to ensure the performance of reward model, where only high confidence and low variance data are selected. Moreover, we provide the generalization bound of reward model to analyze the factors influencing reward accuracy, and demonstrate that the policy learned by LEASE has theoretical improvement guarantee. The developed theory is based on state-action pair, which can be easily combined with other offline algorithms. The experimental results show that LEASE can achieve comparable performance to baseline under fewer preference data without online interaction.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper presents a novel algorithm for offline preference-based reinforcement learning (PbRL) aimed at addressing the challenges of designing rewards and the high costs of online interaction. The LEASE algorithm leverages a learned transition model to generate unlabeled preference data, which is then filtered through an uncertainty-aware mechanism to ensure the performance of the reward model. The paper claims to provide a generalization bound for the reward model and a theoretical improvement guarantee for the policy learned by LEASE. The experimental results are said to demonstrate that LEASE can achieve comparable performance to baseline methods with fewer preference data without online interaction.

### Strengths
- The proposed LEASE algorithm is novel, which introduces a new way to handle the challenge of limited preference data with a learned transition model. The selection mechanism for unlabeled data based on confidence and uncertainty is a thoughtful contribution to improving the stability and accuracy of the reward model.

-Theoretical Framework: The paper attempts to provide a theoretical foundation for the algorithm, which is a step towards more principled offline PbRL methods.

### Weaknesses
 - While the paper provides a theoretical analysis of the algorithm, it is not rigorous enough. For example, the approximation error of the reward function usually depends on a condition number that is exponential to $R_{\text{max}}$ when learned from preference data [1], but it seems missing from the derived bound. The approximation error of reward error does not directly translate into an additional error term in the performance bound and requires careful treatment (e.g., use a pessimistic reward function [2]). The authors use a handwaving argument (i.e., the law of large numbers) to derive (A.24) from (A.23), but it is not accurate. Using a concentration inequality is necessary in the finite sample case.

- The paper lacks some benchmarks and baselines to validate the effectiveness of the proposed method. For benchmarks, The D4RL benchmark is known to be insensitive to the accuracy of the reward function [3], and adding benchmarks like Meta-World would greatly strengthen the paper. Also, there are some recent works on offline PbRL that have a strong performance like [4,5], and LEASE should be compared with them.

### Questions
See the Weakness section.

### Soundness
2

### Presentation
2

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
The paper studies the problem of improving sample efficiency in offline preference-based reinforcement learning (PbRL). The proposed LEASE algorithm aims to address this issue by generating synthetic unlabeled segment pairs using an ensemble of learned transition models. These synthetic pairs are subsequently labeled with an ensemble of pre-trained reward models, followed by a filtering process that ensures the quality of the pseudo labels. The filtering mechanism employs a confidence principle, which requires that the models have high certainty in discriminating between segment preferences, and an uncertainty principle, which stipulates low variance in the predictions of the ensemble models. An offline RL algorithm can then be employed to learn on the augmented labeled dataset. The paper also supports its claims with theoretical analysis, providing an upper bound on the reward model's error learned on an augmented dataset and a bound on the policy improvement. The empirical results on the D4RL benchmark demonstrate that LEASE achieves comparable performance to baselines while using less preference data.

### Strengths
1. The paper is well-organized, with the methodology and theoretical contributions presented clearly, making the core ideas easy to understand.
2. Improving sample efficiency in offline PbRL is an important and challenging problem, with significant implications for many real-world applications.
3. The paper provides contributions both in empirical algorithm development and theoretical analysis. Although there are concerns regarding the assumptions, the theoretical contributions add valuable insight into understanding the role of reward models and policy performance in PbRL.
4.  In addition to benchmark scores, the paper includes experiments that evaluate performance with varying amounts of preference data, as well as an analysis of the relationship between the learned reward model and the ground truth. This helps in understanding the effects of the different components of LEASE.

### Weaknesses
1. The proposed LEASE algorithm closely follows the pipeline of Surf[1], with only two major differences: (1) Surf augments data using random temporal cropping, whereas LEASE generates synthetic data with a learned transition model; (2) Surf only uses confidence for label filtering, whereas LEASE employs both confidence and uncertainty principles. Despite these differences, a direct comparison with Surf is missing, which would help clarify the effects of the introduced transition model and the uncertainty principle on the final performance. Without this comparison, it is challenging to establish the uniqueness or superiority of LEASE.
2. The main results in Table 1 compare LEASE with URLHF, a previous baseline that uses more data than LEASE. However, it is crucial to also include a comparison with URLHF using the same amount of data as LEASE. This would allow readers to determine whether LEASE truly achieves superior performance with fewer data or if the perceived gains are simply due to the different quantities of data used. The current results are not sufficiently convincing without this comparison.
3. The theoretical analysis relies on assumptions that may be unrealistic in practical settings, and the connection between theory and the empirical algorithm is weak. Specifically:
   - Assumption 2: Given a fixed learned reward model, it is possible to construct an adversarial unlabeled dataset such that the pseudo-labeling error \(\eta\) becomes very large. More detailed analysis is needed to understand whether the specific data generation process of LEASE can mitigate such worst-case scenarios effectively.
   - Filtering Mechanism: While it is intuitive that filtering low-quality data improves labeling accuracy, there is no clear theoretical justification for why the proposed filtering mechanism (confidence + uncertainty) is superior to previous methods that only use confidence.



### Questions
In addition to Weaknesses 1-3, we have following questions.
1. Some details of the algorithm are missing. In Line 6 of Algorithm 1, which policy is used together with the transition model to generate the data? In Line 8, the “reward update condition” is not clear. Additionally, there lacks an explanation for the “the reward model only update once instead of updating constantly in this process” statement.
2. Can Theorem 1 show that using augmented data is better? When $N_u=0$, it is clear that the constant term increases, but the pseudo-labeling error becomes zero. Is it possible that the bound is even tighter with no augmentation?
3. How well is the learned transition model? A bad transition model can lead to poor augmentation quality.
4. In Figure 3, “the linear relationship between reward predicted by LEASE and ground truth is better” is not very clear. What is the possible reason that FRESH’s predictions are very narrow?
5. Some minor problems:
(1) In the “Model-based Reinforcement Learning” part in section 2, model-based RL is not always offline, and the presentation is a bit.
(2) A ‘tilde’ is missing for $N_u$ in Equation 9.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes a novel model-based offline RL algorithm that improves the efficiency of utilizing limited preference data. LEASE utilizes a learned transition model to rollout data, and label preferences with confidence and uncertainty measures. LEASE can achieve high performance with as few as 100 queries on mujoco tasks.

### Strengths
1. The problem of preference efficiency is vital and fundamental in offline meta-RL.
2. The proposed method is sound and sensible.
3. Experiment results are convincing.

### Weaknesses
1. Lack of analysis on the effect of transition model accuracy. The learned transition model can be inaccurate, and accumulate errors during rollout. Will this do a lot of damage to algorithm performance?
2. Lack of analysis of baseline algorithms' performance with different numbers of preference data. How much data is needed for baseline algorithms to achieve comparable performance to LEASE?
3. I would like to see results of more baseline algorithms, e.g., previous model-based offline RL algorithms.

### Questions
Please refer to the weakness part.

### Soundness
3

### Presentation
3

### Contribution
3
