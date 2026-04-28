# Polyrating: A Cost-Effective and Bias-Aware Rating System for LLM Evaluation

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 8, 6

## Abstract
Rating-based human evaluation has become an essential tool to accurately evaluate the impressive performance of large language models (LLMs). However, current rating systems suffer from several important limitations: first, they fail to account for biases that significantly influence evaluation results, second, they require large and expensive preference datasets to obtain accurate ratings, and third, they do not facilitate meaningful comparisons of model ratings across different tasks. To address these issues, we introduce \tool, an expressive and flexible rating system based on maximum a posteriori estimation that enables a more nuanced and thorough analysis of model performance at lower costs. \tool can detect and quantify biases affecting human preferences, ensuring fairer model comparisons. Further, \tool can reduce the cost of human evaluations by up to $41\%$ for new models and up to $77\%$ for new tasks by leveraging existing benchmark scores. Lastly, \tool enables direct comparisons of ratings across different tasks, providing a comprehensive understanding of an LLMs' strengths, weaknesses, and relative performance across different applications.
    \footnote{Code available in supplementary material.}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors propose, POLYRATING, an large language model evaluation system. POLYRATING can detect and quantify biases that affect human preferences, improve sample efficiency, reduce evaluation costs, and enable cross-task model scoring comparisons. It achieves a significant improvement on the sample efficiency, reducing the cost of human evaluation by up to 77% for new tasks and 41% for new models.

### Strengths
- POLYRATING is a multivariate rating system that can detect and quantify biases affecting human and LLM-based evaluations of LLMs.
- Such effective system reduces the cost of human evaluation by up to 77% for new tasks and 41% for new models, which is meaningful and practical in the real-world applications.
- The paper is easy to follow.
- Comprehensive experiments are conducted, demonstrating the effectiveness of the proposed method.

### Weaknesses
Null

### Questions
Will POLYRATING also be appliable to other domains that use large language models, such as computer vision, information retrieval, etc.? How is the cost for the adaptation to these domains?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper addressed that current rating systems for LLMs suffer from several limitations: biases, human annotations, and shift-invariance.\
Then, the authors propose POLYRATING, a multivariate rating system based on MAP estimation.\
POLYRATING uses maximum a posteriori estimation (MAP) to estimate model ratings across tasks, including base ratings and task-specific adjustments.\
It also incorporates shared parameters to model factors like answer length and readability that affect preferences.

### Strengths
1. The notations and equations throughout the paper are clear, well-formulated, and add rigor to the methodology.
2. The justification for POLYRATING is robust, with a well-explained rationale for the multivariate approach.
3. Extensive experiments demonstrate the effectiveness of POLYRATING, showing its superiority over traditional rating methods in several key areas.

### Weaknesses
1. The modeling features are somewhat ambiguous; it is unclear which specific features are applied for each task, or the criteria used for feature selection. More detailed information on feature selection per task would be helpful. For instance, while readability is mentioned, the specific implementation of the Flesch Reading Ease score and its potential limitations are not discussed. Furthermore, it's not clear how features are normalized or if any feature interaction terms are considered. The paper lacks a discussion on the potential for multicollinearity among the selected features and how this might affect the stability and interpretability of the model.
2. POLYRATING employs both model-shared and model-specific weights. It would be useful to clarify how the system initializes weights for newly added models and whether it can efficiently update ratings for new models without requiring a full retraining of the rating system. The paper does not specify the optimization algorithm used for MAP estimation, nor does it discuss the convergence properties of the algorithm, especially when new models are added. The computational cost of updating the model with new models or preferences is also not addressed, which is important for practical applications.

### Questions
Please refer to Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces Polyrating, a novel multivariate rating system designed specifically for evaluating Large Language Models (LLMs). The system addresses three key limitations of current rating approaches: bias awareness, cost efficiency and cross-task comparability. Polyrating uses maximum a posteriori estimation with shared parameters to quantify and account for various biases in human and LLM-based evaluations. The system demonstrates up to 77% cost reduction for new tasks and 41% for new models by leveraging existing benchmark scores. It also enables direct rating comparisons across different tasks by solving the shift-invariance problem inherent in traditional rating systems. The paper provides thorough empirical validation using public datasets like Chatbot Arena and theoretical proofs of the system's optimality.

### Strengths
1. The paper makes good practical contributions by introducing a novel framework for LLM evaluation. Fundamental limitations in current approaches are well addressed, providing strong theoretical foundations with proper convergence guarantees and demonstrating substantial practical improvements.
2. The authors present comprehensive empirical validation across multiple datasets with comparison against baseline approaches and clear ablation studies showing the contribution of each component.
3. The significant practical impact demonstrated (up to 77% cost reduction for new tasks and 41% for new models by leveraging existing benchmark scores) offers immediate positive value to the field.
4. The paper is generally well written with clear problem motivation and logical flow from theory to implementation to results.

### Weaknesses
1. There is limited discussion of computational complexity and scalability analysis. The paper could include runtime analysis for both training and inference phases of Polyrating, and recommended batch sizes and optimization strategies for large-scale deployment. Similarly, a short discussion of how the MAP optimization scales with number of models (k), tasks (d) and samples (n) would be useful.

2. The hyperparameter selection process for standard deviations sigma_j and sigma_j' could be better explained. The relationship between dataset size and optimal prior values should be analyzed and sensitivity analysis showing how different prior choices affect final ratings would also be valuable.

3. The system assumes static model capabilities but the paper should address rapid model changes with, eg: analysis of rating stability over time, methods for updating ratings incrementally as new data arrives, guidelines for maintaining rating consistency across model versions, etc.

4. The paper doesn't explore well on how the system performs with extremely sparse preference data (cold-start scenarios). The authors could analyze the minimum number of preferences needed per task/model pair. Also, methods for handling completely missing task-model combinations should be detailed.

### Questions
1. What is the computational complexity of the optimization process and how does it scale with the number of models and tasks?
2. How sensitive is the system to the choice of priors? Could you provide guidelines for selecting appropriate priors?
3. How does the system handle rapid changes in model capabilities over time?
4. How does the system handle extremely sparse preference data for new tasks or models?

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This manuscript introduces Polyrating, a multivariate rating system for evaluating Large Language Models (LLMs). The authors aim to address several key challenges in current LLM evaluation methods, including accounting for biases, reducing the cost of human evaluations, and enabling meaningful comparisons of model performance across different tasks. Polyrating uses maximum a posteriori (MAP) estimation to incorporate different tasks and biases into the rating process. Experiments are conducted on publicly available human preference data to demonstrate the effectiveness of the proposed system.

### Strengths
1. The authors clearly identify important limitations in existing LLM evaluation approaches, specifically focusing on the influence of biases, the high cost of human evaluation, and the lack of comparability across tasks. The proposed Polyrating is designed to directly address these challenges, providing a clear motivation for the work.

2. The manuscript provides a theoretical analysis of Polyrating, demonstrating its convergence properties. This provides a strong theoretical foundation for the proposed system and strengthens the confidence in its practical applicability.

### Weaknesses
1. The manuscript lacks a comparison with existing multivariate rating systems. Empirical comparison and discussion of adaptations for LLMs are needed.

2. Experimental evidence to support some of the claimed benefits of Polyrating, is insufficient. Model selection for task comparability is questionable. The efficiency analysis lacks clarity on calculation methods.

### Questions
1. Line 233: Why are different optimization methods (Newton's method and L-BFGS) used for different parameters? What's the rationale?

2. How are sample efficiency improvements (e.g., "38%" in line 361) calculated?

3. In Table 2 and 3, several models are chosen to illustrate the differences in task comparability between Polyrating and a unidimensional approach. The following questions arise:

3-1: Line 410: What specifically makes Mixtral's performance "very different"? The tables don't clearly show this. Providing a more precise explanation or visualization of these differences is necessary to support this claim.

3-2: Line 413: The Chinese task analysis uses proprietary models with undisclosed training details and the Mixtral model, which, due to its specific role in the Chatbot Arena setup, is not suitable for this comparison. Please consider revising the experimental setup to enhance the validity of the comparisons.

4. While existing multivariate rating systems are mentioned, their performance isn't compared to Polyrating. Include empirical comparisons and highlight performance differences would significantly strengthen the manuscript.

### Soundness
3

### Presentation
2

### Contribution
2
