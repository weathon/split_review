# ContraSim: Contrastive Similarity Space Learning for Financial Market Predictions

- Decision: Reject
- Scores: 5, 3, 6, 6

## Abstract
We introduce the Contrastive Similarity Space Embedding Algorithm (ContraSim), a novel framework for uncovering the global semantic relationships between daily financial headlines and market movements. ContraSim operates in two key stages: 
(i) Weighted Headline Augmentation, which generates augmented financial headlines along with a semantic fine-grained similarity score, and (ii) Weighted Self-Supervised Contrastive Learning (WSSCL), an extended version of classical self-supervised contrastive learning that uses the similarity metric to create a refined weighted embedding space. This embedding space clusters semantically similar headlines together, facilitating deeper market insights. Empirical results demonstrate that integrating ContraSim features into financial forecasting tasks improves classification accuracy from WSJ headlines by 7%. Moreover, leveraging an information density analysis, we find that the similarity spaces constructed by ContraSim intrinsically cluster days with homogeneous market movement directions, indicating that ContraSim captures market dynamics independent of ground truth labels. Additionally, ContraSim enables the identification of historical news days that closely resemble the headlines of the current day, providing analysts with actionable insights to predict market trends by referencing analogous past events.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
In this paper, a novel Weighted Self-Supervised Contrastive Learning (WSSCL) method is introduced to cluster news-lines based on learned semantic embeddings. LLMs are used to create modified prompts containing semantically identical or augmented news-lines. An enhanced version of KNN algorithm based on information theory is also introduced for clustering, in order to handle imbalanced labelled classes. Experiments on the task of stock market direction prediction show the effectiveness of the proposed method.

### Strengths
The paper focuses on an interesting problem, that is stock market direction prediction. The proposed method based on contrastive learning of text embeddings is reasonable. The example about rephrasing, slight ablation, and negative modification of the headline in Table 1 is illustrative and to the point.

### Weaknesses
Only one dataset (the NIFTY dataset) is used. It'd be great if the authors could use more datasets for evaluation. The lack of diverse datasets makes it difficult to assess the generalizability of the proposed method. Specifically, the NIFTY dataset represents a specific market and time period, and the performance of the model might be highly dependent on the characteristics of this particular dataset. It is unclear if the proposed method would perform well on other stock markets, or even on other types of time-series data. The absence of comparison with other datasets limits the scope of the conclusions that can be drawn from the study.

### Questions
The estimated baseline values are a mean of random samples following the (23%, 60%, 17%) label split in Table 3. Does it mean if a trivial classifier always predicts the label of a sample is Neutral, it would achieve 60% accuracy?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper proposes a model for stock movement prediction.

### Strengths
N/A

### Weaknesses
1. Low-quality presentation.
2. Lack of serious experiments.
3. Lack of contributions.

1.  The presentation of this paper is poor, which directly affects readers' understanding of the model design and problem formulation. It is unclear whether some model details are omitted or buried under misleading representations
    1.  There are numerous grammar mistakes and typos in the first paragraph of Section 3.1, with almost every sentence containing issues. This makes understanding the motivation behind building the proposed embedding space difficult.
    2.  It is unclear why the authors chose to use 10 and 30 to control the number of news articles sampled per day. Are these numbers theoretically justified, suggested by domain experts, or supported by empirical results? Also, what happens if there are fewer than 10 financial-related news articles in a day?
    3.  What is the motivation behind using random sampling when there are more than 30 news articles per day? The use of randomness makes it difficult to ensure that the space will cover all topics described in the news for that day. In the worst-case scenario, important topics might be completely omitted.
    4.  The authors claim that they only keep newslines and ignore tabular data. What does this mean? This statement seems to come out of nowhere.
    5.  In the description of creating headlines, it is unclear why "prompts" are sometimes created and, at other times, "headlines" are created. Is there a specific reason for this, or are these typos?
    6.  In Equation 3, it is unclear what the text refers to.
    7.  The notation $N_i$ in the description below Equation 3 should be $N_k$
    8.  The symbol $h$ in Equation 3 should be $\hat{h}$
    9.  The augmentation method lacks a quality control mechanism for headline generation. Also, the definitions of "slight ablation" and "negative" are unclear. In the given example, it appears that the authors only used a language model to generate fake company names, which lacks a clear motivation.
    10. The section on "generating newsline buckets" is difficult to understand due to grammar mistakes and undefined terms, making the entire subsection challenging to follow.
    11. The method used by the authors to achieve "known semantic distance" lacks motivation. It appears that the authors manually assigned values of 1, 0.5, and 0 to three different augmentations without justification.
    12. Grammar mistakes and typos continue throughout the rest of the paper, making it challenging to list them all. However, there are some critical ones. For example, in the WSSCL section, the authors state that there are only three movements: Fall, Natural, and Fall again.
    13. The experiment section lacks serious comparisons to justify the performance of the proposed model.

### Questions
The presentation of this paper is poor, which directly affects readers' understanding of the model design and problem formulation. It is unclear whether some model details are omitted or buried under misleading representations
1. There are numerous grammar mistakes and typos in the first paragraph of Section 3.1, with almost every sentence containing issues. This makes understanding the motivation behind building the proposed embedding space difficult.
2. It is unclear why the authors chose to use 10 and 30 to control the number of news articles sampled per day. Are these numbers theoretically justified, suggested by domain experts, or supported by empirical results? Also, what happens if there are fewer than 10 financial-related news articles in a day?
3. What is the motivation behind using random sampling when there are more than 30 news articles per day? The use of randomness makes it difficult to ensure that the space will cover all topics described in the news for that day. In the worst-case scenario, important topics might be completely omitted.
4. The authors claim that they only keep newslines and ignore tabular data. What does this mean? This statement seems to come out of nowhere.
5. In the description of creating headlines, it is unclear why "prompts" are sometimes created and, at other times, "headlines" are created. Is there a specific reason for this, or are these typos?
6. In Equation 3, it is unclear what the text refers to.
7. The notation $N_i$ in the description below Equation 3 should be $N_k$
8. The symbol $h$ in Equation 3 should be $\hat{h}$
9. The augmentation method lacks a quality control mechanism for headline generation. Also, the definitions of "slight ablation" and "negative" are unclear. In the given example, it appears that the authors only used a language model to generate fake company names, which lacks a clear motivation.
10. The section on "generating newsline buckets" is difficult to understand due to grammar mistakes and undefined terms, making the entire subsection challenging to follow.
11. The method used by the authors to achieve "known semantic distance" lacks motivation. It appears that the authors manually assigned values of 1, 0.5, and 0 to three different augmentations without justification.
12. Grammar mistakes and typos continue throughout the rest of the paper, making it challenging to list them all. However, there are some critical ones. For example, in the WSSCL section, the authors state that there are only three movements: Fall, Natural, and Fall again.
13. The experiment section lacks serious comparisons to justify the performance of the proposed model.

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
4

### Summary
The paper presents ContraSim, a contrastive learning framework for financial market prediction that creates a dense embedding space for financial news headlines. The approach has two main components:

1. Weighted Headline Augmentation: This technique generates variations of financial headlines with known semantic distances, including reworded, slightly ablated, and negative versions, allowing the model to capture rich semantic relationships between headlines.
2. Weighted Self-Supervised Contrastive Learning (WSSCL): Extending traditional contrastive learning, WSSCL uses augmented headlines to establish a continuous similarity space, clustering semantically similar headlines and separating dissimilar ones.

The framework introduces a novel metric, Info-kNN, to measure the density of semantically similar clusters. When integrated with a language model-based classifier, ContraSim achieves a 7% improvement in classification accuracy and a 13% boost in balanced accuracy over the baseline. Additionally, it provides practical support for financial analysts by identifying similar historical market days, offering valuable insights for forecasting.

### Strengths
1. Innovative and Practical Framework: The integration of contrastive learning through Weighted Headline Augmentation and WSSCL in financial market prediction presents a novel approach that assists financial analysts by enabling the identification of historical market conditions.
2. Enhanced Performance: The framework’s substantial improvements in classification accuracy (+7%) and balanced accuracy (+13%) validate its effectiveness.
3. Info-kNN Metric: The introduction of the Info-kNN metric, which evaluates clustering in the embedding space using information-theoretic principles, is a notable contribution. This metric provides a new way to assess contrastive learning models and has potential applications beyond financial data.

### Weaknesses
1. Limited Ablation Studies: The current ablation studies are limited, particularly in assessing the individual impact of the headline augmentations (reworded, slightly ablated, and negative). Examining how each augmentation affects accuracy and clustering—especially by showing the effect of their removal—would strengthen the claims. A more granular analysis is needed to understand the contribution of each augmentation type. For instance, do reworded headlines contribute more to semantic understanding than slightly ablated ones, or do negative headlines primarily improve the model's ability to distinguish between dissimilar examples? The impact of removing each augmentation type should be quantified using metrics such as classification accuracy, F1 score, and clustering purity. A similar analysis could be extended to Info-kNN and WSSCL components. Specifically, the paper should explore the effect of removing Info-kNN and using a standard k-NN approach, as well as the impact of using a standard contrastive loss instead of WSSCL. These ablations are crucial for understanding the necessity of each component.

2. Narrow Scope in Experiments: Although the authors mention plans for broader application, the current validation is confined to financial data, which limits the immediate generalizability of the findings. The financial domain has unique characteristics (e.g., high volatility, specific jargon) that might not be present in other domains. Including experiments from other domains, such as general news articles or social media text, would provide a more robust assessment of the framework's generalizability. Alternatively, a more in-depth discussion of potential applications, including specific examples of how ContraSim could be adapted to different domains, would enhance the broader impact of this work. Without such analysis, it is difficult to ascertain whether the reported performance gains are specific to financial data or if they can be expected in other contexts.

### Questions
Could you provide more detailed insights into how the different headline augmentation types (reworded, slightly
ablated, negative) contribute individually to the observed improvements in classification accuracy and clustering
effectiveness? While the paper outlines these augmentations, it would be helpful to understand the individual
impact of each augmentation type on the model's learning process. Additionally, a more detailed ablation study
of key components, such as augmentation types, Info-kNN, and WSSCL, would offer a clearer understanding of
their respective contributions to the overall performance.

### Soundness
3

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
The paper introduces ContraSim, an innovative approach for predicting financial market movements that employs a two-part method: it first creates semantically varied financial headlines through Weighted Headline Augmentation, and then applies Weighted-Self Supervised Contrastive Learning (WSSCL) to refine the embedding space. This combination allows ContraSim to effectively group newslines that reflect similar market trends, achieving a notable 7% improvement in classification accuracy for financial forecasts. Additionally, the authors present a novel metric called Info-kNN to assess how well the embedding space captures significant semantic relationships within financial news.

### Strengths
It presents a methodology that integrates advanced techniques such as Weighted Headline Augmentation and Weighted-Self Supervised Contrastive Learning (WSSCL), providing a fresh perspective on the interplay between financial news and market behavior.  The introduction of the Info-kNN metric to evaluate semantic clustering in the embedding space is another key contribution, offering researchers a robust tool for assessing how well models capture the complexities of financial data.

### Weaknesses
First, the paper does not inform the reader how ContraSim contributes to the field relative to other approaches. Second, apparently LLMs bring their own biases to the model. Any biases inherited from the LLM can affect the quality of the data and predictions. Predictions based on headlines provides limited scope and prediction errors as headlines are usually written to take attention.

### Questions
What are the types of augmentations utilized?
What are the characteristics of the learned embedding space that influences the interpretability of financial predictions? 
Can you elaborate the hyperparameter tuning process in more detail?

### Soundness
3

### Presentation
3

### Contribution
3
