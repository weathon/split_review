# Demystifying Language Model Forgetting with Low-Rank Example Associations

- Decision: Reject
- Avg Score: 4.00
- Scores: 3, 6, 5, 3, 3

## Abstract
Large Language models (LLMs) suffer from forgetting of upstream data when fine-tuned. Despite efforts on mitigating forgetting, few have investigated whether, and how forgotten upstream examples are dependent on and associated with newly learned tasks. Insights on such associations enable efficient and targeted mitigation of forgetting. In this paper, we empirically analyze forgetting (measured in log-perplexity increase) that occurs in $N$ upstream examples of language modeling or instruction-tuning after fine-tuning LLMs on one of $M$ new tasks, visualized in $M\times N$ matrices. We demonstrate that the matrices display simple low-rank patterns, often well-approximated with multiplicative scalar effects of upstream examples and newly learned tasks. We also examine fine-grained associations with visualization and statistics. Leveraging the low-rank nature of the associations, we predict forgetting of upstream examples when fine-tuning on unseen tasks with matrix completion over the empirical associations. This enables fast identification of most forgotten examples without expensive inference on the entire upstream data. The approach, despite simplicity, outperforms prior approaches that learn semantic relationships of learned tasks and upstream examples with LMs for predicting forgetting. We demonstrate the practical utility of our analysis by showing statistically significantly reduced forgetting as we upweight predicted examples for replay at fine-tuning.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper investigates fine-grained associations between new tasks learned by LLMs and catastrophic forgetting of upstream data previously used for pretraining, under the lens of matrix completion. Modeling LLM forgetting as an $M\times N$ matrix with $M$ new tasks and $N$ upstream datapoints, the authors discover that the associations exhibit a low-rank pattern as a simple multiplicative regression model such as low-rank SVD provide a fairly accurate estimation of the matrix. Inspired by this finding, the paper proposes a novel example replay framework that replays upstream examples predicted to be forgotten under matrix completion during finetuning, thereby mitigating catastrophic forgetting.

### Strengths
- [S1] **Interesting problem and motivation.** Considering wide use of LLM adaptation, understanding fine-grained associations between downstream tasks vs. catastrophic forgetting has great potential as claimed by the authors, as it can inspire techniques for better knowledge retention.
- [S2] **Great presentation.** The paper presents interesting analyses and comparisons with previous similarity-based measures, making it easy to understand comprehensively understand the motivation and inspirations of this work.

### Weaknesses
Despite its strengths, the paper is weak with respect to practicality and experimental results, details of which are as follows.

- [W1] **Weak practicality under large number of downstream tasks.** The proposed framework requires finetuning the base LLM on individual tasks to gather train data for matrix completion, which incurs a high computational cost.  Considering unprecedented model sizes as well as range of downstream tasks for LLMs, we can expect the cost to quickly become intractable in many scenarios. This could be alleviated if we can instead sample a small number of finetuning tasks, and show that the proposed method is robust under small choices of such tasks, but this is somewhat unclear in the current draft.

- [W2] **Weak practicality due to requiring full access to upstream data.** The proposed example replay framework requires full access to upstream data during finetuning, yet we may no longer have access to exact upstream data points due to updates on the data or data sharing policies [A]. Ideally, it would be best to mitigate forgetting on upstream examples without explicitly using them during fine-tuning, yet the matrix completion formulation used in this work seems unsuitable for that direction.

- [W3] **Unconvincing experimental setup.** The proposed framework makes two runs of finetuning, one without replays to gather forgetting information $z_{ij}$ on the train set and perform matrix completion to pick upstream examples to replay, then a second finetuning of the model with intermediate replays on examples chosen. Given this process, it is unclear whether the statistics gathered *post-finetuning without any replay* will hold at every step of *finetuning with replay*, and additional analyses on the predicted forgetting without replay vs. with replay or a similar experiment seems necessary.

- [W4] **Insufficient performance gains.** While the main results in Figure 6 show that the proposed KNN-based approach is statistically better than the random baseline, all methods are significantly far from pre-finetuning performances, leading to concerns on the effectiveness of replay-based methods in mitigating LLM forgetting overall, which weakens the proposed method's practical utility claimed by the authors.

### Questions
Please refer to concerns in the weaknesses block above.

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper investigates the effect of instruction-tuning on language model forgetting and the strategies to mitigate them. In particular, the paper discovers that the associations between learned tasks and forgotten examples can be reasonably described by simple linear/multiplicative models, exhibiting low-rank patterns. This association can be used to select replay upstream samples when training the model on downstream tasks to mitigate the forgetting of prior knowledge.

### Strengths
1. The paper is well written with notable clarity. 
2. The paper provides extensive and well-designed quantitative and qualitative studies to understand the correlation between forgetting the upstream knowledge and tuning on the downstream tasks. 
3. The paper highlights that the importance/similarity of the examples to the target downstream tasks is a different notion compared to their sensitivity to be forgotten. 
4. The proposed predict-then-upweight replay strategy effectively mitigates the sample forgetting for upstream pretraining/instruction-tuning data in terms of perplexity.

### Weaknesses
1. Reducing LLM forgetting of the upstream knowledge during instruction-tuning and alignment stages is an important aspect, but typical instruction-tuning and alignment datasets have other metrics for evaluation. It is unclear whether reducing forgetting has practical benefits or trade-offs to these downstream tasks. 
2. There are extensive discussions about using SVD to approximate the matrix, which certainly proves the hypothesis that leveraging a simple forgetting predictor can be more helpful than task-related features. However, the final forgetting predictor using KNN over SVD reduces the importance of those discussions.

### Questions
1. Could you provide more justifications on why SVD reveals fine-grained associations? Since increasing the rank $r$ of SVD provides a better fitting of the forgetting (perplexity) matrix, different SVD components ($r$-th component) may have opposite patterns since only the summation of all components matters. 
2. Are there particular reasons that the Spearman correlation is chosen over the Pearson correlation in Section 3.3? In addition, have you experimented with the correlation between forgetting and the cosine similarity of the textual representations (e.g., last token representation), which is an alternative to TF-IDF for textual similarity? 
3. In Table 2, it seems that forgetting is more difficult to predict for instruction-tuned OLMo-7B-Instruct. Why is that so? Is it correlated with the absolute perplexity of the upstream data?
4. As also raised in weakness 1, how does the proposed forgetting-mitigation approach affect the performance on the downstream tasks (or even the upstream tasks) that are typically not evaluated by perplexity?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper draws connections between upstream data that is forgotten during fine-tuning, and the new task.  It analyzes forgetting of past data after a model fine-tunes on new data using log perplexity, and shows how a matrix describing upstream loss given a new task can be described with low rank form. This matrix can then be used to predict forgetting of upstream tasks after fine-tuning. Finally, the paper describes a method to mitigate forgetting in fine-tuning by using weighted replay on upstream tasks that are more likely to be forgotten.

### Strengths
-I find it very interesting to describe forgetting using a low-rank representation. This shows that fine-tuning on tasks can be described using predictable forgetting patterns. 

-It was very thought provoking to see how correlated the similarity of various tasks was to the likelihood of those tasks being forgotten.
 
-The paper provides a novel method to perform weighted replay for mitigating forgetting.

### Weaknesses
 -Figure 2: it would be really helpful to add a description and possible analysis featuring what specific knowledge the examples cover, and thus the model forgets. Particularly if there is a correlation between forgetting and specific topics.

-The motivation for predicting forgetting rather than running inference could be more obvious: it is assumed that running inference on upstream examples is expensive, and thus matrix completion offers an alternative for predicting forgetting to mitigate it. However, given that there are enough resources available for a model to perform even costlier fine-tuning, it is not obvious why predicting forgetting rather than running inference is much more beneficial. Perhaps, a further explanation and a direct comparison of the approximate costs associated with performing matrix completion compared to running inference could be included. 

-Figure 6: It would be beneficial to add another baseline which considers weighted sampling for replay based on the actual forgetting values for all data.

### Questions
-Figure 6: Random seems to outperform more complex baselines, can you explain why that might be?

### Soundness
4

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
4

### Summary
This paper explores catastrophic forgetting of the pretraining or instruction tuning data after fine-tuning on downstream tasks. Specifically, the authors attempt to identify which samples (chunks of pretraining data) are forgotten when finetuning on various tasks, with a view to understanding the role of task similarity.

The authors analyse the amount of forgetting (measured by log perplexity increase) on each sample on a range of tasks. Analyzing the resulting data, the authors suggest that this data has a simple structure (though see weaknesses). This analysis relies upon a small selection of LLMs with open-source training data.

Building on this insight, the authors use matrix completion approaches predict which samples will be forgotten when training on a downstream task, though their approach requires access to forgetting data for some samples on the target task.

Finally, the authors use their prediction of which samples will be forgotten to upweight them during replay, and report improved forgetting mitigation compared to some other methods.

### Strengths
- The paper studies an important, timely problem, and connects previous research on task similarity to the contemporary LLM setting.
- Figure 1 is a helpful clarification of the authors' approach.
- The mitigation case study---using replay on their predicted forgotten samples---is a good idea to test the utility of their predictions.

### Weaknesses
 - The results of this paper rest on the idea that that there is a simple structure that explains which samples will be forgotten when training on a given downstream task. However, I don't see clear evidence that this is the case. For example, referring to fig. 2, the authors state that they "see Z generally displays a neat and simple pattern." Such a pattern is not at all clear to me, and I would question the value of visualizing a large matrix in order to draw conclusions about the complexity of its structure.
- The authors rely on linear regression modelling to quantify how well forgetting is explained by (the indices of) each sample and task. The authors admission that "the R^2 scores are relatively lower [on some models]" makes me question the robustness of this approach. Why should the results vary so significantly between models of the same scale (e.g. OLMo-7B and MPT-7B) or even within the same family, where we can assume the pretraining data is the same (e.g. OLMo-7B and OLMo-1B)?
- What do the SVD components in section 3.2, fig. 4, tell us that we did not already know from visualizing the full matrix, e.g. in fig 2c? It is already evident from the full matrix that finetuning on TruthfulQA results in greater forgetting.
- The matrix completion approach requires access to the forgetting of some samples on the test tasks, significantly limiting its practical utility.
- The paper needs significant attention to improve its language and clarity. Numerous sentences don't make sense (e.g., "There has been a growing need for long-term usability of LLMs"), are ungrammatical (e.g., "We perform statistics of forgetting"), or are unclear (e.g., "As a main comparator"). I would also strongly encourage the authors to avoid usage of the vague term "associations" throughout the paper, where the authors tend to mean "task similarity" or "relationship between pretraining and fine-tuning task." For example, the "association matrix Z" might be better described as the "sample forgetting matrix Z".
- The paper lacks substantive discussion of its limitations, with the exception of lines 428-433 on the limitations of replay (rather than the limitations of their work more generally).
- **Minor**: It would be helpful to restructure the abstract to more clearly motivate the problem and what the authors propose. At present there excessive detail about constructing matrices, which makes it hard to understand that the paper's central concern is predicting catastrophic forgetting as a function of task similarity.

### Questions
1. Could the authors elaborate on why OLMo-7B and OLMo-7B-Instruct has "more complicated associations" than the similarly-sized MPT-7B (see weaknesses)? What is the intuition here?
2. The idea that the interaction between pretraining data and finetuning task determines forgetting would be supported by an additional baseline in the matrix completion experiments. Specifically, did the authors consider attempting matrix completion using just an average over finetuning tasks, rather than fitting to all tasks separately? Demonstrating that the average-over-tasks vector is insufficient would strengthen the results in table 2.
3. Could the authors provide more detail on how they determined their significance testing results in fig. 6? How did the authors correct for multiple comparisons?
4. For the replay mitigations in fig. 6, how was the kNN chosen rather than the additive linear or SVD methods (as mentioned on lines 347--353)? If these approaches were also tested, they should be reported, and need to be included in the multiple comparisons correction.
5. What are the fine-tuning tasks used for the mitigations experiments in section 4.2? This section is impossible to evaluate without this information.

### Soundness
1

### Presentation
1

### Contribution
2

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper investigates forgetting in LLMs by building simple, low-rank models of example associations between upstream examples and downstream tasks. Its contributions are to 
1. Demonstrate the simple low rank models can predict forgetting of upstream examples when models are trained on down stream tasks. It visualizes these associations and demonstrates goodness of fit. The authors also argue that these example association models are more predictive of forgetting than other baseline methods.
2. It predicts which examples will be forgotten when finetuned on new tasks and shows that this can be used to optimize the presentation of examples in a replay buffer to mitigate forgetting.

### Strengths
**Originality**: The paper takes an interesting and simple approach to understanding example forgetting and finds some intriguing results.
**Quality**: The paper follows a thread from understanding structure in these forgetting associations to developing a strategy to mitigate forgetting. It provides some baselines to argue for the effectiveness of all of its methods.
**Clarity**: The paper is very well written and clear. All the experiments, figures, methods, results are well explained and easy to follow.
**Significance**: The paper explores a relevant and important topic and presents an effective algorithm for mitigating forgetting.

### Weaknesses
1. While the fact that the forgetting association matrices are low rank, it is unclear what the takeaway from this is/how I should interpret or use this. Additionally I am not sure how to interpret any of the low rank structures. Also, the optimal predictor for forgetting with association matrix completion and what is used for forgetting mitigation is the kNN model which does not directly use this result?
2. I am not sure forgetting as measured by log perplexity is sufficiently convincing and would really like to see downstream accuracy on tasks. Is the forgetting that is observed actually hurting the capabilities of the models? Does it hurt the model's performance on benchmarks?

### Questions
1. What are the takeaways/what does it mean that forgetting association matrices are low rank? Should I expect them to be high rank or should that be the null hypothesis? For the multiplicative model, how should I interpret these R^2 values?
2. For the multiplicative model, do you have any insights on the $\alpha_i$ and $\beta_j$s? Which tasks cause more forgetting and why? Is it because their data is out of distribution? Amount of data? Which examples are more likely to be forgotten and why? Are they weird/noisy examples? Do they have higher loss compared to the mean across the dataset i.e. less well learned? Are they from a specific domain?
3. How do you interpret the fact that kNN does better than SVD at predicting forgetting?
4. Can you show that forgetting isn't just a perplexity phenomena and actually impacts performance on benchmarks? Can this benchmark performance degradation be predicted? The reason this is important is because it is possible to increase perplexity on certain examples on the training set, especially if they are noisy/rare examples without hurting language model capabilities and it would be useful to understand this.
5. It seems to me that predicting the association matrix is not really necessary for mitigating forgetting because the ground truth forgetting is easy to measure: you already have to fine-tune your model on the "test tasks" because you need to measure forgetting on the seed dataset. So you are just saving the inference cost on the rest of the upstream examples you are trying to not forget but just for the test tasks?

### Soundness
2

### Presentation
4

### Contribution
2
