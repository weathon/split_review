Now let me perform calibration searches to anchor the score.Round 1 bracket: **5–7**. The paper clearly outperforms the low anchors (score ≤ 3) and sits below the high anchors (score = 8). Now narrowing within the bracket.Let me read a few of the most comparable anchors:Now I have enough information to write the final consolidated review.

---

## Summary
This paper proposes two modifications to the Vavilala et al. (ICCV 2023) indoor scene primitive decomposition system: (1) *negative* boolean primitives via CSG set difference, allowing the geometry to be represented as union-of-positives minus union-of-negatives, and (2) ensemble of regressors with varying numbers of primitives selected via a refine-then-choose protocol. Supporting engineering improvements include a biased inside-sampling loss, annealing of loss weights, and camera-aware data augmentation. On the standard NYUv2 benchmark the proposed system achieves a ~30% relative improvement in AbsRel over the prior SOTA.

---

## Strengths

- **Refine-then-select decisively outperforms select-then-refine**: Table 2 (tab:ft_gt) shows that R→S reduces AbsRel from 0.076 to 0.066 for the positive ensemble and from 0.076 to 0.064 for the pos+neg ensemble. This clean comparison confirms that the fitting landscape is rife with local minima and start-point quality is a poor predictor of final solution quality — a non-obvious and useful insight.

- **Consistent, large gains over two SOTA baselines on multiple metrics**: Table 3 (tab:auc_gt) shows that the pos+neg ensemble achieves AUC@50 of 91.5% and mean distance of 18.8 cm versus 86.9% / 26.6 cm for Vavilala et al. and 77.2% / 20.8 cm for Kluger et al. — improvements are consistent across six AUC metrics, not just AbsRel.

- **Every individually trained network already beats the prior SOTA**: Table 2 shows the weakest individual network (K=12, K^-=0, refined) achieves AbsRel 0.086 versus Vavilala's 0.098, demonstrating that the engineering improvements (augmentation, annealing, biased loss) are effective in isolation.

- **Honest self-assessment**: The paper explicitly notes "on their own, negative primitives produce small improvements in accuracy" and acknowledges the fitting difficulty and compute cost. This intellectual honesty strengthens trust in the remaining claims.

- **Camera-aware augmentation is an underappreciated but effective contribution**: Table 5 (tab:aug) shows augmentation reduces AbsRel from 0.080 to 0.074 for the K=24 network, with a correctly-noted tradeoff on normal accuracy. The paper explains the correct implementation accounting for calibration, which prior work missed.

---

## Weaknesses

### Fatal
None.

### Major

- **Ensemble size is confounded with negative-primitive contribution (the central evidential gap)**: The "pos" ensemble contains 5 networks (K∈{12,16,20,24,28}, K^-=0); the "pos+neg" ensemble contains 15 networks (the same 5 plus 10 with K^-∈{1,2}). Table 3 and Table 2 show the "pos" vs. "pos+neg" comparison, with pos+neg achieving, e.g., AUC@5 of 48.4 vs. 47.3 for pos (Table 3) and AbsRel 0.064 vs. 0.066 (Table 2). These improvements cannot be cleanly attributed to negative primitives: they could equally reflect the benefit of having three times as many ensemble members, since the expected minimum of N independent draws decreases monotonically in N. This matters because Contribution #1 is *negative primitives*. Within each fixed K, K^-=0 consistently outperforms K^-=1 and K^-=2 for single refined networks across both Table 1 and Table 2. The paper acknowledges this ("on their own, negative primitives produce small improvements") but then pivots to the ensemble result — exactly the quantity the confound affects. The obvious missing control is a 15-member positive-only ensemble (five K values × three random seeds) versus the 15-member mixed ensemble. This single experiment would resolve whether negative primitives or ensemble size drives the "pos+neg" gain, and its absence leaves the paper's first and most prominently labeled contribution inadequately evidenced.

### Minor

- **Selection on depth then evaluation on depth inflates the AbsRel headline figure**: The refine-then-select protocol chooses among 5 or 15 refined solutions by comparing rendered depth to GT depth; the primary reported metric is AbsRel of that same quantity. The expected minimum AbsRel across N draws from a distribution decreases monotonically in N, so part of the AbsRel improvement is a statistical selection artifact ("min of multiple draws") rather than a genuine representation gain. The other metrics (normals, segmentation, AUC) also improve — confirming the overall effect is real — but the absolute magnitude of the AbsRel gains, which the abstract foregrounds as ">30% relative error," is partially inflated by this protocol. The paper would be more precise if it acknowledged this and led with the AUC metrics (which use a different scoring axis) as the primary evidence of improvement.

- **Biased sampling loss claim slightly overstated**: The text (Section 4) says the $L_{inside}$ loss is "clearly helpful across all numbers we tried," but Table 4 (tab:bias) immediately shows that for K=20, K^-=1, the best AbsRel is achieved at w_inside=0.0 (0.080 vs 0.083 at w_inside=0.1). The paper then correctly notes this and sets w_inside=0.1 as a compromise, but the initial phrasing contradicts the data. Minor textual inconsistency, but should be corrected.

### Trivial

- The claim in the text that "negative primitives are selected from the ensemble about half the time" (referencing Fig. 4) is imprecise. Fig. 4 shows how often each ensemble member is selected, not specifically whether a member with active negative primitives is selected. Table 2 (avg K^-=0.80 per selected image) is the cleaner statistic and should be the primary reference for this claim.

---

## Nice-to-Haves

- A pruned ensemble ablation (e.g., 3 or 7 ensemble members rather than 15) would tell readers whether most of the gain concentrates in the first few ensemble members or distributes broadly — useful for practitioners concerned with the ~14-minute inference time.
- Characterizing which scene types or geometric conditions cause the selector to prefer negative primitives (e.g., presence of arched doorways, partial occlusions, concave furniture) would deepen the motivation for the CSG representation beyond its current average-K^- statistic.
- Variance/confidence intervals across the 654-image NYUv2 test set would help readers judge whether small differences (e.g., AbsRel 0.064 vs. 0.066) are statistically reliable given the dataset size.
- An ablation training both positive and negative primitives from scratch (no curriculum) would verify the claimed necessity of the pretraining schedule beyond "early experimentation showed."

---

## Removed Points
*These points are flagged to be removed; treat them with caution.*

- **Claim that negative primitive contribution in the ensemble disappears**: The harsh critic suggests the improvement "could entirely reflect the simple benefit of having three times as many ensemble members." This is correctly flagged as an evidential gap (retained as Major above), but the critic goes further in sometimes framing this as invalidating the result. The result itself (pos+neg beats pos) is real; only the attribution is uncertain. The conclusion that "the paper's first contribution is entirely vacuous" is too strong and was not retained.

- **Attribution of individual-network improvements over Vavilala et al. is unclear**: The critic notes that augmentation, biased loss, and annealing are bundled together so the 0.098→0.086 gap cannot be assigned to any single change. While true, the paper presents ablations for augmentation (Table 5) and biased loss (Table 4) individually. The absence of a joint full-factorial ablation is standard for this type of applied methods paper and does not rise to a meaningful weakness. Removed.

- **Absence of curriculum training ablation**: The paper states "early experimentation showed" the curriculum (pretrain positive-only, then introduce negatives midway) is beneficial. The critic flags that no ablation supports this. While an ablation would be nice, reporting a training design choice based on experience without a formal ablation is normal practice in this field. Demoted to Nice-to-Have.

- **Compute cost**: The critic notes ~14 minutes per image is high. The paper explicitly acknowledges this in its Limitations section. This is not a scientific flaw and is demoted to a note for practitioners.

---

## Novel Insights
The most genuinely novel observation in this paper is the empirical demonstration that *refine-then-select strictly dominates select-then-refine* in a convex primitive fitting problem. This is an insight about the topology of the optimization landscape: independently refined predictions from diverse start points are more informative than picking the best start point and refining once. This generalizes beyond the specific NYUv2 setting and supports a broader principle that ensemble diversity should be realized in the refinement dimension, not just the initialization dimension. The paper's own data in Table 2 (S→R AbsRel=0.076 for pos, vs. R→S AbsRel=0.066) provide clean empirical backing for this principle.

---

## Suggestions

1. **Run the 15-member positive-only ensemble control** (5 K-values × 3 random seeds). This single experiment either confirms negative primitives' contribution or correctly reframes the narrative around ensemble size, and it resolves the paper's most significant evidential gap before publication.
2. **Reframe the primary metric** to lead with AUC-based results (Table 3), which are not subject to the depth-selection inflation, and present AbsRel as a corroborating metric.
3. **Correct the biased loss claim** from "clearly helpful across all numbers we tried" to "helpful in the low-K regime but neutral or slightly harmful when K is large," which matches the data in Table 4.
4. **Add a brief analysis of which scene types prefer negative primitives**, even a simple breakdown by NYUv2 scene category, to strengthen the first contribution's qualitative story.

---

## Score and Decision

**Calibration anchors summary:**

| Paper | Avg Score | Round | Comparison |
|---|---|---|---|
| TCSaLeANpN (SYNBUILD-3D) | 3.00 | 1 (low) | Far below; dataset paper with less methodological content |
| MqvQUP7ZuZ (DC3DO) | 3.00 | 1 (low) | Far below; broken abstract, weak methodology |
| h1sFUGlI09 (DFormer RGBD) | 5.67 | 1 (mid) | Somewhat comparable in domain (RGBD); DFormer has a pretraining novelty, slightly above in novelty breadth |
| DtFCIfvAFc (Gaussian-Det) | 5.25 | 1 (mid) | Less topically relevant; comparable quality level |
| gINO3tfVEP (TSF-Depth) | 5.50 | 1 (mid) / 2 | Comparable domain; similar level of incremental contribution |
| 9SmukfhJoF (3DGS-Det) | 5.25 | 1 (mid) | Similar quality, less related topic |
| 5UKrnKuspb (NeuralPlane) | 8.00 | 1 (high) | Much stronger; unified neural field approach with multi-view input, broader scope |
| P4o9akekdf (NoPoSplat) | 8.00 | 1 (high) | Much stronger; novel no-pose Gaussian splatting |
| HBEjrlu7Aa (Object-level Data Aug) | 5.67 | 2 | Similar level; augmentation focus, comparable evidence quality |
| mVOz28mPHr (GA-Planes) | 6.00 | 2 | Comparable; has theoretical claims but unclear method, similar empirical strength |
| llSiIJosDj (Instance Completion) | 7.00 | 2 | Stronger; novel problem formulation with broader applicability |
| P1ANzoGg3W (H2O-SDF) | 6.50 | 2 | Comparable; two-phase indoor reconstruction with similar ablation depth |
| DugT77rRhW (Room Layout Reconstruction) | 6.75 | 2 | Comparable; solid empirical results on a well-defined problem, accepted |
| TwBY17Hgiy (Multi-task 3D-Aware Reg.) | 6.00 | 2 | Comparable; methodologically sound, incremental on depth+segmentation |

**Round-1 bracket**: 5–7.

**Round-2 narrowing**: The paper is stronger than the ~5.25–5.67 anchors (DFormer, 3DGS-Det, TSF-Depth) because it delivers a more focused contribution with larger empirical gains and more targeted ablations. It is weaker than the 7.0–8.0 anchors (NeuralPlane, Instance Completion, NoPoSplat) because the scope is narrower, it builds directly on one prior paper, and the negative primitive contribution is partially confounded. It is most comparable to H2O-SDF (6.5, accepted) and DugT77rRhW (6.75, accepted): solid, honest papers with clear empirical validation on established benchmarks, one notable methodological gap each, accepted at their venues. The paper under review has one more significant evidentiary gap (ensemble-size confound) than H2O-SDF but arguably cleaner ablations of its engineering components. Placing it slightly below those anchors at **6.0** is appropriate: genuinely above borderline, but not as clean as the 6.5–7 accepted papers whose contributions are all individually well-evidenced.

**Axes assessment:**
- *Originality*: Moderate — incremental extensions (ensembling + negative primitives) to Vavilala et al., both individually well-motivated.
- *Importance of research question*: Moderate — primitive decomposition of real scenes is a long-standing problem; practical progress matters.
- *Claims supported*: Mostly yes for ensembling; partially for negative primitives (evidential confound).
- *Soundness of experiments*: Good overall; thorough ablations on engineering choices; one key missing control.
- *Clarity of writing*: Good; honest about limitations.
- *Value to community*: Positive; practical improvements on a standard benchmark.

**Final score: 6.0 — Accept**

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>