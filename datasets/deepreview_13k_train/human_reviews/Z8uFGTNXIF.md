# Simplifying Referred Visual Search with Conditional Contrastive Learning

- Decision: Reject
- Scores: 6, 5, 5

## Abstract
This paper introduces a new challenge for image similarity search in the context of fashion, addressing the inherent ambiguity in this domain stemming from complex images. We present Referred Visual Search (RVS), a task allowing users to define more precisely the desired similarity, following recent interest in the industry. We release a new large public dataset, LAION-RVS-Fashion, consisting of 272k fashion products with 842k images extracted from LAION, designed explicitly for this task. However, unlike traditional visual search methods in the industry, we demonstrate that superior performance can be achieved by bypassing explicit object detection and adopting weakly-supervised conditional contrastive learning on image tuples. Our method is lightweight and demonstrates robustness, reaching Recall at one superior to strong detection-based baselines against 2M distractors. Code, data, and models will be released.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper aims at fashion retrieval conditioned on images and texts. Particularly, the text conditions can be categories and captions. This task is tackled via learning the joint embedding of texts and images, similar to conventional multi-modal metric learning methods. A dataset that is extracted from the publicly available dataset LAION-5B is constructed to validate the proposed method.

### Strengths
1. The proposed dataset can facilitate research on multi-modal fashion retrieval.
2. Extensive experiments have been conducted to provide insightful information on this task.
3. The writing of this paper is excellent and easy to follow.

### Weaknesses
1. Although this paper claims its target task is new, I still consider it to belong to multi-modal fashion retrieval. That is, one can include classes, attributes, captions, or even negative prompts in the textual conditions, and then leverage LLMs to process them uniformly. 
2. The failure cases suggest image features are dominant, and hence the proposed method or the task might not be as convenient as it claims. For example, what if the user wants to find clothes with similar styles but different colors, or of the same brand? Moreover, the text conditions seem rather simple, so whether the proposed method can handle fine-grained queries is unclear.
3. The comparison between the proposed method and SOTAs might be unfair, e.g., ASEN is implemented partially and it only uses attributes. Other baselines with similar architectures, like FashionBert should be considered as well. Besides, how is the performance of the proposed method on other fashion retrieval benchmarks?

### Questions
Please refer to the weakness part. I will adjust my score according if my concerns can be addressed.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a new task, named Referred Visual Search (RVS). It aims to search the specific part under the condition of category. The new task sounds good. The authors also introduce a corresponding dataset and framework. Some experimental results look good.

### Strengths
## Strengths

1. The writing is good. It is easy to follow this paper.

2. The motivation sounds reasonable.

3. Some experimental results look good.

### Weaknesses
## Weaknesses

1. It may be not appropriate to use the entire image (even given the conditions) to search for an part area, such as pants. The spatial context of the entire image might introduce irrelevant noise and hinder the model's ability to focus on the specific part. For instance, the background or other clothing items in the image could confuse the model when trying to locate the pants region.

2. Why not crop the part area according to the given condition and then use it to search? This approach could potentially improve search accuracy by eliminating irrelevant image content and focusing the model's attention on the target region. It is unclear why the authors chose to use the entire image instead of a more targeted approach.

3. How to collect the LAION-RVS-Fashion dataset? How to ensure the accuracy of the labels? The original labels are not clear. The lack of clarity regarding the data collection process and label verification raises concerns about the reliability and quality of the dataset. Specifically, what measures were taken to ensure that the bounding box annotations accurately correspond to the referred part?

4. The main content of this paper has 10 pages.

### Questions
Please see above.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes a new task called referred visual search. A new dataset is also created to achieve this task. This paper uses contrastive learning for extracting referred embeddings. Experiments achieve promising results in different tasks in LRVS-F dataset.

### Strengths
1. This paper proposes a challenging task for image similarity search in the context of fashion. A new dataset is also proposed at the same time.
2. Conditional embedding is properly used to achieve this task. Experiments demonstrate the effectiveness of the method.
3. This paper can be a baseline to do more relevant work.

### Weaknesses
1.This task is similar to composed image retrieval. Composed image retrieval aims to find the target image based on the reference image and text description. I have some doubts about the contribution and meaning of the task. 
2.The structure of the model is simple. It lacks innovation. The description of the model is not specific enough. Contrastive learning is often used in the task of composed image retrieval, so it is not an innovative method.
3.Experiments are basically a comparison with other models, but the ablation experiment of your own model and visualization is lacking.

### Questions
1. You say it extracts referred embedding using weakly-supervised training. Why it is a weakly-supervised training?
2. In fig2, it shares weight between the two vision transformers. In this model, it is whether all parameters are shared or only parts of the parameters are shared. And I want to know why to share the weight.
3. In table1 and table2, you say you report bootstrapped means and standards deviations for 0K distractors, but I don’t see the result of the 0K distractors. In addition, your model is similar to some models that used in the task of composed image retrieval. FashionIQ is also a dataset about clothes. Do you try this dataset using your method?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
