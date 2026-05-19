- Decision: Reject
- Avg Score: 3.50
- Scores: 3, 3, 5, 3
Now I have all the evidence I need. Let me produce the final consolidated review.

---

## Summary

This paper introduces a Hawkes process variant in which impact functions are modeled by a neural network operating in a low-dimensional event embedding space. Two model variants are proposed: ENHP (static embeddings, fully interpretable with additive influence) and ENHP-C (contextualized embeddings via a transformer encoder, more flexible but less interpretable). The central claim is that this design preserves interpretability (inspectable topic-level embeddings and a time-varying kernel) while achieving competitive log-likelihood on real-world event-sequence benchmarks, and that the simpler ENHP variant often suffices — implying the expressiveness–interpretability trade-off is largely unnecessary in practice.

---

## Strengths

1. **Embedding-based impact kernel reduces parameter complexity while enabling interpretability at scale.** Equation (8) replaces the O(M²) full impact matrix with an O(D²) kernel in embedding space (D ≪ M). This formulation scales to event spaces with 5,000 types (MemeTrack, Table 1) while maintaining a structure where each embedding dimension corresponds to a latent topic (Section 3.3). Prior neural HPs either require full pairwise modeling or lose this topic-level interpretation.

2. **ENHP achieves competitive performance without transformer layers, supporting the claim that interpretability need not be sacrificed.** On five real-world datasets, ENHP attains an average rank of 2.0 in log-likelihood, compared to 1.8 for NHP and 4.2 for THP (Table 2, Section 4.4). It is the only model among those compared that preserves additive influence and topic-level kernel interpretability while matching top methods.

3. **Optional transformer layers provide a clean architectural tradeoff between interpretability and flexibility.** The framework explicitly separates the impact kernel (interpretable, additive) from contextualization (Equation 9, Section 3.3). Users can add transformer layers when needed or exclude them without changing the core architecture. This differs from models like AttNHP or SAHP, which inherently couple attention mechanisms with the intensity function.

4. **Simulation study verifies recovery of diverse, non-parametric impact functions.** Using synthetic data with step, cosine, and exponential kernels, ENHP recovers all four active functions with better shape fidelity than tick's step-function approximation (Figure 2, Section 4.3), demonstrating that the neural kernel captures patterns beyond exponential decay.

5. **Interpretability on MIMIC-IV reveals clinically coherent topic-level relationships.** Embedding dimensions map to procedures (intubation/ventilation for Input 1, culture results for Inputs 2–3) and the impact kernel shows that obtaining cultures increases the rate of line placement (Section 4.6, Table 3, Figure 3c). This provides a concrete demonstration of how topic-level interpretability works in practice.

---

## Weaknesses

### Fatal
None.

### Major

None. The issues identified below are addressable in revision and do not invalidate the paper's core contribution.

### Minor

1. **Baseline evaluation protocol is ambiguously described.** The paper states: "With the exception of the MIMIC-IV dataset, results for baseline methods on all datasets are reproduced from previously published work (Mei & Eisner, 2017)(Xue et al., 2023)" (line 147), and later says "we are using an open benchmark EasyTPP … to evaluate the other methods" (line 176). While these can be reconciled (using EasyTPP's implementations to reproduce results consistent with those papers), the phrasing is unclear. A reader could reasonably wonder whether numbers were simply transcribed from prior tables. The paper should state explicitly that all baselines were re-run under the same pipeline.

2. **The "complete interpretability" claim overstates the gap relative to SAHP.** The paper acknowledges that SAHP provides interpretability through attention weights that quantify per-event-type influence (Section 2, lines 34–36), but dismisses it for "not explicitly capturing the temporal dynamics of influence decay." The claim that ENHP is "the only model that offers complete interpretability" (line 197) should be more carefully scoped: ENHP's interpretability is of a *different type* (explicit time-decaying impact functions + topic-level embeddings) rather than categorically superior. SAHP does offer per-event-type influence interpretability, just without the temporal dimension.

3. **Key hyperparameters for ENHP/ENHP-C are not reported.** The paper specifies only that the kernel network "consists of a fully connected layer with ReLU activation, followed by a linear output layer" (line 127). Missing details include: number of hidden units, learning rate, optimizer, number of training epochs, batch size, and early stopping criteria. While baselines use EasyTPP defaults, ENHP's own configuration is absent. This is a reproducibility gap.

4. **The main comparison table (Table 2) reports no variance or significance measures.** Standard deviations are shown for the ENHP vs. ENHP-C comparison (Table 1) but not for the cross-model comparison (Table 2). Several differences between methods are small (e.g., Amazon: −0.817 vs. −0.822). Without error bars, it is unclear whether observed differences are meaningful. The paper's claim that ENHP is "competitive" with NHP (rank 2.0 vs. 1.8) is reasonable but weakened by this omission.

5. **Synthetic recovery experiment is too narrow to fully support the flexibility argument.** The simulation uses a single three-dimensional Hawkes process with four simple impact functions (step, cosine, two exponentials). While the recovery is reasonable, a more thorough evaluation would vary kernel complexity (e.g., multimodal, non-smooth), increase the number of event types with structured interactions, or test conditions with no true excitation. The flexibility claim would benefit from additional stress tests.

6. **Which integration method was used is not stated.** The paper discusses both numerical (trapezoidal) and Monte Carlo integration for computing the log-likelihood integral (lines 90–102) and notes that numerical methods are more efficient, but never states which was actually used in experiments. This matters for reproducibility and for assessing computational cost claims.

7. **SAHP was excluded from the comparison with only a vague explanation.** The paper notes "a configuration issue with SAHP in easyTPP" (line 190) without further detail. Even a brief description of the issue would help readers assess whether the exclusion is reasonable.

### Trivial

- The Amazon dataset description contains a garbled phrase: "shoppers often have extra saving for a regular subscription" (line 205–206).
- Notation shifts from `α, δ` (Equation 1, exponential form) to `φ` (Equation 3) without explicit comment; minor consistency improvement.

---

## Nice-to-Haves

- A plot of log-likelihood vs. embedding dimension D for one or two datasets would quantify the cost of interpretability and help practitioners choose D.
- Runtime or memory comparisons would strengthen the scalability claims, especially since the method targets large event spaces.
- The MIMIC-IV interpretability example is a sanity check (patterns consistent with known clinical practice). Showing a *novel* yet validated discovery would be more impactful.

---

## Removed Points

These points were raised by reviewers but removed as invalid, speculative, or non-substantive:

- *"Softplus constraint on W, K(t), μ_k is not justified"* — The paper explicitly states "To ensure the non-negativity of the intensity" (line 114), which is a complete justification. This is a transparent design choice, not a gap.
- *"No attempt to fix SAHP configuration issue is mentioned"* — Speculative. The authors may have attempted fixes; the text merely reports the outcome. This is a reviewer inference, not a verifiable weakness.
- *"SAHP was listed as a baseline but then excluded"* — The paper acknowledges this transparently (line 190). The exclusion is noted; the criticism adds no actionable information.
- *"Hyperparameters for baselines may not have been tuned"* — The paper states "All hyperparameters for benchmark methods are provided by EasyTPP" (line 176). Using a standard benchmark's defaults is a standard and reasonable practice. This is a generic concern, not a specific flaw in this paper.
- *"General interpretability concerns about D > 3 or neural network K(Δt)"* — The paper acknowledges this directly (line 220: "we have chosen a very small embedding dimension (3) to facilitate interpretation in this simplified example"). The MIMIC-IV interpretability is explicitly framed as a didactic example, not as a claim that all deployments use D=3.
- *"Missing runtime/memory comparisons"* — A nice-to-have, not a weakness. The method scales to M=5000 (Table 1), which demonstrates practicality.
- *Pure style/formatting nitpicks* (typos, line breaks, garbled characters) — Parser artifacts, not author errors.
- *"Missing related work"* — Cannot be verified without external sources.
- *Strength Finder's generic strengths* (e.g., "this paper addressed an important problem") — Removed as non-specific.

---

## Novel Insights

None beyond the paper's own contributions. The two reviews largely converged on the same issues (baseline evaluation clarity, interpretability scoping, missing hyperparameter details) and the same strengths (embedding-based kernel design, competitive performance, clean interpretability–flexibility architecture). No reviewer observation revealed a pattern or limitation that the authors themselves had not at least partially considered.

---

## Suggestions

- **Clarify the baseline evaluation protocol.** State explicitly: "We ran all baseline methods ourselves using the EasyTPP framework with default hyperparameters, and our results are consistent with previously reported values." This resolves the ambiguity about "reproduced from previously published work."
- **Add standard deviations or credible intervals to Table 2.** Even reporting whether LL differences are larger than one standard deviation would strengthen the comparison.
- **Report hyperparameters for ENHP/ENHP-C** (hidden units, learning rate, optimizer, epochs, batch size) in the main text or a clearly referenced appendix.
- **Soften the "complete interpretability" claim** by acknowledging that SAHP offers a different form of interpretability (static influence scores) and positioning ENHP's as complementary (temporal + topic-level).
- **State which integration method was used** (numerical vs. Monte Carlo) in the experimental setup.
- **Expand the synthetic study** with more complex kernels (multimodal, non-smooth) and larger event-type sets to better support the flexibility claim.
- **Provide a brief explanation** of the SAHP configuration issue rather than leaving it as a black-box exclusion.

---
