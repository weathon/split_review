# On Quantizing Neural Representation for Variable-Rate Video Coding

- Decision: Accept
- Avg Score: 7.20
- Scores: 8, 6, 6, 8, 8

## Abstract
This work introduces NeuroQuant, a novel post-training quantization (PTQ) approach tailored to non-generalized Implicit Neural Representations for variable-rate Video Coding (INR-VC). Unlike existing methods that require extensive weight retraining for each target bitrate, we hypothesize that variable-rate coding can be achieved by adjusting quantization parameters (QPs) of pre-trained weights. Our study reveals that traditional quantization methods, which assume inter-layer independence, are ineffective for non-generalized INR-VC models due to significant dependencies across layers. To address this, we redefine variable-rate INR-VC as a mixed-precision quantization problem and establish a theoretical framework for sensitivity criteria aimed at simplified, fine-grained rate control. Additionally, we propose network-wise calibration and channel-wise quantization strategies to minimize quantization-induced errors, arriving at a unified formula for representation-oriented PTQ calibration. Our experimental evaluations demonstrate that NeuroQuant significantly outperforms existing techniques in varying bitwidth quantization and compression efficiency, accelerating encoding significantly and enabling quantization down to INT2 with minimal reconstruction loss. This work achieves variable-rate INR-VC through weight quantization for the first time and lays a theoretical foundation for future research in rate-distortion optimization, advancing the field of video coding technology.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
In this paper, the authors propose a post-training quantization method tailored to implicit neural representation (INR) based image and video compression. They argue that existing post-training quantization methods are not suitable for INR-based image and video codecs, and advance the existing PTQ for this specific task. Furthermore, the authors demonstrate how their proposed method can tackle variable rate coding with INR using a single INR model. They experimented with their method on top of existing INR methods and showed that their method performs better with minimal reconstruction loss.

### Strengths
1) Using one single model for different bit rates with post-training quantization is interesting. This alleviates the need to train a model for each bit-rate, this will decrease the training time.

2) The paper provides the mathematical insights to their proposed method, inspired from the Nagel et. al (2020), and formulates the post-training quantization objective with respect to the network calibration. 

3) The experimental results show that the proposed method has a significant gain in the variable-rate coding.

### Weaknesses
1. The authors failed to compare their proposed approach with Neural Network Coding tool (NNC) [1] which also performs post-training quantization, and also can offer variable-bitrate coding by adjusting QP parameters. The authors should compare their method with NNC.




### Questions
1. How the figure 3 is generated. what is the architecture details of the INR network, and what kind of data is used for fitting. Does the analysis is also true for MLP?

2. What is the significance of the equation 5 and 6, whether this optimization problem is solved in the paper. In the abstract, it was mentioned, PTQ was formulated as the mixed-precision quantization, it was not evident for me where the mixed precision quantization is solved. From the table 1, it seems like the mixed-precision quantization was not used. Also detail how the mixed-precision quantization is used.

3.  For Nagel et.al (2020) which formulation was used to compare? In Nagel et. al (2020) whether the equation (25) or equation (21) is used in their respective paper. It is important to specify, the equation (25) is closer to the loss (network calibration) in the proposed paper.
 
4. In equation (16), how the $\mathbf{s}$ is determined, is it learned with respect to the task loss, or is it optimized by the greedy search or is it fixed parameter. 

5.  the network-wise calibration might also be applicable to the generalized neural network, did the authors have done any experiments on the generalized neural codec? 

6. For the quantization aware training approach, the weights initialization with post-training quantization will improve the convergence and reconstruction quality of the QAT. It would be nice to test this feature on some INR method which uses QAT.

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
NeuroQuant is a cutting-edge post-training quantization method for variable-rate video coding that optimizes pre-trained neural networks for different bitrates without retraining.

### Strengths
1. The proposed method achieves variable-rate coding by adjusting QPs of pre-trained weights, eliminating the need for repeated model training for each target rate, which significantly reduces encoding time and complexity.

2. The method demonstrates superior performance in compression efficiency, outperforming competitors and enabling quantization down to INT2 without notable performance degradation.

3. The paper proposes a unified formula for representation-oriented PTQ calibration, streamlining the process and improving its applicability across different models.

4. The approach is backed by both empirical evidence and theoretical analysis, ensuring its robustness and effectiveness in practical applications.

### Weaknesses
N/A
Actually, I am not very familiar with this field, so please have AE consider the opinions of other reviewers more.

### Questions
How does NeuroQuant differ from traditional quantization methods in terms of bitrate adjustment?

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
In this paper, the authors propose post-training quantization for INR-VCs, which achieves variable-rate coding more efficiently than existing methods that require retraining the model from scratch. The proposed model realizes variable bitrate by considering the sensitivity of the weights to quantization, while also incorporating better theoretical assumptions for INR-VC compared to other post-training quantization techniques. The proposed method demonstrates both improved RD performance and faster encoding speed.

### Strengths
- The results look promising. Although NeuroQuant achieves only a marginal improvement over the current best INR-VC (-4.8%), it provides greater efficiency in obtaining multiple rate points.
- The experiments comparing different quantization methods are comprehensive, which will be helpful for future work in this area.

### Weaknesses
 - In Table 2, excluding the pretraining time for NeuroQuant does not seem appropriate. Even with NeuroQuant, pretraining is still required, and the current presentation may be misleading. The authors should consider reporting the pretraining and fine-tuning times separately for both the baseline models and NeuroQuant.
- Similarly, the claim of an 8x encoding speedup is also misleading, as it excludes the pretraining time required for INR-VC encoding (even though NeuroQuant avoids full retraining for each rate point).
- Variable/learnable quantization levels for INR-VC have been explored in related works [1,2,3], so the paper’s claim is inaccurate (e.g., line 43). These methods, which resemble the proposed mixed-precision quantization, also enable fine-tuning for multiple rate points from a single pretrained model (but with QAT). These methods should be discussed and compared in the paper. Specifically, the paper should clarify how the proposed method differs from existing approaches that use quantization-aware training (QAT) to achieve variable bitrates, and provide a detailed comparison of the performance and complexity trade-offs.
- For a fairer comparison, the comparisons to x264/x265 should avoid using the 'zerolatency' setting, as the INR-VCs in the paper inherently have non-zero latency. The use of 'zerolatency' unfairly advantages x264/x265 by sacrificing compression efficiency for speed, which is not a relevant comparison point for the proposed method.
- For ablation study, more sequences should be use for obtaining a representative result. The current ablation study is limited to a single sequence, which may not generalize well to other video content. Expanding the ablation study to include a more diverse set of sequences would provide a more robust evaluation of the method's performance.

### Questions
- The encoding runtime for HiNeRV 3M (22 hours) looks significantly longer than reported in the original paper, even accounting for differences in GPUs. Additionally, the reported memory usage seems unusually high. Are there any differences in configuration, such as the use of FP16 precision in these experiments?
- How much time is required to obtain additional rate points with models like NeRV, HNeRV, FFNeRV, and HiNeRV? Although these models require a pretraining phase, the pretrained model can be fine-tuned to produce multiple rate points by adjusting quantization levels or using entropy coding with regularization [1]. Fine-tuning time is substantially shorter than full training (e.g., 30 epochs for QAT versus 300 + 60 epochs for HiNeRV).
- What is the computational cost (in terms of MACs and wall time) for the proposed calibration process compared to QAT?

[1] Gomes, Carlos, et al. "Video compression with entropy-constrained neural representations."

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes a novel post-training quantization approach designed for INR-VC called NeuroQuant that enables variable-rate coding without complex retraining. It redefines variable-rate coding as a mixed-precision quantization problem. Through network-wise calibration and channel-wise quantization strategies, NeuroQuant achieves SOTA performance compared to popular PTQ and QAT methods.

### Strengths
Compared with existing quantization methods, the proposed method could achieve significant performance improvement, indicating the efficiency of the proposed method.
There are some highlights for the proposed post-training quantization method for INR-VC:
1.	A criterion for optimal sensitivity in mixed-precision INR-VC was proposed, enabling the allocation of different bitwidth to network parameters with varying sensitivities.
2.	Through network-wise calibration and channel-wise quantization strategies,  NeuroQuant minimize quantization-induced errors, arriving at a unified formula for representation-oriented PTQ calibration.

### Weaknesses
1.	The authors did not provide a detailed explanation as to why the proposed PTQ method would be superior to QAT methods such as FFNeRV and HiNeRV.
2.	In the Encoding Complexity section, the authors did not provide a detailed explanation of whether the acceleration brought by NeuroQuant is due to the absence of QAT optimization during training or because NeuroQuant does not require retraining for adjustments at different bitrates.

### Questions
1.	I think that the RD performance of the PTQ method may be slightly inferior to QAT. Could you explain why the proposed PTQ method has better RD performance compared to FFNeRV/HiNeRV?
2.	Could you provide a detailed explanation of the Encoding Complexity section? Does it refer to the encoding complexity of a single bitrate or multiple bitrate?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
In this paper, the authors aim to introduce the variable rate control for INR-based video coding, by simply using PTQ. Therefore, they investigate PTQ approaches with mixed precision on those INR models. They first validate a weak layer independence in such non-generalized INR models. This challenges Hessian-based quantization methods, as they often follow this assumption and adopt diagonal Hessians. Then the authors propose a perturbation-based approach to estimate the intractable Hessian-involved sensitivity criterion (Omega) in the section with eq.9 and eq.10. Therefore, they can perform bit allocation for mix-precision quantization. Then the authors adopt network-wise calibration to further decrease the quantization error. The proposed approach named NeuroQuant achieves a cutting-edge performance w.r.t. both single QP and the whole RD curve.

### Strengths
The paper is well-written and easy to follow. The authors clearly explain their motivation for adopting mix-precision PTQ for variable-rate INR video coding. The experimental results are impressive, with significant PSNR improvements (*e.g.* 0.2 db @6bit and 3 db @2bit for NerV) on all the experimental settings.

### Weaknesses
1. The comparison in Table 1 may be unfair. If I understand correctly, the proposed approach involves mix-precision quantization, which helps bit allocation among layers. Therefore, it introduces extra quantization step parameters (${s}$ in eq.17) to store. I wonder whether the bpp calculation in Fig.4 and Fig.5 considers this quantization parameter. On the other hand, AdaQuant and BRECQ are fix-precision methods so this parameter can be omitted. The authors should clarify their evaluation details, especially the calculation of bpp.

2. The calibration objective derivation in section 3.2 is similar to the *Network-wise Reconstruction* situation discussed in the existing BRECQ paper (Li et al. 2021b, section 3.2). And the authors are also aware of this prior approach. Intuitively, intra-network independence can be seen as one-block intra-block independence, and BRECQ covers this. In behavior, both the calibration methods adopt an MSE-form objective. Thus, I cannot easily recognize those analyses as the contribution of this paper. I request the authors further clarify their contribution against the existing approaches.

3. It would be better to provide more intuitive explanations of the proposed approach, e.g. diagram figures and pseudo algorithm. Considering that not all experts in the video coding community are familiar with model quantization, the math formulations are somewhat confusing.

### Questions
1. I wonder why the improvement is such impressive, compared to the existing quantization approaches. Is the channel-wise quantization conducted on both weight and activation?
1. It seems like the key point of this approach is to adopt a mix-precision one-block BRECQ on INR video coding models. Despite the story about the unique properties of non-generalized INR models, can we further develop the method to a more general MP PTQ with calibration?
2. Is this inter-layer independence a good property for evaluated INR models, or an ill pose? I would appreciate if the authors provide some insight about this property.

### Soundness
3

### Presentation
3

### Contribution
3
