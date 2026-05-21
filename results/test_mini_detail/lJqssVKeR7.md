Now I have all the evidence needed. Let me produce the final consolidated review.

## Summary

This paper proposes **HiSo**, a Hessian-informed zeroth-order (ZO) federated optimization method that accelerates convergence by preconditioning ZO gradient estimates with a learned global diagonal Hessian approximation, while preserving scalar-only communication (no Hessian-related information transmitted). The paper introduces a generalized scalar-only communication FL framework (Algorithm 1) that decouples from vanilla ZO-SGD. Theoretically, it provides conditional convergence rates that can be independent of model dimension *d* and Lipschitz constant *L* under a "well-approximated Hessian" assumption. Empirically, HiSo achieves 1–5× speedups over the prior ZO-FL state-of-the-art (DeComFL) on LLM fine-tuning benchmarks (SST-2, QQP, SQuAD) with OPT-350M to OPT-2.7B models.

## Strengths

- **Generalized scalar-only communication framework (Section 3.3, Algorithm 1).** The paper correctly observes that dimension-free communication in FL relies on scalar representations, not on ZO-SGD specifically, and formalizes this into a general framework. This enables integration of Hessian-informed updates within the scalar-only paradigm—a clean extension over DeComFL, which is tied to vanilla ZO-SGD.

- **Novel low-whitening-rank analysis and tighter variance bound (Section 5.1).** The paper introduces the whitened trace ζ = Tr(H^{-1/2} Σ H^{-1/2}) and demonstrates via simulated eigenvalue distributions (Fig. 4) that ζ ≪ Lκ ≪ Ld, providing a theoretical basis for why Hessian-informed ZO can beat worst-case bounds. This conceptual contribution is independent of whether the specific learned *H* achieves it.

- **Extends convergence guarantees to multiple local updates τ > 1 (Corollary 3).** Prior work (DeComFL) could not give convergence guarantees under the low-effective-rank assumption when τ > 1. HiSo resolves this, providing a rate that remains dimension-independent under the well-approximated and low-whitening-rank conditions—a meaningful theoretical advance over the baseline.

- **Empirically achieves 1–5× speedup over DeComFL in communication rounds (Table 2).** Across all three tasks (SST-2, QQP, SQuAD) and three model sizes (OPT-350M, OPT-1.3B, OPT-2.7B), HiSo consistently requires fewer rounds to match DeComFL's best accuracy, with speedups up to 5.4× on SQuAD with OPT-350M (cutting communication cost from 52.73 KB to 9.77 KB). The communication savings over first-order methods reach 90 million× (Table 3).

- **Explicit qualifiers on limitations.** The paper includes a "Remarks about well-approximated condition" (Section 5.2) acknowledging that verifying the condition in LLMs is hard, and notes that performance at worst degenerates to DeComFL. Footnote 1 clarifies that "Hessian-informed" does not mean the full Hessian is computed. This transparency is commendable.

## Weaknesses

### Fatal

None.

### Major

- **The Hessian update heuristic (Eq. 12) lacks principled justification, undermining the "Hessian-informed" claim.** The rule H_{r+1} = (1-ν)H_r + ν·Diag(|Δx_r|²) is introduced without any derivation or formal connection to the true Hessian diagonal. The paper states "we have a free variable to approximate the diagonal Hessian through the following proposed rule" — this is hand-wavy. While footnote 2 acknowledges the method "resembles RMSProp," the title, abstract, and contribution bullets consistently present the method as "Hessian-informed" (e.g., "utilizes global Hessian information to speed up convergence"). The squared-update heuristic may simply be performing adaptive learning rate scaling (RMSProp-like) rather than genuinely tracking curvature. Without a lemma or empirical validation showing that H_r moves toward the true Hessian diagonal, the central label of the paper is an overclaim. This is the most significant weakness: the paper's core identity as "Hessian-informed" rests on an unsubstantiated heuristic.

### Minor

- **The "dimension-free" convergence rate is conditional on an unverified assumption.** Corollaries 1–3 assume the learned *H* satisfies the "well-approximated Hessian" condition (Definition, Eq. 17). The paper does not prove—or even provide evidence—that the online learned *H* satisfies this condition during LLM training. The simulation in Figure 4 uses a 200-dimensional log-normal toy problem, not an actual LLM. While the paper includes a "Remarks" paragraph acknowledging this limitation, the contribution bullet (line 40) states the dimension-free result without the condition, which could mislead readers. This is a presentation issue: the conditional rate is theoretically valid but should be framed more carefully as a *plausible explanation* rather than a proven property of HiSo.

- **Missing ablation: benefit of the learned Hessian is not isolated.** The only ZO baseline is DeComFL (identity preconditioner). There is no comparison to HiSo with a *fixed* diagonal preconditioner (e.g., estimated once and frozen). Such an ablation would disentangle whether the improvement comes from online adaptation (RMSProp-like scaling) or from genuinely tracking curvature. Without it, the "Hessian-informed" attribution remains ambiguous.

- **Communication cost discrepancy for OPT-1.3B on QQP is not explained.** In Table 3, HiSo's total communication cost is 96.67 KB vs DeComFL's 43.95 KB—more than double—even though HiSo achieves higher accuracy (64.20% vs 63.25%). The paper notes it is "only a little higher" but does not clarify that HiSo required substantially more total rounds to reach its own best accuracy in this case. This nuance is not visible in Table 2, which only reports rounds to match DeComFL's (lower) best accuracy. A brief explanation would avoid confusion.

- **The least-squares derivation (Section 4.1, Eqs. 5–7) has a technical sloppiness.** The scalar (uᵀH⁻¹u)⁻¹ depends on the random u and is absorbed into the learning rate, which is a constant. This changes the distribution of the update. The final update (Eq. 8) is correct and standard, but the derivation's justification is not rigorous.

### Trivial

- **Small-scale FL experimental setup.** The LLM experiments use 6 total clients with 2 sampled per round. This is a limitation for claims about scalability to larger FL deployments, though it is common for LLM fine-tuning given computation constraints.

## Nice-to-Haves

- Direct validation of the learned diagonal H against the true Hessian diagonal (or empirical Fisher) on a small model where computing the diagonal Hessian is feasible (e.g., the CNN from Figure 5). Even a rank correlation would substantially strengthen the "Hessian-informed" claim.
- Ablation with a fixed diagonal preconditioner (estimated e.g., from the first ~100 rounds) to isolate the effect of online adaptation.
- Reporting the total number of rounds to reach each method's own best accuracy in Table 3, not just the final communication cost.
- Adding a brief note on the O(d) per-step computational cost of sampling z ∼ N(0, H⁻¹) for completeness.

## Removed Points

The following points from the input reviews are removed with justification:

1. *"Reproducibility concern: appendix is referenced but not provided."* — The parser strips appendix sections from all papers; they exist in the original submission. (Hard Rule)
2. *"Missing comparison with compressed first-order methods (e.g., FedAdam with compression)."* — This is a missing-related-work/litigation concern; cannot verify existence of such baselines. (Hard Rule)
3. *"The authors could cite relevant work (Qin et al., 2024) more thoroughly."* — Missing related work. (Hard Rule)
4. *"No statistical significance tests are provided."* — The paper reports ± ranges. While more runs would help, this is standard practice for large-scale LLM fine-tuning and not a meaningful weakness. (Soft Rule)
5. *Criticism that the speedup metric is "inflated" because it measures rounds-to-match-DeComFL's-best.* — The metric is transparently defined in the table caption, and both Tables 2 and 3 are provided. HiSo also achieves higher final accuracy in nearly all cases, so reaching DeComFL's (lower) best accuracy is a reasonable comparison point. This is not inflated; it is clearly scoped. (Factually incorrect.)
6. *"The practical effectiveness of ZO-based FL is limited by its seriously slow convergence" characterization is too harsh.* — Not a weakness of the paper itself; removed as irrelevant.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a perspective that the paper itself does not already contain or imply.

## Suggestions

1. **Add a principled justification or empirical validation for the Hessian update rule (Eq. 12).** At minimum, compare |Δx_r|² with the diagonal of the empirical Fisher or Hessian on a small model. If the rule is heuristic, rename it (e.g., "adaptive ZO preconditioning") and tone down the "Hessian-informed" framing accordingly.
2. **Add an ablation with a fixed diagonal preconditioner** to isolate whether the benefit comes from any per-coordinate scaling or specifically from online adaptation.
3. **Clarify the conditional nature of the theoretical rate** in the contribution bullet and abstract—e.g., "under the well-approximated Hessian assumption, HiSo can achieve…" rather than presenting it as unconditional.
4. **Explain the OPT-1.3B+QQP communication cost discrepancy** by reporting total rounds to convergence for both methods in Table 3.

## Score and Decision

**Calibration report:**

| Anchor Paper | Path | Avg Score | Round | Comparison |
|---|---|---|---|---|
| FZooS (Federated ZO with Surrogate Gradients) | ZAMoxm86KV.md | 3.67 | R1 | **Weaker than HiSo.** This paper had an impractical Gaussian process assumption, heavy computation, and unfair comparisons. HiSo's approach is cleaner and more practical. |
| MeZO-A³dam (Adaptive ZO for LLM Fine-tuning) | OBIuFjZzmp.md | 4.75 | R1 | **Slightly weaker than HiSo.** Non-federated ZO paper with an incorrect lemma in its proofs. HiSo covers the FL setting and has stronger empirical breadth, but both share the issue of heuristics not being fully grounded. |
| Ferret (Federated Full-Parameter Tuning) | 9H1uctBWgF.md | 4.67 | R1 | **Comparable to HiSo.** First-order FL method with shared randomness. Had concerns about memory footprint and convergence. HiSo's ZO approach offers different tradeoffs; both have merit and limitations. |
| FedNewton (Newton-type FL) | uaGNerHa1J.md | 4.67 | R2 | **Comparable to HiSo.** Uses second-order info in FL. The generalization bounds are clean but restricted to kernel ridge regression. HiSo targets the more practical LLM fine-tuning setting. |
| Curvature-Informed SGD (PSGD) | sawjxRnVpF.md | 4.50 | R2 | **Weaker than HiSo.** The Lie-group preconditioning is elegant but the evaluation is on centralized (not federated) training. HiSo addresses the more constrained FL communication setting. |
| Δ-SGD (Adaptive FL with Auto-Tuned Clients) | g0mlwqs8pi.md | 6.50 | R2 | **Stronger than HiSo.** This paper had a clean theoretical contribution with milder assumptions and thorough empirical validation across multiple FL scenarios. Accepted poster. |
| PAdaMFed (Problem-Parameter-Free FL) | ZuazHmXTns.md | 7.60 | R1 | **Substantially stronger than HiSo.** Accepted oral. Clean theoretical contribution removing hyperparameter tuning burden, with rigorous empirical support. |

**Round 1 bracket:** The paper sits between the weak band (avg 3.0–3.4: papers with serious methodological issues) and the strong band (avg 7.5+: accepted oral/spotlight papers with very clean contributions). Bracket: (3.5, 7.5).

**Round 2 narrowing:** Among papers in the middle band, HiSo is comparable to or slightly stronger than papers scoring 4.5–4.75 (FedNewton, Ferret, MeZO-A³dam) but clearly weaker than papers scoring 6.0–6.5 (Δ-SGD). The decisive factor is the unsubstantiated Hessian update heuristic and the gap between the "Hessian-informed" claim and what is actually demonstrated. This places the paper below the acceptance threshold.

**Final Score: 5.0** — The paper has a genuinely clever algorithmic idea (preconditioning ZO gradients with a learned diagonal while preserving scalar-only communication) and compelling empirical acceleration. However, the central claim of being "Hessian-informed" is not adequately validated—the update is a heuristic with no proven connection to the true Hessian. The conditional theory, while technically valid, is framed too assertively in the contribution summary. These issues are substantive enough to place the paper below the acceptance threshold in its current form, though the core direction is promising.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>