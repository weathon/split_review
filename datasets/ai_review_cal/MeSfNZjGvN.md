- Decision: Reject
- Avg Score: 2.50
- Scores: 3, 3, 1, 3
Now I have all the evidence needed. Let me compose the final consolidated review.

## Summary

The paper introduces FedPeWS, a warmup-phase strategy for federated learning under extreme data heterogeneity. In the first \(W\) rounds, each client learns a personalized binary mask (at neuron-level via sigmoid + Bernoulli sampling with straight-through estimation) and updates only a subnetwork of the full model. After warmup, training reverts to standard full-model communication. The method is designed as a plug-and-play wrapper compatible with existing FL optimizers. Experiments on synthetic data, CIFAR-MNIST (combined 20-class), and three medical datasets (PathMNIST, OCTMNIST, TissueMNIST) show substantial improvements over FedAvg and FedProx baselines, with the largest gain being 32.72% absolute accuracy over FedAvg in an N=4 disjoint-class setting.

## Strengths

1. **Large and consistent empirical gains over FedAvg/FedProx under extreme heterogeneity.** The most striking result is on N=4 synthetic data with disjoint classes per client (Figure 3): FedAvg collapses to 58.4% accuracy while FedPeWS reaches 91.13% — a 32.72% absolute improvement. This gain is not a fluke of a single hyperparameter setting; it appears across diverse experimental conditions (Tables 1, 2, Figures 5–7).

2. **Plug-and-play integration is demonstrated.** FedPeWS is shown to improve FedProx (Table 2): with \(\eta_g=0.5\), FedProx alone cannot reach 90% target accuracy within \(T\) rounds, whereas FedPeWS+FedProx reaches it in 211 rounds and achieves 98.40% final accuracy versus 82.43%. Three of four tested FedProx scenarios show clear gains.

3. **Low sensitivity to hyperparameters \(\lambda\) and \(\tau\) across wide ranges.** The heatmaps (Figures 5b, 6b) show that FedPeWS achieves similar accuracy for \(\lambda\) spanning three orders of magnitude (0.1 to 1000) and \(\tau\) from 0.2 to 0.8. The method does not require precise hyperparameter tuning to be effective.

4. **Consistent improvement across degrees of heterogeneity.** Dirichlet experiments (Figure 7) with \(\alpha \in \{0.1, 0.5, 1.0, 2.0, 5.0\}\) show FedPeWS outperforms FedAvg at every heterogeneity level, with larger gains at lower \(\alpha\) (higher heterogeneity).

5. **Core mask-learning mechanism works without diversity enforcement.** The N=4 experiment with \(\lambda=0\) (no diversity loss) achieves 91.13% accuracy, demonstrating that the basic mask-learning mechanism is effective independently of the coverage-encouraging diversity term. This also means the main contribution does not depend on the less-specified component.

## Weaknesses

### Fatal

None. The paper's core claim — that personalized warmup via learned subnetworks improves convergence under extreme heterogeneity — is supported by the evidence.

### Major

1. **The global mask probability update and the diversity loss computation are underspecified to the point of irreproducibility.** The algorithm (Alg. 1) initializes \(\theta_g^0 = \sigma(s_g^0)\) and sends \(\theta_g^{t-1}\) to clients, and the diversity loss (Eq. 3 / line 83) uses \(\theta_{g\setminus\{i\}}^{t-1}\) — the global mask probability "excluding the current participant \(i\)." However, **the pseudocode contains no server-side update rule for \(\theta_g\) or \(s_g\).** The server receives \(m_i^t\) from each client on line 89, but no step computes an updated \(\theta_g\) from these values. As a reader, one cannot tell whether \(\theta_g\) is meant to be the average of client mask probabilities, the average of client mask score sigmoids, or something else, nor how "excluding participant \(i\)" is computed from a single global value. Since the diversity loss is offered as a contribution (contribution 2: "incorporates a mask diversity loss to improve the coverage of all neurons"), this gap is significant. The basic method is saved by the \(\lambda=0\) experiments, which show the core idea works without this term. **Why it matters:** The diversity loss, as presented, cannot be correctly implemented from the paper's description.

2. **No comparison against any existing subnetwork-based or mask-learning FL method.** The related work discusses IST (random neuron sampling), FedPM (weight-level mask learning via sigmoid + Bernoulli), HeteroFL, and lottery-ticket FL approaches at length, and directly states "we use a similar approach [to FedPM] in our FedPeWS algorithm." Yet the experiments compare only against FedAvg and FedProx — both non-subnetwork optimization baselines. Without a comparison against at least one subnetwork competitor (e.g., FedPM, or IST, or a random-mask warmup variant), the reader cannot assess whether learned personalized masks offer a genuine advance over simpler subnetwork strategies. The "plug-and-play" claim is shown with FedProx, but the paper's own framing positions subnetwork learning as central. **Why it matters:** The contribution cannot be properly contextualized or its novelty substantiated without this comparison.

### Minor

1. **No analysis of what masks are learned.** The paper never visualizes or quantitatively analyzes the learned masks — e.g., overlap between client masks, sparsity levels, correlation with data heterogeneity, or how masks change during warmup. Since the mask-learning mechanism is the core novelty, this analysis would significantly strengthen the paper.

2. **No ablation isolating the warmup phase from the mask-learning mechanism.** A variant where clients use random fixed subnetworks (rather than learned masks) during warmup would isolate whether the gains come from training on sparser models initially or from learned personalization. The paper tests FedPeWS-Fixed (fixed disjoint masks) on CIFAR-MNIST and Path-OCT-Tissue, but only as an additional variant, not as an ablation that controls for the effect of mask learning. The FedPeWS-Fixed results are presented on the heatmaps but not systematically compared and discussed.

3. **Compute overhead during warmup is not discussed.** Each local step in the algorithm doubles the per-step computation: Procedure I (freeze weights, update mask scores) followed by Procedure II (freeze mask scores, update weights), both requiring forward passes. This overhead is not acknowledged or quantified, which is relevant for practitioners assessing the cost of the method.

4. **Limited evaluation of the FedProx plug-and-play combination.** The FedProx experiments (Table 2) use only the synthetic dataset. The CIFAR-MNIST and medical dataset experiments use only FedAvg as the base optimizer. Since "plug-and-play compatibility" is claimed as a feature, demonstrating it on more than one non-synthetic dataset would strengthen the claim.

### Trivial

- The STE for mask gradient approximation is used without discussion of known issues (e.g., gradient bias). A brief note would improve rigor.
- The synthetic data's 2D→5D expansion is described as "heuristic" but the specific hidden-layer sizes are not reported.
- The paper could clarify that the fixed masks for FedPeWS-Fixed are only applicable when client data distributions are known a priori.

## Nice-to-Haves

- Quantify the communication overhead of transmitting masks \(m_i^t\) during warmup (bits per round).
- Provide guidance on selecting \(\lambda\) and \(\tau\) beyond grid search, or characterize settings where certain \(\lambda\) regimes are preferable.
- Statistical significance tests (e.g., paired bootstrap) for the headline results.
- Extend the medical dataset experiment (Path-OCT-Tissue) to N > 3 by subdividing each medical dataset further.

## Removed Points

These points from the inputs were removed or demoted; treat them with caution:

- **Harsh critic's point #3 (limited larger-N evaluation):** REMOVED — the paper explicitly scopes itself to the cross-silo setting ("N is small," line 56). The N=10 Dirichlet experiments are additional demonstrations beyond the stated scope. Criticisms about insufficient scaling are scope creep.
- **Introduction overclaiming about "most existing heterogeneous FL algorithms fail":** REMOVED — this is a motivational claim in the introduction. The paper demonstrates failure for FedAvg and FedProx, the two most standard baselines, which is sufficient for motivation.
- **Statistical significance not tested:** REMOVED — reporting mean±std over 3 seeds is standard practice. Demanding formal significance tests is not standard for this type of empirical FL paper.
- **Missing related works:** REMOVED per policy — I cannot verify what related works exist outside the paper.
- **Formatting, typos, grammar issues:** REMOVED per policy — these are parser artifacts, not author errors.
- **Missing appendix content / proofs:** REMOVED per policy — the parser strips these; they exist in the original submission.

## Novel Insights

None beyond the paper's own contributions. The two reviews align on the core strengths (large empirical improvements, low hyperparameter sensitivity) and converge on the two main weaknesses (underspecified diversity loss, missing subnetwork baselines). No reviewer identified a flaw that the paper's authors would be unaware of.

## Suggestions

1. **Complete the specification of the diversity loss mechanism.** Clarify how \(\theta_g\) is computed from client mask information on the server, how \(\theta_{g\setminus\{i\}}\) excludes client \(i\), and whether \(\theta_g\) changes across rounds. Add the missing server-side update step to Algorithm 1.

2. **Add comparisons against at least one subnetwork-based FL method.** FedPM is the most natural baseline since the paper already states it "uses a similar approach." IST (with random neuron sampling) would also be informative. At minimum, add a variant where clients use random fixed subnetworks during warmup to isolate the benefit of learned masking.

3. **Provide mask analysis.** Include figures showing: (a) overlap between client masks, (b) how mask sparsity varies across heterogeneity levels, (c) how masks evolve during warmup rounds. This would make the mechanism interpretable rather than a black box.
