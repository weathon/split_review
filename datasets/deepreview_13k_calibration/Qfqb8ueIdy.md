# A Unified Framework for Consistency Generative Modeling

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 3, 6, 6

## Abstract
Consistency modeling, a novel generative paradigm inspired by diffusion models, has gained traction for its capacity to facilitate real-time generation through single-step sampling. While its advantages are evident, the understanding of its underlying principles and effective algorithmic enhancements remain elusive. In response,  we present a unified framework for consistency generative modeling, without resorting to the predefined diffusion process. Instead, it directly constructs a probability density path that bridges the two distributions. Building upon this novel perspective, we introduce a more general consistency training objective that encapsulates previous consistency models and paves the way for innovative, consistency generation techniques.  In particular, we introduce two novel models: Poisson Consistency Models (PCMs) and Coupling Consistency Models (CCMs), which extend the prior distribution of latent variables beyond the Gaussian form. This extension significantly augments the flexibility of generative modeling. Furthermore, we harness the principles of Optimal Transport (OT) to mitigate variance during consistency training, substantially improving convergence and generative quality. Extensive experiments on the generation of synthetic and real-world datasets, as well as image-to-image translation tasks (I2I), demonstrate the effectiveness of the proposed approaches.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a unified framework for consistency generative modeling by introducing two models: Poisson Consistency Models(PCMs) and Coupling Consistency Models(CCMs). The overall training pipeline stays similar to the original Consistency Models. The PCMs attempt to replace the Gaussian distribution of the latent variables in the diffusion models with the Poisson distribution while the CCMs introduce a tuple of random variables to replace the Gaussian distributions. The paper also utilizes Opticmal Transport to further improve the performance of CCMs. Results are shown on a toy dataset and CIFAR-10.

### Strengths
1. Speeding up the diffusion models is an important problem and consistency training has been shown to be an effective way to achieve this.
2. Results on the toy experiments and CIFAR-10 show that the proposed methods improve over the baselines regarding of FID.

### Weaknesses
1. The evaluation is weak. The paper only conducts quantitative comparisons on a toy dataset and CIFAR-10.
2. As in the Consistency Models paper, the consistency distillation method generally performs better than consistency training. However, the paper does not provide any results or comparisons for this.

### Questions
The key contribution that goes beyond the gaussian distribution by replacing the gaussian distribution with either poisson distribution or a joint distribution seems to not specific to the training of consistency models but also the vanilla diffusion models. Could the authors clarify more for on this?

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work proposed a generalized formulation of the Consistency Model [CM, Song et al. 2023], a recent advanced in diffusion generative modeling that enable few number of function evaluation (usually only 1 or 2 NFEs)-sampling but high-quality samples. The authors show that CM can be generalized into a general form with affine probability path that admits a velocity field. This results in an equivalent form continuity equation that describes the dynamic of the probabiliy density path. Equip with this general form, the authors proposed two additional extension of CM, called Poisson consistency model (PCM), based on formulation of the probability path showed in [Xu et al 2022], and Coupling consistency model (CCM), based on the linear probability path of flow matching framework [Lipman et al 2023, Liu et al 2023, Albergo & Vanden-Ejinden 2023]. The authors demonstrate the effectiveness of their proposed methodologies with numerical experiments on unconditional image generation task (CIFAR10) and unpaired image-to-image translation (AFHQ Cat-Dog/Wild-Dog). 



Song, Y., Dhariwal, P., Chen, M. &amp; Sutskever, I.. (2023). Consistency Models. In Proceedings of Machine Learning Research202:32211-32252 Available from https://proceedings.mlr.press/v202/song23a.html.

Xu, Y., Liu, Z., Tegmark, M., & Jaakkola, T. (2022). Poisson flow generative models. Advances in Neural Information Processing Systems, 35, 16782-16795.

Yaron Lipman, Ricky TQ Chen, Heli Ben-Hamu, Maximilian Nickel, and Matt Le. Flow matching for generative modeling. arXiv preprint arXiv:2210.02747, ICLR 2023.

Liu, Xingchao, Chengyue Gong, and Qiang Liu. "Flow straight and fast: Learning to generate and transfer data with rectified flow." arXiv preprint arXiv:2209.03003. ICLR 2023.

Albergo, Michael Samuel, and Eric Vanden-Eijnden. "Building Normalizing Flows with Stochastic Interpolants." In The Eleventh International Conference on Learning Representations, 2023.

### Strengths
Well written and structured paper that is easy to pass through. The main goal of improving and generalizing consistency model framework is well-motivated.

### Weaknesses
I have two main concerns for this paper.

1. **Question mark on novelty:** the idea of writing continuity equation and probability path is not new, and many derivations  from the generalized CM in this paper are followed exactly from [Lipman et al 2023] on flow matching generative models. The formulation of Couping Consistency Model (CCM) -- section 3.4, which is this work's most well-performed framework empirically, the authors again borrowed heavily from previous work of [Lipman et al. 2023] with the linear path $x_t = tx_1 + (1-t)x_0$. Equation (20) and the idea of CCM-OT on learning probability path with joint distribution to reduce training loss variance is straightforward taken from Multisample Flow matching paper [Pooladian et al. 2023, Section 3], but surprisingly there was no mention of this citation around this equation.

2. **Question mark on the results of empirical evaluation:** although the results provided with 1 NFE sampling for CIFAR10 in table 2 and 3 showed that CCM-OT outperformed original CM (denoted DCM in this paper) of [Song et al. 2023], I do not understand where the authors got the FID score of 18.4 for DCM to begin with. In [Song et al. 2023], it is clearly stated that their model reached 1-NFE FID 3.55 & 8.70 with distillation and without distillation, respectively. Therefore, I urge the authors provide a clear explanation on the discrepancy between the reported numbers of the baseline. Moreover, DCM also provided more extensive experiments with ImageNet 64x64 and LSUN Bedroom 256x256, and although I understand the lack of computational resources, I advise the authors to provide results on more datasets for better understanding the gains of their proposed methods compared with baselines, which should also included distillation techniques such as Progressive distillation [Salisman & Ho 2022].

### Questions
See weaknesses.

### Soundness
2 fair

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces a unified and comprehensive framework for consistency generative modeling. In particular, it introduces two novel models: Poisson Consistency Models (PCMs) and Coupling Consistency Models (CCMs), which extend the prior distribution of latent variables beyond the Gaussian form. Additionally, it incorporates optimal transport (OT) to improve the performance of these models further. Through empirical experiments, it demonstrates the effectiveness of the proposed framework across a range of generative tasks.

### Strengths
This paper generalizes consistency models beyond the Gaussian form. In particular, it introduces two novel models: Poisson Consistency Models (PCMs) and Coupling Consistency Models (CCMs) with theoretical analysis. And comprehensive experiments show advantages compared to other diffusion models on both synthetic and real-world datasets, such as unconditional generation of CIFAR-10 and unpaired image-to- image translation (I2I) using AFHQ.

### Weaknesses
1. the notation is a little confusing, which makes the paper hard to follow.
2. The  reverse diffusion process with gaussian noise can reconstruct the original clear image from the noisy version step by step, it would be better to show some figures using PCMs and CCMs.

### Questions
From Eq. 22 and 23, it shows that the continuity equation holds with or without condition z, then what is the physical meaning for z?

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
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper propose a way to unified three different views to formulate consistency model. This framework can inspires different design of consistency losses, and the paper demonstrate that such design can potentially lead to better consistency models. The paper is largely evaluated on three tasks, one is a toy 2D dataset, and then two image generations tasks. The results show that the new

### Strengths
- This theoretical framework that could unify multiple works (Poisson, Coupling, etc) and provide insight for developing new algorithm. To the best of my knowledge, this can be a useful contribution to the community. But I’m not an expert in generative model theory so I will need to defer this to other reviewers as well.

### Weaknesses
 - Both proposed algorithm (PCM and CCM-OT) seems to require additional computes during training. For PCM, the weighted sum is computed through all x_i in the batch and for CCM-OT, the optimal transport is computed among the batch. These operations are not scaling very trivially with the batch-size, while to the best of my knowledge, consistency model seems to work better with larger batch size (e.g. 512 and in this paper case 256). Specifically, the PCM weighted sum requires a full pass over the batch for each sample, which could become a bottleneck with larger batch sizes. Similarly, the optimal transport calculation in CCM-OT, while potentially beneficial, involves solving a linear program, which has a computational complexity that scales super-linearly with the batch size. This could limit the practical applicability of the method, especially when compared to other consistency models that can leverage larger batch sizes more efficiently.

 - the final algorithm is not very clear to me by reading the main paper, there are several tricks proposed. It would be great to have the algorithm written out in the main paper rather than in the appendix.

### Questions
- the final algorithm is not very clear to me by reading the main paper, there are several tricks proposed. It would be great to have the algorithm written out in the main paper rather than in the appendix.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
