# Exposing Text-Image Inconsistency Using Diffusion Models

- Decision: Accept
- Avg Score: 6.00
- Scores: 8, 5, 5, 6

## Abstract
In the battle against widespread online misinformation, a growing problem is text-image inconsistency, where images are misleadingly paired with texts with different intent or meaning. Existing classification-based methods for text-image inconsistency can identify contextual inconsistencies but fail to provide explainable justifications for their decisions that humans can understand. Although more nuanced, human evaluation is impractical at scale and susceptible to errors. To address these limitations, this study introduces D-TIIL (Diffusion-based Text-Image Inconsistency Localization), which employs text-to-image diffusion models to localize semantic inconsistencies in text and image pairs. These models, trained on large-scale datasets act as ``omniscient" agents that filter out irrelevant information and incorporate background knowledge to identify inconsistencies. In addition, D-TIIL uses text embeddings and modified image regions to visualize these inconsistencies. To evaluate D-TIIL's efficacy, we introduce a new TIIL dataset containing 14K consistent and inconsistent text-image pairs. Unlike existing datasets, TIIL enables assessment at the level of individual words and image regions and is carefully designed to represent various inconsistencies. D-TIIL offers a scalable and evidence-based approach to identifying and localizing text-image inconsistency, providing a robust framework for future research combating misinformation. Please refer \href{https://mingzhenhuang.html}{Project Page} for source code and dataset.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies how to detect image-text inconsistency with diffusion models. More specifically, the author designed a pipeline that iteratively use diffusion models to edit the text and images in the image-text pairs to gradually optimize a mask that can point out where the inconsistency come from. This task is interesting and meaningful for misinformation detection, as it provides interpretable prediction results. To evaluate the proposed method, the authors collected a dataset containing image-text pairs and their inconsistency masks. Experiments shows that the proposed method outperforms baselines and gives explanable prediction on the inconsistency.

### Strengths
1. The task studied in this paper is meaningful.

2. The dataset that they collected is contributive to the community.

3. The method is novel.

### Weaknesses
1. The writing is not very good. I read the methodology part several hours to understand their pipeline.

2. The idea is well justified for the inconsistency of object alignment. But what if the predicate is not aligned, i.e. the person is correct but the action is not?

### Questions
How does the annotation and the model handles predicates?

### Soundness
3 good

### Presentation
2 fair

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents D-TIIL for identifying and localizing inconsistencies between text and images. 
A new dataset, TIIL, containing 14K consistent and inconsistent text-image pairs, is introduced for evaluating the method. The D-TIIL outperforms existing approaches in terms of Accuracy scores and demonstrates more explainable results. In a nutshell, the paper offers a scalable and evidence-based approach to identify and localize the text-image inconsistency. However, it also acknowledges the potential misuse of the method for creating deceptive text-image pairs and suggests improving the algorithm and restricting access.

### Strengths
1. Originality: The paper introduces a novel method, D-TIIL, that exposes text-image inconsistency with the location of inconsistent image regions and words. Also, the new TIIL dataset is the first dataset with pixel-level and word-level inconsistency features that provide fine-grained and reliable inconsistency.

2. Quality: The D-TIIL and TIIL dataset generation are thoroughly described. The paper also provides a comprehensive comparison of the proposed method with existing approaches.

3. Clarity: The paper is well-structured and clearly written. The method is explained in detail and the experiment results are presented in an understandable manner.

4. Significance: The D-TIIL method improves the accuracy of inconsistency detection and provides more explainable results. The introduction of the diffusion model makes it possible to align text and images in a latent and joint representation space to discount irrelevant information and incorporate broader knowledge.

### Weaknesses
1. The paper acknowledges that the D-TIIL may struggle with inconsistencies with respect to specific external knowledge, and this could reduce the effectiveness of the method in real-world application.

2. The D-TIIL method relies heavily on the text-to-image diffusion models and benefits a lot from the semantic space that is already well aligned. This dependence could limit the generalizability of the proposed method. Specifically, if the diffusion model's text and image embeddings are not well-aligned, the method's performance will likely degrade significantly. This is a critical limitation as the method's effectiveness is contingent on the quality of the underlying diffusion model.

3. There are some confusing details in the method description section.

4. In the comparison of methods, the reasons why D-TIIL is superior are not discussed and analyzed in detail, and the potential solutions for the failure cases are not provided. The paper lacks a thorough analysis of the specific scenarios where D-TIIL excels or fails compared to the baselines. Without this analysis, it's difficult to understand the method's strengths and weaknesses.

5. More specific discussions and measures could be included to prevent potential abuse rather than simply restricting access.

### Questions
1. Regarding Step 3 in Section 3 METHOD, the proposed E_{dnt} and descriptions like “include extra implicit information from the images and excludes additional implicit information that only appears in the text” raise doubts about the effectiveness of the process of the “text denoising”. Such “text denoising” seems to be too idealistic. In Section 5.4, for example, there is the failure case of the word "office". This leads to the bold suspicion that the D-TIIL method is only valid for simple objects, but not for backgrounds or objects that contain more complex semantics.

2. Also, the high dependency on the diffusion model affects the generalizability of the method. If text and image are not well aligned on the latent space, the validity of the method will be more affected. Semantic entanglement can also exist.

3. Regarding Step 4 in Section 3 METHOD, the descriptions like “We then compute the cosine similarity score between this image embedding and the input text embedding” are confusing to the readers.

4. In the Data Generation part of Section 4 TILL DATASET, T_{m} is unknown where it comes from, is it manually designed?

### Soundness
3 good

### Presentation
2 fair

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
The authors propose D-TIIL (Diffusion-based Text-Image Inconsistency Localization), a system for automatically identifying and explaining text-image inconsistencies. D-TILL uses text-image diffusion models to locate semantic inconsistencies in text-image pairs. Diffusion models trained on large datasets filter out irrelevant information and incorporate background knowledge to identify inconsistencies. In addition, D-TIIL uses text embeddings and modified image regions to visualize these inconsistencies.
To evaluate the effectiveness of D-TIIL, the authors also introduce a new dataset (TIIL) with 14K consistent and inconsistent text-image pairs.

### Strengths
•	The paper is well written and well structured
•	The problem and the related work are well introduced
•	The framework is explained in detail
•	The idea to build consistency scores between stable diffusion and the original image is interesting.

### Weaknesses
•	The general theoretical idea behind the approach lacks clearity
•	The real-world application is not very clear, e.g. wrong labels have a different type of mislabeling than just objects that are swapped
•	Sensitivity to threshold highly influences M and the consistency score

With D-TIIL, the authors have presented an interesting method for using diffusion models to evaluate the consistency of image-text pairs.
However, the utility of the method is not fully evaluated in detail. Deeper insights into why this approach works are lacking. In addition, it would be nice to see how the approach works on other datasets where the labeling is just mixed up or misleading.
In addition, I would recommend for ICLR to investigate the method in more detail in terms of learned representations.

The paper is well written and has some interesting ideas, e.g. the usage of diffusion models for detecting image-text inconsistency. The method and the dataset, both are valuable. However, to be accepted in ICLR I would expect more and deeper investigations about the method and the dataset. What is learned, what are short comings?
There are some doubts, such that the model could be sensitive to the DALE generated part instead being sensitive to the text-image inconsistency. Experiments are missing that evaluate the underlying behavior. Moreover, a second evaluation on another dataset with more established baselines would be preferable to proof some of the assumptions, advantages and shortcomings of the method.

### Questions
•	How does the approach perform on completely wrong image descriptions?
o	Is the whole image masked?
•	Is the model sensitive to the image part generated by DALE and not to the parts which do not correspondent to the text?
o	Is there an experiment that can proof that?
o	Maybe regenerate the image for the dataset also with the right semantic class?
•	Is there another dataset where the method could be compared also to other baselines?

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
This paper develops a new method, D-TIIL, to expose text-image inconsistency with the location of inconsistent image regions and words, which is quite commonly happening in T2I generation diffusion models. To achieve this, they introduce a new dataset, TIIL, for evaluating text-image inconsistency localization with pixel-level and word-level inconsistency annotations.

### Strengths
1. The dataset's contribution is commendable. Existing datasets lack the capacity to furnish evidence regarding inconsistencies occurring at both the image region and word levels, which is essential for evaluating D-TIIL (Diffusion-Based Text-to-Image Inconsistency Localization).

2. The problem addressed in this research is of significant importance. Previous methods have primarily focused on determining the presence of inconsistencies, whereas this paper introduces a novel approach to pinpointing the specific locations where these inconsistencies occur.

### Weaknesses
1. It would be valuable to explore whether this method could be extended to evaluate other text-to-image (T2I) augmentation techniques (i.e., [1-3]). Given the abundance of research on generating images based on textual prompts, applying this method for evaluation purposes could have a broader impact and contribute significantly to the field. Specifically, it is unclear how the proposed method would handle more complex augmentations, such as those that involve style transfer or the addition of multiple objects, which are commonly found in recent T2I models. The lack of evaluation on these more complex scenarios limits the generalizability of the proposed approach.

2. Are there alternative evaluation metrics to assess the correspondence between text and images? Based on my experience with CLIP scores, it may not consistently capture performance accurately in various scenarios. For example, CLIP might score an image as highly aligned with the text even if the image contains subtle inconsistencies, such as an incorrect color or shape of an object. This limitation could lead to an overestimation of the performance of T2I models, and it would be beneficial to explore metrics that are more sensitive to these types of inconsistencies.

### Questions
As mentioned in the above weakness, I would appreciate seeing the proposed method applied more extensively in evaluation. The inclusion of evaluation metrics beyond CLIP scores could enhance the robustness and confidence of this paper.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
