# Smaller, Weaker, Yet Better: Training LLM Reasoners via Compute-Optimal Sampling

- Decision: Accept
- Avg Score: 7.00
- Scores: 8, 8, 6, 6

## Abstract
Training on high-quality synthetic data from strong language models (LMs) is a common strategy to improve the reasoning performance of LMs. In this work, we revisit whether this strategy is compute-optimal under a fixed inference budget (e.g., FLOPs). To do so, we investigate the trade-offs between generating synthetic data using a stronger but more expensive (SE) model versus a weaker but cheaper (WC) model. We evaluate the generated data across three key metrics: coverage, diversity, and false positive rate, and show that the data from WC models may have higher coverage and diversity, but also exhibit higher false positive rates. We then finetune LMs on data from SE and WC models in different settings: knowledge distillation, self-improvement, and a novel weak-to-strong improvement setup where a weaker LM teaches reasoning to a stronger LM. Our findings reveal that models finetuned on WC-generated data consistently outperform those trained on SE-generated data across multiple benchmarks and multiple choices of WC and SE models. These results challenge the prevailing practice of relying on SE models for synthetic data generation, suggesting that WC may be the compute-optimal approach for training advanced LM reasoners.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper challenges the common practice of using strong but expensive (SE) language models to generate synthetic training data, proposing instead that using weaker but cheaper (WC) models may be more compute-optimal. The authors introduce a "compute-matched sampling" framework that enables fair comparison between WC and SE models by accounting for their relative compute costs. At a fixed compute budget, this framework shows that one can generate P_SE/P_WC more samples from a WC model than an SE model. The authors evaluate this approach across multiple model pairs (Gemma2 9B/27B and Gemini Flash/Pro), tasks (primarily mathematical reasoning), and training paradigms (knowledge distillation, self-improvement, and a novel "weak-to-strong improvement"). They assess the generated data along three key dimensions: coverage (problems solved), diversity (unique solutions per problem), and false positive rate (correct answers with incorrect reasoning). The results consistently show that training with WC-generated data outperforms SE-generated data when properly compute-matched.

### Strengths
1. _Originality_:
   - Introduces a novel compute-matched sampling framework with clear mathematical foundations
   - Proposes a new "weak-to-strong improvement" training paradigm that challenges conventional wisdom
   - Provides a fresh perspective on the compute-quality trade-off in synthetic data generation

2. _Experimental Rigour_:
   - Comprehensive evaluation across multiple dimensions:
     * Multiple model pairs (both open and closed models)
     * Various compute budgets and training paradigms
     * Different dataset sizes and difficulty levels
   - Thorough ablation studies that isolate the impact of coverage and diversity
   - Both human and automated evaluation of false positive rates
   - Clear validation of results through transfer learning (Functional MATH)

3. _Practical Impact_:
   - Demonstrates significant cost savings potential (0.15x cost for comparable or better performance)
   - Shows consistent improvements across model sizes (7B to 27B)
   - Provides actionable insights for practitioners
   - Results particularly relevant given the trend of improving smaller models

4. _Technical Depth_:
   - Rigorous mathematical formulation of compute-matching
   - Analysis of traed-offs between coverage, diversity, and error rates
   - Ablation studies support main claims
   - Clear empirical validation of theoretical framework

### Weaknesses
1. _Theoretical Foundation_:
   - Lacks formal analysis of when WC sampling should outperform SE sampling
   - No theoretical bounds on the optimal sampling ratio, especially considering the interplay between model size and task complexity. The paper does not explore how the optimal ratio might shift as the complexity of the reasoning task increases, or as the model size grows significantly beyond the tested range.
   - Missing analysis of the relationship between model size and optimal sampling strategy. It's unclear if the observed trends would hold for much larger models or if there's a point where the benefits of WC sampling diminish.
   - Limited exploration of failure modes and their characteristics. The paper does not delve into the specific types of errors that WC models make compared to SE models, which could provide insights into when each approach is more appropriate.

2. _Methodology Limitations_:
   - Heavy reliance on ground truth for filtering solutions. This limits the practical applicability of the method in scenarios where ground truth is not available, or is expensive to obtain. The paper should explore the impact of imperfect filtering and how it affects the overall performance.
   - Limited exploration of alternative filtering strategies. The paper could benefit from a more comprehensive analysis of different filtering techniques, such as using a smaller model to verify the reasoning steps, or employing a confidence-based filtering approach.
   - FPR evaluation methodology could be more robust (50 human samples probably insufficient). The small sample size for human evaluation of false positive rates raises concerns about the reliability of these results. A more rigorous evaluation with a larger sample size would be beneficial.
   - Some key implementation details relegated to appendices. This makes it difficult to fully assess the reproducibility and practical implementation of the proposed method.

3. _Generalisation Concerns_:
   - Primary focus on mathematical reasoning tasks. The paper's conclusions are primarily based on mathematical reasoning tasks, and it's unclear how well these results would generalize to other domains, such as natural language processing or complex problem-solving tasks.
   - Limited exploration of other domains (coding results show context-dependency). The coding results suggest that the effectiveness of WC sampling may be context-dependent, and a more thorough investigation across different domains is needed.
   - Unclear scalability to larger model sizes. The paper does not address whether the observed benefits of WC sampling would hold for much larger models, which are increasingly common in practice.
   - Performance on more complex reasoning tasks not fully explored. While the MATH dataset is challenging, the paper does not explore performance on even more complex reasoning tasks that require multi-step inference and planning.

4. _Practical Considerations_:
   - Deployment challenges in scenarios without ground truth not fully addressed. The paper does not provide sufficient guidance on how to implement the proposed method in real-world scenarios where ground truth is not readily available.
   - Resource optimisation strategies could be explored more. The paper could benefit from a more detailed analysis of how to optimize resource allocation for synthetic data generation, such as dynamically adjusting the sampling ratio based on task complexity or model performance.
   - Limited discussion of integration with existing training pipelines. The paper does not discuss how the proposed method can be integrated with existing training pipelines, which is a crucial consideration for practical adoption.
   - Cost-benefit analysis could be more comprehensive across different scenarios. The cost-benefit analysis could be expanded to include a wider range of scenarios, such as different model sizes, task complexities, and resource constraints.

### Questions
I will try and cluster my questions in sensible groups.

1. _Theoretical Understanding_:
   - Can you provide theoretical insights into when WC sampling should outperform SE sampling?
   - How does the optimal sampling ratio change with model size and task complexity?
   - What are the key factors that determine the success of weak-to-strong improvement?

2. _Methodology_:
   - How would the results change with more sophisticated filtering strategies?
   - Could you provide more details about the specific prompting strategies used?
   - How sensitive are the results to the choice of temperature and sampling parameters?

3. _Generalisation_:
   - What characteristics of a task make it more/less suitable for WC sampling?
   - How would the results scale to even larger model sizes?
   - What is the relationship between FPR and final model performance?

4. _Practical Implementation_:
   - How would you recommend implementing this in scenarios without ground truth?
   - What modifications would be needed for different domains or tasks?
   - Could you provide more detailed guidance on optimal sampling strategies for different scenarios?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper revisits the trade-offs between generating synthetic data using a stronger but more expensive (SE) model versus a weaker but cheaper (WC) model, and finds that at a fixed sampling compute budget, finetuning LMs with data from a WC model can consistently outperform data from a SE model in multiple settings.

### Strengths
1. The research question is significant, focusing on performance comparison of data sampled from WC and SE models, respectively.
2. The findings are impressive, challenging the traditional belief that data from a strong model is better for finetuning models.
3. The evaluation settings are diverse, demonstrating the effectiveness and robustness of this method, despite only the Gemma series models.

### Weaknesses
1. This paper centers exclusively on the Gemma series, and it is essential to extend the analysis to the Llama series to demonstrate the robustness of the conclusions.
2. While the paper aims to highlight the lower computational cost of the WC model for data synthesis (particularly important for large-scale data generation), all the experiments are conducted on relatively small datasets. This discrepancy undermines the overall contribution of the paper.
3. Compared to the SE model, the WC model can be regarded as a more diverse yet lower-quality variant. Therefore, it is crucial to compare it with techniques designed to enhance output diversity. Specifically, if adjusting the sampling temperature of the SE model consistently results in performance degradation relative to the WC model, this suggests that the WC model provides a superior quality-diversity trade-off compared to merely increasing the sampling temperature.

### Questions
1. Although both low and high budgets are studied, could you please provide the results of an extremely high budget where the cost is not an important factor? This should be indicative of diverse data scales.
2. Despite the train-test splits of MBPP, this paper only trains models on MBPP and tests them on HumanEval. The testing results on MBPP are expected to be provided for a more comprehensive understanding.
3. Writing：
- 1. All the ref links are invalid.
  2. l101, l104: "i.e." should be "i.e.".
  3. l103: grammar error for "we supervise finetune".
  4. l109: use \citet{} for "(Zelikman et al., 2024;Singh et al., 2023).".

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
This paper presents the novel observation that generating synthetic data using a weaker but cheaper (WC) model is more effective than using a stronger but more expensive (SE) model. The authors demonstrate that, under the same budget, data generated by WC models tend to have higher coverage and diversity, though with a corresponding increase in false positive rates. Additionally, they show that models fine-tuned on WC-generated data consistently outperform those trained on SE-generated data.

### Strengths
The paper is well-structured and clearly written, making the methodology and results easy to follow.

The experiments are well-executed and provide convincing evidence of the benefits of the proposed approach.

It addresses a critical issue in synthetic data generation, offering a valuable contribution to this area of research.

### Weaknesses
The conclusion may not hold when using models from different companies. Based on my experience, under the same budget, data generated by a larger model like Qwen2.5 7B could outperform that of a smaller one like Gemma2 2B.

The paper could benefit from experimenting with more complex reasoning tasks, such as tree search algorithms, and using a reward model to evaluate the quality of the generated data.

### Questions
It seems that the difference in data quality between the WC and SE models becomes larger at lower budgets. Is it possible that the WC and SE models generate data of similar quality when the budget is very high?

### Soundness
3

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
The paper investigates whether it is better to (self-)distill from a Gemma-27B LLM or to distill three times more finetuning data from a three times smaller Gemma-9B model. It finds that the three times more data of the smaller model, despite including more errors, leads to a higher performance of the finetuned student model.

### Strengths
* The paper investigates not only knowledge distillation, but also a self-improvement setup
* In Figures 4 and 5, it is interesting that training on model-generated solution paths (one per question; at least in the "27B low compute" setup) gives a better performance than training on human-provided solution paths (also one per question)
* Figure 7 carries an interesting finding: Despite training on the data generated by the small model which has more errors, the ultimate trained model does not have more errors in its reasoning. This implies that the additional data mitigates its lower quality, which might add evidence to the discourse beyond the setup studied in this paper.
* The writing and flow of experiments is mostly clear

### Weaknesses
 * In 21 of the 22 Figures, the paper hinges on "matching the compute", i.e., being allowed to generate 3 times more data when using the 3 times smaller LM. This confounds two factors of variation, making it hard to interpret the findings. This is the main weakness of the paper. One idea to improve on this weakness would be to test out distilling 1, 3, and 9 samples from the large LLM and 3, 9, and 27 samples from the small LLM (instead of the current 1+10 vs 3+30), so that there are both overlapping settings with a matched number of samples and with a matched compute.
* In the only figure where the small LLM is compared to the large LLM without this advantage (Figure 20 in the appendix), the large LLM produces better training data. It can be expected that if we use the large LLM to generate enough data until the student model converges, it will make a better distilled model. Thus, the only real application of the proposed method is when we do not have enough budget to produce enough data to converge. For the finetuning setup of the paper, that would amount to not being able to generate data for 8k-12.5k questions. This is a setup with limited applicability in practice. It would increase the contribution (score) of the paper to investigate problems where budget limits are hit more frequently in practice, like pretraining, see also my question below.
* Relative and absolute increases are reported inconsistently. E.g., in Figure 3b the fact that the proposed small model finds 11 instead of 5 solution paths per question (when it is allowed to generate 3 times more paths in total) is reported as a 125% increase (line 268), whereas the fact that 24% of its solutions paths are wrong compared to 17% of the large model is reported as a 7% increase (line 310). This inconsistency becomes problematic when reporting the increase on percentage numbers (e.g., line 258), where it is unclear whether this is a relative or absolute increase. Keeping the reporting consistent would increase both the presentation and the scientific soundness scores.
* The paper only evaluates Gemma (/Gemini) models. It would help judge the generalization of the claims (and increase the contribution score) to test it out on at least one other LLM, like a Llama model.
* The datasets are very limited to two math datasets, limiting the contribution. As above, more datasets would help judge the range of applicability, especially whether it also works on non-math and non-reasoning datasets.
* The paper does not compare to baselines, despite citing multiple closely related approaches
* The method still requires annotated data, because the LLM-generated data needs to be filtered out if it does not match the GT. It would increase the applicability of the score (and thus the contribution score) if there would be an ablation without filtering, i.e., answering whether the unfiltered erroneous data from the smaller model can still train a better model.

Small notes that did not influence my score and don't need to be rebuttled, I just note them to make the camera-ready better:
* The first paragraph of Section 3 could be shortened; it's message (in Equation 1) is just "if a model has x times more parameters, it takes x times longer to generate".
* typo in line 54, "filters"
* typo in line 103 "we supervise finetune"
* typo in line 151, "consists"
* typo in line 157, "for training student LM"
* typo in line 241, "that where"
* The references exclusively list arxiv versions of the papers, not their actual published versions
* The reference .bib file should best use double brackets for "{{OpenAI}}", "{{The Llama Team}}", to prevent the ill formatting in line 483 ("Team, 2024; Anthropic, 2024; AI, 2024")

### Questions
* Your distillation setup is limited to finetuning. One setup where it would be more realistic to not have enough budget is pretraining. Do you have any results on this? I of course do not expect to pretrain a network until convergence during the rebuttal, but it would already be helpful if you could show the first couple of iterations just to make sure the worse data (higher FPR) does not seem to converge to a much worse model.
* I'd be interested in sample-matched figures. The figures where I'd be most interested in a sample-matched comparison are Figures 4c and 5c. This would allow finding out if a small model can successfully improve a larger model, which would challenge beliefs in the field.
* Just to go sure: In the self-improvement setups, you keep training a model iteratively on its own generations from the current parameters? Or do you mean that you finetune a "fresh" 7B model using an already converged 7B model?

### Soundness
4

### Presentation
4

### Contribution
2
