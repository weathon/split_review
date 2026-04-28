# Estimation of single-cell and tissue perturbation effect in spatial transcriptomics via Spatial Causal Disentanglement

- Decision: Accept
- Avg Score: 6.67
- Scores: 6, 8, 6

## Abstract
Models of Virtual Cells and Virtual Tissues at single-cell resolution would allow us to test perturbations in silico and accelerate progress in tissue and cell engineering. 
However, most such models are not rooted in causal inference and as a result, could mistake correlation for causation.
We introduce Celcomen, a novel generative graph neural network grounded in mathematical causality to disentangle intra- and inter-cellular gene regulation in spatial transcriptomics and single-cell data. 
Celcomen can also be prompted by perturbations to generate spatial counterfactuals, thus offering insights into experimentally inaccessible states, with potential applications in human health. 
We validate the model's disentanglement and identifiability through simulations, and demonstrate its counterfactual predictions in clinically relevant settings, including human glioblastoma and fetal spleen, recovering inflammation-related gene programs post immune system perturbation. 
Moreover, it supports mechanistic interpretability, as its parameters can be reverse-engineered from observed behavior, making it an accessible model for understanding both neural networks and complex biological systems.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces Celcoman, a physics inspired generative graph neural network to infer intra- and inter-cellular gene regulation in spatial transriptomics and single-cell data. Celcoman can also be used to simulate the perturbation effect (such as gene knock off) in silico, offering insights into experimentally inaccessible states. 

This experiment is validated on both synthetic and real datasets, which includes both glioblastoma and fetal spleen samples.

### Strengths
1. I agree with the author's claim that this is the first causally identifiable model for spatial transcriptomics data. 
2. The motivation is well explained and the results on the impact of perturbed spot on surrounding cells are very convincing. It shows why we need to consider cell communication on spacial omnics data. 
3. The idea is novel. The author links GRN inference among neighboring cells with entropy maximization under the control of some lagrangian multipliers, which are then modeled by GNN. Theorem 1 is also inspiring.

### Weaknesses
1. Notation issue. The notations in this paper are not consistent. For example, the author used $s^i_{\alpha}$, $s^\alpha_{i}$, and $s_{\alpha i}$ to refer the same concept.

2. While I understand this is one of the first few papers studying, the lack of baseline comparisons in the experiments makes the results section less convincing. For example, while the results does show the impact of perturbed spot on surrounding area, how accurate it is? With GNN, I'm not surprised to see this kind of phenomenon. Are there any ways to provide a quantitative measurement or comparisons with the methods? Could you add some baselines or ground truth comparison?

3. A common acknowledged fact is that for causal models, there is a huge gap between synthetic data and the data we observe in real life. While the idea of in-silico perturbation data generation is very interesting, can you discuss the similarity/difference between the generated data and real data?

### Questions
1. In section 3.1, you mentioned that the inspiration of this work comes from the notion of force in physics and the objective is to learn the "least" number of forces. Then you said "'least' here is in the sense of entropy". However, later on, all we are trying to do is to maximize entropy. After thinking, I think I sort of understand the concept but someone else may get stuck too. Could you add a bit more explanation on how does the objective of minimizing number of forces transform into maximizing the entropy?

2. Could you comment on the runtime of this algorithm? Also, how long does it take (clock time) to finish the experiment you did in your study?

### Soundness
3

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
3

### Summary
The authors present a novel method for learning causal relationships in the context of spatial transcriptomics data, namely Celcomen. The method is devised to distinguish between inter and intra cellular causal interactions between genes. The authors characterize their method both from a theoretical point of view, demonstrating Celcomen identifiability (granted that assumptions hold), as well as from a practical point of view, applying their methods on real-world data.

### Strengths
The work has very strong theoretical basis. The authors provide proof of the identifiability of their method; moreover, they also honed their implementation so that to tackle large scale problem, for example by introducing a new Mean Field Theory approximation.

### Weaknesses
The main weakness of the manuscript is its poor connection to the underlying biology, as exemplified by the two issues below.

- The authors present a set of three assumptions upon which their whole model relies. However, they never discuss the implications of these assumptions, and without appropriate commentary, I frankly find difficult to understand what these assumptions entails. How do their assumptions compare with respect to the current limits of spatial transcriptomics technologies? Are there specific conditions, tissues, or other situations where these assumptions may not hold? Moreover, how are these assumptions related to more classical assumptions of causal learning theory, namely faithfulness, Markov condition, and causal sufficiency?

- Cells in tissues are usually grouped within functional clusters. Most typically, cells will belong to distinct cell types, which depending on the type of tissue may located together (endothelial cells in the inner layers of blood vessels) or scattered across the connecting matrix (e.g., fibroblast in mussle tissue). Other cases are possible as well: for example, glutamatergic neurons in the cortex will belong to different layers, where each layer will have different roles in cognitive functions. To my understanding, in its current iteration the Celcomen method fully disregards information on cell types or other functional clustering, even if this information can be instrumental in better understanding cell to cell communication mechanisms. For example, causal relationships between cell may be largely dictate on whether these cells are of the same or of different type.

### Questions
I would invite the authors to add an extensive paragraph regarding their assumptions:
- Discuss the biological and technological implications of each assumption
- Compare the assumptions to current limitations of spatial transcriptomics technologies
- Identify specific conditions or tissues where the assumptions may not hold
- Relate the assumptions to classical causal learning assumptions like faithfulness, Markov condition, and causal sufficiency

Modifying Celcomen so that to include cell type information is an onerous task that might deserve a separate publication. However, I would suggest that the authors:
- Acknowledge this limitation of their current model
- Discuss how disregarding cell type information may impact the interpretation of their results
- Propose specific ways the model could be extended in future work to incorporate cell type or functional cluster information

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
3

### Summary
In the manuscript, ‘Estimation of single-cell and tissue perturbation effect in spatial transcriptomics via Spatial Causal Disentanglement’, the authors introduce Celcomen, a generative GNN that incorporates causal inference for the task of predicting perturbation effects and counterfactuals, with applications to spatial transcriptomics data and single-cell data. The authors aim, in addition to predictions, to expose mechanistic interpretability, such as the inference of intra-cellular and inter-cellular gene regulation in such data. The method is demonstrated over multiple synthetic and real biological data.

### Strengths
- The problem that the authors pose is important and timely
- The method seems to be well grounded and robust
- The demonstrations of the method on real data seems to be promising, especially those having to do with disentangling intra vs inter cellular programs in human glioblastoma spatial transcriptomics data, and showing that in silico knockouts affect signal propagation in a biologically expected manner.

### Weaknesses
 - It’s unclear why the spatial structure of cells in tissues should be captured well by a DAG.
- The text could be improved at multiple points for readability.
- In the related work section, it would be better to add a subsection on generative models and disentanglement for single-cell and spatial transcriptomics data.
 - It would be better to give intuition in the text for the meaning of Theorem 2.
- ‘we observed a strong positive correlation between these two gene-gene interaction matrices’ - there are no results/statistics in the main text, and in the supplement we see a maximum of 0.4/0.5 correlation value, so needs to be rephrased. Also, unclear how these results point to identifiability, as there only seems to be analysis of correlation 
- About the actual gene-gene interaction matrices themselves (corresponding to results in Fig. 5) - do these make sense in terms of the current knowledge of existing gene-gene interactions? There are many ways to evaluate these types of questions, and this is crucially missing from the evaluation and results in the paper.
- The discussion section is missing a discussion of the limitations of the approach.

Minor comments:
- some of the references throughout don’t have parentheses around them.
- when introducing spatial transcriptomics, better to give an additional example (or examples), beyond VisiumHD.
- The connections between the visualizations in Fig. 1 and both its caption and the reference to it from the text, are not entirely clear.
- There are some strange phrasing of text throughout. An example (but not the only one): ‘Suppose for instance that nature imposes the colocalization of genes..’
- There are inexact sentences (again, example, but not the only one): “Since half of the time, the nearest neighbor of a nearest neighbor is also a nearest neighbor”
- ‘”Least” here is meant in the sense of entropy’ - needs explanation
- ‘for an ant forced to walk on the surface of a table, this force happens to be electromagnetism’?
- After theorem 1, there are repetitions in the text relative to the numbered equations.
- typo: ‘demonstrates that Celcomen’s usefulness as a toy model for mechanistic interpretability since’, ‘resolutionFarah’

### Questions
Comments:
- It’s unclear why the spatial structure of cells in tissues should be captured well by a DAG.
- The text could be improved at multiple points for readability.
- In the related work section, it would be better to add a subsection on generative models and disentanglement for single-cell and spatial transcriptomics data.
 - It would be better to give intuition in the text for the meaning of Theorem 2.
- ‘we observed a strong positive correlation between these two gene-gene interaction matrices’ - there are no results/statistics in the main text, and in the supplement we see a maximum of 0.4/0.5 correlation value, so needs to be rephrased. Also, unclear how these results point to identifiability, as there only seems to be analysis of correlation 
- About the actual gene-gene interaction matrices themselves (corresponding to results in Fig. 5) - do these make sense in terms of the current knowledge of existing gene-gene interactions? There are many ways to evaluate these types of questions, and this is crucially missing from the evaluation and results in the paper.
- The discussion section is missing a discussion of the limitations of the approach.

Minor comments:
- some of the references throughout don’t have parentheses around them.
- when introducing spatial transcriptomics, better to give an additional example (or examples), beyond VisiumHD.
- The connections between the visualizations in Fig. 1 and both its caption and the reference to it from the text, are not entirely clear.
- There are some strange phrasing of text throughout. An example (but not the only one): ‘Suppose for instance that nature imposes the colocalization of genes..’
- There are inexact sentences (again, example, but not the only one): “Since half of the time, the nearest neighbor of a nearest neighbor is also a nearest neighbor”
- ‘”Least” here is meant in the sense of entropy’ - needs explanation
- ‘for an ant forced to walk on the surface of a table, this force happens to be electromagnetism’?
- After theorem 1, there are repetitions in the text relative to the numbered equations.
- typo: ‘demonstrates that Celcomen’s usefulness as a toy model for mechanistic interpretability since’, ‘resolutionFarah’

### Soundness
3

### Presentation
3

### Contribution
3
