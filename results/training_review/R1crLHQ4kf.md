I now have a thorough understanding of the paper. Let me write the consolidated review.

## Summary

This paper proposes a detection framework for adversarial audio examples targeting ASR systems. The method extracts seven statistical characteristics (median, min, max, entropy, KLD, JSD of the output token probability distribution per time step, plus the median of probabilities) from any E2E ASR system's per-step output distribution, aggregates them over time, and feeds the resulting features into binary classifiers (Gaussian, ensemble, or neural network). The approach is tested across three ASR architectures (wav2vec CTC, LSTM LAS, Transformer), multiple languages, and several attack types, reporting AUROC values above 99% on clean data.

## Strengths

- **Simple, broadly applicable detection strategy.** The method requires no model modification, adversarial training, or data preprocessing — it works with any E2E ASR system that outputs token-level probability distributions. This is a genuine practical advantage.

- **Consistently high reported performance across diverse architectures and conditions.** The claimed AUROC exceeds 99% on clean data across three fundamentally different ASR architectures (wav2vec CTC, LSTM LAS, Transformer) with output vocabularies ranging from 32 to 21,128 tokens, across multiple languages (English, Mandarin, multilingual Common Voice). The method maintains >98% AUROC on noisy data, showing robustness to acoustic perturbations. Results in Tables 4 and 5 consistently and substantially outperform the implemented NF and TD baselines.

- **Demonstrated transferability.** Classifiers trained on C&W attacks transfer to Psychoacoustic attacks (Table 6, mean-median GC and NN columns) and achieve >90% AUROC against untargeted Kenansville attacks — a meaningful generalization property.

- **Computational efficiency.** Detection adds only ~18.74ms per sample on an A40 GPU, suitable for near-real-time deployment.

- **Intellectually honest treatment of adaptive attacks.** The paper acknowledges that the core detection mechanism can be evaded under full-knowledge adaptive attacks, and explores a separate filtering-based fallback. The qualitative finding that adaptive attacks produce noisier examples (max average SNR 18.36 dB vs. 31–54 dB for standard attacks) is useful information for the community.

## Weaknesses

### Fatal
None.

### Major

1. **Small test sets with no uncertainty quantification undermine the headline claims.** The entire detection evaluation uses only 100 benign + 100 adversarial test utterances per model (Sec. 5.1). At an observed AUROC of 0.99 with 200 samples, the 95% confidence interval spans roughly 0.96–1.0. No confidence intervals, bootstrapped estimates, or variance measures are reported anywhere. The paper's central quantitative claim (AUROC >99%) is presented without the statistical grounding necessary to assess its reliability. This is not a fatal flaw — the consistent pattern across models and conditions is compelling — but it substantially weakens the evidential basis for the strongest claims.

2. **Adaptive attack classifier performance is asserted but never numerically reported.** The paper states that "the accuracy of our classifiers experiences a substantial decline across all models due to adaptive attacks" (Sec. 5.3) but provides **no table or figure** showing the actual AUROC or accuracy values for the proposed classifiers (GC, EM, NN) against adaptive attacks. The paper immediately pivots to filtering results (Table 7). Without seeing the magnitude of the decline, the reader cannot evaluate whether the core defense degrades gracefully or collapses entirely. This is a critical omission that breaks the evidentiary chain for the paper's story about adaptive attack robustness.

3. **The filtering-based fallback is evaluated only against a single adaptive attack variant (GC-targeted), and not against attacks designed to evade filtering itself.** The adaptive attack is constructed against a GC optimized for the best characteristic (Table 2 caption). Whether this attack generalizes to the NN/EM classifiers that the paper recommends is unclear. Moreover, the filtering detection (WER/CER comparison) is not stress-tested: an adaptive attacker aware of the filtering step could potentially minimize the filtering-induced transcription change. The filtering results in Table 7 show promise but do not constitute a systematic defense evaluation.

### Minor

1. **Missing modern baselines.** The paper compares against NF and TD, both of which the paper itself acknowledges as weak (TD previously evaded; NF only tested on 10-word systems). No comparison is made with the uncertainty-based detection approach of Däubener et al. (2020), despite the paper citing this work and sharing two of its metrics (mean entropy, mean KLD). Implementing these as baselines would substantially strengthen the comparative evaluation.

2. **NN training data size is ambiguous and overfitting is not addressed.** The paper reports training 3×72-unit fully-connected layers but never clearly states how many training samples are used. With 200 total samples and 100 held for testing, training data appears to be ≤100 samples (possibly less with validation splits). No regularization, validation curves, or cross-validation are reported. Given that the 7 characteristics are aggregated to single scores per utterance, the effective feature dimensionality is small — but the paper does not demonstrate that the NN generalizes rather than memorizes.

3. **Adaptive attacks are generated against the GC and tested against all classifiers (NN, EM).** While the paper describes the mathematical formulation for adaptive attacks against NN and EM classifiers (Sec. 4), the actual generated attacks target the GC (Table 2 caption). It remains an open question whether attacks specifically optimized against the NN or EM would be more effective against those classifiers.

### Trivial

- The paper truncates audio to 5 seconds for computational efficiency but does not discuss whether the proposed characteristics behave differently on longer utterances — a scope limitation worth stating explicitly.
- The relationship between the 100 benign test samples and 100 adversarial test samples (whether they are paired or independent) is not clearly stated.

## Nice-to-Haves

- **Report confidence intervals or bootstrapped AUROC ranges for all main results.** This would address the most serious concern about statistical reliability.
- **Provide a table showing the actual classifier AUROC/accuracy decline under adaptive attacks** (before filtering), so readers can assess the severity.
- **Include Däubener et al.'s uncertainty-based detection as a baseline.** Since the paper already computes entropy and KLD, adding this baseline requires minimal additional effort and would strengthen the comparative claims.
- **Test filtering against adaptive attacks specifically designed to evade the filtering step** (e.g., attacks that minimize WER/CER difference after filtering).

## Removed Points

- *"Tables hard to parse due to formatting" / "tables contain mixed values like 98.6 and percentages"* — Parser artifacts from PDF extraction; not issues in the original submission.
- *"No analysis is given for which aggregation works best or why"* — The paper states this analysis is in App. A.2, which was stripped by the parser.
- *"The paper never justifies why the median probability would differ between benign and adversarial inputs"* — The paper provides empirical justification via histograms (Figure 2) and grounds the characteristics in prior work (Däubener et al., Meyer et al.). A theoretical explanation would be nice but the lack is not a weakness.
- *"Threshold selection makes aggregate comparisons misleading"* — The paper is transparent about the fixed operating point (max 1% FPR, min 50% TPR) and reports per-model results; this is standard practice, not a confound.
- *"The NN trained on vanishingly small data almost certainly leads to severe overfitting"* — The overfitting concern is valid (kept as a minor weakness), but the absolute language ("certainly," "severe") overstates what can be concluded without evidence. Adjusted to a more measured concern.

## Novel Insights

The most interesting observation emerging from these reviews is the fundamental tension between the paper's two defense stages: the core distribution-characteristic detector is fragile under adaptive attacks (as the paper honestly reports), but the resulting noisier adversarial examples are easier to detect through signal-processing filtering. This creates a natural "arms race" dynamic where attack strategies that evade one detection modality strengthen the other. The paper does not fully develop this insight — for instance, it does not characterize the joint operating characteristic of the combined defense — but the observation itself is valuable. A second insight is that the median of output probabilities, despite being near-zero for large vocabularies, empirically carries strong discriminative signal across all tested architectures, which is somewhat counterintuitive and merits further analysis.

## Suggestions

1. **Report the magnitude of the adaptive-attack classifier decline.** Add a table (or extend Table 7) showing AUROC/accuracy for GC, EM, and NN classifiers on adaptive attacks **before** filtering. This is essential for readers to evaluate the severity of the degradation.

2. **Add confidence intervals.** Bootstrap the AUROC estimates for all main results (Tables 4, 5, 6) to quantify statistical uncertainty. This is especially important given the 200-sample test sets.

3. **Include uncertainty-based detection baselines.** Implement the mean-entropy and mean-KLD thresholds from Däubener et al. as a comparison point, since these metrics are already computed.

4. **Clarify the training setup for the NN.** Specify the exact number of training examples, whether a separate validation set is used, and whether any regularization (dropout, weight decay) is applied.

5. **Test adaptive attacks against the NN and EM classifiers**, not just the GC, to verify whether the results of the GC-based adaptive attack generalize.

## Score and Decision

The paper proposes a simple and practically appealing method for detecting adversarial audio examples. The strengths are real: generality across ASR architectures, computational efficiency, and consistent outperformance of existing baselines. However, the evaluation has two significant gaps that undercut the core claims: (1) the small test set (100+100 samples) without confidence intervals makes the headline >99% AUROC numbers hard to assess; (2) the adaptive attack analysis never reports the actual classifier performance decline — the reader is told it drops substantially but cannot see by how much. These gaps are addressable with additional experiments and reporting, but in the current form, the paper's evidence does not fully support its claims. The core idea has merit and the paper would benefit from a strengthened evaluation.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>