## Human Reviewer 1

### Summary
This paper introduces ShadowFM, a generative framework for learning quantum ground states from their classical shadows. The core idea is to apply geometric flow matching on non-Euclidean manifolds inspired by the Bloch sphere, rather than using standard Euclidean approaches. By respecting the intrinsic geometry of quantum measurements, the proposed methods, Spherical Flow and Anisotropic Dirichlet Flow, compared to vanilla flow matching, achieve more accurate predictions of physical observables like correlation functions.

### Strengths
The paper introduces a novel framework by applying geometric flow matching to learn classical shadows of quantum states. It thoughtfully motivates this approach by connecting the non-Euclidean structure of quantum measurements to the Bloch sphere, a departure from prior works that assumed Euclidean geometry.

The proposed "Spherical Flow" and "Anisotropic Dirichlet Flow" methods are empirically validated on the Transverse-Field Ising and Heisenberg models.

### Weaknesses
1. The major weakness is the paper's structure and writing. A significant portion of the early sections is dedicated to explaining well-established concepts, which may be inefficient for an expert audience at ICLR conference.
- Sections 2.1, 2.2, 2.3 and Section 3 provide lengthy introductions to Classical Shadows and flow Matching. While context is necessary, these concepts are foundational and could likely be summarized more concisely, perhaps by focusing only on the specific aspects directly built upon by the authors. This would free up valuable space to elaborate on the novel contributions. If the author desires to present more specific or self-contained content, detailed information (including Algorithm 1 and 2) can be placed in the appendix.
- Furthermore, the motivation in Section 4.1 is good, but the preceding three pages of background and related works dilute the paper's focus and delay the reader's engagement with the key ideas. In a highly competitive venue, it's crucial to present the core innovation as early and clearly as possible. 

A more effective structure might have been to briefly introduce the necessary concepts from FM and classical shadows within the introduction or a much shorter, combined background section, and then move directly to the motivation and detailed methodology of ShadowFM.

2. The paper's core methodological sections (4.2 and 4.3) blend established theory with the authors' modifications. It would be better if the authors delineate their novel technical contributions from the baseline frameworks of RFM and DFM. As presented, it is difficult to isolate the exact innovations beyond the application of existing tools to a new domain.

3. For the Anisotropic Dirichlet Flow, the increased methodological complexity does not consistently yield superior performance over the simpler Spherical Flow (e.g., in the Heisenberg model results of Table 3). What is the justification for this more complex model if its empirical advantage is not universally demonstrated across the tested problems?

4. A critical observation from Table 1 is that the learning-free Classical Shadow baseline consistently outperforms all trained generative models, especially on the correlation metric and in the high-sample regime. Could the authors explain this performance gap and justify the practical utility of the generative approach if it fails to surpass a direct, learning-free estimation method?

4. The primary motivation for introducing a non-Euclidean geometry is an experiment (Figure 2) suggesting that "spin errors" (e.g., $|X^{+}\rangle \rightarrow |X^{-}\rangle$) are significantly more detrimental than "basis errors" (e.g., $|X^{+}\rangle \rightarrow |Y^{\pm}\rangle \text{or} |Z^{\pm}\rangle$). However, the provided plot does not strongly support this claim. The performance gap between the two error types appears marginal across the tested error rates. The paper's assertion that spin errors are "significantly higher"  seems overstated. This weakens the central premise that a geometry specifically designed to maximize the distance between spin-flipped states is necessary and justifies the added model complexity.

5. The paper's experiments compare the proposed methods primarily against other flow-matching variants. This comparison is too narrow and fails to benchmark against the true state-of-the-art in generative modeling for quantum states. Crucially, there is no comparison against machine learning models such as [1,2,3] and a benchmark [4], which have shown strong performance on similar tasks.

[1] Huang H Y, Kueng R, Torlai G, et al. Provably efficient machine learning for quantum many-body problems[J]. Science, 2022, 377(6613).

[2] Wang H, Weber M, Izaac J, et al. Predicting properties of quantum systems with conditional generative models[J]. arXiv preprint arXiv:2211.16943, 2022.

[3] Yao J, You Y Z. ShadowGPT: Learning to Solve Quantum Many-Body Problems from Randomized Measurements[J]. arXiv preprint arXiv:2411.03285, 2024.

[4] Zhao Y, Zhang C, Du Y. Rethink the Role of Deep Learning towards Large-scale Quantum Systems[C]. Forty-second International Conference on Machine Learning, 2025.

### Questions
The selection of "Generative Models" as the primary area suggests the paper's main contribution lies in advancing the fundamental methodology of generative modeling. While the paper does introduce novel geometric adaptations to flow matching, these innovations are exclusively motivated, designed for, and validated on the specific problem of learning quantum states. This raises a crucial question about the work's intended contribution and audience. The work might be more appropriately positioned within an area like "Applications to Physics".

### Soundness
3

### Presentation
2

### Contribution
2

### Rating
2

### Confidence
3

---

## Human Reviewer 2

### Summary
The paper introduces Shadow Flow Matching, a geometric and generative framework for modeling quantum measurement data. Rather than treating measurement outcomes as raw values, the authors embed them into a cross-polytope manifold that captures the symmetry and combinatorial structure of Pauli measurements, essentially a high-dimensional, geometry-aware analogue of the Bloch sphere. Within this space, they apply flow matching to learn distributions of outcomes conditioned on Hamiltonian parameters, allowing the model to follow the curved geometry of quantum shadows instead of a flat Euclidean one. This leads to smoother sampling and better reconstruction of observables like correlation matrices and entanglement measures, even under noise or limited data. By blending geometric insight with generative modeling, the work moves beyond treating quantum data as structureless, aligning machine learning more closely with the intrinsic geometry of quantum mechanics.

### Strengths
1. Mapping quantum measurements into a cross-polytope space is an original and elegant idea—it captures the symmetries of Pauli measurements while moving beyond standard Euclidean embeddings.

2. The paper nicely links discrete measurement data with continuous geometric flows, bringing flow-based generative modeling into quantum ML in a fresh and promising way.

3. The framework shows solid potential for tasks like shadow tomography, expectation reconstruction, and entropy estimation, where structure-aware modeling really helps.

4. The theory and context are well presented, clearly explaining why a geometric approach makes sense and how it connects to broader machine learning and quantum ideas.

5. The visualization of the cross-polytope flow is particularly interesting, helping to convey the intuition behind how flow trajectories respect geometric constraints and how they differ from flat-space generative flows.

### Weaknesses
1. Despite its novelty, the scope of practical applications appears somewhat narrow at this stage. The framework’s advantages are demonstrated primarily on specific shadow-based tasks, and it remains uncertain how easily the approach can scale to broader or more complex domains of quantum learning.

2. A current limitation is the method’s dependence on the structure of Pauli shadows. Since the model architecture and training procedure hinge on these symmetries, adapting it to non-Pauli or arbitrary measurement settings could require substantial reworking of the geometric foundation.

3. The empirical evaluation is somewhat underdeveloped. Comparisons are made to only one baseline, and while qualitative results are encouraging, they leave open questions about quantitative robustness and competitiveness against state-of-the-art generative quantum models.

### Questions
1. Are the current experiments confined to the 1D anti-ferromagnetic Heisenberg model, or has the framework been tested on other many-body systems?

2. How does the proposed approach compare to diffusion-based quantum models, such as Generative Quantum Machine Learning via Denoising Diffusion Probabilistic Models? 

3. Given the method’s dependence on Pauli-based shadows, could the framework extend to alternative measurement protocols like? Is the model’s success contingent on Pauli-specific symmetry?

4. Could this geometric-flow framework be repurposed for broader quantum modeling tasks—for instance, simulating quantum dynamics?

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

---

## Human Reviewer 3

### Summary
The paper presents Shadow FM, which is a flow based method to generate Pauli POVM measurements of a quantum ground state. The Hamiltonian of the system can be used as a conditioning input to generate these samples. There are two approaches in the paper: (i) a spherical / Riemannian flow aligned with the Bloch-sphere geometry and (ii) an anisotropic Dirichlet probability path. The authors test their methods on Heisenberg and TFIM chains.

### Strengths
The paper is well writing and the flow matching framework that the paper uses is well motivated by the geometry of the quantum states. Being a non-autoregressive method is also a positive,  as the shadow distribution is unlikely to have 1D nature for interesting quantum states. The experiments are thorough and interesting.

### Weaknesses
1. All the experiments presented are for 1D models. This is a concerning as the ground states of 1D models have efficient classical representation in terms of MPS representations. 2D experiments would have substantially improved the quality of the results

2. Motivation of restricting to ground states of Hamiltonians is unclear to me? Why not thermal states or states produced by real time evolution? I don't see the learning task itself using any information about the fact this is a ground state of a Hamiltonian.

### Questions
1. For learning ground states, could this method be enhanced by adding a variational component to the loss that also tries to minimize the estimated energy of the state?

2. What is the main bottleneck faced by the authors to go to 2D experiments?

3. In the phase transition studies, do the authors observe any changes in the behavior of the learning algorithm across the phase transition?

4. How do the authors ensure that the distribution over shadow states that the learned model samples from for a new Hamiltonian actually correspond to a physically allowed quantum state? Can a projection step be built into the inference pipeline to project to physically allowed states?

### Soundness
3

### Presentation
2

### Contribution
3

### Rating
6

### Confidence
4

---

## Human Reviewer 4

### Summary
The paper introduces ShadowFM, a geometric flow matching framework for learning ground-state quantum many-body wavefunctions via the distribution of classical shadows.
Instead of modeling full quantum states, ShadowFM learns to generate shadow measurements—compact randomized representations of quantum states—and uses them to estimate physical observables such as correlation functions and entanglement entropies.

### Strengths
- Originality: the paper presented a novel framework called ShadowFM that combines low matching generative modeling with classical shadow tomography for learning quantum many-body ground states.
- Quality: The technical development looks sound and link both geometric and quantum information theory. The paper demonstrates a good understanding of both and integrates them coherently. 
- Clarity: The paper is clearly written, with a well-organized structure. Figures and tables of experiments look good. 
- Significance: The work study a problem that is significant in bridging geometric deep generative modeling and quantum many-body learning. It proposes a scalable, data-driven alternative to classical shadow reconstruction and autoregressive models.

### Weaknesses
- Computational overhead: The anisotropic Dirichlet flow requires precomputing and integrating Beta-function–based terms, which could limit practicality; runtime and memory costs are not quantified in very detail.
- Restricted empirical scope: Experiments are limited to 1D spin chains (TFIM and Heisenberg). The scalability and performance of ShadowFM on larger or higher-dimensional systems are not demonstrated.

### Questions
- Could the authors explain more about the scalability of their methods? For example, for Heisenberg model, could the experiments for $L=30$ be conducted? Also, what about other models?

### Soundness
3

### Presentation
3

### Contribution
2

### Rating
4

### Confidence
2