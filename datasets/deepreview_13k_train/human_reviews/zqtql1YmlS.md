# Fewer May Be Better: Enhancing Offline Reinforcement Learning with Reduced Dataset

- Decision: Accept
- Scores: 5, 5, 8, 6

## Abstract
Research in offline reinforcement learning (RL) marks a paradigm shift in RL. However, a critical yet under-investigated aspect of offline RL is determining the subset of the offline dataset, which is used to improve algorithm performance while accelerating algorithm training. Moreover, the size of reduced datasets can uncover the requisite offline data volume essential for addressing analogous challenges. Based on the above considerations, we propose identifying Reduced Datasets for Offline RL (ReDOR) by formulating it as a gradient approximation optimization problem.  We prove that the common actor-critic framework in reinforcement learning can be transformed into a submodular objective. This insight enables us to construct a subset by adopting the orthogonal matching pursuit (OMP). Specifically, we have made several critical modifications to OMP to enable successful adaptation with Offline RL algorithms. The experimental results indicate that the data subsets constructed by the ReDOR can significantly improve algorithm performance with low computational complexity.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
Motivated by the large size of the offline dataset as well as suboptimal data quality in offline RL, this paper considers the problem of finding a coreset out of the given dataset. The authors first formulate such problem as a task to approximate the actual gradients (from the complete dataset) in the offline training process. And a line of of results are provided to support the low approximation errors. Then the method named Reduced Datasets for Offline RL (REDOR) is proposed, inspired by the orthogonal matching pursuit (OMP). Finally, the method is compared with several baseline methods on D4RL data.

### Strengths
> **Originality**
- Such new method is proposed to select a coreset from the raw offline dataset, which could contribute as an alternative approach in offline RL.

> **Clarity**
- Several informative figures are provided. Especially the one by t-SNE provides a straightforward way to understand the behaviour of such selection process.

> **Significance**
- In some of the settings concerned in the experiments, such method is quite efficient.

### Weaknesses
 > **Quality**
- Several assumptions in Theorem 4.1 are rather stronger than scenarios in actual implementations. One observation often seen in offline RL is the diverging gradients (if without proper training techniques), which, however, are assumed to be uniformly bounded in the paper, w.r.t parameters in respectively policies and Q-functions. This assumption is particularly concerning as it is not clear how the proposed method ensures such boundedness, and the theoretical results may not hold if this assumption is violated. Furthermore, the paper does not provide any empirical verification of this assumption, which limits the practical applicability of the theoretical analysis.
- Despite the multi-round selection strategy introduced in Section 4.2, as long as the empirical returns are used, as depicted in equation (13), the targets in training steps are relatively fixed (in the sense of distributions due to behaviour policies), which then makes (13) no longer an approximation of Bellman backup errors. As a result, it is currently not clear if such approach would lead to a guaranteed good estimation of values/Q-functions. The use of empirical returns, while potentially stabilizing training, deviates from standard Bellman updates and introduces a bias that is not well-characterized. This raises concerns about the convergence properties and the quality of the learned policies.
- According to what the reviewer can understand about the statements and proof for results in Section 5, the theorems only consider the proposed method defined with classic TD loss, while do not consider the techniques emphasized in Section 4.2 - 4.3. As a result, such theoretical discussion is not an actual analysis of the proposed algorithm (feel free to correct me). The theoretical analysis focuses on a simplified version of the algorithm, neglecting the impact of the empirical return targets and the multi-round selection process. This discrepancy between theory and practice makes it difficult to assess the theoretical guarantees of the proposed method.
- In Line 766, within the proof for Theorem 5.2, it is not justified why $S\^k$ can always start from the cluster center ${c\_k}$ of gradients. This assumption lacks justification and could significantly impact the performance of the algorithm if the initial point is not representative of the cluster.

> **Clarity**
- According to the way a Q-function is defined in Line 99, some index of $t$ should be included in the notation of $Q$. The notation for the Q-function is ambiguous and should explicitly include the time step to avoid confusion.
- Horizon $H$ is not explicitly defined. The absence of a clear definition for the horizon $H$ makes it difficult to understand the scope and limitations of the proposed method.
- There is not enough information for $L_{\text{max}}$. The lack of information about $L_{\text{max}}$ makes it difficult to reproduce the results and understand the practical implications of the proposed method.
- There lacks for an introduction to how KRLS, Log-Det and BlockGreedy are implemented in such offline RL settings. The paper should provide more details on how these baseline methods are adapted to the offline RL setting, including any specific implementation choices or parameter settings.

> **Significance**
- As explained in the 'Quality' part, the theoretical results seem not to be exactly for the proposed method.

### Questions
None

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
4

### Summary
This paper introduces a method for dataset selection in offline reinforcement learning (RL) using the Orthogonal Matching Pursuit (OMP) algorithm and Monte Carlo Q losses. The proposed approach selects full trajectories whose loss gradients align well with the residuals.

### Strengths
1. The method demonstrates improved performance compared to the baselines.
2. The paper includes a theoretical analysis that provides a solid grounding for the approach.

### Weaknesses
1. Some key elements of the proposed algorithm are either missing or unclear, and there are some discrepancies between the paper and the accompanying codebase. For instance, the method used to generate "hard" datasets is not fully discussed in the paper, and the percentile $m$ mentioned in the paper differs from that in the codebase. More details are provided in the questions below.

2. Certain parts of the proposed algorithm may contain logical errors or inconsistencies. For example, in Line 4 of Algorithm 2, $r$ is a scalar, yet an inner product operation is applied to it. More details are provided in the questions below.

3. The baselines chosen for comparison seem somewhat outdated, which could affect the perceived significance of the performance improvements demonstrated by the proposed method.

### Questions
1. Could you please clarify how the suboptimal datasets for MuJoCo, namely "hard", were generated? The paper mentioned that they were generated by adding low-quality data, but the quality or source of such data and mix ratio should also be introduced.

2. Regarding $Q_\theta$ in Algorithm 1, could you explain how $Q_{\theta_t}$ was formulated? There is no update term in either the pseudocode or the codebase. Was $Q_\theta$ pretrained or trained simultaneously but omitted? It would be best if the pseudocode or thorough explanations were provided.

3. In Equation 14, it is stated that trajectories in the top $m%$ based on return are filtered, with $m$ set to 50, which would seem to exclude almost the entire random dataset. Could you provide the result of simply selecting trajectories with top $m (=50)\%$ returns for comparison?

4. In the codebase, it seems that in addition to the evaluation of Monte Carlo Q targets, the selection of candidate trajectories via OMP is filtered based on trajectory returns. What is the exact search space of the selected trajectories? If it is the filtered one with trajectory returns, then how can we ensure the fairness of the comparison to baselines that do not utilize such a filter?

5. In the paper, the percentile $m$ is specified as 50 (Top), but in the codebase, it varies (Bottom 50, 70, and 95). Could you clarify the reason for this difference?

6. In Algorithm 2, $r$ is defined as a scalar, but in Line 4, an inner product is applied. Could you kindly explain this?

7. In Line 3 of Algorithm 2, the inequality appears to be reversed. Is this correct?

8. Is there a reason why TD3+BC was chosen as the backbone offline RL algorithm for the MuJoCo tasks? Would using IQL, as in the Antmaze tasks, provide a more consistent comparison?

9. For the MuJoCo tasks, the authors used the "-v0" versions, which are now outdated and differ from the more recent "-v2" versions. Could you explain the reasoning behind using "-v0"?

10. For the "Complete Dataset" scores in the Antmaze tasks, it seems that these values are taken from the IQL paper, which does not provide standard deviations. Could you clarify how these scores were derived?

11. While the baselines used in the experiments appear somewhat dated, dataset selection has recently gained increased attention in offline RL. Hence, it seems that recent algorithms should be contained as baselines. For example, "Improving Generalization in Offline Reinforcement Learning via Adversarial Data Splitting (Wang et al., 2024)" provides a codebase, which could allow for a straightforward comparison. Or, is there any reason why such comparisons are inappropriate?

12. Could you provide more details on what is meant by the "Complete Dataset" baseline? Specifically, is it the original mixture of the desired dataset and the suboptimal dataset, or is it just the original dataset?

### Soundness
2

### Presentation
2

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
The paper explores the interesting concept of finding a subset of the offline dataset to improve the performance of offline RL algorithms using orthogonal matching pursuit. The authors provide empirical and theoretical evidence of performance improvement on benchmark datasets.

### Strengths
1. The paper is well written and the idea is easy to follow.
2. The idea of subset selection is novel and interesting.
3. The paper provides both strong theoretical study and empirical analysis of the proposed method.

### Weaknesses
1. The authors characterize the field of offline RL only in terms of OOD action penalization and constraints on the behavior policy. There should also be a short discussion on model-based methods like MOPO [1] and MoERL [2], as some of these approaches have been shown to outperform model-free methods.

2. Some parts of the paper are difficult to understand without prior knowledge of orthogonal matching pursuit. Specifically, how is $F\lambda(s) = L_{max} - min_w Err_{\lambda} (w, S, L, \theta)$ used in the OMP.

3. If I understand correctly this method may not lead to the claimed reduction in complexity, as training $Q_{\theta}$ and $\pi_{\phi}$ till requires the full dataset.

Minor 

The table references do not match the table numbers. On line 420, I believe the authors are referring to Table 1 instead of 6.2.

Suggestion : If the authors could include a notations table in Appendix it will help in readability and understanding the proofs.

### Questions
Q1. How is the weight $w_i$ or $\lambda$ decided during training and the parameters $L_{max}$, $m$,$\epsilon$ chosen in practice?

Q2. Are the networks Qθ, πϕ networks first trained on the full dataset before starting with the subset selection?

Q3. What is the empirical reduction percentage achieved in each dataset?

Q4. In Figure 1 for the walker2d-expert-v0 environment, the reward first increases and then drops. It is also counterintuitive that the subset selected in ReDOR would perform better than a dataset containing only expert trajectories. Could the authors provide an explanation for this behavior?

Q5. Q5. Could the authors elaborate more on the Prioritize baseline, what do samples with highest TD Loss mean?

Q6. How does ReDOR perform on random datasets such as halfcheetah-random-v2?

Q7. I could not understand Fig 3. Why are the reduced dataset points more for category 6 when it is a subset of complete dataset?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors introduce an approach for reducing the size of a dataset for offline RL by defining this reduction as a submodular set cover problem and using orthogonal matching pursuit. The resulting algorithm is evaluated on a modified version of D4RL locomotion tasks and the original antmaze tasks.

### Strengths
- This is an interesting and novel approach for data selection in RL. The high-level approach/formulation of the problem may be useful as a foundation for extensions. 
- Strong results on a modified version of D4RL, and the unmodified antmaze.

### Weaknesses
There is a discrepancy between the proposed objectives and the resulting objectives that makes me question where the effectiveness of the proposed approach comes from.

The problem is initially defined as finding a subset of the data which results in a higher performing policy than the policy determined by training on the original dataset (Eqn 3). However, this is immediately discarded for another optimization problem, which instead tries to limit change in the value function (Eqn 5). While discovering a smaller dataset which achieves the same performance as the original dataset is an interesting problem, the authors claim in several places (and demonstrate) that their reduced dataset actually improves the performance. So where does the performance gain come from? It's unclear how minimizing the change in the value function directly leads to improved policy performance, especially given the initial objective of maximizing policy performance. The paper lacks a clear theoretical justification for why minimizing value function change should lead to a better policy than training on the full dataset. This disconnect between the stated goal and the actual optimization target is a significant concern.

One possible cause for the performance increase is how the evaluation is done (add noisy/low performing trajectories to the D4RL dataset) and the filtering of low performing trajectories (Eqn 14). I would be very curious if this filtering alone is sufficient to also recover the performance of the algorithm. This concern, along with some missing key experimental details, makes me cautious about the experimental claims made in the paper. Specifically, the paper does not provide details on the characteristics of the added noise, such as the policy used to generate it, or the magnitude of the noise. This lack of detail makes it difficult to assess the validity of the experimental setup. Furthermore, the paper does not specify how many data points are removed by ReDOR, making it difficult to understand the extent of the data reduction and its impact on performance. 

Missing References which also filter the dataset using returns:
- [1] Chen, Xinyue, et al. "Bail: Best-action imitation learning for batch deep reinforcement learning." Advances in Neural Information Processing Systems 33 (2020): 18353-18363.
- [2] Yue, Yang, et al. "Boosting offline reinforcement learning via data rebalancing." arXiv preprint arXiv:2210.09241 (2022).

### Questions
Additional experiments:
- Does simply filtering the dataset by high returns recover the same performance?
- What is the performance of ReDOR on the original version of D4RL? One might expect that reducing mixed quality datasets like medium-expert, or medium, could also result in a high performance. 

Missing experimental details:
- How is the hard dataset generated? How many datapoints are added to the dataset?
- How many datapoints are removed by ReDOR? What is the size of the reduced datasets?

General:
- Is there a way to tune the resulting dataset size? 
- Is Fig 3, episode return = 99.5 for behaviors [2-7] correct or a bug?

### Soundness
2

### Presentation
3

### Contribution
3
