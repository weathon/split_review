Now I'll carefully verify the key reviewer claims against the paper text and write the final review.

---

## Summary

CaPT (CLIP as a Prior Teacher) is a semi-supervised learning framework that integrates an adapter-tuned CLIP model with a fully fine-tuned unimodal network through asymmetric co-training. The method generates co-pseudo labels by fusing predictions from both branches using entropy-based adaptive weighting, then uses these to supervise strong augmentations. The approach delivers substantial performance improvements in extreme low-label regimes, outperforming prior SSL methods by up to 21.38% on CIFAR-100 with one label per class.

## Strengths

- **Exceptional performance in extreme low-label regimes**: Table 3 demonstrates that CaPT achieves 82.51% on CIFAR-100 with 1 label per class, surpassing the second-best method (RegMixMatch at 60.49%) by 21.38 percentage points. Similar strong gains are seen on CIFAR-10 (96.37%) and EuroSAT (96.33%). These are genuinely large improvements that demonstrate the practical value of integrating a VLM prior into SSL.

- **Efficient VLM integration**: Table 4 shows that CaPT consumes 5050 MiB of GPU memory and 0.1044 sec/iter on CIFAR-100 with 2 labels, which is only slightly above FreeMatch (4676 MiB, 0.0939 sec) and substantially below RegMixMatch (6578 MiB, 0.1484 sec), while achieving much higher accuracy (84.83% vs 78.60% and 80.74%). The design choices—adapter tuning instead of full fine-tuning, feature-level Mixup instead of input-level augmentation—are pragmatically effective.

- **Comprehensive cross-dataset validation**: The method is evaluated across standard benchmarks (CIFAR-100, STL10, EuroSAT), large-scale ImageNet, extreme 1-label regimes, and 6 fine-grained datasets (Table 5). Performance is consistently strong with low variance across seeds (Table 1), and the paper honestly acknowledges the FGVC-Aircraft limitation where CaPT (50.12%) trails FreeMatch (51.43%).

- **Well-structured ablation study**: Table 6 systematically validates each component—adapter tuning (CaPT-Ada, -16.40%), debiasing (CaPT-Deb, -12.73% on EuroSAT), unidirectional vs bidirectional flow (CaPT-Uni, -0.88%), single-branch variants, feature augmentation, and entropy weighting. The entropy-based weighting mechanism (Equations 11-13) is shown to consistently beat equal weighting.

## Weaknesses

### Fatal
None.

### Major

- **Overstated framing of "breaking label dependency" and "pattern-homogeneity"**: The paper's two core narrative claims—that SSL has a fundamental structural dependency on labeled data quality, and that asymmetric modalities break pattern-homogeneity—are not adequately supported by the evidence. The "breaking label dependency" claim is essentially describing a well-known transfer learning phenomenon: using a strong external prior (CLIP) helps when labeled data is scarce. The performance gains in the 1-label regime (Section 4.3, Table 3) are largely attributable to CLIP's zero-shot capabilities rather than a novel structural change to SSL mechanics. Similarly, the "pattern-homogeneity" claim rests solely on qualitative attention map comparisons in Figure 3 (a rooster example where CLIP attends to the comb while unimodal ViTs attend to the eye/beak). The paper relegates quantitative validation to Appendix B (cited in footnote 1). Without controlled experiments—such as measuring representational divergence quantitatively, or co-training two vision models with different objectives—the paper cannot substantiate that gains come specifically from asymmetric modalities versus simply from using two models with different pre-training histories.

- **Modest contribution of the bidirectional co-training mechanism**: The CaPT-Uni ablation in Table 6 isolates the co-training contribution. Removing the bidirectional exchange causes only a 0.88% drop on CIFAR-100 and 1.49% drop on EuroSAT. If the mutual learning between branches were the primary algorithmic innovation (as emphasized in the paper's framing—Contribution 2, CLS comparison), these drops should be larger. The dominant performance drivers are CLIP's prior quality and adapter tuning (as shown by CaPT-Ada at -16.40% and CaPT-Deb at -12.73%). The co-training design stabilizes training but contributes less than the narrative suggests.

### Minor

- **Theoretical bound is limited to a toy model**: Theorem 1.1 derives a pseudo-label error bound for a Gaussian mixture model with nearest-prototype classification. While mathematically valid (Equation 1), the connection to actual deep SSL training with ViTs and co-training is thin. The bound formalizes an intuitive relationship—poor prototypes or few labels increase pseudo-label error—that is already visually apparent from Figure 1a. It does not reveal a novel structural property unique to the SSL mechanisms in CaPT.

- **No quantitative measure of cross-modal complementarity**: The paper asserts that CLIP's textual grounding produces "genuinely different representations" that enrich co-training. While Figure 3 provides qualitative evidence of divergent attention patterns, no quantitative analysis (e.g., CKA, representational similarity, or mutual information) is presented in the main text to back this claim. Appendix B is referenced for these experiments.

### Trivial
None.

## Nice-to-Haves

- The paper would be stronger with a reframing around "leveraging VLM priors in SSL" rather than "breaking label dependency." The method's actual novelty is its portable integration pipeline (adapter-tuned CLIP + unimodal network + entropy-weighted co-pseudo labels), not a resolution of a fundamental SSL limitation.
- A quantitative ablation comparing (a) co-training two vision models with different pre-training objectives versus (b) CaPT's asymmetric design would clarify whether cross-modality is essential or whether model diversity suffices.
- Per-sample variance across seeds is shown in Table 1 but without statistical testing. Given the large effect sizes, this is unlikely to change conclusions, but formal significance testing would strengthen rigor.

## Removed Points

- **"The ablation should co-train two vision models with different objectives" as a major flaw**: This is a nice-to-have validation experiment that would strengthen the narrative but is not required to validate the paper's practical results. The method works regardless of whether the specific "asymmetric modalities" explanation is the only causal factor. **Demoted to Nice-to-Have.**
- **"The theoretical bound formalizes well-known intuition" as a major flaw**: The bound is presented in the Introduction as motivation, not as the paper's core contribution. The method and experiments stand on their own. **Demoted to Minor.**
- **"Efficiency comparison is not apples-to-apples since adapter-tuned CLIP is parameter-efficient by design"**: The comparison is against FreeMatch (unimodal, fully fine-tuned) and RegMixMatch (unimodal, fully fine-tuned). The fact that CaPT achieves strong results with less overhead than RegMixMatch is still a valid empirical observation, even if part of the advantage comes from the adapter design choice. **Removed—this is a design choice, not a flaw.**
- **"The entropy-based weighting uses batch-level aggregate entropy rather than per-sample confidence" as a concern**: This is an unusual but not incorrect design choice; it is computationally efficient and the ablation (equal-weighting baseline) shows it beats static weights. **Removed—valid design choice with empirical support.**
- **"CLS comparison is not deeply engaged"**: The paper references CLS (Yao et al., 2022) and explains how CaPT differs (asymmetric-modalities vs. symmetric co-training). Engaging more deeply with CLS's results would be nice but is not a core requirement. Removed as style/nit.
- **"Missing statistical tests" as a weakness**: The paper reports variance across seeds and the effect sizes are large. This is standard in SSL literature. **Removed as nitpick per hard rules.**

## Novel Insights

The harsh critic correctly identifies that the gap between the paper's methodological narrative ("breaking label dependency through asymmetric co-training") and what the ablation studies actually validate (CLIP prior + adapter tuning are the main performance drivers, co-training adds modest stabilization) is a genuine framing issue. However, this framing gap does not invalidate the results. The CaPT pipeline is practically useful: it shows that a small adapter on CLIP, combined with a standard SSL backbone and simple entropy-weighted pseudo-label fusion, can deliver orders-of-magnitude better results in 1-label regimes than any existing SSL method. The insight that a frozen VLM with lightweight adaptation can serve as a reliable pseudo-label source in regimes where conventional SSL collapses is the paper's real contribution—even if the narrative wraps it in more structural language than warranted.

## Suggestions

1. Rephrase theoretical and framing claims to emphasize "leveraging VLM priors for SSL under extreme label scarcity" rather than "breaking fundamental limitations of SSL."
2. Add a quantitative measure (e.g., CKA or linear probe probeability) comparing representations from the CLIP branch vs. the unimodal branch to support the cross-modal complementarity claim in the main text.
3. Conduct or reference an ablation where two vision models with different pre-training (e.g., MAE vs. supervised ViT) co-train to isolate whether modality asymmetry vs. model diversity drives the effect.

## Score and Decision

**Round 1 — Bracketing:**

| Anchor | Avg Score | Comparison |
|---|---|---|
| FwkYeLovHk (CLIP weak-to-strong) | 3.33 | Much weaker—limited experiments, methodological confusion |
| 97D725GJtQ (SemiCLIP) | 5.80 | Weaker—domain-specific SSL for CLIP, limited novelty, fewer datasets |
| dnqPvUjyRI (SemiReward) | 6.00 | Weaker—pluggable reward model with marginal gains, less comprehensive evaluation |
| 3i13Gev2hV (Compositional Entailment) | 8.00 | Stronger—theoretical depth with hyperbolic geometry, fully novel methodology |

Round 1 bracket: **5.5–7.5**. This paper is clearly stronger than SemiReward (6.00) with far more impressive empirical gains and broader evaluation, but the novelty framing concerns and limited theoretical contribution prevent a top-band score.

**Round 2 — Narrowing:**

| Anchor | Avg Score | Comparison |
|---|---|---|
| zBgiCWCxJB (SSOLE) | 6.75 | CaPT has stronger empirical results (21% gains vs modest SSL benchmarks) but SSOLE has deeper theory (orthogonal embedding with non-asymptotic bounds). Both have theory+experiments structure; CaPT's experiments are more compelling. |
| Bo6GpQ3B9a (Out-of-Domain SSL) | 7.00 | More rigorous theoretical framework (DRO, PAC bounds for Gaussian mixtures) but weaker experiments on fewer datasets. CaPT reverses this trade-off: stronger experiments, weaker theory. |
| 1rgMkDWfYV (CLIPSelector) | 4.50 | Significantly weaker—suboptimal baselines, poor writing, novelty concerns. Useful as a lower bound for CLIP+SSL papers. |

**Positioning**: CaPT sits above SSOLE (6.75) on the strength of substantially more impressive empirical results (21% CIFAR-100 improvement, ImageNet scaling, 6 fine-grained datasets). It is broadly comparable to Out-of-Domain SSL (7.00) but on a different axis—CaPT's experiments are superior while its theory is shallower. The framing inflation ("breaking label dependency") is a real concern but does not invalidate the results, which speak for themselves. The modest co-training contribution (CaPT-Uni: -0.88%) prevents a higher score.

**Final score: 7.0**. The paper has strong empirical results that meaningfully advance SSL in extreme low-label regimes, well-structured ablations, and efficient design, but overstates its novelty narrative relative to what the evidence supports.

MY FINAL SCORE: <score>7</score>
MY FINAL DECISION: <decision>Accept</decision>