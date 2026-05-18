Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

---

## Summary

This paper explores the impact of weight-space symmetries (permutation and scaling) on Bayesian neural network posteriors. It contributes: (1) a theoretical formalism showing how the posterior decomposes into mixtures over permutation and scaling symmetries (Proposition 1); (2) an empirical MMD-based benchmark (Table 1) comparing six posterior approximation methods on three vision tasks, using 1000 SGD-trained checkpoints as the reference distribution; (3) the "min-mass problem" analysis demonstrating that scaling symmetries persist even under L2 regularization; (4) a functional collapse analysis showing low variance in pairwise MI across independently trained models; (5) a protocol for tracking permutation frequency during training; and (6) a planned release of thousands of trained checkpoints.

## Strengths

1. **Novel mathematical formalism for symmetry-aware posterior decomposition**: Proposition 1 formally expresses the Bayesian posterior as a continuous mixture over a discrete mixture of permutation and scaling symmetries, clarifying that permutation symmetries create redundant modes independent of data while scaling symmetries have a more complex, data-dependent effect. This provides a theoretical grounding absent in prior work (e.g., Wiese et al. 2023).

2. **Large-scale MMD-based evaluation of posterior approximation methods**: Table 1 provides a systematic comparison of six methods (Dropout, BNN, SGHMC, SWAG, Laplace, Deep Ensembles) in both single-mode and multi-mode variants across MNIST/OptuNet, CIFAR-100/ResNet-18, and TinyImageNet/ResNet-18. The pattern that multi-mode methods (especially Deep Ensembles) achieve lower MMD and better OOD detection metrics is consistent and informative.

3. **Min-mass problem analysis of scaling symmetries**: Propositions 3.2–3.3 and Figure 2 demonstrate that trained networks (even those with weight decay) do not converge to the minimum-mass configuration under scaling transformations, establishing that scaling symmetries remain active. This challenges the common assumption that L2 regularization eliminates scaling effects.

4. **Empirical demonstration that functional collapse does not occur**: Figure 3 shows that pairwise mutual information between independently trained ResNet-18s has very low variance in-distribution and no significant correlation between ID and OOD MI. This provides concrete evidence against the concern that SGD from different seeds converges to functionally equivalent solutions.

5. **Novel protocol for tracking permutation frequency during training**: Using Kendall's τ on successive sorting permutations (Figure 4), the paper characterizes when weight permutations occur during training — primarily during high-learning-rate phases, stabilizing thereafter.

6. **Checkpoint dataset release**: The paper will release thousands of trained models across architectures and datasets, a practical resource for the community.

## Weaknesses

### Major

1. **The MMD reference distribution (1000 SGD checkpoints) is not justified as a meaningful target for posterior estimation quality.** The paper measures MMD between each approximate method's samples and 1000 independently trained SGD checkpoints (lines 274, 280). While the paper calls this the "estimated posterior" (not the "true posterior"), the framing throughout — title, abstract ("explorations of the posterior distribution of deep Bayesian Neural Networks"), and contribution (2) ("evaluat[ing] the quality of various methods for estimating the posterior distribution") — positions the MMD as measuring *posterior estimation fidelity*. But the 1000 SGD checkpoints are themselves just a collection of point estimates from SGD; they are not samples from a Bayesian posterior (which would require HMC or a proper MCMC procedure). MMD here measures how well each method reproduces the *empirical distribution of SGD solutions*, which is a meaningful object but is not the same as the Bayesian posterior. The paper never acknowledges this distinction or defends why this reference distribution is appropriate for benchmarking posterior quality. The fact that an alternative exists (full-batch HMC on the small-scale OptuNet case, which the paper discusses in related work as feasible for small architectures) makes the omission more significant.

2. **MMD sample-size asymmetry is not discussed or controlled.** The reference distribution uses 1000 checkpoints while each approximate method provides only 100 samples (line 280). MMD is sensitive to sample size differences even when distributions are identical. Multi-mode methods (10 runs × 10 samples) may achieve lower MMD than single-mode methods (1 run × 100 samples) simply because sampling from multiple modes better covers the support of the 1000-checkpoint distribution, not because they better approximate a posterior. The paper does not control for this — e.g., subsampling the target to 100 or using a consistent total sample size — nor does it discuss the confound.

### Minor

3. **The symmetry removal procedure (NS column) is underspecified.** The table reports "MMD computed after the removal of the symmetries" (NS column), but the paper does not provide a clear algorithm for how permutation and scaling symmetries are removed from the weight-space samples, especially for ResNet-18 where residual connections complicate per-layer alignment. Section 5.2 describes a sorting procedure for tracking permutations during training (sorting neurons by max weight), but it is unclear whether this same procedure is applied globally for the NS column or whether a different method is used. Without this detail, the NS column is difficult to interpret or reproduce.

4. **The claim that "the complexity of the posterior is orders of magnitude higher than what we understand" is not supported by the evidence provided.** This conclusion (line 326) follows from two observations: (a) pairwise MI has low variance in-distribution, and (b) ID and OOD MI are uncorrelated (Figure 3). Neither observation quantifies the total number of modes or the posterior's overall complexity. Low variance in pairwise MI simply means that models disagree roughly equally; lack of ID-OOD MI correlation is a known phenomenon from the ensemble literature. Neither justifies an "orders of magnitude" claim, which the reviewer verified is not separately argued.

5. **Missing error bars or variance estimates in Table 1.** The reported MMD values lack confidence intervals or bootstrap estimates across random seeds. This is particularly concerning because MMD values (e.g., 0.0 for Deep Ensembles vs 15.0 for single-mode Dropout on MNIST) may be sensitive to finite-sample variability, and the reader cannot assess whether gaps are meaningful.

6. **The BNN (Bayes by Backprop) results are notably poor across most settings (e.g., 18.8 MMD on MNIST single-mode, often worst among methods), but the paper does not discuss why.** Is this due to the mean-field diagonal Gaussian assumption, the ELBO optimization, or the small number of posterior samples? Analysis would be informative for practitioners choosing among methods.

### Trivial

- The permutation sorting used in the frequency analysis (Section 5.2) relies on the maximum weight per neuron, which the paper acknowledges is somewhat arbitrary but reports as the most stable among statistics tried. This is reasonable but would benefit from reporting what other statistics were tried.

## Nice-to-Haves

- **Subsample the reference to 100 or up-sample approximate methods to 1000** to rule out sample-size artifacts in the MMD comparison.
- **For the small-scale OptuNet case (392 parameters)**, add a proper ground-truth posterior from full-batch HMC (which the paper's related work notes is feasible at small scale using e.g., Izmailov et al. 2021's approach). This would validate whether the 1000-SGD-checkpoint reference gives similar rankings to a true Bayesian reference.
- **Connect the min-mass analysis to the MMD evaluation** by checking whether the posterior approximations (BNN, SWAG, etc.) are consistent with the min-mass scaling or whether their L2 regularization biases them away from it.
- **Report what other statistics were tried** for the neuron sorting (Section 5.2) and why max-weight was most stable.

## Removed Points

**These points were assessed but are removed/downgraded from the main weaknesses for the reasons stated:**

- *"The reference distribution is not a legitimate Bayesian posterior" (Harsh Critic, phrased as categorical rejection)* — The paper calls the target the "estimated posterior" (line 280), not the "true posterior." However, the framing is still misleading because the paper's title and abstract situate the work as studying Bayesian posteriors. The point is retained as a Major weakness above, but reframed as a **lack of justification** rather than a categorical invalidation of the paper, since (a) the paper never claims these are HMC samples, and (b) using SGD solutions as a pragmatic reference at scale is a defensible choice if properly scoped and justified.

- *"Min-mass problem is disconnected from posterior estimation"* — The Harsh Critic's point that the min-mass analysis is not tied to the MMD evaluation is accurate but does not constitute a weakness: the analysis is presented as a standalone theoretical contribution about scaling symmetries (lines 211-212 make the transition explicit). The paper never claims the min-mass analysis informs the MMD benchmark. Not a flaw.

- *"Permutation frequency analysis sorting criterion is arbitrary"* — The paper acknowledges trying other statistics and reports max-weight as the most stable (line 344: "We have tried other statistics on the values of the weights, but taking the maximum seems the most stable"). The concern is partially addressed.

- *"The paper should add HMC"* — This is a constructive suggestion, not a present weakness. Moved to Nice-to-Haves.

## Novel Insights

None beyond the paper's own contributions. The main novel observation from cross-referencing the reviews is that the paper's strongest theoretical contribution (the formal decomposition of the posterior over symmetries) and its most practically useful empirical contribution (the MMD benchmark) are not as tightly linked as the paper's narrative suggests. The min-mass problem, functional collapse analysis, and permutation frequency study are individually interesting but read as disconnected vignettes rather than converging evidence for a single thesis about how symmetries affect posterior estimation.

## Suggestions

1. **Reframe the MMD evaluation explicitly**: Acknowledge that the 1000 SGD checkpoints represent an *empirical reference distribution* (the distribution of SGD solutions), not the true Bayesian posterior. Show that this reference is still practically meaningful (e.g., because practitioners care about approximating SGD-plausible weights for uncertainty). Alternatively, for the small-scale case, add an HMC reference.
2. **Subsample the target to 100 or increase approximate method samples to 1000** to control for sample-size effects in MMD. Report bootstrap confidence intervals.
3. **Provide a clear algorithm** for the symmetry removal procedure used in the NS column, including how permutation and scaling symmetries are resolved for architectures with residual connections.
4. **Tone down or better justify** the "orders of magnitude" claim in Section 5.1, which goes beyond what the evidence supports.
5. **Add a brief discussion** of why BNN (Bayes by Backprop) underperforms — is this a known limitation of mean-field VI at this scale, or specific to the implementation?

## Score and Decision

**Originality**: The theoretical formalism and the protocol-level MMD benchmark are novel contributions. The min-mass problem is a genuinely new angle on scaling symmetries.

**Importance**: Understanding how symmetries affect posteriors is an important problem for uncertainty quantification. The paper addresses a timely question.

**Claims**: The central claim that the MMD benchmark evaluates "posterior estimation quality" needs stronger justification. The "orders of magnitude" claim in Section 5.1 is not supported.

**Soundness**: The theory is sound. The empirical methodology has a significant confound (reference distribution choice, sample-size asymmetry) that weakens the main quantitative conclusions.

**Clarity**: Generally well-written. The NS column procedure is underspecified.

**Value**: The theoretical insights, the dataset release, and the individual analyses (min-mass, functional collapse, permutation frequency) are valuable. The MMD benchmark would be more valuable after methodological improvements.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>