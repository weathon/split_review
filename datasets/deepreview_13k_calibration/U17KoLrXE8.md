# ObjectNet Captions: Models are not superhuman captioners

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 5, 5, 6

## Abstract
Even on out-of-domain image captioning datasets such as nocaps, models often outperform humans according to captioning metrics like CIDEr. Yet, in real world conditions, model captions are often wrong. We demonstrate that this performance deficit exists by introducing a new dataset and a new captioning metric. We introduce a new dataset, called ObjectNet Captions, that reduces spurious correlations which machines often exploit. We show the shortcomings of current captioning metrics with a head-to-head experiment against humans, where we find that humans rate human-generated captions as being of much higher quality than machine captions.  Driven by this, we introduce HUMANr, a new, highly robust, easy to replicate, and consistent metric, computed from head-to-head comparisons, which can be crowdsourced at low cost.  We also develop tooling to automatically compute HUMANr. HUMANr is an absolute performance metric: driving it to 0 means that humans can no longer distinguish machine captions from human captions. No current metric provides such a fixed target to aim for along with knowledge of when captioning is solved in this sense. Moreover, HUMANr can reveal that humans still outperform machines, which no current metric is able to demonstrate. Existing metrics both overstate the performance of machine models and, at the same time, they inherently limit it. While most current metrics are saturated, HUMANr provides significant opportunities for further captioning research, thereby opening the door to new advances. ObjectNet Captions and HUMANr are made available to the research community.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces "ObjectNet Captions," a challenging dataset for image captioning, and presents HUMANr, a new metric for evaluating caption quality. It highlights a significant performance gap between human and model-generated captions, emphasizing the limitations of current models in generating detailed, accurate captions. The study's findings challenge the notion that advanced models like GPT-4 surpass human capabilities in this domain.

### Strengths
1. Introduction of a challenging dataset and HUMANr metric.
2. In-depth comparison of existing models with human performance using various metrics.
3. The paper effectively showcases the limitations of current models in handling diverse and complex captioning scenarios.

### Weaknesses
1. The dataset's focus on home environments and its relatively small size (17,674 images) may limit its generalizability. The exclusive focus on indoor, home-like settings restricts the dataset's ability to evaluate models in diverse real-world scenarios, such as outdoor environments, industrial settings, or public spaces. Furthermore, the dataset size, while not insignificant, may not be sufficient to train robust models capable of generalizing to unseen data distributions. The limited variety in scene types could lead to models that overfit to the specific characteristics of home environments.
2. Not including state-of-the-art models like BLIP2 or LLM-based models in the analysis. The absence of evaluations using current state-of-the-art models, particularly those leveraging large language models (LLMs) such as BLIP2, significantly undermines the paper's claim of assessing the current performance landscape in image captioning. The omission of these models makes it difficult to ascertain the true extent of the performance gap between human and machine-generated captions, as these models have shown substantial improvements in other vision-language tasks.
3. The human-centric approach, while insightful, may introduce new biases and subjectivities. While the use of human evaluation is valuable, the study does not sufficiently address the potential for bias in human judgments. Factors such as individual annotator background, cultural context, and personal preferences could influence the evaluation results, making it difficult to ensure consistency and objectivity. The paper lacks a rigorous analysis of inter-annotator agreement and the potential impact of these biases on the overall findings.
4. The cost and scalability of HUMANr in large-scale applications are not addressed. The practicality of using HUMANr for large-scale evaluations is unclear. The paper does not discuss the cost implications of employing human annotators for large datasets and the potential challenges in scaling up the evaluation process. This lack of discussion raises concerns about the feasibility of using HUMANr in real-world applications.
5. The revelation of a performance gap between humans and models is not a novel insight and lacks depth without comparing the most advanced models. The paper's main finding, that there is a performance gap between human and model-generated captions, is not particularly novel. This gap has been widely acknowledged in the field. Without a comparison to the most advanced models, the paper fails to provide a significant contribution to the understanding of the current state of the art in image captioning. The lack of depth in this analysis weakens the overall impact of the paper.
6. The paper omits crucial experimental details, like the computation of HUMANr and handling discrepancies in human evaluations. The methodology lacks crucial details, specifically regarding how HUMANr is computed and how discrepancies in human evaluations are handled. The absence of these details makes it difficult to reproduce the results and evaluate the validity of the conclusions. Without a clear explanation of the aggregation process for human ratings, the reliability of the HUMANr metric is questionable.

### Questions
1. How can the ObjectNet Captions dataset be expanded to cover a broader range of environments and scenarios?
2. What steps can be taken to include state-of-the-art models like BLIP2 in future evaluations?
3. How does HUMANr address the subjectivity and potential bias in human judgment?
4. Are there plans to adapt the dataset and HUMANr for non-English languages or diverse cultural contexts?
5. How can the scalability and cost-effectiveness of HUMANr be improved for widespread adoption?
6. Can the authors provide more details on the methodology, especially regarding the computation of HUMANr and the management of subjective human ratings?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper focuses on the task of image captioning and proposes a new dataset and a new metric. There are some findings, for example, there is a large gap betten human and models on the task of image captioning. The proposed dataset if challenging compared with existing ones, which contains much more unique tokens and n-grams and should be useful for the community.

### Strengths
1. a new dataset is proposed. The dataset is more challenging and contains more unique tokens and n-grams.
2. a new metric is proposed.
3. analysing existing models vs. human using a wide range of metrics.

### Weaknesses
1. the scale of the dataset is small. 
2. the auther only considers traditional image captioning models. Some LLM-based models like LLaVA should be considered and the comparison among these models should be more interesting.
3. the findings that there is a large gap betten human and models is a common sense, so I do not think it is a significant contribution. But if the author can show that the most advanced models like GPT-4v is inferior to humans and the proposed metric is able to measure the gap, it should be more interesting.

### Questions
Some important references related to image captioning metrics are missing.
1. Learning to evaluate image captioning. CVPR 2018.
2. Describing like humans: on diversity in image captioning, CVPR 2018.
3. On diversity in image captioning: metrics and methods, TPAMI, 2022.

### Soundness
3 good

### Presentation
3 good

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
To evaluate the captions generated by machines, this paper collected a dataset and proposed a new human study protocol. The machine-generated captions are compared with human-generated captions and humans are involved in the evaluation loop. The human study is performed on three datasets, i.e., COCO, Nocaps, and ObjectNet Captions. Three models are evaluated in this experiment, i.e., GIT, ClipCap, ExpNet.

### Strengths
This paper focuses on an important problem for the image captioning community, i.e., how big is the difference between machine generate captions and human-generated captions.
The conclusion that the machine-generated captions still underperform human-generated captions on unusual datasets and fail to generate long sentences is insightful for the community.

### Weaknesses
However, there are several unclear questions need clarification.

1. Apart from revealing how big is the difference between machine-generated captions and human-generated captions, it would be meaningful to reveal what is the difference between machine-generated captions and human-generated captions. Though the authors have revealed some differences, such as spurious objects and caption lengths, the root cause seems still unclear. The analysis of differences remains superficial. For example, while the authors mention spurious objects, they don't delve into the types of objects that are spuriously generated or the contexts in which these errors occur. A more detailed analysis, perhaps categorizing the errors based on object classes or scene complexity, would be beneficial. Similarly, simply stating that caption lengths differ is not sufficient; an analysis of the semantic content and information density of captions of varying lengths is needed. 

2. Some experiment details are missing. For instance, how to compute the HUMANr score? The description of the HUMANr score is insufficient to allow for replication. The authors should provide a step-by-step explanation of how the raw human ratings are transformed into the final HUMANr score, including any normalization or aggregation methods used. Without this level of detail, it is difficult to assess the validity and reliability of the metric.

3. Asking human participants to rate between 1-9 seems subjective. If two new image captioning models are evaluated with two different groups of people, will the results be comparable? It would be interesting to show the deviation of two different groups of people rating the same model in Figure 4. The subjective nature of the 1-9 rating scale introduces a potential source of bias. The authors should provide evidence that the results are consistent across different groups of human raters. Showing the inter-rater reliability or the variance in scores across different groups would strengthen the validity of the findings. Furthermore, it would be beneficial to discuss the potential impact of individual rater biases on the overall results.

4. The ObjectNet cannot be regarded as a contribution as the authors only select some images with longer captions.

### Questions
In Section 4.3, paragraph 2, what does ``we eliminated all images where GITL failed any of the seven checks above—human failures were not considered’’ mean?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces ObjectNet Captions, a dataset created to mitigate the exploitation of spurious correlations by machine learning models in image captioning tasks. Along with this dataset, the authors present HUMANr, a novel captioning metric aimed at providing a robust and consistent measure of performance that can be easily replicated and crowdsourced. HUMANr is intended to be an absolute performance metric that provides a clear target for model improvement and the ability to recognize when human-level captioning has been achieved, addressing the overestimation of machine performance by current metrics.


# Post-rebuttal
I appreciate the efforts made by the author. Their responses partially address my concern about the comparison and the scale of dataset. Therefore, I raise my rating. I encourage the author to make their proposed dataset and metric easily to use, such as can easily download and running via `pip`, to let people use them in practical ways.

### Strengths
There are several strengths for this paper:

- Introduction of a new dataset that targets a key issue, specifically the reliance on spurious correlations by captioning models. 
- Development of HUMANr, and it can be easily implemented and crowdsourced.
- Potential to recalibrate the understanding of machine captioning performance, as HUMANr contrasts with existing metrics by showing the superiority of human captions.
- The paper provides tools for automatic computation of HUMANr (in supplementary), facilitating its adoption by the research community.
- It examined several learning-based Captioning models and metrics.

### Weaknesses
I feel there are two major flaw points:

- The authors currently did not use GPT-related captioning models, such as BLIP2. According to my usage, BLIP2 outperforms the compared methods used in this paper.

-  The proposed dataset only contains 17,674 images which are quite small-scale to evaluate a captioning model comprehensively.

### Questions
Please address the concerns mentioned above. 

Could the author please also provide random sampled image-captions pairs. The current appendix only contains a few examples which cannot be assessed comprehensively.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
