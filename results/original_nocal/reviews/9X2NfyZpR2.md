Now I have all the information needed. Let me produce the consolidated review.

## Summary

The paper introduces TbLTA, the first framework for dense long-term action anticipation (LTA) trained exclusively from video transcripts (ordered action lists without timing/duration). It combines a temporal alignment module (ATBA) to generate frame-level pseudo-labels with cross-modal attention for semantically grounding video features, and uses CTC, CRF, and duration losses for supervision. On Breakfast, TbLTA achieves an average MoC of 29.03, outperforming the best fully-supervised method (ActFusion, 28.45) while using no frame-level annotations. On 50Salads and EGTEA, performance is competitive with fully-supervised methods on rare classes, though weaker on 50Salads overall.

## Strengths

- **First transcript-only weakly-supervised approach for dense LTA.** The paper correctly identifies that prior LTA work (including Zhang et al., 2021) still relies on some frame-level labels, while TbLTA uses only transcripts. This is a genuinely new problem formulation that reduces annotation cost. (Sec. 1, lines 19–21; Sec. 2, lines 132–137)

- **Competitive results on Breakfast despite no frame-level labels.** On the Breakfast dataset, deterministic TbLTA achieves an average MoC of 29.03 across all observation/anticipation horizons, exceeding the best fully-supervised method ActFusion (28.45) and far surpassing the only prior weak-supervision baseline WS-DA (15.65 at Obs 30%). This is the strongest evidence that transcript-only supervision can be viable for dense LTA. (Table 1)

- **Well-structured ablation study isolating each component's contribution.** The ablations (Table 4) clearly separate the contributions of CTC, cross-modal attention, CRF, and duration loss. The hierarchy *w/o cross-att* < *cross-att simplex* < **TbLTA** (e.g., 31.5 → 33.9 → 37.2 on Breakfast avg) demonstrates that the masking and gated fusion design choices are empirically justified. The CRF ablation shows particularly large gains at the 50% horizon (on Breakfast at Obs 20%: 30.5 vs 20.0 without CRF; on 50Salads: 22.1 vs 16.0), confirming its role in temporal coherence at long horizons.

- **Competitive on rare classes on EGTEA.** On EGTEA, TbLTA achieves 60.11 mAP on rare classes, outperforming fully-supervised Anticipatr (55.10) and Timeception (59.70), despite lower overall mAP. This suggests transcript-based supervision can mitigate class imbalance. (Table 2)

- **CTC-based alignment adapted to the LTA setting.** Adapting CTC (Sec. 3.2.2) to stabilize pseudo-labels and prevent error propagation into anticipation is a clean technical contribution. The ablation confirms CTC removal degrades accuracy by ~0.6–0.8 points.

## Weaknesses

### Fatal
None.

### Major

- **CRF loss formulation is underspecified — Eq. 5–6 creates a dimensional ambiguity.** The paper places a linear-chain CRF on decoder outputs with emission scores \(Z \in \mathbb{R}^{T_{\text{pred}} \times |\mathcal{C}|}\) and treats the target as "\(\mathcal{Y}_{\text{LTA}}\) the target anticipate transcript" (lines 174–180). However, the decoder is described as generating a variable-length sequence of action segments terminated by an EOS token (line 144), while \(T_{\text{pred}}\) is a fixed number of frames. The paper also generates frame-level pseudo-labels \(\hat{Y}_{\text{pred}}\) for the anticipation interval (Fig. 2 caption, line 116), which would be natural CRF targets. The paper never clarifies whether the CRF operates on frame-level pseudo-labels or on segment-level transcript labels, nor how a variable-length transcript would align with fixed-length frame-level emissions. This ambiguity makes the training objective as written non-reproducible without guesswork. The ablation results (Table 4) confirm the CRF does improve performance, so the implementation likely resolves this — but the paper must disambiguate its formulation.

### Minor

- **No quantitative validation of pseudo-label quality.** The entire framework is supervised by ATBA-generated pseudo-labels, yet the paper never evaluates how accurate these are on the observed portion (e.g., frame-wise mIoU or accuracy against ground-truth segmentation). Without this analysis, readers cannot assess whether the weak supervision signal is reliably grounding the anticipation decoder, or whether the model is overfitting to noisy proxy targets. The main results provide indirect validation, but a dedicated pseudo-label quality analysis would substantially strengthen the paper. (Sec. 3.1, lines 130–131; Sec. 4.4 is only qualitative)

### Trivial
- Minor citation name inconsistencies (e.g., "Damicoli", "Dimecicoli", "Damiccoli" appear to refer to the same author across lines 98, 144, 155, 511).

## Nice-to-Haves
- **Standard error reporting:** Adding error bars (e.g., across splits) would help assess whether the observed differences from fully-supervised baselines are significant.
- **Controlled supervised re-implementation:** Retraining a fully-supervised method (e.g., FUTR) under the same features and splits would more cleanly isolate the cost of weak supervision from implementation differences.
- **Failure analysis on 50Salads:** A per-class breakdown would support the claim that denser action distributions cause the performance gap, rather than offering it as a post-hoc explanation.

## Removed Points

These points from the reviews are flagged to be removed (treat with caution):
- **"CRF loss is ill-defined to the point of being non-computable"** — overstatement; the CRF operates on frame-level outputs and the ablation confirms it works. The issue is a clarity gap, not a structural flaw.
- **"Comparison with supervised methods not controlled (no error bars)"** — standard in this field; not a genuine weakness.
- **"Stochastic vs deterministic comparison is apples-to-oranges"** — the paper reports both separately with clear labeling.
- **"First weakly-supervised claim should be qualified by Kim et al. (2024)"** — paper properly distinguishes dense LTA from symbolic prediction and acknowledges prior work.
- **"ATBA partition not explained"** — paper cites the original work (Xu & Zheng, 2024), which is standard.
- **"EGTEA protocol not specified"** — it is specified (line 198: α ∈ 25%, 50%, 75%, mAP from Nagarajan et al. 2020).
- **"Duration loss underspecified"** — the paper adequately describes the momentum buffer and regression head (lines 186–190).
- **"Ablations use different metric than main table"** — the paper explains this choice (line 235: Top-1 MoC used "as it provides a stable reference point").
- **"Kim et al. (2024) not acknowledged"** — paper explicitly discusses Kim et al. (lines 53–55, 112–114).
- **Pure formatting/style nitpicks** — removed per policy.
- **Strength Finder's generic/superficial strengths** — removed; only evidence-grounded strengths retained.

## Novel Insights

The most interesting observation from the review cross-analysis is that the paper's core claim — that transcript-only supervision can be competitive with dense supervision — is strongly supported on Breakfast (where activities have strong procedural regularities) but considerably weaker on 50Salads (where denser, more variable action distributions amplify alignment noise). This suggests a fundamental trade-off: transcript supervision excels when tasks have stereotyped action sequences, but deteriorates as temporal variability increases. This insight, implicit in the paper's discussion (line 231) but never analyzed quantitatively, is worth elevating as a direction for future work. Additionally, the CRF's outsized impact at long horizons (Table 4: ~10-point gap on Breakfast at 50% horizon) is striking — it suggests that weak-supervision LTA methods may need stronger temporal coherence priors than fully-supervised counterparts, because the pseudo-labels themselves lack boundary precision.

## Suggestions
1. **Clarify the CRF target:** Explicitly state whether the CRF loss (Eq. 5–6) uses frame-level pseudo-labels \(\hat{Y}_{\text{pred}}\) or segment-level transcript labels. If frame-level, re-label the target as \(\hat{Y}_{\text{LTA}}\) (as used in Fig. 2) rather than \(\mathcal{Y}_{\text{LTA}}\). If segment-level, explain the alignment procedure.
2. **Add quantitative pseudo-label analysis:** Report frame-wise accuracy or mIoU of ATBA pseudo-labels on the observed portion against ground-truth, ideally broken down by action class.
3. **Add error bars:** Report per-split standard deviations for the main results (Table 1), especially where the paper claims superiority over supervised methods.
4. **Expand the 50Salads discussion:** Provide a per-class breakdown to empirically support the claim that dense action distributions cause the performance drop.

## Score and Decision

The paper makes a genuine contribution — a well-motivated new problem setting, a thoughtfully assembled architecture, clean ablations, and strong results on Breakfast. Two weaknesses require attention: the CRF formulation ambiguity (must be fixed for reproducibility) and the missing pseudo-label quality validation (needed to assess the supervisory signal's reliability). Neither is fatal; the ablation results confirm both components work as intended. The paper is solid and represents a meaningful step toward reducing annotation costs for LTA.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>