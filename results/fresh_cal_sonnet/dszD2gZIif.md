Now I have a thorough understanding of the paper. Let me run calibration searches to properly score it.Let me read some of the mid-range anchors to better calibrate:Round 1 bracket: **4–6**. Now let me narrow with focused queries in that range.Now I have enough to write the final review. Let me compile everything.

---

## Summary

Swin4TS adapts two core designs from the Swin Transformer — local windowed attention and hierarchical downscaling — to long-term time series forecasting (LTSF). The paper proposes both a channel-independent (CI) and channel-dependent (CD) variant, claims linear computational complexity O(ML) in both sequence length and channel count, and reports state-of-the-art performance on 8 benchmark datasets. The central hypothesis is that the structural similarity between image patches and time patches justifies direct transfer of ViT architectures to time series.

---

## Strengths

1. **Linear complexity O(ML) in both L and M, verified in Table 4.** The paper correctly derives that restricting attention to fixed-size windows reduces complexity from O(L²) to O(L), and extends this to both CI and CD variants (Section 5). Table 4 provides concrete inference-time and memory measurements on the Electricity dataset, confirming the practical efficiency advantage over PatchTST and Crossformer at scale.

2. **Meaningful performance improvements on key benchmarks.** Table 1 documents a 15.8% MSE improvement on ILI (1.967→1.657) and 10.3% on Traffic (0.397→0.356), with consistent best-or-second-best results across all 8 datasets. These are the strongest quantitative evidence for the method's effectiveness, though confidence is limited by aggregation (see Weaknesses).

3. **Ablation study confirms the role of both core components.** Table 3 shows that removing shift-window attention or the hierarchical design individually—or both—increases average MSE by 3.2% on ETTm1 and 2.7% on ETTm2, providing direct evidence that these two Swin-derived mechanisms each contribute to performance.

4. **Interpretable attention visualizations.** Figures 5 and 6 qualitatively demonstrate that local attention captures periodicity while global attention detects trend anomalies on ETTh1. Figure 5 shows cross-channel correlations matching visually similar channel time series—this supports the CD variant's design rationale at a qualitative level.

---

## Weaknesses

### Fatal
None.

### Major

- **Non-standard aggregated evaluation obscures per-horizon performance.** Table 1's caption reads "All the results are averaged from 4 different prediction lengths." This directly contradicts the LTSF community's standard of reporting separate results for T ∈ {96, 192, 336, 720}. Averaging can mask degradation at specific horizons (e.g., if Swin4TS is strong at T=96 but weak at T=720, the average still appears favorable). The headline claims—"15.8% improvement on ILI", "10.3% on Traffic"—are computed on aggregated numbers and cannot be compared to baselines' per-horizon results published in the literature. This does not invalidate the method but does substantially limit confidence in the SOTA framing, since the numbers are structurally incompatible with how competing papers report results.

- **Asymmetric variant selection inflates the apparent system performance.** In Tables 1 and 2, the best-performing of Swin4TS/CI and Swin4TS/CD is bolded per dataset, effectively presenting the best-of-two-model result against baselines that each use a single fixed strategy. The paper acknowledges this as "these two variants complement each other" (line 155), but it does not clearly characterize this as a two-model comparison. On Traffic and Electricity, Swin4TS/CD is "significantly inferior" to Swin4TS/CI (stated explicitly in Section 4.2), confirming the two variants are not interchangeable components of a unified system. A fair comparison would separately evaluate each variant, clearly labeled, against CI and CD baselines.

### Minor

- **Ablation coverage is narrow.** Table 3 covers only Swin4TS/CD on ETTm1 and ETTm2 (2 of 8 datasets, one variant, averaged horizons). Since the shift-window attention and hierarchical design are the two claimed architectural innovations, their contribution should be verified more broadly, particularly on datasets where Swin4TS/CI excels (e.g., Traffic, Electricity). The current ablation cannot rule out that the gains on those datasets come from the CI strategy or the longer lookback window alone.

- **CD prediction head design is underspecified.** Section 3.2, line 117, states: "When processing long multi-variable sequences for prediction, the design of last Linear layer as CI strategy may not be a good choice." The paper flags this as a problem but does not state what prediction head is actually used for Swin4TS/CD. This is a gap in method specification that affects reproducibility of the CD variant.

- **TNT4TS mentioned in the conclusion without results.** Section 6 introduces TNT4TS as a parallel architecture "designed to further confirm this point," but no experimental results are provided. The mention adds no evidence and slightly inflates the scope of the paper's cross-domain claim beyond what is actually demonstrated.

### Trivial

- **O(L) complexity claim relies on fixed N and P.** Section 3.2 states "it actually is O(L) due to that N and P are fixed within each window." This is correct under that assumption, and the paper states the assumption explicitly, but it should note that if a practitioner scales N or P with L (e.g., to maintain coverage over longer inputs), the claim no longer holds. A brief clarifying sentence would prevent misreading.

---

## Nice-to-Haves

- Reporting per-horizon results (T ∈ {96, 192, 336, 720}) would bring the evaluation in line with community standards and substantially strengthen confidence in the SOTA claims. If the gains are consistent across horizons, this would only help.
- An ablation comparing Swin4TS to PatchTST with the same lookback window (L=512) would isolate whether the windowed attention and hierarchical design—rather than patching itself or the longer input—drive the improvements.
- A brief analysis of sensitivity to window size N, patch size P, and number of stages K in the main text would help readers understand the method's key hyperparameters.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"Broken sentence in Section 3.2 is a writing error"** (Harsh Critic): Line 107 reads "Channel-dependence strategy The of Swin4TS with the CI strategy." This is a parser truncation artifact (the section heading and following text were garbled in PDF extraction), not an error in the original submission. REMOVED per the hard rule on parser artifacts.

- **"Baseline input length L=96 vs. Swin4TS L=512 is unfair"** (Harsh Critic): The paper explicitly states "we always compare with the strongest results of each baseline algorithm" (Section 4.1) and notes that PatchTST and DLinear also use L=336 or L=512. Giving each baseline its published-best configuration is a defensible and common practice. REMOVED as the asymmetry favors the baselines (shorter lookback = harder task for them), not the authors.

- **"Complexity claim is the first Transformer-based model with O(ML)"** as a weakness: The claim is technically correct under the paper's stated assumptions; concern that N or P may scale with L is a precision nit already covered in Trivial. REMOVED as a standalone weakness.

- **Strengths: "SOTA on 8 benchmark datasets" as a standalone strength** (Strength Finder, uncaveated): This strength is real but conditional on the aggregated evaluation methodology. Retained in the review but only with the caveat that confidence is limited by the aggregation issue.

- **Generic strength: "demonstrates potential of cross-domain transfer"** (Strength Finder): This is an aspirational framing in the conclusion, not a concretely demonstrated result. REMOVED as too generic/aspirational.

---

## Novel Insights

The paper's most genuinely novel observation—implicit in the results but not explicitly analyzed—is that the Swin Transformer's two specific innovations (windowed attention and hierarchical downscaling) can be independently adopted for 1D temporal data without the spatial inductive biases of 2D images, and still produce gains over global patch attention (PatchTST). The ablation in Table 3 provides preliminary evidence for this decomposition. If supported by broader per-horizon evaluation, this would be a substantive finding about the portability of CV architectural choices to time series, beyond the general "Transformers are cross-domain" narrative.

---

## Suggestions

1. Replace aggregated Tables 1 and 2 with standard per-horizon tables (T ∈ {96, 192, 336, 720}), retaining the averages as a supplementary summary. This is the single highest-leverage change.
2. Present Swin4TS/CI and Swin4TS/CD as separate submissions in tables (not joint best-of-two), with comparison respectively to CI and CD baselines.
3. Extend the ablation (Table 3) to at least 4–5 datasets and include Swin4TS/CI, varying L to isolate the architectural contribution.
4. Specify the CD prediction head clearly—what replaces the linear head flagged as problematic?

---

## Score and Decision

**Originality:** Moderate. Adapting Swin Transformer to 1D time series is a natural step but not done before in this form. The CI/CD flexibility is useful. Not a fundamental methodological breakthrough.

**Importance of research question:** High. LTSF is an active and practically significant problem.

**Support for claims:** Weak-to-moderate. The claims are plausible and the direction is right, but the aggregated evaluation and variant-selection ambiguity prevent clean verification of the SOTA claim.

**Soundness of experiments:** Moderate. 8 datasets is comprehensive; linear complexity is real and demonstrated. Ablation is narrow, evaluation format is non-standard.

**Clarity:** Good overall, with the exception of the underspecified CD head and the TNT4TS mention.

**Value to community:** Moderate. A clean, efficient Swin adaptation with proper evaluation could be a useful contribution; the current form needs revision to meet field standards.

---

### Calibration Anchors

**Round 1 (bracketing):**
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/0Q1mBvUgmt.md` — avg 3.0 — weak anchor; VIPER has limited novelty and weaker evaluation than Swin4TS
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/WFlLqUmb9v.md` — avg 2.5 — weaker than Swin4TS; FIA-Net is less grounded and has significant methodological issues
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/IEs29RYxfK.md` — avg 5.33 — VisionTS; comparable scope (CV-to-time-series), but zero-shot angle is more novel; Swin4TS has more complete evaluation
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/DcG4YnbOT3.md` — avg 4.33 — VisiTER; weaker motivation than Swin4TS, similar evaluation issues
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/UK7Hs7f0So.md` — avg 5.25 — VMFTransformer; different scope, similar rating range
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/1CLzLXSFNn.md` — avg 8.0 — TimeMixer++; clearly stronger: broader scope, per-horizon results, multiple tasks. Swin4TS is below this.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/bWcnvZ3qMb.md` — avg 8.0 — FITS; elegant simplicity, clean evaluation. Swin4TS is weaker.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/vpJMJerXHU.md` — avg 8.0 — ModernTCN; thorough evaluation and strong results. Swin4TS is weaker.

→ Round 1 bracket: **4–6**

**Round 2 (narrowing):**
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/Te5v4EcFGL.md` — avg 6.0 — PatchMixer; patch-based CNN, 7 benchmarks, per-horizon evaluation, cleaner ablation. Swin4TS is similar in scope but weaker on evaluation quality → Swin4TS is below PatchMixer.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/hkgULK8u4d.md` — avg 4.33 — MGTST; multi-scale + cross-channel Transformer, comparable in scope, but has comparison fairness issues and novelty questions similar to (or worse than) Swin4TS. Swin4TS is above MGTST: cleaner design, broader evaluation, more novel architectural inspiration.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/ZRzlhfMqHt.md` — avg 5.25 — ESSformer; sparse segment-based Transformer, similar complexity motivation. Swin4TS is comparable.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/blgJ4g00rC.md` — avg 5.5 — TimeCapsule; multi-scale LTSF, comparable scope, also has evaluation concerns. Swin4TS is at a similar level.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/IxpTsFS7mh.md` — avg 6.67 — VQ-TR; probabilistic time series with linear complexity, strong ablations and per-horizon evaluation. Swin4TS is below VQ-TR.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/oANkBaVci5.md` — avg 6.75 — Simple Baseline MTS; straightforward but with cleaner evaluation. Swin4TS is below.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/9VRFPC29nb.md` — avg 4.5 — Mamba LTSF; has stronger per-horizon evaluation but similar mixed reception. Swin4TS is comparable.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/3rBu7dR7rm.md` — avg 4.33 — LTSF Benchmark paper; different type. Less comparable.

**Narrowing conclusion:** Swin4TS sits between MGTST (4.33) and PatchMixer (6.0). It is clearly above MGTST—the Swin adaptation is cleaner and more principled—but clearly below PatchMixer and VQ-TR (6.67) because those papers use standard per-horizon evaluation and have cleaner ablations. TimeCapsule (5.5) and ESSformer (5.25) are the closest comparisons in terms of scope and quality. Given the major evaluation methodology gaps (averaged results, variant selection), I place Swin4TS at **5.0** — comparable to or slightly below TimeCapsule, and above MGTST.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>