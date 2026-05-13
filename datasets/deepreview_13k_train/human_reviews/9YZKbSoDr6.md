# Multi-domain Analysis and Generalization of Image manipulation loCalization

- Decision: Reject
- Scores: 6, 5, 6, 6

## Abstract
Advanced image editing software enables easy creation of highly convincing image manipulations, which has been made even more accessible in recent years due to advances in generative AI. Manipulated images, while often harmless, could spread misinformation, create false narratives, and influence people’s opinions on important issues. Despite this growing threat, current research on detecting advanced manipulations across different visual domains, remains limited. Thus, we introduce Multi-domain Analysis and Generalization of Image manipulation loCalization (MAGIC), a comprehensive benchmark designed for studying generalization across several axes in image manipulation detection. MAGIC comprises over 192K images from two distinct sources (user and news photos), spanning a diverse range of topics and manipulation sizes. We focus on images manipulated using recent diffusion-based inpainting methods, which are largely absent in existing datasets. We conduct experiments under different types of domain shift to evaluate robustness of existing image manipulation detection methods. Our goal is to drive further research in this area by offering new insights that would help develop more reliable and generalizable image manipulation detection methods. We will release the dataset after this work is published.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper primarily builds a Diffusion-based model and constructs an image manipulation localization dataset with 192k images focused on inpainting tampering types. This dataset is divided into three major categories based on source, content topic, and specific types of Diffusion models used, allowing for evaluation of the model's cross-domain generalization performance. The authors evaluated the performance of several SoTA models on this dataset. A survey on human feedback on the quality of this dataset is also reported.

### Strengths
- The motivation is sound, as cross-dataset or cross-domain performance has consistently posed challenges in the field of image manipulation localization. A dataset focused on cross-domain performance analysis would serve as a valuable benchmark.
- Experiments are comprehensive in demonstrating the utilization of each protocol.

### Weaknesses
## Main issue
- Although the authors claim to have used clustering for categorizing topics, some topics displayed in Figure 2 seem to vary significantly and do not appear entirely reasonable. For instance, it’s unclear how a bicycle image relates to the "ARTS" category, and both "People" and "Ruins" are grouped under "Media." Additionally, the results across many topic classes in Table 4 are quite similar, suggesting that the distribution between classes may not be as distinct as initially anticipated. The lack of clear semantic boundaries between these categories raises concerns about whether the observed performance differences are truly due to cross-domain generalization or simply overfitting to subtle variations within a single domain. The chosen categories, based on article content rather than image content, may not effectively capture the semantic shifts that are crucial for evaluating cross-domain performance in image manipulation localization.
- A paper [A] proposed in Nov. 2023 on ArXiv and accepted by ACM MM 2024 also uses Visual News and COCO to create a fine-grained diffusion and GAN-generated dataset. I understand that ACM MM was held after ICLR submission. However, the two articles have considerable similarities in the background, purpose, and subject matter. While the two papers represent distinct works, it is recommended to discuss [A] in the Related Work section and reconsider the claim in line 149 regarding being the "first diffusion-based manipulation dataset." Since [A] retains the text prompts associated with images, which, with proper handling, could serve as a more accurate basis for topic categorization.
- For dataset-focused papers, it’s common to include tests with standard vision backbones, such as ResNet or Swin, to provide more straightforward benchmarks. Including these could serve as helpful references for comparison.

## Minor issue
- Many AUC metrics in the tables are too close, showing little distinction and some values are excessively low. For instance, Table 3 includes numerous metrics below 0.5, indicating that the model has not effectively learned the corresponding distributions. More distinctive metrics, such as F1 or IoU, may be needed better to assess the model’s performance on each protocol.

- The statement between lines 522–524 appears unconvincing. The current explanation does little to clarify why the performance of PSCC is nearly the opposite of the other two models.

### Questions
See the Weakness Section. Overall, this is a solid piece of work. I will consider raising my rating if improve the presentation of details.

### Soundness
3

### Presentation
2

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
This paper introduces “MAGIC,” a large-scale dataset designed to evaluate the robustness and generalization of image manipulation detection models across multiple domains. MAGIC aims to assess model performance under various domain shifts, including different image sources, manipulation types, semantic topics, and manipulation scales. Results indicate that while the models perform well in distribution (ID), their OOD performance is limited, highlighting the challenges of domain generalization in image manipulation detection.

### Strengths
- MAGIC addresses a pressing issue in image manipulation detection by offering a large-scale dataset with a focus on domain generalization across multiple dimensions. This effort is commendable and fills a gap in manipulation detection research.

### Weaknesses
 - The proposed dataset, while diverse, does not introduce fundamentally new manipulation detection methods or models. The dataset’s construction (e.g., sourcing from MS COCO and VisualNews, manipulation types) is novel but does not demonstrate significant methodological innovation beyond combining existing datasets and manipulation techniques. Thus, the contribution is more incremental than groundbreaking.

- The paper lacks a detailed comparison with other recent datasets or techniques, and the experiments primarily rely on existing architectures without substantial modifications or improvements. The work’s dependence on pre-existing models for analysis and lack of new methodological contributions weaken its overall technical impact.

I am not an expert in this field. But I think that a dataset for image manipulation localization is not sufficient for publication at ICLR.

### Questions
See weakness.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposed a new image manipulation location benchmark for diffusion-based generation methods. It contains two image sources and seven manipulation techniques. The experiments under several settings, also provide some interesting insights.

### Strengths
1. The proposed datasets seem good for image manipulation location tasks.
2. The writing and experiments are pretty good.

### Weaknesses
1. The quality of the manipulated images in Figure 2 is worrying, especially for the removing class. Although the authors mentioned that they apply human evaluation for the generated images, I'm worried about the data balance of the three categories (removal, replacement, and insertion) under high-quality annotations. Specifically, the removal manipulations often leave noticeable artifacts, which could bias the detectors to focus on these specific flaws rather than learning more generalizable manipulation patterns. This is a concern because the detectors might be learning to identify the specific artifacts created by the removal process, rather than the manipulation itself, which could lead to poor generalization to other removal methods or real-world scenarios.
2. The image manipulation methods used in the paper are not very new. Using SD series, like SD2, or even SDXL is better. The current methods might not capture the nuances of more recent diffusion-based manipulations, which could limit the applicability of the benchmark. The lack of more advanced methods also makes it difficult to assess the robustness of the detectors against state-of-the-art manipulation techniques. This is a significant limitation given the rapid advancements in diffusion models.
3. In Table 3, it's interesting that the OOD score is higher than the ID score when trained on MAGIC-News and tested on MAGIC-COCO. It's better to provide a more depth analysis. The fact that out-of-distribution performance exceeds in-distribution performance is counterintuitive and suggests that the models might be overfitting to the specific characteristics of the training data, or that the evaluation setup is not properly capturing the generalization capabilities of the detectors. A deeper analysis is needed to understand the underlying reasons for this unexpected behavior.

### Questions
Please see the weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces two novel datasets for image forensics specifically curated from diffusion-based editing methods: MAGIC-News and MAGIC-COCO. These datasets encompass various topics and object classes, with manipulations including object insertion, replacement, and removal, applied through various editing techniques such as Stable Diffusion, Blended Diffusion, Glide Diffusion, and Adobe Firefly. Experiments demonstrate the performance of several image forensic techniques on these new datasets.

### Strengths
+ Propose new datasets that cover many situations: news (MAGIC-News) or daily lives (MAGIC-COCO)
+ Cover many editing operations: insertion, removal, and replacement
+ Include many editing techniques: Stable Diffusion, Blended Diffusion, Glide Diffusion, and Adobe Firefly.

### Weaknesses
Since this paper mainly focuses on new datasets, the presentation of the datasets should be prepared more carefully. Specifically:
+ Lack of high-quality examples of manipulated images and corresponding GT segmentation mask (Fig. 2 presents low-resolution images)
+ Instead of just listing some numbers only, the visual charts should be used to summarize the statistics of datasets (e.g., editing areas statistics
+ A table of Editing technique summarization would also help, including the number of images, and examples. 
+ For the Dataset Quality Survey, using a flowchart to visualize the process would be better. 
+ Lack of reporting IoU (along with AUC)
+ Lack of classification performance (decide whether an image is a manipulated image or genuine one)
+ The quality of the proposed dataset is a concern (Tab. 6) since some methods are just around 50%)
+ Demonstration of using the proposed datasets would help the performance of detection techniques on other datasets such as MagicBrush [a] and CocoGLIDE [b].

### Questions
+ How to make sure the quality of the generated masks for MAGIC-News (since they are generated automatically from Mask2Former)
+ For the replacement operation, have you tested different-class replacements instead of same-class replacements
+ How to ensure the quality of GLIGEN since it is not a perfect method, any mechanism to ensure its quality?
+ How many images are used for training, val, test, and out-of-domain subsets?

### Soundness
2

### Presentation
2

### Contribution
2
