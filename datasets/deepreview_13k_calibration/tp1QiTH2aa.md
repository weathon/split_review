# Cost-Effective Synthetic Data Generation for Post-Training using QWICK

- Decision: Reject
- Avg Score: 4.50
- Scores: 3, 5, 5, 5

## Abstract
Large language models (LLMs) are showing expert-level ability in various fields (e.g., programming and math). However, this progress heavily relies on the generation of high-quality synthetic data to improve the models’ capabilities during post-training. Generating such data in a cost-effective manner presents a significant challenge. Specifically, stronger models tend to generate higher-quality data but come with a substantial computational cost, while weaker models are cheaper to run but may produce weaker outputs. In this paper, we introduce Question-Wise model pICK (QWICK) to address this challenge. By tracking the empirical reward, cost, and number of trials for each model, QWICK strikes a balance between exploitation and exploration, ultimately converging on a cost-effective model for each specific question. Specifically, QWICK achieves a 50\% cost reduction on a programming dataset and a 40\% cost reduction on a mathematics dataset, without compromising data quality. Furthermore, compared to baseline methods, our approach can produce up to 2.1 times more valid synthetic data at the same cost. Our anonymized code is available at https://anonymous.4open.science/r/QWICK-17C3

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper addresses the challenge of improving LLMs through high-quality synthetic data generation in a cost-effective way. A common method to boost LLM performance involves sampling reasoning chains from teacher LLMs and fine-tuning the target model on these synthetic samples. However, choosing an optimal teacher LLM is complicated due to two primary factors. First, there is a trade-off between cost and reward: state-of-the-art (SoTA) LLMs produce high-quality reasoning chains but are expensive, while smaller models are cheaper yet prone to errors. Second, different LLMs may excel on specific subsets of data, making model selection question-dependent.

To tackle this, the paper formulates the model selection as a Multi-armed Bandit (MAB) problem with budget constraints, where each LLM functions as an arm of the MAB. It introduces QWICK, an algorithm inspired by the Fractional KUBE algorithm for MABs, which is adapted to choose models on a per-question basis based on their estimated utility (reward/cost) of the choice.

The method is evaluated against several baselines, including random model selection and dataset-level model selection using the popular UCB1 algorithm, which importantly does not consider cost. Experiments on three datasets demonstrate that the proposed approach achieves cost-efficiency and is competitive with baselines while requiring a smaller budget.

### Strengths
1. This paper addresses the critical challenge of generating synthetic data to enhance large language models (LLMs) in a cost-effective manner.
2. The proposed algorithm, QWICK, is technically robust, employing a multi-armed bandit formulation with budget constraints.
3. QWICK’s design is simple and has a low memory footprint, facilitating ease of implementation, adoption, and reproducibility.
4. Experimental results show that the method reduces costs by 40-50% compared to baseline methods while maintaining data quality.
5. QWICK demonstrates effectiveness across two distinct reward formulations: binary rewards and ORMs.

### Weaknesses
 - There are some missing comparisons including comparison to always using the best and worst models as well as comparisons with real data.  it was unclear to me if this is the red dotted line in the figures as this line was not included in the legend.  Having the results for each model included the figure would also help show how much better the selection is at various amounts of compute versus only using the 2B, 9B, or 27B models respectively.
- It is unclear how strong the models have to be as even the Gemma-2-2B models are already quite powerful, and the effectiveness of the algorithm is contingent on there being a large diversity in the models.  Can the authors include some ablation with a larger variance of models? This also goes in hand with the previous comment on showing the performance of each model individually.
- One limitation of the proposed approach is that the proposed approach is applied to tasks where the answer is easy to verify.  For other tasks (summarization or more complex instruction following), it may be hard to extend the proposed approach as knowing whether a model produces the correct answer is more difficult.
- The experiments only evaluate on train/test with the same data.  It would be interesting to know if the synthetic data has other impact on the evaluation particularly downstream robustness (e.g. train on MATH and test on GSM).

### Questions
Please see the *Weakness* section for recommendations on experiments and analyses that could further enhance the paper.

**Additional questions and suggestions (not affecting the score)**:
1. How are the initial values for rewards, costs, and usage counts set for the first model in the model pool in Algorithm 1?
2. The question-level reward term occasionally lacks the question number subscript `j` (e.g., on line 136).
3. How is the cost term determined in line 25 of Algorithm 1? Should this line perhaps follow line 29? A similar issue appears in other algorithms within the appendix.
4. Why is the dataset-level reward term updated after each question in Algorithm 1 (line 30), rather than after completing the entire dataset? Has this design choice been empirically validated?
5. Is there an explanation for the observed decrease in model performance when the budget is increased for the MATH and MBPP datasets in Figure 4?

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
This paper introduces Question-Wise model Pick (QWICK) an approach for generating high quality synthetic data with compute budgets.  QWICK uses a multi-armed bandit strategy to select models that can be used for generation.  The proposed approach is evaluated on mat and coding finetuning benchmarks and results indicate compute improvements from training with QWICK finetuning data.

### Strengths
- The paper makes contributions to improving synthetic data generation for finetuning. The authors study this in the setting of limited budget as synthetic data generation is still costly even for finetuning.
- The authors have included algorithms in the paper that detail the implementations including for baseline comparisons in the appendix.  This makes the proposed approach and related approaches easy to understand.

### Weaknesses
 - Dependency on Initial Model Pool: The algorithm's performance is tied to the quality of the initial pool of models, and it does not account for model improvement over time, which may limit its effectiveness in environments with evolving model capabilities.
- Constrained scenario: I assume the authors consider the scenario where the constructer of the dataset uses only API calls. This scenario is kind of narrow, since most of the companies and researchers may have their own GPU resources, I wonder this approach is still applicable under the assumption that some GPU is accessible, so that inference can be done locally.
- What happens to the data generated in previous iterations: I wonder are the samples generated in iterations prior to the termination still kept in the generated dataset? Or are they simply abandoned? If it is the latter, wouldn't it cause waste of computation?

### Questions
- What is the red dotted line in the figures?

### Soundness
2

### Presentation
3

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
This paper presents QWICK (Question-Wise model pICK), a novel algorithm designed to efficiently generate high-quality synthetic data for post-training large language models (LLMs) by dynamically selecting the optimal model for each specific question based on a balance of cost and quality. The approach formulates the problem as a budget-limited multi-armed bandit (MAB), allowing the algorithm to achieve reduction in cost on programming tasks and mathematics datasets compared to traditional methods. QWICK aims to address the challenge of cost-effective synthetic data generation by leveraging both strong and weak models to optimize data quality without exceeding budget constraints.

### Strengths
- Cost-Efficiency: The paper proposes a cost-saving solution for synthetic data generation, achieving significant budget reductions without compromising data quality.
- Adaptive Model Selection: QWICK's question-wise approach allows it to adapt to specific data points by selecting models dynamically, which improves data generation's quality and validity across diverse datasets.
- Empirical Validation: The algorithm demonstrates superior performance in experiments compared to baseline methods

### Weaknesses
 - This paper may be challenging for readers unfamiliar with reinforcement learning, including multi-armed bandits. The authors could consider presenting the methods in a more straightforward manner for clarity.
- The authors only test each dataset on models from the same series. Since models from different series could have comparable costs, how would selecting models from different origins impact the results?
- The prompt to generate synthetic data is missing, whether baselines are the same with QWICK.

### Questions
Please see weaknesses.

### Soundness
3

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
3

### Summary
This paper focuses on addressing the great cost of existing synthetic data generation methods. While stronger models generally produce higher-quality data, they come with significant computational demands. So this paper proposes QWICK, a cost-efficient framework that strategically selects among strong or weak models. By employing a reward mechanism, QWICK identifies the suitable model for each specific question, significantly reducing the cost of generating high-quality data while maintaining strong performance.

### Strengths
- The motivation to reduce the cost of generating high-quality synthetic data is compelling. As written in Lines 186–187, models can exhibit varying performance across the entire dataset, so selecting different models is not only appropriate for specific questions but also more cost-effective than relying solely on larger models.
- With the help of budget-limited multi-armed bandits, QWICK considers utility in determining which model to use, the evaluation metrics are the cost of LLM and the reward with ground truth or ORM. 
- Experimental results show that QWICK consistently outperforms both the random selection baseline and UCB1 specifically while maintaining sample diversity and coverage.

### Weaknesses
- This paper may be challenging for readers unfamiliar with reinforcement learning, including multi-armed bandits. The authors could consider presenting the methods in a more straightforward manner for clarity.
- The authors only test each dataset on models from the same series. Since models from different series could have comparable costs, how would selecting models from different origins impact the results?
- The prompt to generate synthetic data is missing, whether baselines are the same with QWICK.

### Questions
please refer to weakness

### Soundness
3

### Presentation
2

### Contribution
3
