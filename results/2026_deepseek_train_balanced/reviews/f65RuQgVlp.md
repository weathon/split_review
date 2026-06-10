## Summary

This paper introduces an online-FCL (Federated Continual Learning) scenario where data arrives in single-pass mini-batches, and proposes a memory-based approach using Bregman Information (BI) — an epistemic uncertainty estimate derived from a bias-variance decomposition of the cross-entropy loss — to select representative samples for replay. The method is evaluated across vision (CIFAR, medical imaging) and text datasets, against ER, uncertainty-score baselines (LC, MS, RC, EN), and generative FCL methods (MFCL, FedCIL), showing consistent improvements on the forgetting metric.

## Strengths

1. **Novel application of BI for memory management in FCL.** The paper is the first to use the Bregman Information (variance term from a bias-variance decomposition of cross-entropy) for sample selection in federated continual learning. The BI estimator is principled: it captures epistemic uncertainty about the data-generating process rather than aleatoric uncertainty captured by standard confidence scores (Section 3.2, Eq. 1, Figure 2). This connection is clearly motivated.

2. **Broad and challenging evaluation.** The paper evaluates on 7 datasets across 3 modalities: standard vision (CIFAR-10/100), imbalanced biomedical imaging (CRC-Tissue, KC-Cell), and text (20NewsGroups, DBPedia, Yahoo Answers). The medical datasets with realistic imbalance are a meaningful departure from standard benchmarks, and the results on these datasets (e.g., CRC-Tissue M=120: BI bottom-k 62.33% accuracy, 7.99% forgetting vs. next-best RC bottom-k 58.81% accuracy, 8.71% forgetting) demonstrate the method's practical value.

3. **Consistent advantage on the forgetting metric.** Across nearly all settings, BI bottom-k achieves the best or near-best *forgetting* among the uncertainty-based strategies. On CIFAR-10, BI bottom-k achieves the lowest forgetting at M=200 (35.77), M=500 (24.59), and M=1000 (19.07). On text datasets, BI achieves the best forgetting in all 6 configurations (Table 4). This pattern is the paper's most robust empirical finding.

4. **Practical design choices tailored to the online setting.** The burn-in period (30 batches) and jump parameter (q=5 communications per task) address real instabilities in online-FCL that don't arise in offline settings. These are clearly motivated in Section 3.3 and are sensible innovations.

## Weaknesses

### Fatal
None. The paper's core claim — that BI-based memory management can reduce forgetting in online-FCL — is supported by the evidence, albeit with important caveats.

### Major

1. **The forgetting metric is never defined.** The paper repeatedly reports "last forgetting (F)" across all tables but provides no definition of how it is computed. In continual learning, forgetting formulations vary (e.g., average per-task performance drop, maximum per-task drop, or variants). Without knowing the exact formula, readers cannot interpret the paper's central quantitative claims, and results are not reproducible. This is a basic methodological omission that must be addressed.

2. **Statistical evidence is weak for a claim of superiority.** All experiments use only 3 random seeds. On multiple comparisons, BI's advantage over the next-best uncertainty score falls within one standard deviation — e.g., 20NewsGroup M=60 forgetting: BI 29.98±1.37 vs. CBR 30.39±0.80; CIFAR-10 M=1000 accuracy: BI bottom-k 35.83±2.60 vs. EN top-k 36.25±1.22. With 3 seeds, standard deviations are unreliable estimates, and no statistical tests are performed. The paper claims "superiority" (conclusion, line 889) but the evidence supports a more measured claim: BI is competitive with and often ahead of other uncertainty scores on forgetting, with a modest and sometimes overlapping margin.

3. **Text experiments use frozen pretrained embeddings, limiting the cross-modality claim.** For text, the method uses e5-small-v2 as a fixed, pretrained sentence embedder outside the learning loop (Section 4.1). Gaussian noise is then added to these frozen 384-dimensional representations for TTA. This means: (a) the method is not learning text representations, only classifiers on top of them; (b) the embedder was trained on web-scale data that may overlap with evaluation datasets, a potential leakage not discussed; (c) the text setup is structurally different from the vision experiments where the CNN is trained from scratch. The paper's claim of modality-generality is valid for the BI *estimator* (which only needs logits), but the text pipeline depends on an external model not available in many federated settings. This should be acknowledged as a limitation.

### Minor

4. **Generative baseline comparison framing could be sharper.** The paper includes MFCL and FedCIL as baselines (Table 6) and concludes that the proposed method "outperforms state-of-the-art methods." This is accurate but underspecified: these generative methods were designed for *offline* FCL, and the paper itself explains they cannot function in the online setting (Section 5). The 2×–3× accuracy gaps in Table 6 are unsurprising given the setting mismatch. The paper's real comparative strength is against ER, CBR, and the uncertainty scores (LC, MS, RC, EN) — the comparison against generative methods is better framed as a demonstration of why offline methods fail online, not as head-to-head competition.

5. **Evaluation protocol is underspecified.** The paper does not describe how "last accuracy" and "last forgetting" are measured — e.g., whether the global model is evaluated on a held-out test set, whether it's a client-average, or whether tasks are evaluated jointly or separately. This information is needed to interpret the numbers.

6. **Number of perturbations (P) for TTA estimation not stated.** The BI estimator (Eq. 1) depends on a set of P perturbations, and the paper notes "the number of augmentations is important" (Section 5), but the value used in experiments is not given. This is a key hyperparameter for the BI estimate.

### Trivial
- None beyond the omissions noted above.

## Nice-to-Haves

- Increase the number of random seeds (≥10) and report confidence intervals or effect sizes for the main comparisons.
- Include ablation results for the burn-in period and jump parameter in the main text rather than only in the appendix.
- Add a discussion of how the choice between bottom-k and top-k interacts with different uncertainty scores (the paper uses bottom-k for BI but the optimal strategy varies across scores).

## Removed Points

These points were flagged by reviewers but are removed or demoted after cross-checking against the paper:

1. **"Comparison against generative baselines is structurally invalid / circular."** The paper transparently explains that generative methods fail because the online setting violates their offline assumptions (Section 5, line 885). The paper's contribution bullet #2 explicitly states it "highlights the limitations" of these methods in the online setting. This is a valid experimental finding, not a circular validation. Demoted from "invalid" to a minor framing concern above.

2. **"BI's advantage is marginal and inconsistent."** The reviewer's claim that "LC bottom-k achieves 24.89 (the same as BI bottom-k's best)" is factually wrong — LC bottom-k at M=200 is 20.92±0.70, not 24.89 (Table 1). BI bottom-k achieves the best or tied-best forgetting in 11/12 settings. The inconsistency cited is about accuracy, but the paper's primary claim is about forgetting reduction. Removed as partially factually incorrect.

3. **"The formalization is a problem description, not a formalization."** The paper's contribution is primarily the BI-based method, not a deep theoretical formalization. The problem description (Section 3.1) adequately defines the setting for an empirical methods paper. Removed as overly harsh for the paper's scope.

4. **Missing appendix content (class-based averaging table, ablation details).** These were stripped by the PDF parser; they exist in the original submission. Removed per hard rules.

5. **Formatting, style, and typographical nitpicks.** Removed per hard rules (parser artifacts, not author errors).

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Define the forgetting metric explicitly — this is essential for reproducibility and for readers to interpret the core results.
2. Reframe the generative baseline results as an ablation demonstrating why offline methods fail online, rather than a competitive comparison. The headline narrative should focus on the comparison against ER and uncertainty scores.
3. Run additional seeds (at least 10) on the main comparison (CIFAR-10, medical datasets) and report whether the differences between BI and the best competitor are statistically significant via paired bootstrap or similar.
4. Acknowledge the frozen pretrained embedder as a limitation for the text modality, and discuss whether the method could work with learned embeddings end-to-end.

## Score and Decision

MY FINAL SCORE: 6.0
MY FINAL DECISION: Accept