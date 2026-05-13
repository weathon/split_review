# Rethinking the Temporal Modeling for Time Series Forecasting with Hybrid Modeling

- Decision: Reject
- Scores: 6, 6, 5

## Abstract
Time series forecasting is a critical task in various domains, including traffic, energy, and weather series forecasting. Recent research has explored the utilization of MLPs, Transformers, and CNNs architectures for time series modeling, delivering promising results. In this work, we take a step further by systematically studying the strengths and limitations of these methods and integrating their capabilities to formulate a unified framework for time series forecasting with a hybrid modeling approach. We introduce UniTS, a simple yet scalable framework for temporal modeling that incorporates multiple feature learning techniques. Moreover, prior research employed different hyperparameter configurations in various temporal modeling approaches, which might causing unfair performance comparisons. For instance, when predicting with the same forecasting horizon, prior approaches might exhibit significant variations in lookback window lengths.  In our study, we address this issue by validating and standardizing parameters that can significantly impact performance, ensuring a more equitable comparison of models across diverse datasets. UniTS achieves state-of-the-art performance across various domains, and we conduct extensive experiments to further evaluate its capabilities. Our results are fully reproducible, and the source code for this work is available at https://anonymous.4open.science/r/UniTS-8DA8/README.md.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes to combine different models for the long-term time series forecasting in a framework "UniTS", in which Convolutional Neural Network is used to extract local feature and MLP (or Transformer) is used to extract global feature. In addition, this paper points out the unfair comparison issue in existing works due to the lack of standardized parameter design. Experiments on the 8 benchmark datasets are conducted to evaluate the proposal.

### Strengths
This paper uses the advantages of different models and combines them in a framework for a better long-term time series forecasting. This paper also points out the unfair comparison issue in existing works due to the lack of standardized parameter design.

### Weaknesses
1. Some parts of the proposal UniTS are not introduced clearly. e.g.,

What are the meanings of H^{l,N} and H^{g,N} in Figure 1?

How to do the LFE and GFE after Patching?

What is the meaning of j and what is the Decompose in the first equation of section 3.2.3?

2.  The RLinear and RMLP models in the following reference outperform PatchTST on some datasets. It is better to compare with them as well.

Li, Zhe, et al. "Revisiting Long-term Time Series Forecasting: An Investigation on Linear Mapping." arXiv preprint arXiv:2305.10721 (2023).

3. I think it is unfair to compare with PatchTST/64 which uses lookback window length 512 only. As shown in the Figure 2 of the PatchTST paper, the performance is also changed with different lookback windows. It is better to choose the best results from different lookback windows for PatchTST as well, since this paper highlights the unfair comparison issue.

4. The hyperparameter selection (including learning rate, hidden size, e.t.c. besides the use of lookback window length) is only used for the proposed UniTS but not for other baselines. I am doubting whether it results in another unfair comparison problem.

5. There is no complexity analysis, especially, the complexity introduced by the hyperparameter selection.

Typos:
"four primary categories" in Page 1 -> "three primary categories"

"Table 1 provides a overaTidell view analysis" in Page 6 -> "Table 1 provides a overall view analysis"

V_i is not used before explaining it in Page 8.

### Questions
Same to the Weaknesses.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Propose a long-range forecasting model for multivariate time-series using hybrid aprroach through local and global feature extraction mechanism. Their global feature mechanism leverage more like transformer like architecture and local is CNN architecture. The model adapts for input pre-precessing though instance normalization, patching, and decomposition.

### Strengths
1. Model Outperforms the baselines in terms of MSE, MAE score. Experiments are done in multiple public datasets including ILI, electricity, weather, traffic,etc.

2. In terms of long-range forecasting range, model outperforms with prediction length upto 60 compared to the transformer architecture and upto 720 compared to the 2nd best performing model PatchTST.

3. Authors showed an extensive ablation analysis showing usefulness of leveraging different modules (local LFE, global GFE, attention, PE, IN, etc) in the hybrid approach.

4. Paper is well-written with convincing experiments.

### Weaknesses
1. Is there any particular reason to not compare this model with the state-of-the-art long-range forecasting model like Spacetimeformer (Grigsby et al. 2023), and NBeats. Both models perform vey well for long range forecasting on multivariate data. SpaceTimeFormer paper shows result for prediction length upto 672 (on some weather data).

2. LFE and GFE architeture are not very novel, and mostly adapted from state-of-the-arts.

### Questions
1. Is there a reason why patchTST working so much better than transformer achitetures like AutoFormer/Fedformer, especially, where the ablation studies clearly show attention, PE mechanisms are useful?
2. Can you show the results compared to SpaceTimeFormer and Nbeats? SpaceTimeformer model also has local+global architeture approach.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a hybrid model that utilizes multiple structures for improved time series forecasting, demonstrating strong performance across various datasets.

### Strengths
1.This paper conducts comprehensive ablation experiments, analyzing the role of each module in the model. This demonstrates the importance of a multiscale hybrid model in the field of time series prediction.
2.The article provides open-source code, facilitating the reproducibility of experimental results.
3.It thoroughly compares different parameter search methods and the impact of various hyperparameter choices on the model's predictive performance.

### Weaknesses
1.This paper lacks innovativeness, merely combining currently high-performing models without introducing novel elements. The proposed model appears to draw heavily from existing model structures, with limited originality in its design. While the work effectively combines and leverages existing approaches, it lacks a significant level of novelty in terms of introducing truly innovative components.

2.This paper does not provide sufficiently convincing reasons for the selection of these modules. The justification for choosing specific modules over alternatives is weak, lacking a rigorous analysis of why these particular components are optimal for the task. For instance, the paper does not explore the potential benefits of other established time series forecasting modules, nor does it provide a detailed comparison of the selected modules against these alternatives. A more thorough discussion of the design choices, including a comparison with other potential modules and a clear rationale for the final selection, is needed.

### Questions
see my concerns

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
