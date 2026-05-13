# SeMv-3D: Towards Semantic and Mutil-view Consistency simultaneously for General Text-to-3D Generation with Triplane Priors

- Decision: Reject
- Scores: 3, 5, 6, 5, 6

## Abstract
Recent advancements in generic 3D content generation from text prompts have been remarkable by fine-tuning text-to-image diffusion (T2I) models or employing these T2I models as priors to learn a general text-to-3D model. While fine-tuning-based methods ensure great alignment between text and generated views, i.e., \textbf{semantic consistency}, their ability to achieve multi-view consistency is hampered by the absence of 3D constraints, even in limited view. In contrast, prior-based methods focus on regressing 3D shapes with any view that maintains uniformity and coherence across views, i.e., \textbf{multi-view consistency}, but such approaches inevitably compromise visual-textual alignment, leading to a loss of semantic details in the generated objects.
To achieve semantic and multi-view consistency simultaneously, we propose \textbf{\textit{SeMv-3D}}, a novel framework for general text-to-3d generation. 
Specifically, we propose a Triplane Prior Learner (TPL) that learns triplane priors with 3D spatial features to maintain consistency among different views at the 3D level, e.g., geometry and texture. Moreover, we design a Semantic-aligned View Synthesizer (SVS) that preserves the alignment between 3D spatial features and textual semantics in latent space. In SVS, we devise a simple yet effective
batch sampling and rendering strategy that can generate arbitrary views in a single feed-forward inference.
Extensive experiments present our SeMv-3D's superiority over state-of-the-art performances with semantic and multi-view consistency in any view. Our code and more visual results are available at \url{https://anonymous.4open.science/r/SeMv-3D-6425}.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This work proposes a feedforward text-to-3D generation framework with multi-view consistency and semantic alignment. Specifically, it fine-tunes a well-trained diffusion model to produce triplane priors. To achieve better semantic alignment, it further introduces the DINO feature in the semantic-aligned view synthesizer module.

### Strengths
1. This work proposes a triplane-based pipeline to keep multi-view consistency and semantic alignment.
2. The experiments showcase better consistency than MVDream.

### Weaknesses
1. The motivation behind this work appears insufficient.
  - The choice of MVDream-like methods for comparison seems misplaced. Fine-tuned diffusion models typically require additional optimization steps like NeRF or NeuS reconstruction to generate 3D shapes directly. A more appropriate comparison could be made with works such as "ET3D: Efficient Text-to-3D Generation via Multi-View Distillation," which aligns closely with the task at hand.
  - Concerns arise regarding semantic consistency. While prior-based methods have struggled with semantic alignment issues stemming from overfitting to 3D datasets, SEMV-3D's Semantic View Synthesis (SVS) mechanism appears to maintain semantic alignment, largely relying on DINO features. Similar strategies have been observed in instant3D and GRM.

2. The paper overlooks multiview reconstruction-based feedforward pipelines, such as instant3D, LGM, and GRM, which excel in semantic consistency. Notably, instant3D, incorporating DINO and Triplane, shares striking similarities with this approach.
- The claim of Triplane's 'efficiency' in Line 159 may not be entirely justified, particularly compared with 3D Gaussians.

### Questions
- What is the inference time of SEMV-3D per prompt?

- Figure 5 lacks a text prompt. The CA exhibits less benefit in Figure 5.

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
This paper presents a feed-forward text-to-3D generation framework, which consists of a triplane prior learner model and a semantic-aligned view synthesizer. Experiments are conducted to validate the effectiveness of the proposal.

### Strengths
S1. The proposed triplane prior learner is reasonable. 

S2. Learning a high-quality feed-ward text-to-3D generation model is a promising research direction.

S3. The proposed orthogonal attention is suitable for the triplane network.

### Weaknesses
W1. What is the evaluation set used by authors? I am wondering whether the authors use standard benchmarks to evaluate their methods. 

W2. The authors only show two or three qualitative comparison examples in Figure 3. It is encouraged to provide more comparison examples to avoid cherry-picking results. 

W3. The authors only conduct qualitative ablation studies in Sec 4.5. Quantitative ablation studies are also necessary to better validate the effectiveness of each design.  

W4. What is the inference time of the proposed method?

### Questions
Please see the Weaknesses.

### Soundness
2

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
4

### Summary
This paper presents SeMv-3D, a framework for text-to-3D generation that aims to address two main challenges in the field: semantic consistency and multi-view consistency. SeMv-3D utilizes a Triplane Prior Learner (TPL) and a Semantic-aligned View Synthesizer (SVS) to achieve dual consistency. TPL captures spatial coherence across views using a triplane representation, while SVS aligns three-dimensional features with textual semantics. This framework utilizes a batch sampling and rendering method that allows for generating arbitrary views in one feed-forward step. SeMv-3D outperforms existing methods in extensive experiments, achieving state-of-the-art performance despite limitations in text-to-3D data and computational resources.

### Strengths
1. SeMv-3D effectively addresses challenges in achieving both multi-view and semantic consistency in text-to-3D generation.

2. The TPL and SVS modules enable SeMv-3D to maintain high visual-textual alignment while ensuring 3D consistency across different views.

3. The batch sampling and rendering approach enables efficient and flexible view generation in a single inference pass.

4. Extensive experiments demonstrate SeMv-3D’s qualitative and quantitative improvements over state-of-the-art methods.

### Weaknesses
1. The lack of high-quality, large-scale text-3D paired data limits the model's ability to optimize for generalizability. Specifically, the model's performance might degrade when presented with text prompts describing objects or scenes that deviate significantly from the training data distribution. This is a common challenge in text-to-3D generation, but the paper should more explicitly acknowledge the potential for bias and limited diversity in the generated 3D models due to the dataset's constraints.

2. Limited resources impact convergence, which can influence the stability and quality of the model's performance in complex scenarios. The paper should include a more detailed analysis of how resource constraints affect the training process, such as the number of training iterations, the size of the model, and the optimization algorithm's convergence behavior. It is unclear how the model behaves in terms of training stability and convergence, and how these factors affect the final quality of the 3D models, especially for complex prompts.

3. Clarify the novelty of the proposed semantic-aligned method. What is the semantic-aligned strategy, and how can it be applied? The paper should provide a more detailed explanation of the semantic alignment strategy, including the specific mechanisms used to match text embeddings with 3D features. It is not clear how the proposed method differs from existing approaches that also aim to align text and 3D representations. The paper should also discuss the limitations of the proposed semantic alignment strategy and how it might be improved in future work.

### Questions
This paper claims to use semantic and view-consistent methods to achieve high-quality text-to-3D. However, it does not clarify the semantic consistency process. Please provide more details to support the contributions.

1. How does SVS achieve semantic alignment?

2. Details on SVS’s mechanisms to match text with 3D features in latent space would support the semantic consistency claim?

3. Clarify if TPL’s spatial correspondences enhance semantic alignment across views?

4. Explain if TPL features are iteratively refined to improve SVS alignment?

5. Specify how simultaneous multi-view generation strengthens semantic coherence?

6. Evidence comparing SeMv-3D’s semantic consistency to other methods would substantiate this contribution?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper addresses the generalized text-to-3D generation problem. It proposes SEMV-3D -- a text-to-3D generative model composed of two stages: The first stage converts an input text prompt into three orthogonal images forming an “RGB-triplane,” while the second stage maps this “RGB-triplane” to a true radiance field triplane. Specifically, SEMV-3D introduces a Triplane Prior Learner (TPL) module in the first stage, which fine-tunes Stable Diffusion to generate a background-free front view, then refines additional layers (front, side, and top views) to produce the final RGB-triplane. In the second stage, the Semantic-aligned View Synthesizer (SVS) transforms the RGB-triplane into DINO tokens, which are concatenated with semantic descriptors of different prompt parts and passed through a transformer to create the true radiance field. Experiments are conducted in several settings including quantitative, qualitative, and user-study results to demonstrate the effectiveness of the proposed method.

### Strengths
+ The paper is well-organized and written.
+ The introduced modules, particularly in the TPL stages, appear effective; notably, the Orthogonalization Attention (OA) enhances view consistency and 3D detail, likely contributing significantly to the final 3D model.
+ The overall pipeline is logically structured.

### Weaknesses
 + The lack of quantitative results in the ablation study makes it challenging to validate the effectiveness of individual modules.
+ The reasoning behind dividing the TPL stage into two substages, Object Retention (OR) and Triplane Orthogonalization (TO), is unclear.
+ Equation 6 lacks clarity: the meaning of ￼ is undefined, and the OA module should have two input arguments, though equation 6 shows only one.
+ It is unclear why a widely recognized metric like FID (or its variants) is not used to evaluate the model’s generative performance.
+ The method for computing semantic information in the SVS stage is not well-explained.
+ Line 232 should reference Fig. 2 (c) for easier comprehension.
+ There is no time comparison with MVDream or similar approaches.
+ Figures 4 and 5 show results of lower quality compared to MVDream.
+ Visualizations and examples of the RGB-Triplane are needed, as it is an uncommon term.

### Questions
+ In the TPL stage, could merging the two substages impact performance? Since the TO modules seem to encompass the OR modules, could it be possible to train the OR modules individually for each orientation in the first substage, and then aggregate the trained weights with the OA modules in the second? Additional insights on this would be valuable.
+ Could you provide more detail on Equation 6 and the computation of semantic information in the SVS stage?
+ Addressing the choice of metrics would clarify the evaluation approach and strengthen the paper.
+ A comparison between Orthogonal Attention and Epipolar Attention from [a] and [b] would be beneficial.

[a] Kant, Yash, et al. "SPAD: Spatially Aware Multi-View Diffusers." Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2024.

[b] Huang, Zehuan, et al. "Epidiff: Enhancing multi-view synthesis via localized epipolar-constrained diffusion." Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2024.

### Soundness
3

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
This paper proposes a novel framework, SeMv-3D, to ensure both semantic and multi-view consistency in generating 3D representations from text. It introduces a TPL module for learning the triplane prior and an SVS module for aligning textual and 3D visual information.

### Strengths
- This paper is well-organized and well-motivated, targeting the text-to-3D problem with promising application prospects.
- This paper effectively summarizes the limitations of existing methods in terms of semantic and multi-view consistency.
- This paper makes a commendable attempt to address these issues within a unified framework.

### Weaknesses
 - The compared baseline methods are limited, lacking comparisons with recent methods such as [1] and [2].
- The quality of the generated 3D models is limited, with granular and discontinuous surfaces visible in rendered images, particularly in Figures 3, 6 and 7.

### Questions
- Many rendered images have noticeable graininess, such as the result on the right side of Figure 3 and the fish in Figure 6. Can you analyze the reason?

### Soundness
3

### Presentation
3

### Contribution
3
