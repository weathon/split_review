# Streamlining Generative Models for Structure-Based Drug Design

- Decision: Reject
- Scores: 5, 5, 3, 3

## Abstract
Generative models for structure-based drug design (SBDD) aim to generate novel 3D molecules for specified protein targets $\textit{in silico}$. The prevailing paradigm focuses on model expressivity - typically with powerful Graph Neural Network (GNN) models - but is agnostic to binding affinity during training, potentially overlooking better molecules. We address this issue with a two-pronged approach: learn an economical surrogate for affinity to infer an unlabeled molecular graph, and optimize for labels conditioned on this graph and desired molecular properties (e.g., QED, SA). The resulting model FastSBDD achieves state-of-the-art results as well as streamlined computation and model size (up to 1000x faster and with 100x fewer trainable parameters compared to existing methods), paving way for improved docking software. We also establish rigorous theoretical results to expose the representation limits of GNNs in SBDD contexts and the generalizability of our affinity scoring model, advocating more emphasis on generalization going forward.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a two-pronged approach to generate molecules for specific protein target: (1) learn an unlabeled molecular graph (2) optimize conditioned on desired molecular properties. The method shows performance improvement.

### Strengths
This paper dicusses the issue with 3D molecule generation for specific protein targets and proposes the method to solve it. The story line is clear.

Empirical results look strong, besides the trained model is smaller in size, which demonstrate the efficiency of proposed method.

### Weaknesses
The writing of this paper is not very clear. For example, one of the assumption is the conditional independence in Eq (1), however this equation is not self-inclusive. It's not clear what the model assumptions are and what the conclusions are.

My major concerns is that I think the methodology lacks novelty. Most of section 3 is spent on describing what architectures are used to model certain conditional probabilities. It's not clear what is this paper's techinical contribution.

Section 5 describes theoritical analysis, but I don't see how it is connected to the main claim of this paper. For example, section 5.2 talks about generalization bound, the author may want to show that the model has good generalization ability with respest to some terms (L, m, k) in Eq (14).

Eq (1), I think the term "disentengled" is inappropriate here. It's just conditional independence, disentenglement usually refers to something else.

### Questions
Please refer to *weaknesses* section.

Eq (1), I think the term "disentengled" is inappropriate here. It's just conditional independence, disentenglement usually refers to something else.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a new generative model named FastSBDD for structure-based drug design. It disentangles the ligand molecule generation into the unlabelled molecular graph generation and the atom type generation. The unlabelled molecular graph generation module is actually a sampler, which samples unlabelled graphs from ligand database.  The authors build a binding affinity prediction model to select unlabelled graphs with best predicted affinities. The atom type generation module can be a sampler, MoFlow based generator or a generator combined with property filters. The authors perform experiments on Crossdocked2020 and show that their model can achieve better performance with much less time cost. Moreover,  the authors provide theoretical analysis to justify that FastSBDD can generalize well.

### Strengths
- The proposed method is simple and effective. 
- The writing is clear and easy to follow.
- The code is provided.

### Weaknesses
 - The proposed disentanglement doesn't make much sense to me.  I wonder whether the authors redock molecules with AutoDock Vina in their preliminary experiments (Sec 3.1 and Appendix A). I suspect that changing initial 3D conformation can also achieve a high $R^2$ of Vina score is caused by redocking. Otherwise, the Vina score should have a large change. 
- The assumption justification is needed about why the unlabelled graph sampler could be independent of protein
- The proposed method has many filtering operations (filter high-affinity molecules with binding affinity scoring model, filter high QED+SA molecules in the atom type assignment phase) during the generation process. It would be fairer to compare with optimization-based models or compare with generative models and apply a similar property screening operation as post-processing.
- The proposed method can not generate novel 2D graph structures. I'm not sure whether it's a real limitation. If the authors can justify all 2D graph structures can be covered by the ligand database, it's also fine.

### Questions
- How accurate is the binding affinity scoring model? Typically, the model utilized 3D information would be more accurate, but the proposed scoring model only uses the unlabelled 2D molecular graph.
- In theoretical analysis, LU-3DGNN can distinguish G1, G2 with protein-ligand inter message passing. Does it mean considering ligand 3D information will lead to a better model?

### Soundness
2 fair

### Presentation
3 good

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
This work proposes a two-stage method, FastSBDD, for structure-based drug design. In the first stage, a binding-affinity predictor model is used to infer an unlabeled molecular graph. In the second stage, labels are optimized on the graph to improve the molecular properties, such as QED and SA. The results are considerably good and the inference speed is extremely fast. Additionally, theoretical analyses on representation learning under SBDD setting are also provided.

### Strengths
1. This paper introduces metric-aware optimization for generative SBDD settings, which is interesting. 
2. Previous methods directly 3D ligands based on give 3D pockets. However, this paper first generates unlabeled graph (topology) based on the 3D pockets, and then generated atom types and positions based on the unlabeled graph independently of proteins. The experimental results are promising.
3. Theoretical analyses are provided which are lacked in previous SBDD works.

### Weaknesses
1. The rationality of the two-stage method is suspectable. In general, especially from the perspective of structural biology, the protein-ligand interaction is strongly dependent on atom types, positions, and their precise spatial arrangement. However, in this paper, the only dependence on proteins is used to infer the unlabeled molecular graph where only topology information is used, essentially treating the protein pocket as a template for molecular connectivity rather than a binding site with specific chemical and geometric constraints. The second stage, which optimizes atom types and positions, does not involve modeling the protein pockets, thus ignoring crucial protein-ligand interactions. This contradicts with the fundamental knowledge of structural biology where specific interactions such as hydrogen bonds, salt bridges, and hydrophobic interactions are critical for binding affinity and selectivity. The method's approach seems to decouple the topology generation from the crucial chemical context of the protein pocket.
2. The main concern about the experiments is about the fairness of comparison with baselines. First, FastSBDD leverages additional molecular datasets, such as ZINC and ChemBL, while other baselines do not use additional datasets, giving it an unfair advantage in learning a more robust chemical space representation. Second, optimization is considered in FastSBDD, which directly improves the molecular properties. However, the baselines are all generative methods that do not include any optimization steps. It is more proper to compare FastSBDD with molecular optimization methods, such as MARS [1] and RGA [2], which are designed to refine molecular structures based on specific objectives. The lack of comparison with such methods makes it difficult to assess the true contribution of the proposed approach in the context of structure-based drug design. The comparison should be against methods that also perform optimization, not just generation.
3. Besides, many important SBDD baselines are missing, such as DecmopDiff [3]. The absence of these comparisons makes it difficult to place the proposed method within the broader landscape of SBDD techniques.

### Questions
The main questions is about how much protein-ligand interation information is included in unlabeled graphs. More analyses are needed.

### Soundness
1 poor

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The author introduced a novel two-step structure-based drug design method. Unlike the previous models that achieved end-to-end sampling, this approach first created the unlabeled atom graph (no atom type, bond type, and atom coordinates) and then sampled the label. They benchmarked their method with existing SOTA methods like DiffSBDD, Pocket2Mol, and TargetDiff. The results show this method could achieve better performance in terms of molecular property scores and speed.

### Strengths
1. The writing is generally great. Contributions and novelty are clear.
2. The motivation is clear and the problem that the paper wanted to address is important.
3. The paper introduced the theoretical analysis.

### Weaknesses
Firstly, it is important to note that the method did not actually achieve de-novo drug design, as it sampled the unlabeled ligand graph from an existing dataset. This raises questions about the novelty of the generated drug.

Furthermore, there is a lack of clarity regarding whether bond types are preserved in the unlabeled graph. Even if bond types are not preserved, it is not intuitively clear whether there is enough flexibility for atom type when the graph structure is fixed. 

In light of these concerns, the focus on overall diversity is not as meaningful as it could be. It would be more informative to assess and showcase the diversity of generated ligands for each template unlabeled graph. This analysis can reveal the extent of chemical variation achieved by the method, which is a more relevant measure of its potential impact. If the changes between the generated ligands and the template ligands are minor or do not significantly affect the chemical properties, the overall impact of the method may be considerably diminished. 

Without more evidence and explanation regarding the mentioned issues, I think comparing the drug repurpose-like generating method with the de-novo generating method is not fair enough. It might be more appropriate to compare it with other drug repurposing methods.

### Questions
1. Is the bond type preserved in the template unlabeled graph?
2. Is the diversity of the generated ligands for a given template unlabeled graph good enough? Are they significantly different from the original ligand?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
