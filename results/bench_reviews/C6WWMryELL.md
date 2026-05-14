Now I have all the information I need. Let me compose the final consolidated review.

---

## Summary

This paper addresses output length volatility in long-form LLM generation through a three-stage pipeline: (1) VOLTBench, a benchmark that introduces length volatility as a core evaluation metric across structured and unstructured tasks; (2) attention trace analysis identifying "Attention Collapse" and "Attention Instability" as internal signatures of volatility; and (3) SELB, a training-free decoding strategy that forces structural adherence and suppresses known failure modes via logit boosting. The method improves mean output length by 148% and reduces length volatility by 69% over baselines.

## Strengths

- **Novel benchmark angle**: VOLTBench is the first benchmark to systematically measure length volatility across multiple runs, covering both unstructured and structured tasks, multiple languages, and instruction complexities. Prior benchmarks assessed single-generation quality; the volatility framing is a genuine and underexplored addition to long-form generation evaluation. The benchmark design, with its chapter-based format scaling to 500 sections and up to 100k words, deliberately stress-tests models at extremes where failure modes surface.

- **Comprehensive evaluation scope**: The paper evaluates 9+ models spanning proprietary, open-source, and fine-tuned variants (LongWriter-8B), plus multiple training-free decoding baselines (Repetition Penalty, Entropy-Based Stopping, Length Constraint, Lookahead Decoding). The multi-dimensional analysis across language, complexity, and output format provides a broad view of the volatility problem.

- **Practical mitigation with clear empirical gains**: SELB delivers substantial improvements in length adherence (MLA 78.25% vs. LongWriter-8B's 31.6%) and stability (LVC 14.02% vs. 45.4%) without requiring additional training. The method is simple and can be applied to multiple base models (Qwen2.5-7B, Qwen3-8B, Llama-3.1-8B), which is demonstrated in Figure 5.

- **Fine-grained constraint framework**: Embedding character-level, keyword, and theme constraints into prompts enables programmatic quality assessment even for unstructured tasks, providing an objective signal beyond LLM-as-judge alone. This design surfaces a clear collapse in constraint following beyond 100 sections.

## Weaknesses

### Fatal

None.

### Major

- **SCA metric lacks sufficient documentation to support quality claims**: The Structured Content Accuracy metric uses "Execution-based Verification" but the main paper provides no detail on what constitutes a "correct" chapter for Python libraries or LaTeX formulas. Is the code executed against test cases, or merely checked for syntactic validity? The paper reports Qwen2.5-7B at 99.8% SCA and SELB at 100%—the base model's near-ceiling score raises concern that the metric may be too permissive to meaningfully differentiate quality. Without specifying the verification protocol, the claim that SELB "maintains high generation quality" on structured tasks cannot be properly evaluated. This undermines a central pillar of the paper's quality argument.

- **Attention analysis is anecdotal and disconnected from the mitigation method**: Section 5 presents attention traces from only two models on a single task (diary, 40 sections) and identifies two patterns qualitatively. No quantitative evidence—such as correlation between trace features and output volatility across many model-task-seed combinations—is provided. More critically, SELB does not use attention signals; it applies hard decoding constraints (forced section breaks, EOS suppression, filler banning). The paper frames itself as a "benchmarking–probing–mitigation" pipeline but the probing stage does not inform the mitigation design. The attention analysis reads as a separate, preliminary observation rather than an integral link in the claimed pipeline. This weakens the paper's narrative coherence and the claimed novelty of the three-stage approach.

### Minor

- **SELB assumes known chapter structure, limiting generality**: The method requires that section titles and the total number of sections be known in advance (Equation 2 uses $P_{total}$ and $V_{title}^{(p+1)}$). This assumption is natural for the chapter-based VOLTBench tasks but does not hold for many real-world long-form generation scenarios. The SELB-Hybrid extension for free-form generation (Section 6.4) is described only in high-level terms in the main paper, with the mechanism deferred to Appendix I. The reported 97% MLA on a 20k-word novel task is presented without evaluation of readability or coherence, making it hard to assess whether the generalized method produces usable output.

- **UCA relies on LLM-as-judge without calibration evidence in the main paper**: The LLM-as-judge evaluation for unstructured content is a standard practice, but the main paper provides no information on the judge model, prompt design, calibration against human judgments, or potential bias toward longer outputs. These details are deferred to Appendix C. Given that UCA is the primary quality signal for unstructured tasks, this omission weakens confidence in the quality-maintenance claim.

### Trivial

- The paper references Figure 2 when discussing attention traces in Section 5 ("As shown in Figure 2, where models are tasked with generating 40 sections"), but the attention traces appear in Figure 4. This appears to be a figure numbering error.

## Nice-to-Haves

- A simple baseline that combines `max_new_tokens` with forced section breaks (without SELB's proactive boosting) would help isolate whether the improvement comes from the structural enforcement or merely from preventing early stopping. This would strengthen the claim that SELB's specific design choices matter beyond "just keep generating."

- Reporting attention trace statistics across multiple seeds for the same prompt would visually demonstrate how trace variation corresponds to output variation, making the probing analysis more convincing without requiring a full quantitative study.

- Side-by-side output excerpts comparing SELB, LongWriter-8B, and a simple baseline at extreme lengths would complement the abstract metrics and help readers judge content quality directly.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh critic's claim that SCA is "structurally incapable of measuring generation quality"**: Removed as overly categorical. The paper does not describe the verification protocol, making the metric's validity uncertain, but the critic's assumption that it only checks syntax is speculative. We frame this as insufficient documentation rather than a structural impossibility.

- **Harsh critic's claim about missing appendix material making the paper not self-contained**: Removed per hard rules—the appendix is stripped by the parser and exists in the original submission. The paper's heavy reliance on appendices is noted in weaknesses only where main-paper claims are unsupported without appendix details.

- **Strength Finder's "this paper is well-written" and similar generic claims**: Removed as too superficial.

- **Harsh critic's section-by-section notes about formatting, FAD being undefined**: The FAD point is about edge cases (zero chapters) that don't substantially affect the evaluation; removed as a nitpick. The claim about chapter break signaling conventions across models is partially valid but minor—removed as it doesn't threaten core claims.

- **Harsh critic's claim that SELB novelty is overstated because it's "trivial"**: Removed as a subjective framing. Simple methods can be valuable contributions. The real concern—that the method is task-specific and assumes known structure—is kept as a minor weakness.

- **Harsh critic's demand for human evaluation**: Moved to nice-to-have. Human evaluation is ideal but not standard practice for decoding-method papers in this space; LLM-as-judge is widely accepted when properly calibrated.

## Novel Insights

The paper's most novel contribution is the concept of length volatility as a first-class evaluation dimension for long-form generation, operationalized through multi-run sampling and metrics like LVC and FAD. This shifts the evaluation paradigm from "can the model hit the target once?" to "can the model hit the target consistently?"—a distinction with practical importance for cost predictability and reliable deployment. The finding that even LongWriter-8B (a model specifically fine-tuned for long-form generation) exhibits an output standard deviation peaking at 103% of its mean length is a striking empirical result that justifies the volatility framing.

## Suggestions

- **Specify the SCA verification protocol in the main paper**: At minimum, state what "correct" means for each structured task (e.g., "a chapter is correct if the generated Python function passes all provided unit tests"). If the verification is sophisticated, this will strengthen the paper's quality claims. If it is merely a syntax check, the paper should be upfront about this limitation and temper its quality conclusions accordingly.

- **Add a quantitative bridge between probing and mitigation**: Even a simple correlation analysis between attention trace features (e.g., peak frequency, decay rate) and output volatility across different model-task pairs would transform the probing from an anecdotal observation into a diagnostic tool. Alternatively, reframe the paper to acknowledge that the probing and mitigation are parallel contributions rather than a causal pipeline, which would be more honest and still valuable.

- **Evaluate SELB at 500-section extremes**: The paper's benchmark goes to 500 sections but SELB results are shown only for 100-section tasks. Demonstrating that SELB does not degrade into repetition at extreme lengths would substantially strengthen the contribution.

## Score and Decision

**Anchor comparisons:**

| Anchor | Avg Score | Comparison |
|--------|-----------|------------|
| LongWriter-Zero (JWx4DI2N8k) | 6.0 (Oral) | Much stronger: RL-based training with SOTA results and rigorous evaluation. This paper's method and evaluation are substantially weaker. |
| ExpertLongBench (nJvgBolRcR) | 5.5 (Poster) | Comparable scope (benchmark + evaluation framework) but ExpertLongBench had expert-validated rubrics. This paper adds a method contribution but with less rigorous quality validation. Slightly weaker overall. |
| Constrained Decoding of Diffusion LLMs (7Sph4KyeYO) | 5.5 (Poster) | Both propose constrained decoding methods. The diffusion paper has more algorithmic novelty; this paper addresses a more practical problem with a simpler solution. Comparable in contribution level but this paper's evaluation is less thorough. |
| LFQA-E (bJYm4v0Spr) | 4.5 (Poster) | Both are evaluation-focused with a benchmark contribution. Comparable quality of contribution, though this paper adds a method. Our paper's metric documentation gaps pull it toward the lower end. |
| MGAL (RdLSJ5CJsr) | 4.0 (Withdrawn) | This paper is clearly stronger: broader task coverage, adds a method, and has a more novel evaluation angle (volatility vs. traditional comprehension). |
| SagaScale (bYpSLBk8H8) | 3.5 (Reject) | This paper is clearly stronger: the benchmark design is more principled and the paper includes both analysis and mitigation, not just a benchmark. |

The paper makes a genuine contribution by introducing length volatility as an evaluation dimension and providing both a benchmark and a working mitigation. However, the quality evaluation is insufficiently documented to fully support the central claim that SELB maintains generation quality while improving length adherence, and the attention analysis is too preliminary and disconnected from the method to carry the weight the paper assigns it. These are addressable weaknesses but currently prevent the paper from reaching the acceptance bar.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>