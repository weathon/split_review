# ImpScore: A Learnable Metric For Quantifying The Implicitness Level of Language

- Decision: Accept
- Scores: 8, 6, 8

## Abstract
Handling implicit language is essential for natural language processing systems to achieve precise text understanding and  facilitate natural interactions with users. Despite its importance, the absence of a metric for accurately measuring the implicitness of language significantly constrains the depth of analysis possible in evaluating models' comprehension capabilities. This paper addresses this gap by developing a scalar metric that quantifies the implicitness level of language without relying on external references. Drawing on principles from traditional linguistics, we define ``implicitness'' as the divergence between semantic meaning and pragmatic interpretation. To operationalize this definition, we introduce \modelname, a novel, reference-free metric formulated through an interpretable regression model. This model is trained using pairwise contrastive learning on a specially curated dataset comprising $112,580$ (\textit{implicit sentence}, \textit{explicit sentence}) pairs. We validate \modelname through a user study that compares its assessments with human evaluations on out-of-distribution data, demonstrating its accuracy and strong correlation with human judgments. Additionally, we apply \modelname to hate speech detection datasets, illustrating its utility and highlighting significant limitations in current large language models' ability to understand highly implicit content.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces IMPSCORE, a novel metric for quantifying the implicitness level of language by measuring the divergence between semantic meaning and pragmatic interpretation. The authors develop an interpretable regression model trained through pairwise contrastive learning on a newly created large dataset of 112,580 sentence pairs. The metric processes sentences using a text encoder to generate embeddings, maps semantic and pragmatic features into separate spaces, and calculates implicitness scores based on the divergence between these features after space transformation.

Experimental results validate the reliability of IMPSCORE. The authors also conduct a user study comparing the metric's assessments with human evaluations on out-of-distribution data, showing strong correlation with human judgments. They also demonstrate practical applications by analyzing implicitness levels in hate speech detection datasets and evaluating performance of several large language models across different implicitness levels, revealing that model performance degrades as implicitness increases.

### Strengths
- The paper is well motivated and presents a clear operational definition of implicitness and develops a concrete methodology for measuring it. The paper is well written and easy to follow. 
- Experimental results show strong support for the IMPSCORE as a reliable metric. The authors further validate it through careful ablation studies, user studies, and practical applications in analyzing both datasets and model performance.
- The training dataset is substantial and diverse (and is a contribution in itself), drawing from multiple domains and types of implicit language, while the evaluation includes both in-distribution and out-of-distribution testing.

### Weaknesses
 - The metric is developed and tested only for English language content. It is not clear how this would translate to other languages or whether this metric will work in cross-lingual settings.
- While well-designed, the user study involves only 10 participants evaluating 10 questions each, which is a relatively small sample size for validating a metric intended for broad use.

### Questions
- I'm curious if you could run some experiments to test the metric's performance on other languages? An easy (though, not perfect) way would be to look at translated sentence pairs across multiple languages to assess its language independence and potential biases?
- I'd love to see some qualitative error analysis for the metric. Are there any patterns that emerge in the sentences on which IMPSCORE isn't accurate?
- Is IMPSCORE just as reliable on longer sentences as on shorter ones?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces ImpScore, a reference-free metric designed to quantify the level of implicitness in human language. The model for ImpScore is trained via contrastive learning by calculating the divergence between the semantic (literal) meaning and the pragmatic (contextual) interpretation of a sentence. They collected a training data with 112,580 pairs. Through extensive experiments, ImpScore demonstrates strong correlation with human judgments. They also show the utility in evaluating hate speech detection datasets, revealing limitations in current large language models' ability to handle implicit content.

### Strengths
1. The paper tackles a rarely addressed problem, quantifying implicitness in language. It offers a new approach to measuring implicitness that moves beyond binary or purely lexical classifications.
2. ImpScore is a reference-free metric, which distinguishes it from previous metrics that often rely on external references or manual annotations.

### Weaknesses
1. Limited scope of implicit languages. The paper’s dataset includes synthetic data generated by GPT-3.5 and focuses primarily on specific types of implicit language (e.g., hate speech). However, ImpScore’s generalizability across broader types of implicit expressions (such as indirect requests or cultural idioms) remains uninvestigated. I wonder if the authors have evaluated their model on other types of implicit expressions, such as irony or casual dialogues.
2. While the paper performs some ablation studies, it primarily uses Sentence-BERT as the embedding model. Exploring alternative text encoders could provide a more comprehensive understanding of ImpScore’s design choices. They may also utilize some contrastive learning-based models, such as SimCSE. 
3. I am also concerned about their data synthetic approach. The reliance on GPT-3.5 for generating explicit counterparts of implicit sentences could introduce unintended biases, particularly if the model generates stereotypical or simplified responses (we can also see the average length of explicit sentences is much shorter than implicit ones). I wonder if the authors verified the quality of the generated explicit sentences.
4. I also expect some model comparisons. For example, they can use their training data as a binary classification task and compare the classification accuracy between the simple classifier and their proposed model.

### Questions
* How does the performance of ImpScore vary across different types of implicit language (e.g., indirect requests, cultural idioms, irony)? Are there specific types that it struggles with?
* Have you examined any potential biases and quality of the synthetic data?
* Can you compare with existing methods or other baselines for implicitness? For example, the methods mentioned in Related Work (e.g. Garassino et al. (2022) and Vallauri & Masia (2014))?
* I would like to see if you can implement ImpScore to the LLMs' abilities to generate implicit expressions. Similar to the data creation in Section 6.1, you can prompt different LLMs to generate 4 sentences with varying implicitness levels. Then, you calculate the ImpScore for these generations.

### Soundness
2

### Presentation
3

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
This paper introduces a scalar metric to compute the implicitness score for sentences known as IMPSCORE. They also contribute a dataset of 56,290 pairs of implicit and explicit sentences used to train the IMPSCORE model. The metrics reliability is studied through a user study on OOD data. Moreover, the authors apply IMPSCORE on various hate speech benchmarks and also compare the performance of three language models - gpt-4-turbo, llama-3.1-8b-instruct and OpenAI Moderation - on these datasets with varying levels of implicitness.

### Strengths
1. The paper tries to address an important problem of understanding the implicitness level of language through a novel framework to measure it based on the divergence between semantic meaning and pragmatic interpretation of a sentence. It also introduces a novel dataset consisting of diverse samples (validated from a linguistic expert) to train the model used in computing the implicitness score.
2. Overall, the study is comprehensive. Authors justify their choice for the final setting by performing sufficient ablations in terms of the design choices and hyper-parameters. They also conduct a user study to understand correlation of the metric with human judgement.
3. The paper is technically sound and is well written in general.

### Weaknesses
1. The number of sentences used for human judgment correlation (40 - 4 sentences across 10 topics) are not sufficient enough to examine the generalization ability of the IMPSCORE metric. Expanding this set is necessary to improve the reliability of the metric. The limited number of topics and sentences per topic may not capture the full spectrum of linguistic nuances that affect implicitness. For example, the study might be skewed towards certain types of implicit language, such as sarcasm or irony, while neglecting others, like understatement or innuendo. This lack of diversity could lead to an overestimation of the metric's performance on unseen data.
2. Even though some justification is provided to measure the pragmatic distance (in the Introduction section), it is not entirely clear on why it is important. The ablation experiments also does not seem to affect the pragmatic distances, further casting doubts on its significance. Additional explanation for this sub-metric would be beneficial. The pragmatic distance, as currently implemented, appears to be a somewhat arbitrary measure. The paper does not provide a clear explanation of how the Euclidean distance between sentence embeddings effectively captures the pragmatic differences. Furthermore, the lack of impact from ablations on the pragmatic distance suggests that this component might not be contributing meaningfully to the overall performance of the IMPSCORE metric.

### Questions
1. Why is the same hyper-parameter $\gamma_1$ used for both $L_{imp} (s_1,s_2)$ and $L_{imp} (s_1,s_3)$?
2. Is the data split into train, validation and test sets stratified i.e. does it maintain the ratio of positive and negative pairs?

### Soundness
3

### Presentation
4

### Contribution
3
