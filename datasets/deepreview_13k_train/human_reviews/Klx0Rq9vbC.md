# Navigating Concept Drift and Temporal Shift: Distribution Shift Generalized Time-Series Forecasting

- Decision: Reject
- Scores: 3, 6, 3, 6, 5

## Abstract
Time-series forecasting finds broad applications in real-world scenarios. Due to the dynamic nature of time series data, it is crucial for time-series forecasting models to produce robust predictions under potential distribution shifts. In this paper, we initially identify two types of distribution shifts in time series: concept drift and temporal shift. We acknowledge that while existing studies primarily focus on addressing temporal shift issues in time series, designing proper concept drift methods for time series data received comparatively less attention.

Motivated by the need to mitigate potential concept drift issues in time-series forecasting, this work proposes a novel soft attention mechanism that effectively leverages and ensemble information from the horizon time series. Furthermore, recognizing that both concept drift and temporal shift could occur concurrently in time-series forecasting scenarios while an integrated solution remains missing, this paper introduces ShifTS, a model-agnostic framework seamlessly addressing both concept drift and temporal shift issues in time-series forecasting. Extensive experiments demonstrate the efficacy of ShifTS in consistently enhancing the forecasting accuracy of agnostic models across multiple datasets, and consistently outperforming existing concept drift, temporal shift, and combined baselines.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
The paper addresses the challenges of concept drift and temporal shift in time-series forecasting. The authors propose a model-agnostic framework called ShifTS, which integrates a soft attention mechanism (SAM) to handle concept drift and existing temporal shift mitigation techniques. The framework aims to enhance the generalization and forecasting accuracy of time-series models by addressing both types of distribution shifts simultaneously. Extensive experiments demonstrate that ShifTS outperforms existing methods across various datasets and models. However, the methods used to address concept drift lack sufficient persuasiveness, and the techniques for handling temporal shifts do not introduce significant innovation.

### Strengths
- The paper identifies and formulates the dual challenge of concept drift and temporal shift in time-series forecasting, which has been understudied in the literature.
- The use of extensive experiments across multiple datasets and models demonstrates the robustness and reliability of the proposed methods.
- The paper is well-structured .

### Weaknesses
 - The formula $\mathrm{P}(\mathbf{Y}^H)=\mathrm{P}(\mathbf{Y}^H|\mathbf{Y}^L)\mathrm{P}(\mathbf{Y}^L)\mathrm{P}(\mathbf{Y}^H|\mathbf{X}^L)\mathrm{P}(\mathbf{X}^L)$appears in Section 3.2.  However, it is not clear why this equality holds. A detailed derivation or explanation of the probabilistic relationships involved would enhance the clarity and understanding of the formula. Specifically, the equation seems to be incorrectly applying the law of total probability, as it appears to be multiplying conditional probabilities instead of summing over the possible values of the conditioning variables. The lack of justification for this equation undermines the theoretical foundation of the proposed approach.

- Figure 2 is very difficult to understand. It would be beneficial to provide a more detailed caption or a step-by-step explanation of the components and their interactions. Additionally, the term "Agg" appears in both Algorithm 1 and Figure 2 but is not defined or explained in the main text. Including a clear definition and explanation of "Agg" would improve the readability and coherence of the paper. The diagram lacks clear labels for the data flow and transformations, making it hard to follow the proposed method's steps. The role of each block and the specific operations performed within them are not sufficiently explained, hindering a thorough understanding of the framework.

- The soft attention mask  $M$ is introduced, but it is not clear how the attention mechanism is implemented. Meanwhile, it is mentioned that $M$ is independent of $\mathbf{X}^L$ and $\mathbf{Y}^L$ during testing. This raises the question of how $M$ can effectively address concept drift in test data. Please explain how $M$, which is independent of the lookback data, can still mitigate concept drift in the test data. The description of the attention mechanism lacks details on how the weights are calculated and updated during training. The claim that $M$ is independent of lookback data during testing is confusing, as it is unclear how the model can adapt to new patterns if the attention mask remains fixed.

- The paper aims to solve the problem of simultaneous temporal shift and concept drift in time-series forecasting. It is important to explain how the model handles the joint changes in both marginal and conditional distributions. Specifically, it should be clarified what distribution remains invariant and how the model learns to adapt to these changes. Given that handling both types of drifts is challenging even in traditional classification tasks, a detailed explanation of why and how the proposed method is effective in the time-series context would strengthen the paper. The paper does not clearly articulate the assumptions made about the nature of the drifts and how the proposed method addresses these specific types of changes.
- Besides performance metrics, additional evidence is needed to demonstrate how the soft attention mask 
$M$  specifically mitigates concept drift. The paper lacks a detailed analysis of the features selected by the attention mechanism and how these features relate to the concept drift. Visualizations or statistical analysis of the attention weights and the selected features would provide more convincing evidence of the method's effectiveness.

### Questions
Refer to weakness.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper addresses the challenge of distribution shifts in time-series forecasting, specifically focusing on concept drift and temporal shift. The authors identify two types of distribution shifts: concept drift, where the conditional distributions change over time, and temporal shift, where the marginal distributions change. They note that while existing studies primarily focus on temporal shifts, concept drift in time-series data has received less attention. To mitigate concept drift, the paper introduces a novel soft attention mechanism called soft attention masking (SAM). SAM leverages exogenous information from the horizon window to weigh and ensemble time series at multiple horizon time steps, enhancing the model's generalization ability. For addressing both concept drift and temporal shift, the authors propose ShifTS, a model-agnostic framework that integrates SAM with established temporal shift mitigation techniques.

### Strengths
1. The proposed soft attention masking (SAM) looks interesting. It leverages exogenous information to mitigate concept drift by weighing and ensembling time series at multiple horizon time steps.
2. The proposed ShifTS also looks interesting to me. As a model-agnostic framework, it combines various methodologies effectively, resulting in a robust solution.
3. The proposed method is evaluated on 6 series datasets in comparison with several baselines.

### Weaknesses
1. In general, this paper presents how an algorithm works, but lacks in-depth explanation why it works.
2. I am very interested to see how the proposed algorithm works on noisy datasets.

### Questions
1. How does the performance of ShifTS vary across different types of time-series data, especially those with high noise levels or irregular patterns? I highly recommend to add some experiments on this.
2. Is there any plan to explore the application of ShifTS in real-time or online forecasting scenarios, where the model continuously updates with incoming data?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper presents a generalized solution for (univariate) time-series forecasting with considerations of both concept drift and temporal shift. The idea of introducing concept drift to time series forecasting is interesting. The authors have clearly presented the main idea of the proposed framework, aka, ShifTS, with comprehensive experiments of adapting this framework to recent time series methodologies.

### Strengths
The idea of proposing a generalized framework for time series forecasting is both interesting and inspiring. 

The framework itself is well-conceived and is supported by robust experimental validation. 

Additionally, the writing is clear and well-organized, making the work accessible and easy to follow.

### Weaknesses
Although it is interesting to propose a generalised framework that can handle both temporal shift and concept drift, the proposed solution of how they are combined lacks novelty, neither with in-depth insights into these different distributional changes. That is to say, I can understand why this framework works very well, but from my perspective, its potential to inspire further research is somewhat limited. This, combined with the fact that this is not the first study to introduce concept drift in the time series forecasting domain, largely informs my overall evaluation of this submission.

Referring to your definitions:

Definition 3.1 (Temporal Shift (Shimodaira, 2000; Du et al., 2021))
Temporal shift (also known as virtual shift (Tsymbal, 2004)) refers to changes in the marginal probability distributions over time, while the conditional distributions remain the same.

Definition 3.2 (Concept Drift (Gama et al., 2014; Lu et al., 2018))
Concept drift refers to changes in the conditional distributions over time, while the marginal probability distributions remain the same.

Let's take the definition of concept drift from Gama et al., 2014 here:
In their equation (2), "Formally, concept drift between time point t0 and time point t1 can be defined as ∃X: pt0 (X, y)= pt1 (X, y)" which is defined on the joined distribution rather than just the changes in the conditional distributions over time.

This means that if you’re using this definition, it inherently covers changes in marginal probability distributions over time—essentially encompassing what you defined as temporal shift. This overlap is also acknowledged in your mention of “Temporal shift (also known as virtual shift (Tsymbal, 2004)),” with Tsymbal’s work (2004) being a notable study in the concept drift domain.

Therefore, the problem setting and definitions require major revision to ensure rigor, which does not meet the ICLR standards for acceptance.

### Questions
Referring to your definitions:

Definition 3.1 (Temporal Shift (Shimodaira, 2000; Du et al., 2021))
Temporal shift (also known as virtual shift (Tsymbal, 2004)) refers to changes in the marginal probability distributions over time, while the conditional distributions remain the same.

Definition 3.2 (Concept Drift (Gama et al., 2014; Lu et al., 2018))
Concept drift refers to changes in the conditional distributions over time, while the marginal probability distributions remain the same.

Let's take the definition of concept drift from Gama et al., 2014 here:
In their equation (2), "Formally, concept drift between time point t0 and time point t1 can be defined as ∃X: pt0 (X, y)= pt1 (X, y)" which is defined on the joined distribution rather than just the changes in the conditional distributions over time.

This means that if you’re using this definition, it inherently covers changes in marginal probability distributions over time—essentially encompassing what you defined as temporal shift. This overlap is also acknowledged in your mention of “Temporal shift (also known as virtual shift (Tsymbal, 2004)),” with Tsymbal’s work (2004) being a notable study in the concept drift domain.

Therefore, the problem setting and definitions require major revision to ensure rigor, which does not meet the ICLR standards for acceptance.

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
4

### Summary
This paper introduces ShifTS, a framework that addresses both concept drift and temporal shift issues in time-series forecasting. (1) The work presents a novel soft attention mechanism (SAM) for concept drift and integrates it with temporal shift mitigation techniques. (2) demonstrates substantial empirical improvements across diverse settings, and (3) provides a practical, model-agnostic solution to an important problem in time-series forecasting.

### Strengths
1. The SAM mechanism effectively leverages horizon information to mitigate concept drift
The framework successfully combines concept drift and temporal shift solutions in a principled way
2. Comprehensive experiments across six datasets show consistent improvements
    1. Performance gains are substantial: up to 81.9% on ILI and 71.4% on ETTh2 (Table 1)
    2. Results hold across multiple state-of-the-art models, demonstrating generalizability
    3. Ablation studies clearly demonstrate the value of addressing both types of shifts
3. Model-agnostic design enables broad applicability (Implementation is straightforward with minimal to no hyperparameter tuning required)
4. The comparison against other distribution shift methods (Table 2) demonstrates superior performance
5. The theoretical framework linking concept drift to insufficient determination by X_L is well-motivated
6. The paper addresses a significant gap in time-series forecasting by tackling both concept drift and temporal shift

### Weaknesses
 1. Section 4.3 on "MITIGATING TEMPORAL SHIFT" lacks novelty:
    1. Simply restates RevIN equations (4 and 5) without adding new insights
    2. It should be significantly condensed or moved to background/preliminaries, as currently, it merely applies the existing RevIN method.
    3. It takes space that could be better used to explain novel contributions
2. Practical feasibility concerns with exogenous feature forecasting:
    1. The paper proposes forecasting X̂_SUR to support target series prediction
    2. This assumes we can accurately forecast exogenous features, which may be as hard as the original problem. No clear justification for why forecasting exogenous features would be more reliable than direct target forecasting. The surrogate loss (equation 3) doesn't guarantee accurate exogenous forecasts.
    3. The method likely works on the benchmark datasets primarily because X itself has limited concept drift in chosen long-term benchmarking datasets (Limited dataset diversity (ILI, Exchange, ETT share similar characteristics). Success may not generalize to scenarios with significant concept drift in exogenous features themselves. 
    4. Consider synthetic experiments with controlled concept drift in X.
3. The performance gains of ShifTS over baseline methods lack convincing statistical validation:
    1. Performance differences between ShifTS and baseline methods in Table 2 are inconsistent and often marginal (e.g., on ETTh1: ShifTS MSE 0.076 vs FOIL 0.081 vs RevIN 0.085, and on ETTh2: ShifTS 0.194 vs SAN 0.199 vs N-S Trans 0.203), with no statistical significance testing or variance reporting across seeds to validate these small improvements. 
    2. ShifTS's gains over strong baselines like SAN and FOIL appear dataset-dependent, and the margins are small enough to question statistical significance—especially noticeable on Exchange, where temporal shift methods perform comparably (ShifTS 0.470 vs SAN 0.415) and ShifTS+SAN (0.407) perform better than ShifTS alone. 
    3. Without proper variance reporting across different model seeds, it's difficult to conclude if ShifTS truly outperforms existing methods or if the improvements (often 2-5% range) fall within standard deviation ranges of multiple training runs
4. The choice of sparsity regularization in equation (2) needs better motivation
5. The mutual information analysis (Figure 3a) could benefit from more rigorous statistical validation beyond the p-value.

### Questions
1. Statistical Validation:
    1. Could you provide variance analysis across different random seeds and training runs, especially for the marginal improvements (2-5%) shown in Table 2?
    2. How do you justify the statistical significance of improvements over baselines like SAN and FOIL given the small margins?
2. How does ShifTS handle scenarios where exogenous features themselves exhibit strong concept drift? Can you provide empirical evidence showing why forecasting X̂_SUR is more reliable than direct target forecasting? How do poor exogenous feature forecasts impact the final prediction quality?
3. Why were only transformer-based models used despite claims of model-agnosticism?
4. Could you explain how the chosen datasets (ILI, Exchange, ETT) represent different types of concept drift?
5. Why does ShifTS+SAN outperform ShifTS alone on the Exchange dataset? Does this suggest limitations in your approach?

### Soundness
2

### Presentation
4

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper studies the problem of concept drifts and temporal shifts in the time-series forecasting tasks. To address the two problems, the algorithm, namely SHIFTS, is proposed. On one hand, SHIFTS puts forward the idea of SAM to address the concept drift problem. On the other hand, the problem of temporal shifts is combatted by the concept of ReIN,

### Strengths
1) The problems of concept drifts and temporal shifts are rarely considered in the time-series forecasting works. 
2) the problem of time-series forecasting is important and has real-world relevance.

### Weaknesses
Literature Survey

literature survey of time-series forecasting is not rigorous. please include recent works listed below:

- FRNet: Frequency-based Rotation Network for Long-term Time Series Forecasting
- Fredformer: Frequency Debiased Transformer for Time Series Forecasting

Novelty

Novelty is rather limited because the temporal shift is addressed using ReIN. Can you clarify whether you have any modification to the vanilla ReIN method?

Experiments

1) please analyze whether the datasets themselves contain the concept drifts and the temporal shifts.
2) what is the time-series model that you used? what are the time-series models that the baseline algorithms used?
3) There are newer baselines for time-series forecasting. please compare your algorithm with them.

Conclusion

There is no limitation mentioned in the conclusion section.

### Questions
1) what are d_{x} and d_{y}? they are used before being defined.

2) what is the time-series model that you used? what are the time-series models that the baseline algorithms used?

3) can you confirm that the concept drift and the temporal shift are present in the dataset used in this study?

### Soundness
3

### Presentation
2

### Contribution
2
