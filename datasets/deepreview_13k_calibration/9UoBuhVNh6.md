# Applications of Modular Co-Design  for De Novo 3D Molecule Generation

- Decision: Reject
- Avg Score: 6.33
- Scores: 5, 8, 6

## Abstract
De novo 3D molecule generation is a pivotal task in drug discovery. However, many
recent geometric generative models struggle to produce high-quality 3D structures,
even if they maintain 2D validity and topological stability. To tackle this issue
and enhance the learning of effective molecular generation dynamics, we present
Megalodon–a family of simple and scalable transformer models. These models
are enhanced with basic equivariant layers and trained using a joint continuous
and discrete denoising co-design objective. We assess Megalodon’s performance
on established molecule generation benchmarks and introduce new 3D structure
benchmarks that evaluate a model’s capability to generate realistic molecular
structures, particularly focusing on energetics. We show that Megalodon achieves
state-of-the-art results in 3D molecule generation, conditional structure generation,
and structure energy benchmarks using diffusion and flow matching. Furthermore,
we demonstrate that scaling Megalodon produces up to 49x more valid molecules
at large sizes and 2-10x lower energy compared to the prior best generative models.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
In this paper, the authors propose a method for unconditional 3D molecule generation. The proposed approach, called Megalodon, represents molecules with both 3D structure and 2D topology information (atom coordinates and types, bond types and formal charge). The model uses a transformer-based architecture and either diffusion or flow-matching generative model. The proposed approach achieves positive results on experiments on GEOM-drugs dataset.

### Strengths
- The task of molecule generation is important and worth investigating (although the utility of _unconditional_ generation can be discussed)
- The paper achieved good experimental results on GEOM-drugs dataset.
- The paper shows that having a better architecture (ie transformer) and more parameters can help on GEOM-drugs molecule generation.

### Weaknesses
 - The paper is not very well written and could be improved. In particular, there is a lot of training/evaluation details missing, making reproducibility challenging. 
- The paper lacks novelty. The paper uses well-stablished generative models (diffusion or flow matching, already used many times on this task) on a single standard dataset (GEOM-drugs). 
- Many of the parameters choices were made ad hoc. It would be great to see some ablation studies to justify many of the architecture choices made by the authors (eg, the self conditioning, the modifications on DiT architecture).
- The authors only show results in one single dataset (GEOM-drugs). It would be nice to see results in other datasets to make sure results are generalizable, eg QM9, PubChem3D, or other related tasks that relies on different dataset (eg, structure-condition generation instead of only conformer generation), etc.
- The paper misses a lot of references/comparison to related works: eg, GeoLDM (Xu et al, ICML23), VoxMol (Pinheiro et al, NeurIPS23), GeoBFN (Song et al, ICLR24). All these works also explore the problem of unconditional molecule generation. Moreover, the authors wrongly cite MolDiff (Xu et al 23), mentioning that they dont model bond, while they actually do (L120).

### Questions
- Why use only a subset of the metrics proposed by the MiDi paper on Table 1, instead of all the metrics? Also, why ignore the "3D distributional" metrics from MiDi?
- Could the authors elaborate more on how the "self-conditioning" is applied? WHy the choice of using it vs not using it? What is the contribution of self conditioning? 
-  DiT is a model created to operate on images and much of its inductive bias operate on that data domain. Why did the authors decide to use DiT on their model? What about any other transformer-like architecture? DiT also has a autoencoder to go from pixel to latent space, and it seems that the proposed model does not have that.
- From my understanding, the architecture is composed of equivariant and non-equivariant layers (which end up being a non-equivarant model). Is this correct? If so, why this design choice?
- Could the authors elaborate on why did the proposed model is able to generate conformations from molecular graph, while EQGAT-Diff does not? From my understanding the only difference between the two models is the neural network architecture, and it seems quite surprising that this makes such a difference on teh results.

### Soundness
3

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This work presents a transformer-based diffusion and flow matching framework for the co-design of 2D and 3D molecular structures. The coordinate, atom and bond features of the noisy molecule are aggregated through DiT blocks and then used to reconstruct the 3D and 2D structures with an EGNN layer. The authors establish the model architecture for both diffusion and flow matching. The proposed model shows higher generation quality in both manners, especially for larger molecules.

### Strengths
1. The proposed model shows overall higher performance, especially on the more challenging task of generating larger molecules, while also having better memory efficiency than the previous models. 
2. The authors perform comprehensive analysis of the interplay between the 2D graph and 3D structure during molecular generation in previous methods, and offer potential solutions to improve the dependency between the modalities. 
3. This paper also attempts to build a framework adaptable to multiple training methods (diffusion and flow matching), which would be informative for future studies.
4. The authors also offer additional benchmark tasks and metrics for evaluating 3D molecule generation.

### Weaknesses
See Questions.

### Questions
1. How is equivariance preserved? From Appendix B.1.3, it seems the structure blocks should also take the input coordinates and combine them with the DiT block output to update the structure. Intuitively, there should be a skip connection from the input 3D coordinates to the structure blocks. Otherwise the coordinate information would be lost. However, Fig 1 indicates the DiT blocks and structure layers are sequential, where the structure blocks only take the DiT output (which is invariant) to predict the structure. Could the authors clarify on this?
2. For conditional generation, how is the 2D graph information provided to the diffusion model?

### Soundness
4

### Presentation
4

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
This paper proposes Megalodon, a transformer-based model for 3D molecule generation. Megalodon is a modular approach with both diffusion and flow matching objectives that aim to improve 3D structure prediction and validity. The authors conducted experiments on existing benchmarks such as GEOM Drugs and introduced new metrics such as xTB relaxation error. The results indicate Megalodon outperforms existing methods in molecule stability, validity, and energy.

### Strengths
1. The proposed Megalodon is an adaptive architecture that can be adapted with both diffusion and flow matching objectives.

2. The newly introduced benchmarks including energy-based and 3D structure-based assessments are more aligned with practical applications in molecular design and drug discovery.

3. The experimental results are promising, especially along the metrics related to 3D structures.

### Weaknesses
My major concern is the limited technical novelty. The network architecture of Megalodon uses standard DiT models, with only minor modifications such as the structure layer. While the authors introduce a combination of diffusion and flow matching objectives, this integration alone does not constitute a major advancement, as flow matching is a theoretically more general framework than diffusion. There is no surprise that these two objectives can be used in one framework.

### Questions
See weakness.

### Soundness
3

### Presentation
3

### Contribution
3
