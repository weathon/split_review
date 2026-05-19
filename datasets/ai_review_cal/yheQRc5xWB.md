- Decision: Accept
- Avg Score: 5.80
- Scores: 5, 6, 6, 6, 6
Now I have a thorough understanding of the paper and can verify the reviewer claims. Let me compose the final consolidated review.

---

## Summary

This paper proposes Mamba-CDSP, the first state-space model (Mamba-based) approach for time-varying counterfactual prediction (TCP). The key ideas are: (1) using Mamba as the backbone for its linear-time complexity in long sequences, replacing the quadratic-cost Transformer used in prior work; (2) introducing a Covariate-based Decorrelation towards Selective Parameters (CDSP) regularizer that penalizes cross-covariance between the Mamba hidden state and current treatment, intended to reduce sequential confounding bias without the "over-balancing" problem of adversarial methods. The paper offers architectural modifications to Mamba (replacing 1-d convolution with dropout) and theoretical risk bounds comparing CDSP to adversarial balancing.

## Strengths

1. **First Mamba-based model for TCP** — The paper explicitly identifies that prior TCP methods (CRN, RMSN, Causal Transformer) rely on architectures with quadratic or limited-context issues for long sequences, and proposes Mamba as a backbone with linear-time scaling. This is a timely and well-motivated architectural choice. (Lines 14, 22)

2. **Identifies and targets the over-balancing problem** — The paper correctly observes that adversarial domain-confusion balancing (used in CRN, Causal Transformer) can corrupt covariate information when pushed too hard, and proposes decorrelation as an alternative mechanism that preserves more covariate information while still reducing confounding bias. This is a valid conceptual contribution. (Lines 14, 99-100)

3. **Efficiency motivation is well-grounded** — Figure 1(b) contrasts Mamba's empirical runtime (~linear in sequence length) against Causal Transformer's (~quadratic), and the complexity analysis of CDSP vs. adversarial modules (Section 4.3) is clearly articulated. The efficiency advantage of the backbone is real and important for long-sequence TCP.

4. **Architectural adaptation with dropout** — Replacing the 1-d convolution with dropout to mitigate overfitting on temporal data is a sensible, targeted modification motivated by empirical observation. (Line 95)

## Weaknesses

### Fatal
None — the paper's core contribution (Mamba for TCP, decorrelation as an alternative to adversarial balancing) is not rendered entirely invalid by any single issue. However, the weaknesses below are substantial.

### Major

1. **Unjustified step in the core derivation of CDSP (Equation 3)** — The derivation of the CDSP regularizer contains a mathematical error. Equation 3 (line 104-105) writes:
   
   `Cov(h_{t-1}, a_t) = Cov(∑ K_i \tilde{X}_i^h, a_t) = ∑ Cov(K_i \tilde{X}_i^h, a_i) = ∑ K_i Cov(\tilde{X}_i^h, a_i)`
   
   The second equality replaces `a_t` with `a_i` without justification. In general, `Cov(K_i \tilde{X}_i^h, a_t) ≠ Cov(K_i \tilde{X}_i^h, a_i)` — the covariance between a past representation and the *current* treatment is not the same as the covariance between that same representation and the treatment at that past time step. The paper asserts this follows from "the property of cross-covariance," which it does not. This substitution propagates into the entire CDSP regularizer (Equations 4-5, Proposition 1). Unless the authors can justify why this equality holds under the assumed causal structure (e.g., through sequential ignorability combined with an additional Markov-type condition not stated in the paper), the derivation of the regularization is unsupported. This is the most serious issue because the claimed equivalence "decorrelation ↔ regularizing selective parameters" depends on it.

2. **Theoretical analysis does not reflect the CDSP mechanism** — Theorem 1's finite-sample risk bounds are expressed in terms of `‖μ₁-μ₂‖²` (the squared Euclidean distance between treatment-arm covariate means). This is a *distribution balancing* measure. The CDSP method is motivated by *decorrelation* (removing cross-covariance between hidden state and treatment). No argument is given that minimizing cross-covariance implies minimizing `‖μ₁-μ₂‖²` or vice versa. The bounds therefore analyze a quantity that the CDSP regularizer does not directly optimize, making the theoretical support feel disconnected from the actual method. Additionally, the constants `r₁, r₂, r₃` and the term `v` appearing in the bounds are undefined in the extracted text, making the bounds non-quantitative.

3. **No guidance on how the experimental evaluation supports the claims** — The extracted text ends after Section 4.4 and jumps to Section 6 (Conclusion). Section 5 (Experiments) is absent. The only experimental results visible are in Figure 1 (Introduction), which compares Mamba-CDSP to only one baseline (Causal Transformer) on one dataset (Tumor simulator). The paper claims in the abstract to have conducted "extensive experiments on both synthetic and real-world datasets" and to "outperform baselines by a large margin," but the evidence supporting these claims cannot be assessed from the available text. While this is plausibly a PDF parsing artifact, it means the central empirical contribution of the paper is unavailable for review.

### Minor

4. **Optimization of ℒ_CSDP needs clarification** — The regularization term ℒ_CSDP penalizes `\overline{B}_i` and `\overline{C}_j` (the selective parameters), which are *functions of the input* at each time step. The paper states that the covariance matrix term "can be pre-computed for each batch of samples" (line 123). If this means the covariance estimate is detached from the gradient graph, the regularization only affects the `\overline{B}_i` and `\overline{C}_j` directly and not the representations `\tilde{X}_i^h` that feed into the covariance. The paper does not discuss whether gradients flow through the covariance estimation, which is important for understanding how exactly the regularization steers representations toward decorrelation. This is not a fatal issue — standard practice is to compute batch statistics with stop-gradient — but it should be explicitly addressed.

5. **Proposition 1 is stated without proof or sufficient justification** — Proposition 1 (line 115) claims that minimizing `‖K_i Σ‖²` is equivalent to `K_i Σ Σ^T = 0`. This needs more justification: `‖K_i Σ‖² = 0` implies `K_i Σ Σ^T = 0` is straightforward, but the claim that minimizing this norm leads to that condition being the solution merits proof, especially since `K_i` is itself a product of multiple learnable matrices `\overline{B}_i Π \overline{C}_j`. The argument as presented is incomplete.

### Trivial
- There is a minor notation inconsistency: Equation 1 uses `T(a)` for the output but the surrounding text uses `y_t` for the output. (Line 75 vs. line 81)
- Section numbering starts with 4.4 "THEORETICAL ANALYSIS" but the section begins with "3)" (line 137), suggesting a missing or misnumbered subsection.

## Nice-to-Haves
- An ablation that replaces CDSP with standard adversarial balancing on the same Mamba backbone would isolate the benefit of the decorrelation mechanism vs. the backbone change.
- A diagnostic experiment showing that CDSP actually reduces the cross-covariance `Cov(h_{t-1}, a_t)` would directly validate the mechanism.
- The regularization hyperparameter α selection procedure (cross-validation? grid search?) should be described, as the tradeoff between MSE and decorrelation is central to the method.
- The paper could benefit from comparing against non-Transformer baselines on identical Mamba variants to isolate the effect of CDSP from the backbone advantage.

## Removed Points

**Harsh critic's "fatal" classification of missing experiments:** Removed. The instructions specify that parser-stripped content (appendices, proofs, references) should not be penalized. Section 5 (Experiments) is a main section whose absence from the extracted text is likely a parsing artifact. However, since the empirical claims cannot be verified from available material, I have downgraded this to a Major weakness (point #3 above) rather than removing it entirely — the evaluability of claims is genuinely compromised regardless of cause.

**Harsh critic's claim that σ₀, σ₁ are undefined in the bounds:** Removed. Line 137 specifies `X_{|a} ∼ N(μ_a, σ_a I)`, so σ₀ and σ₁ are defined as the per-treatment-arm covariate variances. The critic's assertion that "it is impossible to tell whether CDSP is ever better" is incorrect — given (2+σ₀+σ₁)/4 > 1/2 when σ₀+σ₁ > 0 (always true for positive variances), the CDSP coefficient is strictly tighter. This particular criticism is factually wrong.

**Harsh critic's point about the efficiency being "not a novel contribution":** Removed. The paper's contribution is not "inventing linear-time SSMs" but *adapting them to TCP* and showing the efficiency carries over. Identifying that Mamba can replace Transformers for this task is itself a contribution, even if the backbone's properties are known. This criticism is scope-creep.

**Strength Finder's claim that "Figure 1(a) provides concrete evidence" for effectiveness:** Weakened. The figure compares Mamba-CDSP to only Causal Transformer on one dataset. This is too limited to count as a major strength, though it does suggest promising preliminary results. Moving to a context note rather than retained strength.

**Strength Finder's claim that "Theorem 1 provides formal justification" for CDSP:** Removed (conflicts with verified weakness #2). The bounds do not analyze decorrelation, so they do not formally justify CDSP. The weakness wins per the rules.

## Novel Insights

The reviews surface an interesting tension: the paper's core insight — that decorrelation can substitute for adversarial balancing to avoid over-balancing — is conceptually appealing and well-motivated by the TCP literature. But the mathematical execution of this insight contains a verifiable error (the a_t → a_i substitution) that calls into question whether the CDSP regularizer actually implements the intended decorrelation. A second interesting observation from cross-referencing the strengths and weaknesses is that the efficiency advantage is clearly genuine and well-documented (Mamba vs. Transformer), but it is almost entirely attributable to the backbone choice rather than the CDSP mechanism; the paper would benefit from isolating the contribution of CDSP from the backbone through controlled ablations. The theoretical bounds comparing CDSP to adversarial balancing are actually correct in form (the CDSP coefficient is tighter whenever σ₀+σ₁ > 0), but they address a different quantity (distribution balancing) than CDSP optimizes (decorrelation), suggesting the paper has two partially disconnected narratives.

## Suggestions

1. **Fix the derivation in Equation 3.** Either justify the substitution `a_t → a_i` under the assumed sequential ignorability (plus any additional conditions needed), or derive the CDSP regularizer from a correct covariance decomposition. This is the single most important fix.

2. **Clarify the gradient flow for ℒ_CSDP.** State explicitly whether Σ is detached or back-propagated through, and show a concrete loss computation for a batch of sequences.

3. **Reconnect the theoretical analysis to CDSP.** Either derive bounds in terms of the cross-covariance that CDSP actually penalizes, or provide an argument linking `‖μ₁−μ₂‖²` to the decorrelation objective under the assumed Gaussian-linear setup.

4. **Provide the experiments section.** The evaluation should include: (a) RMSE across varying prediction horizons τ; (b) comparisons to CRN, RMSN, G-Net, Causal Transformer, and a vanilla Mamba (no CDSP); (c) an ablation with adversarial balancing on the same Mamba backbone; (d) runtime scaling; (e) a diagnostic that CDSP reduces cross-covariance.

5. **Define r₁, r₂, r₃ and v** in the theorem statement, or cite where they are defined.
