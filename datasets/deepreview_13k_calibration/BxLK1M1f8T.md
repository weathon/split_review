# Double Check My Desired Return: Transformer with Value Validation for Offline RL

- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 5, 3, 6

## Abstract
Recently, there has been increasing interest in applying Transformers to offline reinforcement learning (RL). Existing methods typically frame offline RL as a sequence modeling problem and learn actions via Supervised learning (RvS). However, RvS-trained Transformers struggle to align actual returns with desired target returns, especially when dealing with underrepresented returns in the dataset (interpolation) or missed higher returns that could be achieved by stitching sub-optimal trajectories (extrapolation). In this work, we propose a novel method that Double Checks the Transformer with value validation for Offline RL (Doctor). Doctor integrates the strengths of supervised learning (SL) and temporal difference (TD) learning by jointly optimizing the action prediction and value function. SL stabilizes the prediction of actions conditioned on target returns, while TD learning adds stitching capability to the Transformer. During inference, we introduce a double-check mechanism. We sample actions around desired target returns and validate them with value functions. This mechanism ensures better alignment between the predicted action and the desired target return and is beneficial for further online exploration and fine-tuning. We evaluate Doctor on the D4RL benchmark in both offline and offline-to-online settings, demonstrating that Doctor does much better in return alignment, either within the dataset or beyond the dataset. Furthermore, Doctor performs on par with or outperforms existing RvS-based and TD-based offline RL methods on the final performance.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces a novel method called "Doctor" that integrates supervised learning (SL) and temporal difference (TD) learning to improve the alignment of predicted actions with desired target returns in offline reinforcement learning (RL). The method uses a bidirectional transformer and a double-check mechanism during inference to validate actions with value functions, ensuring better alignment and improved performance. The work is evaluated on the D4RL benchmark, demonstrating competitive performance compared to existing RvS-based and TD-based methods.

### Strengths
1. The core idea of the paper is interesting and well-motivated, addressing the challenge of aligning predicted actions with desired returns in offline RL.
2. The paper is well-written and easy to follow, making it accessible to readers with a background in RL and transformers.
3. The experimental results on the D4RL benchmark show that the proposed method, Doctor, outperforms several baselines in some tasks, indicating its potential effectiveness.

### Weaknesses
1. Model Choice (Bidirectional vs. Causal Transformer): The use of a bidirectional transformer, rather than a causal transformer, is not fully justified. Since inference is typically performed in a causal manner, it would be beneficial to provide more insight into why a bidirectional transformer was chosen and how it impacts the model's performance during inference. The paper should elaborate on the potential discrepancies between training with bidirectional context and the causal nature of online execution, and whether this could lead to suboptimal performance or instability during deployment.

2. Limitations Discussion: The paper lacks a detailed discussion of the limitations of the proposed work. It would be valuable to acknowledge potential drawbacks or scenarios where the method might not perform as well, setting realistic expectations for future research. For example, the paper should discuss the sensitivity of the method to hyperparameter choices, the potential for overfitting to the training data, and the computational resources required for training and inference.

3. Inference Complexity: The inference complexity of the proposed method may be significantly higher than that of DT. A detailed comparison of the inference speed and computational overhead relative to other models would strengthen the paper. The analysis should include a breakdown of the computational cost associated with each step of the inference process, such as the transformer forward pass, the value function evaluation, and the double-check mechanism, to provide a clearer understanding of the method's efficiency.

4. Performance and Overhead: While the performance is competitive, the gains are marginal compared to the baselines. Given the higher computational cost, a more in-depth analysis of the trade-offs between performance and computational resources is necessary. The paper should quantify the computational overhead of the proposed method in terms of training time, memory usage, and inference latency, and compare these metrics with the baselines to justify the added complexity.

5. Evaluation Scope: The evaluation is conducted only on the D4RL benchmark, which may introduce a bias in the results. To ensure the robustness and generalizability of the proposed method, it would be valuable to conduct additional experiments on other offline RL benchmarks. The paper should consider evaluating the method on a diverse set of tasks with varying characteristics, such as different state and action spaces, reward structures, and data distributions, to assess its performance in different scenarios.

6. Reward Modeling Assumption: if I understand correctly, the underlying assumption is that value prediction is more general/robust than reward modeling for aligning the ground-truth reward during inference, which needs further theoretical justification. An analysis or explanation supporting this claim would add depth to the paper. The paper should provide a theoretical analysis or empirical evidence to support the claim that value prediction is a more reliable signal for aligning actions with desired returns compared to reward modeling, and discuss the potential limitations of this assumption.

### Questions
1. Have you test your method in some robotics benchmarks?
2. Can the inference process be accelerated?

### Soundness
3

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
1

### Summary
This paper proposes to combine supervised learning and temporal difference learning for offline reinforcement learning. First, the model is pretrained by randomly masking a subset of a trajectory and predicting it. In temporal difference learning, the model is trained to predict the action value. Experiments show promising results.

### Strengths
1. It looks reasonable to combine supervised learning and temporal difference learning for offline reinforcement learning. 
2. The paper is easy to follow.
3. Experiments show promising results.

### Weaknesses
1. I am not sure about the novelty as self-supervised learning and value function learning are two common techniques.
2. Ablation studies about the design choices of the proposed framework are needed.
3. The performance over the baselines on different tasks seems inconsistent, as shown in Table 1.

### Questions
Please refer to the weakness.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces Double Checks the Transformer with Value Validation for Offline Reinforcement Learning (Doctor), a framework designed to address alignment issues between actual returns and desired target returns, especially in cases involving underrepresented or higher returns. Specifically, this approach integrates additional temporal-difference (TD) learning into the Transformer architecture, sampling actions around desired target returns and validating them through value functions. Experiments conducted in both offline and offline-to-online settings demonstrate improved alignment with target returns, showcasing the effectiveness of the proposed approach.

### Strengths
1. The paper is well-written and easy-to-read.
2. The motivation is clearly presented, focusing on addressing alignment issues within sequence modeling methods.

### Weaknesses
1. The paper lacks a comparison with state-of-the-art methods, such as RADT[1], which also addresses target return alignment, and QT[2], which enhances stitching capability by incorporating the TD method.
2. The performance improvements in D4RL are not significantly better than these baselines, diminishing the perceived effectiveness of the proposed framework. Although this work integrates the TD learning component into the MTM network, the improvement over MTM is marginal. Furthermore, during online fine-tuning, the performance gains are also less pronounced compared to the ODT baseline.

### Questions
1. Does interpolating between underrepresented returns and stitching information address the same issue? While stitching sub-optimal trajectories can yield better performance, it could also lead to undesirable outcomes not observed in the dataset, representing underrepresented returns. Thus, should the primary focus be on improving the stitching capability?
2. In line 167, $R_t$ is defined as the discounted return, while Decision Transformer (DT) treats it as the undiscounted sum of rewards. What is the rationale behind using the discounted return in this context?
3. In lines 185–186, how does the action-value $q_t$ provide the model with the ability to stitch sub-optimal trajectories?
4. Why was a bi-directional Transformer chosen, given that most DT-based approaches utilize a causal Transformer to predict actions in an auto-regressive manner? This causal structure is typically important during inference to predict future actions based on historical sequences.
5. Is the comparison of results in Table 1 equitable? The Doctor method requires sampling N target returns for alignment. Do the baseline methods also allow for such extensive sampling of target returns to construct their final results?
6. What is the time complexity of inference when compared to other baselines?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
RvS-trained Transformers lacks 1) the capability to interpolate between underrepresented returns in the dataset, and 2) to stitch information from multiple sub-optimal trajectories into a better one, due to its supervised nature.
The paper introduces Doctor, which aligns the return of the policy with the target return, by selecting the action that has the nearest Q function (learned via expectile regression, similar to IQL) to the target returns.
Doctor shows much better return alignment across various target returns, and pars with / outperforms other RvS methods in terms of performance.

### Strengths
1. Doctor shows much better return alignment compared to previous RvS methods.

* Experimental results in Figure 1, Figure 3 shows that Doctor shows much better alignment.
* This alignment can extrapolate for some datasets (i.e. being better than the dataset).

2. The algorithm of Doctor is simple and intuitive.

* The alignment happens in the inference time, and the algorithm is straight-forward (choosing the action with the closest returns)
* Combines SL and IQL-like loss, which does not need to query out-of-distribution actions.

### Weaknesses
1. The experimental results is insuffcient on showing the stitching capability of Doctor.
* While stitching is one of the main reason of integrating TD-learning to SL, the performance improvement compared to MTM (which is a pure RvS method) is incremental (708.6 vs 719.7), according to Table 1.
* Generally, D4RL MuJoCo Gym environments is not a good benchmark to evaluate stitching capabilities. Experimental results in D4RL Maze2D tasks or AntMaze tasks, which are designed for stitching, will be helpful on evaluating the stitching capabilities of Doctor.

2. The experimental results is insufficient on showing that "better alignment in returns help offline-to-online fine-tuning".
* Experiment results in Table 2 shows that the performance increase during online fine-tuning is larger for ODT. It looks counterintuitive, considering superior alignment capability of Doctor.
* Again, D4RL MuJoCo Gym environments might be not a good choice to evaluate offline-to-online fine-tuning. For example, Cal-QL[1] uses AntMaze, Kitchen, Adroit tasks for their experiments; experimental results on these environments might better highlight the superiority of Doctor.

### Questions
Q1. Does having better return alignment helps the final performance?
* i.e., can the problem of return alignment be solved by just having high target returns? (e.g. DT[2] uses 5x maximum returns in the dataset)
* It will be insightful if there are experimental results for ablating the inference-time alignment (with properly tuned target returns, e.g. 1x or 5x maximum return of dataset).

Q2. Does having better return alignment helps online fine-tuning?
* It will be exciting if Doctor is able to show clear improvements in online fine-tuning experiments on AntMaze or Kitchen or Adroit tasks, where offline-to-online methods (e.g. Cal-QL) have showed significant improvements.

Q3. Other than Q1 (final performance) and Q2 (online fine-tuning), can you share your ideas on why having better return alignment is beneficial, if there is any?
* e.g., does it help reducing the effort of searching for the target return used in inference?

Q4. Does Doctor improves stitching capability?
* Experimental results in D4RL Maze2D tasks or AntMaze tasks, which are specifically designed for stitching, would be informative to assess the stitching capability of Doctor.

Q5. What target return is used for evaluation?
* Can you share how did you find it? (e.g. is it the maximum return from the dataset?)


[2] Lili Chen et al., Decision Transformer: Reinforcement Learning via Sequence Modeling, NeurIPS 2021.

### Soundness
2

### Presentation
3

### Contribution
2
