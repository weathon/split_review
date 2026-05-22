## Summary

This paper addresses language-based audio retrieval using a dual-encoder architecture with three proposed enhancements applied to the Clotho dataset: (1) soft-label distillation from an ensemble of pretrained retrieval teachers, (2) LLM-driven caption augmentation via back-translation and caption mixing, and (3) cluster-guided auxiliary classification heads. The best single model reaches mAP@16 of 46.6, and a weighted ensemble attains 48.83 on the Clotho development test split.

---

## Strengths

**S1: Soft-label distillation produces a clear, large, and consistent improvement over standard contrastive learning.** Table 2 (SID 1 → SID 2) shows that adding distillation raises mAP@16 by 3.5–5.8 points across all three backbones (PaSST: 42.08→46.62; EAT: 40.41→45.35; BEATs: 38.12→43.89). This is the largest single performance jump in the paper and provides direct evidence that modeling non-binary correspondences via soft targets is beneficial for audio retrieval.

**S2: Thorough and well-structured ablation across three backbones and five system configurations.** Table 1 defines five System IDs (SID 1–5) that systematically add distillation, augmentation, and cluster guidance. Table 2 reports all corresponding metrics for three backbones, enabling clean attribution of each component's contribution. The ablation design itself is methodologically sound.

**S3: A weighted ensemble of the proposed systems achieves a competitive mAP@16 of 48.83 on Clotho.** The ensemble strategy (E1–E4 in Table 2) combines models from different SIDs and backbones with weights tuned on the validation set, and demonstrates that the models have complementary strengths despite the mixed individual-component results.

---

## Weaknesses

### Major

**M1: The two novel components (LLM augmentation and cluster-guided classification) do not show reliable, consistent improvement over the distillation-only baseline, undermining the paper's core claims.** The paper lists three contributions in the abstract and introduction, but the ablation evidence does not support the latter two as effective:

- **Augmentation (SID 3 vs. SID 2):** For PaSST (the best backbone), mAP@16 *decreases* from 46.62 to 46.41 when augmentation is added. For EAT it improves (45.35→46.05, +0.70) and for BEATs it improves (43.89→44.66, +0.77). The largest gain is under one point, and the best backbone is harmed.
- **Cluster guidance (SID 4/5 vs. SID 3):** For PaSST, SID 4/5 (46.39/46.50) are essentially flat vs. SID 3 (46.41). For EAT, SID 4/5 (45.34/45.34) are below SID 3 (46.05). For BEATs, SID 4 (44.58) is near SID 3 (44.66) while SID 5 (43.88) is lower.

The paper's abstract states these three techniques "jointly improve robustness," but the data show that the distillation-only configuration (SID 2) is competitive with or better than the full pipeline for the strongest backbone, and the additional components produce at best marginal and inconsistent gains. The conclusion acknowledges "mixed single-model gains from cluster supervision," which is an understatement — the evidence does not support augmentation and cluster guidance as effective contributions.

**M2: The cluster-guided auxiliary classification is conceptually misaligned with the retrieval objective and is not analyzed.** Clusters are derived from captions only (via BERTopic on caption embeddings). The auxiliary loss then forces audio encoders to predict the caption-cluster label of their paired caption. Since audio may contain sounds not described in the caption, and captions may describe sounds not present in the audio, forcing this alignment can harm representations. The reported results (flat to negative) are consistent with this concern. The paper provides no analysis of cluster quality, number of clusters, stability, outlier handling (beyond a one-sentence mention), or sensitivity to the loss weight λ₂=0.05, making it impossible to diagnose whether the method fails due to poor cluster quality or a fundamental design issue.

**M3: The soft-label distillation technique, which accounts for nearly all reported gains, is a direct adoption from prior work with no modification.** Section 2.2 explicitly states "we adopted a distillation loss approach from the top-ranked DCASE 2024 Task 8 system (Primus et al., 2024)." While applying this to audio retrieval is a reasonable engineering contribution, the paper presents it as a novel contribution alongside the other two components, which fail experimentally. The paper's headline empirical improvement (SID 1→SID 2) is therefore attributable to prior work, and the two proposed novel components do not advance the state of the art.

### Minor

**m1: No statistical significance or variance is reported for any experiment.** All numbers in Table 2 are single-point estimates with no confidence intervals, standard deviations, or multiple random seeds. Given that the differences among SID 3/4/5 are within fractions of a point (e.g., PaSST mAP@16: 46.41, 46.39, 46.50), it is impossible to determine whether these are real differences or training noise. This does not invalidate the paper (single-run evaluation is common in this area), but it makes the comparison among the paper's own proposed variants uninterpretable.

**m2: The claim in the abstract that "ablations indicate consistent improvements under high correspondence ambiguity" is not supported by evidence in the available paper text.** No analysis breaking down performance by correspondence ambiguity level is presented, making this claim speculative.

**m3: The batch sizes vary substantially across backbones (64 for PaSST, 24 for EAT, 16 for BEATs), which is a known confound for contrastive learning since batch size directly affects the number of negative pairs.** While this is acknowledged as a computational constraint, the paper does not discuss whether backbone performance differences could partly reflect this confound rather than encoder quality.

### Trivial

None.

---

## Nice-to-Haves

- Report results with variance (at least 3 random seeds) for the critical SID comparisons.
- Include an ablation of cluster guidance *without* augmentation (SID 2 + cluster) to isolate its effect.
- Provide a sensitivity analysis on the cluster loss weight λ₂.
- Analyze cluster quality (number of clusters, stability, outlier fraction) to help diagnose why the auxiliary loss does not help.

---

## Removed Points

- *"No missing related works"* — removed per rules (cannot verify from external sources).
- *"Formatting and presentation nitpicks"* — removed per rules (parser artifacts).
- *"SID 2 gets the highest ensemble weights"* — removed because Table 3 shows this is not uniformly true; SID 4 PaSST often receives higher or comparable weights in some ensemble configurations.
- *"Reproducibility concern about proprietary LLM (GPT-4o)"* — removed per hard rules (the paper cites GPT-4o, which exists and is released; the paper also acknowledges this limitation explicitly in the conclusion).
- *"Strength that augmentation helps"* — partially removed from core strengths because it only helps 2/3 backbones and harms the best one; mentioned in minor context instead.
- *"Strength about addressing an important problem"* — removed as generic.
- *"Cluster guidance ablation missing without augmentation"* — moved to Nice-to-Haves (a genuine missing experiment, but not fatal since SID 2 vs SID 3 already shows augmentation's independent effect is also weak).

---

## Novel Insights

None beyond the paper's own contributions. The reviews surface no observation about the method's behavior that the paper itself does not discuss.

---

## Suggestions

1. **Reframe the paper's contributions honestly.** The strongest empirical finding is that soft-label distillation (from prior work) substantially improves dual-encoder audio retrieval. The augmentation and cluster guidance components should be presented as explorations with mixed results, not as validated contributions.
2. **Add variance estimates** for at least the main SID comparisons (SID 2 vs. SID 3 vs. SID 4/5) to enable readers to assess whether the small differences are meaningful.
3. **Either provide evidence for the "high correspondence ambiguity" claim** (e.g., by partitioning the test set by caption diversity) or remove it from the abstract.
4. **Analyze cluster quality** (number of clusters, stability, outlier handling) and include a sweep over λ₂ to determine whether the cluster guidance approach is fundamentally flawed or simply poorly tuned.
5. **Replace GPT-4o with an open-weight LLM** (as the paper acknowledges in future work) to make the augmentation pipeline fully reproducible, especially if "reproducible" is claimed as a contribution.

---

## Score and Decision

### Calibration Anchors

| Anchor Path | Avg Score | Comparison to This Paper |
|---|---|---|
| `l4fMj4Vnly.md` (ADIFF) | 7.50 | Much stronger: proposes a new task, creates datasets, well-supported claims. |
| `TeVAZXr3yv.md` (MMAU) | 7.50 | Much stronger: comprehensive benchmark, extensive evaluation. |
| `nBZBPXdJlC.md` (LTU) | 7.00 | Stronger: more novel contribution (first audio LLM for general audio), thorough ablations. |
| `nplYdpc1Pm.md` (TeminAL) | 4.75 | Similar quality: has a working core idea but limited novelty, insufficient evidence for contributions, similar evaluation concerns. |
| `rAX55lDjtt.md` (APT) | 4.60 | Comparable: mixed evaluation results, some claims not fully supported, reviewer scores span 1–8. |
| `burz7mU0YD.md` (OpenMU) | 3.50 | Slightly weaker: less working evidence, more unfounded claims. |
| `gpKEDj9Dgg.md` (ASR+LLM) | 2.00 | Much weaker: incomplete paper. |

### Rationale

The paper has one well-supported finding (distillation helps audio retrieval, replicating prior work). The two proposed novel components — which the paper presents as core contributions — show no reliable improvement and in some configurations actively harm performance. The paper is honestly reported in the conclusion but the abstract and introduction overstate the contributions. The evaluation is competent in scope (3 backbones, 5 system configurations) but lacks variance reporting for the critical comparisons. The paper is not fatally flawed (the distillation component is reproduced correctly and yields useful results for the community), but its claimed novelty is substantially weaker than advertised.

**Score: 4.0**

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>