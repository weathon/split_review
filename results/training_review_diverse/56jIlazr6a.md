Now I have all the information needed to verify each claim against the paper. Let me construct the final consolidated review.

---

## Summary

This paper proposes Unified Uncertainty Calibration (U2C), a framework that replaces the hard thresholding of reject-or-classify (RC) with a learned non-linear calibration function that integrates epistemic uncertainty into a single softmax over \(c+1\) classes (including an OOD rejection class). The core idea is well-motivated: RC's binary accept/reject decisions cannot communicate aleatoric and epistemic uncertainty, produce miscalibrated predictions, and cannot correct misspecified uncertainty estimates. U2C addresses these through soft integration and non-linear calibration of epistemic uncertainty.

## Strengths

- **Principled unified calibration framework**: U2C replaces RC's binary thresholding with a learned non-linear function \(\tau_u\) that maps epistemic uncertainty into the logit space, enabling the softmax over \(c+1\) classes to jointly model aleatoric and epistemic uncertainty (Section 4, Equation 8). This is a non-trivial departure from prior work and is clearly motivated by three concrete problems with RC.

- **Theoretical characterization of error regimes**: Lemma 5.1 decomposes the error difference between RC and U2C into four regions \((A,B,C,D)\) of the max-logit/epistemic-uncertainty plane, providing insight into when each method wins (e.g., U2C excels when out-distribution mass falls in region \(B\), where aleatoric uncertainty is high but epistemic uncertainty is low). Lemma 5.2 identifies the NLL pathology of RC (infinite NLL when any in-domain mass falls in the reject region or any out-domain mass in the accept region) and shows U2C avoids it through soft probabilities.

- **Broad and systematic evaluation across multiple uncertainty estimators**: Experiments span four benchmark categories (in-domain, covariate shift, near-OOD, far-OOD) and four diverse epistemic uncertainty estimators (MaxLogit, ASH, Mahalanobis, KNN) drawn from the OpenOOD survey, reducing cherry-picking concerns. Results are reported on standard benchmarks including ImageNet, ImageNet-C, ImageNet-R, NINCO, SSB-Hard, iNaturalist, Texture, and OpenImage-O.

## Weaknesses

### Fatal
None.

### Major

- **Non-standard ECE definition with no estimation procedure specified**: Equation (2) defines ECE as \(\mathbb{E}_{(x,y)\sim P}\,\mathbb{E}_{p\sim U[0,1]}[\,|\Pr(h_{f^\star}(x)=y \mid \pi_{f^\star}(x)=p) - p|\,]\). This deviates from the standard binning-based ECE (Guo et al., 2017; Kumar et al., 2019) in two ways: the inner expectation averages uniformly over \(p\sim U[0,1]\) rather than over the data distribution of \(\pi\), and it treats \(\Pr(h=y \mid \pi=p)\) as a continuous function that is not directly estimable from finite samples without smoothing. The paper provides no explanation of how this quantity is estimated from data, nor any justification for choosing this definition over the standard alternative. Since calibration is one of the paper's two main evaluation metrics, the validity of all calibration claims hinges on this definition being correctly operationalized. This is a methodological gap that makes the reported ECE values difficult to interpret or compare with prior work.

- **Theoretical lemmas presented as formal results without proof or derivation**: Section 5 labels Lemma 5.1 and Lemma 5.2 as formal results, but the paper provides no proof, proof sketch, or derivation for either. There is no reference to supplementary material or an appendix. The lemmas are essentially error decompositions into region masses — they yield qualitative insight (e.g., "U2C wins when \(P^{\text{out}}(B) > P^{\text{out}}(C)\)") but do not constitute actionable guarantees or provable conditions under which U2C is strictly better. The "Lemma" label sets an expectation of rigor that is not met.

### Minor

- **Functional form of \(\tau_u\) never specified**: Section 4 states "learn a non-linear epistemic calibration function \(\tau_u : \mathbb{R} \to \mathbb{R}\) by minimizing the cross-entropy on the relabeled validation set" but never describes the function class (e.g., is it an MLP? a kernel regressor? a spline?), the optimization procedure, or any regularization. Without this, U2C cannot be reproduced or compared against.

- **Base classifier architecture and training details absent**: The paper does not specify the architecture used for the main experimental results in Table 1. ResNet152 and ViT-32-B are mentioned in passing as alternative architectures for "additional experiments," but the primary backbone is never named. Essential training details (pretrained or trained from scratch, optimizer, learning rate, epochs) are missing, harming reproducibility.

- **No ablation study**: U2C has two components: (1) relabeling the 5% most uncertain validation examples as OOD, and (2) learning a non-linear calibration function \(\tau_u\). The paper includes no ablation to disentangle which component drives improvements. The "linear U2C" experiments are mentioned but not presented with numerical results in the main text.

- **No sensitivity analysis for the 0.95 percentile threshold**: The choice to relabel the top 5% most uncertain in-domain validation examples as OOD is a critical design decision. No justification or sensitivity analysis (e.g., 1%, 5%, 10%, 20%) is provided, even though this choice directly affects the quality of the relabeled validation set and the learned \(\tau_u\).

- **Statistical rigor**: Experiments are reported on a single train/validation/test split with no error bars or confidence intervals. While the paper's defense (fixed splits, deterministic pipeline) partially mitigates this concern, the learning of \(\tau_u\) involves optimization that may introduce randomness, and the absence of any statistical quantification means the stability of reported improvements cannot be assessed. The breadth of benchmarks and estimators partially compensates, but the lack of error bars is a limitation.

### Trivial
None.

## Nice-to-Haves

- **Additional baselines**: The paper compares only U2C against RC. Including methods that directly calibrate OOD scores or use risk-minimization approaches to abstention could better contextualize the improvements. This is not a required comparison given the paper's stated scope, but would strengthen the evaluation.

- **Computational cost comparison**: U2C requires an additional optimization step (learning \(\tau_u\)) that RC does not. A brief discussion of the computational overhead would be useful.

- **Limitations paragraph**: The paper lacks an explicit limitations section. Important limitations include reliance on a validation set from the in-domain distribution (may be unavailable in some settings) and sensitivity to the quality of the epistemic uncertainty estimator \(u\).

## Removed Points

These points are flagged to be removed, treat them with caution:

1. **"Typesetting errors (missing parentheses, misplaced indices) in lemmas indicate lack of care"** — The formulas appear to contain minor formatting artifacts that are likely parser errors from PDF extraction, not errors in the original submission. Removed per hard rule on parser artifacts.

2. **"Auxiliary experiments (linear U2C, ResNet152, ViT-32-B) are mentioned but not presented"** — The paper states "1 shows additional experiments on linear U2C...as well as other neural network architectures." The bare numeral "1" likely refers to a figure or table in the supplementary material that was stripped by the PDF parser. Removed per hard rule on parser-stripped appendix content.

3. **"Only compares RC vs U2C, missing other baselines"** — The paper's contribution is specifically about replacing RC; comparing only against RC is within its stated scope. Demanding additional baselines is a nice-to-have wishlist item, not a weakness. The comparison with the primary foil is thorough across 4 estimators × ~8 benchmarks.

4. **"No error bars — single split" treated as Critical/Fatal** — While the lack of statistical quantification is a limitation, the paper follows the common practice in OOD detection evaluation (consistent with OpenOOD methodology), evaluates across four diverse uncertainty estimators and multiple benchmark types, and the results are broadly consistent. The paper's defense about fixed splits is partially valid. Downgraded from Critical to Minor.

## Novel Insights

The key novel insight from the reviews is the non-standard ECE definition. The paper's equation (2) defines ECE with an inner expectation over \(p\sim U[0,1]\), which is structurally different from the standard binning ECE used throughout the calibration literature. If the paper actually estimated ECE using this definition (rather than using standard binning as an implementation proxy), the calibration numbers may not be comparable to prior work. This is a potentially significant issue that the authors did not flag.

## Suggestions

1. **Clarify the ECE estimation procedure**: State explicitly how Equation (2) is estimated from finite samples. If standard binning ECE is used as the estimator, say so. Consider reporting both the proposed and standard binning ECE to allow comparison with prior work.

2. **Specify the functional form of \(\tau_u\)**: Describe the function class, optimization details (learning rate, number of epochs, optimizer), and any regularization used. A single sentence would suffice.

3. **State the base classifier architecture and training procedure used for the main experiments** in Table 1. Provide the pretraining source if applicable.

4. **Add an ablation study** comparing full U2C against: (a) U2C with linear \(\tau_u\) (to isolate the value of non-linear calibration), and (b) U2C without the relabeling step (to isolate the value of the OOD relabeling).

5. **Provide sensitivity analysis for the 0.95 percentile threshold** used to relabel validation examples (e.g., 1%, 5%, 10%).

6. **Add error bars** from at least 3–5 runs with different random seeds for a representative subset of benchmarks/estimators. If computational constraints prevent full replication, provide bootstrapped confidence intervals on the fixed split.

## Score and Decision

The core idea is novel, well-motivated, and addresses a genuine limitation of current practice. The evaluation is broad in terms of benchmarks and uncertainty estimators. However, the paper has two major issues that undermine its core empirical claims: (1) the ECE metric is defined in a non-standard way with no explanation of how it is estimated from finite data, making all calibration results difficult to interpret; and (2) the theoretical lemmas are labeled as formal results without any proof or derivation. Additionally, key implementation details (the functional form of \(\tau_u\), the base classifier architecture) are missing, preventing reproduction. These problems are fixable but in the current form significantly weaken the paper's contribution.

Given the importance of the calibration metric to the paper's claims and the lack of clarity around both its definition and the method specification, I lean toward rejection with a clear revision path.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>