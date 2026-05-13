# Rare-to-Frequent: Unlocking Compositional Generation Power of Diffusion Models on Rare Concepts with LLM Guidance

- Decision: Accept
- Scores: 8, 8, 6, 8

## Abstract
State-of-the-art text-to-image (T2I) diffusion models often struggle to generate rare compositions of concepts, e.g., objects with unusual attributes. In this paper, we show that the compositional generation power of diffusion models on such rare concepts can be significantly enhanced by the Large Language Model (LLM) guidance. 
We start with empirical and theoretical analysis, demonstrating that exposing frequent concepts relevant to the target rare concepts during the diffusion sampling process yields more accurate concept composition. 
Based on this, we propose a training-free approach, \algname{}, that plans and executes the overall rare-to-frequent concept guidance throughout the diffusion inference by leveraging the abundant semantic knowledge in LLMs.
Our framework is flexible across any pre-trained diffusion models and LLMs, and can be seamlessly integrated with the region-guided diffusion approaches. 
Extensive experiments on three datasets, including our newly proposed benchmark, \dataname{}, containing various prompts with rare compositions of concepts, \algname{} significantly surpasses existing models including SD3.0 and FLUX by up to $28.1\%p$ in T2I alignment.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper studies how to perform rare concept image generation with current pre-trained diffusion models. The authors leverage the LLMs to extract the rare concept and rewrite the prompt, and then perform rare-to-frequent guidance with the rewritten prompts across the multi-step denoising generating process. Abudent theoretical and empirical analyses are provided to validate the effectiveness of the method.

### Strengths
1) The proposed rare-to-frequent prompt rewrite is novel and effective in terms of generating rare-concept-images.
2) The empirical results looks promising.
3) Solid empirical results are provided to validate the effectiveness of the method.
4) A new benchmark, RareBench, is provided to facilitate research in the task of rare-concept-image-generation.
5) Code and detailed implementation is provided to ensure the reproducibility of the method.

### Weaknesses
(1) The method requires alternating among a set of prompts during denoising process, which makes multiple step inference inevitable. Therefore, this design might not work well with current state-of-the-art acceleration methods, which reduce the number of denoising steps to 4 steps or even less.

(2) There is a small gap between the theoretical analysis and the empirical method. For the theoretical analysis, the author study the scenarios of linearly interpolation of scores produced by different prompts. While for empirical results, the author performs alternating prompts across different denoising steps.

### Questions
Please see weakness (1). The reviewer is curious about how can we apply the proposed method on accelerated version of diffusion models such as consistency model.

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
4

### Summary
This paper examines diffusion-based image generation for objects with unusual attributes, which is termed as rare composition of concepts and pretty common in art design. Current methods are struggle to accurately generate images from rare and complex prompts. To solve this question, this approach effectively utilizes the correlation between frequent and common composition. Specifically, in the early stage of the reverse process, the frequent composition is used to guide noise prediction where the rare one is used. In this way, the frequent one is used to provide good initialization for the final generation. This method is training free with both theoretical analysis and experimental validation provided. An advanced version of the region-based generator is also proposed.

### Strengths
1.	The observation in alternating prompts in diffusion-based models are important.
2.	Both global and region-based generation are proposed.
3.	Detailed visualization are provided.

### Weaknesses
1.	The current design for the scheduling of the selection of frequent and rare composition of concepts is a bit ad-hoc. You always use frequent composition at the beginning and then start randomly selection of composition after a fixed point. Based on your theoretical analysis, any additional guidance can be included or used to determine the selection of composition of concepts? Specifically, the transition point from frequent to random selection seems arbitrary. Is there a principled way to determine this point based on the diffusion process or the semantic content of the prompt itself? For instance, could the variance of the noise at each step or the semantic similarity between the frequent and rare concepts be used to dynamically adjust this transition point?
2.	From your example, each rare composition has only two concept. How do you generalize your approach to more complicated and rare composition (3 or more concepts, such as adj. + adj. + noun, e.g., an agent rabbit with a gun in a casual suit ). It's unclear how the method would handle the combinatorial explosion of possible frequent concept replacements when dealing with more complex prompts. For example, in the case of "an agent rabbit with a gun in a casual suit", which frequent concept would be used to guide "agent rabbit", "rabbit with a gun", or "gun in a casual suit"? How does the method decide which sub-combination to focus on?
3.	Have you tried to use rare components at the beginning and then use frequent instead? The intuitive explanation for using frequent one first is needed.  It will be good if you have relevant experimental results. The current explanation relies on the idea that early diffusion steps determine the rough structure, but this is not rigorously proven. It would be beneficial to see experiments that directly compare the proposed approach with the reverse strategy to validate this claim.
4.	In real world, both rare and frequent composition of concepts are considered in generation. Then, the method that improves quality of rare composition should not hurt the quality of frequent composition. Without manual determination, how can your approach still maintain high generation of frequent composition. In other words, it will be good if you can provide discussion on how your method could be adapted to automatically handle both rare and frequent compositions without manual intervention. Specifically, how does the method determine when a composition is frequent enough to not require guidance from a frequent concept? A clear threshold or criteria is needed to avoid unnecessary interference with already well-formed frequent compositions.

### Questions
Please address my questions in the weakness.

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper deals with generating rare compositions of concepts, which is challenging for existing compositional generation methods.  The authors propose Rare-to-Frequent (R2F), which utilizes LLMs to plan and execute the overall rare-to-frequent concept guidance throughout the diffusion inference.  The paper improves R2F with the layout guidance to achieve more precise spatial-aware generation. Moreover, a new benchmark RareBench is proposed.

### Strengths
- This paper is well-written and easy to follow.
- The method is training-free. Experimental results show that R2F outperforms previous models on various metrics.
- It brings a new task to compositional generation or text-to-image generation.

### Weaknesses
 - For applications, rare concept composition generation is still a relatively niche area, although I acknowledge that it is indeed a novel task within compositional generation. Have you considered exploring a broader range of application scenarios?
- For the computational cost, this paper adopts an approach similar to LMD to enhance R2F, resulting in R2F+, which involves substantial latent and gradient computations. A detailed comparison of computational and memory overhead with other methods is essential to assess the feasibility of the proposed approach.

- I’m not entirely clear on the specific rules LLMs use to determine the “visual detail level.” In your writing, this measure is used in alternating concept guidance to set the guidance length for rare and frequent prompts, with more challenging rare concepts requiring extended guidance. However, LLMs lack knowledge of diffusion priors, which would inform the difficulty associated with generating certain objects or attributes.
- The example you give in Figure 4, where "plants made of glass", I don't think it is a frequent concept. Furthermore, in the initial stages of denoising, diffusion models primarily focus on generating rough visual features (e.g., shape, location). Consider the concept of “furry”; both “furry bird” and “furry tiger” are frequent concepts LLMs may output, yet there is a significant difference in the size and shape of these objects, which has a notable impact on the generated result. Thus, I question whether LLMs can reliably provide suitable frequent concepts.
- Is the design of R2F+ necessary？ In fact, layout-based methods have outstanding spatial awareness,  however, the trade-off is increased computational cost and a decline in image quality (in terms of detail, aesthetics, etc.). First, you need to conduct a comparative evaluation of R2F+ in terms of image quality. Additionally, as noted in Table 3’s T2I-CompBench, R2F achieves higher spatial metrics than both the layout-based method LMD and the LLM-based method RPG. Thus, expanding R2F to a layout-based approach may be unnecessary, as it would only improve spatial performance while significantly compromising image quality.
- You can consider using the IterComp[1], which is a backbone specifically designed for compositional generation and may lead to a more significant performance improvement.

### Questions
- I’m not entirely clear on the specific rules LLMs use to determine the “visual detail level.” In your writing, this measure is used in alternating concept guidance to set the guidance length for rare and frequent prompts, with more challenging rare concepts requiring extended guidance. However, LLMs lack knowledge of diffusion priors, which would inform the difficulty associated with generating certain objects or attributes.
- The example you give in Figure 4, where "plants made of glass", I don't think it is a frequent concept. Furthermore, in the initial stages of denoising, diffusion models primarily focus on generating rough visual features (e.g., shape, location). Consider the concept of “furry”; both “furry bird” and “furry tiger” are frequent concepts LLMs may output, yet there is a significant difference in the size and shape of these objects, which has a notable impact on the generated result. Thus, I question whether LLMs can reliably provide suitable frequent concepts.
- Is the design of R2F+ necessary？ In fact, layout-based methods have outstanding spatial awareness,  however, the trade-off is increased computational cost and a decline in image quality (in terms of detail, aesthetics, etc.). First, you need to conduct a comparative evaluation of R2F+ in terms of image quality. Additionally, as noted in Table 3’s T2I-CompBench, R2F achieves higher spatial metrics than both the layout-based method LMD and the LLM-based method RPG. Thus, expanding R2F to a layout-based approach may be unnecessary, as it would only improve spatial performance while significantly compromising image quality.
- You can consider using the IterComp[1], which is a backbone specifically designed for compositional generation and may lead to a more significant performance improvement.

I will revise my rating according to the author's feedback and the reviewer's discussion.

[1] IterComp: Iterative Composition-Aware Feedback Learning from Model Gallery for Text-to-Image Generation

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
The paper introduces an innovative method for compositional generation of rare concepts. It demonstrates both theoretically and empirically that incorporating frequent concepts related to the target rare concepts leads to more accurate compositions. Building on this analysis, the Rare2Frequent (R2F) approach is presented, which strategically guides the transition from rare to frequent concepts during diffusion inference by utilizing the extensive semantic knowledge available in large language models (LLMs). R2F undergoes comprehensive evaluation, both qualitatively and quantitatively, achieving state-of-the-art results on multiple benchmarks, along with the introduction of a new benchmark for rare compositions.

### Strengths
- The paper is clearly written and well-organized.  
- The results, both qualitative and quantitative, are impressive.  
- Although the concept of transferring knowledge from frequent to rare concepts has been explored in the context of domain adaptation and long-tail learning [1,2,3], its application in diffusion models for image generation is novel.  
- A significant new benchmark, RareBench, is introduced to assess the generation of rare concept compositions.  
- The proposed approach is applied to various diffusion models (SD3.0, Flux, RPG, and region-guided diffusion), demonstrating its effectiveness.  


[1] Parisot., et al. (2022) Long-tail Recognition via Compositional Knowledge Transfer.  
[2] Samuel., et al. (2020) From Generalized zero-shot learning to long-tail with class descriptors.  
[3] Jing., et al. (2021) Towards Fair Knowledge Transfer for Imbalanced Domain Adaptation.

### Weaknesses
My primary concern is that what is deemed rare for the diffusion model may not be considered rare for the LLM. Since the LLM lacks access to the training distribution of concepts used by the diffusion model, it may substitute rare concepts with other rare ones. Providing the LLM with the concept distribution from LION could enhance the results. This distribution has been published by [1].

### Questions
See weaknesses.

### Soundness
3

### Presentation
4

### Contribution
3
