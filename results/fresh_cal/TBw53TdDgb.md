Now I have all the information needed. Let me produce the consolidated review.

## Summary

SADE proposes an autoregressive diffusion method for generating synthetic scene-text images, addressing the problem that standard diffusion models cannot generate characters in positions never seen during training. The key idea is to split images into overlapping vertical parts and generate them sequentially (left to right), with each part conditioned on the previously generated part. The method is evaluated on both a mock number plate dataset and a real-world vehicle type label dataset, using OCR test accuracy as a proxy for synthetic data quality. The results show substantial OCR improvements, particularly for character sequences with characters in positions absent from the training data (e.g., 0% → 94.67% on the vehicle label unseen-position test set).

## Strengths

- **Clear demonstration of the problem**: Section 3.2 and Figure 1 show that a standard diffusion model trained without a specific character-position combination produces garbled images when that combination is requested, concretely motivating the need for SADE's design.

- **Strong empirical evidence for the core claim on unseen positions**: On the mock data experiment 6 (Section 5.1), SADE-trained OCR models achieve **100% accuracy** on 1,508 held-out test images containing '5' in the sixth position — a configuration the original training data lacks. On the vehicle type label set 7 (Section 5.2), the only sequence with a character in an unseen position yields **0% accuracy with original data alone, 72.92% with SADE-only data, and 94.67% with combined data**. These results directly validate the central contribution.

- **Practical real-world improvement**: On the vehicle type label dataset (Figure 6), combining original and SADE-generated data raises average test accuracy from 37.93% to 97.95%, and hold-out accuracy from 78.87% to 94.72%. The method fills a real gap that even a strong off-the-shelf OCR model (Baek et al., 2019) cannot bridge (yellow bars in Figure 6).

- **Novel overlapping-split design**: The strategy of splitting images with at least one character of overlap (Section 3.3) avoids the cropping artifacts that naive part-based generation would produce, where cropped character fragments would be misinterpreted as background.

- **Honest and informative limitations discussion**: Section 5.3 transparently acknowledges artifacts, the tendency of the model to "copy" rather than generate, and the dependence on tuning the number of parts for each dataset. This strengthens the credibility of the reported results.

## Weaknesses

### Fatal
None.

### Major

- **No comparison against existing synthetic data generators**: The paper discusses SynthTIGER, CTIG-DM, and Diff-Text in the Related Work (Sections 2.1–2.2) and even positions SADE as potentially addressing a need for "more modern and realistic scene-text generation engines" (Section 2.1), yet provides no experimental comparison against any of them. Without such comparisons, it is impossible to assess whether SADE advances the state of the art or is simply a different (possibly weaker) approach. The core claim — that SADE-generated synthetic data improves OCR — is demonstrated, but the paper's significance relative to existing methods is unestablished.

- **Missing simple augmentation baseline**: The OCR training pipeline uses "no additional data transformations" (Section 4.4). A natural baseline would be training on original data with standard augmentations (rotation, noise, color jitter, etc.). Without this, the observed improvements could partly or wholly reflect increased data volume/diversity rather than any special property of SADE's generation. This weakens the evidence that SADE is more effective than a straightforward, cheap alternative.

### Minor

- **No ablation of image parts or overlap size**: The number of parts is set to 3 for mock data and 2 for vehicle data, and overlap is fixed at one character, but no ablation study examines how these choices affect generation quality or OCR accuracy. The paper states these were selected "based on searches and early experimentation" (Section 4.3) and "must be tuned" (Section 5.3) but does not present sensitivity analysis. Readers cannot assess how robust SADE is to these hyperparameter choices.

- **High variance across splits**: Standard deviations in accuracy reach up to 33.84 percentage points for synthetic-only models on the vehicle data (Section 5.2). While the paper attributes this to varying similarity between train and test sets, the high variance raises concerns about robustness and makes it difficult to predict the method's reliability on new data.

- **Unjustified 1:3 data mixing ratio**: The choice to mix original and synthetic data at a 1:3 ratio (Section 4.4) is stated without justification or sensitivity analysis. A different ratio might yield substantially different results.

- **No discussion of potential duplication artifacts from overlapping joins**: The Join function "combines image parts by pasting over overlapping regions" (Algorithm 2). If a full character appears in the overlap region, it would appear in both parts; the paper does not discuss how this pasting operation resolves such duplication or what visual artifacts may arise.

### Trivial
None.

## Nice-to-Haves

- **Report unseen-position accuracy consistently across all experiments**: The paper's strongest evidence for the core claim comes from two dedicated test sets (mock experiment 6 and vehicle set 7). Reporting unseen-position accuracy separately for the other experimental setups would strengthen the link between the results and the claimed contribution.

- **Statistical significance tests**: Given the small number of splits (5 for vehicle data), confidence intervals or significance tests would be more informative than standard deviations alone.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"Evaluation protocol does not fully isolate the claimed benefit for unseen positions"** (Harsh Critic point 3): Removed. The paper explicitly designs experiments 6 (mock) and set 7 (vehicle) to test this exact scenario, and the critic acknowledges these are "the strongest pieces of evidence." The request to extend this to all experimental configurations is structurally a nice-to-have, not a weakness.

- **"Relies too much on copying... threatens the validity of the approach"** (Harsh Critic's reading of Limitations): Removed. This concern originates from the paper's own honest Limitations section (Section 5.3), where the authors transparently identify it and commit to addressing it in future work. The empirical results show strong performance despite this issue. Self-acknowledged limitations are not weaknesses to be held against the paper.

- **No FID/manual quality evaluation**: Removed. The paper explicitly and consistently uses OCR accuracy as its evaluation metric (Section 3.5), arguing it directly measures how well synthetic data captures task-relevant variation. This is a principled choice, not an omission. Criticizing the absence of FID or human ratings would be imposing a different evaluation philosophy, not identifying a flaw in the paper's own protocol.

- **No computational cost discussion**: Removed. Not standardly required for a research paper establishing a method. This is a nice-to-have for deployment but not a weakness of the scientific contribution.

## Novel Insights

Neither reviewer identifies a novel insight beyond what the paper itself contributes. The reviews surface standard expectations (baseline comparisons, ablations, augmentation baselines) but do not uncover a latent contradiction, alternative interpretation of the results, or connection to broader phenomena that the authors missed.

## Suggestions

1. **Add at least one comparison against an existing synthetic data generator** (SynthTIGER or CTIG-DM) using identical training/evaluation protocols. This is the single highest-priority addition — without it, the contribution's significance relative to the state of the art cannot be assessed.

2. **Add a simple augmentation baseline** (random affine, noise, occlusion, color jitter applied during OCR training) to disentangle the benefit of SADE's specific generation quality from the general benefit of increased data diversity.

3. **Include an ablation study** on the number of image parts and overlap size, measuring both generation quality and OCR accuracy, to validate the hyperparameter choices and characterize robustness.

4. **Provide a sensitivity analysis for the 1:3 data mixing ratio** to justify the choice or identify the optimal ratio.

## Score and Decision

The paper presents a method with a sound motivation, a clearly described design, and strong empirical evidence that it can generate characters in positions unseen during training — a genuine capability that standard diffusion models lack. The mock and vehicle label experiments, particularly the 0%→94.67% result on the unseen-position test set, demonstrate real practical value.

However, the absence of comparisons against existing synthetic data generators (SynthTIGER, CTIG-DM, Diff-Text) is a significant omission. Without knowing whether SADE outperforms, matches, or underperforms existing approaches, the paper's contribution cannot be properly situated in the literature. The missing augmentation baseline further widens this evidential gap.

The paper's core technical contribution and empirical demonstrations are real and well-supported; the main missing element is situating this contribution relative to existing work through direct comparison.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Accept</decision>