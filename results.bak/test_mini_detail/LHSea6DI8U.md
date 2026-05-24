Now I have sufficient calibration. Let me compile the final review.

**Round 1 Bracket:** Based on the wide-band calibration, I estimated the paper sits between 4 and 7 on the score scale.

**Round 2 Narrowing:** After reading SKI-CL (5.33), STGKD (5.25), FDN (4.75), PN-Train (6.0), and DMD-GNN (6.6), I compared STBP against each:

- **vs. SKI-CL (avg 5.33):** STBP has much stronger empirical results (clear SOTA with ~21% improvement vs. mixed/competitive results), a more novel framework, and cleaner ablations. **STBP > SKI-CL.**
- **vs. STGKD (avg 5.25):** STBP's core idea is more novel and results are more decisive. **STBP > STGKD.**
- **vs. FDN (avg 4.75):** STBP addresses a harder problem (continual learning with expanding graphs) and has stronger empirical evidence. **STBP > FDN.**
- **vs. PN-Train (avg 6.0):** Comparable rigor but STBP tackles a broader problem. The FreNet characterization issue pulls it slightly below PN-Train's crispness. **STBP ≈ PN-Train but slightly weaker.**
- **vs. DMD-GNN (avg 6.6):** DMD-GNN has stronger theoretical grounding. **STBP < DMD-GNN.**

Final estimate situates STBP at approximately **6.0** — solidly above borderline with genuine contributions, tempered by the FreNet characterization issue.

---

## Summary

This paper proposes STBP, a framework for continual spatio-temporal forecasting that couples a frozen general-purpose backbone (with frequency-domain processing and linear graph attention) with an expandable contextual pattern bank. During incremental training, the backbone is frozen to retain general knowledge while the pattern bank expands via parameter addition and interacts with the backbone through prompt-based gating and attention. Experiments on three real-world streaming datasets (PEMS-Stream, CA-Stream, AIR-Stream) show STBP achieves state-of-the-art results, with MAE reductions of ~21% on traffic datasets over the best baseline.

## Strengths

1. **State-of-the-art forecasting accuracy across multiple continual-learning benchmarks.** STBP achieves the lowest MAE, RMSE, and MAPE on all three datasets (Table 1). On PEMS-Stream, average MAE is 12.31 — a 21.44% reduction relative to the best competing method (EAC, 15.67). Results are reported with standard deviations across multiple runs.

2. **Strong few-shot generalization confirming effective knowledge retention.** In Table 2, when later incremental periods have only 10% of the training data, STBP still achieves MAE 13.58 on PEMS-Stream (vs. 16.13 for EAC) and MAE 17.11 on CA-Stream (vs. 20.94 for EAC). This provides concrete evidence that the frozen backbone + expanding pattern bank mitigates catastrophic forgetting.

3. **Linear-time spatial modeling with competitive efficiency.** The dual-stream linear graph attention (DLGA) reduces complexity to O(N) in node count. Figure 8 shows STBP with linear attention uses substantially less GPU memory than quadratic-attention variants as nodes grow, while maintaining the lowest MAE.

4. **Interpretable pattern bank learning meaningful node clusters.** The t-SNE visualization (Figure 6) shows that after incremental training, the contextual pattern bank forms distinct clusters corresponding to different traffic dynamics, and new nodes from later periods are correctly assigned to existing clusters — validating the claimed ability to capture node-level relevance and heterogeneity.

5. **Comprehensive ablation study confirming each component's contribution.** Figure 4 shows that removing the contextual pattern bank (Retrain/Online variants), the backbone (w/o Backbone), or the DLGA module (w/o DLGA) causes clear performance degradation across all datasets, with the full model consistently yielding the lowest errors.

## Weaknesses

### Fatal
None.

### Major

1. **FreNet's FFT operates on the feature dimension, not the time axis, contradicting the claimed temporal frequency analysis.** The paper states FreNet extracts "stable low-frequency components (e.g., periodicity and trends)" via FFT to mitigate distributional drift. However, the pipeline (Eq. 6, line 119–127) projects input **X**ₜ ∈ ℝ^{N×Tₕ} through a linear layer into **H**ₜ ∈ ℝ^{N×d} *before* applying the FFT. This means the FFT operates on the feature dimension *d*, not the temporal axis *Tₕ*. The operation cannot extract temporal periodicity or trends as claimed — it performs spectral filtering in the learned feature space. This is a mismatch between the paper's characterization and its actual mechanism. **Why it matters**: The paper lists "handling distributional drift" as Challenge ❶ and explicitly motivates FreNet as the solution. While the module may still provide useful feature-space filtering, the claimed connection to temporal stability is unsupported. The authors must either redesign FreNet to apply FFT along the temporal axis, or rewrite the motivation to accurately describe what the module does (feature-space spectral filtering) and remove the claim about extracting temporal periodicity/trends. The core empirical results are unaffected, but the paper's internal coherence on this point needs repair.

2. **The dual-stream linear attention formulation lacks justification.** Equation (9) approximates attention as φ(**Q**)φ(**K**)ᵀ**V** + φ(**Q**)φ(**P**ₜ^{(2)})ᵀ**V**, adding the pattern bank as a second key set via simple addition of outer products. Standard practice for multiple key sets would concatenate keys or use separate attention heads. The paper says "see Appendix A.3.1" for derivation details, but within the main text provides no intuitive rationale for why this particular sum formulation should capture "the relationship between evolving input patterns and stored knowledge." **Why it matters**: Without some justification (theoretical or empirical), the reader cannot assess whether this design choice is principled or arbitrary. Adding a brief ablation comparing this additive formulation against alternatives (e.g., key concatenation, separate attention heads) would substantially strengthen the paper.

### Minor

3. **The AIR-Stream results show only 2.35% MAE improvement vs. ~21% on traffic datasets, with no discussion of this discrepancy.** The paper presents strong gains on PEMS-Stream and CA-Stream but a much smaller gain on the meteorological dataset. If FreNet and the pattern bank are critical for handling distributional drift, the smaller gain on a different domain should be explained — either AIR-Stream has less drift, or the method is less effective there. This analysis is missing.

4. **The ablation bar chart (Figure 4) reports approximate values ("~15", "~22") rather than exact numbers with confidence intervals.** The underlying data is available in Table 1, but Figure 4 as presented cannot be read precisely. Additionally, including "EAC" as a labeled variant (it is an independent baseline, not an ablation) in the same figure is somewhat misleading, though the text does clarify its role. These are presentation issues that weaken the visual evidence.

### Trivial

5. The t-SNE visualization in Figures 3 and 6 is qualitative. Adding a quantitative cluster separation metric (e.g., Silhouette score) would strengthen the claim that the pattern bank learns meaningful clusters.

6. The efficiency analysis (Figure 8) uses a "Toy dataset" for the memory scaling plot rather than real datasets. Real-dataset memory scaling would be more convincing, though the real-dataset training-time scatter plots are informative.

## Nice-to-Haves

- The paper mentions the appendix contains incremental period details (how many periods, node counts per period, etc.). These details should be in the main text for reproducibility.
- Reporting statistical significance tests between STBP and the best baseline would strengthen the claims, though the large margins make this less critical.
- The conclusion mentions "single-task setting" as a limitation. Discussing failure cases (e.g., when new nodes are highly dissimilar to any seen pattern, or when the number of incremental periods grows very large) would be useful.

## Removed Points

- **"EAC is not an ablation"**: The paper explicitly states "We also include EAC, which follows a similar approach, for comparison in the ablation study" (line 251). It is included as a reference comparison, not claimed as an ablation. This is transparent.
- **"Missing related work"**: I cannot verify missing references without external knowledge.
- **"Reproducibility / missing appendix details"**: The parser strips the appendix; these details exist in the original submission.
- **Generic concerns about "whether baselines are fair"**: The paper describes how each baseline is adapted for the continual setting (retrain/online). No specific unfairness was identified.
- **"FreNet issue is fatal/structural"**: While real, the issue is a characterization mismatch, not an invalidation of results. The core contributions of the paper (pattern bank + frozen backbone + DLGA) are unaffected.
- **Strength Finder's generic strengths** ("the problem is important", "the paper addresses a timely topic"): Removed as lacking specific content.

## Novel Insights

The most interesting observation from the reviews is the tension between the paper's strong empirical results and the overclaimed component descriptions. The pattern bank + frozen backbone idea is clearly effective (validated by 21% improvements and the t-SNE visualization), but the paper would be stronger if it reined in its claims about what FreNet does and provided a principled justification for the DLGA formulation. The reviews collectively suggest the paper's *actual* contribution — a scalable, interpretable mechanism for continual adaptation without forgetting — is more compelling than the paper's *claimed* contribution about frequency-domain temporal analysis, and the paper would benefit from leaning into the former.

## Suggestions

1. **Correct the FreNet description.** Clarify that the FFT operates on the projected feature dimension, not the temporal axis. Either redesign the module to apply FFT along the time dimension (before the linear layer) or rewrite the motivation to describe what the module actually does (feature-space spectral filtering) and temper the claims about extracting temporal periodicity/trends.

2. **Justify the dual-stream attention formulation.** Add a brief ablation in the main text comparing the additive dual-stream formulation against alternatives (key concatenation, separate attention heads) to show it is not arbitrary. If a derivation exists in the appendix, summarize it in 2-3 sentences in the main text.

3. **Add exact numerical values to the ablation figure (Figure 4)** and remove "EAC" from the ablation set or clearly distinguish it as an external reference line.

4. **Discuss the AIR-Stream discrepancy.** Explain whether this dataset has less distributional drift or whether the method is less effective on meteorological data, and what this implies about the method's applicability.

5. **Report quantitative cluster metrics** (e.g., Silhouette score, Davies-Bouldin index) for the pattern bank visualization to complement the qualitative t-SNE plots.

## Score and Decision

The paper makes a genuine contribution — the frozen backbone + expandable pattern bank framework is novel, well-motivated, and strongly validated by experiments. The improvements on traffic datasets are large and consistent across settings. The FreNet characterization issue is real and needs correction, but it does not invalidate the core contributions or the empirical findings. With revisions addressing the characterization, the paper would be solid.

**MY FINAL SCORE: 6.0**
**MY FINAL DECISION: Accept</score></decision>