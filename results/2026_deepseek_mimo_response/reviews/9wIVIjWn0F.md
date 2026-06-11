Now I have sufficient calibration data. Let me finalize the review.

## Summary
This paper proposes Regression-based Test-time Adaptation (RTA) for CLIP-based vision-language models. The key idea is to train a lightweight LightGBM regression model offline to predict cross-entropy loss from view logits, then use these predicted losses for confident view selection during test-time augmentation. The method is evaluated on single-label (ImageNet variants), multi-label (MSCOCO, VOC2007, NUSWIDE), and cross-domain benchmarks, achieving state-of-the-art results across most settings.

## Strengths
- **Novel and well-motivated oracle analysis (Tables 1-2):** The paper convincingly demonstrates that label cross-entropy loss dramatically outperforms entropy for view selection — e.g., 90.2% vs. 64.3% on ImageNet-A with ViT-B/16 and 64 views (Table 2). This "Ceiling TTA" analysis is a genuinely useful empirical finding.
- **Consistent SOTA across diverse settings (Tables 3-6):** RTA achieves best average accuracy on ImageNet variants for both RN50 (51.85%, +1.91% over BCA) and ViT-B/16 (66.90%, +0.66% over Zero). Multi-label mAP improvements are substantial (e.g., +1.67% on MSCOCO, +1.58% on VOC2007, +3.0% on NUSWIDE for RN50 over ML-TTA). Cross-domain accuracy improves for RN50 (61.78% vs. 61.44% BCA) and ViT-B/16 (68.70% vs. 68.59% BCA).
- **Practical efficiency:** The regression model is a lightweight LightGBM tree (max depth 5, 16 leaves) trained once on only 1,000 samples, requiring no per-instance updates or heavy inference at test time.
- **Novel conceptual reframing of TTA view selection:** Rather than estimating confidence from a single test instance's probability distribution (as in all prior entropy-based TTA methods), RTA learns a distribution-agnostic mapping from logits to loss using diverse offline data. This is a genuinely different information source, supported by Spearman rank correlation evidence (Figure 3).

## Weaknesses

### Fatal
None

### Major
- **Multi-label adaptation is completely undocumented.** The method is described entirely in terms of single-label softmax cross-entropy (Eq. 4) and argmin-based view selection (Eq. 10). Tables 5-6 present multi-label results using mAP, but the paper provides zero explanation of how the method handles multi-label classification — different loss functions (BCE vs. CE), different confidence measures, different ensemble strategies. This is not a minor implementation detail; it changes the meaning of the core algorithm. While the multi-label improvements are numerically substantial (1-3pp gains over ML-TTA), a substantial portion of the experimental section is unverifiable as written.
- **ImageVal-12k provenance is unspecified.** The regression model is trained on "ImageVal-12k" (Section 5.1), but the paper never defines what this dataset is, how it was constructed, or whether it has class/image overlap with the ImageNet evaluation benchmarks. This is a substantive documentation gap for a method whose generalization claim depends on training-test separation.
- **Oracle-to-actual gap is unacknowledged.** The paper's strongest motivation (Tables 1-2) shows oracle LCE achieves 90.2% on ImageNet-A with ViT-B/16. RTA achieves 65.65% — a 24.55pp gap, capturing only ~37% of the potential improvement. The paper never analyzes where or why the regression mapping fails to capture most of this signal, creating a misleading impression where spectacular oracle numbers motivate a method that delivers much more modest actual improvements.

### Minor
- **No variance or significance reporting.** None of the results in Tables 3-6 include standard deviations or confidence intervals. For improvements of 0.1-1.5% over strong baselines (e.g., ViT-B/16 cross-domain: RTA 68.70% vs. BCA 68.59%), this makes it impossible to assess whether differences are meaningful.
- **Cross-domain ViT-B/16 results are marginal.** RTA achieves 68.70% vs. BCA's 68.59% (0.11% difference) on 10 cross-domain datasets, with BCA outperforming RTA on 5 of 10 individual datasets (Pets, Flowers, DTD, EuroSAT, Caltech). The paper presents this as a clean win without acknowledging the mixed picture.
- **Train-test distribution mismatch not analyzed.** The regression model is trained on original images (not augmented views) per Section 4.2, but at test time it predicts losses for augmented views. An ablation comparing regression trained on augmented vs. original images would address a natural concern.
- **"Free lunch" framing is overstated.** The method requires offline training on curated data (ImageVal-12k with confidence threshold ≥ 0.8), training LightGBM to convergence for 100 rounds. The abstract's "negligible additional cost" refers only to inference time.

### Trivial
- **Duplicate TDA row in Table 4 (ViT-B/16).** Two rows labeled "TDA [CVPR 2024]" with different numbers appear (lines 379-380), likely a data or parsing error.

## Nice-to-Haves
- Report regression model quality metrics (MSE between predicted and actual loss on held-out data, selection accuracy vs. oracle).
- Clarify whether separate regression models are trained per CLIP backbone (RN50 vs. ViT-B/16), which matters for the "train once" claim.
- Add a simple baseline: using CLIP's max softmax probability for view selection, to isolate how much improvement comes from regression specifically.

## Removed Points
These points are flagged to be removed, treat them with caution.
- Harsh critic's concern about t-SNE being misleading: The paper acknowledges t-SNE is qualitative and supplements it with Spearman rank correlation (Figure 3). The paper does not over-rely on t-SNE alone, so this criticism is partially addressed.
- Harsh critic's criticism about "free lunch" overstated: While partially valid, the paper's claim of "negligable additional cost" in the abstract clearly refers to test-time overhead. This is marketing language, not a substantive error.

## Novel Insights
The paper's most genuinely novel observation is the dramatic oracle gap between H_LCE and H_SE for view selection (Tables 1-2), revealing that entropy is a substantially suboptimal criterion for confident view selection in TTA. The finding that a lightweight regression mapping from logits to loss can replace entropy-based view selection offers a new direction for TTA research.

## Suggestions
- Add a section explaining the multi-label adaptation, or remove multi-label results and focus on the well-specified single-label setting.
- Specify ImageVal-12k provenance and verify no overlap with evaluation benchmarks.
- Add analysis of the oracle-to-actual gap: what fraction of oracle top-k views does the regression model correctly identify? What is the MSE of predicted vs. actual loss?
- Report error bars or standard deviations across runs.

## Calibration Report

### Anchors Retrieved

**Round 1 (bracketing):**
| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| pdzHpQbGrn.md | 2.50 | 1 | Active test-time prompt learning — much weaker than RTA |
| ZaudLwn0Hm.md | 2.50 | 1 | Few-shot VLM adaptation — much weaker |
| HfJxXbXlYJ.md | 3.00 | 1 | LLM2CLIP — weaker methodology |
| j1FLTvgyAh.md | 2.50 | 1 | Multi-vision multi-prompt — weaker |
| 75PhjtbBdr.md | 6.25 | 1 | ML-TTA — similar scope, RTA improves on its benchmarks |
| kIP0duasBb.md | 6.67 | 1 | RLCF — comparable scope and quality |
| KNtcoAM5Gy.md | 5.50 | 1 | BaFTA — weaker experimental validation |
| yD2JMeKumt.md | 6.00 | 1 | DOTA — many experimental issues |
| uAFHCZRmXk.md | 8.00 | 1 | READ — higher quality but different multi-modal focus |
| 5Ca9sSzuDp.md | 8.00 | 1 | Interpreting CLIP — analysis paper, not comparable |
| 3i13Gev2hV.md | 8.00 | 1 | Hyperbolic VL — not comparable |
| WyEdX2R4er.md | 8.00 | 1 | Visual data-type understanding — not comparable |

**Round 2 (narrowing):**
| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| 7iuFxx9Ccx.md | 6.00 | 2 | SlimTTT — resource-efficient TTT, weaker |
| 3Z2flzXzBY.md | 6.40 | 2 | PASLE — selective label enhancement for TTA |
| 5sU32OCxgZ.md | 6.00 | 2 | TTVD — geometric TTA framework |
| xqxG5WogN6.md | 5.67 | 2 | DART — distribution shift-aware TTA, rejected |
| iylpeTI0Ql.md | 6.00 | 2 | Noisy TTA in VLMs — new task setting |
| TD3SGJfBC7.md | 6.25 | 2 | Learning to adapt frozen CLIP |
| 4wk2eOKGvh.md | 6.50 | 2 | TTE — test-time ensemble |
| 9bMZ29SPVx.md | 7.50 | 2 | CLIP data selection — different task |
| b20VK2GnSs.md | 7.00 | 2 | Concept drift in MLLMs — different scope |
| fCeUoDr9Tq.md | 7.50 | 2 | RoboShot — zero-shot robustification |
| 5BCFlnfE1g.md | 6.75 | 2 | MetaCLIP — CLIP data curation |

### Bracketing and Score Derivation

**Round 1 bracket: 6.0–7.0.** RTA is clearly above the rejected weak anchors (2.5–3.0) and above BaFTA/DOTA (5.5–6.0). It's comparable to ML-TTA (6.25) and RLCF (6.67), both accepted. It's below the 7.5–8.0 papers which introduce new task settings, theoretical contributions, or multi-modal analysis.

**Round 2 narrowing: 6.0–7.0.** Within this bracket:
- RTA is clearly above DOTA (6.00, rejected, many experimental issues), TTVD (6.00, accepted but narrow scope), and SlimTTT (6.00).
- RTA is comparable to or slightly above ML-TTA (6.25) since RTA outperforms ML-TTA on all shared benchmarks, though ML-TTA's multi-label extension is well-documented.
- RTA is comparable to RLCF (6.67) — RTA has more comprehensive benchmarks but the multi-label documentation gap is a weakness RLCF doesn't have.
- RTA is below b20VK2GnSs (7.00) which introduces a new theoretical framework and benchmark.

**Final score: 6.5.** RTA has genuine novelty (regression-based view selection), strong and consistent empirical results across single-label, multi-label, and cross-domain benchmarks, and practical efficiency. However, the undocumented multi-label adaptation, unspecified ImageVal-12k provenance, and unacknowledged oracle-to-actual gap are significant omissions that prevent a higher score. The paper sits above the 6.0–6.25 papers (which it outperforms empirically) and below the 6.75+ papers (which have fewer documentation gaps).

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>