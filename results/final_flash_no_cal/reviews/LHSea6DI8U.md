Now I have a thorough understanding of the paper and can verify every claim. Let me compose the final review.

## Summary

This paper proposes STBP, a framework for continual spatio-temporal forecasting that combines a frequency-domain spatio-temporal backbone (with linear graph attention) with an expandable contextual pattern bank. The backbone is frozen after initial training to preserve general knowledge, while the pattern bank is expanded and fine-tuned to adapt to new nodes and distribution shifts. The framework is evaluated on three real-world streaming datasets (traffic and meteorology), showing consistent improvements over existing CSTF methods and conventional STGNNs, with ablation studies confirming the contribution of each component.

## Strengths

- **Substantial and consistent accuracy gains over state-of-the-art CSTF methods.** Table 1 shows STBP achieves the lowest MAE, RMSE, and MAPE across all three datasets at all forecasting horizons. Compared to the best baseline (EAC), STBP reduces average MAE by 21.44% on PEMS-Stream, 21.93% on CA-Stream, and 2.35% on AIR-Stream. These gains are corroborated in the few-shot setting (Table 2), where improvements are even larger, directly supporting the paper's claims about effective continual learning.

- **Ablation studies confirm that each component is necessary.** Figure 4 shows that removing the contextual pattern bank (Retrain, Online), replacing the backbone (w/o Backbone), or ablating DLGA (w/o DLGA) all cause clear performance degradation. The pattern bank variants (Retrain/Online) perform substantially worse than the full model, confirming that the joint design of backbone + pattern bank is critical.

- **Scalability and efficiency are empirically validated.** Figure 8 demonstrates that STBP's per-period training time and GPU memory are competitive with other CSTF methods, and the linear-attention version avoids the quadratic overhead of full attention. A toy-dataset experiment confirms linear scalability with node count.

- **Interpretable pattern bank structure.** t-SNE visualizations (Figures 3 and 6) show that the learned pattern bank parameters form meaningful clusters corresponding to distinct traffic patterns, and new nodes from later periods are correctly assigned to existing clusters. This qualitative evidence supports the claim that the pattern bank captures node relevance and heterogeneity.

- **Comprehensive evaluation across domains and settings.** The paper tests on three real-world datasets (traffic and meteorology), includes few-shot experiments, case studies, ablation, efficiency analysis, and hyperparameter sensitivity. The baseline set includes both conventional STGNNs and five dedicated CSTF methods.

## Weaknesses

### Fatal
None.

### Major

- **No per-period performance evaluation to support the forgetting-mitigation claim.** The paper claims that STBP "mitigates catastrophic forgetting" (abstract, contributions, conclusion), but all results in Table 1 are averaged across incremental periods. In continual learning, the standard way to demonstrate forgetting mitigation is to report performance on earlier periods after learning later periods — e.g., accuracy on period-1 test set after training on period 2, period 3, etc. Without this, the paper cannot distinguish between a method that (a) fits each new period well while retaining old knowledge, and (b) a method that fits new periods well but overwrites old knowledge. The ablation (Retrain vs. Online) and few-shot experiments provide only indirect evidence. This is the most consequential gap because it concerns a central claimed contribution of the paper.

### Minor

- **Ambiguity about whether old pattern-bank parameters are frozen or updated.** The paper states: "Only the expanded contextual pattern bank P'_τ ∈ R^{N_τ × d} is fine-tuned during training" (Section 4.2), where P'_τ = P_{τ-1} ∥ ΔP_τ includes both old and newly added parameters. It is unclear whether the old parameters (inherited from P_{τ-1}) are frozen or also updated during subsequent fine-tuning. If they are updated, old node representations could drift, potentially undermining the forgetting-mitigation mechanism. The paper should clarify this design choice and ideally provide an ablation comparing freezing vs. updating old pattern-bank parameters.

- **Equation (5) lacks precision.** The prompt-based gating function H'_τ = P_τ^(1) · h_θ(H_τ · (1 + P_τ^(0))) uses "·" without specifying whether this is element-wise multiplication or matrix multiplication. Additionally, h_θ is described as "an arbitrary submodule within the backbone" — it is unclear which submodule h_θ refers to in practice (e.g., the output of FreNet? the feed-forward layer?). This makes the gating mechanism difficult to reproduce without inferring implementation details.

- **No isolated ablation of FreNet.** The paper attributes distribution-drift mitigation to FreNet (Section 4.3), but the ablation studies do not isolate its contribution. The "w/o Backbone" variant replaces both FreNet and DLGA with CNN+GCN, while "w/o DLGA" removes only DLGA. There is no "w/o FreNet" variant that keeps DLGA but removes the frequency-domain processing. As a result, FreNet's individual contribution to the reported gains cannot be disentangled from that of DLGA or the backbone architecture as a whole.

### Trivial

- The scatter-plot in Figure 8 uses marker size to encode GPU memory, making it difficult to compare quantitative memory values across methods. A numerical table or explicit labels would be clearer.

## Nice-to-Haves

- Adding a "w/o FreNet" ablation variant to isolate the contribution of frequency-domain processing to distribution-drift mitigation.
- Reporting per-horizon (3, 6, 12) results in the ablation study, not just averaged metrics.
- Exploring sensitivity to additional hyperparameters such as expansion ratio, learning rate for the pattern bank, or the number of incremental periods.

## Removed Points

The following points from the inputs are removed with rationale:

1. **Claim about "ablation inconsistency" (Harsh Critic):** The critic argues that Retrain (train-from-scratch) outperforming Online (fine-tune) is "unusual" and that the text calling Online "comparable to EAC" is a mismatch. This is removed because: (a) in continual learning, catastrophic forgetting can make fine-tuning worse than retraining from scratch — this is a known phenomenon that actually supports the paper's motivation, not a contradiction; (b) Online MAE ≈ 22 vs EAC ≈ 26 on PEMS-Stream is reasonably characterized as "comparable" (both are in the same regime and far from the full model's ≈15). The text and figure are not in conflict.

2. **Claim about dual-stream attention derivation being invalid (Harsh Critic):** The critic questions whether (φ(Q)φ(K)^⊤ + φ(Q)φ(P)^⊤)V = φ(Q)(φ(K)^⊤V + φ(P)^⊤V) is a "valid approximation." This is removed because the derivation follows directly from the associativity of matrix multiplication and is mathematically correct. It is a standard computation reordering for linear attention.

3. **Claim about FreNet role being vague (Harsh Critic):** Removed because Eq. 6 clearly defines the mechanism: the FFT output is element-wise multiplied by a learnable frequency-domain embedding F_τ ∈ ℂ^{(d/2+1)} before IFFT. The paper's description ("adaptively highlights stable features") is adequate for the level of detail typical in STGNN papers.

4. **Criticism about large gap to conventional STGNN baselines (Harsh Critic):** Removed because the paper explicitly acknowledges that these models are "not designed for continual learning" and uses their retrained-from-scratch variants as lower-bound references. The gap is expected and noted by the authors.

5. **Reproducibility nitpicks about undisclosed hyperparameters (Harsh Critic's "Section-by-Section Notes"):** Removed per the rule that minor implementation details not included in the main text or stripped appendix should not be held against the paper.

## Novel Insights

The reviews reveal a tension that the paper does not fully resolve: the framework freezes the backbone to preserve general knowledge while fine-tuning the pattern bank to adapt. This design implicitly assumes a clean separation between "general" spatio-temporal patterns (backbone) and "node-specific" patterns (pattern bank). The case studies provide qualitative support for this distinction (pattern bank clusters reflect meaningful node groupings), but the paper never tests whether node-specific information encoded in the pattern bank for earlier periods is overwritten when the bank is fine-tuned on later periods. This is the core open question that the missing per-period evaluation would address. Beyond this, the observation that Online (fine-tuning only) underperforms Retrain (training from scratch each period) in the ablation is worth noting: it suggests the backbone, when fully fine-tuned, is unusually susceptible to interference. The frozen-backbone + expandable-prompt design circumvents this, but the root cause of the backbone's sensitivity is not explored.

## Suggestions

- **Add per-period evaluation:** After each incremental stage, evaluate the model on the test sets of all previous periods (or a representative subset). Report a matrix or plot showing accuracy per period over time (standard in continual learning). This would directly substantiate the claim of forgetting mitigation.
- **Clarify the update rule for old pattern-bank parameters:** State explicitly whether P_{τ-1} parameters are frozen or updated during stage-τ fine-tuning. If frozen, note this and discuss any limitation. If updated, provide an ablation comparing the two strategies.
- **Add precision to Eq. (5):** Specify whether "·" denotes element-wise multiplication (⊙) or matrix multiplication, and clarify which submodule h_θ refers to (e.g., "h_θ denotes the output of the FreNet projection layer").
- **Add an isolated FreNet ablation:** Measure performance without FreNet while keeping DLGA and the pattern bank, to quantify FreNet's specific contribution to handling distributional drift.

## Score and Decision

The paper tackles a timely and important problem, presents a well-motivated framework, and demonstrates strong empirical results across multiple datasets and settings. The main weakness is the absence of per-period performance evaluation, which weakens the central claim about catastrophic forgetting mitigation. However, the framework design is sound, the results are convincing in aggregate, and the ablation studies confirm the necessity of each component. The paper makes a solid contribution to continual spatio-temporal forecasting.

<score>7.0</score>
<decision>Accept</decision>