- Decision: Reject
- Avg Score: 3.50
- Scores: 3, 5, 3, 3
Now I have a thorough understanding of both the paper and the reviewer claims. Let me produce the final consolidated review.

---

## Summary

This paper proposes a method for unlearning unwanted data from a matrix factorization-based recommendation model. The approach works by training a small "rescue model" (m2) on a corrected version of the unwanted data (with noisy ratings replaced by item averages) and then fusing the latent features of the faulty serving model (m1) and the rescue model through a Convolution Fusion Function (CFF). The goal is to produce a final model free of the unwanted patterns without retraining from scratch. The method is evaluated on MovieLens 100K and 1M datasets against SISA and full retraining baselines.

## Strengths

- **Avoids full retraining.** The method explicitly avoids training a new model from scratch on the full remaining dataset. Only a small "rescue model" is trained on the subset of data to unlearn, and the rest is feature-level fusion. This is a practically motivated design goal clearly stated in the contributions. (§4.3.4, §7)

- **Empirical evidence that fused features approach original features.** Table 2b reports Euclidean distances showing that the CFF-fused latent features are closer to the original model's features than to the faulty model's features (ℓ₂ < ℓ₁). This provides some internal validation that the fusion mechanism works as intended. (§6)

- **Systematic analysis of unlearning data size.** The ablation study (Figure 3) examines how varying the fraction of data to be forgotten (up to 50% of user data) affects RMSE, providing practical guidance about the method's tolerance to increasing unlearning demands. (§5.4)

- **Addresses a relatively underexplored area.** Unlearning for matrix factorization recommendation models specifically is less explored than unlearning for classification models. The paper targets this gap. (§1, Abstract)

## Weaknesses

### Fatal

None.

### Major

- **Evaluation setup simulates denoising, not realistic unlearning.** The paper constructs a scenario where a clean model (*m_orig*) is trained, noise (ratings set to 5) is artificially injected into selected entries to create a "faulty" model (*m1*), and the task is to recover a model close to *m_orig*. This is a denoising task. In realistic unlearning (e.g., GDPR-based forget requests), the unwanted data was genuine user interactions that are now deemed undesirable — there is no pristine reference model to compare against, and the model's parameters already entangle the unwanted data with everything else. The entire evaluation framework depends on having *m_orig* as ground truth, which does not exist in practice. (§4.3.1, §4.2, §6)

- **No comparison against recommendation-specific unlearning baselines.** The paper cites Chen et al. (2022) and Zhang et al. (2023) as related work on recommendation unlearning (including the Influence Function-based IFRU) but does not compare against them experimentally. Only SISA (a general-purpose method) and retraining are used as baselines. Without comparison to methods actually designed for recommendation models, the claim of outperforming "state-of-the-art" is unsupported. (§2.1, §5.3, Table 2a)

- **The unlearned model outperforms the original model, which is conceptually problematic.** The paper explicitly states that *M_f* shows "a clear increase in the performance" over *m_orig* for smaller unlearning requests, and that *M_f* maintains "lower or almost equal RMSE than the original MF RMSE." An unlearning method should *match* the performance of retraining on the remaining data, not exceed the original model trained on the full clean dataset. That *M_f* achieves RMSE < 1 while *m_orig* is ~1.1 suggests the fusion process is doing something beyond merely removing the unwanted data — it may be adding regularization or other benefits that conflate the evaluation. The paper does not explain or acknowledge this issue. (§6, line 245; §5.4, line 222)

- **Insufficient verification that unwanted data is actually forgotten.** The evaluation relies entirely on aggregate RMSE and Euclidean distances between latent feature matrices. There is no experiment checking whether the unwanted data's influence on specific predictions is removed (e.g., comparing predicted ratings for the unlearned items before and after, membership inference tests, counterfactual recommendation list analysis, or verification on a held-out set of the unwanted interactions). RMSE alone does not confirm unlearning — a model can achieve good RMSE while still retaining traces of the supposedly forgotten data. (§6, Table 2b, §5.2)

### Minor

- **"Theorem 1" is not a theorem.** Section 4.2 labels *"The convolution Fusion Function generates a fading effect"* as Theorem 1, but the "proof" is purely descriptive and empirical (referring to Table 2b). There is no formal argument, derivation, or mathematical proof. This is a mislabeling. (§4.2, lines 85–114)

- **Problem formulation notation is unclear and inconsistent.** Equation 1 uses symbols *D_α*, *D_γ*, and *CT* that are not clearly defined. The surrounding text refers to "T is a function" but the equation uses *CT*. The formulation does not clearly connect to the subsequent method. (§4.2, lines 77–84)

- **No statistical significance or variance reported.** All results are presented as point estimates without standard deviations, confidence intervals, or multiple trials. This makes it impossible to assess the reliability or variability of the reported improvements. (§5, Table 2a, Table 3)

- **CFF architecture details are sparse.** The CFF is described only as having "two convolution layers and two fully connected layers" with no kernel sizes, number of filters, activation functions, loss function, optimizer, learning rate, training data split, or number of epochs. This significantly limits reproducibility. (§4.3.3, Algorithm 1 description)

- **The "first work" claim is overstated.** The paper states "this is the first work that unlearns from the pretrained model using only the specified data to unlearn" while citing Chen et al. (2022) and Zhang et al. (2023) as prior work on recommendation unlearning. Though the specific methodological approach may differ, the broad novelty claim is imprecise. (§1, line 20; §2.1)

### Trivial

- **Missing parentheses and broken LaTeX in several places.** For example, "Table $\perp$" instead of a proper reference, "Eq. $\bigstar$" as a placeholder, and incomplete/broken equations. These are formatting artifacts from PDF extraction but should be checked in the original submission.

## Nice-to-Haves

- **Ablate the CFF component.** The paper claims CFF is essential but provides no experiment without it (e.g., simple averaging of latent features, or using m2 directly). Such an ablation would strengthen the contribution claim. (§4.3.3, §5.4)
- **Report computational cost.** The paper motivates the work by avoiding expensive retraining but never measures training time, inference cost, or efficiency relative to baselines. (§1, §7)
- **Add membership inference or counterfactual evaluation** to verify that the unwanted data's influence is actually removed.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"RMSE of 0.2453 is implausible"** (Harsh Critic point #2): This specific numerical value (0.2453) does not appear in the paper's text. The reported values are embedded in image tables that are not readable as text, so this claim cannot be verified from the available content. Removed for lack of verifiability.
- **"0.8660 vs 1.1005 on ML-100K"** (Harsh Critic point #2, continuation): Same issue — the specific number is not found in the paper's text. Removed.
- **"The method requires more data than retraining"** (Harsh Critic point #5): The paper's claim is that the method avoids training on the *full remaining dataset*. The rescue model m2 is trained only on the (small) subset of data to unlearn. This is a valid efficiency claim, as m2 processes only the unwanted data, not the full dataset minus the unwanted portion. The critic's claim that "more data than retraining" is needed conflates the training data of m2 (small) with the full pipeline's data requirements. Weakened and removed.
- **"The scenario is fundamentally mismatched"** (Harsh Critic point #5): The core of this point is already covered in the Major weakness about the evaluation setup simulating denoising rather than realistic unlearning. The claim about "more data than retraining" is separated and addressed above.
- **Strength: "Outperforms the SISA state-of-the-art baseline"** — The evidence supports that the proposed method achieves lower RMSE than SISA on the tested configuration. However, this strength is partly undermined by the fact that SISA is a general-purpose method not designed for MF collaborative filtering, and no recommendation-specific baselines are compared. Kept in modified form in the Strengths section; the quantitative comparison is acknowledged.
- **Several generic formatting/style nitpicks** (typos, "missing appendix," "section references wrong") removed as parser artifacts or non-substantive.

## Novel Insights

None beyond the paper's own contributions. The harsh critic and strength finder largely recapitulate the paper's claims and limitations without identifying a fundamentally new perspective. The key observation — that an "unlearning" method should not outperform the original clean model — is an important check on the paper's evaluation logic but is an obvious conceptual consistency test rather than a novel insight.

## Suggestions

1. **Reformulate the evaluation for realistic unlearning.** Train a model on the full dataset, designate a subset as "unwanted," define the ground-truth model as one retrained on the remaining data, and evaluate whether the proposed method produces a model behaviorally equivalent to the ground-truth (not just in RMSE but in per-user recommendation lists and membership inference).

2. **Compare against recommendation-specific baselines** (e.g., IFRU from Zhang et al. 2023, or the erasable framework from Chen et al. 2022) that the paper already cites.

3. **Provide full CFF architecture details** (kernel sizes, activations, loss function, optimizer, training procedure) and release code to enable reproducibility.

4. **Acknowledge and explain** why the proposed method sometimes achieves *better* RMSE than the original clean model, or restructure the evaluation to avoid this confound.

5. **Report variance** across multiple random seeds for all experimental results.

6. **Add direct verification of unlearning** — e.g., measure whether predicted ratings for the unlearned items revert to values consistent with a model that never saw those interactions.
