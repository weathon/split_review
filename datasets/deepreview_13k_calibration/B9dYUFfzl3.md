# VADER: Video Diffusion Alignment via Reward Gradients

- Decision: Reject
- Avg Score: 6.00
- Scores: 3, 6, 8, 6, 5, 8

## Abstract
We have made significant progress towards building foundational video diffusion models. 
    As these models are trained using large-scale unsupervised data, it has become crucial to adapt these models to specific downstream tasks. Adapting these models via supervised fine-tuning requires collecting target datasets of videos, which is challenging and tedious. In this work, we utilize pre-trained reward models that are learned via preferences on top of powerful vision discriminative models to adapt video diffusion models.  
    These models contain dense gradient information with respect to generated RGB pixels, which is critical to efficient learning in complex search spaces, such as videos. We show that backpropagating gradients from these reward models to a video diffusion model can allow for compute and sample efficient alignment. We show results across a variety of reward models and video diffusion models, demonstrating that our approach can learn much more efficiently in terms of reward queries and computation than prior gradient-free approaches. Our code, model weights, and more visualization are available at \url{https://vader-vid.io}.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes to utilize pre-trained reward models that are learned via preferences on top of powerful vision discriminative models to adapt video diffusion models. The results across a variety of reward models and video diffusion models showcase the effectiveness of the proposed approach.

### Strengths
The authors propose the use of reward models aimed at enhancing the quality of generated videos. The experimental results demonstrate promising improvements in video quality, showcasing the effectiveness of the proposed approach.

### Weaknesses
1. Algorithm 1 represents a standard approach that utilizes reward feedback within a diffusion model framework, lacking significant innovation.
2. A critical challenge in applying reward feedback to diffusion models is the precise definition and training of the reward model. The manuscript employs certain image-based methods to establish the reward function for video generation; however, these methods may not adequately encapsulate the unique characteristics of video data. It would be beneficial if the authors developed and trained a reward model specifically tailored for video content, similar to advancements made in the field of image rewards [1], thereby contributing more meaningfully to the domain.
3. There appears to be an error in Equation (231). Could you please provide a detailed derivation to clarify this point?
4. The ordering of equations has been overlooked starting from Equation (3). Please ensure all equations are correctly sequenced for clarity and coherence.

### Questions
See weakness

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper addresses the problem of aligning pretrained video generation diffusion models to downstream tasks/domains using available reward functions without using fine-tuning datasets. Specifically, the authors propose updating the parameters of the diffusion model using the gradients of the target reward functions. This is motivated by the analysis provided in the paper (figure 3), showing that the feedback from reward gradients scale much more with video resolution compared to methods based on policy gradients. The authors apply their method to different reward functions, such as image aesthetics evaluation, image-text alignment, and video temporal consistency evaluation functions. The authors also incorporate some techniques to maintain efficiency when fine-tuning the retrained model. The proposed method is compared with multiple pretrained video generation models, as well as their aligned version using policy-gradient-based methods.

### Strengths
- The paper is very well-written and well-structured, making it easy to follow and understand.

- The provided analysis in Fig. 3, which shows the gap between the feedback from reward gradients and policy gradients for higher resolution videos, is valuable.

- The method is evaluated on multiple base video generators, showing consistent results.

- The proposed method shows better results in comparison to the policy-gradient-based baselines in terms of the evaluated metrics. This is also noticeable in the visual results.

- The proposed method has better generalizability on unseen text prompts compared to the baseline alignment methods.

### Weaknesses
 - **Novelty**: To my understanding, the proposed method is in essence a standard fine-tuning method with the objective of maximizing task-specific discriminative/reward functions. The proposed techniques for efficiency, including LoRA, truncated back propagation, and frame subsampling are also all standard and commonly used in different areas. The amount of technical novelty is not a major concern as long as the method has significant findings. However, the behavior shown in the paper, i.e. better alignment of the diffusion model when directly optimized to maximize the target reward function, is not very surprising to me.

- **Experiments**: 
    - In addition to regression in generalizability, another potential down-side of fine-tuning methods is the reduced diversity of the aligned model. Therefore, it is important to properly evaluate the diversity of the generated videos using the aligned model. For example, it would be interesting to see how diverse the videos are the same text prompt compared to the base model. 
    - Additionally, I noticed no video visualizations are provided for aligned models using video reward functions. For example, in the results provided in Fig. 9 does not show much temporal motion in the generated videos. This could also relate to the previous point, where the model could sacrifice temporal variations for more consistent frames.

### Questions
Please see the concerns in the Weaknesses section. I am open to increasing my score, if the authors could clarify their novelty and contribution more, and address my concerns about the experiments.

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors introduce an alignment tuning method for video generation models utilizing gradient backpropagation from reward models. This approach addresses a critical need for producing high-quality, aligned video content. By directly guiding the generation model through reward gradients, the method achieves notable sample and computational efficiency compared to gradient-free approaches.

### Strengths
- The problem to be solved is clearly defined, and its importance is well-acknowledged.

- The use of reward model gradients is highly intuitive and well-explained. Additionally, as the proposed methodology is data-free, it is practically useful and less likely to inherit biases from datasets used in alignment fine-tuning.

- Experimental results show this method is computationally efficient compared to gradient-free approaches such as DDPO and DPO.

### Weaknesses
 **Clarity of Contribution:** It is unclear what the authors’ unique contributions are. Utilizing reward model gradients for alignment tuning has already been demonstrated in text-to-image generation by Prabhudesai et al. and Clark et al. The authors should clarify what specific advancements they are claiming in this area.  

Additionally, the authors mention that there are significant memory overhead issues in video models when implementing these methods, yet a clear, step-by-step ablation study is needed to show how each component of VADER addresses this problem. Specifically, the interaction between LoRA, mixed precision, frame subsampling, truncated backpropagation, and gradient checkpointing needs to be dissected to understand their individual and combined contributions to memory reduction. It is not sufficient to simply state that these methods reduce memory; a detailed analysis of their impact on both VRAM and system RAM is required.

Prabhudesai et al., "Aligning text-to-image diffusion models with reward backpropagation." arXiv. 2023.  
Clark et al. "Directly fine-tuning diffusion models on differentiable rewards." ICLR. 2024.

**Objective of the Alignment Tuning:** The results shown in the DDPO and DPO papers use significantly larger reward query samples. In this paper, however, smaller-scale experiments were conducted to highlight the sample and computational efficiency of reward gradients. This discrepancy may have resulted in DDPO and DPO showing unusually poor results. Since the current alignment settings are data-free, with comparable test times, sample and computational efficiency are not as critical. Therefore, it would be beneficial to include comparisons with DPO and DDPO results over longer training times. The authors should also clarify the specific number of gradient updates and the effective batch size used in their experiments, as these parameters significantly impact the performance of reinforcement learning algorithms.


### Questions
**Comparison with Existing Guidance Methods:** Reward gradients are commonly used in guidance-based research within diffusion models, as seen in studies like DOODL and Universal Guidance. It would be beneficial to analyze and compare the proposed method with these approaches. If direct implementation of these methods is challenging, an alternative comparison could involve modifying the reward guidance objective to apply guidance through $\nabla_{x_t} R$ during generation, similar to the approach taken in this paper.

**Clarification in Experiments (Table 1):** It is unclear which video generation model serves as the baseline in Table 1. The experimental setup mentions the use of VideoCrafter, Open-Sora 1.2, and ModelScope. Is the baseline an average of these models, or is it based on one specific model? Further clarification on this would be helpful.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposed a reward fine-tune method called VADER. By using dense gradient information tied to generated RGB pixels, VADER enables more efficient learning in complex spaces like video generation. Backpropagating gradients from reward models to the video diffusion model facilitates both compute and sample-efficient alignment. Results across various reward and video diffusion models demonstrate that this gradient-based approach learns more efficiently than previous gradient-free methods in terms of reward queries and computational resources.

### Strengths
1. The paper proposes to use gradient information for critic model preference tuning.
2. The experiment results are good.

### Weaknesses
1. Lack of novelty, the paper is more likely to be a tech report rather than a paper. Directly backward the gradient is not novel for RL.
2. The paper proposes a on-policy strategy, while all the comparisons are off-policy strategies which is not fair. There are so many on-policy strategies that perform better than off-policy strategies.
3. Missing experiment details. How do you use DPO/DDPO on your dataset since they need preference pairs for training. How do you create the preference pair?
4. The paper claims to be the first to successfully align video diffusion models using reinforcement learning, which is not true. T2V-Turbo was released earlier and also uses multiple reward models for feedback.
5. The paper uses multiple reward models to simultaneously perform gradient backpropagation, but when comparing with DPO, they use a replay buffer to store preference pairs scored by the reward models. It is unclear how the authors handle the generation of offline preference data under the influence of multiple reward models, as different reward models might produce conflicting preferences.

### Questions
1. More methods should be considered for comparison.
2. More details of the experiments should be enclosed.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces VADER, a method for fine-tuning video diffusion models using reward gradients to improve task-specific alignment. By utilizing pre-trained reward models as discriminators, VADER enhances video quality, text alignment, and temporal consistency. The approach employs memory optimization techniques to enable efficient training, even with limited resources. Experimental results demonstrate that VADER achieves strong performance across various video generation tasks.

### Strengths
1. The authors propose VADER, which uses reward gradients to fine-tune video diffusion models, achieving efficient task adaptation. 
2. This paper experiments with various reward models, making it suitable for multiple video generation tasks and achieving strong results in both subjective evaluations and quantitative metrics.
3. This paper employs several optimization techniques (such as truncated backprop) to enable operation in resource-limited environments.

### Weaknesses
1. The proposed VADER approach, which fine-tunes video diffusion models using reward gradients, optimizes network parameters with various reward models serving as discriminators. This enables improved adaptation to specific tasks. However, the use of reward models in generative model training is a well-explored concept. This paper just extends that approach within the context of diffusion models.
2. Since using reward models to backpropagate gradients requires the diffusion model to produce fully denoised outputs, all denoising steps must be executed, which places high demands on training resources. This might also lead to very small batch sizes. Although the authors employ several tricks to reduce resource usage, it raises the question of whether these adjustments impact the training outcomes. For instance, how much does backpropagation through only one timestep in the diffusion model affect the network parameters?
3. Some visual results in the paper still show misalignment between text and image content. For example, in Figure 7, the prompt "A bear playing chess" leads VADER to generate two bears.

### Questions
See Weakness

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 6

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This work introduces VADER, a method for aligning video diffusion models using reward gradients. VADER repurposes off-the-shelf vision discriminative models as reward models to adapt video diffusion models more effectively. Additionally, the paper presents practical techniques to optimize memory usage, enabling efficient training of VADER on standard hardware.

### Strengths
Originality:
VADER is a novel approach to aligning video diffusion models using reward gradients rather than policy gradient methods. It creatively repurposes various pre-trained vision models as reward models, expanding their utility in video generation.

Quality:
The paper is methodologically rigorous, with strong experimental results demonstrating clear performance gains. Additionally, memory-optimizing techniques make VADER more accessible, broadening its potential user base.

Clarity:
The work is well-organized, with clear explanations and visualizations that effectively showcase the benefits of reward gradients and diverse reward models for alignment.

Significance:
VADER significantly advances practical video generation, making it more accessible and adaptable. This positions VADER as a valuable contribution to generative AI in video synthesis.

### Weaknesses
The paper lacks a quantitative evaluation of the temporal coherence achieved with the v-jepa reward model. While Figure 9 provides qualitative evidence of improvement, the analysis would be more robust with a quantitative assessment of temporal consistency. Adding such an experiment would offer a more comprehensive understanding of VADER's performance in maintaining coherence over time when trained on the v-jepa reward.

While VADER incorporates multiple reward models, the paper lacks a detailed examination of how each specific reward model influences alignment objectives like temporal coherence, aesthetic quality, or text-video alignment. Additionally, it would be valuable to understand how optimizing for one reward, such as aesthetics, might impact the performance on other metrics, like temporal coherence.

### Questions
How are the visualizations selected?
Are the visual examples in the paper randomly chosen, or were they curated to highlight specific successes of VADER? Understanding the selection process would clarify whether the results are representative or potentially cherry-picked.

Why aren’t popular metrics, such as FID/FVD, used in the experiments?
Frechet Video Distance (FVD) is a commonly used metric for evaluating video quality in generative models, albeit with its own limitations and pitfalls. Including it would allow for a more standardized and comparable evaluation.

### Soundness
4

### Presentation
4

### Contribution
4
