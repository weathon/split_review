# EMMA: Empowering Multi-modal Mamba with Structural and Hierarchical Alignment

- Decision: Accept
- Avg Score: 5.75
- Scores: 5, 6, 6, 6

## Abstract
Mamba-based architectures have shown to be a promising new direction for deep learning models owing to their competitive performance and sub-quadratic deployment speed. However, current Mamba multi-modal large language models (MLLM) are insufficient in extracting visual features, leading to imbalanced cross-modal alignment between visual and textural latents, negatively impacting performance on multi-modal tasks. In this work, we propose \textbf{E}mpowering \textbf{M}ulti-modal \textbf{M}amba with Structural and Hierarchical \textbf{A}lignment (EMMA), which enables the MLLM to extract fine-grained visual information. Specifically, we propose a pixel-wise alignment module to autoregressively optimize the learning and processing of spatial image-level features along with textual tokens, enabling structural alignment at the image level. In addition, to prevent the degradation of visual information during the cross-model alignment process, we propose a multi-scale feature fusion (MFF) module to combine multi-scale visual features from intermediate layers, enabling hierarchical alignment at the feature level. Extensive experiments are conducted across a variety of multi-modal benchmarks. Our model shows lower latency than other Mamba-based MLLMs and is nearly four times faster than transformer-based MLLMs of similar scale during inference. Due to better cross-modal alignment, our model exhibits lower degrees of hallucination and enhanced sensitivity to visual details, which manifests in superior performance across diverse multi-modal benchmarks. Code will be provided.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
Mamba has seen widespread use in large language models (LLMs) due to its exceptional efficiency. However, Mamba struggles with processing visual signals, limiting its application in multi-modal LLMs. To address this issue, this paper proposes improving Mamba’s ability to handle visual signals through structural and hierarchical alignment. The authors argue that Mamba’s difficulty with visual data stems from the lack of positional encoding, which causes the gradual loss of fine-grained spatial information during processing. To mitigate this, the paper introduces the EMMA method, which enhances the structural consistency between Mamba’s output visual features and the original image by reconstructing the image through a decoder. Additionally, EMMA incorporates cross-attention within Mamba, combining multi-level intermediate features via cross-attention to form the final output, thereby preventing the loss of fine-grained details in deeper layers. The results show that EMMA leads to improved performance.

### Strengths
- The proposed method is simple yet effective.

### Weaknesses
1.  **Increased Complexity Due to Cross-Attention**:  
   EMMA introduces cross-attention operations into the Mamba network, reverting the model’s original sub-quadratic complexity back to quadratic complexity, which undermines the original intent of using Mamba. The authors should provide a detailed analysis of the computational complexity of the cross-attention operations, including the number of parameters and FLOPs, compared to the overall method. It is unclear if cross-attention is the most efficient method for fusing intermediate features. The authors should explore and compare simpler alternatives, such as linear attention or concatenation followed by a linear layer, to achieve the same goal while maintaining the efficiency of Mamba.

2.  **Training Costs and Fair Comparisons**:  
   EMMA involves additional training steps, specifically for the decoder and hierarchical alignment modules, which should be explicitly detailed in the paper, including the specific optimization algorithms, learning rates, and number of epochs used for each component. Furthermore, when comparing EMMA to other methods, the additional training costs should be listed separately to ensure a fair comparison (training time, GPU hours, memory requirement, and energy consumption). Since EMMA alters the original MLLM architecture by adding a decoder and multi-scale feature fusion, its inference complexity will also increase. Table 4 should include a breakdown of the increased complexity due to these additional components, including the number of parameters and FLOPs. For fairness, Table 4 should also provide EMMA’s inference speed when using Mamba LLM-2.8B, and compare this to the baseline Mamba model without the additional modules.

3.  **Limited Technical Contribution**:  
   EMMA’s approach is somewhat simplistic, as it primarily focuses on enhancing the consistency between deep and shallow features and the original image at the output stage. This method requires extra training, substantial computational resources, and introduces additional structures during deployment, which may not be practical for real-world applications. The technical contribution appears somewhat incremental, as it does not address the fundamental limitations of Mamba in processing visual data. It would be beneficial if this paper could provide a more in-depth analysis of how their method addresses specific challenges in multimodal learning that previous methods have struggled with, such as handling long-range dependencies in visual data or preserving fine-grained spatial information throughout the network.

### Questions
Please refer to the weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a Mamba based integration for vision-language models. Similar to the VLM based framework where there are one vision encoder, one projector, and one LLM. The proposed method takes one image and its corresponding caption as input, followed by multi-scale feature extraction and fusion. A pixel-wise alignment loss is applied to the visual features for structural visual cues preservation, and an autoregressive NLP loss is applied to the textural feature. Experiments are conducted on several benchmark datasets.

### Strengths
1. Pixel-wise alignment loss is interesting. The LLM outputs are text tokens and are further decoded into the image domain for measuring pixel-level similarity with the input image. 
2. The hierarchical alignment via multi-scale fusion is developed to retain fine-grained visual features
3. The experimental results seem promising on the benchmark datasets.

### Weaknesses
1. While the main contribution is set for the loss design of model training, the proposed loss function seems rather general and not specifically for Mamba based structure. The general pixel-wise alignment loss seems functional for all VLMs, rather than only mamba structure. Can you clarify how the proposed loss function leverages or is tailored to the unique properties of Mamba architectures compared to transformer-based VLMs? It's unclear if the pixel-wise alignment loss is truly exploiting Mamba's strengths or if it's a generic technique applicable to any VLM architecture. The paper needs to articulate how the specific characteristics of Mamba, such as its selective state space mechanism, are being leveraged by this loss function, rather than just stating it's used with Mamba.
2. The inputs require both images and captions, how the captions are acquired are not illustrated well. A more detailed description of the data preparation process is desired here. Also, the decoded procedure via Mamba is not illustrated clearly. Is SFT or a similar finetuning process still needed for training VLM? Is related VQA data still required? Such technical details are not shown clearly in the manuscript to show the overall model tuning picture.  It is better to provide a step-by-step explanation of the decoding procedure and clarification on the fine-tuning process to help address the ambiguity. The paper lacks a clear explanation of how the model is trained, specifically whether it uses a standard supervised fine-tuning (SFT) approach or requires additional VQA data. The decoding process, particularly how the Mamba architecture is used to generate the pixel-level output, is also not well-defined.
3. The pixel-alignment loss is set for structure preservation, the role of LLM here is not clear as the caption has been sent to it. So LLM seems to function as a single mapping to fulfill this objective loss. Can you elaborate on the specific role of the LLM in the context of the pixel-alignment loss? It's not clear why the LLM is necessary for the pixel-alignment loss, as the caption is already provided. It seems the LLM is just acting as a mapping function, and the paper needs to clarify how the LLM's language modeling capabilities are integrated into the pixel-alignment process.
4. Feature fusion is not motivated well and seems a general operation for representation enhancement. It would be better to provide a more detailed justification for the choice of feature fusion technique. Specifically, an explanation is expected of how your approach differs from or improves upon standard feature fusion methods, particularly in the context of Mamba-based architectures. The paper does not adequately justify the choice of feature fusion, and it appears to be a generic technique for representation enhancement. The paper needs to explain how the chosen feature fusion method is specifically tailored for Mamba architectures and how it differs from or improves upon existing fusion methods.

### Questions
Overall, the pixel-alignment loss design is interesting but there are many ambiguious technical details to make the contribution clear. Further clarification is required to better position the proposed method within the scope of the visual instruction tuning design of VLMs

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
4

### Summary
The paper introduces Empowering Multi-modal Mamba with Structural and Hierarchical Alignment (EMMA), enhancing Mamba multi-modal large language models (MLLM) by improving their ability to extract fine-grained visual information. EMMA uses a pixel-wise alignment module for better structural alignment and a multi-scale feature fusion (MFF) module to maintain visual information during cross-modal alignment. Extensive experiments demonstrate that EMMA achieves lower latency and faster performance compared to other Mamba-based MLLMs, with superior cross-modal alignment and reduced hallucination. The code for this model will be made available.

### Strengths
1. Well Written: The paper is clearly articulated, making the complex concepts accessible and easy to understand for the reader.

2. Motivation Well Clarified: The authors firstly identify the imbalance in the quality of visual and textual latent features in MLLM Mamba models. They propose a pixel-wise alignment approach to autoregressively enhance the learning and processing of structured visual features, leading to improved cross-modal alignment between visual and textual latents.

3. Experiments Solid: The paper presents comprehensive experiments conducted on a variety of multi-modal benchmarks. These experiments include thorough comparisons with current state-of-the-art models based on both Mamba and transformer architectures, demonstrating the robustness of the proposed approach.

### Weaknesses
1. Why is there an imbalance in the quality of visual and textual latents in the Mamba LLM, where coarse visual features are ineffectively aligned with higher-quality textual features? How does this differ from transformer-based models? Do transformer-based models face the same issue? Specifically, what architectural differences in Mamba contribute to this imbalance, and how do these differences manifest in the learned feature representations compared to transformer models? Is this imbalance more pronounced in Mamba models, and if so, why?

2. Could you provide a more objective, quantitative analysis of the loss of fine-grained visual cues in the LLM, as the current visualizations with just a few images seem insufficient? Is this phenomenon common across MLLMs, or is it specific to the use of the Mamba LLM? What specific metrics could be used to quantify the loss of fine-grained details in the visual feature maps, and how do these metrics correlate with the observed performance degradation? Is this loss of fine-grained information a general issue with MLLMs or is it exacerbated by the Mamba architecture?

3. Why do the current results show that the Mamba LLM still lags behind the transformer architecture? In this case, does the speed advantage gained by using the Mamba architecture sufficiently compensate for the performance loss? What specific factors contribute to the performance gap between Mamba and transformer-based MLLMs, and how do these factors interact with the speed advantages of Mamba? Is the trade-off between speed and performance justified in the context of the specific tasks and datasets used in the experiments?

### Questions
1. Currently, models use ViT as the image encoder. Is it possible to build an MLLM entirely based on Mamba? What potential advantages and challenges might this approach entail?

2. In transformer-based LLMs, is there a similar issue with pixel-level alignment? Would the method proposed in the paper also be applicable to transformer architectures?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
Mamba-based architectures are promising for deep learning models but current Mamba multi-modal large language models (MLLM) are insufficient in extracting visual features. This paper proposes Empowering Multi-modal Mamba with Structural and Hierarchical Alignment (EMMA). It includes a pixel-wise alignment module for structural alignment at the image level to extract fine-grained visual information autoregressively. Additionally, a multi-scale feature fusion (MFF) module is proposed for hierarchical alignment at the feature level to prevent the degradation of visual information. Extensive experiments on various multi-modal benchmarks show that the model has lower latency than other Mamba-based MLLMs and is nearly four times faster than transformer-based MLLMs of similar scale during inference.

### Strengths
1. The imbalance in the quality of visual and texture latent in the Mamba-based VLM does make sense to investigate and this paper proposes an effective method, named Empowering Multi-modal Mamba with Structural and Hierarchical Alignment (EMMA) to solve this problem.

2. The experiments are sufficient to verify the effectiveness of the proposed method.

3. The paper is well-written and easy to follow.

### Weaknesses
1. EMMA essentially enhances the visual representation ability of the model. Therefore, the comparison with peers should be conducted, e.g. the contrastive learning in CLIP and SigLIP. Specifically, it would be beneficial to see experiments where the pixel-wise alignment loss is replaced with the contrastive loss used in CLIP or SigLIP, keeping other components of the method unchanged, to isolate the impact of the proposed loss. Besides, does the masked image construction loss achieve a function similar to EMMA?

2. EMMA uses the visual features from the vision encoder as the target of the Pixel-wise Alignment Loss. However, visual features from the vision encoder may lose the fine-grained information. Does this problem affect the performance of EMMA?

3. High-resolution image is an important direction for MLLM. Structural constraints on the high-resolution visual features are an interesting point to discuss. Authors are suggested to conduct the experiment under a high-resolution setting.

4. Authors are suggested to display more qualitative results.

### Questions
Please see the weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3
