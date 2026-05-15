Now I have a thorough understanding of the paper. Let me compose my consolidated review.

---

## Summary

This paper identifies biases and limitations in existing diffusion model memorization metrics (modified ℓ₂ distance, embedding-based similarity, percentile-based scoring) and proposes SOLIDMARK, a method that augments each training image with a random grayscale border. At evaluation time, the model is prompted to outpaint the border; accurate border reconstruction indicates pixel-level memorization of that image. The paper also re-evaluates known mitigation techniques using SOLIDMARK and releases a pretrained model to facilitate further research.

## Strengths

- **Principled critique of existing metrics (Section 3):** The paper provides concrete evidence (Figure 2) that the modified ℓ₂ distance still reports monochromatic images as false positives, and Figure 3 demonstrates how 95th-percentile scoring can mask fine-grained memorization reductions. This analysis is well-reasoned and exposes real blind spots in current practice.

- **Novel key-query design that eliminates semantic inference (Section 4):** SOLIDMARK's use of a random grayscale border as the key ensures that an unmemorized model cannot infer the key from the image content, addressing a fundamental confound in inpainting-based approaches where masked and unmasked regions are semantically correlated.

- **Perturbation experiments provide compelling evidence for pixel-level detection (Table 5):** Small, often imperceptible augmentations (cropping, rotation, blurring) sharply reduce reported memorizations, especially at low thresholds δ. This demonstrates that SOLIDMARK captures fine-grained pixel-level information rather than semantic similarity, a capability prior metrics do not provide.

- **Detects duplication-induced memorization despite independent keys (Table 3):** The method reports increasing memorization as exact duplicates are added to the training set, even though each duplicate receives a different random border. This addresses a natural concern and validates that the metric captures genuine memorization effects.

- **Enables direct per-image evaluation (Section 6):** SOLIDMARK allows testing whether a specific training image is memorized without requiring repeated random sampling from the model, which is impractical for unconditional models or when the target image is rare. This is a real practical advantage over existing approaches.

## Weaknesses

### Fatal
None.

### Major

- **The mitigation technique re-evaluation rests on an invalid comparison (Table 4, Section 5.3):** The paper compares SOLIDMARK's measurements (fine-tuned SD 2.1 on LAION-5K, eidetic threshold at δ=0.01) against SSCD-based reductions reported by Somepalli et al. (2023b) (full SD model trained on LAION-5B, 95th-percentile scoring). These differ in model checkpoint, dataset size, training procedure, and metric design. The paper does not reproduce the original baselines in its own setup; it simply quotes numbers from a different experiment and treats the discrepancy as a finding. The claim that "reconstructive memorization likely arises more from cues in the prompt compared to pixel-level memorization" is therefore unsupported speculation. No error bars or statistical tests are reported for the SOLIDMARK numbers, and only a single threshold (δ=0.01) is used — despite the paper itself criticizing single-threshold approaches earlier (Section 3.2).

- **No direct validation that border recall correlates with actual image regeneration:** The paper never shows that images whose borders are correctly recalled are also images the model can regenerate nearly identically under standard (border-free) sampling. The perturbation experiments (Table 5) provide indirect evidence, but the central claim — that SOLIDMARK measures memorization of the training image content — would be substantially strengthened by demonstrating that the set of images flagged by SOLIDMARK overlaps significantly with those known to be pixel-exact regenerations via existing methods. Without this, the metric measures recall of an attached random key, and the leap from key recall to image memorization remains an inference rather than an empirical finding.

### Minor

- **ℓSM distance is never explicitly defined:** The paper refers to ℓSM as a "scalar distance function between keys" but never gives the formula (presumably |predicted intensity − true intensity|). This is a simple point but hurts reproducibility for readers who want to implement the metric.

- **False positive rate is acknowledged but not quantified (Section 6):** The paper mentions a false positive probability based on random guessing of the grayscale intensity (~1/256 for a single image) but does not measure or report it empirically. When evaluating thousands of images, this becomes important for interpreting results.

- **Single threshold used in mitigation evaluation contradicts the paper's own advice:** Section 3.2 criticizes existing work for using single-threshold eidetic metrics, yet Table 4 only reports (ℓSM, 0.01). Multiple thresholds would provide a more complete picture.

- **No error bars or statistical tests in any experiment:** All results are reported as point estimates without variance, which is standard in this field but limits confidence in the findings, especially given the small-scale setup (5K-image subset, fine-tuned rather than trained from scratch).

### Trivial

- The term "foundation model" (Section 5.4) is ambitious for a 200K-image, 20-epoch model; consider "pretrained reference model" instead.

## Nice-to-Haves

- A direct correlation experiment: train a model both with and without borders, identify images flagged by SOLIDMARK, and test whether those same images appear as pixel-exact generations under standard sampling from a border-free model checkpoint. This would directly ground the metric in the phenomenon it claims to measure.

- A controlled replication of the mitigation baselines within the same experimental setup (same model, dataset, and evaluation pipeline) rather than quoting numbers from a prior paper.

- An empirical false-positive rate: run SOLIDMARK on images not in the training set and report the distribution of ℓSM values to establish a baseline.

## Removed Points

These points were flagged by reviewers but are removed per policy:

- **Criticism about references "Naseh et al., 2023" and "Dar et al., 2024" not being verifiable:** Per hard rules, all references cited in the paper are assumed to exist. Removed.

- **Claim that SOLIDMARK "cannot evaluate memorization of the original training data" at a conceptual level:** The paper provides a well-motivated proxy (key recall → pixel-level memorization) and perturbation evidence supporting it. The valid criticism about lack of direct correlation is kept in Major, but the categorical claim that the method *cannot* evaluate memorization is removed as an overstatement.

- **Claim that calling the 200K-image model a "foundation model" is "misleading":** The paper fully discloses the model's training details (200K images, 20 epochs, batch size 8). The term is ambitious but not deceptive. Removed as a stylistic nitpick.

- **Various formatting/style nitpicks and missing appendix/proof claims:** Removed per policy.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Replicate mitigation baselines in a controlled setup.** Redo the mitigation comparison (Table 4) using the same model checkpoint, dataset, and evaluation pipeline for both SOLIDMARK and at least one existing metric (e.g., compute SSCD similarity on the same generations). This would either confirm or refute the claimed discrepancy with a valid comparison.

2. **Add a direct validation experiment.** Train a model on border-augmented data, identify images that SOLIDMARK flags. Independently test whether the same model (or a model trained identically without borders) can generate those images pixel-exactly via standard sampling. Report overlap statistics.

3. **Quantify false positive rates.** Run SOLIDMARK evaluation on held-out (non-training) images and report the distribution of ℓSM values. Provide a recommended threshold based on this distribution.

4. **Explicitly define ℓSM** as ℓSM(ĝ, g) = |ĝ − g| where g is the true grayscale intensity (0–255) and ĝ is the predicted intensity. Also consider normalizing by the range.

5. **Use multiple thresholds** in the mitigation evaluation (Table 4) to provide a more complete picture, consistent with the paper's own critique of single-threshold methods.

## Score and Decision

The paper's core contributions — a careful critique of existing memorization metrics and a novel key-query method for per-image evaluation — are valuable and well-motivated. The perturbation experiments convincingly show that SOLIDMARK captures fine-grained pixel-level information. However, the re-evaluation of mitigation techniques (Table 4) is based on an apples-to-oranges comparison that does not support the claimed conclusions, and the lack of direct validation that border recall correlates with actual image regeneration leaves a gap between the method's design and its central claim. These are significant but addressable weaknesses; they do not invalidate the method itself.

The paper would be strengthened by a controlled replication of mitigation baselines within its own setup and a direct correlation experiment. In its current form, the paper makes a novel methodological contribution but overclaims on the mitigation re-evaluation.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>