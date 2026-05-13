# Channel Vision Transformers: An Image Is Worth 1 x 16 x 16 Words

- Decision: Accept
- Scores: 5, 5, 8, 8

## Abstract
Vision Transformer (ViT) has emerged as a powerful architecture in the realm of modern computer vision. However, its application in certain imaging fields, such as microscopy and satellite imaging, presents unique challenges. In these domains, images often contain multiple channels, each carrying semantically distinct and independent information. Furthermore, the model must demonstrate robustness to sparsity in input channels, as they may not be densely available during training or testing. In this paper, we propose a modification to the ViT architecture that enhances reasoning across the input channels and introduce Hierarchical Channel Sampling (HCS) as an additional regularization technique to ensure robustness when only partial channels are presented during test time. Our proposed model, ChannelViT, constructs patch tokens independently from each input channel and utilizes a learnable channel embedding that is added to the patch tokens, similar to positional embeddings. We evaluate the performance of ChannelViT on ImageNet, JUMP-CP (microscopy cell imaging), and So2Sat (satellite imaging). Our results show that ChannelViT outperforms ViT on classification tasks and generalizes well, even when a subset of input channels is used during testing. Across our experiments, HCS proves to be a powerful regularizer, independent of the architecture employed, suggesting itself as a straightforward technique for robust ViT training. Lastly, we find that ChannelViT generalizes effectively even when there is limited access to all channels during training, highlighting its potential for multi-channel imaging under real-world conditions with sparse sensors.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
While the Vision Transformer has demonstrated robust performance with real-world images, its capacity to process multi-channel images, such as those from satellites, is somewhat constrained. To address this limitation, the authors have enhanced the conventional vision transformers by introducing a Hierarchical Channel Sampling (HCS) approach, which tackles the issue of sparse input channels. The proposed ChannelViT model has exhibited impressive results across three datasets, outperforming the traditional vision transformer.

### Strengths
+  The Hierarchical Channel Sampling (HCS) module enhances robustness by performing channel-wise sampling, which proves beneficial in scenarios involving incomplete image channels.
+  ChannelViT surpasses the conventional Vision Transformer (ViT) by demonstrating insensitivity to the number of input image channels, where ViT shows vulnerability.
+    A novel two-stage sampling algorithm is introduced within ChannelViT to selectively obscure input channels, optimizing the model's performance.

### Weaknesses
-    There is a potential risk of information loss, as highlighted in Section 3 of the methodology. The model's approach to segmenting the input image into various channel sequences and processing them individually could disrupt the alignment of channels, particularly in a 3-channel image prediction task. This is concerning because the spatial relationships between channels are crucial for many vision tasks, and independently processing them could lead to a loss of contextual information. The method of reassembling the channels after processing is not clearly defined, which raises concerns about how the model maintains spatial coherence.
-    The patch embedding technique described in Section 3.1 overlooks the issue of channel alignment when deconstructing images into separate channels. Specifically, the linear transformation applied to each channel independently does not account for the inherent correlations that exist between channels in a multi-channel image. This could result in suboptimal feature representations and limit the model's ability to learn meaningful cross-channel interactions.
-    The innovation of the proposed method warrants further scrutiny. Elements such as patch embedding, positional embedding, and Transformer Encoders, as discussed in Section 3.1, do not significantly diverge from the traditional Vision Transformer framework. These aspects should be acknowledged in the Related Work section, with a stronger emphasis on the unique contributions of this research. The core modification appears to be the separate processing of image channels, which, while effective, lacks substantial novelty in the context of existing transformer architectures.
-    The assertion in Section 3.2 that 'HCS guarantees equitable sampling across each m' lacks intuitive justification. While empirical results support this claim, a theoretical rationale would be beneficial. The method of uniformly sampling 'm' does not inherently guarantee that all possible channel combinations are equally represented during training, which could lead to biases in the model's learning process.

### Questions
-    Is HCS also employed during the testing phase? It was mentioned that HCS simulates a test-time distribution during training.
-    Regarding Table 2, when selecting channels for testing, are these chosen at random, or were all possible combinations tested? If it's the latter, could you provide the mean and standard deviation of the results?
-    Has the model's performance been evaluated on datasets with varying channel availability, where some data might have only partial channels while other portions are fully channeled?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work presents ChannelViT, a new ViT variant that: 1) learns a channel embedding for each channel, and 2) proposes a technique called Hierarchical Channel Sampling (HCS) for robustness to partial channels. Together, ChannelViT is reported to demonstrate better robustness to missing channels. Multiple experiments were performed, such as: 1) different model architectures (Channel variants of ViT-S/16 and ViT-S/8), 2) comparison with and without HCS, 3) comparisons across multiple benchmarks including microscopy imaging, 4) comparisons across varying number of channels available, 5) exploration into SSL compability in DINO, and others.

### Strengths
- ChannelViT with HCS proposes a simple but relatively intuitive extension of ViTs, which would have unique applications in multiplexed imaging in which not all "channels" (e.g. - fluorescent probes) are made available. Overall, this work presents a method that targets an important application and may enable significant biological / clinical findings in multiplexed imaging.
- The ablation experiments regarding assessment of partial channels, comparisons and baselines with training on single channels, and experimentation with DINO are thoughtful and well-organized. In particular, the assessment of partial channels and pretraining with DINO highlights its adaptability as a ViT in potentially replacing vanilla ViTs. Table 2 and Figure 4, which demonstrates the performances of Channel ViT (in comparison to vanilla ViT) on JUMP-CP with partial channels, demonstrates minor but consistent improvement.

### Weaknesses
 - While the main application of ChannelViT is in targeting problems such as those in multiplexed imaging due to the challenge of generalizing encoders across datasets that would have the same set of probes, only one dataset explored in this work is related to multiplexed imaging. Experimentation on ImageNet, C17-WILDS, and others are informative and appreciated, are not as relevant to the ultimate application that ChannelViT serves. Though C17-WILDS is microscopy, hematoxylin and eosin (H&E) pathology is not a domain where only the hematoxylin or eosin stains are performed. Rather, it would be more interesting to explore this problem on other relevant multiplexed imaging benchmarks such as RXRX1 [1], RXRX1-WILDS [2], TissueNet [3], and others [4-6]. To this end, it would also be useful to discuss and compare ChannelViT in context with label-free approaches, which suggest channel synthesis as a paradigm for addressing missing channels.
- As a drop-in replacement for ViT in conventional natural image classification or medical imaging tasks, one concern I have (raised in the work) is lack of experimentation on model scale. The title of this work, "Channel Vision Transformers: An Image Is Worth C x 16 x 16 Words", is similar to a title of a related seminal work in ViTs [7], but does not evaluate and demonstrates the scale of Channel ViTs in the same manner in demonstrating its universality of overtaking  current state-of-the-art architectures. As ViT-Small architectures are not the most commonly-used model size for ViT, it would be informative to explore Channel ViTs at greater scale (such as ViT-B and ViT-L). An additional limitation connected to this is the efficiency of learning channel embedings, which may have been the reason for not developing larger ViT models. As shown in the DINO experimentation, even with HCS, training is approximately 3.64x more expensive than its baseline comparison, which may limit its usability.
- I noticed that the results on ImageNet w/ ViT-S/16 DINO pretraining and linear probing (72.62% accuracy) are much lower than reported in the original DINO paper (77.0% accuracy). Performance for supervised ViT-S/16 (71.49% accuracy) is also much lower than what was reported in DINO (79.8% accuracy). With regularization, the performance of ViT-S/16 ranges from 76%-80% [1]. Likely, the linear probe evaluation of this work does not use recommended evaluation protocols for developing the supervised ViT-S/16 baseline, which undermines the authors claim on "ChannelViT not only surpasses the standard ViT in full-channel scenarios". Not considering suggested augmentation and regularization techniques may also harm comparisons with multi-channel evaluation.
- I acknowledge the author's comment on diversifying the evaluation of ChannelViT on different benchmarks (to not be specific to life sciences). However, the evaluation of C17-WILDS seems slightly out-of-place as despite being a microscopy imaging problem, it is ultimately not a multi-channel imaging problem unless one decides to separate the hematoxylin and eosin stains [2]. The channels do have distribution shift between the train and test set as a result of site-specific H&E stain intensity, but if choosing a microscopy benchmark from WILDS, why not evaluate RxRx1 which: 1) also has domain shift, and 2) is multi-channel? Overall, on choosing to evaluate tasks that showcase versatility and are out-of-domain of conventional natural image benchmarks, the reviewer thinks that the out-of-domain tasks could have been picked more appropriately to highlight ChannelViT's strengths.
- If choosing to evaluate on C17-WILDS, it is important to acknowledge existing baselines and leaderboards established that show +95% accuracy using ViT-B/16 [3] (though of little surprise as the baselines in [3] are with transfer learning). Coupled with the 1st point, the authors should contextualize their results with existing baselines, and clarify the experimental design around linear probing.

### Questions
Summarizing my above concerns, though this work would benefit from having additional experimentation related to its targeted application in multiplex imaging, such as:
- Additional evaluation on relevant datasets in multiplex imaging, such as RXRX1 and TissueNet
- Discussion and benchmark evaluation against label-free approaches in multiplex imaging
- Ablation experiments with ViT-B and ViT-L, with expanded discussion on the intended usage of ChannelViT w.r.t. efficiency

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper presents an extension of the Vision Transformer (ViT) architecture for image analysis domains with multi-channel information. This includes microscopy (fluorescence), and satellite (spectral) imaging, among others. The method consists of decoupling channels from the input and passing them as different tokens. To this end, the authors designed a learnable channel embedding and a hierarchical sampling method. As a result, a ChannelViT model learns to associate tokens in the space and channel dimensions, and is robust to channel drops.

### Strengths
* Well motivated paper. The problem of processing multi-channel images is important and the paper presents arguments to design methods that deal with this information effectively.
* The method is simple and effective. Splitting images in a sequence of tokens is an intuitive approach and the results show its effectiveness.
* Beyond tokenizing, an important aspect of the method is sampling channels strategically to learn their associations.
* The analysis in various datasets, including ImageNet, JUMP-CP and So2Sat, adds to the evidence that the method works in practice.
* Various ablations and extensive details presented in the manuscript and the appendix.
* The evaluation includes quantitative and qualitative results that show the benefits of the proposed approach.

### Weaknesses
Major comments:
* Limited baselines reported. The paper only considers ViTs as a baseline, which is a natural comparison given that the proposed method is an extension of this architecture. However, comparison to other architectures, especially CNNs to solve the multi-channel problems should be reported. This is specially important to appreciate the relative performance compared to other solutions tested before in multi-channel images. Specifically, the lack of comparison to established CNN architectures such as ResNet variants, which have demonstrated strong performance in various image analysis tasks, makes it difficult to assess the true novelty and effectiveness of the proposed method. The paper should also include comparisons to other transformer-based methods that have been adapted for multi-channel data.
* Computational cost increases quadratically with the number of channels. This problem is not addressed or commented in the main manuscript. According to the reported times in the appendix, the training cost increases linearly with the number of channels. The computational cost should be analyzed and discussed in more detail. While the solution seems effective, it can be prohibitive in practice. The quadratic complexity of the attention mechanism with respect to the number of tokens, which in this case includes channels, is a significant limitation that needs to be explicitly addressed. The authors should provide a detailed analysis of the computational cost with respect to the number of channels, including memory usage, and discuss potential strategies to mitigate this issue.
* In a similar note as the first point, other adaptations of ViTs have been reported for video analysis and 3D imaging, which also increase the image dimensions in a new axis (different than channels). Do any of these existing adaptations apply for channels? The authors should discuss how the proposed method relates to, and potentially differs from, existing ViT adaptations for handling multi-dimensional data, and justify why those methods are not directly applicable or do not perform as well for multi-channel image analysis. 
* The prediction of treatment in the JUMP-CP dataset is not necessarily a biologically relevant task. Prior literature makes the distinction that this is a pretext task for learning representations (weakly supervised learning), and not the main goal of analyzing these images. This clarification should be mentioned and prior work should be cited. Ideally, a biologically relevant task should be reported to ensure that classification performance in this pretext task is not dominated by confounders or spurious correlations. If this is not possible, an alternative test or explanation should be provided. The authors should provide a more thorough justification for using this task, and discuss the potential limitations of relying on a pretext task for evaluating the quality of learned representations. A more biologically relevant task, such as cell type classification or segmentation, could provide a better evaluation of the method's practical applicability.

Other comments:
* The results in Table 3 are based on a random selection of images with different numbers of channels (25%, etc). The reviewer assumes that the random partition is the same across experiments. The results should be repeated a few times with different partitions and standard deviations should be reported.

Minor comments:
* Figure 5 reports KRAS in the top row and KCNH76 in the bottom row, but the main text refers to them in the opposite order.
* Does figure 6 include error bars? Can you clarify how these were obtained?
* Minor typos: demonstrats, utiliz, involvs.

### Questions
* Can the authors report additional baselines and compare to other state-of-the-art methods in the same datasets that they evaluate? This could clarify the achievements of the method in context to prior art in these domains.
* Can the authors add computational analysis and comparisons to other methods for training / testing time of the methods? Even if the cost is a limitation, reporting and evaluating this aspect transparently can enhance the understanding of how useful this method can be in practice.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors propose a new tokenization scheme for Vision Transformer (ViT), where an input image is split into patches not only in spatial dimensions but also in channel dimensions. This may be beneficial for data where channels carry different semantical information, thus having little correlation, and might not always be present altogether in the data. Additionally to the tokenization scheme, the authors propose Hierarchical Channel Sampling (HCS) to regularize training, adapting the model to imperfect inputs.

### Strengths
* The proposed method outperforms the original ViT model in almost all considered experiments.
* The proposed regularization training scheme proves its efficiency against input channel dropout even for the original ViT.
* It is claimed that it is possible to increase explainability through attention map analysis with the new scheme. 
* The experimental base behind the work is diverse and extensive. Most authors’ statements are supported by an experiment or an ablation in the main section or the Appendix.
* The paper is easy to read and understand (illustrations, tables, etc.), and well-organized.

### Weaknesses
 * The novelty of the work is limited, as it seems that the channel splitting proposed in this paper is similar to a multi-modal approach to multi-channel data that has been explored earlier (albeit not with images). Also, HCS can be viewed as a modification of input channel dropout that has also been known before.
* The gains from the proposed approach are limited to the data with many channels (e.g., some microscopy images) and seem less reasonable for other types. At the same time, the processing with this new approach takes significantly more time.


### Questions
1. I suggest revisiting the title. The inspiration for the title used in this paper has clearly come from the ViT’s “An image is worth 16x16 words”. But in the case of ViT, it was about patches of size 16x16 across all channels, i.e., "Cx16x16", while the proposed approach uses "1x16x16" "words", as the image is split into channels as well. 
2. Please clarify why the proposed channel sampling is “hierarchical.”
3. It would be beneficial to review the notation used in the formulae, e.g. use AB instead of A\cdotB for matrix multiplication.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good
