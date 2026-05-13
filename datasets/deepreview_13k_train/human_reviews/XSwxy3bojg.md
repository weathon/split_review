# Generating Molecular Conformer Fields

- Decision: Reject
- Scores: 5, 3, 3, 6, 5

## Abstract
In this paper we tackle the problem of generating conformers of a molecule in 3D space given its molecular graph. We parameterize these conformers as continuous functions that map elements from the molecular graph to points in 3D space. We then formulate the problem of learning to generate conformers as learning a distribution over these functions using a diffusion generative model, called Molecular Conformer Fields (MCF). Our approach is simple and scalable, and obtains results that are comparable or better than the previous state-of-the-art while making no assumptions about the explicit structure of molecules (\eg modeling torsional angles). MCF represents an advance in extending diffusion models to handle complex scientific problems in a conceptually simple, scalable and effective manner.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a generative filed model to generate a 3D conformer based on the 2D molecular graph. The main contribution of this paper is the extension of the diffusion probabilistic field to the problem of generation conformers. The proposed Molecular Conformer Field (MCF) is defined from eigenvectors of the 2D molecular graphs to 3D atomic positions. Experimental results show the proposed model outperforms the baselines.

### Strengths
S1: The studied problem is interesting and useful.

S2: It is interesting to apply the diffusion probabilistic field to the problem of generation conformers.

S3: The paper is well-written.

### Weaknesses
W1: The novelty is limited from a technological perspective. I see little difference between the diffusion probabilistic field and the proposed molecular conformer field.

W2: Using eigenvectors of the position of the graph in the field seems dangerous for the folloing two reasons. (1) This modeling does not take key information, such as atomic numbers, into consideration. (2) The eigenvector based position cannot effectively indicate distance in the graph without the corresponding eigenvalues.

### Questions
Q1: Can this proposed method distinguish two different 2D molecular graphs that have the same eigenvectors but diffenrent eigenvalues?


After read the authors' response, I increase my score to "5: marginally below the acceptance threshold".

### Soundness
2 fair

### Presentation
3 good

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
the paper propose diffusion model to generate molecule conformation based on atom-to-atom graphs. the paper can generate a distribution of confirmations.

the formulation of the framework of this paper is not clear. I will elaborate in later section.

I checked out Jing et al 2022 for the definition of average minimum RMSD. indeed Jing does not describe this method, the authors should cite the paper Jing cited, that is: Ganea et al. GEOMOL: Torsional Geometric Generation of Molecular 3D Conformer Ensembles.

In Ganea et al, AMR is given in Eq.(5). there is also COV in Eq.(5) which describes the coverage. Coverage would be a more important measure.

### Strengths
the method can generate a distribution of conformations rather than just generate one confirmation. this has good advantage because molecules in the real world takes a distribution of confirmation following the Boltzmann distribution and obeys the law of thermodynamics.

### Weaknesses
if we have n atoms in one molecule, then the conformation space is \mathbb{R}^{3n} instead of \mathbb{R}^3. in the paper authors indicate f: G -> \mathbb{R}^3. I am confused.

section 4.1. Score field network: the author cite and use perceiverIO net and explain why they use that. this is good. the author should explain further for the benefits of the readers, what line 8 of algorithm 1 entails. \epsilon_q ~ N(0,I), line 8 want \epsilon_\theta to map to N(0,I). what is the physical significance in the context of molecule conformations?

the authors claimed that the strength of their method is that there is no need to know some domain knowledge such as torsion angles of molecules. in my opinion this is a serious weakness. would the predictions generate physically non-viable confirmations if it disregard some basic physics and chemistry?

since diffusion model will generate a distribution of conformations, does the distribution follows the distribution of statistical physics? e.g. Boltzmann distribution.

molecules are rotational invariant. that means, one can rotate the conformation by any angles in 3D and the conformation remains a valid conformation. is the diffusion model able to generated rotational invariant distribution of conformation?

### Questions
page 7, paragraph 1, "We generate 2K confirmers for a molecule with K ground truth conformers", how does the author do this? it is important to have 'correct' ground truth. if the authors use MD or MCMC with proper settings, then the ground truth can be correct. what are the settings? explicit water? mean field? what are the molecular interactions?

does the ground truth distribution obeys statistical physics law? NVT? grand canonical ensemble? micro-canonical ensemble?

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a method called Molecular Conformer Fields (MCF) that parameterizes conformers as continuous functions mapping elements from the molecular graph to points in 3D space (3D coordinates). The problem is formulated as learning a distribution over these functions using a diffusion generative model (DDPM). MCF represents an advance in extending diffusion models to handle complex scientific problems in a scalable, simple, and effective manner. The backbone of the score field network is PerceiverIO, a transformer encoder-decoder architecture.

### Strengths
1. The paper is well organized and clearly written; and it’s easy to read.
2. The proposed method demonstrates noticeable enhancements on the small molecule dataset, specifically GEOM-QM9.

### Weaknesses
Inconsistency in Chemical Properties Experiment
In Section A.3.3, which pertains to the chemical properties experiment, this paper adopts experimental results from "Torsional Diffusion." However, there's a discrepancy in the subsets used. Specifically, the paper does not use the identical subset as "Torsional Diffusion," implying that they have selected different molecules. This raises concerns about the validity of their experimental comparison. For it to be persuasive, it should be more convincingly aligned.

Errors in Previous Studies
In section 1, page 2, For example, the quality of conformers from GeoMol (Ganea et al., 2021) and Torsional Diffusion (Jing et al., 2022) depends on the local substructure prediction model which is not differentiable.
In section 2, page 2, In GeoMol (Ganea et al., 2021), the authors propose a regression objective coupled with an Optimal Transport loss to predict the torsional angles of bonds that assemble substructures of a molecule

GeoMol's prediction of the local substructure is based on bond length, bond angle, and torsion angle. The definitions of torsion angle in GeoMol and Torsional Diffusion are different. For Torsional Diffusion, the torsion angle is based on rotatable bonds only.

Insufficient Performance
The GEOM-DRUGS dataset is considered a more challenging metric in this field. The method proposed in this paper demonstrates enhanced performance only regarding recall. Recall measures the capability to locate ground-truth conformers within the generated ones, and this metric is susceptible to influences from the training data. Notably, Torsional Diffusion depends on the local generated by RDKit, utilizing only 30 normalized conformers for each molecule during training. Although both the proposed method and Torsional Diffusion use the same dataset and split, the mean count of conformers in the GEOM-DRUGS dataset is approximately 100. This suggests that the boost in recall could result from the proposed method being trained on over 300% more conformers and having double the training epochs rather than the inherent efficacy of the method.

Furthermore, in terms of precision, the proposed method is worse than Torsional Diffusion, especially evident when Torsional Diffusion undergoes 50 denoising steps, as shown in [Table.9] of the supplemental, and MCF requires 1000 denoising steps.

High Computation Cost
The training settings for the proposed method use 8*A100 with a batch size of 64 (or one A100 with a batch size of 8). In contrast, Torsional Diffusion is trained on a singular A6000 with a batch size of 32. Consequently, the computational expense for each denoising phase for the proposed method is at least four times that of Torsional Diffusion. Considering Torsional Diffusion necessitates only 20 denoising steps, whereas MCF demands 1000, the proposed method, with a computational cost over two hundred times more, should ideally yield superior results, especially with larger molecules.

Absence of Runtime Experimental Results and Lack Significance
A pivotal metric for the conformer generation task is runtime. Even though some early deep-learning research might not have emphasized runtime, recent studies, such as GeoMol [Figure.7] and Torsional Diffusion [Table.2], regard it as a critical experimental metric. Historically, cheminformatics methods recognized runtime as a vital metric even before the advent of deep learning, as documented in [Conformation Generation: The State of the Art].

Furthermore, CREST, a method based on in metadynamics, is used to generate GEOM-Drugs dataset. The computational cost of CREST in GEOM-DRUGS is about 90 CPU core-hours per drug-like molecule, as detailed in [Torsional Diffusion Section 2, Page 2]. In contrast, Torsional Diffusion requires roughly 5-CPU core seconds for a conformer, while MCF might need between 15 to 20 CPU core-minutes (considering the computational cost is over 200 times).

Given that the average number (N) of conformers per molecule is about 100, MCF might need a minimum of 60 CPU core-hours to generate conformers (2N) for a single molecule. This speed is comparable to the dataset's generation rate (90 CPU core-hours per molecule). Hence, the proposed method's significance is low, especially when weighed against its high computational demands.

### Questions
For the chemical properties experiment, would it be possible to replicate the Torsional Diffusion experiment using your code and subset? This approach would ensure a more equitable comparison of results.

For the recall metric, could you consider training your proposed model using only 30 conformers for each molecule? Doing so could validate whether your method truly offers enhanced recall performance when using an identical dataset.

For runtime, are there any strategies you could employ to further reduce the computational cost, such as minimizing the number of denoising steps or downsizing the model? If the computational cost of your method is comparable to that of CREST, the approach generates the dataset, your proposed technique might lack significance.

### Soundness
2 fair

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a new approach Molecular Conformer Fields (MCF) for molecular conformation generation.  The approach is based on   Diffusion Probabilistic Fields (Zhuang et al., 2023), which learns a distribution of functions (fields) with DDPM. The main difference is that the authors compute normalized graph Laplacian to adopt DPF on the graph-structure molecular data. The experiments on GEOM-QM9 and GEOM-Drugs show that the proposed method is very effective, which can outperform or on-par with existing SOTA models, even though the proposed method directly predicts 3D atom positions instead of torsion angles or other domain-specific variables.

### Strengths
It's exciting to see that the proposed method can achieve better performance than TorsionDiff by directly predicting 3D atom positions on the GEOMS benchmark. The empirical results demonstrate the effectiveness of the proposed method.

### Weaknesses
- The proposed method looked novel to me at first, but after I read the DPF paper (Zhuang et al., 2023), I found the novelty is actually limited. The authors compute normalized graph Laplacian as the "index" of atom in the graph,  an analogy of the pixel (x, y) index of the image. The main formulation and model architecture are same to DPF. The core idea of applying diffusion on fields defined on a graph by using the graph Laplacian as an index is not particularly novel, given the existing work on Diffusion Probabilistic Fields.
- In terms of writing, I think more high-level introduction to DPF is needed in the background / preliminary section. The construction of context pairs and query pairs appear at a sudden, without any motivation behind them, which makes the paper hard to read. The paper lacks a clear explanation of why these specific context and query pairs are necessary for modeling the conformer field. The sudden introduction of these pairs without proper motivation makes it difficult to understand the underlying methodology.
- The notation in Sec. 3.2 is problematic. The expression such as $q(f_t | f_{t-1}) = N(f_{t-1} | \sqrt{\bar{\alpha}_t} f_0 + (1 - \alpha_t) I)$ is misleading. While the authors clarify that the noise is added to the signal in the context-query pairs, the notation suggests that the function itself is being treated as a random variable in a Gaussian distribution, which is not accurate. This notation obscures the fact that it is the *output* of the function (i.e., the 3D coordinates) that are being diffused, not the function itself.

### Questions
- Why should the context pair also be corrupted? Is there any motivation behind it?
- In Sec. 3.2 the notation looks problematic. How can a function be used as the variable of Gaussian distribution?
- I don't understand why the proposed method can outperform GeoDiff, both of which are based on DDPM and aim to solve the same task. Does the improvement come from the DPF formulation, the more powerful PerceiverIP architecture, or something else? 
- One related work [1] on conformation generation is missing

[1] Guan, J., Qian, W. W., Ma, W. Y., Ma, J., & Peng, J. Energy-inspired molecular conformation optimization. ICLR 2022.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors apply Denoising Probabilistic Fields (DPFs) to the problem of molecular-conformer generation. This entails training a diffusion model where molecular node identities (given as Lapalcian eigenvectors) are given to the diffusion model in order to denoise associated 3D coordinates of each node. The authors show competitive results with another diffusion-based method (Torsional Diffusion) on three standard molecular-conformer datasets.

### Strengths
### Shows comparable performance to Torsional Diffusion (state of the art)

The authors have shown using three standard datasets: GEOM-QM9, GEOM-DRUGS, and GEOM-XL, that their method of DPFs on molecular conformers is comparable. The performance metrics used encompass recall and precision and matches that used in previous work. The comparisons seem solid for the most part. Overall, although these results do not consistently outperform the state of the art, they look comparable depending on the dataset.

### Demonstrates that equivariant architectures are not strictly necessary for this problem

The authors also call attention to the fact that DPFs get comparable performance to Torsional Diffusion, and this shows that roto-translational equivariance may not be strictly required for conformer prediction (Torsional Diffusion is implemented using an SE(3) equivariant architecture, but the DPF in this manuscript directly generates 3D coordinates of atoms from molecular graphs. Although this is not a core contribution of the paper, it is useful to know nonetheless.

Also, I very much enjoyed and appreciated the quotations in “‘simple’ DDPM loss”.

### Weaknesses
### Limited novelty relative to DPF paper

The technical and empirical novelty is fairly limited in this paper. It is a direct application of DPFs (Zhuang et. al. 2023) to a molecular-conformer generation. The neural network also has an identical architecture, and the difference is solely to apply it to this different problem. The representation of atom/node “coordinates” (i.e. the field domain) as Laplacian eigenvectors is also a direct application of Maskey, et. al. 2022.

### Several claims are not very well substantiated; these claims should be reworded in the text

Below are a list of claims I found in the paper which I did not find to be well substantiated. The authors should either provide stronger evidence for these claims, or reword the claim to be more accurate.

-  The paper claims that explicitly enforcing domain-specific inductive biases (e.g. periodic domain of possible torsional angles in Torsion Diff) comes at a cost, but what is the cost? Torsional Diffusion seems to be performing just as well as MCF (sometimes better). It is not clear what specific limitations are imposed by the cheminformatics methods used in Torsional Diffusion, and whether MCF actually avoids these limitations. For example, does MCF perform better on molecules where Torsional Diffusion fails due to these limitations?

- The paper claims that MCF is more scalable than other methods (e.g. Torsional Diffusion). The architecture of MCF is quite large, however, and for a system of 100 atoms, there are 200 queries to the model (100 context pairs and 100 query pairs). Is it really more scalable than Torsional Diffusion? The authors should provide a more detailed analysis of the computational cost, including training time, sampling time, and memory usage, to support this claim. Furthermore, the fact that DPF relies on both context and query sets means that it effectively requires twice the diffusion steps compared to methods that directly denoise the target coordinates.

- The paper claims that the ablation study shows what factors are important for molecular-conformer generation, but this is a pretty grandiose claim. The ablation study only shows the impact of atom features and the size of the Laplacian eigenvectors, _specifically on MCF performance_. It does not lend insight into what factors are important for molecular-conformer generation in general.
 
- The paper claims that explicitly enforcing roto-translation equivariance is not a strong requirement for generalization, and that equivariance is not particularly useful for molecular-conformer generation. Although the authors have shown similar and comparable performance between an equivariant and non-equivariant architecture, it is not yet clear whether or not equivariance really affects performance. For example, one could ask whether MCFs could outperform Torsional Diffusion if it had used a roto-translationally equivariant architecture (not just PerceiverIO).

### Splitting of molecules into datasets may have leakage

The datasets seem to be split into training/validation/test uniformly at random, but this can lead to train/test leakage. Many molecules in the datasets share very similar scaffolds, and it is well known that prediction between similar scaffolds is much easier. To really assess the quality of the model, the datasets should be split into scaffold-aware subsets to avoid leakage.

I understand this issue is almost certainly inherited from previous works (e.g. Torsional Diffusion), so I do not count this against the evaluation of this paper, but I highly recommend exploring better dataset splits so that we may all do better moving forward.

### The continuity of MCF needs more exploration and explanation

Figure 6 and the exploration of the continuity of MCFs does not seem very strong or insightful. The analysis only shows that the model learns to “round” coordinates toward atom centers. There is no indication that the model actually learns any information about molecular bonds (and not to put atom density on them). One could claim that the model will always output some set of atomic coordinates which are not too close to each other _regardless_ of the input, even if the network has no understanding of bonds.

It is also not clear what the benefit is to being able to predict on interpolated atom coordinates. Is the goal to be able to input the interpolated eigenvector halfway between two nodes and generate the 3D coordinate that is halfway between the two atoms? If so, then this analysis very much shows the opposite. Is the goal to be able to input the interpolated eigenvector halfway between two nodes and probabilistically generate the 3D atomic coordinate of either endpoint atom? If so, then this analysis does somewhat show that, but I don’t see why this latter question is interesting or useful.

### Some parts of the writing can be clearer

- More background on DPF would be nice; this work is so dependent on DPFs, that it would be good to have more background on how they work

- Limitations of this method should really go in the main text

- It would be good to include the definitions of performance metrics like RMSD recall (in the supplement) instead of needing to refer to the Torsional Diffusion paper

- Notation should be cleaner: if a molecule’s conformer is a function $f: \mathcal{G}\rightarrow\mathbb{R}^{3}$, this implies the function maps an entire molecular graph to a single 3D coordinate

- “equivairant” in first paragraph of Section 2

- “In contraposition” should be “In contrast”

### Questions
### Is the dataset split the same as in previous works? Is the RMSD cutoff $\delta$ the same as previous works for precision/recall?

It is crucial that the dataset splits (and RMSD precision/recall $\delta$ value) are the same here compared to prior works, because the performance numbers in the tables are directly copied from those papers.

### What atom features are concatenated? How are bond features incorporated (e.g. double vs triple bonds)? 

### What is the purpose of predicting on the query set instead of context set in DPFs?

This question is more related to DPFs in general (and is not specific to MCFs), to make sure I understand the work. Why is there a separate query set and context set in DPFs? If we are adding noise to the signal of the context set, why not just predict the denoising of the context? Instead, we are taking another query set (with the same coordinates) and adding noise separately and predicting denoising of the query set.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good
