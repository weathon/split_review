# LoR-VP: Low-Rank Visual Prompting for Efficient Vision Model Adaptation

- Decision: Accept
- Scores: 8, 6, 5

## Abstract
Visual prompting has gained popularity as a method for adapting pre-trained models to specific tasks, particularly in the realm of parameter-efficient tuning. However, existing visual prompting techniques often pad the prompt parameters around the image, limiting the interaction between the visual prompts and the original image to a small set of patches while neglecting the inductive bias present in shared information across different patches. In this study, we conduct a thorough preliminary investigation to identify and address these limitations. We propose a novel visual prompt design, introducing **Lo**w-**R**ank matrix multiplication for **V**isual **P**rompting (LoR-VP), which enables shared and patch-specific information across rows and columns of image pixels. Extensive experiments across seven network architectures and four datasets demonstrate significant improvements in both performance and efficiency compared to state-of-the-art visual prompting methods, achieving up to $6\times$ faster training times, utilizing $18\times$ fewer visual prompt parameters, and delivering a 3.1% improvement in performance.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper addresses the task of visual prompting for adapting pre-trained models to specific downstream tasks. The paper investigates the limitations of existing visual prompting techniques, which often based on padding. The paper also proposes a new visual prompting technique based on low-rank matrix multiplication.

### Strengths
- The paper identifies the limitations of existing visual prompting techniques, which often restrict interaction between visual prompts and the original image to a small set of patches.
- A novel visual prompt design based on low-rank matrix multiplication is proposed. This design allows for shared and patch-specific information across rows and columns of image pixels.
- The results are convincing and demonstrate performance and efficiency improvements. The authors include extensive experiments across seven network architectures and several datasets showing a performance improvement compared to state-of-the-art methods.
- The paper is well written and clear.

### Weaknesses
 - A low-rank matrix multiplication is just one way of sharing information across patches. I am surprised that other approaches have not been tested.
- The conclusions in the paper are very superficial and do not offer a deeper insight into the experimental results and the strengths and weaknesses of the proposed approach.
- The paper uses linear probing to transform the labels from the source to the target domain. This is a very simple model and it is not clear why this is more appropriate than other transform models.

### Questions
- Why are alternative approaches of sharing information across patches not explored? 
- The paper uses linear probing to transform the labels from the source to the target domain. This is a very simple model and it is not clear why this is more appropriate than other transform models.
- If I understand correctly, all downstream tasks are image classification tasks. Would the approach be able to deal other downstream tasks, e.g. object detection or segmentation?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes the incorporation of low-rank matrix multiplication in visual prompting, resulting in improved performance compared to existing visual prompting methods, as well as enhanced training speed.

### Strengths
1. the paper is very well-written and easy to follow. The background part is very clear and detailed.
2. the method is simple yet effect. And the author gives good preliminary analysis that motivates the method, which makes a lot of sense to me.

### Weaknesses
1. Regarding the pad-based method, the authors state, "The VP parameters are restricted to interacting with the original image in a limited set of patches, leaving a substantial portion of the image unmodified." I find this assertion questionable. If the backbone is a ViT, the padded tokens will interact with the inner tokens through self-attention, potentially affecting the entire image. The degree of this interaction and its impact on the prompt's effectiveness needs further investigation. Specifically, it's unclear how the spatial locality of the prompt is preserved or diluted through the self-attention mechanism.
2. The authors do not include a comparison or discussion of visual prompt tuning [1], which is a more prevalent method than those cited in the paper. This omission makes it difficult to assess the relative performance of the proposed method against a strong baseline.
3. The dataset utilized in the out-of-distribution generation experiments is insufficient to demonstrate the robustness of the method. It employs several variants of ImageNet, which exhibit minimal domain gaps, and all tasks focus on general object recognition. I recommend using a benchmark similar to AutoVP [2], which includes fine-grained classification and domain-specific tasks for a more comprehensive evaluation. The current evaluation lacks the diversity necessary to convincingly demonstrate the method's generalization capabilities.
4. The comparison between AutoVP and LP appears unusual, as LP seems to outperform AutoVP in most cases. This contradicts the conclusions drawn in the AutoVP paper. Additionally, the performance gap between LoR-VP and LP is minimal. What would be the outcome if AutoVP's output transformation were replaced with LP? This raises questions about the true contribution of the low-rank adaptation beyond a simple linear probing baseline.
5. As a general PEFT method, the evaluation is limitated to image classification, without extension to other tasks such as segmentation, detection, or caption.

### Questions
Please see weakness

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces Low-Rank Visual Prompting (LoR-VP), which uses low-rank matrix multiplication to generate visual prompt, enabling more efficient information sharing across image patches, taking the inductive biases among them into consideration. The authors conducted a preliminary study comparing current SOTA (AutoVP) with three new VP designs, proving that VP should combine the benefits of both patch-specific and shared visual prompting. Tested on several network architectures and datasets, the proposed approach reduces the number of tunable parameters by up to 18× and achieves up to 6× faster training times while improving performance by an average of 3.1%.

### Strengths
Organic integration of LoRA and VP: The originality and novelty of this paper lie in its clever integration of Low-Rank Adaptation (LoRA) with Visual Prompting (VP), two previously established concepts, to create a highly efficient and effective approach for adapting pre-trained vision models. While LoRA has been used to reduce the complexity of model fine-tuning, and Visual Prompting focuses on task-specific adaptation through input modification, the paper's innovation is in combining these methods in a seamless way that enhances both parameter efficiency and model performance. By introducing low-rank matrix multiplications into the visual prompting process, LOR-VP allows shared and patch-specific information across the entire image, significantly outperforming existing methods in both speed and accuracy.

Exemplary clarity of reasoning:  In the preliminary study, the authors provide a well-structured and logical explanation for their design choices. They clearly demonstrate why both patch-specific and shared information in visual prompts are necessary by highlighting the limitations of existing methods that treat patches independently or focus only on peripheral areas. Additionally, their decision not to scale down the image emphasizes the importance of retaining maximum information for accurate model adaptation. This clear, step-by-step reasoning effectively justifies the development of LOR-VP, ensuring the method addresses these shortcomings while optimizing performance.

### Weaknesses
The preliminary study lacks rigor in controlling variables, as the impact of image scaling is not isolated from the role of patch-specific information. While design 4 (Patch-Same) outperforms others, the study does not definitively clarify whether its success is due to shared prompting across patches or the fact that the image is not scaled, leaving ambiguity about the true cause of the performance improvement. This undermines the ability to attribute the gains solely to patch sharing.

In the methodology section, the paper lacks formal mathematical proof detailing how the information across rows and columns in the visual prompts is linked, which leaves the assumptions of inductive bias vague. Additionally, while the low-rank matrix approach is intended to capture shared information, it does not explicitly guarantee that the natural relationship between neighboring pixels is preserved, and the exact nature of the associations formed between pixels remains unclear, weakening the justification for its effectiveness.

The method's performance relies heavily on empirical results without offering strong theoretical guarantees about convergence, optimality, or robustness in different settings, which could limit its broader adoption in critical applications.

The ablation studies comparing different output transformations lack clarity in distinguishing the contributions of the output transformation versus the LOR-VP component. Simply showing that LOR-VP outperforms other methods under the same output transformation doesn't clarify whether the performance gains are primarily due to the low-rank adaptation (LoRA) or the output transformation itself. Additionally, there is a noticeable performance drop for ViT models when using ILM and FLM, while Swin models do not exhibit this behavior. The authors fail to investigate or explain this discrepancy, leaving a gap in understanding why certain architectures are more sensitive to specific label mapping methods. A more detailed analysis of these interactions and a clearer separation of the contributions from each component are needed for a more rigorous assessment.

The paper lacks a thorough analysis of failure cases or edge scenarios where the LOR-VP method may struggle, such as on noisy or adversarial images. While the authors conduct robust experiments across multiple datasets and architectures, there is no exploration of how the method performs under conditions that deviate from the standard datasets, like adversarial attacks or high levels of image noise. For example, in Section 5.3, where robustness is discussed, the evaluation focuses on out-of-distribution generalization but does not account for adversarial robustness or resilience to noise, which are critical factors for real-world deployment. Without this analysis, it is unclear how reliable or stable LOR-VP would be in challenging environments, potentially limiting its practical use in more demanding applications.

### Questions
Impact of Image Scaling vs. Patch-Specific Information: Can you provide additional experiments or controlled studies to isolate the impact of image scaling from patch-specific information, to clarify whether the performance gains in design 4 are due to shared prompting or the lack of image scaling?

Mathematical Proof for Row and Column Information Link: Could you include a more formal mathematical explanation or proof of how the information across rows and columns in the visual prompts is linked, ensuring that the inductive bias of neighboring pixels being more related than distant ones is preserved?

Theoretical Guarantees on Convergence and Robustness: Can you offer theoretical insights or guarantees about the convergence, optimality, or robustness of the LOR-VP method, to complement the empirical results and ensure its reliability in diverse settings?

Clarifying the Contributions of Output Transformation vs. LOR-VP: Could you conduct additional ablation studies to more clearly separate the impact of the output transformation from the LOR-VP component, particularly to clarify why ViT models show a significant performance drop with ILM and FLM while Swin models do not?

Analysis of Sensitivity to Label Mapping in Different Architectures: Can you explore why ViT models seem more sensitive to label mapping methods compared to Swin models, and provide a deeper investigation into the factors causing this discrepancy?

Handling Noisy or Adversarial Images: Can you include experiments testing LOR-VP's performance under adversarial attacks or in the presence of noise, to assess its robustness and ensure its reliability in more challenging or real-world scenarios?

### Soundness
2

### Presentation
3

### Contribution
3
