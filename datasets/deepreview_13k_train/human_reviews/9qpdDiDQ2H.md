# MetaOOD: Automatic Selection of OOD Detection Models

- Decision: Accept
- Scores: 6, 3, 6, 6

## Abstract
How can we automatically select an out-of-distribution (OOD) detection model for various underlying tasks? This is crucial for maintaining the reliability of open-world applications by identifying data distribution shifts, particularly in critical domains such as online transactions, autonomous driving, and real-time patient diagnosis. 
Despite the availability of numerous OOD detection methods, the challenge of selecting an optimal model for diverse tasks remains largely underexplored, especially in scenarios lacking ground truth labels.
In this work, we introduce \method, the first \textit{zero-shot}, \textit{unsupervised} framework that utilizes meta-learning to select an OOD detection model automatically. 
As a meta-learning approach, \method leverages historical performance data of existing methods across various benchmark OOD datasets, enabling the effective selection of a suitable model for new datasets without the need for labeled data at the test time.
To quantify task similarities more accurately, we introduce language model-based embeddings that capture the distinctive OOD characteristics of both datasets and detection models. 
Through extensive experimentation with 24 unique test dataset pairs to choose from among 11 OOD detection models, we demonstrate that the \method significantly outperforms existing methods and only brings marginal time overhead. 
Our results, validated by Wilcoxon statistical tests, show that \method surpasses a diverse group of 11 baselines, including established OOD detectors and advanced unsupervised selection methods.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In this paper, the authors propose MetaOOD, which utilizes meta-learning to select an OOD detection model automatically. The motivation is that each OOD detection algorithm might excel in specific scenarios but may not perform well universally, therefore it is important to select one particular OOD detection for each task. MetaOOD utilizes historical performance data of existing methods across a variety of benchmark out-of-distribution (OOD) datasets to enable efficient model selection for new datasets, eliminating the need for labeled data at test time. To more accurately measure task similarities, the authors incorporate language model-based embeddings that capture the unique OOD characteristics of both datasets and detection models. Through extensive testing across 24 unique test dataset pairs and 11 OOD detection models, the authors show that MetaOOD consistently outperforms current methods with minimal additional computation time.

### Strengths
1. The idea of using meta-learning to select the best OOD detection method for each specific task is interesting.
2. The paper is generally easy to understand and clearly written.
3. The experiments show the effectiveness of the proposed method.

### Weaknesses
1. Figure 1 needs to be improved. The notations in the figure are confusing and unclear. Specifically, the flow of information and the meaning of each arrow and box are not immediately obvious, making it difficult to grasp the overall methodology at a glance. For example, it's unclear how the dataset embeddings and method embeddings are generated and used in the meta-learning process.
2. The design of the textual description seems ad-hoc and cannot be applied in the case of without detailed dataset information. The paper does not specify how to handle datasets where detailed textual descriptions are unavailable or insufficient, which limits the generalizability of the approach. The reliance on subjective textual descriptions introduces a potential source of bias and inconsistency.
3. Detailed results on the selected OOD method for each dataset are missing. Without this information, it is difficult to assess the practical utility of the proposed method and understand which OOD detection methods are favored for different types of datasets. This lack of transparency makes it hard to verify the claims of the paper.

### Questions
1. Does the proposed method rely on the architecture of the trained model?
2. What is the training time of the proposed method?
3. If there is one additional OOD method, how can incorporate this method into the proposed MetaOOD?
4. What are the main factors that influence the choice of an OOD method based on the characteristics of the training and test sets?

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
4

### Summary
This paper presents MetaOOD, a “model” selection approach for out-of-distribution (OOD) detection. MetaOOD utilizes language models to generate feature embeddings of both the meta dataset and “models”, allowing for the optimal “model” selection based on anticipated performance on the test set. The results on the Wilcoxon statistical tests show the promising performance of MetaOOD.

### Strengths
1. The motivation is sound. It is interesting to see a meta-selection approach to the OOD detection problem since there are so many methods in this OOD domain.
2. The proposed method is simple and straightforward. The results on the traditional methods are promising.

### Weaknesses
1. The definition of "OOD model" is confusing. There are many post-hoc detection methods in the detection problem, which should not be classified as “models”. For instance, the paper includes the MSP method for the selection experiments. However, MSP is just a simple post-hoc technique that can be applied to most classification models (e.g., ResNet) using the SoftMax function. This method should not be considered as a model, which is misleading considering another factor, “model architecture,” in the experiments.

2. The methodology lacks depth. MetaOOD merely utilizes language models to extract embeddings for dataset and model descriptions, and then select the top-1 method based on these embeddings. The approach lacks insight and overlooks potential issues. For instance, the embeddings derived from descriptions may not accurately capture the true characteristics of the models and datasets. Also, simply selecting the top 1 can overlook the nuances of methods and the potential problems of the utilized datasets.

3. The experimental results are unconvincing. The baseline methods included are outdated, with the most recent method (NCF) dating back to 2017.

4. The terms OOD and OOD detection should not be used interchangeably. It is unclear what is meant by "OOD dataset" given such a name strategy. Is it referring to a commonly recognized OOD dataset distinct from the in-distribution (InD) dataset, or simply an OOD detection dataset (includes train, val, and test splits for detection methods)?

5. I am curious whether this paper was generated by a language model, such as GPT-4. The writing style, particularly in Section 3.3.1, resembles AI-generated text. Given the simplicity of the method, the Method Section could be more concise, potentially requiring only 0.5 pages to convey the core elements of the approach. However, the current version spans 2.5 pages.

### Questions
NA

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper postulates that by identifying which OOD detection models have historically performed well on datasets similar to the one currently being considered, one can select the model most likely to be effective without needing labels for supervised training.  A meta-learning approach is used to take past performance data from various models (across data sets); when new dataset arrives, the approach checks for similarity between the new dataset and historical ones using embeddings. The assumption is that the selected model will perform well as it is closest to the data set under use.  Meta-learning (training) is done offline with curated data sets; while OOD model selection is online as a specific data point arrives.  Results show that their approach works better than compared other techniques.  Experiment approach itself is reasonable and approach is sound.

### Strengths
Integration of language model based embeddings; Empirical eval. is done to good detail. this technique is actually useful. though it is a logical next step ~ the approach itself can be used in other contexts or at-least the idea can be adapted. Sufficient detail is provided makes work transparent.

### Weaknesses
Eval is too narrow and limited ~ so results may not generalise or this approach may be limited to the data set / domain attempted; esp. since there is no formal conceptual development as such we do not know when and where this method will work or have an intuition for where the limit may be.  Although there is the claim of unsupervised world-first etc. ~ there is still a need for other forms of supervised and curated training. Assumes text descriptions are good in the evals and curated data sets - but does it hold for the real world?  All the usual limits of language models apply here too. Scalability not known -- again since we do not have specific underlying theory.

### Questions
Can the authors add a diagram to better illustrate how this technique would work in practice? This will help translatability of this work into other contexts faster.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper presents MetaOOD, a framework for automatic selection of out-of-distribution (OOD) detection models without requiring labeled data. It leverages historical performance data and language model embeddings. The approach aims to improve the reliability of OOD detection in critical applications, such as autonomous driving and online transactions. Overall, MetaOOD addresses the challenge of adapting to data shifts effectively and efficiently.

### Strengths
The paper's strengths include the introduction of a zero-shot, unsupervised framework for OOD detection model selection, which enhances adaptability to new datasets. It effectively utilizes language model-generated embeddings to capture nuanced dataset characteristics, improving model selection accuracy. The extensive experimentation demonstrates superior performance compared to eleven established methods, showcasing its robustness. Additionally, the framework incurs minimal runtime overhead, making it efficient for practical applications. The use of the Wilcoxon signed-rank test is a plus of the paper. The p-values suggests the proposed approach works well.

### Weaknesses
The paper's weaknesses include a reliance on the quality of language model embeddings, which may vary based on the model used and the nature of the input data. Additionally, the framework's performance may be limited by the diversity of the historical data pool, potentially affecting generalization to unseen datasets. The lack of extensive real-world testing could raise concerns about its applicability in practical scenarios. Lastly, the complexity of the approach may pose challenges for reproducibility and implementation in different contexts. Obtain datasets and model feature/embeddings from their textual descriptions appear a bit strange and somewhat unreliable.

### Questions
No questions.

### Soundness
3

### Presentation
2

### Contribution
3
