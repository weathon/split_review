- Decision: Reject
- Avg Score: 3.00
- Scores: 3, 5, 1, 3
Now I have all the information I need. Let me construct the final consolidated review.

## Summary
2-3 sentence summary of the paper's contribution.

## Strengths
List concrete, verified strengths.

## Weaknesses
Organized by severity. I need to carefully verify each claim from both reviewers against the actual paper text.

Let me construct the review now.

---

First, let me verify a few more details about the ablation reporting:

1. Line 273: "Without a batch normalization layer, over 9 runs, the best model gets an E2EE of 71%" — so the paper reports 9 runs for this ablation but only reports the best, not the distribution. This is valid criticism.

2. Line 274: "when started with the annealing algorithm's final and penultimate δ values, the model converged to E2EE values of 68% and 71% respectively" — no mention of number of seeds. Valid criticism.

3. Figure 5 (error-vs-sparsity): The caption doesn't mention error bars or number of runs. The paper does elsewhere note "9 seeds" for some experiments. But this figure description lacks such info. Valid criticism.

Now let me finalize.## Summary

This paper introduces Sparling, a method for learning intermediate representations with extreme activation sparsity (≥99%) using only end-to-end supervision. The technique combines a spatial sparsity layer (quantile-adjusted ReLU with per-channel thresholding) and an adaptive annealing schedule that gradually reduces density based on validation accuracy. Experiments on three domains (DigitCircle, LaTeXOCR, AudioMNIST) demonstrate that the learned sparse layers accurately localize ground-truth motifs despite no direct motif supervision, and achieve density levels (0.005%) that L1 or KL-regularized baselines cannot reach while maintaining low motif error.

## Strengths

1. **Extreme sparsity levels demonstrated quantitatively**: Table 1 reports Sparling achieves a density of 0.005% on DigitCircle (99.995% sparsity), which is ~4.6× sparser than the best L1 baseline (0.023%) — and the KL baseline cannot go below 0.1%. This directly supports the paper's central claim that Sparling "enforces levels of activation sparsity unachievable using other techniques."

2. **Motif identifiability validated across three diverse domains with multi-seed statistics**: Figure 1 (caption: "bar height depicts the mean across 9 seeds, while individual dots represent the individual values and the error bar represents a 95% bootstrap CI of the mean") shows motif errors (FPE, FNE, CE) all averaging below 10% on DigitCircle and AudioMNIST, with proper statistical reporting including individual seed values and confidence intervals. The inclusion of an AudioMNIST held-out test set (speakers 52–60) provides evidence that learned motifs generalize rather than memorize.

3. **Annealing strategy proven necessary through clear ablation**: Section 5.2 (line 273-274) shows that removing batch normalization causes failure (best of 9 runs: 71% E2EE), and starting directly at the final density also fails (68% and 71% E2EE). This demonstrates that both components of the method are essential.

4. **Minimal end-to-end degradation after retraining**: Figure 4 and the associated text show that removing the sparsity bottleneck and fine-tuning only the output head recovers performance close to the Non-Sparse baseline, indicating the sparsity constraint does not permanently degrade model capacity — a useful sanity check that strengthens the contribution.

## Weaknesses

### Fatal
None.

### Major

1. **KL-divergence baseline comparison lacks a proper table.** The paper states that "the KL-divergence was unable to achieve a density below 0.1%, even when we used a loss weight as high as λ = 10^5 and 3 × 10^6 steps" (line 253), and concludes KL is "unsuitable." This provides *some* quantitative information, but there is no table comparable to Table 1 for L1 (which shows density, FPE, FNE, CE, E2EE across multiple λ values). The reader cannot evaluate whether alternative hyperparameter configurations of KL might perform differently, or compare the full cost-accuracy profile. Given that the paper's claim of "unachievable using other techniques" (abstract) depends on the baseline comparisons, this asymmetry in reporting quality is a significant gap.

### Minor

2. **AudioMNIST ground-truth motif pipeline is underspecified.** The paper describes AudioMNIST as "synthesiz[ing] short clips of audio representing sequences of 5-10 digits over a bed of noise" from AudioMNIST samples (line 210). For motif evaluation (FPE, FNE, CE), ground-truth motif locations must be known — presumably temporal intervals for each spoken digit. The paper does not describe how these intervals are determined (e.g., are they aligned to the original isolated digit recordings? inferred from synthesis parameters?). This is a reproducibility gap; other researchers cannot replicate the motif evaluation on this domain without this information.

3. **Weak statistical reporting for key ablations and the sparsity-error tradeoff figure.** (a) The "without batch normalization" ablation reports "over 9 runs, the best model gets an E2EE of 71%" — only the best is reported, not the distribution. (b) The "without annealing" ablation reports only two E2EE values (68%, 71%) with no indication of how many seeds were tried. (c) Figure 5 (error-vs-sparsity) shows curves without error bars or any statement about whether it reflects a single run or multiple seeds. Since the paper uses 9 seeds for its main motif error figure and reports 95% CIs there, the lack of comparable statistical rigor on these central results weakens confidence.

4. **Information bound derivation (§2.5) has an undefined variable.** The derivation (lines 131-140) introduces η (eta) in the inequality H(M[i,c]) ≤ H(B(δ_{i,c})) + ηδ_{i,c}, but η is never defined anywhere in the paper. The section even bears the label \label{sec:defines-eta}, yet η is never defined. The chain-rule justification is also not clearly justified. This section is not needed for the paper's empirical contributions, but as written it is mathematically incomplete and could mislead readers. The authors should either define η properly and justify the steps, or remove this section.

### Trivial
- The minimum batch size condition (|z_n|δ ≥ 10C, footnote on line 173) is stated without justification for the specific constants.

## Nice-to-Haves
- **Sensitivity analysis for adaptive annealing hyperparameters**: The paper uses a single set of parameters (M=2e5, d_T=1e-7, δ_update=0.75). A brief ablation on one domain showing robustness to these choices would strengthen the engineering contribution.
- **Comparison to post-hoc thresholding**: Discussing whether one could simply train a non-sparse model and then threshold activations at test time, and why this would not recover motifs.
- **Limitations discussion**: The paper's Motif Identifiability claim depends on sparsity, locality, and necessity assumptions. A brief discussion of settings where these might fail (e.g., overlapping motifs, continuous-valued motifs) would improve completeness.

## Removed Points
*These points were identified in the reviews but removed after verification against the paper text. They are retained here for reference but should not be weighted in the assessment.*

- **"Per-channel vs. global threshold not clarified"** (harsh critic): The paper is clear on this — line 177 explicitly states: "q is applied across all dimensions except the last: it produces a value for each channel that represents the threshold u for which the proportion of elements above u in the tensor at that channel is δ." The paper correctly states that δ is enforced per-channel. This point reflects a misreading, not a paper flaw.
- **"Theoretical connection to information bottleneck as a strength"** (strength finder): The derivation in §2.5 has an undefined variable (η) and unjustified steps. It cannot be claimed as a strength in its current form; it is a weakness (captured above as Minor #4). Claiming this as a strength would require the derivation to be correct and complete.
- **"Missing related works"**: Not included per instructions (cannot confirm existence of external references).
- **Formatting/style nitpicks and typos**: Removed per instructions (parser artifacts, not author errors).

## Novel Insights
None beyond the paper's own contributions. The key finding — that an adaptive quantile-based sparsity layer, annealed via validation accuracy, can achieve density levels an order of magnitude below what L1 or KL losses can reach, and that this extreme sparsity is necessary for recovering ground-truth motifs — is the paper's own contribution rather than an insight synthesized from the reviews.

## Suggestions
1. Provide a table for the KL-divergence baseline (analogous to Table 1 for L1) with multiple loss weights and the resulting density, FPE, FNE, CE, and E2EE values. This is essential for substantiating the claim that KL is unsuitable for the target sparsity regime.
2. Add error bars or multi-seed trajectories to Figure 5 (error-vs-sparsity), and report the number of seeds used for the annealing ablation.
3. Describe the AudioMNIST synthesis pipeline in detail, including how ground-truth motif temporal intervals are determined.
4. Either fix the information bound derivation (define η, justify the chain-rule step) or remove §2.5 entirely — the paper's empirical contributions stand without it.
5. Add a brief sensitivity analysis for the adaptive annealing hyperparameters (δ_update, M, d_T) on at least one domain.
