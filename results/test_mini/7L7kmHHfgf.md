Now I have all the information I need. Let me construct the final review.

## Summary

This paper proposes PIRN, a prototype-driven reconstruction framework for few-shot multimodal anomaly detection (MAD) using RGB and surface-normal inputs. Three core innovations are introduced: Balanced Prototype Assignment (BPA) via optimal transport to prevent codebook collapse, Adaptive Prototype Refinement (APR) via gated GRU updates to handle unseen normal variations at inference, and Multimodal Normality Communication (MNC) for cross-modal knowledge transfer. Evaluated on MVTec-3D-AD, Eyecandies, and Real-IAD D3, PIRN achieves strong few-shot performance and substantial computational efficiency gains (85% fewer FLOPs vs FIND).

## Strengths

- **Consistent few-shot SOTA with controlled backbone for the strongest competitor**: PIRN outperforms the backbone-controlled INP-Former baseline (adapted with same ViT-B/14 DINOv2 backbone) by +3.7 AUROC_I at 10-shot MVTec-3D-AD (0.922 vs 0.885), and similarly across all shot settings (Table 1). This gap cannot be attributed to backbone choice.
- **Computational efficiency with top accuracy**: PIRN requires 103.36G FLOPs (17.49ms latency), which is 85% fewer FLOPs and 4.35× faster than FIND (728.46G, 76.09ms) while achieving essentially identical accuracy (0.922 vs 0.921 AUROC_I, Table 4). This combination of accuracy and efficiency is a genuine practical advantage.
- **Thorough ablation and analysis**: Each component is ablated (Table 2), prototype count and decoder depth are analyzed (Tables 5, 6), token aggregation methods for APR are compared (Table 7), and modality availability is decomposed (Table 3). The displacement analysis (Figure 4) provides mechanistic insight into how BPA routing separates normal vs anomalous tokens.
- **Strong Real-IAD D3 localization**: PIRN achieves the best pixel-level AUROC (0.961) on the challenging real-world dataset, and is top-2 in 13 out of 20 categories (Table 8).
- **Clear motivation and well-structured method**: The three challenges (codebook collapse, static prototypes, missing cross-modal interaction) are cogently described, and each module directly addresses one of them.

## Weaknesses

### Fatal
None.

### Major

1. **FIND omitted from the main results table despite being a near peer**. FIND (Li et al., 2025) achieves 0.921 AUROC_I on 10-shot MVTec-3D-AD in Table 4 — essentially tied with PIRN's 0.922. Yet FIND is absent from Table 1 (the main few-shot comparison across all settings). Including FIND only in the efficiency table while claiming "consistently superior performance" over existing baselines in Table 1 is a significant transparency gap. The paper should either include FIND in the main results table or clearly explain why it is omitted (e.g., if FIND's published evaluation does not cover all settings tested). This weakens the headline claim of "significant performance gains."

2. **Baseline training configurations in the few-shot setting are underspecified**. The paper does not describe whether BTF, AST, M3DM, CFM, and 3D-ADNAS were re-implemented or run with official code, what backbone they used (many of these methods were originally evaluated with ResNet-based backbones rather than DINOv2 ViT-B/14), or how hyperparameters were selected per shot setting. Only INP-Former specifies backbone control ("same ViT-B/14 backbone"). Without this information, the large margins over these baselines (e.g., +10.4% over M3DM at 10-shot) cannot be cleanly attributed to PIRN's method vs. a stronger frozen encoder. The paper must clarify, for each baseline: (a) whether official code was used, (b) what backbone and pretraining, (c) how hyperparameters were tuned per shot setting.

### Minor

3. **Ablation baseline decoder is not described**. Table 2's first row ("excludes all proposed modules") achieves 0.828 AUROC_I, but the paper never explains what this baseline decoder actually does — is it a simple linear reconstruction, a standard attention decoder with no prototype codebook, or something else? Without this description, the ablation is not fully interpretable, and it is unclear whether the baseline is deliberately weak.

4. **Soft mining loss is referenced but not defined**. The training loss is described only as "a soft mining loss (Luo et al., 2025)" without specifying the exact formulation. For reproducibility, the loss function should be written out or the specific equation in INP-Former should be cited.

5. **Large detection/localization discrepancy on Real-IAD D3 not discussed**. For `frontline_head` (likely OCR for `frontal_head`), PIRN achieves AUROC_J = 0.717 (detection) vs AUROC_P = 0.993 (localization) — a 27.6 point gap that is by far the largest among the reported methods. The paper does not comment on this. While not invalidating the overall results, unexplained class-level failures reduce credibility.

### Trivial

6. **Sinkhorn iteration count not specified**. The paper reports FLOPs/latency for OT-based modules but does not state how many Sinkhorn iterations were used during training and inference, which is relevant for reproducibility and understanding the efficiency numbers.

## Nice-to-Haves

- An experiment validating APR's robustness to anomalous inputs at inference (e.g., measuring prototype drift when synthetic anomalies are introduced vs. clean normal inputs). The paper's argument that anomalous patches contribute diffusely to OT assignments is plausible but empirically unverified.
- Reporting learned gate values ($g_{rgb}$, $g_{sn}$) in MNC to show whether cross-modal injection is aggressive or conservative.
- Re-running the top-2 baselines (INP-Former and FIND) with the same DINOv2 backbone and training pipeline on all few-shot settings to eliminate any remaining backbone confound.

## Removed Points

- **Prototype contamination as a fatal flaw**: The critic asserted this as a "methodological gap that limits confidence," but the paper already provides a principled argument (OT diffusion for anomalous patches, GRU gating). The concern is speculative and not a verified weakness; it is better framed as a nice-to-have experiment.
- **"First to integrate VQ prototype codebook" overclaim**: The critic questioned whether this claim needs verification. The paper already qualifies it with "To the best of our knowledge," and the claim is not central to the evaluation. This is a presentation nitpick, not a substantive weakness.
- **Missing related works / code release / missing appendix content**: Removed per instructions (code/appendix availability are not evaluable from the parsed text; missing related works cannot be verified without external sources).
- **Formatting/style nitpicks and typos**: These are parser artifacts, not author errors.
- **Strength Finder generic strengths** (e.g., "addressed an important problem"): Removed as generic; only specific, evidence-grounded strengths are retained.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a consistent pattern across prototype-based AD papers at this venue: both PIRN and the similar UIP-AD (avg 4.00) were criticized for omitting a closely related SOTA baseline (FIND and INP-Former, respectively) from the main results table. This suggests that the community norms around baseline inclusion in few-shot MAD papers are still being established, and reviewers are increasingly sensitive to selective baseline reporting.

## Suggestions

1. Include FIND in the main few-shot results table (Table 1) across all shot settings, not just in the efficiency comparison. This is the single highest-impact action for improving the paper's credibility.
2. Document the backbone, training protocol, and hyperparameter selection for every baseline in the few-shot setting. If baselines were run with their original weaker backbones while PIRN uses DINOv2, state this explicitly and acknowledge the gap.
3. Describe what the "excludes all proposed modules" ablation baseline actually does architecturally (e.g., "a 2-layer MLP decoder with no prototype codebook and cosine reconstruction loss").
4. Define the soft mining loss explicitly (either write the equation or cite the specific equation from INP-Former).
5. Briefly comment on the frontal_head detection-localization discrepancy in Real-IAD D3.

## Score and Decision

### Calibration Procedure

**Round 1 — Bracketing** (search topic: "few-shot anomaly detection multimodal prototype reconstruction"):
- Low band (avg < 3.5): DPNR (2.00), various prototype/VLM papers (3.00). PIRN is clearly stronger.
- Mid band (3.5–7.5): UIP-AD (4.00), DCR²-AD (5.00), TokenCLIP (5.50), FoundAD (6.00). PIRN's closest peers.
- High band (avg > 7.5): avg 8.00 (oral/poster papers, different topics). PIRN is not at this level.

**Round 1 bracket**: 5.0–6.5.

**Round 2 — Narrowing** (2 queries inside the bracket):
- TokenCLIP (5.50, Reject): Zero-shot AD with OT alignment. PIRN has a stronger method contribution and more datasets but weaker baseline transparency. Comparable overall, PIRN slightly stronger.
- FoundAD (6.00, Accept Poster): Few-shot AD with frozen foundation encoders. Similar level of contribution; PIRN has more thorough ablations and 3 benchmarks vs 2, but FoundAD's evaluation is better controlled. PIRN is slightly weaker on experimental rigor.
- UIP-AD (4.00, Withdrawn/Reject): Almost identical topic (multimodal AD, prototypes). PIRN is clearly stronger (better ablations, backbone-controlled INP-Former baseline, efficiency analysis).

**Final calibration**: PIRN sits between TokenCLIP (5.50, Reject) and FoundAD (6.00, Accept Poster). The method is novel and the experiments are mostly solid, but the two major weaknesses (FIND omitted from Table 1, underspecified baseline configurations) prevent it from reaching FoundAD's level of experimental trustworthiness. Score: **5.5**.

**Anchors used**:
| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| /home/wg25r/review_agent/human_reviews_2026/iO9CRytDvf.md (DPNR) | 2.00 | R1 low | Much weaker: false claims, missing results |
| /home/wg25r/review_agent/human_reviews_2026/Mam9PS8ENb.md (UIP-AD) | 4.00 | R1 mid | Weaker: missing INP-Former baseline, fewer ablations |
| /home/wg25r/review_agent/human_reviews_2026/qqlWHIjJ24.md (DCR²-AD) | 5.00 | R1 mid | Different topic (MLLM reasoning); similar score band |
| /home/wg25r/review_agent/human_reviews_2026/ny5Jrfhy61.md (TokenCLIP) | 5.50 | R2 | Comparable: both use OT, similar rigor level. PIRN slightly stronger method, slightly weaker baseline controls |
| /home/wg25r/review_agent/human_reviews_2026/YRrlJ8oVEH.md (FoundAD) | 6.00 (Accept Poster) | R2 | Stronger experimental control; PIRN has more comprehensive ablations |

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>