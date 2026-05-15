Now I have all the information I need. Let me construct the final review.

## Summary

The paper proposes using executable code as a testbed to study semantic diversity of LLM generations, introducing an open-ended program synthesis dataset where semantic diversity is measured by comparing program execution outputs on test cases. The authors evaluate diversity across base models and their instruction-tuned counterparts, finding that while instruction tuning (especially preference tuning) reduces lexical and syntactic diversity, it can increase semantic diversity. They also demonstrate that existing neural diversity metrics (CodeBERTScore, ICE-Score) correlate poorly with their execution-based semantic diversity.

## Strengths

- **Novel methodology for automated semantic diversity measurement.** The idea of leveraging executable code to define semantics through program outputs (Section 3, Section 4) is sound and enables cheap, objective, and scalable evaluation of diversity across hundreds of thousands of generations, overcoming the limitations of human evaluation and unreliable neural proxies.

- **Sample-size invariance correction.** The paper identifies that naïve diversity metrics are confounded by sample size (Figure 3) and adopts a pairwise averaging approach (Equation 2) that ensures fair comparisons even when models produce different numbers of coherent programs. This is a correct and important methodological refinement often overlooked in prior work.

- **Demonstration that neural diversity metrics fail to reflect execution semantics.** The correlation analysis (Figure 4) shows that CodeBERTScore and ICE-Score are negatively correlated with execution-based semantic diversity, and the paper provides concrete failure examples (Figure 5) where neural metrics assign high similarity to semantically distinct programs. This is a useful cautionary finding for the community.

- **Broad empirical scope.** The study covers multiple model families (LLaMA-3, LLaMA3.1, CodeLLaMA, Qwen-Coder-2.5, OpenAI, Anthropic), different tuning methods (SFT, PPO, DPO, rejection sampling), model sizes, and prompting strategies.

## Weaknesses

### Fatal
None.

### Major

- **The central claim that instruction tuning increases semantic diversity is confounded by coherence and not properly disentangled.** The paper's semantic diversity metric records all error-producing programs that fail identically (e.g., failing to define the function) as semantically identical (Section 4, line 83: "if the generated programs fail to implement the function f(...) entirely, this metric penalizes diversity, as such generations are all incorrect in the same way"). Since base models have much lower coherence rates (e.g., CodeLLaMA-7B base coherence = 0.36 vs. instruct = 0.92 in Table 2), their incoherent outputs overwhelmingly produce identical error signals, mechanically depressing their semantic diversity score. The paper acknowledges it can analyze semantic diversity among well-formed programs only (footnote, line 83) and claims that "semantic diversity is not lost when accounting for coherence" (line 163), but **never reports the conditioned analysis in any table or figure**. The reported semantic diversity scores (Tables 1, 2) are computed over all samples, including incoherent ones. Without the conditioned breakdown, the observed increase in semantic diversity could be entirely an artifact of increased coherence rates rather than greater diversity of solutions. This is the most important unresolved issue in the paper.

- **The paper conflates "instruction tuning" broadly with "preference tuning" in its framing, despite evidence supporting only the latter.** The title and abstract use "instruction tuning" generically (Abstract: "instruction-tuning reduces syntactic and lexical diversity" and "increases semantic diversity"). However, the paper's own results (Section 5.3, line 132) show that for SFT-only models (CodeLLaMA-SFT, Magicoder SFT variants of CodeLLaMA, LLaMA-3, LLaMA3.1), the decreases in lexical and syntactic diversity are not statistically significant, and the semantic diversity increases have only moderate effect sizes. The significant results are driven by preference-tuned models (PPO, DPO, rejection sampling). While the paper notes this distinction in Section 5.3, the title, abstract, and introduction present the finding as a general property of instruction tuning. This overclaim misrepresents the actual scope of the evidence.

- **The correlation analysis (Figure 4) aggregates across all models and problems, making it an between-model comparison rather than a within-model finding.** The reported negative correlations between lexical/syntactic and semantic diversity are likely driven by the fact that instruction-tuned models (which have high semantic diversity and low lexical diversity) are pooled with base models (which have the opposite pattern). The paper partially acknowledges this (Section 5.2, line 118: "these kinds of phenomena may contribute to the negative correlations") but does not provide within-model correlations to validate whether the relationship holds when controlling for model identity. The correlation analysis as presented does not support the claim that lexical/syntactic diversity and semantic diversity are generally inversely related within a fixed model.

### Minor

- **The dataset of 21 problems is relatively small for generalizing to "open-ended program synthesis."** While the paper generates 2,100 programs per model × prompt configuration, the diversity metric is computed per-problem and averaged across only 21 paired observations for statistical tests. The Wilcoxon signed-rank test with N=21 has limited power for moderate effect sizes. The paper does not justify why 21 problems are sufficient or how they were selected from the larger CODENET pool. This doesn't invalidate the results but weakens their generalizability.

- **The Discussion (line 163) claims "semantic diversity is not lost when accounting for coherence" but provides no supporting evidence or figure for this claim.** This appears to be a statement based on an unreported analysis. If the authors have this data, it should be presented.

- **The correlation analysis between diversity metrics (Figure 4) would benefit from per-model breakdowns** to assess whether the observed negative correlations are primarily between-model artifacts.

### Trivial
None.

## Nice-to-Haves

- Reporting semantic diversity conditioned on coherent programs only (and ideally on correct programs only) would directly address the main confound and is the most important addition.
- Per-model correlation plots between lexical/syntactic and semantic diversity would complement the pooled analysis.
- Histograms of output values or error types for a few example problems would make the "increase in semantic diversity" concrete and allow readers to assess whether the increase reflects diverse correct solutions or diverse failure modes.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"The invariance proof is in the missing appendix, so we cannot verify"**: The appendix was stripped by the PDF parser, not removed by the authors. Per standard policy, appendix content cannot be cited as missing.
- **"The observation about preference-tuning imparting a 'voice' is unsupported speculation"**: This is explicitly labeled as speculation in Section 6 ("We speculate that..."), which is appropriate for a discussion section. Speculation does not need to be empirically supported.
- **"Using price as a proxy for model size for commercial models introduces uncertainty"**: The paper explicitly acknowledges this limitation (Section 5.4: "model size is not transparent, so we use price per generated token as a proxy") and draws only weak conclusions from the commercial model analysis.

## Novel Insights

The most interesting observation emerging across the reviews is that the paper's negative result—that neural diversity metrics (CodeBERTScore, ICE-Score) fail to capture execution semantics—is actually its most robust and least confounded contribution, while its positive claim (that instruction tuning increases semantic diversity) is the most vulnerable. This inverts the paper's own emphasis: the cautionary methodological contribution is better supported than the headline empirical finding. The paper's methodology for measuring semantic diversity through code execution is genuinely novel and useful, but the empirical findings about instruction tuning require more careful analysis before they can be accepted.

## Suggestions

1. **Report semantic diversity conditioned on coherent programs only.** Compute AvgDiv over only the subset of programs that satisfy the coherence criteria (function definition, no syntax/runtime errors, print output). If the significant increase in semantic diversity for instruction-tuned vs. base models persists, the core claim stands. If it shrinks or disappears, the claim must be revised accordingly. This single analysis determines whether the paper's main finding is valid.

2. **Revise the title and abstract to scope claims to preference-tuned models where the evidence lies**, or present a more nuanced claim differentiating SFT from preference tuning.

3. **Report within-model correlations** between lexical/syntactic and semantic diversity to disentangle model-level effects from genuine tradeoffs.

## Score and Decision

The paper proposes a genuinely novel methodology for studying semantic diversity through code execution and provides a useful caution about neural diversity metrics. However, its central empirical claim—that instruction tuning increases semantic diversity—is undermined by a confound between coherence and diversity that the authors acknowledge but do not resolve in their reported results. The paper overclaims by framing "instruction tuning" broadly when the evidence is primarily about preference tuning. These issues are addressable, but in its current form the headline finding is not adequately supported.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>