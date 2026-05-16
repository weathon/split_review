## Summary

This paper proposes Gramtector, a method for AI-generated text detection that uses interpretable grammatical patterns (PoS n-grams) as features. The key idea is to learn which grammatical patterns are predictive of human vs. LLM authorship, then either train an interpretable classifier on these 20 selected patterns or present them directly to humans in a human-in-the-loop setting. The paper evaluates the classifier across multiple domains (arXiv, Reddit, CNN, Wikipedia) and LLMs (ChatGPT, GPT-4, LLAMA-2-70B, BARD), showing AUROC scores close to 1. The human trial reports that participants using the patterns improved detection accuracy from 40% to as high as 86% in a subgroup, with a tiered design revealing that too much AI guidance paradoxically hurts performance.

---

## Strengths

- **Human-in-the-loop approach shows meaningful performance gains.** The paper demonstrates that non-expert humans using interpretable grammatical patterns can substantially improve their detection accuracy. Even the more conservative overall population results (Table 3) show clear improvement over the 40–43% baseline. The tiered experimental design (Levels 1–3) is a well-structured way to study how different forms of AI assistance affect human decision-making.

- **Robustness to adversarial evasion.** Gramtector maintains performance under prompt engineering and paraphrasing attacks, while vocabulary and stylometric feature baselines collapse (e.g., TPR dropping from 98% to 4% under paraphrasing, Table 2). This supports the core insight that grammatical structure is a relatively intrinsic LLM characteristic that is hard to alter.

- **Strong classifier performance across domains and models.** The 20-feature logistic regression achieves AUROC scores close to 1 on arXiv, Reddit, CNN, and Wikipedia datasets, and generalizes across ChatGPT, GPT-4, LLAMA-2-70B, and BARD (Figure 2). Outperforming fine-tuned BERT variants on some datasets with only 20 interpretable features is a genuinely positive result.

- **Novel finding about over-reliance on AI guidance.** The finding that Level 1 (PoS tagging only) outperforms Levels 2 and 3 among engaged participants is a nuanced and non-obvious result about human-AI collaboration: directly presenting predictions (Level 3) induces black-box reliance and degrades performance.

---

## Weaknesses

### Fatal

None.

### Major

- **The abstract and introduction present the 86% accuracy figure without adequate qualification.** The abstract states "an improvement in the detection accuracy from 43% to 86%" and the introduction says "accuracy increases from 40% to around 86%." However, as clarified in Section 5.2, this 86% corresponds to the subgroup of participants who were both *engaged* and *actively used the provided grammatical patterns* (a self-selected subset). The overall accuracy for all participants at Level 1 is lower (Table 3). While the improvement even at the population level is still meaningful, presenting the subgroup result as the headline number in the abstract — with no indication that it refers to a subset — is misleading and inflates the paper's central claim. This is fixable with transparent reporting, but as written it undermines the credibility of the contribution.

- **The human trial lacks essential methodological transparency.** The paper does not report: (1) the number of participants, (2) how they were recruited, (3) whether participants were randomly assigned to conditions, (4) how the "engagement" categories (unengaged, engaged, engaged+using patterns) were operationalized or measured, and (5) the criteria for classifying responses into these categories. Since the engagement categories are central to the analysis — they are used to isolate the 86% subgroup — the lack of transparency about their definition is a significant gap. Without this information, it is unclear whether the reported accuracy gains reflect a causal effect of the patterns or self-selection (e.g., more capable participants naturally gravitating toward using the patterns). This does not invalidate the results, but it prevents proper evaluation of the human trial.

### Minor

- **The robustness evaluation, while clean, is limited in scope.** The paper compares Gramtector against vocabulary and stylometric features on two attack scenarios (prompt engineering and paraphrasing), citing Sadasivan et al. (2023) for the attack methodology. The comparison is fair (same framework, different features) and the results are clear, but the adversarial conditions are not described in sufficient detail: the paper does not specify what paraphrasing model was used, how aggressive the paraphrasing was, or how the adversarial prompts were constructed. The conclusion that "grammatical sentence structure is an intrinsic characteristic of the LLM that is challenging to alter" would be stronger with more detail and with testing against additional evasion strategies (e.g., human post-editing of LLM output).

- **No statistical significance reported for classifier comparisons.** In Figure 2, Gramtector is compared against RoBERTa and DistilBERT baselines, but no statistical significance tests are reported for the differences. This is a gap in an otherwise rigorous classifier evaluation.

- **The paper does not specify the exact p-value test used in Table 3.** The caption states "The p-value assesses whether p̂ is larger at the given level compared to the baseline" without identifying the specific statistical test employed. This reduces the interpretability of the reported significance levels.

- **Handling of rare/near-zero-variance PoS n-gram features is not discussed.** The paper extracts 100,004 grammatical features from PoS n-grams up to length 7. It is not described whether any frequency thresholding or variance-based filtering was applied before the L1-regularized logistic regression. While L1 regularization handles sparsity to some degree, a brief note on preprocessing would improve reproducibility.

### Trivial

- The paper cites Miller's law (7±2 items) to ground its feature count but then selects 20 patterns as a "good trade-off." A sentence reconciling the 20-feature choice with the cited cognitive limit would reduce friction for readers.
- No limitations or ethics discussion is included, which is somewhat conspicuous for a paper on AI text detection with societal implications.
- The paper jumps from Section 1 to Section 3 without an explicit Related Work section (likely stripped by the parser).

---

## Nice-to-Haves

- A brief within-subject analysis or regression controlling for engagement would strengthen the causal claims of the human trial.
- Testing against human post-editing of LLM output as an additional evasion scenario would broaden the robustness claims.
- Explicit reporting of the PoS tag consolidation mapping (from Penn Treebank to 9 categories) in the main text rather than just Table 1.

---

## Removed Points

These points are flagged to be removed; treat them with caution.

- *"The discussion of existing methods oversimplifies the landscape"* — This is a subjective framing criticism, not a verifiable factual error. Removed.
- *"The paper does not compare against GPTZero or other deployed detectors"* — Whether a specific deployed detector is included is a design choice; the paper's baselines (RoBERTa, DistilBERT) are reasonable and standard. Removed as preference-based.
- *"The paper should compare against other interpretable or pattern-based methods"* — The paper compares against vocabulary and stylometric features within the same framework, which is a fair and controlled comparison. This would be scope creep.
- *"The 20 features exceed Miller's 7±2 range"* — The paper explicitly acknowledges this as a trade-off ("should not significantly surpass this cognitive threshold"). Kept only as a trivial note, not a substantive weakness.
- *"The paper should discuss whether fewer patterns degrade performance"* — Figure 2 shows AUROC as a function of the number of features, effectively answering this question. Already addressed.
- *"The exact mapping should be included (in appendix if necessary)"* — Table 1 already provides this mapping. The critic missed it (likely parser-stripped image). Removed.

---

## Novel Insights

The main novel insight across the reviews is the **tension between interpretability and guidance in human-AI collaboration**: the paper's Level 1 (PoS tagging with manual pattern matching) outperformed Levels 2 and 3 (more automated highlighting) among engaged participants, suggesting that making AI assistance too easy (i.e., directly showing predictions) induces black-box reliance and degrades human judgment. This finding is more interesting than the absolute accuracy numbers and deserves more prominence. The reviews did not surface additional insights beyond what the paper itself contributes.

---

## Suggestions

1. **Revise the abstract and introduction** to clearly state that the 86% accuracy is for the subgroup of engaged participants who actively used the patterns, and also report the overall population accuracy (e.g., "overall accuracy improved from 43% to ~69%, and reached 86% among participants who actively engaged with the patterns").
2. **Report the full human trial methodology**: number of participants, recruitment method, randomization procedure, and explicit criteria for the engagement categories (unengaged vs. engaged vs. engaged+using patterns).
3. **Specify the paraphrasing model and prompt engineering details** in the robustness evaluation for reproducibility.
4. **Add a brief limitations paragraph** discussing domain specificity and the need to retrain patterns for new domains/models.

---

## Score and Decision

This paper addresses an important problem and proposes a genuinely interesting approach. The core idea — using interpretable grammatical patterns for human-in-the-loop detection — has merit, and the tiered human trial design yields a non-trivial finding about optimal AI guidance. The classifier results are strong.

However, the two major weaknesses are non-trivial: the abstract's unqualified 86% claim is misleading, and the human trial lacks essential methodological details (N, recruitment, engagement criteria) needed to evaluate whether the reported gains are causal. Both are fixable, but as presented, the evidence does not fully support the strength of the claims in the abstract. The paper would benefit from major revision with transparent reporting.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>