# Hummingbird: High Fidelity Image Generation via Multimodal Context Alignment

- Decision: Accept
- Scores: 8, 6, 6, 6

## Abstract
While diffusion models are powerful in generating high-quality, diverse synthetic data for object-centric tasks, existing methods struggle with scene-aware tasks such as Visual Question Answering (VQA) and Human-Object Interaction (HOI) Reasoning, where it is critical to preserve scene attributes in generated images consistent with a multimodal context, i.e. a reference image with accompanying text guidance query. To address this, we introduce $\textbf{Hummingbird}$, the first diffusion-based image generator which, given a multimodal context, generates highly diverse images w.r.t. to the reference image while ensuring high fidelity by accurately preserving scene attributes, such as object interactions and spatial relationships from the text guidance. Hummingbird employs a novel Multimodal Context Evaluator that simultaneously optimizes our formulated Global Semantic and Fine-grained Consistency Rewards to ensure generated images preserve the scene attributes of reference images in relation to the text guidance while maintaining diversity. As the first model to address the task of maintaining both diversity and fidelity given multimodal context, we introduce a new benchmark formulation incorporating MME Perception and Bongard HOI datasets. Benchmark experiments show that Hummingbird outperforms all existing methods by achieving superior fidelity while maintaining diversity, validating Hummingbird's potential as a robust multimodal context-aligned image generator in complex visual tasks.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces Hummingbird, a diffusion-based image generator that aligns generated images with a multimodal context comprising a reference image and text guidance. The model combines Global Semantic and Fine-Grained Consistency Rewards by a Multimodal Context Evaluator, leveraging vision-language models (BLIP-2). Hummingbird generates high-fidelity images that preserve scene attributes while maintaining diversity, performing favorably against state-of-the-art (SOTA) methods in tasks such as Visual Question Answering (VQA) and Human-Object Interaction (HOI) Reasoning.

### Strengths
1.	Interesting framework. The use of the Multimodal Context Evaluator with reward mechanisms (Global Semantic and Fine-Grained Consistency) is a unique approach that successfully addresses both the fidelity and diversity.
2.	Comprehensive Evaluation. The model is tested across various benchmarks and datasets, including VQAv2, GQA, and ImageNet, validating robustness under both scene-aware and object-centric tasks.
3.	Performance Gains. Empirical results show that Hummingbird consistently performs favorably against the other SOTA methods in terms of accuracy and consistency for VQA and HOI tasks. This validates the effectiveness of the proposed method in downstream tasks.
4.	Detailed Analysis: The paper includes thorough ablation studies that explore the impact of individual components and different pretrained MLLMs.

### Weaknesses
1.	Clarity of the Fine-Grained Consistency Reward. How the ITM classifier's positive class is determined sholud be clarified further.  What does the class ‘j’ mean in equation (5)?
2.	Limitations are not discussed. It would be more insightful to discuss about the potential limitations and possible improvement of the idea.

### Questions
### Questions
1.	How does the ITM classifier select the positive class for computing the Fine-Grained Consistency Reward?
2.	Would the model maintain robust performance when using alternative, less powerful MLLMs or other multimodal context encoders in place of BLIP-2?
3.	Could the method be adapted for tasks involving more nuanced or abstract text guidance beyond factual scene attributes, such as visual structures (e.g., relative positioning of objects) or style?

### Comments
- Including failure cases or limitations would provide more completeness of the paper.
- The paper would give more insights if the paper could outline about the future work.

### Soundness
4

### Presentation
4

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
This paper proposes an image data augmentation pipeline based on diffusion models. Paired reference image and text guidance embeddings have been used into a diffusion model with LoRA to generate an image, and then the image can be optimized by a multimodal context evaluator who returns a global semantic reward and fine-grained consistency reward. Experimental results have been conducted to prove its effectiveness

### Strengths
1. The first work applying diffusion models for image data augmentation.
2. A pioneering study demonstrating the potential of synthetic data.
3. Produces impressive results.

### Weaknesses
1. The writing needs improvement; for example, the introduction should clearly state that the research task focuses on data augmentation.
2. Consider adding the following experiments: 1) evaluation of augmented image quality, such as using FID scores and user studies. 2) more assessment of the proposed augmentation's performance in training, not test-time. 3) Inclusion of a baseline in Table 4, such as "random seed + stable diffusion," to compare data augmentation capabilities, as the vanilla diffusion model does have variety, and I think 20 random seeds are not enough.
3. Other aspects mentioned in Questions.

### Questions
1. Could you provide further details on how to enhance the fidelity of generated images with respect to spatial relationships? While the CLIP Text Encoder is effective, it sometimes struggles to accurately capture spatial features when processing the longer sentences in the Context Description in Figure 2.
2. when generating the x_hat, you use CLIP Image Encoder and CLIP Text Encoder. However, in the BLIP-2 module, you opt for the BeRT text encoder instead. Could you clarify the rationale behind this choice?
3.  How is Textual Inversion, which fine-tunes a rarely used text embedding to learn novel concepts, being applied for data augmentation in your comparison experiments?
4.  Regarding line 274, what criteria do you use for convergence? Additionally, could you present your convergence curve in experiment?

### Soundness
2

### Presentation
2

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
The paper presents a new diffusion-based image generation method designed to address the challenge of maintaining both diversity and high fidelity in multimodal contexts. The main contributions are:

1. Introducing Hummingbird, a diffusion model capable of generating high-fidelity and diverse images based on multimodal context (a reference image and text guidance).

2. Proposing a novel Multimodal Context Evaluator that simultaneously maximizes global semantic and fine-grained consistency rewards, ensuring that the generated images maintain scene attributes from the multimodal context while preserving diversity.

3. Presenting a new benchmark using the MME Perception and Bongard HOI datasets, demonstrating Hummingbird's superiority in generating high-fidelity and diverse images compared to existing methods.

### Strengths
Originality: The paper introduces a new multimodal context alignment approach that balances diversity and fidelity. The introduction of a Multimodal Context Evaluator and reward mechanism demonstrates high originality.

Quality: The experimental design is well-conducted, clearly validating the proposed method's effectiveness in maintaining diversity and high fidelity.

Significance: Generating high-fidelity and diverse images is crucial for many complex visual tasks, particularly those involving scene understanding. Hummingbird demonstrates excellent performance in this area.

Clarity: The paper is well-organized, with a natural flow between sections, and the experimental results clearly highlight the comparative advantages over existing methods.

### Weaknesses
1. Lack of comprehensive theoretical basis: While global semantic and fine-grained consistency rewards are proposed, there is a lack of detailed mathematical derivation or theoretical analysis, especially regarding why these rewards are effective in improving fidelity.

2. Limited evaluation dataset diversity: The paper uses the MME and Bongard HOI datasets, but their representativeness may be limited, particularly regarding generalizing the model to broader scenarios. It is recommended to validate the method on more diverse datasets in future work.

### Questions
1. What is the basis for selecting the global semantic and fine-grained consistency rewards in the Multimodal Context Evaluator? Could more mathematical derivation or theoretical support be provided to explain the effectiveness of these reward mechanisms?

2. The experiments primarily use the MME and Bongard HOI datasets. Could the performance of the method be validated on larger or more diverse datasets? This would be crucial to demonstrate the generalizability of the method.

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces Hummingbird, an image generation model that creates high-fidelity and diverse images aligned with multimodal context. It outperforms other methods on scene-aware tasks and uses a novel evaluator to optimize image generation.

### Strengths
1、High Fidelity and Diversity: Hummingbird generates images that are both diverse and maintain high fidelity to the multimodal context, which is crucial for complex visual tasks like VQA and HOI Reasoning.

2、Novel Multimodal Context Evaluator: The model uses a new evaluator that optimizes Global Semantic and Fine-grained Consistency Rewards, ensuring that generated images accurately preserve scene attributes from the reference image and text guidance.

3、Superior Performance: Benchmark experiments demonstrate that Hummingbird outperforms existing methods, showing its potential as a robust multimodal context-aligned image generator.

### Weaknesses
1、What is the use of using multimodal input as a condition? What are the benefits of using text as a condition compared to Stable Diffusion?

2、The sophisticated Multimodal Context Evaluator and the fine-tuning process might imply high computational requirements.

3、The performance of Hummingbird is likely to depend heavily on the quality and relevance of the multimodal context (reference image and text guidance) provided. In scenarios where the context is ambiguous or low-quality, the model's effectiveness may be compromised.

4、While Hummingbird shows strong performance on VQA and HOI Reasoning tasks, the document does not provide evidence of its effectiveness on a broader range of tasks.

### Questions
See weakness.

### Soundness
3

### Presentation
3

### Contribution
3
