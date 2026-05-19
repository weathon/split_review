## Summary
Maestro proposes a training framework for low-rank neural networks that combines ordered dropout (applied to factorized weight matrices) with hierarchical group-lasso regularization and progressive shrinking. The key idea is to learn the rank ordering per layer during training rather than applying a post-hoc SVD decomposition, enabling data-dependent rank selection and "train-once, deploy-everywhere" flexibility. The method is evaluated on MNIST, CIFAR-10, ImageNet, and Multi30k (translation) across fully-connected, convolutional, and attention layers.

## Strengths
- **Ablation study cleanly validates each component's contribution (Tab. 5, the paper's ablation table).** Removing group-lasso regularization increases training MACs by 1.33× and parameters from 4.08M to 11.2M with no accuracy gain; removing progressive shrinking similarly increases cost without benefit; and the full-training variant (sampling all ranks each step) raises training MACs to 1.97× for no gain. This directly supports the claim that sampling + HGL + progressive shrinking are all necessary for efficiency.

- **Flexible deployment without retraining (Fig. 4a).** Greedy pruning of a Maestro-trained model (λ=0) maintains substantially better accuracy–latency trade-offs than pruning an SVD-factorized model at the same GMACs. This demonstrates the practical value of the learned ordered representation for deployment to varying hardware targets, as claimed.

- **Generality across architectures and layer types.** The method is applied to fully-connected, convolutional, and attention layers and evaluated on four datasets spanning two modalities (vision and translation). This breadth supports the claim that the approach is a general framework rather than a one-off technique.

- **The progressive shrinking mechanism eliminates the need for full-rank warmup** (which both Pufferfish and Cuttlefish require, as noted in Sec. 3.3). This is a meaningful practical improvement in training efficiency.

## Weaknesses
### Fatal
None.

### Major

1. **The strongest empirical claim (Multi30k transformer, Tab. 2) uses Pufferfish results from the original work without controlled re-running.** The paper reports Maestro perplexity 6.90 vs. Pufferfish 7.34 at 25% of the GMACs and 52% of the parameters, but the Pufferfish numbers are labeled "Results from original work." Without re-running Pufferfish under the *same* training schedule, hyperparameters, tokenization, and evaluation protocol, it is impossible to attribute the gains to Maestro's method rather than to implementation differences. The paper does not describe the transformer training setup in sufficient detail to assess comparability. For a comparison that the abstract calls out as headline evidence ("6% lower perplexity at a quarter of the computational cost"), this lack of experimental control is a significant weakness. (The ImageNet comparisons, by contrast, are better controlled — baselines are marked as "without label smoothing (same as our setup for Maestro).")

2. **The paper claims "lower training overhead" compared to Pufferfish/Cuttlefish but does not quantify this against the actual baselines.** The ablation study (Tab. 5) reports *relative* training GMACs for Maestro variants (1.00× vs. 1.33× vs. 1.97×), which is informative for internal comparisons. But the paper provides no absolute training FLOPs, wall-clock time, or comparable metric for Pufferfish and Cuttlefish. The qualitative argument (Pufferfish requires full-rank warmup) is sensible, but without a direct measurement, the claimed training efficiency advantage is asserted rather than demonstrated.

### Minor

3. **The theoretical contribution (Sec. 4, Theorem 1) is modest and presented informally.** Theorem 1 states that for the linear case, the LoD objective is equivalent to PCA on a transformed dataset, recovering SVD for uniform data. This result is labeled "Informal" and no proof is given. The paper acknowledges that the SVD recovery is "consistent with the prior results [Horvath et al., 2021]" — i.e., it is not a new finding for the linear case. The extension to data-dependent ordering is conceptually interesting, but the paper's theoretical analysis does not extend beyond the linear single-layer setting. The abstract's phrasing that "our theoretical analysis demonstrates that in special cases LoD recovers SVD and PCA" is accurate but overstates the reach of the theory.

4. **On ImageNet (Tab. 4), gains over Pufferfish/Cuttlefish are marginal.** In the partial decomposition setting, Maestro achieves 76.04% vs. Pufferfish 75.99% and Cuttlefish 76.00% — differences within 0.05 percentage points. Only single-run results (without confidence intervals) are reported. In the full decomposition setting, the +0.51pp gain over Pufferfish is more meaningful, but the baselines operate at slightly different parameter counts (9.4M vs. 9.2M). The practical advantage on ImageNet is small.

5. **The justification for rank sampling relies on a heuristic.** The paper honestly states (Sec. 3.3, lines 175-176) that the strong growth condition enabling one-summand-at-a-time sampling "is unclear" for DNNs and that the claim rests on empirical observation. While this transparency is commendable, it means the sampling efficiency has no theoretical backing in the deep-learning setting.

### Trivial
None. The paper is generally well-written and the formatting issues present in the extracted text are parser artifacts.

## Suggestions
1. **Re-run Pufferfish and Cuttlefish under fully matched conditions on Multi30k**, including identical optimizer, learning rate schedule, tokenization, and evaluation. Report the full training cost (FLOPs or time) for all methods. This is the single most important improvement.
2. **Provide multi-seed runs with confidence intervals** for the ImageNet comparison, where the accuracy differences are small (≤0.5pp).
3. **Either provide a formal proof of Theorem 1 (or a reference to one) in an appendix, or relabel it as an "Observation"** with clear attribution to prior work (Horvath et al., 2021) for the SVD-recovery case. This would better calibrate reader expectations about the theoretical contribution.
4. **Directly measure and report training FLOPs/wall-clock time** for Maestro (including HPO overhead of 2-3 runs) vs. Pufferfish and Cuttlefish, so the claimed "lower training overhead" is quantitatively substantiated.

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>

## Questions


## Decision
Reject
