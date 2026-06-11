Now I have sufficient calibration data. Let me write the final review.

## Summary

This paper establishes a formal first-order duality between activation steering and influence functions for neural networks. It proves that any steering vector can be represented as an ℓ₁-minimal signed influence measure over training data (and vice versa, Theorem 4.2), introduces a geometric diagnostic γ that quantifies when steering can substitute for influence (Theorems 5.1, 6.2), derives spectral optimality for direction selection (Theorem 5.3), and provides Rademacher complexity bounds for low-rank steering (Theorem 6.1). Experiments on GPT-2 Medium (detoxification) and ResNet-50 (ImageNet) partially validate aspects of the theory.

## Strengths

1. **Closed-form duality between steering and influence (Theorem 4.2).** The paper proves a direct mathematical equivalence that bridges two previously disconnected strands of interpretability research: any steering vector can be represented as an ℓ₁-minimal signed measure over training influence vectors and vice versa. This is a genuinely novel theoretical insight, cleanly derived through a primal-dual formulation, and goes well beyond the conceptual analogies drawn in prior work.

2. **Geometric feasibility diagnostic γ with tight bounds (Theorem 5.1, Theorem 6.2).** The paper characterizes when activation steering can substitute for influence functions via the smallest principal-angle cosine γ between two Jacobian subspaces, with a tight √(1−γ²) bound on relative logit error and a no-free-lunch lower bound when γ is small. Figure 2 validates that γ increases with layer depth on GPT-2 Medium (from 0.64 to 0.94), supporting practical use. This diagnostic is novel and potentially useful for practitioners.

3. **Empirical validation of first-order linearity at scale (Section 7.2, Figure 1).** Over 5000 prompt-token pairs on GPT-2 Medium, predicted vs. actual logit shifts achieve cosine 0.978, confirming that the first-order approximation underlying the framework holds in a realistic setting with a billion-parameter-scale model.

## Weaknesses

### Major

- **Steering-to-data mapping claimed but never demonstrated.** The paper's fourth listed contribution (Section 1) promises that practitioners can "identify the responsible training examples" given a steering vector, and the abstract claims "a constructive algorithm for mapping undesired behaviors back to causal training examples." Corollary 1 provides the theory, and Section 4.1 states "see Section 7" — but Section 7 contains no experiment showing this mapping in action. There is no case study tracing a steering vector to specific training documents, no inspection of top-weighted examples from ρₛ, and no validation that the identified examples are causally relevant. This is the paper's most distinctive practical payoff, and it is entirely unvalidated. The gap between the paper's framing and its evidence on this point is substantial.

- **Detoxification experiment (Table 1) shows IAS underperforming CAA on both metrics with no compensatory evidence.** IAS achieves 0.0164 toxicity vs. CAA's 0.0150, and 13701 PPL vs. CAA's 13291 — worse on both. The paper highlights CAA's numbers in bold but does not articulate a compensating advantage for IAS. If the argument is that IAS's value lies in traceability, that experiment was not done. The reader is left with a method that appears strictly dominated on the only performance comparison presented.

### Minor

- **Slope of 1.50 in Figure 1 left unaddressed.** The first-order equivalence experiment reports cosine 0.978 (confirming collinearity) but slope 1.50, meaning the actual logit shift magnitude is systematically 50% larger than predicted — not 1.0 as exact first-order equivalence would give. The paper calls this "consistent with the expected linear regime" without discussing why the magnitude deviates, whether this reflects a calibration issue, or whether the steering magnitude is outside the first-order regime. This discrepancy undercuts confidence in the theory's quantitative predictions.

- **Spectral optimality experiment (Section 7.4) provides only weak validation of Theorem 5.3.** The experiment shows the spectral direction's radius exceeds a null distribution of random directions (p≈0.005). This is the weakest possible standard; a proper test would compare actual downstream steering performance (e.g., class logit increase) of the spectral direction against multiple candidate directions (CAA, gradient-based, etc.). Showing it beats random does not substantiate optimality.

- **Influence function computation underspecified.** The paper uses influence functions for GPT-2 Medium (350M parameters) but does not describe the iHVP approximation method (conjugate gradient? LISSA? EK-FAC?), convergence criteria, or computational budget. Given that influence functions are known to be fragile for large models (Basu et al., 2021, cited), this missing detail is notable.

- **Cost model claim conflates different operations.** The paper states "requiring only two backward passes per input" (Contribution 4). This is accurate for computing a single IAS vector from a given Δθ, but constructing ρₛ over the training set additionally requires computing influence scores I(z→x) for each training example — a much more expensive operation involving per-example iHVPs.

- **Generalization bound (Theorem 6.1) applicability could be clarified.** The bound treats IAS as a rank-k correction added as a residual to the output (f_θ + αUVᵀ), but IAS operates by adding a vector to a hidden layer's activations. The mapping from the activation perturbation Δh* to a "rank-k submatrix of the layer weight" is not derived in the main text.

### Trivial

- No sensitivity analysis for key hyperparameters (choice of layer ℓ=8, damping λ, rank k).
- The recommended γ < 0.5 threshold for skipping steering is not empirically validated.

## Nice-to-Haves

- A small-scale case study demonstrating the steering→data tracing, even on a manageable training subset, would close the most glaring gap.
- Comparison against additional steering baselines (representation engineering, gradient-based steering).
- Investigation and discussion of the slope=1.50 discrepancy in Figure 1.

## Removed Points

- Criticism that the feasibility assumption Im(J_θ→y) ⊆ Im(J_h→y) is strong: the paper explicitly bounds the error when this fails via Theorems 5.1 and 6.2, which address this concern directly.
- Speculation about influence function fragility as a fatal flaw: the paper cites the relevant concern (Basu et al.) but any actual failure would need to be demonstrated on this paper's specific setup, not merely asserted.
- Pure formatting/style nitpicks, missing appendix content, and reproducibility criticisms about undisclosed trivial hyperparameters — these reflect parser artifacts or standard practice rather than substantive issues.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface observations about the paper that go beyond what the paper itself states.

## Suggestions

1. **Demonstrate the steering→data mapping.** Even a single worked example — construct a steering vector for a specific behavior, compute ρₛ over a manageable training subset, and show qualitatively or quantitatively that top-weighted examples are causally relevant — would close the biggest gap between claims and evidence.

2. **Address the slope=1.50 discrepancy.** Investigate whether this is a calibration artifact, a sign that the steering magnitude is outside the first-order regime, or a structural mismatch. Explicitly state what it implies for the theory.

3. **Strengthen the spectral optimality experiment** by comparing the spectral direction against other candidate steering directions on downstream performance, not just against random directions.

4. **Specify the iHVP approximation method** used and its convergence criteria.

5. **Reframe the detoxification comparison** to clarify whether IAS is intended to match CAA on raw performance while offering traceability — and then demonstrate that traceability.

---

**Calibration Report:**

**Round 1 (Bracketing):** Searched three bands on steering/influence/duality topics. Low band (<3.5) returned papers scoring 3.0–3.4 — clearly weaker. Middle band (3.5–7.5) returned papers ranging 3.67–7.0, including topically closest papers at 5.0. High band (>7.5) returned papers at 8.0 — clearly stronger. **Initial bracket: 4.5–6.5.**

**Round 2 (Narrowing):** Searched within (4.5–6.5) and (5.0–7.0) on steering and influence topics. Key anchors:
- *"From Steering Vectors to Conceptors and Beyond"* (5.00, Reject) — most topically similar; weaker theory, but at least had experiments showing improvement over baselines. The paper under review has stronger theory but a more severe experimental gap. **Slightly better → supports 5.5.**
- *"Effectively Steer LLM To Follow Preference"* (5.50, Reject) — steering theory + experiments; comparable weakness profile. **Comparable → supports 5.5.**
- *"Steering Language Models with Activation Engineering"* (5.00, Reject) — influential steering paper with split reviews; less theoretical novelty. **Notably above this → supports 5.5.**
- *"Enhancing Training Robustness through Influence Measure"* (6.20, Accept) — influence functions application with cleaner experiments; less novel theory. **Slightly below this → supports 5.0–5.5.**
- *"What Data Benefits My Classifier?"* (6.40, Accept) — thorough empirical validation; less theoretical novelty. **Notably below this → supports ≤5.5.**

The paper sits between the 5.0–5.5 steering papers (stronger theory, weaker experiments) and the 6.2–6.4 influence papers (weaker theory, stronger experiments). The theoretical contribution is genuinely novel and well-presented, but the headline practical claim (tracing steering to training data) is completely unvalidated, and the core detoxification comparison shows the proposed method underperforming the baseline. A score of **5.5** reflects "borderline with notable strengths but insufficient experimental support for the advertised claims."

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>