Now I have a thorough understanding of the paper. Let me write the consolidated review.

---

## Summary

This paper proposes "Duet," a method for certified robustness training that aims to preserve clean accuracy by transferring rotation-matrix information from a pre-trained vanilla (non-robust) model to the certification model. The approach uses SVD to decompose weight matrices into rotation matrices (U, V^T) and singular values (Σ), then adds a similarity loss that aligns the certification model's rotation matrices with those of the vanilla model. A low-rank approximation is used to reduce computational cost. Experiments on CIFAR-10 report a +3.76% clean accuracy improvement with a −0.93% certified accuracy drop relative to a global-Lipschitz-regularized baseline.

## Strengths

- **Direct and quantified claim of clean accuracy preservation**: The paper reports +3.76% clean accuracy improvement and −0.93% certified accuracy degradation (contributions list, Section 1). This directly addresses a recognized problem in certified robustness — the clean-accuracy penalty — and provides concrete numbers, even though the baseline is specified only vaguely.

- **Rotation matrix similarity is empirically measured and improves**: The paper reports that rotation-matrix similarity between the vanilla and certification models increases from 77.8% (standard certified training) to 95.6% (with Duet) (Section 5). This provides direct evidence that the knowledge-transfer mechanism is working as intended.

- **Low-rank approximation for efficiency**: The method proposes using only a few orthogonal unit vectors (top-r) from the vanilla model's rotation matrices to reduce storage and computation (Section 4.3). This is a practical consideration that addresses a real deployment concern.

- **Novel angle of attack on the clean-accuracy problem**: Identifying the role of rotation matrices (as distinct from singular values/spectral norms) in clean accuracy degradation is a genuinely different perspective from prior work, which has focused on regularization strength, warm-up schemes, or local Lipschitz computation.

## Weaknesses

### Major

1. **Central motivation is asserted without empirical support.**  
   Section 4.2 claims that certified robustness training makes singular values "similar" and that "the maximum singular value σ₁ is the same as the other singular values," which allegedly "disables" rotation matrices and causes clean accuracy to drop. **No evidence is provided for this claim** — no plots of singular value distributions, no comparison of σ₁/σ₂ ratios between vanilla and certified models, no analysis of whether certified models actually have flatter singular value spectra. This claim is also mechanically questionable: Lipschitz regularization controls the *product* of spectral norms across layers, not the equality of singular values within a single weight matrix. The paper provides no argument or evidence connecting the two. Without this diagnosis, the motivation for the proposed loss is much weaker, and the paper reads as a solution in search of a problem.

2. **Experimental reporting is critically incomplete.**  
   The paper reports only *differences* in accuracy (+3.76% clean, −0.93% certified) relative to a baseline described as "previously trained certified robustness model that only utilized global Lipschitz regularization" (contributions, Section 1). The absolute clean and certified accuracies of the baseline (and of Duet) are never given. The vanilla model's accuracy is reported (90.06%), which is useful as an upper bound, but without baseline numbers the reader cannot assess whether a 3.76% gain is from a low or already-competitive starting point. Similarly, no standard deviations or multi-run statistics are reported. The paper mentions comparing against both global Lipschitz (Lee et al., 2020) and local Lipschitz (Huang et al., 2021) methods, but no absolute results for either are presented. This makes it impossible to verify the claimed improvement or situate it within the literature.

3. **Evaluation is limited to a single setting.**  
   Experiments are conducted only on CIFAR-10 with one architecture (6 conv + 2 FC), one perturbation type (ℓ₂), and one perturbation radius (36/255). No results on CIFAR-100, Tiny ImageNet, ℓ∞ perturbations, or other standard architectures (e.g., ResNet) are provided. This is acceptable for a preliminary methodological paper, but the claims of general applicability ("practical training method," "wide range of scenarios") are not supported by the evidence.

### Minor

4. **The similarity loss formulation is provided without justification or ablation.**  
   The loss \( L_{sim} = \sum_l \| \frac{\|\sigma_{cer}^l\|}{\|\sigma_{van}^l\|} Rota_{van} - \frac{\|\sigma_{van}^l\|}{\|\sigma_{cer}^l\|} Rota_{cer} \|_2 \) (Section 4.4) uses a specific reciprocal scaling with spectral-norm ratios. The paper does not explain why this particular form is correct, derive it from any principle, or ablate it against simpler alternatives (e.g., direct cosine similarity between U and V matrices, Frobenius norm of UU^T differences, or standard logit-level KD). Without this, the reader cannot tell whether the specific form matters or whether any rotation-alignment loss would work.

5. **No ablation of the low-rank approximation.**  
   Section 4.3 motivates low-rank approximation to "select important rotation matrix information and reduce computational cost," but no experiments vary the rank r or measure the trade-off between r, clean accuracy, and certified accuracy. It is unclear how many singular vectors are needed and whether the approximation actually preserves clean accuracy.

6. **Computational overhead is not reported.**  
   The method adds a forward pass through the vanilla model, SVD computation (even with low-rank approximation), and an additional similarity loss term. The paper claims SVD is "offline" and "cheap" but provides no wall-clock training time or memory comparison against the baseline. This makes it difficult to assess practical deployability.

7. **Writing quality impedes understanding.**  
   The paper contains numerous passages that are grammatically broken or unclear (e.g., repeated sentences in Section 4.4, garbled descriptions in the experiment section). The related work section reads as a list of citations without a clear narrative distinguishing the proposed approach. The paper would benefit from thorough editing.

### Trivial

- The paper does not specify training hyperparameters (learning rate, batch size, number of epochs, loss weighting coefficient between certified loss and L_sim). While hyperparameter details are often left to the code release, the combination of losses is a design decision that should be stated in text.
- No discussion of limitations, failure cases, or settings where the method might not work (e.g., when the vanilla model's architecture differs from the certification model, or when the vanilla model has low accuracy).

## Nice-to-Haves

- Validation of the singular-value-collapse hypothesis with plots of σ distributions for vanilla, standard-certified, and Duet-trained models.
- Ablation studies comparing the proposed L_sim against simpler rotation-alignment losses and standard knowledge distillation.
- Absolute accuracy tables with standard deviations for all methods (vanilla, global Lipschitz baseline, local Lipschitz, Duet) on a consistent evaluation protocol.
- Sensitivity analysis on the low-rank approximation rank r.

## Removed Points

These points are flagged per the consolidation rules; they should be treated with caution:

- **Algorithm 1 being an "unreadable image placeholder" / Figures and Tables unreadable** — These are parser artifacts. The original PDF would have legible figures, tables, and algorithm pseudocode. These observations are artifacts of text extraction, not paper flaws.
- **"No textual description of the training loop, weight scheduling, hyperparameters"** (partially) — Hyperparameter omission is considered a nitpick per consolidation guidelines. The core training procedure is described in Algorithm 1 in the original submission.
- **"The only comparison appears to be against a single global-Lipschitz method"** — Factually inaccurate. The paper explicitly mentions comparing against both global Lipschitz (Lee et al., 2020) and local Lipschitz (Huang et al., 2021) methods, even though absolute results are not tabulated.
- **Strength (Strength Finder's output) about "Insightful diagnosis"** — Dropped because it conflicts with Verified Weakness #1 (central motivation is unsubstantiated).
- **Strength about "Concrete training procedure via Algorithm 1"** — Algorithm 1 is an image in the original; its content cannot be evaluated from the text extraction.
- **Strength about "Clear comparison to baselines"** — Overstates what is actually presented, as absolute numbers are missing.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the standard concerns (missing absolute numbers, limited evaluation, unvalidated motivation) but do not offer a new synthesis or unexpected connection to other bodies of work.

## Suggestions

1. **Validate the core hypothesis**: Add an empirical analysis showing that certified robustness training does (or does not) collapse singular value spectra. Plot σ₁/σ_k ratios or singular value entropy across layers for vanilla, standard-certified, and Duet-trained models. This is essential to justify the paper's narrative.

2. **Report absolute numbers in a proper table**: Include clean accuracy, certified accuracy, and their standard deviations (over multiple runs) for: (a) the vanilla model, (b) the global-Lipschitz baseline (Lee et al., 2020 / BCP), (c) a local-Lipschitz baseline (Huang et al., 2021), and (d) Duet. Report the baseline numbers you are improving from.

3. **Ablate the similarity loss**: Compare the proposed L_sim against at least (i) a direct Frobenius-norm alignment of U matrices, (ii) an unweighted version without the spectral-norm scaling ratios, and (iii) standard feature-level or logit-level knowledge distillation.

4. **Expand the evaluation**: Add results on CIFAR-100 and/or Tiny ImageNet, and at least one ℓ∞ perturbation setting, to demonstrate generality beyond the single ℓ₂ CIFAR-10 configuration.

5. **State the full training objective explicitly in text**: Provide the total loss as \( \mathcal{L}_{total} = \mathcal{L}_{cert} + \lambda \mathcal{L}_{sim} \) (or whatever the form is), report λ and any scheduling, along with basic hyperparameters (learning rate, batch size, epochs, optimizer).

## Score and Decision

The paper identifies a real problem (clean accuracy degradation in certified robustness) and proposes a novel angle (rotation-matrix alignment via SVD) that has intuitive appeal. However, the core diagnostic claim motivating the method is presented without evidence, the experimental reporting is critically incomplete (no absolute accuracy numbers, single setting), and the loss formulation is not justified or ablated. These gaps are structural, not cosmetic, and prevent assessment of the claimed contribution.

**Originality**: Moderate. The rotation-matrix perspective is relatively novel.
**Importance**: Moderate. Clean accuracy preservation is a recognized challenge.
**Claims support**: Weak. The central motivation is unvalidated, and the experiments lack essential detail.
**Soundness**: Weak. Without absolute numbers or ablations, the main result cannot be verified.
**Clarity**: Below average. The writing is often unclear, and key procedural details are missing from the text.
**Value**: Moderate potential, but the current manuscript does not realize it.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>