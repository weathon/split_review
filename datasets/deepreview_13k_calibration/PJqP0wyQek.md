# MS-Diffusion: Multi-subject Zero-shot Image Personalization with Layout Guidance

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6, 6

## Abstract
Recent advancements in text-to-image generation models have dramatically enhanced the generation of photorealistic images from textual prompts, leading to an increased interest in personalized text-to-image applications, particularly in multi-subject scenarios. However, these advances are hindered by two main challenges: firstly, the need to accurately maintain the details of each referenced subject in accordance with the textual descriptions; and secondly, the difficulty in achieving a cohesive representation of multiple subjects in a single image without introducing inconsistencies. To address these concerns, our research introduces the MS-Diffusion framework for layout-guided zero-shot image personalization with multi-subjects. This innovative approach integrates grounding tokens with the feature resampler to maintain detail fidelity among subjects. With the layout guidance, MS-Diffusion further improves the cross-attention to adapt to the multi-subject inputs, ensuring that each subject condition acts on specific areas. The proposed multi-subject cross-attention orchestrates harmonious inter-subject compositions while preserving the control of texts. Comprehensive quantitative and qualitative experiments affirm that this method surpasses existing models in both image and text fidelity, promoting the development of personalized text-to-image generation.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces the MS-Diffusion framework, a layout-guided zero-shot image personalization approach for multi-subject scenarios. The author features a grounding resampler to enhance subject fidelity with semantic and positional priors and a novel cross-attention mechanism to ensure that each subject is represented in specific areas and facilitating the integration of multi-subject data while mitigating conflicts between text and image subject control.

### Strengths
- The paper is well-written and well-organized, presenting a clear and compelling motivation for the study.
- This method is the first to introduce layout-guided zero-shot image personalization for multi-subject scenarios.
- The paper showcases impressive qualitative results, particularly in layout control capabilities across both single- and multi-subject personalization, as well as in handling prompts with complex interactions among multiple subjects.

### Weaknesses
 - In Section 2.2, second paragraph, the sentence "Though past research in this field has significantly enhanced the ability to reference single subjects, few zero-shot multi-subject personalized models" is a bit unclear. I suggest rephrasing this sentence for clarity.

- In Section 3.1, as well as in the rest of the paper, it appears that the transpose notation (T) is missing for K in the equations of calculating attention maps.

- The paper does not provide sufficient detail on how the M-DINO metric is calculated, making it difficult to assess its validity for measuring multi-subject fidelity. It is unclear how the product of multi-subject DINO scores effectively captures subject neglect, and what specific thresholds or criteria are used to determine a significant drop in fidelity.


### Questions
- Could the authors provide a bit more detail on how the M-DINO metric is calculated and how it measures multi-subject fidelity?

- I came across a recent paper [1] on a similar task and recommend testing its evaluation metric on a few cases to see if it could be helpful for assessing multi-subject fidelity.

- The qualitative results presented are impressive, particularly in handling prompts with complex interactions among multiple subjects. Could the authors provide additional examples demonstrating these capabilities, as well as discuss any current limitations?

[1] Identity Decoupling for Multi-Subject Personalization of Text-to-Image Models (https://arxiv.org/pdf/2404.04243)

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
5

### Summary
This paper introduces MS-Diffusion, a zero-shot personalized image generation method for multiple subject entities. Given one or more reference subjects and the text prompt, the model generates high-quality target image based on the inputs accordingly, containing the subject following the desired text descriptions.
The main contribution of the paper is the proposal of integrating grounding information for multi-subject personalized generation, and a newly designed grounding resampler for incorporating the given grounding information. 
By training a SDXL model with the encourage modules on a large-scale private dataset, the algorithm yield favorable results compared to previous designs.

### Strengths
1. High-quality multi-subject personalized generation.
 2. The novel design of the grounding resampler provides extraordinary performance boost compared to previous baselines.

### Weaknesses
• Lack of baseline comparisons and limited contributions
        ◦ The author claimed that they are the first to incorporate grounding information for multiple subject image personalization, however, plenty of existing works have proposed similar designs, for example Subject Diffusion, where the layout is also determined by bounding boxes as cross attention regularizations, while there are no related in-depth discussions. The paper fails to adequately differentiate its approach from existing methods that also leverage spatial information for subject control, such as those using bounding box-based attention mechanisms. A more thorough comparison, including a discussion of the specific architectural differences and their impact on performance, is needed.
        ◦ The comparison with previous design on the benchmark is also limited. The evaluation lacks a comprehensive comparison against relevant state-of-the-art methods, making it difficult to assess the true novelty and effectiveness of the proposed approach. The choice of baselines seems arbitrary, and a more rigorous evaluation should include a wider range of methods, particularly those that also incorporate spatial control for multi-subject generation.

    • Limited performance boost
        ◦ In Table 2, the performance boost is rather trivial when comparing with SSR-Encoder on Multi-subject setting. Specifically, while SSR-encoder was trained based on SD1.5 and the proposed method is trained based on SDXL, the performance for is almost the same, except for a higher CLIP-T score. The marginal improvement in performance, especially considering the use of a more advanced base model (SDXL), raises concerns about the effectiveness of the proposed method. The fact that the performance is nearly identical to a model trained on an older base model (SD1.5) suggests that the gains might not be solely attributable to the proposed architecture.

### Questions
1. Comparing to method like Subject Diffusion and GLIGEN, what makes proposed layout control novel?
    2. In figure 2, the author proposed several limitation cases identified from previous methods, however, they are not further discussed or addressed in the following paragraphs, for example, how is subject overcontrol defined? It usually better to have some specific discussion to recall and address the problems mentioned in the introduction.
    3. On the multi-subject generation benchmark, the performance boost compared to the baseline SSR-encoder remains minimal, despite the proposed method being trained on a larger and more advanced base model (SDXL versus SD1.5). This outcome appears to serve as a counterexample, challenging the effectiveness of the proposed design.
    4. The seems to produce a higher CLIP-T scores (better text following) than previous methods, however, this performance boost might also come from the usage of SDXL where multiple text encoder is designed specifically for increase text adherence. Please justify this boost comes from the proposed model design rather than the base model.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes a zero-shot method for multi-subject personalization of text-to-image models. This is done through a pre-training phase where an adapter is trained to adapt a diffusion model on additional conditions derived from input images. In particular, the authors use 3.6M videos to extract two views of the same subject. Each training sample comprises segmented entities, their bounding boxes and a ground truth frame including all entities. 

The paper discusses mainly two design choices for their adapter, namely, a Grounded Resampler, and a Multi-Subject Cross Attention Layer. The grounded resampler is used to distill the subject-features through Preceiver like architecture. The authors propose to initialize the queries using entity word-embedding and bounding-box coordinates, to boost the localization of the sampling queries.

In addition, to avoid any information leakage between subjects, the authors use a Masked Cross attention where queries corresponding to a certain subject only attend the subject features.The proposed method also uses element-wise masking to avoid injected features from the reference images into background patches.

### Strengths
[1] The paper introduces a zero-shot multi-subject personalization method. 

[2] There are interesting components to the proposed method like the data-collection from video and the Grounding Resampler Unit. However I feel like more in-depth analysis and ablation should be carried out to validate that design choices considered are indeed important.

### Weaknesses
[1] The paper is hard to follow and some parts need further clarification. In particular, The “Multi-subject Cross Attention” section is not clear and needs major revision. The description lacks precise details on how the attention masks are constructed and applied, making it difficult to understand the mechanism for separating multiple subjects. It's unclear how the queries, keys, and values are specifically handled within this cross-attention module to achieve subject-specific attention. The paper would benefit from a more detailed, step-by-step explanation of the process, including the mathematical formulation of the attention mechanism and the masking strategy.

Lack of ablation on critical parts of the methods:

[2] Using videos for Data collection (e.g, in which ref. Image is different from gt. image) is claimed to be a key contribution. However, there’s a lack of ablation on how much this method helps the authors. The paper does not provide a clear comparison between training with video-derived data and training with static image pairs. This makes it difficult to assess the actual benefit of the proposed data collection strategy. A controlled experiment is needed to isolate the impact of using video data, by comparing performance with a dataset of static image pairs with similar content and diversity.

[3] In the Grounding Resampler; how important is the initialization (words+bounding box) to the module localization capability ? The paper mentions that the queries are initialized with word embeddings and bounding box features, but it is not clear how this initialization affects the resampler's ability to localize and extract subject features. It is also unclear how the bounding box features are encoded and integrated with the word embeddings. An ablation study is needed to evaluate the impact of this initialization, by comparing performance with random initialization or initialization with only word embeddings or bounding box features.

[4] Lacking qualitative samples of interesting use-cases such as - spatial relation (e.g, On-top) and object-interactions (e.g., two subjects playing tennis). The only interesting case I find in the paper is fitted to “virtual try-on” which could be a by-product of the training data.

### Questions
[1] L243-253: In the description of the cross-attention layers, in addition to the information injected from the text features, the authors show information that is injected from the reference image as well. In SD, the only features injected are those from the text. While injected image features through the cross-attention layers have been proposed (e.g, IP-Adapter), this wasn’t part of the original model. Please revise this section, and consider explicitly indicating the origin of the image features (f_i). 

[2] Grounding Resampler: the authors initialize the queries with word-embeddings and bounding-box Sinusoidal/Fourier features. But in another part of the text, the authors claim these embeddings are learnable. I am confused, is it learnable because of the query project-matrices ? Or do you pass the entity-word-embedding along with Bounding-Box features to another Projection matrix ? Can you please clarify this point.   Please provide a step-by-step explanation of how the queries are initialized and then updated during training, clearly stating which components are learnable and which are fixed.

[3] Do the results in Figure 4 correspond to the MS-Diffusion model before or after fine tuning on DreamBench ? Please clearly label all results in the paper to indicate whether they are from zero-shot or fine-tuned models.

[4] The Multi Subject Cross Attention module has been used (e.g, in ELITE). To my understanding, MSDiffusion only extends this to multi-subject use cases. Can you please highlight the differences ?

[5] It would be nice to provide dataset statistics. In particular, what percentage of the data there are multiple-subjects, excluding trivial cases like a person and clothes. At least from the qualitative samples, it looks like the model performs very well on clothing entities and a single subject. 

[6] Can you provide some information regarding the computational complexity of the method. In particular, it would be nice to report the additional overhead indeed by the method. Please report inference time and memory usage compared to baseline zero-shot models, for both single-subject and multi-subject generation tasks.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
Text-to-image generation models have advanced but face challenges in multi-subject scenarios. The MS-Diffusion framework is introduced to address these. It uses grounding tokens and feature resampler for detail, and layout guided cross-attention for location control. Experiments show it surpasses existing models in fidelity, promoting personalized text-to-image generation.

### Strengths
1.	The paper introduced the first layout-guided zero-shot image personalization with multiple subjects framework, which consolidates the accommodation of multiple subjects, the incorporation of zero-shot learning capabilities.

2.	The idea of decoupling and controlling the generation of the texture and position of the subject in the image is very reasonable.

3.	The paper is well written and easy to follow. The elaboration of the idea is very clear, and the framework of the structure diagram is also very easy to understand.

4.	The experiments are also very sufficient.

### Weaknesses
1.	The practice of controlling image generation through local cross attention is not innovative enough. It has been widely adopted in many existing layout-guided text-to-image generation methods. Specifically, the use of masked attention to control object placement is a common technique, and the paper does not sufficiently demonstrate a novel application of this mechanism. The method's reliance on local cross-attention for spatial control, while effective, lacks a significant departure from existing approaches.

2.	Judging from the quantitative and qualitative experimental results provided in the article, the improvement of image generation effect compared to existing methods is relatively limited. The gains in image quality and text alignment, while present, do not appear substantial enough to justify the complexity of the proposed framework. The quantitative metrics, while showing some improvement, do not convincingly demonstrate a significant leap in performance over existing state-of-the-art methods. The qualitative results also do not show a dramatic improvement in visual fidelity or text alignment.

3.	The extraction method of image features used by the grounding resampler proposed in the article has also been used in past papers, and its innovation is limited. The use of learnable query tokens for feature extraction, while effective, is not a novel contribution. The paper does not adequately justify why this specific approach is superior to other existing feature extraction techniques, and the grounding resampler's contribution seems incremental rather than transformative.

### Questions
1.	The grounding resampler proposed in the article also compresses image features. Why is it better than the image encoder used in existing methods? Can more qualitative analysis experiments be provided?

2.	The experiments in the article are based on Stable Diffusion XL. Now, newly emerging text-to-image diffusion models such as Flux inherently have better control over the generated content. Do these models not need an additionally trained structure to achieve satisfactory control?

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
5

### Summary
This paper proposes multiple subjects (MS-Diffusion) framework, which consolidates the accommodation of multiple subjects, the incorporation of zero-shot learning capabilities, the provision of layout guidance, and the preservation of the foundational model's parameters. 
MS-diffusion explicitly utilizes the layout information of the reference images to extract the information of multiple subjects separately to inject into the base model.

### Strengths
1.The authors alleviate the problem of combining natural objects in two thematic scenarios.
2.The framework is easy to think of and sensible.
3.The writing is clear and easy to understand.

### Weaknesses
1.Missing results for multiple topics (>2).
2.Missing results for comparison with paper [1].
3.The authors do not mention the Image encoder used.To the best of our knowledge, the Image encoder if it is a CLIP may lose the details of the themes, leading to the results in the last graph of Figure 4 and Figure 5.
4.From the CLIP-I scores in Table 2, it seems that text fidelity is not significantly improved.
5.How does it perform in scenes where the theme is people and anime? Especially the problem of combining people with anime characters.

### Questions
How does it perform in scenes where the theme is people and anime? Especially the problem of combining people with anime characters.

### Soundness
3

### Presentation
3

### Contribution
3
