# Deep Signature: Characterization of Large-Scale Molecular Dynamics

- Decision: Accept
- Scores: 8, 6, 6

## Abstract
Understanding protein dynamics are essential for deciphering protein functional mechanisms and developing molecular therapies. However, the complex high-dimensional dynamics and interatomic interactions of biological processes pose significant challenge for existing computational techniques. In this paper, we approach this problem for the first time by introducing Deep Signature, a novel computationally tractable framework that characterizes complex dynamics and interatomic interactions based on their evolving trajectories. Specifically, our approach incorporates soft spectral clustering that locally aggregates cooperative dynamics to reduce the size of the system, as well as signature transform that collects iterated integrals to provide a global characterization of the non-smooth interactive dynamics. Theoretical analysis demonstrates that Deep Signature exhibits several desirable properties, including invariance to translation, near invariance to rotation, equivariance to permutation of atomic coordinates, and invariance under time reparameterization. Furthermore, experimental results on three benchmarks of biological processes verify that our approach can achieve superior performance compared to baseline methods.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper introduces Deep Signature, a framework for characterizing dynamics on graphs. Deep Signature involves three key components: (1) graph coarsening using a deep spectral clustering module, (2) computation of path signatures to capture global inter-node interactions using iterated integrals over time, and (3) a two-layer MLP for property prediction.
The authors tested Deep Signature on three datasets: (1) gene expression dynamics, classifying into degradation or dimerization types, (2) GPCR dynamics, distinguishing between active and inactive states, and (3) EGFR mutant dynamics, predicting drug sensitivity. They conducted an ablation study validating the contribution of each loss component in the model and performed limited comparisons with methods based on static structures, dihedral angles, and GraphLSTM.

### Strengths
1. Incorporates appropriate symmetries for (temporal) 3D point cloud learning. In particular, the invariance to time reparameterization is key because the underlying MD simulations might be prone to random restarts and miscellaneous artefacts preventing them from being a smooth "video" (ie, the MD itself might be erratic with the same state sampled repeatedly).

2. Deep Signature _learns_ the ideal CG beads relevant to the task, bypassing the need to manually remove degrees of freedom (eg: CA-level coarse-graining, as done in existing methods). The use of the signature transform allows for local and global temporal interactions to be captured well, as opposed to learning representations on separate frames. 

3. I'm confident this method can be used for good representation learning of trajectory information for tasks beyond the ones mentioned in the paper (eg: interpolation in the latent space of protein conformations, perhaps for ensemble generation).

4. Demonstrates relatively good performance compared to weak and strong temporal graph learning baselines (like GraphLSTM).

### Weaknesses
The paper does not clarify the level of coarsening necessary to make path signature computations feasible. For instance, in gene regulatory dynamics, the graph was reduced from 100 nodes to 30, while the EGFR dataset was reduced from approximately 5000 atoms to 50 nodes, but the level of coarsening for the GPCR dataset is unspecified. This raises questions about whether 50 nodes is a computational limit for the method. Additionally, while protein structure can be intuitively coarsened into backbones, sidechains, and motifs, the interpretation for coarsened graphs in gene expression dynamics is unclear. It is uncertain if the coarsened nodes correspond to gene hubs or other biologically meaningful groupings.

The equation used to model GRN dynamics (Eqn 13 in Section B.1) appears incorrect. Specifically, for dimerization (when f=2), the concentration should should be squared under Michaelis-Menten kinetics, rather than simply doubling the decay rate. This could lead to inaccurate modeling of gene expression dynamics and affect the results in this section.

The comparisons used in the experiments are limited and static, primarily involving the first and last frames (head, tail, and head & tail) which do not capture temporal dynamics. The authors do not benchmark against dynamic approaches that consider time-varying information, such as MDTraj [1], Timewarp [2], and DSR [3]. Including these comparisons would provide a more rigorous evaluation of Deep Signature's effectiveness relative to established tools for molecular trajectory analysis.

The authors claim that the coarsened dynamics in Fig 6c follow the same trend as the original dynamics, yet this similarity is not quantified. Providing a quantitative measure, such as correlation coefficients between the original and coarsened dynamics at various coarsening levels, would better support this claim. Additionally, the paper would benefit from comparisons of the authors' coarsening strategy against other deterministic and learnable methods for protein graph coarsening to demonstrate its effectiveness and fidelity in preserving dynamics.

The description of the cross-validation process and test set creation is confusing. The authors mention “for each running, we evaluate the prediction accuracy of our method on an independent unseen test set and report the averaged results,” but it is not clear how this set is constructed. If results are averaged, please report the standard deviation in all the tables.

### Questions
1. Existing equivariant neural networks with geometric inductive biases have been outperformed, both in terms of performance and efficiency, by Transformer-style architectures (ie, something as simple as torch.nn.TransformerEncoder). Was any ablation done that compares Deep Signature with such architectures that "tokenize" the trajectory intervals?   

2. I'm curious what the learned coarse-grained beads/maps look like for GPCR proteins – is it creating CG beads only based on atoms within a locality? How does this compare to naively taking atoms within some radial ball and considering them a bead? More often than not, these naive CG choices work well in practice, without the need to overcomplicate it with a learnable method. I'd like to see whether this "learned GCN-based coarse-graining" is really necessary.

3. How sensitive is the path signature transform to very dynamic conformational changes in a short duration of time? For instance, as I mentioned above, fast-folding proteins undergo significant changes in 3D shape in just short simulations. Can this method capture this dynamics well enough?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
In the paper, the authors introduce the Deep Signature framework to capture complex dynamics using the evolution trajectories. The Deep Signature framework includes spectral clustering, signature transform and a classifier. Additionally, the authors show that the framework satisfies the desired symmetry constraints. Experiments on  gene regulatory dynamics, EGFR mutation dynamics and GPCR dynamics exhibit the empirical performance of the framework.

### Strengths
1. The presentation of the method is very clear and easy to understand.
2. The motivation of applying signature transform is reasonable.

### Weaknesses
1. Lack of experiments on large dataset. As the paper claims, the Deep Signature framework can capture large-scale complex dynamics. So I think experiments on datasets with large amount of data and system size are necessary. But the paper only includes the experiments on datasets with large system size.

2. I think the baseline in this paper is too weak. For example, the author should compare the strong baseline with graph transformer architecture[1] based on the first/last frame of the trajectory. Comparations between these strong baseline may strengthen the empirical performance of the framework.

### Questions
1. I think the classification task using evolution trajectories is not a common setting. Could you explain why this problem setting is reasonable comparing to the one frame classification setting?  Do we really need the complete trajectory to do classification?

2. I do not understand your setting in the EGFR dynamics experiment since I'm not an expert on this domain. Could you please explain why the trajectory can be labeled according to its sensitivity towards the drug? I think the sensitivity should be a number rather than a 0/1 label.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper presents a framework, Deep Signature, designed to analyze the dynamics and interatomic interactions of large-scale molecular system. The method uses a deep spectral clustering model to capture coarse grained dynamics, a path signature transform module to characterize interatomic interactions through iterated integrals, and a classifier for property prediction. Theoretically, Deep Signature is shown to maintain desirable symmetry properties. The method demonstrates improved accuracy across three benchmarks and demonstrates interpretability.

### Strengths
1. Authors develop an end-to-end framework to characterize interatomic interactions and dynamics of large-scale molecules, it shows improvement on three benchmarks and provides interpretability. 
2. The size of the system is reduced by deep spectral clustering module without any expert knowledge. 
3. The framework's desirable properties are supported by theoretical analysis.

### Weaknesses
1. The authors compare their approach to baseline methods, but a more comprehensive comparison with some SOTA baselines would provide a more robust evaluation. Specifically, the choice of baselines seems limited, and a comparison against methods that explicitly model temporal dependencies in molecular dynamics, such as recurrent neural networks or temporal convolutional networks, would be beneficial. The current comparison does not fully demonstrate the advantages of the proposed method over existing time-series analysis techniques.
2. The manuscript would benefit from a comparison of deep spectral clustering module with existing coarse graining methods. While the authors mention the use of spectral graph theory, a direct comparison with established coarse-graining techniques, such as those based on force-matching or structure-based approaches, would provide a clearer understanding of the advantages and limitations of the proposed deep spectral clustering module. This comparison should also include an analysis of the computational cost and the impact on the accuracy of downstream tasks.
3. An analysis of the model’s sensitivity to hyperparameters would provide insights into its robustness and reproducibility. The paper lacks a detailed discussion on how the various hyperparameters, such as the learning rate, batch size, and the depth of the neural networks, affect the performance of the model. A sensitivity analysis, showing how the performance varies with different hyperparameter values, is essential to ensure the reliability and reproducibility of the results.

### Questions
1. How were the hyperparameters chosen, such as the loss coefficient parameters $\lambda_i$,  the number of nodes in deep spectral clustering model, and time interval $[r_i, r_{i+1}]$ in path signature transform?
2. When visualizing critical pathways and interatomic interactions on the EGFR dynamics, why were three atoms identified specifically? Could more than three be selected?
3. Have the authors considered comparing their approach with advanced time series classification algorithms？
4. How does the computational efficiency of the proposed method compare to baseline methods?

### Soundness
2

### Presentation
3

### Contribution
3
