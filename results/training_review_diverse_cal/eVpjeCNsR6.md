I've thoroughly verified all claims against the paper text. Here is the final consolidated review:

---

## Summary

This paper introduces EraseDiff, an unlearning method for diffusion models that replaces the ground-truth noise target with uniform noise on forgetting data while fine-tuning on remaining data. The core idea — training the model to predict uniform noise instead of the true Gaussian noise for samples to be forgotten — is simple and practical. Experiments on CIFAR10, UTKFace, CelebA, and CelebA-HQ with both conditional (DDIM) and unconditional (DDPM) diffusion models show effective class/attribute removal while preserving utility on remaining data, with substantial computational savings (~10 minutes vs ~27 hours for retraining).

## Strengths

- **Simple and effective forgetting mechanism**: Replacing the denoising target with uniform noise samples (Eq. 5) is an elegant operationalization of the forgetting objective. The paper correctly identifies that any distribution differing from the true Gaussian noise accomplishes the goal, and picks uniform noise for its simplicity (no extra hyperparameters). This is conceptually cleaner than gradient ascent (NegGrad).

- **Strong empirical evidence for conditional class/attribute removal**: Tables 1–3 provide quantitative results on CIFAR10 and UTKFace. Forgetting-class FID scores jump from ~19 to ~256 (birds on CIFAR10), and classifier accuracy on generated forgetting-class images drops to 0.002 (CIFAR10) and 0 (UTKFace). These are unambiguous signals of effective unlearning.

- **Demonstrated preservation of utility on remaining data**: Remaining-class FID increases only modestly (3.64 → 7.89 on CIFAR10, Table 2) and the paper qualitatively validates this with visualizations (Figure 2). The weight distance to the retrained model (1.3534 vs. theoretical minimum 1.3533, Table 3) provides additional corroboration.

- **Substantial computational efficiency**: The complexity analysis (Section 5.4) and empirical timing (~10 minutes vs. ~27 hours retraining, ~32 hours for full training) make a strong case for practical deployability, directly answering RQ3.

- **Outperformance over state-of-the-art baselines**: Table 3 and Figure 4 show that both NegGrad and BlindSpot either fail to scrub (Fi-neTune, Unscrubbed) or destroy utility on remaining data (FID > 200 for NegGrad and BlindSpot on remaining classes). EraseDiff is the only method that simultaneously achieves high forgetting-class FID (268.11) and reasonable remaining-class FID (68.52).

## Weaknesses

### Fatal

None.

### Major

- **The bi-level optimization framing is over-complicated relative to the actual algorithm.** The paper formulates the problem as a bi-level optimization (Section 3.2) where the outer objective preserves utility and the inner objective erases forgetting data. However, the inner objective \(f(\phi, \mathcal{D}_f)\) does not intrinsically depend on the outer variable \(\theta\) — the coupling is introduced artificially through initialization (\(\phi^0 = \theta\)). The final update (Eq. 9) reduces to a weighted sum of two gradients: \(\nabla_\theta \mathcal{F}(\theta, \mathcal{D}_{rs}) + \lambda \nabla_\theta \hat{f}(\theta, \mathcal{D}_f)\). This is effectively multi-objective fine-tuning, not a genuine bi-level solution where the inner problem's solution explicitly shapes the outer problem. The bi-level formalism does not add algorithmic value and obscures the simplicity of what is otherwise a clean, practical method. The logical chain from "maximize NLL" (Eq. 3) to "minimize \(\|\hat{\epsilon} - \epsilon_\theta\|^2\) with \(\hat{\epsilon}\sim\mathcal{U}\)" (Eq. 5) is present in the text but could be much clearer — specifically, the replacement of \(\epsilon\) with \(\hat{\epsilon}\sim\mathcal{U}(0,1)\) is presented as a trick rather than a derived consequence of the NLL maximization goal.

### Minor

- **MIA evaluation relies solely on loss histograms without reporting quantitative accuracy.** The paper trains a binary classifier for membership inference (Section 5.2, Figure 1) but never reports its classification accuracy or AUC. The loss distribution overlap is visually suggestive but not a standard MIA metric. While the paper correctly notes that MIA is inherently difficult for diffusion models (generated images already look realistic), reporting the actual attack accuracy would substantially strengthen the claim of successful data scrubbing.

- **KL divergence results (Figure 3) are presented as histograms without numerical values or a precise definition** of how the KL distance is computed (beyond "distance between the approximator's output \(\epsilon_T\) distribution and the standard Gaussian noise \(\epsilon\) distribution"). Without numbers, it is impossible to compare the magnitude of divergence shift across methods or to reproduce the metric.

- **No ablation study on hyperparameters \(\lambda\) and \(K\) in the main paper.** The paper states \(\lambda = 0.1\) by default and mentions it "could also be automatically computed" (line 102), but provides no empirical study of how sensitive the method is to this hyperparameter or to the number of inner gradient steps \(K\). These are the key design choices in the algorithm.

- **The adaptation of the BlindSpot baseline to diffusion models is not specified.** The paper describes BlindSpot's general strategy (partially-trained model + mimicking) but does not explain how "mimicking the behavior" is instantiated for a diffusion model (e.g., what loss function is used for the distillation/mimicking step). This makes the comparison less transparent than it should be.

### Trivial

- **Notation inconsistency**: The paper uses \(\theta\) for the outer objective's parameters, switches to \(\hat{\theta}\) in Eq. (3), then introduces \(\phi\) for the inner objective in Section 3.2 without a clean notational scheme. This creates unnecessary confusion when reading the method section.

- **The gradient notation \(\nabla_\phi \hat{f}(\phi, \mathcal{D}_f)\) in Eq. (9)** is technically correct — the text states "with \(\phi = \theta\)" — but is unnecessarily confusing. Writing \(\nabla_\theta \hat{f}(\theta, \mathcal{D}_f)\) directly would be clearer and would avoid the appearance of a syntax error.

- **Weight distance comparison of 1.3534 vs. 1.3533 (Table 3)** shows precision to four decimal places for what is likely a stochastic optimization result, making the "close alignment" claim seem like an artifact of floating-point arithmetic rather than meaningful evidence.

## Nice-to-Haves

- An ablation study on \(\lambda\) (even at a few values: 0.01, 0.1, 1.0) and \(K\) (e.g., 1, 5, 10) would help users understand the method's robustness.
- Reporting a quantitative MIA accuracy or AUC for EraseDiff and baselines would make the privacy claim more persuasive.
- A simplified presentation that directly presents EraseDiff as multi-objective fine-tuning (utility loss + forgetting loss) rather than bi-level optimization would make the contribution more accessible.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

1. **Missing quantitative unconditional results in the main paper**: The reviewer claims the paper lacks quantitative results for unconditional unlearning (CelebA/CelebA-HQ). However, the paper states these results are in the appendix (line 136: "more results ... in the appendix"). The appendix was stripped by the parser; it existed in the original submission. The main paper does include qualitative unconditional results (Figure 5, Section 5.6) on Hugging Face unconditional DDPMs. Per the hard rule, weaknesses about missing appendix content are removed.

2. **Gradient update is "syntactically wrong"**: The reviewer claims Eq. (9)'s \(\nabla_\phi \hat{f}(\phi, \mathcal{D}_f)\) while updating \(\theta\) is incorrect. The paper explicitly states "with \(\phi = \theta\)" before Eq. (9). \(\nabla_\phi \hat{f}(\phi, \mathcal{D}_f)\) evaluated at \(\phi = \theta\) is mathematically equivalent to \(\nabla_\theta \hat{f}(\theta, \mathcal{D}_f)\). This is standard notation in optimization papers that distinguish the function's formal parameter from the evaluation point. The notation is confusing but not wrong. The criticism is factually incorrect.

## Novel Insights

The reviewer's central insight that the bi-level framing is decorative — the algorithm is effectively multi-objective fine-tuning — is legitimate and identifies a mismatch between the paper's claimed formalism and its actual machinery. However, this does not diminish the empirical effectiveness of the method, which is driven by the simple and well-chosen uniform-noise forgetting target. The most valuable takeaway from the review process is that the paper's genuine contribution (the forgetting loss design) would be better served by a more direct presentation.

## Suggestions

1. Restructure Section 3 to present the method directly as multi-objective fine-tuning: minimize \(\mathcal{F}(\theta, \mathcal{D}_r) + \lambda f(\theta, \mathcal{D}_f)\) where \(f\) uses the uniform-noise target. Drop or significantly de-emphasize the bi-level formalism, which adds complexity without explanatory or algorithmic value.
2. Report MIA accuracy (and AUC, if feasible) numerically in the main paper, even if only to show that MIA is near-chance after unlearning.
3. Provide a precise definition of the KL divergence metric used in Figure 3 and include numerical KL values in a table.
4. Add a brief ablation study on \(\lambda\) (at minimum) in the main paper or appendix.

## Score and Decision

**Originality**: Good — the uniform-noise forgetting target is a novel and practical contribution to diffusion model unlearning.

**Importance of research question**: High — data privacy and the "right to be forgotten" are timely and practically important concerns for generative models.

**Claims support**: Generally well-supported for conditional settings. The MIA and KL evidence are weaker but the FID/accuracy results carry the main claims.

**Soundness of experiments**: Solid for conditional models. The unconditional evaluation relies on qualitative results (Figure 5) in the main paper, with quantitative results in the appendix.

**Clarity of writing**: Adequate but the bi-level framing obscures the method's simplicity. Notation could be cleaner.

**Value to community**: The method is simple, effective, and easy to implement. The code release increases its practical value.

The paper has a genuine, well-executed contribution despite the over-engineered framing and some minor evaluation gaps. None of the verified weaknesses are fatal — they concern presentation, framing, and evaluation depth rather than validity of the core claims.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>