# FFCA-Net: Stereo Image Compression via Fast Cascade Alignment of Side Information

- Decision: Reject
- Scores: 6, 6, 5

## Abstract
Multi-view compression technology, especially Stereo Image Compression (SIC), plays a crucial role in car-mounted cameras and 3D-related applications. Interestingly, the Distributed Source Coding (DSC) theory suggests that efficient data compression of correlated sources can be achieved through independent encoding and joint decoding. This motivates the rapidly developed deep-distributed SIC methods in recent years. However, these approaches neglect the unique characteristics of stereo-imaging tasks and incur high decoding latency. To address this limitation, we propose a \textbf{F}eature-based \textbf{F}ast \textbf{C}ascade \textbf{A}lignment network (FFCA-Net) to fully leverage the side information on the decoder. FFCA adopts a coarse-to-fine cascaded alignment approach. In the initial stage, FFCA utilizes a feature domain patch-matching module based on stereo priors. This module reduces redundancy in the search space of trivial matching methods and further mitigates the introduction of noise. In the subsequent stage, we utilize an hourglass-based sparse stereo refinement network to further align inter-image features with a reduced computational cost. Furthermore, we have devised a lightweight yet high-performance feature fusion network, called a Fast Feature Fusion network (FFF), to decode the aligned features. Experimental results on InStereo2K, KITTI, and Cityscapes datasets demonstrate the significant superiority of our approach over traditional and learning-based SIC methods. In particular, our approach achieves significant gains in terms of 3 to 10-fold faster decoding speed than other methods.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This manuscript utilizes features and prior knowledge of stereo images in their proposed stereo image compression framework, which achieves advanced compression performance and accelerates decoding time by 3-10 times compared to other learning based methods.

### Strengths
Originality: This paper uses the prior knowledge of stereo images for decoding acceleration, resulting in strong originality.

Quality: This paper provides a detailed description of the prior assumptions used, which is reasonable to some extent; This paper has conducted sufficient experiments to prove that the proposed method can achieve the most advanced compression performance and faster compression speed.

Clarity: This paper provides a clear introduction to the background and motivation of stereo image compression through an abstract, as well as the improvements and advantages of the proposed method compared to other compression algorithms; The structure of the paper is complete and the overall description is relatively clear.

Importance: This paper should have certain reference value for the field of stereo image compression. The proposed method can maintain the compression performance at the STOA level and achieve 3-10 times faster decoding speed than previous learning based algorithms.

### Weaknesses
The improvement of network encoding speed in this manuscript mainly relies on prior knowledge of binocular stereo images. However, these prior assumptions may not be applicable in all cases. Overreliance on prior knowledge may result in the loss of information, which the neural network itself can learn that is beneficial for encoding reconstruction.

The description of techniqe details are not clear or complete enough. For example, , what is the relationship between main and side image in the method section? For non overlay patches, which kind of operation should be done if there are non integer patches remaining. The description of the dataset in the experimental section was too simplistic, such as not introducing scale, resolution, scene, etc.

Although the decoding speed of the method proposed in this paper is significantly improved compared to other methods, the average decoding time for images with a resolution of 832x1024 is 4.91 seconds, which is still difficult to accept in practical applications.

### Questions
1. What is the relationship between Main image and Side image? Is the side image encoded? How to encode? How to measure the final decoding time?

2. Which module mentioned in this paper has the most significant acceleration on image decoding?

3. Do the boundary patches at both ends of the binocular stereo image in the dataset used in the paper require special processing operations?

4. In the definition of G in formula (7), if the distance between two features is less than a certain threshold, it is actually a significant difference. Is there a problem with the description here? What is the definition of $G^c$?

5. Does the bpp term in the loss function only contain the potential representation z, without using any prior knowledge from other learning based compression methods? Is it already included? Are there any special considerations for model optimization based on MS-SSIM?

6. In the ablation experiment, the Fast Feature Fusion module slightly reduced PSNR. Which result proves that the FFF module can achieve faster decoding? How many iterations can the FFF module undergo to achieve the best results?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents FFCA-Net for the task of stereo image compression. Based on the fact in data compression, this method adopts independent encoding and joint decoding structure, and leverage the side information of decoder, proposing FFCA net based on the coarse-to-fine cascaded alignment.  With stereo patch matching, a pyramid-based sparse stereo refinement network, and a lightweight feature fusion module, the proposed method achieves good performance and fast decoding speed when compared with existing learning-based approaches.

### Strengths
The overall design is reasonable, and the realization is practical. Ablation study is provided to verify the effectiveness of the proposed technique components.

### Weaknesses
Most of the technique, although correct, seems incremental, either based on well-known fact/priors, or quite similar to existing method. For example, the fast fusion module, is similar to multi-frame fusion based works. However, other than this, the work is well-motivated, and reasonable designed to achieve good performances with fast speed.

### Questions
In Table 1, although most of the results are good, some of the best results belong to the method LDMIC.

Although not the same, some of the design componments are similar to the Huang 2023. 

Fig. 2 needs to be refined. Current version, the text cannot be read clearly when printed.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces the Feature-based Fast Cascade Alignment network (FFCA-Net), a novel approach to stereo image compression (SIC) suited for applications such as 3D imaging and car-mounted cameras. Contrary to conventional methods reliant on joint encoding and decoding, which place a substantial burden on the encoding terminal, FFCA-Net adopts a strategy of independent encoding and joint decoding, effectively minimizing decoding latency. The network implements a coarse-to-fine cascaded alignment methodology. Initially, it applies a feature domain patch-matching module to reduce redundancy and noise, succeeded by a sparse stereo refinement network aimed at precise alignment of inter-image features. Subsequently, a lightweight yet potent Fast Feature Fusion network (FFF) is utilized to adeptly decode the aligned features.

### Strengths
- The proposed FFCA-Net showcases exceptional performance, outshining competing methods, including those from recent publications, in various evaluations.
- The innovative modules introduced in the paper contribute significantly to enhancing image quality, as evidenced by the results presented in Table 3.

### Weaknesses
- The foundational concepts of the paper, including the coarse-to-fine cascade structure, hourglass-like stereo rectification, and feature fusion layer, appear to be somewhat straightforward, potentially raising questions about the novelty of the approach.
- The paper would benefit from a detailed discussion on the limitations and potential challenges associated with the proposed FFCA-Net.
- Typos and Formatting:
    - On Page 3, change “simultaneously” to “Simultaneously.”
    - Ensure consistent punctuation at the end of equations (1-6, 8-9) with periods, and a comma at the end of equation (7).
- For enhanced clarity and consistency in presentation, ensure that all numerical values across tables, such as Table 2 and Table 3, are expressed with the same number of decimal places.

### Questions
- Are there any limitations to the proposed method?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
