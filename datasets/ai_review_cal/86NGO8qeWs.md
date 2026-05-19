- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 8, 6, 6
Now I have all the verification I need. Let me write the consolidated review.

## Summary

This paper introduces CompA, a suite of two expert-annotated benchmarks (CompA-order with 400 real-world instances, CompA-attribute with 200 synthetic instances) for evaluating compositional reasoning in audio-language models (ALMs), structured in the Winograd twin-sentence format. Using these benchmarks, the authors show that existing ALMs (CLAP, MMT, etc.) perform near random on compositional reasoning tasks. They then propose CompA-CLAP, a two-stage fine-tuning approach: (1) contrastive learning with LLM-generated compositionally-aware hard negatives, and (2) a novel modular contrastive loss built from template-based synthetic multi-event audio that teaches fine-grained order and attribute binding. CompA-CLAP substantially improves over baselines on both benchmarks (e.g., +16.7 text score on CompA-order, +9.5 on CompA-attribute) while preserving standard retrieval and classification performance.

## Strengths

- **First systematic study of compositional reasoning in ALMs, with novel benchmarks.** CompA-order and CompA-attribute fill a clear gap: existing retrieval benchmarks (Clotho, AudioCaps) are dominated by single-event audio where bag-of-words models can perform well. The paper demonstrates this convincingly with a word-order shuffling experiment (Fig. 1) and a noun-distribution analysis. The benchmarks are carefully designed in the Winograd twin-sentence format and, for CompA-order, draw on real-world AudioSet Strong audio with expert annotation.

- **CompA-CLAP shows large and clear improvements on real-world compositional audio.** On CompA-order (entirely real audio), CompA-CLAP raises text score from CLAP-LAION's 24.0 to 40.70 (+16.7), audio score from 9.25 to 35.60 (+26.35), and group score from 5.50 to 33.85 (+28.35). These gains on expert-annotated real audio directly support the core claim that the method teaches genuine compositional reasoning rather than exploiting synthetic artifacts.

- **The modular contrastive learning approach is cleverly tailored to the data-scarce audio setting.** Creating synthetic multi-event audio by concatenating/overlaying single-event snippets from AudioSet Strong, then generating fine-grained positives (captions of varying granularity) and negatives (by swapping order/attributes) via templates, enables scaling compositional training without requiring pre-existing compositional audio-caption pairs. This is a practical and novel contribution.

- **The method preserves standard performance while improving compositionality.** Table 1 shows CompA-CLAP's zero-shot classification and retrieval results are on par with the already-strong CLAP (ours) baseline, with minimal degradation (e.g., 89.1% vs 90.2% on ESC-50). This rules out the concern that compositional reasoning gains come at the cost of general capability.

- **Ablation studies quantify each component's contribution.** The "- Hard Negative" and "- Modular Contrastive" rows in Table 2 show that removing either stage degrades performance (e.g., CompA-order group score drops from 33.85 to 20.20 or 21.25), providing clear evidence that both stages are useful.

## Weaknesses

### Fatal
None.

### Major

- **No ablation separating architecture improvements from data improvements for the base CLAP model.** The paper trains its own CLAP using both a different text encoder (Flan-T5-large vs. RoBERTa) and a different training set (CompA-661k vs. LAION-audio-630K). Line 151 states this model "outperforms [wu2023large] on all existing retrieval benchmarks ... by 0.15%-4.67%, and CompA-order and CompA-attribute by 11.85%-23.8%." Since architecture change and data change are confounded, it is unclear how much of CompA-CLAP's subsequent compositional improvement is attributable to a stronger base model versus the compositional training losses. An ablation training the original CLAP architecture on CompA-661k (or the new architecture on LAION-audio-630K) would disambiguate this.

- **CompA-attribute uses synthetic audio (WavJourney), creating a potential confound for the attribute evaluation.** The test set for attribute binding is entirely synthetic (line 98: "we used synthetically generated audios from WavJourney"), while CompA-CLAP's modular contrastive training also creates synthetic audio via template-based concatenation/overlay. Although the training and test pipelines differ (WavJourney text-to-audio generation vs. snippet concatenation from AudioSet Strong), the shared synthetic nature leaves open the possibility that some gains on CompA-attribute reflect sensitivity to synthetic artifacts rather than genuine attribute-binding ability. This concern is substantially mitigated by the strong and uncontaminated results on CompA-order (real audio), so it does not threaten the paper's core claims, but it limits the interpretability of the CompA-attribute numbers specifically.

### Minor

- **Benchmark sizes (400 + 200) limit statistical precision.** With only 200 test instances in CompA-attribute, a 1.54 percentage-point group-score gap (e.g., 15.13 vs. 16.67 random) corresponds to roughly 3 instances. The paper reports very small standard deviations (e.g., ±0.09 for 15.13), which appear to be across random seeds rather than bootstrap confidence intervals on the benchmark. Reporting statistical significance (e.g., paired bootstrap) would help establish that observed differences reflect genuine model capability rather than noise.

- **The claim "all models … perform worse than our random baseline on CompA-attribute" (line 279) is imprecise.** On the text score, CompA-CLAP (44.28) substantially exceeds random (25.0). The shortfall is on the audio score (22.52 vs. 25.0) and the group score (15.13 vs. 16.67). The paper should qualify which metric this observation refers to, since the text-score result tells a meaningfully different story.

- **"Only train the last few layers" (line 182) is underspecified.** The number of trainable layers affects both reproducibility and the interpretation of how much the pre-trained representations are being modified. This should be stated explicitly.

- **No statistical significance testing is provided for the main CompA benchmark comparisons.** Given the small test sets, reporting whether improvements are statistically significant (e.g., via bootstrap resampling) would strengthen confidence in the results.

### Trivial
- The paper does not show example hard-negative captions generated by the LLM in the main text (though tables referenced in Section 4.4 suggest examples exist in the appendix).

## Nice-to-Haves
- An analysis of CompA-CLAP's performance on the *compositional* subsets of Clotho and AudioCaps (instances with >1 event) would bridge the gap between standard benchmarks and CompA.
- A comparison of LLM-based hard negative generation against simpler rule-based swapping (as in NegCLIP) would clarify the benefit of the LLM approach.
- Reporting inter-annotator agreement for the CompA benchmarks (especially CompA-attribute where audio is synthetic and annotation may be less natural) would strengthen benchmark trustworthiness.
- An ablation using the same 251k template-based synthetic audios with *vanilla* CLAP loss would disentangle gains from additional training data vs. the modular contrastive formulation.

## Removed Points
These points were raised by reviewers but are removed for the reasons stated:

- **Code/data not released / project page not accessible**: REMOVED per hard rule — the paper cites a project page (line 10). Per instructions, cited entities are assumed to exist and be accessible as of the review date.
- **"No examples of hard negatives are shown"**: REMOVED — the paper references Table \ref{tab:sents} and \ref{tab:comparission} in Section 4.4, and Figure reference in Section 4.3, which exist in the original submission but were stripped by the parser.
- **"Related work should compare more directly with Winoground/NegCLIP"**: REMOVED — Section 6 (lines 289-290) already discusses both Winoground and NegCLIP (Yuksekgonul et al.) in appropriate context.
- **Figure quality nitpicks (hard to read, tiny numbers)**: REMOVED — formatting artifact from PDF extraction.
- **Criticism that the paper's claim about "not better than random" on CompA-attribute is misleading because text/audio scores beat random**: REMOVED in its original form because the critic's own analysis is factually wrong — the audio score (22.52) does NOT beat random (25.0). However, the imprecision in the paper's wording is retained as a Minor weakness with corrected facts.
- **"Method improvement over CLAP-LAION may come from seeing more training data" (general synthetic-data concern)**: This is partially addressed by the ablation rows in Table 2, which show that removing either training stage degrades performance even when the same synthetic data is used. The specific concern about data quantity vs. loss formulation is retained as a Nice-to-Have.

## Novel Insights
None beyond the paper's own contributions. The reviews do not surface any genuinely novel observation that the paper itself does not already make.

## Suggestions
1. **Disambiguate architecture and data contributions**: Add an ablation where the original CLAP architecture (RoBERTa text encoder) is trained on CompA-661k, or the Flan-T5 architecture is trained on LAION-audio-630K, to isolate the source of the base CLAP improvement.
2. **Address the synthetic confound for CompA-attribute**: Either (a) collect a small set of real-world attribute-binding instances and report performance there, or (b) explicitly test whether a model trained only on real data shows a gap on synthetic vs. real attribute test sets. At minimum, add a discussion acknowledging this limitation.
3. **Report statistical significance for CompA results**: Use bootstrap resampling to compute confidence intervals on model rankings, particularly for the 200-instance CompA-attribute benchmark.
4. **Specify the number of trainable layers** in the hard-negative fine-tuning stage.
5. **Provide concrete examples in the main text**: Show an LLM-generated hard negative, a set of template-based positives at various granularities, and a success/failure case on CompA.
