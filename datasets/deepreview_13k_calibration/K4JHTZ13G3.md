# Screener: Learning Conditional Distribution of Dense Self-supervised Representations for Unsupervised Pathology Segmentation in 3D Medical Images

- Decision: Reject
- Avg Score: 5.33
- Scores: 5, 5, 6

## Abstract
Accurate and automated anomaly segmentation is critical for assisting clinicians in detecting and diagnosing pathological conditions, particularly in large-scale medical imaging datasets where manual annotation is not only time- and resource-intensive but also prone to inconsistency. To address these challenges, we propose Screener, a fully self-supervised framework for visual anomaly segmentation, leveraging self-supervised representation learning to eliminate the need for manual labels. Additionally, we model the conditional distribution of local image patterns given their global context,  enabling the identification of anomalies as patterns with low conditional probabilities and assigning them high anomaly scores.

Screener comprises three components: a descriptor model that encodes local image patterns into self-supervised representations invariant to local-content-preserving augmentations; a condition model that captures global contextual information through invariance to image masking; and a density model that estimates the conditional density of descriptors given their global contexts to compute anomaly scores.

We validate Screener by training a fully self-supervised model on over 30,000 3D CT images and evaluating its performance on four large-scale test datasets comprising 1,820 3D CT scans across four chest and abdominal pathologies. Our framework consistently outperforms existing unsupervised anomaly segmentation methods. Code and pre-trained models will be made publicly available.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces a self-supervised method for anomaly segmentation in 3D medical images. The model architecture includes a descriptor, condition, and density module. However, the paper lacks clarity in its presentation, with limited explanations and no figures to illustrate the pipeline, making it challenging to grasp the overall workflow and novelty of the approach.

### Strengths
1. This work introduces a large-scale dataset on pathology segmentation, integrating data from NLST, AMOS. AbdomenAtlas.
2. This work aims to solve the meaningful problem of self-supervised pathology segmentation.
3. Lacks the statistics of the claimed large dataset. The author should summarize and describe this dataset in detail.

### Weaknesses
1. This work is poorly written and lacks clarity in conveying its high-level concept. The descriptions of the descriptor, condition, and density models are unclear, and there are no experiments demonstrating the effectiveness of these components.
2. A pipeline illustration figure is recommended to show the workflow of this work.
3. Lacks the statistics of the claimed large dataset. The author should summarize and describe this dataset in detail.

### Questions
1. Add a figure to show the pipeline of this work.
2. Add the summary for the dataset statistics, such as size, density, pathology distribution.
3. Add experiments/qualitative comparison to demonstrate the effectiveness of proposed components

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper presents SCREENER, a self-supervised framework for anomaly segmentation in 3D medical CT images, specifically aimed at pathology detection. SCREENER learns conditional distributions of dense self-supervised representations, assigning higher anomaly scores to patterns with low conditional probability. This method includes three components: (1) a descriptor model that encodes local patterns, (2) a condition model encoding global context, and (3) a density model estimating the likelihood of descriptors, yielding anomaly scores for segmentation. Trained on 30,000 CT scans, SCREENER outperformed existing unsupervised anomaly segmentation methods across multiple pathologies, showcasing its potential in large-scale, label-scarce medical imaging tasks.

### Strengths
+ **Comprehensive Introduction and Related Work:** The introduction and related work sections are thorough and well-written. They offer a solid overview of existing methods in medical anomaly segmentation and clearly highlight their limitations, supported by relevant examples from the literature.

+ **Extensive Training Dataset:** The model is trained on a dataset of over 30,000 3D CT scans, which is a significant advantage for self-supervised learning. This large dataset aids in accurately modeling the distribution of healthy CT images, allowing the model to distinguish normal from abnormal patterns more effectively.

### Weaknesses
 - **Unclear Illustration of the Proposed Method:** The method section lacks clarity on what parts are novel contributions versus prior work. For example, Section 2.3 largely describes existing techniques, such as SimCLR and VICReg, but it’s unclear how much these influence the new SCREENER model. The paper would benefit from clearly marking new contributions at the start of each subsection and relegating baseline methods to the experimental settings section. A figure illustrating the architecture would greatly improve comprehensibility. The description of how SimCLR is used to generate 'dense features' is particularly vague, given that SimCLR is typically used for image-level representation learning, not dense feature extraction. The paper needs to specify how the SimCLR framework is adapted to produce dense feature maps suitable for pixel-level anomaly detection.

- **Inappropriate Metric Selection:** The paper focuses on anomaly segmentation, yet uses anomaly detection metrics (AUROC) rather than segmentation-specific metrics, such as Dice Similarity Coefficient (DSC), Intersection over Union (IoU), Hausdorff Distance (HD), or Normalized Surface Distance (NSD). Without these, it’s difficult to assess the model's effectiveness in precise segmentation of anomalies. The use of pixel-level AUROC is especially problematic because it does not account for the spatial contiguity of the predicted anomalies. A model could achieve a high AUROC by correctly identifying a small number of anomalous pixels scattered throughout the image, without accurately segmenting the actual anomaly regions. This makes it difficult to evaluate the practical utility of the method for tasks requiring precise delineation of pathological areas.

### Questions
1. Clarify Novelty in SCREENER: The proposed SCREENER method claims to modify the density-based UVAS framework but lacks clarity on what modifications were made and their specific advantages. Clear differentiation of new versus existing components would help readers understand the proposed method’s originality.

2. Dense Features Learned by SimCLR: The paper states that SimCLR learns “dense features” (lines 81-82), but this is misleading as SimCLR typically captures global features to distinguish one image from another. Defining what is meant by "dense features" here and how SimCLR is adapted for this purpose would improve accuracy.

3. Define Key Terms: Essential terms like "conditional distribution," "local image patterns," and "global image content" are insufficiently explained, making the method challenging to follow. Definitions and possibly examples would clarify the underlying assumptions and techniques used.

4. Figure 1 Anomaly Map Clarity: In Figure 1, the second column shows an image flagged as diseased (as indicated by attention maps), yet lacks a mask. A mask in this column or clearer labeling would clarify the model's detection process.

5. AUROC Use for Segmentation Tasks: AUROC is not ideal for segmentation tasks, which typically require spatial accuracy. Metrics like HD or NSD would provide more nuanced insights into segmentation quality, particularly for edge or boundary delineation.

### Soundness
3

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
5

### Summary
This paper introduces SCREENER, a fully self-supervised framework for anomaly detection in 3D CT images. SCREENER learns a conditional distribution of dense image patterns, leveraging a descriptor model and conditional density model to assign anomaly scores based on rarity. The method shows promising performance on several CT pathology datasets, though some aspects could benefit from further clarity, additional benchmarks, and comparisons.

### Strengths
Promising Results: SCREENER achieves impressive results across multiple datasets, particularly given its unsupervised nature. The method could advance anomaly detection in settings with limited labeled data.

Use of Conditional Density Modeling: The paper’s approach to conditioning on context in the density model is innovative and contributes to improving detection accuracy by simplifying anomaly scoring.

Effective Self-Supervised Learning Approach: SCREENER’s use of self-supervised pretraining on a large CT dataset provides a valuable alternative to supervised feature extractors, addressing the scarcity of annotated medical images.

### Weaknesses
Limited Comparative Evaluation: While SCREENER shows good performance on mixed CT datasets, it is challenging to assess its true impact due to the limited number of similar baseline methods for comparison. Including a maximum Dice score comparison to supervised SOTA or additional metrics from benchmarks like MOOD would allow for a clearer evaluation. The lack of a Dice score comparison is particularly concerning given that the method is ultimately intended for segmentation, and without this metric, it's difficult to gauge the practical utility of the method compared to existing segmentation approaches, even if they are supervised. The paper should clarify how the anomaly scores relate to segmentation performance.

Lack of Standard Dataset Benchmarks: Although the authors focus on CT images, adding results on a standard brain dataset would help position SCREENER relative to established anomaly detection methods and increase its comparative strength even if this is not the primary goal of the work. The absence of such benchmarks makes it difficult to understand how SCREENER would perform in a different modality or on different types of anomalies, limiting the generalizability claims of the study. Specifically, the paper should include results on a dataset with well-defined and commonly used evaluation metrics for anomaly detection.

Domain Gap Influence: The effect of domain gaps between different CT datasets is not discussed. SCREENER is tested on a single combined dataset, but further analysis of domain variance (standard deviations, confidence intervals) would better inform its generalizability. Clarifying how domain gaps might impact performance is also relevant, as it remains unclear how well SCREENER would generalize to datasets with different characteristics. The paper should include a more rigorous analysis of how the model performs when trained and tested on different subsets of the data, to assess the impact of domain shifts.

Architecture and Sampling Details: The choice of downsampling size (h, w, s), upsampling, and overall architecture needs further discussion to make the design decisions transparent and reproducible. The paper should provide a detailed justification for the specific architecture choices, including the number of layers, filter sizes, and activation functions. The lack of these details makes it difficult to reproduce the results and understand the impact of these design choices on performance.

Related Work and Citations: The paper could improve its citation of related work, including references to early synthetic anomaly detection methods (e.g., FPI) and CRADL, which has a similar structure involving a SIMCLR pretrained encoder and Gaussian/flow-based density models. Additionally, work on applied studies on anomaly scoring could enhance the background section. The paper should also discuss the limitations of existing methods and how SCREENER addresses these limitations.

Clarity and Detail in Writing: The paper is somewhat unclear, with missing details that could make its contributions and methodology more convincing. For example, some claims (such as those about density models or scale of CT data) are not fully supported, and the paper’s writing could more clearly convey the innovations and unique aspects of SCREENER. The paper should provide more concrete examples and visualizations to support its claims.

Overlapping Test and Training Data: Some test sets, like LiTS and KiTS, are partially represented in the training dataset AbdomenAtlas, which could raise concerns about test set contamination. While this overlap may not significantly affect results, a clear discussion of this issue is necessary to address any potential impacts. The paper should provide a clear statement regarding the independence of the training and test sets, and if there is any overlap, the potential impact should be discussed.

### Questions
Can you provide results for a maximum Dice score comparison with a supervised SOTA model to better position SCREENER’s effectiveness?

How does SCREENER perform on standard anomaly detection datasets (e.g., brain datasets), and would such benchmarks enhance the comparability of results?

Could you elaborate on the potential influence of domain gaps across different datasets in SCREENER’s performance, and is there any analysis of variance across domains?

How do choices like downsampling size, h, w, s, and upsampling affect SCREENER’s performance, and could these details be further specified?

How do you address the overlap of training and test datasets, specifically with parts of LiTS and KiTS also in AbdomenAtlas?

### Soundness
4

### Presentation
3

### Contribution
3
