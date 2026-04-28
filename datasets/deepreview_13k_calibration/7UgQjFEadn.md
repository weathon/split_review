# Modality-Specialized Synergizers for Interleaved Vision-Language Generalists

- Decision: Accept
- Avg Score: 5.75
- Scores: 5, 6, 6, 6

## Abstract
Recent advancements in Vision-Language Models (VLMs) have led to the emergence of Vision-Language Generalists (VLGs) capable of understanding and generating both text and images. However, seamlessly generating an arbitrary sequence of text and images remains a challenging task for the current VLGs. One primary limitation lies in applying a unified architecture and the same set of parameters to simultaneously model discrete text tokens and continuous image features. Recent works attempt to tackle this fundamental problem by introducing modality-aware expert models. However, they employ identical architectures to process both text and images, disregarding the intrinsic inductive biases in these two modalities. In this work, we introduce Modality-Specialized Synergizers (MoSS), a novel design that efficiently optimizes existing unified architectures of VLGs with modality-specialized adaptation layers, i.e., a Convolutional LoRA for modeling the local priors of image patches and a Linear LoRA for processing sequential text. This design enables more effective modeling of modality-specific features while maintaining the strong cross-modal integration gained from pretraining. In addition, to improve the instruction-following capability on interleaved text-and-image generation, we introduce LeafInstruct, the first open-sourced interleaved instruction tuning dataset comprising 184,982 high-quality instances on more than 10 diverse domains. Extensive experiments show that VLGs integrated with MoSS achieve state-of-the-art performance, significantly surpassing baseline VLGs in complex interleaved generation tasks. Furthermore, our method exhibits strong generalizability on different VLGs.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper aims to improve the understanding ability of existing Vision-Language Generalists (VLGs) and propose the Modality-Specialized Synergizers (MoSS). Moss focuses on two things: 1) To build high-quality interleaved text and images, Moss modifies the connectors (such as the Linear layers between the image encoder and LLMs) in VLGs) by introducing a linear LoRA (for textual inputs) and Convolutional LoRA (For image inputs). 2) To improve the understanding of perform interleaved tasks. MoSS develops a high-quality instruction dataset (with 184,982 instances). Experiment results show the improvements of the introduced two LoRAs and ablations show the efficiency of the convolutional LoRA.

### Strengths
1) This paper is written well with clear figures and tables, which make the readers easy to follow the story.

2) The ideas that utilize model-specific adapter to process the text and image make sense to me. Such adapter may capture inherent semantics of corresponding inputs.

3) This paper develops a high-quality interleaved instruction dataset, which will benefit to the VLG community.

4) Experiments and ablations show the improvements and efficiency of the proposed modules

### Weaknesses
1) One of the core concerns is the novelty of the two LoRA types. Given the facts that both Linear LoRA and convolutional LoRA are not new to recent vision-language models, the contributions are limited. Specifically, the application of linear LoRA to text and convolutional LoRA to image inputs, while intuitive, lacks significant novelty as these techniques are already established in the field. The paper does not adequately demonstrate a novel adaptation or insight in their usage within the VLG context.

2) Technically, MoSS believes that the linear layer could lose the visual information and adopts the convolution LoRA to capture local patch features. However, the ViT-based image encoder in EMU (ViT are often used in VLMs) already flattens an image into a token sequence and employs self-attention to model their dependencies. That is, the ViT outputs inherently contain the local information, and the linear adapter acts as a semantic translator that maps the visual features into LLM space. Thus, the necessity of the convolutional LoRA for VLG is questionable, particularly given that self-attention mechanisms are already capable of capturing both local and global dependencies. The argument that linear layers lose visual information is not well-supported, especially considering the capabilities of ViT architectures.

3) MoSS argues that previous methods use the same framework for both text and image. If we consider the model-specific encoder and the shared adapter as a whole module, we find that they already use different frameworks to process the text and image. The claim of a unified framework in previous methods is not entirely accurate, as most VLMs already employ distinct encoders for different modalities. The core issue is not the framework, but rather the modality-specific adaptation within the shared LLM component, which is not clearly addressed by the proposed approach.

4) Can the authors apply MoSS to more powerful models, such as Emu 3, to test its robustness? The current evaluation is limited to Emu2 and Chameleon, which may not fully demonstrate the generalizability of MoSS to more advanced models. Testing on more recent and powerful models is crucial to validate the effectiveness of the proposed method in a broader context.

### Questions
Please see the Weaknesses section.

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
3

### Summary
This paper proposes a new modality-specialized training method called MOSS and an instruction-turning dataset for interleaved text-and-image generation. By adopting MOSS on two existing frameworks, they show improvements on an interleaved evaluation benchmark (InterleavedBench).

### Strengths
1. This paper proposed a novel design that enhances VLGs to generate interleaved content with modality-specialized parameters and adaptation architectures.
2. This paper introduces an open-sourced large-scale instruction-tuning dataset that allows interleaved multi-image and text input and output.

### Weaknesses
1. The proposed convolutional LoRA (Equation 4) is similar to the LoRA proposed in [1]. The authors claim that their new LoRA could alleviate the information loss, yet no experimental comparison between the two kinds of Conv LoRAs is provided. It is unclear how the specific modifications in Equation 4, such as the choice of kernel sizes or the application of the convolution to the full-rank feature map, contribute to the claimed improvement. A detailed ablation study is needed to justify the design choices of this ConvLoRA.
2. The evaluation is limited.
    1. They only evaluate on InterleavedBench and an image editing benchmark called MagicBrush. The coverage of the evaluation is relatively small. 
    2. Since the proposed model can do both image and text generation, more benchmarks could be included to measure the model performance from different perspective. E.g., multimodal understanding benchmarks like MMMU, MathVista, VQAv2, POPE. image generation benchmarks such as GenEval and T2I-CompBench. The absence of these standard benchmarks makes it difficult to assess the generalizability of the proposed method.
3. For the proposed data:
    1. The automatic data annotation pipeline  mentioned in Line 298 is not elaborated. How did the authors acquire LeafInstruct from existing academic dataset?  The lack of detail makes it hard to reproduce the dataset or assess its quality. Specifically, the process of converting existing datasets into the interleaved format is unclear. 
    2. According to Line 299, the details of dataset construction are shown in Table 3. I cannot find any construction details in Table 3. This inconsistency between the text and the table makes it difficult to understand how the dataset was created.
4. This paper is not well organized and written. Some reference (such as the above table reference) is not accurate. This may cause it is not easy to read and understand. The inaccurate referencing and lack of clarity in the writing hinder the comprehension of the proposed method and its evaluation.
5. The improvements are relatively limited. Adding MOSS only gets the open-source state-of-the-art performance on 3/5 metric. Adding MOSS onto Chameleon even causes text quality drop. Did the authors have hypnosis or investigate these results? The fact that the proposed method does not consistently improve performance across all metrics raises concerns about its robustness and general applicability. The drop in text quality when applied to Chameleon is particularly concerning and requires further investigation.
6. No qualitative results of Chameleon-MOSS.

### Questions
Please see above.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper examines the intrinsic inductive biases present in vision and language modalities in VLGs. It introduces MoSS, a novel approach that optimizes existing unified VLG architectures through modality-specialized adaptation layers—ConvLora for capturing local priors in image patches and LinearLora for handling sequential text. Additionally, the paper presents LeafInstruct, an open-source interleaved instruction tuning dataset. Experimental results demonstrate that MoSS enhances VLG model performance.

### Strengths
1. The paper proposes a novel idea that parameters for processing information of different modalities in VLGs should be trained with different strategies.
2. The proposed MoSS method brings promising enhancement in model performance of VLGs.

### Weaknesses
1. The performance improvement shown in Table 1 is inconsistent, with Chameleon displaying a decline in text quality after training with MoSS.

2. It remains unclear whether the observed performance enhancements are attributable to the MoSS training method or the LeafInstruct dataset (see Questions).

3. The parameters of ConvLora cannot be merged into the original parameters, as convolution is not linear. This limitation may lead to increased computational costs during inference.

### Questions
I wonder whether the results for the four middle rows in Table 1 reflect the model's original performance or its performance after full-parameter fine-tuning on LeafInstruct. Did you try full-parameter fine-tuning using your constructed data? Or full-parameter fine-tuning with two different sets of parameters for image and text tokens?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work aims to enhance the interleaved text-image generation capabilities of VLGs. The authors note that current VLGs use the same architecture for processing and generating both text and images, which may not adequately capture the distinct inductive biases inherent to each modality. To address this, they propose the Modality-Specialized Synergizers (MOSS), introducing modality-specific parameters within a unified model architecture. Specifically, they integrate convolutional LoRA for image processing and Linear LoRA for text processing.

### Strengths
1. This work proposes to address the distinct inductive biases of each modality by using specialized LoRA parameters.
2. The proposed method is intuitive and straightforward.
3. A new high-quality interleaved instruction tuning dataset with 184,982 instances covering over 10 domains is introduced.
4. The study conducts experiments on two different VLG backbones with both discrete and continuous image token spaces.

### Weaknesses
1. There are existing works focusing on interleaved image-text generation that the authors have overlooked, such as [1-3]. These works are not included in the experimental comparisons.

     [1] MM-Interleaved: Interleaved Image-Text Generation via Multi-modal Feature Synchronizer    
     [2] OpenLEAF: Open-Domain Interleaved Image-Text Generation and Evaluation    
     [3] Anole: An Open, Autoregressive and Native Multimodal Models for Interleaved Image-Text Generation    

2. In Figure 1, the authors only show the performance of continuous embedding-based VLGs for interleaved text-image generation. What about discrete-based VLGs?

### Questions
1. Could the authors elaborate on why, even after fine-tuning with interleaved text-image data, a unified model is still unable to capture modality-specific inductive biases?

2. What is the relationship between the capability for interleaved image-text generation and the use of discrete tokens versus continuous embeddings? Which approach holds a distinct advantage?

### Soundness
3

### Presentation
3

### Contribution
3
