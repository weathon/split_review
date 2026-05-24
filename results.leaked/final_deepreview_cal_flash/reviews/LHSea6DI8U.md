Now I have a thorough understanding of the paper. Let me synthesize the final review.

## Summary

The paper proposes STBP, a framework for continual spatio-temporal forecasting that combines a frequency-domain backbone (FreNet) with a dual-stream linear graph attention (DLGA) module, and an expandable contextual pattern bank that uses prompt-based guidance to mitigate catastrophic forgetting. The backbone remains frozen after initial training while the pattern bank is updated incrementally to adapt to new nodes and distributions. Experiments on three streaming datasets show substantial improvements over existing CSTF methods, with 21%+ MAE reduction on traffic datasets.

## Strengths

1. **Strong empirical results with clear contributions**: STBP consistently and substantially outperforms all compared baselines (including recent methods EAC, STRAP, PECPM) across three real-world datasets. On PEMS-Stream and CA-Stream, the average MAE reduction over the best baseline is ~21%, which is a genuine advance in CSTF. The gains are supported by standard deviations from multiple runs.

2. **Well-designed framework integrating two complementary mechanisms**: The framework cleanly separates responsibilities — the backbone handles spatio-temporal modeling and distributional drift, while the pattern bank handles knowledge retention and adaptation. The ablation study (Section 5.3, Figure 4) validates that each component contributes meaningfully (removing the backbone, DLGA, or pattern bank all cause significant degradation).

3. **Methodologically novel combination**: The paper introduces (a) a frequency-domain network for CSTF, (b) a dual-stream linear graph attention that incorporates pattern bank embeddings as an additional key stream with O(N) complexity, and (c) a prompt-based gating mechanism between the pattern bank and backbone via three parameter groups (P⁰, P¹, P²). Each of these design choices is technically justified.

4. **Comprehensive evaluation extending beyond main results**: Few-shot experiments (Table 2) demonstrate robustness under data scarcity, efficiency analysis (Figure 8) shows the O(N) attention scales gracefully, and t-SNE visualizations (Figures 3, 6) provide qualitative evidence that the pattern bank learns meaningful node clusters.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Misleading description of the frequency-domain analysis (FreNet)**: The paper states that FreNet "capture[s] temporal correlations while emphasizing stable components in the data, such as periodicity and trends" and claims it extracts "stable low-frequency components." However, the FFT is applied after a linear layer that maps X_τ ∈ ℝ^{N_τ × T_h} to H_τ ∈ ℝ^{N_τ × d}. The learnable frequency embedding F_τ ∈ ℂ^{(d/2+1)} confirms the FFT operates on the feature dimension d, not along the temporal axis T_h. The paper's recurring language about temporal periodicity presupposes a time-axis FFT, which the described operation does not perform. This does not necessarily invalidate the method — FFT on learned features can still serve as useful spectral filtering — but the stated motivation and justification are inconsistent with the mechanics. The authors should clarify the FFT axis and either correct the narrative or provide a rationale for why FFT on the feature embedding extracts stable temporal patterns.

2. **Overclaimed interpretation of the "w/o Backbone" ablation**: The ablation replaces the STBP backbone with CNN+GCN modules from TrafficStream/STKEC/EAC while retaining the pattern bank. The paper claims this "highlights the portability and adaptability of the pattern bank across different backbone architectures." However, the pattern bank's gating (Eq. 5) and dual-stream attention (Eq. 9) are designed for specific interaction points with the FreNet+DLGA backbone. Grafting it onto a CNN+GCN backbone without adapting those interactions tests compatibility at most, not portability. The primary conclusion — that the backbone is indispensable — is well-supported by the performance drop; the portability claim should be downplayed or the experiment redesigned.

3. **Incomplete specification of the continual learning setup**: The main text does not state the number of incremental periods, how nodes are distributed across periods, or what fraction of nodes is added at each period for each dataset. These details (likely deferred to the appendix) are important for interpreting task difficulty and for reproducibility. Similarly, it is not explicitly stated whether old pattern bank parameters remain frozen or are also updated when new nodes are added (Eq. 4 says "only the expanded contextual pattern bank P'_τ is fine-tuned," which could mean only the newly added parameters ΔP_τ).

4. **Modest gains on AIR-Stream**: The 2.35% MAE improvement over the best baseline on AIR-Stream is much smaller than the ~21% gains on traffic datasets, and for some horizons/metrics the improvement is marginal or within standard deviation overlap. This does not weaken the paper, but the framing ("substantial improvements") should be tempered for the air quality domain.

### Trivial

- The notation "·" in Eq. 5 should specify whether it is element-wise or matrix multiplication (context suggests element-wise, but it is not stated).
- The second FreNet "restor[es] the feature shape to ℝ^{N_τ × T_h}" via an unspecified mechanism (presumably a linear layer mapping d → T_h).

## Nice-to-Haves

- Per-period results (e.g., MAE at each incremental stage) would allow readers to assess whether the model truly avoids catastrophic forgetting or performs well on average due to strong initial performance. Reporting a forgetting metric (e.g., average forgetting from continual learning literature) would strengthen the anti-forgetting claims.
- The pattern bank grows linearly with the number of nodes, which the paper could acknowledge as a potential limitation for city-scale networks with millions of sensors.
- A direct comparison of FFT on the feature dimension vs. FFT on the temporal dimension would clarify whether the unconventional placement is actually beneficial for the stated purpose.

## Removed Points

These points from the harsh critic are removed or demoted for the reasons given:

- **"Ambiguous and potentially flawed frequency-domain analysis" labeled as structural/fatal** → Demoted to Minor. The method is not flawed; the description is misleading. The FFT on the feature dimension can still be useful as latent spectral filtering. The critic's framing as a structural issue that "undermine[s] confidence that the paper's stated contributions are correctly supported" overstates the severity.
- **"Weak evidential support for the pattern bank's portability"** → Kept as Minor but reduced severity. The critic's framing that "the conclusion does not follow from the experiment" is accurate for the portability claim, but the main claim (backbone indispensability) is well-supported.
- **"The results may still be strong, but the paper's internal explanation... becomes suspect"** → This is a valid criticism of explanation quality, not of the results themselves. Kept as Minor.
- **Missing hyperparameter tuning details for baselines** → Partially valid but baselines' hyperparameters are typically set by their original papers. The paper says "More details on this are included in Appendix A.4.2." Defer to appendix.
- **Formatting/style nitpicks about notation clarity** → Kept as Trivial.
- **Strength Finder's claim about "portability and adaptability of the pattern bank across different backbone architectures"** → Conflicts with the verified weakness about the w/o Backbone overclaim. Demoted accordingly — the strength about pattern bank learning meaningful clusters is fine, but the portability framing is rejected.

## Novel Insights

The most interesting observation from the reviews is the tension between the paper's strong empirical performance and the ambiguity in its technical justification for a core component (FreNet). The harsh critic correctly identifies that the FFT is applied on the feature dimension rather than the temporal axis, but frames this as potentially fatal. A more nuanced view is that the paper accidentally describes a method that is more interesting than it claims: FFT on learned feature embeddings with a learnable frequency mask is a form of adaptive spectral filtering in latent space, which could be justified as a flexible frequency-domain processor without claiming temporal periodicity extraction. The negative reviews would strengthen significantly if this were reframed honestly. Separately, the fact that the w/o Backbone ablation still outperforms most baselines (w/o Backbone MAE ~24 vs. EAC ~26 on PEMS-Stream) suggests the pattern bank provides meaningful benefits even with a weak backbone — this is actually a more interesting finding than the overclaimed portability.

## Suggestions

- Clarify the FFT axis in FreNet (Eq. 6) and revise the associated narrative to accurately describe what the operation does (FFT on the learned feature embedding, not the temporal axis), or alternatively, redesign FreNet to apply FFT along the temporal dimension if periodicity extraction is the goal.
- Add one sentence specifying how pattern bank updates work: whether only ΔP_τ is fine-tuned or the full P'_τ including the initial P_{τ-1} portion.
- Include a table in the main text showing the number of incremental periods and node counts per period for each dataset, or at minimum reference the appendix section that contains them.
- Downplay the "portability" claim for the w/o Backbone ablation and refocus on the well-supported conclusion about backbone indispensability.

## Score and Decision

### Calibration Anchors

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| FRzCIlkM7I (EAC — continual STG forecasting) | 6.75 | R1, R2 | Most directly comparable. STBP outperforms EAC by ~21% MAE on traffic, has more elaborate methodology, but has FreNet description issues EAC does not. |
| kVlfYvIqaK (DyGPrompt — dynamic graph prompts) | 6.00 | R2 | Different task (node classification on dynamic graphs). STBP is stronger empirically and more comprehensive. |
| uvFhCUPjtI (EFT — evolving Fourier transform) | 6.00 | R2 | Different task (link prediction on temporal graphs). STBP has stronger empirical eval. |
| 82Mc5ilInM (FreeDyG — freq. enhanced dynamic graphs) | 6.75 | R2 | Different task (link prediction). STBP comparable in methodological novelty, stronger in empirical breadth. |
| mkjKqeBXkt (KITS — spatio-temporal kriging) | 5.67 | R1 | Different task (kriging). STBP is clearly stronger. |
| mHkbi3XM58 (conditional density estimation) | 3.25 | R1 | Different domain. Weak anchor. |

**Round 1 bracket**: Between 6.75 (EAC) and 8.0 (strong accept anchors). The EAC paper is the most directly comparable and STBP clearly outperforms it.

**Round 2 narrowing**: Anchors in (5.5, 8.0) show papers on related topics scoring 5.67–6.75. STBP is empirically stronger than all of them and has greater methodological novelty than most, but the FreNet description issue and mild overclaim in the ablation prevent it from reaching the 8+ tier.

**Final score**: **7.0**

The paper makes a genuine empirical advance in continual spatio-temporal forecasting with a well-structured framework and thorough evaluation. The flaws are presentation/justification issues, not fatal methodological errors. Score 7.0 positions it clearly above the directly comparable EAC paper (6.75) while acknowledging the need for clarification on the FreNet design.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>