Now I have all the context I need. Let me write the final consolidated review.

**Round 1 bracket:** After reviewing the calibration results, I place this paper between the weak anchors (~2-3 for flawed spatio-temporal papers) and the strong anchors (8+ from unrelated domains), most likely in the 5.5-7.5 range. The most topically relevant anchor is SNIP (5.33, Reject), which addresses expanding-node ST forecasting with prompting.

**Round 2 narrowing:** The MMCKM paper (6.00, Accept Poster) is a good solid anchor in traffic ST forecasting. The STBP paper is stronger than both SNIP (worse weaknesses: synthetic datasets, single expansion stage) and comparable-to-slightly-stronger than MMCKM (better empirical gains, more practical problem). 

**Final position:** Above both SNIP (5.33) and comparable or slightly above MMCKM (6.00). Score 6.5 — a solid Accept paper with genuine contributions but some presentational weaknesses that keep it from the top tier.

---

## Summary

This paper proposes STBP, a framework for continual spatio-temporal forecasting (CSTF) that combines a frequency-domain backbone (FreNet) with a dual-stream linear graph attention mechanism (DLGA) and an expandable contextual pattern bank. The backbone captures stable temporal components and dynamic spatial correlations, while the pattern bank handles node-level heterogeneity and mitigates catastrophic forgetting via prompt-based gating and parameter expansion. On three real-world streaming datasets (PEMS-Stream, CA-Stream, AIR-Stream), STBP achieves substantial improvements over state-of-the-art CSTF baselines, particularly on traffic datasets where MAE reductions exceed 20%.

## Strengths

- **Strong and well-supported empirical results on traffic datasets**: Table 1 shows STBP reduces average MAE by 21.44% on PEMS-Stream and 21.93% on CA-Stream versus the best CSTF baseline (PECPM/EAC), with consistent gains across all horizons and metrics. These are large, unambiguous improvements supported by standard deviation reporting.

- **Novel and well-motivated architecture design**: The combination of a frequency-domain network (FreNet, Eq. 6) to handle distributional drift, a dual-stream linear graph attention mechanism (DLGA, Eq. 7–9) that achieves O(N) complexity, and an expandable contextual pattern bank for continual adaptation is a coherent solution to the four challenges the paper identifies. The linear attention with pattern-bank integration (using P_τ^(2) as an additional key) is a clean way to incorporate learned knowledge without quadratic cost.

- **Interpretable qualitative evidence**: The t-SNE visualization (Figures 3 and 6) shows that the contextual pattern bank autonomously learns to cluster nodes by shared temporal dynamics, with new nodes correctly assigned to existing clusters. This provides direct empirical support for the claim that the bank captures node-level heterogeneity and relevance, going beyond prior prompt-based CSTF methods.

- **Strong few-shot performance**: Table 2 demonstrates STBP achieves MAE of 13.58 on PEMS-Stream with only 10% data per period, outperforming EAC (16.13) by 15.8%, validating the claim that the frozen backbone + expandable pattern bank retains general knowledge and adapts efficiently with limited data.

- **Efficiency demonstrated empirically**: Figure 8 confirms that the linear attention approximation reduces memory and time relative to full attention, and the pattern bank adds only linear cost as nodes grow. The code is provided.

## Weaknesses

### Major
None.

### Minor

1. **Imprecise reporting of ablation results**: Figure 4 and the accompanying table report approximate values with tildes (e.g., "~15", "~20") rather than exact numbers with standard deviations, as is done for the main results in Table 1. While the relative trends are clear, the lack of precision weakens the quantitative evidence for the contribution of each component. The authors should provide exact numerical values.

2. **Mixed results on AIR-Stream not fully discussed**: STBP's improvement on AIR-Stream is modest (2.35% MAE reduction vs. EAC, average MAE 23.64 vs. 24.21), and on RMSE at horizons 6 and 12, EAC is marginally better (RMSE 6: STBP 39.81 vs. EAC 39.63; RMSE 12: STBP 44.97 vs. EAC 44.65). The paper states STBP "outperforms all competing models" without acknowledging this RMSE pattern. While MAE is a reasonable primary metric and the average RMSE still favors STBP (37.76 vs. 37.83), the inconsistency merits discussion, particularly since it may indicate domain-dependence (traffic vs. meteorology) of the frequency-domain approach.

3. **Linear attention kernel not fully specified**: Section 4.3 states that "Softmax used for approximation in our implementation" but does not specify which random feature mapping φ(·) is used (e.g., Performer-style FAVOR+, or simple ReLU-based approximation). This detail matters for reproducibility, as different kernel approximations have different variance properties.

4. **Minor overclaim in terminology**: The "prompt-based guidance" described in Eq. (5) is a multiplicative gating mechanism with learnable per-node parameters, which is somewhat different from the prepended-input prompts common in NLP. This does not undermine the method's effectiveness but the terminology slightly overclaims the connection to prompt tuning.

### Trivial
- The "toy dataset" used in the efficiency study (Figure 8) is not described — what node counts were tested?
- The EAC baseline appears both in the main results (Table 1) and in the ablation study (Figure 4), which is slightly confusing since the ablation figure includes "EAC" as a variant alongside "Our" — the text clarifies this, but a note in the figure caption would help.

## Nice-to-Haves

- A cleaner ablation that replaces the backbone with a simpler but still general backbone (e.g., STID's embedding + MLP) while keeping the pattern bank and prompt interaction identical would better isolate the benefit of FreNet + DLGA specifically, beyond the current "w/o Backbone" which replaces with CNN + GCN from baselines.
- A brief discussion of when the frequency-domain backbone's assumptions (stable periodic components) hold and when they might break (e.g., non-stationary meteorological data) would strengthen the paper's honesty and generalizability.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Undefined streaming period segmentation**: The harsh critic claimed the paper never states how periods are constructed from raw datasets. However, the paper explicitly references Appendix A.4.1 for "Detailed dataset statistics" and follows the established EAC (Chen & Liang, 2025) protocol. The appendix was stripped by the parser and exists in the original submission. Per the hard rules, criticisms about missing appendix content are removed.
- **Unclear baseline tuning**: The paper follows prior work (Chen & Liang, 2025) for the evaluation protocol. The baselines are CSTF methods used in their natural setting. This is a generic concern applicable to most comparison papers and is not specific evidence of unfair comparison.
- **Criticisms about "prompt" terminology overclaiming similarity to NLP**: This is a naming preference, not a substantive weakness. The paper clearly defines the mechanism.
- **Missing statistical significance tests**: Requesting paired t-tests is a non-standard practice for ST forecasting where single-run evaluation with std is the norm. The gains on traffic datasets are large enough to be unambiguous.

## Novel Insights

Beyond the paper's own contributions, the most interesting takeaway from the reviews is the structural similarity between STBP and the SNIP paper (z45L1eYoHE.md, 5.33): both use a frozen backbone with node-level prompting/pattern banks for expanding-node scenarios. The key differentiator is STBP's more sophisticated backbone (frequency-domain + linear attention) versus SNIP's static computed priors. STBP's approach yields substantially larger empirical gains, suggesting that in CSTF, the backbone quality matters at least as much as the continual learning strategy — a point the paper makes but the combined evidence from these two papers strongly supports.

## Suggestions

1. Replace the approximate values in the ablation table (Figure 4) with exact mean ± std values, matching the reporting standard of the main results.
2. Add a brief paragraph discussing the AIR-Stream results: note the smaller improvement and the RMSE pattern, and offer a hypothesis (e.g., meteorological data having less stable periodicity than traffic data).
3. Specify the random feature mapping used for the linear attention (e.g., FAVOR+, ReLU-based, or softmax-approximated with a specific kernel).
4. Describe the toy dataset used in the efficiency study (node counts tested, number of periods).

## Score and Decision

**Bracketing (Round 1):** Retrieved four weak anchors (2.00–3.00, all Reject/Withdrawn) for spatio-temporal topics, four middle anchors (4.50–5.33, mixed Accept/Reject), and four strong anchors (8.00, all Accept — but from unrelated domains like 3D generation and protein design). The topically relevant middle anchors (SNIP at 5.33, PhySTA at 5.33, MMCKM at 6.00) form the usable comparison set. **Initial bracket: 5.5–7.5.**

**Narrowing (Round 2):** Queried for spatio-temporal forecasting papers in the (5.5, 7.5) band. Retrieved MMCKM (6.00, Accept Poster, four 6s) and others. MMCKM is a solid traffic ST paper with good novelty and clean ablations. Compared to MMCKM, STBP has a more practical problem setting (continual learning vs. standard prediction), larger empirical gains (20%+ vs. "comparable" on some metrics), but weaker ablation reporting (approximate values). 

**Final anchors used:**
| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| z45L1eYoHE.md (SNIP) | 5.33 | R1 | Weaker — synthetic setups, single expansion stage, smaller datasets |
| b6Py2zy0fK.md (PhySTA) | 5.33 | R1 | Similar quality but different problem; STBP has stronger empirical gains |
| fhDqFk4DgI.md (MMCKM) | 6.00 | R2 | Solid paper; STBP comparable or slightly stronger in empirical magnitude |
| Rw06dyqE5f.md (Coden) | 4.50 | R1 | Much weaker — confused problem definition, poor writing |

**Positioning:** STBP is clearly stronger than SNIP (5.33) and comparable to MMCKM (6.00) with slightly larger empirical gains. The main weaknesses (imprecise ablation numbers, mixed AIR-Stream RMSE) are minor and fixable. Score is above the median of the relevant anchors.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>