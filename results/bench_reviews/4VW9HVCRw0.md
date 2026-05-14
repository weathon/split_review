Now I have a thorough understanding of the paper and calibration anchors. Let me write the final consolidated review.

---

## Summary

This paper introduces the task of **Free-Form HOI Generation** — generating diverse, text-controllable hand-object interactions beyond the grasp-centric paradigm that dominates prior work. The authors contribute (1) **WildO2**, a 4.4k-sample in-the-wild 3D HOI dataset reconstructed from internet videos via a semi-automated pipeline (O2HOI frame pairing, single-image reconstruction, differentiable-rendering camera alignment, and hand-object refinement), (2) **TOUCH**, a three-stage framework with contact-map prediction via CVAEs, a multi-level coarse-to-fine conditioned diffusion model, and cycle-consistency refinement, and (3) comprehensive experiments demonstrating controllable generation of diverse interactions including pushing, pressing, and rotating.

## Strengths

- **Novel task formulation**: The paper identifies a genuine gap — prior HOI generation is grasp-centric and cannot capture the diversity of daily non-grasping interactions. The free-form HOI generation task is well-motivated and timely for AR/VR and robotics. The paper explicitly argues why existing paradigms (force closure, grasp taxonomies) impose restrictive inductive biases (Sec. 1).

- **Substantial dataset contribution**: WildO2 provides 4.4k unique interactions across 92 intents and 610 object categories with per-vertex contact maps, fine-grained hand-part segmentation (17 parts), and multi-level language annotations (SSCs + DSCs). The O2HOI frame pairing strategy (dense-matching-based mask transfer avoiding diffusion inpainting) is clever and practically useful. The pipeline design is transparent, modular, and evolvable (Appendix A.2.1 demonstrates upgrading InstantMesh → Hunyuan3D 3.0).

- **Well-ablated method design**: The multi-level coarse-to-fine conditioning is the strongest technical contribution. Removing the multi-level injection structure drops contact IoU from 0.728 to 0.525 (Tab. 2), a dramatic degradation confirming the design's importance. The contact map prediction via CVAEs (Fig. 6) and the cycle-consistency refinement (Tab. 2, "✗ refiner" variant) are each validated through ablation. The text encoder comparison (Qwen vs. CLIP/BERT/MPNet) provides useful engineering insight.

- **Honest failure analysis**: The paper includes a categorized failure case analysis (Appendix A.1.3) identifying pose bias toward grasping, orientation errors, contact mismatch, and penetration artifacts — a level of candor that strengthens credibility.

## Weaknesses

### Fatal

None.

### Major

- **Dataset ground-truth quality is unvalidated against independent 3D measurements**: The entire training and evaluation pipeline uses WildO2's reconstructed meshes as ground truth. The reconstruction relies on single-image InstantMesh for object geometry, single-image hand pose estimation, and heuristic contact-map computation. While the paper reports manual inspection/refinement and 2D consistency checks, no quantitative validation against multi-view stereo, depth sensors, or manual 3D annotations is provided. The paper itself demonstrates (Appendix A.2.2, Fig. 14) that many samples fail reconstruction. For successful samples, systematic geometric or articulation errors could propagate into the learned model and all reported metrics (MPVPE, penetration depth, contact IoU). This is the most substantive limitation: the evaluation metrics measure fidelity to the dataset's own reconstructions, not to true physical interactions. The paper's transparency about pipeline limitations (evolvability, failure modes) mitigates but does not eliminate this concern.

### Minor

- **Baseline breadth is limited**: The paper compares against ContactGen and Text2HOI, which are reasonable representatives for a new task. However, the field has seen recent text-guided grasp methods (e.g., SemGrasp; see Li et al., 2024b in the paper's own references) that, while grasp-focused, could serve as additional reference points after adaptation. The paper's strong performance over two baselines does not fully isolate the contribution of the TOUCH architecture from the contribution of training on the larger, more diverse WildO2 dataset.

- **Semantic controllability claims are partially conflated with dataset annotation structure**: The DSC captions contain explicit hand-part and object-part contact specifications (e.g., "applying [thumb, index pad] to gently lift one end of the [edge] of [card]"). The model is trained and evaluated on these captions. While the ablation removing TDSC (Tab. 2, contact IoU drops from 0.728 to 0.698) shows the model can operate without fine-grained text, the paper does not systematically evaluate whether the model generalizes to user-provided prompts that lack explicit contact-part directives — a more realistic deployment scenario. The "fine-grained semantic controllability" claim is thus partially supported but somewhat overstated.

- **Out-of-domain generalization is purely qualitative**: The Objaverse experiments (Fig. 7) lack quantitative metrics (penetration, contact plausibility, human ratings). Without quantitative evaluation, it is unclear how far the method truly generalizes beyond the WildO2 distribution. The use of LLM-generated captions further confounds the evaluation since these may not match real user inputs.

- **Force-expression analysis conflates adverb with action/object category**: The 22–25% larger contact area for "firm" vs. "gentle" prompts (Fig. 9) is measured across the whole dataset. Without a controlled experiment varying only the force adverb while holding action and object constant, it remains possible that the effect is driven by co-occurring factors (e.g., "firmly" appears more often with grasping actions that naturally have larger contact areas).

### Trivial

- The 500-iteration TTA (Appendix, line 1660) represents a substantial inference-time cost that is not discussed in the main text.
- The VLM-assisted evaluation methodology is underdescribed, making its reliability difficult to assess.

## Nice-to-Haves

- A controlled experiment disentangling the effect of force adverbs (firmly vs. gently) while keeping action and object fixed would strengthen the semantic controllability claims.
- Quantitative evaluation (penetration, contact metrics) on the Objaverse out-of-domain samples would strengthen the generalization claims.
- Reporting inference time including TTA would help practitioners assess practical deployability.

## Removed Points

These points are flagged to be removed — treat them with caution.

- **Harsh Critic Point 1 (Unvalidated Dataset — framed as fatal)**: The critic calls this a "structural" and "decisive" flaw that invalidates all claims and recommends rejection solely on this basis. **Removal justification**: While the dataset quality concern is real and preserved as a Major weakness above, framing it as fatal overstates the issue. The paper's contribution includes the task formulation, method, and dataset pipeline — not just the dataset's geometric precision. The pipeline is transparent, evolvable, and includes manual refinement. Many accepted papers in this space use in-the-wild reconstructions without external multi-view validation. The paper acknowledges limitations. The concern is downgraded from fatal to major.

- **Harsh Critic Point 2 (Missing baselines: SemGrasp, GraspGPT, NL2Contact)**: **Removal justification**: Per the hard rules, I do not have external sources to verify these works' relevance or release status, and the paper already justifies its baseline selection (line 420-421: "As existing methods have not explored fine-grained controlled HOI generation"). The baseline criticism is preserved at a weaker level as a Minor point about breadth, not about specific missing methods.

- **Strength Finder "The problem of moving beyond grasp-centric HOI generation is timely and important"**: **Removal justification**: Generic, no specific evidence beyond stating the problem. This is filler.

- **Strength Finder "The dataset construction effort and the multi-level annotation scheme show significant engineering work"**: **Removal justification**: Generic praise. Moved to the specific strength about WildO2.

- **Harsh Critic "cycle-consistency loss assumes near-bijective point-to-point contact"**: **Removal justification**: The critic speculates that surface-to-surface contact would be penalized but provides no evidence this occurs in practice. The paper's ablation (Tab. 2) shows the refiner improves contact IoU, suggesting the loss is effective. This is theoretical speculation without empirical grounding.

- **Harsh Critic "user study involves only 10 volunteers, insufficient for statistical significance"**: **Removal justification**: This is a one-size-fits-all criticism — 10 users is standard for perceptual studies in this subfield (ContactGen and many HOI papers use similar sample sizes). The paper reports multiple quantitative metrics alongside the user study.

- **Harsh Critic "The ablation of injection layer split (Appendix Tab. 4) shows later-biased fine injection yields comparable results, suggesting SSC may be redundant"**: **Removal justification**: The multi-level design ablation (Table 2, "✗mul.") shows a dramatic 0.525 vs. 0.728 drop, confirming the structure matters. The Appendix layer-split experiment explores a hyperparameter variant, not a refutation of the core design.

- **Harsh Critic formatting/style nitpicks**: All removed per hard rules.

## Novel Insights

The reviews raise a tension worth noting: the paper's DSC captions embed explicit contact-part directives that make the semantic controllability evaluation partially circular — the model is tested on the same distribution of captions it was trained on. This points to a broader methodological challenge for text-conditioned HOI: how to design captions and evaluations that separate "replicating dataset patterns" from "inferring appropriate interactions from high-level intent." The paper's SSC-only ablation partially addresses this but does not fully resolve it. A future benchmark where some captions omit contact-part details would cleanly test this distinction.

## Suggestions

- The authors should consider a held-out validation of reconstruction quality for at least a small subset of WildO2, e.g., comparing to photogrammetry or manual annotation, to bound the expected error.
- Adding a quantitative evaluation (penetration, contact plausibility) for the Objaverse out-of-domain samples would substantially strengthen the generalization claim.
- A controlled experiment on force expression that fixes action+object and varies only the adverb would cleanly isolate the effect.

## Score and Decision

**Anchor comparison:**

| Path | Avg Score | Decision | Comparison to TOUCH |
|------|-----------|----------|---------------------|
| SIGHT (ff3gboFkss) | 3.00 | Reject | Much weaker: unclear motivation, insufficient metrics, no in-the-wild data. TOUCH is clearly stronger. |
| HOIDiNi (mHgaCF2qI5) | 3.60 | Withdrawn/Reject | Weaker: methodological gaps, poor presentation of core technique. TOUCH has clearer ablations. |
| HOI-PAGE (qZhk7prB7v) | 4.50 | Reject | Comparable task ambition but less rigorous evaluation; hand poses appear averaged. TOUCH has better quantitative results. |
| CLUTCH (W7YRskO47j) | 5.00 | Accept (Poster) | Similar: in-the-wild dataset + method. TOUCH has more novel task formulation and stronger ablations. Slightly above. |
| UniHand (upUl6hMYwy) | 5.33 | Accept (Poster) | Comparable: strong technical design with computational cost concerns. TOUCH is at similar level. |
| SynHLMA (EzJowEZ1UJ) | 5.50 | Reject | Similar domain; limited novelty was a key rejection factor. TOUCH has a more clearly novel task. |
| UniHM (cVX3VqO8BO) | 5.50 | Accept (Poster) | Comparable: dataset + language-guided HOI. TOUCH is at a similar contribution level. |

TOUCH sits between CLUTCH (5.0) and UniHM/UniHand (5.33–5.50). The novel task formulation and well-ablated method place it above CLUTCH, but the dataset ground-truth validation gap and limited baseline breadth pull it below the 5.5-tier papers. A score of **5.0** reflects a solid paper with real contributions and addressable weaknesses — suitable for poster acceptance.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>