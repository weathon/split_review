# FreeMorph: Tuning-Free Generalized Image Morphing with Diffusion Model

- Decision: Reject
- Avg Score: 5.75
- Scores: 5, 5, 5, 8

## Abstract
We present **FreeMorph**, the first tuning-free method for image morphing that accommodates inputs with varying semantics or layouts. Unlike existing methods, which rely on fine-tuning pre-trained diffusion models and are limited by time constraints and semantic/layout discrepancies, FreeMorph delivers high-fidelity image morphing without extensive training. Despite its efficiency and potential, tuning-free methods still face challenges in maintaining high-quality image morphing due to the non-linear nature of the multi-step denoising process and bias inherited from the pre-trained diffusion model. In this paper, we introduce FreeMorph to address this challenge by integrating two key innovations. **1)** We first propose a **guidance-aware spherical interpolation** design that incorporates the explicit guidance from the input images by modifying the self-attention modules, addressing identity loss, and ensuring consistent transitions throughout the generated sequences. **2)** We further introduce a **step-oriented motion flow** that blends self-attention modules derived from each input image to achieve controlled and directional transitions that respect both input images. Our extensive evaluations demonstrate that FreeMorph outperforms existing methods with training that is 10X - 50X faster, establishing a new state-of-the-art for image morphing. The code will be released.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes a method for image interpolation with off-the-shelf T2I diffusion models. By modifying the attention modules using two proposed methods, the continuousness of the interpolations is improved, without having to fine-tune the diffusion model. The authors also introduce auxiliary tricks to further improve interpolation performance. The contribution of the various proposed components to improved interpolation performance is validated using an extensive ablation study, and the overall performance is compared qualitatively and quantitatively with some alternative approaches.

### Strengths
The quantiative and qualitative experiments, especially the ablation study seem well-executed and thorough, with the exception of one important method missing (see weaknesses). I really appreciate the authors thoroughly evaluating across different levels of challenging interpolations and proving a large number of qualitative comparisons in the appendix.

The proposed method seems reasonable in construction and effective in practice.

In the comparisons performed by the authors, their proposed method seems to provide a clear improvement over the methods they compare against.

Besides small mistakes (see questions), the paper is generally well-structured, reasonably well-written and easy to follow.

### Weaknesses
Attention Interpolation for Text-to-Image Diffusion (He et al., 2024) is cited in the related work section but never compared to, despite the methods seeming quite similar. Given that the authors were aware of this work at the time of submission, I would expect the authors to discuss how their and this method relate and incorporate it into quantitative and qualitative comparisons.

Similarly, Smooth Diffusion (Guo et al., CVPR 2024) is quite closely related and could also be compared to, although it requires additional tuning and thus seems a lot less relevant as a baseline. Demonstrating that the proposed method performs similarly to one requiring extra fine-tuning would strengthen the paper substantially.

Eq. 3 looks wrong to me. Defining it with j as an integer in the range [1, 5] does not result in a slerp, as far as I know.

3.4: I think using a DCT instead of an FFT could help improve quality by getting rid of the correlation between the pixels on the left and right (and top and bottom respectively) edge of the image.

The number of decimal digits in tables is excessive. Please reduce it to a reasonable number (more than 3 or 4 digits should not be necessary in most cases) to aid readability.

There are a bunch of small mistakes. I'd recommend going over the paper and fixing them for a potential camera-ready version, as the current state looks a bit sloppy. Some examples: l. 122: "ur" -> "Our", l. 130: "Recently, Recently,"; l. 132: "wang2023interpolating"; l. 194: wrong citation for LDM, l. 211: I think DiffMorph should be attributed to different people.

### Questions
Eq. 3 looks wrong to me. Defining it with j as an integer in the range [1, 5] does not result in a slerp, as far as I know.

3.4: I think using a DCT instead of an FFT could help improve quality by getting rid of the correlation between the pixels on the left and right (and top and bottom respectively) edge of the image.

The number of decimal digits in tables is excessive. Please reduce it to a reasonable number (more than 3 or 4 digits should not be necessary in most cases) to aid readability.

There are a bunch of small mistakes. I'd recommend going over the paper and fixing them for a potential camera-ready version, as the current state looks a bit sloppy. Some examples: l. 122: "ur" -> "Our", l. 130: "Recently, Recently,"; l. 132: "wang2023interpolating"; l. 194: wrong citation for LDM, l. 211: I think DiffMorph should be attributed to different people.

### Soundness
3

### Presentation
2

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
This paper presents FreeMorph, a tuning-free method for image morphing that accommodates inputs with varying semantics and layouts. Several modules are proposed to enhance the quality of image interpolants, ensuring a smooth transition that remains consistent with the given images at both ends.

### Strengths
1. This method does not require training, making it more accessible to regular users.
1. The authors have conducted extensive experiments to identify the best combination of modules and hyperparameters.
1. Although this is a task that is difficult to evaluate, I can appreciate the authors’ efforts to provide both quantitative and qualitative results.

### Weaknesses
Related to the task
1. There are some unverified claims at the core of this task. For example, see lines 254-255.
2. What constitutes good image morphing is somewhat underdefined. The intended effect that this paper seeks to achieve feels too vague and abstract, making it challenging to identify a clear definition of effective image morphing.
3. Even with quantitative metrics like PPL, high scores do not necessarily indicate results that align with human preferences, which can be highly subjective.

Related to the proposed method
1. While the authors have introduced several modules, their use appears to have been determined empirically. The selection of hyperparameters and the final module composition could benefit from clearer justification, as they seem somewhat arbitrary at times.
2. Given that the method involves multiple components, the presentation could be more streamlined. It can be difficult to understand the specific problem each module aims to address. (Please see questions below for further clarification.)
3. The generated samples have pretty visible ghost artifacts. To me, that would not be considered as good image morphing.

### Questions
1. What's the intuition behind Equation 5. How does it relate to identity preservation?
1. How does Equation 6 connect to motion flow? What do you mean by "step-oriented"?

### Soundness
2

### Presentation
2

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
This paper presents a novel tuning-free image morphing approach, which utilizes the pre-trained stable diffusion and manipulates its self-attention to achieve high-fidelity morphing. Specifically, it proposes a guidance-aware spherical interpolation and step-oriented motion flow, and respectively apply them in different steps of the reverse diffusion/forward denoising processes. Based on the qualitative and quantitative results, the proposed approach outperform the existing methods.

### Strengths
- The proposed tuning-free morphing approach is straightforward and effective. The modified interpolation of the self-attention is able to produce more natural transition between morphing sequences.
- A new dataset, Morph4Data, is presented and used in the evaluation. This dataset contains four categories, which helps in a detailed analysis on the image morphing methods.
- This paper presents and analyzes many baseline settings in the ablation study. This helps in understanding the specific role of each key design.

### Weaknesses
 - This paper is apparently not well prepared for publication. For example:
  - There are many errors in spelling (“ur” in line 122, “owever” in line 133, etc.) and formulations (missing “{“ and “}” in line 179, etc.). 
  - In equation (7), since m has the same size as z, what does it mean by “m=1”? 
  - Both “DeepMorpher” and “deepmorpher” appear in the paper.
  - The image captions of Fig.2 and Fig.3 is too simple. Reader have to move to the main text to try to understand the figures.
- In the introduction, it mentions a comprehensive evaluation system, including a new dataset and specialized metrics. But in Sec 4.1, it says “following IMPUS and DiffMorpher, we ... using the following metrics”. Where are the proposed specialized metrics? 
- This paper presents both the qualitative and quantitative evaluations. In the figures, the “spherical interpolation” looks good than the existing method DiffMorpher. But based on the quantitative evaluation in Table 1, “spherical interpolation” performs worse than DiffMorpher. Therefore, either the visual results are cherry-picked, or the evaluation metrics cannot adequately measure the results. Without a human perceptual study, it’s difficult to get a conclusion when comparing the two methods.
- The proposed algorithm contains a reverse diffusion process and a forward denoising process. In my understanding, the diffusion process of DDIM is to directly add noise without using the trained network. But in Algorithm 1, the modified attention mechanism is applied in the diffusion process. There should be more details to explain how to implement this diffusion process. In addition, why the forward denoising steps also have “for t=1 to T”?
- For the experiment “Ours(Var-A)” in line 469, what does it mean to “omit the original attention mechanism”? Completely remove the attention?

### Questions
My main concerns are the evaluation metrics and the technical details about the reverse diffusion process. I'd like to increase my rating if there are convincing explanations or evidences in the rebuttal.

### Soundness
3

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper propose FreeMorph, a tuning-free pipeline that can generate transitions between two images within 30 seconds. It proposes two components, guidance-aware spherical interpolation, and Step-oriented motion flow, which yields smooth transitions between source and target images, even at examples of cross semantics. Both visual and quantitative evaluations are provided.

### Strengths
I think this paper is above the bar, with good results and reasonable techinques. Experiments are well designed, limitations are discussed.

### Weaknesses
Some motivation parts are not that clear to me, see below

This paper targets at two issues related to the image morphing, identity loss and directional trasition. However, I do not see the importance of these two issues. Why they are important and worthing efforts for this task. 

For example, when not preserving the identity, what results would be like. Similarly, what is the issue when miss preserve directional transition. I understand that the smooth transition is important, is it the same as the meaning of directional transition?

 These are important questions to me when reading the introduction. I can see cool examples in the intro, but cannot figure out clearly the core issues that this paper handles. I try to solve this by see examples of compared other methods, and some of them are still OK during the transition. 

What is the successful rate, are the results cherry-picked

### Questions
This paper targets at two issues related to the image morphing, identity loss and directional trasition. However, I do not see the importance of these two issues. Why they are important and worthing efforts for this task. 

For example, when not preserving the identity, what results would be like. Similarly, what is the issue when miss preserve directional transition. I understand that the smooth transition is important, is it the same as the meaning of directional transition?

 These are important questions to me when reading the introduction. I can see cool examples in the intro, but cannot figure out clearly the core issues that this paper handles. I try to solve this by see examples of compared other methods, and some of them are still OK during the transition. 

What is the successful rate, are the results cherry-picked

### Soundness
3

### Presentation
3

### Contribution
3
