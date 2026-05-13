# Large-Vocabulary 3D Diffusion Model with Transformer

- Decision: Accept
- Scores: 6, 6, 6

## Abstract
Creating diverse and high-quality 3D assets with an automatic generative model is highly desirable. Despite extensive efforts on 3D generation, most existing works focus on the generation of a single category or a few categories. In this paper, we introduce a diffusion-based feed-forward framework for synthesizing massive categories of real-world 3D objects \textit{with a single generative model}. Notably, there are three major challenges for this large-vocabulary 3D generation: \textbf{a}) the need for expressive yet efficient 3D representation; \textbf{b}) large diversity in geometry and texture across categories; \textbf{c}) complexity in the appearances of real-world objects. To this end, we propose a novel triplane-based 3D-aware \textbf{Diff}usion model with \textbf{T}rans\textbf{F}ormer, \textbf{DiffTF}, for handling challenges via three aspects. \textbf{1}) Considering efficiency and robustness, we adopt a revised triplane representation and improve the fitting speed and accuracy. \textbf{2}) To handle the drastic variations in geometry and texture, we regard the features of all 3D objects as a combination of generalized 3D knowledge and specialized 3D features. To extract generalized 3D knowledge from diverse categories, we propose a novel 3D-aware transformer with shared cross-plane attention. It learns the cross-plane relations across different planes and aggregates the generalized 3D knowledge with specialized 3D features. \textbf{3}) In addition, we devise the 3D-aware encoder/decoder to enhance the generalized 3D knowledge in the encoded triplanes for handling categories with complex appearances. Extensive experiments on ShapeNet and OmniObject3D (over 200 diverse real-world categories) convincingly demonstrate that a single DiffTF model achieves state-of-the-art large-vocabulary 3D object generation performance with large diversity, rich semantics, and high quality. Our project page:~\url{https://ziangcao0312.io/difftf_pages/}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a two-stage 3D generation method, where 1) in the first stage, triplanes and a shared decoder are fitted on Shapenet/OmniObject 3D dataset. 2) in the second stage, a diffusion model is trained on the fitted triplanes. The author proposes a novel transformer-based denoiser (based on the proposed cross-plane attention) for training the diffusion model, and show state-of-the-art 3D generation results.

### Strengths
1. It makes a lot of sense to use attention to model the inter- and cross-plane relations in a triplane, and learn such relations on massive amount of data. Ablation studies show that this is very effective.    2. The proposed method achieves state-of-the-art generation results on both Shapenet and OmniObject3D datasets in terms of geometry and texture quality, and diversity.

### Weaknesses
1. I feel that this paper’s writing is very confusing, and could be improved significantly for clarity.
    - The method section shows that this is a two-stage model; but Fig. 2 seems to suggest that this is a single-stage model. The authors might want to make Fig. 2 clearer.
    - For figure 4, since the generation results on OmniObject3D are class-conditioned, would it make sense to arrange the results in a specific order of classes in order for the readers to easily compare different methods?
    - I have to dig into the appendix to find the architecture of the shared triplane decoder; there’s no reference to appendix in section 3.1. What’s worse, even looking at the appendix, I’m still unable to find out the width of the MLP layers for the triplane decoder.
    - I find it a bit hard to imagine what exactly the architectures are for the different variants in the ablation “Studies of 3D-aware transformer modules”. The authors might want to elaborate more in the appendix, or better draw figures to the ablated architectures.
    - Section 4.3 mentioned about the importance of triplane normalization. But this is never mentioned in the method section. In fact, the authors might want to show a histogram of the unnormalized triplane values in the appendix.

### Questions
1. What is the prediction objective of DiffTF’s diffusion model? Is it \epsilon-prediction, x_0 prediction or v-prediction?
2. What’s the size of the shared triplane decoder?
3. For the 3D-aware transformer part, as the triplane resolution is only 16x16 and the patch size is 2, this means that there’re only 8x8=64 tokens on each plane, and 64x3=192 tokens in total. Why not just do self-attention over all these 192 tokens, instead of using the cross-plane attention? Would this simpler architecture also work? In fact, looking at figure 3(b), such simple self-attention is already used in the 3D-aware encoder/decoder.
4. How does the proposed cross-plane attention compared against Rodin’s 3D-aware convolution? Does it make sense to compare with this work qualitatively and quantitatively, as the cross-plane attention seems a major contribution of this work?
	Rodin: A Generative Model for Sculpting 3D Digital Avatars Using Diffusion
5. It seems that the model is trained per-category on shapenet cars, chairs, airplanes? Why not train a class-conditioned generator just like what has been done on the OmniObject3d data?

### Soundness
3 good

### Presentation
1 poor

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents a 3D generation pipeline based on triplane diffusion. To achieve this, triplane fitting is conducted on the train set, and the output triplanes are used as the inputs to the diffusion model. Initializing as three pure noise planes, the paper uses a transformer-based architecture with cross-plane attention to enhance the 3D-awareness of the generation.

### Strengths
* The task of 3D generation, especially on large-scale open vocabulary datasets is challenging and well-motivated.
* The paper is elegantly written and easy to understand.
* Through ablation studies were done to justify its design choices.
* Evaluations were done with reasonable metrics using both older ShapeNet dataset, and new large-scale OmniObject3D. Large margin of improvements can be observed.

### Weaknesses
* The contribution of the paper mainly comes from its transformer-based architecture and combining existing tricks in designing such architectures. The overall workflow has been introduced and well studied by prior works such as [1] and [2].
* Upon the efforts of enhancing 3D-awareness of the generation, the rendered results still suffer from noisy geometry and texture details. It is not well-discussed what could be the source of these limitations.



[1] Shue, et al. 3d neural field generation using triplane diffusion, in CVPR, 2023.
[2] Chen, et al. Single-Stage Diffusion NeRF: A Unified Approach to 3D Generation and Reconstruction, in ICCV, 2023.

### Questions
None

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper aims at increasing robustness over a wide range of objects for 3D content generation. It uses tri-plane as a compact 3D representation. To fuse the information on three axis, it proposes to use cross attention, named 3D-aware transformer. Experiments on Omniobjects and ShapeNet show that the proposed method produce realistic results.

### Strengths
1. The generated 3D objects are realistic. The geometry is better than prior works.
2. Using cross-attention to achieve information fusing of tri-plane is interesting and also efficient in terms of 3D processing.
3. Directly training a 3D diffusion model is hard. The paper is one of the good start.

### Weaknesses
1. The paper lacks the introduction of the whole pipeline which links each module together and also the training pipeline which demonstrate which module is pre-trained and which is trained in each step. I am still confused how Step 1 and 2 are related, especially how the fitted tri-plane are used, or is it only the tri-plane decoder is used.
2. The improvement over GAN-based method is not obvious when the texture is on. They all seem realistic.
3. The time complexity should be analyzed, with comparisons over prior methods.

### Questions
See Weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
