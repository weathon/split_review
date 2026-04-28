# ContextRef: Evaluating Referenceless Metrics for Image Description Generation

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6

## Abstract
Referenceless metrics (e.g., CLIPScore) use pretrained vision--language models to assess image descriptions directly without costly ground-truth reference texts. Such methods can facilitate rapid progress, but only if they truly align with human preference judgments. In this paper, we introduce \ourdataset, a benchmark for assessing referenceless metrics for such alignment. \ourdataset\ has two components: human ratings along a variety of established quality dimensions, and ten diverse robustness checks designed to uncover fundamental weaknesses. A crucial aspect of \ourdataset\ is that images and descriptions are presented in context, reflecting prior work showing that context is important for description quality. Using \ourdataset, we assess a variety of pretrained models, scoring functions, and techniques for incorporating context. None of the methods is successful with \ourdataset, but we show that careful fine-tuning yields substantial improvements. \ourdataset\ remains a challenging benchmark though, in large part due to the challenge of context dependence.\footnotemark{}\looseness=-1

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
1: You are unable to assess this paper and have alerted the ACs to seek an opinion from different reviewers.

### Summary
This work introduces a new benchmark to evaluate the alignment of referenceless metrics, like CLIPScore, with human preferences in the context of image description generation. It comprises human ratings and robustness checks, emphasizing the importance of context in image descriptions. The assessment reveals that none of the existing methods fully meet the benchmark, especially in context sensitivity. However, the paper suggests that fine-tuning can enhance metric performance, although ContextRef remains a challenging benchmark due to the complexity of context dependence.

### Strengths
ContextRef represents a significant advancement in the evaluation of referenceless metrics for image description generation. By emphasizing the importance of context, it addresses a critical gap in existing benchmarks.
The benchmark includes both human ratings along various quality dimensions and robustness checks. This comprehensive approach allows for a more nuanced understanding of the strengths and weaknesses of referenceless metrics.
By focusing on context, ContextRef aligns more closely with real-world scenarios where image descriptions are typically encountered, making the benchmark more relevant and applicable.
he paper sheds light on the often-underestimated role of context in image description quality, contributing valuable insights to the field and encouraging future research to consider this aspect more thoroughly.

### Weaknesses
This work involves human ratings, which are subjective and can introduce bias. The paper could benefit from a more detailed discussion of how raters were selected and trained to ensure consistency and mitigate potential biases.

Overall, I am not working on this area at all, I would like to check comments from other reviewers for the final rating.

### Questions
no.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes an evaluation protocol to evaluate referenceless metrics commonly used for the assessment of text image description generators. Authors first build an evaluation dataset as a subset of the WIT dataset comprising 204 image-caption-context-description samples. This dataset is used for a user study, where humans are rating the quality of different image description across multiple axes. Human preference is then used as a reference to evaluate the quality of referenceless metric, alongside measures of metric robustness by applying several transformations to the generated descriptions. Finally, authors investigate whether model-based metrics can be improved by fine-tuning models on human scores and augmentations.

### Strengths
The paper addresses an interesting topic. Referenceless metrics are often used as a means to demonstrate the performance of a new model, with limited insights into how reliable they can be. Providing a solution to understand which metrics are most accurate has the potential to be very useful.  

Authors have evaluated a large set of model-based evaluation metrics, with the somewhat low correlations suggesting a lack of reliability. Furthermore, the reference dataset and associated human study are a useful resource that could be used to evaluate future metrics.

### Weaknesses
The paper presentation could be substantially improved. The related work section is focusing almost solely on the clip model,and fails to provide an accurate review of pre-existing related literature. Authors should review pre-existing metrics, related benchmarks and evaluation strategies. Specifically, the related work should include a discussion of metrics such as SPICE, CIDEr, and METEOR, which are commonly used in image captioning evaluation, and how these compare to the referenceless metrics explored in this work. Similarly, section 3 provides descriptions of metrics being analysed in this work, and lacks accurate descriptions to understand the particularities of each method. For example, only encoder architectures are discussed for the Flamingo model, but the actual mechanisms used to compute the metric are not discussed. The paper should clarify how the Flamingo model's cross-attention mechanism is used to score the image-text alignment, and how this differs from other metrics. The strategy used to integrate context information as also poorly explained, and could benefit from providing equations. For instance, it is unclear how the context is concatenated or otherwise incorporated into the input for each model, and how this affects the final score. 

Certain claims seem excessive. Authors mention that their results suggests that referenceless metrics can be successfully used based on observed correlation, however somewhat low correlations are observed (.2-.3), suggesting the opposite. In addition, the use of context is highlighted multiple times throughout the paper, yet the impact of integrating this context variable is barely discussed, the only relevant experiment is the use of shuffled contexts in section 5.2. It would have been interesting to discuss context more in depth and how it impacts user evaluation and metric performance. For example, a more thorough investigation into how different types of context (e.g., surrounding text, image metadata) affect metric performance would be beneficial. 

The fine-tuning experiment in section 6 doesn’t seem particularly necessary, as metrics become tailored for a specific dataset/user preference, This reduces applicability and generalizability, and seem to contradict the main objective of the paper. The fine-tuning process risks overfitting to the specific nuances of the dataset and human preferences, making it less useful for evaluating image description quality in other contexts. The authors should clarify the motivation behind this experiment, and how it contributes to the overall goal of developing reliable referenceless metrics.

### Questions
- Section 4.1 mentions that the dataset is built by collecting caption-alt description pairs for each image, yet in the human study, it is mentioned that 5 descriptions are provided. Where are the additional descriptions obtained from? 

- There appears the be a lot of similarities between the data collection and human study protocol proposed in this paper and in Kreiss et al 2022b. Can authors clarify how related these two strategies are?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents ContextRef, a new benchmark designed to assess the alignment of referenceless image description quality metrics with human preferences. The proposed benchmark incorporates human-subject ratings across diverse quality dimensions and ten robustness checks to gauge metric performance under varying conditions. Additionally, the study delves into several metric approaches, revealing that none of them prove successful on ContextRef due to their insensitivity to fundamental changes in examples. Lastly, the paper suggests that careful fine-tuning has the potential to enhance metric performance while acknowledging the ongoing challenge of effectively accounting for context.

### Strengths
1. This paper is well-written and easy to understand.
2. The introduction of the new benchmark, ContextRef, is indeed a valuable contribution to the field. A crucial feature of ContextRef is the presentation of images and descriptions within a contextual framework, which plays a crucial role in generating appropriate descriptions.

### Weaknesses
While the paper highlights the underperformance of existing methods when dealing with context, this finding is unsurprising to me since the tested models were not trained with context.

### Questions
Please refer to the weakness part.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
