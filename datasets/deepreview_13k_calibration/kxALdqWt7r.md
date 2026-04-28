# Model Editing for CLIP with Unknown Spurious Correlations in Visual Encoder

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 6, 5, 5

## Abstract
CLIP, despite its robust zero-shot capabilities, often suffers from spurious correlations that can lead to prediction errors, especially when deployed in environments different from their training data. This paper addresses the challenge of correcting errors in CLIP, particularly when only limited data is available and the underlying biases causing errors are unknown. 
To tackle this issue, we introduce a novel two-phase model editing framework. In the first phase, we propose to utilize a data-driven approach to identify the spurious features that directly contribute to errors without prior knowledge of the biases and nullify the corresponding components in the model, creating a spurious-feature-ablated model. 
In the second phase, we edit the original model by aligning the model's outputs with those of the spurious-feature-ablated model for misclassified samples to correct errors, while also aligning with the original model for the remaining data to maintain locality. Our experiments on the synthetic dataset and real-world datasets demonstrate the effectiveness of our method in both identifying the causes of errors and rectifying the model to significantly improve model performance.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This work focuses on correcting the errors in CLIP-ViT. The authors propose a two-stage model editing framework for this task. In the first stage, they identify which components of the model cause the errors, then nullify these parts to create a spurious-feature-ablated
model that is less influenced by misleading features. In the second stage, the model is edited by learning the error-corrected knowledge for editing and the error-unrelated knowledge from the original model for locality. Experiments are conducted to show the performance of the proposed editing framework.

### Strengths
1. The motivation of the work is strong and model editing in CLIP is novel.
2. The proposed causal perspective on error analysis is unique and provides a more targeted way of identifying error sources than conventional feature importance methods.

### Weaknesses
1. The title indicates that this work is about CLIP, but this work only focuses on CLIP-ViT. The scopes are inconsistent.
2. The methodology section introduces several techniques, including attention head selection based on causal significance and post-deployment editing, but it is not always clear how these techniques fit together into a cohesive framework. For instance, the logic behind moving from attention head analysis to feature editing may be difficult to follow on a first read.
3. Spurious features can be challenging to separate when entangled with meaningful information.

### Questions
1. How does the proposed framework handle cases where spurious correlations are not clear-cut or are entangled with causal features?
2. How is error identification handled differently in synthetic versus real-world datasets, where features are less controlled?
3. Does the method support cases where there are multiple interacting spurious correlations? 
4. The two-phase framework includes post-deployment editing, which may increase the overall computational cost. Has the impact on inference speed or computational overhead been measured, especially for large-scale models?
5. How does the model ensure that post-deployment edits improve generalizability rather than just adjusting to recent deployment-specific noise? Are there checks in place to limit overfitting?

### Soundness
2

### Presentation
1

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
This paper addresses the challenge of correcting CLIP's prediction errors that arise from spurious correlations, particularly in scenarios where only limited data is available and the underlying biases are unknown. The authors propose RefineCLIP, a two-phase model editing framework:

1. In the first phase, the method identifies problematic attention heads through a data-driven approach using four proposed metrics ($\text{DE}_A$, $\text{DE}_B$, $\text{DE}_C$, $\text{DE}_D$) that analyze the direct contributions of attention heads to prediction errors. This is achieved by comparing feature representations between correctly and incorrectly classified samples.
2. In the second phase, the framework introduces a learnable diagonal projection matrix to adapt CLIP's representations. The training objective combines three components:
    - Success loss: aligns model outputs with those of the spurious-feature-ablated model for misclassified samples
    - Locality loss: preserves original predictions for unrelated samples
    - Cross-entropy loss: utilizes available ground truth labels

The authors evaluate their method on both synthetic (Binary Waterbirds) and real-world datasets (CelebA, ImageNet-R, ImageNet-A), demonstrating that RefineCLIP can effectively identify spurious correlations and correct predictions while maintaining locality.

### Strengths
- The paper addresses an important and practical scenario where model errors need to be corrected with limited data and without prior knowledge of biases.
- The proposed method for identifying problematic attention heads through data-driven metrics is innovative and well-grounded in the understanding of transformer architectures.
- The experimental design using the Waterbirds dataset with known spurious correlations provides a good validation of the method's ability to identify problematic features.

### Weaknesses
## Major weaknesses
1. Limited theoretical foundation
    - The paper heavily relies on Proposition 1 (in appendix) for the equivalence of metrics, but this crucial theoretical foundation is not properly discussed in the main text. The connection between the proposed metrics and the actual error correction is not clearly established, making it difficult to understand why these specific metrics are effective in identifying problematic attention heads. A more rigorous justification is needed to explain how these metrics directly relate to the spurious correlations the method aims to address.
    - The choice of diagonal projection matrix over alternatives (full matrix, LoRA) lacks theoretical justification. The paper does not provide a clear rationale for why a diagonal matrix is sufficient for adapting CLIP's representations, especially given that a full matrix or low-rank adaptation (LoRA) could potentially offer more flexibility in capturing complex relationships. The lack of discussion on the trade-offs between these choices weakens the justification for the proposed approach.
2. Insufficient Comparison
    - The comparison with existing methods is limited mainly to Tip-adapter, ignoring numerous recent CLIP few-shot adaptation methods. For instance, prompt learning approaches like CoOp[^1] have shown strong performance in few-shot scenarios, while more recent methods like PLOT[^2] and CLAP[^3] have further advanced the state-of-the-art in robust few-shot adaptation of vision-language models. The paper needs to demonstrate how RefineCLIP compares to these state-of-the-art methods in terms of both performance and efficiency.
    - The relationship with prompt learning approaches is not discussed, despite potential similarities in goals and methods. The paper should address how the proposed method differs from prompt learning techniques, particularly in terms of the underlying mechanisms for adapting the model and the types of biases they target. A discussion of the advantages and disadvantages of each approach would provide a more comprehensive understanding of the field.

## Minor weaknesses
1. Presentation Issues
    - Complex methodology lacks clear visualizations (e.g., for W, C, A sets and DE metrics calculations). The paper would benefit from a more detailed visual explanation of how these sets are constructed and how the DE metrics are calculated. This would help the reader better understand the data flow and the rationale behind the proposed metrics.
    - Redundant explanations of symmetric metrics make the paper unnecessarily verbose. The paper could be more concise by clearly stating the symmetry between the metrics and avoiding repetitive explanations.
2. Limited Analysis
    - The tradeoff between edit success and locality (shown in Fig. 2) deserves more detailed analysis. The paper should provide a more in-depth discussion of the factors influencing this trade-off, such as the number of samples used for editing, the choice of target classes, and the specific hyperparameters of the method. A more comprehensive analysis would help the reader understand the limitations and practical implications of the method.
    - The conclusion lacks discussion of limitations and future directions. The paper should acknowledge the limitations of the proposed method, such as its reliance on specific types of spurious correlations or its sensitivity to certain hyperparameters. The conclusion should also suggest potential avenues for future research, such as extending the method to other types of biases or exploring alternative adaptation techniques.
    - Hyperparameter sensitivity analysis is inadequate. The paper should provide a more thorough analysis of the sensitivity of the method to its hyperparameters, such as the weights in the combined loss function. This analysis should include a discussion of how the performance of the method varies with different hyperparameter settings and provide guidance on how to choose appropriate values.

### Questions
1. Could you clarify why a diagonal projection matrix was chosen over alternatives like full matrix or LoRA? What are the theoretical or practical advantages?
2. How does your method compare with recent prompt learning approaches for few-shot CLIP adaptation? Particularly, methods like CoOp[^1], PLOT[^2], and CLAP[^3] have shown strong performance in similar few-shot scenarios. Could you elaborate on the advantages and disadvantages of your approach compared to these methods?
3. The edit success vs. locality tradeoff seems crucial. Could you provide more insights into how this tradeoff is affected by different factors (e.g., number of samples, choice of target classes)?
4. How sensitive is the method to the choice of hyperparameters α and β in the combined loss function?

[^1]: Zhou, Kaiyang, et al. "Learning to prompt for vision-language models." International Journal of Computer Vision 130.9 (2022): 2337-2348.
[^2]: Chen, Guangyi, et al. "Plot: Prompt learning with optimal transport for vision-language models." arXiv preprint arXiv:2210.01253 (2022).
[^3]: Cai, Yichao, et al. "CLAP: Contrastive Learning with Augmented Prompts for Robustness on Pretrained Vision-Language Models." arXiv preprint arXiv:2311.16445 (2023).

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces a novel, data-driven method for editing CLIP models. The proposed approach comprises two main phases:

1. **Detection and Ranking of Faulty MSA Heads**: This phase involves calculating DE scores to evaluate changes in similarity to text features. This is achieved by replacing the Multi-Head Self-Attention (MSA) head features with averaged features from either correctly or incorrectly classified labels. The DE scores enable the ranking of MSA heads, thereby identifying which heads are faulty and may require editing.
2. **Training the Projection Matrix for Localized Edits**: To facilitate successful and localized edits, the method involves training a projection matrix, denoted as $\theta$, using a specifically designed loss function. This loss function ensures that the edits made to the MSA heads do not compromise the model's overall performance and maintain the desired locality of the changes.

### Strengths
The paper is clearly structured and easy to understand. The experimental results appear to be good.

### Weaknesses
1. **Comparison with Trainable Versions of Existing Methods**: The paper fails to consider the trainable version of Tip-Adapter. Since the proposed method involves training, it would be reasonable to finetune Tip-Adapter for a fairer evaluation. The absence of this comparison makes it difficult to assess the true advantage of the proposed approach, particularly given that both methods are data-driven and involve some form of parameter optimization. A direct comparison with a fine-tuned Tip-Adapter would provide a more robust benchmark.
2. **Insufficient Emphasis on Contributions**: The presentation does not adequately highlight the unique contributions of the proposed method. The authors note that the first stage resembles Gandelsman et al. and the second stage aligns with Santurkar et al., yet claim that the method is data-driven and does not require prior knowledge. However, previous works like Tip-Adapter also fall into this category, which undermines the novelty of the proposed approach. The paper needs to more clearly articulate how the combination of these existing ideas results in a novel and significant contribution, especially given that the individual components are inspired by prior work. The claim of being data-driven is not sufficient to establish novelty, as other methods also leverage data for model adaptation.
3. **Inconsistent Experimental Design**: It is puzzling that the authors conduct experiments on the Waterbirds dataset for edit success, yet switch to different datasets (CelebA and ImageNet-R/A) for edit locality. It would be better to explain the motive of such a design. The lack of a consistent evaluation framework across different aspects of the method makes it harder to interpret the results holistically. The choice of datasets for different experiments should be justified with clear reasoning, and ideally, a more unified experimental design should be adopted to facilitate a more comprehensive understanding of the method's performance.
4. **Limited Experimental Scope**: The experiments would benefit from a broader scope, particularly regarding success edits across multiple datasets. In contrast, Tip-Adapter has been evaluated on 10 different datasets, which provides a more comprehensive understanding of performance. Expanding the testing to include additional datasets would enhance the credibility of the findings. The current experimental setup, while demonstrating the method's effectiveness on specific datasets, does not provide sufficient evidence of its generalizability and robustness across diverse scenarios.

### Questions
Besides my concerns raised in the Weakness, I have a few more questions.
1. **Visualization of Method Comparisons**: Could the authors provide an alternative version of Fig. 1 that displays heatmaps for each method separately, potentially including more images? This would enhance the understanding of the proposed method's superiority in detecting faulty heads.
2. **Impact of MSA Heads on Performance**: Does the number of Multi-Head Self-Attention (MSA) heads, denoted as TTT, influence the performance of the proposed method? A discussion and analysis regarding this aspect would be beneficial.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper addresses the issue of CLIP capturing spurious correlations during feature extraction, leading to prediction errors, and proposes a model editing method for CLIP called RefineCLIP. Specifically, RefineCLIP ranks each attention head in every layer based on its contribution to correct and incorrect classifications and sequentially ablates the outputs of certain attention heads. The contribution is determined by the change in the model's features and the class text features before and after ablation. Additionally, the model introduces an extra diagonal matrix as model parameters and fine-tunes it. The paper conducts experiment on the Waterbirds Dataset to validate the performance of the proposed method.

### Strengths
1. The method for evaluating the contribution of each attention head is novel.

### Weaknesses
1. Some existing studies [1] indicate that model editing can harm the generalization ability of the base model, contrary to the claim in this paper that it does not affect unrelated data. The experimental results in Figure 2 also indicate this. Specifically, while the method aims to correct spurious correlations, the ablation process could inadvertently remove features important for generalization on unrelated data, leading to a drop in performance. This is a critical concern that needs more thorough investigation and discussion.
2. The proposed method requires training and cannot be applied to unlabeled images. The reliance on labeled data for identifying misclassifications limits the applicability of the method in scenarios where labeled data is scarce or unavailable. Furthermore, the training process introduces additional computational overhead, which may be a concern for resource-constrained environments.
3. The readability of the paper is not good. Including a schematic diagram of the proposed method could improve this. The lack of a clear visual representation makes it difficult to understand the interaction between different components of the proposed method. The paper would benefit from a detailed flowchart or diagram illustrating the data flow and processing steps.
4. The comparison methods are insufficient. This paper only compares with TextSpan [2] and the training-free methods Tip-adapter [3], without comparing with more debiasing methods for CLIP. The absence of comparisons with other state-of-the-art debiasing techniques makes it difficult to assess the relative performance of the proposed method. A more comprehensive evaluation is needed to establish the superiority of the proposed method.
5. There is a lack of visualization results. From the visualization in Figure 1, it is still unclear how the attention regions of the model changed during classification before and after ablation. The paper needs to provide more detailed visualizations showing the changes in attention maps and feature representations after the proposed editing process. This would help in understanding the mechanism of the proposed method.
6. The ablation experiments are insufficient. The roles of the three losses mentioned in Section 3.3 are not analyzed. The weights of these three loss functions are also not clearly defined. The paper should include a detailed ablation study to analyze the contribution of each loss term and the impact of different weight settings. This is crucial for understanding the sensitivity of the method to hyperparameter choices.

### Questions
1. In the ablation experiment shown in Figure 3, the results are explained as coming from learning from the ablated model and the initial model. However, when all elements of the diagonal matrix are 1, the loss function in Equation 11 and 12 seems to be 0, making these loss functions meaningless. What are the details of this ablation experiment? How is the diagonal matrix used for fine-tuning initialized?

### Soundness
3

### Presentation
2

### Contribution
2
