Now I have a solid calibration. Let me write the final consolidated review.

---

## Summary

This paper proposes a compositional meta-learning framework that formalizes tasks as sequences of reusable computations (module RNNs) selected by a learned gating RNN, and solves new test tasks via probabilistic inference (particle filtering) rather than parameter updates. The framework is well-motivated, clearly described, and the core idea — transforming task acquisition into constrained hypothesis testing within a learned generative model — is both principled and novel. Results on two synthetic domains (6D shift operations and 2D motor trajectories) demonstrate that the model can recover ground-truth modules and transition statistics, perform one-shot inference under sparse feedback, and generalize to longer tasks. However, the experimental validation is limited to very simple, low-dimensional tasks that match the model's assumptions, and the empirical evidence falls short of the paper's broader claims.

---

## Strengths

1. **Principled and novel framework.** The paper formalizes compositional meta-learning as inference in a learned probabilistic generative model (Equations 1–8), combining RNN expressivity (gating RNN for non-Markovian transition structure, module RNNs for arbitrary emission functions) with the machinery of particle filtering. This is a clean and conceptually appealing departure from gradient-based meta-learning and prior modular approaches that still require parameter updates at test time (e.g., Rosenbaum et al., 2017; Ponti et al., 2022).

2. **One-shot inference without parameter updates is qualitatively faster than gradient-based meta-learning.** Figure 3e directly shows that the proposed method (grey) infers a held-out test task from a single episode (MSE drops immediately below 0.1), while MAML, MLDG, and pre-trained RNNs require hundreds of episodes to reach comparable performance. This difference is genuinely qualitative — not incremental — and directly supports the central thesis that inference can substitute for weight updates.

3. **Clear demonstration of sparse-feedback and length-generalization capabilities.** Figures 2e–f and 4e show that the model maintains coherent hypotheses during long feedback-free periods (the gating RNN constrains possible module sequences based on learned durations), and generalizes to tasks four times longer than any training task. These are non-trivial behaviors that emerge from the interaction of the learned gating dynamics and the particle filter, and are uniquely enabled by the framework.

4. **Systematic ablations identify the specific contribution of each architectural component.** Figure 3a–d compares the full model against three controls (RNN without task identity, RNN with task identity, model with flat transitions). Only the full model succeeds on test tasks under sparse feedback, providing direct evidence that both the modular architecture and the learned gating are necessary for the claimed capabilities.

5. **Domain transfer demonstrated across rule learning and motor learning.** Section 2.4 shows that the same framework recovers ground-truth motor skills and transition statistics, and performs one-shot inference under sparse feedback in a trajectory-composition domain, supporting generality beyond the rule-learning setting.

---

## Weaknesses

### Fatal
None.

### Major

1. **Experimental validation is on extremely simple, low-dimensional synthetic tasks, far below what the paper's framing implies.** The core demonstrations use only two tasks: 6D linear shift operations (essentially permutation matrices) and 2D straight-line motor skills with fixed durations. Both are hand-crafted so the ground-truth modular structure exactly matches the model's assumptions (correct number of modules, fixed durations, deterministic transitions). The paper frames the approach as "join[ing] the expressivity of neural networks with the data-efficiency of probabilistic inference," but provides no evidence that (a) the particle filter scales to high-dimensional observations, (b) the gating RNN can handle complex, variable-duration task grammars, (c) the modules can learn anything beyond near-linear transformations, or (d) the method works on any established meta-learning benchmark (e.g., Omniglot, Mini-ImageNet, or a realistic continuous control task). The paper acknowledges its "proof-of-principle" nature, but for a top venue the gap between the claims and the evidence is too large. A single medium-scale benchmark would significantly strengthen the paper.

2. **No comparison to other modular meta-learning methods.** The paper mentions Alet et al. (2019) as the most similar approach ("We effectively replace this search by probabilistic inference on learned structure, greatly improving sample efficiency") but provides no empirical comparison. The comparison class in Figure 3e is limited to gradient-based methods (MAML, MLDG) and general pre-training, which are not designed to exploit modular structure. A direct comparison to Alet et al. or other modular approaches on the same tasks is needed to substantiate the claim that the probabilistic inference mechanism yields quantitative benefits over search-based modular methods.

3. **The gating RNN learns fixed, task-independent durations that limit applicability.** The task design assigns each module a fixed, deterministic duration (3/4/5 steps) that is identical across all tasks. The gating RNN learns these exact durations and relies on them for sparse-feedback reasoning. In real-world settings, operations rarely have such rigid, fixed durations — the duration of a "chopping" skill varies depending on the ingredient. The paper does not address how the model would handle variable-duration chunks or whether it could learn duration distributions rather than fixed counts.

### Minor

1. **Fixed number of modules is assumed.** The model is given exactly the same number of modules as ground-truth operations. While Appendix A1 (referenced) shows some robustness to mismatch, the paper acknowledges this as a limitation and discusses dynamic module addition only as future work. This reduces practical applicability, though it does not invalidate the core contribution.

2. **Gradient computation through the particle filter is underspecified.** The paper states that parameters are optimized "through gradient descent on negative log marginal likelihood, backpropagating the loss through the particle filter" using "the gumbel-softmax reparameterisation trick to calculate gradients through the sample of Equation 2." However, gradients through the resampling step (Equation 6) — a known challenge for differentiable particle filters — are not discussed, and no reference to a standard differentiable particle filter technique is cited. The reproducibility statement mentions full code, which mitigates this, but the technical specification in the paper itself is incomplete.

3. **No analysis of computational cost or scaling behavior.** The paper does not report particle count, training time, inference time, or how these scale with problem dimensionality. This makes it difficult to assess whether the approach is practical beyond toy tasks.

### Trivial
None.

---

## Nice-to-Haves

- Evaluation on a medium-scale benchmark where modular structure is plausible but not hand-crafted (e.g., a continuous control task like learning motor primitives in DM Control, or a visual reasoning benchmark like CLEVR).
- Empirical comparison to Alet et al. (2019) on the same tasks.
- Analysis of how performance varies with the number of particles and training data size.
- Investigation of variable-duration module sequences (e.g., durations drawn from a distribution rather than fixed).

---

## Removed Points

- **"Unfair comparison to gradient-based meta-learning"** (Harsh Critic, Critical Issue #2 framed as structural unfairness): The comparison to MAML/MLDG is not "unfair" — the paper is comparing inference-based vs. gradient-based adaptation, which is a legitimate comparison to contextualize the speed difference. The task favors the modular approach by construction, which is expected when evaluating a compositional method. The real gap is the lack of comparison to other modular methods, which is captured as Major weakness #2 above. *[Demoted from the original framing of structural unfairness to the specific gap of missing modular baselines.]*

- **"Critical training details underspecified threatening reproducibility — appendix not available"** (Harsh Critic, Critical Issue #3, appendix-specific portion): Per the hard rules, weaknesses about missing appendix content are removed because the parser strips appendices from all papers. The gradient-through-resampling concern is retained as a Minor weakness (see above), but the complaint that "the appendix might contain this, but it's not available in the review" is removed. *[Partially retained as Minor weakness #2.]*

- **"Method is demonstrated only where number of modules is known a priori"** framed as reducing contribution significance (Harsh Critic, Critical Issue #4): The paper acknowledges this limitation and shows some robustness to mismatch (Figure A1). This is retained as Minor weakness #1 but downgraded from the harsh critic's severity framing, since it is openly discussed and partially addressed. *[Retained as Minor weakness #1.]*

- **Strength Finder claims about "domain generality" and "principled probabilistic formulation":** These are valid but somewhat generic. They are retained but calibrated: the domain generality is real (rule learning + motor learning) but both are toy domains, so the strength is real but tempered. The "principled formulation" is indeed a strength and is retained as Strength #1.

- **Strength Finder generic strengths about "important problem":** Removed. "The paper focuses on an important problem" is generic and does not distinguish the paper.

---

## Novel Insights

None beyond the paper's own contributions. The reviews converge on the same assessment: the framework is novel and elegant, but the experiments are too limited for the claims.

---

## Suggestions

1. **Add at least one medium-scale benchmark.** A continuous control task with plausible modular structure (e.g., DM Control's dog or quadruped, where gaits can be composed) or a visual reasoning benchmark would substantially increase credibility. This is the single most impactful improvement.

2. **Compare to modular meta-learning baselines (especially Alet et al., 2019).** The paper claims that probabilistic inference is better than search — this should be demonstrated empirically.

3. **Specify the gradient estimation through the particle filter more precisely.** Cite the relevant differentiable particle filter technique (e.g., Karkus et al., 2018) or describe the custom gradient estimator used.

4. **Report computational cost.** Number of particles, training wall time, and inference wall time for the current tasks would help readers assess scalability.

5. **Discuss variable-duration modules.** Even a simple experiment where module durations vary across tasks would clarify whether the current fixed-duration design is essential or incidental.

---

## Score and Decision

**Round 1 bracketing**: Weak anchors (avg ~2–3) include papers on meta-interpretability and projected subnetworks — clearly weaker than this paper. Strong anchors (avg 8+) include papers on learning-to-defer and hyperbolic VLMs — clearly stronger and different domains. The paper sits in the middle band (3.5–7.5).

**Round 2 narrowing**: Within the middle band, three comparison anchors are most informative:

- **"Discovering modular solutions that generalize compositionally"** (avg 6.50, accepted): Studies modular meta-learning via teacher-student hypernetworks with theoretical results + experiments on complex environments (2D navigation, continuous control). Stronger than the current paper due to theoretical grounding and richer experiments. Current paper is weaker.

- **"Compositional Interfaces for Compositional Generalization"** (avg 4.75, rejected): Modular architecture for compositional generalization in a toy grid-world environment. Criticized for limited contribution and toy setting. Current paper has a more novel framework and cleaner results — it is stronger.

- **"When and how are modular networks better?"** (avg 4.25, rejected): Controlled study on boolean functions and MNIST. No novel method, just analysis. Current paper is clearly stronger in both method novelty and result quality.

The paper is clearly above the 4.25–4.75 rejected-anchor level: it has a genuinely novel framework, well-motivated design, and clean demonstrations of non-trivial capabilities (sparse feedback, length generalization). However, it falls well short of the 6.5 accepted-anchor level because it lacks theoretical results and experiments on problems of realistic complexity. The gap between the paper's ambitious framing and its proof-of-principle experiments is the decisive factor.

**Final score**: **5.0** — a paper with a novel and promising framework and clean proof-of-principle results, but whose experimental validation is too limited for acceptance at a top venue. The core ideas are publishable and should be encouraged, but require at least one realistic benchmark to cross the acceptance threshold.

**Decision**: **Reject**

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>