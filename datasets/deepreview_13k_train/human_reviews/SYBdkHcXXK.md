# When Semantic Segmentation Meets Frequency Aliasing

- Decision: Accept
- Scores: 8, 5, 5

## Abstract
Despite recent advancements in semantic segmentation, where and what pixels are hard to segment remains largely unexplored. Existing research only separates an image into easy and hard regions and empirically observes the latter are associated with object boundaries. In this paper, we conduct a comprehensive analysis of hard pixel errors, categorizing them into three types: false responses, merging mistakes, and displacements. Our findings reveal a quantitative association between hard pixels and aliasing, which is distortion caused by the overlapping of frequency components in the Fourier domain during downsampling. To identify the frequencies responsible for aliasing, we propose using the equivalent sampling rate to calculate the Nyquist frequency, which marks the threshold for aliasing. Then, we introduce the aliasing score as a metric to quantify the extent of aliasing. While positively correlated with the proposed aliasing score, three types of hard pixels exhibit different patterns. Here, we propose two novel de-aliasing filter (DAF) and frequency mixing (FreqMix) modules to alleviate aliasing degradation by accurately removing or adjusting frequencies higher than the Nyquist frequency. The DAF precisely removes the frequencies responsible for aliasing before downsampling, while the FreqMix dynamically selects high-frequency components within the encoder block. Experimental results demonstrate consistent improvements in semantic segmentation and low-light instance segmentation tasks.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes two novel de-aliasing filter (DAF) and frequency mixing (FreqMix) modules to alleviate aliasing degradation by accurately removing or adjusting frequencies higher than the Nyquist frequency. The paper observes three different wrong segmentation types potentially caused by aliasing (a) False response, (b) Merging mistake (c) Displacement. In addition, the paper designed a simple de-aliasing filter to precisely remove aliasing as measured by their aliasing score. Additionally, we propose a novel frequency-mixing module to dynamically select and utilize both low and high-frequency information. The work has really comprehensive ablation studies, and the induction logic is comprehensive. They have proved their proposed method surpasses strong baselines Mask2Former, PointRend.

### Strengths
1. The experiment of the paper is very comprehensive and solid. The authors provide analysis of (1) the relationship between blur kernel size with Boundary, Three type errors, and Aliasing score.  (2) Noise level in effect to aliasing. (3) their cut-off frequency in relationship with accuracy and aliasing. (4) In comparison with other anti-aliasing modules. (5) Show effectiveness with model scaling up. (6) In Comparison with SoTA segmentation model.

2. The paper introduces the concept of equivalent sampling rate for the Nyquist frequency calculation and proposes an aliasing score for quantitative measurement of aliasing levels.

### Weaknesses
Actually, I think from a research perspective, I believe the paper is valid and sound so I recommend accepting this paper. However, from a higher level of view, many traditional problems including anti-aliasing have been eroded by the current trend of Large Models. The effectiveness of more training data or advances in pre-trained model weights will shrink the marginal gain of those methods. Especially for the transformer-based architecture, the downsample operation is no longer max-pooling even adaptive-pooling. this potentially alleviates the aliasing problem itself.

### Questions
It would be really appreciated if the authors shared their thoughts on whether aliasing is still a problem if the backbone downsampling is fully adaptive in a transformer-based architecture.

### Soundness
3 good

### Presentation
3 good

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
The work proposes a new anti-aliasing scheme by redefining the cutoff frequency. This is done by considering the expansion in both the channel dimension and the spatial dimension. The proposed aliasing score showed a strong correlation with various segmentation errors. Additionally, the authors introduced a new anti-aliasing and spectral filter that enhances the segmentation performance.

### Strengths
1. Investigates the critical yet under-explored question regarding the effect of aliasing in computer vision models.
2. The proposed fixes enhance performance.
3. The paper is well-written and clearly explained.

### Weaknesses
1. The proposed module, FreqMix, requires additional forward and inverse Fourier transforms at each layer. Compared to other methods, this increase in time complexity (inference and training) needs to be discussed. The paper lacks a detailed analysis of the computational overhead introduced by these transforms, specifically how the FFT and iFFT operations scale with different input sizes and channel dimensions. This is crucial for understanding the practical applicability of the method, especially in resource-constrained environments.
2. Experiments are limited. It is necessary to conduct evaluations on other benchmark datasets, such as MS COCO and Pascal VOC. The current evaluation is insufficient to demonstrate the generalizability of the proposed method. The paper should include a broader range of tasks and datasets to validate its effectiveness across different scenarios and object complexities. The absence of results on standard datasets like COCO and Pascal VOC makes it difficult to compare the proposed method with existing state-of-the-art techniques.
3. Improvements are marginal. While the paper shows some performance gains, the magnitude of these improvements is not substantial enough to justify the added complexity of the proposed method. The paper needs to provide a more compelling argument for the practical significance of these marginal improvements, especially considering the added computational cost. It is unclear if the observed gains are consistent across different architectures and hyperparameter settings.

### Questions
1. I need more clarification about the robustness of ESR (equivalent sampling rate). Clearly, the filters are orthogonal for the shown example (Fig 3). So there is no loss of information.
But what if the filters are not orthogonal to each other? Assume a worst-case scenario where all filters are equal. In that case, the proposed ESR will give us a wrong sampling rate. So, is the proposed ESR intended to replace the regular “sampling rate,” or is it intended as a heuristic to select cutoff frequency? If it is the second, then the paper should clarify it.
2. Section 3.2, “Metrics for three errors.” — I think the middle one should be the definition of MErr.
3. “aligning with the observations in Figure 1 that false responses and merging mistakes predominantly exist in areas with relatively low aliasing scores.” — could you clarify how we are associating aliasing scores with a region of an image? 
4. “However, for deeper features at the second and third stages, the aliasing ratio decreases.
This decrease does not signify a reduction in aliasing; rather, it occurs because the earlier high level of aliasing results in severe degradation. Consequently, the features become ‘hard pixels,’ meaning that the following stage struggles to extract useful information and loses response to objects.” — How can we confirm that it is caused by the side effect of aliasing? Applying significant noise can generate an out-of-distribution (OOD) sample of the internal layers, which can also lead to poor feature extraction.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
In this paper, the authors introduce a challenging yet critical topic for semantic segmentation, i.e., pixel-wise aliasing. They categorize the hard pixel error into three types: false response, merging mistakes and displacements. Creatively, the de-aliasing filter and frequency mixing modules are introduced to alleviate the aliasing degradation. Experiments demonstrate that these findings can consistent improve the semantic segmentation performance.

### Strengths
#1 The topic is attractive where the unexplored aliasing phenomenon for semantic segmentation are carefully investigated. This funding can motivate the researcher in the related community. 
#2 The authors utilize the DAF and FreqMix to remove the aliasing in Fourier domain and balance high-frequency components in the encoder block. Converting the features to frequency domain by DFT is straightforward, but finding the aliased false prediction for semantic segmentation is interesting.

### Weaknesses
 #1 Lacking visualization for the three type of errors in the experiment. Though the authors provide the results on ADE20K, it does not clearly present the visualization to the correction of three type of errors for semantic segmentation. In addition, how the DAF and FreqMix help locate these errors are not visualized.

### Questions
#1. The authors must provide more visualizations on the three types of errors and the corresponding feature maps in frequence domain. 
#2. As to the DAF and FreqMix, how the filtered feature maps can help find the location of error map should be invastigated. 
Overall, the topic for finding the aliasing is interesting, the reviewer encourage the author further explore this missing parts in the semantic segmentation.

### Soundness
3 good

### Presentation
1 poor

### Contribution
3 good
