# Reconstructive Visual Instruction Tuning

- Decision: Accept
- Scores: 6, 6, 6, 6, 5

## Abstract
This paper introduces \underline{\textbf{r}}ec\underline{\textbf{o}}nstructive vi\underline{\textbf{s}}ual in\underline{\textbf{s}}truction tuning (\method), a family of Large Multimodal Models (LMMs) that exploit \textit{vision-centric supervision signals}.
In contrast to conventional visual instruction tuning approaches that exclusively supervise text outputs, \method prompts LMMs to supervise \textit{visual outputs} via reconstructing input images.
By doing so, it capitalizes on the inherent richness and detail present within input images themselves, which are often lost in pure text supervision.
However, producing meaningful feedback from natural images is challenging due to the heavy spatial redundancy of visual signals.
To address this issue, \method employs a denoising objective to reconstruct latent representations of input images, avoiding directly regressing exact raw RGB values.
This \textit{intrinsic activation} design inherently encourages LMMs to maintain image detail, thereby enhancing their fine-grained comprehension capabilities and reducing hallucinations.
Empirically, \method \textit{consistently} brings significant improvements across different visual encoders and language models.
In comparison with \textit{extrinsic assistance} state-of-the-art alternatives that aggregate multiple visual experts, \method delivers competitive performance with a single SigLIP visual encoder, demonstrating the efficacy of our vision-centric \textit{supervision} tailored for \textit{visual outputs}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes a new LMM training approach with an additional branch for input image reconstruction. The results show the model enhances fine-grained comprehension and reduces hallucinations. ROSS employs a denoising objective to address spatial redundancy that reconstructs latent visual tokens rather than raw RGB values. Empirical evaluations demonstrate that ROSS consistently outperforms conventional LMMs using single or multiple visual encoders on visual understanding benchmarks.

### Strengths
**Novel Image-Based Supervision**: ROSS leverages image reconstruction as a supervisory signal, enabling the model to capture fine-grained visual features and semantics that significantly reduce hallucination artifacts compared to text-supervised approaches. The idea conceptually makes sense and is proven in the experiments.

**Comprehensive Analysis of Model Variants**: The paper provides a thorough study of various architectural choices and configurations within the ROSS framework, offering insight into optimal setups.

**Empirical Validation**: Extensive ablation studies and benchmark evaluations demonstrate ROSS's superior performance metrics, particularly in tasks requiring high-fidelity visual understanding, with statistically significant improvements over state-of-the-art baselines.

### Weaknesses
 - Potential Unfairness in Comparisons: While the paper includes an ablation study where variables like training data are controlled for fair comparison with other models, its main results table appears to use different datasets compared to competing methods. This inconsistency in data setup might lead to an unfair advantage for ROSS, making it difficult to assess the true comparative effectiveness of the approach against state-of-the-art methods. Specifically, the use of different pre-training and fine-tuning datasets across models makes it challenging to isolate the impact of the proposed reconstruction loss. The paper should provide a more rigorous comparison using identical datasets for all models to ensure a fair evaluation.

- Computational Overhead: The denoising process introduces extra computational overhead during training, but the paper does not quantify or discuss this cost, leaving readers uncertain about the practical trade-offs of using this approach. The lack of detailed information regarding the increase in training time, memory consumption, and overall resource requirements makes it difficult to assess the practical applicability of the method, particularly in resource-constrained environments. A thorough analysis of the computational costs is needed to understand the trade-offs between performance gains and computational expenses.

- Limited Analysis of Generation vs. Reconstruction Performance: The paper compares ROSS’s reconstructive approach to generative methods, noting that the generative approach underperforms in comprehension tasks. However, it lacks a thorough exploration of why the generative method yields lower performance. A more in-depth discussion of the limitations and differences between the two approaches would enhance understanding and help identify when reconstruction might be preferable to generation in multimodal tasks. The paper should delve into the specific mechanisms that cause the generative approach to fall short in comprehension, such as potential issues with text-image alignment or the model's ability to capture fine-grained details.

### Questions
It would be cool if authors could address the concerns in weakness.

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
The paper uses image denoising as an auxiliary training task to improve VLMs abilities.
Denoising encourages the VLM to preserve image detail.
The work is motivated by the MAE (masked auto-encoder) line of work for training foundational vision encoders.
The auxiliary task helps VLMs achieve higher benchmark numbers.

### Strengths
Whereas text-based LLMs have achieved amazing results only with next-token prediction, when we have image + text VLMs, it has always seemed that only doing next-token prediction for text could be improved upon.  In that regard, the technique proposed in this paper, to use image denoising as a pretext task, seems like step forward, as a way to add more supervision to the VLM and to improve results. 

The benefits to the metrics are actually significant in some cases, not just epsilon levels, which is great to see.

It seems to me like the method is described clearly and the results are presented clearly.

### Weaknesses
1. I wish the benchmarks cited in the paper to measure the benefits of their method, i wish those benchmarks more closely matched recent popular work such as "The Llama 3 Herd of Models" or "Qwen2-VL", which include benchmarks like TextVQA, DocVQA, etc ... It may not change the conclusion but when we compare methods, it's important to look at a representative distribution of benchmarks. Table 4 has some of these common benchmarks, but not all of them. Furthermore, i wish Table 4 (or perhaps Table 3) included the same benchmarks but also had a very clean A/B experiment that was a baseline without the method vs. using the method. Table 3 has this but Table 3 has a different set of benchmarks! So it's rather confusing what conclusion to draw.

2. The fact that the work was done at lower image resolution also limits the impact of the work. While it may be a perfectly reasonably thing to study the problem initially at lower resolution, I believe that most people care about the models with the best metrics, and all of those methods today use image tiling to handle high resolution images.

### Questions
How will the results change at higher resolution and what would the comparison look like when compared against tile-based methods like LLava-1.6 or any of the more recent VLM work like Qwen2-VL etc ...?

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
This paper introduces ROSS, a novel approach to enhance Large Multimodal Models (LMMs) through vision-centric supervision signals. Unlike conventional visual instruction tuning that only supervises text outputs, ROSS introduces a reconstructive objective where LMMs must reconstruct input images' latent representations. 

The authors address the challenge of spatial redundancy in visual signals by employing a denoising objective to reconstruct latent representations rather than raw RGB values. The approach demonstrates significant improvements across various benchmarks, particularly in fine-grained visual comprehension and hallucination reduction, while maintaining a lightweight architecture compared to existing methods that rely on multiple visual experts.

### Strengths
This paper is very novel and address the very important topic on vision-centric learning in LMM.

Specifically, the paper introduces an innovative vision-centric supervision method that leverages the inherent richness of input images, addressing a clear gap in existing LMM training approaches. The use of denoising objectives for latent representation reconstruction is particularly clever as it handles the spatial redundancy problem.

The authors conduct extensive experiments across multiple benchmarks, including thorough ablation studies that systematically evaluate different components of their approach (regression vs. denoising, different tokenizers, architecture choices). The comparison with state-of-the-art methods is particularly thorough.

ROSS achieves competitive or superior performance using only a single visual encoder, making it more efficient than existing approaches that require multiple visual experts. This has significant practical implications for deployment and scalability.

The methodology is well-grounded in existing literature and builds thoughtfully on previous work in both vision and language domains. The authors clearly explain how their approach differs from both traditional visual instruction tuning and newer aggregated visual instruction tuning methods.

### Weaknesses
I think the major weakness is about the Computational Costs. While the paper emphasizes the efficiency of using a single visual encoder, it lacks detailed analysis of training time, memory requirements, and computational costs compared to baseline methods.

Besides, the paper doesn't thoroughly discuss the sensitivity of ROSS to various hyperparameters, such as the denoising schedule or architecture choices. It would be benefitical to add this part analysis and show ROSS's denoising part is robust and easy to train.

### Questions
This not be a major issue, but it's not very natural to see that using vision encoder to encode image pixels into LLM's embeddings and use another denosing module to reconstruct it back to image pixels. 

This may introduce improvements since the model better maintains the information of original images, but it may be more natural to see it's used in a quantized tokenizer based LMM like EMU-3 and Chamelon.

I was wondering how the authors feel about this and have insights on this question?

### Soundness
4

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
4

### Summary
This paper introduces Reconstructive Visual Instruction Tuning (ROSS), a novel approach that leverages input images as additional supervision signals to enhance fine-grained visual perception capabilities. Through extensive empirical studies, the authors explore optimal training settings, such as auxiliary module design and the nature of supervision signals. Experimental results indicate that ROSS consistently improves the performance of existing vision-language models.

### Strengths
1. The paper is well-organized and easy to follow, with a clear presentation of the key ideas. It is always inspiring to see that a simple auxiliary loss can improve the performance of large multimodal models.
2. The authors have put a lot of effort into designing experiments that thoroughly ablate the proposed training methods. This rigor in experimentation is highly appreciated and adds to the paper’s credibility.

### Weaknesses
1. The proposed method lacks novelty and insight. As noted in Section 2, previous work, such as [1], has explored using images as additional supervision in the form of generative objectives. Consequently, the contribution of this paper is limited, focusing mainly on a variation of established methods.
2. The proposed method lack interpretability. While using pixel-level reconstruction as an auxiliary task may enhance fine-grained image recognition, this approach risks impairing the language capabilities of the multimodal model, as the final task output is high-level semantic language. The authors provide insufficient experiments and explanations regarding this trade-off, leaving questions about potential impacts on language performance. The core issue is that the reconstruction loss is applied directly to the visual feature embeddings before they are processed by the language model, which may not be the most effective way to align visual and textual representations. This approach might inadvertently bias the visual features towards low-level pixel information, potentially hindering the model's ability to extract high-level semantic concepts necessary for tasks like VQA.
3. The scalability of the empirical findings is uncertain. It remains unclear whether the optimal settings identified would hold in different scenarios or with variations in model scale, training data, and other factors. Although the authors attempt to address this concern with results in Table 3, these efforts are insufficient, as many relevant variables remain unexplored.

### Questions
1. The results in Table 4 appear counter-intuitive, as ROSS-13B performs consistently worse than ROSS-7B. This raises concerns about whether the proposed method is well-suited to larger-scale models. Clarification on this disparity and potential scalability issues would strengthen the paper.
2. The analysis in Section 5.2 is unclear. My understanding is that the authors aim to demonstrate that additional visual supervision enables the model to better focus on relevant areas of the image during VQA tasks. However, the reasoning behind this effect is not well-explained. Further elaboration on the mechanisms or evidence supporting this claim would enhance interpretability.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a new variant of visual instruction tuning. Different from previous works that only utilize textual supervision, the proposed method additionally exploits visual supervision by reconstructing the contexts of input images. In particular, a denoising structure is introduced to better learn the latent representations. Experiments are conducted on several benchmarks.

### Strengths
1. The paper is well-organized and easy to read.
2. The motivation is straightforward.

### Weaknesses
1. The novelty is somewhat incremental. Utilizing image supervision is a very straightforward idea, and can be implemented by various ways. Denoising-based reconstruction is a very well-developed strategy in the field of image diffusion/generation. There is no specific in-depth design in the proposed architecture.

2. The authors claim that the proposed method capitalizes on the inherent richness and detail present within input images themselves, which are often lost in pure text supervision. In which cases, the information within the image is important? The authors should provide a more detailed analysis of this aspect. Is this information crucial for all common cases?

3. No experiments on complexity and efficiency. Of course, utilizing more self-supervision loss can definitely improve the model's performance. However, this image-aware training may cost more time and GPU memories compared to previous text-only supervision. The authors should provide an in-depth analysis of complexity and efficiency for fair comparison.

4. Given an image-text pair input, just some of the image-based contents are aligned with the text. I do not see any text-guided image reconstruction design in the architecture. This may help reduce the redundancy contexts.

### Questions
1. The novelty is somewhat incremental. Utilizing image supervision is a very straightforward idea, and can be implemented by various ways. Denoising-based reconstruction is a very well-developed strategy in the field of image diffusion/generation. There is no specific in-depth design in the proposed architecture.

2. The authors claim that the proposed method capitalizes on the inherent richness and detail present within input images themselves, which are often lost in pure text supervision. In which cases, the information within the image is important? The authors should provide a more detailed analysis of this aspect. Is this information crucial for all common cases?

3. No experiments on complexity and efficiency. Of course, utilizing more self-supervision loss can definitely improve the model's performance. However, this image-aware training may cost more time and GPU memories compared to previous text-only supervision. The authors should provide an in-depth analysis of complexity and efficiency for fair comparison.

4. Given an image-text pair input, just some of the image-based contents are aligned with the text. I do not see any text-guided image reconstruction design in the architecture. This may help reduce the redundancy contexts.

### Soundness
2

### Presentation
3

### Contribution
2
