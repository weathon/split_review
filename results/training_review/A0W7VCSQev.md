I've carefully read the paper and verified the reviewer's claims against the actual text. Here is the consolidated review.

---

## Summary

This paper introduces two scoring methods derived from internal attention mechanisms in LLMs — the QK-score (query-key dot product) and Attention-score (attention weight) — extracted from specific "select-and-copy" attention heads, for multiple-choice QA. The key claim is that these internal signals outperform standard logit-based answer selection, especially for smaller models in zero-shot settings. Experiments on LLaMA models (7B–70B) across MMLU, CosmosQA, HellaSwag, HaluDialogue, and a synthetic dataset show accuracy improvements of up to 16–27% on real benchmarks and near-perfect accuracy on the synthetic task where the baseline fails.

## Strengths

- **Substantial and consistent accuracy gains over standard logit-based MCQA across multiple model scales and datasets.** The QK-score method improves accuracy by 7–16% on LLaMA2-7B (Figure 2) and up to 27% on HellaSwag with LLaMA3-8B (Table 1). These gains hold across models from 7B to 70B parameters in zero-shot settings, and the method is often on par or better in few-shot settings. On the synthetic SSD dataset, the gap is dramatic: QK-score achieves near-perfect accuracy while the baseline drops below random (Figure 5b/6b), cleanly demonstrating that the model internally knows the correct answer but cannot express it through the final logit.

- **Identification of stable "select-and-copy" heads that generalize across datasets, shot settings, and model sizes.** Heads (14,24) and (14,20) consistently appear among the top 5% of best performing heads across all four real datasets and multiple shot settings (Figure 6a). Zero-ablation of these heads causes accuracy drops, in some cases below random chance (Figure 4), providing causal evidence that these heads play a functional role in MCQA performance.

- **Robustness to option permutation (Permutation Accuracy) and to the addition of extra uncertainty options.** Across zero-shot experiments, the QK-score achieves higher PA than the baseline, indicating less sensitivity to option ordering (Figure 2, Table 1). The method also maintains performance when "E. None of the above" and "F. I don't know" are added, whereas PriDe fails in this setting (Section 5.4).

- **A simple unsupervised head-selection heuristic based on attention concentration and diversity.** The paper proposes a scoring method that identifies the known best heads (e.g., (14,24) and (14,20)) in the top 20 on real datasets and top 10 on the synthetic dataset without requiring labeled validation data (Section 7). This is practically useful for settings where validation labels are scarce.

- **The synthetic SSD dataset provides a clean, controlled testbed.** SSD isolates the model's ability to follow the MCQA format from its factual knowledge. The baseline's failure on this trivial task (accuracy near random) while QK-score from select-and-copy heads approaches 90%+ accuracy provides strong evidence that the method genuinely recovers knowledge that the model possesses but cannot surface through standard output logits.

## Weaknesses

### Fatal
None.

### Major

- **The addition of "E. None of the above" and "F. I don't know" to all real datasets (MMLU, CosmosQA, etc.) creates an evaluation asymmetry that is not adequately controlled for.** The baseline computes softmax-normalized probabilities across all six option letters (A–F); adding two extra options necessarily redistributes probability mass away from A–D, mechanically lowering accuracy. The QK-score, in contrast, computes raw (unnormalized) dot products for each option independently, so adding E/F does not affect scores for A–D. Although both methods face the same six-option input, this asymmetry in how scores are computed means the baseline is systematically disadvantaged in a way that is orthogonal to the paper's core claim about "extracting knowledge." The paper does not report results on the original 4-option format for any real dataset, making it impossible to quantify how much of the observed improvement is genuine versus an artifact of this design choice. This is the most significant weakness in the experimental design.

- **The core theoretical claim that QK-score avoids positional bias under RoPE is underspecified.** The paper states (Section 3, line 88) that QK-score "does not use the positional shift when comparing the queries and keys" and (Section 4, line 117) that "in QK-score we do not apply positional transformation." Under RoPE (used by LLaMA models), the rotation is applied to q and k *before* the dot product during attention computation. The paper never specifies whether the extracted q and k vectors are pre- or post-RoPE. If post-RoPE vectors are used (which is the standard representation accessible via model internals without modifying the forward pass), then the QK-score already encodes positional information, and the claimed distinction from attention scores is incorrect. If pre-RoPE vectors are used, the extraction method is not described. This ambiguity undermines the theoretical motivation for preferring QK-score over attention scores and the interpretation of results that depend on this distinction.

### Minor

- **No confidence intervals, standard deviations, or variance estimates are reported for any accuracy results.** The head selection procedure uses only 5% of each dataset as validation (e.g., ~700 examples from MMLU's ~14k across 57 subjects). Head selection on such small validation sets could be noisy, and without uncertainty estimates the stability and statistical significance of the reported improvements cannot be assessed.

- **The method's performance is sensitive to the choice of option-representative token (Figure 2), with different token types (EOL, period, label, etc.) yielding substantially different results across zero-shot and few-shot settings.** While the paper analyzes this variation, it does not provide guidelines or a principled way to select the right token type for a given setting, and the brittleness to prompt formatting details (whether newlines are present, punctuation choices) is a practical concern for deployment.

- **The ablation evidence for a causal role of select-and-copy heads (Figure 4) is presented without numerical comparisons or statistical tests.** The paper states that ablating top heads causes "a significant drop in accuracy, sometimes below random performance" (line 254), but no numerical values, effect sizes, or statistical significance tests are reported to support this claim. The visual comparison to random-head ablation shows a difference that the paper acknowledges is "not visually dramatic" (as the critic notes). Stronger quantitative evidence would strengthen the causal claims.

- **The claim of "universal" heads is based on heads appearing in the top 5% across conditions, which is a relatively weak criterion.** With ~1024 heads total in LLaMA2-7B (32 layers × 32 heads), top 5% selects ~51 heads per condition. That two heads ((14,20) and (14,24)) appear frequently is suggestive but not strong evidence of mechanistic specialization — they could simply be "commonly good" rather than uniquely specialized for MCQA. The paper's own admission that other heads are needed for the synthetic dataset (heads (8,8) and (12,15) are unique to SSD) further complicates the universality claim.

- **The paper lacks comparison to other head-based scoring methods**, such as mean pooling of QK-scores across all heads or using final-layer attention patterns, which would help isolate whether the benefit comes from using specific heads versus using QK-score as a scoring mechanism in general.

### Trivial

- Figure/table cross-references in the text occasionally refer to figures by wrong labels (e.g., the ablation discussion references Figure 4 but the figure appears to be labeled Fig.~ref{fig:ablation} as Figure 5 in the text).
- The synthetic dataset plot (Figure 6b) is described in the caption as showing "various numbers of options (number of options is plotted on x axis, varies from 0 to 24)" but the range 0–24 includes an implausible "0 options" case.

## Nice-to-Haves

- Evaluating the QK-score method on standard 4-option MCQA benchmarks (without E/F additions) would directly address the main experimental concern and substantially strengthen the paper's claims.
- Combining complementary heads (e.g., (14,20) and (14,24), which the paper notes have complementary selection biases toward A/D vs. B/C) could potentially improve performance through ensembling and reduce the need for per-dataset head selection.
- Providing a clear description of how q/k vectors are extracted (pre- vs. post-RoPE) and whether a modified forward pass is needed, to enable reproduction.
- Release of code for the extraction and scoring pipeline.

## Removed Points

These points from the reviewer inputs were checked against the paper and removed:

- **Criticism that SSD is "simple word matching" and doesn't demonstrate format limitations.** The paper explicitly designed SSD to "estimate the ability of the model deal with the bare task format" (line 149). The SSD results show the model internally recognizes the correct answer (QK-score accuracy near 90%) but cannot output it (baseline near random) — this directly validates the paper's core thesis about format limitations. The critic misunderstands the purpose of SSD. **(Removed: misunderstanding of paper content)**

- **Criticism that PA exempting E/F from shuffling is inconsistent.** The paper's justification is sound: E and F have fixed text ("None of the above," "I don't know"), so shuffling them does not test order dependence. This is a principled design choice, not an error. **(Removed: the paper's treatment is appropriate)**

- **Criticism that "select-and-copy" head definition is undersupported.** The definition is operational (heads whose QK/attention scores yield high accuracy), which is standard practice in mechanistic interpretability papers. The paper additionally provides ablation evidence for a causal role. **(Removed: the paper's empirical approach is appropriate for its scope)**

- **Strength Finder's strengths about robustness to permutation and SSD were partially in tension with verified weaknesses.** However, the SSD strength is valid and supported; I kept it with appropriate caveats. Removed no strength that was both specific and supported.

## Novel Insights

Beyond the paper's own contributions, the most interesting observation emerging across the reviews is the complementary selection bias of heads (14,20) and (14,24) (one biased toward A/D, the other toward B/C). This suggests the model may decompose the MCQA task across multiple heads, each handling a subset of the option space, rather than having a single "oracle" head. If this is a general phenomenon — that "select-and-copy" heads partition the option space rather than each solving the full problem — it has implications for how we interpret attention-head specialization and how we design extraction methods (ensembles may be more appropriate than single-head selection). This observation is noted but not explored in the paper, and it points toward a potentially fruitful direction for follow-up work.

## Suggestions

1. **Report results on at least one real dataset in the standard 4-option format** (without E/F additions) to quantify the extent to which the reported improvements depend on the asymmetric setup. This is the single most important experiment to add.

2. **Clarify the RoPE handling in a revised version.** State explicitly whether q/k vectors are extracted pre- or post-RoPE, and if pre-RoPE, describe how. If post-RoPE vectors are used, either revise the theoretical claim about positional bias or demonstrate empirically that the residual positional information does not drive the results.

3. **Add confidence intervals or bootstrapped error bars** to the accuracy and PA results, especially given the small validation sets used for head selection.

4. **Report numerical ablation results** (accuracy before/after ablation, with effect sizes) alongside the visual figure, and include a simple significance test (e.g., permutation test) comparing top-head vs. random-head ablation.

5. **Evaluate an ensemble** of complementary heads (e.g., (14,20) and (14,24)) to see whether selection bias can be mitigated and whether ensemble accuracy exceeds single-best-head accuracy.

## Score and Decision

The paper identifies an interesting and practically useful phenomenon — that specific attention heads' internal signals can outperform the model's final output logits on MCQA tasks — and provides extensive empirical characterization across model scales. The core observation is likely real and valuable to the community. However, two issues prevent acceptance in the current form: (1) the asymmetric experimental setup (adding E/F options to all real datasets without reporting standard 4-option results) makes it impossible to determine how much of the reported improvement is genuine versus an artifact of the design, and (2) the underspecified RoPE handling undermines the paper's key theoretical distinction between QK-score and attention scores. These are addressable with additional experiments, but they are substantive enough that the paper should not be accepted without revision.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>