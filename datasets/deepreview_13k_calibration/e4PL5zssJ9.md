# Symmetry-Driven Discovery of Dynamical Variables in Molecular Simulations

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 5, 5

## Abstract
Molecular dynamics simulations are crucial for understanding complex biomolecular systems, but they are often hindered by the high dimensionality of the configurational space. This paper introduces two novel approaches for discovering effective degrees of freedom (DoF) in molecular dynamics simulations by leveraging approximate symmetries of the energy landscape. We present a scalable symmetry loss function compatible with existing force-field frameworks and a Hessian-based method efficient for smaller systems. Both approaches enable systematic exploration of conformational space by connecting structural dynamics to energy landscape symmetries. Applied to alanine dipeptide, our methods comprehensively sample the Ramachandran plot, including shallow minima. Simulations initiated from our DoF-sampled points converge to all important conformations, demonstrating the methods’ effectiveness in navigating complex energy landscapes. These approaches offer powerful tools for efficient exploration in molecular simulations, with potential applications in protein folding and drug discovery.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors propose a method to discover effective degrees of freedom in molecular systems, for the aim of fast exploration of low-energy configuration space without prior knowledge of internal coordinates or collective variables. Effective degrees of freedom are directions in configuration space which approximately preserve the energy, and are in this sense viewed as symmetries of the energy. Specifically, degrees of freedom are unit vectors of the Lie algebra of the general linear group of transformations acting on configuration space. The authors propose a symmetry loss to find effective degrees of freedom, which are those along which energy changes minimally, but where conformation changes significantly. The authors refine this symmetry loss with variants using the Hessian of the energy. The proposed method is validated on the model system of alanine dipeptide, where it recovers all important conformers but with dramatically fewer timesteps of molecular dynamics.

### Strengths
I find the work exciting because the application of symmetry discovery to enhanced sampling is novel, introduces a new notion for effective degrees of freedom, and empirically appears to dramatically accelerate exploration of molecular configuration spaces. The explanation and derivation of the method is clear and well-paced. The ideas introduced by this work inspire many directions for future work.

I appreciate the extensive discussion of methods for enhanced molecular dynamics sampling.

### Weaknesses
There are issues with presentation which hold this submission back from acceptance.

The major issue is that not enough analysis is given to characterize the learned degrees of freedom.
- How does the conformation qualitatively change for a given learned degree of freedom? Do these actually resemble the individual true torsions? For example, does a single learned degree of freedom primarily rotate a single dihedral angle, or is it a more complex motion involving multiple angles? It is difficult to assess the physical interpretability of these degrees of freedom without such analysis.
- It is stated that "the degrees of freedom still remain invariant across" conditions in vacuum and solvent - how can this be true if each column of Figs 2 and 4 discovers slightly different conformers? This statement needs further clarification, as it is not clear how the degrees of freedom can be invariant if the resulting conformations are different. The relationship between the learned degrees of freedom and the resulting conformations needs to be more rigorously defined.
- What does the beta-sheet conformation look like, and where does it appear on the Ramachandran plot? Where do the rediscovered conformers lie on the plot? The location of the beta-sheet and other conformers on the Ramachandran plot is not clearly indicated, making it difficult to assess the method's ability to recover known conformations. A more precise mapping between the discovered conformations and the Ramachandran plot is needed.
- In Figs 1 and 3, the twisted gridlines differ for each method, and do not appear to cover the entire phi-psi space. How should I interpret this? It is my understanding that the beta conformation should be located at the origin of these grids, but it is not clear to me where that is located. The interpretation of these gridlines is unclear, and their relationship to the underlying conformational space needs to be better explained. The fact that they do not fully cover the phi-psi space raises concerns about the completeness of the exploration.
- Many conformers shown in Fig 4 do not visually resemble the leftmost column. What is the threshold for dihedral angle similarity? A quantitative measure of similarity between the discovered conformers and the reference structure is needed to assess the accuracy of the method. The lack of a clear threshold makes it difficult to evaluate the results.

There are numerous minor errors:
- Citation style should have parentheses (\citep) when not using the authors as a noun.
- Inconsistent capitalization of "Lie algebra", "Alanine dipeptide", "DOF"
- Line 50: "symmetry, loss"
- Line 62: "WE show"
- Line 192: should be $x'=gx$
- Line 286: $H_2$ is defined incorrectly
- Line 286: "Then it also minimizes ... can be minimized"
- Line 343: "Effective-ness"
- Line 345: Missing equation number
- Line 363: "m is the number samples"
- Line 377: "Alanine Dipepetide" is misspelled
- Line 388: "direct otimization"
- Lines 754-755: duplicate statements

Experimental setup is not entirely clear. What optimization algorithm was used to minimize losses? How costly is this optimization in terms of number of energy gradient evaluations?

What are the min/max bounds on the 31x31 gridpoints?

### Questions
- The method of discovering effective degrees of freedom is stochastic - would multiple trials from the same initial optimized point be expected to converge to similar effective degrees of freedom? How do the discovered degrees of freedom vary as the initial optimized point is varied?
- Given that the proposed method locally searches for directions where energy remains flat, is it correct that the method would not be able to discover new minima that are separated from the initial point by large energy barriers?
- Starting from a single optimized configuration, is it true that the method only requires calculating the Hessian once?
- What, if any, challenges are expected when applying this method to energy functions defined by neural force fields?

An overview figure visualizing the learned effective degrees of freedom as paths on an energy landscape could help to quickly explain what these effective degrees of freedom are.

Since energy calculation is usually the bottleneck in sampling, one way to quantitatively state your speedup is by listing the number of energy, gradient-energy, and Hessian evaluations required by each method.

Another metric, if just focused on sampling, could be the effective sample size (ESS) as measured for Boltzmann generators:

- Klein, L., Krämer, A., & Noé, F. (2024). Equivariant flow matching. Advances in Neural Information Processing Systems, 36.


The related work section "Identifying the DoF" could touch on more of the "collective-variable-free" literature:
- Sipka, M., Dietschreit, J. C., Grajciar, L., & Gómez-Bombarelli, R. (2023, July). Differentiable simulations for enhanced sampling of rare events. In International Conference on Machine Learning (pp. 31990-32007). PMLR.
- Holdijk, L., Du, Y., Hooft, F., Jaini, P., Ensing, B., & Welling, M. (2024). Stochastic optimal control for collective variable free sampling of molecular transition paths. Advances in Neural Information Processing Systems, 36.

### Soundness
3

### Presentation
1

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The others propose a method that tries to identify the effective degrees of freedom of molecular simulations. They do this 2 ways, with Hessian based methods for small systems, and with a loss function for larger ones. They suggest this can explore the conformation space better.

### Strengths
They describe interesting theory that indeed is useful for molecular modeling.

### Weaknesses
They do not mention existing similar work in machine learning within the last 4 years it seems. 
The figures need to be improved. Which is a? b? c? etc in Figure 1 for instance. 
The results do not seem to match their analysis. Their only experimental results is Ramachandran plots of alanine dipeptide. They mention that 'we see that almost all the Hessian-based methods recover all the major
conformations of alanine dipeptide with relatively short simulation times.'. but this is very difficult to see from their results. All the plots seem to show completely different distributions. 
They do not compare to other baselines in recent literature. (https://pubs.acs.org/doi/10.1021/acs.jctc.4c00454, https://pubs.aip.org/aip/jcp/article/160/17/174109/3287814/Deep-learning-path-like-collective-variable-for,
https://openreview.net/forum?id=TnIZfXSFJAh)
They do not show the distributions of energies of the generated molecules. It could very well be the Ramachandran plots look decent, but the energies are completely off and non-physical. Judging by the molecules they show, it looks like the energies for many of them are very high.

### Questions
Can you plot the distribution of energies?
Can you share the github page?

### Soundness
2

### Presentation
2

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
In this paper, the authors develop two novel approaches for the analysis of degrees of freedom of molecular dynamics simulations. The key idea is to study the symmetry of energy landscape with Lie algebra and further connect the structure dynamics with energy landscape symmetries. Two detailed approaches are considered, including a scalable symmetry loss function and a Hessian-based method. The proposed model has been validated on alanine dipeptide molecular dynamic simulation dataset. The identified two effective degree of freedoms are the two dihedral angles over the peptide bonds, which are consistent with setting.

### Strengths
The authors propose two new models for for the analysis of degrees of freedom of molecular dynamics simulations, by the consideration of symmetry of energy landscape. The method are very novel and interesting. The results on the Alanine dipeptide are consistent with the general setting.

### Weaknesses
1) The method have only be validated on a "toy"-type example of Alanine dipeptide, which contains only two degrees of freedom. It is not clear the potential performance of the model on more general MD simulations, in which more degrees of freedom are standard cases. Further, the authors have not compare with other models. It is not clear what is the potential advantage of the current models over existing models.
2) The code is not available, thus it is hard to really evaluate the algorithm.
3) Even though this is an interesting algorithm for analyzing MD simulation data, it does not fall into the general machine/deep learning category. I would think the paper is more suitable for a computational chemistry/biology journal.  
4) The paper is badly prepared with lots of typos and mistakes. Details will be given in the question part.

### Questions
1) The missing of the code and data for the paper. Thus it is impossible to check or reproduce the results in the paper.
2) Too many typos and mistakes, for instance 
    a1. Page 1, "a symmetry. loss"
    a2. Page 5, "0 The second term"
    a3. Page  7, "equation ??"
    ....
    In general, the paper is poorly prepared! 
3) The advantage of the model and the potential application of models on complicated systems are still not clear. The toy-example of Alanine dipeptide has only two very simple degree of freedom, which should be (easily) identified. What is the advantage of the current model over existing models? How is the potential of using the current model for more realistic complicated MD simulations.

### Soundness
3

### Presentation
2

### Contribution
2
