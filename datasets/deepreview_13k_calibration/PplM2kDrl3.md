# Domain Guidance: A Simple Transfer Approach for a Pre-trained Diffusion Model

- Decision: Accept
- Avg Score: 6.67
- Scores: 6, 8, 6

## Abstract
Recent advancements in diffusion models have revolutionized generative modeling. However, the impressive and vivid outputs they produce often come at the cost of significant model scaling and increased computational demands. Consequently, building personalized diffusion models based on off-the-shelf models has emerged as an appealing alternative. In this paper, we introduce a novel perspective on conditional generation for transferring a pre-trained model. From this viewpoint, we propose *Domain Guidance*, a straightforward transfer approach that leverages pre-trained knowledge to guide the sampling process toward the target domain. Domain Guidance shares a formulation similar to advanced classifier-free guidance, facilitating better domain alignment and higher-quality generations. We provide both empirical and theoretical analyses of the mechanisms behind Domain Guidance. Our experimental results demonstrate its substantial effectiveness across various transfer benchmarks, achieving over a 19.6\% improvement in FID and a 20.6\% improvement in FD$_\text{DINOv2}$ compared to standard fine-tuning. Notably, existing fine-tuned models can seamlessly integrate Domain Guidance to leverage these benefits, without additional training.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces "Domain Guidance" (DoG), a new transfer approach for pre-trained diffusion models aimed at enhancing domain alignment and generating high-quality outputs. DoG builds on classifier-free guidance (CFG) but adapts it to transfer learning by incorporating pre-trained model knowledge to guide the generative process. Through empirical and theoretical analysis, the authors demonstrate DoG’s effectiveness in maintaining pre-trained knowledge, improving image fidelity, and reducing out-of-distribution errors. The results indicate substantial improvements in several metrics (FID and FDDINOv2) across various downstream tasks compared to standard fine-tuning and CFG.

### Strengths
1. DoG’s design as a CFG variant is well-motivated, with clear delineation of the benefits over standard CFG. The illustrations of DoG’s guidance process effectively highlight its domain-alignment benefits.
2. Quantitative results show that DoG significantly outperforms CFG, particularly on datasets with substantial domain shifts. Qualitative results are also compelling, with DoG generating visually consistent images even with increased guidance weights.
3. The paper provides a theoretical foundation for DoG, showing how it maintains domain alignment and mitigates OOD sampling errors, supported by an illustrative analysis using Gaussian mixtures.

### Weaknesses
1. The paper could benefit from more discussion on DoG’s adaptability, particularly in domains vastly different from the pre-trained model’s source domain. Specifically, the analysis should explore scenarios where the target domain exhibits significant distributional differences, such as variations in texture, style, or object composition, compared to the pre-training data. The current evaluation, while demonstrating improvements, does not fully explore the limits of DoG's transfer capabilities in extreme domain shift scenarios.
2. The influence of guidance weights is explored, but further sensitivity analysis could strengthen the understanding of DoG’s stability across diverse settings. The current analysis focuses on a limited range of guidance weights and does not thoroughly investigate the impact of varying these weights across different datasets and model architectures. A more comprehensive analysis should include a wider range of guidance weights and examine their effect on both image quality and domain alignment, potentially revealing optimal ranges for different transfer scenarios.
3. While diverse datasets are used, further tests on varying resolutions and different architectures could better illustrate DoG’s flexibility. The current experiments are primarily conducted on a fixed resolution and a specific diffusion model architecture. It is unclear how DoG would perform with different input resolutions, such as lower or higher pixel counts, or with different diffusion model architectures, such as those employing different attention mechanisms or network depths. This limits the generalizability of the findings and the understanding of DoG's robustness.

### Questions
Please refer to the weaknesses.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This submission proposed a new conditioning method to transfer a diffusion model
 to a new domain named Domain Guidance (DoG).
The idea behind DoG is to pull the generation process toward the target domain
from the pre-trained domain.
Given a pretrained model and fine-tuned version of it, domain guidance guides the process
to the direction that the fine-tuned one indicates and against the pretrained ones's direction.
Theoretical analyses show that DoG mitigates sampling from out-of-distribution area of the target domain.
Experiments show that DoG outperforms CFG in combination with diffusion models finetuned in relatively small
datasets.

### Strengths
- The motivation and idea of DoG is clearly presented, and the paper is overall easy to follow.
- Theoretical analyses and toy examples well depict the advantage of DoG.
- DoG outperformed CFG, a de facto standard method for diffusion guidance with a margin.

### Weaknesses
 - Range of applicable models is not discussed well:
The experiments are conducted with ImageNet-pretrained  DiT-XL/2 and 
but is it mandatory to use the same architecture and initialization weights to perform DoG?
Furthermore, transfering diffusion models to small datasets are often done with LoRA [a] rather than full finetuning.
Is DoG applicable to LoRA-based transfer?
[a] LoRA: Low-Rank Adaptation of Large Language Models 


- Relationship with Autoguidance:
A similar idea is presented in a preprint [b] which uses less-trained version of the model for guidance, 
instead of unfinetuned version in DoG.
Discussing this may be useful, while it it not mandatory due to its unpublished state and missing it should not be penalized.
[b] Guiding a Diffusion Model with a Bad Version of Itself, NeurIPS 2024 to appear.

### Questions
Please see Weaknesses 1.

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work leverages pre-trained knowledge as the domain guidance to guide the model toward the target domain. This work thinks that domain guidance facilitates better domain alignment and higher-quality generations, and provides correlation theoretical analyses.

### Strengths
Originality: The idea of using the pre-trained model as a domain guidance to guide transfer learning is innovative.

Quality and Clarity: The quality of this is satisfactory and the analysis is thoughtful. The paper is well-written, with a thorough and comprehensive ablation study.

Significance. This work provides a contribution to the transfer learning of diffusion learning. In particular, this work can be seamlessly integrated into the existing fine-tuning models without additional training.

### Weaknesses
1. Is there a domain gap between personalized scenarios and general scenarios?
2. During the transfer learning process, does all the knowledge from the pre-trained model need to be effectively utilized?
3. How can the impact of the knowledge in the pre-trained model be assessed in the target domain?
4. For DF-20M (which has no overlap with ImageNet) and ArtBench-10 (whose feature distribution is completely distinct from ImageNet), why can guidance from the model pre-trained on ImageNet lead to better generation?
5. Is the distribution of the downstream domain a subset of the distribution of the pre-trained domain?

### Questions
it is the same as Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3
