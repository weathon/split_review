Now I have a clear calibration picture. Let me write the final review.

**Round 1 bracket**: The paper sits between "Evading Data Contamination Detection" (4.25) and "How much can we Forget about Data Contamination?" (6.75).

**Round 2 narrowing**: The paper is comparable to "Crosslingual Capabilities and Knowledge Barriers" (5.67) — both study multilingual LLM behavior, both have experimental design limitations — but our paper has a more novel finding. It's clearly above "Generalization v.s. Memorization" (5.00) which had more fundamental methodological issues, and below "Detecting Pretraining Data / Min-K% Prob" (6.25) which had higher impact and cleaner execution.

**Final score**: **5.5** — a paper with a genuinely novel research question and clever probe extension, but with significant experimental confounds (volume confound, no clean baseline, internal contradiction in results interpretation) that weaken the conclusions.

---

## Summary

This paper investigates whether translating English benchmarks into Arabic can mask data contamination in LLM evaluation. The authors fine-tune four open-weight models on varying proportions (0%, 10%, 50%, 100%) of Arabic-translated test data from MMLU, XQuAD, and MLQA — while all conditions also include the English test data — then evaluate on the original English benchmarks. They extend the TS-Guessing probe with a choice-reordering strategy and an Index Recall Rate (IDR) metric to detect memorization. The key empirical finding is that for some models, evaluation scores rise with contamination while TS-Guessing probes remain near-zero, suggesting translation conceals contamination signals without eliminating the performance benefit. The paper also sketches a Translation-Aware Contamination Detection (TACD) framework as a conceptual blueprint.

## Strengths

- **Choice-reordering extension of TS-Guessing with IDR metric**: The adaptation of TS-Guessing to shuffle MCQ answer choices before masking (Section 3.3, Figure 1) is a clever and non-trivial methodological contribution. The IDR metric (Section 3.4, line 183) — measuring whether the model echoes the pre-shuffle answer letter after reordering — captures a memorization signal invisible to standard exact-match or n-gram overlap methods. This probe design is well-specified and appropriately distinguishes index-level memorization from content-level reasoning.

- **Empirical demonstration that translation can mask contamination signals**: The contrast between Table 2 (evaluation scores) and Table 3a (TS-Guessing probes) provides concrete evidence for the translation-as-masking phenomenon. The cleanest example is Mistral-7B-Instruct: MMLU accuracy rises from 0.577 to 0.690 with increasing contamination, yet its TS-Guessing IDR remains at 0.000 across all contamination levels. This demonstrates that a model can benefit from memorized content that surface-level contamination probes — applied after Arabic-to-English translation — completely fail to detect.

- **Well-specified experimental paradigm with reasonable breadth**: The training condition formula D_train = D_EN ∪ D_AR(p) with p ∈ {0, 10%, 50%, 100%} (Section 3.1, lines 130-132) provides a systematic framework for varying Arabic translation exposure. The multi-model (4 models) × multi-dataset (3 benchmarks) scope shown in Table 2 provides adequate empirical breadth, with consistent MMLU monotonic trends across all four models.

## Weaknesses

### Fatal
None.

### Major

- **Training data volume is confounded with contamination level.** The training formula D_train = D_EN ∪ D_AR(p) holds D_EN constant while D_AR grows with p (lines 130-132). As p increases from 0% to 100%, the model sees strictly more total training data. Any performance improvement attributed to contamination could be partly or entirely explained by increased training data volume. The paper provides no volume-matched control (e.g., subsampling English data at lower p to equalize total examples). This confound weakens every inference about contamination effects drawn from Table 2, since observed gains conflate "more contamination" with "more training examples."

- **Sections 4.1 and 4.2 make incompatible claims about the same Table 2 data.** Section 4.1 (line 189) states that MMLU "exhibits a generally monotonic increase as contamination rises" with substantively non-flat trends (Mistral MMLU: 0.577→0.690). Section 4.2 (line 201) then claims that "across contamination levels p ∈ {10, 50, 100}%, the models exhibit approximately equal performance on all evaluated benchmarks" and describes a "near-flat trend." These two characterizations cannot both be true. Even restricting to p=10,50,100 (as Section 4.2 specifies), Mistral MMLU jumps from 0.580 to 0.690 — an 11-point gain that is not "approximately equal." The paper never acknowledges or reconciles this contradiction, undermining confidence in the interpretation of results.

- **All training conditions include English test data, limiting what can be concluded about translation-specific contamination.** The p=0 condition is not a clean baseline — it fine-tunes on D_EN, the English test data (line 130-132, described as "EN-only" at line 142). The experiment therefore measures the marginal effect of adding Arabic translations on top of English contamination, rather than isolating the effect of translation-mediated contamination. The abstract and introduction frame the paper as investigating whether "translation into Arabic conceals traditional contamination signals," but the design cannot separate translation effects from English-language contamination already present in all conditions.

### Minor

- **TS-Guessing probe lacks a p=0 baseline.** TS-Guessing is applied only at p ∈ {10, 50, 100}% (line 158), with no measurement at p=0. Without knowing baseline IDR and EM rates for a model trained only on English test data, it is harder to interpret whether observed probe results reflect contamination-specific memorization or some baseline tendency.

- **No statistical variance reported.** The paper reports point estimates from what appear to be single LoRA fine-tuning runs per condition. No standard deviations, confidence intervals, or significance tests are provided. Non-monotonic patterns (e.g., LLaMA IDR: 0.287→0.643→0.410; Gemma IDR: 0.350→0.029→0.005) may reflect noise, yet the paper offers detailed mechanistic narratives about "overfit to distributional quirks" (lines 193, 197) without variance estimates to ground them.

- **TACD framework is a conceptual blueprint, not an implemented contribution.** The abstract states the paper "propose[s] a Translation-Aware Contamination Detection framework," but Section 5.3 (line 252) explicitly characterizes it as "a forward-looking blueprint rather than a complete implementation." The three components are sensible but not operationalized. The contribution the paper delivers is narrower than the abstract suggests.

- **XQuAD/MLQA TS-Guessing probe design conflates contamination with general knowledge.** The probe masks a critical token in the question (e.g., "What is the [MASK] of France?", line 162) and treats correct completion as contamination evidence. However, a model could correctly answer "capital" from general knowledge without having memorized the specific benchmark item. The interpretation of high EM as contamination rather than general knowledge is therefore questionable for this probe variant.

- **The embedding analysis referenced in Section 4.3 lacks essential details.** The paper states "The embedding figure shows that Arabic→English translations remain close to their English originals in representation space, with high cosine similarity" (line 224) but provides no information about which model, layer(s), or similarity computation was used. This is a gap for a claim that underpins the explanation of why translation masks contamination.

### Trivial
None.

## Nice-to-Haves
- A volume-matched control condition would substantially strengthen the experimental design.
- Multi-seed fine-tuning with reported variance would add needed rigor.
- Reporting TS-Guessing at p=0 would improve probe interpretability.
- The XQuAD/MLQA probe could mask spans in the context passage rather than single question tokens to reduce conflation with general knowledge.

## Removed Points
These points were flagged for removal — treat them with caution.

- **Harsh Critic: "critical details are deferred to a stripped appendix, including all hyperparameters"** — REMOVED. The appendix was stripped by the parser; the original submission includes Appendix A with hyperparameters (Section 7, line 264).
- **Harsh Critic: TS-Guessing IDR non-monotonicity described as "strikingly non-monotonic" and entirely unexplained** — DEMOTED to Minor weakness #5. The paper does acknowledge non-monotonic patterns in Section 4.1 (lines 191-197), but the interpretations lack statistical grounding. The real problem is absence of variance estimates.
- **Strength Finder: "Honest and self-aware framing of the TACD framework"** — REMOVED. Being honest about limitations is good practice but does not constitute a concrete contribution. This is the absence of a weakness, not a strength.
- **Harsh Critic: speculative-fatal claims about appendix content** — REMOVED per hard rules. Criticisms depending on information not present in the parsed paper (speculation about stripped appendices) are invalid.

## Novel Insights
None beyond the paper's own contributions. The reviews confirm the central observation — that translation can mask contamination signals while the model still benefits — is genuinely novel, while also identifying structural experimental limitations that bound the strength of the conclusions.

## Suggestions
- The most impactful revision would be to add a volume-matched control condition (subsample English data at lower p to equalize total training examples) or to explicitly bound the confound through analysis.
- Reconcile Sections 4.1 and 4.2 explicitly: either qualify the "near-flat" claim to apply only to TS-Guessing probes, or acknowledge that MMLU evaluation scores do show non-trivial increases.
- Acknowledge upfront (in abstract and introduction) that all conditions include English test data, and frame the contribution in terms of the marginal effect of Arabic translation contamination rather than absolute translation-masking effects.

## Calibration Anchors

| Paper | Path | Avg Score | Round | Comparison |
|-------|------|-----------|-------|------------|
| Evading Data Contamination Detection for Language Models is (too) Easy | Nk1MegaPuG.md | 4.25 | R1 | Our paper is clearly better — more coherent experimental design, more novel contribution |
| Elephants Never Forget: Testing Language Models for Memorization of Tabular Data | lwtaEhDx9x.md | 4.75 | R2 | Our paper is stronger — more focused research question and clearer empirical finding |
| Generalization v.s. Memorization: Tracing Language Models' Capabilities Back to Pretraining Data | IQxBDLmVpT.md | 5.00 | R2 | Our paper has a more striking empirical finding and a more focused design |
| Crosslingual Capabilities and Knowledge Barriers in Multilingual Large Language Models | BCyAlMoyx5.md | 5.67 | R2 | Comparable — both study multilingual LLM behavior with design limitations; our paper's finding is more novel |
| Understanding Catastrophic Forgetting in Language Models via Implicit Inference | VrHiF2hsrm.md | 5.75 | R2 | Hard to compare directly (different topic), but similar quality tier |
| Detecting Pretraining Data from Large Language Models (Min-K% Prob) | zWqr3MQuNs.md | 6.25 | R2 | Our paper is below this — Min-K% Prob has higher impact and cleaner execution |
| How much can we Forget about Data Contamination? | Nsms7NeU2x.md | 6.75 | R1 | Our paper is clearly below — stronger experimental design with theoretical analysis |
| To the Cutoff... and Beyond? | m2NVG4Htxs.md | 6.75 | R1 | Our paper is clearly below — clever natural experiment with more robust design |
| Training on the Test Task Confounds Evaluation and Emergence | jOmk0uS1hl.md | 8.00 | R1 | Our paper is substantially below — exceptional paper with broad implications |

**Round 1 bracket**: 4.5–6.5. **Round 2 narrowed to**: 5.0–6.0, anchored against "Generalization v.s. Memorization" (5.00) and "Crosslingual Capabilities" (5.67). The paper lands at 5.5 — above the 5.0 paper (which had more fundamental novelty limitations) but below the 6.25 Min-K% Prob paper (which had higher impact and cleaner methodology). The experimental confounds (volume confound, no clean baseline, internal contradiction) prevent a higher score despite the genuinely novel research question and clever probe extension.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>