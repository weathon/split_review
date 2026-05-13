# Dissecting Bit-Level Scaling Laws in Quantizing Vision Generative Models

- Decision: Reject
- Scores: 3, 6, 5, 5

## Abstract
Vision generative models have recently made significant advancements along two primary paradigms: diffusion-style and language-style, both of which have demonstrated excellent scaling laws. Quantization is crucial for efficiently deploying these models, as it reduces memory and computation costs. In this work, we systematically investigate the impact of quantization on these two paradigms. Surprisingly, despite achieving comparable performance in full precision, language-style models consistently outperform diffusion-style models across various quantization settings. This observation suggests that language-style models have superior bit-level scaling laws, offering a better tradeoff between model quality and total bits. To dissect this phenomenon, we conduct extensive experiments and find that the primary reason is the discrete representation space of language-style models, which is more tolerant of information loss during quantization. Furthermore, our analysis indicates that improving the bit-level scaling law of quantized vision generative models is challenging, with model distillation identified as a highly effective approach. Specifically, we propose TopKLD to optimize the transfer of distilled knowledge by balancing "implicit knowledge" and "explicit knowledge" during the distillation process. This approach elevates the bit-level scaling laws by one level across both integer and floating-point quantization settings.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
- This paper presents a systemic analysis of the impact of quantization on vision generative models, particularly comparing diffusion-style and language-style models. Under the bit-level scaling law that has been studied in language modeling, the authors show that the language-style model consistently outperforms the diffusion-style model. 

 - The authors also provide explanations and investigations into the reason for their distinctive behaviors in low-bits. 

 - To further enhance the bit-level scaling of language-style models, the TopKLD-based distillation method is proposed by balancing implicit knowledge and explicit knowledge.

### Strengths
- The paper provides a comprehensive study of how quantization affects two major paradigms of vision generative models, which is crucial for deploying these models efficiently. The finding that language-style models have superior bit-level scaling laws compared to diffusion-style models, might also shed light on further model optimization and deployment.

 -  The proposed TopKLD method for knowledge distillation during the quantization process is innovative and shows experimental promise in improving bit-level scaling laws.

### Weaknesses
 - The major weakness of this work is the limited scoop. As both VAR and DiT are specific cases in diffusion and language-style vision generative models, their behavior may not apply to other types of vision generative models. Compared to the original paper about k-bit inference scaling laws, the model scope is relatively small, which makes the conclusion unclear to generalize to different model types.

 - The authors provide some analysis about the reason behind models' scaling behaviors and discuss the relevance of the discrete representation. However, vision AR and diffusion models are not distinctive from the representation side. (see question) fds

### Questions
- The authors should consider adding different model types into the investigations, that cover more typical language-style and diffusion-style vision generative models.

 - Language-style vision generative models follow the autoregressive modeling in language modeling, while not necessarily being discrete. Similarly, diffusion-style models do not always adopt a continuous representation. How would the analysis apply to discrete diffusion and 
continuous AR?

 - Meanwhile, the error analysis from the discrete and continuous domains does not seem to conclude for language-style and diffusion-style models (related to Q2)

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper investigates bit-level scaling laws in quantized vision generative models, specifically comparing diffusion-style and language-style models. The authors find that while both models perform similarly in full precision, language-style models consistently exhibit superior bit-level scaling across various quantization settings. This robustness is attributed to the discrete representation space of language-style models, which enhances resilience to quantization noise. The authors propose TopKLD, a novel knowledge distillation method that balances implicit and explicit knowledge transfer, thereby further optimizing bit-level scaling in quantized models. Their findings provide valuable insights into efficient quantization strategies and underscore the potential of language-style models for low-bit precision applications.

### Strengths
1. The paper investigates bit-level scaling laws in quantized vision generative models, specifically comparing diffusion-style and language-style models. The authors find that while both models perform similarly in full precision, language-style models consistently exhibit superior bit-level scaling across various quantization settings. This robustness is attributed to the discrete representation space of language-style models, which enhances resilience to quantization noise. 
2. The authors propose TopKLD, a novel knowledge distillation method that balances implicit and explicit knowledge transfer, thereby further optimizing bit-level scaling in quantized models. Their findings provide valuable insights into efficient quantization strategies and underscore the potential of language-style models for low-bit precision applications.

### Weaknesses
1. Inconsistent Scaling Comparison in Figure 1: The paper aims to show that language-style models have superior bit-level scaling compared to diffusion-style models. However, the models compared in Figure 1 have different initial total model bits and compute bits, which may itself cause scaling variations. This discrepancy introduces an additional variable that weakens the effectiveness of Figure 1 in supporting the authors’ claim. Aligning initial bit settings could help provide a clearer, more controlled comparison.
2. Limited Advantage of TopKLD in High-Bit Settings: While the authors introduce TopKLD to enhance bit-level scaling, Figure 7(c) and Figure 5(a) suggest that in the W8A8 setting, TopKLD performs similarly to existing methods like SmoothQuant, without a clear improvement. Given that TopKLD introduces extra training overhead, its benefit seems marginal in these high-bit settings. Providing a comparison across a broader range of bit settings could clarify the scenarios where TopKLD is genuinely advantageous.
3. Insufficient Experimental Validation of TopKLD’s Effectiveness: The effectiveness of TopKLD is only partially validated, as shown by its comparison with ForwardKLD and ReverseKLD at 3-bit in Figure 7(b). However, a more comprehensive evaluation against other mainstream quantization methods under varied conditions would provide a stronger basis for its practical effectiveness.
4. Lack of Analysis on the Computational Overhead of TopKLD: TopKLD introduces an additional training overhead, but the paper does not quantify the computational cost compared to existing methods. A detailed analysis of training time, computational resources, and memory requirements would provide a more complete view of its trade-offs, particularly for resource-constrained applications.

### Questions
1. Could you provide a more controlled comparison in Figure 1 with equivalent initial model and compute bits for both language-style and diffusion-style models?——The initial bit settings differ between the models, which complicates the interpretation of bit-level scaling behaviors. A more controlled experiment with similar initial bit allocations would strengthen the comparison and isolate the scaling differences more effectively.
2. What specific advantages does TopKLD offer over existing methods in low-bit settings, and could you clarify its computational cost?——While TopKLD is introduced to enhance bit-level scaling, its benefit seems marginal in higher-bit configurations, as shown in Figure 7(c). Could you provide additional data on TopKLD’s performance in low-bit settings and quantify the extra training cost, as well as its memory and computational overhead, compared to other methods like SmoothQuant?
3. Can you expand the experimental validation of TopKLD with comparisons to other mainstream quantization methods across more bit configurations?——The effectiveness of TopKLD is primarily shown in comparison with ForwardKLD and ReverseKLD in the 3-bit setting. Including a broader range of comparisons with other quantization approaches (e.g., OmniQuant, GPTQ) across different bit levels would give a clearer picture of where TopKLD has a distinct advantage.
4. Could you provide additional insights into the potential applications of your findings on bit-level scaling laws?——The study primarily focuses on theoretical scaling improvements, but practical insights or applications for specific deployment scenarios (e.g., mobile devices, edge computing) would make the results more actionable. Could you elaborate on specific scenarios where the bit-level improvements from language-style models might offer a tangible benefit?

### Soundness
2

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
This paper investigates the impact of quantization on the performance of image generation models. By comprehensive experiments in many aspects, such as “model bits (MT), compute bits (CT)”, “post-training quantization (PTQ), quantization-aware training (QAT)”, “diffusion model (DiT), auto-regressive model (VAR)”, the authors observe that image generation models have  bit-level scaling laws. And they further discover that VAR is more robust to quantization than DiT due to its discrete representation space. Finally, they propose a knowledge distillation based quantization method, called TopKLD, to improve the bit-level scaling laws of VAR.

### Strengths
This paper demonstrates the bit-level scaling laws of image generative models through comprehensive experiments in terms of model bits and compute bits. By analysis of the reconstruction error of middle representations in VAR and DiT, the paper draws the conclusion that VAR is more robust to quantization and could generalize to other discrete auto-regressive models. And further, the paper proposes TopKLD, a quantization-aware training process, to improve scaling behavior of VAR at low bits region.

### Weaknesses
Bit-level scaling laws and the robustness of discrete auto-regressive models seem to be intuitive and straightforward, therefore the main contribution of this paper is the proposed quantization method, TopKLD. As a knowledge distillation based quantization-aware training method, the comparison and ablation studies are not enough. Specifically, the paper lacks a thorough exploration of different knowledge distillation loss functions beyond forward and reverse KL divergence. Furthermore, the impact of the 'top-K sampling' parameter on the scaling behavior is not sufficiently investigated, leaving a gap in understanding its influence on the proposed method. The paper also contains a minor error in referencing Figure 5, which should be Figure 7(a).

### Questions
1. TopKLD should be compared to more distillation loss functions besides of forward and reverse KL Divergence, such as Logits MSE, JS Divergence and so on. 
2. How does the parameter of “top-K sampling” affect the scaling behavior should be studied.
3. The “Figure 5” in line 427 should be “Figure 7(a)”

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
3

### Summary
This paper explores scaling laws for model quantification. Besides, TopKLD is introduced to lift the decoder-only model's bit-level scaling performance.

### Strengths
1. This paper conducted many experiments based on VAR and DIT to explore the scaling law at the bit level.
2. The language-based model enjoys a better bit-level scaling law. The conclusion is interesting.
3. TopKLD seems effective in various quantitative aspects of VAR.

### Weaknesses
1. The paper is more like an experimental report than a research paper. I think the comparison between VAR and DIT is too lengthy and the TopKLD is short.
2. The model size of VAR is small. Is the necessity of quantifying small models sufficient?
3. Can you provide a direct visualization result that clearly shows the bit-level scaling law?

### Questions
See weakness.

### Soundness
3

### Presentation
3

### Contribution
3
