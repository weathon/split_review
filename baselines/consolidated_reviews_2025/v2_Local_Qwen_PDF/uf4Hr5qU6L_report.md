## Summary
# Final Review Report

## Summary
This paper proposes PRECOT (Problem Representation Enhanced CoT), a two-stage prompting framework that first extracts the initial state (given information) and goal state (objective) from a question to form a structured problem representation, and then uses this representation to prime the Chain-of-Thought (CoT) solution process. Inspired by cognitive psychology theories of human problem-solving, the authors evaluate PRECOT across 15 benchmarks in arithmetic, commonsense, and symbolic reasoning using PaLM 2 and GPT-3. The results show that PRECOT consistently outperforms standard few-shot and zero-shot CoT on most tasks, particularly those requiring context filtering and state tracking. Error analysis reveals that problem representation reduces major semantic-logical errors, shifting failures toward minor computational mistakes. The paper provides a compelling empirical demonstration that explicit state grounding enhances LLM reasoning, though it would benefit from clearer mechanistic hypotheses, stronger baseline comparisons, and explicit discussion of limitations such as extraction dependency and latency.

## Strengths
1. **Clear Cognitive Motivation:** The paper effectively bridges cognitive psychology (problem representation construction) with LLM prompting, providing a theoretically grounded rationale for why structuring initial and goal states might improve reasoning.
2. **Comprehensive Empirical Evaluation:** The evaluation covers 15 diverse benchmarks across arithmetic, commonsense, and symbolic reasoning, using two distinct LLMs (PaLM 2 and GPT-3). This breadth strengthens the generalizability claims.
3. **Insightful Error Analysis:** The manual error categorization (Figure 2) provides valuable qualitative evidence that PRECOT reduces major semantic-logical errors, offering a deeper understanding of *how* the method helps beyond simple accuracy metrics.
4. **Ablation on Extraction Quality:** The PRECOT+ analysis (Section 5.2) is a strong methodological choice that isolates the impact of extraction quality, clearly demonstrating that better state representation directly correlates with improved reasoning performance.
5. **Reproducibility:** The authors provide detailed prompt templates in the appendix and use public API engines with greedy decoding, facilitating straightforward reproduction of the results.

## Weaknesses
1. **Lack of Mechanistic Hypothesis:** The paper does not clearly articulate *why* problem representation improves reasoning. Is it due to context filtering, attention focusing, self-consistency, or simply increased prompt length? Without a hypothesis, the contribution reads as empirical prompt engineering rather than a principled framework.
2. **Weak Baseline Comparisons:** The evaluation only compares against standard few-shot and zero-shot CoT. It omits stronger modern baselines like Self-Consistency, Plan-and-Solve, or Tree of Thoughts, making it difficult to assess whether PRECOT's gains are competitive with state-of-the-art reasoning methods.
3. **Under-specified Method Details:** Section 3.2 is critically brief. It does not specify the exact prompt structure (e.g., whether extracted states are prepended, appended, or interleaved), hindering reproducibility. The reliance on greedy decoding (temperature=0) without variance reporting also limits statistical reliability.
4. **Selection Bias in Error Analysis:** The error analysis samples only problems where *both* CoT and PRECOT fail. This misses the most informative cases (CoT-fail/PRECOT-success) and limits causal claims about error reduction. Inter-annotator agreement metrics are also missing.
5. **Overstated Novelty Claims:** The claim that PRECOT is the "first attempt to integrate problem representation" ignores adjacent methods that implicitly structure problem spaces (e.g., planning, decomposition, self-ask). The novelty is more incremental than presented.
6. **Missing Limitations Discussion:** The conclusion lacks a balanced discussion of limitations, such as the increased latency from two-stage prompting, the dependency on extraction quality (especially in zero-shot), and the method's weakness on knowledge-heavy tasks (e.g., StrategyQA).

## Key Issues
1. **Reproducibility Risk due to Under-specified Prompt Structure:** Section 3.2 lacks the exact prompt template showing how "Given Information" and "Objective" are integrated with the question and answer trigger. Without this, independent reproduction is impossible.
2. **Causal Attribution Gap in Error Analysis:** The error analysis only examines cases where both methods fail, preventing a direct causal link between problem representation and error reduction. The absence of inter-annotator agreement further weakens the reliability of the qualitative claims.
3. **Boundary Condition Oversights:** The narrative glosses over performance drops in zero-shot GSM8K and knowledge-heavy tasks (StrategyQA, CSQA). Failing to explicitly scope the method to context-dependent reasoning reduces the scientific rigor of the contribution claims.
4. **Missing Variance Reporting:** All experiments use greedy decoding (temperature=0) without reporting variance across multiple runs or seeds. This makes it difficult to assess the statistical significance of the reported gains, especially for small margins.

## Actionable Suggestions
1. **Add Explicit Prompt Template:** In Section 3.2, include a concrete prompt template showing the exact placement of "Given Information" and "Objective" relative to the question and answer trigger. This is critical for reproducibility.
2. **Strengthen Baseline Comparisons:** Add comparisons against at least one stronger baseline (e.g., Self-Consistency or Plan-and-Solve) to contextualize PRECOT's gains. If compute is limited, provide a theoretical discussion of how PRECOT complements these methods.
3. **Expand Error Analysis:** Include a "CoT-fail/PRECOT-success" subset in the error analysis to directly demonstrate the benefit. Report inter-annotator agreement (e.g., Cohen's Kappa) for the error categorization.
4. **Scope the Contribution Explicitly:** In the results and conclusion, explicitly contrast context-dependent tasks (where PRECOT excels) with knowledge-dependent tasks (where it struggles). Acknowledge the extraction quality bottleneck and latency trade-offs.
5. **Report Variance:** If possible, report mean±std over multiple seeds or runs, especially for tasks with small performance margins. If greedy decoding is strictly required, acknowledge this as a limitation.
6. **Refine Novelty Claims:** Soften the "first attempt" claim to "one of the first to explicitly separate initial/goal state extraction as a dedicated pre-reasoning stage," and discuss how PRECOT differs from planning/decomposition methods in the Related Work.

## Storyline Options + Writing Outlines
### Abstract Outline (Complete)
- **S1 (Problem & Domain):** Chain-of-Thought (CoT) prompting has advanced LLM reasoning, but models often struggle with distractor-heavy contexts and complex state tracking because they jump directly into solution searching.
- **S2 (Significance/Challenge):** Without initial grounding, reasoning trajectories frequently deviate from the goal or get distracted by irrelevant information, limiting CoT's reliability in multi-step tasks.
- **S3 (Prior Gap):** While recent methods focus on trajectory control (e.g., planning, decomposition), few explicitly structure the problem space before reasoning begins.
- **S4 (Proposed Method):** We propose PRECOT, a two-stage prompting framework that first extracts the initial state (given information) and goal state (objective) to form a structured problem representation, then primes the CoT solution process with this representation.
- **S5 (Key Result & Bounded Implication):** Evaluated across 15 benchmarks, PRECOT consistently outperforms standard CoT, particularly in arithmetic and symbolic tasks requiring context filtering. Error analysis reveals that explicit state grounding significantly reduces major semantic-logical errors, though performance remains tightly coupled with extraction quality.

### Introduction Outline (Complete)
- **P1 (Big Picture & Problem):** Scaling LMs and CoT prompting have improved multi-step reasoning, but CoT remains vulnerable to specific failure modes: sensitivity to irrelevant context, error accumulation, and inability to track complex state transformations.
- **P2 (Gap & Motivation):** Current prompting strategies primarily focus on solution searching (e.g., decomposition, planning) without addressing how the model initially understands the problem. In cognitive psychology, human problem-solving begins with problem representation construction—structurally encoding initial and goal states—which guides subsequent solution searching.
- **P3 (Proposed Solution):** We introduce PRECOT, which explicitly separates problem representation construction from solution searching. By forcing the LLM to extract and structure key states before generating reasoning steps, we hypothesize that PRECOT reduces context noise and aligns reasoning trajectories.
- **P4 (Evidence Preview):** Extensive evaluation across arithmetic, commonsense, and symbolic reasoning shows PRECOT outperforms few-shot and zero-shot CoT on most tasks. Qualitative error analysis demonstrates a significant reduction in major semantic-logical errors.
- **P5 (Contribution Summary):** (1) PRECOT framework with explicit two-stage state extraction. (2) Comprehensive evaluation showing consistent gains, especially in context-dependent tasks. (3) Error analysis and ablation studies revealing that extraction quality is the primary bottleneck, offering insights into representation-aware prompting.

## Priority Revision Plan
| Priority | Action Item | Expected Impact | Effort |
|---|---|---|---|
| **P0** | Add explicit prompt template in Section 3.2 showing exact placement of extracted states. | Resolves reproducibility risk; enables direct implementation. | Low |
| **P0** | Soften novelty claims and discuss adjacent methods (Plan-and-Solve, ToT) in Related Work. | Prevents rejection for overstated novelty; improves scientific rigor. | Low |
| **P1** | Expand error analysis to include CoT-fail/PRECOT-success cases and report inter-annotator agreement. | Strengthens causal claims about error reduction. | Medium |
| **P1** | Explicitly scope contribution to context-dependent tasks; acknowledge limitations (latency, extraction dependency, knowledge-heavy task weakness). | Improves objectivity and sets realistic expectations. | Low |
| **P2** | Add comparison against stronger baselines (e.g., Self-Consistency) or provide theoretical justification for omission. | Contextualizes gains within modern reasoning literature. | High |
| **P2** | Report variance across multiple seeds/runs where feasible. | Increases statistical reliability of small-margin claims. | Medium |

**Revision Order:** Execute P0 items immediately to secure reproducibility and novelty framing. Follow with P1 items to strengthen empirical claims and scoping. Address P2 items if compute/resources allow.

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory
| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|---|---|---|---|---|---|---|
| E1 | PRECOT improves arithmetic reasoning vs CoT | GSM8K, GSM-IC, SVAMP, AQuA; PaLM 2, GPT-3 | Accuracy | Few-shot PRECOT consistently outperforms; zero-shot mixed on GSM8K | Context filtering benefit | Zero-shot extraction quality bottleneck |
| E2 | PRECOT improves commonsense reasoning | StrategyQA, CSQA, SocialIQA, Date, Causal Judg., Ruin Names | Accuracy | Gains on context-dependent tasks; drops on knowledge-heavy tasks | Task-specific scoping needed | Lacks analysis of knowledge-retrieval failure mode |
| E3 | PRECOT improves symbolic reasoning | Colors, Deduction, Tracking, Coin Flips, Last Letters | Accuracy | Large gains on state-tracking tasks (Coin Flips, Colors) | State-tracking benefit | Missing variance reporting |
| E4 | Error severity reduction | Manual analysis of 100 incorrect predictions per model | Error category distribution | Semantic-logical errors reduced; shifted to minor errors | Qualitative mechanism insight | Selection bias (both fail); no inter-annotator agreement |
| E5 | Extraction quality impact (PRECOT+) | Zero-shot reasoning with few-shot extracted states | Accuracy | PRECOT+ outperforms zero-shot PRECOT and CoT on GSM8K | Extraction quality is primary bottleneck | Not a standalone method; relies on manual/few-shot extraction |

### Research-Theme Gap Diagnosis
The core research value (new knowledge about representation-aware prompting) is well-supported for context-dependent tasks. However, reproducibility is hindered by missing prompt templates, and generalizability is limited by the lack of variance reporting and stronger baseline comparisons. The causal link between representation and error reduction is weakened by selection bias in the error analysis.

### Proposed Research Experiments (P0/P1/P2)
| Target Claim | Hypothesis | Minimal Design | Controls/Baselines | Metrics | Success Criterion | Est. Cost/Time | Expected Gain |
|---|---|---|---|---|---|---|---|
| Extraction bottleneck | Automated extraction quality directly correlates with reasoning accuracy | Correlate extraction F1/similarity with final accuracy across 500 samples | Standard CoT | Correlation coefficient (Pearson/Spearman) | r > 0.5 | Low (1 day) | Quantifies dependency; guides future extraction improvements |
| Causal error reduction | PRECOT reduces semantic-logical errors in CoT-fail cases | Analyze 200 cases where CoT fails but PRECOT succeeds | CoT error distribution | Error category shift | Significant reduction in major errors | Medium (2 days) | Strengthens causal claim; removes selection bias |
| Variance reliability | Gains are statistically significant across runs | Run PRECOT and CoT 5 times with different random seeds (if applicable) or temperature variations | CoT variance | Mean±std, paired t-test | p < 0.05 for key tasks | Medium (API cost) | Validates small-margin claims |

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score:** 6/10

**Rationale:** The paper presents a well-motivated and empirically validated prompting framework that demonstrates clear benefits for context-dependent reasoning tasks. The cognitive psychology inspiration and error analysis provide valuable insights. However, the score is moderated by the lack of mechanistic hypothesis, under-specified method details (prompt structure), weak baseline comparisons, and overstated novelty claims. The selection bias in error analysis and missing limitations discussion further reduce confidence in the generalizability claims.

**Post-Revision Target:** [7, 8]/10

**Path to Target:** Achievable if authors (1) add explicit prompt templates for reproducibility, (2) soften novelty claims and discuss adjacent methods, (3) expand error analysis to remove selection bias, and (4) explicitly scope the contribution to context-dependent tasks while acknowledging limitations. These revisions would significantly strengthen the scientific rigor and defensibility of the paper without requiring extensive new experiments.