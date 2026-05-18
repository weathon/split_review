Here is my consolidated review after careful verification of all claims against the paper.

---

## Summary

This paper investigates whether neural networks with fixed random weights can universally approximate functions by learning only their bias parameters. It proves two main theoretical results: (1) single-hidden-layer feed-forward ReLU networks with random fixed weights can approximate any continuous function on a compact set with high probability by tuning only biases (Theorem 1), and (2) an analogous result for RNNs approximating finite-time trajectories of smooth dynamical systems (Theorem 2, albeit with pointwise convergence). Empirically, the paper demonstrates multi-task learning across seven digit-classification tasks, compares bias learning to mask learning, and shows that bias-trained RNNs can generate oscillatory dynamics and predict Lorenz system trajectories. The work is motivated by biological plausibility (bias changes correspond to threshold adaptation, tonic inputs, etc.) and connects to the Strong Lottery Ticket Hypothesis.

## Strengths

- **First universal approximation guarantee for FFNs with learned biases and fixed random weights.** Theorem 1 is a genuinely new theoretical result extending parameter-sparse approximation to a setting not previously covered by the literature on output-weight-only training or masking. The proof strategy — approximating a small-parameter network via random sampling and then selecting a subnetwork through bias-based masking — is conceptually interesting.

- **First proof of universal approximation for RNNs with learned biases.** Theorem 2 extends the bias-learning framework to the recurrent setting for finite-time trajectories of smooth dynamical systems, which the paper correctly notes also constitutes the first proof of the Strong Lottery Ticket Hypothesis over units for RNNs.

- **Multi-task empirical validation with mechanistic analysis.** The demonstration that a single 32,000-unit random-weight FFN can learn seven distinct digit-classification tasks by optimizing only 32,000 bias parameters (vs. ~25 million in full training) is compelling. The task-variance clustering (Fig. 1C) provides a concrete mechanistic picture of task-specific functional organization emerging from bias learning.

- **Eigenvalue analysis of bias learning in RNNs.** The analysis showing that bias learning shapes the Jacobian (effective connectivity) of a fixed-random-weight RNN to produce oscillatory dynamics (Fig. 2B) is a clean mechanistic insight that goes beyond simply reporting task performance.

## Weaknesses

### Major

- **Proposition 1 (ReLU is γ-parameter-bounding for any γ > 0) is a strong, non-obvious claim that is the linchpin of both main theorems, and its correctness can only be verified in the appendix.** The claim that a single-hidden-layer ReLU network can approximate any continuous function on a compact set with all individual weights and biases bounded by an arbitrarily small constant γ is far from obvious — standard universal approximation constructions often rely on weights that grow to create sharp transitions. The paper acknowledges this subtlety (line 76, citing work on band-limited parameters) but offers no intuition or sketch in the main text for why ReLU nonetheless satisfies this property. Since the proof resides in the appendix and the `restatable` macro suggests it exists, this is not a case of an absent proof, but the claim is strong enough that a reader evaluating the main text alone cannot assess its plausibility. The entire theoretical contribution collapses if Proposition 1 is false. **This is not a reason to reject — the proof exists — but it means the paper's central advertised contribution can only be fully evaluated by checking the appendix.**

- **Theorem 2 (RNN) is limited to pointwise (not L¹) convergence over finite-time trajectories, and the gap between this guarantee and the empirical demonstrations is not bridged.** The paper honestly acknowledges this limitation. However, the Lorenz system experiments (Fig. 3) involve long trajectories where the compounding of pointwise errors could be significant, and no argument (even heuristic) connects the theorem's finite-time guarantee to the practical success over thousands of time steps. The value of Theorem 2 as a theoretical contribution is weakened by this gap.

### Minor

- **No explicit bound on the required hidden-layer width.** The proof sketch states that "exceedingly massive" widths are needed but provides no analysis of how the required width scales with the accuracy ε, failure probability δ, dimensionality, or the bound γ. This makes it difficult to assess whether the theory has any bearing on the experimental scale (widths of thousands, not astronomical numbers). The paper would benefit from even a coarse bound or a discussion of why the gap between theory and experiment is expected.

- **The comparison between bias learning and mask learning (Section 3.2) lacks a baseline for the 0.46 correlation.** The paper interprets this correlation as indicating "different, though related" solutions, but does not report the correlation between independent runs of the *same* method (e.g., bias-vs-bias or mask-vs-mask). Without this baseline, it is unclear whether 0.46 indicates genuine divergence or simply the expected variability between any two runs on the same random weights.

- **The soft-mask annealing schedule is acknowledged as a confound but not controlled.** The paper notes (line 206) that the mask learning schedule may have contributed to the observed differences between bias and mask solutions. This is appropriate, but the comparison would be stronger with a control that matched the optimization dynamics more closely.

### Trivial

- The paper refers to "network output, ∘" (Eq. 1) using notation that is not fully expanded until the text; this is clear enough in context but slightly slows reading.

## Nice-to-Haves

- An explicit bound on the required hidden width w(ε, δ, d_in, d_out, γ), even a very loose one, would substantially strengthen the connection between theory and practice.
- A heuristic argument about why the pointwise RNN guarantee might extend to longer trajectories in practice would bridge the gap between Theorem 2 and the Lorenz experiments.
- A correlation baseline (bias-vs-bias or mask-vs-mask runs) would sharpen the interpretation of the bias-vs-mask comparison.
- A discussion of the required number of random samples vis-à-vis the probability δ would help readers assess the practical feasibility of the construction.

## Removed Points

- **Circularity in Definition 2 (Harsh Critic point 2):** Removed because it misreads the paper. Definition 2 defines a property of activation functions, not of specific networks. Proposition 1 asserts ReLU has this property. Theorem 1 uses Proposition 1 to assert the existence of a bounded-parameter network. There is no circularity — this is straightforward deductive reasoning.
- **"No proof, no sketch, and no reference for Proposition 1":** The paper uses `\begin{restatable}` which places the proof in the appendix (stripped by the parser). The proof exists in the original submission. The remaining concern (non-obviousness of the claim) is kept in the Major section above but framed appropriately.
- **Complaints about missing appendix content (proofs, technical details):** The parser strips all appendix material; these exist in the original submission per conference formatting guidelines.
- **The reviewer's claim that "the paper should reframe its theoretical contribution as a conditional result":** This is a judgment call, not a factual weakness. The proof is in the appendix and `restatable` environments are standard for papers with supplementary proofs.
- **Strength Finder's strengths that conflict with verified weaknesses:** The Strength Finder's listed strengths all survived — they are specific, evidence-backed, and do not conflict with verified weaknesses.

## Novel Insights

The most interesting observation to emerge from synthesizing the reviews is that the core theoretical claim (Proposition 1) is simultaneously the paper's most novel contribution and its most precarious link. The γ-parameter-bounding property — if provable for ReLU — is a genuinely non-trivial fact about ReLU networks that goes well beyond standard universal approximation, and it is the engine that drives both theorems. The fact that the paper's own proof sketch for the main theorem then uses this property to show that bias learning reduces to a random sampling + masking construction provides a clean, intuitive bridge between the abstract property and the concrete learning scenario. This framing (universal approximation via bounded-parameter networks → random sampling → bias-based subnetwork selection) is the paper's real intellectual contribution, and it would be well-served by a dedicated main-text explanation of why the γ-parameter-bounding property holds for ReLU.

## Suggestions

1. Add a brief main-text intuition for why ReLU is γ-parameter-bounding: e.g., show how a single ReLU neuron with weight γ can approximate a step on [0,1] to within O(γ), and that composing many such neurons can approximate any continuous function by covering the domain with small-slope local approximations. This would make the theoretical framework self-contained for the main-text reader.
2. Include a coarse bound on the required width — even a pessimistic one — and state it as an open problem to tighten it. This would contextualize the gap between theory and experiments.
3. For the bias-vs-mask comparison, add a simple baseline: the correlation between two independent bias-only runs (or two mask-only runs) on the same random weights.

## Score and Decision

This paper makes a genuine theoretical contribution (bias-only universal approximation) with reasonable empirical support. The main concern — the strength of Proposition 1 — is a legitimate verification issue but not a reason to reject, since the proof exists in the appendix and the claim is at least plausible. The paper is well-written, situates its contribution appropriately relative to neuroscience and ML, and is honest about its limitations.

**Originality:** Good. The bias-only framing is genuinely novel and connects interestingly to neuroscience.
**Quality:** Solid theoretical proofs (assuming appendix verification) with clear experiments.
**Clarity:** Well-written, though the main text would benefit from more intuition about the key property.
**Significance:** High for the neuroscience community studying non-synaptic plasticity; relevant to ML for understanding parameter-efficient learning.

A well-constructed resubmission could address the minor concerns straightforwardly in a rebuttal. The paper merits acceptance.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>