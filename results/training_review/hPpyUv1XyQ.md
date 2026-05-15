Now I have a thorough understanding of the paper and can carefully verify each reviewer claim. Let me write the consolidated review.

## Summary

The paper generalizes Minimum Bayes' Risk (MBR) decoding by incorporating a posterior over model parameters into the expected risk computation, thereby accounting for weight uncertainty during text generation. This formalization yields practical sequence-level and token-level ensemble decoding strategies (Eqs. 9, 10, 13) and also provides a criterion for selective prediction. Experiments across translation, summarization, data-to-text, and regression tasks — using prompted, finetuned, and from-scratch-trained models — show consistent improvements over compute-matched single-model MBR baselines.

## Strengths

- **Principled theoretical framework**: The paper derives uncertainty-aware MBR from Bayesian decision theory (Eq. 5 in §3.1), providing a clean justification for ensembling multiple models during decoding — which prior work (e.g., Farinhas et al., 2023) used heuristically without the Bayesian connection. The paper explicitly acknowledges this prior work (§3.2 Discussion) and clarifies its own contribution as the theoretical framing.
- **Consistent empirical gains under matched compute**: Uncertainty-aware MBR improves over single-model MBR baselines across diverse tasks (Tables 1, 2, 3) while matching the number of utility computations and effective beam size. Improvements are observed not only on word-overlap metrics but also on quality estimation (COMET) and hallucination metrics (LaBSE).
- **Systematic exploration of posterior types and combination strategies**: The paper compares unimodal (IVON), multimodal (Deep Ensemble), and snapshot posteriors, alongside both sequence-level (Eqs. 9, 10) and token-level (Eq. 13) model combination, with a careful analysis of their computational trade-offs.
- **Diversity–performance correlation validated**: Figure 1 shows a clear positive trend between ensemble prediction diversity (self-BLEU) and downstream quality, and demonstrates that increasing diversity (e.g., via higher posterior temperature) directly improves decoding — connecting the mechanism to a known property of ensembles.
- **Scaling behavior characterized**: Section 4.5 and Figure 3 map how performance scales with ensemble size and hypothesis set size under different posterior types and decoding algorithms, providing actionable guidance for deployment.
- **Effective for black-box LLM ensembling**: Table 3 demonstrates that the sequence-level estimators work with zero-shot prompted LLMs where token probabilities are unavailable, showing practical utility beyond the Bayesian training scenario.

## Weaknesses

### Fatal

None.

### Major

- **The "uncertainty-aware" attribution is not disentangled from general ensemble diversity.** The paper's central claim is that accounting for *weight uncertainty* drives improvements. However, the experiments consistently show that performance correlates with prediction diversity (Fig. 1, §4.3), which is a property of *any* diverse ensemble — not specifically of a Bayesian posterior. The main experiments compare against a single-model MBR baseline, but there is no control experiment that substitutes non-Bayesian independently-trained models (e.g., multiple AdamW runs with different seeds) for the posterior samples. The paper does compare unimodal posterior samples (IVON) to Deep Ensembles (multiple IVON means, which approximate standard ensembles), and finds that the unimodal posterior — which has no training overhead — can also improve decoding (Tables 1, 2). This partially addresses the concern by showing that the posterior distribution itself (not just multiple training runs) adds value, particularly in the finetuning setting. Nevertheless, without a direct comparison to non-Bayesian ensembles, the paper overclaims in attributing gains specifically to "weight uncertainty" rather than to the well-known benefits of ensemble diversity. This is the single most significant limitation.

- **Selective prediction experiments lack external baselines.** Section 4.4 evaluates the proposed expected-utility criteria (\(s^*\) and \(\bar{s}\)) only against variants of the same method (different posteriors, hypothesis set strategies). Established abstention criteria for language models — such as maximum softmax probability, predictive entropy, or semantic entropy (Kuhn et al., 2023) — are not compared. Without these baselines, the reader cannot assess whether the proposed criteria are actually useful for selective prediction, only that they can rank outputs internally. The paper's scope in this section is explicitly comparative among its own methods (it says "We compare different methods for using expected utility as the selective prediction criterion"), but this framing does not excuse the absence of standard baselines.

### Minor

- **No variance or statistical significance measures.** All tables report single point estimates. Given that improvements are often small (fractions of a BLEU or COMET point), it is difficult to assess reliability. The paper does cite Kocmi et al. (2024) to link COMET improvements on IWSLT17 to human preference probability, which partially addresses significance for one dataset, but error bars or confidence intervals across runs are absent throughout.

- **Unimodal posterior does not consistently outperform the baseline for from-scratch models.** Table 2 shows that when training from scratch with matched compute, the unimodal posterior (IVON samples) does not always beat the single-model baseline. This weakens the generality of the "for-free improvements" claim and makes the method's effectiveness contingent on the training regime, which the paper acknowledges but does not fully explain.

### Trivial

- Figure axis labels and some table footnotes are difficult to parse in the extracted text (parser artifacts — the original submission likely formats these clearly).

## Nice-to-Haves

- A comparison of the proposed selective prediction criteria against standard abstention baselines (e.g., max softmax probability, predictive entropy, semantic entropy) with risk-coverage curves.
- A control experiment replacing posterior samples with non-Bayesian ensembles (e.g., AdamW with different random seeds) to isolate whether the Bayesian posterior provides benefits beyond diversity.
- A more fine-grained analysis of diversity vs. individual model quality in Figure 1 (e.g., controlling for mean single-model performance).

## Removed Points

These points are flagged to be removed, treat them with caution.

- **Harsh critic's claim that "the paper does not establish that modeling weight uncertainty is the reason for the observed improvements" as a fatal flaw.** The paper does compare against the single-model mean (MBR @ mean) and shows that sampling from the posterior improves upon it. The unimodal posterior (single IVON run, no extra training cost) outperforms the single-model baseline in finetuning. This provides evidence that posterior sampling — not just ensembling multiple independent runs — contributes. The missing non-Bayesian comparison is a genuine limitation (moved to Major), but the paper does not *entirely* fail to establish the value of weight uncertainty.

- **Harsh critic's claim that "the practical proposals are existing MBR procedures" as a weakness.** The paper explicitly acknowledges that Farinhas et al. (2023) uses Eq. (9) without the weight-uncertainty connection. The contribution is the theoretical unification, the systematic exploration of multiple posterior/combination strategies, and the empirical validation — not algorithmic novelty per se. This is adequately scoped.

- **Harsh critic's claim that "the introduction oversells" about lack of methods for uncertainty-aware decoding.** The paper's claim that "there is still a lack of methods that react to or adjust for this type of uncertainty during decoding" is accurate: prior ensemble MBR work did not frame itself through the lens of weight-uncertainty, and existing uncertainty-aware decoding methods are limited. This is a reasonable characterization of the gap.

- **Strength Finder's "effective for ensembling black-box LLMs" as a distinct strength.** This is genuine evidence but it is a specific instance of the broader empirical finding, not a separate contribution.

## Novel Insights

The most interesting finding beyond the paper's own claims is the asymmetry in how posterior expressiveness helps: for finetuning (LoRA), even a unimodal posterior rivals Deep Ensembles, while for training from scratch, only multimodal posteriors deliver consistent gains. This suggests that the effective "parameter uncertainty subspace" is much smaller during finetuning, making simple posterior approximations sufficient. Combined with the diversity correlation, this points toward a practical recipe: when finetuning with parameter-efficient methods, sampling from a lightweight posterior (IVON with LoRA) gives essentially "free" improvements; for full training, the extra cost of Deep Ensembles may be necessary. The scaling analysis further clarifies that the optimal combination strategy (token-level vs. sequence-level) depends on both the hypothesis set size and the decoding algorithm — a nuanced finding that goes beyond a blanket recommendation.

## Suggestions

1. **Add a non-Bayesian ensemble baseline.** Train multiple models with AdamW (different seeds) and apply the same MBR ensembling. If the Bayesian and non-Bayesian ensembles perform similarly, reframe the contribution around the theoretical justification and the "for-free" unimodal posterior improvement (which requires only one IVON run). If the Bayesian ensemble outperforms, this strongly supports the "uncertainty-aware" attribution.
2. **Add standard abstention baselines to selective prediction.** Compare \(s^*\) and \(\bar{s}\) against max softmax probability and predictive entropy on risk-coverage curves. This may require only a small additional computation.
3. **Report variance across at least 3 random seeds** for the main comparisons (Tables 1, 2) to establish whether the observed improvements are reliable.

## Score and Decision

This paper makes a solid theoretical contribution by grounding ensemble MBR in Bayesian decision theory and provides a systematic empirical evaluation across diverse settings. The weaknesses — primarily the incomplete attribution of gains to uncertainty vs. diversity, and the missing selective-prediction baselines — are real but addressable and do not invalidate the core contribution. The paper is above the acceptance threshold for a top venue.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>