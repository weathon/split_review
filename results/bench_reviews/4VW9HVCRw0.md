## Summary
The paper introduces "Free-Form HOI Generation," a task targeting non-grasping hand-object interactions (push, poke, rotate, etc.), and contributes (i) WildO2, a 4.4k-sample in-the-wild 3D HOI dataset built via an automated reconstruction pipeline from Something-Something V2, with 17-part hand segmentation and VLM-generated fine-grained captions, and (ii) TOUCH, a three-stage framework combining dual contact-map CVAEs, a multi-level (coarse-to-fine) conditioned diffusion model, and a cycle-consistency + physical refinement module with test-time adaptation.

## Strengths
- **Novel task framing and dataset contribution.** The free-form HOI scope is a real gap relative to grasp-centric datasets/methods (Sec. 1, Sec. 2.3). WildO2 (Sec. 3) provides 4.4k samples, 92 intents, 610 object categories, dense contact maps, and 17-part hand segmentation that includes dorsal regions — the latter is more granular than typical grasp datasets and well-matched to non-grasp verbs.
- **Engineering value of the O2HOI pairing strategy.** Pairing each interaction frame with an unoccluded object-only frame and transferring SAM2 masks via dense matching (Sec. 3.1) is a sensible alternative to diffusion inpainting, and the three-stage reconstruction pipeline (Sec. 3.2) appears competent.
- **Strong, internally consistent ablations.** Tab. 2 cleanly isolates components: removing the hand/object contact prediction drops P-IoU from 0.728 → 0.492; removing multi-level conditioning drops it to 0.525. The authors honestly flag that "✗ refiner" gets artificially low PD/PV because the hand drifts away — this kind of metric-honesty is commendable.
- **Cycle-consistency formulation.** The bidirectional Φ/Ψ contact mapping loss (Eq. 7) is a clean regularizer for an under-constrained problem.
- **Coarse-to-fine conditioning is shown to matter.** The split injection of SSC/global geometry in early blocks and DSC/local contact features in later blocks (Eqs. 4–5) is non-trivial and supported by ablation.

## Weaknesses

### Fatal
None.

### Major
- **Structural mismatch between "free-form non-grasping verbs" framing and a static-pose output.** The paper's selling point is enabling pushing/poking/rotating/tipping/flipping, but the model outputs a single static hand pose H given an object mesh (Sec. 4, Fig. 4). Verbs like "push," "tip," "roll" are defined by trajectories; a frozen mid-action hand snapshot near an object is hard to distinguish from a hovering hand or a near-grasp without temporal context (see e.g., Fig. 5 row 4 "Push handle" and row 7 "Push with quick precise motion"). The paper acknowledges this only briefly in Sec. 6 Limitations. This isn't an unfair scope-creep complaint — the static-vs-dynamic gap directly undermines how strongly the headline differentiation from grasp-centric work can be claimed.
- **Evaluation is conducted entirely against pseudo-GT produced by the same noisy pipeline used at training time.** The reconstruction pipeline has 55% success (Fig. 3a), and the held-out test split shares dominant error modes (object scale ambiguity, single-image depth, camera alignment artifacts) with training. P-IoU, P-F1, MPVPE, and P-FID are all measured against this pseudo-GT (Sec. 5.1). No cross-dataset quantitative evaluation on real-3D-captured datasets (e.g., GRAB, HOI4D, OakInk, ARCTIC) is reported — only qualitative Objaverse generalization in Fig. 7. Given that the headline metric gap over Text2HOI (P-IoU 0.776 vs 0.711) is modest, this is a substantive evidential gap.
- **Only two baselines, both adapted by the authors.** Tab. 1 compares only ContactGen and Text2HOI (with its temporal axis removed). The paper itself notes both baselines drift on WildO2 (Sec. 5.2) and that they were augmented with optimization-based post-processing to be fair, but the comparison is still between TOUCH's full pipeline (which has a dedicated refiner + TTA) and methods retargeted to a setting they were not designed for. Without a more recent text-conditioned grasp baseline re-trained on WildO2, attribution of the gain to TOUCH's contributions is weaker than it appears.

### Minor
- **Most of the P-IoU lift over Text2HOI comes from refinement + TTA, not the diffusion model itself.** Tab. 2: without TTA, P-IoU = 0.728 vs Text2HOI's 0.711 (with optimization post-processing). The multi-level diffusion's marginal benefit over a baseline that has been similarly augmented is small. Reporting variance/multi-seed runs on Tabs. 1–2 would help calibrate whether the ablation gaps (especially "✗ Lcyc": 0.702) exceed noise.
- **No counterfactual test of the force-semantics finding.** The "22–25% larger contact area for firm vs gentle" (Sec. 5.4.3) could reflect dataset co-occurrence — "firm/tight" captions may correlate with grasps (which intrinsically have larger contact area). A controlled swap that varies only the adverb at test time on the same intent would isolate the conditioning effect.
- **Independent CVAEs for hand and object contact maps.** Bidirectional consistency is enforced post-hoc through the cycle loss (Eq. 7) and refinement, but the two CVAEs are uncoupled at prediction (Sec. 4.1). Starting from inconsistent maps is a design choice that deserves at least an ablation against a jointly modeled alternative.
- **OOD evaluation is qualitative-only.** Sec. 5.4.2 and Fig. 7 show four Objaverse examples; this is suggestive, not evidence of generalization.
- **No per-verb breakdown.** Aggregate metrics could be dominated by grasp-like samples; reporting metrics separately for grasping vs. push/poke/rotate/tip would directly test the paper's core differentiation claim.

### Trivial
- P-FID on only 677 test point clouds is statistically noisy as a distributional metric; PS based on 10 users should be reported with inter-rater agreement.
- The VLM-verification rate for DSCs (Sec. 3.3) is not quantified; since DSCs are the central control signal, the agreement/disagreement rate matters.

## Nice-to-Haves
- A small temporal-sequence variant, even on a subset, would directly address the static-pose limitation.
- Failure-case visualizations on non-grasp intents (push, poke, tip) would strengthen credibility more than additional successes.
- Side-by-side comparison between the static generated pose and the corresponding ground-truth video frame for the same verb across multiple verbs.
- A recent text-conditioned grasp baseline (e.g., one re-trained on WildO2) attached to the same refinement module to isolate the contribution of the diffusion design from the refiner.

## Removed Points
*Treat with caution — these are flagged as not credibly supportable as written.*
- *(Harsh critic) "Manual verification rate / who verified DSCs not reported."* Reproducibility nitpick about annotation logistics; rule on appendix-deferred reproducibility details applies.
- *(Harsh critic) Requests for SemGrasp / GraspXL / GrabAffordance retrained on WildO2.* The harsh critic frames this as a fairness fix; while a stronger baseline would be nice, demanding specific named methods veers into missing-related-work territory and the paper already adapts two representative baselines from the two main paradigms (CVAE-based, text-conditioned diffusion). Kept only as a Nice-to-Have.
- *(Strength finder) "Strong out-of-domain generalization" framed as a major strength.* Sec. 5.4.2 is qualitative-only with four examples; weakened — not a substantiated strength.
- *(Strength finder) "Comprehensive multi-faceted evaluation" as a strength.* Conflicts with the verified major weakness about pseudo-GT evaluation; removed.

## Novel Insights
None beyond the paper's own contributions. The O2HOI pairing strategy and 17-part hand segmentation including dorsal regions are tangible engineering ideas worth highlighting, but the reviews do not surface insights beyond what the paper itself argues.

## Suggestions
- Honestly reframe the contribution as "diverse, fine-grained static HOI snapshot generation including non-grasp configurations," and reserve "free-form temporal interaction" for a follow-up, OR add even a minimal temporal extension.
- Add cross-dataset quantitative evaluation on at least one real-captured 3D HOI benchmark (or report contact metrics on a manually-curated clean subset of WildO2 separately from the auto-reconstructed bulk).
- Report multi-seed variance for Tabs. 1–2; some ablation gaps are within plausible noise without it.
- Per-verb metric breakdown to test whether the model actually wins on the non-grasp verbs that motivate the paper, not just on grasp-like samples.
- Counterfactual semantic-controllability test: hold object + intent fixed; vary only contact-part description or only "firm"/"gentle"; report quantitative change in pose/contact area.

## Evaluation Axes
- **Originality:** Genuinely novel task framing (free-form non-grasping HOI) and dataset; method components are largely recombinations of standard pieces (CVAE contact + DDPM + cycle loss + TTA).
- **Importance of research question:** High — the field is grasp-centric.
- **Whether claims are well supported:** Partially. The dataset/pipeline claim is supported; the "generation of free-form interactions including push/poke/rotate" claim is supported visually but undercut by the static-pose output and pseudo-GT-only evaluation.
- **Soundness of experiments:** Mixed. Ablations are well-designed; baselines are thin and evaluation data is self-produced.
- **Clarity of writing:** Generally clear; method section is well-structured.
- **Value to community:** Moderate to high — WildO2 and the pipeline are likely to be reused.

## Score and Decision

Anchors retrieved (all in the calibration batch):
- `nTNElfN4O5.md` (IHDiff, avg 5.50, Reject) — diffusion prior for two-hand interactions; like TOUCH, useful generative formulation but limited evaluation; similar tier.
- `ZYwLfi50GI.md` (HOI-Diff, avg 5.25, Reject) — text-driven 3D HOI via diffusion + affordance prediction; closest analogue methodologically; ended up rejected at similar score.
- `OWIk5E4lJs.md` (Interactive-Action Image Gen, avg 5.20, Reject) — text-driven generation with synthetic priors; mixed bag.
- `KfkmwYQXWh.md` (InterDance, avg 5.60, Reject) — new dataset + diffusion generator; similar dataset+method structure, similar score band.
- `Cf8HBieRzL.md` (UniContact, avg 3.50, Reject) — contact synthesis for manipulators, weaker reception; the paper under review is clearly stronger.
- `J4D5WVoc5g.md` (ViTaM-D, avg 4.50, Reject) — visual-tactile HOI reconstruction; similar domain but weaker experimental story; TOUCH is somewhat stronger on dataset contribution.
- `xcHIiZr3DT.md` (Pseudo-Tactile, avg 2.50, Reject) — clearly weaker than the paper under review.
- `WtHKqtHVXo.md` (LLM robot policy code, avg 4.00, Reject) — off-topic-ish; weaker.
- `YOpa6dTrpt.md` (Pedestrian Motion Reconstruction, avg 7.00, Accept) — large-scale dataset + benchmark, accepted; this paper's dataset is smaller (4.4k samples) and its pipeline is more derivative, so it doesn't quite reach this anchor.
- `qrv4wcmmxe.md` (Zero-shot HOI Detection, avg 6.00, Reject) — adjacent domain; cleaner contribution but still rejected.
- `cfuZKjGDW7.md` (TAO-Amodal, avg 6.00, Reject) — benchmark contribution; comparable in nature, higher cleanliness of evaluation.
- `gVWEq7LITG.md` (TF-HOT, avg 3.50, Reject) — weaker than the paper under review.
- `otoggKnn0A.md` (FHA-Kitchens, avg 4.00, Reject) — dataset paper, weaker than this one.
- `WM5G2NWSYC.md`, `ZbOSRZ0JXH.md`, `i28ZjVxl81.md` — off-topic low anchors (<3); paper under review is clearly stronger.

The paper sits very close to HOI-Diff (5.25) and IHDiff (5.50) — same problem space, same diffusion+contact recipe, same pattern of "interesting task + new method + limited evaluation." TOUCH adds a meaningfully novel dataset construction story, which pushes it slightly above those anchors, but the static-pose-vs-verb mismatch and self-evaluated pseudo-GT pull it back. It does not reach the 6+ band of cleaner dataset-benchmark accepts (Pedestrian Motion Reconstruction, 7.00).

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>