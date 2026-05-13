# Human-Feedback Efficient Reinforcement Learning for Online Diffusion Model Finetuning

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
Controllable generation through Stable Diffusion (SD) fine-tuning aims to improve fidelity, safety, and alignment with human guidance. 
Existing reinforcement learning from human feedback methods usually rely on predefined heuristic reward functions or pretrained reward models built on large-scale datasets, limiting their applicability to scenarios where collecting such data is costly or difficult.
To effectively and efficiently utilize human feedback, we develop a framework, \myshorttitle{}, 
which leverages online human feedback collected on the fly during model learning. Specifically, \myshorttitle{} features two key mechanisms: (1) \emph{Feedback-Aligned Representation Learning}, an online training method that captures human feedback and provides informative learning signals for fine-tuning, 
and (2) \emph{Feedback-Guided Image Generation}, which involve generating images from SD's refined initialization samples, enabling faster convergence towards the evaluator's intent. 
We demonstrate that HERO is $4\times$ more efficient in online feedback for body part anomaly correction compared to the best existing method. 
Additionally, experiments show that HERO can effectively handle tasks like reasoning, counting, personalization, and reducing NSFW content with only 0.5K online feedback.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper introduces HERO, a framework for fine-tuning Stable Diffusion (SD) models using online human feedback to improve alignment with human intent. HERO addresses the limitations of traditional methods, which rely on costly predefined rewards or pre-trained models, by leveraging real-time human feedback through two main components: Feedback-Aligned Representation Learning and Feedback-Guided Image Generation. Experiments show that HERO is more efficient than prior methods in tasks such as anomaly correction, reasoning, counting, personalization, and reducing NSFW content, achieving significant improvements with minimal feedback.

### Strengths
* The article is well-structured and easy to follow, and the motivation is clear. The approach is simple but effective. 

* The proposed method seems to be novel. And the empirical results on several tasks demonstrate the effectiveness of the proposed method.

### Weaknesses
 * Compared to D3PO that does not require specific reward model, the proposed method in this paper clearly make the training process more complex and introduce computational overhead.

* The proposed method uses online human preferences. Does that mean the human annotator need to provide preference to the generated image at each run of the stable diffusion model? If so, it is might be difficult to collect enough data for training the encoder as contrastive learning requires a large amount of data to converge. Additionally, how to measure the performance of the trained encoder $E_\theta$?

* D3PO seems to be the closest baseline and achieves second-best results in Figure 3. Why the authors not provide results of D3PO in Table 2?

### Questions
Please refer to the Weakneses.

### Soundness
4

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
The paper introduces HERO, a novel framework designed for fine-tuning diffusion models using human feedback, aimed at improving text-to-image (T2I) generation tasks. HERO uses feedback-aligned representation learning to create a latent representation space guided by human annotations. Human evaluators categorize generated images into “best,” “good,” or “bad,” to guide a contrastive learning process that constructs an embedding space. Triplet loss is applied to align embeddings of “best” and “good” images while distancing “bad” images, resulting in a reward signal that guides the model toward human preferences. The framework employs DDPO (Diffusion-based Policy Optimization) for updates and uses LoRA for parameter efficient fine-tuning. At inference, images are sampled from a Gaussian mixture model based on the noise latents of “good” and “best” images from previous iterations, balancing quality and diversity. Experimental results indicate that HERO achieves high success rates across various T2I tasks, demonstrating both sample efficiency and superior performance compared to other feedback-guided methods.

### Strengths
- **Originality**: HERO presents a unique extension of binary signal methodologies to continuous reward signals, effectively merging representational learning with reinforcement learning to enhance the alignment of generated images with human feedback.
- **Clarity**: The paper is well-written, with clearly labeled diagrams and detailed qualitative examples that illustrate the feedback process. The structured presentation of the HERO framework, including its iterative feedback mechanism, allows readers to easily grasp the method's operation. The paper also includes many qualitative examples, showcasing the benefit of the HERO pipeline
- **Performance**: Results demonstrate that HERO significantly enhances sample efficiency and alignment compared to previous methods, highlighting its practical impact in T2I generation tasks.
- **Flexibility across tasks:** The results suggest that the pipeline can be widely applied to a wide range of tasks - such as content safety improvement to reasoning-based generation.

### Weaknesses
1. **Limited Task Diversity and Complexity**:
    - Evaluation is conducted across only five T2I tasks, which is significantly less than comparable works like D3PO, which evaluated across 300 prompts.
    - Tasks are primarily simple single-object scenarios and do not encompass multi-object compositions or complex interactions. Expanding to more challenging tasks would improve the robustness of the findings. The current tasks do not sufficiently explore the model's ability to handle complex spatial relationships, occlusions, or interactions between multiple objects, which are critical for real-world applications. For example, generating a scene with multiple interacting agents or objects with complex spatial arrangements would be a more rigorous test of the proposed method.

2. **Insufficient Diversity and Convergence Analysis**:
    - The paper lacks a quantitative analysis of the diversity-quality trade-off, particularly missing comparisons between non-fine-tuned and feedback-guided generators. The analysis should include metrics that specifically measure the range of outputs and the degree to which the model explores the latent space. Without this, it is difficult to assess whether the model is simply memorizing a narrow set of outputs or if it is truly generalizing. Furthermore, the paper does not analyze the convergence behavior of the fine-tuning process, which is essential to ensure that the model is not overfitting to the training data.
    - There are no established metrics for evaluating mode collapse or potential overfitting to ideal seeds, which could limit the practical application of the generator. The absence of such metrics makes it difficult to ascertain the robustness of the model and its ability to generate diverse and high-quality images across different initial conditions.

3. **Concerns Regarding Human Feedback Methodology**:
    - Results are reported based on a limited number of human evaluators, with each evaluator responsible for different seeds. This implies a lack of inter-annotator agreements and introduces potential biases from relying on individual evaluators, which could skew the model's alignment and generalization capabilities. The lack of inter-annotator agreement makes it difficult to assess the reliability of the human feedback and raises concerns about the generalizability of the results.
    - There is also limited information on evaluation reliability measures, such as the criteria used for selection. The paper should provide more details on the specific instructions given to the evaluators and the measures taken to ensure consistency in their ratings. Without this information, it is difficult to assess the validity of the human feedback and its impact on the model's performance.

### Questions
Some questions and suggestions for the authors to consider:
1. Expand evaluation to include more diverse and complex tasks, particularly multi-object scenarios
2. Will the authors consider performing a thorough analysis of diversity with established metrics to better understand the trade-offs in quality?
3. Is there a plan to establish structured protocols for feedback collection that involve multiple evaluators to enhance reliability and reduce biases?
6. Would the authors be able to incorporate an analysis of failure cases along with strategies for mitigation in future work?

### Soundness
2

### Presentation
4

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
This paper introduces HERO, a new framework for fine-tuning Stable Diffusion models using online human feedback efficiently. HERO integrates two novel components: Feedback-Aligned Representation Learning and Feedback-Guided Image Generation. These components are designed to maximize learning efficiency by converting human judgments into informative training signals, thereby reducing the reliance on large pre-trained models or extensive heuristic datasets. The model demonstrates significant improvements in online learning efficiency, requiring considerably fewer instances of human feedback compared to previous methods, while effectively enhancing image generation aligned with human preferences.

### Strengths
1. Efficiency in Feedback Use: HERO significantly reduces the need for human feedback instances by using them more effectively compared to previous methods, such as D3PO.
2. Direct Use of Human Judgments: By converting direct human feedback into learning signals without the need for pre-trained models, HERO simplifies the training process and potentially increases the model's responsiveness to nuanced human evaluations.
3. Improved Learning from Sparse Data: The methodology allows for effective learning even when limited data is available, which is a critical advantage in scenarios where generating or collecting extensive labeled datasets is impractical or impossible.

### Weaknesses
1. Algorithmic Complexity: The incorporation of sophisticated mechanisms like contrastive learning and feedback-based sampling may introduce complexity that complicates the model's implementation and optimization, potentially requiring specialized knowledge or resources to manage effectively. Specifically, the paper does not provide a detailed analysis of the computational overhead introduced by the feedback-aligned representation learning and feedback-guided image generation components. The description of the embedding map as a 'simple network' lacks sufficient detail to assess its actual complexity and resource requirements, especially in the context of large-scale Stable Diffusion models.
2. Sensitivity to Feedback Quality: The performance of HERO heavily depends on the relevance and accuracy of the feedback provided. Inconsistent or poor-quality feedback could mislead the learning process, leading to suboptimal or biased model behavior. The paper acknowledges this dependency but does not explore the potential impact of noisy feedback on the model's convergence or the quality of the generated images. It is unclear how the model would perform with varying degrees of feedback quality or if there are any mechanisms to detect and mitigate the effects of poor feedback.

### Questions
1. How can HERO be adapted to remain robust against noisy or contradictory feedback, which is common in real-world scenarios?
2. Could there be a hybrid approach that integrates automated feedback mechanisms with human judgments to reduce dependency on constant human input while retaining the benefits of nuanced understanding?
3. How transferable is the HERO framework across different domains or types of generative models? Can the principles applied here be adapted for use in non-visual tasks, such as text generation or music synthesis?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
In this paper, the authors introduce HERO (Human-feedback Efficient Reinforcement learning for Online diffusion), a novel method for enhancing text-to-image (T2I) models using limited human feedback. The approach leverages human evaluation to refine image quality: in the data collection phase, a human annotator labels a batch of generated images with positive and negative feedback, selecting the single best image among them. HERO employs a triplet loss function to train a visual encoder by mapping embeddings based on these annotations. A reward signal, derived from the cosine similarity between the learned representation of an input image and the selected best image, guides the model optimization and image generation process. The model utilizes Proximal Policy Optimization (PPO) to apply Low-Rank Adaptation (LoRA) to a stable diffusion model. Experimental results demonstrate that HERO outperforms baseline approaches, achieving higher success rates in generating preferred images.

[Update]: Based on the additional observations across multiple metrics, revise Soundness from 2 to 3 and final review from 5 to 6.

### Strengths
This paper is a clear and structured presentation, which makes it easy to understand the proposed methodology and its underlying concepts. 
The experiments cover a diverse set of four T2I tasks and transferability and validate the effectiveness of the proposed method.

### Weaknesses
1. A primary concern with the paper is that the T2I model's performance is only assessed through task success rates. Important factors such as image diversity and aesthetic quality are not quantitatively evaluated, which are crucial metrics and should be included, as seen in the baseline D3PO [1].

2. Additionally, the proposed method requires extra human labeling to identify the best image in each batch, which introduces additional information. This requirement makes direct comparison with other baselines less equitable, as they may not rely on such intensive human input.

Given these concerns, I would currently not recommend acceptance of this paper.

### Questions
Listed in the weakness section.

### Soundness
3

### Presentation
3

### Contribution
2
