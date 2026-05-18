Now I have a complete picture of the paper. Let me write the consolidated review.

## Summary

The paper identifies three problems with the standard reject-or-classify (RC) recipe for handling out-of-domain inputs — lack of communication between aleatoric and epistemic uncertainty, miscalibrated binary abstention, and unit mismatch between logits and uncertainty scores — and proposes Unified Uncertainty Calibration (U2C) to address them. U2C learns a non-linear calibration function τ_u that maps the epistemic uncertainty score to a logit, then integrates it with the c in-domain logits via a shared (c+1)-dimensional softmax. Experiments across four epistemic uncertainty estimators and eight ImageNet benchmarks show that U2C consistently improves classification error and expected calibration error over RC.

## Strengths

1. **U2C achieves consistent improvements over RC across diverse benchmarks and multiple epistemic uncertainty estimators.** Table 1 shows that replacing RC with U2C yields lower err and ece on nearly every combination of four epistemic methods (MaxLogit, ASH, Mahalanobis, KNN) and eight benchmark types spanning in-domain, covariate shift, near-OOD, and far-OOD scenarios. Deteriorations, when they occur, are small. This provides clear evidence that the proposed approach delivers on its primary claim of outperforming RC.

2. **U2C provides a principled integration of aleatoric and epistemic uncertainties that directly addresses three real limitations of the RC recipe.** Section 4 describes how the shared softmax norm enables the two uncertainty types to "communicate," how non-linear τ_u allows correcting misspecifications in the epistemic estimate, and how the soft (c+1)-th class score enables calibrated abstention at varying confidence levels. These are well-motivated improvements over hard thresholding.

3. **Evaluation across a full spectrum of distribution shifts with multiple epistemic uncertainty families.** The paper tests on in-domain (ImageNet-te), covariate shift (ImageNet-C, -R, -v2), near-OOD (NINCO, SSB-Hard), and far-OOD (iNaturalist, Texture, OpenImage-O) using four different epistemic estimators — MaxLogit (logit-based), ASH (activation shaping), Mahalanobis (density-based), and KNN (distance-based) — demonstrating generality of the approach.

4. **Lemma 5.2 provides a concrete theoretical advantage of U2C over RC.** Showing that RC has infinite NLL whenever in-domain data falls in the rejection region or out-domain data in the acceptance region (which is guaranteed by construction), while U2C's soft predictions avoid this pathology, is a clean formal argument that supports the method's motivation. This is the paper's strongest theoretical point.

## Weaknesses

### Fatal
None.

### Major

1. **The core method component — the non-linear calibration function τ_u — is not specified.** The paper states "learn a non-linear epistemic calibration function τ_u: ℝ → ℝ" (Section 4) and gives the optimization objective in Equation (7), but never states what function class τ_u belongs to. Is it a small MLP? A spline? A monotonic transformation? For a methods paper, this is the central component of the proposed contribution, and its parametrization is essential for reproducibility, implementation, and understanding what "non-linear calibration" actually means. The paper mentions "linear U2C" experiments (Section 6, line 192) but does not elaborate. This gap must be filled for the paper to be acceptable as a methods contribution.

2. **The claim of "state-of-the-art" performance is unsupported by the experiments.** The abstract and contribution paragraph (Section 1) assert that U2C "yields state-of-the-art performance across a variety of standard ImageNet benchmarks" and "significantly outperforms reject-or-classify." However, the experimental section (Section 6) compares U2C **only against RC**. There are no comparisons to other methods that produce (c+1)-class probabilities — such as posterior networks, evidential learning, ensembles with abstention, or even simple baselines like training a classifier with a held-out OOD background class. Demonstrating that a method beats the specific baseline it was designed to replace does not constitute a SOTA claim. The authors should either drop the SOTA language and reframe the contribution as "U2C improves over RC," or expand the experimental comparison to include alternative approaches.

### Minor

3. **The threshold α = 0.95 is used without justification or sensitivity analysis.** The method relabels the top 5% most uncertain in-domain validation examples as the (c+1)-th class. This hyperparameter determines the supervision signal for learning τ_u. There is no discussion of how this value was chosen, no sensitivity analysis, and no evidence that results are robust to this choice across different datasets or uncertainty estimates. An experiment varying α over a plausible range (e.g., 0.90–0.99) for at least one setting would strengthen the paper substantially.

4. **No error bars or measures of variability are reported.** The paper states that "error-bars are absent because there is no randomness involved in our experimental protocol" (Section 6), arguing that the validation/test split is fixed. However, this ignores randomness from training the base network f and from the selection of which 5% of validation examples are relabeled (which depends on the epistemic uncertainty estimate and the specific validation split). Given that many reported improvements are small (0.1–0.5 percentage points in err), it is impossible to assess whether these are meaningful without some measure of variability. Reporting results across multiple seeds or splits would address this concern.

5. **Lemma 5.1 is largely notational rather than analytic.** The lemma decomposes the error difference between RC and U2C into terms involving regions A, B, C, D — but these regions are defined by the decision boundaries of the two methods themselves. The result is that U2C outperforms RC where U2C makes better decisions (region B) and underperforms where RC makes better decisions (region C). It does not connect these conditions to properties of the data distribution or the uncertainty estimator that could be verified or exploited independently of the algorithm. Lemma 5.2 is more substantive.

6. **Results are aggregated without discussing variation across epistemic methods.** Table 1 shows variation — for example, on ImageNet-v2, U2C's err change is -0.1 (deterioration) for MaxLogit but +0.5 (improvement) for KNN. The paper states that U2C "brings improvements... in most experiments" without discussing whether improvements are consistent across epistemic families or concentrate on specific types. This commentary would help readers understand when U2C is most beneficial.

### Trivial

- The text has minor artifacts (e.g., "spannign" instead of "spanning" at line 190) that should be corrected. (Note: these may be OCR issues rather than author errors; if so, ignore.)

## Nice-to-Haves

- Reporting NLL metrics alongside err and ece would directly validate Lemma 5.2's theoretical argument that U2C avoids RC's pathological NLL behavior.
- An ablation comparing linear τ_u vs. non-linear τ_u with explicit architecture details would isolate the benefit of non-linear calibration. The paper mentions such experiments exist but does not report results in the main text.
- A simple baseline of "add a constant logit offset for the c+1 class and learn a temperature" would help position U2C relative to the simplest possible learned alternatives.
- The quadrant-of-knowledge discussion (Section 4) is conceptually interesting but could be strengthened by connecting it quantitatively to the decision regions in Lemma 5.1 or to empirical results.

## Removed Points

The following points from the reviews were removed or downgraded:

- **"The theoretical analysis does not deliver new insight"** → downgraded to Minor (point 5 above). The critic's characterization of Lemma 5.1 as a "tautology" is overly harsh — the decomposition does provide a framework for thinking about when U2C helps. However, the criticism is partly valid: the lemma is more notational than analytic. Lemma 5.2 is genuinely non-trivial.

- **"The paper contrasts RC and U2C on the basis that RC's softmax vector uses hard indicator functions... the comparison is fair only under the paper's choice to force RC into a probabilistic format"** → removed. The paper's evaluation uses probabilistic metrics (ECE, NLL) that require probabilistic outputs. Characterizing RC's implicit probabilistic output (hard 0/1 for the c+1 class) is a fair analysis of its properties under the chosen evaluation framework. The paper is transparent about this construction.

- **"The discussion of unknown-unknowns... remains disconnected from the technical contribution"** → removed to Nice-to-Haves. The quadrant discussion is conceptual framing, not a technical claim, and does not affect the paper's core contribution.

- **"In its current form the paper cannot be accepted because the method is not reproducible"** → This assessment is noted in the Major weaknesses but tempered: the core idea (soft combination via a learned τ_u) is clear, and the missing specification is a well-defined gap that could be resolved. The contribution is not fatally flawed.

## Novel Insights

None beyond the paper's own contributions. The reviews identify gaps but do not add a new synthesis or perspective that goes beyond what the authors provide.

## Suggestions

1. **Specify τ_u explicitly in the main text** — state the function class (e.g., a two-layer MLP with ReLU, 32 hidden units, no skip connections) and training procedure (learning rate, optimizer, number of epochs, any regularization). This is the single most important revision.
2. **Drop or substantiate the SOTA claim** — either remove "state-of-the-art" from the abstract and introduction, or add comparisons to alternative (c+1)-class uncertainty methods (e.g., posterior networks, ensembles with abstention, training with an OOD background class).
3. **Add a sensitivity experiment for α** showing err/ECE across a range (0.90–0.99) for at least one benchmark and one epistemic estimator.
4. **Add variability estimates** — either multiple random seeds for training the base network, or bootstrap resampling of the validation split, with standard deviations or confidence intervals.
5. **Report NLL results** in Table 1 or a supplementary table to directly validate Lemma 5.2.

## Score and Decision

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>