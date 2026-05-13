# Maintaining Structural Integrity in Parameter Spaces for Parameter Efficient Fine-tuning

- Decision: Accept
- Scores: 6, 6, 6, 5

## Abstract
Adapting pre-trained foundation models for various downstream tasks has been prevalent in artificial intelligence. Due to the vast number of tasks and high costs, adjusting all parameters becomes unfeasible. To mitigate this, several fine-tuning techniques have been developed to update the pre-trained model weights in a more resource-efficient manner, such as through low-rank adjustments. Yet, almost all of these methods focus on linear weights, neglecting the intricacies of parameter spaces in higher dimensions like 4D. 
Alternatively, some methods can be adapted for high-dimensional parameter space by compressing changes in the original space into two dimensions and then employing low-rank matrix adaptations. However, these approaches destructs the structural integrity of the involved high-dimensional spaces. To tackle the diversity of dimensional spaces across different foundation models and provide a more precise representation of the changes within these spaces, this paper introduces a generalized parameter-efficient fine-tuning framework, designed for various dimensional parameter space. Specifically, our method asserts that changes in each dimensional parameter space are based on a low-rank core space which maintains the consistent topological structure with the original space. It then models the changes through this core space alongside corresponding weights to reconstruct alterations in the original space. It effectively preserves the structural integrity of the change of original N-dimensional parameter space, meanwhile models it via low-rank tensor adaptation. Extensive experiments on computer vision, natural language processing and multi-modal tasks validate the effectiveness of our method.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces FLoRA, a parameter-efficient fine-tuning (PEFT) method for adapting pre-trained foundation models across various parameter spaces while preserving the model’s structural integrity. FLoRA minimizes the computational burden of full fine-tuning by maintaining the original parameter organization, allowing efficient task-specific adaptability of different architectures. This approach supports scalable adaptation in large models, optimizing both resource use and performance. Empirical and theoretical evaluations show FLoRA’s robustness, highlighting its promise as an efficient approach for model adaptation.

### Strengths
+ The motivation behind maintaining the topological structure of the pre-trained matrices is compelling, providing a strong foundation for the proposed approach. 

+ The paper is well-organized and easy to follow, with each section clearly building upon the previous. 

+ The analysis section aligns well with the proposed objectives, and the approach to evaluating whether the core space is low-rank adds depth to the analysis.

### Weaknesses
 - The work appears to have similarities with existing approaches such as LoTR and LoKR; however, the paper does not adequately address how FLoRA distinguishes itself from these methods. This lack of clarification raises serious concerns about the novelty of the proposed approach.
- The manuscript does not provide sufficient evidence to demonstrate how the representations in FLoRA surpass those of LoRA and DoRA. It remains unclear how FLoRA broadens parameter adjustments and how this relates to enhancing parameter learning flexibility.
- The feature amplification factor introduced in the study may lack a direct correlation with actual task performance gains, making it difficult to interpret its significance in relation to improved task-specific outcomes. Currently, the correlation is indicated only using a single dataset and model architecture.
- The correlation observed between the Frobenius norm and feature amplification could be incidental rather than causal. There is insufficient evidence to support the claim that a larger norm consistently leads to enhanced task-specific performance.
- The scalability and computational efficiency of the proposed approach may be limited when applied to extremely high-dimensional tensors, potentially affecting its practicality for very large foundation models.

### Questions
Please see weaknesses above. Below are additional questions:
* What exactly is the difference between the current method and existing methods, particularly LoTR? The decomposition appears identical since both methods use Tucker decomposition, yet the paper claims that there are differences. It is hard to appreciate the paper without knowing about the differences between this work and past methods.
* How is the feature amplification factor considered a reliable indicator of task-specific information amplification, and what insights does it provide regarding task-specific performance? Furthermore, what methods are employed to measure task-specific information in the context of this study?
* What significance does the average Frobenius norm of $\Delta W$ hold for FLoRA's performance during fine-tuning? Can the magnitude of this norm be directly correlated to the effectiveness of task-specific adaptation? The presented correlation is based solely on a single sample, and there is no clear explanation provided for why this correlation would exist in the first place.
* How does the feature amplification factor of FLoRA in the DeBERTaV3-base model compare to that of other fine-tuning methods applied to the CoLA dataset? Does FLoRA exhibit a distinct pattern in terms of norm growth or amplification factor throughout the training process?
* If different versions of the DeBERTa model were evaluated, would the Frobenius norm or amplification factor be affected by changes in model architecture, or are these metrics consistently reliable across various transformer-based models?
* Without a direct comparison of the Frobenius norm and amplification factor metrics against alternative fine-tuning approaches, such as standard LoRA or full fine-tuning, it is challenging to assert FLoRA's superiority. If these metrics do not demonstrate a clear advantage over other methods, this could weaken the strength of the conclusions drawn in the paper.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a new generalized PEFT method, FLoRA, for N-dimension parameter space. FLoRA is based on the Tucker decomposition and uses a low-rank core tensor and N low-rank matrices to reconstruct the original parameter tensors. The introduction of the low-rank core space helps preserve the structural integrity of the original parameters space. Experiments on CV, NLP and multi-modal tasks validate the effectiveness of the proposed method over baselines like LoRA and DLoRA.

### Strengths
1. The generalization of LoRA on N-dimension parameter space with form of Tucker decomposition is interesting and effective.

2. The authors conduct many experiments on multiple kinds of tasks and validate the effectiveness of the proposed FLoRA method.

3. The paper is well-written and easy to follow.

### Weaknesses
1. In Line 183, the paper mentions that “in any convolution layer, there exists a convolution core”. Is this an assumption or supported by evidences and theories? More discussion should be added to improve the reliability of this claim.

2. How does the learned convolution core help preserve the convolution’s property of spatial locality?

3. It would be better to compare the FLoRA method with some PEFT method designed for CV tasks, such as [1].

4. Can you provide the standard deviations of the main results (Table 1 etc.)?

### Questions
See weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces FLoRA as a new approach to Parameter-Efficient Fine-Tuning (PEFT), focusing on preserving the structural integrity of high-dimensional spaces in large models.  The authors argue that existing PEFT methods, especially those relying on low-rank matrix adaptations, often disrupt the crucial spatial relationships within these high-dimensional spaces, particularly in convolutional layers, leading to suboptimal performance. 

FLoRA addresses this issue by introducing a low-rank core space that maintains the original spatial dimensions of the parameter space being adapted. For example, for a convolutional layer, FLoRA employs a 4D core tensor that mirrors the structure of the convolutional kernel. This ensures that spatial locality, crucial for convolution operations, is preserved during fine-tuning. 

The core space is then combined with corresponding weights to reconstruct the changes in the original parameter space. This approach allows FLoRA to achieve high performance while being efficient in terms of trainable parameters. The paper demonstrates FLoRA's effectiveness across various tasks in computer vision, natural language processing, and multi-modal learning, showcasing its superior performance compared to existing PEFT methods.

* **FLoRA outperforms traditional low-rank methods like LoRA, especially in tasks involving convolutional layers.** This is attributed to FLoRA's ability to preserve the spatial structure of high-dimensional parameter spaces.
* **FLoRA achieves performance comparable to or even exceeding that of full fine-tuning, while using significantly fewer trainable parameters.** This makes it a highly efficient and effective method for adapting large models to downstream tasks.
* **The paper provides empirical evidence for the existence of a low-rank core space within different dimensional parameter spaces.** This supports FLoRA's central premise and suggests its potential for broader applicability.

### Strengths
* **Significant Performance Gains:** The paper convincingly demonstrates FLoRA's superior performance over existing PEFT methods on both ConvNeXt (Table 1) and InternViT (Table 2) architectures.  The improvements are particularly noteworthy on ConvNeXt, which relies heavily on convolutional layers, highlighting FLoRA's strength in handling high-dimensional parameter spaces.  The results show that FLoRA not only outperforms other low-rank adaptation methods like LoRA and DoRA by a substantial margin (at least 15% on average across different parameter budgets) but also achieves performance comparable to, and in some cases even better than, full fine-tuning. 

* **Parameter Efficiency and Practicality:** The authors emphasize FLoRA's practicality by showcasing its ability to achieve these strong results while significantly reducing the number of trainable parameters and training time. The paper explicitly states that FLoRA can achieve comparable performance to full fine-tuning with an 80% reduction in parameter budget.  Additionally, Table 5 provides evidence of FLoRA's efficiency in terms of both training time and GPU memory usage compared to other methods, particularly DoRA.

* **Insightful Analysis of Low-Rank Representation:** The paper goes beyond simply presenting performance results. It provides a detailed analysis of why FLoRA's low-rank representation is more effective than other methods. Figure 4, which compares the Frobenius norm and feature amplification factor of FLoRA, LoRA, and DoRA during training, offers valuable insights. This analysis reveals that while LoRA and DoRA might initially amplify task-specific features more aggressively due to their constraints on matrix patterns, FLoRA's less constrained approach allows it to capture a broader range of task-specific information, leading to higher amplification factors upon convergence. The paper also suggests a strong correlation between the Frobenius norm of the learned changes (∆W) and the ability to capture task-specific information.

* **Clear and Well-Written:** The paper is well-structured, and the concepts are explained in a clear and concise manner.  This clarity makes it easy for readers to understand the motivation behind FLoRA, its technical details, and the significance of the results. 

* **Addressing a Gap in PEFT Research:** The authors clearly identify a gap in existing PEFT research, which primarily focuses on linear layers while neglecting the complexities of high-dimensional parameter spaces. FLoRA is presented as a solution to this problem, demonstrating its novelty and potential impact on the field.

### Weaknesses
 *   **Limited Scope of LLM Fine-tuning Experiments:** The paper lacks experiments on LLM fine-tuning (e.g., LLaMA3-8B), despite PEFT methods being commonly used in these scenarios. Evaluating FLoRA's efficacy on LLMs would enhance the paper's practicality and relevance.
*   **LoRA's Applicability in Vision-Based Models:** The paper focuses on LoRA as a comparison point for FLoRA, but LoRA is not a standard fine-tuning technique for vision-based models like ConvNext and Mask-RCNN. Comparing FLoRA to more prevalent methods like last-layer fine-tuning and prompt tuning would offer a more comprehensive evaluation of its effectiveness.
*   **Missing DoRA Results on LLaVA-1.5-7B:** The paper doesn't report the performance of DoRA on LLaVA-1.5-7B fine-tuning, despite mentioning a DoRA result of 67.6, which surpasses FLoRA's performance. Including comprehensive comparisons with state-of-the-art methods like DoRA is crucial for establishing FLoRA's superiority.
*   **Compatibility with Weight-Decomposed Formulations:** The paper does not address whether FLoRA is compatible with weight-decomposed formulations like those proposed by DoRA. Exploring potential integration with other advanced PEFT techniques could reveal further benefits and limitations of FLoRA.
*   **Lack of Theoretical Grounding for the Core Space:** The paper demonstrates the existence and effectiveness of a low-rank core space empirically but lacks a theoretical framework to explain these findings. Providing a theoretical foundation for the core space's properties would strengthen the paper's claims and provide valuable insights into FLoRA's underlying mechanisms.
*   **Potential Computational Overhead:** While the paper asserts that FLoRA exhibits better parameter efficiency than LoRA for larger kernel sizes, it doesn't thoroughly analyze the computational costs in diverse settings. A more comprehensive analysis of FLoRA's computational complexity in various scenarios, especially for extremely large models or complex tasks, is recommended.
*   **Focus Beyond Convolutional Kernels:** While FLoRA demonstrates its effectiveness on convolutional kernels, it should be assessed on other high-dimensional weight matrices.  Given its positioning as a fundamental low-rank adaptation method, a broader range of experiments would validate its general applicability and effectiveness.
*   **Quantifying the Impact of Structural Integrity:** The paper could benefit from a more in-depth exploration of whether preserving structural integrity truly matters in weight adaptation for computer vision. This could involve experiments or analyses that isolate the impact of structural preservation on performance, further validating FLoRA's core principle.

### Questions
Already listed in the Weaknesses section.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper presents FLoRA, a novel parameter-efficient fine-tuning framework that addresses the challenge of adapting pre-trained models across diverse parameter space dimensions. Leveraging Tucker decomposition, FLoRA proposes to model parametric changes through a low-rank core space, ostensibly preserving the structural integrity of high-dimensional parameter spaces. The methodology is evaluated across a spectrum of tasks encompassing computer vision, natural language processing, and multimodal learning. The authors report that FLoRA demonstrates superior performance compared to existing methods, notably LoRA, while utilizing fewer trainable parameters. This efficiency is attributed to FLoRA's capacity to maintain the topological structure of the parameter space.

### Strengths
1)	The motivation behind this paper is significant. When using LoRA to fine-tune convolutional layers, it either disrupts the original topology or adds too many parameters. FLoRA, with Tucker decomposition, effectively adjusts high-dimensional parameter spaces, aiding the application of parameter-efficient fine-tuning across more models.
2)	Although FLoRA is motivated by improvements in tuning high-dimensional parameter spaces, the paper still includes many experiments with models that mainly use linear layers. The experimental setup of the paper covering many fields including computer vision, NLP and multimodal tasks, and shows good performance.
3)	The authors compare FLoRA with LoRA and DoRA, using both theoretical reasoning and empirical evidence. They employ metrics like Frobenius norm and feature amplification factor, offering insights into learning patterns. Notably, they explore the correlation between Frobenius norm and task-specific information amplification.

### Weaknesses
1) The performance gains of FLoRA on linear layer-based models appear limited. While the motivation to address topological distortions in high-dimensional parameter spaces is commendable, it potentially constrains FLoRA's applicability across diverse model architectures. Although the analysis utilizing Frobenius norm metrics and unrestricted low-rank subspaces is insightful, I recommend enhancing the paper through: A more rigorous theoretical treatment, exploring deeper mathematical foundations. An expanded experimental paradigm encompassing various model architectures, tasks, and datasets. These enhancements would strengthen the generalizability claims and broaden FLoRA's potential impact in the field of parameter-efficient fine-tuning.
2) The initialization strategy in FLoRA deserves more exploration. Although the authors use a conservative approach, diverse methods could enhance performance. Advances in LoRA initialization indicate room for improvement. A study comparing various strategies might boost FLoRA's effectiveness and stability across tasks and models. I look forward to the authors expanding research on how initialization affects FLoRA's low-rank subspace, potentially leading to more robust fine-tuning.

### Questions
See above

### Soundness
2

### Presentation
2

### Contribution
2
