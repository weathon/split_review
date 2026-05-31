Now I have all the information I need to write the consolidated review. Let me produce it.

## Summary

The paper proposes UGaze-Geo, a weakly-supervised 3D gaze estimation framework that incorporates three geometry-guided constraints (iris re-projection correspondence, eyelid/eyeball radius regularization, and head-pose rotation consistency) and models eyeball rotation probabilistically to produce uncertainty-aware gaze estimates. The method disentangles head pose and eyeball movement, uses anatomical priors to supervise without gaze labels, and evaluates across within-dataset and four cross-dataset protocols, reporting SOTA results.

## Strengths

- **Gaze-label-free geometric constraints enable data-efficient training (verifiable).** Sections 3.1–3.2 define three constraints (iris re-projection, eyelid radius, rotation consistency) that require no gaze labels. The prose in Section 4.1 states that with only 50% of Gaze360 labels, Gaze-Geo still outperforms the fully-supervised Gaze360 (Kellnhofer et al., 2019) on the Gaze360 test set. This directly supports the weak-supervision claim.

- **Novel rotation consistency constraint leverages head-eye anatomy.** Eq. 8–9 formalize a constraint enforcing constant eyeball rotation and center across head-pose-augmented images. The text in Section 4.4 reports that combining all three constraints yields error reductions of 9.2%, 15.7%, 14.9%, and 27.8% across within- and cross-data tasks compared to the baseline, with the rotation consistency constraint individually outperforming the eye-anatomy constraints.

- **Probabilistic modeling of eyeball rotation improves cross-dataset accuracy.** Section 3.3 replaces deterministic eyeball rotation with a predicted Gaussian distribution, rewriting losses via sampling and KL-divergence. The prose in Section 4.4 reports that the uncertainty-aware model (UGaze-Geo) improves over the deterministic Gaze-Geo on cross-dataset tasks (e.g., from 6.98° to 6.87° on one task, and from text-garbled numbers on another).

- **Comprehensive evaluation across four cross-dataset protocols.** Section 4.3 reports results on four tasks (D_G→D_M, D_G→D_D, D_E→D_M, D_E→D_D) with three SOTA results: 2.26%, 4.87%, and 3.24% improvements over prior methods. This provides broad evidence of generalization.

- **Ablation isolates each constraint's contribution.** Table 4 (discussed in Section 4.4) incrementally adds constraints to the baseline, reporting specific error reductions at each step (e.g., 4.40°→4.11° for Geo-1,2 on one task, and further improvements with Geo-3). This allows attribution of each component.

- **Anatomically principled constraints are dataset-independent by design.** Section 3.1 models the eyeball with two learnable parameters (eyeball radius, iris radius) and derives constraints from general human anatomy (eyelid landmarks lying on eyeball surface, iris alignment after projection). These are not tied to any specific dataset.

## Weaknesses

### Fatal
None.

### Major

- **Uncertainty quantification is claimed but never validated.** The paper lists uncertainty quantification as a contribution (Section 1: "Our model can also quantify the predicted gaze uncertainty"), formally defines it (Eq. 13–14), and devotes a subsection to it (Section 4.5 "Uncertainty Validation"). However, Section 4.5 consists of a single sentence describing *how* uncertainty is computed — there is no quantitative evaluation whatsoever: no calibration curve, no error–uncertainty correlation analysis, no comparison of uncertainty against a deterministic baseline, no ablation showing whether predicted uncertainty correlates with actual error. This directly invalidates the uncertainty-awareness claim. The reader cannot assess whether the predicted uncertainty is meaningful or just a byproduct of the sampling procedure.

### Minor

- **Ablation numbers for the uncertainty-aware model over the deterministic model are partially garbled in the text.** In Section 4.4, the comparison "improving the baseline+Geo-1,2,3 model from (7.57 °)→ 33°)" contains a clear garbled entry ("33°") that appears to be a parsing artifact. While the prose context supports the claim that UGaze-Geo improves over Gaze-Geo on cross-dataset tasks, the exact improvement margins on this particular task cannot be read reliably.

- **Pre-trained iris detector details are deferred.** The paper uses a pre-trained iris detector (mentioned in Section 3.2, Constraint 1) that outputs a 2D Gaussian distribution per landmark, but the main text does not specify what detector is used, how it was trained, or on what data. A brief characterization would help assess the method's dependence on this upstream component. (The authors reference Section B, which was likely in the appendix but is unavailable here.)

### Trivial
None.

## Nice-to-Haves

- The paper could optionally include confidence intervals or variance estimates for the reported gaze angular errors to better quantify result reliability.
- A brief analysis of failure cases (e.g., large head rotations, occluded eyes) would enrich the experimental section.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Criticism that Tables 1–4 are missing and evidence is insufficient.** The tables are embedded as images in the original PDF and appear as image placeholders in the text extraction. This is a parser artifact, not an author error. The prose text provides substantial numerical results (17.7% improvement, 5.4%/6.6% error reductions, 2.26%/4.87%/3.24% cross-dataset improvements, specific ablation progressions like 4.40°→4.11°). Removed per formatting-artifact rule.

- **Criticism about missing training hyperparameters (λ1–λ5, learning rate, optimizer).** The paper references appendix Section B for implementation details. Per the parser-artifact and missing-appendix rules, these details existed in the original submission but were stripped. Removed.

- **Criticism that the paper cannot be accepted because foundational evidence is missing.** This follows from the table-criticism above, which is a parser artifact. While the uncertainty validation gap is real and addressed separately, the core experimental results for gaze accuracy are present in the prose. Removed as derivative of the removed table criticism.

- **Strength about "8.86° on the full test set" from Table 1.** This specific number cannot be verified from the prose text (which gives only qualitative descriptions of Table 1). Removed because it references unverifiable content from the image table.

- **Strength about "13.7% improvement" and "8.90°→7.68°" from Table 4.** The text reports 8.90°→8.20° for Geo-1,2 on one cross-data task, not 8.90°→7.68°. The 7.68° number may be from the image table but cannot be verified from the prose. Removed.

- **Strength about "3.81° vs 3.85° on MPIIFaceGaze" from Table 2.** The prose reports "5.4% and 6.6% of reduced gaze error by Gaze-Geo and UGaze-Geo" but does not give the specific absolute numbers 3.81° and 3.85°. Removed as unverifiable from the text.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

- **Add a quantitative uncertainty evaluation.** The most critical gap is Section 4.5. The authors should add at minimum: (1) an error–uncertainty correlation plot (e.g., grouping samples by predicted uncertainty and showing average angular error per bin), (2) a calibration analysis (e.g., expected calibration error), and (3) comparison against a deterministic baseline's empirical error distribution. Without these, the uncertainty-awareness claim is unsubstantiated.

- **Include key training details in the main text.** While implementation details may be in the appendix, adding the λ1–λ5 weighting values and the identity/source of the pre-trained iris detector to the main paper would improve reproducibility assessment.

- **Clean up the garbled text in the ablation prose.** The "7.57°→33°" entry in Section 4.4 appears corrupted and should be corrected with the proper value.

## Score and Decision

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>