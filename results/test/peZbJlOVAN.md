Now I have all the information needed to verify each claim against the paper. Let me produce the consolidated review.

## Summary

This paper introduces a benchmark for evaluating the robustness of instruction-following LLMs against prompt injection attacks, using an open-book QA setup with four datasets (NaturalQuestions, TriviaQA, SQuAD, HotpotQA) and two metrics — Performance Drop Rate (PDR) and Instruction Discrimination Rate (IDR). Through experiments with eight models (proprietary and open-source), the paper finds that instruction-following capability and model size do not necessarily correlate with injection robustness, and that more robust models can be disproportionately affected by explicit "ignore previous instructions" attack phrases. The work also analyzes injection position, instruction type, and attack/defense mechanisms.

## Strengths

1. **Novel benchmark with principled, quantitative metrics.** The paper fills a gap noted in its own literature review — "comprehensive and quantitative evaluations on assessing the robustness of LLMs against prompt injection attacks are still absent" — by introducing PDR and IDR, which measure both performance degradation and whether the model prioritizes original vs. injected instructions. The QA-based setup enables scalable automatic evaluation while grounding the task in a realistic retrieval-augmented generation scenario.

2. **Counterintuitive finding about instruction-following and robustness.** The paper empirically demonstrates that high instruction-following performance (as measured by AlpacaEval win rate) does not predict injection robustness. Zephyr-7B-Beta has a 90.60% AlpacaEval win rate but is the least robust model, while GPT-3.5-Turbo is among the most robust despite not being the largest or highest-ranked. This finding, supported consistently across all four datasets (Figures 2–3), challenges the implicit assumption that better instruction-following implies better instruction discrimination.

3. **Multi-dimensional analysis of attack and defense factors.** The paper systematically investigates injection position (start, middle, end), instruction type (context-relevant vs. irrelevant), prompt order (QCA vs. CQA), and attack/defense strategies. This yields specific, non-obvious insights — e.g., that robust models show the largest vulnerability when injection is at the end (Figure 5), and that jailbreak prefixes cause a disproportionate relative PDR increase in otherwise robust models (Figure 6). These analyses go beyond a single benchmark score and inform practical defense considerations.

4. **Human evaluation corroborates automatic metrics.** The human evaluation on 100 samples (three annotators, 80.5% agreement, Fleiss's κ = 0.7302) with a five-category annotation scheme confirms the overall robustness rankings from automatic evaluation (Figure 7), lending qualitative reliability to the quantitative findings. The human annotation also captures nuanced behaviors (e.g., Claude-2 and Zephyr-7B often answering both questions) that automatic metrics cannot distinguish.

5. **Investigation of both context-relevant and irrelevant injected instructions.** Testing irrelevant injections (e.g., "Come up with a haiku poem") alongside context-relevant questions reveals that most models are more robust to irrelevant instructions, while smaller models with limited context understanding show minimal effect (Figure 4). This helps differentiate factors affecting robustness.

## Weaknesses

### Fatal
None.

### Major

1. **Unvalidated GPT-4 generated QA pairs for three of four datasets.** For NaturalQuestions, TriviaQA, and HotpotQA, each context has only one gold QA pair, so the authors use GPT-4 to generate alternative (q', a') pairs. The paper provides no validation that GPT-4's generated answers (a') are actually extractable from the context — no manual inspection, no automatic check, no accuracy statistic. This directly impacts the reliability of Adv'(f) and consequently IDR for these three datasets. If GPT-4's answers are frequently wrong (not present as answer spans in the context), then: (a) a model that correctly ignores the injected instruction could be penalized for failing to match a non-existent span, and (b) a model that naively follows the injected instruction would also be penalized. The direction and magnitude of this distortion are unpredictable. **Scope note:** This primarily affects IDR and the secondary analysis; PDR (the main robustness metric) depends only on accuracy on the original question and is not affected by this issue. The paper would be significantly strengthened by reporting a validation statistic (e.g., what fraction of GPT-4's answers match an extractable span) and ideally a 50–100 sample manual check.

### Minor

1. **Imprecisely phrased claim about "more susceptible to compromise."** The abstract states that "models with a better grasp of the context and instruction-following capabilities will potentially be more susceptible to compromise by injected instructions" (line 8). The data (Figure 6) shows that robust models experience a *larger relative increase* in PDR under specific jailbreak prefixes. However, weaker models already have very high PDR without attack (little room for additional harm), and robust models still have substantially lower PDR in absolute terms after attack. The finding is interesting and worth reporting, but the current wording invites misinterpretation as "robust models are more likely to be compromised overall." The paper should state this as a relative effect on robustness degradation under explicit attack phrases, not as greater overall susceptibility.

2. **No confidence intervals or statistical tests on main results.** The bar charts in Figure 2 show point estimates for 8 models across 4 datasets (1000 samples each). Standard errors are not negligible at this sample size, yet no error bars or significance tests are provided. It is unclear whether differences like Vicuna-33B vs. LLaMA2-70B-Chat on HotpotQA are real or noise. While the trends are consistent across datasets (which provides some implicit validation), the lack of uncertainty quantification weakens the precision of the ranking claims.

3. **Limited exploration of how refusal behavior interacts with automatic metrics.** The human evaluation notes that GPT-3.5-Turbo occasionally refuses to answer (line 356). When this happens, both Adv and Adv' go to zero, which could bias IDR. A brief analysis of how frequent refusal is in the automatic evaluation and how it affects the reported metrics would improve transparency.

4. **Misleading description of Alpaca-7B as "leading."** The paper states it evaluates "eight leading instruction-following LLMs according to AlpacaEval" (line 115). Alpaca-7B has a 26.46% AlpacaEval win rate — far below the other models and not "leading" by any standard. While the table transparently reports this number, the blanket "eight leading" phrasing in the text is inaccurate.

### Trivial
None.

## Nice-to-Haves

- A brief analysis of agreement between automatic metrics (EM/F1) and human labels on the 100-sample human evaluation set, to help readers calibrate how much to trust the automatic results.
- Error bars or bootstrapped confidence intervals on the bar charts (Figure 2).
- A more extended discussion of the limitation that automatic EM/F1 evaluation cannot distinguish between "answered original question correctly" and "answered original question correctly but also followed injected instruction" (the human evaluation partially addresses this).

## Removed Points

- **"System prompt doubles as a defense" concern:** The paper explicitly describes the system prompt defense in Section 3.1 (lines 149–155) and Section 5.3 examines the no-defense condition (Figure 6). This is already well-addressed and transparently documented.
- **Criticism about "not yet released" or unavailable models:** No such issue — all models cited are publicly known and available.
- **Any formatting/style nitpicks or requests for missing appendix content:** Removed per guidelines (these are parser artifacts).

## Novel Insights

The review corpus does not surface a genuinely novel synthesis beyond what the paper itself already contributes. The most interesting tension in the reviews — that the GPT-4 generation gap mainly threatens IDR while PDR is robust to it — actually helps clarify that the paper's primary findings (robustness rankings, lack of correlation with instruction-following) rest on firmer ground than the unvalidated component might suggest.

## Suggestions

1. **Validate the GPT-4 generated QA pairs.** Report the percentage of GPT-4's answers that can be exactly matched or matched by F1 against extractable spans in the context, on at least a manually inspected sample of 50–100 examples per dataset. If accuracy is high, this concern is largely resolved; if not, consider restricting the IDR analysis to SQuAD only or developing a filtering strategy.

2. **Rephrase the "more susceptible to compromise" claim.** Replace the blanket statement in the abstract/conclusion with a precise description: robust models experience a larger relative increase in PDR under specific jailbreak prefixes, even though they remain more robust in absolute terms.

3. **Add confidence intervals.** Bootstrap the PDR and IDR estimates and report standard errors or confidence intervals in the bar charts, so readers can assess whether observed differences are meaningful.

4. **Acknowledge the refusal behavior gap.** Briefly note whether GPT-3.5-Turbo's occasional refusal affects the automatic metric calculations and how.

## Score and Decision

The paper makes a solid contribution: a well-motivated benchmark, clean metrics, extensive experiments, and genuinely non-obvious findings about the disconnect between instruction-following capability and injection robustness. The main methodological gap (unvalidated GPT-4 generated QA pairs) is real but scoped — it primarily affects IDR, not the paper's primary PDR-based findings — and is fixable with a validation check. The other issues are presentation-level. The contribution stands on its own merits.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>