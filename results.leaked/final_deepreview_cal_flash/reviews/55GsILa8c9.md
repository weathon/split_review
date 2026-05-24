Now I have all the information I need. Let me produce the final consolidated review.

## Summary

CausalNovo introduces a causality-informed framework for de novo peptide sequencing that learns causal (signal-related) representations from mass spectra while suppressing reliance on non-causal (noise) peaks. The method formalizes the task via a Structural Causal Model, derives independence and sufficiency principles, and implements them through a contrastive learning objective (for intervention invariance) and cross-entropy losses on disentangled causal/non-causal representations. Experiments across three benchmarks (Nine-species, Seven-species, HC-PT) and three strong baselines (CasaNovo, AdaNovo, π-HelixNovo) show consistent and often large improvements in amino acid, peptide, and PTM-level accuracy.

## Strengths

1. **Consistent and substantial empirical gains across all settings.** Every baseline benefits on every metric and every dataset (Table 1): amino acid precision improves by up to +14.2% (AdaNovo on HC-PT), peptide precision by up to +12.0% (CasaNovo on Seven-species), and PTM precision by up to +15.1% (π‑HelixNovo on Seven-species). The improvements are not sporadic—they hold across all three Transformer-based baselines and all three datasets, strongly validating the core claim.

2. **Demonstrable robustness to noise via multiple complementary analyses.** The vulnerability analysis (Figs. 1, 3) shows that when noise peaks are systematically replaced, baseline precision degrades sharply while CausalNovo-enhanced models degrade far less (average Relative Improvement of +13.5%–+15.7% on HC-PT). The NSR analysis (Fig. 4) shows CausalNovo maintains higher precision at all noise-signal ratios, with average gains of +10%–+12%. This multi-perspective evidence directly supports the claim that the framework reduces reliance on spurious correlations.

3. **Mechanistic validation through attention analysis.** Table 7 provides interpretable evidence: CausalNovo raises the fraction of predictions where all three top-attended peaks are causal from 19.26% to 32.87%, and reduces the fraction where none are causal from 12.73% to 10.76%. This connects the causal representation learning objective to actual model behavior.

4. **Principled causal formulation grounded in an SCM.** Section 3.2 formalizes de novo sequencing with a Structural Causal Model and derives two actionable principles (independence and sufficiency). Even though the implementation-theory correspondence has issues (see Weaknesses), the overall conceptual framework is clear and provides a principled departure from purely statistical approaches.

5. **Thorough ablation studies.** Tables 4 and 5 decompose the contribution of each component (independence contrastive loss, purification objective, symmetric training, replace-based perturbation, causality enhancement), confirming each adds measurable value.

6. **Cross-species generalization.** Table 3 shows CausalNovo improves CasaNovo on all nine species in leave-one-out validation (average +2.6% peptide precision), demonstrating that the benefits extend across diverse organisms.

## Weaknesses

### Major

1. **The independence objective as implemented does not realize the claimed conditional mutual information.** The paper states the goal as maximizing $I(z_c; z_c' \mid C)$ (line 99) and later $I(z_c; z_c' \mid Y)$ (Eq. 5), but the implemented contrastive loss (Eq. 5) is a standard InfoNCE loss that operates on pairs $(z_c, z_c')$ from the same spectrum versus negatives from other spectra in the batch. This loss approximates unconditional MI $I(z_c; z_c')$, not conditional MI $I(z_c; z_c' \mid Y)$ — the label $Y$ does not appear in the contrastive objective. The paper acknowledges that "each peptide is unique" (implicitly via "Y can serve as a proxy for C"), which means conditioning on $Y$ would trivially reduce to the unconditional case, but the text does not make this reasoning explicit. The causal motivation (invariance to intervention) still works with unconditional contrastive learning, but the theoretical framing as *conditional* MI is misleading and should be corrected or clarified.

2. **The purification objective is described in a confusing and potentially contradictory manner.** Section 3.3 states the auxiliary objective "maximizes $I(z_s; Y)$ which can indirectly lead to the purification of $z_c$." Maximizing the mutual information between the *non-causal* representation $z_s$ and the label $Y$ would normally encourage $z_s$ to carry predictive information, which seems to contradict the goal of isolating causal information in $z_c$. The paper's explanation of why this aids purification is unclear (the paragraph from "However, since $z_c$ and $z_s$ may share..." onward is particularly hard to parse). The ablation in Table 4 shows this component is empirically beneficial, suggesting the implementation works, but the textual rationale needs substantial revision. A competitive disentanglement mechanism (where both $z_c$ and $z_s$ are pushed toward $Y$ while the independence constraint forces a split) could justify the design, but this is not articulated in the paper.

### Minor

3. **No error bars, standard deviations, or multi-run statistics.** All results in Tables 1–7 are reported from a single run. Given that retrained baselines differ substantially from originally published numbers (e.g., π-HelixNovo on HC-PT: original 0.588, retrained 0.532; CasaNovo on HC-PT: original 0.442, retrained 0.525), it is important to establish whether the reported CausalNovo improvements are stable across random seeds. Reporting means and standard deviations over at least 3 runs would address this.

4. **Key hyperparameters for the causal intervention are not specified.** The tolerance threshold $\gamma$ (Eq. 4) and the replacement fraction $\alpha$ (Section 3.4.1) are never given numerical values in the main text. These parameters control the intervention quality and directly affect results. (If they appear in the appendix, they should be in the main paper.)

5. **Retrained baseline discrepancies are not discussed.** Tables 1–2 report both the original published numbers and retrained results. The differences are sometimes large (e.g., π-HelixNovo drop from 0.588 to 0.532 on HC-PT). A brief explanation of possible causes (e.g., different random seeds, hardware differences, hyperparameter tuning mismatches) would help the reader assess whether the CausalNovo gains partly reflect weakened baselines rather than genuine improvement.

6. **Cross-species validation is only conducted on CasaNovo.** Table 3 tests only one baseline. Extending this analysis to AdaNovo and π-HelixNovo would strengthen the model-agnostic claim, especially since the model-agnostic framing is a key selling point.

7. **The "model-agnostic" claim rests on only three Transformer-based models.** All three baselines use Transformer encoder-decoder architectures. Testing on a non-Transformer model (e.g., convolutional PointNovo or DeepNovo) would more convincingly demonstrate agnosticism.

### Trivial

8. The tool or library used to generate theoretical spectra (for identifying signal vs. noise peaks) is not cited. Adding a reference (e.g., pyteomics or the relevant algorithm) would improve reproducibility.

## Nice-to-Haves

- A sensitivity analysis for $\gamma$ and $\alpha$ (similar to the perturbation analysis in Table 6) would help understand how sensitive results are to these choices.
- A breakdown of where the 2.3× training time overhead goes (additional forward passes? re-encoding? contrastive loss computation?) would help practitioners.
- In Eq. (5), the denominator includes the positive pair twice (once in the numerator and once in the sum over negatives); standard InfoNCE excludes the positive from the negative set. Clarify whether this is intentional or a typo.

## Removed Points

The following points from the input reviews were removed per the filtering rules:

- *"The paper does not cite the tool used to generate theoretical spectra (e.g., pyteomics or similar). Adding this reference would improve reproducibility."* — This is not a criticism of the paper's quality but a minor citation suggestion. Moved to Trivial weakness (point 8).

- *"The computational overhead is mentioned (2.3× training time), but a breakdown of where the extra time goes would be useful."* — This is a nice-to-have improvement, not a weakness. Moved to Nice-to-Haves.

- *The harsh critic's claim that the authors "intended to minimize I(z_s;Y)"* — This is speculative. The competitive mechanism interpretation (maximizing both I(z_c;Y) and I(z_s;Y) under the independence constraint) is a viable alternative that the paper may have intended but failed to articulate clearly. Moved to the weakness description.

- *Formatting, typo-level, and strawman criticisms* — None present in the inputs that survive the filtering rules.

## Novel Insights

The most insightful observation from the reviews is that the independence objective (conditional MI framing) and the purification objective (maximizing I(z_s;Y)) form a pair of tensions that could be productively reframed as a *competitive disentanglement* strategy. The contrastive loss on $z_c$ enforces invariance to noise interventions, while both $z_c$ and $z_s$ are pushed to predict $Y$ via separate decoders. The competition forces the model to route intervention-invariant $Y$-relevant information into $z_c$ and intervention-variant $Y$-relevant information into $z_s$. This framing, if made explicit, would reconcile the apparent contradiction in the purification loss — but the paper does not articulate it, leaving a confusing explanation in its place.

## Suggestions

1. **Fix the independence objective framing.** Either (a) explicitly state that the objective is unconditional MI $I(z_c; z_c')$ and explain why this is sufficient for the invariance goal, or (b) provide a rigorous justification for how the implemented loss approximates $I(z_c; z_c' \mid Y)$ given that each peptide is unique (and thus $Y$ is a deterministic function of the input).

2. **Rewrite the purification objective section.** Clearly explain the competitive disentanglement mechanism. If the intended logic is that maximizing $I(z_s; Y)$ under the independence constraint forces a cleaner causal/non-causal split, state this explicitly. If the implementation actually minimizes $I(z_s; Y)$, correct the text.

3. **Add multi-run statistics** (mean ± std over ≥3 seeds) for the main results (Tables 1–2) to quantify result stability.

4. **Report $\gamma$ and $\alpha$ values** in Section 3.4.1 or in the Implementation Details section.

5. **Briefly discuss the retrained-baseline discrepancies** to reassure readers that the baselines were not inadvertently weakened.

---

### Score Calibration

**Round 1 — Bracketing.** Three queries covering <3.5, 3.5–7.5, and >7.5 on related topics (de novo sequencing, causal representation learning, protein benchmarks). Retrieved anchors include weak papers scoring 2–3 (rejected), mid-range scoring 4.25–7.00 (mixed accept/reject), and strong scoring 8.0 (accept). The paper clearly outranks the <3.5 band and is not as strong as the 8.0 band, placing it in the middle band.

**Round 2 — Narrowing (4.5–7.5).** Two queries retrieved directly relevant anchors:
- *RankNovo* (5.50, Reject): Directly comparable de novo sequencing paper. CausalNovo has larger empirical gains and a more principled approach → CausalNovo is stronger.
- *Hotspot-Driven Peptide Design* (6.20, Accept): Comparable quality in different sub-area → similar tier.
- *InfoCORE* (6.50, Accept): Similar theoretical framing (InfoNCE, conditional MI). InfoCORE has cleaner theory but weaker empirics; CausalNovo has stronger results but sloppier theory → comparable.
- *Severing Spurious Correlations* (7.00, Accept): Mixed reviews (10,5,5,8). CausalNovo has more consistent empirical evidence.

**Round 1 bracket:** 5.0 – 7.0. **Round 2 narrowing:** The paper is clearly above RankNovo (5.50) and comparable to InfoCORE (6.50) and the accepted peptide design paper (6.20). **Final score: 6.5.**

**Anchors considered:**
| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| G536mmC2HL | 3.00 | R1 | Much weaker; rejected molecular method |
| IZiKBis0AA | 3.00 | R1 | Much weaker; rejected drug design |
| 8GhwePP7vA | 4.25 | R1 | Weaker causal representation learning paper |
| OGtnhKQJms | 7.00 | R1 | Stronger; more rigorous causal identifiability theory |
| 87B3zDRMjv (RankNovo) | 5.50 | R2 | Weaker; less comprehensive, smaller gains |
| jqmptcSNVG | 6.20 | R2 | Similar tier; peptide design (different task) |
| 7TOs9gjAg1 (InfoCORE) | 6.50 | R2 | Similar tier; information-theoretic debiasing |
| Bk13Qfu8Ru | 7.00 | R2 | Slightly stronger; spurious correlation mitigation (mixed reviews) |

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>