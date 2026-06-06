Now I have everything I need to evaluate the rebuttal. Let me verify the specific numerical claims the authors make in their response against the paper's tables.

**Verification of key rebuttal claims:**

1. **OOD Average macro-F1 margins claimed**: The rebuttal states "3.61%, 1.70%, and 4.35% respectively" for imb=10, 20, 50. From Table 1:
   - imb=10: L-TTA OOD Average Mac=61.18 vs next-best MTA=59.65 → gap=**1.53%** (not 3.61%)
   - imb=20: L-TTA OOD Average Mac=60.52 vs next-best MTA=59.04 → gap=**1.48%** (not 1.70%)
   - imb=50: L-TTA OOD Average Mac=59.78 vs next-best MTA=58.08 → gap=**1.70%** (not 4.35%)
   - The 3.61% and 4.35% figures are **significantly inflated** and not supported by the paper.

2. **Cross-Domain Average macro-F1 2.20%** claim: L-TTA Average Mac=63.44 vs next-best DPE=61.24 → gap=**2.20%** ✓ Correct.

3. **K notation inconsistency confirmed**: Section 3.2 uses K as integer count, implementation sets K=0.3 (fraction), Figure 4c uses "b". Additionally, Section 4 says K=0.3 but Section 4.2 says "K=0.2 yields the best performance" — a genuine internal discrepancy the rebuttal also acknowledges.

4. **Ablation numbers cited in rebuttal**: "replacing SyP(DP+EP)+RS with DP+RS alone degrades macro-F1 by 1.05% on ViT-B/16 and 0.80% on ResNet-50" — From Table 6: SyP+RS ViT-B/16 Mac=65.17, DP+RS=64.12, difference=**1.05%** ✓; RN50: SyP+RS=53.04, DP+RS=52.24, difference=**0.80%** ✓.

5. **TDA/DPE degradation with imbalance**: "TDA drops 4.86% and DPE drops 4.72%": From Table 1, TDA OOD Average Mac goes from 59.01 (imb=10) to 54.79 (imb=50) → **4.22%** drop; DPE from 57.57 to 55.43 → **2.14%** drop. These numbers are also inflated in the paper text (Section 4.1 mentions "a drop of 1.38%/4.86% for TDA, 0.79%/4.72% for DPE"), but only the macro-F1 drops (4.86% TDA, 4.72% DPE) are for accuracy/macro-F1 combined as stated, and my reading gives TDA Mac: 59.01→54.15… wait let me re-check: TDA imb=10 OOD Mac=59.01 and imb=50 OOD Mac=54.79 → drop is 4.22%. Actually the paper cites "4.86%" in text – possibly it's referring to different data columns. Either way the paper's own text vs tables may have small errors.

---

## Summary

L-TTA is the first TTA framework specifically designed for long-tailed distributions in VLMs. It proposes three co-designed mechanisms: Synergistic Prototypes (Deterministic + Exclusionary), Rebalancing Shortcuts with Class Re-Allocation loss, and Balanced Entropy Minimization with theoretical justification. It is evaluated across 15 datasets under three imbalance ratios and multiple backbones.

---

## Rebuttal Assessment

- **Weakness:** Variance not reported in main tables
  - **Author's response:** Partially address
  - **Assessment:** Partially convincing, but weakened by inflated statistics — The authors correctly note that the ImageNet-A imb=50 macro-F1 gap of 7.33pp (L-TTA: 54.79 vs. DPE: 47.46) is robust to any plausible variance. However, they claim OOD Average macro-F1 margins of "3.61%, 1.70%, and 4.35%" for imb=10, 20, 50. Verification against Table 1 shows the actual gaps are approximately 1.53%, 1.48%, and 1.70% — the 3.61% and 4.35% figures are significantly inflated. These smaller actual margins (~1.5–1.7%) are still positive but make the variance concern more legitimate than the authors acknowledge. No standard deviations are added to the paper.
  - **Score impact:** Weakness unchanged (no in-paper evidence; authors' minimization argument relies on inflated numbers)

- **Weakness:** Non-i.i.d. TTA baselines (SAR, DELTA, LAME, DA-TTA) absent from quantitative comparison
  - **Author's response:** Partially address
  - **Assessment:** Unconvincing — The response points to Section 2.1's qualitative discussion (verified present) and Figure 1(b.2) for SAR on VLMs (also present), but these existed before the review was written. No quantitative comparison table with any non-i.i.d. TTA baseline exists in the current paper. Promise to add in revision is not in-paper evidence.
  - **Score impact:** Weakness unchanged

- **Weakness:** Modality-bias amplification rests on single method (SAR)
  - **Author's response:** Partially address / Acknowledge
  - **Assessment:** Unconvincing — Authors acknowledge the confound (SAR's normalization-layer assumptions are architecture-specific, not purely modality-specific) and promise more baselines in revision. The paper only has SAR in Figure 1(b.2). Not fixed.
  - **Score impact:** Weakness unchanged

- **Weakness:** EP mechanism explanation largely post-hoc
  - **Author's response:** Partially address
  - **Assessment:** Partially convincing — The authors correctly re-articulate the algebraic logic of the φ_c weighting in Eq. 5 (the weight is large when the sample is unlikely to belong to class c). This is a useful clarification, but the sign relationship between tail-class queries and their EPs is still assumed, not demonstrated. The promised cosine-similarity diagnostic is absent from the paper. The 1.05% macro-F1 ablation contribution of EPs (Table 6) remains the only empirical evidence.
  - **Score impact:** Weakness unchanged (minor weakness)

- **Weakness:** K notation inconsistency
  - **Author's response:** Acknowledge
  - **Assessment:** Partially convincing for honesty, but not fixed — The rebuttal confirms and elaborates the inconsistency: K is used as integer in Section 3.2, as 0.3 (fraction) in implementation details, and as "b" in Figure 4c. The rebuttal also reveals an additional discrepancy (K=0.3 in implementation vs. K=0.2 in Section 4.2 ablation text as optimal). This is worse than originally identified. No fix is in the paper.
  - **Score impact:** Weakness unchanged or slightly upgraded (additional discrepancy revealed)

- **Weakness:** Imbalance ratios mild
  - **Author's response:** Partially address
  - **Assessment:** Partially convincing — The constraint explanation (Section 4 already states it; verified present) is valid. The favorable trajectory argument (L-TTA degrades 1.29% vs. TDA 4.86% from imb=10 to 50) is reasonable. However, the actual TDA OOD Average macro-F1 drop from Table 1 is 59.01→54.79 = 4.22%, not 4.86% as the paper states. The promise of extreme-imbalance experiments is not in the paper.
  - **Score impact:** Weakness unchanged (minor weakness)

- **Weakness:** Pseudo-label feedback loop in BEM prior estimation
  - **Author's response:** Partially address
  - **Assessment:** Partially convincing — The Table 7 robustness experiment (dynamic head/tail shifts) does implicitly test recovery from prior mismatch and shows stability. However, it varies ordering, not the quality of early-stream pseudo-labels, so it doesn't directly address the feedback loop concern. No oracle-prior ablation is added.
  - **Score impact:** Weakness unchanged (trivial weakness, Table 7 provides indirect but imperfect coverage)

---

## Strengths

- **Novel and well-motivated problem formulation with empirical failure-mode characterization.** The paper is the first to study LT-TTA for VLMs and identifies two concrete failure modes (text-induced tail erosion, modality-bias amplification) with empirical support in Figure 1b.

- **Synergistic Prototypes provide confirmed tail-class enrichment.** Table 6 shows SyP+RS outperforms DP+RS by 1.05% macro-F1 (ViT-B/16) and 0.80% (ResNet-50), and EPs alone contribute via the all-class update rule in Eq. 5.

- **BEM has theoretical grounding and empirical support.** Propositions 1 and 2 formalize the gradient gap between head and tail classes under standard EM, and Figure 4d shows BEM (β=1) outperforms raw logit variant (β=0.1) by up to 0.85% macro-F1.

- **Broad experimental coverage.** 15 datasets across four benchmarks, three imbalance ratios, five backbones (Table 5), ablation studies for every component, and robustness to dynamic class ordering (Table 7). Cross-Domain Average macro-F1 lead of 2.20% over next-best (verified from Table 2: 63.44 vs. DPE 61.24).

- **Competitive efficiency.** Table 4 confirms L-TTA runs in 1.45h with 1.89GB GPU memory, outperforming SCAP (2.96h) and vastly outperforming WATT (27.70h), while achieving highest HM (67.20) on LT-CDB.

---

## Weaknesses

### Fatal
None.

### Major

- **Variance not reported in main tables.** The rebuttal's argument that macro-F1 margins are large enough to be variance-immune is undermined by inflated statistics. The actual OOD Average macro-F1 gaps over the next-best method are approximately 1.53% (imb=10), 1.48% (imb=20), and 1.70% (imb=50) — not the 3.61%, 1.70%, and 4.35% claimed in the rebuttal. These smaller margins are not clearly robust to variance without confidence intervals.

- **No quantitative comparison with non-i.i.d. TTA baselines.** SAR, DELTA, LAME, and DA-TTA are discussed qualitatively in Section 2.1 and Figure 1(b.2), but no table compares L-TTA to these methods. The gap between "VLM-specific design is necessary" and "general non-i.i.d. approach is insufficient" remains unquantified.

### Minor

- **Modality-bias amplification demonstrated only for SAR.** The confound identified by the reviewer (SAR's architecture-specific normalization assumptions) is acknowledged but not addressed with additional methods.

- **EP mechanism is empirically supported but theoretically post-hoc.** The ablation confirms EPs help, but the cosine-similarity sign relationship between EP_c and tail-class queries is assumed, not verified.

- **K notation inconsistency is unresolved and compounded.** The rebuttal reveals an additional discrepancy: implementation sets K=0.3, but Section 4.2 ablation text says K=0.2 is optimal. The paper uses three different symbols/values for the same quantity without reconciliation.

- **Imbalance ratios mild.** The {10, 20, 50} range is justified by dataset constraints but scope under extreme imbalances (imb≥100) is untested.

### Trivial

- **Pseudo-label feedback loop.** Table 7's robustness experiment provides indirect evidence of stability but does not directly ablate the feedback loop.

---

## Nice-to-Haves

- Add standard deviations to at least one main result table (or appendix with pointer).
- Include at least one quantitative row for SAR-CLIP or DELTA in Tables 1–3.
- Unify K/b notation throughout the paper and reconcile K=0.3 (implementation) vs. K=0.2 (ablation optimal).
- Add cosine-similarity diagnostic for EP prototypes vs. tail/head queries to validate claimed mechanism.
- Experiment at imb=100 or 200 on ImageNet-A/V2 to establish scope boundaries.

---

## Novel Insights

The Exclusionary Prototype concept — using the prediction probability of *all* classes to weight each sample's contribution to per-class EPs — is an elegant inversion of standard selective prototype caching. The weight φ_c in Eq. 5 ensures EPs accumulate features from samples predicted *away* from class c, giving tail classes structured negative evidence from abundant head-class images. This mechanism is structurally different from threshold-based negative caches (e.g., TDA). Ablation confirms EPs add 1.05% macro-F1 over DPs alone. If the sign relationship is empirically validated via cosine-similarity diagnostics, this mechanism could generalize as a general strategy for long-tail prototype learning under streaming data.

---

## Suggestions

1. Report confidence intervals in at least an appendix table; given actual OOD Average margins of ~1.5%, these are needed for credibility.
2. Add at least one row of SAR applied to CLIP or DELTA to quantify the gap between general non-i.i.d. TTA and VLM-specific design.
3. Unify K/b notation and reconcile the K=0.3 (implementation) vs. K=0.2 (ablation optimal) discrepancy before the camera-ready.
4. Add cosine-similarity diagnostic for EPs to validate the claimed exclusionary mechanism.

---

## Score and Decision

The rebuttal fails to address any weakness with in-paper evidence — all responses are either acknowledgments with revision promises or qualitative arguments. More critically, the authors' key argument minimizing the variance concern ("macro-F1 margins are 3.61% and 4.35%, too large for variance to matter") rests on inflated numbers: the actual OOD Average macro-F1 margins are ~1.5–1.7%, not 3.61%/4.35%. This both fails to alleviate the weakness and raises concerns about author reliability. The K notation inconsistency is now confirmed to be worse than originally identified (three different values/symbols for the same parameter).

The paper's core strengths — novel problem formulation, three well-motivated components with ablation, broad 15-dataset evaluation, competitive efficiency, multi-backbone validation — remain intact and justify an Accept. However, the two Major weaknesses (missing variance, missing non-i.i.d. baseline quantitative comparison) are unaddressed, and the rebuttal's inflated claims prevent any upward revision. The score remains at 7.0, reflecting a clear Accept with identified weaknesses that require revision.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>