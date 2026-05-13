# Sparse Refinement for Efficient High-Resolution Semantic Segmentation

- Decision: Reject
- Scores: 6, 5, 6, 5

## Abstract
Semantic segmentation empowers numerous real-world applications, such as autonomous driving and augmented/mixed reality. These applications often operate on high-resolution images (\eg, 8 megapixels) to capture the fine details. However, this comes at the cost of considerable computational complexity, hindering the deployment in latency-sensitive scenarios. In this paper, we introduce \textbf{SparseRefine}, a novel approach that enhances \textit{dense low-resolution} predictions with \textit{sparse high-resolution} refinements. Based on coarse low-resolution outputs, SparseRefine first uses an entropy selector to identify a sparse set of pixels with high entropy. It then employs a \textit{sparse} feature extractor to efficiently generate the refinements for those pixels of interest. Finally, it leverages a gated ensembler to apply these sparse refinements to the initial coarse predictions. SparseRefine can be seamlessly integrated into any existing semantic segmentation model, regardless of CNN- or ViT-based. SparseRefine achieves significant speedup: \textbf{1.5 to 3.7 times} when applied to HRNet-W48, SegFormer-B5, Mask2Former-T/L and SegNeXt-L on Cityscapes, with negligible to no loss of accuracy. Our ``\textit{dense+sparse}'' paradigm paves the way for efficient high-resolution visual computing.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper tackles the problem of efficient semantic segmentation for high-resolution images. The key idea is to perform inference on low-resolution and refine the high entropy pixels using a sparse convolution network in high resolution. Refinement on sparse pixels makes the method efficient compared to the vanilla high resolution semantic segmentation. The proposed method makes significant speedups on Cityscapes dataset on 4 recent neural network architectures maintaining performance.

### Strengths
* The idea is simple and makes sense. The area to be refined is indeed sparse, and using sparse NN to the refined area makes sense and should improve the time-complexity.

* I enjoyed the generality of the method. Because the method does not assume any restrictions on the segmentation architecture and only uses the segmentation logit, the method is applicable to any segmentation model. The segmentation model can be plug-and-play.

* The experiments are well conducted. The authors show the generality of the method with 4 recent architectures and on various datasets. I believe there is a computational gain to the method maintaining the performance.

* The paper is well-written and easy to follow. All the expectations made in the introduction are satisfied.

### Weaknesses
 * I’m not sure how the training data for the refinement was created. To train the refinement module, sparse high entropy pixels are required. How are the high entropy pixels acquired? Is it acquired from the pretrained segmentation architectures? Also, is the refinement model trained for each of the NN architectures in Table 1, or is it universal?

 * From my understanding, the low-resolution model is trained from the training data. The goal of obtaining the training data for refinement is to match the distribution of high-entropy areas for validation and split. If the low-resolution model is trained from training data, and produces a high-entropy area on training data, then won't the distribution of the high-entropy model for validation and training have different distributions?

 * It would be interesting to report the scores with universal module. Although the performance would not be optimal, I think the community can benefit from using the kitchen-sink model to quickly see how the model can benefit from using it.

### Questions
* (minor) Have the authors explored refining in a multiresolution fashion. It seems the method is applicable to different resolutions, such as 4x downsampling and upsampling twice with 2 refinement architectures.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces an efficient method for 2D image segmentation task, without sacrificing the accuracy. A solution is proposed to sparsely refine the interpolated coarse prediction, based on the unconfident predicted regions identified by an entropy selector. The experiments are evaluated on Cityscapes, BDD100K, DeepGlobe and ISIC datasets, validating the efficiency of the proposed method.

### Strengths
This work explores applying a sparse refinement on the interpolated coarse prediction, which uses an entropy selector to help to sparsely identify the erroneous regions, without the need to refine the prediction in a full image-size. Thus, this approach gives a reduction in computation during inference.

### Weaknesses
1. I agree that the integration of multiple components into a feasible solution is a non-trivial task. However, the composition of such existing works implies that the proposed work lacks sufficient novelties. The core idea of using a low-resolution prediction followed by a sparse refinement is not entirely new, and the paper does not sufficiently highlight the unique aspects of their approach compared to existing methods that employ similar strategies. The novelty is further diminished by the fact that the individual components, such as the entropy selector, are also not novel.
2. Although the authors claim the proposed work provides a significant speedup in inference. However, a comparison in terms of a more persuasive metric, GFLOPS, is missing, which is independent of the machine speed and commonly used for measuring the inference efficiency of a network model. The paper should provide a more detailed analysis of the computational cost, including the number of operations for both the coarse prediction and the sparse refinement steps. This is crucial for a fair evaluation of the method's efficiency.
3. The details of the entropy selector, and the elaboration on the effectiveness of the entropy selector are missing. The paper lacks a thorough analysis of how the entropy threshold is determined and how it affects the performance of the method. Furthermore, it does not provide sufficient evidence to support the claim that the entropy map accurately identifies erroneous regions, and how robust this selection is across different datasets.

### Questions
Another important approach about the uncertainty in segmentation, e.g. Bayesian Deep Learning method [1], is missing in literature and comparison.
[1] Kendall, Alex, and Yarin Gal. "What uncertainties do we need in Bayesian deep learning for computer vision?." Advances in neural information processing systems (2017).

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The manuscript presents an approach to accelerate semantic segmentation inference. The proposed approach combines low-resolution predictions from some standard baseline with sparse high-resolution predictions delivered by MinkowskiUNet. The sparsity is enforced by only looking at pixels with high entropy baseline predictions. These pixels are processed by the sparse feature extractor (Minkowski UNet) while preserving the same sparsity pattern throughout the model. Sparse features are converted to predictions through projection onto the Cityscapes taxonomy. Finally, the joint predictions are recovered by ensembling the dense low-resolution predictions with sparse high-resolution predictions according to regressed weights.

### Strengths
S1. The proposed method succeeds to improve the inference speed (1.5x - 2.0x) of popular heavy-weight models while keeping the mIoU performance.

S2. Sparse feature extraction appears as a powerful and under-researched computer vision technique.

S3. Simplicity of the method will likely lead to derivative future work.

S4. I was really surprised that looking at sparse pixels with so little context could contribute that much to the final performance.

S5. I was also surprised that showing low resolution features to the sparse feature extractor did not help.

### Weaknesses
W1. The three components of the solution (entropy-based uncertainty, Minkowski engine, weighted ensembes) have been proposed in the related work.

W2. Proper validation of hyper-parameter \alpha has not been discussed (validating on test data is not acceptable),

W3. Training the sparse feature extractor requires a lot of computational power (96 RTXA6000 days).

### Questions
Questions

Q1 It would be interesting to ablate capacity of the sparse feature extractor (eg. halving the numbers of feature maps throughout the model).

Q2 Was MinkowskiUNet pre-trained or trained from scratch?

Q3. Show the accuracy for 100% density in Table 5a.

Q4. Include simple average ensembling in Table 5c.

Q5. Explain the magnitude selector.

Q6. Show MACs in Table 7.

Q7 Report minimal hardware requirements (total GPU RAM) for reproducing the experiments

Consider citing earlier work on multi-resolution semantic segmentation:
- HRDA: Context-Aware High-Resolution Domain-Adaptive Semantic Segmentation (ECCV 2022)
- Efficient semantic segmentation with pyramidal fusion (PR 2021)
- HookNet: Multi-resolution convolutional neural networks for semantic segmentation in histopathology whole-slide images (MIA 2021)

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
To improve semantic segmentation performance on low resolution images, the authors propose Sparse Refinement, which composes of entropy selector, 3d-point-clouds-encoder-like sparse feature extractor, and ensembler. As shown in the experiments, the proposed plug-to-play module speed up sota models while keeping the prediction accuracy. The proposed method is also compared to token pruning and mask refinement. Extensive designs are discussed and breakdowns are shown with clarity.

### Strengths
The paper is well written and easy to follow. The motivation and the proposed module is described clearly. Experiments and ablation studies are conducted to verify its superiority. Although the proposed module seems to be a simple collection of existing methods, the performance improvement it brings is significant. The introduction of sparse feature extractor, which is like MinkowskiUNet, extracts features from sparse patterns. The entropy selector is also verifies in figure 3.

### Weaknesses
The proposed module is powerful and clearly stated. The main weakness in this paper I find is the lack of comprehensive experiments.
1. To evaluate a deep learning based model, the authors may want to try various datasets to prove its generalization. The cityscapes, and three domain-specific datasets are not enough. Please try coco, ade20k,pascal…
2. For table 2, it would be better if the authors briefly describe evaluation metrics.
3. In ablation studies, how does the model without ensembler performs?
4. Similar to weakness1, the authors may want to discuss how does the entropy selector behaves on other datasets. 
5. The authors may want to briefly discuss, or derive mathematically, why final prediction or intermediate feature doesn’t improve performance.

### Questions
1. in figure 3, is the recall-precision curve based on the sample image or the cityscapes dataset as a whole? 
2. The authors don’t have to answer this question if their time is limited: since the sparse feature extractor is inspired by 3d point clouds’ encoders, I wonder how does the proposed module perform on 3d benchmarks like 3d semantic segmentation and depth estimation.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good
