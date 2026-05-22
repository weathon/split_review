Good. Now I have enough data to write the review. Let me compile my analysis.

**Calibration summary:**
- Round 1 bracket: 5.0 to 7.5
- Round 2 anchors: HOI-Diff (5.25, Reject), IHDiff (5.50, Reject), DICE (6.00, Accept)
- TOUCH is clearly more substantial than HOI-Diff (better dataset, better method, more thorough evaluation), and comparable to or slightly better than DICE (more comprehensive contributions: new task formulation + new dataset + three-stage method, though with evaluation weaknesses). Final positioning: 6.5.

---

## Summary

This paper introduces "Free-Form HOI Generation," extending hand-object interaction synthesis beyond grasp-centric paradigms to diverse non-grasping actions (pushing, poking, rotating). The authors construct WildO2, a 4,414-sample 3D HOI dataset from Something-Something V2 videos using an automated O2HOI frame-pairing and reconstruction pipeline, and propose TOUCH, a three-stage framework comprising dual-CVAE contact map prediction, multi-level conditioned diffusion with coarse-to-fine text injection, and a physical refinement module with cycle-consistency loss. Experiments demonstrate improvements over ContactGen and Text2HOI across contact accuracy, physical plausibility, diversity, and semantic consistency metrics.

## Strengths

- **Novel task formulation with genuine motivation.** The paper convincingly argues that existing HOI generation methods are locked into grasp-centric paradigms even when conditioned on detailed language (§1). Defining Free-Form HOI as a distinct task with appropriate evaluation axes is a meaningful contribution that opens a research direction.

- **Clever dataset construction pipeline with practical engineering.** The O2HOI frame-pairing strategy (§3.1) — finding an unoccluded object reference frame paired with an interaction frame, then transferring masks via dense matching — is a well-motivated solution to the hand-occlusion problem that avoids both geometric inconsistencies from diffusion-based inpainting and the cost of manual annotation. The pipeline achieves 55% success rate, yielding 4,414 samples with multi-level annotations.

- **Contact map prediction as a critical spatial prior.** The dual-CVAE design generating separate hand and object contact maps (§4.1) directly addresses the core argument that grasp-centric priors are insufficient. The ablation in Table 2 convincingly validates this: removing contact maps ("✗ hoc.") drops P-IoU from 0.728 to 0.492, the largest single-component impact.

- **Coarse-to-fine conditional injection with strong ablation support.** The hierarchical design injecting global features in early Transformer blocks and local contact features in later blocks (§4.2, Eqs. 4–5) is justified by clear reasoning and validated by ablation: removing multi-level structure ("✗ mul.") drops P-IoU from 0.728 to 0.525.

- **Insightful observation about misleading penetration metrics.** The paper correctly identifies (§5.3) that low penetration metrics can be deceptive when hands drift away from objects entirely, as shown by the "✗ refiner" variant. This is a valuable methodological observation for the HOI generation community.

- **Fine-grained 17-part hand segmentation.** The segmentation scheme (§3.3) including dorsal, palmar, knuckle, and nail regions supports non-grasping contact specificity beyond typical coarse finger-level divisions, directly enabling the paper's core claims about non-grasping interactions.

## Weaknesses

### Fatal
None

### Major

- **Marginal diversity gains without statistical support.** Table 1 shows diversity improvements from ContactGen/Text2HOI to TOUCH: entropy 2.85 → 2.93 (~3%), cluster size 5.20/4.93 → 5.40 (~4%). For a paper whose central thesis is that existing methods lack diversity and TOUCH recovers it, these are small absolute gaps with no variance estimates, confidence intervals, or statistical significance tests reported anywhere. The largest diversity-adjacent gap is actually on Text2HOI's cluster size (4.93 → 5.40), but this difference is still modest. The paper needs either larger demonstrated gaps or statistical evidence that the current gaps are reliable.

- **Opaque semantic consistency evaluation methodology.** The VLM evaluation and Perceptual Score (PS) show the largest gaps between TOUCH and baselines (PS: 8.8 vs 7.5; VLM: 7.1 vs 6.5), making them the most discriminating metrics for the paper's central claim about semantic controllability. Yet the methodology is largely unspecified: how is the VLM score computed (what prompts, what rubrics)? The user study involves only 10 participants with no details on the evaluation protocol (what raters were shown, what scale was used, what instructions were given, inter-rater agreement). These metrics are doing heavy lifting in the paper's argument but cannot be independently assessed for validity.

- **Only two baselines, both adapted from other tasks.** ContactGen was designed for grasp generation with coarse hand part labels, and Text2HOI was designed for temporal human-object interaction with its temporal axis removed. While the authors acknowledge this and add post-processing optimization to improve fairness, the architectural intent gap means outperforming these baselines primarily shows the baselines are poorly suited to this task, not that TOUCH's approach is optimal. The comparison would be substantially strengthened by at least one more recent or more relevant baseline.

### Minor

- **"In-the-wild" framing overstates data provenance.** WildO2 is built from Something-Something V2 (Goyal et al., 2017), a crowdsourced dataset where workers perform prescribed actions in controlled settings (e.g., "picking [something] up"). The paper describes this as "the first large-scale, in-the-wild 3D HOI dataset" built from "internet videos." While SSv2 does involve real objects and non-lab environments, it is meaningfully different from truly in-the-wild video sources like Ego4D or YouTube. The characterization should be more precise.

- **Out-of-domain generalization supported by only 4 examples.** Figure 7 shows 4 Objaverse CAD objects with generated interactions, including verbs outside the primary annotated intents. While visually interesting, this is too thin to support a generalization claim. At minimum, some quantitative metric on a held-out object set would strengthen this considerably.

- **Static snapshot limitation is acknowledged but not deeply discussed in the context of claims.** The paper acknowledges this in the Conclusion (§6), but many interaction verbs in WildO2 (e.g., "push," "rotate," "tip over") are inherently temporal and dynamic. Generating a single static pose for "tip water bottle over" captures at most one frame of a multi-step process. The paper could more carefully scope its claims about the range of interactions it can represent.

- **Binary contact maps may lose useful information.** The CVAE contact maps are binary ({0,1}), as stated in §4.1. For diverse interactions like pushing or rotating, the sharpness of a binary representation may discard information about contact pressure or confidence that could be useful for distinguishing subtle interaction variations. This is a reasonable design choice but could benefit from brief justification.

### Trivial

None

## Nice-to-Haves

- Report per-intent or per-interaction-type breakdowns of metrics rather than only aggregate statistics. The 92 intents likely have very different modeling quality; a per-category analysis would be far more informative.
- Evaluate contact map prediction accuracy (precision, recall, F1) of the CVAE against ground-truth contact maps in isolation, to clarify how much downstream quality comes from contact prediction vs. the diffusion model.
- Provide quantitative out-of-domain evaluation (e.g., contact coverage, penetration rate) on a held-out Objaverse set.
- Add failure case analysis: when does the method fail, and are failures concentrated in certain interaction types, object shapes, or text descriptions?
- Report what fraction of VLM-generated DSCs required manual correction and how consistency was assessed during verification.

## Removed Points

These points are flagged to be removed, treat them with caution.

- **"Dataset averages ~48 samples per intent, many intent-object combinations have very few examples"** — While valid, this is acknowledged by the paper's use of resampling for class imbalance. The concern about overfitting is speculative without evidence.
- **"Pipeline's 55% success rate limits practical scalability"** — The paper explicitly reports this in Figure 3(a) and discusses the failure modes (31% hand pose estimation failure). The rate is stated transparently; criticizing transparency seems circular.
- **"The paper does not discuss the limitations of relying on SSv2's action vocabulary"** — This is a scope creep concern. SSv2 is a reasonable starting point and the paper acknowledges limitations in the Conclusion.
- **"Comparison should include at least one more recent baseline or oracle"** — This was kept as a major weakness but only two baselines is acknowledged; the issue is really about the gap between baselines and the proposed task, not author negligence.
- **Harsh critic's generic concern about "binary contact maps losing information"** — Kept as minor since the paper does use binary maps, but this is a design choice, not a flaw.
- **Strength finder's claim about "strong out-of-domain generalization evidence" (Figure 7)** — Demoted to minor weakness given only 4 examples shown, as verified.
- **Strength finder's claim about "comprehensive evaluation"** — While the 4-axis evaluation framework is well-designed, the implementation of the semantic consistency axis is insufficiently specified. Conflicts with verified weakness about opaque VLM/user study methodology; the weakness wins.

## Novel Insights

The paper's most genuinely novel observation is that penetration depth and volume metrics can be misleading for free-form HOI evaluation when hands drift away from objects without making contact — the "✗ refiner" ablation demonstrating deceptively low penetration scores due to non-contact (§5.3, Table 2) is a methodological insight that the HOI community should take seriously. The cycle-consistency loss (Eq. 7) enforcing bidirectional hand↔object contact mapping invertibility is also a creative self-supervised regularization approach. The semantic nuance observation (§5.4.3, Figure 9) — that the model learns to associate "firm/gentle" language with 22-25% contact area differences without explicit force modeling — is a concrete emergent property worth noting, though it would benefit from more rigorous quantification.

## Suggestions

1. **Strengthen diversity evaluation.** Run multiple seeds and report standard deviations for entropy and cluster size. Consider reporting per-intent diversity breakdowns to show which interaction types benefit most.
2. **Specify VLM evaluation methodology.** Report the prompts, scoring rubrics, and model used for the VLM-assisted evaluation. For the user study, report the number of participants, their expertise, the rating scale, what they were shown, and inter-rater agreement (e.g., Cohen's κ or Krippendorff's α).
3. **Add a third baseline.** Even a simple oracle (e.g., nearest-neighbor retrieval from the training set) or a more recent method would provide better context.
4. **Quantify contact map prediction quality.** Report precision, recall, and F1 of predicted vs. ground-truth contact maps on the test set.
5. **Add quantitative out-of-domain evaluation.** Compute contact, penetration, or diversity metrics on a held-out Objaverse set with LLM-generated captions.

## Scoring and Anchor Analysis

**All retrieved anchors:**

| Round | Anchor ID | Paper | Avg Score | Comparison |
|-------|-----------|-------|-----------|------------|
| 1 | RFJGFrMvYj | TCIG | 1.50 | Much weaker; generic image generation |
| 1 | KWo4w1UXs8 | PoseDiffusion/GUNet | 3.00 | Weaker; pose skeleton generation only |
| 1 | kCnLHHtk1y | Chinese Ancient Buildings | 3.00 | Weaker; narrow domain application |
| 1 | 9GNTtaIZh6 | Mask-Guided Video Gen | 3.00 | Weaker; video generation |
| 1 | nTNElfN4O5 | IHDiff | 5.50 | Less comprehensive (two-hand only); TOUCH is clearly stronger |
| 1 | ZYwLfi50GI | HOI-Diff | 5.25 | Similar task but weaker dataset, less thorough evaluation; TOUCH substantially better |
| 1 | J4D5WVoc5g | ViTaM-D | 4.50 | Weaker; tactile-based reconstruction |
| 1 | SLDqCpHPuP | Pose Priors from LMs | 5.00 | Different approach; less comprehensive |
| 1 | LbEWwJOufy | TANGO | 8.50 | Stronger; co-speech gesture video, more polished |
| 1 | vaEPihQsAA | CyberHost | 7.60 | Stronger; audio-driven body animation |
| 1 | zMoNrajk2X | CADS | 8.00 | Stronger; diversity in diffusion sampling |
| 1 | 3b9SKkRAKw | LeFusion | 8.00 | Stronger; medical image synthesis |
| 2 | nTNElfN4O5 | IHDiff | 5.50 | TOUCH clearly stronger |
| 2 | rfrtFwnF62 | DICE | 6.00 | Comparable scope; TOUCH has stronger overall contribution |
| 2 | WXXuORQwbQ | Sparse Mask HSI | 5.00 | Weaker; different task |
| 2 | L2kbdthX5M | SignAvatars | 6.25 | Different domain |
| 2 | IZMPWmcS3H | HIFA | 6.67 | Different task (text-to-3D); accepted |
| 2 | ktG8Tun1Cy | CSD | 6.75 | Different task; more focused |
| 2 | LtuRgL03pI | InstructScene | 7.50 | Stronger; more polished evaluation |
| 2 | H2Gxil855b | Atlas Gaussians | 7.00 | Stronger; 3D generation |

**Round 1 bracket:** 5.0 – 7.5
**Round 2 narrowing:** TOUCH is clearly better than HOI-Diff (5.25) and IHDiff (5.50), and comparable to/slightly better than DICE (6.00). TOUCH has a more comprehensive contribution (new task + new dataset + three-stage method + multi-level text conditioning) but weaker evaluation rigor. Positioned above DICE's 6.00 but well below the 7+ papers that have more polished evaluation and broader impact. Final score: **6.5**.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>