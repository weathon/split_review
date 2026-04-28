# Making Pre-trained Language Models Great on Tabular Prediction

- Decision: Accept
- Avg Score: 7.00
- Scores: 8, 6, 6, 8

## Abstract
The transferability of deep neural networks (DNNs) has made significant progress in image and language processing. However, due to the heterogeneity among tables, such DNN bonus is still far from being well exploited on tabular data prediction (e.g., regression or classification tasks). 
Condensing knowledge from diverse domains, language models (LMs) possess the capability to comprehend feature names from various tables, potentially serving as versatile learners in transferring knowledge across distinct tables and diverse prediction tasks, but their discrete text representation space is inherently incompatible with numerical feature values in tables.
In this paper, we present \textit{TP-BERTa}, a specifically pre-trained LM for tabular data prediction. Concretely, a novel \textit{relative magnitude tokenization} converts scalar numerical feature values to finely discrete, high-dimensional tokens, and an \textit{intra-feature attention} approach integrates feature values with the corresponding feature names. Comprehensive experiments demonstrate that our pre-trained TP-BERTa leads the performance among tabular DNNs and is competitive with Gradient Boosted Decision Tree models in typical tabular data regime. % Our pre-trained model will be publicly available.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces a novel approach to adapt pre-trained language models for tabular data prediction, presenting the TP-BERTa model based on RoBERTa's architecture. This model employs a unique method termed "relative magnitude tokenization" to transform scalar numerical feature values into a more discrete, high-dimensional token format. This tokenization process enables the language model to comprehend relative value magnitudes within the language representation space. Additionally, the paper showcases the intra-feature attention (IFA) mechanism that fuses feature names and their corresponding values attentively. Comparative evaluations on 145 datasets reveal that the TP-BERTa outstrips conventional tabular deep neural networks (DNNs) and is on par with Gradient Boosted Decision Tree models in typical tabular data settings.

### Strengths
1. **Originality:**  
    - The approach of "relative magnitude tokenization" (RMT) is an inventive technique for adapting pre-trained language models to tabular data. This method of converting scalar values to a tokenized format to be perceived as meaningful words within the language model's vocabulary stands out as a significant contribution.
    - The intra-feature attention (IFA) module to fuse feature name and value embeddings is another commendable addition to the field. This ensures a more contextual understanding of the feature within the model.
  
2. **Quality:**  
    - The proposed model has been extensively tested against 145 datasets, which is a comprehensive evaluation to validate its efficacy.
    - Superior performance against established models like common tabular DNNs and close competition with GBDTs further establish the quality and utility of the proposed approach.
  
3. **Clarity:**  
    - The paper delineates the methodology with sufficient detail, ensuring understanding and reproducibility.

### Weaknesses
1. It would have been beneficial if the paper delved deeper into the limitations and potential pitfalls of the relative magnitude tokenization technique. Understanding how the granularity of this tokenization might impact model performance, especially in cases with intricate numerical nuances, is crucial. Specifically, the paper should explore the sensitivity of the model to the number of magnitude tokens used. A finer-grained tokenization might capture subtle differences in numerical values, but could also lead to overfitting or increased computational cost. Conversely, a coarser tokenization might lose important information. The paper lacks a detailed analysis of how the choice of bin size affects performance across different datasets, particularly those with varying distributions of numerical features.
2. Comparisons with Gradient Boosted Decision Trees are noted, but an in-depth discussion regarding scenarios where GBDTs might outshine or underperform against the proposed TP-BERTa would provide readers with a clearer perspective. The paper should investigate specific dataset characteristics that favor one approach over the other. For instance, GBDTs are known to perform well on datasets with a high number of irrelevant features or complex feature interactions. It would be valuable to understand how TP-BERTa performs in these scenarios. Additionally, the paper should explore cases where the interpretability of GBDTs might be preferred over the black-box nature of the proposed model.

### Questions
1. How does the TP-BERTa model perform when handling missing, extreme or highly imbalanced values?
2. Could the authors provide insights into the computational complexity introduced by the relative magnitude tokenization and intra-feature attention mechanisms, especially when scaling to larger datasets?
3. Were there specific domains or types of datasets where the TP-BERTa particularly excelled or faced challenges?
4. Can the relative magnitude tokenization be fine-tuned or adaptively adjusted (e.g., bin size) based on the domain or the nature of the data to potentially yield better results?
5. Has there been any visualization or analysis conducted to assess how effectively the proposed model captures the representations of numerical values?

### Soundness
3 good

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
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presents pre-training methods for the tabular data. Unlike the traditional text-based pre-training such as masked LM or language modeling, tabular data does not have common token distributions and is not suitable for the traditional pretraining mechanism. The paper introduces a way to discretize the continuous values to discrete tokens based on their relative magnitude. Doing so allows posing a pretraining objective over heterogeneous features.

---

The score is updated post-rebuttal. See the other comment for the details.

### Strengths
* Paper is mostly clearly written.

### Weaknesses
 * It is very unclear if some distributional patterns from common tabular data can be generalized to other data with completely different distributions. In text, pretraining can learn generic linguistic features such as meaning of the English words or grammars. In tabular data, the core assumption does not hold because it differs drastically between data sources.
* The empirical comparison does not essentially provide evidence that pre-training is the main factor to improve the performance of the downstream tasks. It is not clear if the performance gains are due to the pre-training itself or simply due to the increased model capacity from using a large language model architecture. The experiments do not sufficiently isolate the effect of the proposed pre-training method from the effects of the base model architecture.


### Questions
* As discussed in the weaknesses section, pretrained tokens from the quantized tabular data do not have a good interpretation of what they are really capturing from. I hope authors can provide discussions and empirical analysis on the tokens that they are capturing.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposed a new pretrained model for table prediction called TP-BERTa. TP-BERTa is based on the RoBERTa architecture with two modifications: 1) it discretizes numerical feature values as relative magnitude tokens (RMT) so that the tokens can be treated as meaningful words in the LM’s vocabulary, 2) it adopts the intra-feature attention (IFA) method to attentively fuse the embeddings of feature name and values to a single embedding. TP-BERTa has been trained on a combination of 101 classification datasets and 101 regression datasets. Results show that TP-BERTa outperforms other tabular deep learning models and is comparable to GBDT. Ablation studies show that RMT and IFA boost the performance.

### Strengths
1. According to Table 1, the performance of TP-BERTa is strong. It consistently outperforms other tabular DL models and is comparable to XGBoost and CatBoost.
2. The idea of applying relative magnitude tokens (RMT) in tabular DL models is novel according to my knowledge. As pointed out by the "On Embeddings for Numerical Features in Tabular Deep Learning" paper, appropriately embed numerical features is important for tabular DL models. RMT can enhance language models in handling the numerical values that appear often in tabular datasets. As shown in the upper-half of Table-2, RMT significantly outperforms the value2str strategy.

### Weaknesses
1. Compared with RMT, the intra-feature attention method is marginally novel and is not showing significant performance boost.
2. The author has not studied the impact of pretrain data diversity in the performance of TP-BERTa. For example, how good will TP-BERTa be if it is only pretrained on 10 classification datasets and 10 regression datasets?

### Questions
What's the impact of pretrain data diversity in the performance of TP-BERTa? (See weakness)

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work introduces TP-BERTa, an LLM for tabular data prediction. TP-BERTa achives strong performance on many regression tasks and binary classification tasks. TP-BERTa incorporates 2 novel changes: (1) relative magnitude tokenization and (2) intra-feature attention.

### Strengths
- The model performance is very strong, even outperforming tuned XGBoost and other tabular methods. The paper does a good job comparing against many relevant baselines
- The introduced method architecture changes are both clear and intuitive
- Ablations for these changes and the experiments suggest that they both contribute to TP-BERTa's improved performance.

### Weaknesses
 - The experiments are restricted to binary classification, would be nice to see experiments for multi-class classification as well
- The method introduces a hyperpameter lambda which is simply fixed to 0.1. It would be nice to see more discussion / ablations of this parameter.
- Authors claim the model will be made available but at this time have not shared any code

### Questions
- Is it possible to perform the magitude tokenization without an added loss term and hyperparameter (e.g. by carefull designing the embeddings)?
- Is there a reason to prefer C4.5 discretization over CART?
- Will the authors release all code or only the trained model?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
