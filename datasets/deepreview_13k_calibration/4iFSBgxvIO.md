# Cached Multi-Lora Composition for Multi-Concept Image Generation

- Decision: Accept
- Avg Score: 5.33
- Scores: 6, 5, 5

## Abstract
Low-Rank Adaptation (LoRA) has emerged as a widely adopted technique in text-to-image models, enabling precise rendering of multiple distinct elements, such as characters and styles, in multi-concept image generation. However, current approaches face significant challenges when composing these LoRAs for multi-concept image generation, particularly as the number of LoRAs increases, resulting in diminished generated image quality. 
In this paper, we initially investigate the role of LoRAs in the denoising process through the lens of the Fourier frequency domain.
Based on the hypothesis that applying multiple LoRAs could lead to "semantic conflicts", we have conducted empirical experiments and find that certain LoRAs amplify high-frequency features such as edges and textures, whereas others mainly focus on low-frequency elements, including the overall structure and smooth color gradients.
Building on these insights, we devise a frequency domain based sequencing strategy to determine the optimal order in which LoRAs should be integrated during inference. This strategy offers a methodical and generalizable solution compared to the naive integration commonly found in existing LoRA fusion techniques.
To fully leverage our proposed LoRA order sequence determination method in multi-LoRA composition tasks, we introduce a novel, training-free framework, Cached Multi-LoRA (CMLoRA), designed to efficiently integrate multiple LoRAs while maintaining cohesive image generation.
With its flexible backbone for multi-LoRA fusion and a non-uniform caching strategy tailored to individual LoRAs, CMLoRA has the potential to reduce semantic conflicts in LoRA composition and improve computational efficiency.
Our experimental evaluations demonstrate that CMLoRA outperforms state-of-the-art training-free LoRA fusion methods by a significant margin -- it achieves an average improvement of $2.19$% in CLIPScore, and $11.25%$% in MLLM win rate compared to LoraHub, LoRA Composite, and LoRA Switch.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
In this paper, the authors propose an analysis of typical LoRA algorithms when subjected to a caching mechanism. The study is further extended with the proposal of a framework integrating multiple LoRA mechanisms, aiming at reducing concept-related uncertainty, which is expected to show reduced semantic misconceptions. The proposed method is extensively evaluated in terms of CLIPScore and  MiniCPM-V  testing.

### Strengths
The paper is generally well written and, (at least for the class of similar papers) rather easy to follow. 
The claims of the authors, on which the paper writing discourse is based on, are verified through evaluations which can become clear, if correctly exemplified.

### Weaknesses
Even if the writing is good, the quality of the visuals (e.g Fig 4, 6) can be improved. 
A lack of visual comparisons is not expected, given the fact that the most of the evaluations showing a certain advantage of the proposed method are either purely subjective or extremely difficult to quantify. 
At least in terms of quantitative evaluations (in terms of CLIPScore), the introduction of the cache mechanism does not show consistent results, but rather mixed. A systemic improvement/degradation of the performance its difficult to identify or explain, at least for the cache mechanism analysis. 
A total lack of evaluations in terms of computational effort/efficiency.

### Questions
Does a multiple LoRA mechanisms ensemble improve the behavior of the generative model in terms of concepts that are under-represented at the data level?
Can you provide some examples in which the method shows improved semantic consistency? 
Why are the claims at the end of page 9 and the beginning of page 10 not proven through a visual comparison?
What (or how can be quantified) is the computational effort of the compared methods?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper works on fixing issues of using Lora for multi-concept image generation. Particularly, this paper empirically find that some LoRAs amplify high-frequency features, and others focus on low- frequency elements. Based on this observation, a frequency domain based sequencing strategy is presented to determine the optimal order in which LoRAs should be integrated during inference, and a training-free framework, namely Cached Multi-LoRA (CMLoRA), is designed to integrate multiple LoRAs while maintaining cohesive image generation. Experiments suggest that CMLoRA outperforms SOTA training-free LoRA fusion methods for multi-concept image generation.

### Strengths
1.Frequence domain analysis for multi-component generation is indeed an interesting idea. 

2.The proposed solution is easy and clear (although high-level insight is not very obvious.)

3.The experiments are good in explain the effectiveness of the solution.

### Weaknesses
1. It’s not clear why frequency domain is needed to solve the multi-component generation task. A clear investigation and analysis on how they come up with this solution can further strengthen the contribution of the work. Particularly, more analysis is needed to explain why shift attention from spatial domain to frequency domain.

2. The observation that some LoRAs amplify high-frequency features, and others focus on low- frequency elements is based on a naïve experiment. More analysis or theoretical analysis is needed to better appreciate the proposed idea.

3. The experimental results is good but not convincing to explain the superiority of the solution.

### Questions
1.I’m not sure about Figure 1. Do you assume that meaningful amplitude difference happens only at the same time steps for the two Loras? In another word, do you assume different Lora categories are well-aligned along time step? Furthermore, given that the observation in Figure 1 motivates the proposed method, it’s suggested to provide comprehensive analysis to explain the high/low frequency issues of different Loras.

2.The proposed solution in Section 2.2 is presented without deep analysis. Can you please provide a high-level analysis of your solution to explain your method in a progressive way? e.g. eq (2), eq (3) is introduced directly without explain why.

3.The observation is based on Lora categories from Ref1. How does the method perform with respect to different Lora categories? 

4.The collective guidance in eq (5) seems related to classifier free guidance, can you please provide further analysis?

5.Benchmark comparison in Table 1 seems marginal performance gain. Please explain further.

6.Please also explain in detail the “semantic conflict” issue as there exists no experiments to verify the existence of this issue (or maybe I failed to find it, please show me where I can find it.)

Ref1, Multi-lora composition for image generation, 2024.

### Soundness
2

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
5

### Summary
This paper introduces Cached Multi-LoRA (CMLoRA), a framework for training-free, multi-concept image generation that integrates multiple Low-Rank Adaptation (LoRA) modules in text-to-image diffusion models. By analyzing LoRAs in the Fourier domain, CMLoRA partitions LoRAs into high- and low-frequency sets, applying high-frequency LoRAs in early denoising stages and low-frequency ones later to reduce semantic conflicts. A novel caching mechanism selectively activates non-dominant LoRAs, enhancing computational efficiency while maintaining image quality. Evaluated against existing methods, CMLoRA shows superior performance in aesthetic and compositional quality, demonstrating its effectiveness for generating complex, coherent images from multiple concepts.

### Strengths
1.  The paper introduces a novel Fourier-based approach to address the challenge of multi-LoRA composition by partitioning LoRA modules into high- and low-frequency categories. This frequency-aware sequencing strategy is innovative, as it moves beyond the typical naive integration of LoRAs by leveraging the frequency domain to systematically order their application during inference. This approach effectively mitigates semantic conflicts and represents a creative combination of LoRA adaptation with Fourier-based analysis, contributing a unique perspective to the field of multi-concept image generation.

2.  The paper’s methodology is sound and well-supported by rigorous experimentation. The introduction of the Cached Multi-LoRA (CMLoRA) framework is methodically detailed, with clear mathematical formulations and a thorough explanation of the caching mechanism. The empirical evaluations are comprehensive, covering a range of established metrics like CLIPScore and MLLM-based benchmarks, which validate the claims across different aspects of multi-concept image synthesis, including element integration, spatial consistency, and aesthetic quality.

3. The proposed CMLoRA framework addresses a significant limitation in current LoRA-based image generation methods by enabling efficient and high-quality integration of multiple LoRA modules. The training-free nature of CMLoRA increases its practical applicability, making it more accessible for scenarios where training resources are limited or infeasible.

### Weaknesses
1. What are the failure cases? A couple of visual examples of failed outputs could provide more insights into the limitations of the CMLoRA method.

2. How were the caching hyperparameters $c_1$ and $c_2$ chosen, and how sensitive is the model’s performance to their variations? Furthermore, there is limited discussion of how the caching interval impacts the final performance in terms of both computational efficiency and image quality. Additional experiments that explore the impact of varying these parameters would make the paper’s claims around caching strategy more robust and actionable for readers interested in applying or extending CMLoRA.

3. What is the exact impact of the frequency-based LoRA partitioning, and would alternative sequencing strategies be effective?

4. The paper’s evaluations focus primarily on a limited set of datasets (anime and realistic styles within the ComposLoRA testbed) and may not generalize to broader multi-concept applications. Furthermore, CLIPScore and the other metrics used may not fully capture nuances in compositional fidelity, particularly as the number of LoRAs increases. Expanding the scope of datasets and incorporating additional image quality metrics, such as perceptual quality or domain-specific measures, would strengthen the applicability of CMLoRA across a wider range of practical scenarios.

### Questions
1. Could you provide examples or further analysis of cases where CMLoRA might struggle with semantic conflicts? For example, are there certain LoRA combinations or types of images where the method performs suboptimally?

2. Could you clarify how you determined the values for the caching hyperparameters $c_1$ and $c_2$? Did you observe any significant performance variations with different values, and if so, could you provide insights on optimal settings?

3. Have you tested CMLoRA on datasets beyond the anime and realistic styles in the ComposLoRA testbed? If not, could you discuss how the method might adapt to other domains?

### Soundness
2

### Presentation
3

### Contribution
2
