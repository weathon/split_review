Now I have all the information I need. Let me write the final consolidated review.

## Summary

This paper proposes STBP, a framework for continual spatio-temporal forecasting (CSTF) that combines a frequency-domain spatio-temporal backbone (FreNet + DLGA) with an expandable per-node contextual pattern bank. During incremental training after the first stage, the backbone is frozen to preserve general knowledge while the pattern bank is expanded and fine-tuned, interacting with the backbone via gating and dual-stream attention mechanisms. Experiments on three datasets (PEMS-Stream, CA-Stream, AIR-Stream) show large improvements on traffic data (~21% MAE reduction) and competitive results on air quality, with convincing few-shot performance.

## Strengths

1. **Linear-time dual-stream graph attention (DLGA) reduces spatial complexity from O(N²) to O(N) while incorporating pattern-bank knowledge as an extra key stream.** The DLGA module (Eqs. 7–9) uses random-feature-mapping linear attention and adds the contextual pattern bank P_τ^(2) as a second key, avoiding explicit adjacency matrix construction. The toy-dataset efficiency study (Figure 8) directly validates the linear memory scaling, and the ablation (Figure 4) shows DLGA removal causes significant performance degradation across all three datasets.

2. **Frequency-domain network (FreNet) with learnable spectral filtering provides a principled mechanism to mitigate distributional drift without relying on RNNs or TCNs.** The backbone applies FFT → learnable frequency embedding → IFFT (Eq. 6) to isolate stable low-frequency components. The ablation confirms the backbone's importance: the "w/o Backbone" variant (FreNet+DLGA replaced with CNN+GCN) performs substantially worse.

3. **Strong results on traffic datasets with large margins, and convincing few-shot performance.** On PEMS-Stream, STBP reduces average MAE by ~21.4% over the best CSTF baseline (12.31 vs. 15.67 for EAC/PECPM); on CA-Stream by ~21.9% (15.77 vs. 20.20). In the few-shot setting (Table 2) with only 10% training data in later periods, STBP outperforms all baselines by a substantial margin (MAE 13.58 vs. 16.13 for EAC on PEMS-Stream).

4. **The contextual pattern bank learns interpretable node clusters without explicit clustering supervision.** t-SNE visualizations (Figures 3 and 6) show that after training, the pattern bank organizes nodes into clusters with distinct temporal dynamics, and new nodes from later periods are correctly grouped into existing clusters, providing qualitative evidence of generalization.

## Weaknesses

### Fatal
None.

### Major

1. **The marginal improvement on AIR-Stream (2.35%) vs. ~21% on traffic datasets is not discussed, and at some metrics STBP is actually worse than baselines — weakening the claim of being a "general" backbone.** On AIR-Stream, STBP's average MAE is 23.64 vs. 24.21 for PECPM (only 2.35% improvement). At RMSE horizon 6, STBP scores **39.81 vs. PECPM's 39.63** — meaning STBP is *worse* at this specific metric — yet the table bolding makes STBP appear uniformly best. The paper offers no discussion of why the method's effectiveness varies so dramatically by domain (traffic vs. air quality), despite explicitly claiming a "general spatio-temporal backbone." This is a significant gap because the method's design (frequency-domain filtering for strong periodicity, per-node parameterization for dense spatial correlations) may exploit traffic-specific structure in ways that do not transfer to domains with weaker periodicity or sparser spatial dependencies.

2. **No per-period performance trajectory is reported, which is critical for a continual learning method.** The paper reports metrics averaged across all incremental periods but never shows how STBP's accuracy evolves over time (e.g., whether it degrades, plateaus, or improves across periods). For a method whose core claim is mitigating catastrophic forgetting, this omission makes it impossible to distinguish between a method that stays stable versus one that starts strong but degrades.

### Minor

3. **Missing parameter count comparison.** The contextual pattern bank scales linearly with node count (N × d parameters). CSTF baselines like EAC use compact prompt pools that do not scale linearly with node count. The paper reports training time and GPU memory but never total parameter counts for any method, making it difficult to attribute performance advantages to algorithmic design versus raw parameter capacity.

4. **The "w/o Backbone" ablation is underspecified regarding interaction mechanism.** The ablation replaces FreNet+DLGA with CNN+GCN while retaining the pattern bank, but it is not described how the pattern bank's prompts (P^(0), P^(1), P^(2)) are rerouted through the CNN+GCN backbone. The gating mechanism in Eq. 5 and the dual-stream attention in Eq. 9 are designed around the specific backbone architecture, so it is unclear whether the comparison isolates backbone quality or measures a misalignment between the prompt mechanism and the replacement architecture.

5. **The specific random feature map for linear attention is not named in the main text.** The paper says "Softmax used for approximation in our implementation" and defers to the appendix, but the choice of random feature map (e.g., positive orthogonal features vs. the exp-sin/cos approximation) affects numerical behavior and reproducibility.

### Trivial
None.

## Nice-to-Haves
- A discussion analyzing why STBP works well on traffic (strong daily periodicity, dense spatial correlations) but less well on air quality (weaker periodicity, sparser correlations) would honestly bound the method's scope and strengthen the paper.
- Adding a clean ablation that isolates the dual-stream attention mechanism (standard linear attention without P^(2) as extra key) would better quantify the benefit of the prompt-key mechanism specifically.

## Removed Points

These points were raised in the reviews but are removed or demoted for the following reasons:

- **"The 21%+ improvements are inflated by handicapped baselines (GWNet, STID retrained from scratch)"** — The paper's reported improvement of 21.44% is "compared with the best baseline." On PEMS-Stream, the best baseline is PECPM (a CSTF method) at 15.67 MAE, not the retrained-from-scratch GWNet at 19.87+. The 21% figure is computed against the best CSTF method and is thus not inflated by the conventional baselines. The paper is transparent that GWNet/STID are retrained from scratch following prior work (Chen & Liang, 2025). **Removed as factually inaccurate.**

- **"The paper never acknowledges the near-tie on AIR-Stream"** — The paper explicitly reports the 2.35% improvement number on AIR-Stream (line 238), acknowledging the marginal gain. While it does not discuss *why*, it does acknowledge the magnitude. **Partially removed — the "never acknowledges" claim is inaccurate, but the lack of explanation remains as Weakness #1.**

- **"EAC as an ablation variant is confusing"** — The ablation study includes EAC as a comparison reference alongside method variants. This is standard practice. **Removed as nitpick.**

- **"The paper's backbone claims are misleading because EAC and PECPM's prompt mechanisms are not 'simple'"** — The paper's characterization refers to backbone architecture (stacks of graph and temporal convolutions), not to the prompt mechanisms. This is a reasonable characterization of the field. **Removed.**

## Novel Insights

None beyond the paper's own contributions. The dual-stream linear attention mechanism that uses the pattern bank as an extra key (Eq. 9) is the most novel architectural contribution, and the few-shot experiment provides the strongest evidence for the frozen-backbone + expanding-pattern-bank design's generalization ability.

## Suggestions

1. Add a per-period accuracy trajectory plot showing STBP's MAE/RMSE across each incremental period to demonstrate true continual learning (stability) rather than just averaged performance.
2. Report total parameter counts for all methods, broken down by backbone and pattern bank/prompt pool components, to enable fair comparison of efficiency.
3. Add a discussion section addressing why performance differs between traffic and air quality domains, including implications for the method's generality.
4. Specify the exact random feature map used (in the main text) and the Softmax approximation details for reproducibility.
5. Clarify how the pattern bank prompts interact with the CNN+GCN backbone in the "w/o Backbone" ablation, or replace it with an ablation that removes only the dual-stream mechanism while keeping FreNet.

### Calibration Report

All anchor papers retrieved:

**Round 1 (Bracketing):**
| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| 0je4SA7Jjg.md (Cell-embedded GNNs) | 3.40 | 1 | Different task (physical simulation); less relevant |
| 5x9kfRXhBd.md (Forex forecasting) | 3.00 | 1 | Different domain; less relevant |
| TYyzypZrgU.md (Domain-grounding) | 2.50 | 1 | Different topic; less relevant |
| NIhRwzqhUz.md (Dynamic TSP) | 3.00 | 1 | Different problem; less relevant |
| FRzCIlkM7I.md (EAC paper) | **6.75** | 1 | **Directly comparable** — same CSTF sub-area, prompt tuning. STBP has stronger traffic results but weaker AIR-Stream results and similar evaluation gaps (no per-period curves, parameter bloat concerns). Slightly weaker overall due to undiscussed domain discrepancy. |
| vJGKYWC8j8.md (TFMoE) | 4.00 | 1 | Similar task but only one dataset. STBP is clearly stronger (3 datasets, stronger novelty, better results). |
| uiyljVIP0k.md (S2GNN) | 5.40 | 1 | Spectral GNN for STF. STBP has clearer motivation, more coherent story, better results. Stronger than S2GNN. |
| H1nykRhieN.md (MvHSTM) | 4.00 | 1 | Different task (static traffic forecasting). Less relevant. |
| Cjz9Xhm7sI.md (Weather nowcasting) | 8.00 | 1 | Different task (3D radar prediction). Less relevant. |
| uKZdlihDDn.md (Fluid simulations) | 7.60 | 1 | Different task. Less relevant. |
| cmfyMV45XO.md (Feedback NODEs) | 8.00 | 1 | Different topic. Less relevant. |
| KbetDM33YG.md (Online GNN eval) | 8.00 | 1 | Different topic. Less relevant. |

**Round 2 (Narrowing within 4.5–7.5):**
| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| rGdEM131Ht.md (Time-frequency EBM) | 5.60 | 2 | Different task (generative time series). Less directly comparable. |
| uiyljVIP0k.md (S2GNN) | 5.40 | 2 | Already discussed above. |
| mUDazL3mTJ.md (FDN) | 4.75 | 2 | Interpretable ST forecasting. Less novel architecture. STBP is stronger. |
| drovOv7IKB.md (FreCoformer) | 5.00 | 2 | Frequency-domain time series. Different task. |
| kVlfYvIqaK.md (DyGPrompt) | **6.00** | 2 | **Comparable** — prompt learning on dynamic graphs. All 6s. STBP has more comprehensive experiments and stronger forecasting results. Comparable quality. |
| V6uxd8MEqw.md (MISA prompt CL) | 6.50 | 2 | General continual learning (not ST-specific). Less directly comparable. |
| rjuZyMfLSd.md (System dynamics CL) | 6.25 | 2 | Continual learning for physical dynamics. Less directly comparable. |
| akKNGGWegr.md (ST knowledge distillation) | 5.25 | 2 | Different approach (distillation). Less relevant. |
| N0nTk5BSvO.md (TESTAM) | **5.75** | 2 | **Comparable** — traffic forecasting with MoE. Similar evaluation depth. STBP has larger improvements and better ablation but similar gaps (missing complexity analysis). STBP is slightly stronger. |
| vXSCD3ToCS.md (DynST) | 4.60 | 2 | Dataset paper. Different contribution type. |

**Round-1 bracket:** The paper clearly sits in the middle band (between ~4 and ~7). It is substantially stronger than papers at 3–4 (TFMoE, S2GNN) but has gaps relative to the top CSTF paper (EAC at 6.75).

**Round-2 narrowing:** Comparing against the most relevant anchors (EAC at 6.75, DyGPrompt at 6.00, TESTAM at 5.75), STBP is:
- **Slightly weaker than** EAC (6.75): EAC has a cleaner "expand and compress" principle, tested on more diverse data (traffic, weather, energy), while STBP's AIR-Stream results are much weaker than its traffic results and this is undiscussed. STBP also lacks per-period curves that EAC provides.
- **Comparable to or slightly stronger than** DyGPrompt (6.00) and TESTAM (5.75): STBP has stronger experimental results and more architectural novelty than TESTAM, and more comprehensive evaluation than DyGPrompt.

Given the genuine contributions (DLGA, FreNet, strong few-shot results) weighed against the significant evaluation gaps (undiscussed domain discrepancy, no per-period curves, no parameter counts), a final score of **6.0** is appropriate — a solid paper with real contributions but with clear weaknesses that prevent a higher score.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>