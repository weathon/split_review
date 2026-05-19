- Decision: Accept
- Avg Score: 5.40
- Scores: 5, 8, 6, 5, 3
Now I have a thorough understanding of the paper and can cross-check every reviewer claim. Let me produce the consolidated review.

## Summary

This paper presents SparsyFed, a method for sparse training in cross-device federated learning that combines Powerpropagation weight reparameterization, adaptive layer-wise activation pruning, and TopK weight pruning before communication. The key idea is to enable dynamic sparse masks that maintain client consensus while reducing communication and computation. Experiments on CIFAR-10, CIFAR-100, and Speech Commands with ResNet-18 show accuracy competitive with dense models at sparsity levels up to 95%, exceeding ZeroFL and FLASH baselines, with measured communication reductions up to 19.29× versus the dense model.

## Strengths

- **Consistent accuracy advantage across sparsity levels.** Table 1 shows SparsyFed outperforming ZeroFL, FLASH, and TopK at every tested sparsity level (90%–99.9%) and across all three data heterogeneity settings (IID, α=1.0, α=0.1). The advantage is particularly clear at 90–95% sparsity where accuracy approaches or exceeds the dense baseline — this is the core empirical contribution and it is well-supported.

- **Measured communication reduction with accuracy maintained.** Section 5.2 and Figure 6 (left) report downlink communication reductions: 19.29× versus the dense model and 1.66× versus ZeroFL. The paper correctly notes that FLASH has comparable communication costs (0.97×) but lower accuracy, and that SparsyFed achieves higher accuracy at any given communication budget. This is an honest, evidence-backed comparison.

- **Quantitative demonstration of mask consensus.** Section 5.3 (Figure 6 right) directly measures global model sparsity across rounds. SparsyFed maintains sparsity close to the 90% target, while ZeroFL drops below 47% and TopK below 83%. This is a concrete, visually supported finding that explains why SparsyFed's communication advantage holds in practice.

- **Ablation studies isolate component contributions.** Section 5.4 ablates three reparameterization methods (fixed-mask, spectral, Powerpropagation) and Section 5.5 ablates activation pruning, with results reported for multiple sparsity levels and heterogeneity settings. This gives readers a clear picture of which components drive the gains.

## Weaknesses

### Fatal
None. The core empirical findings (accuracy at high sparsity, communication savings, mask consensus) are supported by the experiments. The issues below are serious but fixable.

### Major

- **The "200× per-round weight regrowth" claim is unsubstantiated.** The abstract (line 4) states SparsyFed "achieves a per-round weight regrowth 200 times smaller than previous methods." No experiment in the paper defines this metric or reports a 200× factor. Section 5.3 shows that SparsyFed maintains ~90% global sparsity while ZeroFL drops below 47% — which qualitatively demonstrates much lower regrowth — but the specific quantitative claim of 200× has no supporting evidence. The paper must either present the experiment that computes this number or retract the claim. A headline quantitative contribution in the abstract that is untraceable in the evaluation body is a significant reliability issue.

- **The "adaptation to never-seen data distributions" claim is untested.** The abstract and introduction (line 4, lines 12–14) frame plasticity to "never-seen data distributions" as a key advantage over fixed-mask methods. All experiments use static LDA partitions with fixed α. There is no evaluation involving concept drift, changing client populations, mid-training distribution shifts, or temporal non-stationarity — precisely the scenarios the plasticity argument motivates. Section 5.3's mask consensus analysis on a static distribution does not demonstrate adaptation to unseen distributions. The paper should either add such an experiment (e.g., two-phase training with different α values) or clearly scope the claim to static heterogeneous distributions. This is a structural mismatch between motivation and evaluation.

### Minor

- **The "single hyperparameter" claim is imprecise.** The paper states it "only needs a single hyperparameter" (abstract) and that Powerpropagation introduces "only one hyperparameter" (line 69). However, the method also requires setting the global target sparsity ŝ (line 73), which directly trades off accuracy vs. communication and is a tunable design choice in practice. Powerpropagation's β is the *only new* hyperparameter added beyond standard FL, and the paper should clarify this rather than claiming a single hyperparameter outright.

- **No variance or uncertainty quantification for main results.** Table 1 reports accuracy without standard deviations or multiple seeds. Federated learning is high-variance, especially at α=0.1 non-IID settings. Without some measure of uncertainty, it is impossible to assess whether SparsyFed's reported advantages over baselines are statistically significant. The community increasingly expects multi-seed reporting for FL experiments.

- **Activation pruning harms accuracy at extreme sparsity — this trade-off should be more prominently acknowledged.** Table 2 shows that at 99.5% and 99.9% sparsity, removing activation pruning *improves* accuracy (especially under α=0.1). The paper (line 152) acknowledges degradation "under extreme sparsity" and justifies activation pruning for computational speedup. This is a reasonable trade-off, but since extreme sparsity is the regime the paper emphasizes (up to 99.9%), the negative impact should be discussed more directly rather than described as "minimal impact at higher density levels."

### Trivial
- The text mentions "fig. 3.right" (line 134) in Section 5.3 which seems to be a cross-reference error (likely should refer to a panel of Figure 6).
- Algorithm 2's description of how per-layer activation sparsity s_{t,l} is derived from weight sparsity (line 9 of the algorithm description in Section 3) could be stated more explicitly for reproducibility.

## Nice-to-Haves
- An ablation of Powerpropagation β over a range (e.g., β∈{1,2,3,4}) would strengthen the claim that the method introduces minimal hyperparameter tuning burden.
- Including FedDST as an additional baseline would broaden the comparison, though the existing baselines (ZeroFL, FLASH, TopK) are the most directly relevant dynamic/fixed-sparsity methods.

## Removed Points
*These points were raised by reviewers but removed after verification against the paper. They should be treated with caution.*

- **"Hardware measurements (wall-clock time, FLOPs, energy) are missing"** — The paper explicitly states (line 19) that FLOP/memory reduction requires "suitable hardware support" and focuses its evaluation on accuracy and communication cost, which is a valid scoping choice given that communication is the primary bottleneck in cross-device FL. The paper does not claim measured speedups.
- **"FedDST is not included as a baseline"** — The paper cites FedDST in related work and positions itself relative to it. Including every related method as an experimental baseline is not feasible. The chosen baselines (ZeroFL, FLASH, TopK) are the most relevant for the dynamic-vs-fixed-mask comparison.
- **"Larger models and more architectures should be tested"** — Requesting an entirely different architecture (e.g., transformer for Speech Commands) is scope creep. The paper evaluates on three datasets covering two modalities (vision, audio) with ResNet-18, which is a standard benchmark choice for the sparse FL literature.
- **"The plasticity strength" (Strength Finder #5)** — Conflicts with the verified weakness that plasticity to unseen distributions is not experimentally tested. Per the merging rules, the weakness wins, so this strength is removed.

## Novel Insights

The most useful insight from the review process is that the paper has two tiers of claims: the well-supported ones (accuracy at high sparsity, communication savings, mask consensus) and the overclaimed ones (200× regrowth, adaptation to unseen distributions, single hyperparameter). The meta-review pattern reveals that the paper would be substantially stronger if it either produced evidence for the ambitious claims or retracted them and let the solid-but-more-modest contributions speak for themselves. The disconnect between the abstract's sweeping framing and the paper's actual evaluation scope is the single issue that, if addressed, would most improve the paper.

## Suggestions

1. **Either substantiate or remove the "200× per-round weight regrowth" claim.** If a precise definition and calculation exist, add an experiment (e.g., a table measuring the average number of weights transitioning from zero→non-zero per round for each method, with the ratio). Otherwise, remove the claim from the abstract and let the qualitative mask consensus finding (Figure 6 right) stand on its own.

2. **Scope the plasticity claim to match the evaluation.** Replace "never-seen data distributions" with language about robustness to heterogeneous *static* distributions, or add a dedicated plasticity experiment (e.g., switching from α=1.0 to α=0.1 midway through training and measuring accuracy recovery).

3. **Clarify the hyperparameter claim.** Rephrase as "adds only one new hyperparameter (β) beyond the target sparsity ŝ required by all sparse FL methods."

4. **Add uncertainty quantification.** Report at least 3 seeds with mean and std for the main accuracy table.

5. **Acknowledge the activation pruning trade-off more directly** in Section 5.5 — state clearly that at sparsities >99%, activation pruning reduces accuracy but is retained for computational benefits, and quantify the speedup if possible.
