Now I have a thorough understanding of the paper and all the reviewer claims. Let me draft the consolidated review.

---

## Summary

This paper proposes INR-Bayes, a Bayesian variational-EM framework for joint sparse-view CT reconstruction using implicit neural representations (INRs). Unlike prior joint-INR methods (FedAvg, MAML, INRWild) that use shared information primarily to accelerate convergence, INR-Bayes introduces latent variables (mean and variance) that capture common weight patterns across objects and actively regularize individual reconstructions via a KL divergence term. Experiments on six datasets (four CT, one 4DCT, one natural image) show consistent improvements in PSNR/SSIM, robustness to overfitting under extended training and noisy measurements, and generalization to unseen subjects.

## Strengths

- **Principled Bayesian framework with adaptive regularization.** The variational-EM formulation (Section 4) introduces latent variables ω, σ that capture population-level weight statistics. The KL divergence in the E-step creates a self-adjusting regularization: weight elements with larger learned σ are less regularized, while those with smaller σ are pulled toward the shared mean. This is a clean, principled mechanism that differs qualitatively from the averaging (FedAvg) or meta-initialization (MAML) strategies used in prior joint-INR work. The closed-form M-step (Eq. 8) is efficient and theoretically grounded.

- **Consistent and substantial empirical gains.** Across all six noiseless settings in Table 1, INR-Bayes achieves the highest PSNR (e.g., Inter-walnut 36.13 vs. next-best MAML 35.66; Intra-lung 33.90 vs. MAML 33.26; Inter-Faces 31.31 vs. next-best LLT-TV 30.09). Under noisy measurements (Table 2), the advantage widens substantially (Noisy Walnut 30.13 vs. next-best RegLLT-TV 28.51). The method is evaluated on diverse datasets (walnuts, aluminum alloy, lung CT, 4DCT, faces) and multiple experimental configurations (intra-object, inter-object, varying angles, varying number of nodes).

- **Demonstrated robustness to overfitting.** A well-known challenge in iterative CT reconstruction is that performance peaks early then degrades. The paper extends training to 60K iterations (Figure 4) and shows that baselines (SingleINR, MAML, FedAvg) deteriorate while INR-Bayes plateaus stably. Under noisy measurements (Figure 5), all methods reach similar peak PSNR but baselines rapidly collapse due to overfitting while INR-Bayes maintains quality. This robustness is practically significant because optimal stopping criteria are hard to determine without ground truth (Figure 6).

- **Generalization to unseen subjects.** The learned prior (latent variables) transfers to new patients without update (Table 3), achieving 31.31 PSNR vs. MAML 30.42 and SingleINR 30.22. The method also benefits from more joint nodes (Figure 7), suggesting the prior improves with more data.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Iteration budget allocation for meta-learning baselines.** The paper gives all INR methods a fixed total of 30K iterations, but MAML uses the first 10K (FedAvg the first 20K) for meta-initialization, leaving fewer iterations for per-object adaptation. This design conflates the method's inherent quality with the number of adaptation steps. While an equal-total-budget comparison is a defensible standard choice, the paper's central claim that INR-Bayes achieves "higher reconstruction quality" could be affected if MAML or FedAvg were allowed more adaptation iterations after meta-training. The authors should either add experiments that equalize adaptation iterations (at the cost of unequal total compute) or explicitly justify why the current allocation is the most informative comparison.

- **No multiple random seeds for main results.** The paper reports mean and standard error computed over reconstructed images (across different objects/slices) but does not state whether results come from a single training run or multiple seeds. Neural network training with variational approximations and MC sampling can exhibit variance. Without evidence that the observed PSNR improvements (~0.5–1.5 dB over the next-best method) are statistically significant across seeds, confidence in the precise numerical margins is reduced. The standard errors reported over images provide some confidence, but multi-seed results would strengthen the claim.

- **Limited discussion of the conditional independence assumption.** The paper assumes conditional independence across objects to enable parallel computation (Section 4), but does not discuss what kinds of shared structure (e.g., common edges, background) might be lost by this assumption or when it could hurt performance (e.g., very dissimilar objects). Acknowledging this boundary would improve the paper's honesty and guide future work.

- **CelebA forward model unspecified.** The paper evaluates on CelebA as a natural-image domain but never explains how CT projections are simulated from face images (e.g., are images treated as 2D attenuation maps and forward-projected?). A brief sentence in the experimental setup would clarify this.

### Trivial

- **Table 1 caption slightly overstates consistency.** The caption reads "consistently showing that INR-Bayes outperforms other methods" while RegLLT-TV actually achieves the best SSIM on CelebA (0.858 vs. 0.847). The paper text does acknowledge this exception, but the caption would benefit from a qualifier like "with one exception noted in the text."

- **Minor presentational issues.** The paper could clarify the connection between FedAvg and Reptile in Section 3.1, and briefly explain why the INRWild static/transient decomposition is ill-suited for CT (multiple distinct objects vs. one scene with occlusions). These are small clarifications.

## Nice-to-Haves

- **Ablation on EM cycles (R).** The paper fixes the number of EM cycles but does not show how reconstruction quality varies with R. A plot demonstrating that the method converges and is not sensitive to this hyperparameter would strengthen the practical claims.

- **Sensitivity analysis for β (KL weight).** The paper states β is tuned on a subset but does not show performance across a range of β values on any dataset. Demonstrating robustness to this hyperparameter would strengthen the claim that the framework is principled.

- **Quantitative analysis of learned σ.** The paper claims that weight elements with larger σ are less regularized. A histogram or visualization of learned σ values across layers, related to object properties, would make this "self-adjusting regularization" claim more concrete.

- **Additional noisy training curves.** The noisy overfitting demonstration (Figure 5) is shown on WalnutCT only. Adding curves for LungCT noisy or AluminumCT noisy would further substantiate the claim.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Criticism that the abstract's claim about current techniques not being tailored for reconstruction quality is "accurate only after the paper's experiments."** This is a standard convention for research papers — claims in the abstract are expected to be supported by the paper's content. This is not a valid weakness.

- **Criticism that novelty is "moderate" because the method applies standard variational EM.** The critic acknowledges this "does not invalidate the contribution." The paper's contribution is the application of this framework to the novel problem of INR-based joint CT reconstruction, with demonstrated practical benefits. Framing assessments are subjective and this point adds no actionable criticism.

- **Criticism that "only one noisy dataset is shown for training curves."** The paper shows noisy training curves on WalnutCT (Figure 5), noiseless training curves on LungCT (Figure 4), and noisy peak-performance results across four datasets (Table 2). The single-curve presentation is standard for visual clarity; the broader noisy evaluation is already comprehensive.

- **Request for "multiple seeds (≥3) for at least the four main datasets."** This is already noted in Minor above. The expanded version here is redundant.

## Novel Insights

The reviews collectively surface an interesting tension: the paper's main strength — a principled Bayesian framework with adaptive regularization — is also the source of its most subtle experimental concern. The KL divergence term that prevents overfitting is parameterized by a learned variance that adapts per weight element, which is genuinely novel in the joint-INR context. Yet the same training budget used to learn this prior could also be seen as giving the method an advantage over meta-learning baselines that must split their budget between meta-training and adaptation. The deeper insight is that INR-Bayes does not need to "spend" iterations on a separate meta-phase because the latent variables are updated jointly with individual networks via EM cycles — the regularization is a side effect of training, not a separate stage. This architectural property, not just the total iteration count, is what drives the advantage. The paper would benefit from making this contrast explicit.

## Suggestions

1. **Address the iteration budget concern** by either: (a) running an additional experiment where MAML and FedAvg are given enough total iterations so that they have 30K adaptation steps (i.e., 40K total for MAML, 50K for FedAvg), or (b) providing a clear justification for why the current split is the most informative comparison and noting that the equal-total-budget design follows standard practice.

2. **Report results from at least 3 random seeds** for the main datasets (or a representative subset like Inter-walnut and Inter-lung) to establish statistical significance across initializations.

3. **Add a brief sentence** in the experimental setup explaining how CT projections are simulated from the CelebA face images.

4. **Add a limitations paragraph** discussing when the conditional independence assumption might break down (e.g., objects from very different anatomical regions or imaging modalities).

5. **Soften the Table 1 caption** to acknowledge the CelebA SSIM exception explicitly.

## Score and Decision

The paper makes a solid contribution to INR-based CT reconstruction. The Bayesian framework is principled, the experiments are extensive (six datasets, multiple configurations, overfitting and generalization studies), and the results consistently favor the proposed method. The two main concerns — iteration budget allocation for meta-learning baselines and the absence of multi-seed statistics — are real but do not undermine the central claim that INR-Bayes provides meaningful robustness and improved reconstruction quality. These are addressable in revision. The paper is largely sound and the weaknesses are fixable.

MY FINAL SCORE: <pineapple>3.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>