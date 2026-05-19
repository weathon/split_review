- Decision: Accept
- Avg Score: 6.67
- Scores: 8, 6, 6
Now I have all the information I need. Let me construct the final consolidated review.

---

## Summary

This paper proposes that the Chinchilla scaling law can be extended to sparse pre-training by replacing the total parameter count \(N\) with the *average* number of active parameters \(\bar{N}\) during training, yielding a unified scaling law for both dense and sparse models. The authors also conduct a systematic search over sparse pre-training schedules (dense phase, iterative pruning phase, recovery phase) on 162M models to recommend an optimal allocation (25% dense, 50% pruning, 25% recovery). The central empirical demonstration — Figure 1, showing four sparse/dense model pairs matched on average active parameters achieving nearly identical loss — is compelling.

---

## Strengths

- **Unified scaling law with strong empirical anchor.** Replacing \(N\) with \(\bar{N}\) in the Chinchilla law (Equation 2) and fitting it to 30 data points (5 sparsity levels × 3 model sizes × 2 training durations) yields an average absolute prediction error of 0.016 (Figure 3). This is a concrete, non-trivial finding: the same functional form that governs dense pre-training also governs sparse pre-training, with only the parameter-count variable reinterpreted.

- **Direct controlled experiment (Figure 1).** Four pairs of sparse and dense models matched on average active parameters and total compute achieve near-identical final loss, despite having radically different training dynamics (sparse models start dense and lose parameters). This is the strongest piece of evidence for the central claim and is presented clearly.

- **First systematic sparse pre-training schedule search.** The paper evaluates a grid of compute allocations across the dense/pruning/recovery phases, LR, and batch size at 162M scale, identifying a concrete recommended schedule (25%–50%–25%) that is near-optimal across sparsity levels and two training durations. The failure-mode analysis (Figure 6) provides actionable guidance on what *not* to do.

- **Larger-scale study than prior work.** The largest model uses \(4.5\times10^{20}\) FLOPs, over 5× the compute of the largest in Frantar et al. (2023). This demonstrates the findings hold at a scale more relevant to LLM pre-training.

---

## Weaknesses

### Fatal
None.

### Major

- **No comparison to alternative scaling laws.** The claim that the average-parameter formulation is the *right* way to extend Chinchilla to sparsity is never tested against alternatives. One could fit the same 30 data points with a Frantar et al. (2023)-style law (using final sparsity as an additional term) or a Chinchilla law using *final* (not average) active parameters. Without such baselines, the reader cannot tell whether Equation (2) is genuinely superior or merely different. The paper asserts unification but does not demonstrate it empirically.

- **Schedule optimality validated only at one model scale, then applied universally.** The optimal schedule (25%–50%–25%) is identified by sweeping on 162M models only (Section 6.1: "Focusing on the 162M-10× and 162M-20× models"). This schedule is then used for all model sizes (58M, 162M, 468M) when fitting the scaling law. No evidence is provided that this schedule transfers to other scales. Scaling laws are known to interact with model size; the paper should at minimum test a few alternative schedules at 58M and 468M to verify the finding is robust.

- **The theoretical derivation (Section 5.2) is a plausibility argument, not a derivation.** Several steps weaken the claimed rigor: (a) The claim that loss spikes from pruning "do not affect the final loss" is stated without empirical evidence or analysis; (b) the constancy of \(C_{0:k-1}^{-\alpha-1}\) is shown for only one model (410M) and one value of \(\alpha\); (c) the derivation models the *change* in loss but never integrates back to recover the specific functional form \(A/\bar{N}^\alpha + B/D^\beta + E\), so the link between the derivation and Equation (2) remains informal. The paper acknowledges this section as a "justification" rather than a proof, but the stated contribution ("We present a theoretical analysis… that justifies using the average number of active parameters") overstates the strength of the argument.

### Minor

- **Fitted scaling-law parameters not reported.** The values of \(A, B, E, \alpha, \beta\) — five free parameters central to the paper's main contribution — are never listed. This impedes reproducibility and makes it impossible for others to compare or build on the scaling law, even approximately.

- **No uncertainty quantification on the fit.** 30 data points for 5 parameters is a reasonable but not generous ratio. The paper does not report confidence intervals, bootstrap estimates, or any measure of uncertainty on either the parameter values or the predicted losses. Overfitting is a plausible concern, especially given the maximum error of 0.03 at 60% sparsity.

- **"Lossless compression" claim overreaches.** The paper claims "2× lossless compression" based on perplexity alone. The limitations section acknowledges that "perplexity does not always correlate with model utility," yet the main text still uses the term "lossless," which implies zero quality degradation across all measures. This should be qualified.

- **Derivation assumes a single \(\alpha\), but Figure 2 shows two regimes.** The paper notes that a linear fit before and after a transition point yields \(\alpha \approx 0.203\) and \(\alpha \approx 0.041\), respectively, but the derivation proceeds with a single \(\alpha\). This inconsistency is noted but not addressed.

### Trivial
None.

---

## Nice-to-Haves

- Downstream task evaluations (e.g., BoolQ, PIQA, ARC-Easy) on a subset of models would substantially strengthen the practical relevance and justify the "lossless" language.
- Testing the optimal schedule at one additional scale (58M or 468M) would resolve the transferability concern with relatively low cost.
- A comparison to post-training pruning baselines (SparseGPT, Wanda) on the same architectures would contextualize the compression claims.
- Reporting variance across multiple seeds for key configurations would clarify the noise level in the measurements.

---

## Removed Points

*These points were flagged by the original reviewers but are removed from the main review for the reasons stated.*

- **"80 configurations claim is unclear":** The harsh critic questioned where the "80" figure comes from. The paper says "over 80 combinations of sparse pre-training schedules, sparsity levels, and training durations." Given the grid (schedule combinations × sparsity levels × training durations), 80 is a plausible total. This is a minor counting ambiguity in a non-archival abstract, not a substantive weakness.
- **"Effective compute undercuts practical relevance":** The paper openly acknowledges this limitation in its final section. A paper can contribute a theoretical finding about scaling laws even if hardware support for unstructured sparsity is not yet mature. This is a scope limitation, not a flaw.
- **"No comparison to post-training pruning baselines":** The paper's contribution is a scaling law and schedule search for *pre-training* sparsity, not a method for post-training pruning. Comparing to SparseGPT/Wanda would be comparing apples to oranges.
- **Strength-finder claims that conflict with verified weaknesses:** The strength about "theoretical justification grounded in empirical observations" partially conflicts with the verified weakness about the derivation being informal. Since it has a concrete anchor (Section 5.2, Figure 2), it is retained in the Strengths section with appropriate context from the Weaknesses.
- **Generic strength-finder claims removed:** The strength finder's framing of "optimal dense hyperparameters transfer" as a standalone strength is generic (many pruning papers find this). It is subsumed under the broader schedule-search strength.

---

## Novel Insights

The most interesting observation from the reviews — one not fully articulated in the paper itself — is that the paper's two main contributions (the scaling law and the schedule search) are somewhat in tension. The scaling law claims that only the *average* active parameter count matters, regardless of *when* pruning happens. Yet the schedule search finds that *when* pruning happens (the allocation across phases) strongly affects final loss, even holding average active parameters constant. This suggests the average-parameter law may be an empirical approximation that holds near the optimal schedule but would break down for pathological schedules (e.g., pruning everything in the first 1% of training). The paper would be stronger if it explicitly acknowledged and tested this boundary condition.

---

## Suggestions

1. **Compare to alternative scaling laws**: Fit a Frantar et al. (2023)-style law and a law using final (not average) active parameters to the same 30 data points. Report which fits best and quantify the improvement.
2. **Validate schedule transferability**: Run at least 2–3 alternative schedule allocations at one additional model scale (58M or 468M) and report whether the 25–50–25 recommendation remains optimal.
3. **Report fitted parameters and uncertainty**: List the values of \(A, B, E, \alpha, \beta\) from the fit, and provide bootstrap confidence intervals on the predicted losses.
4. **Qualify "lossless"**: Replace "lossless compression" with language like "no degradation in perplexity under the same compute budget."
5. **Address the transition-point inconsistency**: Either incorporate the two-regime \(\alpha\) observation into the derivation, or acknowledge it explicitly as a limitation of the single-\(\alpha\) assumption.

---
