Now I have all the information needed. Let me produce the final consolidated review.

## Summary

This paper introduces GSM-Symbolic, a benchmark generated from symbolic templates of GSM8K problems that enables controlled, distributional evaluation of LLM mathematical reasoning. The authors conduct a large-scale study across 25 open and closed models, demonstrating that LLMs exhibit substantial performance variance across different instantiations of the same question, degrade and become more variable as problem complexity increases, and suffer catastrophic drops (up to 65%) when irrelevant clauses are added (GSM-NoOp), with failures persisting even when the same question is provided as a few-shot example. The work provides strong evidence that LLM mathematical reasoning is best characterized as pattern matching rather than genuine logical inference.

## Strengths

1. **GSM-Symbolic's symbolic templates enable controlled, distributional evaluation of LLM reasoning, going beyond single-point metrics.** Section 3.1 and Figure 1 illustrate how templates parameterize names, numbers, and conditions to generate diverse instantiations of the same logical problem, allowing accuracy to be measured as a distribution (Figure 2) rather than a single number. This directly supports the claim that current GSM8K single-point evaluations are unreliable.

2. **Systematic ablation of change type (names vs. numbers) reveals that LLMs are far more sensitive to numerical variations.** Section 4.2 and Figure 4 show that when only proper names are changed, original GSM8K performance remains near the center of the distribution, but shifting to numerical changes (or both) causes a clear leftward shift and increased variance. A true formal reasoner would be invariant to such superficial changes.

3. **Performance degrades and variance increases monotonically as the number of clauses grows, showing fragility under increased complexity.** Section 4.3 and Figure 6 present distributions for GSM-M1 → GSM → GSM-P1 → GSM-P2 with very consistent shifts leftward and widening variance across all six models shown, providing multi-model evidence that LLM reasoning does not scale linearly with problem steps.

4. **GSM-NoOp demonstrates catastrophic drops (up to 65%) from irrelevant clauses, with in-context shots of the same question failing to recover performance.** Section 4.4 and Figure 7a show the largest drops (e.g., Phi-3-mini > 65%), while Figure 7b shows that even with 8 shots of the exact same question from GSM-Symbolic (NoOp-Symb), performance remains within the original standard deviation and does not recover. This is the paper's strongest evidence that LLM "reasoning" is pattern matching rather than logical inference.

5. **Large-scale study across 25 open and closed models (2B–27B plus GPT-4o, o1-mini, o1-preview) strengthens the generality of conclusions.** Nearly 500 total evaluations make the observed trends harder to attribute to a single architecture or training set.

6. **The NoOp-Symb experiment (8 shots of the same question from GSM-Symbolic) shows that even near-identical training examples with correct reasoning chains do not help models ignore irrelevant clauses.** This goes beyond prior work (GSM-IC) by showing the issue is not merely distracting context but a fundamental inability to separate relevant from irrelevant information.

## Weaknesses

### Fatal

None.

### Major

None. The paper's core claims are well-supported by the evidence.

### Minor

1. **The kiwi example used to illustrate GSM-NoOp (Figure 4) is not unambiguously irrelevant.** The clause "but five of them were a bit smaller than average" could be interpreted by some as implying those kiwis should not be counted—the word "but" signals a contrast, and in real-world contexts, "smaller than average" produce are sometimes considered substandard. While the paper's interpretation (all kiwis count unless explicitly discarded) is correct for the math problem, this ambiguity weakens the example's force as a demonstration of models' failure to ignore irrelevant clauses. A stronger design would use clauses that are *uncontroversially* irrelevant (e.g., "they were sold in a different store" or "he also had an apple"). The broader NoOp finding is still robust across multiple templates, but the headline example could be sharper.

2. **The data contamination hypothesis (Section 4.1) is not explored against alternative explanations.** The paper notes that for 21/25 models, GSM8K accuracy lies on the right tail of the GSM-Symbolic distribution, suggesting data contamination. However, an equally plausible explanation is distributional shift: GSM-Symbolic samples numbers from wider ranges (5–100 and 100–500) and uses unfamiliar proper names, which could shift the entire distribution leftward even without contamination. The paper presents contamination as "one explanation" (appropriately hedged), but does not discuss or control for the distributional-shift alternative. A comparison to a version of GSM-Symbolic using the original GSM8K values would strengthen this claim.

3. **The template selection process (100 out of 1319 test examples) lacks documented criteria.** The paper states it uses 100 templates for "manageable dataset size" but does not specify whether these 100 were randomly selected, stratified, or chosen based on any criteria. The final automated check ("if fewer than two models answered correctly, review manually") suggests some templates may be problematic. Without documentation of selection methodology, it is unclear whether the observed patterns generalize to the full GSM8K test set.

4. **No analysis of error types on GSM-Symbolic variance sets.** The paper reports accuracy drops but does not categorize *how* models fail when numbers or names change (e.g., wrong variable substitution, skipped steps, arithmetic errors). Such analysis could distinguish pattern-matching failure from simple calculation errors and would strengthen the paper's interpretation of the observed variance.

5. **Limited analysis of why the NoOp-NoOp condition does not help.** The paper shows that providing 8 shots of different GSM-NoOp questions (where the correct answer ignores the NoOp clause) fails to improve performance, but does not explore *why*. This is a key piece of evidence (models fail to generalize the "ignore irrelevant" pattern across different question structures) that warrants deeper discussion.

6. **The P2 condition adds a discount clause that genuinely adds a reasoning step**, complicating the interpretation that the performance decline is purely about pattern-matching difficulty rather than increased computational steps. (The paper acknowledges this in a footnote at line 192—"adding or removing a clause does not always result in an exact increase or decrease of one in the number of required reasoning steps"—but the caveat could be more prominent and its implications discussed.)

### Trivial

None.

## Nice-to-Haves

- **Error-type breakdown** for failures on GSM-Symbolic and GSM-NoOp (e.g., what fraction of errors come from subtraction vs. addition vs. other operations on NoOp problems) would strengthen the pattern-matching interpretation.
- **A controlled comparison** using GSM-Symbolic with the original GSM8K values (to test distributional shift vs. contamination) would make the contamination discussion more rigorous.
- Reporting how many templates failed automated checks or required manual review would give readers a better sense of coverage and difficulty.
- A brief discussion of why smaller models sometimes perform better on NoOp-Symb (Figure 7c) would be informative.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

1. **"P2 condition adds an extra reasoning step"—already acknowledged by the paper.** The harsh critic claimed the P2 discount clause complicates interpretation, but the paper explicitly states (footnote, line 192): "adding or removing a clause does not always result in an exact increase or decrease of one in the number of required reasoning steps... our main focus is to understand the *evolution* of the performance distribution." This criticism is a strawman; the paper already addresses it.

2. **"Lack of statistical tests"—overstated.** The paper relies on visual inspection of clear, multi-model distributions and reports concrete metrics (e.g., gap between best/worst performance for specific models). The distributions are sufficiently clear to support the claims. Requesting formal p-values for every comparison is not standard for this type of large-scale empirical study and would not change the conclusions.

3. **"No discussion of greedy decoding vs. sampling"—scope creep.** Using greedy decoding is standard for GSM8K evaluations. Testing temperature sampling is a useful extension but not a flaw in the current study.

4. **"Number of shots claim needs quantitative backing"—trivial.** The paper states the number of shots "did not significantly change the performance and conclusions" based on preliminary experiments. While a quantitative result would be nice, the core experiments all use the same setup (8-shot CoT), so this does not affect any reported results.

5. **"Section-by-section: Related Work could more cleanly distinguish GSM-Symbolic from GSM-IC"—subjective presentation preference, not a weakness.** The paper already distinguishes itself (controllable difficulty, multiple instantiations, deeper issue beyond prompting).

6. **"Conclusion's 'human-like cognitive abilities' is too grandiose"—subjective editorial opinion.** The phrase appears once in the conclusion's final sentence and is a standard aspirational framing for the field.

## Novel Insights

The reviews surface one genuinely novel observation not fully explored in the paper itself: the finding that *some weaker models actually improve on NoOp-Symb* (Figure 7c). The harsh critic correctly notes this is "intriguing but not analyzed"—smaller models may be less prone to overthinking, or their lower baseline accuracy makes them less susceptible to being misled by the irrelevant clause because they have learned simpler heuristics. Exploring this asymmetry between strong and weak models could reveal something fundamental about the nature of the pattern-matching failure (is it a feature of *capability* or of *overfitting to training distributions*?). This goes beyond the paper's current contribution but is a worthwhile direction.

## Suggestions

1. Replace or supplement the kiwi example with an *uncontroversially* irrelevant clause to eliminate any ambiguity about whether the NoOp is truly irrelevant.
2. Add a brief discussion of distributional shift as an alternative to contamination when interpreting the right-tail GSM8K performance.
3. Document the template selection criteria (how were the 100 of 1319 chosen?) to establish representativeness.
4. Add an error-type breakdown for GSM-NoOp (e.g., fraction of failures involving subtraction vs. addition vs. multiplication of the NoOp quantity) to directly illustrate the pattern-matching hypothesis.
5. Provide a brief analysis or hypothesis for why some weaker models improve on NoOp-Symb.

## Score and Decision

This paper makes a genuine, well-supported contribution. The experiments are large-scale (25 models, ~500 evaluations), the findings are important for the community, and the conclusions are appropriately hedged. The weaknesses are minor—they concern presentation, depth of analysis, and alternative interpretations for secondary claims—and do not threaten the paper's core contributions. The paper would be strengthened by addressing the template selection documentation and the kiwi example ambiguity, but these do not warrant rejection.

MY FINAL SCORE: <score>8</score>
MY FINAL DECISION: <decision>Accept</decision>