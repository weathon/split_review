Now I have all the information needed. Let me compile the final review.

## Summary

This paper proposes TbLTA, the first weakly-supervised framework for dense long-term action anticipation (LTA) that relies only on video transcripts (ordered action lists without timestamps) during training. The method combines a temporal alignment module (ATBA) to generate pseudo-labels, a cross-modal attention layer to ground video features with transcript semantics, and a multi-part loss including CTC, CRF, and duration objectives. On the Breakfast dataset, the deterministic variant achieves competitive results with fully-supervised methods (29.03 avg MoC vs 28.45 for ActFusion); on 50Salads it is clearly behind (20.92 vs 28.39). A stochastic variant produces stronger numbers (37.15 avg on Breakfast), though the evaluation protocol is deferred to supplementary material.

## Strengths

- **First transcript-only LTA framework with genuine novelty.** TbLTA is indeed the first approach to train dense long-term anticipation using only video transcripts, eliminating the need for frame-level annotations. This is well-motivated and addresses a real scalability bottleneck.

- **Competitive deterministic results on Breakfast.** At Obs 30% on Breakfast, TbLTA achieves 40.28 MoC (10% prediction horizon) vs 35.79 for the best fully-supervised method (ActFusion), and leads across all four horizons at this observation level. This demonstrates that transcript-level semantics can capture procedural structure effectively on this dataset.

- **Cross-modal attention with structural masking shows clear benefits.** The localized cross-attention design (Eqs. 1-2) is well-supported by the ablation study: removing it drops average MoC by ~5.7 points on Breakfast, while an unconstrained variant recovers only ~1.9 points, confirming the value of the mask derived from pseudo-labels.

- **Competitive on rare classes on EGTEA without dense labels.** TbLTA achieves 60.11 mAP on rare classes, outperforming supervised Anticipatr (55.10) and Timeception (59.70), suggesting transcript-level supervision can help mitigate class imbalance.

## Weaknesses

### Fatal
None.

### Major

- **The ablation study (Table 4) conflates two evaluation protocols without clear labeling.** The numbers in Table 4 (e.g., Breakfast avg 37.2) cleanly match the stochastic Top1 variant from Table 1 (37.15), not the deterministic variant (29.03). The text says "we report results using the Top-1 MoC metric" without stating that these are stochastic-protocol results. Since Table 1 carefully separates deterministic ("Ours (TbLTA)") from stochastic ("Ours (TbLTA)* - Top1"), a reader naturally expects the ablation to be reported under the cleaner deterministic protocol. This mismatch means ablations and main comparisons are on different footings, and the paper never explains why the stochastic protocol was chosen for ablations. The paper would be substantially stronger if ablations were reported under the same protocol as the primary comparison.

### Minor

- **Mixed results are weaker than the framing suggests in aggregate.** On 50Salads, deterministic TbLTA averages 20.92 vs 28.39 for ActFusion — a 7.5-point gap. On Breakfast, the deterministic variant is genuinely competitive (29.03 vs 28.45). The paper acknowledges the 50Salads weakness in the discussion ("complementary picture") but the abstract and conclusion language ("competitive with, and occasionally superior to, fully supervised methods") emphasizes the best case. A more balanced summary would strengthen the paper.

- **Notational inconsistency in CTC formulation.** The CTC loss defines π = [π₁, …, π_{αT}] over the observed portion only, but the marginalization in Eq. 4 sums over t=1 to T. The intended mechanism (standard CTC for transcript alignment) is clear from context, but the notation should be consistent.

- **Weakly-supervised baselines are limited.** Only WS-DA (Zhang et al., 2021) is reported, and only at a single observation setting (30%). A simple baseline — e.g., applying ATBA alone and repeating the last observed action class — would help isolate the value of the anticipation-specific components in the pipeline.

- **No variance estimates.** Single numbers are reported per setting without error bars or significance tests. On a 50-video dataset like 50Salads, this is a meaningful omission.

### Trivial
None.

## Nice-to-Haves

- Reporting computational cost (training time, inference speed, GPU memory) would aid practical adoption.
- An ablation replacing ATBA with a simpler alignment (e.g., CTC-only) would clarify the contribution of the pseudo-label generation step.
- More discussion of failure modes on 50Salads (the paper notes denser action distributions and frequent transitions) would deepen the contribution.

## Removed Points

- **"Stochastic evaluation protocol is undefined"** — The paper states "We also report the stochastic protocol of Abu Farha & Gall (2019) in the supp. mat." The supplementary material is stripped by the parser; the protocol is defined there. Removed per hard rules (missing appendix content).
- **"CTC loss is ambiguous and undermines reproducibility"** — The CTC mechanism is standard and the intended application is clear. The notational inconsistency (π defined over αT, summation to T) is minor and easily fixed, not a reproducibility threat. Removed as overblown.
- **"ATBA module should be noted earlier"** — ATBA is introduced in the methodology section (§3.1) where it belongs architecturally. Removed.
- **"Comparisons are framed selectively"** — The paper's statement "competitive with, and occasionally superior to" is a fair description of the mixed results. The deterministic variant IS competitive on Breakfast and IS clearly behind on 50Salads. The paper discusses both cases. Removed, though I retain a minor note about balance.
- **Strength Finder claims about stochastic variant outperforming all supervised methods** — These depend on the stochastic protocol whose definition is in the supp. mat. and conflate different evaluation regimes. Demoted to the mixed-results framing concern.
- **Several generic strengths from the Strength Finder** (e.g., "the problem is important", generic statements about ablation value) — removed as not specific enough to this paper's concrete evidence.

## Novel Insights

Beyond the paper's own contributions, the review reveals that the deterministic results on 50Salads are meaningfully behind fully-supervised methods, and that the stochastic variant's impressive numbers cannot be cleanly compared because the ablation table uses a different evaluation protocol than the main comparison. This suggests that the paper's strongest evidence (the stochastic numbers) and its self-contained analysis (ablations) share the same protocol, but this is not transparently communicated. The core empirical claim — "transcript supervision can match dense supervision" — is genuinely supported on Breakfast but not yet clearly established across all benchmarks.

## Suggestions

1. **Clarify the ablation evaluation:** State explicitly whether Table 4 reports deterministic or stochastic-protocol results, and ensure all ablations use the same evaluation footing as the primary comparison. If the stochastic protocol is preferred for ablations, justify this choice.

2. **Add naive weakly-supervised baselines:** A simple "repeat last observed action" baseline or a CTC-only alignment baseline would help isolate the contribution of each component.

3. **Include variance estimates** for the key comparisons, especially on 50Salads where the dataset is small.

4. **Balance the framing:** Acknowledge more explicitly that the deterministic approach is competitive on Breakfast but has a significant gap on 50Salads, and discuss what properties of 50Salads (denser actions, frequent transitions) explain this gap.

5. **Fix the notation in Eq. 4** so that the summation index matches the defined range of π.

## Score and Decision

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>