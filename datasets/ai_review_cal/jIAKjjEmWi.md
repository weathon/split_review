- Decision: Reject
- Avg Score: 4.00
- Scores: 3, 5, 3, 5
Now I have a thorough understanding of the paper. Let me write the final consolidated review.

## Summary

This paper introduces A-MoD, a parameter-free routing mechanism for Mixture-of-Depths (MoD) transformers that computes token importance scores directly from the attention maps of the preceding layer, eliminating the need for a learned linear router. Evaluated on ImageNet finetuning and transfer learning across four ViT architectures (DeiT-Tiny, DeiT-Small, ViT-Base, ViT-Large) at two capacity levels (50%, 12.5%), the method consistently outperforms standard MoD routing with accuracy gains of up to 2% and achieves up to 2× faster convergence during transfer learning.

## Strengths

- **Consistent accuracy improvement over standard MoD on ImageNet finetuning**: Table 1 and the accompanying text show A-MoD outperforming standard routing across all four model sizes at both capacity levels, with the largest gains (up to 2.3%) for smaller models like DeiT-Tiny (68.20 vs. 65.90 at 50% capacity). The trends are consistent across architectures — a strength of breadth.

- **Faster convergence, especially from pretrained checkpoints**: Section 4.3 reports concrete convergence improvements: e.g., on Flowers102 with ViT-Large, A-MoD reaches 94.5% accuracy in 35 epochs while standard routing requires 100 epochs to reach the same value. This is a practical benefit directly attributable to reusing pretrained attention maps rather than learning a router from scratch.

- **Near-zero-shot capability**: Figure 3(c) shows A-MoD achieving 78% accuracy on ImageNet without any additional training when adapted from a pretrained checkpoint, because the existing attention maps already identify task-relevant tokens. Standard routing cannot do this since its router must be learned.

- **Higher correlation with token importance than standard routing**: Figure 7 and the associated analysis show that A-MoD's routing scores correlate strongly with leave-one-out token importance (p-values < 10⁻⁸), whereas standard routing sometimes shows negative correlation with large p-values (>0.5 in some layers). This provides mechanistic evidence that attention maps encode meaningful importance signals.

- **Training stability across learning rates**: Section 4.2 notes a learning rate sweep (Figure 13) where A-MoD outperforms standard MoD for every tested learning rate, indicating reduced sensitivity to this hyperparameter.

## Weaknesses

### Fatal
None.

### Major

- **No measures of variance or statistical significance across runs.** All reported results appear to be single runs. Table 1 reports accuracy without standard deviations, and no experiment is described as seed-averaged. Given that many performance gaps are in the 0.5–2% range (and A-MoD is marginally worse for ViT-Base at 12.5% capacity), the reader cannot assess whether the reported improvements are reliable or within noise. This is the single most significant evidential weakness. The paper shows consistent directional trends across 4 architectures × 2 capacities × multiple datasets, which partially mitigates the concern, but the absence of variance reporting is a methodological gap.

- **Contribution 1 overclaims relative to the transfer learning findings.** Contribution 1 states: "We find that MoD is not only viable but also advantageous for visual tasks, providing empirical evidence that it can outperform traditional models in terms of both FLOPs and performance." However, Section 4.3 explicitly states: *"We find that MoD models are unable to match the isoFLOP model performance on transfer tasks."* The ImageNet finetuning results (Table 1) support the claim, but the transfer results — where *neither* MoD variant matches the isoFLOP baseline — directly contradict the unqualified version. The paper acknowledges this as a limitation of MoD in general, but the abstract and contribution statement do not reflect this nuance. The narrative should be scoped more precisely: A-MoD improves over standard MoD routing, and MoD with A-MoD can outperform isoFLOP models on in-distribution finetuning, but MoD (regardless of router) lags behind isoFLOP on transfer tasks.

### Minor

- **Attention map quality not verified for larger models.** The paper cites Darcet et al. (2024) on attention collapse in larger ViTs (lines 172–173) — where attention maps concentrate on a single token and lose semantic meaning — but does not verify whether the ViT-Large models used in the experiments suffer from this phenomenon. Since A-MoD's routing depends entirely on attention map quality, demonstrating that attention maps remain meaningful for the larger architectures in the study would strengthen confidence in the method's generality.

- **The isoFLOP model recalculation is unclear in the layer ablation (Section 4.5).** When MoD layers are restricted to later layers and early layers are kept dense, the FLOP budget changes. The paper states A-MoD "is able to match the corresponding isoFLOP baseline" (line 183), but it does not specify whether the isoFLOP baseline was recalculated to match the new architecture. A brief clarification is needed.

- **The leave-one-out correlation analysis, while informative, is an indirect validation.** The paper claims A-MoD makes "better routing decisions" (line 35), but the evidence is correlational. A more direct causal test — e.g., comparing accuracy obtained via A-MoD routing vs. random routing vs. an oracle that selects tokens with the largest leave-one-out loss — would more directly support this claim. The current analysis is consistent with the claim but does not prove it.

### Trivial
None.

## Nice-to-Haves

- **From-scratch training experiment.** The paper only evaluates from pretrained checkpoints. While this is the explicitly stated use case (A-MoD is designed for adapting pretrained transformers), a from-scratch experiment would clarify whether the benefits of attention-based routing are intrinsic or depend on pretrained attention maps.

- **Wall-clock throughput comparison.** The paper claims "no additional computational overhead" (line 48) but does not measure throughput. The standard router's linear layer is cheap, so the difference is unlikely to matter, but a brief wall-time comparison would substantiate the claim.

## Removed Points

These points are flagged to be removed; treat them with caution:

1. **Circular dependency in leave-one-out analysis (Harsh Critic, point 2).** The critic claimed A-MoD's high correlation could reflect that "attention maps themselves are used to compute both the routing scores and the attention maps that produce the loss, creating a circular dependency." This is factually incorrect: the paper explicitly states the leave-one-out importance is computed *on the vanilla transformer* (line 174: "if that token is omitted in the vanilla transformer"), not on the MoD model. There is no circular dependency. **Removed as factually wrong.**

2. **Equation (2) notation ambiguity (Harsh Critic, Section-by-Section).** The critic suggested the equation is ambiguous about whether the `r_i` multiplication applies only to processed tokens. The equation (line 82–83) is standard and clearly shows the multiplication only in the `if` branch (processed tokens), not the `else` branch. **Removed as a misreading.**

3. **"Difficult to train" overstatement (Harsh Critic, Section-by-Section).** The critic claimed the paper overstates the difficulty of training MoD routers. This is a subjective opinion about the paper's framing, not a verifiable weakness. The paper cites known training instability in MoE/MoD literature (Zoph et al., 2022; Fedus et al., 2022b). **Removed as subjective.**

4. **Generic "from-scratch training" and "wall-clock time" as weaknesses rather than nice-to-haves.** Moved to Nice-to-Haves as they are outside the paper's stated scope or not standard for this type of empirical contribution.

5. **Generic strength about problem importance (Strength Finder).** The Strength Finder's framing about the problem being "important" is generic and not specific to this paper's contribution. However, the specific strengths listed are concrete and evidence-backed, so I retained all six specific points.

## Novel Insights

None beyond the paper's own contributions. The reviewers did not surface insights that go beyond what the paper itself argues.

## Suggestions

1. **Report seed-averaged results with confidence intervals** for at least a subset of configurations (e.g., DeiT-Tiny 50% where the gap is largest, and ViT-Base 12.5% where A-MoD is marginally worse) to establish reliability.
2. **Reframe Contribution 1** to explicitly separate the finetuning finding (A-MoD + MoD outperforms isoFLOP) from the transfer finding (MoD lags behind isoFLOP; A-MoD improves convergence but not absolute accuracy). The paper's own Section 4.3 already contains this nuance; the contribution list should reflect it.
3. **Verify that attention maps remain semantically meaningful** for ViT-Large (e.g., by reporting the correlation analysis from Figure 7 for ViT-Large, or by measuring attention entropy) to address the known attention collapse concern.
4. **Clarify the isoFLOP baseline recalculation** in the layer ablation (Section 4.5): state explicitly whether the isoFLOP model's layer count was adjusted for the new FLOP budget.
