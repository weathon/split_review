# Unified Multimodal Discrete Diffusion

- Decision: Reject
- Scores: 6, 6, 5, 6

## Abstract
Multimodal generative models that can understand and generate across multiple modalities are dominated by autoregressive (AR) approaches, which process tokens sequentially from left to right, or top to bottom. These models jointly handle images, text, video, and audio for various tasks such as image captioning, question answering, and image generation. While AR models have been highly successful in the text domain, they have been found suboptimal for processing images, videos, and audio due to the high correlation between adjacent tokens which waste inference-time compute by separately predicting each one. In this work, we explore discrete diffusion models as a unified generative formulation in the joint text and image domain, building upon their recent success in the text domain alone. Discrete diffusion models offer several advantages over AR models, including improved control over quality versus diversity of generated samples, the ability to perform joint multimodal inpainting (across both text and image domains), greater controllability in generation through guidance. Leveraging these benefits, we present the first Unified Multimodal Discrete Diffusion (UniDisc) model, which is capable of jointly processing text and images for a variety of downstream tasks. We compare UniDisc to multimodal AR models of similar capacity, demonstrating that UniDisc outperforms them in terms of both performance and inference-time compute, and enhanced controllability, editability, inpainting and flexible trade-off of inference time versus generation quality.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
Motivated by the superiority of diffusion models, this work aims to unify text and image generation within a discrete diffusion formulation. The main challenge to unification is the sampling steps for different modalities, e.g., text needs more sampling steps than image. To address this issue, the authors propose to use different time schedules for each modality, and balance the noise schedule accordingly during training. Comprehensive experiments are included to demonstrate how discrete diffusion works for different modalities.

### Strengths
- Unifying text and image generation with discrete diffusion sounds given that diffusion process is easier to control, and image diffusion achieved great success recently.
- The writing is clear and easy to follow.
- The motivation to address issue of different time schedules for different modalities is also practical.
Experiments are comprehensive. For example, the authors illustrate the inference efficiency, discriminative ability, fine-tuning from AR models.

### Weaknesses
 - The main concern is the performance compared to the baselines. The method is good at conditional generation while performing worse on the unconditional generation, with mixed results observed. 
- The balance between different modalities seems empirical and handcrafted.

### Questions
How do you implement CFG in Chameleon? The model size of Chameleon in experimental comparision. Is it reproduced with the same training set?

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
4

### Summary
The paper proposes a discrete diffusion model that unifies the generative modeling of image and text. To improve the inference efficiency, the paper proposes to denoise image and text with different timesteps. A specific training strategy is proposed correspondingly, which makes image timesteps randomly offsets the text timesteps by a $\delta t$. Experiments are conducted to analyze the unconditional and conditional image-text generation ability, together with image/text retrieval ability, and image-text joint inpainting ability.

### Strengths
1. The approach of this paper is novel. Considering that the decoder-only auto-regressive transformers have become the main stream of language modeling, this paper explores diffusion for both image and text, representing a completely different direction.
2. The experiments are conducted comprehensively. In specific settings (relatively small model size and data scale), the proposed method performs better than the AR baseline in unconditional and conditional image-text generation tasks.

### Weaknesses
+ About the motivation. 
  + The paper says that "generating image tokens autoregressively is slow and wasteful as nearby tokens are highly correlated, and this process results in many unnecessary forward passes through the network". However, from Fig. 4(a) of the paper, AR strikes even better speed-quality trade-off. Moreover, from the conceptual perspective, AR can be more efficient than diffusion models, since AR models benefit from the kv cache during inference, making each forward pass only need to perform the calculation of a single token， while diffusion models have to compute all the tokens in each forward pass. It is also worth noting that the reported speed-quality trade-off in Fig 4(a) is based on a batch size of 8, which favors AR models due to the benefits of batching with KV caching. At a batch size of 1, the relative performance of AR models may degrade due to underutilization of GPU resources.
  + In practice, models usually go through supervised fine-tuning on downstream tasks before actually being put into use. In this way, lots of benefits can be unleashed in the AR paradigm, including generating arbitrary-length sequence, multi-task, multimodal reasoning, and image/text inpainting or editing. However, for diffusion models, due to the token length limitation, tasks involving dynamic sequence length are difficult to implement. Moreover, it is very inflexible when it comes to tuning the pretrained diffusion model into a VQA model for multiple-round conversations.
+ About experiments
  + The paper claims that Perplexity + Entropy is a better indication of the quality of generation results. However, there is no guideline to determine the relative importance of these two metrics when there is trade-off. As a result, it is still unclear whether the proposed method is better than the AR paradigm. The paper does not provide a clear justification for why a simple sum of perplexity and entropy is a good metric, especially when these two metrics can have different scales and units. A more principled approach would involve normalizing or weighting these metrics based on their relative importance for the task at hand.
  + From Fig.3, it seems that the proposed method is not more efficient than the AR paradigms.

### Questions
1. About image-text retrieval. The paper says that $p(x_{text}|x_{img})$ determines which text is retrieved. For AR model, this is easy to calculate, since the text order is predefined, and the probability can be easily calculated as the cumulative product of the probabilities of all text tokens. However, for the diffusion model, the method for calculating this probability seems unclear. Could the authors clarify this probability calculation process?
2. About details. What is the meaning of the notation $K$ in section 3.3 paragraph 4 "$\mathcal{U}(\frac{N_{min}}{K}, \frac{N_{min}}{K})$"?

### Soundness
3

### Presentation
3

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
The paper introduces UniDisc, a unified multimodal discrete diffusion model that operates on both text and image modalities. Unlike traditional autoregressive (AR) models, UniDisc leverages discrete diffusion, which masks tokens and then learns to reconstruct them. This approach offers several advantages, including enhanced controllability, joint image-text inpainting, and efficiency in inference.

### Strengths
1. This paper introduces a unified multimodal discrete diffusion approach designed to address the limitations of both continuous diffusion and autoregressive (AR) models. Unlike continuous diffusion models, which struggle with discrete data like text, UniDisc leverages discrete noise through token masking, enabling it to seamlessly handle both images and text in a single model. By unifying the generation process for different modalities, UniDisc allows for efficient, high-quality multimodal outputs with better control over trade-offs between quality and diversity.

2. The authors conduct extensive experiments across various tasks, datasets, and evaluation metrics to assess UniDisc's capabilities. These experiments include unconditional and conditional generation tasks, which highlight UniDisc's ability to generate both text and images independently and conditioned on each other. Through these experiments, UniDisc demonstrates superior performance over AR baselines, especially when using classifier-free guidance (CFG) in conditional generation tasks, which significantly boosts its quality over AR models.

### Weaknesses
1. It is recommended to add a visual diagram showing the step-by-step workflow of your proposed method. A clear pipeline figure would make your methodology much easier to follow.

2. While the authors include some visualization results in the appendix, the paper would benefit from more comprehensive examples of the model's outputs. Since this is a generation-focused paper, it is suggested to include a diverse set of generated images and texts directly in the main manuscript. Showing results across different scenarios would help readers better evaluate the method's capabilities and performance.

### Questions
Please refer to the weaknesses section.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents Unified Multimodal Discrete Diffusion (UniDisc), a model that leverages discrete diffusion for joint text-image generation tasks. UniDisc uses discrete diffusion by masking tokens and iteratively denoising them， which allows for enhanced controllability, quality-diversity trade-offs, and efficient inpainting across modalities. UniDisc is designed to overcome AR limitations, such as inefficiency in image generation and lack of flexibility in conditional generation. The model introduces a modality-specific caching mechanism to address varying token sampling needs for images and text, resulting in improved inference efficiency. Evaluation across multiple datasets shows that UniDisc outperforms AR baselines in generation quality, inference efficiency, and retrieval tasks, demonstrating its potential for scalable multimodal applications.

### Strengths
* Overall I find that the writing is clear and well-structured, making it easy for readers to follow the arguments and understand the key points.
* The exploration of discrete diffusion for multimodal tasks is valuable. The proposed framework demonstrates the potential of various multimodal tasks, such as text-image jointing inpainting and retrieval.
* The paper shows sufficient ablation studies to verify the effectiveness of each design choice of UniDisc.

### Weaknesses
 * This paper mainly applies discrete diffusion to multimodal tasks and integrates some existing techniques from previous papers, such as classifier-free guidance and sampling schedules from MaskGiT, D3PM, etc. Therefore, the technical contribution of this paper is limited.
* However, if this paper is considered an empirical paper, it lacks a comprehensive comparison with other advanced methods on important benchmarks, such as the original Chameleon, EMU, Next-GPT, and CoDI. Additionally, it is well known that the greatest advantage of AR models lies in scaling laws, while many studies have found that scaling for Non-AR models (Discrete Diffusion) is a bottleneck. Therefore, training only a 100M model and comparing it with a single AR baseline is not very convincing. More fair comparison experiments should be conducted across different model sizes and data scales.
* While the authors highlight several "firsts" as contributions of this paper, the majority of the components are based on existing techniques. For example, the proposed multimodal caching strategy for discrete diffusion models essentially applies two different schedules to two distinct modalities. And I notice that the UniD3 [1] looks very similar to this paper. Could you elaborate the differences with this paper?
* A major concern remains that the generative performance of the model falls significantly short of the state-of-the-art across various tasks. The quality of the generated images exhibits very noticeable "MaskGiT-style" artifacts. The paper does not compare against any unified multimodal generative models or specialist models for image or text generation, providing only an autoregressive model as a baseline. Additionally, the model size of 300M parameters is smaller than many models trained on ImageNet, let alone text-to-image or multimodal generative models. From my own recent experience training MaskGiT/Discrete Diffusion models ranging from 100M to 3B parameters, I’ve observed that scaling effects tend to saturate beyond 1B parameters. Therefore, I would have liked to see a more in-depth exploration of scaling for discrete diffusion models.

### Questions
* In Table 2, the FID significantly drops after applying CFG to the AR baseline, while UniDisc gains a significant performance boost. This is an unusual result that CFG greatly hurts the FID of AR models. Could you please explain this observation and provide more details on the implementation of the AR model?
* In Figure 4, the paper compares the inference efficiency between UniDisc and AR baseline. Does the AR baseline integrate techniques like Flash-Attention, which can greatly boost the inference speed?

### Soundness
3

### Presentation
4

### Contribution
3
