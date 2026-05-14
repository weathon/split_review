Now I have a thorough understanding of the paper, the critic claims, and the calibration anchors. Let me write the consolidated review.

---

## Summary

STBP proposes a framework for continual spatio-temporal forecasting that combines a frozen general spatio-temporal backbone (FreNet for frequency-domain temporal processing + DLGA for linear graph attention) with an incrementally expandable contextual pattern bank. The backbone remains fixed after initial training to preserve general knowledge, while the pattern bank expands and adapts via parameter expansion and prompt-based gating to handle evolving graph topologies and distribution shifts. Experiments on three real-world streaming datasets show substantial accuracy improvements over CSTF baselines (21%+ MAE reduction on two datasets).

## Strengths

- **Strong empirical performance across diverse streaming scenarios.** STBP reduces average MAE by 21.44% (PEMS-Stream), 21.93% (CA-Stream), and 2.35% (AIR-Stream) compared to the best baseline EAC (Table 1). Gains are consistent across forecasting horizons and hold in few-shot settings (Table 2), indicating robust knowledge reuse when new data is limited.

- **The frozen backbone + expandable pattern bank design is conceptually sound and empirically validated.** The ablation study (Section 5.3) shows that removing the pattern bank ("Retrain" and "Online" variants) or replacing the backbone with a simpler CNN+GCN stack ("w/o Backbone") causes significant performance degradation, confirming that both components are necessary and that their collaboration drives the improvements.

- **DLGA provides an effective and efficient mechanism for dynamic spatial modeling.** Ablating DLGA (Figure 4) causes clear performance drops, and the efficiency study (Figure 8) demonstrates that linear attention reduces computational overhead while preserving dynamic spatial correlation modeling. The dual-stream design that incorporates the pattern bank as an additional key is a clean integration.

- **The contextual pattern bank autonomously captures meaningful node-level structure.** t-SNE visualizations (Figures 3, 6) reveal clusters corresponding to distinct temporal behaviors, and new nodes from later incremental periods are correctly assigned to existing clusters, corroborating the bank's ability to consolidate and generalize spatio-temporal patterns without explicit clustering constraints.

- **Comprehensive evaluation spanning multiple domains and expansion regimes.** Three datasets cover traffic and air quality domains with node increases from 10% to 254% (Tables 4–5), including both gradual and explosive graph growth. The few-shot evaluation, parameter sensitivity analysis, and efficiency study add depth.

## Weaknesses

### Fatal
None.

### Major

- **FreNet does not perform temporal frequency analysis as the paper claims.** The input X_τ ∈ ℝ^{N_τ × T_h} is first mapped through a linear layer to H_τ ∈ ℝ^{N_τ × d}, collapsing the temporal dimension. The FFT is then applied to H_τ along the feature (d) dimension, not the time dimension. Consequently, the operation cannot extract temporal periodicity, trends, or any frequency content related to the original time series — the "low-frequency components" in this transform refer to slow variations across feature dimensions, not temporal patterns. The paper's central claim that "FreNet is designed to capture temporal correlations while emphasizing stable components in the data, such as periodicity and trends" (Section 4.3) is therefore misleading. This does not necessarily invalidate the empirical results (the FFT-based feature transformation may still be useful), but it means a key part of the method's motivation and claimed mechanism is unsupported as described. The authors should either (a) clarify that the FFT operates in feature space and adjust claims accordingly, or (b) re-implement to apply FFT along the temporal axis.

- **The paper claims to mitigate catastrophic forgetting but never measures forgetting.** Standard continual learning metrics such as forgetting rate, backward transfer, or per-period performance degradation on earlier tasks are absent. The evaluation relies solely on average metrics across all incremental periods, which cannot distinguish between genuine knowledge retention and a model that simply performs well on new tasks while silently degrading on old ones. For a paper whose third stated challenge is "alleviating catastrophic forgetting" (Section 1), this omission directly undermines a core contribution claim.

### Minor

- **No ablation isolates FreNet's specific contribution.** The "w/o Backbone" variant replaces both FreNet and DLGA with a CNN+GCN stack, conflating the two modules. A targeted ablation replacing FreNet with a standard temporal module (e.g., MLP, TCN, or GRU) while keeping DLGA and the pattern bank intact would allow readers to assess whether frequency-domain processing provides any benefit over simpler alternatives. The current ablation supports the backbone as a whole but leaves FreNet's individual value unquantified.

- **Notation ambiguity in the prompt-based guidance equation.** Equation (5) uses "·" without specifying whether it denotes element-wise (Hadamard) product, matrix multiplication, or broadcast operations. Given the dimensions involved (P_τ^(0), P_τ^(1) ∈ ℝ^{N_τ × d} and H_τ ∈ ℝ^{N_τ × d}), clarifying the exact operation at each step would improve reproducibility.

### Trivial
None.

## Nice-to-Haves

- A direct visualization comparing FreNet's frequency-domain embeddings to raw time-series spectra would help substantiate the claim of stable component extraction, even if the FFT operates in feature space.
- Reporting per-period test performance on the first incremental period's data after each subsequent update would provide a rough estimate of forgetting without requiring a full CL metric suite.
- A discussion of how the random feature mapping φ(·) in DLGA (Eq. 9–10) affects expressivity compared to standard softmax attention would strengthen the linear attention justification (the paper defers details to Appendix A.3.1, which is reasonable).

## Removed Harsh Critic Points (after cross-checking with the paper)

- **"The linear attention derivation is hand-waved"**: The paper explicitly states "For further details on the approximation derivation, see Appendix A.3.1." The appendix is stripped by the PDF parser — this is not a paper flaw. Removed.
- **"The exact point in the computation graph where each P component interacts should be explicitly illustrated"**: Figure 2 already shows the architecture with the three pattern bank components P^(0), P^(1), P^(2) annotated at their interaction points. The text in Section 4.2 describes P^(0) interacting via gating (Eq. 5) and P^(2) acting as a key in DLGA. Sufficiently clear.

## Calibration

Compared to closely related anchor papers: **SNIP** (avg 5.33, Reject) addresses a similar expanding-node forecasting problem with prompting, but has less architectural novelty, weaker empirical results, and synthetic node expansion — STBP offers stronger experiments and a more complete framework. **TIFO** (avg 5.00, Reject) proposes frequency-domain processing for time series with theoretical backing, but its contributions were judged as incremental reinterpretation — STBP's FreNet has a similar issue with misleading frequency-domain motivation, but STBP's overall framework (backbone + bank) is more substantial. **DPGNet** (avg 2.00, Reject) suffers from weak novelty, baseline inconsistencies, and marginal improvements — STBP is clearly stronger on all dimensions. I assess STBP at approximately the same quality level as SNIP/TIFO, with stronger empirical results offset by the FreNet motivation issue and missing forgetting metrics.

## Overall Assessment

STBP presents a well-engineered continual forecasting framework with genuinely strong empirical results. The frozen backbone + expandable pattern bank + prompt-based guidance is a coherent and validated design, and DLGA is an effective spatial module. However, the paper has two significant issues: (1) the FreNet module's claimed temporal frequency analysis is misleading because the FFT operates on feature dimensions, not the time axis, which undermines a central motivation; and (2) the paper repeatedly claims to mitigate catastrophic forgetting but never reports any forgetting metric, leaving this key claim unsubstantiated. These issues are addressable — clarifying or correcting FreNet and adding forgetting metrics would substantially strengthen the paper. In its current form, the contribution is promising but not fully supported.

**Score: 5.0 — Reject (with encouragement to resubmit after addressing the FreNet description and adding forgetting metrics).**

---

Now let me produce the final output with the correct score.

<center>MY FINAL SCORE: 5</center>