Now I have a thorough understanding of the paper and the calibration anchors. Let me write the consolidated review.

## Summary

This paper proposes STBP, a continual spatio-temporal forecasting framework that pairs a frequency-domain backbone (FreNet) with linear-complexity graph attention (DLGA) and an expandable, trainable contextual pattern bank that interacts via prompt-based gating. The backbone is frozen after initial training; only the pattern bank is updated in later incremental stages. Experiments on three real-world streaming datasets show STBP outperforms existing CSTF methods substantially on traffic datasets (~21% MAE reduction over EAC on PEMS-Stream and CA-Stream) and modestly on an air-quality dataset.

## Strengths

- **State-of-the-art accuracy on traffic streaming datasets**: STBP achieves the lowest MAE, RMSE, and MAPE across all metrics and horizons on PEMS-Stream and CA-Stream, with an average MAE reduction of 21.44% and 21.93% over the best CSTF baseline (EAC). The gains are consistent across forecasting horizons (3, 6, 12 steps) and backed by standard deviation reports.

- **Effective catastrophic forgetting mitigation via frozen backbone + expandable pattern bank**: The ablation study (Figure 4) shows that removing the pattern bank ("Retrain" and "Online" variants) causes MAE to rise from ~12.3 to ~20+ on PEMS-Stream, and the "w/o Backbone" variant (replacing FreNet+DLGA with CNN+GCN) likewise degrades performance sharply. This pair of ablations cleanly validates the necessity of both components.

- **Scalability via linear-complexity spatial modeling**: The Dual-Stream Linear Graph Attention (DLGA) reduces complexity from O(N²) to O(N) while incorporating the pattern bank as an additional key stream. The efficiency study (Figure 8) confirms that on a toy dataset, the O(N) version uses substantially less GPU memory and training time than the O(N²) variant, while STBP overall incurs only minimal overhead compared to lighter baselines like EAC.

- **Robustness under extreme data scarcity**: In the few-shot setting (Table 2, 10% training data), STBP outperforms all baselines by a wide margin (e.g., PEMS-Stream MAE 13.58 vs. next best EAC 16.13), demonstrating that the backbone and pattern bank jointly extract reusable knowledge from limited new data.

- **Self-organized, interpretable node representations**: The t-SNE visualization of the pattern bank (Figures 3 and 6) shows that, without explicit clustering constraints, the bank forms distinct clusters corresponding to nodes with similar temporal dynamics, and new nodes are correctly grouped into existing clusters. This offers an interpretability advantage over black-box prompt methods.

## Weaknesses

### Major

- **Missing parameter count comparisons**: The paper does not report the number of trainable parameters for STBP versus any baseline. Since STBP's backbone (FreNet + DLGA + pattern bank with N×d×3 parameters) is more complex than typical CSTF backbones, it is impossible to assess whether the observed performance gains stem from the proposed continual learning strategy or simply from higher model capacity. Reporting per-model parameter counts and, ideally, a capacity-controlled experiment (e.g., scaling up baselines to match STBP's size) would make the comparison fully informative.

### Minor

- **Pattern bank update protocol could be clarified**: Section 4.2 states "Only the expanded contextual pattern bank P'_τ is fine-tuned during training" where P'_τ = P_{τ-1} ∥ ΔP_τ. The text strongly implies that the *entire* bank (old rows + new rows) is fine-tuned and that "only" contrasts with the frozen backbone, not with the old rows. However, the phrasing "the expanded contextual pattern bank" could be read by some as "only the newly added part." A one-sentence clarification (e.g., "The entire pattern bank P'_τ is fine-tuned while the backbone remains frozen") would eliminate ambiguity and would also make room for a useful discussion of whether updating old rows causes any forgetting on old nodes.

- **Modest improvement on AIR-Stream tempers the generality claim**: On AIR-Stream, STBP's average MAE is 23.64 vs. the best baseline (EAC) at 24.21 — a 2.35% improvement. While this is not noise (the difference exceeds the reported std of both methods), it is notably smaller than the 21%+ gains on the two traffic datasets. The paper acknowledges this briefly but should temper the "general superiority" framing or discuss why air quality presents a harder case for the method (e.g., different temporal dynamics, fewer nodes, different sampling rate). This does not undermine the core contribution, but the claim of across-the-board superiority would benefit from qualification.

- **Linear attention normalization is not discussed**: Equation 9 presents the dual-stream linear attention as ϕ(Q)(ϕ(K)ᵀV + ϕ(P)ᵀV). Standard linear attention (Katharopoulos et al., 2020) includes a normalization denominator (the sum of attention weights) to ensure proper scaling. The paper mentions that ϕ(·) uses a Softmax approximation and refers to the appendix, but does not state whether normalization is applied and how the dual-stream addition interacts with it. This should be clarified in the main text.

- **No direct evaluation of distributional drift handling**: The paper claims FreNet "handles distributional drift" by extracting stable low-frequency components, but the ablation replaces the entire backbone (not just FreNet), so it does not isolate this capability. A targeted experiment — e.g., injecting synthetic drift and measuring whether FreNet's frequency-domain processing degrades more gracefully than a time-domain alternative — would substantiate the claim.

### Trivial

- None that merit listing beyond those already covered above.

## Nice-to-Haves

- Include a controlled baseline with the same backbone but a simpler replay strategy (e.g., storing historical representations rather than learnable parameters) to further isolate whether the parameter bank's structure is crucial or just its capacity.
- Provide per-period FLOPs or training-time breakdowns to make the efficiency comparison more granular.

## Removed Points

- **The harsh critic's point #1 about "ambiguity in which pattern bank parameters are updated"** is overblown. The paper writes "Only the expanded contextual pattern bank P'_τ is fine-tuned during training" where P'_τ = P_{τ-1} ∥ ΔP_τ. The natural reading is that the concatenated bank (old+new rows) is fine-tuned, and "only" contrasts with the frozen backbone. While a clarification would help, the framing as a "critical issue" that "contradicts the paper's claim" is a misreading.
- **Table formatting artifact critique**: The harsh critic notes "multiple numbers per cell" in Table 1 — this is a parser artifact from PDF extraction, not an author error.
- **Ablation criticism about w/o Backbone not isolating specific design choices**: The ablation is designed to validate that both components are necessary, not to attribute credit to every sub-module. The paper separately ablates DLGA (Figure 4, w/o DLGA), which does provide finer attribution. This criticism demands scope the paper never claimed.
- **Strength Finder's strengths that are generic** (e.g., "this paper addressed an important problem") have been dropped.
- **The harsh critic's suggestion about "statistical significance test for AIR-Stream"** is unnecessary — the improvement (23.64 vs 24.21) is 1.3× the larger std, making a significance test likely positive but not the standard practice in this area.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Add a table comparing parameter counts for STBP and all baselines in the main comparison.
2. Clarify in Section 4.2 whether the entire pattern bank or only the new rows are fine-tuned, and briefly discuss the stability-plasticity trade-off this creates.
3. Add a sentence in Equation 9's description about whether normalization is applied and how the dual-stream addition preserves or modifies the standard linear attention scaling.
4. Temper the "generally superior" framing by acknowledging that AIR-Stream gains are smaller and speculating on why (e.g., different temporal resolution, domain characteristics).

## Score and Decision

**Calibration Report**

Round 1 — Bracketing:
- Weak anchors (score < 3.5, avg 2.5–3.0): trajectory forecasting, RL for traffic, LLM benchmarks → STBP is clearly stronger.
- Middle anchors (3.5–7.5): EAC (6.75), KITS (5.67), Unifying Long/Short ST (5.40), SKI-CL (5.33) → STBP is comparable to EAC, better than the others.
- Strong anchors (> 7.5, avg 8.0): FITS, radar nowcasting, PhyMPGN, TimeMixer++ → STBP is not at this level of novelty or impact.

Round 1 bracket: [5.5, 7.5].

Round 2 — Narrowing:
- Queries in (4.5, 6.5): RePST (5.50), SVQ (6.00), CL with vision-language (5.00), TFPS (5.40) → all weaker than STBP.
- Queries in (6.0, 7.5): EAC (6.75), MS-GODE (6.25), Mayfly (7.33), N-ForGOT (6.25) → STBP is comparable to EAC and moderately stronger than MS-GODE and N-ForGOT, but not at Mayfly's level.

Final comparison vs. EAC (6.75, the closest anchor):
- STBP has a more sophisticated backbone and stronger traffic results (21% vs. EAC).
- STBP has some clarity issues (pattern bank update, linear attention normalization) that EAC's reviews did not flag.
- STBP's AIR-Stream results are weaker.
- Overall, STBP is of comparable quality to EAC, perhaps slightly below due to the clarity issues and modest AIR-Stream gains.

Final score: **6.5**

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>