# DEEM: Diffusion models serve as the eyes of large language models for image perception

- Decision: Accept
- Scores: 6, 8, 8, 8, 6

## Abstract
label{sec:abs}
The development of large language models (LLMs) has significantly advanced the emergence of large multimodal models (LMMs). While LMMs have achieved tremendous success by promoting the synergy between multimodal comprehension and creation, they often face challenges when confronted with out-of-distribution data, such as which can hardly distinguish orientation, quantity, color, structure, etc. This is primarily due to their reliance on image encoders trained to encode images into task-relevant features, which may lead them to disregard irrelevant details. Delving into the modeling capabilities of diffusion models for images naturally prompts the question: Can diffusion models serve as the eyes of large language models for image perception? In this paper, we propose \name, a simple but effective approach that utilizes the generative feedback of diffusion models to align the semantic distributions of the image encoder. This addresses the drawbacks of previous methods that solely relied on image encoders like CLIP-ViT, thereby enhancing the model's resilience against out-of-distribution samples and reducing visual hallucinations. Importantly, this is achieved without requiring additional training modules and with fewer training parameters. We extensively evaluated \name on both our newly constructed RobustVQA benchmark and other well-known benchmarks, POPE and MMVP, for visual hallucination and perception. In particular, \name improves LMM's  visual perception performance to a large extent (e.g., 4\% ↑ on RobustVQA, 6.5\% ↑ on MMVP and 12.8 \% ↑ on POPE ). Compared to the state-of-the-art interleaved content generation models, \name  exhibits enhanced robustness and a superior capacity to alleviate model hallucinations while utilizing fewer trainable parameters, less pre-training data (10\%), and a smaller base model size. Extensive experiments demonstrate that \name enhances the performance of LMMs on various downstream tasks without inferior performance in the long term, including visual question answering, image captioning, and text-conditioned image synthesis

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces the diffusion model into the image perception process of large language models to reduce excessive compression of visual details, thereby enhancing the model's robustness and its ability to mitigate hallucinations. An end-to-end multimodal model with interleaved text-image modeling capabilities is trained to perform various multimodal tasks in a unified manner. A new robustness benchmark for large multimodal models is developed to assess their visual robustness capabilities. The extensive experimental results demonstrate the effectiveness of the proposed method.

### Strengths
1. The paper introduces a new benchmark, RobustVQA, specifically designed for evaluating the visual robustness capabilities of the large multimodal models.
2. The proposed method is the first to introduce the diffusion model into the image perception of large language models, which is simple but effective.
3. The proposed method trained end-to-end with interleaved text-image data can perform various multimodal tasks in a unified manner.

### Weaknesses
1. The insight of the paper is the integration of the diffusion model into the image perception process of LLMs while training to correct potential semantic biases in the image encoder. It is crucial to validate the generalization capability of the proposed method across existing LMMs to enhance their image perception. However, the validation is somewhat limited, focusing solely on LLaVA, as shown in Table 5. Could the proposed method be flexibly applied to additional existing architectures, such as BLIP-2 and MiniGPT-4?
2. The claim that the proposed method can "correct potential semantic bias in the image encoder and alleviate excessive compression of visual details" seems intuitive. Are there any validations or qualitative comparisons between existing LMMs trained with and without this method? For instance, maybe comparisons of feature maps for image tokens encoded by the image encoder trained with and without the proposed method.
3. The contribution of the constructed RobustVQA benchmark seems somewhat limited, as it focuses primarily on evaluating visual robustness. Emphasizing the unique advantages of the RobustVQA benchmark over existing benchmarks through more extensive qualitative or quantitative comparisons with other benchmarks in some aspects would enhance its value.

### Questions
See Weaknesses

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper enhances large language models image perception by using diffusion models to align image encoder semantics, improving resilience to out-of-distribution data and reducing visual hallucinations. Without extra modules or parameters, DEEM outperforms on benchmarks like RobustVQA, POPE, and MMVP, using fewer parameters and less data. It strengthens visual tasks such as question answering, captioning, and image synthesis, showcasing robust perception and reduced hallucinations.

### Strengths
1. This paper design a new robustness benchmark RobustVQA for visual robustness capabilities of multi modal models.
2. DEEM is the first approach to enhance image perception in LLMs using diffusion models, making it novel.
3. This approach is highly versatile, demonstrating effective experimental results across benchmarks.
4. This paper is well written and easy to follow.

### Weaknesses
 1. Since diffusion models need to be utilized during both training and inference, the computational cost will be high.
2. If this model is used with an LLM that has a much larger number of parameters, how would its performance be affected?

### Questions
Please refer to weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposed a method to enhance the image perception ability of large multimodal models (LMMs), by leveraging the generative feedback of diffusion models. This reduced the visual hallucination and strengthen the perception ability in against out-of-distribution samples. Also a benchmark is developed, specifically designed for out-of-distribution or challenging samples. Extensive experiments showed that the proposed method achieves an improvement in a collection of benchmarks and downstream tasks.

### Strengths
The paper is well-structured and it shows a good originally. This is a pioneering work in using diffusion models to specifically enhance the image perception capabilities of LMMs.

### Weaknesses
W1) The detail information of RobustQA is missing. This makes the experiments result look less convincing. How many samples are in the benchmark? Please also include a diversity chart to show how robust the benchmark is.

W2) Figure 2 is difficult to follow. Please revise the figure, e.g. adding some step indicators, legends for arrows.

W3) Typo "obnly" in the last paragraph of Section 3.3.

### Questions
Q1) Regarding RobustVQA, would it be possible to also run on close-source models (GPT4o/Gemini1.5Pro)? I am curious on how the close-source solutions perform against the proposed benchmark.

Q2) In Table 9, it states "Questions in the yes or no format can well evaluate the performance of the models on the RobustVQA benchmark, while questions in the multiple choice format are very random, and MM-interleaved tend to output the first option. Therefore, we
adopt yes or no format in our experimental settings." seems a bit unconvincing to me. Would LMM also be easier to guess the solution if there is only 2 choices for yes/no format?

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The DEEM model integrates diffusion models with large multimodal models (LMMs) to enhance image perception capabilities, especially for out-of-distribution data. DEEM employs generative feedback from diffusion models to correct potential semantic biases in image encoders, resulting in more accurate and robust visual perception. Evaluations across benchmarks such as RobustVQA, POPE, and MMVP demonstrated improvements in visual robustness and reduced visual hallucinations compared to traditional methods. This enhancement is achieved without additional training parameters, using fewer resources and a smaller model scale.

### Strengths
1.	Innovation in Multimodal Integration: DEEM introduces diffusion models as “visual auditors” for LMMs, a novel approach for refining visual inputs and reducing errors from biased image encoders.
	2.	Efficiency: The approach reduces dependency on larger, more complex models by using a smaller image encoder (CLIP-ConvNext-B), which lowers computational requirements.
	3.	Robustness: Demonstrates resilience against adversarial and out-of-distribution data, enhancing the model’s suitability for diverse, real-world scenarios.
	4.	Extensive Evaluation: The paper provides a comprehensive analysis using custom (RobustVQA) and widely recognized benchmarks (POPE and MMVP), showing DEEM’s performance gains in both robustness and visual perception.

### Weaknesses
1.	Reliance on Diffusion Models: Although diffusion models enhance robustness, they also introduce computational complexity. Future versions might explore alternative approaches that achieve similar robustness with lower computational costs. Specifically, the computational overhead of the diffusion process, especially during iterative refinement, could be a bottleneck for real-time applications or deployment on resource-constrained devices. The paper does not sufficiently explore the trade-offs between the level of diffusion refinement and the resulting performance gains, leaving open the question of whether a less computationally intensive diffusion process could achieve comparable results.
	2.	Generalization Limits: While DEEM shows strong performance for specific multimodal tasks, its generalization to other modalities (e.g., audio) remains unexplored. The current approach is heavily tailored to visual inputs and may not be directly transferable to other modalities without significant modifications. The paper lacks a discussion on the challenges and potential adaptations required to extend DEEM to other data types, such as time-series data or textual data beyond image captions, which limits the broader applicability of the proposed method.
	3.	Training Overheads: The training process, though optimized, may still be prohibitive for some use cases where computational resources are constrained. The paper does not provide a detailed analysis of the training time and memory requirements, making it difficult to assess the practical feasibility of the approach for different computational environments. Furthermore, the paper does not explore techniques such as distributed training or model parallelism to mitigate these overheads, which could be crucial for scaling the method to larger datasets or more complex models.

### Questions
1. Could the diffusion model’s role be optimized or reduced without compromising robustness? For instance, could a selective application of diffusion-based feedback lower training costs?
2. Could the impact of scaling down the diffusion model be evaluated further to assess how smaller models might perform in balancing robustness and efficiency?
3. Have you considered a comparative analysis of DEEM with approaches like "De-Diffusion Makes Text a Strong Cross-Modal Interface"?

https://openaccess.thecvf.com/content/CVPR2024/papers/Wei_De-Diffusion_Makes_Text_a_Strong_Cross-Modal_Interface_CVPR_2024_paper.pdf

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces DEEM, a method that leverages the generative feedback of diffusion models to align the semantic distributions of image encoders, addressing issues faced by large multimodal models (LMMs) when encountering out-of-distribution data such as orientation, quantity, color, and structure. DEEM improves the resilience of LMMs against such data and reduces visual hallucinations without the need for additional training modules and with fewer training parameters. It demonstrates significant improvements in visual perception performance across several benchmarks (RobustVQA, POPE, and MMVP), exhibiting enhanced robustness and superior capability to mitigate model hallucinations while using fewer trainable parameters and less pre-training data, and being smaller in base model size. Extensive experiments show that DEEM enhances the performance of LMMs across various downstream tasks, including visual question answering, image captioning, and text-conditioned image synthesis.

### Strengths
**Strengths**

1. **Originality**:
   - The paper presents a novel approach, DEEM, which integrates diffusion models to enhance the visual perception capabilities of large language models (LLMs) for multimodal tasks. 

2. **Quality**:
   - The paper provides comprehensive empirical evidence to support the effectiveness of the proposed method. The authors perform extensive evaluations on newly constructed and well-known benchmarks (e.g., RobustVQA, POPE, and MMVP), demonstrating the method's robustness and performance improvements.

3. **Clarity**:
   - The paper is well-structured and clearly written, providing a detailed description of the DEEM architecture, training process, and experimental evaluation.

4. **Significance**:
   - DEEM significantly enhances the robustness and visual perception capabilities of LMMs, addressing a critical challenge in the field of multimodal machine learning.

### Weaknesses
 **Weaknesses**

1.  **Scalability Concerns**:
    - While DEEM demonstrates improved performance using fewer training parameters and a smaller base model size, the requirement to employ diffusion models as an additional component could potentially increase computational overhead. The computational cost of running the diffusion model, especially during training, is non-trivial, and this overhead may become a significant bottleneck as the size of the image encoders and the resolution of input images increase.
    - As the model size continues to grow, will the computational burden brought by the diffusion models outweigh the performance gains? After all, as the model size increases, its capabilities significantly improve, and computational costs become the primary bottleneck. The introduction of diffusion might bring negative returns. The paper does not provide a detailed analysis of the computational scaling of DEEM with respect to the size of the image encoder and the input resolution, which is crucial for assessing its practical applicability.

2.  **Robustness Limitation**:
    - Although DEEM significantly enhances visual robustness, the paper acknowledges that the method cannot completely eliminate but only alleviate robustness knowledge forgetting during subsequent fine-tuning stages. This indicates a potential long-term limitation in maintaining the enhanced robustness through the entire lifecycle of model updates and task-specific fine-tuning. The paper lacks a thorough investigation into the mechanisms that cause this robustness forgetting and how it can be mitigated more effectively. It is unclear if the forgetting is due to the fine-tuning process itself or inherent limitations in the DEEM architecture.

3.  **Limited Analysis of Failure Cases**:
    - The paper largely focuses on positive results and improvements brought by DEEM. However, it lacks an in-depth analysis of cases where the method might fail or underperform compared to existing approaches. In particular, in the example shown in figure 9 of the supplementary materials, many generated images exhibit significant errors in color, spatial arrangement, and orientation. These generation flaws somewhat undermine the paper's claim that diffusion models can enhance visual understanding, as diffusion models also cannot perfectly restore visual features. The paper should include a more comprehensive analysis of failure modes, including specific examples and potential reasons for these failures, to provide a more balanced view of the method's capabilities and limitations.

### Questions
**Questions for the Authors**

1. **Scalability and Computational Efficiency**:
   - How does the use of diffusion models as an additional component impact the overall computational efficiency and memory usage, especially for larger versions of image encoders?
   - Have you explored any strategies for optimizing computational resources? If so, could you provide details on these optimization techniques and their effectiveness?

2. **Robustness Knowledge Forgetting**:
   - You mentioned that DEEM cannot completely eliminate robustness knowledge forgetting. Do you have insights or preliminary results on potential methods for further mitigating this issue?

3. **Failure Case Analysis**:
   - Could you provide more details or examples of cases where DEEM underperforms compared to other state-of-the-art methods?
   - What common patterns or factors have you identified in these failure cases, and what potential solutions might address these issues?

4. **Impact of High-Resolution Inputs**:
   - How does the increase in input image resolution from 256 to 448 pixels impact the performance and training dynamics? Are there diminishing returns at higher resolutions?
   - Have you evaluated the impact of image resolution on the computational requirements and time to convergence?

5. **Diffusion Model's Role**:
   - Could you elaborate on how the diffusion model corrects and aligns the semantic outputs of the image encoder during training? Are there specific examples or visualizations that illustrate this process?
   - How critical is the specific architecture or configuration of the diffusion model in achieving these results?

In summary, while the paper proposes combining diffusion models with LLMs to enhance the model's perceptual capabilities, this approach is not entirely novel, as seen in works like Transfusion (https://www.arxiv.org/abs/2408.11039). Additionally, if the sole purpose is to enhance the model's visual perception, introducing such a complex diffusion module may seem excessive. If a diffusion module is introduced, the authors should also focus on evaluating image generation capabilities. Alternatively, the authors should attempt to use simpler methods as baselines to highlight the necessity of introducing the diffusion module. The ablation studies in the paper do not seem to cover this aspect.

### Soundness
2

### Presentation
2

### Contribution
2
