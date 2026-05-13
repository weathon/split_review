# Discrete Inversion: A Controllable Latent Space for Multinomial Diffusion and Masked Generative Models

- Decision: Reject
- Scores: 3, 6, 8

## Abstract
Discrete diffusion models have achieved notable success in tasks like image generation and masked language modeling, yet they face limitations in controlled content editing. This paper introduces {\bf Discrete Inversion}, the first approach to enable precise inversion for discrete diffusion models, including multinomial diffusion and masked generative models. By recording noise sequences and masking patterns during the forward diffusion process, Discrete Inversion facilitates accurate reconstruction and controlled edits without the need for predefined masks or attention map manipulation. We demonstrate the effectiveness of our method across both image and text domains, evaluating it on models like VQ-Diffusion, Paella, and RoBERTa. Our results show that Discrete Inversion not only preserves high fidelity in the original data but also enables flexible and user-friendly editing in discrete spaces, significantly advancing the capabilities of discrete generative models.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper provides controlled editing of discrete diffusion models by discrete inversion.

Discrete inversion records transition sequences and masking patterns during the forward diffusion process.

For editing, the proposed method uses partial inversion and re-generation.

Experiments evaluate the proposed method on discrete image diffusion models and language diffusion models.

### Strengths
1. The problems and the solutions are clear and sound.
    1. inversion regarding discrete diffusion models -> DDPM inversion
    2. editing -> SDEdit-like partial inversion and generation
2. Evaluations are well-structured.

### Weaknesses
1. Recording-based approach is trivially adopted from DDPM inversion to discrete diffusion models: recording transitions and masks instead of noises. Please describe non-trivial differences due to problem settings such as discrete property.
2. Solving editing with partial inversion and re-generation is trivially adopted from SDEdit. Please describe non-trivial differences due to problem settings such as discrete property.
3. Analysis of the mutual information between z_t and x_0 is trivial: it decreases along t. Please describe non-trivial aspects of this tendency.
4. The choice of the competitor is not sound. Why should the masked inpainting be the competitor? In addition, DDIM + SD1.4 + P2P is outdated (2022). DDPM inversion (2024) should suffice.
5. Introduction wastes too much space on continuous diffusion models. It should better describe discrete diffusion models and masked generative models.
6. Section 3.2 contains too much details of previous methods.

### Questions
Questions are merged in the weaknesses because they are closely connected.

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
4

### Summary
This paper proposes an inversion approach, Discrete Inversion, for discrete diffusion models. By offering a faithful inversion method that enables edits for discretized models, they enable image and text editing without the need of manipulating the cross-attention maps, unlike many of the editing methods operating on continuous diffusion models. Instead of directly manipulating such features, Discrete Inversion proposes saving intermediate latents and masks during inversion and leveraging them during sampling. With the proposed inversion algorithm, authors empirically prove that accurate construction is guaranteed and address the editability of the inverted samples with additional hyperparameters, where each are ablated throughout the experiments provided.

Following a detailed description of the proposed algorithm, authors demonstrate the effectiveness of their method on both text and image modalities both in terms of editing and reconstruction performance. Over the experiments provided, authors present comparisons with continuous diffusion models for editing task and inpainting coupled with discrete diffusion models for image domain. For textual editing results, the experiments compare masked generation with the proposed approach by both assessing the model by RoBERTa itself (Accuracy and Textual Similarity) and by using ChatGPT as a classifier.

### Strengths
- Authors introduce Discrete Inversion, which serves as the first inversion method for masked diffusion models, which enables applications such as image editing with a pipeline different than inpainting based editing.
- The theoretical foundations of the proposed algorithm is expressed clearly.
- Editing and reconstruction performance of the proposed method is demonstrated with sufficient metrics that shows the effectiveness of the methods.
- In addition to the proposed inversion algorithm, authors propose a dataset for semantic editing on text which can be leveraged by future studies as a standardized benchmark.

### Weaknesses
 - The authors provide some claims that are now completely correct, which can be considered as over-generalization. Between lines 154-157, authors generalize the editing methods for diffusion models into two classes which are prompt-based editing with DDPM-based methods and cross-attention manipulation based methods with DDIM-based methods. Such approaches are not the only ways to perform semantic editing on images, whereas techniques like semantic guidance [1, 2] also exists which does not interfere with the main generation prompt and the cross-attention maps. Even though such approaches may not be suitable for comparisons, such claims should be corrected as it can be falsifying. If there is a specific reason that the authors only do consider cross-attention map manipulation based edits for continuous diffusion models, it should be explained clearly.
- $Cat(x;\pi)$ operator should be clarified before its first usage in line 181, as Eq. 1. This would improve readability of the proposed algorithm.
- For an accurate comparison between the approaches based on continuous diffusion models and masked generative models, the authors should expand the comparisons on Table 2 with mask based ControlNet[3]. This baseline can also simulate the effect of preserving unmasked regions (unedited regions). Such a comparison would be more reliable as it will operate on the same masked conditions, where continuous diffusion models by themselves do not have such restrictions in the way masked diffusion models have.

### Questions
- Authors should describe why they consider RoBERTa as a diffusion model. RoBERTa is not natively a diffusion model but a masked generative model. However, the model is described as a text discrete diffusion model in line 377. Please explain the relationship and the connection between the masked generative modeling and diffusion models explicitly, if you made any related assumption. 
- For clarity, authors should consider including a brief definition of the operator $Cat(x;\pi)$
- Additionally, authors are encouraged to reflect on the weaknesses mentioned both in terms of textual clarity and experiments that can result in a more robust baseline.
- Is there any reason why ControlNet is not included as a part of the comparisons? If there is a specific reason, please explain.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper presents Discrete Inversion, a novel approach for precise inversion in discrete diffusion models.It records noise sequences and masking patterns during forward diffusion.This enables accurate reconstruction and controlled edits without predefined masks or attention map manipulation.The paper demonstrates its effectiveness in both image and text domains.It evaluates the method on models like VQ-Diffusion, Paella, and RoBERTa.Results show high fidelity preservation of original data and flexible editing in discrete spaces.

### Strengths
- It seems no one has explored this direction, as far as I know.
- The paper is well-organized across its various sections.

### Weaknesses
 - It seems no one has explored this direction, as far as I know.
- The paper is well-organized across its various sections.

 - The method needs to cache every timestep, so the size is T×D×K. The token number D can be large, e.g., 32×32 in LDM, and K can be quite large too, e.g., 17K. Also, from the last paragraph of the paper on Discrete Flow Matching (Meta), the required timestep is normally larger than its counterpart in continuous space, which further exacerbates the extreme cache burden.
- A theoretical analysis should be provided to show that the inversion indeed makes sense.
- In Line 042, for flow matching, two papers from Michael Albergo are missing.
- Why not directly use categorical sampling instead of using the Gumbel-Softmax trick? maybe because categorical sampling is also inherently using SG trick? the author should make it clear.
- Why is there a minus sign, and what is the motivation in Eq7?
- The algorithm has a drastic issue: it is dependent on the seed. What if we change the seed? It seems the sampling trajectories will not align with the backward process.
- The paper itself feels rushed. I don't understand the details of Alg1 and Alg2. What are lambda1 and lambda2 used for?
- I have no idea why Remark 3.1 is necessary in this draft.
- It's surprising to see the inf result in Table 1, which means no stochastic events happen during the forward and backward processes. Also, I am confused about the difference between the second and third rows in Table 1.
- A basic introduction to RoBERTa is necessary for us to understand your experiment.
- How about if we change the masking schedule? Can it still achieve inversion and editing?
- No code is provided.

### Questions
As above

I will further increase my score if my concerns are fully resolved.

### Soundness
3

### Presentation
2

### Contribution
3
