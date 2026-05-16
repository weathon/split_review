Here is my final consolidated review.

---

## Summary

This paper proposes Semantic Entropy Probes (SEPs) — linear probes trained on LLM hidden states to predict semantic entropy (SE), a sampling-based uncertainty measure. By distilling SE into a probe that operates on a single generation, SEPs eliminate the 5–10× test-time cost of sampling-based hallucination detection while retaining much of the performance. The central empirical finding is that SEPs generalize better to out-of-distribution tasks than probes trained on accuracy labels, across five models (Llama-2 7B/70B, Mistral-7B, Phi-3, Llama-3-70B) and four QA datasets.

## Strengths

- **Computational efficiency**: SEPs reduce the test-time overhead of semantic uncertainty quantification to a single forward pass, avoiding the 5–10× cost of sampling-based methods (Section 4, Figure 1). This is a practically meaningful contribution given the adoption barriers of prior SE methods.

- **Consistent OOD generalization advantage**: SEPs outperform accuracy probes on held-out tasks across all 7 model/dataset configurations in Table 2, with ΔAUROC ranging from +2.2 to +10.5 percentage points. The trend is consistent across models (Mistral-7B, Phi-3, Llama-2 7B/70B, Llama-3-70B) and both short- and long-form generation.

- **Uncertainty predicted before generation (TBG)**: SEPs successfully capture semantic entropy from the hidden state of the *last input token*, before any output is generated (Figures 3–4). This enables uncertainty-aware deferral with a single forward pass.

- **Counterfactual validation**: The context-addition experiment (Figure 5) shows that SEP predictions shift in the same direction as ground-truth SE when the task difficulty changes, confirming the probe captures meaningful uncertainty rather than spurious correlations.

- **Comprehensive ablations**: Performance is mapped across layers, token positions (SLT/TBG), models, generation lengths, and tasks, showing that SE is broadly encoded in mid-to-late layers (Figures 1–4).

## Weaknesses

### Fatal
None.

### Major

- **No empirical comparison to other unsupervised probing methods.** The paper claims to set "a new state-of-the-art for cost-efficient hallucination detection" (lines 67, 78) and suggests SEPs "may be the best unsupervised method" (line 378), yet the only probing baseline is an accuracy-supervised probe. Several prior works propose unsupervised or self-supervised probing objectives for truthfulness that also operate on a single generation — most notably CCS (Burns et al., 2024) and the linear "truth direction" methods (Marks et al., 2023; Azaria & Mitchell, 2023). The paper reviews these in Section 2 and notes their validity has been questioned (Farquhar et al., 2023), but never *empirically* compares SEPs to them. Without this comparison, the reader cannot assess whether SE is a *distinctively* good probing target or whether *any* internal-consistency target would yield similar OOD benefits. The overclaim relative to the evidence is the paper's most significant weakness.

### Minor

- **Binarization of semantic entropy is not validated against a regression variant.** The paper converts continuous SE into binary labels via a threshold (Eq. 1) and trains a logistic regression classifier. The paper mentions alternatives such as soft labelling were explored and defers to the appendix (line 206), but the core methodological question — whether binarization discards useful signal compared to directly regressing on raw SE values — is not addressed in the main text. Since SEPs are evaluated on AUROC for a *binary* task (correct/incorrect), this may be adequate, but the paper would benefit from showing that a regression-trained probe (or that performance is robust to threshold choice) does not materially change the conclusions.

- **Generalization results are on a limited task scope (4 QA datasets) without formal significance testing.** The leave-one-out OOD evaluation uses only four datasets (TriviaQA, SQuAD, BioASQ, NQ Open), all free-form QA. The paper reports standard errors but no paired significance test (e.g., Wilcoxon signed-rank) across the 4 tasks. While the consistent advantage across 7 model/dataset configurations mitigates this, the claims about generalization beyond QA (e.g., to summarization, dialogue, reasoning) are unsupported. The paper acknowledges this in passing but the framing in the abstract and conclusions emphasizes generalization more strongly than the evidence supports.

- **Training cost of SEPs is under-discussed.** The paper emphasizes test-time cheapness but requires generating 10 samples per training query (Section 4) and running an NLI model for clustering to compute SE labels. This upfront cost is non-trivial. A transparent discussion of the total cost of producing training data (especially relative to simply using accuracy labels) would help readers assess practical trade-offs.

- **"Cheap detector" baselines are limited.** Beyond accuracy probes, the cheap (single-generation) methods compared are only log-likelihood and p(True). Other low-cost detectors such as logit-based uncertainty on the first token or internal consistency checks are not included.

### Trivial
None.

## Nice-to-Haves

- An experiment training SEPs on truly unlabelled data (e.g., LLM-generated questions) would significantly strengthen the practical appeal, as suggested in the Future Work section.
- Per-task breakdown of the leave-one-out results in a dedicated table (beyond Figure 7) showing AUROC for each held-out dataset individually rather than aggregates would clarify whether the advantage is driven by any single dataset.

## Removed Points

These points were raised by reviewers but are removed with justification:

- **"Paper provides no direct evidence that hidden states better encode SE than accuracy"** (Harsh Critic, Discussion section) — This is factually incorrect. The paper *does* provide such evidence at lines 449–451, where in-distribution AUROC for predicting SE is shown to be significantly higher than AUROC for predicting accuracy (Figures referenced as fig:acc_vs_se_prediction_id_*). The evidence may not use representational similarity analysis, but it is present and valid.

- **"Per-task results are not inspected / aggregated numbers hide dataset-driven effects"** — Per-task results *are* visible in Figure 7 (short-gen-ood bar plot) and are discussed in the text (e.g., BioASQ differences highlighted at line 383). A deeper analysis (e.g., removing BioASQ) would be a nice addition but is not absent.

- **Criticisms about missing appendix content** (soft labelling details, prompt templates, layer selection) — The parser strips appendix sections from all submissions; these exist in the original paper.

- **"Weakness about unfair comparison"** — The criticism about missing CCS comparison is retained above; it is a real gap. However, any suggestion that the paper should have used *different* baselines that would favor the reviewer's preferred method is not present here.

## Novel Insights

The reviews highlight an important distinction about the paper's contribution: the paper convincingly shows that SE is a *better supervisory signal than accuracy* for probe-based OOD generalization, but the claim that SE probes are the "best unsupervised method" conflates two different axes (supervisory signal vs. probing objective). The key insight that emerges is that *model-internal* uncertainty signals (SE) transfer better across tasks than *external* labels (accuracy) — this is the paper's real contribution. The missing comparison to CCS/Marks et al. is important because those methods also use model-internal signals (activation patterns for truthfulness) and would test whether the advantage comes from SE specifically or from using any internal consistency signal.

## Suggestions

1. **Add an empirical comparison to at least one unsupervised probing baseline** (e.g., CCS on the same hidden states and tasks). This is the single most impactful addition for supporting the "state-of-the-art" and "best unsupervised method" claims.

2. **Validate the binarization**: train a regression variant of SEP (predicting raw SE values instead of binary labels) and compare AUROC on the end hallucination-detection task. Show that the threshold (Eq. 1) is stable across tasks or that performance is robust to its choice.

3. **Add a statistical significance test** for the OOD comparison (e.g., paired Wilcoxon across the task folds).

4. **Tone down the "state-of-the-art" and "best unsupervised method" claims** to match the evidence, or qualify them as "among single-generation probing methods" / "relative to accuracy-supervised probes."

5. **Include a Limitations paragraph** transparently discussing: (a) evaluation restricted to QA, (b) only 4 datasets, (c) no comparison to other unsupervised probes, (d) upfront training cost of SE label generation.

## Score and Decision

The paper proposes a well-motivated and useful method with a clear conceptual contribution: that semantic entropy is a more transferable probing target than accuracy. The experiments are reasonably thorough across models and show a consistent and practically meaningful OOD improvement. The main weakness is overclaiming relative to the comparison set — the absence of any empirical comparison to CCS or similar unsupervised probing methods undermines the "state-of-the-art" and "best unsupervised method" framing. This is addressable with additional experiments and more measured claims. The core scientific finding (SE > accuracy as a probing target for OOD generalization) is solid and well-supported by the evidence presented.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>