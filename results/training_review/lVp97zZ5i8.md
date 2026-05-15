Now I have all the evidence needed to cross-check the reviewer's claims. Let me produce the final review.

---

## Summary

TempMe proposes a temporal token merging method for efficient text-video retrieval, built on a two-stage progressive multi-granularity framework (ImgMe + ClipMe) that merges redundant tokens across video frames. The core idea — that temporal redundancy across frames is a major source of inefficiency that existing image-level token compression methods (ToMe, DiffRate) fail to address — is well motivated. On MSRVTT with ViT-B/16, TempMe reduces output tokens to 5% of the baseline while simultaneously improving R-Sum by 4.4–5.3 points over prior efficient methods, with consistent gains across four datasets and both ViT-B/32 and ViT-B/16 backbones.

## Strengths

- **Identifies and addresses temporal redundancy as a distinct bottleneck in efficient text-video retrieval.** The paper clearly motivates why image-level token compression (ToMe, DiffRate) is insufficient for video: these methods only handle intra-frame spatial redundancy and ignore the far larger temporal redundancy across frames (Figure 1a). The proposed cross-frame merging directly targets this gap. The paper shows that applying ToMe within each frame (ImgMe) actually *hurts* accuracy compared to the LoRA baseline (191.4 vs 193.0 R-Sum, Table 8), underscoring the need for temporal-aware merging.

- **Achieves a strong accuracy-efficiency trade-off against prior SOTA methods.** On MSRVTT with ViT-B/16, TempMe reaches an R-Sum of 206.7 using 121.4 GFLOPs and 127 output tokens (5% of input), outperforming parameter-efficient methods like VoP (202.3 R-Sum, 246.2 GFLOPs) and DGL (200.7, 251.2) in *both* accuracy and efficiency simultaneously (Table 2). The improvements are consistent across ActivityNet, DiDeMo, and LSMDC (Table 3). Against LoRA alone (the underlying base method), TempMe improves R-Sum by 5.6 points while reducing GFLOPs by 34%.

- **Comprehensive ablation studies isolate component contributions.** Table 8 shows ImgMe (spatial merging alone) hurts accuracy while ClipMe recovers it, and Table 9 disentangles the roles of Temporal Modeling (cross-frame attention for accuracy) from Token Reduction (efficiency gains). The paper also ablates frame count, merging strategies, and clip positional embeddings (Section 4.4).

- **Generalization experiments show applicability beyond the core setting.** TempMe improves full fine-tuning of CLIP4Clip with a 7.9% R-Sum gain, 1.57× training speedup, and reduced memory (52.7 GB vs 70.1 GB). It also extends to a video foundation model (UMT), though with caveats discussed below.

## Weaknesses

### Fatal
None.

### Major
- **The accuracy-efficiency trade-off revealed by the ablation is not discussed.** Table 9 shows that "Temporal Modeling" alone (cross-frame attention without token reduction) achieves R-Sum 199.7 with 54.3 GFLOPs, while the full TempMe achieves R-Sum 198.6 with 34.8 GFLOPs. This is a clean Pareto trade-off: you lose 1.1 R-Sum points for a 36% GFLOP reduction. The paper presents TempMe as the definitive solution ("lower complexity and better performance" in the abstract), but never explicitly acknowledges that its own temporal-modeling-only variant is strictly more accurate (though less efficient). The paper's headline claims (e.g., 4.4% R-Sum improvement over VoP/DGL) are against prior SOTA and remain valid, but the omission of this trade-off from the narrative is a significant oversight that makes the contribution look more Pareto-optimal than it actually is. The authors should include the temporal-modeling-only row in the main comparison tables and explicitly discuss the trade-off.

- **Key implementation details are missing, affecting reproducibility.** (a) The merging ratios \(R_c\) and \(R_I\) (defined in Section 3.2) are never given numeric values — only qualitative descriptions like "a large subset" and "a larger proportion." (b) The number and placement of ClipMe blocks are not specified (the paper mentions a progressive framework but doesn't state how many ClipMe blocks are used or at which transformer layers they operate). (c) The r value for ImgMe is given (r=2 for ViT-B/32, r=10 for ViT-B/16), but the corresponding merging ratios for the ClipMe block are absent. Without these, the method cannot be faithfully reproduced.

### Minor
- **The UMT generalization experiment compares against a deliberately modified baseline.** To apply TempMe to UMT (which natively processes all frame tokens jointly), the paper introduces UMT4Clip — a version where UMT processes frames individually, which the paper acknowledges "inevitably lead[s] to a decline in performance" (206.7 vs 212.3 R-Sum). The claim "performance close to UMT while requiring only one-third GFLOPs" (p. 7) compares UMT4Clip+TempMe (209.2) directly against UMT (212.3), not against UMT4Clip (206.7). While the paper provides the UMT4Clip baseline for transparency, the comparison against original UMT overstates how well TempMe transfers to joint spatio-temporal architectures. A more direct integration of TempMe into UMT's native architecture (without degrading UMT first) would be a cleaner demonstration of generality.

- **No error bars or variance reported for any result.** Table 6 mentions that "each experiment was conducted five times with different random seeds" yet reports only point estimates. Since some margins over baselines are small (e.g., 1–4 R-Sum points), the reader cannot assess whether differences are meaningful or due to seed variation. While single-run evaluation is common practice in parts of this field (making this a minor rather than major issue), the fact that the authors collected multi-seed data but did not report it is a missed opportunity.

### Trivial
- The ablation distinction between "Temporal Modeling" and "Token Reduction" (Table 9) could be more precisely defined. The paper's text description (Section 4.4.2) explains what each function does at a high level, but it is not explicitly stated whether "Temporal Modeling" = the ClipMe block *without* merging operations, or whether it includes ImgMe merging. Clarifying the exact module configuration of each row would improve interpretability.

## Nice-to-Haves
- An ablation of the merging ratios \(R_c\) and \(R_I\) (sweep from 0.25 to 1.0) showing the accuracy-FLOPs Pareto frontier.
- Failure case analysis: Are there video categories (fast cuts, high motion, occlusions) where TempMe degrades accuracy? The paper currently assumes uniform temporal redundancy.
- Reporting standard deviations for the multi-seed experiments already conducted in Table 6.
- Direct application of TempMe to joint spatio-temporal models (VideoMAE, UMT) without first degrading them to per-frame processing.

## Removed Points
These points are flagged to be removed; treat them with caution.

- *"The '95% token reduction' and '51% GFLOPs reduction' claims are tied to specific configurations and used generically"* — The paper explicitly contextualizes these numbers with "With ViT-B/16 as the backbone on MSRVTT" (Figure 1d). The numbers are correctly computed for that setting and not presented as universal. **Removed: factually incorrect criticism.**

- *"Figure 5 qualitative...does not demonstrate any retrieval benefit"* — Qualitative token-merging visualizations are by design illustrative; the retrieval results are quantitatively validated in all main tables. This criticism applies to qualitative figures generically. **Removed: generic nitpick.**

- *"Table 1 token count format should clarify whether the transformer operates on a single long sequence or multiple sequences"* — The output format \(1 \times 97\) unambiguously indicates a single sequence after temporal merging. **Removed: answered by the paper's own notation.**

- *"The paper should compare training costs for parameter-efficient settings"* — The paper's focus is primarily on **inference** efficiency (which is where token merging matters most in this setting). **Removed: scope creep.**

## Novel Insights

The most interesting observation emerging from the reviews — beyond the paper's own contributions — is that the ablation (Table 9) reveals a clean decomposition of TempMe into two opposing forces: cross-frame *attention* (Temporal Modeling) that improves accuracy at a computational cost, and cross-frame *merging* (Token Reduction) that cuts computation but degrades accuracy. The full TempMe is the equilibrium point where the accuracy gains from temporal attention mostly compensate for the accuracy loss from aggressive token reduction, yielding a net accuracy improvement over LoRA with substantially lower cost. This suggests that the method's success hinges on the temporal modeling (cross-frame attention) being strong enough to offset the information loss from merging — a design tension the paper could explore more explicitly (e.g., by varying the aggressiveness of merging across layers).

## Suggestions

1. **Add the temporal-modeling-only row to the main SOTA comparison (Table 2) and explicitly discuss the accuracy-efficiency trade-off** in the narrative. This would make the paper's contribution more transparent and strengthen, not weaken, the overall framing.

2. **Specify numeric values for \(R_c\) and \(R_I\) and the number/placement of ClipMe blocks** either in the main text or in a reproducibility statement. These details are essential for reproducing the reported results.

3. **Report standard deviations for the multi-seed experiments (Table 6)** that the authors already ran but did not present, and add a brief statement about run counts for other experiments.

4. **Reframe the UMT experiment** to more clearly separate the baseline degradation (UMT4Clip vs UMT) from the benefit of TempMe (UMT4Clip vs UMT4Clip+TempMe). The comparison against original UMT should be presented as a reference point with the caveat that UMT was modified, not as a direct claim.

## Score and Decision

The paper makes a genuine contribution — identifying and addressing temporal redundancy via cross-frame token merging for video-text retrieval — and supports it with extensive experiments across four datasets and multiple backbones. The weaknesses (the unacknowledged accuracy-efficiency trade-off in the ablation, missing implementation details, no error bars, and the somewhat strained UMT comparison) are real but addressable and do not invalidate the core claims against prior SOTA. The work is original, the experiments are sound (if incomplete on one dimension), and the findings would be valuable to the community.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>