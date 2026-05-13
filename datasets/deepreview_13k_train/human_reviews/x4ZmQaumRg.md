# Active Learning for Neural PDE Solvers

- Decision: Accept
- Scores: 8, 6, 8, 6

## Abstract
Solving partial differential equations (PDEs) is a fundamental problem in engineering and science.  While neural PDE solvers can be more efficient than established numerical solvers, they often require large amounts of training data that is costly to obtain. Active Learning (AL) could help surrogate models reach the same accuracy with smaller training sets by querying classical solvers with more informative initial conditions and PDE parameters. While AL is more common in other domains, it has yet to be studied extensively for neural PDE solvers. To bridge this gap, we introduce \alforpde{}, a modular and extensible active learning benchmark. It provides multiple parametric PDEs and state-of-the-art surrogate models for the solver-in-the-loop setting, enabling the evaluation of existing and the development of new AL methods for PDE solving. We use the benchmark to evaluate batch active learning algorithms such as uncertainty- and feature-based methods. We show that AL reduces the average error by up to 71\% compared to random sampling and significantly reduces worst-case errors. Moreover, AL generates similar datasets across repeated runs, with consistent distributions over the PDE parameters and initial conditions. The acquired datasets are reusable, providing benefits for surrogate models not involved in the data generation.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper provided a bechmark called AL4PDE, which unifies active learning (AL) with neural PDE solvers. Specifically, it studies how several state-of-the-art neural surrogate model may be applied to solve parametric PDEs under a solver-in-the-loop (AL) setting. A complete set of numerical experiments on various tasks is included to justify the effectiveness of AL based methods compared to methods based on random sampling.

### Strengths
Extensive numerical experiments on multiple PDEs are provided to validate the effectiveness of the proposed methodology. Also, details about the numerical experiments, such as the neural network models and training procedures, are included for the sake of completeness.

### Weaknesses
1. Though the authors have conducted a literature review on how AL has been used for solving other problems from scientific ML, such as PINN and direct prediction, it seems to the reviewer that the authors have missed a few important references like [1,2]. It might be meaningful for the authors to include these work and briefly discuss them in the introduction. 

2. Given that this work aims for a complete benchmark on various tasks, the authors might consider including some more experiments on high-dimensional PDEs, just like the setting of [3]. The current experiments, while extensive, are limited to relatively low-dimensional problems, which might not fully capture the challenges in real-world applications involving complex, high-dimensional systems. The benchmark would benefit from the inclusion of such cases to demonstrate the scalability and robustness of the proposed AL framework.


### Questions
The parameter $c$ mentioned in line 96-97 (referred to as the field variables or channels) seems a bit ambiguous here as the following PDE doesn't contain anything about $c$. Would it be possible for the authors to provide more detailed explanation for the field variable/channel $c$ here? (This also highly relates to the parameter $N_c$ appearing in equations (3) and (5).)

References:

[1] Bruna, Joan, Benjamin Peherstorfer, and Eric Vanden-Eijnden. "Neural Galerkin schemes with active learning for high-dimensional evolution equations." Journal of Computational Physics 496 (2024): 112588.

[2] Gajjar, Aarshvi, Chinmay Hegde, and Christopher P. Musco. "Provable active learning of neural networks for parametric PDEs." In The Symbiosis of Deep Learning and Differential Equations II. 2022.

[3] Gao, Wenhan, and Chunmei Wang. "Active learning based sampling for high-dimensional nonlinear partial differential equations." Journal of Computational Physics 475 (2023): 111848.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a benchmark framework for neural PDE solvers under active learning (AL) settings (AL4PDE). It provides a modular benchmark with various parametric PDEs and AL methods. The experimental results show that AL significantly reduces average and worst case errors compared to random sampling and yields reusable datasets across experiments.

### Strengths
The paper is well-presented and easy to follow.

The proposed framework is novel in extending neural PDE methods with active learning methods.

The benchmark includes various batch selection strategies and neural PDE solvers, covering recent and classical works.

### Weaknesses
One key benefit of AL is data efficiency, which is also stressed in the paper. It is important to show how much data reduction can be achieved with reasonable model performance. Current experiment section only shows performance comparison of different active learning methods and lacks the "offline" performance, which is training the model with full dataset and evaluate its performance.

At line $88$, the author claims "We demonstrate that using AL can result in more accurate surrogate models trained in less time." As mentioned above, this claim is not supported with empirical evidence as the experimental section only compares active learning performance, which cannot demonstrate improvement in accuracies regarding offline performance.

The novelty of this framework seems limited, as it is a combination of existing AL and neural PDE methods.

### Questions
Please refer to the strengths and weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
Thie article introduces an active learning benchmark for neural PDE solver. It compare exploration-exploitation tradeoffs based uncertainty (epsitemic uncertainty of an ensemble of models with top-K and SBAL) or features (using dimensionality reduction using Gaussian sketching with Core-Set and LCMD). The authors then show a benchmark of these method on 1D and 2D parametric PDEs adding the baseline of sampling uniformly at random to represent the lack of active learning.

### Strengths
Contributing a benchmark in active learning for PDE solvers fills a needed gap in computational infrastructure for PDE solvers that is key to the central challenge of data efficiency.
The article is pedagogical and presents clearly the capability of the benchmark.

### Weaknesses
The authors should help compare methods of Bayesian active learning and those of the field of design of experiments (DoE), which is missing in the literature review. For example, instead of using a baseline of uniform sample, Latin Hypercube sampling should be provided, as well as more sophisticated DoE methods. This benchmark effort is an opportunity to bridge these areas of research and communities that try to solve the same problem with a slightly different point of view and a different approach.

The benchmark should broaden the UQ methods by connecting to existing efforts (for example, the open-source UQ 360). Any UQ method that provide a confidence interval should suffice for active learning as the spread of the confidence interval can be a proxy of the uncertainty.

In the implementation details, the tradeoffs of the choice of taking the spatial average over the features to make make feature-based AL translation invariant are not discussed. It seems that the averaging creates a significant dimensionality reduction that may outweigh the benefits of a translational invariance in terms of data efficiency.

All the implementations use periodic boundary conditions, which significantly limits the scope of applications.

### Questions
Could you please add baselines form DoE?

Could you link your benchmark code to existing open source code for uncertainty quantification (e.g. UQ 360)?

Could you explain the tradeoffs of reducing the dimensionality of features vs. implementing translational invariance in terms of data efficiency of the feature-based AL?

Could you add examples that do not use periodic boundary conditions?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes a modular active learning (AL) framework for training surrogate models of partial differential equation (PDE) solvers. It introduces a numerical solver for generating PDE samples, several surrogate models, batch selection strategies, and acquisition functions designed for active learning within this framework.

### Strengths
The well-designed modular framework provides a solid foundation for further research on active learning in the context of PDEs.

### Weaknesses
1. Although the framework is tailored for PDE problems, the implemented acquisition functions are orthogonal to PDE problems i.e. they are AL methods that are used in general domains. As a framework of AL for PDE, at least some PDE-specific AL methods such as adaptive sampling [1], also mentioned in Related Work, should be also implemented.

2. The paper’s scope in terms of the surrogate models, acquisition functions, and types of PDEs studied is quite limited, impacting its practical applicability.

### Questions
No question

### Soundness
3

### Presentation
3

### Contribution
2
