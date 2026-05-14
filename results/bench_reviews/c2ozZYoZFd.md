Now I have a thorough understanding of the paper and all the calibration anchors. Let me write the final consolidated review.

---

## Summary

This paper presents a meticulous, multi-pronged re-examination of Nguyen et al. (2024) (an ICLR 2025 Oral paper that introduced min-p sampling), demonstrating that the original paper's own data and code fail to support its central claim of min-p's superiority. The re-analysis covers all four lines of the original evidence: (1) human evaluations (revealing omitted data, incorrect statistical pooling, and mischaracterized qualitative feedback), (2) NLP benchmark evaluations (using a novel "best-of-N" methodology to equalize hyperparameter tuning volume), (3) LLM-as-a-Judge evaluations (exposing methodological ambiguity and unbalanced tuning), and (4) community adoption claims (showing inflated, retracted statistics). The paper extracts six general lessons for rigorous empirical ML research, turning a specific critique into a broadly applicable blueprint.

## Strengths

- **Novel methodological contribution — "best-of-N" hyperparameter control**: The paper introduces a principled subsampling-based procedure (Sec. 3.1) that equalizes hyperparameter search volume across methods and measures maximum attainable performance as a function of tuning budget. This directly addresses the common pitfall of methods winning simply because they were tuned more. Figures 4–5 compellingly show min-p's advantage vanishing under equal tuning. This methodology extends beyond the case study and is proposed as a general tool for detecting cherry-picking (Sec. 1, Sec. 6 Lesson 1).

- **Textbook-quality statistical re-analysis of human evaluations**: The re-analysis (Sec. 2.2, Table 1) replaces the original paper's single pooled t-test with 12 one-sided paired t-tests with Bonferroni correction, plus an intersection-union test for the "consistently outperforms" claim. This reveals that only 1 of 12 comparisons is significant after correction, directly falsifying the claim of consistent superiority. The use of 95% confidence intervals (Fig. 1) provides transparent visual evidence.

- **Data transparency yields concrete discoveries**: The authors discovered that one-third of human evaluation scores (for basic sampling) were excluded without justification (Sec. 2.1). Their manual annotation of qualitative responses (Sec. 2.3, Fig. 2) showed basic sampling was preferred by more evaluators than min-p, directly contradicting the original paper's qualitative summary. This demonstrates the irreplaceable value of releasing and independently inspecting raw data.

- **Comprehensive coverage across all four lines of evidence**: The paper systematically addresses human evaluations, NLP benchmarks, LLM-as-a-Judge evaluations, *and* community adoption claims. This breadth makes the overall critique far more compelling than if it targeted a single experiment, and it builds a cumulative case that the original paper's conclusions are unsupported across the board.

- **Actionable, grounded lessons for the community**: Section 6 distills six concrete lessons (controlling for hyperparameter volume, correct statistical testing, data transparency, scrutinizing qualitative claims, methodological clarity, watching for selective reporting) directly from the case study. These are pedagogically useful and serve as a checklist for reviewers and researchers.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **Abstract overstates the scope of the NLP benchmark sweep**. The abstract claims "Extensive hyperparameter sweeps on NLP benchmarks show..." (plural), but the hyperparameter sweep was conducted only on GSM8K (the authors are transparent about this limitation at lines 429–431, citing compute constraints of ~6000 A100-hours). The main text is appropriately scoped ("we only evaluated GSM8K CoT"), but the abstract's plural "benchmarks" could mislead readers about the breadth of the empirical counter-evidence on this point. Changing "benchmarks" to "a benchmark" or "GSM8K" would resolve this.

### Trivial

- **The selective reporting claim in Section 4.3 relies on a Telegram post by the original first author** rather than a direct re-computation from the publicly available raw data. While the Telegram admission is probative and the paper is transparent about its source, the evidence would be stronger if the authors independently recomputed win rates from the original data to verify the claim. This does not undermine the overall conclusion about the LLM-as-a-Judge evaluations, which already stands on multiple independent criticisms (under-specification, indirect design, hyperparameter imbalance).

## Nice-to-Haves

- Extending the NLP benchmark sweep to GPQA (the other benchmark used in the original paper) would more thoroughly substantiate the counter-claim. The authors already acknowledge compute limitations; this is a natural direction for future work rather than a requirement for the current submission.

## Removed Points

*These points are flagged to be removed, treat them with caution.*

1. **"Overstated generality — single-benchmark result conflated with multi-benchmark conclusion" (Harsh Critic, labeled "Critical Issue 1")**: Partially valid in spirit but overblown in severity. The abstract overstatement is a phrasing issue, not an evidential gap. The paper is fully transparent about the GSM8K-only scope in the main text. The point is retained but downgraded from "Critical" to "Minor" above, and the critic's recommendation to "tone down the NLP claim in the abstract" is preserved as a Minor weakness.

2. **"Provide stronger evidence for the selective reporting claim" (Harsh Critic)**: Retained as Trivial. The Telegram post is evidence; demanding re-computation from raw data is a nice-to-have, not a defect.

3. **"Missing experiments — extending to GPQA" (Harsh Critic)**: Moved to Nice-to-Haves. The paper explicitly scopes this out due to compute budget and already demonstrates its point on GSM8K.

4. **"The paper's qualitative human responses contradict this" (Strength Finder item about qualitative annotation)**: This is actually a strength of the current paper's own analysis, not a weakness. The Strength Finder's characterization is accurate — retained as a strength above.

5. **Strength Finder's "compelling visual communication"**: Retained as a supporting strength but merged into other points, as it's a presentation quality rather than a standalone contribution.

## Novel Insights

Beyond the paper's own contributions, a noteworthy insight emerges from the synthesis of the four lines of evidence: the pattern of errors is systematic rather than incidental. The original paper omitted data that hurt min-p (basic sampler scores), pooled across settings in a way that favored min-p (using poorly-chosen top-p hyperparameters in the low-diversity condition), tuned min-p 2–10× more than baselines in LLM-as-a-Judge evaluations, reported the higher of two scores for min-p but the lower for top-p, and inflated community adoption numbers by an order of magnitude. Each error individually might be dismissed as a mistake; collectively they form a consistent directional pattern that the "best-of-N" methodology helps make visible. This pattern-revelation function — where a fairness-control method exposes not just a lack of advantage but a systematic tilt — is a meta-insight that strengthens the case for adopting such controls broadly.

## Suggestions

- **Fix the abstract**: Change "Extensive hyperparameter sweeps on NLP benchmarks" to "Extensive hyperparameter sweeps on GSM8K" or "an NLP benchmark" to accurately reflect scope. This is a one-line fix.
- **Strengthen Section 4.3**: If the raw LLM-as-a-Judge data is publicly accessible, independently recompute win rates rather than relying solely on the Telegram post. If not feasible, add a sentence acknowledging the evidence source and its limitations explicitly.
- **Clarify the "best-of-N" naming**: The paper uses "best-of-N" to describe subsampling hyperparameter configurations, which may confuse readers familiar with the standard usage (selecting the best of N sampled outputs, e.g., Nakano et al. 2021). A brief disambiguation note would help.

## Score and Decision

**Anchor comparison:**

| Path | Avg Score | How this paper compares |
|------|-----------|------------------------|
| `1CR1MTIgmq.md` (TPAMI rebuttal) | 0.00 | The 0.00 paper was purely an attack with no methodological contribution. The current paper is fundamentally different: it contributes a novel methodology (best-of-N), generalizable lessons, and rigorous statistical framework. |
| `UKPDpKGXAi.md` (EEG confound) | 2.00 | The 2.00 paper pointed out a confound but had limited contribution and poor presentation. The current paper has far greater depth, breadth (four evidence lines), and constructive value. |
| `fZJvPuadUT.md` (Optimal Stopping vs BoN) | 4.00 | The 4.00 paper had a theory-practice gap and questionable novelty framing. The current paper's best-of-N methodology is more directly practical and its claims are well-scoped. |
| `cPTgQDMD5p.md` (AutoDeco, decoding) | 5.00 | The 5.00 paper is topically related (decoding/sampling) but had methodological concerns about training labels and missing baselines. The current paper is more methodologically rigorous. |
| `GLPmZhhCAE.md` (NH-Fair benchmark) | 5.50 | Similar theme: showing that a well-tuned baseline beats fancy methods. NH-Fair contributed a large benchmark; the current paper contributes a novel methodology and a comprehensive critique. Comparable in quality, different in genre. |
| `M7TNf5J26u.md` (AstaBench) | 7.00 | Both are rigorous, well-executed contributions. AstaBench is broader in scope (benchmark suite); the current paper is deeper in methodological critique and statistical rigor. |
| `Ml8t8kQMUP.md` (SAEnce) | 7.00 | Both earned strong scores for methodological rigor. SAEnce contributed a novel causal inference procedure; the current paper contributes a novel fairness-control methodology and a replicable blueprint. |

The paper is methodologically rigorous, contributes a novel and practical methodology (best-of-N hyperparameter control), and delivers a compelling case study with generalizable lessons. The weaknesses are minor (abstract phrasing) to trivial (informal evidence source for one sub-claim). It compares favorably to the 5.50 NH-Fair anchor (similarly rigorous but our paper has a novel methodology) and sits at a level comparable to the 7.00 anchors, which earned Oral decisions for their rigor and community value. The scope is narrower (a case study rather than a large benchmark or system), but the execution is excellent and the extracted lessons have broad applicability.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>