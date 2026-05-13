# Diff-Prompt: Diffusion-driven Prompt Generator with Mask Supervision

- Decision: Accept
- Scores: 3, 6, 6, 8, 6

## Abstract
Prompt learning has demonstrated promising results in fine-tuning pre-trained multimodal models. However, the performance improvement is limited when applied to more complex and fine-grained tasks. The reason is that most existing methods directly optimize the parameters involved in the prompt generation process through loss backpropagation, which constrains the richness and specificity of the prompt representations. In this paper, we propose Diff-Prompt (Diffusion-driven Prompt Generator), aiming to use the diffusion model to generate rich, fine-grained prompt information for complex downstream tasks. Specifically, our approach consists of three stages. In the first stage, we train a Mask-VAE to compress the masks into latent space. In the second stage, we leverage an improved DiT (Diffusion Transformer) to train a prompt generator in the latent space, using the masks for supervision. In the third stage, we align the denoising process of the prompt generator with the pre-trained model in the semantic space, and use the generated prompts to fine-tune the model. We conduct experiments on a complex pixel-level downstream task, referring expression comprehension, and compare our method with various parameter-efficient fine-tuning approaches. Diff-Prompt achieves a maximum improvement of 8.87 in R@1 and 14.05 in R@5 compared to the foundation model and also outperforms other state-of-the-art methods across multiple metrics. The experimental results validate the effectiveness of our approach and highlight the potential of using generative models for prompt generation. Code is available at https://anonymous.4open.science/r/Diff-Prompt-FF2D.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
To address the limitation of prompt learning in applying to complex tasks requiring high granularity, the authors propose a three-stage training prompt generator named Diff-Prompt. This method aims to generate rich prompts and provide sufficient information for pretrained models in fine-grained downstream tasks. Through experiments on two vision-language understanding datasets and comparisons with other methods across visual aspects and various metrics, they demonstrate the superiority of their approach.

### Strengths
The paper's comparative experiments include multiple models and provide statistical results, offering guidance for other researchers interested in prompt learning.
The proposed Diff-Prompt surpasses other existing efficient fine-tuning methods on multiple evaluation metrics, which may stimulate further thinking among researchers.
The authors train the prompt generator through mask supervision, controlling the generation of fine edge information via mask variations, which is a novel idea.

### Weaknesses
Diff-Prompt is compared with two different types of efficient parameter tuning methods, but the number of baselines for the two methods is seriously imbalanced. It would be preferable to include more comparative experiments with adapter methods.
Compared with previous work, this paper seems focused on training masks through diffusion models to generate masks with fine edges for boundary control, but the contribution beyond this aspect is insufficient.
The authors claim to generate rich prompts, but the masks generated during the diffusion process do not exhibit finely controllable generation. This approach may not necessarily adapt to highly fine-grained tasks, which is evidently inconsistent with the problem the authors intend to solve.

### Questions
The authors mentioned that Diff-Prompt may suffer from poor generalization. Based on this, have they proposed any improvement plans to mitigate this issue and enable reproduction by other researchers?
How does the strategy of Diff-Prompt differ from independently training a conditional mask generator and then performing information interaction with a multimodal encoder?
During prompt generation, did the authors consider how to maintain a balance between visual and textual information to avoid information imbalance caused by modality bias?

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper introduces Diff-Prompt, a diffusion-based prompt generation method aimed at enhancing fine-tuning for complex multimodal tasks. Unlike conventional prompt tuning methods, which struggle with fine-grained tasks due to limited prompt richness, Diff-Prompt uses a multi-stage process with a Mask-VAE and an improved Diffusion Transformer to generate detailed, task-specific prompts. This approach outperforms other fine-tuning methods, achieving notable improvements in recall and accuracy on tasks requiring nuanced multimodal understanding.

### Strengths
-The motivation of this paper is very clear and interesting, making it an engaging topic worth exploring in depth.

-The illustrations in the paper are very clear, and the validation on the visual grounding task is quite comprehensive.

-There is a significant improvement in some metrics for the referring expression comprehension task.

-The code has been released, which I believe will be very helpful for further study.

### Weaknesses
1. Generalizability needs further verification: Why was testing only done on GLIP? How would it perform with other models? Why was the evaluation limited to the referring expression comprehension task? What about tasks like RES and PNG for segmentation? Would it also be effective for other more complex tasks? If it only works with this model and task, then the contribution is quite limited, and the paper's title should be adjusted to specify that it is focused on the REC task.

2. The introduction of diffusion slows inference speed by twofold, which is a significant cost. Could this be optimized?

3. In Tables 1 and 2, the improvement in the UB metric compared to MaPLe is minimal, despite MaPLe being a much simpler method. Why?

4. The effectiveness of using diffusion in this paper warrants deeper analysis. Since the core contribution of the method itself isn’t very substantial, the primary value lies in using diffusion to generate prompts. Exploring the underlying mechanism further could provide more profound insights.

### Questions
1. Generalizability needs further verification: Why was testing only done on GLIP? How would it perform with other models? Why was the evaluation limited to the referring expression comprehension task? What about tasks like RES and PNG [1] for segmentation? Would it also be effective for other more complex tasks? If it only works with this model and task, then the contribution is quite limited, and the paper's title should be adjusted to specify that it is focused on the REC task.

[1] PPMN: Pixel-Phrase Matching Network for One-Stage Panoptic Narrative Grounding.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces Diff-Prompt, a diffusion-driven prompt generator designed to enhance fine-tuning of pre-trained multimodal models. Traditional prompt learning methods often fail on complex tasks due to limited prompt richness and specificity. Diff-Prompt addresses this by using a three-stage process: (1) compressing mask information into latent space with a Mask-VAE, (2) employing an enhanced Diffusion Transformer (DiT) to generate prompts in the latent space with mask supervision, and (3) aligning these generated prompts with a pre-trained model's semantic space for fine-tuning. Experimental results show that Diff-Prompt significantly outperforms other methods on pixel-level tasks, achieving notable improvements in recall metrics (R@1 and R@5).

### Strengths
1. The use of a Mask-VAE and diffusion-driven prompt generator enables the creation of rich prompts, which improves the model's ability to effectively capture information in the latent space.
2. The alignment of generated prompts with the pre-trained model in the semantic space ensures better guidance for the pre-trained model, enhancing performance during fine-tuning.
3. The experimental results on a complex fine-grained multimodal downstream task validate the effectiveness of the proposed method, showcasing its applicability to challenging scenarios.

### Weaknesses
Compared to other methods, Diff-Prompt has slightly more learnable parameters (5.5M). More parameters may require more memory and lead to longer inference time.

### Questions
1. The vision and language adaptors adopt the same architecture. How to reasonably exploit the advantages of vision and language cues to ensure consistent fine-tuning of the pre-trained model?
2. What potential strategies could be employed to address the high computational complexity and image input size limitations of the Diff-Prompt model?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces Diff-Prompt, a novel prompt learning approach that leverages diffusion models to generate rich prompts for multimodal tasks. Diff-Prompt employs a three-stage process: first training a Mask-VAE to compress masks into latent space, then using an improved Diffusion Transformer to generate prompts in this latent space with mask supervision, and finally aligning the denoising process with the pre-trained model in semantic space. The method addresses limitations of existing prompt learning approaches by generating more informative and task-specific prompts.

### Strengths
I find the approach to be innovative and a departure from other methods in prompt learning for improved generalization. The paper is well presented, and easy to follow. The method achieves strong performance on two vision-language understanding datasets, RefCOCO and Flickr30k compared to existing methods.

### Weaknesses
I have two major concerns regarding this work.

1. The authors do not report on other generalization benchmarks such as the ones reported by prompt learning techniques like CoOP and Maple, which the authors compare with. These are representative tasks in generalization to novel classes, new target datasets and unseen domain shifts. Why were these benchmarks not considered, since methods reporting on these benchmarks are considered in the evaluation?

2. The authors are missing comparisons with multiple recent works related to prompt learning for generalization such as [1,2,3,4,5,6]. Why were these methods not considered during evaluation and comparison?

[1] Z. Li et al., "PromptKD: Unsupervised Prompt Distillation for Vision-Language Models", in CVPR, 2024.

[2] M. U. Khattak et al., "Self-regulating Prompts: Foundational Model Adaptation without Forgetting," ICCV, 2023.

[3] J. Hasan et al., "Align Your Prompts: Test-Time Prompting with Distribution Alignment for Zero-Shot Generalization," NeurIPS, 2023.

[4] S. Roy and A. Etemad, ‘Consistency-guided Prompt Learning for Vision-Language Models’, in ICLR, 2024.

[5] Y. Zhang, C. Zhang, K. Yu, Y. Tang, and Z. He, ‘Concept-Guided Prompt Learning for Generalization in Vision-Language Models’, in AAAI, 2024.

[6] Y. Zhang, K. Yu, S. Wu, and Z. He, ‘Conceptual Codebook Learning for Vision-Language Models’, in ECCV, 2024.

### Questions
Please refer to the weaknesses. In general I am concerned with evaluation settings which are different compared to other major works in prompt learning, as well as missing comparisons to recent works.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces the Diffusion-driven Prompt Generator (Diff-Prompt), which leverages the diffusion model to generate detailed and comprehensive prompt information for intricate downstream tasks.

### Strengths
This paper is well organized
The performances are competitive

### Weaknesses
(1)	The definition in DEEP PROMPTING is confused. What is the definition of E_{i}
(2)	What mechanism do you use to the D latent features of generated prompt? It is not clear
(3)	In subsection 3.1, this study is linked to referring expression comprehension. Nonetheless, there is a lack of information on how the proposed method generates a position to accurately locate the target object described in the expression. 
(4)	The advantage of using the generated prompt is not clear. Why can we replace the generated prompts with learnable prompts

### Questions
see above-mentioned issues

### Soundness
3

### Presentation
2

### Contribution
2
