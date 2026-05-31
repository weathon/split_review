Now let me run calibration searches to anchor the score.Round 1 bracket: **6.0 to 7.5**. The τJp paper (direct predecessor, avg 6.0) and attention-only FT paper (avg 6.25) are the closest topical anchors. TAK solves the exact data-dependency limitation that reviewers criticized in τJp, achieves better empirical results, and adds a principled GGN derivation. Now narrowing within the bracket.Now I have enough to write the final consolidated review. Based on Round 2 anchors, my bracket narrows to **6.5–7.5**: TAK is clearly stronger than the τJp paper (avg 6.0) it builds on (solving its data-dependency limitation, outperforming it empirically), comparable in depth to the MAP/AdaFisher papers (6.25–6.33), and below the deeper second-order optimization papers (7.33).

---

## Summary

TAK (Task Arithmetic with KFAC regularization) addresses cross-task interference in task arithmetic by framing weight disentanglement as a curvature matrix approximation problem. The paper derives, under linearized fine-tuning, that the representation drift regularizer reduces to a quadratic form in the Jacobian Gram matrix, which is identified as the GGN under squared loss, enabling adoption of KFAC. A novel Kronecker accumulation scheme collapses per-task curvature factors into a single O(1) surrogate. The method is dataless, achieves state-of-the-art results in task addition and negation across vision (3 ViT scales) and language (T5-base) benchmarks, and eliminates the need for coefficient tuning.

---

## Strengths

- **Clean theoretical derivation from representation drift to GGN (Sec. 3.1–3.2):** Under linearization, the drift penalty $\mathcal{L}^{\text{drift}}_{t \to t,t'}(\tau_{t'}) = \alpha_{t'}^2 \tau_{t'}^\top G_t(\theta_0) \tau_{t'}$ (Eq. 3) reduces to a quadratic form in the Jacobian Gram matrix. The paper then identifies this as the GGN under squared loss (Sec. 3.2), connecting the task arithmetic objective to the well-established KFAC literature in a principled and non-trivial way.

- **O(1) accumulation with empirically validated fidelity (Table 3):** The Kronecker merge heuristic (Eq. 8) is directly compared to the exact O(T) formulation on three architectures. The gap is negligible for ViT-B/16 and T5-base (≤0.1 points absolute), with only a small consistent gap on the smaller ViT-B/32 (86.0 vs. 86.6 best α). This confirms the practical scheme as a faithful approximation.

- **Dataless method matches or exceeds the data-dependent τJp baseline (Tables 1–2):** TAK achieves 85.8/88.3/91.6 absolute accuracy (ViT-B/32/-B/16/-L/14) vs. τJp's 85.0/88.2/90.9 at α=1, while requiring zero external task data. In task negation, TAK reduces target accuracy further (3.4/3.4/3.5 vs. 6.7/4.7/3.7) while better preserving control accuracy, solving the practical limitation that reviewers of the τJp paper explicitly identified as a weakness.

- **Robustness to scaling coefficient α (Fig. 4a):** The KFAC-regularized model maintains near-peak accuracy across α ∈ [0, 2] on ViT-B/32, whereas all unregularized and post-hoc merging strategies collapse sharply away from their optimal α. This eliminates the need for held-out validation data for coefficient search.

- **Practical efficiency (Fig. 6):** With a single MC sample, KFAC pre-computation for all 8 vision tasks takes only 4 minutes total. During training, the KFAC regularizer runs ~3× faster than τJp and adds only +12% VRAM overhead in the linearized regime.

- **KFAC compression analysis (Fig. 7b):** Block-diagonal compression reduces storage from ~550 MB to ~70 MB (87% reduction) at only 1-point absolute accuracy cost on ViT-B/16, demonstrating practical deployability under memory constraints.

---

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Asymmetric weighting in the Kronecker merge (Eq. 8) is unjustified.** The heuristic $\sum_{t \neq t'} \lambda_t (B_t^l \otimes A_t^l) \approx (\sum_{t \neq t'} B_t^l) \otimes (\sum_{t \neq t'} \lambda_t A_t^l)$ applies the task weights $\lambda_t$ to $A$ but not $B$ without any stated rationale. The paper acknowledges this as a heuristic ("Empirically, this heuristic (Eq. (8)) matches the un-merged formulation's performance"), but provides no analysis of when the approximation degrades or why the asymmetric weighting is chosen over alternatives (e.g., distributing $\sqrt{\lambda_t}$ to each factor). Users of the method cannot predict failure cases.

- **Task negation improvement over τJp is unexplained.** TAK outperforms τJp by a large and uniform margin in negation (3.4 vs. 6.7, 3.4 vs. 4.7, 3.5 vs. 3.7 across ViT-B/32/-B/16/-L/14), whereas in task addition the margin is small (Table 1 vs. Table 2). This asymmetry is never discussed. Whether it reflects a structural advantage of KFAC's curvature proxy for negation, or a sensitivity of τJp's hyperparameters in that setting, would materially strengthen the paper's contribution story.

- **Weaker language task performance is insufficiently analyzed.** TAK achieves 78.7 vs. τJp's 81.3 absolute accuracy on T5-base (Table 2 bottom). The paper's explanation — "textual domains may still benefit from even more accurate curvature estimation" — is a single vague sentence. An analysis of which of the six NLI tasks drive the gap, or whether the overlap in vocabulary projection layers is a structural factor, would ground the limitation more usefully.

- **MC sample degradation is noted but unexplained (Fig. 7a, Sec. 4).** The paper states "performance deteriorates beyond [1–2 MC samples], with variance across seeds increasing" but offers no mechanism. As MC sampling should reduce curvature estimation variance, the degradation is non-obvious and worth at least a hypothesis.

### Trivial

- **KFAC memory cost for ViT-L/14 is not reported.** The paper reports KFAC storage for ViT-B/16 (~550 MB full, ~70 MB block-compressed) but not for ViT-L/14, whose substantially wider layers have quadratically larger KFAC factors. Since ViT-L/14 yields the strongest empirical results, reporting its storage cost (and whether compression is needed) would inform practitioners at scale.

---

## Nice-to-Haves

- **Figure 5 task localization is partially tautological.** The regularizer directly minimizes $\|J_\theta f(x, \theta_0)\tau_t\|^2$ for out-of-distribution inputs, so the histogram showing these values concentrated near zero is expected by construction. The more informative question — whether task localization as measured here correlates with per-task accuracy gains — is not addressed. The figure is visually compelling but more analytical grounding would help.

- **Analysis of what information the KFAC at $\theta_0$ encodes.** The paper shows that the pre-trained model's curvature is sufficient to approximate data-dependent regularization, but does not explain why. A focused comparison of the principal directions of $G_t$ computed at $\theta_0$ vs. $\theta_t^*$ would clarify the regime where dataless curvature is expected to suffice.

- **Criterion mismatch (squared loss vs. cross-entropy) deserves a sentence of justification.** Section 3.2 notes "If we choose squared error rather than the training criterion, the GGN becomes the Jacobian Gram matrix exactly." Since models are trained with cross-entropy, a brief explanation of why this criterion substitution remains a useful proxy would preempt reader confusion.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"The comparison with TaLoS may involve different configurations" (Harsh Critic).** The paper explicitly marks TaLoS numbers with †: "Numbers marked with † for TaLoS (Iurada et al., 2025) are taken from the original paper." Cross-paper comparison in the non-linear regime is standard practice; the margin on the only metric where TaLoS leads (ViT-B/16 normalized: 92.4 vs 91.0) is not large enough to constitute a major concern. REMOVED as minor.

- **Claim that the derivation relies on squared loss "mismatches" cross-entropy training (Harsh Critic framing as a significant concern).** The paper explicitly acknowledges this in Sec. 3.2, calling it a criterion substitution that enables the GGN connection. This is an intentional design choice, not an oversight. REMOVED as a stated paper limitation rather than a deficiency.

- **Strength: "Task localization as direct evidence of weight disentanglement" (Strength Finder).** Partially valid but partially tautological as noted above. RETAINED in Nice-to-Haves with caveat.

---

## Novel Insights

The paper's most novel technical observation is that representation drift regularization under linearized fine-tuning is equivalent to a quadratic form in the Jacobian Gram matrix, which in turn is the GGN under squared loss. This connection is non-obvious and practically consequential: it allows the entire body of KFAC approximation literature to be applied to a problem (weight disentanglement in task arithmetic) that was previously addressed only through data-dependent Jacobian-vector products. Equally noteworthy is the empirical finding that KFAC computed at the *pre-trained* initialization $\theta_0$ contains sufficient task-specific curvature information to match data-dependent regularization — suggesting that well-pre-trained models' curvature at initialization already encodes much of the task-relevant geometry needed for disentanglement.

---

## Suggestions

1. **Explain or remove the asymmetry in Eq. (8).** Either justify why $\lambda_t$ is applied to $A$ and not $B$ (or symmetrically), or run an ablation comparing $(\sum_t \lambda_t B_t) \otimes (\sum_t A_t)$, $(\sum_t B_t) \otimes (\sum_t \lambda_t A_t)$, and $(\sum_t \sqrt{\lambda_t} B_t) \otimes (\sum_t \sqrt{\lambda_t} A_t)$ to show the choice is robust.
2. **Analyze the task negation asymmetry.** Determine whether the larger TAK advantage in negation vs. addition is due to τJp's hyperparameter sensitivity in the negation setup, or to a structural property of curvature-based regularization.
3. **Expand the language task analysis** to identify which of the six NLI tasks are most affected by the approximation gap.
4. **Report ViT-L/14 KFAC storage** with and without compression so practitioners can assess feasibility at large scale.

---

## Score and Decision

**Calibration anchors:**

| Path | Avg Score | Round | Comparison |
|---|---|---|---|
| 1VwWi6zbxs (τJp paper) | 6.00 | R1+R2 | Direct predecessor; TAK is clearly stronger (dataless, better negation, principled derivation) |
| dj0TktJcVI (Attention-Only FT) | 6.25 | R1 | TAK outperforms this in most settings and has stronger theoretical grounding |
| irPcM6X5FV (Submodule Linearity) | 6.00 | R1+R2 | Similar task arithmetic domain; TAK's GGN derivation is more principled |
| 1v7SRWsYve (MAP) | 6.33 | R2 | Quadratic approximation for model merging; TAK has comparable depth but different scope |
| D7KJmfEDQP (Uncertainty-based merging) | 6.00 | R2 | Similar empirical scope; TAK has better theoretical foundation |
| puTxuiK2qO (AdaFisher) | 6.25 | R2 | Second-order optimizer using Fisher; TAK uses KFAC for regularization — different problem, similar technical depth |
| g8sGBSQjYk (Second-order KFAC parameterization) | 7.33 | R2 | Deeper theoretical KFAC contribution; stronger formalism than TAK |
| 8j9hz8DVi8 (CASPR Kronecker preconditioner) | 7.33 | R2 | Strong Kronecker approximation theory; TAK's theoretical depth is below this level |

**Round 1 bracket:** 6.0–7.5. **Round 2 narrowing:** TAK is consistently stronger than all the 6.0 anchors (τJp, submodule linearity, gradient matching) due to: (1) principled GGN derivation, (2) constant-complexity accumulation, (3) dataless operation matching data-dependent competitors. It is comparable to the 6.25–6.33 anchors. It falls below the 7.33 anchors, which have deeper theoretical machinery (convergence guarantees, formal Kronecker approximation theory). TAK's minor weaknesses (asymmetric heuristic, unexplained negation gap, incomplete language analysis) are not sufficient to bring it below the 6.0–6.5 anchors. Final score: **7.0**.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>