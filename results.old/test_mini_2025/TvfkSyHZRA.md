Now I have sufficient calibration data. Let me write the final review.

---

## Summary

This paper argues that grokking's delayed generalization and dependence on regularization arise from two linked issues: (1) **Naïve Loss Minimization (NLM)** — after overfitting, gradients align with the weight direction, scaling logits without changing predictions; and (2) **Softmax Collapse (SC)** — this logit scaling eventually triggers floating-point absorption errors in the Softmax, zeroing out gradients and stopping learning. The paper introduces StableMax, a numerically stable softmax replacement that enables grokking without regularization, and ⊥Grad, an optimizer that removes the NLM gradient component and eliminates the delay in generalization. The work also provides a unified explanation for why existing methods (weight decay, MSE loss) induce grokking.

---

## Strengths

1. **Identification of Softmax Collapse as a concrete, measurable numerical barrier to grokking.** The paper formally defines SC (Definition 3) and provides clear evidence — across dataset sizes and floating-point precisions — that SC onset coincides with test accuracy plateaus, and that increasing precision (float32 → float64) pushes SC later and improves test performance (Figure 2). This is a specific, testable mechanism not isolated before.

2. **StableMax enables grokking without any regularization on standard benchmarks.** On addition mod 113, product mod 113, and sparse parity with 40% training data, replacing Softmax with StableMax drives test accuracy to 100% with zero weight decay (Figure 4, left). The accompanying weight-norm plots (Figure 4, middle) show that generalization occurs while weight norms grow, decoupling grokking from weight-norm reduction and contradicting the "Goldilocks zone" narrative.

3. **⊥Grad eliminates the delay in generalization entirely.** On transformer subtraction mod 113 and MLP addition mod 113, ⊥AdamW and ⊥SGD reach 100% test accuracy in hundreds of epochs whereas standard optimizers fail to generalize (Figure 6a,b). The trajectory analysis (Figure 7) shows ⊥SGD moves directly toward low test loss, unlike SGD which first increases test loss — directly demonstrating that removing the NLM component eliminates the overfitting phase.

4. **Unified explanation for why existing grokking methods work.** Section 5.2 coherently explains weight decay (counteracting NLM through L2 regularization), MSE loss (logits cannot overshoot targets, so NLM does not decrease loss), and dataset-size effects within the same NLM/SC framework. This ties together disparate prior observations under a single mechanism.

5. **Input representation experiments confirm that modular arithmetic is not intrinsically special.** Section 4.1 shows that replacing one-hot inputs with low-dimensional binary representations turns modular addition into a standard task with simultaneous train/test improvement (Figure 4, right), verifying that the delay is caused by ease of memorization rather than any property of the arithmetic operation itself.

---

## Weaknesses

### Fatal
None.

### Major

1. **The causal role of Softmax Collapse is not fully isolated from the functional change of StableMax.** StableMax replaces the exponential with a piecewise linear/reciprocal function, which changes the loss landscape in ways beyond numerical stability (e.g., different gradient magnitudes for large positive logits, different implicit bias). The paper's higher-precision (float64) experiments serve as a partial control — they use the original Softmax with reduced absorption errors — but float64 only delays SC, it does not produce full generalization (Figure 2c, even at 70% data). Without a control experiment that uses the *original* Softmax with a purely numerical intervention (e.g., arbitrary-precision arithmetic for just the Softmax sum, or pruning exp terms below machine epsilon), we cannot definitively distinguish whether StableMax succeeds because it avoids SC or because its different functional form alters optimization dynamics. This is the single most important gap in the central causal claim. The correlation evidence (SC fraction in Figure 2) is suggestive but does not establish causation.

### Minor

2. **Evaluation domain is narrow.** All experiments are on small-scale algorithmic tasks (modular arithmetic, sparse parity) and a 200-sample MNIST subset. The paper cites Lv et al. (2024) and Humayun et al. (2024) to argue that grokking is more pervasive, but never demonstrates that SC, StableMax, or ⊥Grad matter for any larger-scale model or task. This does not invalidate the controlled-setting contribution, but it bounds how broadly the conclusions can be drawn, particularly since the paper proposes new training components.

3. **NLM → weight decay explanation is partly correlational.** The trajectory plots (Figure 7) show SGD+WD initially follows the NLM direction before turning, and the trade-off analysis (Figure 6c) is a plausible mechanistic story. However, there is no causal intervention (e.g., explicitly penalizing only the NLM component of the gradient) that isolates *why* weight decay works. ⊥Grad itself is such an intervention for the optimizer, but the paper does not use it to deconstruct weight decay's effect.

4. **No error bars or multiple-seed results.** For a paper making claims about training dynamics (Figure 2, Figure 4, Figure 6), the absence of variance information is a notable omission, even for deterministic full-batch settings where initialization can still matter.

5. **Missing comparison to related projection-based methods.** ⊥Grad projects the gradient orthogonal to the weight direction. The paper briefly cites Heo et al. (2021), Wang et al. (2024), and Kosson et al. (2024), but does not compare to weight normalization (Salimans & Kingma, 2016) or LARS, which also control the radial component of updates. Such comparison would help contextualize the novelty.

### Trivial

6. **Figure 7 caption contains a typo:** "LSGD + StatMolux" should read "⊥SGD + StableMax."

7. **The paper could state the SC detection criterion more explicitly.** While Eq. (2) is precise under FP arithmetic (checking if Σ e^{z_k} ≐ e^{z_y}), stating the implementation-level check (e.g., checking if the max logit exceeds the next-largest by more than ~2^23 in float32) would aid reproducibility.

8. **Minor presentational gap:** Section 3.3 states StCE leads to grokking on "all common grokking tasks on both MLPs and transformers," but the main-text figures show StCE results only on MLPs. (The appendix may contain transformer results; referencing them in the main text would improve clarity.)

---

## Nice-to-Haves

- A control experiment using the original Softmax with high-precision arithmetic (e.g., Python's `decimal` module for the sum) to isolate whether numerical stability alone — not changed functional form — is what enables grokking. This would directly strengthen the central causal claim.
- Extending experiments to a larger-scale or more realistic setting (e.g., a small language model on a reasoning task, or a vision model with more data) to test whether SC and NLM matter beyond the controlled grokking regime.
- Reporting results across 3–5 random seeds for key figures (Figure 2, 4, 6).

---

## Removed Points

- **"SC detection threshold not specified"** — Removed because the paper clearly defines SC via Eq. (2) (Σ e^{z_k} ≐ e^{z_y} under FP arithmetic), which is a precise, deterministic condition given the FP format. No additional threshold is needed.
- **"StableMax probabilities should be compared to Softmax probabilities"** — Removed because Proposition 1 proves StableMax is a composition of Softmax with a logit transformation; the comparison in Figure 3 (s(x) vs. e^x) is the informative one for numerical stability analysis.
- **"Missing related works"** — Removed per instructions (cannot verify external literature completeness).
- **Weaknesses that are generic area-of-concern speculation** (e.g., "could the metric be measuring a proxy," "are confounders controlled") — Removed as they lack concrete anchors in the paper.
- **Strength Finder items that conflate "interesting problem" with demonstrated contribution** — Removed generic strengths (e.g., "addresses an important problem," "well-written") and kept only strengths grounded in specific evidence from the paper.

---

## Novel Insights

The harsh critic's observation that SC's causal role is confounded with StableMax's functional change, combined with the fact that the float64 experiment only delays but does not prevent SC collapse, suggests a potentially stronger interpretation: perhaps even "pure" numerical stability (without changing the exponential) would not be sufficient for full grokking, and StableMax's linear growth for positive logits actively *prevents* the logit explosion that makes NLM harmful in the first place. If this were true, the paper's frame would shift from "numerical errors halt learning" to "the exponential function's instability window is too narrow, and any saturating/linear activation that keeps gradients alive would work." The reviewers did not develop this angle, but it emerges from the tension between the SC claim and the incomplete float64 control.

---

## Suggestions

1. **Isolate the numerical effect of SC.** Repeat the main StCE experiments using the original Softmax but with a numerically stabilized sum (e.g., `math.fsum` or a log-sum-exp that prunes negligible terms). If this also produces grokking, the causal role of SC is directly confirmed. If it does not, then StableMax's success derives from other properties (e.g., bounded gradient growth for large logits), and the paper's central causal claim needs refinement.

2. **Add error bars or multiple-seed trajectories** for at least Figures 2, 4, and 6 to quantify variability.

3. **Include a comparison to weight-normalized or LARS-style optimizers** in the ⊥Grad experiments to contextualize the novelty.

4. **If appendix contains transformer/StCE or MNIST/StCE results, reference them explicitly in the main text** (e.g., "see Appendix X") to substantiate the claim about "all common grokking tasks on both MLPs and transformers."

---

## Score and Decision

### Calibration Report

**Round 1 (Bracketing):**
| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| "Reconstruct the Understanding of Grokking through Dynamical Systems" (a8XwgTZzE0.md) | 2.0 | R1 | Much weaker — unclear writing, weak results, no concrete contributions. |
| "Grokking at the Edge of Linear Separability" (l1raPjOUPA.md) | 6.0 | R1 | Weaker — oversimplified setting (linear logistic regression), criticized for trivial extensions of prior work. |
| "Numerical Pitfalls in Policy Gradient Updates" (u4dORXVAnx.md) | 5.6 | R1 | Weaker — identified an issue but proposed methods hurt performance; less central phenomenon. |
| "Small-scale proxies for large-scale Transformer training instabilities" (d8w0pmvXbZ.md) | 8.0 | R1 | Stronger — extremely thorough experimental study with clear practical insights; accepted oral. |

**Round 1 bracket:** 6.0–7.5.

**Round 2 (Narrowing):**
| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| "Grokking as the transition from lazy to rich training dynamics" (vt5mnLVIVo.md) | 6.0 | R2 | Comparable but different contribution type; reviewers found limited experimental/theoretical depth. Current paper has more concrete methods (StableMax, ⊥Grad). |
| "Grokking in Linear Estimators" (GH2LYb9XV0.md) | 5.5 | R2 | Weaker — linear models with very simplified setting; criticized for not matching original grokking phenomenon. |
| "Approaching Deep Learning through Spectral Dynamics" (PJjHILiQHC.md) | 6.25 | R2 | Weaker — broad empirical approach, less focused contribution. |
| "Generalized Neural Collapse for a Large Number of Classes" (TmcH09s6pT.md) | 7.0 | R2 | Stronger theoretical results; rejected despite high scores due to framing issues. |

**Final score:** The paper makes genuine contributions (SC identification, StableMax, ⊥Grad) with clear empirical support on standard grokking tasks. It is stronger than typical grokking-explanation papers (5.5–6.0) because it proposes novel, working methods and a unified framework, not just a correlational story. However, it falls below top-tier papers (8.0+) due to the unresolved causal isolation of SC from StableMax's functional change, narrow evaluation scope, and missing statistical rigor. The paper sits between the 6.0 and 7.5 anchors, closer to the upper-middle of that range given its concrete contributions and clear writing. Score: **6.5**.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>