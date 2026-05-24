Now I have a good calibration. Let me produce the final consolidated review.

## Summary

The paper proposes ITHP, a hierarchical information bottleneck model for multimodal fusion. The key idea is to designate one modality as "prime" and build a chain of latent states (B₀ → B₁) that sequentially compress information from the prime modality while preserving relevant information about secondary modalities. Experiments on sarcasm detection (MUSIARD) and sentiment analysis (CMU-MOSI, CMU-MOSEI) show improvements over baselines, including surpassing reported human-level performance on CMU-MOSI.

## Strengths

- **Novel hierarchical IB formulation for multimodal fusion**: Extending the IB principle beyond a single bottleneck to a chain of bottlenecks (Equations 2–5) is a conceptually interesting direction. The idea of treating one modality as primary and using IB to relate it to successive modalities is genuinely different from standard concatenation or tensor-fusion approaches.

- **Strong empirical results on CMU-MOSI/MOSEI**: ITHP-DeBERTa achieves 88.7% BA, 88.6% F1, 0.643 MAE, 0.852 Corr on MOSI (Table 2) and 87.3% BA, 87.4% F1 on MOSEI (Table 3). These numbers outperform valid DeBERTa-based baselines (MMIM_d: 85.8/85.9; MAG_d: 86.1/86.0 on MOSI) by clear margins of ~2.5–2.7%. The improvement over reported human-level performance on all four MOSI metrics is noteworthy.

- **Clear improvement over concatenation baseline on sarcasm detection**: On MUSIARD, ITHP raises weighted F1 from 71.5% (MSDM concatenation) to 75.2% for three-modality fusion (Table 1). The paper also shows ITP (single-stage IB) outperforms concatenation for every two-modality combination (e.g., V-A: 70.3% vs 65.7%).

- **Systematic sensitivity analysis**: Figure 4 provides a clean 6×6 grid of β and γ values, demonstrating that performance varies predictably and identifying an optimal operating region (β=32, γ=8). The observation that higher β (text relevance) matters more than higher γ is consistent with the two-modality ablations.

## Weaknesses

### Major

- **No ablation isolating the hierarchical structure for three modalities**: For two modalities, the paper compares ITP (single-stage IB) against MSDM (concatenation). For three modalities, ITHP (hierarchical) is compared only against MSDM (concatenation). There is no comparison against a non-hierarchical three-modality baseline — e.g., a single IB bottleneck operating on concatenated [X₀,X₁,X₂] or a non-IB hierarchical model with the same architecture. Without these, it is unclear whether the improvement comes from the IB objective itself, the hierarchical design, or the combination. The paper acknowledges the modality-order limitation but does not experimentally quantify how much the hierarchy matters versus other design choices.

- **Loss function derivation is presented as tighter than it is**: The paper formulates a constrained optimization (2) with three explicit ε-constraints, then states it "construct[s] a Lagrangian function" leading to (3). However, (3) does not correspond to the standard Lagrangian of (2): the ε parameters and the I(X₀;X₁)/I(X₀;X₂) terms disappear without derivation, and the roles of β, λ, γ are introduced heuristically. The paper should clarify that (3) is a heuristic two-level IB objective motivated by (2), not a direct Lagrangian solution. This gap does not invalidate the method (the objective is still a reasonable IB loss), but the framing overstates the theoretical grounding.

- **No statistical significance or variance reporting**: None of the main results tables report standard deviations, confidence intervals, or number of runs. For datasets like MOSI (~2,199 samples), variance matters. Without error bars, it is impossible to assess whether the reported improvements (e.g., 88.7 vs 86.1 BA) are robust or within noise.

### Minor

- **Sarcasm detection evaluation uses a single 2019 baseline**: MSDM is the only comparator on MUSIARD. More recent multimodal methods (e.g., transformer-based approaches) would strengthen the evaluation and better situate the contribution.

- **Human-level comparison lacks context**: The human numbers (85.7% BA, 87.5% F1, etc.) are cited from prior work without describing the annotation procedure, number of annotators, or whether the human prediction task is directly comparable to the automated evaluation. This makes the "first to outperform human-level" claim less substantiated than it could be.

- **Modality ordering is set by heuristic, not validated**: The paper sets modality order by feature dimensionality (sarcasm: V→T→A) or hypothesis (sentiment: T→A→V). The limitations section mentions Table 11 in the appendix for alternative orders, but the main text provides no systematic evidence that the method is robust to ordering. A simple experiment varying the order on one dataset would substantially strengthen the paper.

### Trivial

- Table 2 header has a typo ("FI" instead of "F1").

## Nice-to-Haves

- Reporting training time, parameter counts, or inference speed relative to baselines would help assess practical utility.
- An analysis or visualization of what the latent representations B₀ and B₁ actually capture (e.g., measuring I(B₀;X₁) vs I(B₀;irrelevant features)) would provide useful validation of the IB mechanism.
- Testing on additional multimodal settings (e.g., vision+language, sensor fusion) would demonstrate broader applicability beyond text+audio+video.

## Removed Points

- **Criticism about Self-MM_d inflating results**: The paper includes Self-MM_d (55.1% BA) in Table 2 and explicitly states "Self-MM itself heavily relies on the feature extraction process performed by BERT, resulting in a significant degradation." The table also includes MMIM_d (85.8%) and MAG_d (86.0%) as valid DeBERTa baselines that ITHP clearly outperforms. The presence of the collapsed Self-MM_d does not inflate ITHP's advantage relative to the fair baselines.

- **Criticism about "reciprocal feedback" neuroscience overclaiming**: The neuroscience sections describe background research on reciprocal connectivity in the brain, not properties of the ITHP model. The model description (Section 2) clearly presents a feedforward architecture. This is a standard neuroscience-inspiration framing, not a misleading claim.

- **Criticism about unfair backbone comparison**: ITHP uses DeBERTa, while several baselines use BERT. However, the paper also includes DeBERTa-based variants of MMIM and MAG (MMIM_d, MAG_d) which serve as valid fair comparisons. The BERT-based numbers provide additional context. No unfair advantage is being hidden.

- **Criticism about missing appendix content**: The parser strips appendices from all papers. The paper claims Appendix Table 11 addresses modality ordering and Appendices B-F contain architectural details. These exist in the original submission.

- **Generalized criticism about "could the metric be measuring a proxy"**: These are unspecified speculative concerns without concrete anchors in the paper text.

- **Several formatting and typo nitpicks**: Remove as per parser-error rule.

- **Generic strengths about "addressing an important problem"**: Removed as they lack specific evidence.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface any genuinely novel observation about the approach that the authors themselves have not stated.

## Suggestions

1. Add a crucial ablation: compare ITHP against (a) a single IB bottleneck on concatenated three-modality input, and (b) ITHP with reversed or random modality order on at least one dataset. This directly tests whether the hierarchy provides value.
2. Report standard deviations or confidence intervals for all main results (error bars from at least 3 runs).
3. Clarify the relationship between the constrained optimization (2) and the loss (3) — either by providing the full Lagrangian derivation (showing how ε is absorbed into Lagrange multipliers) or by explicitly stating that (3) is a heuristic IB-based objective inspired by (2).
4. Provide context for the human-level numbers: cite the original source, describe the annotation procedure, and note whether the comparison is direct.
5. Add a more recent baseline for the sarcasm detection experiment.
6. Fix the "FI → F1" typo in Table 2.

## Score and Decision

**Round 1 bracketing**: The paper sits between weak anchors (2.6–3.4, papers with serious flaws or withdrawn) and strong anchors (7.6–8.0, oral/spotlight papers). The most relevant middle-band anchors are in the 3.8–6.33 range. Initial bracket: **3.5–6.5**.

**Round 2 narrowing**: Comparing against the anchors:

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| `BZWssJoYEv` (Holistic Multimodal Interaction) | 5.50 | R1 | Slightly stronger theory but weaker experiments. ITHP has more concrete results but looser theory. ITHP is comparable or slightly weaker. |
| `INqLJwqUmc` (Narrowing IB Theory) | 5.25 | R1, R2 | Accepted as poster. Stronger theoretical framing but similar methodological gaps. ITHP has more extensive experiments. Comparable quality. |
| `PflweLMInP` (CMML-Net sarcasm) | 5.25 | R1, R2 | Rejected. Similar empirical scope, similar issues with missing ablations. ITHP has broader dataset coverage. Comparable. |
| `2jEiFTLRwX` (VisionFuse) | 5.00 | R2 | Withdrawn. Comparable methodological quality but different domain. ITHP is slightly more original. |
| `iSLDihAfYi` (Sparsely multimodal) | 4.80 | R2 | Rejected. Similar empirical evaluation issues (missing ablations). ITHP is slightly stronger. |
| `9DDJuab67K` (Unimodal-driven Distillation) | 3.80 | R1 | Rejected. Weaker experimental support. ITHP is clearly stronger. |
| `1waeKNeQzG` (Style-Coherent Fusion) | 5.50 | R2 | Rejected. Comparable overall quality with different strengths/weaknesses. |

The paper is stronger than the weakest anchors (~3.8) and comparable to or slightly weaker than the ~5.5 anchors. It has a genuinely interesting idea and strong empirical signal, but the missing ablations and loose theoretical framing prevent it from reaching the ~5.5–6.0 level of papers like "Barycentric Alignment" (6.33) or even "Holistic Multimodal Interaction" (5.5), which had stronger theoretical or experimental rigor. The paper sits closest to the 5.0–5.25 anchors.

**Final score: 5.0** — a paper with a promising idea and decent results, but with structural gaps in the evaluation (missing ablations for the core architectural claim, no variance reporting, overstated theoretical derivation) that prevent a clear accept recommendation. Major revision with additional experiments could bring it to a stronger position.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>