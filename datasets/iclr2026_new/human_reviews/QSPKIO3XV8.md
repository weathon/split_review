## Human Reviewer 1

### Summary
This paper proposes a method to improve neural operator learning by incorporating a dimension- and domain-aware co-decoder architecture. The key idea is to decouple solution representations into dimension-specific components and domain-conditioned features, then fuse them to approximate the target PDE operator. The authors argue that this decomposition improves generalization and sample efficiency for solving PDEs in different geometric domains and dimensional settings. Empirical evaluation is performed on benchmark PDE problems, comparing against several neural operator baselines, showing lower relative L2 error in some test cases.

### Strengths
- Clarity of high-level motivation: The paper identifies a meaningful and real challenge — neural operator models typically struggle to generalize across domains or dimensional configurations. This is a relevant problem in scientific machine learning.

- Clean architectural formulation: The proposed “co-decoder” idea is structurally simple and easy to integrate with existing neural operator backbones.

- Readable exposition: The manuscript is well structured and technically consistent at the high level, with decent visualizations and clean mathematical notation.

- Experimental setup uses multiple PDE benchmarks: This is a step beyond trivial toy problems, indicating an attempt at broader evaluation.

### Weaknesses
While the problem is important, the contribution is weak both conceptually and empirically:

- Limited novelty:
The central idea—decomposing and fusing dimensional and domain representations—is not fundamentally new. Variants of similar factorization and conditional embedding approaches have already been explored in operator learning, meta-PDE frameworks, and equivariant neural operator designs. The paper lacks a crisp theoretical justification or truly novel algorithmic insight. It feels like another architectural tweak rather than a new paradigm.

- Insufficient baseline coverage:
The paper only compares against basic operator learning baselines (e.g., FNO, DeepONet, or UNet-like variants). To substantiate the claims of improved generalization, it is essential to compare against stronger and more recent models, including: (1) Koopman neural operator as a mesh-free solver of non-linear partial differential equations, (2) Solving High-Dimensional PDEs with Latent Spectral Models. These methods are explicitly designed for high-dimensional PDE problems and constitute state-of-the-art baselines.

- Superficial ablation analysis:
The ablations only show minor performance differences when components are removed. This raises concerns about whether the proposed “co-decoder” mechanism truly drives the reported improvements or if the gains are marginal/random noise.

- Lack of theoretical insight:
The authors repeatedly claim that dimension/domain factorization improves generalization, but no formal analysis or empirical probing (e.g., transfer learning between dimensional settings, robustness to domain shifts) is provided to support these claims.

- Limited scope of experiments:
The experiments are narrowly focused, and it’s unclear whether the method scales or generalizes to more challenging PDEs (e.g., higher-dimensional or irregular geometries). There is no comparison on computational overhead, parameter efficiency, or training stability.

- Unconvincing performance gains:
Even within the provided benchmarks, the improvements are often modest and lack statistical rigor (e.g., no error bars, limited repetitions, unclear significance testing). This weakens the claim of superiority over baselines.

- Overclaiming in narrative:
The abstract and conclusion use strong language (e.g., “universal”, “robust generalization”, “significant improvement”) that is not backed by the presented evidence. This is a recurring issue in weak submissions.

### Questions
- Clarify the real contribution:
What is fundamentally new about the co-decoder mechanism compared to existing conditional or factorized representations used in neural operator models? A clearer theoretical framing or architectural justification is needed.

- Stronger experimental validation:
Please evaluate on more challenging PDE families, including higher-dimensional settings and irregular domains. Include robustness and scalability analyses. Provide multiple runs with error bars to assess statistical significance.

- Ablation rigor:
Conduct deeper ablations: Test the effect of removing either the domain or dimension factor separately. Vary the embedding capacity to show necessity. Test sensitivity to the number of training domains.

- Efficiency and complexity:
What is the computational overhead of the co-decoder compared to baseline neural operators? If the architecture is more complex, does it provide any real benefit in efficiency or generalization to justify it?

- Transfer/generalization tests:
If the paper claims better generalization across domains or dimensions, please provide explicit cross-domain or cross-dimensional generalization experiments, not just single-domain evaluation.

### Soundness
2

### Presentation
2

### Contribution
1

### Rating
0

### Confidence
5

---

## Human Reviewer 2

### Summary
This work combines several popular techniques to solve PDEs with PINNs, including tensor decomposition, domain decomposition, and Mixture-of-Experts (MoE). It is like a technique report not a research paper. The motivation of combining such techniques is not clear. I recommend rejection.

### Strengths
Using a neural network inspired by tensor decomposition is a good idea. In fact, several recent studies have explored solving PDEs with tensor-based neural network architectures.

### Weaknesses
1. The proposed framework simply adds a Mixture-of-Experts (MoE) layer to a dimension-decomposition backbone. This combination seems arbitrary and lacks a clear reason or theoretical justification. The MoE layer makes the model more complex but does not show any real advantage over a well-tuned single network or simpler decomposition methods. The claimed “automatic” domain decomposition is not properly compared with existing, simpler domain decomposition approaches used in PINNs, so its benefit remains unclear.  


2. The reported improvements in accuracy and efficiency are small compared with standard PINNs or other PINN-based methods. The added model complexity and training cost are not justified by the limited gains shown on low-dimensional test problems.

### Questions
see the Weaknesses part.

### Soundness
3

### Presentation
2

### Contribution
3

### Rating
4

### Confidence
5

---

## Human Reviewer 3

### Summary
This paper proposes Dimension Domain Co-Decomposition (3D), a unified framework for solving partial differential equations (PDEs) based on Physics-Informed Neural Networks (PINNs). The framework jointly performs dimension decomposition, which factorizes the solution into dimension-wise components using a shared MLP for parameter efficiency, and domain decomposition, implemented through a Mixture-of-Experts (MoE) mechanism that automatically partitions the solution space into subregions without pre-defined boundaries. In addition, the paper introduces a novel quantitative interpretability metric, Variable Interpretability (VI), which measures how well the learned dimension-wise latent components align with ground-truth factors. Experimental results on several PDE benchmarks (Poisson, Wave, Burgers, and Linear Transport equations) demonstrate that the proposed method achieves improved accuracy, scalability, and interpretability compared to standard PINNs and prior decomposition methods.

### Strengths
1. The paper elegantly combines dimension decomposition and adaptive domain decomposition into a single framework, addressing both scalability and local adaptivity issues in PDE solving.

2. The introduction of the VI metric provides a quantitative way to assess per-dimension interpretability, an aspect rarely considered in PINN literature.

3. The introduction of the shared MLP is well motivated and effectively reduces the parameter count, especially in high-dimensional settings.

4. The evaluation includes multiple types of PDEs (elliptic, hyperbolic, nonlinear), with detailed parameter analysis on rank $r$ and expert number $K$, providing empirical evidence.

### Weaknesses
1. The paper presents a clean combination of dimension decomposition, MoE-based domain decomposition, and a variable interpretability metric. While the empirical results are solid, the theoretical innovation is limited：Both parameter sharing and MoE are well-established techniques. The paper would benefit from a clearer articulation of the core technical challenge or insight specific to this setting, and from theoretical analysis connecting the VI metric to the proposed model’s design to make the contribution more solid.

2. The experiments do not include comparisons with state-of-the-art PDE solvers such as Fourier Neural Operator (FNO) [1], which are highly relevant baselines.

3. Ablations that remove the dimension factorization or the MoE router are necessary to substantiate the co-decomposition claim.

4. Although the paper tests a high-dimensional (10D) Poisson equation, the PDEs considered remain relatively simple. The robustness and generality of the proposed 3D framework would be more convincing if tested on more complex or non-analytically-solvable systems.

[1] Fourier Neural Operator for Parametric Partial Differential Equations.

### Questions
1. Have the authors evaluated the consistency and robustness of the learned domain decompositions？

2. The paper highlights parameter and memory efficiency, but does not report actual training time or convergence comparisons. Could the authors provide quantitative evidence to support the claimed computational advantages of 3D?

### Soundness
2

### Presentation
3

### Contribution
2

### Rating
4

### Confidence
3

---

## Human Reviewer 4

### Summary
The paper proposes a unified Dimension Domain Co-Decomposition (3D) framework that integrates dimension decomposition and Mixture-of-Experts (MoE)–driven domain decomposition for solving high-dimensional partial differential equations (PDEs). The key contributions include:
1. A shared-MLP dimension decomposition architecture that processes coordinate–index pairs, reducing parameters and improving scalability.
2. A Variable Interpretability (VI) metric, which measures the alignment between learned latent dimension representations and ground-truth components.
3. A MoE-based automatic domain decomposition, which adaptively partitions the computational domain without predefined regions or interface constraints.

The framework demonstrates improved accuracy, efficiency and interpretability across several PDE benchmarks. However, certain aspects of the theory and experiments require further clarification. If the authors address these points in their rebuttal, I would be willing to raise my score.

### Strengths
1. **Originality**.
The introduction of the VI metric is a creative and measurable approach to interpretability in PDE learning. The unified framework that combines shared-MLP design for multi-dimensional inputs with MoE based domain decomposition is also an innovation that enhances scalability.

2. **Clarity**.
The paper is generally well-structured, with clear explanations of the architecture, mathematical formulation, and experimental setup. Figures effectively illustrate both the decomposition mechanisms and domain partitions.

3. **Reproducibility**.
The paper provides detailed implementation settings, including network architectures, training procedures, and hyperparameters, ensuring high reproducibility.

### Weaknesses
1. **Lack of theoretical justification for the VI–convergence relationship**.
The paper implicitly proposes an important but unproven proposition: if for all dimensions $j$, $VI_j \to 1$, then the model prediction $\hat{u}$ converges to the true separable solution $u$.
   Currently, this claim is only supported empirically, where high VI values are observed to correlate with low prediction errors. However, no formal mathematical proof is provided to substantiate this relationship.

2. **Fixed number of experts $K$ limits adaptivity and may cause compromise responses**.
The number of experts $K$ is manually chosen rather than learned adaptively. When the PDE solution contains multiple fine-grained or highly localized structures (e.g., shocks, vortices, or high-frequency regions), a fixed small $K$ may fail to provide adequate domain resolution. Consequently, the router’s softmax weighting may average across distinct subregions, diminishing the local specialization property of the Mixture-of-Experts and leading to compromise responses. This design constraint restricts flexibility for more complex or multi-scale problems.

3. **Router–expert coupling risks instability and expert starvation**.
The strong interdependence between the router and experts introduces potential training instability. If an expert achieves slightly lower error early in training, the router may continuously reinforce its weight allocation, causing other experts to receive negligible gradients—a phenomenon known as expert starvation. In problems with rapidly evolving or multi-shock dynamics, delayed router adaptation can further trigger oscillatory expert switching and degrade convergence stability.

### Questions
1. Is it possible to provide a rigorous mathematical justification for VI?

2. During training, was a multi-stage training strategy used, where the routing is fixed first and then the experts are updated, in order to improve overall convergence stability?

3. According to the discussion in Section 3.2, VI is closely related to the separability of the ground truth and the properties of the matrix itself. Why, then, in Table 2, is VI correlated with frequency?

4. In Table 2, the 10-dimensional Poisson requires a smaller $r$ than the 5-dimensional Poisson, which seems somewhat counterintuitive. Conventionally, higher-dimensional problems typically require a larger $r$ to adequately represent multi-dimensional separable structures.

### Soundness
3

### Presentation
3

### Contribution
2

### Rating
4

### Confidence
3