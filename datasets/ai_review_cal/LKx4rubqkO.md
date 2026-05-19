- Decision: Reject
- Avg Score: 3.75
- Scores: 3, 3, 3, 6
Here is the final consolidated review.

---

## Summary

This paper proposes a metric-learning approach for detecting LLM-generated text. Given a text and its known context (prompt), the system generates an LLM reference response, then uses a learned distance metric to compare the two and decide origin. The method uses a frozen MPNet encoder with a lightweight metric network trained via same-context triplets (two LLM responses + one human response per context). The paper also contributes four new datasets (NQ, SQUAD, SciQ, Wiki) totaling over 85,000 context–triplet entries, all using GPT-3.5 Turbo. The proposed models achieve F1 scores of 0.87–0.95 and train extremely efficiently (8 seconds/epoch for the full-text model vs. 70+ minutes for finetuning DistilBERT/RoBERTa).

## Strengths

1. **Same-context triplet learning is a novel and well-motivated formulation for LLM detection.** The paper adapts triplet loss to the specific setting where both anchor and positive are LLM responses and the negative is a human response, all sharing the same context (Section 3.2, Figure 2). This framing avoids needing access to the generative model's internal probabilities or output distributions, addressing a real gap in the literature (Section 2).

2. **Extremely efficient training compared to supervised LLM finetuning.** The full-text model trains at 8 seconds per epoch on ~51k triplets; the sentence model at ~3 minutes/epoch. By contrast, finetuning DistilBERT takes 70 minutes/epoch and RoBERTa 125 minutes/epoch on the same data split (Section 5, lines 126–127). This efficiency advantage is concrete and well-documented.

3. **Four new benchmark datasets for the research community.** The paper constructs and will release four datasets (NQ: 59,945; SQUAD: 18,813; SciQ: 4,419; Wiki: 2,071 entries) in the format of context + triplet responses (one human, two GPT-3.5 Turbo). The construction process is transparent, including prompt engineering, filtering criteria, and handling of response lengths (Section 4). These fill a gap noted in the introduction.

## Weaknesses

### Fatal

None.

### Major

1. **Improvement over a simple MPNet-distance baseline is marginal, and no statistical validation is provided.** The baseline (threshold on raw MPNet embeddings) achieves F1 of 0.84–0.96, which overlaps almost entirely with the proposed models' 0.87–0.95 (Section 5, line 128). The paper acknowledges that on smaller datasets (SciQ, Wiki), the full-text model and baseline are "relatively similar," and the sentence model performs *worse* than baseline in cross-domain settings. Despite stating "tested in 10 runs" (line 128), the paper reports only bar-chart means in Figure 4 with **no error bars, confidence intervals, or significance tests**. Without variance information, the reader cannot assess whether the metric-learning component provides any reliable benefit over a trivial distance threshold on pretrained embeddings. This weakens the central claim that the proposed architectures contribute meaningful improvement.

2. **Missing fair, lightweight baselines.** The paper dismisses supervised classifiers because a deep classifier (20 layers, 12M parameters) "could not converge" on MPNet embeddings, and finetuning LLMs is too expensive (line 126). However, a shallow classifier (e.g., logistic regression or SVM) on the same MPNet embeddings would be a natural, lightweight, and likely competitive baseline — and it is neither implemented nor discussed. This omission is consequential: if a simple linear probe on MPNet embeddings matches or exceeds the metric-learning models, the core methodological contribution is undermined. The evaluation as presented appears to set up a comparison against only the weakest plausible baseline.

3. **The known-context requirement is under-acknowledged in the paper's framing.** The detection pipeline requires the exact prompt used to produce the text under scrutiny. This is stated in contribution 1 ("for known contexts," line 21) and noted as future work (Section 6), but the abstract and introduction frame the approach as a general, "balanced among computational costs, accessibility, and performances" detection method (abstract, line 5) without prominently caveating this limitation. In real-world settings (e.g., checking a student essay, a social media post, or a news article), the prompt is typically unknown. The method's applicability is therefore restricted to scenarios where the context is available — a significant scope constraint that should be stated upfront rather than deferred to future work.

### Minor

1. **Evaluation is limited to GPT-3.5 Turbo across all experiments.** All four datasets use only GPT-3.5 Turbo as the LLM source (Section 4). The paper does not test generalization to other LLMs (GPT-4, Llama, Claude, etc.). Given that model-specific patterns may differ, the method's robustness across LLMs is unestablished.

2. **No quantitative analysis of failure cases.** The paper reports aggregate F1 scores but does not analyze *where* the metric model helps beyond the MPNet baseline or where it hurts. Such analysis (e.g., which prompts produce the largest/smallest improvements) would strengthen the contribution's depth.

3. **Figure 4 bar charts lack readable precision.** Exact F1 values with standard deviations (across the 10 runs) are not reported in a table, making the results hard to evaluate quantitatively. The paper should provide a tabular summary.

### Trivial

- Minor wording issues ("beset" → "best" on line 17, "An metric-based" → "A metric-based" on line 21).
- The triplet loss formula (Section 3.2) contains garbled macro notation ("m{\bar{a}}x") — a LaTeX artifact.

## Nice-to-Haves

- Including AUC or ROC analysis alongside the threshold-based F1 would strengthen the evaluation.
- Testing on at least one additional LLM (e.g., Llama or GPT-4) would improve generalizability claims.
- A context reconstruction baseline (e.g., using a prefix of the text as a proxy prompt) would help quantify the practical impact of the known-context requirement.

## Removed Points

- **"Known-context limitation is fatal / structural"** — Demoted from Fatal to Major. The paper explicitly states "for known contexts" in contribution 1 (line 21) and acknowledges context reconstruction as future work (line 144). This is a real limitation but the paper is not hiding it entirely; it is under-acknowledged in the abstract/conclusion framing, not absent.

- **"Missing comparison to zero-shot/few-shot LLM-as-judge approaches"** — Removed. The paper's premise is to avoid reliance on the generative model's internals, and LLM-as-judge approaches (prompting an LLM to classify) are a qualitatively different paradigm. Demanding this comparison is scope creep. (Harsh Critic, critical issue 3b.)

- **"Supervised classifiers failed to converge — this omission makes evaluation appear staged"** — The paper does report attempting deep supervised classifiers (20 layers, 12M params) and their failure to converge. The valid criticism is the *absence of shallow classifiers* (logistic regression, SVM), which is retained in Major weakness #2. The claim that the evaluation is "staged" is an unsupported characterization and is removed.

- **"Figure 5 histograms are illustrative but not quantitative"** — Removed. They are *meant* to be illustrative (distribution visualization), and the paper notes they "show clear separation." This is a standard use of histograms.

- **"Context reconstruction should be a current limitation, not a future direction"** — Merged into Major weakness #3. The critic's framing is retained but downgraded: the paper does mention it as future work, which is standard practice. The issue is the absence of the caveat in the abstract and conclusion.

- **Strength Finder strength #4 ("Robust performance across diverse settings")** — Demoted from the main list. The F1 ranges overlap with the baseline, and on smaller datasets the method does not improve. The claim of "robust" is overstated given the evidence. The efficiency advantage (strength #2) is the stronger argument.

## Novel Insights

None beyond the paper's own contributions. Both reviews primarily surface expected gaps (missing baselines, limited statistical validation, scope limitations) rather than generating novel observations about the paper that the authors themselves missed.

## Suggestions

1. **Add error bars / standard deviations** to all bar charts and report exact F1 values in a table. With 10 runs available, this is trivially doable and would let readers assess whether the metric-learning component provides a reliable benefit.
2. **Implement shallow classifier baselines** (logistic regression or SVM on MPNet embeddings). If the metric-learning models still outperform these, the contribution is strengthened. If not, the paper should honestly report this.
3. **Restate the known-context limitation directly in the abstract** (e.g., "for scenarios where the generating prompt is known") and in the introduction's framing. This would prevent misleading readers about the method's applicability.
4. **Include a section analyzing when/why the metric model improves over the baseline** and when it does not — this would deepen the paper's own contribution.
5. **Present a table** of exact F1 scores with standard deviations for all models × settings, so readers can quantitatively compare.
