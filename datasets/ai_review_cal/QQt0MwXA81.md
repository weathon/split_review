- Decision: Reject
- Avg Score: 6.20
- Scores: 8, 8, 5, 5, 5
Now I have all the information I need. Let me synthesize the review carefully, cross-referencing every claim against the paper.

## Final Consolidated Review

---

## Summary

This paper investigates whether LLMs exhibit human-like response biases by systematically modifying survey questions from the Pew American Trends Panel (ATP). Drawing on five well-documented response biases from social psychology (acquiescence, allow/forbid asymmetry, response order, opinion floating, odd/even scale effects) and three non-bias perturbations (typos, letter shuffles), it evaluates nine models across the Llama2, Solar, and GPT-3.5 families. The key findings are that no model consistently shows significant, directionally correct shifts for all biases while remaining unaffected by perturbations; RLHF-ed models are less sensitive to biases but more sensitive to perturbations; and a model's ability to replicate human opinion distributions is not correlated with exhibiting human-like response biases.

---

## Strengths

- **Systematic evaluation framework with non-bias perturbations as controls.** The paper pairs each bias modification with non-bias perturbations (typos, randomized letter changes) that humans are expected to be robust against (Section 2, Figure 1). This design tests the *specificity* of response changes — whether LLM sensitivity is unique to bias-relevant modifications or a general instability — which is a methodological advance over prior work that only checked directional alignment.

- **RLHF models show quantitatively documented opposite sensitivity patterns.** Comparing base Llama2 models with their chat counterparts (lines 162-169), the paper finds that RLHF-ed models show *less* sensitivity to bias modifications but *more* sensitivity to perturbations — in 23 out of 29 settings where both model pairs show significant effects, RLHF-ed models have 81% larger effect sizes on perturbations. This is a novel and precise characterization.

- **Uncertainty analysis tests a specific behavioral prediction.** Section 4 operationalizes a known human pattern (confident respondents are less affected by question modifications; citing hippler1987response) by measuring normalized entropy. Of nine models, only two show a weak positive correlation (r ≤ 0.5), with seven showing no significant correspondence — directly supporting the paper's main conclusion with a different behavioral dimension.

- **Decoupling opinion replication from bias alignment.** Section 5 (Figure 3) shows that a model's "representativeness" (how well its response distribution matches human opinion polls) is not correlated with its bias-alignment behavior. For instance, GPT-3.5 turbo and turbo-instruct have nearly identical representativeness scores but opposite bias patterns — a non-obvious finding that challenges a common proxy for human-likeness in prior work.

- **Dataset grounded in established social psychology literature.** The five response biases are drawn from well-studied survey design phenomena (Section 2.1, Table 1), and the 2578 question pairs are built on an existing validated instrument (ATP). This anchoring makes the negative findings interpretable and relevant to practitioners.

---

## Weaknesses

### Fatal
None. The paper's core empirical contribution — documenting LLM behavior across these five biases and three perturbations — is sound. No verified weakness invalidates the central findings.

### Major

- **The claim that perturbations "do not affect human responses" lacks direct citations and a human baseline on the specific stimuli used.**  
  The paper states that typos and randomized letter changes are "known to not affect human responses" (line 41) and that humans are "known to be robust against" them (line 68). However, it provides no citations supporting this claim specifically for survey-style multiple-choice questions. The citations in the paper (e.g., kalton1982effect, weisberg1996introduction) are about *response biases*, not about human robustness to typos/letter shuffles. This matters because one of the paper's central comparative findings — "unlike humans, all models display statistically significant changes to non-bias perturbations" (line 150) — depends on the claim. The paper explicitly acknowledges it does not run a human study on these exact modifications (line 247), so the assertion about human immunity on these specific stimuli is an assumption. While the paper can frame its findings as "LLMs are sensitive to perturbations that we expect would not systematically shift human responses," the stronger phrasing currently used ("that do not elicit significant changes in humans," abstract line 11) exceeds what the evidence supports.

- **The representativeness vs. bias-alignment correlation analysis lacks statistical rigor.**  
  Section 5 (lines 203-206, Figure 3) claims "there is little correspondence" between representativeness and bias-aligned behavior, but this is based on visual inspection of a scatter plot with only 9 data points (models). No formal correlation test is reported, and a sample of 9 provides very weak statistical power. Additionally, the representativeness metric is measured on *unmodified* questions while bias sensitivity is measured on *modifications*, so a null correlation is not particularly surprising. The paper should report a formal correlation (e.g., Spearman's ρ) with appropriate caveats, or acknowledge the analysis is exploratory.

### Minor

- **Effect sizes are not reported in the main results.** The heatmap (Figure 2) shows only significance and direction (blue/orange/hatched). While the paper references a full table in the appendix (Table tab:full_results), the main text does not summarize effect sizes. Since the paper's criterion for "human-like" behavior emphasizes significance, a reader cannot assess whether LLM effects are comparable in *magnitude* to the (often small) human effects documented in prior meta-analyses. The footnote on line 125 that "prior studies generally do not focus on magnitudes" is not universally true — many meta-analyses report standardized effect sizes.

- **No power analysis or discussion of minimal detectable effect.** With 50 samples per question per model, the paper does not discuss whether this sample size is adequate to detect the small effect sizes typical of human response biases. For binary-choice questions, the standard error of a proportion is ~0.07, making a ~14 percentage-point change detectable at p≈0.05; for multi-option questions, power is lower. A post-hoc power analysis or minimal detectable effect calculation would strengthen the credibility of null results (e.g., when models show non-significant Δ_b).

- **The uncertainty analysis (Section 4) shares the same human-baseline limitation.** The paper finds weak correlations for only 2 of 9 models, but no human correlation is reported for the same stimuli. While the paper cites hippler1987response for the human pattern, it doesn't provide the human effect size or confidence interval, so it is unclear what range of correlations would count as "human-like."

### Trivial
None.

---

## Nice-to-Haves

- **A small-scale human validation study** on a subset of the bias-modified and perturbation-modified questions (e.g., 100–200 participants on ~20 question pairs) would ground the evaluation and convert the paper's key assumption into a tested finding. This is the single highest-leverage improvement.

- **Replacing or supplementing the binary significance criterion with effect-size comparisons** (e.g., Cohen's d of Δ_b) and showing whether LLM effects fall within the range of human effects from prior meta-analyses would produce more nuanced and defensible conclusions.

- **Formal statistical testing** of the correlation between representativeness and a bias-alignment score (e.g., number of biases correctly aligned minus number of perturbation effects), with appropriate caveats about the small sample.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

1. **"The central claim is unsupported — the evaluation does not measure what it claims to measure because it lacks a human control condition."**  
   *Reason for removal: Overstated.* The paper's claim is explicitly scoped to comparing LLM behavior against *trends from prior social science studies* (line 38, line 247). The paper acknowledges the absence of a human study on the exact stimuli as a limitation. The framework *is* falsifiable within its own terms (if a model showed the expected pattern across all biases and no perturbation effects, the paper would accept it as human-like). The critic's assertion that the conclusion is "unfalsifiable" is incorrect. This is a legitimate methodological constraint but not a fatal or structural flaw that invalidates the paper's contribution.

2. **"The criterion for human-like behavior is overly strict and inconsistent with how response biases are studied in humans."**  
   *Reason for removal: Misunderstands the analysis design.* The paper uses a t-test *across questions* (aggregate, per bias type), not per-item testing (line 124). This is exactly how human response biases are studied at a population level. The paper does not set a strict binary "pass/fail" criterion; it presents results observationally (e.g., "no model aligns across *all* biases" is a factual observation, not an a priori threshold). The claim that "human participants themselves almost certainly would not meet this bar" is speculative — the paper never asserts that the bar must be met for a model to be "human-like" in any absolute sense.

3. **"The 'all' criterion conflates bias sensitivity and perturbation sensitivity."**  
   *Reason for removal: These are presented as two distinct findings, not conflated.* The paper clearly separates them: "no model aligns with known human patterns across all biases" and "all models display statistically significant changes to non-bias perturbations" (lines 150-151). These are separate empirical observations.

4. **"Introduction assumes validity of evaluation criteria."**  
   *Reason for removal: Generic.* Every paper assumes the validity of its evaluation methodology. The criteria (t-tests, significance thresholds) are standard.

5. **"Methodology description is vague about bias implementations."**  
   *Reason for removal: Partially addressed.* The paper describes which modifications were manual (acquiescence, allow/forbid) and which were systematic (option order, removal/appending) (lines 79-80). More detail is always possible but the paper provides sufficient information for the level of analysis.

6. **"Manual modifications introduce experimenter bias."**  
   *Reason for removal: Generic and unsupported.* For acquiescence bias (adding "allow" vs. "forbid" to questions), manual modification is the only feasible approach given the diversity of question content. The modifications follow principled rules.

---

## Novel Insights

The reviews surface two insights that go beyond the paper's own contributions. First, the finding that RLHF *amplifies* sensitivity to superficial perturbations (typos, letter shuffles) while *dampening* sensitivity to meaningful bias modifications reveals an important and underappreciated failure mode of alignment techniques: RLHF may be optimizing for surface-level "helpfulness" at the cost of making models more brittle to irrelevant prompt variations. Second, the decoupling of representativeness (opinion matching) from bias alignment suggests that current evaluations of LLMs as human proxies may be measuring orthogonal capabilities — a model can match population opinion distributions while behaving wildly differently from humans under systematic prompt variation, which has implications for any downstream use requiring behavioral fidelity, not just output distributions.

---

## Suggestions

1. **Add explicit citations for the claim that typos and letter shuffles do not systematically shift human survey responses**, or soften the language to "we hypothesize these perturbations would not affect humans based on general principles of reading comprehension." This is a quick fix that would significantly strengthen the perturbation analysis.

2. **Include a supplementary table of mean Δ_b and Δ_p values (with standard deviations or Cohen's d) in the main paper**, not just in the appendix. This would allow readers to assess whether LLM effect sizes are plausible given human effect sizes from prior literature.

3. **Replace the visual-only correlation claim in Section 5 with a formal Spearman rank correlation** (with the caveat of n=9) or explicitly reframe it as an exploratory observation.

4. **Add a brief power analysis** discussing the minimal detectable effect given 50 samples per question, to contextualize null findings.

5. **Clarify the scoping of claims**: replace "perturbations that do not elicit significant changes in humans" with "perturbations that we expect would not elicit significant changes in humans" unless direct human evidence is provided.

---
