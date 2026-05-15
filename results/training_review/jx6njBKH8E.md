Now I have a thorough understanding of the paper and all reviewer claims. Let me construct the consolidated review.

## Final Consolidated Review

## Summary
This paper introduces a novel training data extraction (TDE) attack that amplifies memorization of pre-training data by adversarially fine-tuning a language model. The method uses DetectGPT's perturbation discrepancy to pseudo-label self-generated texts as more or less likely to contain training data, then fine-tunes the target LM via RLHF to favor low-discrepancy (more "human-like") texts. On OPT models with over 1B parameters, the attack achieves a 4–8× increase in extracted training data, supported by ablation studies showing the amplification reflects genuine memorization rather than overfitting to pseudo-labels.

## Strengths

- **Novel attack paradigm that exploits fine-tuning to amplify memorization.** Unlike prior work that treats the target LM as static and focuses on post-hoc extraction strategies (better prompts, ranking, sampling), this paper shows that an adversary can proactively increase the model's leakage of pre-training data through fine-tuning. This shifts the threat model in a practically relevant direction (Sections 1, 3).

- **Consistent and large empirical gains across model scales.** The attack produces a 4–8× increase in true positive extractions for OPT models with ≥1B parameters (e.g., 1.3B: 97→775; 13B: 193→786) and is tested across six model sizes (125M–13B), revealing that larger models are disproportionately more vulnerable (Table 2, Figure 2).

- **Ablation studies rule out trivial overfitting explanations.** Three controlled analyses (deduplication, uniqueness of extracted samples, and generation diversity via self-BLEU/unique n-grams) collectively demonstrate that the fine-tuned LM produces genuinely new memorized content rather than simply regurgitating a fixed set of pseudo-labeled texts (Tables 3–6, Section 6). Up to 98% of extractions from the fine-tuned model are unique relative to the reference model.

- **Pseudo-labeling strategy that avoids ground-truth membership knowledge.** The method uses DetectGPT's perturbation discrepancy as a relative ranking signal, bypassing the need for access to the pre-training dataset or empirical threshold selection. The sorting-based pairing heuristic is a practical compromise between random pairing and computationally prohibitive exhaustive search (Section 4.1).

## Weaknesses

### Fatal
None.

### Major

- **Missing control experiment: fine-tuning on self-generated text without the pseudo-labeling signal cannot be ruled out as a confound.** The paper's central claim is that pseudo-labeling based on perturbation discrepancy *causes* the 4–8× amplification. However, there is no experiment where the target LM is fine-tuned on the same 100k self-generated texts with random pairwise preferences (or a language-modeling objective, without any membership signal). If such a control also yields comparable amplification, the pseudo-labeling mechanism is not the driver — the observed effect could stem from any continued training on model-generated text (e.g., amplifying confident tokens, distributional shift). The existing ablations (deduplication, uniqueness, diversity) address overfitting to *specific* pseudo-labels but do not isolate whether the *preference signal* is necessary. This is the paper's most significant weakness, as it undermines the attribution of the attack's effectiveness to the proposed pseudo-labeling component rather than to fine-tuning on self-generated text in general.

### Minor

- **No direct validation that low perturbation discrepancy correlates with actual membership in pre-training data.** The attack pipeline assumes that texts with lower DetectGPT perturbation discrepancy are more likely to contain verbatim training data. The paper never validates this assumption against ground truth — e.g., by checking whether low-discrepancy generations from the reference model actually exhibit higher 50-token overlap with the training dataset. The only support offered is that an RM trained on *pseudo-labels* (not ground-truth membership) reaches ~65% accuracy on held-out pseudo-labeled pairs (Table 1). This confirms only that the discrepancy signal is learnable, not that it corresponds to real membership. The end-to-end results in RQ2 provide indirect evidence (the pipeline works), but direct validation of the core premise would substantially strengthen the paper.

- **RQ1 RM accuracy is measured against pseudo-labels, not against actual extraction success.** Table 1 reports that the RM achieves ~65% binary accuracy in distinguishing "chosen" vs. "rejected" texts. However, this metric reflects consistency with the *pseudo-labels*, not with ground-truth membership. The paper frames this as evidence that the RM can "discern generated texts containing more training data" (Section 5.1), but this conflates label consistency with real-world discrimination. An experiment correlating RM scores with actual extraction counts would clarify the gap.

- **Pairing heuristic quality is not quantified.** The sorting-based pairing strategy (top half vs. bottom half by perturbation discrepancy) is described as a "compromise" but never evaluated — e.g., what fraction of pairs are correctly ordered relative to ground-truth membership? The paper notes that the simplified DetectGPT (10 perturbations, T5-Large vs. 100 perturbations, T5-3B) may reduce label reliability but does not measure the impact of these simplifications on pseudo-label quality (Section 4.1).

### Trivial

- **Main results (Table 2) lack confidence intervals or repeated-run variance.** The paper justifies single-run evaluation by the large sample size (100k texts), which is reasonable for point estimates but error bars would aid interpretation — especially for the 8.0× increase in OPT-1.3B, which is an outlier relative to other models.

- **The maximum extracted length of 1,163 words is stated but no concrete example is shown.** A qualitative example of the amplified extractions would help illustrate the practical severity of the attack.

## Nice-to-Haves

- A control experiment fine-tuning on self-generated text with no preference or random preferences (as described in the Major weakness above).
- Direct validation of the perturbation-discrepancy-to-membership correlation by comparing discrepancy scores against suffix-array-based ground-truth membership for generated texts.
- Correlation analysis between trained RM scores and actual extraction success.
- A comparison of the sorting-based pairing heuristic against random pairing or a more optimal strategy (e.g., simulated annealing).
- Extension to a second model family (e.g., LLaMA) to assess architectural generality.

## Removed Points

- **Threat model inconsistency (white-box vs. API).** REMOVED: The paper's threat model is coherent — the adversary has full parameter access. The three motivations (open-source models, parameter extraction techniques, and fine-tuning APIs) are valid reasons why such access is realistic, not contradictory statements about the threat model. The paper never claims the adversary only has black-box API access; fine-tuning APIs for open-source models do provide parameter access. The critic misread this section.

- **Excluded datasets (CC-Stories, CCNewsV2) potentially biasing results.** REMOVED: The paper explicitly acknowledges this limitation and provides its rationale for exclusion. The critic's speculation that the excluded datasets are "especially prone to extraction" is unsupported and speculative.

## Novel Insights

The most interesting finding across the reviews is the tension between the paper's strong empirical results and the unaddressed baseline question. The 4–8× amplification is clearly real for the proposed pipeline, but without a control it remains an open question whether this amplification is attributable to the pseudo-labeling signal specifically or to any continued training on self-generated text. The ablation studies convincingly rule out overfitting to a fixed set of pseudo-labels, but they do not address this deeper attribution question. Additionally, the observation that RM accuracy on pseudo-labels *decreases* for larger target models (Table 1) while extraction amplification *increases* (Table 2) is an intriguing inverse correlation that the paper notes but does not explain — suggesting that the pseudo-labeling signal becomes weaker even as the attack becomes more effective, which merits further investigation.

## Suggestions

1. **Add a control experiment** where the target LM is fine-tuned on the same 100k self-generated texts using random pairwise preferences (or directly as a language-modeling objective, or with DPO on random pairs). If amplification drops significantly compared to the proposed method, it confirms the pseudo-labeling signal drives the effect. If amplification is comparable, the paper's contribution shifts to showing that *any* fine-tuning on self-generated text amplifies exposure — still interesting but different from the claimed mechanism.

2. **Directly validate the core premise** by computing the correlation between perturbation discrepancy and ground-truth membership (50+ token overlap with training data) on the reference model's generations. An AUC or rank correlation would settle whether low-discrepancy texts are genuinely more likely to be extractions.

3. **Clarify RQ1's framing**: explicitly note that the RM accuracy reflects consistency with pseudo-labels, not ground-truth membership, and supplement with a more direct evaluation (e.g., do RM-preferred texts actually yield more extractions in a held-out generation round?).

## Score and Decision

This paper presents a novel and practically important attack direction with striking empirical results across six model scales. The methodology is creative and the ablation studies are thorough. However, the missing control experiment — isolating whether the pseudo-labeling signal is causal or whether any fine-tuning on self-generated text would yield comparable amplification — is a significant gap that undermines attribution of the paper's central claim. This weakness is addressable but currently unresolved.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>