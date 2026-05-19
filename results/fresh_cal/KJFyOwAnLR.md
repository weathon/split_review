Now I have a thorough understanding of the paper and can verify the reviewer claims against the actual text. Let me produce the final consolidated review.

## Summary

This paper tests the "mirroring hypothesis"—that neural manifold geometry reflects latent causal structure in the world—using a digital twin model of macaque V4 (a ResNet50 trained to predict responses of 1,244 V4 neurons). The authors compare two visual scenarios: (1) object rotation, where the circular structure is already present in pixel space; and (2) texture rotation, where it is not. They find that the trained model recovers a circular manifold from textures whose pixel-space lacks linear orientation structure (decoding error drops from 0.6 rad to 0.12 rad), provides evidence of near-equivariance via rotation matrix fitting, and demonstrates cross-condition generalization—a decoder trained on one texture transfers to others (off-diagonal circular correlation 0.83 vs. 0.39 in untrained controls). The findings are extended to ImageNet-trained models, suggesting the principles are not unique to the V4-trained model.

## Strengths

- **Non-trivial recovery of latent structure from unstructured input (Section 4.3, Figure 4b–c).** For four texture classes where pixel-space lacks a linearly decodable circular manifold (mean angular error 0.6 rad), the trained digital twin reconstructs a low-dimensional circular manifold enabling linear decoding (mean error 0.12 rad). The untrained network performs worse (0.24 rad), isolating training as the key driver. This directly supports the claim that the system recovers latent world geometry that is absent in the input.

- **Cross-condition generalization through manifold alignment (Section 4.4, Figure 5c).** Decoders trained on one texture class transfer to novel textures in the trained model (avg. off-diagonal circular correlation 0.83) but fail in the untrained model (0.39). This provides concrete evidence linking manifold alignment to out-of-distribution generalization, a central claim.

- **Systematic experimental design distinguishing trivial from non-trivial structure preservation (Sections 2, 4.2, 4.3).** The paper explicitly contrasts cases where structure is already present in the input (object rotation, Section 4.2) with cases where it must be recovered (textures, Section 4.3), and always compares trained vs. untrained networks. This cleanly isolates when neural recovery is genuinely non-trivial—a distinction prior work often overlooks.

- **Extension to a task-optimized artificial network (Section 4.4, Figure 5d–f).** The key findings (structure recovery, linear decoding, cross-condition generalization) replicate in a robust ResNet trained on ImageNet, showing that these geometric principles are not unique to the V4-trained model but may be general to trained vision systems.

## Weaknesses

### Fatal
None.

### Major

- **The equivariance test is narrow and does not convincingly establish near-equivariance as a property of the full representation (Section 4.3, Figure 4e).** The authors fit a 2D rotation matrix only to the *first two principal components* of the neural responses. Equivariance is formally a property of the full high-dimensional representation; restricting the test to the top 2 PCs is a weak proxy. The paper does not report how much variance those two PCs capture, whether a rotation matrix fits better than a general linear transformation (which would also capture circular structure), or whether the fitted rotation is consistent across different neuron subsets. Without these controls, the result may reflect that any roughly circular 2D projection can be approximated by a rotation matrix. Since the equivariance claim is one of three main findings, the evidence needs to be substantially stronger.

- **Cross-condition generalization is tested only within oriented textures sharing the same type of feature (Section 4.4).** All four texture classes (Arrows, Bars, Banded, Stratified) have clear directional/orientable structure. The claim that "equivariant representations facilitate generalization" is supported by showing transfer *among* oriented textures, which primarily tests whether orientation is encoded in a texture-invariant manner for textures with similar feature types. The paper does not test transfer to non-oriented or isotropic textures, nor to textures with different frequency content. The conclusion should be scoped more narrowly.

### Minor

- **No validation metric for the digital twin is reported in this paper (Section 4.1).** The paper states the architecture "has been demonstrated to effectively predict V4 neuronal responses (Cadena et al., 2023)" and cites the data source (Willeke et al., 2023), but does not provide its own test-set correlation, fraction of explainable variance, or any quantitative measure of how well the specific trained model predicts held-out V4 responses. A brief validation statement would substantially strengthen confidence that the observed geometric structures reflect properties of V4 rather than modeling artifacts.

- **Statistical rigor is uneven (Sections 4.3, 4.4).** Key results (decoding error, rotation matrix fit, CCG circular correlations) lack confidence intervals across random initializations or data splits. The paper reports mean errors across textures but not variance across repeated model fits or cross-validation folds. The rotation matrix fit (Figure 4e) uses 80 trials from 20 random 80-20 splits, but there is no chance-level baseline (e.g., shuffling angle labels) to calibrate what "good" performance means.

- **Framing occasionally conflates model findings with biological findings (Abstract, Discussion).** The paper states "we demonstrate that neural representations in area V4 of the primate visual cortex … reflect geometric structures" and "the emergence of near-equivariant representations in the visual cortex." Since all experiments are *in silico* on a model, these statements overreach. The paper is transparent about using digital twins, but the biological phrasing should be tempered (e.g., "in a model of V4" or "in a digital twin of V4") to avoid implying direct neural recordings.

- **The "mean slope of fitted lines" metric used in Figure 4d is non-standard.** Plotting the slope of the fitted line between true and predicted angles across layers is harder to interpret than angular error or R², and it conflates scale with alignment. This is a presentation choice that could be improved.

### Trivial
None.

## Nice-to-Haves

- Test the equivariance claim more rigorously: fit a rotation matrix to higher-dimensional response subspaces (e.g., 5–20 PCs), compare against a general linear map baseline, and check consistency across neuron subsets.
- Include non-oriented texture classes (e.g., stochastic or isotropic patterns) in the CCG experiment to scope the generalization claim more precisely.
- Report the Portilla & Simoncelli texture metamer parameters (or release the stimuli) to aid reproducibility.
- Add chance-level baselines (permutation tests) for the rotation matrix fit and decoding analyses.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"The method for fitting the rotation matrix is relegated to the appendix (Section A.4, unavailable) with only a vague description."** — Removed per hard rule: the parser strips appendix sections from all papers; they exist in the original submission. The paper provides a description ("projected gradient scheme") with details in the (present but stripped) appendix.
- **"The contribution is positioned as a discovery about biological vision, but the experiments are entirely computational... As it stands, the reader cannot distinguish between a genuine neuroscientific finding and a modeling artifact."** — Partially removed as overstatement. The paper is transparent about using a digital twin (stated in abstract and Section 4.1) and cites prior validation. The framing-overreach concern is retained as a minor weakness, but the claim that the reader "cannot distinguish" is factually incorrect given the paper's clear description of its computational approach.
- **"The paper claims to 'demonstrate the emergence of equivariant representations' in V4... Because the only data-driven component is the digital twin (which is never validated against neural data), these claims are actually about a model of V4, not about V4 itself."** — Demoted from structural/fatal to minor framing concern (retained above). The paper explicitly states "digital twin model of primate V4 neurons" and cites prior validation work.
- **"In theoretical analyses, presented in A.5, we demonstrate... The appendix is stripped, but Section A.4 (fitting rotation matrix) and A.5 (theoretical analysis) are essential for evaluating the claims; without them, the methods are incomplete."** — Removed per hard rule about missing appendix content being a parser artifact.
- **"The texture generation process (Portilla & Simoncelli metamers) is described, but the exact parameters are not provided."** — This is a reasonable reproducibility suggestion but is demoted to nice-to-have rather than a weakness.
- **"The paper should release or detail the stimuli to allow reproduction."** — Same as above.
- **"Why not also test other backbones or layers? Showing that the same findings hold in different architectures would strengthen the claim of universality."** — Nice-to-have; the paper already tests a V4-trained model, its untrained variant, an ImageNet-trained ResNet, and its untrained variant.
- **"The paper would be more honest if it presented itself as a computational study..."** — Removed as editorializing. The paper is clear about its computational methodology.
- **Some strengths from the Strength Finder: generic phrasing like "this paper addressed an important problem" — not present in the strength finder's output, so nothing to remove there.**

## Novel Insights

The reviews collectively surface a tension: the paper's central methodological contribution (using digital twins to probe neural manifold geometry with systematic stimulus control) is also its central vulnerability (the biological claims depend on the fidelity of a model that is not independently validated here). This tension runs deeper than the standard "model vs. brain" caveat because the paper's framework specifically distinguishes trivial from non-trivial structure recovery, making the model's internal representations the object of study rather than merely a tool for prediction. An interesting path forward would be to treat the digital twin as an *in silico* preparation whose predictions generate experimentally testable hypotheses: the paper's strongest result (CCG across textures) could be directly verified by recording V4 responses to the same stimuli, which would simultaneously validate the model and confirm the biological reality of the observed manifold alignment.

## Suggestions

1. Add a brief validation paragraph in Section 4.1 reporting the trained digital twin's held-out prediction accuracy (e.g., correlation or fraction of explainable variance on the test set from Willeke et al., 2023) to establish model fidelity.
2. Strengthen the equivariance test: fit a rotation matrix to the response projected onto more PCs (5–20), compare against a general linear map, and report how much variance the fitted 2D subspace captures.
3. Add chance-level baselines (e.g., permutation of angle labels) to the rotation matrix fit and decoding analyses.
4. Add confidence intervals or error bars across random seeds/data splits for the key quantitative results (decoding error, rotation matrix fit, CCG).
5. Scoping: explicitly acknowledge in the Discussion that the texture generalization experiment only tests transfer among oriented textures, and that generalization to non-oriented textures remains an open question.

## Score and Decision

**Originality:** 7/10 — The mirroring hypothesis framework is not entirely new, but the application to vision via digital twins with the structure-maintained vs. structure-lost distinction is a novel experimental paradigm.

**Importance of research question:** 8/10 — Understanding how neural representations relate to world structure and enable generalization is a fundamental question in neuroscience and AI.

**Claims support:** 6/10 — The core claim (non-trivial structure recovery) is well-supported. The equivariance claim is weakly supported. The CCG claim is supported within the scoped domain.

**Soundness of experiments:** 7/10 — Experimental design is thoughtful (trained vs. untrained, objects vs. textures, extension to ImageNet models). Weaknesses are in the equivariance methodology and limited texture diversity.

**Clarity of writing:** 8/10 — Well-structured, clear framework presentation, good motivation throughout.

**Value to community:** 7/10 — Provides a useful paradigm and testable hypotheses for studying neural manifold geometry in vision.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>