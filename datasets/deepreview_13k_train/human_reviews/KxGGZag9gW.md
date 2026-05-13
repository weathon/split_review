# EigenLoRA: Recycle trained Adapters for Resource Efficient Adaptation and Inference

- Decision: Reject
- Scores: 6, 3, 5, 6

## Abstract
Low-Rank Adapters (LoRA) are lightweight components that have made fine-tuning large models on domain-specific tasks inexpensive. This has resulted in an abundance of adapters in a growing open-source public community. We ask the question: can these adapters be used to inform and further streamline adaptation to new tasks? We introduce EigenLoRA, a parameter-efficient fine-tuning method that uses trained adapters to perform fast adaptation on new domains with orders of magnitude fewer parameters than LoRA. Our method finds a principal subspace that aligns with the domain of the trained adapters. This allows for efficient and fast adaptation to new tasks in this domain by simply learning coefficients on the principal components of this subspace. Furthermore, EigenLoRA makes inference time task-switching memory efficient. Instead of saving and loading whole LoRAs, EigenLoRA can simply load lightweight coefficients. EigenLoRA works across a variety of domains and tasks and is a viable solution for edge-based and efficient personalization applications.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces EigenLoRA, an approach for parameter-efficient fine-tuning that leverages the principal subspaces of low-rank adapters (LoRA) trained on various domain-specific tasks. EigenLoRA reduces the parameter count by up to 100x and optimizes memory efficiency, benefiting tasks such as inference on resource-constrained devices. By identifying a domain’s principal subspace, EigenLoRA offers a lightweight way to perform new task adaptations by only learning coefficients within this subspace, avoiding full weight reinitialization. The approach is validated on image classification and NLP benchmarks, demonstrating competitive performance with significantly lower computational overhead.

### Strengths
1. EigenLoRA achieves high parameter and memory efficiency, cutting parameters by up to 100x. This makes it ideal for low-resource deployments.
2. The method performs well across various tasks, matching LoRA’s results with far fewer parameters, and proving its versatility.
3. Figures and tables are well-designed.
4. EigenLoRA’s low memory demand fits well with real-world edge applications, like personal devices with limited resources.

### Weaknesses
1. EigenLoRA’s success depends on high-quality adapters, which might be limiting in under-researched domains. The method's reliance on the principal components of LoRA adapters means that if these adapters are not well-trained or if they encode noise, the performance of EigenLoRA could degrade significantly. This is particularly concerning in domains where pre-trained adapters are scarce or of questionable quality, potentially hindering the applicability of the method.
2. Guidance on picking the right number of principal components would help with applying this method across diverse tasks. The paper lacks a clear methodology for determining the optimal number of principal components to retain for a given task. This is a critical parameter that can significantly impact performance, and without clear guidelines, users may struggle to apply EigenLoRA effectively across different domains and tasks. The absence of a principled approach for this selection makes the method less user-friendly and potentially less robust.
3. Failure cases need more examples to help users understand when and why the method might struggle. While the paper presents successful applications of EigenLoRA, it lacks a thorough analysis of scenarios where the method fails or underperforms. Understanding these failure modes is crucial for users to assess the limitations of EigenLoRA and to make informed decisions about its applicability. More detailed examples of failure cases, along with explanations of the underlying causes, would be beneficial.
4. While suited for edge devices, more real-world benchmarks would strengthen claims about efficiency in low-memory environments to meet ICLR standards. The paper claims that EigenLoRA is suitable for edge devices due to its low memory footprint. However, the experimental validation primarily focuses on standard benchmarks. To better support this claim, the paper should include evaluations on more realistic edge device scenarios, such as resource-constrained hardware or tasks with real-time constraints.

### Questions
Q1. How do you envision managing the dependency on trained adapters in a practical deployment setting? Are there scenarios where this reliance could hinder flexibility?
Q2. Can EigenLoRA be extended or modified to handle tasks involving multi-modal or cross-domain data? If so, what challenges do you foresee?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces EigenLoRA, a parameter-efficient fine-tuning method that improves upon LoRA by recycling information from previously trained adapters through identifying a principal subspace shared by adapters trained on related tasks within a domain, allowing new tasks to be adapted by learning coefficients for pre-extracted principal components rather than full LoRA matrices, which results in using up to 100x fewer parameters and achieving up to 2x faster convergence during training while improving memory efficiency by ~18x when switching between multiple tasks during inference by only loading lightweight coefficients rather than full adapter matrices, demonstrating wide applicability across different modalities and domains with both theoretical foundations including approximation bounds for reconstruction error and practical validation, positioning it as a resource-efficient solution particularly suitable for edge devices and personalization applications.

### Strengths
This work presents comprehensive experiments and evaluations on language and CV models, image generation, and achieves good results.

### Weaknesses
1. Absent evidence of practical cost optimization: In fact, the reduced number of training parameters but still requires a large number of fixed parameters in the forward process. These fixed parameters also incur significant additional overhead. That is, this approach does not significantly reduce the time and memory needed in fine-tuning. Just reducing training parameters is not practical and diminishes fine-tuning performance.


2. Lack of novelty: Actually, this work just utilizes SVD as the initialization of LoRA and dynamically selects the fine-tuning of the eigens, which  already many studies in previous works. Adaptive Budget Allocation for Parameter-Efficient Fine-Tuning (ICLR), DyLoRA: Parameter-Efficient Tuning of Pre-trained Models using Dynamic Search-Free Low-Rank Adaptation. EACL.


3. Lack of solid evaluations: Evaluation In Vision Transformer, the GLUE benchmark heavily relies on hyperparameter tuning, and the image generation fine-tuning effect is not sensitive to the design of the LoRA. In other words, those presented experiments  are not a solid reflection of the performance of the proposed method. I suggest that the authors present more evidence of in Commonsense Reasoning and instruction fine-tuning tasks in recent LLMs. e.g., Llama 3 8B and 70B, Llama 3.2 1B and 3B, DeepSeekMoE，Mixtral-8x7B.

4. Numbers Trainable Parameters such as +0, in Tables 1 and 3 are confusing. I believe that +0 does not mean that there is no additional fine-tuning overhead . The authors need to use other cost metrics.

5. Absence of theoretical Support: why partial updated LoRA variants like this one would be better than full parameter updated LoRA variants. 

6. Lack of recent parameter-efficient LoRA method discussion. e.g., LoRA-XS: Low-Rank Adaptation with Extremely Small Number of Parameters, NoRA: Nested Low-Rank Adaptation for Efficient Fine-Tuning Large Models.

### Questions
See weaknesses.

### Soundness
3

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
3

### Summary
This paper introduces EigenLoRA, a parameter-efficient fine-tuning method centers on extracting a shared subspace of essential directions (PCs) from multiple already-trained LoRA adapters. Instead of learning a full new adapter for each task, it only learns a small set of task-specific coefficients that combine these principal components to achieve adaptation. This approach dramatically reduces the number of parameters needed for fine-tuning and allows efficient task-switching by loading just the task-specific coefficients rather than full adapter matrices.

### Strengths
1. EigenLoRA significantly reduces the number of trainable parameters required for new tasks, which is particularly valuable for low-resource devices or applications with strict memory constraints. By isolating task-specific coefficients and retaining shared principal components, EigenLoRA offers a reduction in memory usage during inference.

2. The method is empirically validated on diverse domains—including image classification, natural language understanding, and text-to-image generation—demonstrating its versatility and robustness across modalities and tasks.

3. EigenLoRA’s initialization in a shared principal subspace results in faster convergence during training, allowing it to reach or exceed baseline performance more efficiently than traditional approaches.

### Weaknesses
1. The paper omits evaluations on certain baseline datasets, such as the RESISC45 dataset for image classification, which was included in VeRA’s evaluations. 

2. The specific ViT model used for image classification is not clearly identified, and the paper does not fully explain why certain settings yield different results compared to those in baseline studies.

3. Unlike VeRA, which includes comparisons across different model backbones (for image classification), this paper only evaluates a single backbone, limiting the assessment of its generalizability.

4. While baseline methods conduct evaluations on E2E and instruction-tuning tasks, this paper neither includes these benchmarks nor provides a rationale for their exclusion.

5. The proposed method uses customized hyperparameter settings, including varying learning rates and schedulers, while baselines adhere to a fixed set of hyperparameters, potentially compromising the fairness of comparisons.

6. Although the authors mention a study of the effect of the number of principal components K in Section A.2.2, no detailed results are provided.

7. In lines 883-884, the choice of rank r = 8 is not explained, nor is there an exploration of the impact of different r values on performance.

8. Some figures appear to be low-resolution screenshots from wandb, affecting readability of visual results.

### Questions
See the weakness part

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The authors propose a new method based on LoRA called EigenLoRA. This method focuses on the K principal component of the weight matrices of LoRA. This allows for a reduction in the number of parameters to learn during training, time computation, and inference memory usage. After an introduction to their method, the authors propose several experimental studies to show the benefit of EignenLoRA for different modalities and tasks.

### Strengths
- The paper is very well written. It is easy to follow the paper and understand the needs of the field and how they improve LoRA with eigendecomposition.
- The method proposed is an simple but efficient improve of the LoRA method
- A complete experimental part is proposed where EigenLoRA is tested over four different datasets. Each experiment show a benefit of the method.

### Weaknesses
Major comment:
- The introduction and related work are short, and it could have been interesting to see a comparison with another method in the experiment study. Specifically, while the authors compare against LoRA, PiSSA, and VeRA, it would be beneficial to see a comparison against other dimensionality reduction techniques or other methods that also focus on low-rank adaptation. This would help to contextualize the performance of EigenLoRA within the broader landscape of parameter-efficient fine-tuning methods. The current comparisons, while relevant, do not fully explore the potential of alternative approaches.
- In part 4.2.1, the part with the initialization is not very clear. Why does initialization add a lot of parameters to EigenLoRA? Why does it help for specific tasks (see MRPC), and why is it disruptive for others (see RTE)? Do you have any intuitions? It's unclear how the initialization process interacts with the core EigenLoRA method, and the paper would benefit from a more detailed explanation of the mechanisms at play. The current explanation lacks sufficient depth to understand the behavior of the method under different initialization conditions.

Minor comments:
- Tables 2 and 3 have no bold performances, which is harder to read.
- No x-axis title for figure 4

### Questions
- In practice, how do you choose the K? Do you always have to find the K best representative principal components?

### Soundness
4

### Presentation
4

### Contribution
3
