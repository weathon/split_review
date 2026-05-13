# ControlAR: Controllable Image Generation with Autoregressive Models

- Decision: Accept
- Scores: 6, 8, 6, 5

## Abstract
Autoregressive (AR) models have reformulated image generation as \textit{next-token prediction}, demonstrating remarkable potential and emerging as strong competitors to diffusion models.
However, control-to-image generation, akin to ControlNet, remains largely unexplored within AR models.
Although a natural approach, inspired by advancements Large Language Models, is to tokenize control images into tokens and prefill them into the autoregressive model before decoding image tokens,
it still falls short in generation quality compared to ControlNet and suffers from inefficiency.
To this end, we introduce ControlAR, an efficient and effective framework for integrating spatial controls into autoregressive image generation models. Firstly, we explore control encoding for AR models and propose a lightweight control encoder to transform spatial inputs (\eg, canny edges or depth maps) into control tokens. 
Then ControlAR exploits the \textit{conditional decoding} method to generate the next image token conditioned on the per-token fusion between control and image tokens, similar to positional encodings.
Compared to prefilling tokens, using conditional decoding significantly strengthens the control capability of AR models but also maintains the model efficiency.
Furthermore, the proposed ControlAR surprisingly empowers AR models with arbitrary-resolution image generation via conditional decoding and the specific controls.
Extensive experiments can demonstrate the controllability of the proposed \name{} for the autoregressive control-to-image generation across diverse inputs, including edges, depths, and segmentation masks.
Furthermore, both quantitative and qualitative results indicate that \name{} surpasses previous state-of-the-art controllable diffusion models, \eg, ControlNet++.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces ControlAR, a method to efficiently enable controllability in autoregressive (AR) image generation models. ControlAR proposes a control encoder that transforms spatial control inputs (e.g., edges, depth maps, segmentation maps) into sequential control tokens, which are leveraged during conditional decoding to enable precise control over the generated images.

### Strengths
1. The proposed method enables fine-grained control in autoregressive image generation by using a control encoder and conditional decoding, achieving high image quality with low additional training cost.

2. This method provides effective resolution control, allowing AR models to overcome the limitations of fixed-resolution generation.

### Weaknesses
1.  Performance comparisons with recent models such as Lumina-mGPT and Cm3leon (or Anole), such as in segmentation-to-image tasks, would strengthen this paper. Additionally, an analysis or discussion on the potential for integration with these models would be beneficial.

2. Spatial conditions like segmentation maps and Canny edges impose strong constraints on structure diversity in generated outputs. Exploring whether some structural diversity can be incorporated within the conditional decoding step would be beneficial.

3. Need for discussion on representative failure cases. A discussion of representative failure cases among the generated results would provide valuable insights into the limitations of the proposed method and potential areas for improvement.

### Questions
Please see the Weaknesses

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
The paper presents a method to condition an autoregressive generative image model on different modalities, such as edges, depth, and others. The application formulation is very similar to ControlNet for diffusion models, but the method is novel for AR models. The proposed method consists in (1) generating patch embeddings for the conditioning input (2) adding those embeddings to the image embeddings in certain augmented layers in the AR model (3) processing the combined patches normally. The new layers are trained on a large dataset with conditioning inputs and the method achieves strong results.

### Strengths
The paper has several strengths that make it compelling:
The work has a very simple formulation that is elegant. There is good demonstration on how it’s better than the other obvious approach of conditional prefilling. Also, very few other work exists tackling this problem and this is, to the best of my knowledge, a novel approach for conditioning AR models. They also present class-to-image and T2I evaluations and show strong results on several datasets.

Also, this direction of research discovers essential knowledge for these new models, which we already have for diffusion models. And we can also see that ControlAR is smaller than a typical ControlNet. Further, the paper has good details on experimental setup, good  ablations, specifically some interesting ones on position+quantity of control layers.

### Weaknesses
I don't think I have found weaknesses in the work that should lead to rejection. I am curious about what would happen if certain experiments were run, and these are not very extensive. Some examples:
1. Which layers are ideal to introduce the new control layers on? Right now we have a coarse study of this but it could go deeper, although it's a lot of work that might not be super useful in the end.
2. Some output images shown in the paper show some color saturation or excess contrast - is this an effect of the control layers or just the base model? Is training the control layers biasing the model towards some unrealistic outputs?

### Questions
I think I am strongly decided for acceptance given the strengths of the paper. I'll read the other reviews in case I missed anything but currently don't have major questions. The paper presents a straightforward improvement that is necessary for these types of models and does a great job in presenting it, and in evaluating it.

### Soundness
4

### Presentation
4

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
The paper introduces ControlAR, a method for image-controlled autoregressive-based image generation. A ViT-based encoder is used to extract features from control images such as edge or depth maps, and a conditional decoding method (adding the control features and token features according to a fixed corresponding spatial relationship) is used to generate the output image. This paper has demonstrated good quantative and visualization results. This method also enables image generation at arbitrary resolutions according to the resolution of the control image.

### Strengths
- **Important topic**: The image-controlled generation task is in general of great interest, and important for the recently re-rised research trend on AR-based image generation models.
- **Simple and reasonable**: This method is a reasonable exploration towards controlled generation in image AR models with simple token feature addition in decoding.
- **Good ablations** on training strategy, fusion strategy (cross-attention or addition, addition layers), control encoders.
- **Good visualization results**.

### Weaknesses
I will put all questions in this section. Note that they're not all weaknesses.

1. **Equation (4) is not written properly**, here $q_i$ represents a discrete image token, then $q_i \in [V]$, where $V$ is the vocabulary or codebook size. Then, the summation of a discrete token with another continuous feature $q_i + C_{i+1}$ in Equation (4) is not well defined. Besides, ControlAR adds up the control feature to the token feature in three intermediate layers, not the input embedding.

2. **About the pathway choice**
    
    Throughout the paper and in Fig. 2, the authors argue that compared to putting control tokens in the sequence ("conditional prefilling"), ControlAR benefits from a shorter sequence length and eliminates the need for the model to learn a fixed one-to-one spatial mapping. This makes sense that ControlAR is a cheaper way to train a image-controlled AR generation model.

    However, I have some concerns about this path: ControlAR trains each controlled generation task separately, rather than offering a general model. Besides, the predefined one-to-one spatial mapping of ControlAR seems to be restricted to specific tasks. In contrast, putting control tokens in the sequence has the potential to support general generation of texts and images, and will allow flexible and diverse control relationships between them. For example, one might require image-controlled generation based on style rather than spatially local controls like edges or segmap; and one might require referencing multiple control images to generate a single output. 

    After all, if the goal is simply to achieve specific, local controls, well-established diffusion models and strategies are already very handy. One of the key motivations of the recent trend in exploring AR image generation models is to achieve a more general and flexible framework that can unify control and generation across modalities, right? I would like to know the authors' opinion on this.

3. **Lack some details and explanations**
    1. About the ablation on control encoders: What are the messages? Is vanilla training better or self-supervised training better for control feature extraction? It's not intuitive that we need different ViT models to extract features from control images for class-to-image and text-to-image generation. 
    2. For C2I, the authors initialize the control encoder with VIT-S. The original position encoding is global trainable and of fixed size, and is thus not suitable for multi-resolution. How do the authors handle this?
    3. Section 4.2 lacks detailed information on multi-resolution training. It would be helpful if the authors provided more details, such as the size of the multi-resolution dataset used for training, the design of the architecture (e.g., positional encoding) for multi-resolution adaptation, and so on.
    4. It would be beneficial if the author evaluate the text-image alignment.

4. **About resolution control**

    The paper saied ControlAR extend the ability of the autoregressive model to generate arbitrary resolution, making it "easy" to achieve any-resolution image generation without resolution-aware prompts. I have two questions and suggestions: (1) Can ControlAR or its extension enable resolution control when no specific control image like edge or seg map is available? If so, how? (2) Since both ControlAR and resolution-aware prompts require additional training, it is unclear if ControlAR actually offers a easy solution, despite the intuition tells us so. A quantitative or qualitative comparison with resolution-aware text prompts would strengthen this argument.

Minor: Typo: double "," in the 3rd contribution

### Questions
See the weakness section.

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
4

### Summary
This paper introduces ControlAR, a framework that enables autoregressive (AR) models to generate high-quality images with precise spatial controls.

### Strengths
1. The idea is simple but effective: a lightweight control encoder that transforms spatial inputs (edges, depth maps, etc.) into control tokens, and conditional decoding method that fuses control tokens with image tokens during generation. 

2. This work shows strong results across multiple tasks (edges, depth maps, segmentation).

### Weaknesses
1. The paper's efficiency comparison between ControlAR and ControlNet++ (22M vs 361M parameters) is misleading. Comparing parameter counts between diffusion-based and AR-based models is fundamentally unfair due to their different architectures and generation mechanisms. The paper should instead compare inference time, FLOPs, or other more relevant efficiency metrics between similar architectures.


2. The use of pretrained visual encoders (CLIP, DINOv2) is a standard practice in multimodal learning

3. The quantitative improvements shown in Tables 1 and 2 are marginal.

### Questions
see Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3
