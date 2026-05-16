I now have all the information needed. Let me produce the consolidated review.

## Summary

This paper investigates the "mirroring hypothesis" — the idea that geometric structure in neural representations mirrors causal structure in the world — by leveraging a digital twin model of macaque V4 neurons (a ResNet50 core with neuron-specific readouts trained on neural responses to natural images). Using two stimulus paradigms (rotated objects and rotating texture classes), the authors show that (1) when latent structure (circular rotation) is preserved in pixel space, it propagates through networks; (2) when structure is absent in pixel space (texture metamers), a trained V4 digital twin nevertheless recovers a circular manifold that enables linear orientation decoding; (3) this representation exhibits near-equivariance; and (4) the aligned manifolds enable cross-condition generalization — a decoder trained on one texture transfers to others. A robust ResNet trained on ImageNet shows similar properties, suggesting the principles may be universal.

## Strengths

- **Demonstrates recovery of latent circular structure from unstructured texture images in a trained neural network model.** The paper shows (Figure 4b–c) that pixel-space texture manifolds lack linear circular structure (mean angular error 0.6 radians), while the trained digital twin recovers a clean circular manifold enabling near-perfect linear decoding (0.12 radians). The untrained network performs worse (0.24 radians), confirming that training, not architecture alone, drives this recovery. The quantitative framing (structure maintained vs. lost in data space) is a useful conceptual contribution that helps distinguish trivial preservation from nontrivial computation.

- **Provides converging evidence from a robust ResNet.** The finding that an ImageNet-trained robust ResNet (layer 3, corresponding to V4) shows similar manifold recovery, linear decodability, and cross-condition generalization (Figure 5d–f) strengthens the paper's claim that these geometric principles may be general properties of trained vision systems, not artifacts of the specific V4 digital twin.

- **Cross-condition generalization experiment is well-designed and shows a striking effect.** The trained digital twin yields off-diagonal circular correlations of 0.83 vs. 0.39 for the untrained network (Figure 5c), demonstrating that training produces manifold alignment that enables zero-shot transfer across texture classes. This is the paper's most compelling piece of evidence and directly supports the functional benefit of the proposed representational geometry.

- **Clear and well-motivated framework.** Section 2's distinction between "structure maintained" and "structure lost" in the data space, and the argument that only the latter constitutes non-trivial computation, is pedagogically valuable and addresses a genuine gap in the neural manifold literature.

## Weaknesses

### Major

- **The spatial replication of neurons is a likely confound that may artificially create the observed structure.** Each of the 1244 V4 tuning curves is replicated 49 times across a 7×7 spatial grid (Section 4.1), yielding 60,956-dimensional response vectors with massive redundancy. Since the texture stimuli tile the visual field, this creates built-in translation-like structure regardless of training. The paper reports no results without this replication, so it is impossible to determine whether the key findings (circular manifolds, linear decodability, equivariance, cross-condition generalization) reflect genuine emergent geometry or are artifacts of this design choice. This confound affects the paper's core empirical claims about the V4 digital twin specifically. The robust ResNet results (Section 4.4) do not have this issue and provide partial converging evidence, but the paper's headline claims about "the visual cortex" depend on the digital twin findings.

- **The digital twin is not validated for the test stimuli, so claims about V4 are unsupported.** The model was trained on natural images but is tested on rotated objects and texture metamers — stimuli differing substantially from the training distribution. The paper provides no validation: no correlation between model predictions and held-out neural data (even for natural images), no checks on whether tuning properties generalize, and no robustness tests across model seeds or architectures. The strong claims throughout the paper (e.g., "the visual cortex recovers the world manifold" in the Section 4.3 title, "neural representations in area V4 of the primate visual cortex... reflect geometric structures" in the Discussion) infer properties of real biological V4 from an unvalidated model. Without validation for these specific stimuli, the paper's evidence primarily concerns the geometry of a particular neural network model, not necessarily the geometry of V4. This is the single highest-priority issue to address.

- **Equivariance analysis is too narrow to support the "near-equivariant" claim.** The test (Section 4.3, Figure 4e) fits a 2D rotation matrix to the first two principal components of the activations. This is a limited test: it assumes the relevant representation lives in exactly 2 dimensions and that the group action is a rotation in those coordinates. No quantification is provided of how much neural variance these two PCs capture (the "VE" labels in Figure 4b are not reported numerically in the text or figure caption), so the analysis may be operating on a small fraction of the signal. The paper does not test whether alternative transformations (scaling, reflection, shear) fit equally well, whether the rotation generalizes across textures, or whether the remaining dimensions break equivariance. The claim that "training enhances the network's equivariance" is plausible but far from proven with the current evidence.

### Minor

- **Cross-condition generalization results lack statistical rigor.** The reported circular correlations (diagonal 0.96, off-diagonal 0.83 for trained; 0.88 and 0.39 for untrained) are presented without confidence intervals, standard deviations, or significance tests. The decoder details are underspecified: the paper states a decoder was "trained to determine the angle of one texture class" but does not specify the decoder architecture (linear regression on the full 60K-dimensional space?), regularization, or train/test split for this experiment. A baseline (chance-level correlation, or predicting the mean angle of the training texture) would help contextualize the 0.83 off-diagonal value. The untrained model's diagonal correlation of 0.88 shows substantial orientation information is available without training, making the trained model's diagonal of 0.96 a modest improvement — the real advantage is in off-diagonal transfer (0.83 vs. 0.39), which should be emphasized more.

- **Only one trained model is used throughout.** The entire analysis rests on a single model instantiation. Repeating the key experiments with multiple independently initialized and trained models would indicate how robust the geometric findings are to training stochasticity. This is especially important given the spatial replication confound.

- **The texture stimuli and decoder methodology are underspecified.** The paper mentions "texture metamers" from Portilla & Simoncelli (2000) and identifies four texture classes (Arrows, Bars, Banded, Stratified), but does not specify: number of images per texture class, pixel sizes, whether textures tile the visual field, the precise decoder used for CCG (linear regression? on what features?), or the training/test protocol. The robust ResNet results (Section 4.4) are presented without architecture specifics, number of textures tested, or any quantitative comparison to the V4 model beyond visual similarity.

### Trivial

- The text appears to have a formatting artifact: "mean (across objects) angular errors of 0.007 radians, 0.008 radians, and 0.2" (presumably 0.2 radians) lacks the unit for the third value.

## Nice-to-Haves

- Remove the spatial replication and repeat key analyses (PC manifolds, decoding, equivariance fit, CCG) using only the original 1244 neurons at their learned receptive field positions. If results hold, this would substantially strengthen confidence in the findings.
- Validate the digital twin for the test stimuli: compute correlation between model predictions and held-out V4 responses for natural images, and argue (or test) why this should generalize to textures and rotated objects.
- Deepen the equivariance analysis: measure the norm of the difference between transformed representations and representations of transformed inputs across many dimensions (e.g., using canonical correlation or a learned linear map), and compare to a null distribution.
- Report uncertainty estimates (confidence intervals or standard deviations across folds/seeds) for all quantitative results.
- Include explicit comparisons between the V4 digital twin and the robust ResNet in a single table, with sample sizes and statistical tests.

## Removed Points

These points are flagged to be removed; treat them with caution.

- *"The theoretical appendix (A.5) is referenced but unavailable in the manuscript"* — Removed because the parser strips appendix sections; they exist in the original submission.
- *"The paper lacks a limitations paragraph"* — Removed as a formatting/style nitpick. The Discussion does discuss limitations (color perception reshaping, pitch perception), though not exhaustively.
- *Typo comments (e.g., "fti" instead of "fit")* — Removed as parser artifacts, not author errors.
- *Suggestion to record from real V4 for these stimuli* — Removed as scope creep; this would be a fundamentally different paper requiring months of animal experimentation.
- *"Check original" regarding the 0.2 value* — Removed as this is the reviewer's uncertainty, not an actual error in the paper (the value is present in the text).
- *Strength finder's claim about "quantitatively tests equivariance by fitting rotation matrices"* — While present, the strength is downgraded in impact because the test is too narrow (only 2 PCs), as noted in the Major weaknesses.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a perspective not already present in the paper's framing and results.

## Suggestions

1. **Most critical:** Either (a) remove the spatial replication and re-run all analyses with the original 1244 neurons, or (b) provide a principled argument and control experiments showing the replication does not create spurious structure. Without this, the core V4 digital twin findings remain confounded.
2. **Second most critical:** Validate the digital twin for the test stimuli, or at minimum acknowledge this limitation explicitly and soften claims about "the visual cortex" to claims about "a model of V4."
3. Report confidence intervals / standard deviations for all key quantities (decoding errors, circular correlations, equivariance test loss).
4. Deepen the equivariance test to examine the full representation, not just the top 2 PCs.
5. Repeat the main experiments with at least 3 independently trained model seeds.

## Score and Decision

The paper addresses an important question with a clever methodology and a useful conceptual framework. However, the spatial replication confound and the lack of digital twin validation for the test stimuli are structural issues that undermine the central claims about V4. The equivariance analysis is too thin to carry the weight placed on it. The ResNet results provide partial converging evidence but do not salvage the V4-specific claims. A major revision addressing the spatial replication, model validation, and statistical rigor is necessary before the paper could be accepted.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>