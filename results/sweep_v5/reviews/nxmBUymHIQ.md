Now I have all the information I need. Let me write the consolidated review.

## Summary

This paper proposes LoLoRA, a fine-tuning method for LLMs that combines gradient-free local updates (via Hebbian PCA or autoencoder loss) on the LoRA matrix A with standard gradient-based training of matrix B. The core idea is to adapt A during the forward pass without storing its input activations, matching the memory profile of LoRA-FA (frozen A) while dynamically tracking the optimal PCA subspace. The paper also provides a theoretical result (Theorem 4.4) characterizing the optimal A under a random-regression model, showing it should span the top eigenspace of the input covariance.

## Strengths

1. **Clean theoretical characterization of optimal A under idealized conditions.** Theorem 4.4 proves that, under a random regression target with i.i.d. Gaussian weights, the expected-loss-minimizing A is any nonsingular linear transformation of the first r eigenvectors of Σ_zz. This is a neat theoretical crystallization of the intuition behind PCA-based initialization methods like EVA, and the theorem plus its autoencoder counterpart (Theorem 4.6) are presented clearly and correctly.

2. **Systematic ablation of local update rules.** Table 6 compares five local rules (HPCA, HPCA no-mean, HPCA svd-first, AE, SoftHebb) across three ranks on TinyLlama-1.1B / Alpaca, and Table 5 compares four initializations for LoRA-FA. This controlled study, spanning ranks r=2,4,8, provides a useful empirical map of which local rules work and how they compare to frozen baselines. The best HPCA and AE variants converge to perplexity within ~0.02 of full LoRA.

3. **Honest acknowledgment of limitations.** The conclusion explicitly notes that the theory assumes stationary targets in isolated submodules, which "is not strictly the case in multilayer architecture," and acknowledges the "small amount of extra optimizer state" required by LoLoRA. This transparency is commendable.

## Weaknesses

### Fatal

None.

### Major

1. **The empirical advantage over LoRA-FA (the primary baseline) is marginal or negative on most benchmarks, despite added complexity.** On GLUE (Tables 1–2), LoLoRA HPCA underperforms LoRA-FA (uniform) on 5 of 8 tasks (CoLA, RTE, MNLI, QQP, SST-2), ties on 2 (MRPC, STS-B), and is better on 1 (QNLI). On mathematical reasoning (Table 3), LoLoRA HPCA ties with LoRA-FA (EVA) at 0.829 — both are within one standard deviation of standard LoRA (0.821). On multimodal fine-tuning (Table 4), LoLoRA HPCA (perplexity 2.93) is better than LoRA-FA (uniform) (2.97) but worse than LoRA-FA (EVA) (2.92). The method is **never unambiguously better than the best LoRA-FA variant** on any benchmark, and on the largest benchmark (GLUE) it is generally worse than LoRA-FA (uniform). Given that LoLoRA adds local-update machinery (optimizer state, staleness of A in B's gradient, algorithmic complexity) that LoRA-FA does not require, the benefits do not convincingly outweigh the costs.

2. **The theoretical gap between the idealized setting and the actual deep-network scenario is significant and unbridged.** Theorem 4.4 assumes (a) i.i.d. Gaussian entries in ΔW₀ (the "target" weight change), (b) a fixed input covariance Σ_zz, and (c) isolated submodules with stationary targets. In a deep transformer where B and all other layers co-adapt, the effective target for each submodule shifts throughout training and the input distribution to each submodule changes. The paper acknowledges this in the conclusion but does not provide experiments in the setting where the theory actually applies (e.g., frozen features + linear readout), nor does it analyze whether the non-stationarity degrades the HPCA convergence. The reasoning chain from Theorem 4.4 → LoLoRA algorithm therefore relies on an untested assumption that local convergence to the instantaneous eigenspace remains beneficial as that eigenspace shifts.

3. **Memory savings over LoRA-FA are incompletely quantified and practically negligible.** LoRA-FA stores zero optimizer state for A (it is frozen). LoLoRA requires an optimizer (Opt_loc) with running means, momentum, or similar state for the local updates on A. The paper reports "peak extra GPU memory" but does not break out the optimizer state contributed by LoLoRA's local optimizer. From Table 4, the gap between LoLoRA HPCA (24.1 GB) and LoRA-FA (23.9 GB) is only 0.2 GB, virtually all of which is plausibly the extra optimizer state — meaning the memory savings over LoRA-FA are near zero. The paper's central efficiency claim ("further reducing memory") conflates savings relative to standard LoRA (which LoRA-FA already achieves) with savings relative to LoRA-FA (which are unsubstantiated).

### Minor

1. **The claim "HPCA consistently outperforms standard LoRA-FA in two out of three experimental setups" (Conclusion) is misleading.** "Standard LoRA-FA" is the uniform-initialization variant. On GLUE (the largest setup), LoLoRA does not consistently outperform standard LoRA-FA — it is worse on most metrics. On math reasoning the difference is within noise (0.829 vs 0.826). Only on the multimodal setup is LoLoRA clearly better (2.93 vs 2.97 perplexity). Counting this as "two out of three" is generous.

2. **The local update overhead in wall-clock time is significant but under-discussed.** In Table 4, LoLoRA HPCA takes 2h52m vs LoRA-FA (uniform) at 2h46m — essentially tied. But LoLoRA HPCA (EVA) takes 3h30m, substantially longer than standard LoRA (2h45m). While the paper correctly attributes this to EVA initialization, it does not discuss that the practical runtime of LoLoRA plus a competitive initialization can exceed that of standard LoRA.

3. **The LoLoRA vs. LoRA-FA comparison on GLUE uses uniform initialization for LoRA-FA but does not include LoRA-FA with HPCA-like dynamic initialization.** The most natural ablation would be LoRA-FA initialized via a single forward-pass PCA (as in EVA but without running updates). The paper compares LoLoRA only to LoRA-FA with a static EVA initialization, not to LoRA-FA that has been given the same data access for initialization.

### Trivial

None that survive filtering.

## Nice-to-Haves

- A controlled experiment on a frozen-features + linear readout setting (e.g., CIFAR-10 features from a frozen ResNet) where the stationarity assumption of Theorem 4.4 actually holds would validate whether the theory translates to practice even in that restricted regime.
- Reporting total optimizer state (including LoLoRA's local optimizer) alongside peak memory would resolve the ambiguity about actual memory savings.
- A sensitivity study on the frequency of local updates (every step vs. every N steps) could help identify whether the overhead can be reduced without harming performance.

## Removed Points

- **Criticism about "optimal initialization conflating frozen vs. locally-updated A."** The theorem characterizes the optimal fixed point for A, not the update rule. The paper uses this to motivate what subspace A should converge to; it does not claim the theorem directly proves the update rule. This is a valid use of the theory.
- **Criticism about "missing related works" or "missing appendix" content.** The appendix was stripped during parsing; these criticisms cannot be verified and may reflect parser artifacts.
- **Criticism that "the theorem is trivial" (Theorem 4.5).** Whether the result is expected does not make it incorrect; the paper uses it primarily to contrast the asymmetry between A and B.
- **Criticism that "FREE_MEMORY(z) savings are zero relative to LoRA-FA."** This is factually incorrect: LoRa-FA also does not store activations for A's backward. The memory savings of both methods over standard LoRA come from the same mechanism (no activation storage for A). LoLoRA's additional memory cost is the local optimizer state, which the paper acknowledges.
- **Generic, unsupported strengths from the Strength Finder** about "important problem" and "addressed a timely question" are removed; only concrete, evidenced strengths are retained.
- **Criticism about "the paper never being better than standard LoRA"** is factually incorrect — on Table 3, LoLoRA HPCA achieves 0.829 vs LoRA's 0.821 (higher point estimate, though within noise).

## Novel Insights

None beyond the paper's own contributions. The reviews raise a coherent meta-criticism: the paper's theoretical framing (optimal frozen A under stationary targets) and its proposed method (online local updates of A in non-stationary deep networks) operate in different regimes, and the empirical evaluation does not close this gap. The most informative section is the ablation study (Tables 5–6), which shows that any method converging to the top PCA eigenspace — whether frozen (EVA) or online (HPCA, AE) — performs similarly, and that the main cost is the gap to full LoRA, not the choice between static PCA and online HPCA.

## Suggestions

1. **Reposition the contribution.** The paper's strongest finding is that HPCA-based local updates achieve performance nearly identical to a good static initialization (EVA) without requiring a separate PCA pre-pass. The paper should lead with this practical advantage (online adaptation avoids a separate data pass) rather than overclaiming performance or memory benefits over LoRA-FA.

2. **Provide a memory breakdown.** Report total optimizer state (including Opt_loc) alongside peak memory for each method. Without this, the claim of "further reducing memory" beyond LoRA-FA is unsupported.

3. **Test the theoretical regime.** Add a simple experiment (e.g., frozen features + linear readout) where stationarity holds, as a sanity check that Theorem 4.4 translates to a real (if restricted) setting. This would strengthen the theory→method connection.

4. **Clarify the comparison framing.** When comparing to "standard LoRA-FA," specify which initialization is used (uniform). The conclusion's "two out of three" claim should be revised to accurately reflect the GLUE results.

## Score and Decision

**Calibration anchors:**
- **VeRA** (7.25, Accept) — Clean, simple method with strong experiments. LoLoRA has more theoretical depth but weaker empirical evidence and greater complexity.
- **LoRAM** (6.20, Accept) — Novel training scheme with strong memory savings. LoLoRA's memory savings over baselines are much smaller, and its experiments are less extensive.
- **ReLoRA** (5.75, Accept) — Simple, effective method with clear benefits. LoLoRA's empirical improvements are less clear-cut.
- **LoRA-FA** (5.33, Reject) — Incremental over LoRA, marginal memory benefits. LoLoRA adds theoretical grounding and ablations but the core empirical story is similarly weak.
- **Activations Aren't Cheap** (4.25, Reject) — Limited novelty, narrow impact. LoLoRA has stronger theory but the practical impact is similarly limited.
- **SiVA** (3.75, Reject) — Weak theory, limited experiments. LoLoRA has better theory and more thorough ablations.

Relative to these anchors, LoLoRA sits between LoRA-FA (5.33) and ReLoRA (5.75): it has a genuine theoretical contribution and thorough ablations that LoRA-FA lacks, but its empirical evidence does not demonstrate a clear advantage over simpler baselines, and its memory savings over LoRA-FA are unquantified and likely negligible. The contribution is incremental and the evidence is insufficient to outweigh the added complexity.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>