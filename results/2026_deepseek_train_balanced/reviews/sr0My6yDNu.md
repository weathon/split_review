Now let me finalize the review.

## Summary
The paper addresses adversarial robustness degradation under continual learning without data replay. It proposes Double Gradient Projection (DGP), which extends GPM by adding SVD-derived bases that constrain weight updates to preserve sample gradients across tasks, designed to work with defense algorithms that operate via sample gradient smoothing (IGR and AT).

## Strengths
- **Principled extension from output preservation to gradient preservation.** Section 3.1 derives a clean mathematical condition (Eq. 11: ∂X^l/∂X · ΔW^l = 0) that parallels GPM's output-preservation condition but targets sample gradients. The chain-rule derivation (Eqs. 8–10) and the recursive argument are mathematically sound.
- **Direct mechanism validation (Fig. 5).** The cosine similarity of sample gradients from the first task is measured across subsequent tasks. DGP shows a relatively flat downward trend compared to baselines, providing direct evidence that the mechanism the method was designed to achieve actually operates as intended — stronger than reporting only downstream metrics.
- **Important empirical finding about CL-defense incompatibility.** The paper reports that EWC + IGR ≈ naive SGD, with a plausible explanation: both methods add regularization terms whose guidance on weight update directions interferes. This is a practically useful finding independent of the proposed method.
- **Broad evaluation scope for IGR.** The IGR experiments span four benchmarks (Permuted MNIST, Rotated MNIST, Split-CIFAR100, Split-miniImageNet) and three attack types (FGSM, PGD, AutoAttack). The largest advantages for DGP appear under the strongest attack (AutoAttack), which is the regime where robustness matters most.

## Weaknesses

### Fatal
None.

### Major
1. **No quantitative results reported — all evidence is visual.** The paper defines ACC and BWT (Eq. 14) but never reports a single numerical value in text or tables. All results are conveyed through line plots (Figs. 3, 4) at small resolution. A reader cannot determine final ACC values, BWT values, or whether the advantage over baselines is, say, 2 or 20 percentage points. For an empirical paper at a top venue that claims superiority, this is a decisive evidential gap. (Verified: the paper contains zero tables; BWT appears only in Eq. 14 and is never mentioned again.)
2. **The "class of defense algorithms" claim is only partially supported.** AT is evaluated only on Permuted MNIST (Fig. 4) — the simplest benchmark with a fully-connected network, 10 permutation tasks, and only two baselines (GEM and GPM). There is no AT evaluation on CIFAR100 or miniImageNet. Since the paper claims DGP collaborates with "a class" of defense algorithms, the evidence for AT must extend beyond the easiest setting. (Verified: Fig. 4 caption states results are "on PMNIST dataset" only.)
3. **No experimental comparison against the only existing robust continual learning method.** The paper acknowledges Bai et al. (2023) in Related Works but does not compare against it, citing the setup difference (they allow replay). While a direct comparison in the same setting is not straightforward, the omission is conspicuous. A controlled experiment (e.g., DGP without replay vs. Bai et al. with replay to show comparable robustness without the memory requirement) or a principled argument for infeasibility would be expected. (Verified: Bai et al. is discussed only in Section 5 and absent from all experiments.)

### Minor
1. **BWT is defined as a metric but never reported.** Backward transfer (forgetting of previous tasks) is central to the paper's thesis, yet it is never used or discussed after Eq. 14. (Verified: BWT appears only once, in Eq. 14.)
2. **The SVD truncation threshold α is not specified.** The threshold α^l (Eq. 6) controls the stability-plasticity trade-off. It is not reported per dataset or layer, harming reproducibility. (Verified: Eq. 6 mentions α^l but no numerical values appear anywhere.)
3. **Computational overhead is not discussed.** DGP performs two SVDs per task (activations + Jacobians) plus gradient projection, versus GPM's single SVD. Wall-clock time or FLOPs relative to baselines is not reported, which matters for practical adoption.
4. **The "weak guarantee" approximation error is not quantified.** The column-wise summation compression (Eq. 12) reduces the Jacobian SVD from O(n·m₁ × mₗ) to O(n × mₗ). The paper asserts it is "sufficient to yield desirable results" but provides no analysis of how much gradient information is lost. A small-scale comparison of the full vs. compressed SVD would help assess this.

### Trivial
None. (Format/typo criticisms excluded per filtering policy.)

## Nice-to-Haves
- An ablation adding a matched-rank set of random bases to GPM (instead of gradient-derived bases) would help establish that the benefit is specific to gradient information, not simply an effect of having more constraints.
- A small-scale comparison of the full Jacobian SVD vs. the compressed (column-sum) SVD on Permuted MNIST to quantify the approximation error of the "weak guarantee."

## Removed Points
- **"Hyperparameters reported as triplets without explanation"**: The paper explicitly states "batch size, number of epochs, and input gradient regularization λ are set to 32/10/50, respectively" — the order is clearly explained. Removed because the reviewer misread the paper.
- **"Gradient stability hypothesis is only correlational, not causal"**: The paper already includes GPM+IGR as a baseline and provides direct mechanism evidence (Fig. 5). The claim that the evidence is "correlational" is overstated — the paper tests the mechanism chain. Removed.
- **"Independent first-layer design simplifies the problem undiscussed"**: The paper discusses this design choice (Lines 285–286), states baselines receive the same setup, and gives a rationale for choosing it over fixing the first layer. The design is transparent and fair. Removed.
- **"Missing related works / too brief"**: Per policy, missing related works should not be listed as a weakness. Removed.
- **Typo/grammar criticisms** ("GDP" vs "DGP", "can maintaining", "mitigating rapidly degradation"): Per policy, these are treated as parser artifacts. Removed.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. Add a table reporting final ACC and BWT (with standard deviations) for all methods on all benchmarks, under all three attacks and the clean setting. This single change would most directly address the paper's main evidential gap.
2. Evaluate DGP + AT on at least Split-CIFAR100 to substantiate the "class of defense algorithms" claim.
3. Provide a discussion or controlled experiment comparing against Bai et al. (2023), even if the setups differ.
4. Report the α values used for SVD truncation per dataset and per layer to enable reproducibility.
5. Report wall-clock time or relative computational cost of DGP vs. GPM.

## Score and Decision

The paper addresses a genuinely underexplored problem with a principled method and provides mechanism-level validation. However, the complete absence of quantitative results tables — all evidence is visual from line plots — is a decisive evidential gap for an ICLR submission. Combined with the partial support for the "class of defense algorithms" claim and the missing comparison against the one existing robust CL method, the paper in its current form does not make a convincing case for its central claims, even though the underlying ideas are promising and fixable.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>