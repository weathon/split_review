Now let me run the calibration search to score this paper.Let me read some of the closest anchors and narrow the bracket:Initial bracket: **5.0–7.0**. The paper is clearly above weak papers (2.5–3.0) but has genuine methodological gaps that prevent it from reaching top-tier (8.0). Let me narrow within this range.Let me read two more targeted anchors:Now I have enough information to write the final review. Let me synthesize everything.

---

## Summary

This paper proposes **Regression-based Test-Time Adaptation (RTA)**, which trains a LightGBM decision tree offline to map CLIP logit vectors to pseudo-label cross-entropy (CE) loss, then selects the augmented views with the lowest predicted loss at test time. The key motivation is a "Ceiling TTA" analysis showing that ground-truth CE loss for view selection dramatically outperforms Shannon entropy (e.g., ViT-B/16 with 64 views: 89.0% vs. 70.6% on ImageNet). Experiments span single-label ImageNet benchmarks, 10 cross-domain datasets, and multi-label tasks, with RTA consistently exceeding prior entropy-based TTA methods.

---

## Strengths

1. **The Ceiling TTA analysis provides a compelling empirical foundation.** Tables 1–2 demonstrate that ground-truth CE-based view selection yields massive gains over entropy-based selection (e.g., RN50 on ImageNet-A: 70.9% vs. 35.7% at 64 views). This clearly establishes that a high-quality loss signal latent in the logits is exploitable, directly motivating regression-based prediction of this signal.

2. **RTA delivers consistent, broad improvements across heterogeneous benchmarks.** Table 3 shows RTA improving RN50 OOD average by +2.26% over BCA and ViT-B/16 OOD average by +0.81% over Zero; Tables 4–6 add cross-domain and multi-label gains (e.g., ViT-B/16 MSCOCO mAP: 58.95% vs. 57.52% for ML-TTA). The breadth and uniformity of these gains under two backbone architectures and three task families constitutes solid empirical evidence.

3. **Computational practicality.** The regression model requires only 1,000 high-confidence ImageNet samples for training, no gradient updates at test time, and runs LightGBM inference on logit vectors—negligible overhead relative to 64-view CLIP forward passes. This is explicitly verified in the setup (Section 5.1).

---

## Weaknesses

### Fatal
None.

### Major

- **Missing max-confidence baseline.** For training samples with confidence ≥ 0.8, the pseudo-label is the argmax class and the CE loss in Eq. (4) equals `−log(max_j softmax_j(s))`—a *deterministic*, closed-form function of the logit vector `s`. A well-trained LightGBM on inputs `s` and target `−log(max_j softmax_j(s))` will approximate this function closely, meaning view selection by smallest predicted CE loss is likely equivalent to selecting views by **highest max-softmax confidence**. The paper never tests this: simply rank the 64 augmented views by `max_j p_j` and pick the top-k. This baseline requires no regression model whatsoever. If RTA outperforms it, the regression captures something genuinely non-trivial; if not, the contribution reduces to showing that max-confidence view selection beats entropy minimization—a simpler but real finding. The Spearman correlations in Figure 3 (showing strong correlation between top logits and CE loss) and the t-SNE in Figure 2 are consistent with the trivial reading. This is the most critical experiment missing from the paper.

- **Unexplained dimensionality mismatch for cross-domain experiments.** The regression model is trained on 1000-dimensional ImageNet logit vectors (Algorithm 1, lines 6–7, class count L = 1000). Yet cross-domain tests use datasets with very different class counts: Cars (196), VOC2007 (20), Aircraft (100), UCF (101). A LightGBM model trained on 1000-dim feature vectors cannot directly accept 20- or 196-dim vectors because learned split thresholds are indexed to specific logit positions. The paper claims "the regression mapping only needs to be trained once in the initial stage, and then it can directly adapt to test instances with arbitrary distributions" (Introduction), but it never explains *how* this is achieved given the dimensionality mismatch. Either there is an undisclosed adaptation step (contradicting the "train once" claim) or a dimension-invariant encoding (e.g., sorted top-k logit values) is used but not described. The results in Table 4 are presented as if this were resolved, but the mechanism is absent.

### Minor

- **Multi-label extension is mechanically undefined.** The CE loss in Eq. (4) assumes a single ground-truth class. For multi-label classification (MSCOCO, VOC2007, NUSWIDE), pseudo-labels are multi-class and the CE formulation does not directly apply. Tables 5–6 present multi-label results without explaining what loss the regression predicts or how multi-label confident-view selection interacts with mAP scoring. The results may be valid but the method is incomplete as described.

- **Ceiling gap is unacknowledged.** RTA achieves 71.13% on ImageNet for ViT-B/16 vs. the LCE ceiling of 89.0% (Table 2, 64 views)—a gap of ~18%. The paper presents LCE as motivation and implies regression approaches it, but never acknowledges or explains this large gap. The RN50 gap is even larger (~24% on IN-A: 70.9% ceiling vs. 36.79% RTA). This does not invalidate the contribution (since RTA outperforms other label-free methods), but the narrative coherence suffers. A brief acknowledgment that the regression captures only part of the oracle signal would strengthen honesty.

### Trivial

- **Notation inconsistency in Section 4.3.** Equations (8)–(10) and Algorithm 2 use `x_i^{reg}` when the context is test-time inference; the superscript should be `x_i^{test}`. This creates confusion between the training and test-time stages.

---

## Nice-to-Haves

- A feature importance analysis for the LightGBM model would clarify whether the tree predominantly uses the top-1 logit (collapsing to max-confidence) or exploits multi-class logit structure.
- Statistical significance reporting (even approximate) for the narrow margins on ViT-B/16 (e.g., +0.24% on IN-1k over Zero) would strengthen the empirical claims.

---

## Removed Points

*These points are flagged to be removed—treat them with caution:*

- **"Free lunch" is overstated** — Removed as a minor semantic nitpick. The paper uses "free lunch" colloquially to mean no test-time gradient updates, not zero cost; this is a style criticism.

- **Ceiling gap as a "fatal" issue** — Demoted. LCE is an oracle that has access to ground-truth labels. The relevant comparison is against other label-free methods, where RTA does improve. A large gap from an oracle is expected and does not undermine the contribution.

- **Figure 5 y-axis scale misleads** — Removed as a formatting nitpick. The total accuracy variation (~0.6–0.8%) across sample counts is real and the caption is not false; this is not a substantive error.

- **Section 4.1 analysis is "trivial"** — Removed. The Spearman and t-SNE analyses are consistent with the trivial reading, but their inclusion is not a logical error; they support the method's design intent. The *missing baseline* is the substantive issue, not the motivating analysis.

- **Statistical significance as fatal** — Moved to Nice-to-Haves. Single-run evaluation without confidence intervals is standard in large-scale TTA benchmarks, so this is a norm-consistent request rather than a mandatory fix.

- **Strength: "This paper addresses an important problem"** — Removed as generic. Retained only evidence-grounded strengths.

---

## Novel Insights

The observation that a regression model trained on pseudo-labeled ImageNet logits generalizes to multiple OOD ImageNet variants and cross-domain tasks is potentially interesting—if the dimensionality mismatch is resolved and the regression is shown to exceed direct max-confidence selection. The current paper cannot confirm whether the tree captures something beyond max-probability selection, because the logit-to-CE mapping for high-confidence samples is mathematically a deterministic function of the maximum logit. Establishing that the tree exploits richer multi-class logit structure (or confirming it reduces to max-confidence) would be the genuinely novel finding worth reporting.

---

## Suggestions

1. **Add a direct max-confidence baseline**: at test time, select the top-k views by `max_j p_j` from the logit vector and compare against RTA. This experiment costs essentially nothing and directly determines whether the regression model contributes anything beyond max-probability selection.
2. **Explain or fix the cross-domain dimensionality handling**: state explicitly whether the regression uses a fixed-size sorted representation of logits, whether cross-domain evaluation keeps ImageNet class labels, or whether domain-specific retraining occurs. This is essential for reproducibility.
3. **Add one paragraph on the multi-label regression target**: clarify what CE loss is predicted in multi-label scenarios—e.g., whether the regression is applied with single-label CE and the view selection is then reused unchanged, or whether the multi-label problem is adapted.

---

## Score and Decision

**Calibration anchors (all rounds):**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| pdzHpQbGrn.md (Active TTA Prompt Learning) | 2.50 | R1 weak | Far weaker; incomplete contribution |
| HfJxXbXlYJ.md (LLM2CLIP) | 3.00 | R1 weak | Weaker; rejected |
| ZaudLwn0Hm.md (Prototypical few-shot CLIP) | 2.50 | R1 weak | Far weaker |
| j1FLTvgyAh.md (MVMP) | 2.50 | R1 weak | Far weaker |
| kIP0duasBb.md (RLCF) | 6.67 | R1 mid | Accepted; broader task scope but similarly complex; RTA's methodology gaps are comparable |
| yD2JMeKumt.md (DOTA) | 6.00 | R1 mid | Rejected at 6.0; has serious evaluation gaps. RTA's gaps are different but comparable in severity |
| 75PhjtbBdr.md (ML-TTA) | 6.25 | R1 mid | Accepted; directly related work cited by RTA. RTA's empirical scope is broader but has larger methodology gaps |
| Rc3RP9OoEJ.md (InCPL) | 5.00 | R1 mid | Rejected at 5.0; simpler contribution, weaker baselines |
| WyEdX2R4er.md (Visual Data-Type VLMs) | 8.00 | R1 strong | Far stronger; novel benchmark + 39-model analysis |
| 5Ca9sSzuDp.md (CLIP Image Decomp) | 8.00 | R1 strong | Far stronger; fundamental analysis |
| TPZRq4FALB.md (READ multi-modal TTA) | 8.00 | R1 strong | Stronger; theoretical framework + strong empirical |
| iGbuc9ekKK.md (DuoDuo CLIP 3D) | 5.75 | R2 | Different domain; similar quality level |
| z7PhIgVmZU.md (BAT-CLIP) | 5.50 | R2 | Rejected; bimodal TTA for CLIP corruptions. Similar scope, similar gaps |
| YeSxbRrDRl.md (Dist Loss regression) | 6.67 | R2 | Different domain; regression loss method accepted |
| 7iuFxx9Ccx.md (SlimTTT) | 6.00 | R2 | Rejected; resource-adaptive TTT |
| 4wk2eOKGvh.md (TTE linear mode) | 6.50 | R2 | Accepted; TTA ensemble, no major gaps |
| 9w3iw8wDuE.md (DeYO) | 7.00 | R2 | Accepted; stronger theoretical motivation, clear confidence metric |

**Round 1 bracket: 5.0–7.0**

**Round 2 narrowing:** The two most comparable accepted papers are ML-TTA (6.25) and RLCF (6.67). DOTA was rejected at 6.0 despite showing some gains, largely due to unresolved methodological questions. BAT-CLIP was rejected at 5.50 with methodological gaps comparable to RTA's.

RTA is **better than BAT-CLIP** (broader benchmarks, more consistent gains), **comparable to DOTA** (both have an unexplained core mechanism), and **slightly weaker than ML-TTA** (which has a complete and explained methodology). The missing max-confidence baseline is the distinguishing issue: if the regression reduces to max-confidence, the claimed contribution disappears. This is not speculation—it follows mathematically from the training target (Eq. 4) applied to high-confidence samples. This places the paper below ML-TTA's quality level and closer to 5.5.

**Final score: 5.5** — Borderline reject. The empirical contributions are real, the motivation is sound, and the paper is clearly written. However, the two major gaps (missing max-confidence baseline; unexplained cross-domain dimensionality handling) must be resolved before acceptance.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>