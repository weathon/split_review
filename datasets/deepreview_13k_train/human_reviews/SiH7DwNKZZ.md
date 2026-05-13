# Vision-LSTM: xLSTM as Generic Vision Backbone

- Decision: Accept
- Scores: 6, 6, 6, 5, 5

## Abstract
Transformers are widely used as generic backbones in computer vision, despite initially introduced for natural language processing. Recently, the Long Short-Term Memory (LSTM) has been extended to a scalable and performant architecture -- the xLSTM -- which overcomes long-standing LSTM limitations via exponential gating and parallelizable matrix memory structure. In this report, we introduce Vision-LSTM (ViL), an adaption of the xLSTM building blocks to computer vision. ViL comprises a stack of xLSTM blocks where odd blocks process the sequence of patch tokens from top to bottom while even blocks go from bottom to top.
Experiments show that ViL holds promise to be further deployed as new generic backbone for computer vision architectures. \\
Project page: \url{https://nx-ai.io/vision-lstm/}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper introduces VIsion-LSTM, a novel general-purpose vision backbone building on top of xLSTM. The proposed ViL models show good visual understanding performance in various tasks (e.g., image classification, semantic segmentation) and exhibit superior inference speed over Vision Transformer and Vision Mamba.

### Strengths
1. It's interesting to try transfering different language models into vision. As Tranformer has shown a very successful adaptation in computer vision and Mamba has recently been introduced into various vision tasks, showing comparable performance, validating the similar effect of LSTM can provide many insights to the community.

2. The performance is good. xLSTM shows competitve results in classification and semantic segmentation.

3. The detailed ablations of architectural design are interesting and can inspire future works.

### Weaknesses
1. On the ImageNet-1k classification task, the model seems not to scale well. The ViL-Base underperforms DeiT-III by a large margin. Is this caused by a technical reason (e.g., insufficient hyper-parameter search) or the limitation of LSTM's learning capacity? Can ViL scale to a larger size?

2. In the main tables of the paper, the authors emphasize comparing the models' FLOPs as a measure of speed, which may not be a fair comparison between recurrent models and transformers. Typically, at the same FLOPs or inference speed, recurrent models train significantly slower than transformers. Did the authors provide a direct comparison of speed during the training stage?

3. Some considerable performance improments come from the 2D convolution.

### Questions
Is ViL a plain architecture or involving feature downsampling operations? It is not clearly disscussed in the paper.

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
This paper applies the recently proposed language model architecture xLSTM to the field of computer vision, and the proposed backbone is named Vision-LSTM (ViL). The image is firstly separated into patch tokens as in ViT, then ViL applies xLSTM module to image tokens in the bidirectional order since the image is non-causal data. This paper compares ViL with other vision backbones (ViT, DeiT, etc.) in three vision tasks, including classification, semantic segmentaion and transfer learning, where the experiments show that ViL achieves strong performances and also demonstrates a good trade-off between performance and computations.

### Strengths
1. The proposed ViL display xLSTM also performs well in visual feature encoding and can be considered a strong candidate for a universal visual backbone.
2. Extensive experiments are conducted to verify the strong performance of ViL on three vision tasks.

### Weaknesses
1. The technical contribution is limited: the proposed ViL is a simple adaptation of xLSTM blocks to vision tasks. Although it contains some necessary modifications for processing non-causal image data (bidirectional flip, conv2d, etc.), it is still straightforward. 
2. Lack of experiments to prove the main advantages of ViL: compared with transformers, the ViL has linear complexity. But the experiments do not provide enough evidence to show this advantage. For example, the mentioned lack of an optimized hardware implementation could also be a potential and important technical contribution for ViL (a prototype implementation should also be a good contribution). Adding an ablation study to demonstrate the effectiveness of ViL for processing higher-resolution / using larger models should also be a good choice. 
3. The writing can be further improved and the paper should be self-contained: Section 2.1 lists lots of equations about mLSTM, but they are not used. Actually, the introduction of mLSTM is also difficult to understand with these equations and limited text. Additionally, the paper length is a little shorter than 10 pages.

### Questions
For semantic sementation task, does ViL use feature pyramid and how to implement it?

Please also refer to the weakness section, especially for the second and third points.

### Soundness
3

### Presentation
2

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
This work bringing the advantages of LSTM to computer vision to build a new vision backbone with linear complexity.  Previous vision backbone such as Vision Transformer and  VIsion Mamba have challenges in the computational complexity of processing high-resolution image tasks, so this work extends LSTM by extending the gating and parallelizable matrix memory structure to address long-standing limitations. The proposed backbone Vision LSTM (ViL) is validated in image classification, semantic segementation etc.

### Strengths
1.  The new attemption of new linear vision backbone is great.
2.  This work has detailed experimental setup in classification, transfer learning and segmentation. ViL performs well on ImageNet accuracy, ADE20K mIoU and VTAB-1K accuracy.

### Weaknesses
1. Because of the good training receipt (data augmentation, optimization method etc.), it is not difficult to get good performance to train a new vision backbone. My main concern is how to validate the scaling law of a new backbone, namely the proposed ViL.  

2. The largest model size of ViL is 89M and 115M (ViL-B), so how to validate the performance still can keep spurious with larger model size.

3. The training and inference latency of ViL, compared with ViM and ViT, is also a concern. As LSTM is non-parallel compared with Transformer, inference latency would be a very important problem.

### Questions
Please refer to the weaknesses.

### Soundness
2

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
3

### Summary
This paper introduces Vision-LSTM (ViL), a novel generic backbone for computer vision tasks that adapts the recently proposed xLSTM architecture to vision. ViL processes images by splitting them into patches and processing sequences of patch tokens using alternating xLSTM blocks. Odd blocks process the sequence from top-left to bottom-right, while even blocks process it from bottom-right to top-left. The key advantage of ViL is its linear computational and memory complexity with respect to sequence length, which makes it more efficient than Transformers for high-resolution images. The authors conduct experiments on ImageNet-1K classification, ADE20K semantic segmentation, and VTAB-1K transfer learning tasks, showing that ViL achieves competitive or superior performance compared to Vision Transformers (ViT), Vision Mamba (Vim), and other recent architectures. They also provide ablation studies on architectural design choices and discuss limitations and future work.

### Strengths
Originality: The paper presents a novel adaptation of the xLSTM architecture to computer vision tasks, which is a creative application of recent advancements in sequence modeling to vision.

Quality: The experimental evaluation is thorough, including comparisons with strong baselines on standard benchmarks (ImageNet-1K, ADE20K, VTAB-1K). The authors also perform ablation studies to justify architectural choices.

Significance: The proposed ViL architecture offers linear computational and memory complexity with respect to sequence length, addressing a key limitation of Transformers (quadratic complexity) in high-resolution image tasks. This has potential implications for scaling vision models to higher resolutions.

Clarity: The paper is well-written and clearly explains the methodology, experiments, and results. The figures and tables are informative and enhance understanding.

### Weaknesses
Practical Implementation: The lack of an optimized hardware implementation of the mLSTM limits the practical runtime performance of ViL compared to ViTs, which benefit from highly optimized libraries. This may hinder immediate adoption of ViL in real-world applications.

Scope of Experiments: While the experiments are comprehensive for the given datasets, the evaluation is limited to ImageNet-1K and related benchmarks. Larger-scale pre-training on datasets like ImageNet-21K or JFT-300M could strengthen the claims and demonstrate scalability.

Limited Exploration of Extensions: The paper mentions potential future work such as self-supervised pre-training and hierarchical architectures but does not explore these avenues. Including preliminary results or discussions on these topics could enhance the paper's contribution.

Technical Limitations Affecting Design Choices: Some architectural design choices, such as limiting traversal directions due to technical constraints (lack of optimized implementations), suggest that the current version of ViL may not be fully optimized from a methodological standpoint.

### Questions
Could the authors compare against transformers under wall clock time instead of FLOPs?
Could the authors provide more details on the potential for optimized hardware implementations of the mLSTM, and how this might impact practical runtimes compared to ViTs? Are there any ongoing efforts in this direction?
Have the authors considered applying ViL to larger-scale datasets or tasks that particularly benefit from high-resolution inputs, such as medical imaging or video understanding? How do they anticipate ViL would perform in these settings?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents a new vision backbone based on Extended Long Short-Term Memory (xLSTM), which is first proposed in NLP domain. The model ViL consists of a linear projection, a list of mLSTM blocks, and a prediction head. In each mLSTM block, the image feature patches go through a recurrent process with modified LSTM nodes. The model can be configured using a chunkwise mode to enable efficient parallel processing. The experiments show the proposed model achieve competitive performance on several vision tasks: imageNet classification, semantic segmentation, and transfer learning.

### Strengths
-	The proposed framework is clean and straightforward. 
-	The model achieves competitive performance on classification, segmentation, and transfer learning comparing to existing models vision transformer, vision-mamba and ConvNeXt.
-	On segmentation tasks, it is able to outperform existing methods with lower FLOPs, due to the efficiency of the recurrent processing on high image resolutions.

### Weaknesses
 - The overall novelty of the work is limited. The framework is directly adapted from xLSTM in NLP. The benefit on parallel inference is also directly inherited from the xLSTM framework. The reviewer would like to see some modifications to the original framework to make the model more suitable for the image-domain tasks, such as incorporating image priors or efficient message passing. The current approach lacks a clear demonstration of how the recurrent structure is specifically advantageous for image processing beyond what the original xLSTM provides for sequence data. The modifications made, such as the backward traversal, seem incremental rather than fundamental changes that exploit the 2D image structure.
- In figure 3, it seems the performance of ViL saturates faster than ViT models. On ImageNet, it is worse than DeiT-III on large-size settings. Not sure the scalability of this work if the model size gets even larger. In Table 1, ViL-B is also not as good as Mamba-B. More results on larger models is referred to make the experiments stronger. The performance saturation observed in Figure 3 raises concerns about the model's ability to scale effectively with increased data and model size, which is a critical aspect for modern vision backbones. The lack of competitive performance compared to DeiT-III and Mamba-B, even with smaller models, suggests that the model may not be fully optimized for image classification tasks.
- There are no latency numbers on CPU/GPUs for ViL. Such numbers are critical for new vision backbones. The absence of concrete latency measurements on standard hardware platforms makes it difficult to assess the practical applicability of the proposed model. While FLOPs provide a theoretical measure of computational cost, they do not always translate directly to real-world performance, especially given the potential for hardware-specific optimizations.

### Questions
What is the memory consumption / latency of the xLSTM compared to vision mamba? Does it have any advantage?

### Soundness
3

### Presentation
2

### Contribution
2
