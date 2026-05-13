# Space-Time Attention with Shifted Non-Local Search

- Decision: Reject
- Scores: 5, 5, 5

## Abstract
Efficiently computing attention maps for videos is challenging due to the motion of objects between frames. While a standard non-local search is high-quality for a window surrounding each query point, the window's small size cannot accommodate motion. Methods for long-range motion use an auxiliary network to predict the most similar key coordinates as offsets from each query location. However, accurately predicting this flow field of offsets remains challenging, even for large-scale networks. Small spatial inaccuracies significantly impact the attention module's quality. This paper proposes a search strategy that combines the quality of a non-local search with the range of predicted offsets. The method, named Shifted Non-Local Search, executes a small grid search surrounding the predicted offsets to correct small spatial errors. Our method's in-place computation consumes 10 times less memory and is over 3 times faster than previous work. Experimentally, correcting the small spatial errors improves the video frame alignment quality by over 3 dB PSNR. Our search upgrades existing space-time attention modules, which improves video denoising results by 0.30 dB PSNR for a 7.5\% increase in overall runtime. We integrate our space-time attention module into a UNet-like architecture to achieve state-of-the-art results on video denoising.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper addresses non-local search (ie, dense point tracking) from temporal sequences. The authors propose a two stages approach, where at first a local displacement is estimated, the followed by a local search. This framework improves upon previous work which either estimate a point-wise large scale shift, or compute a a local displacement/correlation. The framework is validated in the context of space-time attention, for application such as denoising on Davis dataset.

### Strengths
1) Non global image matching/search is a hard problem. Applications related to video analysis (object tracking, denoising) are important. 

2) The proposed approach (first predicting an off-set, then refinining the estimation in a local search window) is intuitive. The merits of the approach are shown experimentally (frame alignment, space-time attention for video denoising).

### Weaknesses
1) The technical explanations of the implementation of the approach are difficult to follow. Section 3.1 and 3.2 could certainly be clarified and simplified. For example,  specify the meaning of the indices, use different letters for different variables (what is the difference between I and \tilde_I?; if K_v is the variable for the Keys then do not use K again to denote the number of neighbor, etc). The description of the offset prediction network is particularly vague, lacking details on its architecture and training procedure. The use of the term 'local search' is also ambiguous; it is not clear how the search space is defined, what are the search parameters, and how the search is performed in practice. The relationship between the predicted offset and the subsequent local search is not clearly articulated, making it hard to grasp the core mechanism of the proposed approach.

2) The results section is not clear to me. I suggest the authors to start the experiments section by summarizing how they will attempt to demonstrate what are the advantages of their approach through several specific applications using different datasets and different evaluation metrics. The current presentation of the results lacks a clear narrative, making it difficult to understand the significance of the reported numbers. For instance, it is not clear how the video alignment task directly validates the proposed non-local search method. The connection between the method's components and the observed performance gains is not clearly established. The choice of datasets and evaluation metrics, while standard, is not sufficiently justified in the context of the proposed method.

### Questions
See above

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes Shifted Non-Local Search for frame-wise alignment. Specifically, the query points are searched in the windows which is shifted by the predicted optical flows. The top-k locations are then aggregated with Guided Deformable Attention and 3D convolution.

### Strengths
1. The authors demonstrate that optical flow requires only minor spatial corrections for frame-wise alignment.

2. The authors introduce In-Place Computation, which significantly reduces the memory working set and consequently enhances speed.

3. The proposed method achieves state-of-the-art results on video denosing task.

### Weaknesses
1. The way authors show that optical ﬂow only needs small spatial corrections is from the results of Sintel-Clean benchmark, however, this setting is far from the real-world dataset, where blur and degradation could happens. Moreover, these results are from methods with high computational cost, which is not feasible for the online setting.

2. the idea is already explored in video enhancement task, such as BasicVSR++ [1] RVRT [2], where the deformable convolutions/attentions' offsets are computed on top of the SpyNet predicted optical flow. Moreover,  IART [3] propose an cross-attention scheme by searching around the OF-shifted window.

3. This paper is the mixture of 

[1] BasicVSR++: Improving Video Super-Resolution with Enhanced Propagation and Alignment (CVPR2022)

[2] Recurrent Video Restoration Transformer with Guided Deformable Attention (NeurlPS2022)

[3] An Implicit Alignment for Video Super-Resolution (arXiv:2305.00163)

### Questions
1. the reproduced results for RVRT 39.29 seems deviate a lot from the original paper 40.57 for DAVIS sigma=10, why this is the case? Moreover, I think RVRT already implement offsets on top of predicted optical flow, which I think is the same method with the proposed one.

2. Is there direct comparison on STAN alignment with guided deformable attention? (i.e. comparing results by only changing the alignment module, keep the original backbone unchanged for RVRT.)

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a dense offset field (like optical flow) by using attention, and shows demonstrations of video frame alignment (Fig7) and video denoising (Fig8).

The paper claims to propose a kind of a combination of NATTAN (non-local search) and GDA (shift or displacement prediction) as shown in Figure 1. It first finds a large displacement somehow, then refines it using attention, as demonstrated in Fig3. Thus the proposed method is called "shifted" "non-local search".

The core of the paper is section 3.1, which shows the whole process using top-k search with attention, and section 3.2 introduces the case when shift F is given.

Section 3.3 justifies that the refinement of optical flow leads to a better offset estimation, and section 3.4 simply states that the method is implemented on CUDA (which is called in-place).

Experiments show that the proposed method gives a better quality, less memory usage (Fig9) and faster computation (Fig10).

### Strengths
This approach is somewhat on the hardware side and is thus very advantageous in terms of speed and memory consumption over other methods. The method is implemented "in-place", whatever it means as no details are disclosed, so fewer memory consumption is very attractive compared to recent memory-hungry large models.

Denoising performance is better than others as shown in Tables 1 and 2, and table 2 shows that the proposed method has a good trade-off between computation time and gpu memory.

### Weaknesses
Patch-based offset correction: as long as reading section 3.1, similarities for search are computed to each "reference locations" and "search locations", depending on strides S_Q and S_K. Given the predicted offset F, which is floating point coordinates, corrected coordinates reside in the integer grid. In experiments strides were set to 2 (probably, as it is now shown), however it is slower as shown in Table 10. There are no experiments on denoising and alignment with stride 2, it is difficult to expect the proposed method to work as better as stride 1.

Experiments: Results show that the proposed method works as expected, but so many details are not explained and hence it is hard to see how the method really works and how it behaves for different hyper-parameters under ablation studies. For example, patch size P, feature extractor for patches, details predicting offset F, K of top-K,

Insights: This paper is on "space-time attention" and top-k patches are used for the search over T frames. It should be shown that how these top-k patches are selected, how patches attend to where/when, and how corrections are improved, because such insights would be a great help for understanding the method and prompting potential following works.


Other comments:

Organization and writing: Symbols and concepts defined in section 3.1 are not well connected to the following sections and explanations, which makes the logical flow hard to understand.

Offset instead of alignment/denoising: Experimental results demonstrate how the method works in applications, however, directly investigating the learnt offset value F would be helpful for evaluating the proposed method.


Terms:

- "STAN" appears first in p5, but explained and spelled in p8.
- N_Q and N_K for Reference locations and Search locations do not match as Q is for query and K for key.

### Questions
see above

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair
