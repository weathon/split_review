# Segment Anything with Multiple Modalities

- Decision: Reject
- Avg Score: 5.67
- Scores: 5, 6, 6

## Abstract
\footnotetext{* Co-first authors with equal contributions. $^\dagger$ Co-corresponding authors.}
Robust and accurate segmentation of scenes has become one core functionality in various visual recognition and navigation tasks. This has inspired the recent development of Segment Anything Model (SAM), a foundation model for general mask segmentation. However, SAM is largely tailored for single-modal RGB images, limiting its applicability to multi-modal data captured with widely-adopted sensor suites, such as LiDAR plus RGB, depth plus RGB, thermal plus RGB, etc. We develop MM-SAM, an extension and expansion of SAM that supports cross-modal and multi-modal processing for robust and enhanced segmentation with different sensor suites. MM-SAM features two key designs, namely, unsupervised cross-modal transfer and weakly-supervised multi-modal fusion, enabling label-efficient and parameter-efficient adaptation toward various sensor modalities. It addresses three main challenges: 1) adaptation toward diverse non-RGB sensors for single-modal processing, 2) synergistic processing of multi-modal data via sensor fusion, and 3) mask-free training for different downstream tasks. Extensive experiments show that MM-SAM consistently outperforms SAM by large margins, demonstrating its effectiveness and robustness across various sensors and data modalities. Project page: \url{https://xiaoaoran.io/projects/MM-SAM}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
In this article, the author extends SAM from a single RGB modality to a multimodal approach. To achieve this, they designed three key modules: (1) a fine-tuned image encoder to process X-modal data, aligning its encoded features with those of RGB data and effectively utilizing SAM's pre-trained mask and prompt encoders; (2) a selective layer for efficient fusion of encoded features from different modalities; and (3) the use of multimodal pseudo-labels to optimize network parameters, equipping the model with the ability to extend effectively to multimodal tasks. Experimental results demonstrate the effectiveness of the proposed design.

### Strengths
1.This work is the first to extend SAM from single-modal to multi-modal data.

2.The experiments are comprehensive, and the fine-tuned model contributes valuable insights for advancing the field.

3.The modules designed by the author effectively leverage SAM's existing capabilities, and the fine-tuned model demonstrates promising zero-shot potential.

### Weaknesses
1.The modules proposed by the authors are derived from prior work, which may limit the originality of this study.

LoRA does not appear to be a novel technology. The low-rank technology is first proposed in 2021:

[1] Hu, Edward J., et al. "Lora: Low-rank adaptation of large language models." arXiv preprint arXiv:2106.09685 (2021).

And, it has been widely used across NLP and CV fields. The related works about combination of SAM and LoRA:

[2] Lu, Xiaoyan, and Qihao Weng. "Multi-LoRA Fine-Tuned Segment Anything Model for Urban Man-Made Object Extraction." IEEE Transactions on Geoscience and Remote Sensing (2024).

[3] Cai, Lingcong, et al. "Towards Cross-Domain Single Blood Cell Image Classification Via Large-Scale Lora-Based Segment Anything Model." 2024 IEEE International Symposium on Biomedical Imaging (ISBI). IEEE, 2024.

The SFG is seems like a adaptive features fusion module and the similar idea has been used in many fields, for examples:

[1] Li, Xiangtai, et al. "Gated fully fusion for semantic segmentation." Proceedings of the AAAI conference on artificial intelligence. Vol. 34. No. 07. 2020.

[2] Li, Yang, et al. "Self-attention enhanced selective gate with entity-aware embedding for distantly supervised relation extraction." Proceedings of the AAAI conference on artificial intelligence. Vol. 34. No. 05. 2020.

[3] Chen, Xiaokang, et al. "Bi-directional cross-modality feature propagation with separation-and-aggregation gate for RGB-D semantic segmentation." European conference on computer vision. Cham: Springer International Publishing, 2020.

Please detail the difference between the propose methods and the above.

2.The impact of the selective layer is unclear due to a lack of ablation studies. Will the results be greatly affected by removing the SFG module?

3.SAM’s performance on uncommon data distributions (e.g., remote sensing and earth observation data) tends to be limited. Relying 
s solely on pseudo labels without manual annotation could constrain the effectiveness of MM-SAM. Please provide additional experiments or analysis specifically on these uncommon data distributions.

4.The methodology lacks details on how the model fuses single-modal mask predictions \(M_I\) and \(M_X\) from RGB and X-modal data. Please provide the details about fusion algorithm or method description.

### Questions
See weakness.

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
MM-SAM expands the capabilities of the SAM to work with multi-modal data from sensor suites, enabling segmentation of data from diverse sensors, both individually and in combination. MM-SAM achieves this by adapting SAM's image encoder, which was originally trained on RGB images, to effectively handle other modalities, such as depth, thermal, LiDAR, and hyperspectral data. 

The framework addresses three main challenges: adapting SAM to diverse non-RGB sensors, fusing data from multiple sensors, and enabling mask-free training. To overcome these challenges, MM-SAM introduces two modules: Unsupervised Cross-Modal Transfer (UCMT) and Weakly-supervised Multi-Modal Fusion (WMMF).

UCMT incorporates a modal-specific patch embedding module and parameter-efficient tuning using LoRA within SAM's image encoder. This allows MM-SAM to extract features unique to each sensor modality while keeping the number of added parameters low. A crucial part of UCMT is the embedding unification loss, which aligns the embeddings of different modalities within the output latent space of SAM's image encoder. 

WMMF introduces a lightweight selective fusion gate to adaptively fuse multi-modal embeddings. This gate dynamically adjusts the weighting of embeddings from different modalities, effectively using the strengths of each sensor in diverse situations. 

Extensive experiments on seven datasets demonstrate MM-SAM's effectiveness.

### Strengths
1. Pioneering Work: MM-SAM is the first study to extend visual foundation models, specifically SAM, for use with data from multiple sensor suites. 

2. Simplicity and Efficiency: MM-SAM is designed to be technically straightforward, using relatively simple modules like UCMT and WMMF for adaptation. This simplicity makes it easier to understand and implement. 

3. Label-Free Adaptation: MM-SAM can adapt to different sensors without requiring mask annotations. It significantly reduces the effort and cost associated with data annotation.

4. Robustness and Versatility: MM-SAM shows superior effectiveness across a wide range of sensor modalities and diverse scene types. This broad applicability makes MM-SAM a valuable tool for various downstream tasks.

5. Shared Latent Space: The output latent space of SAM's RGB image encoder can be effectively shared across different sensor modalities. This shared space allows MM-SAM to generate modality-specific embeddings that are still compatible with the other components of SAM (the prompt encoder and mask decoder), leading to effective cross-modal segmentation. The shared latent space also simplifies multi-modal fusion, allowing for adaptive weighting of embeddings from different sensors.

6. Strong Empirical Results: Extensive experiments across a diverse range of datasets and sensor modalities provide compelling evidence for MM-SAM's effectiveness.

### Weaknesses
1. Lack of Novelty in Individual Techniques: While the combination and application of these techniques to adapt SAM for multi-modal data might be novel, the lack of groundbreaking innovation in the individual methods could be seen as a weakness. 

2. Limited Comparison with Segmentation-Specific Methods: The experiments primarily compare MM-SAM with SAM and SAM 2, without comparing it to other state-of-the-art methods specifically designed for segmentation tasks, particularly those tailored for specific modalities. For example, on SemanticKITTI, existing LiDAR-specific algorithms can achieve higher mIOU (2DPASS 72.9) on single-mode data without additional training data compared to MM-SAM's performance of 66.4.

### Questions
Please refer to the weakness.

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
4

### Summary
The paper focuses on extending the foundation model SAM to support other modalities. By inheriting the segmentation priors, MM-SAM achieves remarkable zero-shot performance.

### Strengths
1. The MM-SAM is trained in an unsupervised manner with the potential to be easily extended to new modalities and applied to many downstream tasks.

2. MM-SAM supports the multi-modality inference, the segmentation results look good.

3. The method is simple and easy to follow.

### Weaknesses
1. Missing training details, please refer to Questions.

2. The UCMT and WMMF lack significant insight, the pseudo-label based training is a typical way in unsupervised and weakly supervised learning.

### Questions
1. The SAM demands a prompt input, how to obtain the prompt as input during training? And how about prompt input during inference?

2. If trained MM-SAM is an all-in-one model? Each modality maintains an independent image encoder LoRA?

3. In my understanding, MM-SAM is trained with single or paired modalities, it can be generalized to multi-modality input during inference, is it right? What is the relation with Imagebind? [1]

[1] ImageBind: One Embedding Space To Bind Them All

### Soundness
3

### Presentation
3

### Contribution
2
