- Decision: Accept
- Avg Score: 5.50
- Scores: 5, 6, 6, 5
Now I have a thorough understanding of the paper and can verify all claims. Let me write the final consolidated review.

## Summary

The paper proposes CURE, an adversarial training framework with three components: (i) selective weight conservation/updating based on a Robust Gradient Prominence (RGP) score that measures gradient importance on both natural and adversarial samples, (ii) a revision model updated via stochastic momentum, and (iii) a KL consistency loss between revision and training models. The method is motivated by a layer-wise empirical study showing that freezing certain blocks while updating others improves the robustness-generalization trade-off. Experiments on CIFAR-10, CIFAR-100, and SVHN report favorable trade-offs (via a new NRR metric) and Δ=0 robust overfitting (best = last accuracy).

## Strengths

- **Insightful layer-wise empirical motivation (Section 3).** The analysis freezing/reinitializing individual blocks in ResNet-18 and measuring resulting natural/robust accuracy and CKA representation similarity provides genuine, grounded motivation for selective updating. The finding that updating middle blocks (U-23) yields better trade-offs and reduced overfitting is a direct precursor to the method design, giving readers a clear *why* before the *how*.

- **Full elimination of robust overfitting in reported results (Table 3).** CURE achieves Δ=0.00 for both natural and AutoAttack accuracy on PreActResNet-18 and WideResNet-34-10, meaning the best observed checkpoint and the final checkpoint have identical accuracy. Every baseline method (AT, TRADES, AWP, KD, TE, IDBH) shows a negative Δ for AA, indicating performance decline. This is the paper's most striking empirical result.

- **Competitive individual accuracy numbers across architectures and datasets (Tables 1–2).** On CIFAR-10 (WRN-34-10): Nat 87.05, PGD20 58.28, C&W 55.25 — the highest natural accuracy among all methods shown and competitive adversarial accuracy. On SVHN (ResNet-18): Nat 92.77, PGD20 61.56, C&W 57.34 — clear improvements over baselines. These individual numbers are verifiable independent of the undefined NRR metric.

- **The RGP criterion is a principled and novel idea (Section 4, Eq. 5).** Using gradient norms from *both* natural and adversarial samples with a balancing coefficient α to decide per-weight updates (rather than manual layer freezing or full-network updates) is a clever, well-motivated mechanism that operationalizes the empirical insights from Section 3.

## Weaknesses

### Major

- **NRR metric is introduced but never defined (structural evaluation gap).** The paper states "We introduce the Natural-Robustness Ratio (NRR) metric to quantify the trade-off" (line 159) and uses NRR as a headline claim ("CURE achieves the highest NRR among all methods"). Yet the formula for NRR is never given — not in the main text or any visible section. The table captions say "NRR quantifies the trade-off between natural performance and C&W attack results" (lines 165, 190), but this describes *what* it measures, not *how* it is computed. Without the formula, the paper's central quantitative claim cannot be evaluated, reproduced, or compared against future work. This is not a minor omission — a metric used as a primary evaluation criterion must be explicitly specified.

- **No ablation study isolating CURE's three components.** CURE consists of: (i) RGP-based gradient masking (the core conceptual contribution), (ii) a revision model with stochastic momentum update, and (iii) a KL consistency loss between revision and training model. The revision-with-consistency-regularization component is structurally similar to mean teacher / knowledge distillation — a well-known technique that alone can improve accuracy and reduce overfitting. Without an ablation that separates these components (e.g., comparing full CURE vs. RGP-only vs. revision-only vs. RGP+revision w/o consistency loss), the paper cannot rule out that revision + consistency loss accounts for most of the gains. This means the purported benefit of the selective update mechanism (the paper's main novelty) is confounded with a known technique.

- **Perfect Δ=0.00 results require clarification (Table 3).** CURE shows Δ=0.00 for *both* natural and AA accuracy on *both* PreActResNet-18 and WideResNet-34-10 — i.e., best and last accuracies are identical to two decimal places across all four cells. Given that adversarial training test accuracy typically fluctuates by at least a few tenths of a point epoch-to-epoch, and that "best" and "last" are undefined in the paper (no explanation of whether "best" is best over all epochs, and "last" is the final epoch, or whether validation-based checkpoint selection was used), this perfect alignment requires explanation. Was the "last" checkpoint chosen to coincide with the best? Are numbers rounded from a very small but non-zero gap? The paper should state the epoch budgets, whether early stopping was used, and ideally show error bands over multiple runs to substantiate the overfitting claim.

### Minor

- **Natural corruption evaluation lacks baseline comparisons (Figure 5/Fig. cor).** The paper shows CURE's performance on 15 corruption types (blur, digital, noise, weather) but does not overlay any baseline methods in the figure or discuss comparisons in the text. Without a reference point, this experiment does not support comparative claims about corruption robustness. Adding even a single baseline (e.g., AT, TRADES) would make this section meaningful.

- **No statistical variance reported.** All results are point estimates from single runs. Adversarial training, particularly robust overfitting measurements, exhibits non-trivial variance across seeds. While single-run reporting is common in this subfield, reporting at least one multi-seed experiment (e.g., on the primary CIFAR-10 WRN setting) would substantially increase confidence in the results, especially given the striking Δ=0 claim.

- **Abstract claims about "memorization" are not empirically supported.** The abstract states that CURE "effectively tackles both memorization and overfitting issues," but no analysis of memorization (e.g., per-sample memorization metrics, influence functions, or training set label leakage) is presented. The text mentions memorization only in passing (line 127: "avoid memorization"; line 241: "memorizes adversarial examples"). This is an overclaim relative to what the paper demonstrates.

### Trivial

- None that are not already absorbed into higher-tier weaknesses.

## Nice-to-Haves

- **Specify computational cost.** The method requires gradient computation for both natural and adversarial samples plus forward/backward passes for the revision model consistency loss. Reporting relative training time vs. standard AT would help practitioners assess the practical overhead.

- **Add a larger-scale dataset.** The current evaluation is limited to CIFAR-10, CIFAR-100, and SVHN (resolution ≤32×32). Even a single experiment on Tiny ImageNet or a downsampled version of ImageNet would strengthen the claim of being "dataset- and architecture-agnostic."

- **Clarify gradient mask recomputation frequency.** Is the RGP mask recomputed every iteration, every epoch, or once? This affects both overhead and behavior.

## Removed Points

These points are flagged to be removed per filtering rules; treat them with caution:

- **Missing hyperparameter values (p%, α, γ, r, d) and training details.** Per hard rule: "REMOVE nitpicks about reproducibility such as undisclosed hyperparameters, trivial implementation details, or large artifacts impractical to include in a submission." These details may exist in the (stripped) appendix.

- **"Missing related works"** and **"missing entries in tables"** (e.g., ST-AT C&W for WRN). Per rules: do not mention missing related works; missing table entries are a presentation detail that the full submission would resolve.

- **"Method may not work on large-scale datasets."** This is pure speculation with no evidence either way.

- **Strength Finder's claim about "robustness to natural corruptions showing improved accuracy over baselines."** The paper does not overlay baseline methods on the corruption figure or discuss comparisons in the text. This strength claim is unverifiable from the given content.

- **"The adversarial examples are generated to maximize KL divergence (Eq. 4) but RGP uses CE loss — inconsistency."** This is not an inconsistency: the KL divergence generates adversarial perturbations (a standard TRADES-style inner maximization), while the RGP score (Eq. 5) uses cross-entropy gradients to measure weight importance on both distributions. These are different objectives serving different purposes.

- **"Two decimal Δ=0 is impossible" / speculation about cherry-picking.** The Δ=0 concern is valid and retained (Major tier), but the speculative assertion of deliberate gaming without evidence is removed. The concern is about insufficient explanation, not fraud.

## Novel Insights

The two reviews in combination surface one genuine insight beyond the paper's own contributions: the paper's empirical analysis in Section 3 (showing that freezing early layers and updating middle/late layers improves trade-off) is its strongest evidence, but the proposed method's direct connection to this analysis is weaker than it first appears. The empirical study freezes entire blocks; the method operates at the weight level via gradient masking. Neither review demonstrates that the weights CURE freezes correspond to the blocks the empirical analysis identifies as worth freezing. This disconnect — between the block-level finding and the weight-level mechanism — is a missed opportunity for validation that would strengthen the paper's narrative considerably. A simple experiment overlaying the RGP mask pattern on the frozen-block results from Section 3 would directly validate whether RGP discovers the same conservation patterns as the manual analysis.

## Suggestions

1. **Define NRR explicitly** with its formula, and justify why it is preferable to reporting individual accuracy numbers or existing trade-off metrics.

2. **Add a component ablation** on at least one dataset/architecture pair: (a) full CURE, (b) CURE without revision (RGP masking + standard AT loss only), (c) CURE without RGP masking (revision + consistency loss only, all weights updated), (d) standard AT baseline. This is the single most important addition to substantiate the paper's core claim.

3. **Clarify the Δ=0 results**: define "best" and "last," report the epoch budget, state whether any form of checkpoint selection was used, and show accuracy curves with multiple seeds (error bands) over the full training trajectory for CURE vs. baselines.

4. **Add baseline comparisons to the natural corruption figure** so readers can assess whether CURE's corruption robustness is genuinely better than alternatives.
