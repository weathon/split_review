# JetFormer: An autoregressive generative model of raw images and text

- Decision: Accept
- Avg Score: 6.25
- Scores: 6, 6, 8, 5

## Abstract
Removing modeling constraints and unifying architectures across domains has been a key driver of the recent progress in training large multimodal models. However, most of these models still rely on many separately trained components such as modality-specific encoders and decoders. In this work, we further streamline joint generative modeling of images and text. We propose an autoregressive decoder-only transformer---JetFormer---which is trained to directly maximize the likelihood of raw data, without relying on any separately pretrained components, and can understand and generate both text and images. Specifically, we leverage a normalizing flow model to obtain a soft-token image representation that is jointly trained with an autoregressive multimodal transformer. The normalizing flow model serves as both an image encoder for perception tasks and an image decoder for image generation tasks during inference. JetFormer achieves text-to-image generation quality competitive with recent VQVAE- and VAE-based baselines. These baselines rely on pretrained image autoencoders, which are trained with a complex mixture of losses, including perceptual ones. At the same time, JetFormer demonstrates robust image understanding capabilities. To the best of our knowledge, JetFormer is the first model that is capable of generating high-fidelity images and producing strong log-likelihood bounds.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes JetFormer, an end-to-end autoregressive transformer designed for multimodal generation of text and images. JetFormer utilizes a normalizing flow to encode images into soft tokens, eliminating the need for pretrained encoders and enabling direct learning from raw data. The model’s unified structure for text and image processing enhances its multimodal adaptability, with additional techniques like a noise curriculum to improve image quality. JetFormer achieves competitive performance with state-of-the-art VAE-based models in tasks such as text-to-image generation and image captioning.

### Strengths
1. JetFormer processes text and images within a single autoregressive transformer, removing the need for modality-specific encoders and supporting seamless multimodal generation tasks.
2. JetFormer’s fully end-to-end training from raw data enables it to potentially learn task-specific representations, enhancing adaptability without relying on pre-trained embeddings.

### Weaknesses
1. The claim that pre-trained modality-specific encoders (e.g., VQ-VAE) limit performance due to task-agnostic design lacks sufficient quantitative or qualitative evidence to substantiate this limitation convincingly. The paper does not adequately demonstrate that the supposed limitations of pre-trained encoders are a significant bottleneck compared to other factors, such as the inherent challenges of multimodal learning or the specific architecture of the generative model. Without a direct comparison that isolates the impact of the encoder, it's difficult to accept this claim as a primary justification for the proposed end-to-end approach.
2. While end-to-end training in JetFormer may offer the advantage of learning task-specific latent representations, this approach could also introduce challenges in terms of training stability and computational cost. The paper does not provide a comparative analysis between end-to-end and two-stage methods (e.g., VAE-based embeddings followed by generative model training), leaving it unclear whether the benefits of end-to-end learning outweigh the potential costs and stability issues. Furthermore, the paper does not discuss the potential for overfitting when training both the encoder and decoder jointly, especially given the increased number of parameters and the complexity of the normalizing flow used for image encoding. The lack of ablation studies on the impact of different training strategies on the stability of the end-to-end approach is also a concern.
3. JetFormer’s approach of combining text and image modalities into a unified embedding space lacks clear justification. Without evidence of improved multi-task performance or multimodal synergy, it is unclear if a shared embedding space is necessary or beneficial for this model’s architecture. The paper does not explore whether separate embedding spaces for text and images, with a cross-attention mechanism, might be more effective or efficient. The potential for interference between modalities within a shared space is not addressed, and it is unclear if this approach is truly advantageous for multimodal generation tasks.

### Questions
(suggestion) To validate the advantages of JetFormer’s end-to-end learned image embeddings, additional experiments are needed to compare its performance against models using well-established VAE-based embeddings. Such comparative analysis would clarify whether JetFormer’s learned embeddings offer benefits over pre-trained embeddings in terms of image generation quality and task-specific adaptability.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper titled "JetFormer: An autoregressive generative model of raw images and text" presents a novel system designed for the understanding and generation of image-text data, with a particular focus on its performance on academic datasets. The model, JetFormer, is part of a broader category of large multimodal models trained on web data, and it shares similar ethical considerations, such as the need for de-biasing, safety-tuning, and the use of content filters to ensure safe deployment.

JetFormer is characterized by its end-to-end training approach, which, while computationally demanding, offers the potential for scalability and improved performance. However, the model currently faces limitations in visual quality compared to state-of-the-art diffusion models that utilize pretrained latent representations. Additionally, the computational requirements are significant, especially when dealing with high-resolution images, which necessitates efficient handling of image data, such as modeling at the patch level.

The paper also discusses a PCA-inspired variant to reduce redundant dimensions, which involves reshaping input data into sequences of flattened patches and applying a learnable, invertible linear map. This approach aims to manage the complexity of the data and improve the model's efficiency.

Overall, the contributions of the paper include the development of JetFormer, an exploration of its capabilities and limitations, and the proposal of methods to enhance its performance and safety in practical applications.

### Strengths
Originality: The paper introduces innovative techniques to enhance the quality of image generation models, particularly through the use of a novel noise curriculum and the factoring out of latent dimensions. The approach of factoring out redundant dimensions using a PCA-inspired variant before applying a flow model is a creative solution to improve model efficiency and performance. This originality is further demonstrated by the introduction of classifier-free guidance during sampling, which adds a unique aspect to the model's design.

Quality: The quality of the research is evident in the thorough experimentation and evaluation conducted. The paper employs robust evaluation metrics, such as the ADM FID evaluation suite and precision/recall metrics, to assess image sample quality on ImageNet1k. Additionally, the use of MS-COCO FID-30k for text-to-image tasks and the reporting of CIDEr scores for image captioning and VQAv2 accuracy for visual question answering further demonstrate the comprehensive nature of the quality assessment. The results indicate that the proposed enhancements significantly improve the quality of generated images.

Clarity: The paper is well-structured and clearly articulates the methodologies and findings. The explanation of the process of factoring out redundant dimensions and the subsequent impact on model performance is detailed and easy to follow. The use of visual aids or diagrams, if included, would further enhance the clarity of the presentation, but the textual explanation alone provides a solid understanding of the research contributions.

Significance: The significance of the paper lies in its potential impact on the field of image generation and understanding. By addressing the computational challenges associated with modeling images at the patch level and proposing solutions that reduce computational burden while maintaining or improving image quality, the research offers valuable insights and tools for future developments in the field. The ability to improve model quality for natural images and the implications for tasks such as zero-shot classification, image captioning, and visual question answering highlight the broad applicability and importance of the work.

### Weaknesses
Model Performance and Design Choices: The paper highlights several design choices that impact model performance, such as the use of dropout and PCA transforms. It notes that modeling images after PCA leads to worse results and that omitting noise curriculum results in significantly poorer outcomes. These observations suggest that the model's performance is sensitive to specific preprocessing and design choices, which may limit its robustness and generalizability. Specifically, the sensitivity to the noise curriculum is concerning, as it suggests the model may not be learning a robust underlying representation of the data but rather relying on a specific training regime. The fact that modeling after PCA performs worse indicates that the learned representation by PCA might not be suitable for the subsequent flow model, suggesting a potential mismatch in the feature space.

Factoring Dimensions: The paper discusses the impact of factoring out dimensions at different stages of the model. It finds that not factoring out dimensions after a flow model leads to quality loss, and while factoring out dimensions with a learnable linear mapping before the flow improves results, it still underperforms compared to post-flow factoring. This indicates a potential area for improvement in the model's architecture to optimize performance. The fact that post-flow factoring is superior suggests that the flow model might be learning some form of disentangled representation, and factoring dimensions before the flow might disrupt this process. The underperformance of pre-flow factoring, even with a learnable linear mapping, suggests that the mapping itself might not be optimal or that the flow model is more effective at learning the appropriate feature space for dimension reduction.

Lack of Comprehensive Evaluation: While the paper reports metrics based on the median of 10 runs and test-dev accuracy for VQAv2, it does not provide a thorough evaluation across diverse datasets or scenarios. A more extensive evaluation would help in understanding the model's strengths and limitations better. For example, the model's performance on datasets with different characteristics, such as those with more complex textures or different object distributions, is not explored. Furthermore, the evaluation of the model's robustness to adversarial attacks or noisy inputs is also missing, which are important aspects to consider for real-world applications.

### Questions
Please refer to the weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper proposes an end-to-end autoregressive model that can jointly understand and generate both image and text. The model consists of two components. A normalizing flow is applied to convert images into soft tokens for autoregressive modeling. The main backbone is a decoder-only transformer that predicts the next soft token. The paper explores two effective approaches to help model convergence. One is to introduce an evolving noise level during the training schedule. Another one is to dropout the redundant dimensions within the soft token when modeling the distribution auto-regressively. Experiments are conducted to evaluate the proposed method both quantitatively and qualitatively.

### Strengths
1. The paper is well-writen and is easy to follow.
2. The proposed method is innovative, showing a promising approach towards end-to-end image-text joint probabilistic modeling. It shows that it is possible to directly optimize NLL for potentially any modality.
3. The paper identifies two crucial training techniques to help the model converge better, which are crucial for the method's effectiveness.
4. Experiments are conducted sufficiently. It also shows the proposed method can potentially benefit from scaling up the model size.

### Weaknesses
1. In figure 3 of the paper, it seems that the noise curriculum makes the final NLL get slightly higher than without using the noise curriculum, but experimentally, the model clearly benefits from the noise curriculum training technique. Does this indicate that NLL may not be the best objective for image-text generation task? A more theoretical explanation is helpful for the readers to understand this phenomenon.
2. The detailed architecture of the normalizing flow model is not clearly explained. Better make it clear by showing diagrams of the model blocks and calculations.

### Questions
1. About information leakage. Since the image tokenizer is also trainable, it seems possible for the image tokenizer to attend to the next input token that the auto-regressive transformer should predict, i.e. the information of the next token is leaked into the input tokens, causing a trivial solution. Just wonder why this won't happen in Jetformer?

### Soundness
4

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
4

### Summary
This paper propose a generative model for generating text and images, it propose to use a normalizing flow model to simultaneously encode and decode images. The flow model generates soft token image representation that is jointly trained with an autoregressive decoder only transformer architecture. 

The main contribution of the paper is to first explore the usage of normalizing flow models as image tokenizers that can achieve an end-to-end training without the need to use a pretrained autoencoder for images.

### Strengths
- The paper is well written and easy to follow.

- The exploration of a normalizing flow model in vision language pretraining setting is an original and unexplored idea.

- The proposed method eliminate the needs to rely on pretrained components, by training the whole system end-to-end, the use of soft-tokens with normalizing flow is needed to avoid the mode collapse typical of VAEs.

### Weaknesses
 - The central claims of the paper are not supported by experimental results: The model performance on both text-to-image taskt is worse with respect to older and smaller models based on pretrained VQ-VAE (e.g MAGVLT [1]), while the improvement on understanding tasks is slight, training for image understanding greatly reduces the performance on image generation.

- The paper does not compare with recent baselines such as VAR models [2] for simple settings like ImageNet256 where VAR achieve 1.92 FID and Jetformer has 6.64 using the same training data and similar model size.

- Optimizing image tokens during training can add instability to the training dynamics, this is especially true in complex large scale multimodal settings. The paper does not provide sufficient analysis of the training stability, especially given the end-to-end nature of the approach, which could be more prone to instability compared to a two-stage approach with a fixed tokenizer.

- The main comparison to validate the usage of this modeling approach with respect to use a VQ-VAE in a controlled setting would be to compare it against a baseline, trained in the exact same setting  by substituting the normalizing flow with a VQ-VAE. The lack of this comparison makes it difficult to isolate the impact of the proposed tokenization method.

- How the approach scales is not clearly analized in the paper by just showing to models scales with relative low difference in parameters count

### Questions
- What do you think it is the main practical advantage of removing the pretrained image tokenizer for autoregressive image modeling?

- Recent papers as Transfusion [3] shows strong results by training with mixed modal corpus of data, a discussion on how this approach compare to your method would be beneficial. 

- Recent developments in image generation and deep learning guided compression shows that using a pretrained autoencoder to compress and reduce image dimensionality is really effective, moreover decoupling image tokenization from the generative training strategy can have some benefits in terms of training dynamics. What is your perspective on these considerations? 


[3] Transfusion: Predict the Next Token and Diffuse Images with One Multi-Modal Model. Zhou et al

### Soundness
2

### Presentation
3

### Contribution
2
