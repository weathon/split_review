# The Latent Road to Atoms: Backmapping Coarse-grained Protein Structures with Latent Diffusion

- Decision: Reject
- Scores: 5, 3, 5, 3

## Abstract
Coarse-grained(CG) molecular dynamics simulations offer computational efficiency for exploring protein conformational ensembles and thermodynamic properties.
Though coarse representations enable large-scale simulations across extended temporal and spatial ranges, the sacrifice of atomic-level details limits their utility in tasks such as ligand docking and protein-protein interaction prediction.
\textit{Backmapping}, the process of reconstructing all-atom structures from coarse-grained representations, is crucial for recovering these fine details.
While recent machine learning methods have made strides in protein structure generation, challenges persist in reconstructing diverse atomistic conformations that maintain geometric accuracy and chemical validity.
In this paper, we present Latent Diffusion Backmapping (LDB), a novel approach leveraging denoising diffusion within latent space to address these challenges. 
By combining discrete latent encoding with diffusion, LDB bypasses the need for equivariant and internal coordinate manipulation, significantly simplifying the training and sampling processes as well as facilitating better and wider exploration in configuration space.
We evaluate LDB’s state-of-the-art performance on three distinct protein datasets, demonstrating its ability to efficiently reconstruct structures with high structural accuracy and chemical validity.
Moreover, LDB shows exceptional versatility in capturing diverse protein ensembles, highlighting its capability to explore intricate conformational spaces. 
Our results position LDB as a powerful and scalable approach for backmapping, effectively bridging the gap between CG simulations and atomic-level analyses in computational biology.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes a new framework for backmapping, called Latent Diffusion Backmapping (LDB). This method uses a VQ-VAE to discretize local all-atom structures into a codebook latent space. The diffusion model is then trained on this latent space distribution, so that during inference, the latent variables are generated conditioned on the CG structure and then mapped back to all-atom structures via the VQ-VAE decoder.

### Strengths
The model shows good structural accuracy and chemical validity.
The usage of latent diffusion for backmapping is new. Discretization of the local geometry for backmapping has been previously explored (Chennakesavalu & Rotskoff, 2024) using rotamer libraries, but the learnable discretization (via VQ-VAE) proposed by this paper is original and reasonable.

(Chennakesavalu & Rotskoff, 2024) Data-efficient generation of protein conformational ensembles with backbone-to-side chain transformers, J. Phys. Chem. B 2024, 128, 9, 2114–2123

### Weaknesses
While I think the modeling choices like discretization and latent diffusion make sense and are meaningful, the evidence of their advantages is not convincing, primarily due to the lack of evaluation on diversity or distribution matching between the ground truth and sampled conformations.
In GenZProt paper, diversity and the Earth Mover’s Distance (EMD) scores are reported in Appendix A, and there are qualitative analysis of diversity/distribution matching in Figure 8. In DiAMoNDBack paper, the diversity score is reported with the comparison with GenZProt in Table 1 and 2, and there are both quantitative (in JSD) and qualitative analysis of the generated distributions in Figure 5.
Since the paper is tacking the ‘backmapping’ problem, which aims to reconstruct the fine-grained conformational ensemble conditioned on the CG structure, rather than protein side chain packing (PSCP), which might suffice to find a single probable fine-grained structure, some evaluation on the generated ensemble’s diversity and distribution matching is required.
Moreover, the paper claims “Diffusion leverages stochastic noise, which allows for exploration across diverse conformations while maintaining structure validity. This is evident in the RMSD and Clash metrics, where our diffusion-based model consistently achieves better results. (line 485-505)“. The structure validity claim is well-supported by RMSD, GED, Clash, Interaction, GDR scores, but there is no evidence for the conformational diversity claim.
I have a concern that the discretized latent space would be bad for generating diverse structures despite being better at generating chemically valid structures. So it would be great if the authors can show that the discretization does not harm the diversity. If the authors provide diversity and distribution matching evaluations, I am willing to consider increasing the rating.

### Questions
A different paper was used to cite GenZProt in Section 5.1, instead of (Yang & Gomez-Bombarelli, 2023).

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper develops a model for backmapping coarse-grained protein structure. The model architecture consists of two parts (1) a VQ-VAE is trained to map all-atom structures into a discrete latent associated with each amino acid residue (2) a GNN is trained to generate these discrete latents from the coarse grained structure via diffusion. The method is assessed on PED, ATLAS, and PDB structures and is shown to outperform recent methods GenZProt and DiamondBack.

### Strengths
* The proposed latent diffusion approach has not been previously developed for the backmapping task. The approach is reasonable and appears to be effective.
* By encoding the all-atom coordinates into node-level latents in a graph, the dimensionality of the generative modeling task is reduced.
* The encoding and decoding of the latents from internal coordinates helps ensures that decoded structures are chemically valid.

### Weaknesses
**Originality**
* Although the approach is reasonable and well-motivated, it amounts to a relatively straightforward application of currently popular ideas. Latent diffusion and discrete tokenization have been well explored in many related contexts, including protein structure. There are not any aspects of the model design that seem particularly surprising or insightful.
* To improve on this axis, the paper should present nonobvious and/or nontrivial conceptual development that motivates the methodology.

**Quality**
* The experimental validations are brief and are of average quality. Given that the method is generative, i.e., produces a backmapped distribution, it is surprising that there are no distributional accuracy metrics. Chemical validity is also a rather low bar that can be passed by any heuristic reconstruction + relaxation. Some other metrics introduced by the authors are not well justified or explored.
* To improve on this axis, the paper should present evaluations that go beyond than existing works in this space. Some suggestions include, e.g., energies, distributional similarities, or metrics used by the PDB in validating atomic models. Since there is a smaller body of ML work on this task, case studies or similar experiments would better make the case that the improvements are meaningful (and not just incremental).

**Clarity**
* The paper's structure is a little odd, placing a lot of emphasis on architectural and training details but deferring dataset and evaluation details to the appendix. I would recommend swapping this because the task is relatively unfamiliar to the ML audience.
* The paper contains many overly verbose "filler phrases" that repeat similar points and do not add much to the exposition. Some examples of what I mean (there are many, many more):

> Such dynamics lead to distinctive conformational variations, which contribute to the diverse functions
of proteins and are of great significance for maintaining normal features in vital organisms. (What are "distinctive variations", "normal features", or "vital organisms"?)

> Despite challenges posed by the scarcity and uneven distribution of protein conformation data, we
employed a Vector Quantized Variational Autoencoder. (What is an "uneven distribution"? Why does scarcity contraindicate a VQ-VAE, and why did you proceed with one anyways?)
 
These are just rhetorical questions --- my point is that the authors do not need to say these things if there is not a clear reason to say them. In general my sense is that the introduction could be trimmed by an entire page without loss of meaning.

* To improve on this axis, the paper should be significantly rewritten for concision and clarity, and should focus on explaining things less likely to be familiar to the audience.

**Significance**

In sum, although the work does technically advance the state of the art on this task, in my opinion the significance of the results and novelty of the method do not quite meet the bar for ICLR.

### Questions
* "Residues with fewer than 13 heavy atoms are excluded." Most amino acids have fewer than 13 heavy atoms. Could the authors clarify?
* How are the internal coordinates defined exactly? Why are there 13 bond lengths, bond angles, and dihedral angles?
* "The network processes three inputs: node coordinates, atom types, and an initial noise vector." Why are atom types still involved at the latent diffusion stage?

### Soundness
3

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper presents Latent Diffusion Backmapping (LDB), a novel approach for backmapping coarse-grained protein structures. LDB combines discrete latent encoding with diffusion to address challenges in reconstructing atomistic conformations. Results on multiple datasets demonstrate its state-of-the-art performance and versatility.

### Strengths
- LDB effectively addresses the challenges of limited exploration in conformational space and accurately reconstructs all-atom 3D protein structures from coarse-grained representations. 
- The use of discrete latent representations simplifies the diffusion process and improves overall efficiency, while also enhancing structural accuracy and chemical fidelity. 
- The evaluation of LDB on multiple diverse protein datasets demonstrates its state-of-the-art performance and versatility, highlighting its potential for practical applications in computational biology.

### Weaknesses
The presentation of the method is not very clear. Feel free to correct me if there are any misunderstandings.

- In line 243, an SE(3)-equivariant GNN is used to output bond lengths, angles, etc. Does this indicate that an equivariant network generate an invariant representation? In line 284, the input of ProteinMPNN is CG models. Why does a CG model contain the atom type? 
- In line 286, why do you add noise to the CG model? In my opinion, it serves as a condition into the network, like the BERT in text-to-image models. But in Stable Diffusion, we never add noise to text embeddings.
- In line 295, how do you parameterize the epsilon-theta? Is it the ProteinMPNN?

More ablation studies are required. Since a main contribution of this study is latent discrete diffusion, it would be interesting to see what would happen if the diffusion models are trained in the coordinate space and how the vocab size and hidden size affect the result.

### Questions
NA

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
Latent Diffusion Backmapping (LDB) is a generative model approach for modeling protein conformations. A discrete latent space is learned over all-atom protein structures with a VQ-VAE followed by a diffusion model to sample protein conformations. The work claims state-of-the-art (SOTA) results on three protein datasets which I do not agree with. LDB does not achieve SOTA on all metrics and the metrics are confusing as to whether they are relevant to evaluating protein ensembles.

### Strengths
* Discrete latent diffusion approach is novel to modeling protein conformations.
* LDB outperforms Genzprot and DiAMoNDBack on most metrics across the three datasets.

### Weaknesses
I have several major concerns.

* After having read the paper twice (including the appendix), I still do not understand the method. The problem definition in section 3 is to sample from p(x|X,V) where x is the coordinates and (X, V) is the coarse grained (CG) representation. Then the method in section 4 proceeds to describe a VQ-VAE for compressing protein structures then a graph latent diffusion model to sample discrete latents. Which part is sampling x and which part is sampling (X, V)? The methods section is poorly written with many details left unanswered.

* The paper claims several times that "diffusion in high-dimensional spaces complicates the multi-step denoising process" but provides no evidence of this. In fact, if the latent dimensionality is 36 then isn't this higher dimension than the 3 dimensional coordinates? I would have liked to see a direct comparison or some references but none are provided.

* I do not understand the metrics. If the benchmarks are protein conformation datasets then there should be distributional metrics such as in AlphaFlow [1]. For instance, what does it mean for computing RMSD to PED00055 when it has 20-140? Do you take the min RMSD of the model's samples to the frames? Each metric described in the appendix lacks details on how to calculate them.

* The paper in its current form is not reproducible. There just lacks too much details on the model, metrics, baselines and ablations (how was VAE-difusion and VQ-VAE-flow implemented?). Why was AlphaFlow not compared to?


[1] https://arxiv.org/abs/2402.04845

### Questions
My major questions are above. Additional questions.

* Line 168. What is n_f? What are "element types of the protein"? Why are the amino acids real valued instead of integer or categorical?

* Line 177. There are no details with how the internal coordinates are obtained. This is another reason why this work is not reproducible due to the lack of algorithmic details.

* Line 185. The work claims to generate all-atom structures but then this states only the C-alpha coordinates are used. So which is it?

* Line 253. The authors point to Jing et al 2022 to reconstruct full-atom structure but Jing et al 2022 is torsional diffusion for small molecule conformations. How does this relate to the protein structures here?

* Line 273. Where is your evidence of 3D diffusion doing poorly? We know SOTA methods like AlphaFold3 [1] and RFdiffusion [2] work very well in 3D.

* Why was AlphaFlow not compared to?

[1] https://www.nature.com/articles/s41586-024-07487-w

[2] https://www.nature.com/articles/s41586-023-06415-8

### Soundness
1

### Presentation
1

### Contribution
2
