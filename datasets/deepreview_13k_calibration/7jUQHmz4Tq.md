# D3AD: DYNAMIC DENOISING DIFFUSION PROBABILISTIC MODEL FOR ANOMALY DETECTION

- Decision: Reject
- Avg Score: 3.00
- Scores: 3, 3, 3

## Abstract
Diffusion models have found valuable applications in anomaly detection by capturing the nominal data distribution and identifying anomalies via reconstruction. Despite their merits, they struggle to localize anomalies of varying scales, especially larger anomalies like entire missing components. Addressing this, we present a novel framework that enhances the capability of diffusion models, by extending the previous introduced implicit conditioning approach \cite{DBLP:conf/iclr/MengHSSWZE22} in three significant ways. First, we incorporate a dynamic step size computation that allows for variable noising steps in the forward process guided by an initial anomaly prediction. Second, we demonstrate that denoising an only scaled input, without any added noise, outperforms conventional denoising process. Third, we project images in a latent space to abstract away from fine details that interfere with reconstruction of large missing components. Additionally, we propose a fine-tuning mechanism that facilitates the model to effectively grasp the nuances of the target domain. Our method undergoes rigorous evaluation on two prominent anomaly detection datasets VISA and BTAD, yielding state-of-the-art performance. Importantly, our framework effectively localizes anomalies regardless of their scale, marking a pivotal advancement in diffusion-based anomaly detection.  All code will be made public upon acceptance.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes an approach termed dynamic denoising diffusion probabilistic model (D3AD) for the task of anomaly detection. D3AD designs a pipeline with three specific components: (i) a dynamic conditioning mechanism based on KNN, (ii) a domain adaptation mechanism that aims to learn the representation in the target domain, (iii) a latent diffusion model for reconstruction. D3AD achieves SOTA performance on some metrics in two datasets.

### Strengths
•	This paper proposes a novel dynamic noise injection mechanism that makes sense.

•	 The performance gains for anomaly localization look good, especially on PRO metric.

### Weaknesses
•	D3AD has not been validated on the most widely used dataset, MVTec[1], and I'm curious about its performance on this dataset.

•	The impact of the dynamic noise amount on the reconstruction results is not clear from this paper, and it appears that the reconstruction quality is not very good based on Figure 3.

•	The novelty of this work is very limited. The proposed conditioned denoising and domain adaptation are similar to DDAD[2]. Besides, the anomaly scoring paradigm is similar to RD4AD[3]. As a result, the framework of D3AD looks like a combination of existing works.

•	D3AD performs poorly on Image AUROC compared to the diffusion-based methods mentioned in the paper, such as DDAD and DiffusionAD.

### Questions
•	Is there more detailed experimentation or theoretical basis to explain why noise is not needed during inference?

•	Are there more visual results showcasing the reconstruction of different types of anomaly regions?

•	How does D3AD perform on MVTec, which is one of the most widely used datasets?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper presents a new framework called D3AD that aims to resolve the issue of localizing anomalies of varying scales using diffusion models. The framework enhances the capability of diffusion models by integrating a dynamic conditioning mechanism with prior information from a KNN model, a domain adaptation mechanism, and a specialized latent diffusion model. The proposed method is supported by thorough evaluation and analysis and demonstrates superior performance on two benchmark datasets.

### Strengths
1) The paper introduces novel contributions to the field of anomaly detection using diffusion models. including dynamic conditioning, noiseless input scaling, and latent diffusion model.
2) The proposed method achieves state-of-the-art performance on two benchmark datasets, VisA and BTAD, demonstrating its effectiveness in anomaly detection and localization.

### Weaknesses
1) The paper introduces novel contributions to the field of anomaly detection using diffusion models. including dynamic conditioning, noiseless input scaling, and latent diffusion model.
2) The proposed method achieves state-of-the-art performance on two benchmark datasets, VisA and BTAD, demonstrating its effectiveness in anomaly detection and localization.

### weaknesses:
 1) The paper provides a well-structured framework, but the explanation of each component lacks clarity and precision. In addition, the paper lacks verification of the validity of some arguments.
2) The description of some methods used in the paper is obscure. For example, the paper does not provide a clear and rigorous mathematical explanation of the proposed DIC method, but only a short description of it.
3) Some of experimental results in the paper lack detailed discussions. For example, the paper lacks careful analysis of qualitative results and does not link experimental results to the proposed methods logically.
4) The paper is imprecise and unpolished. There are a number of grammatical errors in the text, so careful checking and revision is recommended.

### Questions
There are some key details missed so that it is difficult to draw convincing conclusions:
1)	How did you determine an noiseless and only scaled input $x_{\hat T}$ is optimal for faithful reconstruction?
2)	Why did you chose |B|=10?
3)	What is meaning of “unnoised”? It would be better to replace “unnoised” with “noiseless”.
4)	Could you please elaborate the qualitative effect of DIC based on Figure 6?
5)	How did you localize and detect anomalies of varying scales? The main body lacks a detailed description of the solution to this problem and the corresponding experimental analyses.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper proposes D3AD, an anomaly detection method based on the pre-trained diffusion model. Authors propose two components that deviate from the conventional works; dynamic implicit conditioning which selects dynamic time steps for noising and guidance based on the reference latent that is not constructed by adding noise. Such contributions are integrated with domain adaptation strategy and final anomaly map reconstruction to consist of D3AD.  Authors experiment with D3AD in the VisA and BTAD datasets.

### Strengths
(1) The idea of dynamic time for anomaly detection is interesting.

### Weaknesses
The paper has various issues on soundness and significance. Specifically, I am confused about why the proposed method should work, given that the method comprises differences against existing diffusion-based anomaly detection. Further, unlike the authors insist, D3AD misses various benchmarks, competitive baselines, and even metrics for comparison. Below are my specific details on the issue I have on this paper.

**Originality & Soundness & Clarity** 
(1) The paper overclaims about the domain adaptation technique. DDAD [1] also uses a similar objective to fine-tune the feature extractor. I would rather appreciate that the authors lower the tone.
(2) The authors formulate reference $z_{\hat{T}}$ as a multiplication of the latent without any noise addition. However, I do not find any support for why such guidance on the latent should work. The authors may elaborate on why this helps in detail via further analysis.
(3) I do not understand how the binary search function $\psi$ can choose the right time on the bin. Further details should be provided on how this works or at least introduce related concepts.
(4) I am also confused about how the method constitutes a "predefined histogram" in Figure 3.

**Significance**
(1) The authors claim their methods show **state-of-the-art** performance but I doubt this is true. For example, [2] scores I-AUC of 97.6, P-AUC of 98.4, and PRO of 94.9 while this method scores 96.0/97.9/94.1. I don't feel that this method outperforms DDAD even since DDAD scores 99.3 I-AUC in the VisA dataset, which is somehow not shown in Table 1. The authors should compare all the baselines in previous conferences (e.g. ICML, CVPR, ICCV) to support this bold claim.
(2) I also feel like three metrics least (I-AUROC, P-AUROC, p_PRO) should be compared as a whole in the major table (e.g. Table 1).
(3) I am curious why the authors dropped the MvTec dataset for comparison since most anomaly detection algorithms are compared in the dataset. It is hard to assert that the method shows state-of-the-art performance without comparing the MvTecAD dataset in my opinion.
(4) Even addressing this issue, I am confused about the gain of this paper since the proposed model uses a latent diffusion model, unlike the other diffusion-based methods.
(5) Furthermore, diffusion-based methods show slow sampling speed due to computation-heavy U-Nets and multiple inference steps. It would be beneficial to note the computational cost of this method compared to competitive baselines.

### Questions
see Weakness


**References**\
[1] Anomaly detection with conditioned denoising diffusion models, arXiv 2023\
[2] Remembering normality: memory-guided knowledge distillation for unsupervised anomaly detection, ICCV 2023

### Soundness
1 poor

### Presentation
2 fair

### Contribution
1 poor
