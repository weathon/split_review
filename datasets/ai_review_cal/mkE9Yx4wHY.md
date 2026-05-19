- Decision: Reject
- Avg Score: 5.50
- Scores: 5, 6, 3, 8
Now I have all the information needed. Let me construct the consolidated review.

---

## Summary

This paper introduces *Alignment with Anchor Preference Pairs*, a method for constructing DPO preference pairs to improve LLM self-exclamation quality without annotated rationales. The key idea is to categorize model responses on each prompt into three groups—consistently correct, variable, and consistently incorrect—and apply tailored preference-pair strategies for each. On four reasoning benchmarks (AQuA-Rat, ARC-Challenge, LogiQA, OpenbookQA), the method improves explanation quality relative to a judge-only ranking baseline, with positive ∆W-L margins on two datasets versus the base model.

## Strengths

- **Novel categorization-based preference pair construction.** The three-group taxonomy (consistently correct / variable / consistently incorrect) with strategy-specific handling is a genuine departure from existing self-alignment methods that construct preference pairs solely from judge-based scores. This is clearly described in Algorithm 1 and Section 3.3.

- **Consistent empirical advantage over the judge-only ranking baseline.** On all four datasets, $\mathcal{M}_{\text{Anchor}}$ achieves higher (or less negative) $\Delta_{W-L}$ than $\mathcal{M}_{\text{Rank}}$, the pure judge-based counterpart. On ARC-Challenge and LogiQA, $\mathcal{M}_{\text{Anchor}}$ reaches positive $\Delta_{W-L}$ (+3.3% and +6.9%) while $\mathcal{M}_{\text{Rank}}$ remains negative (−3.18% and −5.9%). The improvement direction is consistent across all four benchmarks.

- **Quantified measurement of SFT-driven explanation degradation.** The paper documents that supervised fine-tuning for classification reduces explanation quality by 15.6–30.9% $\Delta_{W-L}$ across datasets (Table 1), then shows that anchor-aligned alignment narrows or reverses this gap—establishing both the problem and the method's effect clearly.

- **Methodological precautions in experimental design.** The use of separate SFT models per dataset (avoiding multi-task contamination), LoRA adapters for DPO regularization, and a self-contained judge ($\mathcal{M}_{\text{Base}}$ during alignment) are well-motivated choices that reduce confounding factors.

## Weaknesses

### Fatal

None. The core claim—that the anchor preference pair method improves explanation quality over a judge-only baseline—is supported by the empirical results.

### Major

1. **The comparison between $\mathcal{M}_{\text{Anchor}}$ and $\mathcal{M}_{\text{Rank}}$ conflates multiple design differences, making attribution unclear.** The two methods differ in several ways simultaneously: (a) for variable prompts, $\mathcal{M}_{\text{Anchor}}$ uses ground-truth labels to restrict winning explanations to correct predictions, while $\mathcal{M}_{\text{Rank}}$ does not; (b) for consistently incorrect prompts, $\mathcal{M}_{\text{Anchor}}$ generates a winning explanation from a debater prompted with the correct answer, while $\mathcal{M}_{\text{Rank}}$ picks the least-bad wrong explanation; (c) even for consistently correct prompts, $\mathcal{M}_{\text{Anchor}}$ selects the *lowest*-scoring explanation as the loser (Algorithm 1, line 156: $\min$ score) while $\mathcal{M}_{\text{Rank}}$ selects a *random* loser. These confounds mean the improvement could be driven primarily by correctness-based filtering or debater injection rather than the categorization and tailored strategies per se. A clean ablation—comparing $\mathcal{M}_{\text{Anchor}}$ against a variant that uses ground-truth labels for filtering (i.e., always preferring correct-prediction explanations when available) but does *not* apply the category-specific refinements—would isolate the grouping contribution. Without it, the evidence for "tailored strategies per category" being the causal factor is weaker than claimed.

### Minor

2. **No human evaluation of explanation quality.** The paper's central dependent variable—self-explanation quality—is measured entirely through Llama-3-70B-Instruct as an automated judge. While LLM-as-Judge is standard practice in the alignment field, the claim is about improving outputs meant for human interpretation. No human study (even small-scale), inter-annotator agreement, or correlation with human judgments is provided. A 100-sample validation study would substantially increase confidence that the measured improvements are perceptible to humans.

3. **Lack of statistical grounding for reported results.** (a) The $\pm$ values on accuracy in Table 1 are not defined (standard deviation across runs? across prompts? standard error?) and no number of training runs is reported. For a method with stochastic components (sampling temperature, DPO steps, random loser selection in $\mathcal{M}_{\text{Rank}}$), run-level variance is important. (b) Win-rate differences between $\mathcal{M}_{\text{Anchor}}$ and $\mathcal{M}_{\text{Rank}}$ are reported without confidence intervals or significance tests, despite $N=16$ samples per prompt being available for bootstrapping. (c) The abstract uses "significantly improves" without statistical testing—an overstatement given the modest absolute margins (1–5 percentage point win-rate differences).

4. **Missing dataset composition statistics.** The distribution of prompts across the three categories (consistently correct, variable, consistently incorrect) is not reported for any dataset. Without this information, the reader cannot assess how often each strategy is deployed or understand the $\lambda$ analysis, which relies on only 4 data points (one per dataset). A 4-point trend is suggestive but too weak to be conclusive.

5. **Text-algorithm inconsistency for the consistently correct case.** The main text (Section 3.3, line 133) defines $\mathbb{A}_{i}^{l}$ for consistently-correct prompts as "all explanations with scores lower than the maximum," while Algorithm 1 (line 156) defines it as explanations with the minimum score. These differ: the text allows multiple lower-scoring candidates, the algorithm restricts to the single worst. The paper should clarify which is correct.

### Trivial

6. **Figure 1 (per-criterion scores):** The differences between $\mathcal{M}_{\text{Anchor}}$ and $\mathcal{M}_{\text{Rank}}$ appear visually small on several criteria; error bars would aid interpretation.

## Nice-to-Haves

- A human evaluation study on a randomly sampled subset of 100–200 prompts across datasets, with pairwise comparisons between $\mathcal{M}_{\text{Anchor}}$ and $\mathcal{M}_{\text{Rank}}$ outputs, would dramatically strengthen the paper's central claim.
- Reporting the distribution of prompt categories for each dataset would make the $\lambda$ analysis substantially more interpretable.
- Clarifying the $\pm$ notation (standard deviation across runs? across prompts? how many runs?) and adding bootstrapped confidence intervals for win rates would improve statistical transparency.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"Label leakage" framing (harsh critic, Critical Issue 1):** The critic describes M_Anchor's use of ground-truth labels as "direct label leakage." This is a misleading characterization. Using ground-truth labels to guide preference pair construction is the explicit, stated design of the anchor method, not an unwanted information leak. The paper is transparent about requiring labels. The underlying concern (confounded comparison) is valid and retained as Major weakness #1; the "leakage" framing is removed.

2. **"Distribution shift from M_Base as debater" (harsh critic, Section 3 note):** The critic claims using M_Base as debater introduces a problematic distribution shift because it's a "different model." In fact, M_Base and M_SFT both start from Llama-3-8B-Instruct; M_Base is the unmodified starting point. The paper acknowledges using the debater for consistently-incorrect prompts and this is a deliberate design choice. The concern is speculative and does not identify a concrete artifact in the results.

3. **"Limitation that the method requires classification labels not fully discussed" (harsh critic, limitations section):** The paper's limitations section (line 312) explicitly states: "the selection of preference pairs via the anchor strategy relies on a classification task as the probing mechanism, which restricts its applicability." The critic's observation is a restatement of what the paper already acknowledges.

4. **"Ordinal-to-interval scaling issue" (harsh critic, Section 2 note):** The critic notes that qualitative verdicts (excellent/satisfactory/needs improvement/unsatisfactory) are converted to numeric scores and summed. This is standard practice in NLP evaluation and does not constitute a meaningful weakness of a methods paper.

5. **"Missing justification for N=4" (harsh critic, Section 4.2):** The paper states that "N=4 provides a reasonable assessment of the model's consistency and variability." For a 4-option multiple-choice task, four samples per prompt is a standard and well-motivated choice. The critic's request for a "small study varying N" goes beyond what is expected.

6. **"No human evaluation as a critical/fatal issue" (harsh critic, Critical Issue 2):** While the absence of a human study is noted (retained as Minor weakness #2), the critic overstates this as a "significant gap" that undermines the core contribution. Given that LLM-as-Judge evaluation is the prevailing standard in the self-alignment literature (e.g., Self-Rewarding, Meta-Rewarding, Constitutional AI), the lack of a human study does not put the paper's claims in jeopardy—it is a gap, but a minor one by field norms.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a genuinely novel observation that the paper itself does not make.

## Suggestions

1. **Add an ablation study** comparing $\mathcal{M}_{\text{Anchor}}$ against a variant that uses ground-truth labels to filter preference pairs (correct-prediction explanations as winners; incorrect-prediction explanations as losers) but does not apply the group-specific scoring refinements. This would isolate whether the categorization/tailoring strategies themselves add value beyond correctness-aware filtering.

2. **Clarify the $\pm$ notation** in Table 1 (standard deviation across what unit?), add confidence intervals for win-rate estimates via bootstrapping, and state the number of independent training runs.

3. **Report the per-dataset distribution** of prompts across the three categories (consistently correct / variable / consistently incorrect) to contextualize the $\lambda$ analysis and the frequency of each strategy.

4. **Resolve the text/algorithm inconsistency** for losing-explanation selection in the consistently-correct case (all-below-max vs. min-only).

5. **Tone down "significantly"** in the abstract and claims unless statistical tests justify it. The consistent directional advantage is the real finding; claiming significance without evidence is unnecessary.
