# Targeted synthetic data generation for tabular data via hardness characterization

- Decision: Reject
- Avg Score: 3.75
- Scores: 6, 3, 3, 3

## Abstract
Synthetic data generation has been proven successful in improving model performance and robustness in the context of scarce or low-quality data. 
Using the data valuation framework to statistically identify beneficial and detrimental observations, we introduce a novel augmentation pipeline that generates only high-value training points based on hardness characterization.
We first demonstrate via benchmarks on real data that Shapley-based data valuation methods perform comparably with learning-based methods in hardness characterisation tasks, while offering significant theoretical and computational advantages. Then, we show that synthetic data generators trained on the hardest points outperform non-targeted data augmentation on simulated data and on a large scale credit default prediction task. In particular, our approach improves the quality of out-of-sample predictions and it is  computationally more efficient compared to non-targeted methods.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes a novel synthetic data augmentation approach focused on enhancing binary classification models, particularly on tabular data. It introduces a targeted synthetic data generation pipeline, using KNN-based Shapley values to identify the "hardest" points in the training data. By generating synthetic data specifically for these challenging data points, the paper aims to strengthen the model’s ability to generalize to new, unseen data while reducing computational overhead compared to non-targeted augmentation methods. Empirical evaluations demonstrate the benefits of this approach in improving out-of-sample prediction quality, particularly in applications like credit default prediction.

### Strengths
1. Originality: The paper introduces a novel approach to synthetic data generation, focusing on "hard" data points identified via KNN-based Shapley values. This method augments only challenging points, enhancing model robustness and bridging data valuation with data augmentation.

2. Quality: Extensive experiments on real and simulated datasets. Detailed benchmarking against existing hardness characterizers and comprehensive hyperparameter tuning validate the method, particularly w.r.t. its computational efficiency and model robustness.

3. Clarity: The paper is well-structured and clear. The figures and precise mathematical formulations make it easier to understand the paper. 

4. Significance: This approach has broad applicability for fields like finance and healthcare, where robust tabular data predictions are essential. By focusing on challenging data points, the method not only improves model performance but also offers a cost-effective solution.

In summary, the paper makes a strong contribution to synthetic data generation and introduces novel methods and demonstrates practical benefits for high-stakes applications involving tabular data.

### Weaknesses
1. The paper's focus is restricted to binary classification tasks, which limits the generalizability of the approach. The current methodology, relying on binary cross-entropy loss and associated metrics, may not directly translate to multi-class scenarios where class imbalances and different decision boundaries require more nuanced handling. For instance, the 'hardest' points in a multi-class setting might not be those with the highest Shapley values in a binary sense, but rather those that are close to multiple class boundaries or are misclassified across several classes. The authors should at least discuss how the method could be adapted to multi-class problems, considering metrics like macro-averaged F1-score or weighted accuracy.
2. The paper relies heavily on KNN Shapley values for hardness characterization. While KNN Shapley values offer a computationally feasible approach, their reliance on local neighborhoods might not capture the global structure of the data, potentially overlooking truly challenging points that are not close to other points. Furthermore, the choice of 'k' in KNN can significantly impact the results, and the paper does not sufficiently explore the sensitivity of the method to this parameter. Exploring alternative methods such as gradient-based techniques (e.g., GraNd) or dropout-based uncertainty measures, even if computationally more expensive, could provide a more robust characterization of data hardness. The authors should at least acknowledge the limitations of KNN Shapley values and discuss potential biases.
3. The method relies on specific synthetic data generators like CTGAN and TVAE, which may not perform as effectively on all types of tabular data (e.g., highly skewed or sparse datasets). These generators, while popular, have known limitations in capturing complex data distributions, especially when dealing with mixed data types (categorical and numerical) or high-cardinality categorical features. The paper does not provide sufficient analysis of the sensitivity of the proposed method to the choice of synthetic data generator. A more thorough investigation, including a comparison with other generators or an analysis of the data characteristics that make CTGAN or TVAE more suitable, is needed.
4. The study uses a fixed threshold (e.g., augmenting 10% of the hardest points) which seems a bit hard to justify. This fixed threshold approach lacks a principled basis and might not be optimal for all datasets. The optimal percentage of data to augment is likely to vary depending on the data distribution, the model complexity, and the specific task. A more adaptive approach, perhaps based on a performance plateau or a validation set, would be more robust. The authors should explore methods to dynamically determine the optimal augmentation threshold, rather than relying on a fixed percentage.

### Questions
See above in weaknesses for suggestions/questions.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
This paper proposes to (1) use data valuation methods rooted in game theory to characterize samples that are difficult / hard to learn, and (2) improve model learning / performance by generating synthetic data around these hard / highly valued samples. It is an empirical study that extends our understanding of known methods (KNN Shapley, Data-IQ, SMOTE, CTGAN, TVAE).

### Strengths
This work proposes to change the perspective on data distillation, i.e. to augment the most valuable points in training data, instead of pruning the least valuable ones. The idea itself is original and valuable, but...

### Weaknesses
 ... my impression is that this work resembles a shorter workshop paper rather than a complete contribution, i.e.:

0. (For context, there are no theoretical contributions in the paper, which is not a weakness in isolation.)
1. **Empirical evaluation.** There is little signal that the proposed method works. Although I am generally in favor of interesting, simple ideas, even insightful negative results, experiments are lacking:
  - A) Overall results with only 4 tabular dataset-model pairs are rather anecdotal and insufficient to make meaningful conclusions. What holds back from doing a comprehensive benchmark on 10++ datasets/models (e.g. OpenML-CC18, OpenML-CTR23 benchmarks) that would empirically show the method's superiority? The choice of datasets seems arbitrary and doesn't cover a wide range of data characteristics or complexities. The models used are also limited; expanding to include other common models (e.g., LightGBM, CatBoost) would strengthen the empirical findings.
  - B) Results presented in Sec. 4.1 are unconvincing, i.e. the method performs well on one of two datasets. The heatmap is unclear (I can't see differences between the columns/rows); why not present AUPRC in a table / lineplot / barplot, also with deviations / confidence? Moreover, it seems the mentioned conclusion about differences between the methods (L297-L302) could be derived without doing this benchmark at all. The lack of error bars or confidence intervals makes it difficult to assess the statistical significance of the results. A more rigorous statistical analysis is needed to support the claims.
  - C) Regarding Sec. 4.2, L468-473: I can instead argue that the chosen dataset + model (Amex + XGBoost) is not a good example to show the added value of the proposed method. Mind you, this improvement by 0.0004 seems to be the paper's main result. The reported improvement is negligible and could easily be due to random chance or hyperparameter tuning. The paper does not demonstrate a clear, substantial benefit from the proposed method.
  - D) The last Section 4.3 with Figure 9 is an ablation "to verify the robustness of the results" on synthetic data instead of making a convincing case on more various datasets. This ablation study on synthetic data does not address the core issue of the method's effectiveness on real-world datasets. The synthetic data experiments lack the complexity and variability of real-world data, making the robustness claims weak.
2. **Computational efficiency.** There are multiple unsupported claims made about the method's efficiency, also as compared to baselines. There are no experimental results to support these claims, e.g. analyzing the computational speed of KNN Shapley, showing its impact on the XGBoost model's convergence and computational time. The paper needs to provide empirical evidence of the computational cost of each step, including KNN Shapley calculation and synthetic data generation. A comparison of runtimes with baseline methods is necessary to support the efficiency claims.
3. **Redundancy in presentation?** Subjectively, the paper has overlong descriptions and too many figures, if only to fill the 10 pages. There are 9 figures containing 26 subfigures / tables, potentially obfuscating the unseen key result / contribution. See details below.

### Questions
0. **Redundancy?** Only for example:
  - Section 2. "Background" spans 2 pages describing in (too) much detail the already published methods (KNN Shapley, Data-IQ, SMOTE, CTGAN, TVAE), which are later applied but not modified or analyzed.
  - L315-L348 are details about training a single XGBoost model that would usually be found in the Appendix.
  - L351-369 discusses results only for the Data-IQ method (Seedat et al., 2022). Virtually Section 4.2.1 reads like a critique of Data-IQ (Seedat et al., 2022) instead of showing the applicability of the proposed method. Perhaps it can be better communicated to the reader at the beginning of this section / in its title (currently "Harndess characterization").
  - Figure 7 provides no valuable information.
1. The font size in Figures 1, 6, 7, 8(a,b), and 9(a) is too small. This could be fixed by saving the figures to smaller sizes so that all the elements will increase in comparison.
2. Please clarify: how do you label generated samples?
3. Clarify in the paper: In Sec. 3, what is model A? Does it need to be a KNN? (no)
4. Discuss in the paper: Does this method work for tabular regression tasks? (no)
5. In L300, we read "not requiring model training", but then L376 says "To choose the best K, validation Gini is monitored as we re-train XGBoost after gradually removing the hardest datapoints".
6. What is the motivation behind using the normalized Gini coefficient "2*AUCROC − 1" instead of F1?

There is a related work that came to mind when reading the paper:

- How does this relate to the concepts of dataset distillation (arXiv:1811.10959) and dataset condensation (ICLR 2021)?
- Can alternative data generators, e.g. TabDDPM (ICML 2023) or Adversarial random forests (AISTATS 2023), be used in this framework?

### Soundness
2

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
This paper presents two main contributions:
* Proposing the use of KNN Shapley values for hardness characterization
* Proposing a synthetic data augmentation pipeline that relies on training a generative model exclusively on hard data points

Both contributions are evaluated empirically. The effectiveness of Shapley values on a benchmark consisting of two real world datasets where it is compared to other hardness characterization baselines. 
The synthetic data augmentation pipeline is applied to a large credit default prediction dataset, demonstrating modest performance gains, with a slight advantage observed when augmenting using only hard examples.

### Strengths
The paper is generally well-written, with a coherent presentation of the main ideas.

The authors go to great lengths to justify every decision and significant care seems to have been taken to achieve a sensible evaluation setup that appropriately accounts for the inherent variance in the methods.

### Weaknesses
The main weaknesses of the paper lie with the experimental setup:
1. The main claims of the paper on data augmentation are supported by experiments on a single real-world dataset. This seems insufficient to draw meaningful conclusions about the wider applicability of the method. I would be interested to know if the conclusions hold on a wider range of datasets with different sizes and tasks.
2. Likewise, the results on KNN Shapleys as a hardness characterization are supported by evaluations on a benchmark of only 2 tabular datasets.
3. It would also be interesting if KNN Shapleys were compared to other hardness measures on the downstream synthetic data augmentation task.
4. More recent methods such as [1], [2] or [3] have shown significant improvements for synthetic data generation in tabular data over TVAE and CTGAN. It would be more relevant to evaluate the synthetic data generation pipeline with these methods.


**Minor Point**

The authors might want to be more precise with statements that can be easily misinterpreted such as (page 8):
> For models trained on the 10% hardest points we augment by 100%, while for models trained using
> the entire dataset we augment by 10%, thus guaranteeing the same amount of synthetic samples
> across all experiments. 

I am assuming the 100% refers to the size of the training set used for the generative model (10% of the original training set).

### Questions
1. The authors set aside a significant portion of data for hardness characterization. This does not seem ideal in a scenario where data augmentation is required since the additional data could be used for training the model instead. Do other hardness measures also require such hold-out sets?
2. Is there any downside to adding back the held out data together with the generated synthetic data when retraining the model? If not why wasn't this part of the experimental setup?
3. KNN assumes a distance metric over the input space. This is problematic for structured tabular data with mixed categorical and numerical features where a natural distance metric is not available and each feature can have different importances and scales. How was the distance chosen for KNN and how can the authors justify it?

### Soundness
1

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper proposes targeted synthetic data generation for tabular data using hardness characterization. It introduces a pipeline that focuses on generating synthetic data for the hardest points within the training dataset, as identified by a KNN Shapley-based hardness characterizer. The paper shows that augmenting only the hardest points improves out-of-sample performance and computational efficiency compared to non-targeted data augmentation approaches.

### Strengths
Originality: The idea of augmenting the hard samples is novel as is using KNN Shapley values to target hard samples for synthetic data generation is interesting as it differs from the different hardness characterization literature. Although see weaknesses below: neither in KNN shapley novel neither is targeted synthetic data generation.

Quality: The empirical quality is good and the methodology is rigorous and well-executed, with solid empirical benchmarks.

Clarity: The paper is well written and the clear details elucidate the problem and solution well.

Significance: Targeted synthetic data generation could be impactful in improving model robustness, particularly when data is scarce or of poor quality. So overall the problem seems important

### Weaknesses
There are three major weaknesses: Novelty, metrics and evaluation

Novelty:
- Use of KNN Shapley: the proposed approach to assess samples using KNN-Shapley isn’t novel, rather already proposed in Jia et al. (https://arxiv.org/abs/1911.07128). So while the application to synthetic data is novel, the proposed KNN-shapley assessment approach option itself is not novel. By itself this isn't an issue. But because the paper proposes to use an off-the-shelf valuation approach, it then warrants assessing why this is the best data valuation approach vs other alternative data valuation approaches (e.g. https://arxiv.org/pdf/2306.10577). Specifically, the paper should explore the sensitivity of the KNN parameter and provide a justification for its choice, as the quality of the Shapley values is directly impacted by the neighborhood definition. Furthermore, the computational cost of KNN-Shapley, especially on larger datasets, should be discussed and compared against other data valuation methods.

- Targeted synthetic data generation: The paper proposes KNN-shapley to do the targeting. However, the idea of using the targeted samples to condition synthetic generation also mirrors other works from data-centric literature (see https://arxiv.org/abs/2310.16981), which use the hardness ideas mentioned in the paper. It is important to contrast the different approaches in the related work for targeting synthetic data generation vs what's proposed in the paper --- both conceptually and empirically to understand strengths and weaknesses. The paper needs to clarify how its approach differs from simply oversampling hard examples, and whether the synthetic data adds any unique value beyond what could be achieved by re-weighting or oversampling the existing hard samples. A more detailed analysis of the synthetic data's characteristics compared to the original hard samples is needed to justify the complexity of the proposed approach.

Metrics:
- The paper shows the effect of the synthetic data in terms of performance and Gini scores. It is important when using synthetic data to also assess how the statistical fidelity is affected. i.e. is the synthetic data good statistically with respect to real data. It would improve the paper to assess fidelity metrics like KL-Divergence, MMD, Precision and Recall. The paper should also consider metrics that evaluate the diversity of the generated synthetic data, as simply replicating the same hard examples would not be beneficial. It is crucial to demonstrate that the synthetic data expands the feature space and does not just create copies of existing data points. The paper should also analyze the impact of the synthetic data on the feature distributions, and whether the synthetic data introduces any biases or artifacts.
- Examples of widely used synthetic data metrics (particularly fidelity) can be found in: (1) https://arxiv.org/abs/1806.00035, (2) https://arxiv.org/pdf/2406.13130v1, (3) https://arxiv.org/abs/2102.08921

Evaluation:
The assessment on the Amex dataset is interesting, however to claim generality of the findings a greater diversity of datasets should be explored, either across domains or with different properties (sample sizes, feature dimensionality). The paper should also consider evaluating the approach on datasets with varying degrees of class imbalance, as the effectiveness of targeted synthetic data generation might be different for balanced and imbalanced datasets. Furthermore, the paper should provide a more detailed analysis of the computational cost of the proposed approach, including the time required for hardness characterization, synthetic data generation, and model training. This is important for assessing the practical applicability of the proposed method.

### Questions
- Q1: As mentioned in the weaknesses how does the proposed approach to targeted synthetic data generation compare conceptually and empirically to: https://arxiv.org/abs/2310.16981

- Q2: How does the augmentation of only hard samples affect statistical fidelity?

- Q3: Would you say the findings are generalizable to any tabular dataset?

### Soundness
2

### Presentation
4

### Contribution
2
