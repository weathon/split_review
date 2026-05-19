Now I have a thorough understanding of the paper and can verify each claim. Let me produce the final consolidated review.

## Summary

This paper introduces a formal cognitive-science framework (representative heuristics, kernel-of-truth) to quantify political stereotyping in LLMs. The authors define mathematical metrics (γ, ε, κ) to measure how much LLM responses exaggerate political positions compared to empirical survey data, test seven models across two datasets (ANES, MFQ), and propose three prompt-based mitigation strategies. The core finding is that LLMs systematically inflate Republican positions and deflate Democratic positions beyond both empirical reality and human stereotyping.

## Strengths

1. **Novel formalization of representativeness in LLMs using likelihood ratios.** The paper mathematically defines representativeness (Eq. 2), kernel-of-truth (Eq. 4), and exaggeration (Eq. 3, κ) in a way that is directly testable on LLM outputs. This goes beyond prior work that only measured political leanings without a formal cognitive-bias framework. The distinction between empirical probabilities (`p_{a,X}`) and believed probabilities (`p^B_{a,X}`) is maintained consistently throughout (lines 59–70).

2. **Consistent evidence of exaggeration across multiple models and datasets.** Figures 2–4 show that for both ANES and MFQ data, LLM responses systematically inflate Republican positions and deflate Democrat positions compared to both empirical means and human predictions across all seven tested models (GPT-4, GPT-3.5, Gemini, Gemini-Pro, Llama2-70B, Llama3-8B, Qwen2.5-72B). Table 2 formalizes this via ε parameters.

3. **Parallel comparison with human predictions, not just empirical data.** Figure 2 includes "Human Pred Mean" (responses from human participants on the Beliefs Question), allowing the paper to show that LLM exaggeration exceeds even human tendency to stereotype — strengthening the claim that the bias is model-specific.

4. **Prompt-based mitigation strategies with measurable effects.** Table 3 reports κ values across four prompt strategies (Baseline, AWARENESS, REASONING, FEEDBACK), showing that the highest κ values consistently occur at baseline and specific prompt strategies reduce κ, providing evidence that cognitive-science-inspired prompts can reduce exaggeration.

5. **Transparent reporting of exceptions and negative results.** Tables 1 and 2 note cases where γ or ε are negative, and the paper acknowledges model-specific exceptions (e.g., Llama3-8B showing opposite trends for certain moral foundations in Fig. 3).

## Weaknesses

### Fatal
None.

### Major

1. **No formal statistical inference.** Results are presented as point estimates with standard deviations, but no hypothesis tests are conducted (e.g., testing whether γ > 0 or ε > 0 reliably across questions). For example, Table 2 reports ε = 0.28 with sd = 0.62 for one condition — with noise this large relative to the estimate, it is unclear whether the effect is statistically meaningful. Without inferential statistics or confidence intervals, the strength of the evidence for the central claims ("LLMs exhibit representative heuristics") is difficult to assess.

2. **Small question set with strong conclusions.** The ANES analysis uses only 10 questions (9 on 7-point scales, 1 on a 4-point scale); the MFQ similarly covers a small number of moral dimensions. Drawing broad conclusions about "how LLMs exhibit representative heuristics" from such a limited question bank — even if tested across 7 models — overstates the generalizability of the findings.

3. **Mitigation evaluation measures κ but not accuracy.** The mitigation analysis (Table 3) reports whether κ decreases under different prompt strategies, but κ is a proxy for exaggeration, not a direct measure of response quality. The paper does not verify whether reduced κ corresponds to responses that are actually closer to empirical means or less stereotyped. No human evaluation of the mitigated responses is conducted. As a result, it is unclear whether the prompts genuinely reduce stereotyping or simply shift the model to a different stylistic register.

### Minor

1. **Mitigation experiments lack essential baselines.** The AWARENESS prompt explains the representativeness heuristic and then asks for a response; the FEEDBACK condition presents the model with its own answer and asks for revision. Neither condition includes a simple control such as "Please respond accurately" or a no-intervention re-query. Without these controls, it is difficult to attribute observed κ reductions to the specific heuristic-awareness mechanism rather than generic regression toward the mean or prompt effects.

2. **Some claims overstate the evidence given negative/zero values.** The paper states "All the models adhered to the kernel-of-truth hypothesis for ANES and MFQ (except for Llama3-8b)" (line 175), yet Table 1's color coding shows negative γ values exist for some topics even within models that are said to "adhere." Similarly, Table 2 notes that for ANES, Llama2-70b and GPT-4 do not show positive ε. These are acknowledged as exceptions but the main text's phrasing is stronger than the data warrants.

3. **κ metric formulation lacks justification from cited literature.** The paper introduces κ (Eq. 3) as `p^B_{a*,X+} / p^B_{a*,X-} = κ · p_{a*,X+}` without explaining why this specific ratio is the appropriate measure of "exaggeration" or how it relates to Bordalo et al. (2016). While the metric is intuitively clear, the paper does not justify why it should be preferred over alternatives.

4. **Human prediction dataset not adequately described.** The paper references Talaifar & Swann Jr (2019) for human prediction data on MFQ and ANES Beliefs Questions, but provides no details on sample size, demographics, recruitment methodology, or data collection timing — all of which are essential for assessing comparability with the LLM responses.

5. **No discussion of training data contamination.** Many ANES questions are well-known public survey items that likely appear in LLM training corpora. The kernel-of-truth results could partly reflect memorization rather than the cognitive mechanism the paper posits. This concern is not addressed.

6. **Analysis is limited to means; no distributional analysis.** The paper only analyzes mean-level responses. Showing that the *distribution* of LLM responses is more extreme than human responses (e.g., via variance or tail probabilities) would substantially strengthen the claim that a heuristic (which predicts extremity) is at work.

7. **Reproducibility details missing.** The paper does not specify the number of LLM queries per question, temperature settings, or any rejection/retry criteria. These are important for reproducibility, especially for the mitigation experiments where small prompt changes can produce large variance.

### Trivial

1. Typo in abstract: "suggeseting" → "suggesting" (line 7).

## Nice-to-Haves

- Replace point estimates with inferential statistics (e.g., test whether γ > 0 and ε > 0 across questions, accounting for multiple comparisons).
- Report per-question breakdowns alongside averages to show the variability behind the means.
- Add a synthetic experiment where representativeness is directly manipulated (e.g., by altering base rates in a description) to test whether LLM responses shift accordingly — this would directly test the heuristic mechanism rather than just observing that believed means are more extreme.
- Analyze individual response distributions (variance, tail probabilities) alongside means.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

1. **Circularity / ambiguous operationalization of representativeness** — REMOVED because it is factually incorrect. The paper clearly distinguishes empirical probabilities (`p_{a,X}`) from believed probabilities (`p^B_{a,X}`) throughout Section 3 (lines 57–70). The representativeness R (Eq. 2) uses empirical `p_{a,X}` with no superscript. The `P_{A^{(N)}}^{X+}` term in Eqs. 5–6 is defined as `Σ p_{a,X+} / Σ p_{a,X-}` (line 107) — i.e., empirical probabilities. There is no ambiguity and no circularity.

2. **Claim that κ conflates representativeness with baseline probability** — REMOVED. The κ equation explicitly normalizes the believed representativeness ratio by the empirical base rate `p_{a*,X+}`, which is precisely the correct normalization for measuring exaggeration.

3. **Claim that "stereotypes" definition is vague** — REMOVED. The paper provides a clear operational definition: "we consider 'stereotypes' as a distinct form of misalignment (between LLMs and human responses), involving particularly exaggerated judgments" (line 14).

4. **Claim that Eqs. 5–6 lack derivation/citation** — REMOVED. These equations are simple linear models that directly operationalize the representative heuristics hypothesis. They are self-explanatory given the definitions that precede them; no derivation is required.

5. **Claim that the paper overstates novelty about deviation being underexplored** — REMOVED. The paper's contribution is the formal cognitive-science framework and its specific mathematical operationalization (γ, ε, κ), not merely the observation that LLMs deviate from empirical positions. Prior work did not formalize LLM deviation through the lens of representative heuristics.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a genuinely novel observation that the paper itself misses — they largely converge on asking for stronger statistical validation, broader evaluation, and cleaner experimental controls.

## Suggestions

1. Add formal hypothesis tests (e.g., bootstrap or permutation tests) for whether γ > 0 and ε > 0, with per-question breakdowns. This is essential for establishing the reliability of the core claims.

2. Expand the question set significantly, or at minimum temper the claims to match the actual scale of the evaluation (10 ANES questions).

3. In the mitigation experiments, (a) add control conditions (e.g., "Please respond accurately"), (b) directly measure whether mitigated responses are closer to empirical means, and (c) conduct a human evaluation to assess whether reduced κ corresponds to less stereotyped content.

4. Discuss the potential for training data contamination (ANES data in LLM training corpora) and, if possible, test with questions designed to be absent from training data.

5. Provide missing experimental details (temperature, number of queries per question, rejection/retry criteria) for reproducibility.

## Score and Decision

**Originality**: Moderate — applying known formalisms (representative heuristics from cognitive science) to a new domain (LLM political biases) is a reasonable contribution.  
**Importance**: Moderate to high — understanding how LLMs systematically exaggerate political positions has real societal implications.  
**Claims support**: Weak to moderate — the evidence is suggestive but lacks statistical rigor; the evaluation scale is small.  
**Soundness of experiments**: Moderate — the framework is well-defined but the empirical backing is thin (few questions, no inference, incomplete mitigation controls).  
**Clarity of writing**: Good — the paper is generally well-organized and the methodology is clearly described.  
**Value to community**: Moderate — the formal framework could be useful if properly validated, but in its current form the empirical support is not strong enough to serve as a reliable reference.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>