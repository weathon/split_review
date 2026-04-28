# Learning to Rank for AutoML: enhancing pipeline selection with ranking information

- Decision: Reject
- Avg Score: 4.33
- Scores: 5, 5, 3

## Abstract
This paper introduces a learning-to-rank (LTR) framework to address the problem of pipeline selection in automated machine learning systems. The traditional approach to AutoML involves learning to predict the performance of various pipelines on a given task based on data acquired from previous tasks (i.e., meta-learning), which can be complex due to the need for different models for each task-specific metric. The proposed framework aims to select the best pipeline based on ranking rather than estimating a target metric, aligning more closely with the ultimate goal of the task (i.e., selecting pipeline candidates in order, from more to least promising). This approach enables more robust, metric-agnostic solutions that are easier to compare using ranking metrics like NDCG and MRR. The paper evaluates LTR strategies on public OpenML datasets, demonstrating a clear advantage for ranking-based methods. Additionally, the integration of LTR with Bayesian optimization and Monte Carlo tree search is explored, leading to improvements in the ranking metrics. Finally, the study found a strong correlation between ranking metrics (e.g., NDCG and MRR) and AutoML metrics, such as the task objective metric and the time to find the best solution, providing insights into how ranking-based methods could enhance AutoML systems.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
Overall the paper proposes an improvement in Automation of ML pipeline by predicting rank of an approach in the pool given config and data instead of predicting a metric score or formulating as a true ranking problem. They show promising results on different datasets and metrics. The experiment section is fairly elaborate.

### Strengths
Fairly elaborate experiment section.
Simple change to existing approach.

### Weaknesses
Writing can be improved significantly. It is a bit hard to read and understand the contributions as they are mixed with previous work and formulation.
Novelty is low.

### Questions
It is said that the approach is metric agnostic, you say that because the approach only cares about rank and not the metric value right? even though thats the case the rank order is determined by the metric right?? Would is still be metric agnostic? or is it metric-value agnostic?

In experiments given you are predicting rank order only would it make sense to try some classifier also instead of just regressors??

Would it also make sense to compare your approach to a model trained with some ranking loss function instead only comparing with score-based approach??

In BO approach used, you mention its pretrained, can you clarify how?

### Soundness
3

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
2

### Summary
This paper proposes an approach for AutoML which is based on learning the rank/position of candidate configurations rather than their absolute performance score. Multiple regression models are evaluated for learning to map a configuration to a position/rank. Experiments on several AutoML benchmarks show improved performance compared to score-based models.

* I am not an expert on AutoML, not sure why this paper was assigned to me. I can only provide a low-confidence review.

### Strengths
* The empirical results seem appealing in terms of achieving better performance compared to a score-based approach.
* The paper is clearly written.

### Weaknesses
 * The proposed approach is using a regression model with ranks instead of scores, which is different from a ranking algorithm which outputs a permutation. The authors state this clearly in the paper, however they do sometimes call this a learning-to-rank problem (e.g., in the title and in line 512), which often refers to ranking losses (pairwise/listwise) and not regression using ranks. It may be interesting to see how a ranking loss based approach would compare to the regression based one.
* The proposed approach covers only search spaces with a predefined set of configurations that is enumerable. Large search spaces are not handled. This limits the applicability of the method to scenarios where the configuration space is known a priori and is relatively small. The method would not be suitable for problems with very large or continuous search spaces, which are common in many AutoML applications.
* The use of positions instead of performance scores seems somewhat incremental (replacing scores by ranks). While the authors show empirical improvements, the core idea of using ranks as targets for regression, instead of scores, does not represent a major conceptual leap. It would be beneficial to see a more in-depth analysis of why this simple change leads to better performance, beyond just empirical results.

### Questions
* Table 2: is there an explanation of the missing entries for D1 in the table? Maybe I missed it.
* In Related Work, there is some recent work from neural architecture search, a related problem in AutoML, using ranking instead of scoring for training predictors. Some examples are:
  * Renas: Relativistic evaluation of neural architecture search, Xu et al. (2021)
  * DCLP: Neural Architecture Predictor with Curriculum Contrastive Learning, Zheng et al. (2024)
  * FlowerFormer: Empowering Neural Architecture Encoding using a Flow-aware Graph Transformer, Hwang et al. (2024)
Can you please comment on how this relates to your work?

Minor/typos:
* Line 135: perhaps give MSE (s_ij - f_ij)^2 as an example loss?
* Line 255: “This set of OpenML tasks includes 104 tasks, split *evenly* between 71 classification and 33 regression problems” — what do you mean by “evenly”?
* Table 2: Consider adding a legend for colors in addition to or instead of the caption description. Also, consider sorting first by dataset and then by model, it seems like the similarity within a dataset is higher than within a model. This would also be consistent with the arrangement figures 1 and 2.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper introduces a learning-to-rank (LTR) framework to improve pipeline selection in automated machine learning (AutoML). Traditional AutoML methods predict performance metrics to select optimal pipelines, which can be limiting and resource-intensive. Instead, this framework uses ranking-based selection, focusing on ranking pipelines by performance potential rather than estimating specific metrics. By aligning selection with ranking metrics such as NDCG and MRR, this method creates a more robust, metric-agnostic approach.

The paper evaluates LTR with sequential optimization techniques like Bayesian optimization and Monte Carlo tree search on OpenML datasets, finding significant improvements over the score-based methods. Key contributions include:
* Introducing LTR approach for AutoML pipeline selection.
* An empirical comparison demonstrating the advantages of ranking-based over score-based methods.
* Insights into the correlation between ranking metrics and traditional AutoML objectives.

### Strengths
1. Paper is well written, pleasing-to-read.
2. Comprehensive experiments, with details available in the appendix.

### Weaknesses
1. I personally enjoyed the paper and the work of replacing autoML task with learning to rank. However, my main worry is that the impact of the work could be limited. I might be biased. But my feeling is that attentions have been attacked to LLM and related works. The paper might be better justified for its impact if authors can show some evidence like introducing LTR improves AutoML for LLM training or prompting, etc. This may well beyond the scope of the work.
2. MCTS results missing on OpenML-Weka in Figure 1. Didn’t find any explanation for the missing results there either.
3. Minor issue: “green > 0, dark green > 10” in Line 347 and “yellow < 0, orange < 10”  in Line 348 should be better with percent signs like “green > 0, dark green > 10%” and “yellow < 0, orange < 10%”.

### Questions
1. Why rank-based approach show consistently (slightly) worse performance on D2 AMLB classification task in Table 2? Any intuition? Can rank-based approach be useful for specific tasks?

### Soundness
2

### Presentation
3

### Contribution
1
