Now I have a thorough understanding of the paper. Let me produce the consolidated review.

## Summary

This paper proposes a detection method for adversarial audio examples in ASR systems by extracting six statistical characteristics (median, max, min, entropy, KL divergence, Jensen-Shannon divergence) from output probability distributions at each time step, aggregating them, and training binary classifiers (Gaussian classifiers, ensembles, neural networks). The method is evaluated across multiple ASR architectures (wav2vec, LSTM, Transformer) and languages (English, Mandarin, multilingual), achieving AUROC >99% for targeted attacks. The paper also explores adaptive attacks and a filtering-based fallback defense.

## Strengths

1. **Consistent near-perfect detection across diverse ASR models and languages**: Table 4 reports AUROC exceeding 99% on clean data and 98% on noisy data for all tested end-to-end ASR systems (wav2vec, LSTM LAS, Transformer) across English (LibriSpeech), Mandarin (Aishell), and multilingual (Common Voice) corpora. This directly supports the paper's central claim and demonstrates generalization across architectures with output vocabularies ranging from 32 to 21,128 tokens.

2. **Method is simple, model-agnostic, and requires no model modification or adversarial training**: Section 4 defines a straightforward pipeline that computes six characteristics from the output distribution per time-step, aggregates them, and feeds them into standard binary classifiers. The approach works on any ASR that outputs a distribution over tokens without extra preprocessing or retraining — a practical advantage over methods requiring adversarial training or architectural changes.

3. **Systematic identification of the most discriminative characteristic**: Section 6 and Table 6 report that the mean (over time steps) of the median of output probabilities consistently provides strong discriminative power across both targeted and untargeted attacks. The paper also shows that NNs trained only on C&W attacks transfer well to Psychoacoustic and Kenansville attacks, providing practical feature selection insights.

4. **Broad evaluation coverage**: The paper tests detection across five attack types (C&W, Psychoacoustic, PGD, Genetic, Kenansville) plus adaptive attacks, using three datasets covering three languages and three distinct ASR architectures (Tables 2–7). This breadth substantiates that the method is not narrowly tuned to one attack or domain.

## Weaknesses

### Major

1. **Evaluation sample size is small and lacks statistical rigor**: The detection experiments use only 100 benign and 100 adversarial test samples per model (Section 5.1, Table 4 caption). No confidence intervals, standard errors, or bootstrap estimates are reported. While the consistent >99% AUROC across all models mitigates some concern about overfitting to a specific sample, the absence of any uncertainty quantification means the headline numbers rest on an under-powered evaluation. This is the most significant threat to the credibility of the claimed performance.

2. **Missing comparison against the most relevant prior work**: The paper compares against Temporal Dependency (Yang et al., 2019) and Noise Flooding (Rajaratnam & Kalita, 2018) — both from narrower settings (TD: single English ASR; NF: 10-word classification with untargeted attacks). However, the paper itself cites Däubener et al. (2020), who proposed detection for hybrid ASR based on two of the same uncertainty metrics (mean KLD and mean entropy). The paper does not benchmark against Däubener's approach re-implemented on the same E2E models. Without this comparison, it is unclear whether the added characteristics (median, min, max, JSD) and binary classifiers provide meaningful improvement over the simpler uncertainty-based baseline. Showing that the method outperforms TD and NF does not establish significance, as these are acknowledged to be limited.

3. **Adaptive attack evaluation is insufficiently thorough**: The adaptive attack (Section 4, Eq. 2-3) adds an L₁ penalty nudging the characteristic score toward the benign mean (for GC/EM) or the NN's benign-class output. For the NN classifier, this is a principled approach since the NN output is the classification boundary. However, for the Gaussian classifier, the attack minimizes distance to the benign mean rather than optimizing directly for crossing the classification threshold (i.e., the likelihood ratio boundary). The evaluation only tests this single heuristic configuration (α=0.3, 1000 iterations). The paper's claim that AEs become "easier to detect through filtering" depends on the adaptive AEs being noisy, but this property has not been demonstrated against a stronger, principled adversary that directly minimizes the detector's TPR. **This weakness does not invalidate the paper's core contribution** — the filtering fallback is presented as an additional empirical observation, not the central claim — but it limits the strength of the robustness conclusions drawn.

### Minor

1. **Threshold selection criterion is unusual and potentially misleading**: The paper (Section 5.3) adopts a threshold criterion of "maximum FPR below 1% (if available) while maintaining minimum TPR of 50%." Allowing TPR as low as 50% inflates the reported accuracy numbers in Tables 5 and 7. However, the primary metric (AUROC in Table 4) is threshold-independent and remains strong, so this is a presentation issue rather than a core flaw.

2. **Design choices for the aggregation and classifiers are empirically motivated but lack justification**: The paper tests 6 characteristics × 4 aggregations = 24 scores without explaining why mean-of-median works best or why the NN uses 3 layers of 72 hidden nodes. The ranking is deferred to Appendix A.2, and no ablation on architecture is provided. This doesn't threaten the main results but limits interpretability and guidance for practitioners.

3. **Detection performance on untargeted Genetic attacks is very low (e.g., 36.8% AUROC for LSTM with GC in Table 6) but downplayed**: The paper acknowledges this ("Genetic attack proves challenging to detect") and notes that untargeted attacks are "less threatening" and produce noticeable noise. While this is a reasonable defense, the low detection on a valid attack class should be presented more prominently as a limitation rather than a post-hoc justification.

### Trivial

- The caption for Table 7 reports accuracy with adaptive C&W AEs, but the text (line 164) describes the improvement as 0.57% (from 97.07% to 97.64%), which is a very small gain; the paper should clarify whether this is statistically meaningful rather than presenting it as a clear win.

## Nice-to-Haves

- Provide bootstrap confidence intervals on the AUROC for the existing 200-sample test setup to quantify uncertainty without requiring more data.
- Include an ablation comparing the proposed classifiers against a baseline using just the two Däubener metrics (mean KLD, mean entropy) on the same E2E models and datasets to isolate the value of the added characteristics.
- Add a brief analysis of how adversarial attacks distort the output distribution (e.g., does entropy increase uniformly across time steps?), giving theoretical grounding for why the characteristics work.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Adaptive attack has "no gradient at all" for the Gaussian classifier** (Harsh Critic, Critical Issue 2): Removed because it is factually incorrect. The score s^c(x) is computed from the ASR output distribution, which is differentiable with respect to the input. The L₁ penalty on the score does have a gradient through the ASR model. The paper's adaptive attack is gradient-based, just not directly optimizing the classification boundary.
- **"The method's novelty is modest relative to prior work"** / "incremental extension" (Harsh Critic, Critical Issue 4): Removed because it is a subjective judgment that conflates the paper's scope with Däubener et al.'s different setting (hybrid ASR, digit recognition). The paper extends from two metrics to six, from hybrid to E2E ASR, from single-system to multi-architecture/multi-language evaluation, and adds adaptive attacks with filtering — which is a substantive rather than incremental set of contributions.
- **"No comparison is made to filtering alone"** (Harsh Critic, Section-by-Section): Removed because filtering is introduced as a second-line defense specifically for adaptive attacks, and the relevant baseline (accuracy without filtering for adaptive AEs) is already provided in Table 7.
- **"Perceptual validation of adaptive attack noise"** (Harsh Critic, Missing Parts): Removed because the paper asserts "easier to spot" based on objective SNR measurements (max average 18.36 dB), which is a standard proxy for perceptibility. Requiring a full listening study is beyond the paper's scope.
- **"Data split details are missing"** (Harsh Critic, Section-by-Section): Weakened rather than removed. The paper mentions a held-out set for fitting Gaussians and a validation set for ranking (lines 71, 117) but does not fully specify sizes — this is a minor clarity issue, not a fatal omission. Folded into the "design choices not justified" minor weakness.

## Novel Insights

None beyond the paper's own contributions. The two reviews largely agree on the paper's empirical findings (strong AUROC on targeted attacks, broad evaluation coverage) and on the main limitation (small test sample, missing comparison to the most relevant prior work). The harsh critic's claims about gradient-free adaptive attacks and insufficient novelty were not supported by the paper text and have been removed.

## Suggestions

- **For the most impactful improvement**: Increase the evaluation's statistical credibility by (a) reporting bootstrap confidence intervals on the AUROC for the current 200-sample setup, or (b) if computational budget allows, scaling to at least ~500 benign and 500 adversarial samples per condition. Without this, the claim of >99% AUROC rests on thin evidence.
- **Add the missing baseline**: Re-implement Däubener et al.'s uncertainty-based detection (mean KLD and mean entropy) on the same E2E models and datasets to directly demonstrate the value added by the additional characteristics and binary classifiers. If these simple features already achieve >99% AUROC, the paper should be transparent about this.
- **Strengthen the adaptive attack evaluation**: Test the NN detector against a PGD-based attack that directly maximizes the detector's false negative rate through the NN's classification boundary. Report whether such AEs remain noisy. This would significantly strengthen the robustness claims.
- **Explicitly acknowledge limitations**: Add a paragraph discussing the small test set, the single-seed evaluations, and the low detection rates for Genetic attacks as limitations rather than scattering these points across the text.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>