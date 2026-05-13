# ACRF: Compressing Explicit Neural Radiance Fields via Attribute Compression

- Decision: Accept
- Scores: 6, 8, 8, 6

## Abstract
In this work, we study the problem of explicit NeRF compression. Through analyzing recent explicit NeRF models, we reformulate the task of explicit NeRF compression as 3D data compression. We further introduce our NeRF compression framework, Attributed Compression of Radiance Field (ACRF), which focuses on the compression of the explicit neural 3D representation. The neural 3D structure is pruned and converted to points with features, which are further encoded using importance-guided feature encoding. Furthermore, we employ an importance-prioritized entropy model to estimate the probability distribution of transform coefficients, which are then entropy coded with an arithmetic coder using the predicted distribution. Within this framework, we present two models, ACRF and ACRF-F, to strike a balance between compression performance and encoding time budget. Our experiments, which include both synthetic and real-world datasets such as Synthetic-NeRF and Tanks&Temples, demonstrate the superior performance of our proposed algorithm.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work addresses the problem of compressing explicit Neural Radiance Fields (NeRFs) for 3D data representation. The authors introduce a framework called Attributed Compression of Radiance Field (ACRF) to achieve this. ACRF prunes the neural 3D structure and encodes it as points with features using importance-guided encoding. It also employs an importance-based entropy model to optimize the encoding process. The authors present two models, ACRF and ACRF-F, balancing compression performance and encoding time. Experiments on synthetic and real-world datasets, including Synthetic-NeRF and Tanks&Temples, showcase the superior performance of their approach.

### Strengths
- The idea is simple yet effective.
- The experimental results are convincing and the ablation study shows the necessity of each component.

### Weaknesses
Major
- The proposed method is based on voxel-grid compression of NeRF with limited change so the novelty of it is limited.
- The paper writing can be further improved. For instance:
  - In section 3, the concrete definitions of r and N are not shown.
  - The motivation for adopting entropy minimization mentioned in section 4.3 is unclear.
Minor:
- I recommend the authors mention which section in the supplementary describes the details in the main paper.

Major:
- Could you provide more elaboration about why RAHT with point importance introduces additional high-frequency noise to the original features and necessitates the transmission of importance values for decoding?
- Could the author provide more explanations for the motivation for adopting entropy minimization?
- How can the \labmda be tuned to control the model size?

Minor:
- Why do the authors only conduct the ablation study on the chair of the Synthetic-NeRF dataset? Could the authors provide experimental results of the ablation study on different datasets?

### Questions
Major:
- Could you provide more elaboration about why RAHT with point importance introduces additional high-frequency noise to the original features and necessitates the transmission of importance values for decoding?
- Could the author provide more explanations for the motivation for adopting entropy minimization?
- How can the \labmda be tuned to control the model size?

Minor:
- Why do the authors only conduct the ablation study on the chair of the Synthetic-NeRF dataset? Could the authors provide experimental results of the ablation study on different datasets?

------------------------------------------------
### Post rebuttal:

Most of my concerns are addressed after reviewing the authors' responses and discussion between authors and reviewers. I am willing to raise my evaluation from 5 to 6.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This manuscript proposed a novel framework of Radiance Field attribute compression, which treated the compression task of explicit neural 3D representation as 3D data compression. Specifically, the neural 3D structure is pruned and converted to points with features, which are further encoded using importance-guided feature encoding. An importance-prioritized entropy model is proposed to estimate the probability distribution of transform coefficients, which are then entropy coded with an arithmetic coder using the predicted distribution. Experimental results demonstrate that the proposed method achieves superior performance on both synthetic and real-world datasets such as Synthetic-NeRF and Tanks&Temples.

### Strengths
The whole manuscript is well structured and the technique details are easy to follow. Experimental results demonstrate that the proposed method achieves superior performance on both synthetic and real-world datasets, in terms of RD performance and encoding/decoding time,.

The method proposed in this manuscript follows the standard point cloud attribute compression process, and has been optimized based on the characteristics of the explicit neural 3D representation in multiple stages such as data pruning, feature encoding and entropy minimization. The idea is reasonable and interesting.

### Weaknesses
1）Some technique details are not clear enough. For example, only encoding time data are provided in Table 1, it is suggested to provide decoding time data to highlight the practicality of the proposed algorithm. The model size and quality info are missing in Fig. 5.

2)  Other type of compression methods such as Rho et al. (Rho et al., 2023) are not evaluated in this manuscript.

3) Typos. ``As depicted in 6,``=>``As depicted in Fig. 6,``

### Questions
Please refer to the Weaknesses section.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a novel approach for explicit NeRF compression, focusing on compressing the latent features of the NeRF model. More specifically, the authors first conduct a comprehensive analysis of NeRF compression and reformulate the task as 3D data compression. Then, they propose their ACRF framework, comprising pruning, feature encoding, and entropy minimization. Experiments were conducted to demonstrate the effectiveness of the proposed method, both for the compression performance and coding speed.

### Strengths
1. Originality: The analysis and reformulation of NeRF compression seems reasonable, and the utilization of attribute compression is practical.
2. Quality: The experimental results validate the effectiveness of the proposed algorithm, which integrates the conventional image compression pipeline with several NeRF-oriented modules.
3. Clarity: The paper is well-written and easy to read.
4. Significance: Given the rising popularity of NeRF models, the investigation of NeRF compression is of great significance.

### Weaknesses
1. From the perspective of conventional image compression, additional computation and time budget is required for encoding and decoding, which might be a problem for real NeRF applications. 
2. In the related works (Sec. 2.2), it would be better to illustrate the main difference between the proposed method and prior research, such as the mentioned 3DAC, Rho et al. and ReRF.
3. Experiments: In Table 2, it seems that there is a performance drop with additional information (Voxel Grid, A). Please check the result and give some explanations. Similarly, in Figure 6, Baseline A outperforms A+Imp FE. Please justify.
4. Experiments: In Figure 5, the qualitative results of two relatively simple scans are provided. It would be beneficial to extend the analysis to include more complex scans (e.g., object with high reflectance).
5. In the appendix (Sec. D), it seems that the proposed modules do not perform well on PointNeRF. It would be beneficial to extend the analysis in the appendix, and add some discussions in the main paper.

### Questions
1. Include discussion and future direction for recent NeRF algorithms. The gaussian-splatting algorithm represents the radiance field in a point-cloud-like structure, showcasing notable achievements in training and rendering performance. One limitation of this approach is the significant storage budget. For example, the output model takes over 1GB for unbounded scenes, like bicycle in mipnerf360. It will be interesting to integrate these techniques with the proposed algorithm.
2. See weakness 3, 4, 5 and 6.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Given a pre-trained NeRF model with an explicit 3D representation, this paper aims to reduce the model size while maintaining good performance. It proposes reformulating the task as 3D data compression with three steps.
Firstly, it proposes view-dependent pruning, which eliminates features with low absolute values.
Then, it performs a point-based wavelet transform with octree coding to convert features with importance to coefficients.
Lastly, it minimizes the information entropy for the coefficients.
Depending on whether there is a rendering loss, two versions are introduced.
Experiments are conducted on the Synthetic-NeRF and Tank&Temples datasets to show their significant compression rates.

### Strengths
[Results] The quantitive results in Fig. 4 and encoding time comparison Tab. 1 show the proposed method achieves a modestly larger compression ratio in comparison with voxel-based methods and a remarkably higher compression ratio in comparison with point-based methods.

[Novelty] The proposed three-step method is reasonable, achieves remarkable improvements in compression performance, and simultaneously reduces the encoding time.

### Weaknesses
[Clarity]

- In Sec.4.1, the paper uses a half page and two formulations to introduce view-dependent pruning. I think this part seems redundant. Because the following view-independent pruning is not based on the view-dependent pruning.

- In Sec.4.2, the paper introduces $e = RAHT(p,f \cdot I_l)$ as a straightforward implementation. I am not sure how to introduce the importance and then recover $f$. Actually, I think $f \cdot I_l $ destroy $f$ and it is hard to recover $f$. It is not a noise issue. Instead, I think the proposed mask strategy is more intuitive. Also, if $e = RAHT(p,f \cdot I_l)$ is important, it would be better to use it as a baseline. I think this part introduces more confusion.

- I could not follow the first formula in Section 4.3, the independent variables are distributions p and q, but in the right of the equation, there is only q. I am not sure how to eliminate the distribution of p. Are any assumptions or references missing?

- Fig.1 is too small, and it does not provide enough explanation. I cannot follow the meaning of the color or the connection between local patterns and latent features.

- Fig.5 is hard to distinguish. All the results of different methods seem the same. It would be better to highlight their difference.

[Fig.4] In Fig.4, the compressed model achieves a 100 $\times$ compression ratio while obtaining a higher SSIM (top right). Would you please provide more discussion on it?

[Speed & Practicality] In Sec.5.1 Encoding Time Comparison part, the paper claims that the proposed method only requires additional 1s for decoding. This part is vague. I am not sure whether this time has a huge impact or is insignificant during testing. The overall compression seems complex. I suggest the decoding time and the overall inference time should be discussed in detail. More specific settings, including batch size, image size, and overall inference time, are needed.

[$|f_v|$] Eq.5 is not so convicting. For me, I think it is easy to understand that the minimum absolute value means low information. But I am not sure the maximum absolute value can be employed to quantify the amount of information. The paper claims this is based on''statistical measures''. It would be better to provide statistical evidence or some references to support this claim.

[Task specific] The feature encoding and the entropy minimization seem like standard strategies for data compression and are not specifically designed for Nerf. It would be better to highlight the main contribution of those two parts regarding Nerf.


[Experiments]

- This paper claims that integrating pruning strategies into training pipeline is time-consuming and impractical for compression(Section 4.1). But it is still important to compare those existing methods(Deng & Tartaglione, 2023; Xie et al., 2023), even the proposed method is a post-optimization method.

- The comparison experiments are insufficient. I suggest to compare previous works like (Li et al.,2023; Rho et al., 2023;)

[Typo]
- Section 1, propsoe -> propose
- Appendix Section C, subscript error
-The description of baselines should be more specific (Fig. 5), like the definitions of "ACRF(DVGO)" and "ACRF-F(DVGO)".

### Questions
See weakness

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
