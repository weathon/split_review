Now I have all the information I need. Let me write the consolidated review.

## Summary

This paper proposes Privacy-Aware Sparsity Tuning (PAST), a defense against membership inference attacks that replaces uniform ℓ1 regularization with per-parameter adaptive weights. The weights are derived from the gradient of the member/non-member loss gap with respect to each parameter — a quantity the paper calls "privacy sensitivity." PAST first trains a model to convergence, then tunes it with the adaptive-ℓ1 loss to selectively sparsify parameters that contribute most to the loss gap. Experiments on five datasets (Texas100, Purchase100, CIFAR-10/100, ImageNet) and under multiple attack types show that PAST improves the privacy-utility trade-off relative to undefended models and, on CIFAR-10/100, outperforms existing defense baselines.

## Strengths

- **Novel idea of per-parameter adaptive regularization for MIA defense.** The insight that not all parameters contribute equally to membership leakage, and that regularization should therefore be non-uniform, is well motivated. The empirical finding that the top 20% of parameters (by gradient of loss gap) account for 89.27% of cumulative sensitivity (Figure 1b) provides a concrete foundation for this approach, even if only shown on one setting.

- **Clear evidence that adaptive weighting outperforms uniform L1/L2.** The ablation in Figure 5a directly compares four combinations (L1, L2, L1+Ours, L2+Ours) on CIFAR-100. PAST (L1+Ours) strictly dominates the other three across the utility-privacy frontier, isolating the adaptive weight as the source of improvement over standard regularization.

- **Efficient and practical as an add-on defense.** PAST adds only ~10.4% time overhead over standard training (1374s vs 1245s on DenseNet121 / CIFAR-100). The two-stage design (converge first, then tune) means it can be applied on top of pre-trained models — including those trained with other defenses — and Table 2 shows consistent P1 improvements when added to five different defense methods.

- **Rigorous attack evaluation.** The paper assumes adaptive black-box adversaries with full knowledge of the defense mechanism and hyperparameters, training shadow models with identical settings. This follows best practices for MIA evaluation.

- **Broad dataset coverage.** Results span tabular (Texas100, Purchase100) and image (CIFAR-10/100, ImageNet) benchmarks, demonstrating applicability beyond a single domain.

## Weaknesses

### Fatal
None.

### Major

- **The privacy sensitivity measure (gradient of loss gap) is never validated as causally meaningful for MIA defense.** The paper defines "privacy sensitivity" as ∇θ_i G (gradient of the loss gap) and builds the entire method on this quantity, but never tests the core causal claim: does regularizing the top X% of parameters by this criterion actually reduce MIA success more than regularizing the same number of parameters chosen randomly, or by another criterion (e.g., bottom X%, or magnitude-based selection)? The ablation (Figure 5a) shows that PAST's adaptive weighting helps vs. uniform L1, but this does not isolate whether the *gradient-based selection* is the reason — it could be that any non-uniform redistribution of regularization within a module provides a benefit. This missing control experiment is a significant gap in the paper's evidence chain.

- **The claim of "state-of-the-art" privacy-utility trade-off is only fully supported on CIFAR-10 and CIFAR-100.** Table 1 compares PAST only against *undefended* models on Texas, Purchase, and ImageNet, not against any defense baseline. The privacy-utility curves with full baseline comparisons (Figures 3 & 4) are only shown for CIFAR-10/100. On the other three datasets, the paper only demonstrates that PAST improves over no defense — which is a lower bar than SOTA. The abstract and conclusion assert broader SOTA performance than the experiments establish.

- **No comparison to pruning-based defenses.** Since PAST induces sparsity, comparison to magnitude-based pruning (with/without fine-tuning) is a natural and missing baseline. The related work section discusses pruning as a defense (citing Huang et al., Wang et al.), and given that PAST also produces sparse models, readers cannot evaluate whether the benefit comes from selective regularization specifically or simply from any method that induces structured sparsity.

### Minor

- **The parameter-importance analysis (Section 3.1) is only demonstrated on one setting (ResNet-18, CIFAR-10, one random split).** The paper treats the finding that "only few parameters matter" as a general property of over-parameterized models, but provides no evidence across different architectures, datasets, or random seeds. While the PAST method itself is evaluated more broadly, the motivational claim lacks generality.

- **The practical requirement for non-member data (the inference set) is under-discussed as a limitation.** The method requires a holdout set from the same distribution to compute the loss gap. While this is shared with some prior defenses (Mixup+MMD, AdvReg), the paper's limitations section focuses only on label-only and white-box attacks and does not address when clean non-member data might be unavailable (e.g., sensitive domains). This should be elevated.

- **The time-consumption figure (Figure 6c) is not fully described.** The text gives numerical values only for PAST (1374s) and Base (1245s), but the bar chart includes bars for other defense methods without reported numbers or clear labeling in the text, making those comparisons difficult to interpret.

- **Unclear motivation for the module-size normalization factor |M(θ_i)| in the γ_i computation.** The formula γ_i = |M| · ∇G_i / Σ∇G_j ensures that within each module the total regularization weight sums to |M| (matching standard L1's per-module total), but the paper does not explain this design choice or discuss alternatives (e.g., normalizing so that Σγ_i = 1 globally). The readership is left to infer the rationale.

### Trivial
None.

## Nice-to-Haves

- An experiment comparing the MIA advantage when regularizing top-X% vs. random-X% vs. bottom-X% of parameters by the gradient criterion would directly validate the core assumption and substantially strengthen the paper.
- Full baseline comparisons (privacy-utility curves or P1 scores against all defense methods) on Texas, Purchase, and ImageNet would complete the SOTA claim.
- A comparison against magnitude-based pruning (with identical sparsity levels) would clarify whether PAST's advantage is specific to its gradient-based selection or achievable via simpler sparsification.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"Computing gradients of the loss gap each epoch is not trivial"** — subjective opinion; the paper quantifies overhead (10.4%), which is very low. Not a valid weakness.
- **"The normalization |M| arbitrarily up-weights larger modules"** — misreading of the formula. The |M| factor ensures the sum of γ_i over a module equals |M|, matching standard L1's per-module total regularization. This is a deliberate design choice, not an arbitrary up-weighting.
- **"Combined with other defenses (Table 2) does not compare against training longer"** — strawman; the paper's claim is that PAST improves upon existing defenses, not that it beats extended training of those defenses.
- **"The comparison in Figure 5a gives PAST an extra degree of freedom"** — both L1 (varying λ) and PAST (varying α with fixed λ) produce one-parameter families in the ablation. The critic's suggestion of per-layer λ for L1 is speculative. Both methods have one degree of freedom in the comparison shown.
- **Strength Finder's claim that 14.8%→5.2% is "relative 64.9% reduction" vs vanilla** — the paper actually compares PAST to MixupMMD at those numbers, not to vanilla. The strength (PAST beats MixupMMD) is still valid; only the specific comparison target is misidentified. This is a minor inaccuracy in the strength description, not a weakness of the paper.

## Novel Insights

The most interesting observation from these reviews is that the paper's strongest experimental evidence (the CIFAR-10/100 privacy-utility curves showing dominance over eight baselines) and its most significant evidential gap (the unvalidated gradient-based selection criterion) target different claims. The former supports the end-to-end claim that "adaptive weighting works," but the latter targets the mechanistic claim that "gradient-of-loss-gap identifies the right parameters to regularize." The paper conflates these two claims, but they are logically separable: even if the gradient criterion is not the optimal way to select parameters, the adaptive weighting framework (PAST) still shows consistent improvement over uniform baselines. Clarifying which claim the paper seeks to establish would help focus future validation experiments.

## Suggestions

1. **Validate the privacy sensitivity criterion directly.** Add an experiment that compares regularizing top-X% (by gradient of loss gap) vs. bottom-X% vs. random-X% of parameters, holding the total regularization budget and sparsity level constant. If the top-X% selection consistently yields lower attack advantage, the core motivation is confirmed; if not, the method's success may come from non-uniform regularization in general rather than targeted selection.

2. **Complete the baseline comparisons on all datasets.** Report P1 scores or attack advantage at matched accuracy for all defense methods on Texas, Purchase, and ImageNet to substantiate the full SOTA claim.

3. **Add a pruning baseline.** Compare against magnitude-based pruning (one-shot or iterative) at matched sparsity levels to disentangle the benefits of selective sparsification from sparsity itself.

4. **Elevate and discuss the non-member data requirement.** Explicitly acknowledge in the limitations section that PAST requires a holdout set from the target distribution, and discuss scenarios where this might be impractical (e.g., medical datasets where all available data is sensitive).

5. **Clearly separate the two claims** ("adaptive weighting helps" vs. "gradient of loss gap is the right selection criterion") in the paper's narrative, and present evidence for each.

## Score and Decision

The paper proposes a well-motivated idea with a clean method and generally solid experiments on two datasets where full baselines are compared. The ablation isolating the adaptive weight as the key mechanism is convincing. However, the core proxy measure (gradient of loss gap) remains unvalidated as a meaningful indicator of parameter-level privacy importance, and the SOTA claim is over-extended to datasets where only undefended baselines are reported. These are substantive but not fatal gaps — they narrow rather than invalidate the contribution. The paper is publishable with revisions.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>