Now let me produce the final, polished review.

## Summary

The paper introduces SambaMOTR, a multiple object tracker that uses synchronized state-space models (SSMs) for query propagation. The core idea is to model each tracklet's history with an SSM (Mamba) and synchronize hidden states across tracklets via self-attention, enabling joint modeling of long-range temporal dependencies and tracklet interactions. Additional contributions include MaskObs (handling uncertain observations during occlusions) and an efficient long-sequence training recipe. SambaMOTR achieves substantial SOTA improvements on DanceTrack (+3.8 HOTA, +5.2 AssA), BFT (+2.8 HOTA), and SportsMOT (69.8 HOTA).

## Strengths

1. **Novel and well-motivated synchronization mechanism for set-of-sequences SSMs**: Samba introduces memory synchronization (Eq. 3, lines 150–161) where hidden states across tracklets interact via self-attention before output projection, going beyond prior work (e.g., MeMOTR's independent EMA-based processing of each tracklet). The ablation confirms that synchronization alone yields >1% improvement across all metrics (line 267).

2. **Substantial and consistent SOTA gains across three challenging datasets**: SambaMOTR achieves +3.8 HOTA/+5.2 AssA on DanceTrack over MeMOTR (line 247); +2.8 HOTA/+4.9 AssA on BFT over OC-SORT (line 250); and 69.8 HOTA on SportsMOT with +4.6 AssA over OC-SORT (lines 254–255). These are large, consistent margins across datasets with very different motion patterns (dance, bird flocks, team sports).

3. **MaskObs provides principled occlusion handling**: Unlike prior methods that freeze track queries during occlusions (MOTRv2, MeMOTR), MaskObs (Eq. 5, line 182) masks uncertain observations from the SSM state update while still updating hidden states using long-term memory and interactions with other tracklets. Ablation shows +1.3 HOTA improvement (line 265).

4. **Efficient long-sequence training recipe**: Training on 10-frame sequences with gradients only on the last 5 frames (line 190) enables learning longer-range dependencies without increased GPU memory. Ablation shows +1.9 AssA improvement (line 269) and the paper notes this strategy is compatible with existing frameworks.

5. **Honest limitations section**: The paper explicitly acknowledges the quadratic complexity in the number of sequences due to self-attention in synchronization (line 279), and the issue of dropped tracklets leaving the scene before N_miss expires (lines 277–278), with a concrete suggestion for future work (long-term re-identification).

## Weaknesses

### Major

1. **Overclaimed "without any hand-crafted heuristics" contradicted by the paper's own design choices**: The abstract states that SambaMOTR "implicitly learns to track objects accurately through occlusions without any hand-crafted heuristics" (line 4). Yet the method relies on τ_mask=0.5 for MaskObs (line 182), τ_det=0.5 for newborn object initialization (line 196), τ_track=0.5 for track inactivity (line 198), and N_miss tuned per dataset (35/20/50) "due to different dataset dynamics" (line 233). These are explicitly hand-set thresholds. While the core *propagation* is learned (contrasting with Kalman-filter-based methods), the unqualified claim in the abstract is too strong and should be revised to accurately describe what is learned vs. what is set by hand.

### Minor

2. **"Linear-time" complexity claim stated too broadly without qualification**: The paper calls Samba a "novel linear-time set-of-sequences model" in the abstract, introduction (lines 32, 36, 45), and conclusion (line 286) without qualification. The Limitations section (line 279) then reveals that Samba has "quadratic complexity in the number of sequences due to the use of self-attention in memory synchronization." While "linear in sequence length" is the standard reading in the SSM literature and the number of tracklets is bounded in practice, the unqualified repetition of "linear-time" across all prominent positions conflates two complexity axes. Clarifying this distinction upfront rather than relegating it to Limitations would prevent misleading readers.

3. **Sources of improvement not fully decomposed**: Line 263 states that the vanilla Mamba baseline (without synchronization or MaskObs) "outperforms MeMOTR's EMA-based history and temporal attention module." This means a nontrivial portion of the headline SOTA gain over MeMOTR is attributable to the Mamba backbone rather than the paper's novel contributions (synchronization + MaskObs + long training). The ablation shows synchronization adds ~1% HOTA and MaskObs adds ~1.3% HOTA, but the paper does not explicitly quantify how much of the remaining gain comes from simply replacing EMA with Mamba. Decomposing this would allow readers to better assess the marginal value of each proposed component.

4. **Confidence function conf(·) is under-specified**: In the MaskObs description (lines 178–186), conf(x^i_t) is defined as "the predictive confidence of the corresponding bounding box" but does not specify whether this is the Deformable DETR classification score, objectness score, or something else. While this is a small detail, it affects reproducibility.

### Trivial

5. **Inference thresholds all set to 0.5 without ablation**: The paper states "For simplicity, τ_det=τ_track=τ_mask=0.5" (line 233) but provides no ablation or sensitivity analysis for these thresholds. A quick ablation showing robustness or trade-offs would be useful, especially since these are the very "hand-crafted heuristics" the abstract claims to avoid.

## Nice-to-Haves

- **Failure case analysis**: The paper reports aggregate HOTA/AssA gains but does not analyze where the model still fails. For a method that claims to address occlusions, a breakdown by occlusion duration or degree would be illuminating.
- **Model size or FLOPs comparison**: Speed is reported (16 FPS on RTX 4090) but parameter counts or FLOPs are not. Since the method adds self-attention over hidden states, comparing overhead relative to Mamba or MeMOTR would contextualize the acknowledged complexity trade-off.
- **Ablation on cheaper synchronization alternatives**: The paper could strengthen evidence for the *specific* form of synchronization (self-attention) by comparing with simpler interaction mechanisms (e.g., averaging hidden states, or no interaction), confirming that the added complexity is necessary.
- **Ablation on MaskObs threshold alternatives**: Testing whether MaskObs could be replaced by a soft weighting scheme (rather than the hard threshold τ_mask) would further validate the design choice.

## Removed Points

*These points were flagged by reviewers but removed after verification against the paper:*

- **Footnote generality claim not experimentally validated**: The footnote (line 31) states the approach "can, in principle, be applied to any sequence model that includes an intermediate memory representation." The harsh critic criticized this as a promise not kept. However, this is a speculative forward-looking statement in a footnote — not a central claim — and it is unreasonable to demand experimental validation of every possible extension. **REMOVED** as outside the paper's scope.
- **Criticism about missing comparison with methods that would require different evaluation protocols**: Not applicable. The paper compares fairly with prior work using the same detector (Deformable DETR) where possible (lines 242–243).
- **Generic concerns about "could the metric be measuring a proxy"**: The harsh critic's areas-of-concern sweep produced no such specific claims that survive verification. **REMOVED** as speculative.

## Novel Insights

None beyond the paper's own contributions. The paper's core insight — that synchronizing hidden states across multiple SSM-tracked sequences via self-attention enables joint modeling of trajectory interdependencies — is already well-articulated in the paper.

## Suggestions

1. **Revise the abstract and introduction** to qualify the "without any hand-crafted heuristics" and "linear-time" claims. For the former, clarify that the *propagation module* is learned end-to-end while simple inference thresholds remain. For the latter, clarify that complexity is linear in time (sequence length) but quadratic in the number of tracklets.
2. **Add an explicit decomposition** of how much of the SOTA gain over MeMOTR comes from switching to Mamba (without synchronization) versus the paper's novel additions (synchronization, MaskObs, long training). The ablation numbers are in the (parser-stripped) table; the prose should walk through this decomposition clearly.
3. **Specify exactly what conf(·) returns** — e.g., the maximum classification logit, the objectness score, or the detection confidence from Deformable DETR's classifier.

## Score and Decision

This paper makes a solid technical contribution: the idea of synchronizing SSM hidden states across tracklets is novel, well-motivated by the problem domain, and backed by substantial empirical gains on three challenging benchmarks. The ablations are thorough and the limitations are honestly discussed. The primary weaknesses are framing issues (overclaiming "without any hand-crafted heuristics" and unqualified "linear-time") that are fixable through careful rewriting, and a minor lack of granularity in decomposing the sources of improvement. The core method and evaluation are sound. I recommend acceptance with revisions addressing the framing concerns.

MY FINAL SCORE: <score>8.0</score>
MY FINAL DECISION: <decision>Accept</decision>