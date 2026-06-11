Now I have a clear comparative picture. Let me finalize.

**Round 1 Bracket:** 4.5 – 6.0

**Round 2 Comparison Summary:**
- TbLTA is clearly stronger than InterAct (5.00, rejected for limited novelty + insufficient ablation rigor) and Sparse Skill Extractor (4.75, rejected for overclaiming + evaluation gaps)
- TbLTA is comparable to VSNLS (6.00, accepted) — both are "first weakly-supervised X" papers with modular architectures and identifiable evaluation limitations, but TbLTA's architectural contributions are more technically substantive
- TbLTA is somewhat below AntGPT (6.25, accepted) — AntGPT achieves SOTA across more benchmarks with fewer dataset-specific caveats

**Final Score:** 5.5. The paper has genuine novelty (first transcript-only LTA), impressive Breakfast results, and well-designed architectural components with meaningful ablations. But the 50Salads performance gap (~7.5 points below ActFusion) is substantial and insufficiently diagnosed, and the EGTEA evaluation simplification (19 verbs vs. 106 classes) goes undiscussed as a limitation. These pull what could have been a clear accept down to borderline territory.

---

## Summary
TbLTA proposes the first framework for dense long-term action anticipation trained exclusively from video transcripts (ordered action lists without timing), eliminating the need for frame-level boundary annotations. The architecture combines temporal alignment for pseudo-label generation, cross-modal attention with transcript-derived local masking, CTC-based alignment, CRF-based temporal coherence, and a self-supervised duration loss. Results on Breakfast show competitive or superior performance to fully supervised methods, while 50Salads shows a substantial gap and EGTEA evaluation is restricted to verb prediction only.

## Strengths
- **First transcript-only supervision for dense LTA**: The paper is genuinely the first to eliminate dense frame-level annotations entirely for LTA training. Prior work (Zhang et al., 2021) still required frame-level labels for observed segments. This represents a meaningful advance in reducing annotation burden for LTA.
- **Strong performance on Breakfast**: The deterministic TbLTA achieves 29.03 average MoC at 30% observation on Breakfast, surpassing all fully supervised baselines including ActFusion (28.45) and FUTR (26.59) — a genuinely compelling result for weak supervision.
- **Cross-modal attention with local masking is well-designed and impactful**: The construction of a binary local mask to restrict transcript action embeddings to their predicted temporal neighborhoods (Equations 1-2) yields ~5.7 point improvement on Breakfast over no cross-attention and ~1.9 points over unconstrained cross-attention (Table 4). This is a substantial architectural contribution, not a minor tweak.
- **CRF loss provides meaningful long-horizon coherence**: The linear-chain CRF (Equations 5-6) contributes ~4.1 points on Breakfast and ~5.3 points on 50Salads at longer horizons (Table 4), directly addressing the instability of long-term autoregressive forecasts.
- **Practical multi-stage training scheme**: The progressive training (pretraining → alignment → end-to-end, line 198) is a sensible engineering solution to the cold-start pseudo-label problem that enables the method to work without any frame-level initialization.

## Weaknesses

### Fatal
None.

### Major
- **Performance collapses on 50Salads without adequate diagnosis**: At 30% observation, TbLTA averages 20.92 MoC vs. ActFusion's 28.39 — a ~7.5 point gap. The paper attributes this to "weaker temporal regularities" in 50Salads (Section 4.2), but offers no controlled experiment or quantitative diagnostic to support this explanation. Since 50Salads is one of only two primary LTA benchmarks, the claim that transcript-based supervision is "very robust" (Abstract) or broadly "competitive with fully supervised methods" (Conclusion) is overstated. The paper acknowledges the gap but does not investigate it empirically, leaving a central scientific question unanswered: under what conditions does transcript-only supervision work?

- **EGTEA evaluation is restricted to verb prediction only, substantially simplifying the task**: EGTEA contains 106 verb-noun action classes, but the paper evaluates on only 19 verb classes (Section 4.1, line 194). This collapses the label space to ~18% of its original size and removes the fine-grained discrimination that makes EGTEA challenging. The paper never discusses this as a limitation, yet the competitive rare-class results (Table 2) are obtained on this dramatically simplified task and cannot be interpreted as evidence that TbLTA works on EGTEA as standardly used.

### Minor
- **Stochastic TbLTA* results appear alongside deterministic baselines without comparable stochastic competitors in the main table**: The paper places TbLTA* (stochastic, reporting Mean and Top-1 MoC) in Table 1 while moving stochastic baselines to the supplementary material (line 223). The deterministic TbLTA row is the appropriate comparison to deterministic baselines and is clearly labeled, but including stochastic baselines in the main table would make the comparison fully transparent.

- **Missing combined ablation of the architectural additions**: The paper ablates individual components (w/o CTC, w/o cross-att, w/o CRF, w/o duration) but never evaluates a combined minimal baseline: ATBA pseudo-labels fed directly to a simple decoder, stripping all four additions simultaneously. This would clarify whether the core ATBA pseudo-labeling idea does most of the work or whether the full architectural stack is necessary. Each component's incremental contribution is shown, but the joint contribution is not quantified.

- **Duration loss relies on momentum-based class priors without discussion of dataset-specific bias**: The self-supervised duration loss (Eq. 7) uses class-wise duration statistics accumulated in a momentum buffer. The paper acknowledges this is "only a weak duration prior" (Section 4.3), but does not discuss whether these priors could overfit to dataset-specific duration distributions rather than capturing generalizable temporal statistics.

### Trivial
- **Citation inconsistency in Table 1**: ActFusion is cited as "Guo et al. (2024)" in the table rows but is introduced as "Actfusion (Gong et al., 2024)" in the text (line 66). Should be corrected for consistency.

## Nice-to-Haves
- Reporting standard deviations across splits would improve rigor, especially for 50Salads (only 50 videos, 5 splits) where split-to-split variance can be substantial.
- A brief quantification of annotation cost (transcripts vs. frame-level labels) would substantiate the paper's motivating claim about annotation efficiency.
- Failure mode categorization (e.g., missed action insertions, boundary shifts, duration errors) with quantitative breakdown would strengthen the qualitative analysis beyond the two examples in Figure 3.

## Removed Points
These points are flagged to be removed, treat them with caution:
- *Grammar issue in Eq. 4*: This is a presentation/formatting nitpick that does not affect the paper's validity. Removed.
- *Table 4 duplication (lines 249-257 and 259-269 are identical)*: The critic notes this is explicitly a parsing artifact, not an author error. Removed.
- *"Guo et al. (2024) refers to a different paper" as a fatal error*: The critic speculates that the table citation is wrong. Kept as a trivial citation inconsistency — we cannot verify the full reference list.
- *No variance reporting*: Moved to Nice-to-Haves. Many LTA papers report single-run or split-averaged results without confidence intervals; this is not a standard requirement in the field.
- *Annotation cost analysis*: Moved to Nice-to-Haves. The paper's contribution is methodological, not an annotation study.
- *Failure analysis categorization*: Moved to Nice-to-Haves. While useful, the paper already provides qualitative examples and acknowledges duration estimation as a challenge.
- *Compute time analysis*: Generic request applicable to almost any paper; removed.
- *"No comparison to a minimal transcript-based baseline" framed as a methodological gap requiring all components stripped*: The paper addresses component contributions through individual ablations. Kept as Minor with softened framing requesting a combined baseline.

## Novel Insights
The most novel insight emerging from the review process is that transcript-based supervision's effectiveness appears strongly modulated by the temporal regularity of the underlying activity domain. The stark Breakfast/50Salads asymmetry — where the method beats all supervised baselines on one dataset but trails by large margins on the other — suggests that procedural rigidity is a limiting condition for transcript-only LTA. This is not merely an evaluation observation but a substantive constraint on the approach's operating regime. The paper's failure to diagnose this empirically leaves open a key scientific question: what specific properties of activity structure (action density, transition frequency, duration variability) determine when transcript supervision suffices?

## Suggestions
- Run a controlled experiment on Breakfast that systematically degrades temporal regularity (e.g., by subsampling or shuffling transcript action order) to quantify how procedural structure relates to alignment quality and downstream anticipation accuracy. This would transform the current post-hoc observation into a scientific finding.
- Either extend EGTEA evaluation to the full 106-class verb-noun setting or explicitly frame the current results as a preliminary verb-only study with clear limitations stated in both the results section and the conclusion.
- Include stochastic baselines (e.g., Abu Farha & Gall, 2019; Zatsarynna et al., 2024) in Table 1 alongside TbLTA* or move TbLTA* to a separate table for transparent comparison.

---

**Calibration anchors referenced:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| `N581Nje6fH.md` (Long Horizon Episodic Decision Making) | 1.50 | R1 | Far below TbLTA — fundamentally flawed |
| `3ZdGSTxKuy.md` (Harry Potter OOD) | 2.00 | R1 | Far below TbLTA — weak methodology |
| `MI0UiWeqOl.md` (Poly-Autoregressive) | 2.33 | R1 | Far below TbLTA |
| `PageLgQlXz.md` (Dual-level Prototypes STAL) | 4.00 | R1 | Below TbLTA — weaker contribution |
| `DE2RMJVjgI.md` (Fine-grained Separation TAL) | 4.25 | R1 | Below TbLTA — narrower scope |
| `dl34rOnbqJ.md` (Actions-to-Action) | 4.40 | R1 | Clearly below TbLTA — core ablation fails, weak novelty |
| `HCoSsULNxG.md` (Sparse Skill Extractor) | 4.75 | R2 | Below TbLTA — overclaiming, evaluation gaps |
| `sEARCNzhrP.md` (InterAct) | 5.00 | R2 | Below TbLTA — limited novelty, insufficient ablations |
| `Y7jJN0VQ4y.md` (Continual Learning WS-VAD) | 5.71 | R1 | Similar tier — accepted but borderline |
| `GQgPj1H4pO.md` (VSNLS) | 6.00 | R1+R2 | Comparable — first weakly-supervised X, similar evaluation breadth |
| `HEXtydywnE.md` (LASER) | 6.00 | R1+R2 | Slightly above TbLTA — more polished evaluation |
| `Bb21JPnhhr.md` (AntGPT) | 6.25 | R1+R2 | Above TbLTA — SOTA across more benchmarks, fewer caveats |
| `f3CdjpPkSq.md` (Action Sequence Augmentation) | 6.50 | R1 | Above TbLTA |
| `14fFV0chUS.md` (TRACE) | 6.75 | R1 | Above TbLTA |
| `9Cu8MRmhq2.md` (Norton) | 8.00 | R1 | Far above TbLTA |

TbLTA sits between the 5.00-5.25 rejected papers and the 6.00 accepted papers — closer to VSNLS (6.00) in ambition and structure but pulled down by the undiagnosed 50Salads gap and the EGTEA simplification. Score: 5.5.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>