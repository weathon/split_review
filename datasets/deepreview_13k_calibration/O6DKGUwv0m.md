# Empowering Teachers with Enhanced Knowledge via Variable Scale Distillation Framework

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 5, 5

## Abstract
Knowledge distillation, a widely used model compression technique, enables a smaller student network to replicate the performance of a larger teacher network by transferring knowledge, typically in the form of softened class probabilities or feature representations. However, current approaches often fail to maximize the teacher’s feature extraction capabilities, as they treat the semantic information transfer between teacher and student as equal. This paper presents a novel framework that addresses this limitation by enhancing the teacher’s learning process through the Variable Scale Distillation Framework. Central to our approach is the Rescale Block, which preserves scale consistency during hierarchical distillation, allowing the teacher to extract richer, more informative features. In extensive experiments on the CIFAR100 dataset, our method consistently outperforms state-of-the-art distillation techniques, achieving an average accuracy improvement of 2.12\%. This demonstrates the effectiveness of our approach in fully leveraging the teacher’s capacity to guide the student, pushing the boundaries of knowledge distillation.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces the Variable Scale Distillation Framework (VSDF), which enhances teacher-student knowledge transfer by training the teacher on inputs of varying scales. This approach is supported by a Rescale Block that aligns feature maps between teacher and student, addressing the feature mismatch issue caused by differences in input scale. Additionally, a self-supervised aggregated task is incorporated to improve the teacher’s feature extraction capacity, enabling the student network to achieve better generalization and accuracy, especially in low-data scenarios. The authors demonstrate this approach’s efficacy on CIFAR-100, showing improvements in both classification accuracy and transfer learning.

### Strengths
1. The VSDF enables the teacher network to leverage richer features by introducing variable scale inputs, which pushes beyond typical one-to-one input matching in distillation. 

2. This framework taps into the teacher’s full capacity and could offer substantial improvements in cases where the student network benefits from a diverse set of learned representations.
   
3. The Rescale Block’s design addresses a common challenge in knowledge distillation: mismatched feature scales between teacher and student networks. 

4. The paper provides a well-rounded empirical analysis with an ablation study, comparisons to state-of-the-art distillation methods, and few-shot learning performance.

### Weaknesses
1. The introduction of VSDF and Rescale Block raises concerns about computational overhead. The experiments would benefit from additional metrics on training time, computational cost, or memory usage compared to standard distillation techniques, which could affect the method’s practicality in resource-limited environments. Specifically, the paper lacks a quantitative analysis of the training time complexity, making it difficult to assess the actual overhead of the proposed approach. It is crucial to provide metrics such as the increase in training time per epoch for both the teacher and student networks, as well as the overall training time, to properly evaluate the method's efficiency.

2. While the teacher benefits from richer inputs, this may not always yield proportionally significant improvements in the student’s performance, especially when dealing with datasets of smaller resolutions or non-visual domains where variable scale inputs may not be as effective. The paper does not explore the limitations of the variable scale input, particularly in scenarios where the input resolution is already high, or where the data does not inherently benefit from multi-scale analysis. The effectiveness of this approach should be evaluated across a broader range of data types and resolutions.

3. CIFAR-100 (32X32) is a commonly used dataset, but the lack of experiments on larger or more complex datasets with higher resolution limits the generalizability of the results. The paper should include experiments on datasets with higher resolutions, such as ImageNet, to demonstrate the scalability and effectiveness of the proposed method in more realistic scenarios. The current results only show the performance on low-resolution images, which is not sufficient to claim general applicability.

4. While the self-supervised aggregated task shows promising results, the paper does not sufficiently analyze the contribution of individual self-supervised tasks (such as rotation versus permutation) to overall performance. The paper should include an ablation study that isolates the impact of each self-supervised task on the final performance. Without this analysis, it is difficult to understand which tasks are most beneficial and why.

5. this approach might benefit from a clearer theoretical foundation or explanation, particularly regarding why specific transformations, like rotation, improve generalization more than others. Without this, the choice of transformations may appear somewhat arbitrary. The paper should provide a theoretical justification for the choice of self-supervised tasks, explaining why rotation, for example, is more effective than other transformations. This would strengthen the theoretical basis of the proposed method.

6. The hierarchical distillation losses and the aggregated task losses are complex and potentially difficult to tune. This complexity may limit reproducibility or make the method sensitive to hyperparameter selection. A more streamlined loss function could simplify the application of this framework without sacrificing performance. The paper should provide a detailed analysis of the sensitivity of the proposed method to the hyperparameters of the loss functions. Specifically, the impact of different weights for each loss component should be evaluated to understand the robustness of the method.

### Questions
1. What is the added computational cost of VSDF and the Rescale Block? Please evaluate the training time complexity.

2. Is it possible to evaluate VSDF on larger datasets like ImageNet?

3. What is the impact of each self-supervised task (e.g., rotation vs. channel permutation)? Why might some perform better? Please explain.

4. How does VSDF scale with larger teacher or student models? Are there any scenarios this method struggles?

5. Please provide details of the hyperparameters tunning for the loss functions.

6. Does the Rescale Block work effectively across different input resolutions or tasks? It is better to explain and evaluate explicitly.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes the Variable Scale Distillation (VSD) Framework for knowledge distillation, where a teacher network processes images at varying scales to capture richer feature representations. A Rescale Block is introduced to maintain scale consistency between teacher and student features, aiming to improve the knowledge transfer process. Experimental results on different datasets demonstrate improved student performance compared to existing distillation methods.  However, I have several concerns, especially regarding the novelty, evaluation rigor, and justification of the proposed Variable Scale Distillation (VSD) framework.

### Strengths
1. Leveraging multi-scale images in the teacher network could potentially enrich the knowledge transferred to the student which is interesting.
2. This paper opens up the concept of utilising teacher potential.
3. This addition aims to maintain feature consistency, addressing common misalignment issues in hierarchical knowledge transfer.

### Weaknesses
1. Both variable scaling and self-supervised integration have been explored separately in past work, and combining them here lacks a distinct methodological contribution. The paper does not sufficiently articulate how the specific combination of these techniques leads to synergistic benefits beyond what each method achieves independently. It is unclear if the performance gains are simply additive or if there's a more complex interaction at play.
2. There’s no clear analysis explaining why rescaling improves transfer quality. Empirical results are shown, but insights or qualitative explanations are missing. The paper lacks a mechanistic explanation of how the Rescale Block facilitates better knowledge transfer. It's not clear if the improvement is due to better feature alignment, or some other effect of the rescaling process. The absence of feature-level analysis makes it difficult to understand the underlying mechanisms.
3. The paper does not explore how different scaling techniques might impact results, which could limit the framework’s robustness. The choice of bilinear interpolation is presented without justification, and the potential impact of other interpolation methods (e.g., nearest-neighbor, bicubic) on the final performance is not investigated. This lack of exploration raises concerns about the generality of the results.
4. The framework is tested mainly on CIFAR100 (lower resolution), which raises questions about its generalizability. Additional tests on larger, varied datasets would add credibility. It is suggested to evaluate the proposed approach on higher-resolution based images. The limited evaluation scope makes it difficult to assess the framework's applicability to more complex and realistic scenarios.

### Questions
1. Please discuss how this framework differs conceptually and practically from existing methods using multi-scale and self-supervised learning in distillation.

2. How does the choice of scaling method (e.g., bilinear interpolation) affect the results? Please consider testing different scaling methods to assess the robustness of the framework, as certain methods may impact performance differently.

3. Why rescaling improves feature transfer? Is it possible to provide any theoretical or visual analysis that supports this? Including feature-level visualizations or theoretical justifications would help clarify why rescaling benefits knowledge transfer.

4. Is it better to test the VSD framework on larger and more diverse datasets of higher resolution? Expanding evaluation to larger datasets would help validate the generalizability and broader applicability of the framework.

5. It is suggested to conduct ablation studies to isolate the impact of the Rescale Block on the student’s performance.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes the Variable Scale Distillation Framework, which incorporates several techniques. First, it trains the teacher model on images doubled in size using cross-entropy loss, then distills the enhanced features into the student model with original-sized images to fully leverage the teacher's intricate architecture and extensive parameters. During the distillation process, to match the feature map sizes between multiple layers of the teacher and student networks, the paper introduces a Rescale Block, which increases the student model's feature map size by copying and pasting existing features. Additionally, to incorporate the benefits of supervised techniques, it rotates the input images and broadens the dimensions of the final vector space while training both the teacher and student models. Finally, binary cross-entropy loss is applied between the intermediate feature maps and the ground-truth labels. To evaluate the performance of the proposed method, they compare it with state-of-the-art methods in supervised, few-shot, and transfer learning tasks across various datasets.

### Strengths
This paper explores various techniques to enhance the performance of the student model.

### Weaknesses
The motivation for and effects of the proposed method are overall unclear. The paper claims that doubling the image size as input to the teacher model helps fully leverage the teacher network’s intricate architecture and extensive parameters, which other existing KD methods overlook. However, the authors provide neither explanations nor experimental evidence for this assertion. Could you provide comparison results for the teacher model's feature representations when using doubled-size images versus original-size images as input? Additionally, could you explain why using quadrupled-size images decreases the performance of both the teacher and student models?

Additionally, the authors apply some self-supervised techniques but do not clarify which advantages of self-supervised learning were intended in this paper. and this paper does not demonstrate the effectiveness of training the teacher model and distilling knowledge to the student, even at the expense of increased training cost. Could you provide experimental results on directly training the student model using the proposed self-supervision technique for the teacher model, Variable Scale Image Refinement, while keeping the teacher model fixed (no training) and leaving the rest of the proposed method unchanged?

The paper claims to introduce a Hierarchical KD Branch to distill feature knowledge from multiple teacher layers to the student model, but this approach is already common in feature-based knowledge distillation (e.g., FitNet [Romero et al., 2015], ReviewKD [Chen et al., 2021]). Furthermore, the concrete principles behind the Rescale Block method and $fmap_j$ are not adequately explained.

The experimental section also lacks sufficient evidence to support the authors' claims. The paper only compares a single pair of student and teacher networks in both the ablation study and further analysis sections, limiting the reliability of the results.

In response to my previous question, the authors referenced HSAKD and stated that they provided a citation. After reviewing the HSAKD paper, I found their method to be strikingly similar to the loss terms described in Sec. 3.2.2 (i.e., $L^S_{agg1}$, $L^S_{agg2}$, $L^S_{KD1}$, and $L^S_{KD2}$). Additionally, the authors acknowledged that they employed an additional linear classification step, which appears to be borrowed from the task loss and mimicry loss framework of HSAKD. Furthermore, the ablation study shown in Fig. 3 (left) of HSAKD closely resembles the ablation study in Fig. 4(b) of this work.

While borrowing ideas from prior work is not inherently problematic, the lack of clear explanation and citation in the Training section (Sec.3.2.2) of the Method, as well as the absence of explicit acknowledgment in the Experiment section, creates a significant risk of confusing readers. Without clarification, readers may mistakenly believe these methodologies are entirely novel to this work. This is a serious concern. If the four loss terms in this method differ from HSAKD’s, I urge the authors to clearly explain these differences in detail.

Although the initial similarity caused some confusion, I understand that the novelty of this work lies in two main aspects as described in the paper:

- Adding scale transformations to HSAKD.
- Introducing a Rescale block.

However, these contributions feel somewhat incremental, and I remain unconvinced of their broader impact. Moreover, the lack of detailed explanation about the Rescale block and the absence of ablation studies related to it (even after the revision period) leave me questioning the novelty and effectiveness of this method.

Despite the discussion phase and additional feedback provided, none of the reviewers’ concerns appear to have been addressed in the revised manuscript. While the responses in the OpenReview comments provide some clarification, the manuscript itself remains unchanged. This makes it difficult to evaluate whether the concerns have been resolved in a meaningful way. Additionally, the claims in the manuscript remain unclear.

### Questions
1. Could you explain the reason why doubling the image size as input to the teacher model helps fully leverage the teacher network’s intricate architecture and extensive parameters?
2. Did you only use rotation and resizing transformations for the pre-processing of the input images (M=2) during teacher training?"
3. Could you explain why using quadrupled images reduces the performance of both the teacher and student models?
4. Could you cite the paper that proposes the supervision technique for broadening the dimensions of the final vector space during training?
5.Could you explain what information is transferred from the teacher through aggregated-task learning with self-supervision compared to existing KD methods, and how this benefits the student model?
6.  Could you provide more detailed information about  Rescale Block and $fmap_j$?
7.  Did you utilize additional linear classification layers for Eq. (3) and Eq. (4) to match the feature map size and labels?
8.  Could you provide experimental results on directly training the student model using the proposed self-supervision technique for the teacher model, Variable Scale Image Refinement, while keeping the teacher model fixed (no training) and leaving the rest of the proposed method unchanged?
9.  Could you report the ablation study and further analysis with more pairs of teacher and student networks (both similar and different architectures)?
10. Could you report the results of the teacher model trained with your proposed methods, as well as without them?
11.In Section 4.1.4, "Correlation Matrix of Logits" (page 7), isn't a higher correlation between the teacher's logits and the student's logits preferable?
12. Could you report the ablation study on the method without training the teacher?
13. Could you provide comparison results for the teacher model's feature representations when using doubled-size images versus original-size images as input? 

Things to improve the paper that did not impact the score:
1. Please follow the formatting instructions of ICLR regarding citations within the text, ensuring that \citep{} and \citet{} are used appropriately.
2. Possible typo: In line 3 of the Knowledge Distillation section (2.1) on page 2, 'Hinton et al.' is written twice.
3. Please unify the notation for referencing, deciding whether to use 'Equation 5, Figure 5' or 'Eq. (5), Fig. (5).'
4. Possible typo: On page 5, "$\lambda_1$ and $\lambda_2$" should be corrected to "$\lambda_1$ ,$\lambda_2$ , $\lambda_3$  and $\lambda_4$ "

### Soundness
1

### Presentation
2

### Contribution
1
