Now I have a thorough understanding of the paper. Let me produce the consolidated review.

## Summary

This paper introduces a novel training data extraction (TDE) attack that adversarially fine-tunes a pre-trained language model to amplify its exposure of the original pre-training data. The key idea is to pseudo-label the model's own generations using perturbation discrepancy (from DetectGPT), then fine-tune the model via RLHF to favor responses predicted to contain more memorized training data. On six OPT models (125M–13B), the attack yields a 4–8× increase in extracted training sequences for models over 1B parameters, with ablation studies showing the gain reflects genuine memorization rather than overfitting to noisy labels.

## Strengths

- **Novel attack paradigm that amplifies memorization rather than extracting from a fixed model.** Prior TDE attacks are post-hoc (better prompts, sampling, ranking). This paper proposes actively fine-tuning the LM to increase its tendency to regurgitate pre-training data (Section 1, "This strategy differs from prior studies by aiming to intensify the LM's retention of its pre-training dataset"). This opens a new vector of privacy risk.

- **Large and consistent empirical gains across model scales.** Table 2 (tab:precision) reports a 4–8× increase in true positives for all OPT models with ≥1B parameters (e.g., OPT-1.3B: 97 → 775, ×8.0). The improvement is systematic — every model size shows an increase, and the gain grows with model scale (Figure 2, fig:size_tp), consistent with and extending the known log-linear relationship between size and memorization.

- **Ablation evidence rules out trivial overfitting explanations.** After deduplication, amplification persists (up to 8.4× for OPT-1.3B, Table 3); 70–98% of extracted samples from the fine-tuned LM are unique — not overlaps with reference-LM extractions (Table 4); and diversity metrics (self-BLEU, unique n-grams) show the model does not collapse (Tables 5–6). Together these indicate genuine memorization enhancement, not memorization of pseudo-labels.

- **Pseudo-labeling method avoids hard membership thresholds.** By comparing relative perturbation discrepancy between paired generations (Section 4.1) rather than applying an absolute threshold, the approach sidesteps a key difficulty in prior membership-inference-based attacks (mattern2023membership).

## Weaknesses

### Fatal
None.

### Major

- **The pseudo-labeling proxy is not directly validated against ground-truth training data membership.** The attack's core assumption is that texts with lower perturbation discrepancy (more "human-like" per DetectGPT) are more likely to contain verbatim training data. The paper validates only that an RM can learn to discriminate perturbation discrepancy differences between text pairs (~62–70% accuracy, Table 1). This confirms step one of a two-step chain, but the link from "lower discrepancy" → "contains training data" is not independently verified. A direct check is missing: sample generated texts, compute their ground-truth overlap with training data (using the same suffix-array method as the main evaluation), and measure whether the pseudo-labels correlate with actual membership. Without this, one cannot rule out the possibility that the RM is detecting a correlate of fluency or topic rather than memorization. The indirect evidence (the fine-tuned LM produces more true positives) is suggestive but does not isolate the mechanism — the fine-tuning could be amplifying training-data exposure for reasons other than the pseudo-labels correctly identifying member texts. This is the most significant gap in the evidence chain.

### Minor

- **Main attack results lack error bars or repeated runs.** Table 2 reports a single set of true-positive counts per model. The paper justifies this with "generating 100,000 massive texts can reduce bias for true positives" (Table 2 caption), which addresses sampling variance in text generation. However, variance from other stochastic components — RM training seeds, PPO random seed, dataset split for RM training vs. PPO — is not quantified. Because the headline claims (4–8× increase) depend on these numbers, readers cannot assess their stability. The RM accuracy in Table 1 is averaged over 5 seeds; the same diligence applied to the full pipeline would strengthen confidence.

- **No utility metric for the fine-tuned model.** The attack's diversity analysis (Section 6.3) reports that self-BLEU decreases after fine-tuning and interprets this as "improved diversity." However, a decrease in self-BLEU could also indicate reduced coherence (the model generating less structured text). Without a held-out perplexity or similar quality metric, the "diversity" interpretation is ambiguous. Even though attackers may not prioritize utility, understanding the cost of amplification (does the model become nonsensical?) matters for assessing practical risk.

- **Fraction of failed RM training runs is not reported.** The paper notes that some RM training runs produced "flawed learning outcomes" (accuracy converging to 0 or not improving) and repeats training until 5 valid results emerge (line 324). The paper's justification (an adversary can repeat until success) is reasonable, but the failure rate itself is informative — a high failure rate would mean the attack is unreliable in practice. Reporting the number of discarded runs would allow readers to assess practical robustness.

### Trivial

- Table 1 caption says "Epoch 0 denotes before RM's training starts," but epoch 0 accuracies range from 49.7–52.2%, not exactly 50%. A brief explanation (e.g., due to finite sample size or inherent asymmetry in the paired dataset) would avoid confusion.

## Nice-to-Haves

- **Comparison with a simpler supervised baseline.** The RLHF pipeline skips the SFT step (line 214). A natural baseline is supervised fine-tuning on the "chosen" texts directly (i.e., supervised learning to minimize loss on low-discrepancy generations). This would isolate whether the RL/PPO component is necessary or if simpler optimization suffices.
- **Sensitivity analysis for excluded datasets.** CC-Stories and CCNewsV2 were excluded for practical reasons (lines 285–286). A small-sample overlap check against these datasets would bound the potential undercount.
- **Acknowledgment of parameter-extraction scale limitations.** The threat model invokes model extraction techniques (Carlini 2020, Wu 2023) which have been demonstrated on smaller neural networks. Explicitly noting that full parameter extraction for >1B LMs is not yet demonstrated in practice would sharpen the threat model's realism.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

1. **Claim that excluded datasets could systematically bias findings** (critic: "if those datasets contain disproportionately more extractable sequences..."). This is speculation without evidence. The paper explicitly acknowledges the exclusion as a limitation (line 638). It is not a concrete weakness.

2. **Claim that deduplication results show amplification comes from "repetition" not "new memorization."** For 5 of 6 model sizes, the amplification after deduplication is stable or increases (e.g., 1.3B: 8.0× → 8.4×). Only OPT-13B drops (4.1× → 2.6×). The generalization that "a nontrivial portion" comes from repetition is not supported by the data.

3. **Criticism that Section 7 (mitigations) is "entirely speculative."** This is a Discussion section, explicitly described as exploring potential defenses (line 589: "we discuss two potential defense strategies"). The paper appropriately does not claim experimental validation.

4. **Criticism about "cherry-picking" RM training runs.** The paper justifies this directly: "an adversary can also control RM's fine-tuning, hence repeating training until success is deemed reasonable" (line 324). The remaining point (reporting failure rate) is kept as a Minor weakness.

5. **Request for statistical significance test on Figure 2 gap.** The linear approximation shows a clear visual trend. Significance testing is not standard for this type of empirical attack evaluation, and the consistent pattern across 6 model sizes is itself strong evidence.

## Novel Insights

The reviews surface one genuinely novel observation not emphasized in the paper itself: the deduplication results (Table 3) reveal an interesting asymmetry — after deduplication, the amplification factor *increases* for smaller models (125M: 1.7× → 2.5×; 350M: 1.6× → 2.1×) but *decreases* for the largest model tested (13B: 4.1× → 2.6×). This suggests that the mechanism of amplification differs by scale: for smaller models, the fine-tuning enables access to *new* memorized sequences that were latent but rarely generated; for the largest model, a greater proportion of the gain comes from generating the same memorized sequences more frequently. This scale-dependent distinction is worth exploring in future work.

## Suggestions

- Directly validate the pseudo-labeling assumption: compute ground-truth training data overlap for a sample of generated texts and measure its correlation with perturbation discrepancy. This single experiment would substantially strengthen the paper's core evidence chain.
- Repeat the full pipeline (RM training + PPO + evaluation) for at least one model size (e.g., OPT-1.3B or 2.7B) across 3–5 seeds and report the range of true-positive amplification.
- Report a utility metric (perplexity on WikiText-103 or a held-out portion of the Pile) for the fine-tuned models, to disambiguate the diversity interpretation and quantify the utility cost of the attack.

## Score and Decision

This paper presents a genuinely novel attack scenario with clear empirical results. The core idea is original and practically motivated. The main weakness — that the pseudo-labeling proxy is not directly validated against ground-truth membership — is a real evidential gap, but it does not invalidate the paper's contribution; it weakens the mechanistic understanding. The evidence chain (RM learns perturbation discrepancy → fine-tuning with this RM amplifies exposure) is indirect but coherent, and the strength of the empirical results (4–8× amplification, consistent across scales, robust to deduplication) makes the central claim credible. With the suggested direct validation, the paper would be very strong. In its current form, it is a solid contribution with one significant but addressable gap and several minor concerns.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>