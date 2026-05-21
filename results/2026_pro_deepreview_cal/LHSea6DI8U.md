Now I have sufficient calibration data. Let me synthesize the final review.

---

## Summary
This paper proposes STBP, a continual spatio-temporal forecasting framework that pairs a frozen general-purpose backbone (frequency-domain network FreNet + dual-stream linear graph attention DLGA) with an incrementally expandable contextual pattern bank. The backbone is trained jointly with the pattern bank only in the first period, then frozen; the pattern bank expands via parameter addition and fine-tunes to adapt to new nodes and distributions, interacting with the backbone through prompt-based gating and serving as an extra key in attention. Experiments on three streaming datasets show strong improvements over CSTF baselines (21%+ MAE reduction on two traffic datasets), robust few-shot performance, and linear computational scaling.

## Strengths
- **Strong and consistent forecasting improvements**: Table 1 demonstrates STBP achieves the best MAE/RMSE/MAPE across all three streaming datasets, with average MAE reductions of 21.44% (PEMS-Stream), 21.93% (CA-Stream), and 2.35% (AIR-Stream) compared to the best baseline (EAC). The few-shot results in Table 2 further show STBP maintaining a decisive lead with only 10% training data in subsequent periods.
- **Well-designed ablation study validates core components**: Figure 4 cleanly demonstrates that removing the backbone (replacing FreNet+DLGA with CNN+GCN) and ablating DLGA individually both cause clear performance degradation. The Retrain and Online variants confirm the frozen-backbone + expandable-bank design is essential for mitigating catastrophic forgetting.
- **Efficiency and scalability verified experimentally**: Figure 8 shows STBP achieves O(N) memory scaling via linear attention, maintaining competitive training time while delivering superior accuracy. The toy dataset experiment confirms the linear vs. quadratic scaling contrast.
- **Meaningful pattern bank organization**: The t-SNE visualization in Figure 6 shows the pattern bank learns interpretable node clusters corresponding to distinct temporal behaviors, with new nodes correctly placed into existing clusters — supporting the claim that the bank captures node relevance and heterogeneity without explicit clustering supervision.
- **Architectural generality**: The backbone does not rely on predefined adjacency matrices, making it applicable across diverse streaming spatio-temporal graphs with evolving topologies, validated by results on datasets with different node-expansion patterns.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor
- **FreNet's contribution to distribution-drift mitigation is asserted but not independently isolated**: The paper claims FreNet "emphasizes stable components... more resilient to distributional changes" (Section 4.3), but no ablation tests FreNet against a simpler temporal module (e.g., TCN or MLP-mixer) with comparable capacity. The "w/o Backbone" ablation replaces both FreNet and DLGA with CNN+GCN, and "w/o DLGA" removes only DLGA — neither isolates FreNet's specific benefit. This weakens the paper's specific claim about frequency-domain processing for drift mitigation. The overall framework's effectiveness is not in doubt, but the attribution to this mechanism remains an untested intuition.
- **Marginal improvement on AIR-Stream is reported but not discussed**: The MAE reduction on AIR-Stream is only 2.35% (23.64 vs. 24.21), in stark contrast to ~21–22% on the two traffic datasets. The paper reports this result (line 245) but offers no analysis of what dataset properties or method limitations might explain this discrepancy. A brief diagnostic discussion would clarify the conditions under which STBP's advantages are most pronounced.
- **Sensitivity to the initial frozen period is not analyzed**: The backbone is trained only at τ=1 and then permanently frozen (Section 4.2). While the Online variant (full fine-tuning) is shown to degrade performance, this does not address whether performance would change if a different or later period were used as the initial training stage. A sensitivity study varying the freeze point would strengthen the practical robustness claims.
- **Privacy protection claim is unsupported**: Line 111 states the pattern bank "offers advantages in privacy protection" because it stores abstract parameters rather than raw data. No analysis or citation supports the claim that these parameters are not invertible to original data. The claim should be moderated or removed.

### Trivial
- **Three parameter groups (i=0,1,2) in the pattern bank are introduced without justification** (Section 4.2, line 107). A sentence explaining their designated roles would aid clarity.
- **The toy dataset in the efficiency study (Figure 8) is not described** — size, generation method, and node counts are absent from the main text.
- **Few-shot experimental details are incomplete in the main text** — the number of few-shot periods and total incremental periods are deferred to the appendix but would benefit from brief mention in Section 5.1.

## Nice-to-Haves
- An ablation replacing FreNet with a standard temporal convolution (TCN) or MLP-mixer of equivalent capacity would test whether the frequency-domain design genuinely helps with distribution shifts.
- A sensitivity study varying which period serves as the initial training stage (e.g., starting at a later period) would demonstrate robustness to the choice of frozen backbone.
- A brief diagnostic on AIR-Stream (e.g., measuring time-series stationarity or node expansion rate) could explain the smaller improvement and help readers understand STBP's domain of applicability.

## Removed Points
These points are flagged to be removed; treat them with caution.

- **Harsh Critic: DLGA dual-stream motivation unclear** — The paper explicitly states (line 129) that P^(2)_τ acts as an additional key "enabling the model to assess the relationship between evolving input patterns and stored knowledge." This is adequately motivated. Removed.
- **Harsh Critic: Case study oversells findings** — The claim that the pattern bank "autonomously distinguishes heterogeneous and relevant nodes" (line 105) is reasonably supported by Figure 6's t-SNE visualization showing meaningful clusters with distinct temporal patterns. The conclusion is proportionate to the evidence. Removed.
- **Harsh Critic: Graph expansion handling unclear** — The paper explicitly states that DLGA does not rely on predefined adjacency matrices and models correlations through attention (Section 4.3). This is a deliberate design choice, not an omission. Removed.
- **Harsh Critic: Missing number of incremental periods** — These are standard appendix-deferred details; the appendix was stripped by the parser but exists in the original submission. Removed.
- **Strength Finder: Generic/problem-importance strengths** — The strength "this paper addresses an important problem" was not included as it is generic and applies to nearly every paper. Only concrete, evidence-backed strengths were kept.

## Novel Insights
The review process did not surface genuinely novel insights beyond the paper's own contributions. The harsh critic's point about FreNet lacking independent validation is the most actionable observation — it identifies that the paper's claim about frequency-domain processing for drift mitigation is conflated with the overall backbone contribution, and isolating it would either strengthen or appropriately bound that specific claim.

## Suggestions
- Add a FreNet-specific ablation (e.g., replace FreNet with a TCN of similar parameter count) to validate the frequency-domain claim independently.
- Include a short paragraph in Section 5.2 discussing the AIR-Stream discrepancy, with hypotheses about dataset properties that might reduce STBP's advantage.
- Clarify Eq. 5 by specifying that h_θ denotes whichever backbone submodule (FreNet, DLGA, or feedforward) the gating is applied to in a given context.
- Briefly justify the three parameter groups (P^(0), P^(1), P^(2)) with one sentence about their respective roles.

## Score and Decision

**Round 1 bracket**: The paper falls between 6.5 and 8.0 based on comparison with topically similar anchors: EAC (FRzCIlkM7I, 6.75) is the most directly comparable work (same task, similar prompt-based continual ST forecasting approach), while the 7.5+ anchors (PhyMPGN at 8.0, Time-MoE at 7.33) represent more transformative contributions in adjacent areas.

**Round 2 narrowing**: Within the 6.0–7.5 band, STBP is clearly stronger than EAC (6.75): it achieves substantially larger empirical improvements (21% vs. EAC's margins), uses a more sophisticated backbone architecture (FreNet+DLGA vs. simpler STGNN), and provides a more comprehensive evaluation suite including few-shot, efficiency scaling, and case studies. However, STBP falls short of the 7.5+ papers, which demonstrate deeper theoretical grounding or broader paradigm shifts. The remaining evidence gaps (FreNet not isolated, AIR-Stream discrepancy undiscussed, initial-period sensitivity unexamined) are real but minor — they do not undermine the central contribution.

**Anchors reviewed**:
| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| FRzCIlkM7I (EAC) | 6.75 | R1/R2 | STBP is stronger: better backbone, larger improvements, more comprehensive evaluation |
| mkjKqeBXkt (KITS) | 5.67 | R1 | STBP is substantially stronger in both contribution and evaluation |
| fU8H4lzkIm (PhyMPGN) | 8.00 | R1 | PhyMPGN has deeper novelty and theoretical grounding; STBP is more applied and incremental |
| V6uxd8MEqw (MISA) | 6.50 | R2 | STBP has more domain-specific novelty and stronger empirical results in its domain |
| uKZdlihDDn | 7.60 | R1 | More transformative contribution in a different area |
| Cjz9Xhm7sI | 8.00 | R1 | More transformative contribution in a different area |
| GRMfXcAAFh | 8.00 | R1 | More transformative contribution in a different area |

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>