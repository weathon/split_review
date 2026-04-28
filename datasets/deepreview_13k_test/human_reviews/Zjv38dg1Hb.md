# Generalized Consistency Trajectory Models for Image Manipulation

- Decision: Accept
- Scores: 8, 8, 3

## Abstract
\vspace{-3mm}
Diffusion models (DMs) excel in unconditional generation, as well as on applications such as image editing and restoration. The success of DMs lies in the iterative nature of diffusion: diffusion breaks down the complex process of mapping noise to data into a sequence of simple denoising tasks. Moreover, we are able to exert fine-grained control over the generation process by injecting guidance terms into each denoising step. However, the iterative process is also computationally intensive, often taking from tens up to thousands of function evaluations. Although consistency trajectory models (CTMs) enable traversal between any time points along the probability flow ODE (PFODE) and score inference with a single function evaluation, CTMs only allow translation from Gaussian noise to data. This work aims to unlock the full potential of CTMs by proposing generalized CTMs (GCTMs), which translate between arbitrary distributions via ODEs. We discuss the design space of GCTMs and demonstrate their efficacy in various image manipulation tasks such as image-to-image translation, restoration, and editing.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
Consistency trajectory models (CTM) are a recent technique for accelerated sampling of diffusion models, which involves training a model to predict any intermediate point of the Probability Flow ODE (PFODE) trajectory allowing traversal between any time points along the PFODE. This work extends CTMs to develop generalized CTMs (GCTMs) using conditional flow matching to enable one-step translation between two arbitrary distributions via ODEs instead of only Gaussian noise-to-data transformation in CTMs. They utilize flow matching to allow more flexible couplings between starting and target distributions, including independent coupling used by diffusion models as a special case. This broadens the applicability of GCTMs to handle arbitrary image-to-image translation tasks in addition to unconditional generation, and reduces the computational costs associated with these tasks by reducing the need for multiple neural function evaluations.

### Strengths
This is overall a nice submission with significant novel technical contributions.

The proposed  generalized CTM is formulated in a principled manner and is explained well.

The paper nicely extends consistency trajectory models to allow translation between arbitrary distributions via flow matching.

The design space is systematically examined, studying the effects of different couplings,  Gaussian perturbation and $\sigma_{max}$ for  stable training.

Experiments are performed on a variety of image restoration and editing tasks in both zero-shot and  supervised manner. In image restoration, the proposed method outperforms consistency models in zero-shot setting, and provides results competitive with supervised regression with a higher perceptual quality.

### Weaknesses
I do not find any major concerns in the paper.

In Fig.6, the noise to image GCTM  editing results with NFE = 1 look a little blurred, with background details washed out.

The authors could consider citing and discussing the following parallel works which also aim to perform image-to-image tasks with few NFEs:
Mei etal. CoDi: Conditional Diffusion Distillation for Higher-Fidelity and Faster Image Generation. In CVPR 2024
Zhao etal. CoSIGN: Few-Step Guidance of ConSIstency Model to Solve General INverse Problems. In ECCV 2024
He etal. Consistency Diffusion Bridge Models. In NeurIPS 2024.
Xiao etal. CCM: Real-Time Controllable Visual Content Creation Using Text-to-Image Consistency Models. In ICML 2024
Starodubcev etal. Invertible Consistency Distillation for Text-Guided Image Editing in Around 7 Steps. Arxiv June 2024.

### Questions
Can you provide the details of computational costs, and training time required for GCTM, and compare this with  CTM, and the  teacher model?


In CTMs [Kim et al., 2024b], adversarial training can be incorporated to further enhance the quality of samples. Can adversarial training also be incorporated in the proposed GCTMs?

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper proposes Generalized Consistency Trajectory Models (GCTMs), which extend Consistency Trajectory Models (CTMs) to support sampling from arbitrary distributions rather than being restricted to Gaussian distributions. By reparameterizing the flow matching (FM) ODE in a way analogous to CTMs, the authors provide a general framework that includes CTMs as a special case when the sampled distributions is Gaussian. The paper also explores the design space of the proposed method. The proposed method achieves state-of-the-art performance in multiple image generation and manipulation tasks without relying on pre-trained teacher models.

### Strengths
* The paper is theoretically sound and inspring in that: 
(1) The reparameterization of the FM ODE to resemble the CTM form allows the proposed GCTM to perform consistent trajectory sampling between arbitrary distributions, which is highly flexible and useful.
(2) GCTM is rigorously shown to generalize CTMs. This makes it possible to train the GCTM using the same training stratagies for training CTMs. 

* The paper includes exploration of the design space for the proposed model, such as OT coupling for accelerated sampling (~2.5x as the baseline), Gaussian perturbation for more diverse generation. 

* GCTM achieves state-of-the-art results across various applications, such as image restoration and translation, without needing a pre-trained teacher model.

### Weaknesses
*Gaussian Perturbation in Section 4.1:

The introduction of Gaussian perturbation seems contradictory to the main goal of GCTM - sampling from arbitrary distributions. Specifically, in the case of multiple labels corresponding to a single observation (L302-303), Gaussian perturbation does not apply necessarily, as these label variations are not expected to follow an iid Gaussian distribution.

*Lack of teacher model distillation training scheme:

The reason for the absence of distillation from a teacher network is not fully addressed, although the method is claimed to be a generalization of CTM method. Given that distilling from a teacher could potentially improve training efficiency, an explanation for this choice would strengthen the paper.

*Performance gap with iCM:

GCTM does not outperform improved Consistency Models (iCM), but the reason for this gap is not fully explored. A deeper analysis of this performance difference would be valuable.

### Questions
Please refer to the weakness section above.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This work presents "GENERALIZED CONSISTENCY TRAJECTORY MODELS" a generative model framework that allows consistency trajectory models for arbitrary coupling of image distribution while the original approach of CTM is restricted to the classical (image, pure noise) independent coupling.

### Strengths
The paper is a mixed approach of CTM and Conditional Flow Matching that is rigorous.
The theoretical presentation is new as far as I know.

While this is surely of interest, in its current state, the quality of the presentation and the quality of the experiments are not high enough for a pulication at ICLR.

### Weaknesses
The main issue of this paper is that CTM is not used on high-resolution images.
The community does not need methods for 64x64 image processing, this resolution is not high enough to assess image to image translation or image restoration.
In comparison,

Unpaired Image-to-Image Translation via Neural Schrödinger Bridge
Download PDF
Beomsu Kim, Gihyun Kwon, Kwanyoung Kim, Jong Chul Ye
ICLR 2024
uses 256x256 and 512x512 and discuss difficulty for other methods to be of higher resolutions.

As another recent example,
Extremal Domain Translation with Neural Optimal Transport
Milena Gazdieva, Alexander Korotin, Daniil Selikhanovych, Evgeny Burnaev
NeurIPS 2023
uses 64x64 and 128x128 examples (already to low in my opinion).

Also comparison with the original pix2pix GAN method is not fair using 64x64 resolution since it is based on a local patch-based discriminator (less resolution means less patches to analyze).


l. 425  "we demonstrate image restoration task of GCTM on ImageNet with higher resolution (256 × 256 resolution) to demonstrate it scalability."
There is no comparison done in the appendix.
Comparison with few NFE and many NFE methods (eg DPS, [Chung & Kim et al ICLR 2023]) is necessary to assess the performance.


All the background section is written without references.
Especially, Section 3.3 FLOW MATCHING (FM) seems far from the original paper by Lipman et al, at least in notation.
Is it just a reinterpretation of CFM using diffusion-like notation?


Another main issue is the use of Optimal Transport coupling (l. 255 (Entropy-regularized) Optimal transport coupling).
This is a chicken and egg problem. If one knew the OT coupling presented by Equation (24) this would be a very good generative model (the best one in a sense) and we would not require a CTM.
What is done in practice is Algorithm 3 Sinkhorn-Knopp (SK) (l. 760) with two batches of size M.
(on a side remark, I don't understand why using entropy regularization here instead of computing an optimal assignment (eg using the emd function from the POT library) unless the batch size M is larger than 1000. This would ensure to use all the data.)
Anyway, there is a big gap between equation (24) which is continuous and discrete algorithm restricted on two discrete batches. Expressing the coupling in continuous space resulting from this discrete procedure is probably intractable (and far from Equation (24)).
This is linked with l. 361: We postulate this is because (1) OT coupling leads to straighter ODE trajectories.


Sampling algorithm and details are missing. This sentence is hard to understand "especially when we use a smaller number of timesteps N (l. 323)". Is gamma sampling from [Kim, Lai et al 2024] used?


Table 1: The CTM paper [Kim, Lai et al 2024] reports FID of 1.98 for Diffusion Models – Distillation Sampling with NFE = 1. What is the 5.28 FID reported here?


The Theorems are more Propositions since their proofs only involves reparameterization of ODE/expectation.


Minor corrections / suggestions:
* l. 170 eq (9): There is a cohabitation of [0,T] and [0,1] convention (change x1 in xT)
* l. 245: joint distributions of q(x0) and q(x1) (speak of q(x0,x1) instead ?)
* l. 253:  add with normal distribution
* l. 269 is hard to inderstands. An ODE as t tends to 0 does not have a rigorous meaning.
* Many references point to ArXiv papers while published at conferences or journals (l. 544, l. 547, l. 553, ...)

### Questions
What is the value for the batch size M used for OT-based couplings ?

Table 1: The CTM paper [Kim, Lai et al 2024] reports FID of 1.98 for Diffusion Models – Distillation Sampling with NFE = 1. What is the 5.28 FID reported here?

### Soundness
2

### Presentation
2

### Contribution
2
