# Feature Discrimination Analysis for Binary and Ternary Quantization

- Decision: Reject
- Scores: 8, 5, 5

## Abstract
In machine learning, quantization is widely used to  simplify data representation and facilitate algorithm deployment on hardware. Considering the fundamental role of classification in machine learning, it is imperative to investigate the impact of quantization on classification.  Current research primarily revolves around quantization errors, under the assumption   that  higher quantization errors generally lead to lower classification performance. However, this assumption lacks a solid  theoretical foundation, and often contradicts empirical findings. For instance, some  extremely low bit-width quantization methods, such as  $\{0,1\}$-binary quantization and $\{0, \pm1\}$-ternary quantization,  can achieve comparable or even superior classification accuracy compared to the original non-quantized data, despite exhibiting high quantization errors. To  evaluate the classification performance more accurately,   we  propose to directly investigate the feature discrimination of quantized data, rather than analyze its quantization error. It is found that  binary and ternary quantization can surprisingly improve, rather than degrade,  the feature discrimination of original data. This remarkable performance is validated through classification experiments  on diverse data types, including images, speech and text.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes “feature discrimination” to analyze the impact of quantization on classification, which offers a more direct and rational assessment of classification performance rather than relying on quantization error as previous researches asses classification performance roughly.

### Strengths
1. The motivation is interesting and the addressed quantization analysis problem is meaningful. 
2. The proposed feature discrimination analysis is pretty novel.
3. Sufficient and rigorous theoretical proof to derive the value range of the quantization threshold τ based on µ and σ for binary quantization and ternary quantization, respectively. 
4. Clear method statement, careful logic and sufficient explanations.
5. Adequate experiments on both synthetic data and real data.

### Weaknesses
1. As for Eq. (5), further explanations are need to state why discrimination between two classes of data can be formulated to Eq. (5) for clarify.
2. In the Remarks paragraph on P4, the authors said “it is demonstrated that the desired thresholdτdoes exist, when the two classes of data X∼N(µ, σ2 ) and Y∼ N(−µ, σ2 ) are assigned appropriate values for µ and σ”. Are µ and σ in the quantization space set? I mean once the quantization method is used, the distribution in the quantization space is determinate. How can we guarantee appropriate values for µ and σ? In other words, if the quantization space does not meet the condition, is the analysis reasonable or applicative?
3. In real data experiments, we see the value ranges for the threshold τ, it is better to provide the values for µ and σ in the real data case to further analyze the influence of the distributions for quantization.

### Questions
1. What if it is not a binary classification problem (more than two classes) or for image classification problem with muti-labels?
2. The paper provides theoretical analysis that the appropriate threshold τ exists, but how to set it not depending on the classification accuracy?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper presents the study of binary and ternary quantization for the classification problem through the feature discrimination capability analysis. The main contribution of this paper is to prove that quantization errors do not necessarily lead to decreased classification performance. The proof is done through theoretical analysis and experiments with simulated and real-life data sets. Thus, the estimation of the classification performance can be achieved by examining the feature discrimination of quantized data rather than only the quantization errors.

### Strengths
As the authors claim, this may be the first study to exploit feature discrimination to analyze the impact of quantization on classification. One important finding is that the quantization thresholds have an impact on feature discrimination and classification performance. The authors conducted theoretical analyses to prove that binary and ternary quantization can enhance feature discrimination between two classes of data. The choice of the quantization threshold becomes a key factor for better classification performance.  

The work is original and interesting, and the paper is well written and presented. The idea was proved through numerical analysis and experiments with simulated and real-time data.

### Weaknesses
Although the paper is easy to follow, some problems still need to be clarified. 
 
-  As stated in 2.4, the major goal of this paper is to investigate whether there exist threshold values in binary and ternary quantization to improve feature discrimination. This is confusing, as different threshold values will result in different feature discrimination measures. Then, what is the significance of this finding? Could you please clarify the practical implications of finding threshold values that improve feature discrimination or how the finding will help optimize the classification process?

- The abstract mentions classification generally but does not specify the number of classes. In the study, the experiment is binary classification, even for real-life data. Does that imply any relation between binary and ternary quantization with binary classification or even ternary classification? This raises the question: is this finding for general classification or binary classification only? What additional work would be needed to generalize the findings to multi-class (>3) classification problems?

- The design of the experiments can be improved to support the claims directly. For instance, the experiments whose results are presented in 4.1.2 considered data sparsity, data dimension, different classifiers, and the difference between binary and ternary quantization. To some extent, the results raise more questions. The comparison between binary and ternary quantization does not derive any solid conclusion, just stating, "yield superior performance." The variables considered in the experiments are not directly related to the core topic. The variables should include the "feature discrimination measure" and "quantization error," and experiments should consider the three scenarios with original data, binary, and ternary quantization.   

- In Figure 3, the classification with binary or ternary quantization does not always achieve a better result. Then, an optimal threshold value is expected, but how? This is not available in this study. In practice, how can this value be determined for varied scenarios (such as data dimension)? 

- The paper criticizes using quantization errors to estimate classification performance. Is it possible to show the quantization errors in the experiments as a baseline? This will help better understand the value of the work. A comparison of quantization errors and classification performance across different threshold values, to directly illustrate the limitations of using quantization errors as a proxy for classification performance may be beneficial.

### Questions
The experiment results show classification accuracies with original, binary, and ternary data. Is it possible to show the feature discrimination capability (e.g., the ratio between inter-class and intra-class scatters) represented with some numbers and quantization errors? This is what the study directly deals with. 

From the experimental results, we may conclude that classification with binary or ternary quantization does not always achieve a better result, even for binary classification. An optimal threshold value is essential, but there is still no solution to find that. 

Finally, it would be better to clarify whether the finding is for general classification or binary classification and why.

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
4

### Summary
This paper proposes a method to analyze the impact of binary and ternary quantization on the performance of classification tasks by focusing on feature discrimination rather than quantization errors. Unlike traditional approaches that primarily uses quantization errors to estimate performance degradation, this work demonstrates that by selecting a proper quantization threshold, binary and ternary quantization can sometimes improve classification accuracy by enhancing feature discrimination. Through theoretical analysis and empirical experiments on synthetic and real datasets, the paper provides valuable insights into how specific quantization thresholds can yield optimal classification performance.

### Strengths
1. The paper analyzes the impact of binary and ternary quantization on classification performance based on feature discrimination, which directly correlates to classification performance and offers an alternative to quantization error as a metric.

2. Theoretical derivations are well-supported with numerical experiments across different types of datasets, including synthetic and real datasets.

### Weaknesses
1. No large datasets were used: The datasets used in classification tasks are too small. Experiments on large datasets are needed to verify whether the conclusions and findings of this paper are still valid.

2. The classification tasks are too simple: The authors verified the impact of quantization on feature discrimination only in binary classification tasks which are too simple and the conclusions and findings of this paper may not work for complex classification tasks.

3. Limited classifiers were studied: The work only studied the impact of binary and ternary quantization on feature discrimination of KNN and SVM. How about MLP or decision trees or other classifiers?

### Questions
1. This paper said the quantization on the data with large sparsity will have a negative effect on the performance which is contradictory to a current paper [1].
[1] Chen, M., & Li, W. (2023). Ternary and Binary Quantization for Improved Classification. Authorea Preprints.

2. Is the proposed feature discrimination-based quantization analysis approach applicable to quantization methods beyond binary and ternary?

### Soundness
2

### Presentation
3

### Contribution
2
