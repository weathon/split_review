# Frequency-Aware Transformer for Learned  Image Compression

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
Learned image compression (LIC) has gained traction as an effective solution for image storage and transmission in recent years. However, existing LIC methods are redundant in latent representation due to limitations in capturing anisotropic frequency components and preserving directional details. To overcome these challenges, we propose a novel frequency-aware transformer (FAT) block that for the first time achieves multiscale directional ananlysis for LIC. The FAT block comprises frequency-decomposition window attention (FDWA) modules to capture multiscale and directional frequency components of natural images. Additionally, we introduce frequency-modulation feed-forward network (FMFFN) to adaptively modulate different frequency components, improving rate-distortion performance. Furthermore, we present a transformer-based channel-wise autoregressive (T-CA) model that effectively exploits channel dependencies. Experiments show that our method achieves state-of-the-art rate-distortion performance compared to existing LIC methods, and evidently outperforms latest standardized codec VTM-12.1 by 14.5\%, 15.1\%, 13.0\% in BD-rate on the Kodak, Tecnick, and CLIC datasets

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
A learned image compression approach based on transformer architecture is presented. The main innovation is the introduction of a frequency-aware module that performs multi-scale, directional analysis of the transformer features, and then uses an FFT to weight the important frequency components. Results show mild to moderate improvements in the RD-curve and BD-metric on various datasets.

### Strengths
The intuition behind the method is sound. Writing and explanation is clear. Results show improvements over various transformer-based baselines.

### Weaknesses
This is a general comment rather than a specific weakness. It is not entirely clear how much improvement is brought about by the specific structure of the FDWA and FMFFN blocks, rather than the fact that some learnable layers have been included which would increase the overall capacity of the network. The authors have provided a few ablations in Figures 5. and 6. which do somewhat support their claim, but I feel this could be made stronger in future versions. For instance,

1. What if additional windows with different aspect ratios were used? Would these provide further improvement? This could be achieved by either increasing $K$ (the number of heads), or by using the same number of heads but partitioning into more groups to accommodate the different aspect ratios?

2. The impact of the FMFFN block seems to be rather small. What if instead of a block FFT, a learnable conv layer (and deconv for the IFFT) was used?

### Questions
Included in comment above.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper aims to reduce redundancies in the latent representation of Learned Image Compression methods.
For this purpose it proposes a new frequency-aware transformer block which utilizes two new components.
1. FDWA: a window attention block to capture various frequency components
2. FMFFN: a block which modulates the frequency components 

Additionally this paper proposes a transformer-based channel-wise autoregressive entropy model (T-CA)
In combination these methods achieve SOTA performance on various datasets.

### Strengths
1. The method achieves SOTA performance without unreasonable performance cost.
2. The paper is well written and provides nice visualizations of core ideas.

### Weaknesses
There are no explicit ablations of some design decisions of the FAT block. What effect do the relative window sizes of the FDWA module have? What's the impact of omitting some of the windows (eg. omitting vertical/horizontal windows)?

There are typos in the caption of Figure 3 (p.6) and Table 2 (p.8)

### Questions
How does the use of the T-CA entropy model affect inference times (compared to existing models such as CHARM)?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
To overcome the problem of existing LIC (Learned Image Compression) methods are redundant in latent representation, this paper suggests a nonlinear transformation and makes the following three improvements:

1)	This paper proposes a frequency-decomposition window attention (FDWA), which leverages diverse window shapes to capture frequency components of natural images.

2)	This paper develops a frequency-modulation feed-forward network (FMFFN) that adaptively ensembles frequency components for improved R-D performance.

3)	This paper presents a transformer-based channel-wise autoregressive model (T-CA) for effectively modeling dependencies across frequency components.

Experimental results show that this paper achieves state-of-the-art R-D performance on several datasets.

### Strengths
1) The paper is overall easy to understand and clearly written. One of the primary strengths of this paper is the claimed SOTA rate-distortion performance. 
2) The authors found that existing learned image compression methods lead to potential representation redundancy due to limitations in capturing the anisotropic frequency components of anisotropy and preserving directional details. Some attempts including FMFFN and FDWA are proposed to address this issue.

### Weaknesses
1) The idea of applying frequency processing to the learned compression framework is not new. For example, conv in the frequency domain [1] has been used in Balle’s early work [2]. Wavelet-based compression framework has also been proposed [3]. The authors should cite, compare, and identify their differences. Specifically, the paper lacks a detailed discussion on how the proposed frequency-decomposition window attention (FDWA) and frequency-modulation feed-forward network (FMFFN) differ fundamentally from existing frequency-based approaches. The use of FFT to transform features into the frequency domain, while common, needs more justification in the context of learned compression, especially given the computational overhead. The authors should clarify how their method avoids the limitations of prior work that used similar frequency-based techniques but did not achieve the same level of performance.

[1] Rippel, Oren, Jasper Snoek, and Ryan P. Adams. "Spectral representations for convolutional neural networks." Advances in neural information processing systems 28 (2015).

[2] Ballé, Johannes, Valero Laparra, and Eero P. Simoncelli. "End-to-end optimized image compression." arXiv preprint arXiv:1611.01704 (2016).

[3] Ma, Haichuan, et al. "iWave: CNN-based wavelet-like transform for image compression." IEEE Transactions on Multimedia 22.7 (2019): 1667-1679.

2) The authors should compare with more existing works (e.g. [3,4]) to demonstrate the SOTA performance of the paper. The comparison should not only focus on rate-distortion performance but also include computational complexity, training time, and memory usage. The current comparison is limited and does not provide a comprehensive view of the proposed method's advantages and disadvantages. For example, the paper should compare against methods that use similar transformer architectures but do not explicitly incorporate frequency domain processing, to isolate the benefit of the proposed frequency-aware approach. Furthermore, the paper should include comparisons with more recent methods, such as [5], to ensure the state-of-the-art claim is well-supported.

[4] Liu J, Sun H, Katto J. Learned image compression with mixed transformer-cnn architectures[C]//Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2023: 14388-14397.

[5] Fu H, Liang F, Liang J, et al. Asymmetric Learned Image Compression with Multi-Scale Residual Block, Importance Scaling, and Post-Quantization Filtering[J]. IEEE Transactions on Circuits and Systems for Video Technology, 2023.

### Questions
1. Table 1 and Table 5 in the article involve flop calculations, may I ask the authors what methods or tools they used to calculate the complexity? As far as I know, many existing tools that count complexity do not calculate correctly the complexity of the internal operators of the transformer. Besides, Table 5 is kind of confusing. Can the authors explain what the (1), (2), (3) in the table mean here.

2. Adding a transformer on the codec side would result in a longer training time and a larger memory requirement that is not hardware-friendly for the actual deployment of the compression model. Can the authors provide the training time as well as the corresponding average and peak memory consumption for both training and test? Besides, the three methods compared in Table 5 are all transformer-based methods, and there is no comparison of decoding time with, for example, Minnen[1] and GMM[2], where both the encoder and decoder use a CNN structure.

[1] Minnen D, Singh S. Channel-wise autoregressive entropy models for learned image compression[C]//2020 IEEE International Conference on Image Processing (ICIP). IEEE, 2020: 3339-3343.

[2] Cheng Z, Sun H, Takeuchi M, et al. Learned image compression with discretized gaussian mixture likelihoods and attention modules[C]//Proceedings of the IEEE/CVF conference on computer vision and pattern recognition. 2020: 7939-7948.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper studies the frequency problem of learned image compression and develops a frequency-aware method for this problem based on multiscale and directional analysis, called FAT. The method introduces two modules to capture frequency component. Based on FAT, the learned image compression achieves better rate-distortion performance. The method shows improvement over learned codec and conventional codec baselines by a healthy margin.

### Strengths
1. The proposed FAT is a novel idea that captures multiscale and directional frequency components and outperforms SOTA.

2. Nice visualization on multiscale and directional decomposition of frequency component. It is an interesting finding that structural information within different frequency ranges also plays a crucial role in learned image compression.

### Weaknesses
1. It is interesting to find that FDWA achieves a significant improvement compared to 4x4 blocks and 16x16 blocks. However, it is not clear that how does the multiscale decomposition and the directional decomposition affect. The authors are suggested to provide an ablation study on FDWA.

2. The frequency-aware transformer is realized by two modules, FDWA and FMFFN. Have you tried these two mechanisms in the entropy model? Entropy model plays a crucial role in learned image compression. In my opinion, it is more important to capture frequency component in entropy model. It would be a great improvement if the frequency-aware mechanism works.

### Questions
1. Have you ever tried other decomposition ways such as (1) smaller size and bigger size for square window (I am wondering how much improvement can be obtained in this mechanism), or (2) more diverse shapes.
 
2. What impact does the block size in FMFFN have? When you set the block size responding to the maximum window size in FDWA, does it mean that the FMFFN is used to refine the high-frequence of features?
 
3. If the decomposition of window size works, how about directly using different sizes of convolution?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
