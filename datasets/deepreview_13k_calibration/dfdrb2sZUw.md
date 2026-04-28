# Risk Aware Negative Sampling in Link Prediction

- Decision: Reject
- Avg Score: 4.75
- Scores: 6, 5, 5, 3

## Abstract
It is commonly believed that Message Passing Neural Networks (MPNNs) struggle in link prediction settings due to limitations in their expressive power. Recent work has focused on developing more expressive model classes, which are capable of learning link representations through techniques such as labeling tricks, the inclusion of structural features, or the use of subgraph methods. These approaches have yielded significant performance improvements across a range of benchmark datasets. However, an interesting question remains: have we fully wrung out the performance by optimizing the other aspects of the training process? In this work, we present results that indicate that significant amounts of model performance have been left on the table by the use of easy negative-samples during training. We theoretically explore the generalization gap and excess risk to quantify the performance loss caused by easy negatives. Motivated by this analysis, we introduce Risk Aware Negative Sampling in Link Prediction (RANS), which efficiently performs dynamic hard-negative-mining. Empirical results show that a simple GCN augmented by RANS realizes between 20\% and 50\% improvements in predictive accuracy when compared with the same model trained with standard negative samples.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors propose a new methodology for negative sampling that considers theoretically provable assumptions about excess risk in the supervised link-prediction (LP) setting to enhance expressiveness and therefore performance of LP models. From which, the theorems and proofs are integrated into a clean algorithm which is applied in experiments that demonstrate: enhanced performance versus other sampling methods, more practical alignment between training/validation/testing performance, demonstrable closing of the performance gap between negative sampling strategies, and competitive performance for simple baselines versus SOTA LP methods.

### Strengths
* The authors take great care to relate their work to existing methodologies, such as expressive sampling methods and even other architectures like GANs. This flows nicely into the theoretical assumptions and justifications, providing a solid foundation from which the proposed RANS relates to other works.
* The proofs used for the intuition behind constructing the RANS algorithm are exceptionally clear, the added context is helpful for quantifying the impact of the theoretical assumptions and the logical flow is intuitive as to what sort of contribution that RANS provides.
* The authors make use of experimental methodologies that are also intuitive and relate well to existing research on sampling strategies, coupled with the use of the HR@K metric adds robustness to the performance gains provided by RANS in all experiments conducted for this paper.

### Weaknesses
 * The current use of smaller benchmark datasets is of great practical concern, especially given that the risk associated with sampled negative edges is dependent on an estimation. Do we see a similar level of performance improvement when testing with larger benchmarking datasets, such as the OGB datasets [1]? Without such a test, it is difficult to determine whether replacing easy negative samples with the risk-aware negative samples at a given epoch is not only a safe assumption but whether or not the theoretical assumptions hold in larger sample spaces. Specifically, the risk estimation could be highly sensitive to the size and structure of the graph, and the performance gains observed on smaller datasets might not translate to larger, more complex graphs where the distribution of edges is significantly different. The paper should include experiments on larger datasets to validate the robustness of the proposed method.
* I understand that maintaining fixed hyperparameters and model is important for testing just the sampling strategies, but given the relatively high-level of variance within the results for each table, especially Table 1, it seems pertinent to run a significance test between the scoring distributions to provide statistical confidence on potential performance gains across sampling strategies. The lack of statistical significance testing makes it difficult to ascertain whether the observed differences are due to the sampling method or random variation. Reporting p-values or confidence intervals would strengthen the claims about the effectiveness of the proposed method.
* The results in Table 3 are difficult to believe given that GCN+RANS is the untuned variant applied in previous experiments. Have the SOTA LP methods been tuned on the cora and citeseer datasets? This becomes especially critical given that lack of tests on larger benchmark datasets coupled with RANS theoretical assumption. The performance of GCN+RANS relative to state-of-the-art methods on these datasets is surprisingly high, raising questions about whether the comparison is fair. If the state-of-the-art methods were tuned and GCN+RANS was not, then the comparison is not a fair assessment of the sampling strategy's potential. It is crucial to clarify the experimental setup and ensure a fair comparison.
* What sort of restrictions might there be on applying RANS to SOTA LP methods such as BUDDY or SEAL? Given the performance enhancement RANS provides to GCN, testing potential gains that RANS can provide to the more-expressive SOTA LP architectures could provide strong empirical evidence on RANS effectiveness, eliminating concerns about it's practical applicability and reliance on risk-estimation. The paper should provide more evidence that RANS can be effectively integrated with other link prediction models, as the current results only show its effectiveness with GCN. The lack of experiments with more complex models limits the generalizability of the findings.

### Questions
* See "Weaknesses" Section of the review for the most-pertinent questions.
* Are the nu and delta hyperparameters in Algorithm fixed at runtime? If so, it is not possible to tune the hyperparameters to better understand their effect on performance or even expressivity?
* What is the intuition for setting nu to 0.95 and delta to 0.1? Is this just to restrict the sampled search space without being too restrictive? Considerations about these assumptions could be used for additional experiments on better understanding negative sampling, similar to what was detailed in Table 2.
* The following is not critical to the current review. Given the increased research interest in negative-sampling for link-prediction, article [2] may be of interest to the authors, especially the experiments regarding the alignment of positive and negative sample distributions. 
[2] Nguyen, Trung-Kien, and Yuan Fang. "Diffusion-based Negative Sampling on Graphs for Link Prediction." In Proceedings of the ACM on Web Conference 2024, pp. 948-958. 2024.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
While recent advancements like labeling tricks, structural features, and subgraph techniques have improved link prediction performance, this paper investigates the potential benefits of using hard negative samples to further enhance model accuracy. The authors present a theoretical analysis from an empirical risk perspective, and introduce Risk Aware Negative Sampling (RANS). This method can be integrated with any MPNN model to improve training effectiveness. Experimental results demonstrate that a GCN model equipped with RANS achieves 20% to 50% higher predictive accuracy compared to models trained with standard negative sampling.

### Strengths
1. It provides a theoretical analysis from the empirical risk perspective to demonstrate that using hard negative samples could enhance the performance.

2. The experiment shows that a simple GCN plugged with the proposed method could advance the model performance, and behave better than other hard negative sampling methods.

### Weaknesses
1.While the analysis is interesting, the idea that hard negative sampling could improve model performance is somewhat expected. Additionally, the paper lacks a clear comparison between the proposed method and existing hard negative sampling approaches. Further analysis and discussion could help clarify the advantages of RANS over existing methods.

2.Some claims in the paper require additional clarification. For example, the statements made in lines 213-239 would be more convincing with empirical evidence or supporting citations.

3.The proposed method appears to have high computational complexity, which could limit its scalability on large datasets.

4.Including results on Open Graph Benchmark (OGB) datasets, such as ogbl-collab, ogbl-ppa, and ogbl-citation2, would strengthen the evaluation and make the results more generalizable.

5.While the experiments demonstrate that RANS improves GCN performance, it would be valuable to see if it can also enhance other popular methods, such as SEAL, BUDDY, Neo-GNN, ELPH, etc.

### Questions
1.What's the advantage of the RANS comparing with the existing hard negative sampling methods.

2.Do you have empirical evidence or supporting citations to support claims in lines 213-239?

3.What's the computational complexity of the RANS? Does it has the scalability issue for large datasets?

4.What are the results on OGB datasets?

5.What are the results on other popular methods using RANS, such as SEAL, BUDDY, Neo-GNN, ELPH?

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
5

### Summary
This paper proposes the Risk-Aware Negative Sampling (RANS) method for GNN-based link prediction. RANS dynamically samples hard negatives based on model predictions, with the goal of reducing excess risk.

### Strengths
- This paper unveils the significance of negative sampling in link prediction tasks, providing both empirical and theoretical evidence to support its importance.
- Experimental results demonstrate that RANS achieves notable performance improvements.

### Weaknesses
 **W1.** Although the authors provide a theoretical analysis to highlight the importance of negative sampling, the methodological novelty may be insufficient for ICLR, as the proposed approach merely involves sampling hard negatives based on model predictions. Moreover, the method lacks a specific focus on link prediction and could be readily applied to other domains and tasks, which is not a tailored solution.

**W2.** The paper requires more thorough proofreading, as several critical issues diminish the overall quality. 

Examples include:
   1. Algorithm 1:
      - The algorithm seems to be missing details, particularly around Line 6.
      - In Line 4, shouldn’t it be $N_{\text{easy}} = \sum_{\text{neg}} \mathbb{I}(p < \delta)$ instead of $\mathbb{I}(p > \delta)$? The easy negatives would be those with low scores from the link predictor.
      - The combination of mathematical notation and pseudo-code elements feels cluttered.
      - The inclusion of the `argsort` operation appears redundant, as the sorted indices do not seem to be used for filtering or refining ${\tilde{D}^n}^\prime$.
      - It’s unclear how many samples are selected as new negatives, making it difficult to infer from the algorithm table. Additionally, a more detailed description of the proposed methodology in Section 6 would be beneficial.
      
   2. What does $\tilde{D}_{p,n}$ in line 318 indicate?

   3. The caption for Figure 1 should be revised; the central ring atoms are actually represented as *larger* vertices.

**W3.** The paper's focus is exclusively on GCNs in both theoretical and empirical analyses, which limits the scope of applicability. The authors should provide experimental results with other backbone GNNs to verify RANS's versatility.

**W4.** The authors do not provide an analysis of hyperparameter sensitivity. Although RANS appears computationally efficient compared to subgraph GNNs, its practical applicability could be compromised if performance varies significantly with changes in parameters like $\eta$ and $q$.

**W5.** The paper omits important and popular link prediction benchmarks, such as OGBL-COLLAB and OGBL-DDI [1]. Experiments are only conducted on small-scale datasets. 

### Questions
See weaknesses.

### Soundness
3

### Presentation
1

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
This paper studies the negative sampling in link prediction. Different from previous studies focusing on developing more expressive models for link prediction, this study dives into the selection of negative samples and how a proper selection can maximize the potential performance of any parameterized link prediction models. It introduces Risk Aware Negative Sampling (RANS), which can effectively improve various GNN-based link prediction models by iteratively sampling harder negative node pairs from the graph.

### Strengths
[S1] The paper has a clear motivation for studying the effect of negative sampling on link predictions.

[S2] The proposed negative sampling method is algorithmically simple and effective.

[S3] The experimental results show that RANS can improve the performance of various link prediction models.

### Weaknesses
[W1] The scalability is a big issue, which makes RANS almost inapplicable to any large-scale graphs. If I understand correctly, the step 2 in the Algorithm would cost at least $O(N^2)$ for each training epoch. This is not acceptable for any link prediction models if they have the ambition to be applied in the real world.

[W2] Following W1, this makes RANS hard to evaluate on OGB link prediction datasets, including Collab, PPA, and Citation2. These benchmarks have become the commonly accepted testbeds for link prediction methods.

[W3] The connection between theoretical analysis and the methodology is weak. In fact, the theoretical analysis section (Section 5) has a minor contribution. Its analysis has nothing related to the task at hand, which is link prediction. The conclusion in the analysis is too general to focus on its impact on the link prediction task.

### Questions
* Even though the study of negative sampling for link prediction is both novel and interesting, the implementation part is too inefficient to be applied to many real-world use cases. Do authors consider any other efficient way to select the harder samples?

### Soundness
2

### Presentation
3

### Contribution
2
