# AdaSR: Adaptive Super Resolution for Cross Platform and Dynamic Runtime Environments

- Decision: Reject
- Avg Score: 4.50
- Scores: 5, 3, 5, 5

## Abstract
Image super resolution models (SR) have shown great capability in improving the visual quality for low-resolution images. Due to the compute and memory budgets of diverse platforms, e.g., cloud and edge devices, practitioners and researchers have to either (1) design different architectures and/or (2) compress the same model to different levels. Additionally, a majority of the works in current literature aim to achieve state-of-the-art performance by hand-designing singular efficient models. However, even on the same hardware, the compute resource dynamics change due to other running applications. As such, one single model that satisfies required frames-per-second (FPS) when executed in isolation may not be suitable when other running applications present. To overcome those issues, we propose AdaSR, an Adaptive SR framework via shared architecture and weights for cross platform deployment and dynamic runtime environment. Unlike other works in literature, our work focuses on the development of multiple models within a larger meta-graph such that they can fulfill latency requirements by compromising as little performance as possible. Particularly, AdaSR can be used to (1) customize architectures for different hardware (e.g., different security cameras), and (2) adaptively change the compute graph in dynamic runtime environment (e.g., mobile phones with concurrently running applications). Different than prior arts, AdaSR achieves this by adaptively changing the depth and the channel size with shared weights and architecture, which introduces no extra cost on memory and/or storage. To stabilize the shared weight training of AdaSR, we propose a progressive approach where we derive loss functions for each block and function matching operations with max-norm regularization to address dimension mismatches. We extensively test AdaSR on different block-based GAN models, and demonstrate that AdaSR can maintain Pareto optimal performance in terms of latency vs. performance tradeoff with much smaller memory footprint and support dynamic runtime environments.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes an adaptive SR framework, AdaSR, for cross-platform deployment and dynamic runtime environment. AdaSR can be implemented in existing SR models and achieves a promising tradeoff between latency and performance.

### Strengths
+ This is well-motivated for practical applications of SR models. The paper is easy to follow.
+ The proposed method can achieve a good balance between latency and performance.

### Weaknesses
Although I greatly appreciate the motivation for practical applications of SR methods in diverse platforms, my main concern is about the empirical evaluation of the effectiveness. 

- As claimed in the paper, "none ... address the challenges in dynamic runtime environment ..." and the proposed AdaSR aims to address this issue. It is confusing and ambiguous for the experiment settings for the cross-platform and dynamic runtime environment. Specifically, the paper does not clearly define what constitutes a 'dynamic runtime environment' in the context of SR. Is it varying computational resources, changing input resolutions, or other factors? The lack of clarity makes it difficult to assess the validity of the experiments.

- The evaluations for "cross-platform Pareto optimality" (Sec. 4.1) and "dynamic runtime environment" (Sec. 4.2) are conducted on a very small test set, i.e., set14, Fig.3 and Fig.4. I do not think those results are convincing. The use of a single, small dataset like Set14 raises concerns about the generalizability of the findings. The paper needs to demonstrate the effectiveness of AdaSR on a more diverse set of images and across different types of content. Furthermore, the figures do not provide sufficient quantitative data to support the claims of Pareto optimality. The specific PSNR and latency values should be included in the plots or tables.

- In Sec. 4.3, "to support adapting models for cross-platform deployment and dynamic runtime environment, AdaSR achieves state-of-the-art performance, AdaSR achieves state-of-the-art performance". However, Tab.1 just shows the results on existing SR datasets. How can we learn from those evaluation results and how to demonstrate the effectiveness under cross-platform deployment and dynamic runtime environment? The results in Table 1 do not directly address the core claim of the paper, which is the adaptability of SR models for diverse platforms. The table only shows performance on standard datasets, and it is not clear how these results translate to real-world scenarios with varying hardware and runtime conditions. The paper needs to provide a more direct evaluation of the adaptability aspect, beyond just showing performance on standard benchmarks.

### Questions
Please refer to the issues in "Weakness" section.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors proposed AdaSR, a framework that can train multiple image super resolution models via shared architecture and weights for cross platform deployment and dynamic runtime environment.

### Strengths
1. The technical part of this paper is written clearly and easy to follow.

2. The AdaSR achieves fairly good results, but I'm not sure if they are SOTA since the comparisons involve parameters, FLOPS and multiple SR datasets that are hard to align. Therefore, I suggest the author provide a more comprehensive experiment report.

### Weaknesses
1. The novelty of this paper is quite limited. It seems that AdaSR adapts the width and depth, which is similar to many previous works such as [*]. The core novelty, the combination of progressive distillation and NAS, is not sufficiently compelling, as these techniques have been explored separately. The specific method of combining them and its advantages are not clearly articulated or demonstrated to be a significant advancement over existing approaches.

2. The performance improvement is marginal compared with MDDC. The results in Table 1 do not convincingly demonstrate the superiority of AdaSR over MDDC. It's difficult to ascertain which method performs better given the reported numbers, and the lack of statistical significance analysis further weakens the comparison. Furthermore, the absence of a citation for MDDC in the paper makes it hard to verify the baseline and its relevance. Also, the authors should compare with more recent baselines that reflect state-of-the-art performance.

3. Lack of experiment results on perceptual metrics. The absence of LPIPS or similar perceptual metrics makes it difficult to evaluate the visual quality of the super-resolved images. PSNR and SSIM, while useful, do not always correlate well with human perception. The authors should include perceptual metrics to provide a more complete evaluation.

4. Lack of visual qualitative comparison. The limited number of visual qualitative comparisons (only two in Figure 5) makes it hard to assess the visual quality of the results. More visual examples, showing a variety of scenes and textures, are needed to demonstrate the strengths and weaknesses of the proposed method.

5. The authors use tons of indentation between figures, paragraphs and headings. This excessive indentation makes the paper visually cluttered and hard to read. It's unclear if this formatting choice adheres to ICLR guidelines.

### Questions
I couldn't find any citations in your paper about MDDC in Table 1.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Super-resolution models significantly enhance the visual quality of low-resolution images. However, a notable limitation is their challenging adaptability to different hardware platforms, given the platform diversity. Moreover, these models often lack consideration for the runtime environment in which they operate. This environment can substantially impact their performance, influenced by both the hardware characteristics and available runtime resources. In response to these limitations, this paper introduces AdaSR, a solution designed to address these challenges. AdaSR employs a progressive knowledge distillation model training approach, which optimizes memory usage by dynamically adjusting depth and channel sizes based on the specific hardware during runtime while maintaining accuracy as much as possible. The experimental results demonstrate the effectiveness of AdaSR to a certain extent.

### Strengths
+ The motivation of this paper is insightful.
+ The design of the approach is clear and straightforward.
+ The paper is well organized.

### Weaknesses
 - Some key procedures of this approach need further clarification.
- Additional experiments are necessary to assess the model's performance in dynamic runtime environments.
- This approach requires retraining of existing models. What are the associated training costs in terms of time and hardware expenses?
- In Chapter 3.2.1, it is mentioned, “... increase the size of the adaptable model, ... and repeat the process ...”. The question is: When increasing the size each time, are all blocks in the adaptable model synchronized? For instance, do block 1 through block M increase to the same block size and channel size each time? If this is the case, does this approach iterate through all possible solutions within the search space?
- Is it feasible to apply or extend this approach to non-block-based models?
- In the experimental setup, the parameters beta_1 and beta_2 for the ADAM optimizer are set to the same values as those in the FAKD approach. Are there specific reasons for maintaining these parameters consistent with FAKD?
- It would be beneficial to include information about the available memory spaces in the experiments, as it is a crucial factor in characterizing the dynamic runtime environment.
- In Table 1, the significance of the bold values is ambiguous. They do not represent the best performance in the comparisons. More detailed clarifications are required.
- Chapter 4.2 does not sufficiently demonstrate AdaSR's robust adaptability in a dynamic runtime environment. An ablation study may be necessary, as it is an important statement declared in the Introduction. This is particularly relevant for showcasing AdaSR's adaptability in a dynamic runtime when “other running applications are present.”
- A minor writing issue: In Chapter 3.3, there is a phrase, “... we a training method with ...”

### Questions
1. This approach requires retraining of existing models. What are the associated training costs in terms of time and hardware expenses?
2. In Chapter 3.2.1, it is mentioned, “... increase the size of the adaptable model, ... and repeat the process ...”. The question is: When increasing the size each time, are all blocks in the adaptable model synchronized? For instance, do block 1 through block M increase to the same block size and channel size each time? If this is the case, does this approach iterate through all possible solutions within the search space?
3. Is it feasible to apply or extend this approach to non-block-based models?
4. In the experimental setup, the parameters beta_1 and beta_2 for the ADAM optimizer are set to the same values as those in the FAKD approach. Are there specific reasons for maintaining these parameters consistent with FAKD?
5. It would be beneficial to include information about the available memory spaces in the experiments, as it is a crucial factor in characterizing the dynamic runtime environment.
6. In Table 1, the significance of the bold values is ambiguous. They do not represent the best performance in the comparisons. More detailed clarifications are required.
7. Chapter 4.2 does not sufficiently demonstrate AdaSR's robust adaptability in a dynamic runtime environment. An ablation study may be necessary, as it is an important statement declared in the Introduction. This is particularly relevant for showcasing AdaSR's adaptability in a dynamic runtime when “other running applications are present.”
8. A minor writing issue: In Chapter 3.3, there is a phrase, “... we a training method with ...”

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, the authors present a framework for training an SR model that delivers consistent performance across different platforms. The techniques such as Block-level Progressive Knowledge Distillation, Function Matching, Depth Consolidation, and Bayesian-tuned Loss Function were utilized. This approach achieved the good trade-off curve in PSNR relative to computational cost, and the performance was validated across a range of devices.

(+) Typo or Layout Error
- Section 3.2.2 : "have the same dimensions/"
- Caption of Figure 2 : overlapped with the main paragraph

### Strengths
- The problem setup is commendable, addressing the important issue of super-resolution across different platforms and dynamic runtime environments.
- A variety of experiments support the claims made in the paper.
  - Figure 3 shows the superiority of the trade-off curve compared to conventional knowledge distillation models.
  - Figure 4 demonstrates operation on various architectures such as Snapdragon 845, Intel i5, and RTX 1080 Ti.
  - Table 1 compares the results on different datasets.

### Weaknesses
 - In Figure 4 and Table 1, the performance of AdaSR is still inferior to that of MobiSR and the large SR model.
- The training process of AdaSR appears to be complex, making it more challenging to extend to other platforms compared to designing a bespoke SR model for the target platform.
- Section 3.2.2 : "have the same dimensions/"
- Caption of Figure 2 : overlapped with the main paragraph

### Questions
- Why regularization for mapping layer is enough to keep the inference performance when removing the mapping layer? In my experience SR model is very sensitive to that kind of operation. Is there a related analysis or experiment?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
