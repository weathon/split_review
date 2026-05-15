Now I have a thorough understanding of the paper. Let me compose the final consolidated review.

## Summary

SparsyFed proposes a sparse adaptive federated learning method combining activation pruning during the backward pass, Powerpropagation weight reparameterization, and TopK communication pruning to train highly sparse models in cross-device FL. The method achieves 95% sparsity with minimal accuracy degradation across CIFAR-10, CIFAR-100, and Speech Commands, outperforming sparse training baselines (TopK, ZeroFL, FLASH). The central argument is that SparsyFed simultaneously addresses data heterogeneity, maintains plasticity (unlike fixed-mask FLASH), and requires few hyperparameters.

## Strengths

- **Consistently best accuracy among sparse methods across sparsity levels and datasets.** Table 1 (aggregated results with ResNet-18 on CIFAR-10, CIFAR-100, Speech Commands) shows SparsyFed exhibits the lowest accuracy drop among all baselines at every target sparsity (90%–99.5%). At 90–95% sparsity, it sometimes matches or surpasses the dense model.
- **Demonstrates stable client consensus on sparse masks.** Figure 6 (right) and §5.3 show that SparsyFed maintains global model sparsity close to the 90% target, whereas ZeroFL and TopK drop to 47% and 83% respectively in early rounds — providing empirical evidence for the consensus mechanism.
- **Rigorous baseline re-implementation.** The authors re-implemented ZeroFL and FLASH rather than relying on reported numbers, enabling controlled comparison on equal footing.
- **Clean ablation studies.** Activation pruning (§5.5) and weight reparameterization (§5.4) are ablated with clear results, isolating the contribution of each component.

## Weaknesses

### Fatal

None.

### Major

1. **The headline quantitative claim ("200× smaller per-round weight regrowth") is completely unsupported.** The abstract states SparsyFed "achieves a per-round weight regrowth 200 times smaller than previous methods" as a central contribution. However, this quantity is never defined, measured, or referenced anywhere in the body of the paper — not in §5.3 (consensus analysis), not in any figure, table, or appendix reference. No experiment reports per-round weight regrowth for SparsyFed or any baseline. A core advertised result is therefore unsubstantiated. The authors must either remove this claim or clearly define and measure it (e.g., number of weight indices flipping sign between rounds, normalized per round).

2. **Plasticity — the paper's main differentiator from FLASH — is never directly evaluated.** The paper repeatedly motivates SparsyFed by its ability to adapt to "never-seen data distributions" (abstract, §1, §3, §5.3) and argues that fixed-mask methods like FLASH lack this capability. Yet all experiments use a static LDA-partition (fixed α value for the entire training run). There is no experiment involving distribution shift across rounds: no rotating classes, no changing client populations, no new labels appearing over time. Without such evaluation, the plasticity advantage over FLASH is asserted rather than demonstrated. This is not a minor omission — it is the central theoretical advantage the paper claims over its strongest baseline.

### Minor

3. **Only a single random seed is used.** The paper states (line 82) that seed 1337 is fixed for the LDA partitioning; no multiple seeds or error bars are reported for any experiment. This makes it impossible to assess the statistical significance of the reported accuracy differences between methods — particularly concerning at sparsity levels where margins are narrow.

4. **Only one model architecture is evaluated.** All experiments use ResNet-18. The paper claims general applicability to cross-device FL but does not evaluate smaller architectures (e.g., MobileNet, 2-layer CNN) that would be more representative of edge devices, nor transformer-based models. This limits the generality of the findings.

5. **Activation pruning's computational benefits are asserted, not measured.** §5.5 shows activation pruning has minimal accuracy impact, which is useful information. However, the paper claims this "reduces computational cost" without measuring FLOPs, latency, or energy savings on actual or simulated hardware. The benefit of this component is therefore only half-demonstrated.

### Trivial

6. **The "single hyperparameter" claim in the abstract is imprecise.** The abstract says the method "only needs a single hyperparameter," but the user must choose both target sparsity ŝ and the Powerpropagation parameter β. While ŝ could be considered a requirement specification rather than a tunable hyperparameter, and the paper notes β is from the adopted Powerpropagation method, the phrasing is misleading as stated.

7. **The communication cost metric, while explained and applied consistently across methods, is non-standard.** The paper measures cost "as if only one client were participating" (§4). This normalization is clearly described and applied uniformly to all methods, so relative comparisons (19.29× vs. dense, 1.66× vs. ZeroFL) are internally consistent. However, the absolute savings factor would differ under standard FL cost accounting (accounting for all clients), and this should be acknowledged.

## Nice-to-Haves

- An experiment with round-wise distribution shift (e.g., swapping client data partitions mid-training) would directly validate the plasticity argument.
- Reporting results over 3+ seeds with mean and standard deviation for key accuracy and communication figures.
- Evaluating on smaller architectures (e.g., a 2-layer CNN or MobileNet) to strengthen claims about cross-device suitability.
- Measuring actual FLOP reduction or wall-clock speedup from activation pruning on representative hardware.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"Figure 6 (right) is referenced but not visible in the extracted text"** — This is a PDF-parser artifact. The figure exists in the original paper. Not a paper flaw.
- **"FLASH excluded from consensus comparison — convenient omission"** — The paper explicitly explains (line 136) that FLASH uses a fixed mask after round 1, so it trivially achieves perfect sparsity by design. This exclusion is methodologically justified, not a convenient omission. The comparison is meaningful as-is.
- **"Spectral reparameterization is an unfair baseline"** — The ablation compares reparameterization methods that could be plugged into the same pipeline, to show which works best. Powerpropagation winning over alternatives (including spectral and fixed-mask) is a valid ablation result even if spectral was originally designed for a different purpose.
- **"Introduction motivation is anecdotal"** — The three motivating challenges (data heterogeneity, plasticity, hyperparameter complexity) are well-established in the cross-device FL literature cited by the paper (Kairouz et al., 2021; Wang et al., 2021; etc.). Not a valid weakness.
- **"Method justification for Powerpropagation is vague"** — The paper provides a clear intuitive explanation: small-magnitude weights have limited impact on updates, so Powerpropagation's rich-get-richer dynamics guide clients toward a shared subset of weights. This is sufficient for an empirical paper.
- **"Does not evaluate transformer-based models"** — While a valid scope extension (captured in Nice-to-Haves), the paper scopes to ResNet-18 for comparability and states this clearly. Not a required evaluation for an accepted contribution.

## Novel Insights

Beyond the paper's own contributions, the reviews do not surface additional novel insights. The key observation — that dynamic mask methods for FL must balance consensus (avoiding regrowth) with plasticity (avoiding fixed masks) — is already articulated by the paper.

## Suggestions

1. **Define and measure per-round weight regrowth** if the 200× claim is to be retained. Report this for all methods (SparsyFed, ZeroFL, FLASH, TopK) at a representative sparsity level.
2. **Add a distribution-shift experiment** — e.g., partition client data by α=0.1 for rounds 1–100 then switch to a different partition for rounds 101–200, and compare SparsyFed's accuracy recovery to FLASH's.
3. **Report results over multiple seeds** (at least 3) with standard deviations for the main accuracy tables.
4. **Clarify the hyperparameter count** — either count both ŝ and β explicitly, or clearly state that ŝ is a user-specified requirement rather than a tunable hyperparameter.
5. **Quantify activation pruning savings** with a FLOP count or profiled latency on CPU/mobile hardware.

## Score and Decision

The paper addresses a well-motivated problem and demonstrates genuine empirical strength (best accuracy among sparse FL methods across multiple datasets and sparsity levels). However, two issues substantially weaken the contribution's credibility: (a) the headline "200×" claim in the abstract is completely unsupported by any experiment in the body, and (b) the plasticity argument — the paper's main differentiator from FLASH — is never directly tested. These are fixable in revision but cannot be ignored in the current submission. The remaining weaknesses (single seed, single architecture, imprecise hyperparameter claim) are minor and common in conference papers. Overall, the paper's core empirical contribution (a practical method achieving 95% sparsity with minimal accuracy loss and stable mask consensus) is solid, but the unsupported quantitative claim and untested central advantage prevent acceptance in the current form.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>