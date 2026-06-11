I now have sufficient calibration evidence. Let me produce the final review.

---

## Summary

This paper identifies a genuine gap — there is no prior work on machine unlearning for Forward-Forward (FF) models — and proposes FF-Erase, a guidance-model-based method that shifts goodness vectors toward a reference distribution via KL divergence, enabling stable unlearning where naive gradient ascent causes model collapse. It also introduces G-MIA, a membership inference attack using layer-wise goodness vectors for unlearning verification. Experiments on standard vision benchmarks show FF-Erase achieves comparable effectiveness to retraining at 1.9–3.1× speedup.

## Strengths

- **First systematic diagnosis of why conventional unlearning fails on FF models (§1, §6.3, Figure 5):** The paper identifies that GA on FF models causes either model collapse (large λ) or ineffective forgetting (small λ) due to FF's BP-free, layer-wise training. Figure 5 empirically validates across six λ values that no single λ works for FF models — a concrete, architecture-specific problem diagnosis.

- **G-MIA consistently outperforms standard black-box MIA (FL) across all tested settings (§6.1, Figure 3):** Using layer-wise goodness vectors, G-MIA beats the standard final-layer MIA on all datasets and architectures tested (TinyCNN, AlexNet, VGG13 across CIFAR-10/100, MNIST, Fashion-MNIST). On VGG13/CIFAR-100, G-MIA achieves the best accuracy among all methods including white-box attacks.

- **Quantified 1.9–3.1× speedup with explicit cost decomposition (§4.3, Table 1, Figure 4):** Equation (9) decomposes total unlearning time into guidance acquisition and goodness-decrease phases. Empirically validated across 9 configurations — e.g., FF-Erase(R)-(0.5,0.5) completes in 518.5s (46.8% of retraining's 1107s), with the breakdown into t₀ and t₁ components explicit and empirically grounded.

- **Ablation with random guidance model (R.G.M) cleanly proves guidance necessity (Table 1, §6.4):** R.G.M causes accuracy on forgetting data to collapse to 55.53% vs 80–82% for all proper guidance models, ruling out the explanation that the KL-loss alone provides stability. This is a well-designed negative control.

- **Two practical guidance-model strategies for different data regimes (§4.2):** Mini-retrained (for abundant remaining data) and fast-distilled (for scarce remaining data) strategies with Table 1 directly comparing their trade-offs — e.g., D-(0.5,0.5) achieves G-MIA ACC of 0.556 while R-(0.5,0.5) achieves 0.562, showing distillation is competitive when data is abundant but remains viable with fewer samples.

## Weaknesses

### Fatal

None.

### Major

- **No statistical uncertainty reported in any quantitative result (§6, Figures 3–5, Table 1).** Every result is a single point with no error bars, standard deviations, or mention of multiple random seeds. This is critical because the paper's comparisons involve small differences that could be within noise: G-MIA ACC of 0.5245 vs retraining's 0.551 (Figure 4c, a difference of ~0.027), and Acc_f ranges of 80.48–81.58 with retraining at 81.61 (Table 1, differences of 0.03–1.13 points). Without variance estimates, the reader cannot assess whether FF-Erase truly matches retraining or whether the improvement over GA is meaningful. For a paper making precise numerical comparisons that underpin its central claims (effectiveness equivalence to retraining, speedup ratios), this is the most impactful weakness.

- **G-MIA is misleadingly characterized as a "black-box" attack (§1, §5).** The paper repeatedly calls G-MIA a "black-box" attack (abstract: "powerful and lightweight black-box attack"; §1 contributions: "Accurate Black-Box Unlearning Verification"; line 62: "superior accuracy under a strict black-box constraint"), but the attacker requires goodness vectors from every layer of the model (line 200: "the attacker can obtain the output of the target model of attack, i.e., the goodness vectors from all layers"). In standard MIA terminology, accessing intermediate representations is grey-box, not black-box (which is restricted to final outputs). The comparison against FL (final-layer MIA, Figure 3) is therefore not apples-to-apples — G-MIA uses strictly more information. The paper should reclassify G-MIA as a grey-box attack and reframe comparisons accordingly. This is a framing/scope issue, but it directly affects how readers interpret the claimed advantages.

- **The G-MIA verification metric has a plausibly circular relationship with FF-Erase (§6.2, Figure 4c) that is neither acknowledged nor addressed.** FF-Erase explicitly manipulates goodness vectors toward a guidance model's distribution via KL divergence (Eq 5), while G-MIA determines membership by classifying those same goodness vectors (Eq 10). The fact that FF-Erase(D) achieves a G-MIA ACC of 0.5245 — *lower* than retraining's 0.551 — is suspicious: if retraining is the gold standard, an approximate method outperforming retraining on G-MIA suggests G-MIA may be measuring goodness-vector alignment rather than genuine membership information removal. This does not invalidate the method, since the guidance model is genuinely ignorant of forgetting data, but it requires discussion. The paper should either (a) provide alternative verification (e.g., model inversion, downstream task degradation on forgetting data) or (b) demonstrate that G-MIA is robust to the specific alignment operation FF-Erase performs.

### Minor

- **Only one dataset-model configuration for the main unlearning experiments (§6.2).** Figure 4 uses only VGG13 on CIFAR-10; other configurations are relegated to the appendix (stripped by the parser). The claimed 1.9–3.1× speedup's generality across architectures and datasets is therefore uncertain from the main paper alone.

- **No ablation or sensitivity analysis for the recovery step frequency K (§4.1).** K is described as "empirical" and "determined by the dataset" (line 160), but no experiments explore its impact on the effectiveness–efficiency trade-off. Since K directly appears in the speedup formula (Eq 9: K⁻¹ term), this is a notable omission.

- **Potential information leakage in the fast-distilled guidance model (§4.2).** The fast-distilled strategy (Eq 8) uses KL divergence with the original model's output on remaining data. Since the original model was trained on *all* data (including forgetting data), this could theoretically propagate some influence of the forgetting data into the guidance model, partially undermining its role as "ignorant of the forgetting data" (line 121). Likely a small effect in practice, but unaddressed.

### Trivial

- Slight numeric discrepancy between Figure 4 caption (RE G-MIA ACC = 0.5320) and Table 1 (RE G-MIA ACC = 0.551) — likely from different experimental configurations but should be clarified.
- The text claims G-MIA "presents a better performance than white-box MIAs" (§6.1) but Figure 3's caption notes ST (a white-box method) is the best overall MIA. The claim should be scoped precisely ("better than some white-box methods").

## Nice-to-Haves

- An ablation on the sensitivity of G-MIA to synthetic data quality (used for shadow model training) would strengthen the paper.
- Adding at least one larger dataset (e.g., CIFAR-100 with a deeper model) to the main-text unlearning results.
- A dedicated limitations section would improve the paper's completeness.

## Removed Points

*These points were raised by reviewers but are excluded from the main evaluation for the reasons stated below; they are preserved here in case they are useful during discussion.*

- **"Baseline comparisons are too narrow"** — Removed. GA is a reasonable representative of BP-based unlearning methods. The paper's structural argument about why BP methods fail (layer-wise independence, parameter sensitivity) is method-agnostic. Demanding concrete impossibility arguments for each family of methods (teacher-student, influence functions, etc.) is scope creep and would not change the paper's core claims.
- **"No code release"** — Removed per hard rule: questioning the existence or release status of cited entities is not permitted.
- **"Missing related works"** — Removed per hard rule: I cannot verify what related works are missing without external sources.
- **Formatting/style nitpicks and parser artifacts** — Removed per hard rule: formatting artifacts are parser issues, not author errors.
- **"Missing appendix content"** — Removed per hard rule: the parser strips appendix sections; they exist in the original submission.
- **"G-MIA synthetic data sensitivity is not evaluated"** — Removed as speculative: the paper does not evaluate this, but there is no evidence the concern materializes.
- **Strength Finder's generic/delusional strengths** — Removed. Several claimed strengths (e.g., "the paper addressed an important problem," "this paper targeted an interesting question") are generic and not specific to the paper's content.

## Novel Insights

The most insightful observation from the reviews is the potential circularity between FF-Erase and G-MIA, specifically that FF-Erase(D) achieves lower G-MIA scores than retraining. This exposes a subtle verification tautology: FF-Erase optimizes goodness-vector alignment toward a guidance model (Eq 5), and G-MIA measures membership via goodness-vector patterns (Eq 10). When FF-Erase outperforms retraining on G-MIA, it does not necessarily mean FF-Erase is a *better* unlearning method — it may mean G-MIA is partially measuring the alignment artifact rather than genuine membership removal. This does not invalidate FF-Erase (the guidance model is genuinely ignorant of forgetting data, making the alignment direction correct), but it means the G-MIA scores for FF-Erase should be interpreted more cautiously, and the paper would benefit from a second, independent verification signal.

## Suggestions

1. **Add standard deviations / error bars (multiple seeds) to all quantitative results.** This is the single highest-priority fix. Every claim of "matches retraining" or "outperforms baselines" is currently unverifiable.
2. **Reclassify G-MIA as a grey-box or intermediate-output attack** rather than "black-box," and reframe comparisons against FL accordingly. If the authors wish to claim a black-box attack, they should restrict G-MIA to the same information as FL (final output only).
3. **Discuss and address the potential circularity between FF-Erase's goodness alignment and G-MIA's goodness-based verification.** Provide at least one supplementary verification method (e.g., model inversion attacks, measuring the model's behavior change on forgetting data in a downstream task).
4. **Add an ablation on K (recovery frequency)** in the main text, since K directly affects both utility and the claimed speedup.
5. **Include at least one additional dataset-model configuration** (e.g., a deeper model on CIFAR-100) in the main-text unlearning results to substantiate the generality of the speedup claim.

## Score and Decision

### Calibration Procedure

**Round 1 (Bracketing):** Three queries on machine unlearning, verification, and speedup with score bounds (−∞,3.5), (3.5,7.5), and (7.5,∞). Weak anchors clustered at 1.5–3.0 (all Reject). Middle anchors clustered at 5.33–6.0 (one Accept at 6.0, the rest Reject). Strong anchors at 7.6–8.0 (all Accept, but on unrelated topics). **Initial bracket: 4.5–6.0.**

**Round 2 (Narrowing):** Two queries on Forward-Forward training (3.5–5.5) and MIA-based unlearning verification (5.0–7.0). Key anchors and their comparison to this paper:

| Anchor | Score | Decision | Comparison |
|--------|-------|----------|------------|
| "The Trifecta" (FF paper, wcKGK0tRHD) | 5.0 | Reject | Comparable topic (FF), similar evaluation scope but our paper has stronger novelty (first FF unlearning vs. incremental improvements). Our paper's evaluation has a more impactful gap (no error bars). |
| "Unlearning via Sparse Representations" (TLBPjECC5D) | 5.25 | Reject | Similar contribution level (novel unlearning approach). Our paper addresses a broader problem (not just class unlearning) and provides a verification method, but lacks error bars. Comparable quality. |
| "Deep Unlearning: Fast and Efficient" (pUOesbrlw4) | 5.25 | Reject | Mixed reviews (8,3,5,5). Similar contribution level. Both papers have evaluation gaps (theirs: no MIA verification; ours: no error bars). |
| "Information Theoretic Eval Metric" (NGF1wDDBMm) | 5.75 | Reject | Stronger evaluation rigor than our paper (it is about evaluation metrics), but different contribution type. |
| "A Closer Look at ML for LLMs" (Q1MHvGmhyT) | 6.0 | Accept | Stronger evaluation completeness (multiple scenarios, clear metrics). Our paper has more novel problem identification but weaker evaluation. |

**Round 1 bracket: 4.5–6.0. Round 2 narrowing: the paper is most comparable to the 5.0–5.25 anchors** — papers with genuine contributions but evaluation limitations that prevented acceptance.

### Final Score

The paper has a genuinely novel contribution (first FF unlearning method) and well-motivated design. However, the absence of any variance estimates in quantitative results — especially when claims depend on small differences — is a major evidential gap. The G-MIA threat-model mischaracterization and potential circularity further weaken the evaluation. Compared to calibration anchors, the paper sits closest to papers scoring 5.0–5.25 (novel idea, meaningful contribution, but evaluation shortcomings that prevent acceptance at a top venue).

**Score: 5.0**

**Decision: Reject** — The paper's core idea is promising and the problem is well-framed, but the evaluation gaps (primarily the lack of error bars and the G-MIA frame issues) are too significant to support the strength of the claims made.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>