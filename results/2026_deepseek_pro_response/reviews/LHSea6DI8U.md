Now I have enough anchors to place STBP precisely. Let me finalize:

**Anchor comparisons:**
- **EAC (6.75, Accepted)**: STBP directly improves over EAC by 21-22% on traffic, has a more sophisticated backbone, more comprehensive experiments. STBP is clearly stronger.
- **MISA (6.50, Accepted)**: General CL with frozen backbone + prompts. STBP has more architectural novelty and stronger domain results. STBP is stronger.
- **Budgeted Online CL (7.50, Accepted)**: Clean evaluation framework, thorough baselines, principled budget formulation. STBP's domain results are stronger but Budgeted CL's evaluation is more rigorous.
- **FITS (8.00, Accepted)**: Elegant simple method (frequency-domain time series), all 8s. STBP is more complex and has the forgetting evaluation gap preventing it from reaching this tier.

STBP lands at **7.0**: clearly above EAC (6.75) thanks to better results and more sophisticated architecture, but below Budgeted Online CL (7.50) because the forgetting measurement gap and FreNet isolation issue are material evaluation shortcomings.

Now let me write the final review.

## Summary
STBP proposes a continual spatio-temporal forecasting framework combining a frozen frequency-domain backbone (FreNet + dual-stream linear graph attention) with an incrementally expandable contextual pattern bank. After joint training in period 1, the backbone is frozen and only the pattern bank adapts via parameter expansion and prompt-based gating, aiming to mitigate catastrophic forgetting. Experiments on three streaming datasets show 21-22% MAE improvement over the best CSTF baseline on traffic data, with more modest gains on air quality.

## Strengths
- **Substantial and consistent empirical gains on traffic data**: 21.44% and 21.93% MAE reduction over EAC on PEMS-Stream and CA-Stream, with consistent margins across all horizons and metrics (Table 1).
- **Well-structured ablation study**: Retrain and Online variants isolate the pattern bank's contribution; w/o Backbone and w/o DLGA test backbone components. All variants cause significant degradation (Figure 4), confirming components are independently necessary.
- **Principled efficiency gain via DLGA**: Linear attention reformulation (Equation 9) reduces spatial complexity to O(N) while incorporating the pattern bank as a second key stream. Validated on synthetic data (Figure 8).
- **Pattern bank autonomously learns meaningful clusters**: t-SNE (Figures 3, 6) shows natural clustering where nodes within clusters share temporal dynamics, and new nodes are absorbed into existing clusters.
- **Few-shot robustness**: Table 2 shows strong performance with only 10% training data in later periods.

## Weaknesses

### Fatal
None.

### Major
- **No direct measurement of catastrophic forgetting despite it being a central claim.** The abstract, introduction (Challenge ❸), and conclusion all position STBP as mitigating catastrophic forgetting, yet evaluation reports only *average* performance across all periods (Table 1, line 142). The ablation variants (Retrain, Online) and the frozen-backbone design provide structural and indirect evidence, but standard continual-learning practice requires per-period performance trajectories, backward transfer, or at minimum performance on early periods after learning later ones. Without such metrics, a model could achieve good average performance by adapting aggressively to recent periods while performing poorly on early ones — precisely the failure mode continual learning is meant to prevent. The claim that STBP specifically *mitigates catastrophic forgetting* (rather than simply being a strong model on average) is not directly verified.

- **FreNet's contribution to distributional-drift mitigation is not isolated.** FreNet is introduced as addressing distributional drift (Section 4.3, line 112: "FreNet is designed to capture temporal correlations while emphasizing stable components...which are more resilient to distributional changes"), and the paper claims it makes "a notable contribution" (line 262). The ablation tests w/o Backbone (removes FreNet+DLGA together, replaced with CNN+GCN) and w/o DLGA (keeps FreNet). While the gap between these in Figure 4 implicates FreNet indirectly, there is no dedicated ablation isolating FreNet (e.g., replacing it with a TCN/RNN of comparable capacity). The specific claim that frequency-domain processing mitigates distributional drift is asserted but not directly tested.

### Minor
- **AIR-Stream gains are substantially weaker and undiscussed.** STBP achieves only 2.35% MAE improvement on AIR-Stream vs. 21-22% on traffic datasets; RMSE is essentially tied with EAC (37.76 vs. 37.83). The "general backbone" framing warrants discussion of this domain gap.
- **Three-bank design lacks ablation.** The pattern bank uses three parameter groups (P^(0) for gating, P^(1) for scaling, P^(2) as attention key) with no comparison against simpler configurations.
- **Unsubstantiated privacy claim.** Line 104 asserts the pattern bank "offers advantages in privacy protection" without any privacy analysis or evidence.

### Trivial
- Figure 8 uses scatter plots for efficiency; a table would allow more precise numerical comparison.

## Nice-to-Haves
- An offline-training upper bound (full STBP on all periods simultaneously) to contextualize the continual-learning performance sacrifice.
- Varying which period is used for initial backbone training to test whether the frozen knowledge is genuinely general.

## Removed Points
These points are flagged to be removed, treat them with caution.

- *Harsh Critic: "what if the first incremental period is not representative?"* — REMOVED. Speculative; not tied to any concrete flaw in the paper.
- *Harsh Critic: "paper does not discuss how prompt-based guidance relates to AdaLN or FiLM-style conditioning"* — REMOVED per hard rules: do not mention missing related works without external verification.
- *Harsh Critic: "Table 1 is corrupted by the PDF parser"* — REMOVED. Parser artifact, not an author error.
- *Harsh Critic: "no discussion of how many incremental periods each dataset contains... appendix likely contains them"* — REMOVED per hard rules: do not criticize missing appendix content.
- *Harsh Critic: "no hyperparameter sensitivity analysis for number of pattern banks (3)"* — REMOVED. The paper includes sensitivity for feature dimension d (Figure 5); demanding sensitivity for every hyperparameter is excessive.
- *Strength Finder: "FreNet is theoretically well-justified for mitigating distribution drift"* — REMOVED as a standalone strength. While the motivation is plausible, this claim conflicts with the verified Major weakness that FreNet's contribution is not empirically isolated.

## Novel Insights
The dual-stream linear graph attention (DLGA) is a genuinely clever synthesis: adding the pattern bank as a second key stream in a linear attention formulation (Equation 9) simultaneously achieves O(N) spatial complexity and integrates stored knowledge into correlation computation. The reformulation φ(Q)(φ(K)ᵀV + φ(P^(2))ᵀV) cleanly separates input-driven and prompt-driven attention contributions. This design pattern could generalize beyond spatio-temporal forecasting to other incremental learning scenarios where a frozen backbone needs to incorporate expanding knowledge.

## Suggestions
- Add per-period MAE/RMSE trajectories for STBP, EAC, and the Retrain baseline — the single highest-impact addition, directly addressing the forgetting measurement gap.
- Add a "w/o FreNet" ablation replacing FreNet with a TCN/RNN of comparable capacity while keeping DLGA and the pattern bank unchanged.
- Discuss the AIR-Stream domain gap honestly: acknowledge smaller gains and analyze potential reasons (e.g., weaker periodicity in air quality making frequency-domain filtering less beneficial).

---

### Anchor Summary

| Paper | Path | Avg Score | Round | Comparison |
|-------|------|-----------|-------|------------|
| Forward Explanation (CF) | ZyMXxpBfct.md | 1.50 | R1 | Unrelated theoretical CL paper; far below STBP |
| Hyperspherical replay | A1JdcLawSu.md | 3.00 | R1 | General CL method; STBP substantially stronger |
| Replay can provably increase forgetting | kf9phcBvQ5.md | 3.00 | R1 | Theoretical CL; STBP stronger |
| CAN | SI6zocV2SS.md | 1.50 | R1 | Architecture for CL; STBP far stronger |
| KITS | mkjKqeBXkt.md | 5.67 | R1 | Spatio-temporal kriging; STBP has stronger results and fewer fundamental issues |
| Online Continual Graph Learning | 4sJJixGIZX.md | 5.00 | R1 | Related problem; STBP stronger |
| **EAC (Expand and Compress)** | FRzCIlkM7I.md | 6.75 | R1,R2 | Direct baseline; STBP achieves 21-22% better results with more sophisticated architecture |
| Mayfly | n7Sr8SW4bn.md | 7.33 | R1,R2 | Graph stream summarization; comparable novelty level |
| **MISA** | V6uxd8MEqw.md | 6.50 | R2 | Prompt-based CL with frozen backbone; STBP has more novelty and stronger results |
| TiC-CLIP | TLADT8Wrhn.md | 6.25 | R2 | Continual training of CLIP; different domain |
| Whole-Brain Neural Activity | 4UXIGATUTj.md | 6.33 | R2 | Different domain |
| **Budgeted Online CL** | dOAkHmsjRX.md | 7.50 | R2 | Clean CL framework with thorough evaluation; STBP has stronger domain results but Budgeted CL has more rigorous evaluation |
| **FITS** | bWcnvZ3qMb.md | 8.00 | R1,R2 | Elegant frequency-domain time series; STBP is more complex with evaluation gaps |
| Deep Temporal Graph Clustering | ViNe1fjGME.md | 7.33 | R2 | Different task (clustering); comparable tier |

**Round 1 bracket**: 6.5–8.0
**Round 2 narrowing**: Compared against EAC (6.75, below), MISA (6.50, below), Budgeted Online CL (7.50, slightly above), and FITS (8.00, above). STBP lands at 7.0 — clearly above EAC/MISA but with evaluation gaps preventing it from reaching Budgeted CL/FITS territory.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>