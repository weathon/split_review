Now I have enough understanding of the paper. Let me do calibration search.Based on my analysis, I have enough to position the paper. The round-1 bracket was 3.5-7.5; round-2 narrowed it to 5-6.5. TOUCH is comparable in topic to HOI-Diff (5.25, reject) and DICE (6.0, accept). It is stronger than HOI-Diff (new task formulation, new dataset, more thorough ablations) but has comparable methodological concerns to those reject-level papers (eval circularity, baseline-input asymmetry, "large-scale" overclaim). Let me write the final review.

## Summary
The paper introduces **Free-Form HOI Generation**, extending hand-object interaction synthesis beyond grasp-centric scenarios. It contributes **WildO2**, a 4,414-sample 3D HOI dataset reconstructed from Something-Something-V2 clips via a pipeline that combines image-to-3D object reconstruction, single-image hand reconstruction, camera alignment via differentiable rendering, and contact-zone ICP refinement. It also proposes **TOUCH**, a three-stage framework: dual CVAEs for hand/object contact prediction, a multi-level conditioned diffusion model that injects coarse (SSC) and fine (DSC) text plus geometry hierarchically across Transformer blocks, and a physical refiner with a self-supervised cycle-consistency loss.

## Strengths
- **New task and dataset for non-grasping HOI** (Sec. 3, Fig. 3): WildO2 contains 4.4k unique interactions across 92 intents and 610 object categories, including non-grasping motions (pushing, poking, rotating, tipping). The diversity along intents and object categories is genuinely novel relative to lab-collected HOI datasets that are dominated by stable grasps.
- **Quantitative gains across all metrics in Table 1**: P-IoU 0.776 vs. 0.620/0.711, MPVPE 2.97 vs. 5.46/4.69, and P-FID 4.13 vs. 6.08/15.72 against ContactGen and Text2HOI.
- **Cycle-consistency refinement is well-motivated and shows clear effect** (Sec. 4.3, Eq. 7): the bidirectional Φ/Ψ mapping is a principled regularizer for hand–object contact, and Table 2 confirms its impact (P-IoU 0.728 → 0.513 without the refiner). The paper also correctly notes that PD/PV alone are misleading without contact, evidenced by the deceptively low PV of the "✗ refiner" variant (PV 2.98) — a nuanced caveat that distinguishes free-form from grasp-only evaluation.
- **O2HOI frame pairing for occlusion-aware object reconstruction** (Sec. 3.1): instead of relying on diffusion-based inpainting of occluded objects (which introduces geometric inconsistencies), the authors transfer SAM2 segmentation from an object-only frame to the interaction frame via dense matching. This is a sensible scalability mechanism.
- **Force-related semantic association is quantified, not just claimed** (Sec. 5.4.3, Fig. 9): the 22–25% larger contact area for "firm/tight" vs. "gentle" is reported with both qualitative and aggregate statistics.

## Weaknesses

### Fatal
None.

### Major

- **Evaluation reference is the same pipeline that produced the training data, with no external benchmark check** (Sec. 3.2, Sec. 5.1). The "ground truth" used to compute every quantitative metric in Table 1 — P-IoU, P-F1, MPVPE, PD, PV, P-FID — comes from the WildO2 reconstruction pipeline, which itself optimizes contact and physical losses (Eq. 2, including L_contact, L_pene, L_anatomy). TOUCH's refiner imposes structurally similar losses. The paper performs final manual inspection at 4,414 samples, but never quantifies 3D fidelity of WildO2 reconstructions against any independent reference (e.g., GRAB/HO3D/HOI4D/ARCTIC subset). The Objaverse out-of-domain results (Fig. 7) are qualitative only. The risk that the model partly fits reconstruction artifacts rather than real-world HOI is not disambiguated — and this matters because the central claim is "natural, physically reasonable" generation. Even a small held-out benchmark with coarse contact/penetration metrics would convert "we match our own reconstructor" into "we generalize to independently captured HOI."

- **Baselines receive a strictly poorer input than TOUCH, conflating architecture with input richness** (Sec. 5.2). The paper explicitly states ContactGen is given "coarse hand part labels" and Text2HOI is "guided by coarse text conditions," while TOUCH consumes both SSCs and DSCs. Since the multi-level coarse-to-fine conditioning is the paper's stated methodological contribution, a controlled comparison — feeding both DSC and SSC through Text2HOI's text encoder, or stripping TOUCH to coarse text only — is necessary to attribute Table 1's gains to the architecture rather than to the extra fine-grained text the baselines lack. The current asymmetry favors TOUCH and obscures what is actually being measured.

### Minor

- **The ablations partly redistribute the story**: Table 2 shows P-IoU drops from 0.728 to 0.513 when the refiner is removed and to 0.525 when the multi-level structure is removed, while removing DSC or SSC individually only drops it to ~0.70. Both the refiner and the multi-level injection are similarly large contributors; the paper's framing emphasizes the multi-level coarse-to-fine semantic control as the primary contribution, but the refiner is at least as load-bearing. This doesn't invalidate the result, but the narrative would be more honest if the refiner were treated as a first-class contribution rather than a half-page module.
- **"Large-scale" is an overclaim for 4,414 samples** (Abstract, Sec. 1). Established HOI datasets (GRAB, ARCTIC, HOI4D, OakInk) are substantially larger. The genuine and defensible novelty is *diversity* (intents, object categories, non-grasping motions), and the paper invites unflattering comparisons by leading with "large-scale" instead.
- **Cycle-consistency mappings Φ, Ψ are described only conceptually** (Sec. 4.3). Whether they are nearest-neighbor, learned, or differentiable surrogates is not specified in the main text, and nearest-neighbor mappings can collapse trivially when contact regions are large or symmetric. An ablation against a non-cycle variant ("✗ L_cyc." in Table 2 shows P-IoU 0.702) does confirm the loss helps, but the mapping details would matter for replication.
- **Split-point i = 4 for coarse-to-fine injection is asserted, not ablated** (Sec. 4.2, Eqs. 4–5). The "✗ mul." row only tests removing the schedule entirely. Comparing i ∈ {2, 4, 6} or uniform injection would substantiate the architectural choice rather than relying on a single design point.
- **VLM-assisted evaluation likely uses a related VLM to the one used for DSC annotation** (Sec. 3.3, Sec. 5.1). The paper uses Qwen-VL for DSC annotation; if the VLM evaluator is from the same family, it scores its own descriptive priors. The PS perceptual score draws on 10 users with no inter-rater agreement reported. P-FID values cluster in a narrow range (4.13, 4.84, 5.41) and ablation diversity metrics differ by less than 0.1; without seeds or CIs, several ablation differences are within plausible noise.
- **Hand and object contact CVAEs are independent** (Sec. 4.1). There is no explicit consistency constraint that ensures the predicted hand-contact patch and object-contact patch are spatially reachable simultaneously; the downstream diffusion must rediscover this from data. A joint or coupled formulation would more directly support the paper's "contact relationships as constraint" thesis.

### Trivial
- Eq. 4–5 use overlapping global condition sets across stages but the change is small; clearer notation showing which features drop in/out at i = 4 would help readability.

## Nice-to-Haves
- Even a small quantitative out-of-domain evaluation on a subset of HOI4D/ARCTIC non-grasping clips would substantially strengthen the empirical case.
- A symmetric baseline configuration — Text2HOI and ContactGen given DSC inputs through their text encoders — would resolve the architecture-vs-input ambiguity in Table 1.
- Seeds / variance estimates for the ablation table, given how close several numbers are.
- Reframe the contribution to give the refiner equal billing with the multi-level diffusion; this aligns the narrative with the ablation evidence.

## Removed Points
*These points were flagged from the harsh critic but removed or demoted; treat with caution.*

- *Reviewer concern about contact-map thresholds in Sec. 3.3 affecting "leaderboard"*: the thresholding choice does affect the metric, but the same thresholds are applied consistently to all methods, so it is not a fairness issue. Demoted.
- *"4,414 retained samples are accepted as ground truth, but the paper never quantifies their 3D fidelity"* (overlap with the major weakness already retained). Merged into the major eval-circularity weakness.
- *Stronger framing of "fatal" for the eval-on-own-pseudo-GT issue*: the paper does manually inspect and refine the final 4,414 samples (Sec. 3.2), which provides at least a sanity check that the harsh critic ignored. Demoted from fatal to major.
- *Generic strength-finder claims* ("automated three-stage reconstruction pipeline", "first large-scale dataset") — kept the diversity strength, dropped the "large-scale" claim because it is one of the verified weaknesses.

## Novel Insights
The combination of *contact-as-constraint* with *coarse-to-fine semantic conditioning* is a sensible architectural response to non-grasping HOI, and the cycle-consistency loss is a clean self-supervised regularizer for ambiguous hand–object correspondence. The O2HOI frame pairing — using a separate object-only frame to bypass occlusion-aware inpainting — is a useful idea for scaling 3D HOI annotation from internet video. Beyond these, the reviews surface no fundamentally novel observations beyond the paper's own contributions.

## Suggestions
- Add a quantitative out-of-domain evaluation against any independently captured non-grasping HOI source, even with coarse metrics, to disambiguate "matches WildO2 pipeline" from "generates real HOI."
- Re-run ContactGen and Text2HOI under matched text inputs (concatenated DSC+SSC into their text encoders) and report whether TOUCH still wins.
- Specify Φ, Ψ formally in the main text and ablate the cycle-consistency mapping choice.
- Drop "large-scale" framing in favor of "diverse," which the data actually support.
- Reframe contributions so the refiner is presented as a co-equal contribution, matching the ablation magnitudes.

---

## Calibration Trace

**Round 1 anchors retrieved:**
- `RFJGFrMvYj.md` (avg 1.50, weak band) — Text-to-image generation; not directly comparable, much weaker.
- `TJHB4ySVZM.md` (avg 3.40, weak band) — Data extrapolation T2I; weaker scope than TOUCH.
- `kCnLHHtk1y.md` (avg 3.00, weak band) — Chinese ancient buildings T2I; weaker, narrow scope.
- `KWo4w1UXs8.md` (avg 3.00, weak band) — Pose generation with GCN+diffusion; weaker.
- `nTNElfN4O5.md` (avg 5.50, middle band, **read in full**) — IHDiff, 3D interacting hands diffusion. Comparable to TOUCH in being the "first generative model" for a specific 3D hand task, with limited technical novelty critiques and weak baseline comparisons. TOUCH is broader in contribution (dataset + task + method).
- `OWIk5E4lJs.md` (avg 5.20, middle band) — Interactive-action image generation; similar profile, broad disagreement among reviewers.
- `ZYwLfi50GI.md` (avg 5.25, middle band, **read in full**) — HOI-Diff. Closest comparison: text-driven HOI synthesis with diffusion + affordance/contact prediction + refinement. Same general design (decompose into contact + generation + refinement), comparable concerns (lack of recent comparisons, physical plausibility issues), reject.
- `bVBLqKoiJ1.md` (avg 4.00, middle band) — Paint-by-Inpaint; off-topic.
- `u1cQYxRI1H.md` (avg 10.00, strong band) — IC-Light; much stronger contribution.
- `LbEWwJOufy.md` (avg 8.50, strong band) — TANGO; stronger contribution.
- `vaEPihQsAA.md` (avg 7.60, strong band) — CyberHost; stronger contribution.
- `6O3Q6AFUTu.md` (avg 8.00, strong band) — NoiseDiffusion; stronger.

**Round-1 bracket:** TOUCH sits between the middle (5–6) anchors and below the strong band. Plausible range: 5.0–6.5.

**Round 2 anchors retrieved (narrowing):**
- `rfrtFwnF62.md` (avg 6.00, **read in full**) — DICE, hand-face interaction reconstruction (accept). Topical neighbor. Stronger empirical case (real benchmark + in-the-wild eval) than TOUCH's own-pipeline-only eval. TOUCH has broader task novelty but weaker out-of-distribution evidence.
- `1CIUkpoata.md` (avg 6.00) — 6D pose tracking in internet videos; topically adjacent (in-the-wild manipulation).
- `5GgjiRzYp3.md` (avg 5.50) — Intent3D; less directly comparable.
- `OzUNDnpQyd.md` (avg 7.00) — protein conformation; off-topic.
- `Nq7yKYL0Bp.md` (avg 6.33) — protein diffusion; off-topic.
- `qH9nrMNTIW.md` (avg 6.25) — protein-ligand diffusion; off-topic.

**Round-2 narrowing:** The two most topical neighbors are HOI-Diff (5.25, reject — limited evaluation, no proper hand-object handling) and DICE (6.0, accept — first end-to-end method, strong in-the-wild empirical results). TOUCH has stronger task/dataset novelty than HOI-Diff but weaker external evaluation than DICE. The eval-circularity and baseline-asymmetry concerns are real but not fatal; the dataset contribution and method are concrete. The paper lands between HOI-Diff and DICE, closer to the borderline.

**Final score:** 5.5 — borderline reject; the contribution is real but two specific empirical concerns (eval on own pseudo-GT; asymmetric baseline conditioning) prevent the headline claims from being adequately demonstrated as currently presented.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>