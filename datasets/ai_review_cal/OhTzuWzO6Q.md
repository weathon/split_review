- Decision: Reject
- Avg Score: 4.75
- Scores: 5, 5, 3, 6
I now have a thorough understanding of the paper and have verified all claims against the paper text. Let me produce the consolidated review.

## Summary

This paper proposes a personalized federated learning framework that trains local Bayesian neural networks of potentially different architectures on each client. Collaboration is achieved by using an unlabeled public "alignment dataset" (AD) at the server: clients share their outputs (logits) on the AD, the server aggregates them, and each client then tunes its weight-space prior parameters to minimize a functional distance between its own output and the aggregated (corrected) output. The paper also claims a formal differential privacy guarantee via Gaussian noise added to the shared outputs. Experiments on MNIST, CIFAR-10, and CIFAR-100 under non-IID settings show substantial gains over strong baselines, especially when some clients have limited data or compute.

## Strengths

1. **Functional-space collaboration under model heterogeneity.** The paper's core idea — using outputs on a public dataset to define priors rather than aggregating weight distributions — is genuinely novel and directly addresses the problem of heterogeneous client architectures where weight-space aggregation is impossible. Section 3.2.1 clearly motivates this move to function-space, and Figure 1a demonstrates that under compute heterogeneity (30% small clients), the method outperforms homogeneous baselines forced to use only small models. This is a well-motivated and demonstrated contribution.

2. **Strong empirical results in challenging low-data, heterogeneous regimes.** In non-IID settings with 50 or 100 training instances per class (Table 1), the proposed method achieves roughly 6% higher test accuracy on average across MNIST, CIFAR-10, and CIFAR-100 compared to the best baseline. For example, on CIFAR-10 medium setting, the method obtains 75.23% vs. pFedGP's 68.44%. The margins are large and consistent across datasets.

3. **Comprehensive evaluation across three types of heterogeneity.** The experiments systematically vary compute capacity (Figure 1a), data quantity (Figure 1c), and statistical distribution (non-IID, Table 1), demonstrating versatility beyond prior work that typically focuses on one type of heterogeneity. Figure 1c shows the method degrades more gracefully than baselines as the fraction of resource-limited clients increases.

4. **Flexible personalization via convex combination.** Equation 3 introduces a tunable parameter γ that mixes global and local outputs during prior optimization, giving clients explicit control over the degree of personalization vs. global knowledge sharing.

## Weaknesses

### Major

1. **Privacy analysis is not rigorous; the claimed DP guarantee is unsupported.** The paper's differential privacy argument (Theorem 4.2) hinges on bounding the L2 sensitivity of a client's output on the alignment dataset to √2 (Δ² ≤ 2, line 126). There are two specific problems:
   - The paper states "the logit representation for each input, i.e., the normalized output" in the same sentence (line 126), conflating unbounded logits with normalized probabilities. If the shared values are truly logits (as implied by the method description where cross-entropy is used as a distance measure on logits, line 88), the sensitivity is unbounded.
   - Even if softmax-normalized outputs are used, the sensitivity of a *trained neural network's* output on a fixed public input with respect to a change in one *training point* is not a fixed constant. It depends on the training algorithm, model capacity, and regularization — none of which are controlled or bounded in the proposed method. No gradient clipping, output clipping, or any training-time DP mechanism is applied. The paper's claim that the analysis "does not assume any specifics of how each client is trained" (line 128) is actually a red flag: the analysis *must* account for the training process to bound sensitivity. As presented, the DP guarantee is not valid, and the privacy-related contribution (a key advertised feature) collapses.

2. **No calibration or uncertainty evaluation despite being a central motivation.** The abstract, introduction, and discussion repeatedly claim "well-calibrated outputs," "uncertainty quantification," and "calibrated responses" as core benefits (lines 4, 12, 16, 36, 174). Yet the experiments report only classification accuracy. No expected calibration error (ECE), reliability diagrams, or any uncertainty metric is provided. For a paper that frames uncertainty quantification as a primary motivation alongside heterogeneity and privacy, this is a significant omission.

### Minor

3. **Prior optimization mechanism could be clearer.** While a researcher familiar with variational BNNs could likely implement the described procedure, the paper does not explicitly state how the prior parameters ψ map to the Gaussian (μ, σ) parameters of the weight distribution, nor how gradient descent on the functional distance d(Φ_i^corrected, Φ_i(AD; W_i)) backpropagates into ψ (e.g., via the reparameterization trick). Adding a brief algorithm box or pseudocode explicitly distinguishing the prior-optimization phase (updating ψ) from the variational-inference phase (updating θ) would substantially improve reproducibility.

4. **Missing standard deviations for several entries in Table 1.** Only the DP-FedAvg row shows explicit ± values (line 153). Other entries lack reported error bars despite the table being cited with accuracy results. Multiple random seeds should be reported for all methods.

5. **No ablation of the mixing coefficient γ.** The paper sets γ=0.7 after tuning but does not study sensitivity to this hyperparameter, which controls the critical trade-off between global knowledge and personalization.

6. **Custom implementation of pFedBayes baseline.** The paper states "We used our own implementation of the pFedBayes algorithm since the source code was not publicly available" (line 155). While sometimes unavoidable, this introduces risk that the baseline is undertuned, which could inflate the reported gains.

### Trivial

7. Line 88 contains a garbled reference ("Φ_i(AD; W_i)") due to the text extraction process.
8. The Figure 1 caption is cut off mid-sentence at line 165.

## Nice-to-Haves

- Sensitivity analysis of AD size (fixed at 2000; how does performance vary with fewer or more public samples?)
- Communication cost comparison (the method shares C×|AD| floats vs. millions of weight parameters — quantifying this advantage would strengthen the paper)
- A no-collaboration baseline (each client trains alone, without the AD) to isolate the benefit of the proposed functional-space collaboration

## Removed Points

The following points from the reviewer inputs were removed with justification:

- **"No previous work has jointly addressed all these learning issues" is overstated.** The critic mentions pFedBayes. However, pFedBayes does not handle compute heterogeneity (different architectures) or formal DP, so the claim is reasonable. **Removed.**
- **Asymmetric comparison (baselines not given AD).** The paper already addresses this with an additional experiment showing that pre-training baselines on AD does not change their performance (line 162). **Removed.**
- **Method is not reproducible / structural gap in prior optimization.** Demoted from "structural/fatal" to Minor (point 3 above). The description is sufficient for the target audience; greater clarity would help but the method is implementable as described. **Moved to Minor.**
- **Missing appendix content / proofs.** The appendix (Theorems C.2, C.3) is referenced but removed by the text extraction process; this is a parser artifact, not a paper flaw. **Removed.**
- **Missing related works on function-space VI.** The paper mentions function-space priors (Sun et al., 2019; Flam-Shepherd, 2017) and scopes its contribution to FL; engaging more deeply would strengthen but is not a fatal omission. **Moved to Nice-to-Have.**
- **Strengths about the DP guarantee (Strength Finder #2).** This conflicts with the verified weakness about the flawed DP analysis, so it is dropped per protocol. **Removed.**
- **Generic/superficial strengths from Strength Finder** that lack concrete citation content. **Removed.**

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Fix the privacy analysis.** Either (a) apply a proper DP mechanism with sensitivity control (e.g., clip the outputs to a fixed L2 norm before adding Gaussian noise, and provide a rigorous Renyi DP accountant that accounts for both local training and output sharing), or (b) remove the DP claim and re-scope the paper as a non-private framework, or (c) adopt DP-SGD on the client models and provide a proper analysis. The current analysis is not publishable as-is.
2. **Add calibration evaluation.** Report expected calibration error (ECE) and/or reliability diagrams to substantiate the repeated claims about uncertainty quantification.
3. **Clarify the prior optimization loop.** Provide pseudocode or an explicit description: (a) how ψ parameterizes the Gaussian prior (means μ and variances σ²), (b) how the functional distance d(·,·) backpropagates into ψ (via reparameterized sampling from the prior), and (c) the precise distinction between the ψ-optimization phase and the θ-optimization (variational) phase.
4. **Include error bars for all methods in Table 1** and report results over multiple seeds.
5. **Add ablation of γ** to show sensitivity of results to the personalization/global-knowledge trade-off.
