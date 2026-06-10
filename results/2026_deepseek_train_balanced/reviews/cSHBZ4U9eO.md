Here is my consolidated final review.

---

## Summary

This paper provides a theoretical analysis of Divide-and-Conquer (DaC) prompting for LLMs, situating its expressivity relative to IO prompting ($S(IO) \subset \mathsf{TC}^0 \subseteq \mathsf{NC}^1 \subseteq S(DaC)$) and CoT ($S(DaC) \subseteq S(CoT)$). It derives two conditions identifying when DaC is beneficial — (C1) the task is harder than $S(IO)$, (C2) the task contains parallel sub-tasks and suffers from intermediate errors — and validates them on large-integer arithmetic, hallucination detection (HaluEval), and fact verification (SciFact). DaC consistently achieves the highest scores across all settings.

## Strengths

- **First formal complexity-theoretic analysis of DaC prompting's expressivity.** The result $S(IO) \subset \mathsf{TC}^0 \subseteq \mathsf{NC}^1 \subseteq S(DaC)$ provides a principled lower bound on what DaC can achieve that goes beyond prior empirical-only studies (e.g., Cui et al. 2023). This is a genuine advance over the existing literature.
- **Proposition 2 linking DaC's structure to reduced decoding context window size.** The claim that DaC's average decoding context window is strictly smaller than CoT's on parallel sub-tasks provides a concrete mechanistic hypothesis connecting DaC's architecture to reduced intermediate errors, grounded in established work on error propagation (Yang et al. 2023).
- **Two derived conditions are actionable and testable.** The conditions (harder than $S(IO)$, parallel sub-tasks with intermediate errors) provide clear, falsifiable guidance for practitioners deciding when to apply DaC.
- **DaC achieves the highest metrics across all experimental settings** (GPT-3.5 and GPT-4; HaluEval and SciFact), consistently outperforming IO, CoT, CoT-SC, ToT, and Least-to-Most.

## Weaknesses

### Major

- **CoT baselines behave anomalously on GPT-3.5, undermining the empirical comparisons.** On both HaluEval (Table 1) and SciFact (Table 2), standard CoT underperforms simple IO prompting by 15+ F1 points for GPT-3.5 (46.85 vs 61.69; 56.09 vs 72.12). Additionally, CoT-SC underperforms CoT on SciFact GPT-4 (70.09 vs 74.03), contradicting the expected relationship where CoT-SC (multi-sample ensemble) should be at least as good as single CoT. The paper notes the latter anomaly but offers only the vague explanation that "existing works' improvement may not be robust" (line 284). No verification of baseline correctness (example prompts, sample outputs, or qualitative inspection) is provided. Since the paper's empirical claims rest on relative comparisons, this gap shifts the burden onto the authors to demonstrate that the baselines were not simply given poor prompts.

- **Weak mapping from theory to experimental operationalization.** Condition 1 (task harder than $S(IO)$) is never formally shown for the NLP tasks. For fact verification, the paper says "we can reduce a 2-BTI problem to fact verification by describing the two trees with natural language" (line 242) — but provides no actual reduction, no argument for why this reduction preserves hardness, and no formal connection. Condition 2 is operationalized by mechanically splitting documents into sentences, assuming each sentence's veracity is independent — an assumption that is unargued and often false (e.g., cross-sentence claims, anaphora). The experiments classify rather than demonstrate causation.

- **No prompts are shown for any method.** For a paper whose method is entirely about prompting strategy, the exact prompts for decomposition ($d$), tackling ($t$), merging ($m$), and all baselines are central to evaluation and reproducibility. Their absence is a significant gap.

### Minor

- **Proposition 2 is stated without derivation or clearly defined notation.** The inequality $C + \sum_{i=1}^k \frac{(r_i-1)^2}{2\sum_{j=1}^k r_j} < C + \frac{\sum_{i=1}^k r_i - 1}{2}$ is presented without showing how it arises from the decoding process. The quantities $r_i$ (is it tokens? characters? sub-task response length?) and $C$ are imprecisely defined. Without derivation, the proposition functions as a heuristic observation rather than a formal result.

- **No error bars, confidence intervals, or discussion of variance.** All results are single numbers per condition. Given known LLM output variability, the stability and significance of the reported advantages are unknown.

- **No efficiency/cost analysis.** DaC makes multiple LLM calls (one per sub-task plus decomposition and merging), which is substantially more expensive than a single CoT call. The paper does not acknowledge or quantify this tradeoff despite it being critical for practical deployment.

### Trivial

- The proof of Proposition 1 ($S(DaC) \subseteq S(CoT)$) is straightforward to the point that the paper's labeling it alongside the main Theorem may overstate its status; this is a minor presentational issue.
- "appliance scope" (line 88, 153) → "applicability scope."

## Nice-to-Haves

- Providing a full derivation of Proposition 2's inequality would strengthen the theoretical framing.
- Designing an experiment that varies the degree of parallelizability within a single task (e.g., controlling the amount of cross-sentence dependency) would provide stronger causal evidence for Condition 2.
- Showing qualitative example outputs from CoT and DaC to verify that the methods are reasoning as expected.

## Removed Points

These points are flagged to be removed; treat them with caution:

1. **Criticism that the 2-BSI proof is "missing" or that "no construction is given."** The paper says "Here we give a brief flow of the proof" (line 134) and presents a sketch; the full construction appears to reside in a section (referenced as \ref{sec.limit}) that was stripped by the PDF parser. Per policy, weaknesses about missing content from stripped sections are removed. The presentation in the main text is thin but this is a presentation concern, not evidence of absent work.

2. **Criticism about "no ablation of prompt templates, no hyperparameter search details"** — Removed as reproducibility nitpicks per policy (prompt templates for standard methods like CoT are well-established).

3. **Claim that Proposition 1's proof is "vacuously true" and thus meaningless.** The proof is intentionally straightforward and correctly establishes the expressivity ordering; calling it vacuous overstates the issue.

4. **Criticism that the theoretical analysis is "methodologically incomplete" due to sketch-level presentation** — Same rationale as #1; the full proofs may exist in stripped sections.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Fix the baselines.** Provide the exact prompts used, show sample outputs from CoT and IO to demonstrate correctness, and either explain the 15+ point gap on GPT-3.5 or correct the prompts. This is the single highest-impact improvement.
2. **Release all prompts in full** for DaC (all three stages) and all baselines, alongside the paper or in a supplementary.
3. **Report variance** (multiple trials or bootstrapped confidence intervals) or justify single-run evaluation.
4. **Formalize the theory-to-experiment connection** or reframe the experiments as illustrating the conditions rather than "validating" them.
5. **Include a cost comparison** (total tokens processed, API calls per example) across methods.

## Score and Decision

The paper tackles a legitimate and well-motivated question, and its theoretical framing of DaC's expressivity is novel. However, in its current form, the empirical evidence is undermined by unexplained anomalous baseline behavior, the connection between theory and experiments is asserted without argument, and crucial methodological details are missing. The paper needs substantial revisions to meet ICLR standards.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>