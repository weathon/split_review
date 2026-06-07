## Summary

This paper proposes IMP-Loss and DIMP-Loss, two weighted-loss objectives for training classifiers on LLM-generated synthetic data. The methods use a "quality checker" (a model trained on a small real-world dataset) and a "diversity checker" to reweight each synthetic sample — IMP-Loss uses a separate model trained on the synthetic data as the diversity checker, while DIMP-Loss uses the model currently being trained. Experiments on three text classification benchmarks (Financial Phrasebank, Tweet Irony, MRPC) with BERT and GPT-3.5-turbo show consistent improvements over CE-Loss, Focal Loss, and a meta-learning baseline (DML).

## Strengths

1. **Consistent and meaningful empirical gains on LLM-generated data.** In Table 1, both IMP-Loss and DIMP-Loss outperform CE-Loss, Focal Loss, and DML across all three datasets when training on GPT-3.5-generated data. Gains over CE-Loss range from ~2–6% absolute accuracy (e.g., Financial: 82.67% vs 77.39%; Tweet Irony: 81.89% vs 76.91%). No baseline beats either proposed method on any metric in this setting.

2. **Clean importance-sampling derivation for IMP-Loss.** Eqs. 84–95 derive IMP-Loss from importance sampling theory, showing that weighting by \(P(y|\mathbf{x})/Q(y|\mathbf{x})\) makes the expected loss under \(Q\) converge to the expected loss under \(P\) (under the assumption \(Q(\mathbf{x}) \approx P(\mathbf{x})\)). This provides theoretical grounding that distinguishes IMP-Loss from heuristic reweighting.

3. **Computational efficiency of DIMP-Loss.** Section 4.4 shows DIMP-Loss requires only one training pass plus one forward pass on \(D_Q\) beyond standard CE-Loss, avoiding the need to train a separate diversity-checker model. This is concretely cheaper than IMP-Loss and dramatically cheaper than meta-learning baselines like DML.

4. **Ablation confirms the diversity checker's contribution.** The "w/o diversity checker" row in Table 1 shows that removing the diversity component from IMP-Loss causes measurable degradation (Financial Acc drops from 82.09% to 81.35%, F1 from 79.40% to 77.94%), directly attributing gain to the diversity mechanism rather than the quality checker alone.

5. **Practical efficiency demonstrations.** Table 3 shows DIMP-Loss works with a smaller quality checker (BERT-base guiding BERT-large), and Figure 2 shows even 10% of training data suffices for an effective quality checker. These validate the method's practicality in resource-constrained settings.

## Weaknesses

### Major

1. **DIMP-Loss derivation contains significant gaps that are papered over.** The transition from the data-selection objective (Eq. 134: maximize the joint likelihood of \(D_{P'}\) after updating on one point from \(D_Q\)) to the ratio in Eq. 135 (\(\hat{P}(y|\mathbf{x}; \theta_t, D_{P'}) / \hat{P}(y|\mathbf{x}; \theta_t)\)) is stated as "by applying Bayes' rule" but is not actually derived — it is at best an asserted simplification with the derivation omitted. Then the numerator \(\hat{P}(y|\mathbf{x}; \theta_t, D_{P'})\) is approximated by \(\hat{P'}(y|\mathbf{x})\) (a model trained from scratch on \(D_{P'}\) only), which is a different object entirely, and the paper provides no argument that the two should be close. While the method may work empirically, the paper presents this as a principled derivation when the chain of reasoning is broken. This weakens the paper's theoretical narrative. (The paper references an appendix section for further derivation, but the main-text presentation as-is is insufficient to support the claimed derivation.)

2. **The DML baseline performs anomalously poorly, and the paper provides no evidence it was properly configured.** DML achieves 71.70% on Financial (synthetic) vs CE-Loss's 77.39%, and 60.33% on large real-world Tweet Irony vs CE-Loss's 68.75%. DML is a meta-learning method designed to optimize weights for a held-out real set — such large margins below CE-Loss are unusual and suggest the official-code defaults may not be appropriate for this setting. The paper states only that official code was used, without discussing hyperparameter tuning. Since the comparison table treats DML as a main baseline, this undermines the fairness of the experimental comparison. (The core claims still survive against CE-Loss and Focal Loss.)

### Minor

3. **Evaluation scope is narrow relative to the claims.** The experiments cover one classifier (BERT), one generator (GPT-3.5-turbo-1106), and three short-text classification datasets. The abstract frames the contribution as providing "potential solutions to effectively leveraging synthetic data from any suitable data generator," but this generality is asserted without evidence. While the title scopes to text classification, the method's robustness across generators, architectures, or text classification subdomains is untested. This constrains the paper's significance.

4. **No variance/statistical significance reported for the main results table.** Table 1 shows only point estimates — no standard deviations, confidence intervals, or repeated-run statistics. The training dynamics figure (Fig. 1) shows 4-seed ranges but only for a subset of methods and only for accuracy. Without variance information, the reader cannot assess whether the reported 1–5% gains are reliable or noisy.

5. **Limited baseline set and missing component analysis across settings.** Beyond CE-Loss, only two non-CE baselines are included (Focal Loss, DML). A baseline of weighting by quality-checker confidence alone (\(\hat{P'}(y|\mathbf{x})\) without the diversity denominator) is tested only for IMP-Loss and only on LLM-generated data (the "w/o diversity checker" row). Adding this baseline systematically across all settings and for DIMP-Loss would better isolate the diversity component's contribution.

6. **Model calibration is not discussed despite reliance on probabilistic weights.** Both methods use ratios of softmax outputs as weight components. Fine-tuned BERT models on small datasets are known to be poorly calibrated. The paper does not discuss whether calibration matters for the weighting to work as intended, or whether the method is robust to miscalibration because only the relative ordering of weights matters. This is an unexamined assumption.

7. **Rhetorical overclaim on one metric.** Section 5.1.3 claims the methods "surpass the accuracy of the data generator." This is true for accuracy on all three datasets, but on MRPC the F1 scores of IMP-Loss (70.52) and DIMP-Loss (70.04) are below GPT-3.5 few-shot (71.75). A reader scanning the bold text may infer broader dominance than the evidence supports.

### Trivial

None that rise above the level of typical parser artifacts.

## Nice-to-Haves

- Broaden evaluation to at least one additional data generator (e.g., Llama-3, GPT-4) or one additional classifier architecture (e.g., RoBERTa, DeBERTa) to support the claimed generality.
- Either tune DML carefully or replace it with a baseline whose configuration is better understood in this setting.
- Add calibration analysis (reliability diagrams, ECE) for the quality checker and diversity checker to address the unexamined calibration assumption.
- Reframe the DIMP-Loss derivation honestly as a heuristic motivated by data selection rather than claiming a rigorous Bayesian derivation, or fix the derivation to justify the approximations.

## Removed Points

These points were flagged for removal during filtering; treat with caution.

1. **"Data generation process is underspecified in the main text."** — REMOVED because the paper explicitly references the appendix (supplementary materials) for prompt details, generation parameters, and dataset sizes. The parser strips appendix content; the details exist in the original submission.
2. **"Noisy data experiments promised but not present."** — REMOVED because the paper references Sec. 5.3 (noisy data) which appears in the appendix. The parser strips appendix sections; these existed in the original submission.
3. **"Fatal" or "structural" claims about DIMP-Loss derivation that depend on speculative gaps rather than confirmed paper content.** — The critic's framing of the derivation issue as a "structural" problem was retained as Major (since it is verifiable from the paper), but further speculation about what might be missing from appendix content was removed.
4. **"Complaints about missing related works"** — REMOVED per instruction (no external sources to confirm existence).
5. **Formatting/style nitpicks** — REMOVED per instruction (parser artifacts, not author errors).

## Novel Insights

None beyond the paper's own contributions. The information-theoretic diagnostic (Section 3.2) showing higher conditional entropy in synthetic data while \(\text{KL}(P\|Q) < \text{KL}(Q\|P)\) is a useful observation about why synthetic data can be beneficial despite distribution shift, but it is clearly the paper's own contribution.

## Suggestions

1. Address the DIMP-Loss derivation gap: either provide a proper derivation that tracks the approximations, or honestly reframe it as a heuristic inspired by data selection (the method works empirically either way).
2. Report variance (e.g., across 5 seeds) for all entries in Table 1 so readers can assess the stability of the gains.
3. Add at least one evaluation with a different generator (Llama-3, GPT-4) or classifier architecture to support the "any suitable generator" claim.
4. Provide evidence that DML was properly tuned for Fair comparison, or replace it with a baseline whose configuration in this setting is better characterized.
5. Include the quality-checker-only weighting baseline across all settings (both LLM-generated and real-world data) to fully isolate the diversity term's contribution.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Reject</decision>