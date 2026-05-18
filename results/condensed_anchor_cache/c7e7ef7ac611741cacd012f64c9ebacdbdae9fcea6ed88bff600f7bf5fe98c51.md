- Decision: Reject
- Scores: 5, 5, 3, 3, 3

## Merged Review

### Summary
The paper proposes Dual Corruption Denoising AutoEncoders (DC-DAE), a method for missing data imputation that augments inputs via concurrent masking and additive noise during training, combined with a balanced loss function to trade off reconstructing artificial missingness versus denoising observed values. The approach is tested on five tabular datasets (Breast, Letter, Shuttle, Glass, Spam) and compared with GAN, DAE, VAE, and other deep learning baselines. Reviewers are split: two rate 5 (positive, see value in the combination and clear presentation), three rate 3 (concerned about limited novelty, insufficient evaluation, and marginal empirical gains). All agree the writing is clear and the architecture is simple.

### Strengths
- Effective for missing data imputation in tabular datasets; achieves state-of-the-art NRMSE on Breast, Letter, and Shuttle datasets across various missing rates (R1, R2, R3).
- Clear and well-structured writing, easy to follow; good discussion of GAN-based and VAE-based methods (R1, R5).
- Simple, plug-and-play architecture without attention mechanisms or adversarial training; can be combined with other denoising models (R1, R2).
- Dual corruption (masking + additive noise) augments data representation and improves generalization (R2). Reviewer 3 considers the integration of dual noise injection, masking, and a reconfigured loss function to be a novel and original combination; ablation experiments confirm the synergistic benefit of all three components (R3).
- Balanced loss function provides a tunable trade-off between reconstructing artificially-masked entries and denoising observed values (R1, R4).
- Ablation studies reveal incremental gains from cross-attention between data and mask (R3).

### Weaknesses
- **Novelty is limited**: Masking and additive noise are well-established data augmentation techniques; the combination is incremental rather than a breakthrough (R1, R2, R4, R5). The paper lacks theoretical justification for why this specific combination is superior to using either technique alone or other augmentation strategies (R2, R4). One reviewer (R3) disagrees and views the integration as original, but the majority finds the contribution insufficient.
- **Need to differentiate from standard data augmentation**: The method should clarify how it differs from simply applying data augmentation to all models (R1).
- **Experimental evaluation is narrow and incomplete**:
  - Only tabular datasets with small feature numbers are used; no evaluation on complex, large-scale datasets (e.g., images, text) where deep learning excels, limiting generalizability claims (R2, R5).
  - Only NRMSE is reported; missing metrics for real-world downstream tasks (e.g., classification accuracy). A closely related method, DAEMA, also reports classification accuracy (R4, R5).
  - Missing comparisons with traditional machine learning imputation methods (e.g., MICE, KNN, matrix completion) (R5).
  - No standard deviations or confidence intervals in Table 2; statistical significance of NRMSE improvements is questionable, especially given small dataset sizes (R2).
- **Performance is not consistently superior**:
  - DC-DAE outperforms baselines on Breast, Letter, and Shuttle, but on Glass and Spam it is worse than MIWAE, HI-VAE, and MIDA (R3, R5).
  - At high missing rate (β=0.8), DC-DAE’s average NRMSE (0.9732) is slightly higher (worse) than MIWAE (0.9698) (R3).
  - The claim of significantly surpassing other methods may be overstated; advantage is marginal in many cases (R3).
- **Potential unfair comparison**: The Glass dataset NRMSE reported for DAEMA in Table 2 differs from the value in the original DAEMA paper (Table 1). It is unclear whether the same parameters were used for a fair comparison (R4).
- **Balanced loss function lacks sufficient analysis**:
  - No ablation or sensitivity experiments showing how imputation performance varies with the weighting hyperparameters α and β; the choice is unjustified and robustness is unexplored (R3, R4).
  - The regularization introduced by the weighting appears to lack potency; the paper does not explain how the balanced loss addresses inherent biases in reconstruction (R3, R4).
- **Method details and clarity issues**:
  - Notation for noise ε (page 4) should be distinguished from regular text (R1). Clarify that “*” denotes the Hadamard product (R3). Restate definitions of variables M, M̂, X, X̂, and M with a straight-line hat in Section 4.4 (R3).
  - Equation (4): clarify whether noise is added only to observed values and update notation to `ε*(1−M)` (R2).
  - Equation (5) appears incorrect based on the loss function description and Fig. 1 (R5).
  - Equation (6): is it standard for DAEs to pass the mask matrix as input? Is the artificial mask intended to help the model distinguish real vs. synthetic missingness? (R2).
  - Section 5.6.1 explanation is unclear: why different sample sizes are used, what the numbers in the table mean; analysis is not comprehensive or quantitative (R1).
  - Figures 2, 3, 4: text and numbers are too small; Figures 3 and 4 should be centered (R1).
  - Citation formatting inconsistency (e.g., [6] in Section 4.3) (R2).
- **Missing clarifications and requested experiments**:
  - How does the model account for distribution shift caused by adding synthetic missing values during training? (R2)
  - When handling MNAR (Appendix A.1), how does the model avoid learning to discriminate between real and artificially-introduced missingness? (R2)
  - Why is the validation method (presumably a single hold-out) chosen instead of multi-fold cross-validation for moderate-sized datasets? (R2)
  - Trade-offs of using overcomplete representations (Section 5.6.3) regarding model complexity and overfitting (R2).
  - In scenarios where GAN components provide incremental gains (Section 5.6.2), under which conditions are they beneficial and how should they be optimized? (R2)
  - Recommend evaluating on more diverse and larger-dimensional datasets (R3, R5).
  - Want to see downstream task performance (e.g., classification accuracy) to assess practical utility beyond NRMSE (R4, R5).