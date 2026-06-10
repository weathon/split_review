## Summary

The paper introduces Fuzzed Randomized Smoothing (FRS), a defense against textual backdoor attacks in pre-trained language models. FRS combines randomized smoothing with MCTS-based "fuzzing" to identify vulnerable text segments and concentrate randomization there, alongside a biphased parameter smoothing scheme that avoids the computational overhead of training separate models on randomized datasets. The theoretical analysis (Corollary 1) shows that the proposed targeted randomization multiplicatively expands the certified robustness radius relative to uniform randomization, and experiments across three datasets, three attack types, and models up to 8B parameters demonstrate strong empirical defense performance.

## Strengths

- **MCTS-guided targeted randomization is a novel and well-motivated idea.** Section 4.3 presents a concrete algorithmic instantiation (selection via UCB, expansion guided by linguistic features, simulation via KL-divergence scoring, backpropagation) that adapts software fuzzing concepts to discrete text for backdoor defense. This departs from the uniform randomization of standard randomized smoothing and targets a real limitation (poison-agnostic passive defense).

- **Biphased parameter smoothing addresses a practical bottleneck.** Section 4.2 avoids the prohibitive cost of training \(K\) separate models on \(K\) randomized datasets by smoothing only the top-\(H\) layers' parameters with Gaussian noise during fine-tuning and inference. This makes the approach computationally plausible for large PLMs where prior randomized smoothing work would be impractical.

- **Consistent empirical advantage across a 73× model-size range.** Table 4 evaluates FRS against TextGuard on BERT-base (110M) through LLaMA3-8B (8B), covering both encoder and decoder architectures. FRS achieves higher CA, PA, and lower ASR on every configuration, demonstrating that the benefits generalize beyond a single model scale.

- **Ablation study confirms both modules contribute.** Table 3 shows that removing either the biphased model parameter smoothing or the fuzzed text randomization degrades performance, with the worst degradation under combined removal. This provides clear causal evidence for each component.

- **Operates in the realistic post-attack setting without poisoned data access.** The paper correctly identifies (Section 1, lines 16–18) that in pre-training-phase backdoor attacks, the defender lacks access to poisoned training data—a constraint many existing defenses do not satisfy. FRS performs defense during fine-tuning and inference only.

## Weaknesses

### Fatal

None.

### Major

1. **The empirical "certified robustness radius" measurement does not follow a formal certification protocol.** Section 5.2.2 measures robustness radius as "the maximum percentage of tokens that can be perturbed while the model still maintains correct prediction with high probability." This is an empirical search for the largest perturbation the model survives, not a certification bound derived from the noise distribution and a binomial confidence interval as in standard randomized smoothing (Cohen et al., 2019). In standard certification, the radius follows analytically from the lower bound on the majority-class probability; here the paper searches empirically and calls the result "certified." Since the paper's title and central framing hinge on *certifying* robustness, this disconnect is significant. The theoretical analysis (Corollary 1) claims a broader *certified* radius, but the experiments validate at best a broader *empirical* robustness radius. The claim that "Corollary 1 is persuasively validated with empirical results" (line 273–274) overstates what the empirical protocol can establish.

2. **Assumption 1 (Effective Parameter Smoothing) is not properly justified.** The assumption states that the smoothed model's output on benign inputs matches the clean model's output. The paper asserts this "can be approximately guaranteed with the biphased parameter smoothing... as long as η in Eq. 4 is set small enough" (line 197), but provides no proof, no quantitative analysis of what "small enough" means, and no discussion of how the added Gaussian noise \(\epsilon_{\text{top-}H}\) affects output distributions. The entire certification chain (Theorem 1 → Corollary 1) depends on this assumption—if it fails, the theoretical guarantee does not hold.

3. **The theoretical bound does not account for MCTS failure probability.** Theorem 1's bound uses \(\Delta = 1 - \omega^{R_r L}\), which assumes the trigger segment falls entirely within the identified vulnerable area \(T(\mathbf{x}')\) and that randomization probability \(\omega\) is applied uniformly there. If MCTS fails to locate the trigger (or identifies a segment that does not overlap with the actual trigger), the effective randomization probability on the trigger reverts to \(\omega_L\) rather than \(\omega_H\), and the bound collapses. The paper acknowledges that "with more MCTS iteration budget, the confidence that the trigger is successfully captured can be higher" (line 219) but provides no analysis, empirical measurement, or probabilistic bound on MCTS's success rate. A certification guarantee that depends on an unmeasured search procedure is incomplete.

### Minor

4. **Only one certified defense baseline is compared.** The paper compares against seven empirical defenses but only one certified defense baseline (TextGuard). While TextGuard is the most directly relevant certified method, and the paper notes that vision-domain randomized smoothing methods (Xie et al., 2021; Weber et al., 2023) are not easily ported to text, a single certified baseline limits the strength of the comparative claim. Expanding the certified baseline set would strengthen the evaluation.

5. **No variance or statistical reliability reporting.** Experiments are run five times with different random seeds (line 251), but no standard deviations, confidence intervals, or detailed t-test results are reported anywhere. The \(^*\) markers in table captions indicate "\(p<0.01\) on \(t\)-test" without specifying which comparisons were tested or what the null hypothesis was. This makes it impossible to assess whether reported improvements are statistically reliable.

6. **Key MCTS hyperparameters are not specified.** The number of MCTS iterations per test sample, the exploration constant \(C\), and the mutation set \(M\) are described conceptually (Section 4.3) but no concrete values are given in the implementation details (Section 5.1). Without these, the results cannot be reproduced.

7. **No runtime or computational cost measurements despite "efficient" in the title.** The paper claims defense efficiency as an advantage but provides no wall-clock time, FLOP counts, or inference latency comparisons. A method that performs per-input MCTS search on potentially large models (including LLaMA3-8B) needs efficiency measurements to substantiate this claim. The only efficiency argument is theoretical (broader radius with the same \(K\)) and about training cost reduction via parameter smoothing—both valid but insufficient without empirical cost data.

### Trivial

None.

## Nice-to-Haves

- A control experiment that applies higher randomization probability to *randomly chosen* segments (rather than MCTS-identified ones) would isolate whether the improvement comes from the MCTS targeting or simply from non-uniform randomization.
- A sensitivity analysis of hyperparameters \(\sigma\), \(H\), and \(K\) would help assess robustness to these choices.
- An adaptive attack discussion would strengthen the security analysis, though this is not standard for all defense papers.

## Removed Points

These points were raised by reviewers but are excluded from the main weaknesses above:

- **"Defender cannot access θ_F to verify the defense goal"** — The paper defines the *goal* of certified robustness as behavior consistent with a clean model. This is a target definition, not a verification procedure the defender must execute. Removed as a misunderstanding of the formulation.
- **"Fuzzing analogy is loose and not substantiated"** — This is a subjective framing judgment. The paper explicitly adapts the *concept* of proactive search for vulnerabilities, not the specific mechanisms of software fuzzing. Removed as framing preference rather than a substantive flaw.
- **"Corollary 1 does not connect to Neyman-Pearson certification"** — The paper does not claim a connection to the Neyman-Pearson framework; it operates within its own theoretical setup. Removed as factually incorrect about what the paper attempts.
- **"Low probability that input-level randomization undoes pre-training backdoors"** — This claim is speculative and not grounded in the paper's content. The paper's experiments show empirically that the approach works. Removed as not verifiable from the paper.
- Various typos, formatting nitpicks, and style complaints — Removed per formatting-artifact rules.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Implement a proper certification protocol.** Measure and report the certification rate (fraction of test samples certifiably robust at a given radius), derived from the binomial confidence bound on the majority vote as standard in randomized smoothing. This would directly validate the theoretical claim of broader *certified* radius.

2. **Provide empirical evidence for Assumption 1.** Measure the agreement rate between the smoothed model \(\tilde{f}(\mathbf{x},\tilde{\theta}_F)\) and a clean model \(f(\mathbf{x},\theta_F)\) on benign inputs across different \(\eta\) values to show the assumption holds in practice.

3. **Measure and report MCTS trigger-finding success rate.** For a subset of test samples with known trigger locations, report the fraction of cases where MCTS-identified vulnerable areas overlap with the actual trigger. A bounding analysis on how missing the trigger affects the certification guarantee would strengthen the theory.

4. **Report standard deviations** for all main results (Tables 1, 2, 4) and specify the exact t-test comparisons underlying the \(^*\) markers.

5. **Specify all MCTS hyperparameters** (iteration budget per sample, exploration constant \(C\), mutation set \(M\)) and include a runtime comparison against baselines.

---

**MY FINAL SCORE: <score>5.0</score>**

**MY FINAL DECISION: <decision>Reject</decision>**