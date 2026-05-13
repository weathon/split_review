# GMValuator: Similarity-based Data Valuation for Generative Models

- Decision: Accept
- Scores: 6, 6, 8, 6

## Abstract
Data valuation plays a crucial role in machine learning. Existing data valuation methods have primarily focused on discriminative models, neglecting generative models that have recently gained considerable attention.  
A very few existing attempts of data valuation method designed for deep generative models either concentrates on specific models or lacks robustness in their outcomes. Moreover, efficiency still reveals vulnerable shortcomings. To bridge the gaps, we formulate the data valuation problem in generative models from a similarity-matching perspective. Specifically, we introduce Generative Model Valuator (\textsc{GMValuator}), the first training-free and model-agnostic approach to provide data valuation for generation tasks. It empowers efficient data valuation through our innovatively similarity matching module, calibrates biased contribution by incorporating image quality assessment, and attributes credits to all training samples based on their contributions to the generated samples.  Additionally, we introduce four evaluation criteria for assessing data valuation methods in generative models, aligning with principles of plausibility and truthfulness. \textsc{GMValuator} is extensively evaluated on various datasets and generative architectures to demonstrate its effectiveness.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces GMVALUATOR to solve the data valuation problem for vision generative models, which is important yet has been overlooked by existing studies. GMVALUATOR formulates data valuation as a similarity-matching problem and incorporates image quality assessment to calibrate the contributions of data samples. Despite high computational complexity with large datasets, GMVALUATOR demonstrates effectiveness across multiple datasets and generative models, positioning it as a promising tool for data valuation in the field. Although the technical contribution is obvious, there is still much room for improvement in the author's presentation and content arrangement.

### Strengths
1.	The authors proposed GMVALUATOR to tackle the data valuation issue for generative models. GMVALUATOR is innovative, and model-agnostic, enabling broad applicability and adaptability across various generative models. Besides,  GMVALUATOR does not require retraining of models, offering the advantage in R&D scenarios with limited computational resources.
2.	The authors provide detailed theoretical justification for formulating data valuation for generative models as a similarity-matching problem. They also provide empirical validation for this motivation. This makes the GMVALUATOR being very reasonable.
3.	The authors demonstrated through extensive experimental results that the data valuation method proposed can achieve good results in multiple aspects and over multiple generative models. Besides, they also provided validation of the experimental settings and the open-source implementation, which further increased the credibility of the results.

### Weaknesses
1.	The manuscript is not well written. For example, in the Introduction, before talking about the existing work, it is suggested to generally define/introduce the data valuation problem (including the input and the objective). Moreover, the authors didn't highlight the urgent need for data valuation in existing generative models; this poses a challenge to the motivation of this paper. Most importantly, instead of briefly introducing the principle of the proposed GMValuator (such as why and how to formulate data valuation for generative models as an efficient similarity-matching problem), the author only introduces the goal to be achieved. These places make the content difficult to read.
2.	Although the authors claim that they proposed a versatile data valuation method for generative models, in both the problem formulation, method introduction, and subsequent experiments, they only evaluate it on image samples. Therefore, the statement "for generative models" may be inappropriate. Even though the authors mentioned in the Current Limitation "However, this does not mean that GMVALUATOR cannot be easily adapted to Natural Language Processing (NLP) fields, given its core idea of similarity matching." However, the reason for this statement may need further explanation.

### Questions
1.	As stated by the authors: However, this does not mean that GMVALUATOR cannot be easily adapted to Natural Language Processing (NLP) fields, given its core idea of similarity matching. So,  how to apply the proposed method to generative models for text-based data or data from multiple modalities?
2.	If data valuation is not used in training generative models, what will be the limitations? Can the proposed method or evaluation metrics measure the limitations?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper focuses on the data valuation of generative models. Existing data valuation methods designed for discriminative models cannot adapt to generative models due to 1) lack of robust performance metrics; 2) the large size of generative models; and 3) lack of data labels. In order to mitigate this gap, the authors propose GMValuator. GMValuator is based on similarity matching between training data and generated data. If a training sample is similar to a generated sample, it is considered to have contributed to the generated sample. The value of a training sample is computed by the quality of its contributed generations. Four evaluation criteria are introduced to assess data valuation. Experiments demonstrate the effectiveness of the proposed GMValuator.

### Strengths
- This is the first paper on data valuation on generative models. Previous data valuation methods focus on discriminative models and cannot adapt to generative models.
- Compared to the retraining-based and influence-based methods, GMValuator is efficient. It does not require any retraining or computation of hessian.
- GMValuator is effective on the proposed metrics. GMValuator has significantly improved compared to baseline methods.

### Weaknesses
 - For SOTA text-to-image models like stable diffusion, the image domain is much wider than the test models. As a result, a large number of generated images may be required for accurate data valuation. Meanwhile, generation with these models is slow. More results and ablation on stable diffusion on the SOTA text-to-image models would be helpful.
- While the proposed metrics are intuitively reasonable, it is coarse-grained and may not be able to reflect the effectiveness of data evaluation methods.

### Questions
Please refer ti weaknesses.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes a novel data valuation method for generative models. The authors introduce a model-agnostic, training-free data valuation framework, addressing a significant challenge in the field: existing methods typically require retraining or Hessian calculations, which are computationally intractable. In this approach, the contribution of a training data point to a generated data point is defined as inversely proportional to the distance between the two data points. The author performed extensive experiments against two baselines and showed effectivenss of the propsoed method.

### Strengths
- The paper introduces a novel and intuitive idea for data valuation in generative models, and the results are promising.
- The experiments are well-designed, exploring multiple distance functions and encoders to validate the approach. Also, multiple test scenarios were covered, all showing good supporting results for the proposed method.
- The paper is well-written and easy to follow, effectively conveying the methodology and findings.
- The paper covers relative literature well.

### Weaknesses
 - The impact of the quantization step on the final results is not explored. Understanding this effect would provide a clearer picture of the method’s performance.
- While section 2 introduces some underlying assumptions and a theoretical motivation for using a similarity-guided data valuation score (illustrated in Figure 1), the framework would benefit from a more rigorous theoretical foundation. Further studies on theoretical support could strengthen the framework’s conceptual grounding and its reliability across different applications.

### Questions
- What is the effect of the quantization step in the recall phase? 
- Empirically, how different is the proposed score from a nearest neighbor search with the rerank metric in the embedding space?
- How well does the proposed method generalize to other generative models, such as diffusion models?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
In this paper, the authors introduce Generative Model Valuator (GMVALUATOR), the first training-free and model-agnostic approach to providing data valuation for generation tasks. The authors formulate data valuation for generative models as an efficient similarity-matching problem. The paper further eliminates the biased contribution measurement by introducing image quality assessment for calibration. Also, the paper introduced four evaluation criteria for assessing data valuation methods in generative models.

### Strengths
The strengths of this paper are listed as the following:

1. GMVALUATOR is claimed to be the first modal-agnostic and retraining-free data valuation method for generative models.

2. The authors formulate data valuation for generative models as an efficient similarity-matching
 problem. The paper further eliminates the biased contribution measurement by introducing image
 quality assessment for calibration.

 3. The authors propose four evaluation methods to assess the truthfulness of data valuation and evaluate GMVALUATOR on different datasets, such as benchmark datasets and high-resolution
large-scale datasets, and various deep generative models to verify GMVALUATOR’s validity.

### Weaknesses
The weaknesses of the paper are listed as follows:

1. The paper only mentioned 4 criteria for assessing data valuation methods. They are: C1: Identical Class Test; C2: identical attributes test; C3: Out of Distribution Detection; and C4: Efficiency.  

How about other criteria? 
Why only use these 4? 

For example, how about Cost-Benefit Analysis (i.e., the trade-offs between the costs of acquiring or processing data versus the performance gains from using it in model training)?
Please give some examples and formulas to measure the costs of data acquisition/processing. Then compare them with the performance gains of those data in the context of generative model training. This will be more practical for the proposed new approach. 

2. The paper shall discuss the important aspects of data evaluation, such as accuracy and complexity. For example, how accurate is it for the proposed framework? How much is the complexity while implementing the proposed approach? Also, the authors shall discuss the proposed framework on accurately capturing the contributions of individual data points in various different scenarios. 

3. The paper shall illustrate other aspects such as scalability, whether the proposed approach is useful for handling big data in real-time applications.  For example, the authors can provide the results of testing the proposed method on progressively larger datasets or measuring processing times for different data sizes.

### Questions
GMVALUATOR is claimed as the first modal-agnostic and retraining-free data valuation method for generative models. How about the comparison with other approaches such as Information-Theoretic Measures (Akhilan Boopathy et al., ICML 2023, "Model-agnostic Measure of Generalization Difficulty"), etc.?
Please illustrate whether other approaches are applicable to generative models in a model-agnostic and retraining-free manner, which is important to your claim.

### Soundness
3

### Presentation
3

### Contribution
3
