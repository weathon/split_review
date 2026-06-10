Now I have verified all the claims against the paper. Let me produce the final review.

## Summary

This paper proposes a frequency domain analysis framework for understanding momentum methods in deep learning. The key idea is to treat momentum updates as time-variant filters on gradient signals, with Z-transform analysis distinguishing "orthodox" (pure attenuating, like EMA-SGDM) from "unorthodox" (amplifying+attenuating, like Standard-SGDM) momentum systems. Empirical studies reveal that gradually attenuating high-frequency gradient components while amplifying low-frequency components during training improves generalization. Based on these insights, the authors propose FSGDM, which dynamically adjusts the momentum coefficient using an increasing schedule parameterized by the total training steps to achieve invariant filter characteristics across different training budgets. Experiments across vision, NLP, and RL tasks show consistent improvements over fixed-momentum SGD baselines.

## Strengths

- **Formal Z-transform derivation distinguishing orthodox from unorthodox momentum systems**: The paper derives transfer functions (Eq. 5) and magnitude responses (Eq. 6) for both coupled (EMA-SGDM) and decoupled (Standard-SGDM) momentum, then classifies them as orthodox (|H_k(ω)| ≤ 1, pure low-pass/high-pass) versus unorthodox (|H_k(ω)| > 1 possible, low/high-pass gain). This goes beyond the informal "momentum acts as a low-pass filter" observation in prior work, providing a precise mathematical grounding that directly addresses Question 1 (decoupling vs. coupling).

- **Proposition 1 — dynamic magnitude response invariance to training length**: FSGDM sets μ = c·Σ, and Proposition 1 states that fixing N and c makes the dynamic magnitude response invariant to total training steps. The heatmap experiments (Fig. 4) provide supporting evidence: optimal (c, v) zones for ResNet18/CIFAR-10, ResNet34/Tiny-ImageNet, and ResNet50/CIFAR-100 show high similarity, demonstrating that the filter characteristic — not the raw step count — is what matters for transfer across tasks with different training budgets.

- **Controlled ablation of u_t strategies that directly validates the framework's predictions**: Tables 1–2 systematically test increasing, fixed, and decreasing u_t for both orthodox and unorthodox systems. The results are consistent with the frequency framework: increasing u_t (gradual suppression of high frequencies) yields the best accuracy (77.12% with μ=1k), while decreasing u_t (retaining high frequencies late) collapses to 69.69%. High-pass momentum (suppressing low frequencies) performs worst with fixed u_t=0.9 at 53.43%. These controlled comparisons provide direct empirical support for the claim that high-frequency components are harmful late in training.

- **Consistent empirical gains across vision, NLP, and RL with a single (c, v) setting**: Using c=0.033, v=1 (found on small-scale tasks), FSGDM outperforms both Standard-SGDM and EMA-SGDM on all 7 vision model/dataset pairs in Table 3 (ImageNet ResNet50: 76.91 vs. 76.66), all 6 NLP architectures in Table 4 (Transformer BLEU: 32.40 vs. 31.50), and all 3 MuJoCo RL tasks in Fig. 5. This breadth supports the claim that the frequency-derived design principle generalizes broadly without per-task tuning.

- **Phase response derivation providing a concrete design rule**: Eq. 8 shows that v_k < 0 introduces an extra π radian phase shift, which would reverse the update direction and cause oscillations or divergence. This gives a clear, theoretically motivated criterion to select positive v_k — a practical guideline emerging directly from the frequency analysis.

## Weaknesses

### Major

- **EMA-SGDM NLP results are implausibly low, indicating a broken comparison setup rather than meaningful competition.** In the IWSLT14 experiments (Table 5), EMA-SGDM achieves BLEU scores of 4.99 (LSTM), 1.20 (LSTM-W), and 6.27 (Transformer), while Standard-SGDM achieves 28.12, 24.66, and 31.50 on the same models — a gap of 20–28 BLEU points. The paper's own framework explains the root cause: EMA-SGDM with u_t=0.9 implies v_t=0.1 (since v_t=1-u_t), which attenuates all gradient frequencies by roughly 10× relative to Standard-SGDM's v_t=1. Using the same learning rate for both thus disadvantages EMA-SGDM severely. BLEU scores of 1–5 are essentially random, suggesting the hyperparameters used (learning rate, schedule, etc.) were incompatible with the coupled formulation's 10× attenuation. The paper's claim that FSGDM "outperforms all others" in NLP is therefore misleading — outperforming a baseline that was given inappropriate hyperparameters is not informative. The comparison against Standard-SGDM (which shows an ~1 point BLEU improvement) remains valid, but the EMA-SGDM comparison in NLP is not. This concern is partially mitigated by the fact that FSGDM also outperforms Standard-SGDM (a reasonable baseline) across all 6 NLP architectures, but the paper should acknowledge and discuss this asymmetry.

- **No training hyperparameters are reported for any experiment, making the paper non-reproducible.** The paper states "keeping all other hyperparameters unchanged" (Section 3) and "we do not fine-tune every parameter for each individual model but use the same hyperparameters across all models for convenience" (Section 5), but never reveals what those hyperparameters are. Learning rate, learning rate schedule, batch size, weight decay, and data augmentation values are entirely absent from the paper. This is a basic requirement for any empirical paper, especially one that aims to compare optimizer performance — without these details, readers cannot reproduce the results, evaluate whether the conclusions generalize, or assess whether the chosen hyperparameters unfairly favor any method. The missing hyperparameters also amplify the concern above about the NLP baselines: without knowing the learning rate and schedule, we cannot distinguish between a genuine algorithmic finding and an artifact of poor hyperparameter selection.

### Minor

- **FSGDM is algorithmically identical to the increasing low-pass gain momentum studied in Section 3 (Example 3), making the optimizer contribution incremental.** The increasing low-pass gain momentum (Example 3, Section 3.2) is defined as m_t = u_t m_{t-1} + g_t with u_t = t/(t+μ). FSGDM (Algorithm 1) is m_t = u_t m_{t-1} + v·g_t with u_t = t/(t+μ) and μ = cΣ, where v=1 in practice. The only addition is the parameterization μ = cΣ to make the schedule invariant to total training steps (Proposition 1). The paper does not directly compare FSGDM against the best variant from Section 3 (low-pass gain with μ=10k achieving 80.48% on CIFAR-100 ResNet50 in Table 3 vs. FSGDM's 81.44% in Table 4). While Proposition 1 and the cross-task parameter transfer (c=0.033) are genuine contributions, the gap between FSGDM and a well-tuned increasing schedule appears modest, and the paper should explicitly benchmark against this natural competitor.

- **RL experiments report only reward curves without numerical summaries.** The RL results (Fig. 5) show curves with 75% confidence intervals but no tabulated final rewards or standard deviations. Given 10 random seeds, mean and standard error of final episode rewards should be reported numerically to allow quantitative comparison and interpretation of the claimed improvements.

- **The experimental comparison uses "same hyperparameters across all models for convenience."** While the paper is transparent about this choice (line 271), it conflates optimizer quality with hyperparameter compatibility. A fairer evaluation would tune learning rates independently for each optimizer on a validation set, or at minimum demonstrate that the reported trends hold across multiple learning rate choices. The current setup risks favoring the method whose effective update scale happens to align best with the frozen hyperparameters.

### Trivial

- None of substance (the paper is generally well-written and organized).

## Nice-to-Haves

- **Adam baseline in RL experiments**: The paper acknowledges that Adam is the default optimizer for PPO ("We replace the default Adam optimizer in PPO with FSGDM, Standard-SGDM and EMA-SGDM") but does not include Adam in the comparison. Including an Adam baseline would contextualize the practical significance of FSGDM's improvement over SGDM variants. As the paper explicitly scopes itself to SGD-based momentum optimizers, this is not a required comparison, but it would strengthen the practical claims.

- **Statistical significance testing**: The vision experiments report standard errors from 3 runs. Adding paired significance tests or confidence intervals for the FSGDM vs. Standard-SGDM comparisons would clarify whether the 0.1–1.7 percentage point improvements are statistically reliable.

## Removed Points

These points were flagged by reviewers but removed during filtering. Treat them with caution:

- **"NLP baseline results are structurally invalid and suggest a fundamental experimental error"** — removed the characterization as a "fundamental experimental error." The paper's own framework predicts that EMA-SGDM with v_t=0.1 strongly attenuates gradients, and using the same learning rate for both formulations can explain the poor EMA-SGDM results. This is a hyperparameter fairness issue, not a bug. However, the implausible magnitude of the gap (1.2 BLEU) is retained as a Major weakness.

- **"No comparison against Adam in NLP or RL experiments"** — removed from weaknesses. The paper's stated scope is "conventional SGD-based momentum optimizers" (line 271). Adam is an adaptive optimizer, not a pure momentum variant. Criticizing its absence is scope creep. Moved to Nice-to-Have.

- **"Quasi-stationary approximation limitations are underexplored"** — removed. The paper explicitly acknowledges this approximation (Section 2.1, citing standard references) and it is a reasonable engineering compromise for analyzing stagewise momentum schedules. The critic's concern about analyzing transitions between stages misunderstands the piecewise-constant analysis design.

- **"FSGDM claim of task invariance is weakly tested"** — removed. The claim is tested on CIFAR-10, CIFAR-100, Tiny-ImageNet (heatmap sweeps) AND ImageNet with ResNet50 (Table 3). This is reasonable evidence for a heuristic optimizer, not a theoretical guarantee.

- **"No comparison against learning rate schedule variants"** — removed. This asks the paper to solve a different problem (joint LR-momentum optimization) that is outside its stated scope.

- **Strengths removed** — No strengths were removed as false; all five are grounded in specific evidence from the paper.

## Novel Insights

The harsh critic insight that deserves emphasis: the paper's frequency analysis is primarily *descriptive* (characterizing what different coefficient choices do) rather than *prescriptive* (predicting which choice is optimal without experiments). The framework explains *why* increasing low-pass gain works well — it gradually suppresses high-frequency components while amplifying low-frequency ones — but the specific parameters (c=0.033, v=1) were found empirically through sweeps. The reviewer correctly notes this gap between the framing ("resolving questions from the frequency domain perspective") and the actual derivation path where the key design choices come from experiments, not from the analysis itself. This is not a fatal flaw — many useful frameworks are descriptive — but the paper's introduction is somewhat misleading about the explanatory power of the theory.

Additionally, the calibration across reviewers highlights a critical tension: the paper's frequency framework distinguishes orthodox and unorthodox momentum systems with rigorous mathematics, yet the experiments treat this distinction as a foregone conclusion by using the same hyperparameters across methods with fundamentally different amplification factors. This tension is especially acute in the NLP results where the 10× gradient attenuation of EMA-SGDM (an orthodox system) vs. Standard-SGDM (unorthodox) manifests catastrophically. The paper would be stronger if it acknowledged that its own framework predicts these systems require different learning rate calibrations.

## Suggestions

1. **Report all training hyperparameters** (learning rate, schedule, batch size, weight decay, data augmentation, optimizer-specific settings) for every experimental setup. Without these, the paper is not reproducible.

2. **Address the NLP baseline issue** by either: (a) tuning the learning rate separately for each optimizer (e.g., scaling Standard-SGDM's LR by ~0.1 for EMA-SGDM to compensate for the v_t difference), or (b) acknowledging the asymmetric comparison and discussing its implications for the claimed results. The Standard-SGDM vs. FSGDM comparison in NLP is still informative and should be preserved.

3. **Directly compare FSGDM against the best increasing low-pass gain variant from Section 3** in a controlled experiment, to demonstrate the benefit of the cΣ parameterization over a hand-chosen μ.

4. **Add a table of numerical final rewards** (mean ± std across 10 seeds) for the RL experiments to complement the reward curves.

5. **Clarify in the introduction** that the frequency framework is descriptive (characterizing filter behavior) rather than prescriptive (deriving optimal coefficients), to better align reader expectations with what the analysis actually delivers.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Reject</decision>