Now I have a solid calibration picture. Let me finalize.

**Calibration summary:**

**Round 1 bracket: 5.5–7.5**

**Round 2 narrowing:**

| Anchor | Score | Comparison to our paper |
|---|---|---|
| Deep Unlearning (pUOesbrlw4) | 5.25 | Our paper is stronger (better motivation, cleaner method) |
| Oblivious Unlearning (wAemQcyWqq) | 5.67 | Our paper is stronger (more solid ablation) |
| Decoupling Class Label (OHOmpkGiYK) | 5.75 | Our paper is stronger (fewer technical concerns) |
| Label-Agnostic Forgetting (SIZWiya7FE) | 6.00 | Comparable novelty, our paper slightly cleaner method but thinner main-text evidence |
| Scalable Exact Unlearning (oe51Q5Uo37) | 6.75 | Our paper is weaker (lacks theoretical guarantees, less extensive experiments) |
| Jogging Memory (fMNRYBvcQN) | 6.75 | Our paper is weaker (less extensive evidence, narrower impact) |

**Final score: 6.0** — the paper is comparable to Label-Agnostic Forgetting (both address a novel problem setting with a sound method and solid but not exceptional experiments). The core contribution (first FF unlearning method) is genuine and well-executed, but gaps in experimental rigor (no error bars, single forgetting ratio, G-MIA false-positive uncharacterized) and thin main-text evidence prevent a higher score. These are addressable in revision.

Now let me write the final review.

---

## Summary
This paper proposes FF-Erase, the first machine unlearning method for Forward-Forward (FF) models. FF-Erase uses a separately trained guidance model to provide stable target goodness distributions, steering the original model's layer-wise goodness scores toward those of an FF model ignorant of the forgetting data via KL-divergence minimization, interleaved with periodic "recovering forward" passes on remaining data. The paper also introduces G-MIA, a goodness-based membership inference attack for verifying FF unlearning. Experiments show FF-Erase achieves 1.9–3.1× speedup over retraining with minor accuracy degradation.

## Strengths
- **First formalization of FF unlearning with clear empirical motivation:** The paper identifies two specific, non-trivial challenges unique to FF unlearning — parameter-tuning sensitivity and layer-wise update divergence (§1, lines 38–41). The GA failure is systematically demonstrated in §6.3 (Figure 5), sweeping λ across six orders of magnitude and showing a fundamental dilemma: higher λ causes model collapse, lower λ fails to unlearn.
- **Guidance model design directly addresses the identified challenges:** The KL-divergence-based goodness decrease (Eq. 5) provides a principled solution — the guidance model supplies valid goodness distribution targets (preventing distribution shift into invalid regions) and supplies per-layer targets (resolving the per-layer penalty problem). The R.G.M ablation in Table 1 strongly validates this: random-guidance collapses to ~55% accuracy while even weak proper guidance maintains ~78%+.
- **G-MIA consistently outperforms comparable black-box MIAs:** Figure 3 shows G-MIA achieving higher accuracy than black-box final-layer MIA (FL) across all three architectures, and even matching white-box attacks on deeper models (VGG13/CIFAR-100).
- **Dual guidance acquisition strategies for different data regimes:** Mini-retrained and fast-distilled strategies (§4.2) cover different data-availability scenarios, with Table 1 showing both can achieve effective unlearning with different speed-accuracy trade-offs.
- **Concrete, experimentally grounded efficiency analysis:** Section 4.3 provides a time decomposition (Eq. 9), and Table 1 confirms the predicted 25–35% of retraining time, directly supporting the 1.9–3.1× speedup claim.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor
- **G-MIA false-positive regime with collapsed models:** In Table 1, R.G.M (random guidance, producing a collapsed model with Acc_f=51.18%, Acc_t=55.53%) yields G-MIA scores (ACC 0.553, AUC 0.575) nearly identical to retraining (ACC 0.551, AUC 0.571). This means G-MIA would certify a broken model as successfully unlearned. In practice this is mitigated by also checking model utility, but the paper should characterize this failure mode since G-MIA is proposed as a standalone verification tool.
- **No standalone guidance model metrics reported:** The paper does not report the guidance model's own G-MIA score or test accuracy as a standalone unlearned model. The dashed lines in Figure 4 hint at guidance model accuracy, but formal reporting would clarify whether FF-Erase's forgetting step meaningfully improves upon simply deploying the guidance model (which is already ignorant of forgetting data by construction). This does not invalidate the method — the guidance model likely underperforms on utility since it's trained on less data — but reporting these metrics would strengthen the evidence.
- **No error bars or uncertainty estimates:** No standard deviations, confidence intervals, or multiple-seed results are reported for any experiment. Unlearning evaluations are sensitive to data splits and initialization, making this a notable omission.
- **Only 20% forgetting ratio tested:** All experiments use β=20%. Practical unlearning spans much smaller fractions (individual users, 1–5%) and larger ones (entire cohorts, 50%). Testing at varied ratios would strengthen generality claims.
- **G-MIA "black-box" framing needs qualification:** G-MIA accesses per-layer goodness vectors, which is substantially more information than standard black-box MIAs that use only final prediction outputs. The paper is transparent about what G-MIA uses, but calling it "black-box" without qualification is misleading; it occupies a middle ground.

### Trivial
- The crucial notation clarification that g^l is computed via column-wise L1 norm (making it a vector) is relegated to a footnote (line 98) rather than the main text.
- The claim that "determining the validity of a goodness distribution in advance remains challenging" (§1, line 38–39) is stated without evidence or citation.
- Computational cost of G-MIA shadow model training is not reported, which matters for practical adoption.

## Nice-to-Haves
- Add a pure fine-tuning-on-remaining-data baseline (recovering forward only, without the forgetting step) to quantify the marginal value of the goodness-decrease mechanism. While this is not a standard unlearning baseline (it doesn't actively remove forgetting data), it would clarify whether the interleaved forgetting step adds value beyond simply reinforcing remaining data.
- Vary forgetting ratios (e.g., 1–5% and 50%) to demonstrate FF-Erase's robustness in practical regimes.
- Report statistical uncertainty across multiple random seeds for all key results.

## Removed Points
These points are flagged to be removed, treat them with caution.

- **"Missing the most natural baseline: fine-tuning on remaining data alone" (Harsh Critic Critical Issue 1):** The recovering forward (Eq. 6) is already a component of FF-Erase. Fine-tuning alone without any forgetting step is not a standard unlearning baseline — it does not actively remove forgetting data's influence. While comparing against it would add value (moved to Nice-to-Haves), its absence does not weaken the paper's core claims.
- **"The guidance model may already be a sufficient unlearned model — this is not discussed" (Harsh Critic Critical Issue 2):** The paper does show guidance model accuracy via dashed lines in Figure 4. The guidance model is trained on less data (α₁=30-50% data, α₂=20-50% epochs) and likely has lower utility than the FF-Erase output. This has been downgraded to a Minor weakness requesting formal metrics.
- **"Main-text results are too narrow — only VGG13/CIFAR-10 shown" (Harsh Critic §6.2 note):** The paper states other results are in Appendix C, which was stripped by the parser. Per rules, do not penalize for stripped appendix content.
- **"Influence-function incompatibility with FF should be demonstrated not stated" (Harsh Critic §2 note):** The paper's claim is that these methods were designed for BP models and are not suited for FF. This is a scope statement, not a central claim requiring empirical proof. Removed as scope creep.
- **"The recovering forward alone would suffice — i.e., whether the baseline would work" (Harsh Critic Methodology note):** Redundant with the fine-tuning baseline point above. Moved to Nice-to-Haves.
- **Strength Finder: "Multi-architecture and multi-dataset evaluation scope":** While the paper claims to span 4 datasets and 3 architectures, the main text evidence is limited to VGG13/CIFAR-10 (rest in stripped appendix). The strength is noted but qualified.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
- Report the guidance model's standalone G-MIA score, Acc_f, and Acc_t alongside every row in Table 1. This would let readers directly assess the marginal value of the FF-Erase forgetting step.
- Add a row or brief experiment showing G-MIA scores for models at varying degradation levels (random perturbations, random labels) to characterize the false-positive regime identified in the R.G.M result.
- Qualify G-MIA's "black-box" label — acknowledge it uses per-layer goodness vectors, placing it between traditional black-box and white-box access levels.
- Move the column-wise L1 norm clarification from footnote to main text in §3.1.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>