Now I have enough information to proceed with calibration. Let me run the calibration searches.**Round 1 bracket: 4.5 – 6.5.** The paper is the first in its niche (weakly supervised dense LTA), with competitive results and verified issues (duplicate ablation tables). Let me narrow with Round 2.Now I have all the information I need to write the final review. Let me synthesize.

---

## Summary

TbLTA is the first weakly-supervised framework for dense long-term action anticipation (LTA) that relies solely on ordered video transcripts (no frame-level annotations, no temporal boundaries). It combines a borrowed temporal alignment module (ATBA), cross-modal attention grounded by pseudo-labels, CTC, a CRF-based coherence loss, and a momentum-based duration head in an encoder-decoder architecture. Experiments on Breakfast, 50Salads, and EGTEA establish the first transcript-only baseline for dense LTA, achieving deterministically competitive results with fully supervised methods on Breakfast while trailing more clearly on 50Salads.

---

## Strengths

- **First transcript-only dense LTA baseline with genuine competitive performance on Breakfast.** On Breakfast at 30% observation, deterministic TbLTA achieves 29.03% average MoC vs. ActFusion's 28.45%, outperforming all fully supervised baselines — a concrete and notable result given the absence of any frame-level annotation.
- **Well-motivated problem: transcript supervision drastically reduces annotation cost.** The paper convincingly argues that ordered action transcripts, which capture the logical structure of procedural activities, are a natural and cheap supervision signal for LTA — and the Breakfast results empirically support this thesis.
- **Component ablations confirm each module's contribution.** Removing cross-attention drops Breakfast average by ~5.7 MoC points (Table 3/4); removing CRF causes long-horizon degradation (~5.3 on 50Salads, ~4.1 on Breakfast at 50% horizon); removing CTC consistently degrades both datasets. These are specific, quantified contributions.
- **Interesting rare-class result on EGTEA.** TbLTA achieves 60.11% Rare-class mAP vs. Anticipatr's 55.10% (Table 2), with an honest acknowledgment that overall it trails supervised methods. This suggests transcript semantics can genuinely mitigate class imbalance.

---

## Weaknesses

### Fatal
- None.

### Major

- **Duplicate ablation tables invalidate component-level segmentation vs. anticipation claims.** Tables 3 and 4 in the text are byte-for-byte identical (verified: lines 247–257 and 259–269 contain the same values for all conditions). The paper explicitly claims Table 3 shows "IAS" (segmentation) ablation results and Table 4 shows "LTA" ablation results, and Section 4.3 draws distinct conclusions from each ("Results in Table 3 (IAS) and Table 4 (LTA) show a consistent hierarchy"). One of TbLTA's architectural claims — that improved temporal segmentation propagates into better anticipation — cannot be independently verified from the current tables. This is a concrete internal inconsistency that a reader cannot resolve.

- **Stochastic TbLTA is compared against deterministic supervised baselines without a symmetric stochastic baseline.** Table 1 places TbLTA\* Top-1 in the same table as single-prediction supervised methods. On Breakfast, stochastic TbLTA\* Top-1 reaches 37.15% vs. ActFusion's 28.45% — an ~8-point gap. Without applying the same multi-sample Top-1 protocol to at least one supervised baseline (e.g., stochastic ActFusion), it is impossible to determine whether the gap reflects genuinely better uncertainty modeling or simply that sampling helps any method when predictions are uncertain. The table caption does differentiate deterministic vs. probabilistic frameworks, but the comparison is still asymmetric and the headline claim ("occasionally superior to fully supervised approaches") rests partly on this comparison.

### Minor

- **Unexplained Breakfast/50Salads performance gap weakens the paper's thesis about procedural regularity.** The paper explains the 50Salads gap as arising from "long videos, denser action distributions, and frequent transitions" (Section 4.2). This is plausible but the explanation is not tested: 50Salads has ~20 densely ordered actions per video, which should arguably benefit most from transcript-level structure. The paper does not analyze whether pseudo-label accuracy (measurable from ATBA alignment quality) correlates with the performance difference, leaving the practical limits of the approach unclear.

- **Limited novelty of individual components.** The ATBA temporal alignment module is directly adopted from Xu & Zheng (2024); the CTC loss is standard; the CRF is adapted from Maté & Dimecicoli (2024). The paper's contribution is the combination of these parts in a new setting (weakly supervised LTA) rather than any individually novel component. The cross-modal attention and the stochastic duration head are the most original elements, but the ablation shows the duration head contributes very little on 50Salads (~0.2 points). The paper should more clearly delineate what is genuinely new vs. what is direct adoption.

### Trivial
- None beyond the duplicate table issue already noted.

---

## Nice-to-Haves

- Reporting pseudo-label quality (frame-level accuracy of ATBA pseudo-labels against held-out ground truth, measured per dataset) would directly explain the Breakfast/50Salads gap and give practitioners a diagnostic tool for when transcript supervision is likely to work.
- Applying the stochastic Top-1 protocol to at least one supervised baseline (e.g., ActFusion with multiple stochastic runs) would make the probabilistic comparison interpretable and would either strengthen or refine the current headline claim.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Strength finder claim: "stochastic variant demonstrates the adaptability of transcript supervision to uncertainty modeling."** The stochastic protocol is standard (Abu Farha & Gall, 2019) and TbLTA simply plugs into it; the comparison against deterministic supervised methods is asymmetric. This strength is partially valid but overstated — kept as part of the stochastic comparison weakness instead.
- **Strength finder claim: "first transcript-only dense LTA framework demonstrates competitive performance with fully supervised methods."** Partially valid (Breakfast, deterministic) but misleading as stated given the 50Salads gap and EGTEA overall gap. Kept as a narrowed version in Strengths.
- **Harsh critic abstract/introduction claim: "'very robust alternative' is an overclaim."** This is a presentation concern about a single phrase in the abstract. Borderline trivial; subsumed into the major stochastic/asymmetric comparison point.
- **Harsh critic claim on Section 3.1: attribution of ATBA as non-novel.** Valid but partly a presentation criticism. Retained as part of the minor limited-novelty point above.
- **Harsh critic claim on duration loss stability.** The critic says the self-referential momentum buffer may be unstable. The paper acknowledges the limitation ("we use this term only as a weak duration prior rather than a precise per-instance predictor"). Since the ablation shows small but positive contribution on Breakfast, the concern is not unaddressed. Retained only as context for the minor novelty point.
- **Harsh critic claim on "only one prior weakly supervised baseline."** This is a field limitation, not a paper flaw. WS-DA is the only prior work; criticizing TbLTA for having only one comparison is not actionable. Removed.

---

## Novel Insights

The most genuinely interesting finding is the rare-class mAP result on EGTEA (Table 2): transcript-level supervision outperforms a fully supervised model specifically on low-frequency classes (60.11 vs. 55.10 Rare mAP). This suggests that semantic structure in transcripts can serve as a form of implicit regularization that prevents the model from over-specializing to frequent classes — a different kind of benefit from weak supervision that the paper underexplores and that could have broader implications for class-imbalanced recognition tasks.

---

## Suggestions

1. **Fix Tables 3 and 4.** Publish the correct segmentation (IAS) results in Table 3 with the appropriate metric, so readers can separately evaluate segmentation vs. anticipation component contributions — this is architecturally central to TbLTA's design.
2. **Add a stochastic baseline for at least one supervised method.** Running ActFusion under the same Top-1 stochastic protocol would make the probabilistic comparison in Table 1 interpretable and is straightforwardly implementable.
3. **Analyze pseudo-label quality per dataset.** Reporting ATBA alignment accuracy (when frame-level labels are withheld from training but used for post-hoc evaluation) on both Breakfast and 50Salads would explain the ~8-point performance gap and make the paper's practical scope much clearer.

---

## Score and Decision

**Originality:** Moderate. The problem setting (transcript-only dense LTA) is genuinely novel, but individual components are borrowed from prior work. The cross-modal attention and the overall pipeline integration are the main original elements.

**Importance of research question:** High. Reducing annotation cost for dense LTA is practically significant, and the paper convincingly establishes that the problem is tractable under transcript supervision.

**Whether claims are well supported:** Mixed. The Breakfast competitive-with-supervised claim is well supported deterministically. The global "competitive with fully supervised" claim is overstated given 50Salads and EGTEA overall gaps. The stochastic comparison is asymmetric.

**Soundness of experiments:** Compromised by the verified duplicate ablation tables (Tables 3 and 4 are identical), which prevents evaluation of one of the paper's specific architectural claims.

**Clarity of writing:** Generally clear, but the duplicate tables and the stochastic/deterministic mixing reduce the review's interpretability.

**Value to the research community:** The paper establishes an underexplored benchmark setting and demonstrates viability; the rare-class EGTEA finding is interesting. Contribution is real but bounded by execution issues.

---

### Calibration Anchors

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| f3CdjpPkSq.md (Action Seq. Augmentation) | 6.50 | R1/R2 | Plugin augmentation for LTA; cleaner evaluation, similar scope; TbLTA comparable but has duplicate table issue |
| Bb21JPnhhr.md (AntGPT) | 6.25 | R1/R2 | LLM-based LTA, SOTA on multiple benchmarks; stronger evidence and evaluation than TbLTA |
| HEXtydywnE.md (LASER) | 6.00 | R2 | Weakly supervised video with logic specs; similar contribution level; cleaner presentation |
| GQgPj1H4pO.md (WS Video SGG) | 6.00 | R2 | Weakly supervised video approach; comparable novelty and evidence quality |
| dl34rOnbqJ.md (Actions-to-Action) | 4.40 | R1 | Simpler recurrent LTA model; rejected; TbLTA is clearly more novel |
| DE2RMJVjgI.md (Point-Level TAL) | 4.25 | R1 | Weakly supervised TAL; less directly relevant, rejected |
| IryGDUHxDE.md (Unsupervised action rec.) | 5.25 | R2 | Weakly supervised action recognition; comparable but different task |
| sEARCNzhrP.md (InterAct TAS) | 5.00 | R2 | TAS framework; rejected; comparable execution quality |

**Round 1 bracket: 4.5 – 6.5.**

**Round 2 narrowing:** The closest anchors are the 6.0–6.5 accepted papers (LASER, WS Video SGG, AntGPT, Action Seq. Augmentation). TbLTA is below these on multiple axes: the duplicate table error prevents verification of a specific architectural claim, results are competitive on only one of two primary benchmarks deterministically, and individual components are largely borrowed. It is above the 4.4–5.25 rejects (dl34rOnbqJ, sEARCNzhrP), which either address a much narrower problem or offer less novelty. TbLTA lands below the 6.0-band accepts due to the duplicate tables and mixed evidence, but above the rejects due to genuine first-in-kind contribution and competitive Breakfast results. Final score: **5.0**.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>