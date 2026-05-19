Now I have a clear picture of the paper and the anchor landscape. Let me write the consolidated review.

## Summary

This paper studies OOD generalization under varying *degrees* of distribution shift, arguing that evaluating at only a single or narrow range of shift degrees can produce misleading conclusions about model robustness. Through extensive experiments on synthetic shift tasks (NoisyMNIST, RotatedMNIST, LowLightCIFAR10, NoisyImageNet15) with over 20 DG algorithms and multiple architectures, the paper shows that (1) models appearing robust at a mild shift can collapse at slightly stronger shifts, (2) training on strong shifts does not always guarantee robustness to milder shifts (task-dependent), and (3) CLIP models with linear probing can be surprisingly brittle to downstream distribution shifts.

## Strengths

1. **Important and under-explored research question.** The paper identifies a genuine gap in OOD evaluation: existing benchmarks largely fix the degree of each distribution shift, and the paper systematically shows why this matters. The observation that a model's relative ranking can flip between adjacent shift degrees (Table 1, e.g., VREx from best at D₄ to worst at D₆ with 73.1% relative drop) is a concrete cautionary result for the community.

2. **Extensive empirical coverage.** The paper evaluates over 20 DG algorithms (ERM, VREx, IRM, GroupDRO, Mixup, CAD, etc.) across multiple architectures (4-layer CNN, ResNet-50, EfficientNet-b0, ViT-B/32) and four synthetic shift types (noise, rotation, low-light, resolution). The consistent brittleness observed across these dimensions strengthens the core claim.

3. **Task-dependent asymmetry finding.** Section 4.3 shows that training on strong shifts generalizes well to milder shifts for NoisyMNIST but *harms* performance on mild shifts for RotatedMNIST and the highest-degree LowLightCIFAR10 (Fig. 4). This reveals that the relationship between training shift degree and test robustness is not monotonic and depends on the nature of the shift — a nuance lost in fixed-degree evaluations.

## Weaknesses

### Fatal
None.

### Major

1. **Model selection uses test-domain performance.** The paper selects the "top-3 models" among 20 variants per algorithm by *worst-domain performance* (line 143, caption of Fig. 2; line 186). This criterion uses test-domain data (the worst domain among D₂–D₁₀). The paper never mentions a held-out validation set, and no train/validation/test split is described. Since hyperparameter/model selection on test data can inflate reported performance and distort relative rankings, the central brittleness results (Table 1, Fig. 2) may partly reflect selection artifacts. The paper needs to specify the exact selection protocol and ideally validate the core claims under a proper held-out split.

2. **DG algorithms evaluated on only two source domains.** All DG methods (ERM, VREx, IRM, GroupDRO, etc.) are trained on only two domains: clean (D₀) + one mild shift (D₁) — lines 158–159. Many DG algorithms (especially VREx, IRM, GroupDRO) are designed for and typically evaluated with more source domains (³3) to learn invariant representations. The poor performance of some methods under this constrained setup is not surprising and does not demonstrate inherent brittleness of those algorithms. The paper should either include a condition with more source domains or clearly frame this limitation.

3. **CLIP experiments use only linear probing — the strongest claim is about the wrong target.** Section 5 finds that CLIP with linear probing is "surprisingly much more brittle" to noise than scratch models. However, linear probing is a weak adaptation method that does not modify features. The paper's central CLIP claim (lines 51–53, 291) conflates "CLIP is brittle" with "CLIP *with linear probing on clean data only* is brittle." The paper has a `\comment{...}` block (lines 310–313) noting that "fine-tuning significantly outperforms training from scratch and linear probing on NoisyMNIST" but does not include these experiments in the visible paper. Without fine-tuning as a control condition — the natural baseline for leveraging pre-trained features — the claim about CLIP's brittleness is overblown relative to the evidence presented. The appropriate claim would be "linear probing on clean data is insufficient to transfer CLIP's robustness to unseen shifts," which is less surprising and better supported by existing literature.

### Minor

1. **Results confined to synthetic shifts.** All experiments use controlled synthetic corruptions (Gaussian noise, rotation, brightness+shot noise, downsampling). The paper claims (line 103) that conclusions "also hold for more general problems" but provides no evidence from realistic distribution shifts (e.g., WILDS, natural domain shifts). While synthetic shifts are principled for controlled analysis, the generality claim is unsubstantiated.

2. **GradCAM analysis is anecdotal.** Figure 3 shows one example each for ERM and CAD. The paper states that "ERM relies on local features while CAD uses global structures" (lines 211–213) but provides no quantitative metric (e.g., center-of-mass of attention, locality score). This analysis is illustrative rather than rigorous.

3. **No analysis of the most interesting finding.** Section 4.3 documents a striking task-dependent asymmetry: training on strong rotations harms mild-shift performance, but strong noise does not. The paper does not analyze *why* this happens — e.g., measuring feature similarity across domains, checking whether rotation preserves local features while noise destroys them. This is the paper's most novel result and deserves deeper investigation.

4. **Statistical significance not assessed.** Tables 1–2 report means and standard deviations, but the paper does not test whether differences between algorithms at a given degree (e.g., Mixup vs. VREx at D₅) are reliable. Given large stds, many observed rankings may not be statistically significant.

5. **No quantification of what each shift degree means.** The paper defines degrees as natural number indices but never provides an interpretable calibration (e.g., pixel SNR for NoisyMNIST D₄). Without this, the claim that "slightly stronger" shifts cause large drops is relative to an arbitrary scale.

### Trivial
- Figure 1 is labeled as "a typical situation" observed in the paper but its curves are stylized rather than data-backed, which could mislead readers into thinking they directly summarize experimental results.

## Nice-to-Haves

- Perform model selection using a proper validation split (e.g., held-out from training domains) and verify that the brittleness pattern persists.
- Include at least one multi-degree evaluation on a real-world shift benchmark (e.g., varying weather for driving, varying difficulty for ImageNet-v2).
- Add fine-tuning as a control in the CLIP experiments to distinguish "CLIP is brittle" from "linear probing is insufficient."
- Analyze the task-dependent reversal in Section 4.3 more deeply (e.g., feature similarity measurements, probing intermediate layers).
- Include conditions with more source domains (e.g., 4–5 shift degrees) for the DG algorithm comparisons.

## Removed Points
- **Harsh critic's claim about Figure 1**: "The paper never shows that two models with the same one-point evaluation can have the drastically different curves sketched in the figure." — The paper explicitly states "Consider the situation (that we observed in this work) illustrated in Figure 1" (line 31). The figure is a schematic illustration of the phenomenon, not a claim of exact curve shapes. The paper's results do show different curve shapes across models. This criticism is overly literal.
- **Claim about missing related work on per-severity results**: The harsh critic says Hendrycks & Dietterich 2019 "report per-severity results in their Table 5." The paper currently acknowledges this work by noting only aggregate performance is examined. This level of nuance about a single prior table is too narrow for a review.
- **Criticism about CLIP figure notation (RI_d, CLIP_d being confusing)**: Minor presentation point that the authors can clarify.
- **Criticism about three runs being insufficient**: This is a soft methodological expectation; many empirical papers use 3 runs, and the paper reports standard deviations.
- **Criticism about no code/data release commitment**: Not a standard requirement for evaluation; code release can happen post-acceptance.

## Novel Insights
None beyond the paper's own contributions. The key observation — that model robustness can break sharply between adjacent shift degrees — is the paper's own finding. The reviews do not surface a novel synthesis beyond what the paper provides.

## Suggestions

1. **Validate the core brittleness result under a proper train/validation/test protocol** without using test-domain performance for model selection. This is the single most important revision.
2. **Discuss the two-domain limitation for DG algorithms** explicitly and ideally add one condition with more source domains.
3. **Replace or substantially qualify the CLIP claim**: either run fine-tuning experiments and report them, or reframe the claim to "linear probing on clean data is insufficient to transfer robustness" throughout.
4. **Add analysis of the task-dependent reversal** (Section 4.3): measure representational similarity across degrees for noise vs. rotation to explain why the asymmetry occurs.
5. **Provide an interpretable metric for each shift degree** (e.g., pixel SNR, fraction of pixels corrupted, effective rotation angle) to calibrate reader intuition.
6. **Add a real-world shift experiment** or substantially soften generality claims in the abstract and conclusion.

## Score and Decision

**Round 1 bracket:** Based on calibration search, the paper sits between the weak anchor cluster (avg 2.4–3.0: simple/obvious-flaw papers) and the strong anchor cluster (avg 8.0+). Mid-band anchors average 4.5–6.0.

**Round 2 narrowing:** Compared to the mid-band anchors:
- **Robust Onion** (avg 5.00, Reject) — Similar empirical analysis using synthetic shifts. This paper is stronger in conceptual novelty and breadth of algorithms tested, but has similar limitations (synthetic-only, no method contribution).
- **Understanding Subpopulation Shifts** (avg 5.00, Reject) — Has theoretical framing but strong assumptions. This paper is more empirically grounded.
- **The Lie of the Average** (avg 5.60, Accept Poster) — Similar meta-critique of evaluation methodology, with cleaner theory+experiments. This paper has broader experiments but less clean methodology.
- **Diagnosing Generalization Failures** (avg 6.00, Accept Poster) — Novel framework with empirical validation. This paper has less novelty but more breadth.
- **When Shift Happens** (avg 6.00, Accept Poster) — Theory+experiments, accepted. This paper has no theory, is purely empirical.

This paper's core observation is genuinely important and will interest the community, but the methodological concerns (model selection protocol, DG on only 2 domains, CLIP linear probing only) weaken the strength of the conclusions. The paper is stronger than the avg 5.0 rejected anchors but weaker than the avg 6.0 accepted ones.

**Final score: 5.5**

**Decision: Reject** (with encouragement to resubmit after addressing the major weaknesses, particularly the model selection protocol, CLIP experiments, and DG setup)

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>