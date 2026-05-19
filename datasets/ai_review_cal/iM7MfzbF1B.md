- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 6, 3, 5
Now I have a thorough understanding of the paper. Let me produce the consolidated review.

---

## Summary

This paper proposes MAGE, a system that combines a domain-specific language (DSL) for Legion parallel programming mappers with an LLM-based iterative optimization loop. The DSL abstracts away low-level C++ mapping APIs, enabling LLMs to generate syntactically valid mapper code (80% success rate vs. 0% for raw C++). An LLM optimizer, guided by performance feedback via the Trace framework, iteratively refines mappers across a structured search space. Experiments show LLM-generated mappers matching or exceeding expert-written ones (up to 34% speedup), reducing development time from days to minutes.

## Strengths

- **The DSL demonstrably makes LLM-based mapper generation tractable.** Table 1 shows 8/10 DSL mappers successfully generated vs. 0/10 for C++ (even with up to 10 iterations of compiler feedback). The tenfold reduction in code lines (400+ C++ lines → ~30 DSL lines) is concrete and well-illustrated in Figure 3.

- **LLM-optimized mappers match or exceed expert-written mappers across multiple benchmarks.** The best mappers found by Trace-OptoPrime achieve up to 34% speedup on scientific applications (Circuit) and up to 31% on matrix multiplication algorithms (Section 5.2, 5.3). The paper identifies specific mapping decisions responsible for the gains (e.g., memory placement for Circuit, index mapping for matrix multiply).

- **Ablation study validates the feedback design.** Figure 7 shows that full feedback (system + explanation + suggestions) consistently outperforms system-only feedback and simpler baselines across all three tested benchmarks, justifying the design choices for the optimization loop.

- **Practical impact is demonstrated with concrete time savings.** The search completes within 10 minutes per application, compared to "several days" for manual mapper development (Section 5.2).

## Weaknesses

### Fatal
None.

### Major

- **Performance results lack statistical rigor.** The headline speedups (up to 34%, up to 31%) are reported as "best mapper found across 5 runs," which is an optimistic estimate. The shaded regions in Figures 5 and 6 are undefined in captions or text (standard deviation? min-max? standard error?). The paper itself acknowledges high variance for PUMMA and Solomonik's (Section 5.3: "the throughput of the best mapper... is significantly higher than the average optimization trajectory"), yet no error-bounded estimates, confidence intervals, or per-run distributions are provided. Without this, the reader cannot assess whether the 34% speedup is a reproducible outcome or a rare outlier.

- **The OpenTuner baseline is insufficiently described and likely unfair.** OpenTuner appears only in figure captions (Figures 5, 6) with no description of its configuration, search algorithm, parameter space, or budget. Giving it only 10 iterations — the same budget as the LLM methods — is inappropriate for a traditional autotuner, which would need orders of magnitude more evaluations to explore a high-dimensional space. This comparison adds little evidentiary value and should either be properly configured with a fair budget or removed.

### Minor

- **The C++ vs. DSL code generation comparison lacks a quantitative breakdown.** Table 1 reports binary success/failure per strategy, but the paper does not provide per-attempt statistics: of the 100 C++ attempts (10 strategies × 10 iterations), how many compiled but failed tests vs. never compiled? A detailed breakdown would strengthen the central claim that the DSL is necessary, beyond the qualitative failure analysis in Section 5.1.

- **DSL limitations and coverage are not discussed.** The paper does not address what mapping decisions *cannot* be expressed in the DSL (e.g., adaptive or runtime-dependent policies), limiting the reader's ability to assess the approach's generality. The DSL is described as distilling "key performance-critical aspects" (Section 4.1), but the scope of what is excluded is unspecified.

- **The optimization mechanism of Trace is underspecified.** Section 4.2 describes the feedback loop at a high level, but the "reinforcement learning" framing is not operationalized — how exactly does the LLM use the best previous solution and performance feedback to generate a new candidate? Whether the approach maintains a memory, uses the best-so-far as a starting point, or samples from a distribution of past solutions is unclear from the main text.

- **The ablation study (Section 5.4) covers only 3 of the 9 benchmarks** without a clear justification for the subset. While the results are informative, they would be stronger if extended to all benchmarks or if the selection criteria were explained.

- **No analysis of optimization cost.** The paper states search completes within 10 minutes, but does not report the number of LLM calls, token usage, or cost. This information is important for practitioners evaluating whether the approach is practical for their use case.

- **The number of invalid DSL mappers generated during optimization is not reported.** The ablation suggests that feedback quality affects mapper validity, but error rates are not quantified. Reporting how many iterations produced invalid mappers vs. runnable-but-suboptimal ones would strengthen the feedback analysis.

### Trivial

- The "0-Shot" and "5-Shot" baselines in Figure 7 are defined only in the figure caption, not in the main text. A brief clarification in Section 5.4 would improve readability.

## Nice-to-Haves

- Provide a detailed per-attempt quantitative breakdown of C++ generation failures (compilation vs. test failures) and release prompts/test cases as supplementary material.
- Discuss the potential for adapting the DSL concept to other parallel frameworks (StarPU, Chapel, Ray) beyond Legion.
- Include a comparison with a properly-budgeted non-LLM autotuner (e.g., Bayesian optimization with 100+ evaluations or equivalent wall-clock time) to anchor the LLM approach against traditional methods.
- Clarify what specific mechanism Trace uses to incorporate past solutions into the next iteration's prompt (best-so-far vs. history vs. distribution).

## Removed Points

- **Criticism that the C++ vs. DSL comparison is "unfair" due to inherent DSL simplicity:** The paper's claim is precisely that the DSL's abstraction makes the task tractable. Comparing C++ (at its natural complexity) against the DSL (at its natural simplicity) is the correct comparison to evaluate whether the DSL solves the stated problem. The asymmetry is by design, not a flaw. The specific request for a quantitative failure breakdown is retained in Minor weaknesses as a valid improvement.

- **Suggestion to discuss how the DSL compares to existing DSLs (Halide, TVM):** This calls for adding related-work comparisons that are not required for the paper's contribution evaluation. Per policy, missing related-work discussions are not included.

- **Criticism that the "reinforcement learning" framing is overclaimed:** The paper explicitly references Trace (Cheng et al., 2024) as an RL-inspired framework and describes the iterative refinement process. The framing is standard for this line of work and not an overclaim.

- **Speculation about whether a better C++ prompting strategy could achieve non-zero success:** This is hypothetical and does not constitute a weakness in the paper as presented. The paper provides a clear failure analysis for its specific experimental protocol, which is reproducible.

- **General scope-creep suggestions** (requesting larger datasets, more models, theoretical proofs) that are not standard expectations for an empirical systems paper.

## Novel Insights

None beyond the paper's own contributions. Neither review introduces a perspective not already present in the paper itself.

## Suggestions

1. **Add error bars to all performance figures.** Report the mean and standard deviation (or 95% CI) of the best-found mapper across the 5 runs, and clearly define what the shaded regions in Figures 5 and 6 represent. This alone would substantially increase the credibility of the headline results.

2. **Either properly describe and configure OpenTuner with a fair budget, or remove it.** A 10-iteration OpenTuner baseline is not informative. Either give it a meaningful number of evaluations (100–1000) and describe its configuration, or remove it to avoid misleading comparisons.

3. **Provide a quantitative breakdown of C++ generation failures:** For each of the 10 strategies × up to 10 iterations, report how many attempts compiled, how many passed tests, and what the specific failure modes were. This would turn a qualitative argument into a reproducible finding.

4. **Discuss the DSL's coverage and limitations explicitly.** Even a short paragraph listing what mapping decisions are *not* expressible would help readers assess the approach's practical scope and generalizability.

5. **Report optimization cost** (number of LLM calls, tokens consumed, approximate API cost) alongside wall-clock time to help practitioners evaluate trade-offs.
