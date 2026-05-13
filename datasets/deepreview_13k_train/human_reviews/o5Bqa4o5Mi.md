# $\pi$2vec: Policy Representation with Successor Features

- Decision: Accept
- Scores: 5, 5, 6, 5

## Abstract
This paper introduces \bmname, a method for representing black box policies as comparable feature vectors.
Our method combines the strengths of foundation models that serve as generic and powerful state representations and successor features that can model the future occurrence of the states for a policy.
\mname\ represents the behaviors of policies by capturing statistics of how the behavior evolves the features from a pretrained model, using a successor feature framework. 
We focus on the offline setting where both policies and their representations are trained on a fixed dataset of trajectories.
Finally, we employ linear regression on \mname\ vector representations to predict the performance of held out policies.
The synergy of these techniques results in a method for efficient policy evaluation in resource constrained environments.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The ability to represent reinforcement learning policies in a vector space would allow for quickly evaluating policies' performance offline. Successor features is a learning paradigm that defines a policy's performance (i.e., expected reward) as being linear in the features of the policy. The authors propose to leverage ideas from successor features by predicting the performance of unknown policies with the performance of known policies based on joint learned successor feature embedding. This would allow for evaluating unknown policy's performance offline without needing online interactions.

### Strengths
- The idea of storing an embedding space where you can look up policies could be beneficial for OPE and imitation learning.
- The combination of exploring foundation model features and successor features is interesting.
- The authors provide a very thorough empirical investigation of the performance of the proposed idea across several tasks. Furthermore, they investigated various representation learning ideas beyond changing the underlying foundational model, which provided insight into which representation is important for each task.
- The evaluation metrics chosen provide insight between relative performance (i.e., correlation), absolute performance (i.e., NMAE), and performance against the best policy (i.e., regret). All three metrics captured three different and important aspects of the learning problem, providing a lot of insight.

### Weaknesses
 - This paper needs more analysis regarding why certain features work better for certain settings. At the moment, if I implement this idea, I would have to enumerate all possible pairs.
- The authors only compare to 1 baseline algorithm that only depends on the actions of the policies in the offline dataset. Meanwhile, the proposed method uses the state-action in the offline dataset to learn the successor feature components. I don't know if the performance increase of the baseline is due to the proposed idea or the additional information the proposed idea has access to.



### Questions
- If you had online policy trajectories from behavior policies, how would that affect the proposed idea?
- How did you find the best policy to compare against for the regret metric? Was the best policy feature-dependent or feature-agnostic?
- Why is the correlation metric related to how many evaluations on the reboot are required to find the best policy? I thought correlation was the relationship between the set of predicted values and ground-truth values. This relationship could be arbitrarily bad; no matter how many evaluations you do, the underlying feature may not provide a reasonable signal that relates to the ground truth.
- Can I assume that correlation means relative performance (i.e.,  the ordering of values between the prediction and ground are the same), while NMAE is absolute performance (i.e., the predicted and ground values are exactly the same)?
- What is significant of NMAE? The performance values of Table-1 and Table-2 imply that correlation indicates regret. This means that representations with low regret have a high correlation, but NMAE does not have a relationship to regret.
- Why is action representation the only baseline applicable baseline? The underlying data has states and actions. Would it be unfair to condition a baseline on both state-action pairs?
- The discussion from (i), (ii), and (iii) in the results section is confusing. In results (ii), the authors raise the point that NMAE is better, but in (iii), the authors raise the point that their approach is better in regret. What metric is the most important across these metrics presented?


Missing cites:

- Original Successor feature paper:  Improving generalization for temporal difference learning: The successor representation by Dayan, et al. 1993.
- Successor Feature Representations by Reinke et al 2023
- Successor Feature Sets: Generalizing Successor Representations Across Policies by Brantley et al. 2021
- Successor Features Combine Elements of Model-Free and Model-based Reinforcement Learning by Lehnert et al 2020

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposed a new off-policy evaluation apporach. 
The problem setting is that given a set of historical trajectories sampled from other policies and its corresonding performance, it predicts the performance of a unseen policy. 

The main idea is using the average of successor features over a set of canonical states of each policy, to predict the policy performance.
The successor features are obtained via Fitted Q learning via a policy-agnositic state encoder.

The authors show that proposed approach is usually better than baseline across different domains and metrics.

### Strengths
- This paper studied an important problem of off-policy evaluation.
- As far as I k now, the idea of leveraging successor feature for the purpose of OPE is new.
- The authors conducted extensive set of experiments.

### Weaknesses
 - Potentially missing baseline: I am not closely follow the OPE literature, but could the authors explain why [1] is not suitable for this setting? 
We should be able to get ranking results by that approach.
- Missing key ablations: I think there are implicit key assumptions such as 
	- 1) the historical policies' performance should mostly likely cover the unseen policy. If not, the unseen policy's performance is way better, I hardly expect this approach would work. 
	- 2) the canonical states coverage. How does it affect the performance if state coverage of MDP is small? More specifically, if the historical dataset only cover 50% of
	states that the unseen policy would visit in the MDP, how does it affect the performance?

	It would be good to have a comprehensive understanding when this approach can be effective.
- In section 3.4, \Phi_\pi represents an aggregated average effect of the behavior of π, I think this highly relies on the implicit assumptions mentioned above. It would be 
good that authors can clarify.

### Questions
Please refer to the weakness section.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a method for representing reinforcement learning policies as comparable feature vectors. The idea is to use successor features to capture how a policy changes the states of the environment over time. In particular, the method leverages pretrained foundation models to encode individual states into feature vectors. After training the successor features on offline datasets of trajectories, the method aggregates the state-dependent successor features into a state-independent policy embedding that summarizes the policy's behavior. Finally, the embeddings are used to predict policy performance.

### Strengths
1. Novel policy representation method: The combination of successor features and foundation models provides a new way to summarize and compare policies based on their effects on the environment. Representing policies by their induced state changes rather than their parameters or actions is an interesting idea.

2. Strong empirical results: The paper presents extensive experiments across 5 domains, including real robots. The method outperforms the baseline policy representation method in predicting held-out policy performance.

### Weaknesses
1. Limited theoretical analysis: The paper shows empirically that the obtain successor representations are effective, but provides limited insight/intuition or analysis into why combining successor features and foundation models results in good policy embeddings. It's unclear what properties of the foundation model embeddings are crucial for this success, and how they interact with the successor feature framework. For example, are the learned representations capturing task-relevant features, or are they simply providing a high-dimensional space where linear separability is easier to achieve? A deeper analysis of the feature space and its relationship to policy performance is needed.

2. Restricted to offline setting: The method seems to require pre-collected offline datasets and cannot be applied in an online setting where policies interact with the environment. The offline assumption limits the applicability. The reliance on a fixed dataset makes it difficult to adapt the policy representation to new environments or tasks without retraining the successor features. Furthermore, the method's performance may be highly dependent on the quality and diversity of the offline data, which is not always guaranteed in real-world scenarios.

### Questions
1. Why do successor features plus foundation models work well for policy representation? More analysis on why this combination is effective compared to other representations would be useful.

2. Can this method be extended to an online setting where policies interact with the environment? 

3. How does dataset composition impact the quality of the policy embeddings? Is there any further analysis on dataset requirements and relationships between dataset and representation quality?

4. Have you considered any other methods to aggregate the state-dependent successor features? Averaging seems effective but overly simplistic; are there alternatives that may capture policies better?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents an approach to build a compact, vectorial representation of policies, that can be used for off-policy evaluation. The idea is to leverage pre-trained image-based models to generate state-based features to be used for training successor features for policy evaluation. The policy features ($\pi 2vec$) is obtained by averaging the successor features over a set of states sampled from the offline dataset.

The authors showed that these features are effective in the task of off-policy evaluation.

### Strengths
The paper is clear and easy to follow. The approach is simple and intuitive, and, as far as I know, it is novel.

### Weaknesses
 - I would appreciate more details about the relevance of this setting. What are the use cases you have in mind?
- Could you clarify the metrics used to evaluate the approach? You should report (at least in appendix) the equations.
- Why don't you use ranking metrics (Mean Average Precision, DCG, etc)? These seems quite relevant for evaluating methods for offline policy selection. As you mentioned, absolute error in terms of value prediction may not be always relevant.
- You decided to focus on visual representation without clearly explaining why. I think it is important to evaluate the approach also on state-based observation. How would you select base state features in this setting?
- Similarly, I would have expected an evaluation on standard offline benchmarks (e.g., D4RL or ExoRL). For example, if I'm not mistaken, ExORL provides also image-based observations.

### Questions
See above.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
