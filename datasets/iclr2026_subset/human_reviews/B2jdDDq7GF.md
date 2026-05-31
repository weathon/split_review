## Human Reviewer 1

### Summary
This paper presents a mathematical framework for identifying both the drift and diffusion terms of stochastic differential equations directly from trajectory data. The authors derive a likelihood-based loss for the drift and a quadratic-variation loss for the diffusion, leading to a consistent and asymptotically normal estimator. They extend the approach to high-dimensional settings by parameterizing these functions with neural networks and demonstrate its performance on synthetic SDEs, interacting particle systems, and stochastic PDEs.

### Strengths
•	Solid theoretical foundation grounded in stochastic analysis.
	•	Clear derivations linking the loss to likelihood and Radon–Nikodym principles.
	•	Implementation details are transparent and reproducible.
	•	Numerical tests validate correctness and convergence rates.

### Weaknesses
•	The work is primarily a statistical estimation study, not a machine-learning or representation-learning contribution.
	•	“Deep learning” (Sec. 3.5) is overstated: networks act only as generic function approximators, not as part of a new ML method.
	•	Experiments are fully synthetic and demonstrate mathematical correctness rather than generalization or learning capability.
	•	Lacks any real or learned high-dimensional data relevant to ICLR (e.g., diffusion generative models, Neural SDEs).
	•	No discussion of computational scaling, sample complexity, or robustness to discrete/noisy observations.
	•	The connection to modern diffusion modeling or score-based generative learning—the key SDE context within ML—is missing.

### Questions
1.	How does this framework relate to Neural SDEs or score-based diffusion models used in generative learning?
	2.	How robust is the approach when data are available only at discrete and noisy time points?

### Soundness
3

### Presentation
3

### Contribution
1

### Rating
2

### Confidence
2

---

## Human Reviewer 2

### Summary
This paper introduces a noise-aware framework for identifying both the deterministic drift and the stochastic diffusion terms in high-dimensional stochastic dynamical systems directly from trajectory data. Unlike methods that treat noise as a nuisance, it jointly learns the full state-dependent and correlated noise structure alongside the drift, using a two-stage approach based on quadratic variation for the diffusion and a likelihood-based loss derived from the Girsanov theorem for the drift. The method is validated on examples like interacting particle systems and stochastic PDEs, demonstrating its ability to handle complex noise and scale to high dimensions using deep learning.

### Strengths
* The general idea is easy to follow
* The proposed method is theoretically grounded and is novel

### Weaknesses
* The "Related Works" section (1.1) should be moved to a later part of the paper. Currently, it discusses specific methods and loss functions before the core model and notation have been introduced in Section 2. This disrupts the logical flow and may confuse readers. Positioning it as an independent section after the methodology would provide the necessary context for the comparisons made.

* The theoretical derivation assumes continuous-time observation. In practice, data is discrete, and the method relies on fine time discretization (Δt is small, e.g., 0.001 in examples). Its performance with sparse, irregular, or low-frequency data is not explored and would likely degrade significantly, as approximations for dx_t and quadratic variation become poor.

* The two-stage process is elegant but creates a pipeline error. Any inaccuracies in estimating $\Sigma$ will propagate into and bias the subsequent drift estimation $f$, as the drift loss function depends on $\Sigma^{-1}$. The paper does not analyze the sensitivity of the final result to errors in the first stage.

* All experiments use synthetic data with known ground truth. There is no evaluation on empirical datasets.

### Questions
* The authors claim superior performance, but the paper lacks comparisons against established baselines. How does the method quantitatively compare against, for instance, a well-tuned Neural SDE or a recent variant of SINDy for SDEs on your own benchmarks?

* You highlight handling "correlated and state-dependent noise," yet key examples use diagonal (IPS) or additive (SPDE) noise. Can you demonstrate the method's performance on a system with a full, non-diagonal, state-dependent diffusion matrix?

* The loss function for the drift is derived from the Girsanov theorem, which is a known concept in stochastic processes. What is the specific algorithmic novelty here? Is it the joint framework, the specific decoupling of the estimation, or the application to high-dimensional learning with NNs?

### Soundness
3

### Presentation
3

### Contribution
2

### Rating
4

### Confidence
4

---

## Human Reviewer 3

### Summary
This paper proposes a noise-aware framework for identifying both the drift and diffusion terms in high-dimensional stochastic dynamical systems from trajectory data. The method is derived from the Girsanov theorem and the Radon–Nikodym derivative, leading to a likelihood-based loss that allows simultaneous estimation of the deterministic and stochastic components without assuming the specific form of the noise model. The authors validate their approach on several examples, including interacting particle systems and stochastic PDEs, and provide theoretical convergence guarantees.

### Strengths
1. The paper provides a solid derivation of the drift loss based on stochastic process theory, which is different from the existing methods.

2. Demonstrations on both finite-dimensional and PDE-type stochastic systems show good performance of the proposed method.

### Weaknesses
1. The paper does not compare with established SDE inference methods such as [R1],[R2],[R3] . Without such benchmarks, it is difficult to assess how much improvement the proposed method offers beyond the existing works.

2. Although the introduction mentions physics, biology, and finance, the experiments are purely toy models. It would be useful to explore whether the method could be applied to financial time series or stock dynamics, where stochastic modeling is central, or to other real data domains such as EEG brain signals.

3. Since the method claims to be noise-aware, it would be important to analyze its behavior under different noise magnitudes or correlated noise.

__References__
[R1] Course, K., & Nair, P. B. (2023). State estimation of a physical system with unknown governing equations. Nature, 622(7982), 261-267.

[R2] Oh, Y., Lim, D. Y., & Kim, S. (2024). Stable neural stochastic differential equations in analyzing irregular time series data. arXiv preprint arXiv:2402.14989.

[R3] Li, X., Wong, T. K. L., Chen, R. T., & Duvenaud, D. (2020, June). Scalable gradients for stochastic differential equations. In International Conference on Artificial Intelligence and Statistics (pp. 3870-3882). PMLR.

### Questions
Q1: How does the proposed method compare quantitatively to recent SDE inference frameworks such as the references [R1],[R2],[R3] mentioned in weaknesses.?

Q2: Can the authors demonstrate or discuss whether the learned model generalizes to real-world stochastic processes, for example, financial or biophysical data?

### Soundness
2

### Presentation
2

### Contribution
1

### Rating
2

### Confidence
4

---

## Human Reviewer 4

### Summary
The paper proposes a new framework for the estimation of SDEs via a novel loss function, which is derived from a suitable negative log-likelihood. The authors derive a convergence result in the case where the estimator belongs to a hypothesis class with finite dimension. They evaluate their approach on two synthetic examples: a system of interacting particles and the stochastic heat equation.

### Strengths
- Clearly written and motivated paper
- Theoretical guarantees: convergence results

### Weaknesses
- Lack of scalability
- Validation only on synthetic data
- No numerical comparison against the state-of-the-art in learning SDEs
- Numerical evaluation limited to relatively small dimension not matching the claim of scalability
- No evaluation on real-world data

### Questions
1/ Could you elaborate on the claim of existence and uniqueness of estimator under your formulation (line 98) ?


2/ Can the theoretical results be maintained if one assumes trajectories that are discrete in time as is the case in practice ?


3/ Since your method requires computing matrix square-root which is cubic in complexity, can you justify your claim of scalability to high-dimensions ?

### Soundness
2

### Presentation
3

### Contribution
2

### Rating
2

### Confidence
3