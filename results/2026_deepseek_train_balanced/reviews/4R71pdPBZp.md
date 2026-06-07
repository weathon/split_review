## Summary

This paper proposes EvoMAC, a self-evolving multi-agent collaboration framework for software development that iteratively refines code generation using compiler feedback ("textual backpropagation"), and rSDE-Bench, a benchmark of 53 software-level coding tasks (616 test cases) with automated requirement-oriented evaluation. The core idea—using objective compiler feedback to iteratively improve multi-agent code generation workflows—is sensible, and the ablation study provides credible evidence that each design component contributes positively.

## Strengths

- **Ablation study cleanly isolates the value of each component.** The seven variants (a–g) systematically test multi- vs. single-agent coding/testing teams, with/without evolving, and with/without environment feedback. Removing the compiler's objective feedback (variant f → g) causes a 12–22 percentage point drop across settings, while reducing multi-agent to single-agent setups also yields measurable degradation. This is the paper's strongest evidence and convincingly supports the internal design choices.

- **The self-evolving mechanism demonstrably improves with iteration.** Figures showing accuracy across evolving iterations (Fig. 2, referenced as Fig.~\ref{fig:evolving}) reveal monotonic improvement across all five dataset settings and two underlying LLMs (GPT-4o-Mini and Claude-3.5-Sonnet), showing the mechanism genuinely drives progress rather than providing a one-time boost.

- **Performance advantage holds across task token lengths.** A comparison across the distribution of context lengths (Fig.~\ref{fig:acc_dist}) shows EvoMAC outperforms ChatDev and GPT-4o-Mini uniformly, not just on tasks of a particular complexity.

- **Automatic evaluation correlates well with human judgment.** The reported 0.9922 correlation between rSDE-Bench's accuracy metric and human expert evaluation (over 4 methods × 4 settings = 16 points) substantially exceeds existing metrics (consistency 0.2583, quality 0.3041), supporting the benchmark's validity.

## Weaknesses

### Fatal

None.

### Major

- **A core section ("Theoratical Analysis," Sec. 5) is an unfinished placeholder.** The section header is misspelled, the body contains only the text "To do:" (line 196), and two equations are dropped in with no derivation, narrative, or connection to the rest of the paper. No theorem, proof, or analysis is provided. A paper submitted to a top venue should not contain stub sections; this signals incompleteness. Removing this section would not harm the paper, but its presence as-is is unacceptable.

- **The SOTA comparison conflates iterative refinement with EvoMAC's specific architecture.** The main results (Table 1) compare EvoMAC—which iteratively generates code, receives compiler feedback, and updates its agents—against baselines that generate code once with no opportunity for refinement. The resulting 26.48%/34.78%/6.10% improvements cannot be attributed to EvoMAC's multi-agent or textual-backpropagation design; they include the trivial advantage of "test, find errors, fix, and repeat." The paper does not acknowledge this asymmetry, does not report the number of iterations or LLM calls used, and presents the improvements as evidence of "superior coding capabilities" (line 9). The HumanEval results (94.51% vs. 88.41%) are especially problematic: HumanEval's test cases are used for evaluation, so EvoMAC effectively gets to see test results and fix its code while the single-agent baseline does not. A fair comparison would need to either give baselines the same iterative test-and-fix loop or control for cost/iteration count.

- **The "textual backpropagation" mechanism is underspecified.** The method's core behavior is defined by the prompts used for the gradient analysis and network update agents, but these prompts are not disclosed. References to key implementation details are left dangling ("The detailed implementation of agents can refer to Sec." and "The overall algorithm can refer to Alg." with no completed references in the provided manuscript). The "self-organizing" initialization of the coding/testing teams—presented as a core contribution—is described in only 1–2 sentences (lines 141–142, 145) with no detail on how the organizer agent decomposes requirements or determines agent count. Since the entire behavior reduces to LLM calls governed by prompts, the missing details make the experiments effectively irreproducible without reverse engineering.

### Minor

- **The "first benchmark" claim is overstated.** The paper repeatedly claims rSDE-Bench is "the first benchmark that features both complex and diverse software requirements, as well as the automatic evaluation of requirement correctness" (lines 34, 46, 75). However, SWE-bench (cited by the paper) already provides real-world GitHub issues with automated test-based evaluation. While the paper dismisses SWE-bench as "bug-fixing," many SWE-bench tasks involve feature additions and multi-file modifications. The paper should qualify this claim and explain more precisely what distinguishes rSDE-Bench.

- **The correlation of 0.9922 between automatic and human evaluation is computed over only 16 data points** (4 methods × 4 settings), with no confidence intervals or scatter plot reported. A single outlier could dominate this correlation. Moreover, since the test cases are designed to operationalize the requirements, a high correlation is expected—this is more of a sanity check than strong validation.

- **The assumption that generating unit tests is "significantly simpler" than generating the code itself** (line 104) is stated without empirical support. The paper does not measure whether the testing team produces correct test cases, especially when the coding team's output is wrong. If the testing team generates flawed test cases, the whole feedback loop is compromised.

- **No cost or iteration data is reported.** The reader cannot assess how many LLM calls EvoMAC uses per task, whether the gains are cost-effective, or what the marginal benefit per iteration is. This is important for judging the practical value of the method.

### Trivial

- Section header "Theoratical Analysis" contains a typo.
- Several section references are incomplete ("refer to Sec." without a specified section number).

## Nice-to-Haves

- A limitations section acknowledging failure modes, task types where EvoMAC struggles, and computational cost would strengthen the paper.
- Validating the "generating tests is easier than generating code" assumption by reporting the testing team's success rate.
- Adding confidence intervals to the correlation analysis and reporting statistical significance for the main results.

## Removed Points

These points were flagged by the reviewers but are removed with justification:

- **"The paper does not adequately explain how rSDE-Bench is sufficiently distinct from SRDD/SoftwareDev"** — Softened/reframed in the "first benchmark" minor weakness above; the paper does distinguish on the basis of automated test-case evaluation vs. human evaluation or similarity metrics. The "first" claim is overstated but the benchmark has differentiating features.
- **"The paper's strongest evidence is buried"** — This is more about presentation than a weakness of the work itself; the ablation study is prominently presented in the paper.
- **"Criticism that existing benchmarks 'often depend on expensive human evaluations' is partially inaccurate"** — The critic's point that SoftwareDev uses human evaluation is true, but the paper's statement is about "software generation benchmarks often depend on expensive human evaluations or indirect similarity-based measurements," which is accurate for SRDD (similarity-based) and SoftwareDev (human evaluation). The paper is not incorrect.
- **Generic formatting/style nitpicks** — Removed per instructions.
- **"The paper does not provide prompt templates"** — Moved to major weakness (underspecified mechanism) rather than listed separately.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Remove or substantively complete the "Theoretical Analysis" section. If it cannot be filled with a real result, delete it.
2. Acknowledge the iterative-refinement asymmetry in the SOTA comparison explicitly. Re-frame the HumanEval results to note that EvoMAC benefits from iterative compiler feedback during generation, unlike one-shot baselines.
3. Disclose the prompts used for the gradient agent, updating agent, and organizer agent in the main paper or an appendix.
4. Report the number of evolution iterations used for Table 1, plus cost/LLM-call counts, so readers can assess efficiency.
5. Soften the "first benchmark" claim with appropriate qualifications.
6. Validate the "tests are easier than code" assumption by reporting the testing team's test-case quality.

## Score and Decision

The paper has a genuine idea—iteratively refining multi-agent code generation with objective compiler feedback—and the ablation study provides real evidence for its internal design choices. However, the submission has significant problems: the SOTA comparison conflates iterative refinement with architectural novelty, the headline claims are over-interpreted, key implementation details (prompts, iteration counts, the entire "self-organizing" initialization) are underspecified, and—most critically—a section of the paper is an unfinished placeholder ("To do:"). For a top conference, the paper in its current form does not meet the bar. The core empirical contribution (the ablation) is solid but not surprising, and it is overshadowed by unsupported claims and incomplete sections.

**Score: 3.5** — reject. The paper addresses an interesting problem and has some credible internal evidence, but the experimental framing is misleading, key methodological details are missing, and the presence of an unfinished section makes the submission inappropriate for acceptance.

MY FINAL SCORE: <score>3.5</score>
MY FINAL DECISION: <decision>Reject</decision>