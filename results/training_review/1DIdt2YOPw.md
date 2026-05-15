Now I have a thorough understanding of the paper and all reviewer inputs. Let me produce the consolidated review.

## Summary

The paper investigates whether uncertainty-based abstention can improve LLM reliability across three failure modes: correctness (incorrect answers on answerable questions), hallucinations (unanswerable questions that models fabricate answers for), and safety (unsafe responses to adversarial prompts). The authors compare statistical uncertainty measures (predictive entropy, semantic entropy, negative log-likelihood) with a verbalized measure called In-Dialogue Uncertainty (InDU, based on hedge-word counts) across pretrained and RLHF-finetuned Llama2 models. The central finding is that different uncertainty types are effective for different failure modes — statistical uncertainty for correctness and safety, InDU for detecting unanswerable questions — and that RLHF preserves or enhances uncertainty awareness in most settings.

## Strengths

- **Systematic comparison across three distinct failure modes and two uncertainty types within a unified experimental framework.** The paper evaluates correctness (5 datasets × 2 model types), hallucinations (SelfAware dataset), and safety (2 adversarial datasets) using the same model family and uncertainty measures, providing a coherent picture of where each uncertainty type works best. The finding that statistical and verbalized uncertainty are complementary — statistical works for correctness/safety, InDU for unanswerable questions — is a clear and useful takeaway.

- **The finding that RLHF preserves uncertainty awareness for correctness and safety is non-obvious and practically relevant.** Despite prior work showing RLHF increases miscalibration and reduces output diversity (confirmed in Figure 2), the paper demonstrates that RLHF models achieve comparable or better AUROCs than base models for correctness (e.g., TriviaQA: base 0.78 vs. RLHF 0.85 for semantic entropy) and dramatically better AUROCs for safety (RLHF 0.96–0.99 on AutoDAN vs. near-random for base/instruction-tuned models). This counters the expectation that RLHF harms uncertainty discrimination.

- **Safety results on AutoDAN (AUROC 0.96–0.99, filtering 99% of unsafe responses at 10% false-refusal rate) are striking and merit attention.** Even accounting for potential AUROC inflation from class imbalance, the magnitude of the effect suggests statistical uncertainty on RLHF models carries genuine signal about response safety.

- **InDU requires no additional prompting, sampling, or external models.** The measure counts hedge words directly from the model's output text, making it computationally cheap while proving uniquely effective for distinguishing answerable from unanswerable questions (AUROC 0.69 base, 0.75 RLHF vs. best statistical AUROC of 0.64).

## Weaknesses

### Fatal
None.

### Major

- **The headline correctness improvement claim (2–8%) is only concretely demonstrated on TriviaQA via ARC; the AUROC table (Table 1) does not directly substitute for operational abstention curves on other datasets.** The abstract and introduction state that abstention "can improve correctness across a range of question-answering tasks from 2% up to 8%." However, the Accuracy-Rejection Curves (which directly show accuracy gains from abstention) are only presented for TriviaQA (Figure 1a). The AUROC results in Table 1 confirm that uncertainty *ranks* correct vs. incorrect responses across five datasets, but AUROC does not quantify the accuracy improvement at a given rejection threshold. Without ARCs on additional datasets (e.g., SciQA, CoQA, StrategyQA), the operational claim of 2–8% improvement across tasks is only partially supported.

- **The safety results rely on automated labeling (Llama Guard + keyword heuristics) with no reported agreement or human validation, and the AUROCs on AutoDAN (0.96–0.99) are suspiciously high given the heavy class imbalance (~7.5% unsafe after RLHF).** AUROC can be inflated when the positive class (unsafe) is rare and the model assigns most high-uncertainty scores to a small number of negative (safe) examples. The paper does not report precision-recall curves or the actual score distributions, making it difficult to assess whether the high AUROC reflects genuine discrimination or a class-imbalance artifact. A human evaluation of even 100 labeled responses per dataset would substantially strengthen the claims.

- **The semantic entropy formula (Equation 3) appears inconsistent with the original formulation in Kuhn et al. (2023).** The paper gives SE(x) ≈ −(1/C) Σ_j log p(c_j|x), which averages negative log-likelihoods over meaning clusters. The original semantic entropy is SE(x) = −Σ_j p(c_j|x) log p(c_j|x) — an entropy over cluster probabilities. The paper does not explain this deviation or cite an alternative approximation. This could affect the reproducibility and correctness of the semantic entropy results, which are the best-performing statistical measure for correctness.

### Minor

- **No confidence intervals, error bars, or statistical significance tests are reported for any numerical result.** All AUROCs, accuracy improvements, and rejection rates are point estimates. Given that many AUROCs fall in the 0.6–0.8 range and the correctness improvement from rejecting 5% of samples is only 1.6 percentage points (84.4% → 86.0%), it is unclear whether these differences are robust. While single-run evaluation is common in LLM benchmarking, confidence intervals (e.g., via bootstrapping) would strengthen the credibility of the comparisons.

- **The InDU measure is a simple hedge-word count with limited validation.** The paper uses a single, predetermined hedge-word list with no analysis of false positives (e.g., "maybe" used for politeness/hypotheticals rather than uncertainty) or false negatives (hallucinated responses without hedge words). No comparison to alternative text-based measures (e.g., "I don't know" detection, trained classifiers) is provided. The paper acknowledges it is not "a perfect metric," but since InDU is one of the two central uncertainty types, a basic error analysis would clarify what signal it captures.

- **The safety results use adversarial datasets (AutoDAN, AttaQ) that are designed for red-teaming, raising questions about generalization to naturally occurring unsafe queries.** The paper does not discuss this limitation. The claims about "improving safety by 70–99%" should be understood within this adversarial context.

- **For the correctness setting, ground-truth labeling uses "fuzzy exact match" (checking if the reference answer is contained in the response), which is known to overcount correct answers in verbose responses and undercount paraphrases.** No validation against human judgments or the datasets' official evaluation scripts is provided.

### Trivial

- The semantic entropy formula uncertainty — while a genuine concern — could potentially be clarified as a notation issue where p(c_j|x) is defined differently; the paper would benefit from a clearer citation or derivation.
- Figure 1's safety ARC y-axis is labeled "Safe Response Rate"; the caption clarifies the metric, but the label could be more informative.

## Nice-to-Haves

- Reporting precision-recall curves (or at least the class-conditional score distributions) for the safety experiments, given the class imbalance on AutoDAN.
- A simple baseline comparison: abstaining based on detecting explicit refusal phrases ("I don't know," "I cannot answer") or the model's own output tokens — this would contextualize whether complex uncertainty measures are necessary.
- Human validation of a sample of ground-truth labels for all three settings.
- An error analysis for InDU showing representative examples of false positives and false negatives.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"The hallucination setting is narrowly defined as unanswerable questions"** — The paper explicitly scopes its hallucination experiments to unanswerable questions (Section 4.2: "hallucinations in the context of unanswerable questions"; abstract: "avoid 50% hallucinations via correctly identifying unanswerable questions"). The reviewer's criticism is scope creep: the paper does not claim to address factual errors on answerable questions and clearly states its framing.

2. **"The abstract's phrasing [70–99%] strongly implies a consistent improvement... which is misleading"** — The paper reports 99% on AutoDAN and 70% on AttaQ (line 297) and says "increase safety by 70% up to 99%" in the abstract. This accurately reflects the range across two datasets. The phrasing is not misleading.

3. **"The claim that 'having to explicitly ask for uncertainty estimates does not come natural to humans' is unsupported"** — This is a minor philosophical aside in the Related Work section, not a core claim. It does not affect the paper's empirical contributions.

4. **The "Safe Response Rate" y-axis label concern** — The paper defines safe response rate clearly (line 139). This is a presentation nitpick.

5. **Missing related work on selective prediction methods** — Per instructions, missing related works are not to be flagged without independent verification.

6. **"No error bars" as a fatal flaw** — While noted as a minor weakness above, single-run deterministic evaluation on standard benchmarks is the norm in this subfield (Kuhn et al. 2023, Lin et al. 2023, etc.). The paper's community standards do not require confidence intervals for this type of evaluation, though they would be a nice addition.

7. **Criticism that the paper "never defines what counts as 'verbalized uncertainty' beyond hedge-word counting"** — The paper defines InDU explicitly in Section 3.2: counting hedge words from a published list. The term "verbalized" is used descriptively to contrast with "statistical," not as a separate, un-defined construct.

## Novel Insights

Beyond the paper's own contributions, the reviews surface an interesting tension: the paper shows RLHF preserves uncertainty *discrimination* (AUROC) while increasing *miscalibration* (confidence scores). This decoupling of calibration from discrimination is worth emphasizing as an insight for practitioners — a model can be poorly calibrated yet still rank its responses well by uncertainty, which is sufficient for abstention at fixed rejection rates. The reviewers' differing takes on this finding (the harsh critic sees it as background, while the strength finder treats it as a core result) suggest the paper could more prominently frame this decoupling as a practical takeaway.

## Suggestions

1. **Provide ARCs on at least 2–3 additional datasets (e.g., SciQA, CoQA) to support the 2–8% correctness improvement claim across tasks.** This is the single most important addition. The AUROC table is useful but does not substitute for showing accuracy gains at concrete rejection thresholds.

2. **Clarify the semantic entropy formula.** Either correct Equation 3 to match the standard formulation from Kuhn et al. (2023), or explicitly state and cite the approximation being used.

3. **Add precision-recall curves or report the full score distribution** for the safety experiments, particularly AutoDAN where class imbalance is severe.

4. **Conduct a small human evaluation** of at least 100 safety labels and 100 correctness labels to validate the automated ground-truth metrics.

5. **Add a simple baseline** comparing uncertainty-based abstention to detecting explicit refusal/uncertainty phrases in the model's output (e.g., "I don't know," "I cannot answer").

6. **Acknowledge the limitations** of (a) adversarial-only safety evaluation, (b) the need to pre-specify rejection thresholds, and (c) potential domain sensitivity of the hedge-word list.

## Score and Decision

The paper makes a genuine contribution by systematically mapping which uncertainty type works for which failure mode, and the finding that RLHF enhances safety uncertainty awareness is practically important. However, the gap between the claimed 2–8% correctness improvement "across a range of tasks" and the single-dataset ARC evidence is the most significant weakness. The semantic entropy formula concern and the lack of human validation for safety labels are additional issues. With the ARC and formula issues addressed, the paper would be solid; as-is, the claims slightly outpace the evidence. The paper is borderline but leans toward acceptance given its practical relevance and the novelty of its comparative framework.

**MY FINAL SCORE: <pineapple>5.5</pineapple>**  
**MY FINAL DECISION: <orange>Accept</orange>**