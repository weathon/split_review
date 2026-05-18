Now I have all the evidence I need. Let me compose the final consolidated review.

## Summary

This paper introduces GSM-Symbolic, a benchmark generated from symbolic templates that creates diverse variants of GSM8K grade-school math questions, enabling controlled, distributional evaluation of LLM mathematical reasoning. Through experiments on 25 state-of-the-art models across ~500 evaluation runs, the paper demonstrates: (1) substantial performance variance across different instantiations of the same question, (2) greater sensitivity to numerical changes than name changes, (3) increasing performance degradation and variance as question clauses increase, and (4) catastrophic performance drops (up to 65%) when seemingly relevant but inconsequential clauses are added (GSM-NoOp), which are not mitigated even by in-context examples of the same question. The paper argues these findings suggest LLMs rely on pattern matching rather than formal logical reasoning.

## Strengths

1. **Large-scale, controlled evaluation across diverse models.** The paper tests 25 open and closed models (2B–27B plus GPT-4o, o1-mini, o1-preview) in ~500 evaluation runs, providing a broad empirical basis for claims about reasoning fragility. This goes well beyond prior work that typically tests fewer models or less controlled variants (§3.2, §4).

2. **GSM-Symbolic enables controllable, multi-instance benchmarking.** By creating symbolic templates that generate diverse question variants (changing names, numbers, clauses), the benchmark supports studying performance distributions rather than single-point accuracy. This directly addresses a limitation of static benchmarks like GSM8K, GSM-Plus, and iGSM (§3.1, Fig. 1).

3. **Reveals unwarranted variance and questions reliability of GSM8K metrics.** For 21 of 25 models, original GSM8K accuracy lies on the right tail of the GSM-Symbolic distribution — an unlikely pattern if models were performing robust formal reasoning. This challenges the reliability of single-point metrics on GSM8K (§4.1, Fig. 2, Fig. 3).

4. **Clean ablation on name vs. number changes.** The paper shows models have higher variance and mean drop when numerical values change compared to name changes, with a gradual leftward shift in means across these conditions. This cleanly isolates where models are most brittle (§4.2, Fig. 4).

5. **Difficulty scaling experiments show consistent evolutionary patterns.** As clauses increase (M1 → M2 → P1 → P2), performance shifts left and variance increases uniformly across all models, with the rate of accuracy drop accelerating faster than the linear increase in reasoning steps (§4.3, Fig. 5).

6. **GSM-NoOp exposes catastrophic failure on irrelevant information.** Adding a single seemingly relevant but inconsequential clause causes performance drops up to 65% across all models, including o1-preview. The finding that this is not remedied even by in-context shots of the same question or NoOp examples is a genuine and important advance over prior work such as GSM-IC (§4.4, Fig. 6).

7. **Among the strongest models (o1-preview), the problem persists.** The catastrophic drop on GSM-NoOp is not limited to smaller models; even the state-of-the-art o1-preview shows a significant decline, underscoring the depth of the problem (§4.4, Fig. 6a).

## Weaknesses

### Fatal
None.

### Major
None. The core empirical contributions — the benchmark, the variance analysis, the difficulty scaling results, and the NoOp findings — are solid and well-supported.

### Minor

1. **The contamination hypothesis lacks direct supporting controls.** The paper notes that original GSM8K accuracy lies on the right tail of the GSM-Symbolic distribution and suggests this "could be" due to data contamination (line 149). However, an equally plausible explanation is that the template generation process produces systematically harder questions: the variable value ranges (5–100 for operands, 100–500 for totals) may yield problems with larger numbers, more carries, or less "round" arithmetic than the human-curated originals. The paper does not control for this by comparing the arithmetic complexity (operand size, number of carries, etc.) of original vs. generated questions. The contamination claim is appropriately hedged in the paper ("hinting at," "could be"), but since this is presented as a contribution (line 69), some readers will expect stronger evidence. The observation remains interesting either way, but the contamination interpretation specifically is under-supported.

2. **The NoOp results would benefit from a human baseline or a stronger control condition.** The paper convincingly shows that models fail on NoOp statements, but the statements are deliberately designed to resemble operationally relevant clauses (e.g., "five of them were a bit smaller than average"). The paper itself notes (line 278) that models may be applying learned heuristics from training data where such phrases signal arithmetic operations. This is consistent with pattern matching, but without a human performance baseline or a comparison to clearly nonsensical clauses (e.g., "the sky was blue that day"), it is difficult to distinguish between "models cannot reason about irrelevance" and "models apply heuristics that are statistically appropriate given their training distribution, and these heuristics are hard to override." A human baseline would also clarify whether the task is genuinely easy for a reasoner or whether even humans might be momentarily misled.

3. **Some interpretive claims go slightly beyond what the experiments directly test.** The abstract states "We hypothesize that this decline is due to the fact that current LLMs are not capable of genuine logical reasoning." The experiments demonstrate brittleness — fragility under distribution shift, sensitivity to irrelevant information — which is consistent with pattern matching. However, brittleness is not a positive test for the *absence* of reasoning; a system that reasons correctly some of the time but is brittle could still be reasoning imperfectly. The paper's conclusion (line 326) appropriately hedges ("It may resemble sophisticated pattern matching more than true logical reasoning"), but some claims earlier in the paper are phrased more definitively. This is primarily a framing issue rather than a flaw in the experiments themselves, and the paper would benefit from consistently using language about "limitations" and "fragility" rather than "absence of reasoning."

4. **Statistical significance testing is absent.** The paper reports variance across 50 datasets of 100 examples each but does not provide confidence intervals or statistical tests for the differences between distributions (e.g., name-change vs. number-change distributions, or differences between difficulty levels). Given the large number of evaluations and the clear visual patterns, this does not threaten the core findings, but significance tests would strengthen the quantitative rigor of the claims.

### Trivial
None.

## Nice-to-Haves

- **Human baseline for GSM-NoOp.** Even a small-scale study (50–100 examples) would substantially strengthen the claim that the NoOp clauses are genuinely irrelevant and that this is not a task that would also mislead humans.
- **Error type analysis on NoOp failures.** Categorizing whether models always incorporate the NoOp clause as an operation, sometimes drop necessary information, or show other error patterns would make the pattern-matching claim more concrete.
- **Nonsensical NoOp control.** Testing whether models still fail on clearly irrelevant clauses (e.g., "the sky was blue") vs. plausibly relevant but actually irrelevant clauses would help distinguish between a general failure to filter irrelevance and a specific pattern-matching failure triggered by misleading cues.
- **Difficulty control for the contamination analysis.** Computing whether original GSM8K questions are systematically easier than the generated variants (by operand size, number of carries, etc.) would either strengthen or reframe the contamination discussion.

## Removed Points

- **"The paper does not clearly delineate how GSM-NoOp differs from GSM-IC."** — The paper explicitly states (line 98): "GSM-IC shows that irrelevant context can impair LLM performance, focusing on prompting techniques. Our work, however, suggests a more fundamental issue: LLMs struggle even when given multiple shots of the same question." This is a clear delineation. Removed as factually inaccurate.
- **"The NoOp interpretation conflates pattern-matching with rational sensitivity to distributional cues."** — The paper itself acknowledges this interpretation (line 278: "potentially because their training datasets included similar examples that required conversion to subtraction operations"). The critic's concern is already addressed in the paper. Removed as a strawman.
- **Criticisms phrased as "the paper does not compare to human performance" presented as evidence that the interpretation is "too strong."** — Downgraded from the critic's framing (which implied this invalidates the NoOp finding) to a Nice-to-Have suggestion. The NoOp findings stand on their own as compelling evidence of brittleness even without a human baseline.

## Novel Insights

The most noteworthy insight from the reviews is that the GSM-NoOp finding — that providing in-context shots of the *same question* with the same irrelevant clause structure fails to help models — represents a genuine advance over GSM-IC's focus on prompting techniques. The harsh critic correctly notes this is under-emphasized in the paper's presentation. The finding that some smaller models (Gemma-2B, Mistral-7B) actually improve on NoOp-Symb compared to their (poor) GSM-Symbolic baseline is another underexplored observation that could reveal something about how model scale interacts with reasoning fragility.

## Suggestions

- Reframe the contamination discussion: either add controls to support the contamination claim, or explicitly note that it is one of several possible explanations (including distribution shift in difficulty) and that the paper's main finding — unwarranted variance — does not depend on this interpretation.
- Add a human performance baseline for a subset of GSM-NoOp examples, or add a nonsensical NoOp control condition, to strengthen the claim that models fail to ignore genuinely irrelevant information.
- Throughout the paper, consistently frame the contribution as characterizing the *fragility* and *limitations* of LLM mathematical reasoning rather than making claims about the "absence" of reasoning, which is a stronger claim than the experiments directly support.
- Add confidence intervals or statistical significance tests for distribution comparisons to improve quantitative rigor.

## Score and Decision
Assigning a score based on the paper's solid empirical contributions and reproducible findings. The benchmark is useful, the scale of evaluation is impressive, and the NoOp results are genuinely important. The interpretive issues are real but do not undermine the core contributions — they are matters of framing that can be addressed in revision. The paper represents good, not exceptional, work: it is thorough and revealing but is more of an empirical characterization than a breakthrough in method or theory.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>