# AnyText: Multilingual Visual Text Generation and Editing

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 8, 6, 6

## Abstract
Diffusion model based Text-to-Image has achieved impressive achievements recently. Although current technology for synthesizing images is highly advanced and capable of generating images with high fidelity, it is still possible to give the show away when focusing on the text area in the generated image, as synthesized text often contains blurred, unreadable, or incorrect characters, making visual text generation one of the most challenging issues in this field. To address this issue, we introduce \textbf{AnyText}, a diffusion-based multilingual visual text generation and editing model, that focuses on rendering accurate and coherent text in the image. AnyText comprises a diffusion pipeline with two primary elements: an auxiliary latent module and a text embedding module. The former uses inputs like text glyph, position, and masked image to generate latent features for text generation or editing. The latter employs an OCR model for encoding stroke data as embeddings, which blend with image caption embeddings from the tokenizer to generate texts that seamlessly integrate with the background. We employed text-control diffusion loss and text perceptual loss for training to further enhance writing accuracy. AnyText can write characters in multiple languages, to the best of our knowledge, this is the first work to address multilingual visual text generation. It is worth mentioning that AnyText can be plugged into existing diffusion models from the community for rendering or editing text accurately. After conducting extensive evaluation experiments, our method has outperformed all other approaches by a significant margin.
Additionally, we contribute the first large-scale multilingual text images dataset, \textbf{AnyWord-3M}, containing 3 million image-text pairs with OCR annotations in multiple languages. Based on AnyWord-3M dataset, we propose AnyText-benchmark for the evaluation of visual text generation accuracy and quality.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents an adapter-based module that can be plugged into existing diffusion models to perform multilingual visual text generation and editing. It contains a control net to control the text location and text content and a special text embedding module to improve the multilingual text generation ability. This paper also presents a large-scale multilingual text image dataset, AnyWord-3M, with image-text pairs and OCR annotations in multiple languages.

### Strengths
1. The proposed adapter-based module is a plug-and-play module that can guide visual text generation of many existing pre-trained diffusion models and can apply to multiple languages, which was not achieved in previous works.
2. The proposed text adapter and text encoder are proven to be effective in improving the OCR performance.
3. The proposed AnyWord-3M dataset is the first large-scale text image dataset with multilingual OCR annotations and is useful for future study.

### Weaknesses
1. The method and dataset collection miss a lot of details. For example, is the linear projection layer trained or fixed for ocr encoder in the text embedding module? 
2. A lot of information is not presented in the examples shown in the paper, for example, the layouts for images in Figure 1, and the captions for images in Figure 5.
3. The tight position mask annotation process for the AnyWord-3M dataset is unclear. It is not specified whether the position masks are generated from OCR bounding boxes or from human annotations. If they are from OCR, it is unclear how the model handles irregular text regions, since most OCR models output rectangular bounding boxes rather than tight polygon masks. If they are from human annotation, the scale and cost of such annotation is not discussed.

### Questions
I have some questions about the model architecture, dataset construction, and experiment design.

For the model architecture:
1. Which feature is extracted from PP-OCR to serve as text embedding?
2. Is the linear projection layer for the OCR encoder trained?
3. What is the configuration for the fuse layer? A single convolution layer or a stacked convotion? 
4. What is the input to text controlnet? Based on Figure 2, it seems to be the concatenation of $z_a$ and $z_t$.
5. Why is the image resolution for glyph image 1024x1024 instead of 512x512? This does not align with the final image resolution.

For the dataset construction:
1. How is the tight position mask $l_p$ annotated? As far as I know, the PP-OCR model does not support arbitrary shape text detection.
2. The glyph image $l_g$ contains rotated text; how is the bounding box annotated from the position mask?
3. The captions are generated using BLIP-2 model instead of the original captions. Could authors provide some statistics like the length of the captions and show some example captions for images in AnyWord-3M? How does this difference affect the model performance?

For the experiment:
1. Could authors provide more information about the input for the visual examples? For example, the layouts for Figures 1, 6, 8, 12, the captions for Figures 5, 10, 11.
2. The Sen. ACC and NED metric is measured using the same OCR model as the encoder in model training, which might be unsuitable. Could authors evaluate the OCR performance using another OCR model?
3. Table 3 shows the improvement brought by visual text embedding in Chinese text generation. I wonder if this also improves the English word generation.
4. In the experiment, the text diffuser model is not trained on the same dataset as GlyphControl and AnyText Model. Is it possible that authors fine-tune them on the same data and compare final performance?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The manuscript unfolds AnyText, a profound diffusion-based multilingual visual text generation and editing model. It meticulously tackles the intricacies involved in precise text portrayal within generated images, deploying auxiliary latent modules and text embedding modules as strategic tools. To augment the training phase, the introduction of text-control diffusion loss and text perceptual loss is articulated, which serves to bolster text generation quality. A formidable performer, AnyText triumphs over existing paradigms, championing improved accuracy and quality in text generation. Furthermore, the introduction of a novel dataset, AnyWord-3M, enriches the existing reservoir of multilingual image-text pairs, reflecting a thoughtful contribution to the scholarly community.

### Strengths
(1) A notable innovation lies in the paper's strategic approach to circumvent challenges, ensuring precise text portrayal within generated images.

(2) The infusion of auxiliary latent modules coupled with text embedding modules acts as a catalyst, promoting enhanced accuracy and coherence in the text generation process.

(3) Strategic incorporation of text-control diffusion loss and text perceptual loss during training heralds improvement in the overall text generation quality.

(4) A commendable addition is the introduction of AnyWord-3M, a robust dataset enriched with 3 million image-text pairs, elaborately annotated with OCR in multiple languages, signifying a valuable asset to the research fraternity.

### Weaknesses
(1) The architecture seems somewhat reliant on pre-established technologies such as Latent/Stable Diffusion and ControlNet, which slightly shadows its novelty.

(2) Encumbered by a complex array of components and a multi-stage training regimen, the model’s re-implementation emerges as a challenging task, compounded further by numerous critical hyperparameters requiring manual assignment.

(3) Certain aspects, such as token replacement, require a more elaborate discourse for clearer comprehension, primarily concerning the identification of corresponding tokens and their subsequent utility in text-image generation.

(4) There exists a potential ambiguity concerning the intermediate generative results (x'_0), where the possible presence of noise or blur could compromise the precision of perceptual loss computation.

(5) A clearer depiction of computational resource demands (GPU Hours), beyond the ambiguity of epochs, would enhance the paper’s practicability and replicability.

(6) A more explicit elucidation on the operational synergy between Z_a from the Auxiliary Latent Module and Z_0 from VAE, as depicted in Fig. 2, alongside their application within Text-ControlNet, would augment the manuscript's clarity.

### Questions
N/A

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces modules to enhance the text-drawing capabilities of text-to-image diffusion models. The auxiliary latent module embeds glyph and position information obtained from an off-the-shelf OCR module and fuses these latents as diffusion-step invariant conditions through ControlNet. Additionally, the text embedding module encodes a tokenized prompt, replacing the tokens of rendered glyphs with special tokens. Since these special tokens, the components of the auxiliary latent module, and ControlNet are the only trainable parts in the entire model, this method can be readily applied to existing diffusion models without retraining the diffusion UNet. The modules are trained on the AnyWord-3M dataset, also proposed in this paper. The performance of the proposed method surpasses that of previous text-generation-focused text-to-image diffusion models and also offers multilingual text generation capabilities.

### Strengths
Generating text glyphs properly in images produced by text-to-image diffusion models has been a longstanding issue. Research has shown that this capability can be improved by increasing data and model size, but this is somewhat obvious or expected. Following ControlNet, which proposes controllability for Diffusion UNet, the text glyph generation problem can be solved; however, as shown in this paper, it would result in a monotonous style. One of the paper's strengths is that the generated glyphs harmonize with the content of the generated images and are not monotonous. Additionally, the paper's ability to handle multilingual text glyph generation with relatively less data is another notable strength.

### Weaknesses
As revealed in the ablation study, the most significant performance improvement of this method occurs upon the introduction of text embedding. This is attributed to the performance of PP-OCRv3. If one were not to use the OCR module's embedding and instead employ a general image encoder like the CLIP visual encoder, it is questionable whether the same level of performance improvement would have been achieved. Specifically, the paper lacks a thorough investigation into the impact of different visual encoders on the text generation quality. Furthermore, many modules are added to the vanilla text-to-image diffusion model, but the paper fails to mention the computational overhead that arises as a result. Although the paper highlights multilingual capabilities and provides qualitative results for Korean and Japanese in the figures, it is disappointing that these two languages are excluded from the quantitative results, falling under the "others" category. Moreover, the evaluation is limited by the lack of a comprehensive analysis of the model's performance across diverse scripts and character complexities. Furthermore, it is regrettable that the results of the ablation study are listed only in terms of Chinese sentence accuracy and NED, without any FID measurements. The lack of qualitative results corresponding to each ablation experiment is also a drawback. The ablation study should have included a more comprehensive set of metrics to assess the impact of each module on both text generation and overall image quality.

### Questions
I'd like to pose questions that can address the weaknesses discussed.

1. Could you elaborate on how the PP-OCRv3's performance specifically influences the results?
2. Have you considered measuring the computational overhead when additional modules are integrated into the vanilla text-to-image diffusion model?
3. Why were Korean and Japanese languages included in the qualitative results but not in the quantitative ones?
4. Is there a reason why FID measurements were not included in the ablation study?
5. Why were qualitative results not provided for each individual ablation experiment?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposed AnyText, a diffusion-based multilingual visual text generation and editing model. It combines auxiliary latent model which is a control net for text condition, and a text embedding module which injects text visual information in the prompt latent space. Text-control diffusion loss and text perceptual loss are using in training. A large-scale multilingual text images dataset, AnyWord-3M, is introduced.

### Strengths
- extended control net for text input condition
- new visual text token embedded in the prompt 
- introduced OCR related perceptual loss
- new dataset
- new state-of-the-art under proposed new evaluation benchmark

### Weaknesses
 - using models trained own dataset to compare with previous baselines is not so fair
- the requirement of user given text mask is not always easy in practice.
- It is unclear if the performance gains are solely due to the proposed model architecture or if the training data contributes significantly. The ablation study does not fully isolate the impact of the dataset from the model's architecture. The comparison with existing methods is further complicated by the fact that these methods were trained on different datasets, making it difficult to attribute the improved results to the proposed method alone.
- The necessity of providing a ground truth text mask during evaluation is a limitation. This requirement is not practical in real-world scenarios where such masks are not readily available. The paper does not adequately explore the model's performance when using predicted or noisy text masks, which would be more representative of real-world applications.

### Questions
- It is not clear whether the improved results come from better training data or the proposed model. It would be best to compare the baseline models trained on the same dataset, or train the proposed model on the previous LAION glyph subset.
- in the experiments, the ground truth text mask is used as conditional input. It would be interesting to see what if random text position and mask is used, can it still generate reasonable image?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
