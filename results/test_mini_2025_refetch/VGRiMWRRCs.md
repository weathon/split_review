Now I have enough calibration data. Let me compile the final review.

**Round 1 bracket**: Between 4 and 6.5 — the paper is clearly not in the strong (>7.5) range (those have well-supported claims and thorough experiments), nor in the weak (<3.5) range (which includes papers with vague or unsupported claims and poor experiments).

**Round 2 narrowing**: The paper is weaker than the accepted 6.67 paper ("Learning model uncertainty as variance-minimizing instance weights" — accepted poster with extensive experiments and clear framing) and comparable to the 5.0 paper ("Removing Spurious Concepts" — rejected, had issues connecting theory to method, similar experimental scope). The paper under review has a genuine empirical contribution but its central theoretical framework is disconnected from the method and several key claims are unsupported.

**Final score: 5.0** — marginally below the acceptance threshold.

---

## Summary

This paper proposes using evidential epistemic uncertainty from an ERM-trained model to reweight samples during last-layer retraining for group robustness without group labels. The authors also present an Empirical Bayesian framework intended to unify existing group robustness methods. On four of five benchmark datasets (Waterbirds, MultiNLI, Colored MNIST, CivilComments), the proposed method achieves competitive worst-group accuracy among label-free approaches, and on Waterbirds (91.2%) it narrowly outperforms previous label-free methods.

## Strengths

1. **Competitive worst-group accuracy across multiple benchmarks without group labels.** On Waterbirds (91.2%), MultiNLI (74.5%), and CivilComments (69.8%), the method achieves the best or near-best worst-group accuracy among label-free approaches, with standard deviations reported (Table 4, 5). The Waterbirds result is within 0.2% of the oracle Group DRO (91.4%) that uses group annotations.

2. **Computational efficiency via last-layer retraining.** The method retrains only the final layer after evidential ERM, unlike JTT and CnC which require training a new model from scratch (Section 5.4). This is a practical advantage for scalability.

3. **Qualitative evidence linking uncertainty to spurious feature reliance.** GradCAM visualizations on Waterbirds (Figure 2) show high-uncertainty samples attend to background regions while low-uncertainty samples focus on the bird, providing intuitive support for the core design choice. The t-SNE visualization (Figure 1) on Colored MNIST also aligns with the narrative.

4. **Descriptive mapping of existing methods under a common notation.** Table 1 organizes LfF, JTT, CnC, DFR, and SELF in terms of their estimates of p̂(θ) and p̂(g|x,θ), offering a useful comparative perspective even if the unification is not as deep as claimed.

## Weaknesses

### Fatal
None.

### Major

1. **The Empirical Bayesian framework is not connected to the proposed method.** The paper presents a theoretical apparatus (Section 3) culminating in Tweedie's formula (Theorem 3.1) and claims it justifies the method, but the actual method uses neither. The posterior estimate in practice is set to p̂(g|x,θ) = u(x) = K/S(x) (lines 163-171), with no derivation linking this to the EB framework or Tweedie's estimate. Table 1 describes existing methods but does not show they optimize a shared objective. This leaves the framework as a notational overlay rather than a functional contribution. The claimed contribution of a "unified Empirical Bayesian framework" is not supported by the content.

2. **Theorem 3.1 involves differentiating w.r.t. a discrete variable.** The theorem assumes the marginal likelihood p(y|x,θ) is differentiable with respect to y, but y is a discrete class label in the classification setting studied throughout the paper. The derivative ∂/∂y is not defined for discrete y. While the theorem could apply to a latent continuous representation, the paper does not address this gap or show how to bridge it. The theorem therefore does not provide the stated theoretical grounding for the method.

3. **No quantitative evidence that uncertainty values correlate with group membership.** The paper claims "quantitative analysis showed correlations between uncertainty values and true group labels across all datasets" (line 278), but reports zero numerical metrics — no AUC, correlation coefficient, or any other quantitative measure. Since the entire method hinges on using u(x) as a proxy for p̂(g|x,θ), this is a critical evidential gap. The GradCAM and t-SNE visualizations are qualitative and do not substitute for a direct measurement of the uncertainty–group relationship.

4. **The claim of reduced hyperparameter dependence is unsupported.** The paper states the method "reduces reliance on hyperparameter tuning" (abstract, conclusion) but the experimental setup samples ten random hyperparameter configurations and selects the best on validation performance (Section 5.2), which is itself a tuning procedure. No sensitivity analysis, ablation of λ, or plots of performance vs. hyperparameter values are provided. The claim is therefore asserted rather than demonstrated.

### Minor

1. **Baseline numbers are taken from prior work without re-running.** The paper reports results for CVaR DRO, LfF, JTT, CnC, and AFR as cited from Nam et al. (2020b) and Yang et al. (2023). Small implementation differences (learning rate, weight decay, backbone details) can shift results. While this is common practice, the paper does not discuss whether baselines were matched to the same backbone and optimization setup.

2. **LISA (Yao et al., 2022) is mentioned in the introduction as a method that can be interpreted within the framework but is absent from the experimental comparisons.** Including it would strengthen the comparison. CnC results for MultiNLI are also missing (Table 5).

3. **Methodological ambiguity about validation set usage.** Retraining samples are drawn from "the misclassified portion of the training set and the validation set" (line 191). If validation samples are used both for constructing the retraining set and for hyperparameter selection, this risks information leakage and should be clearly scoped.

### Trivial

1. Table 5 header reads "MultiNLQ" instead of "MultiNLI."  
2. Table 5 lists "LIF" instead of "LfF" for the Nam et al. method.  
3. The paper has two different figures numbered "Figure 1" (a t-SNE plot and a MNIST sample figure on different pages).

## Nice-to-Haves

- An ablation separating the effect of the evidential loss from the effect of the uncertainty weighting would clarify what drives the improvement.
- A version using a simpler uncertainty measure (e.g., prediction entropy from a standard ERM model) as a cheaper baseline would strengthen the case for evidential uncertainty specifically.
- Hyperparameter sensitivity plots (e.g., worst-group accuracy vs. λ) would support the claim of reduced tuning.

## Removed Points

The following points raised by the reviewers were removed or demoted:

- **"Below JTT on CivilComments"** (Harsh Critic): The paper reports 69.8% vs. JTT's 69.3%, so the method is above JTT, not below. Factually incorrect.
- **"Far below SELF's 79.1% on CivilComments"**: SELF uses group annotations on the validation set (Val=Yes in Table 5), so this is a comparison with oracle methods, which the paper already separates in its tables. The criticism ignores this distinction.
- **"Missing related works"**: Removed per instructions since I cannot verify what works exist or do not exist.
- **"Appendix/proofs missing"**: The parser strips appendices; the original submission contained Appendix C (experimental details) and Appendix D (proof of Theorem 3.1).
- **Generic concerns about "evaluation lacks rigor"** without specific anchors: Removed as area-of-concern sweep rather than specific identifiable problems.
- **Generic strengths about "the problem is important"** (Strength Finder): Removed as they are generic, not specific to this paper's contribution.
- **Formatting/style nitpicks**: Removed as parser artifacts.

## Novel Insights

None beyond the paper's own contributions. The key insight — that evidential epistemic uncertainty can serve as a reweighting signal for group robustness — is a reasonable extension of existing uncertainty quantification and last-layer retraining ideas, but the reviews do not surface any novel analytical perspective beyond what the paper itself presents.

## Suggestions

1. Either drop the EB framework entirely and present the method as a clean empirical contribution (uncertainty-guided reweighting with last-layer retraining), or properly operationalize the connection by deriving how the evidential uncertainty estimate approximates the EB posterior.
2. Provide quantitative validation of the uncertainty–group relationship: report AUC of u(x) for predicting minority-group membership, or a correlation coefficient against true group labels.
3. Add hyperparameter sensitivity analysis (worst-group accuracy vs. λ and other key hyperparameters) to support the reduced-tuning claim.
4. Re-run or carefully match baseline implementations under identical conditions, or at minimum discuss the sensitivity of comparisons to implementation details.
5. Clarify the validation set usage to rule out information leakage.

## Score and Decision

Round 1 bracket: [4, 6.5] — the paper is not strong enough for the >7.5 band (papers with fully supported claims and thorough experiments) and not weak enough for the <3.5 band (papers with severe or unsupported claims).

**Anchor comparisons (all rounds):**
| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| /home/wg25r/review_agent/human_reviews/7LZjuA4AB2.md | 3.00 | R1 | Weaker: only studies pre-training of spurious correlations, limited contribution |
| /home/wg25r/review_agent/human_reviews/64vO8qoJfb.md | 3.00 | R1 | Weaker: robustness measurement only, no method proposed |
| /home/wg25r/review_agent/human_reviews/bU0JMHJ8zL.md | 2.50 | R1 | Weaker: literature review, no novel method |
| /home/wg25r/review_agent/human_reviews/lEsNGN1SjG.md | 2.00 | R1 | Much weaker: theoretical but unrelated to group robustness |
| /home/wg25r/review_agent/human_reviews/SksPFxRRiJ.md | 5.00 | R1 | Similar: proposed method for spurious correlations, had theory-method disconnect, rejected |
| /home/wg25r/review_agent/human_reviews/W0zgCR6FIE.md | 5.75 | R1 | Different contribution type (benchmark paper), harder to compare |
| /home/wg25r/review_agent/human_reviews/vuvG5rNBra.md | 5.25 | R1 | Lower quality: privacy + spurious correlations, limited experiments |
| /home/wg25r/review_agent/human_reviews/1qzUPE5QDZ.md | 5.25 | R1 | Similar quality: explanation method for distribution shift |
| /home/wg25r/review_agent/human_reviews/bDWXhzZT40.md | 6.67 | R2 | Stronger: accepted poster, similar uncertainty-weighting idea but with more thorough experiments and clearer framing |
| /home/wg25r/review_agent/human_reviews/fxv0FfmDAg.md | 7.33 | R2 | Stronger: accepted spotlight, clear theory, comprehensive experiments |
| /home/wg25r/review_agent/human_reviews/j4gzziSUr0.md | 7.00 | R2 | Stronger: accepted poster, cleaner bi-level optimization for importance weighting |
| /home/wg25r/review_agent/human_reviews/SuH5SdOXpe.md | 7.50 | R2 | Stronger: accepted spotlight, different topic |

The paper is comparable to the 5.0 anchor (SksPFxRRiJ), which had similar issues: a method for spurious correlations with a theory-method disconnect and incomplete experimental validation. The current paper has a slightly stronger empirical showing but shares the same structural weakness of overclaimed theory. It is weaker than the 6.67 poster (bDWXhzZT40), which had more extensive experiments and a clearer connection between its uncertainty method and its framing.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>