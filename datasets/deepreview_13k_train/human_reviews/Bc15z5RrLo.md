# MixNAM: Advancing Neural Additive Models with Mixture of Experts

- Decision: Reject
- Scores: 3, 6, 6, 3

## Abstract
Additive models, such as Neural Additive Models (NAMs), are recognized for their transparency, providing clear insights into the impact of individual features on outcomes. However, they traditionally rely on point estimations and are constrained by their additive nature, limiting their ability to capture the complexity and variability inherent in real-world data. This variability often presents as different influences from the same feature value in various samples, adding complexity to prediction models. To address these limitations, we introduce MixNAM, an innovative framework that enriches NAMs by integrating a mixture of experts, where each expert encodes a different aspect of this variability in predictions from each feature. This integration allows MixNAM to capture the variability in feature contributions through comprehensive distribution estimations and to include feature interactions during expert routing, thus significantly boosting performance. Our empirical evaluation demonstrates that MixNAM surpasses traditional additive models in performance and is comparable to complex black-box approaches. Additionally, it improves the depth and comprehensiveness of feature attribution, setting a new benchmark for balancing interpretability with performance in machine learning. Moreover, the flexibility in MixNAM configuration facilitates the navigation of its trade-offs between accuracy and interpretability, enhancing adaptability to various data scenarios.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
Additive models like Neural Additive Models (NAMs) are valued for their transparency, clearly showing how individual features impact outcomes. However, their reliance on point estimates and additive structure limits their ability to capture complex, variable feature influences in real-world data. To address these limitations, MixNAM is introduced as a framework that enriches NAMs through a mixture of experts, each capturing different aspects of feature variability. This approach allows MixNAM to model diverse feature contributions, and interactions, and allow distribution estimations. Empirical results show that MixNAM not only outperforms traditional additive models but also approaches the performance of complex black-box methods while providing detailed feature attributions. Its flexible configuration further allows for balancing accuracy and interpretability, adapting to various data scenarios effectively.

### Strengths
- Overall, the paper is clear and well-written.
- The paper attempts to contribute to the important and relevant topic of uncertainty quantification in neural additive models with mixtures of experts
- The proposed method is evaluated on both simulated and real-world data, using multiple criteria, including model additivity, bound tightness, and prediction accuracy.

### Weaknesses
 * The discussion on related work lacks clarity. For instance, the authors state that "these approaches are still limited by their inevitable assumptions of prior distributions and the additive nature of the entire models, which restrict their ability to accurately reflect complex underlying distributions and interactions." However, it is unclear what is meant by "prior distributions." Why can’t these models capture interactions effectively? Why are they considered less flexible? Additionally, the authors mention that "these models generally rely on a simplistic assumption about output distributions." More specific details are needed to understand the limitations that the proposed approach aims to address.

* The type of uncertainty or variability captured by the proposed method is not clearly defined. The authors use various terms, such as "different aspect of the variability," "more comprehensive insight into the output distribution," "captures a broad range of possible outcomes," "detailed variance," and "more comprehensive insight into the output distribution." However, this language lacks rigor and does not clearly communicate the specific type of uncertainty intended to be captured. Furthermore, in a regression context where \(L\) represents the MSE, it is unclear how the proposed method would capture "uncertainty" by minimizing MSE (instead of proper scoring rules).

* Although the authors consider different values for \(K\) and \(C\) in Table 8 in the appendix, the roles of these hyperparameters are not well explained. The results appear relatively consistent, and the impact of using a single expert is missing from the analysis. Additionally, there is no study of the values for \(\gamma\) and \(\lambda\) in equation (8), particularly with extreme values (gamma = 0).

* As demonstrated by the authors in Appendix E, the proposed method can essentially be viewed as a generalized additive model with specific normalization. The added complexity in the approach is not well justified when compared to existing methods.

* Only six relatively "old" datasets are used in this study. A broader selection of available tabular datasets would provide a stronger and more comprehensive evaluation. Refer to Léo Grinsztajn et al. “Why do tree-based models still outperform deep learning on tabular data?” (July 2022) and Pieter Gijsbers et al. “An Open Source AutoML Benchmark” (July 2019) for relevant data sources.

* The authors write, "The bounds represent the maximum and minimum potential outputs for a feature." It would be helpful to clarify what is meant by "possible" in this context. Possible according to what criteria? These bounds are directly affected by the number of experts. How is that important?


Additional Comments

* In expression (12), the denominator equals zero.
* In Figure 4, why is NAM unable to capture multimodality? Were proper hyperparameters used?
* Please clearly indicate what the values after the +/- symbol represent (standard errors?).
* Label the y-axis in Figure 3 for clarity.

### Questions
See weaknesses.

### Soundness
2

### Presentation
3

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
The paper introduces MixNAM, an extension of Neural Additive Models (NAMs) designed to enhance both accuracy and interpretability. MixNAM incorporates a mixture of experts, each capturing different aspects of feature variability, to address the limitations of traditional NAMs, which struggle to represent complex data patterns. Experiments show that MixNAM improves accuracy over traditional additive models while achieving performance comparable to black-box models, achieving a balance between interpretability and predictive power.

### Strengths
- The paper introduce MoE within the NAM framework to overcoming the limitations of traditional additive models. This architecture allows MixNAM to capture data complexity more effectively than NAMs.
- The paper includes experiments across various datasets, including both real-world and simulation data, to demonstrate MixNAM's improved accuracy and interpretability compared to both traditional additive models and more complex black-box approaches.

### Weaknesses
 - Although MixNAM achieves interpretability with improved accuracy, it relies on a dynamic routing mechanism and multiple experts, which might increase computational requirements.  It would be better to include analysis of computational cost and assess the tradeoff of the computational cost and the increased accuracy.
- The paper primarily focuses on tabular data, which raises questions about the generalizability of the framework’s effectiveness to other domains, such as image or text data. The interpretability of additive models relies on the ability to visualize feature contributions through shape plots, which are difficult to define for raw image or text data. The paper should discuss how the interpretability of MixNAM would be maintained in non-tabular data, or acknowledge this limitation.

### Questions
- For datasets with highly sparse features, does the routing mechanism maintain its efficiency, or does it introduce sparsity issues that affect performance?
- The simulation study includes only two random variables. Could the study include more experiments on high dimensional variables to better demonstrate MixNAM's effectiveness?
- How does MixNAM handle extreme cases of feature variability, where the impact of a feature varies widely across different samples?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces MixNAM which improves neural additive model (NAMs) by combining with a mixture of experts (MoE) to capture the feature variability due to its interaction with other features. MixNAM uses multiple experts for each feature and uses a dynamic routing mechanism to assess and combine the relevance of different experts. This improves the prediction performance and gives the upper and lower bound of the feature attribution. The empirical evaluation demonstrates that MixNAM outperforms traditional additive models that ignore interactions and achieves comparable performance to complex black-box models while providing feature attributions.

### Strengths
1. The idea of combining MoE with NAM is novel and can improve the flexibility of NAM to capture feature interactions and maintain interpretability. The claim is supported by extensive experiments and benchmarks against various baselines, in terms of prediction performance and interpretability.

2. MixNAM provides a point estimator of feature attribution but a range of it, which reflects the feature interaction.

### Weaknesses
1. If we look at Table 1, MixNAM is only significantly better than other interpretable methods (with FA) on the Housing and Year dataset by taking the standard error into consideration. 

2. The model is benchmarked only on tabular datasets due to the limited flexibility of NAM on structured datasets, even though it's still beneficial to discuss its potential usage on structured datasets, as they are the primary use cases of neural networks.

3. The performance and interoperability of MixNAM are sensitive to the penalty parameter \lambda. The paper would benefit from a more in-depth discussion on how to choose it.

### Questions
1. How was the hyper-parameter \lambda selected? Was it cross-validated against prediction accuracy? It would be great to provide some heuristics to select it to balance the accuracy and interpretability.

2. It would be great to compare the interpretation of MixNAM with any post-hoc feature attribution (e.g., SHAP) on XGBoost, which is a popular choice to gain interpretability on tabular data. What is the difference between these two options? A practitioner may like to know when they should use an interpretable MixNAM and when they should use XGBoost with post-hoc interpretation methods.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces an enhancement to Neural Additive Models (NAMs) by incorporating a Mixture of Experts (MoE) framework, enabling the model to capture feature variability and complex feature interactions. This approach allows each feature to be modeled through multiple expert predictions, which are dynamically selected based on relevance, thus addressing traditional NAM limitations in handling real-world data complexity. This new framework enhances additive models' utility, offering advanced predictive accuracy and transparency.

### Strengths
1. The paper combines NAMs’ interpretability with MoE’s capacity for multi-aspect feature representation, contributing a new approach to interpretable machine learning.

2. MixNAM’s ability to capture variability in feature impacts is highly relevant for real-world applications that require transparent models with high predictive power. The proposed method also allows users to balance accuracy with interpretability.

### Weaknesses
1. As described in line 164, each expert $E_{ik}$ is implemented as a linear layer, but normally, MLPs are used as base models for experts, the authors should justify why choosing linear model as experts. While parameter sharing is mentioned, the choice of a linear layer as the expert itself is still questionable. The capacity of a linear layer to capture complex, non-linear relationships within the feature space is limited, which is a primary motivation for using MoE in the first place. The authors should provide a more detailed analysis of the impact of this design choice on the model's ability to capture feature variability.

2. The novelty of this paper is quite limited, as they just apply regular MoE architecture on top of each feature's embedding and weighted combine them to obtain the outputs, even so, the authors did not provide a detailed rationale for choosing such a method. The application of MoE to additive models, while potentially useful, lacks a strong theoretical justification. The authors should elaborate on why this specific combination is expected to yield superior results compared to other potential approaches. A more thorough discussion of the theoretical underpinnings of this method is needed.

3. In line 336, it seems that the uncertainty intervals are formulated by a group of expert predictions, this is not a natural way of producing prediction intervals, as the uncertainty should come from the model parameters or the data itself. The interpretation of variability as a measure of feature interaction is unconventional. The authors need to clarify how this variability measure relates to standard uncertainty quantification methods and justify why this specific definition is appropriate for the problem at hand. The lack of connection to established uncertainty quantification techniques is a significant weakness.

4. The multimodal experiments are all based on small-scale simulated datasets, the authors should benchmark its method on larger-scale multimodal benchmarks. The use of only small-scale simulated data limits the generalizability of the findings. The authors should demonstrate the effectiveness of their method on real-world datasets with multimodal characteristics to validate its practical applicability.

### Questions
How does the proposed method handle load imbalance when training MoE models? Is the expert variation penalty similar to the load imbalance loss function?

### Soundness
2

### Presentation
3

### Contribution
1
