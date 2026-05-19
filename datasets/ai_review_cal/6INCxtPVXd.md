- Decision: Reject
- Avg Score: 4.00
- Scores: 3, 5, 5, 3
Now I have all the information needed. Let me compose the final consolidated review.

---

## Summary

This paper proposes a Discriminator-based Mode Affinity Score (dMAS) for conditional GANs, computed as the Fréchet distance between Hessian matrices of the discriminator's loss function. The authors apply dMAS to continual learning: given a target mode (new class), dMAS identifies the closest existing modes, and a weighted combination of their label embeddings is used to fine-tune the cGAN with memory replay. Experiments on MNIST, CIFAR-10/100, and Oxford Flowers show that the overall pipeline improves FID on target modes compared to prior continual GAN methods (EWC-GAN, Lifelong-GAN, CAM-GAN).

## Strengths

1. **dMAS captures the cGAN model state, unlike FID.** The paper correctly identifies that FID uses a fixed Inception network and thus cannot reflect whether the current generator/discriminator is well-trained. Table 1 provides direct evidence: when the truck source model is deliberately undertrained, dMAS selects automobile as the closest mode to bus and outperforms FID-based selection across 10/20/100-shot settings (e.g., 41.81 vs. 46.37 FID at 100-shot). This is a genuine advantage of a model-dependent affinity measure.

2. **dMAS yields consistent, semantically meaningful affinity rankings across random initializations.** Section 4.1 reports 10 trial runs with different random seeds; the standard deviation of the computed distances is low and the ordering of closest modes is preserved across runs. The resulting groupings (digits 0,6,8 close; vehicles close; animals close) align with human intuition, providing empirical evidence of robustness and stability.

3. **The mode-aware continual learning framework consistently improves FID on the target mode.** In Table 2, MA-Continual Learning achieves the best target-mode FID across all six target tasks (MNIST digit 0: 6.32 vs. next-best CAM-GAN 7.02; CIFAR-10 cat: 35.29 vs. 37.29; CIFAR-100 bus: 41.68 vs. 42.81) and the best average FID across all modes for five of six targets. This demonstrates that the overall pipeline is effective.

4. **The paper includes honest discussion of limitations.** In the Oxford Flower experiment, the authors openly note that the model sometimes generates goldquelle-like images instead of calendula due to their close resemblance (Section 4.2), and Theorem 1 is used to acknowledge that adding a new mode can degrade existing modes' performance.

## Weaknesses

### Fatal

None.

### Major

1. **The label-embedding weighting (Equation 4) contradicts the paper's stated motivation.** dMAS is defined as a distance where *0* = identical modes and *1* = completely dissimilar (line 54). Equation (4) weights the label embeddings by `s_{i*} / Σ s_i*` — i.e., larger distances receive *larger* weights. The closest mode (smallest `s`) therefore contributes the *least* to the target label embedding. This is the opposite of what the paper's narrative claims ("identifying and utilizing suitable information from previously learned modes," "closest modes' labels"). Either this is a critical error in the paper's exposition (a transformation such as `1−s` was intended but not written) or the algorithm actually uses this counterintuitive weighting, in which case the method succeeds for reasons different from those claimed. The authors must clarify what was actually implemented and either correct the formula or provide a justification for weighting distant modes more heavily.

2. **The definition of the Hessian in dMAS is ambiguous.** Section 3.1 (line 41) states dMAS is computed from "the second-order derivative of the discriminator's loss with respect to the *input*," but Section 3.2 (line 57) describes it as "quantifying the Fisher Information distance between the model *weights*." The diagonal-approximation discussion (line 50) refers to "the large parameter space," which suggests a parameter-space Hessian. The algorithm pseudocode (Algorithm 1) does not specify which variables the Hessian is taken with respect to. This ambiguity makes the method irreproducible as stated — a reader cannot determine what `H_a` and `H_b` actually represent.

3. **The experimental evaluation does not isolate the contribution of dMAS from the replay mechanism.** The continual learning pipeline uses dMAS to select modes, constructs a weighted label embedding, and fine-tunes with memory replay. The baselines (EWC-GAN, Lifelong-GAN, CAM-GAN) differ on multiple dimensions simultaneously. Without ablations that keep the replay pipeline fixed and vary only the mode-selection method (e.g., random selection, FID-based selection, a simple discriminator-feature distance, or using only the single closest mode's label without weighted combination), it is impossible to tell whether dMAS specifically drives the improvement, or whether any reasonable mode-selection heuristic (or even the replay mechanism alone) would produce similar gains. This is the paper's central claim and needs direct evidence.

### Minor

4. **Main results lack variance estimates and statistical testing.** Table 2 reports FID scores as single point values without confidence intervals, standard deviations, or significance tests. The margins over CAM-GAN are often modest (e.g., CIFAR-10 cat: 35.29 vs. 37.29; CIFAR-100 bus: 41.68 vs. 42.81). Without uncertainty quantification, it is unclear whether these differences are reliable or within run-to-run noise.

5. **The knowledge-transfer experiment (Table 1) shows only one target class (Bus).** The paper states that other scenarios show "similar performance" to FID-based transfer, but only the deliberately worst-case scenario is presented. This undercuts the claim that dMAS is generally superior to FID for mode selection — it merely demonstrates one failure mode of FID.

6. **Theorem 1 is weakly connected to the proposed method.** It states a well-known property of convex optimization (mixing two losses increases each individual loss at the joint optimum). It is not specific to GANs, dMAS, or the label-embedding mechanism, and is not used to derive any design decision. It would be more useful if the paper explained how the proposed method mitigates this trade-off despite the theoretical lower bound.

7. **No sensitivity analysis for the number of closest modes `n`.** The paper fixes `n=2` in all experiments without showing how performance varies with `n=1,3,4`. This is a natural hyperparameter of the method and its sensitivity should be reported.

8. **Computational cost is not discussed.** Computing diagonal Hessians for each source–target pair requires backward passes; for a large number of source modes this could be expensive. A brief discussion of practicality would help readers assess the method's applicability.

### Trivial

None.

## Nice-to-Haves

- A comparison against a simpler non-parametric baseline: using the discriminator's penultimate-layer features to compute a distance between class-conditional means, testing whether second-order information is necessary for good mode selection.
- An extension to sequential addition of many modes (more than two) to support the "lifelong" framing.
- An ablation with fewer target samples (e.g., 10-shot, 20-shot) in the continual learning setting (the paper only uses 100-shot there, while the transfer learning experiment uses 10/20/100-shot).

## Removed Points

- **"Standard deviation figures are mentioned but not shown in the main text."** — The paper references specific figures (`fig:mnist-distance-var`, `fig:cifar-distance-var`, `fig:cifar100-distance-var`) that exist in the original submission (likely in the appendix, stripped by the parser). This is a parser artifact, not a paper flaw.
- **"Criticism that dMAS is not compared to pixel-space distance"** (from strength finder filtering) — The harsh critic notes that "any reasonable feature representation (even pixel-space distance) would produce similar groupings." This is speculative and not backed by evidence in the review; the paper does show that the groupings are non-trivial (e.g., digits 4 and 7 grouping, which is not obvious from pixel space).
- **"Theorem 1 is completely irrelevant"** — softened to Minor because it does provide a formal acknowledgment of the trade-off, even if the connection to the algorithm is weak.
- **Strength Finder's claim about Theorem 1 being a core strength** — This conflicts with the verified weakness that the theorem is weakly connected. Removed per rules.
- **"The paper should compare against its own pipeline with random mode selection"** — This is already listed as Major weakness 3 (missing ablation).

## Novel Insights

None beyond the paper's own contributions. The two reviews agree on the core issues (weighting formula contradiction, Hessian ambiguity, missing ablations) and the core strengths (dMAS model-dependence, consistency, positive results). The key novel observation from cross-referencing the reviews is that the weighting formula issue (Major weakness 1) is more than a notational quibble — it genuinely undermines the claimed interpretation of the method. If the formula is a presentation error, the paper must be corrected. If it was implemented as written, the paper's explanation of why the method works is incorrect.

## Suggestions

1. **Fix the label-embedding formula.** If the implementation uses distances directly as written in Equation (4), explain why weighting distant modes more heavily is beneficial, or switch to a similarity-based weighting (e.g., `1−s` or `exp(−s)`). If this is a typo, provide the correct formula.

2. **Unambiguously define the Hessian.** Specify whether dMAS uses the Hessian w.r.t. discriminator *parameters* or *inputs*. If parameters, specify which layer(s). Align the main-text description with the formal definition.

3. **Add ablations that isolate dMAS.** Keeping the replay pipeline fixed, compare dMAS-based mode selection against: (a) random selection of `n` modes, (b) selection by a simple discriminator-feature distance, (c) using only the single closest mode's label (no weighting). Report whether dMAS adds value beyond these baselines.

4. **Report variances or confidence intervals** for the main FID results (Table 2), or at minimum report that results are averaged over multiple runs.

5. **Either connect Theorem 1 to the algorithm** by explaining how the proposed method specifically addresses the trade-off, or remove it.

6. **Add sensitivity analysis** for the number of closest modes `n`.
