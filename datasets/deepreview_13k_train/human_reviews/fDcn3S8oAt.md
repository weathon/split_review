# LASeR: Learning to Adaptively Select Reward Models with Multi-Armed Bandits

- Decision: Reject
- Scores: 3, 5, 5, 8

## Abstract
Reward Models (RMs) play a crucial role in aligning large language models (LLMs) with human preferences, enhancing their performance by ranking outputs during inference or iterative training. However, the degree to which an RM generalizes to new tasks is often not known \emph{a priori}. For instance, some RMs may excel at scoring creative writing, while others specialize in evaluating math reasoning. Therefore, using only one fixed RM while training LLMs can be \emph{suboptimal}. Moreover, optimizing LLMs with multiple RMs simultaneously can be prohibitively computationally-intensive and challenging due to conflicting signals from different RMs, potentially degrading performance. To address these challenges, we introduce \textbf{\method{}} (\fullform{}), which iteratively trains LLMs using multiple RMs, selecting and utilizing the most well-suited RM for each instance to rank outputs and generate preference data, framed as a multi-armed bandit problem. Our empirical results on commonsense and math reasoning tasks demonstrate that \method{} can boost iterative LLM optimization by optimizing for multiple RMs, improving the absolute average accuracy of Llama-3-8B over three datasets by $2.67\%$  over training with ensemble RM scores while also showing superior training efficiency (e.g., a $2\times$ speedup). Moreover, on WildChat, a benchmark of instruction-following prompts in open-form generation, we find that using Llama-3-8B \method{} leads to a $71.45\%$ AlpacaEval win rate over sequentially optimizing multiple RMs. Extending to long-context generation tasks, we find that on Llama-3-8B, \method{} achieves an average improvement of $2.64$ F1 points on single-document QA tasks and $2.42$ F1 points on multi-document QA over random RM selection when used with best-of-$n$ sampling. Our analysis shows that \method{} is robust to noisy rewards and generalizes to multiple settings.  Finally, we demonstrate that \method{}'s RM selection changes depending on the underlying task or instance, and we verify the presence of conflicting preferences from multiple RMs, which can be mitigated using \method{}

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper discusses one method to use multiple reward models during training. The method uses a linear adapter, called A_k corresponding to reward model k \in [K] which is used to obtain a certain "reward". This reward pertains to how good a reward model is for a given batch of inputs. The inputs are modelled as vectors obtained from the last token of a sentence, averaged over the sentences in the batch. The method strongly suggests using multiple reward models, but why use their method of LinUCB is not clear. The paper suggests that ensembling works, but there are many methods for ensembling. Why use their method is not clear from the given experiments.

### Strengths
- The results are strong. They show improvements over their chosen baselines.
- The paper is written clearly, and is highly readable. All the points are well covered.

### Weaknesses
 - There is no baseline that selects more than 1 reward model over an epoch of training. The baselines are rather weak. What about a simple baseline that learns a classifier to choose the reward model based on the type of query. If Bandit algorithms perform better than such an approach, we can conclude that the method of using covariance works. Without any such baseline, we are left with the conclusion that one should choose the RM depending on the input c(t). Further to this, why use the authors' specific method dependent on c(t) is not clear.
- Why use MAB? why is there no discussion on the advantages gained by using the "exploration" that MABs provide?
- Adversarial training set choice. Imagine there are k RMs. Assume RM k is well coordinated with input_i where i%K = k. In other words, this RM k correlates well with human judgement for every i'th instance for i%K = k. For the remaining inputs, it performs poorly. Similarly, assume this is true for all RMs RM_i \in {RM_1,...RM_K}. Then assume a batch is of size K, where batches arrive without randomized order (i.e. sequential order). Then given a batch, no RM would correspond to the required outputs for all inputs in the batch.

- Why LinUCB? What is the "exploration" here? Why not simply train a classifier (or matrix A) to choose based on some criterion/classifier?
- Why not a linear combination of the reward functions? What if two are good? Why use arg-max over a weighted sum?

### Questions
- Please give more insights on each of the RMs used. For example which RM performs well for which examples? Once that is known, could you cluster the batches for training based on all inputs in the same batch using the same RM? Would that not perform better? Currently a batch is a mix of different inputs, some of which may not be suitable to the RM chosen for the batch.
- If one is using multiple RMs, would one not like to tune the RM itself instead of choosing between RMs that are designed to be good general purpose models (i.e. can you train domain specific RMs rather than generic RMs)? I know the setting is that the reward models are already given to you. But if you are using multiple RMs, would you not like to train the RMs to be good at certain domains?

### Suggestions:

- Please consider adding more details on what the RMs are, and how they were chosen. Does the method generalize to more than 4 RMs?

### Limitations:
- The experiments did not make it clear to me that this is the best way to use multiple reward models. in fact none of the baselines are allowed to choose between multiple RMs for different batches. This points to a trade-off between the memory usage of multiple RMs vs accuracy on downstream tasks.

### Additional points
Happy to raise my score given a convincing rebuttal on some of the concerns raised.

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
This paper introduces LASeR, a novel approach for training large language models (LLMs) by adaptively selecting suitable reward models (RMs) for various tasks, framed as a multi-armed bandit problem. Unlike previous methods that ensemble multiple RMs, LASeR aims to enhance computational efficiency and avoids conflicts from using different RMs, by selecting and utilizing the most appropriate RM for each instance to rank outputs and generate preference data. Extensive experiments demonstrate that LASeR consistently outperforms baseline methods across multiple benchmarks.

### Strengths
1. The proposed LASER iteratively trains LLMs using different RMs by dynamically selecting the most appropriate one for each training instance using a contextual bandit algorithm, specifically LinUCB, which effectively addresses the potential inefficiencies and conflicts present in ensemble methods that handle multiple RMs simultaneously.
2. The paper thoroughly evaluates LASeR across various datasets and tasks, showcasing its superior performance over baselines.

### Weaknesses
1. Fairness of Comparison: In Section 4, LASeR is compared with baselines that do not actively leverage information from interactions with the datasets. The RM selection in these baselines is either fully random or in offline fashion. Specifically, in Table 4, the "best RM" baseline (Zephyr-7b-alpha) is not the top performer on StrategyQA and MMLU, which contradicts claims in Appendix B. Additionally, the sequential RM selection shows better performance than other baselines across most datasets, yet the explanation for this surprising result is missing. It would be more appropriate to compare LASeR with ensemble methods where RM aggregation adapts based on training information, as LASeR leverages training loss to adapt RM selection.
2. Limited Comparison with Ensemble Methods: The paper only compares LASeR with a simple offline RM Ensemble using averaged scores, despite the existence of more sophisticated ensemble methods that incorporate training signals [A1] [A2]. It remains unclear whether LASeR outperforms such methods. Moreover, the results on reasoning are the only ones compared against Offline RM Ensemble. Due to these issues, it is insufficient to infer whether LASeR outperforms ensemble methods in terms of robustness to noisy rewards or different tasks like long-context understanding and instruction-following tasks.
3. Clarification of Unique Contributions: While the paper effectively incorporates LinUCB for RM selection in LLM training, there is insufficient discussion on the challenges encountered during this integration. Highlighting the unique contributions and the advantages over ensemble methods would strengthen the paper.
4. Efficiency Concerns Beyond Accuracy-Time Tradeoff: The paper does not address that, in high-dimensional embedding spaces or with a large number of RMs, LASeR’s need to compute the inverse of the covariance matrix A for each arm could be computationally intensive.
5. Minor issues: 
   1. Undefined/Misleading Notations: For example, in Equation (1), $x$ should be $x_i$, and $\sigma,\beta$ are not defined previously.  Footnote 2 mentions $P$ as the number of sampled pairs per prompt, while $n$ in the notation paragraph seems to have a similar purpose. In section 3.2, the notation should be $\mathbf{x}_{m,t}$ to represent the batch at the $t$-th step of the $m$-th iteration. Also, $\mathbf{x}_t$ should be defined clearly as the set of prompts, but is later used as the set of the $d$-dimensional embedding of the prompt. The left-hand side of equation (2) should be the index of the selected RM, while $R_t^{*}$ is the model itself.
   2. Grammar and Typos: Some sentences, such as those describing the stages of LASER, contain grammatical issues or are incomplete. The reviewer recommends a thorough review for consistency in symbols and text.

### Questions
1. Could the authors elaborate the definition of $e_m$ and the method for generating the sentence embedding from the model $\pi_m$? Which part of Figure 1 corresponds to this process?
2. Could the authors provide insights into why Random RM selection often outperforms the Offline RM Ensemble and why Sequential RM selection surpasses Random RM selection?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduce the LASER framework, which enables LLMs to adaptively select the most appropriate Reward Models for different tasks. This approach addresses the challenges of using multiple RMs by optimizing the selection process, combining with bandit algorithm, such as LinUCB and Exp3, thereby enhancing the performance of LLMs across reasoning, QA and instruction following tasks.

### Strengths
1. Innovative approach to automatically selecting Reward Models using bandit algorithm. This MAB framework, allowing the model to dynamically choose the most suitable RM at instance level based on contextual information (embedding of the last token). This avoid the computational burden of previous approaches that based on RM ensemble.

2. Empirical results presented in the paper indicate that LASER achieves performance improvements over traditional methods, such as ensemble RM scores. LASER achieve improvement in wide range of tasks, suggest it's generalibility.

### Weaknesses
A notable weakness of the paper is the approach taken to set the reward in the MAB problem as the negative training loss. While maximizing the reward is equivalent to minimizing the training loss, this method raises concerns about the alignment of selected preference pairs with the language model. Specifically, if the MAB algorithm consistently selects RM that align with the LM (means that the preference pair generate by the RM has low loss in LM), it's essentially just reinforce the LM's existing biases rather than addressing its mistakes.

This raises a critical question, why would selecting RM that align with the LM lead to improved performance? If the LM makes an error and the RM correctly identifies that mistake, the training loss would be high, which means the MAB algorithm might avoid selecting the RM that highlights the LM's shortcomings. Consequently, this could result in a scenario where the model becomes less capable of correcting its errors, as it may favor RMs that validate its outputs rather than challenge them.

### Questions
Can author address why chosing the reward as the negative train loss would help in mitigating bias of LLM?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper describes LASER, which:
- Uses an ensemble of reward models (specifically 4) to align language models
- Selects reward models with a multi-armed bandit (based on the LinUCB algorithm) to classify the (embedded) input into different RM tasks, and
- Uses the chosen RM with language model sampling to create and train on preference data.

### Strengths
- The paper is well written
- Using LinUCB is well motivated
- Solution makes intuitive sense
- Experiments are extensive

### Weaknesses
Nitpicky things:
- (As far as I know) Figure 2 is not referred to in the main text
- Add a y-axis to Figure 4
- (As far as I know) Appendix B is not referred to in the main text
- I could not find where it mentions how many preference pairs are generated per iteration/



### Questions
I have two questions:
1. Why does the ensemble baseline perform worse than the best RM? This is indicated in lines 95-97 and Table 1.
2. You mention that Table 3 shows results on long-context understanding without training and best-of-n sampling. Do you have any results where you use the RM to generate preference pairs and use those as in-context examples?

### Soundness
3

### Presentation
3

### Contribution
3
