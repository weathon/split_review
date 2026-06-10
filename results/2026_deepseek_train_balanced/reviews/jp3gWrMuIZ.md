## Summary

MINT introduces a benchmark and evaluation framework for measuring LLMs' multi-turn interaction capabilities with tool use (Python code execution) and natural language feedback (simulated by GPT-4). From an initial pool of 29,307 instances across 8 reasoning, coding, and decision-making datasets, the authors curate 586 challenging instances that genuinely require multi-turn interaction. The paper presents an extensive empirical study of 20 open- and closed-source LLMs, with human validation of the GPT-4 feedback simulation, and diagnostic findings about training-data artifacts (ShareGPT underscore escaping, CodeLLaMA `[PYTHON]` overfitting).

## Strengths

- **Principled dataset curation ensuring multi-turn necessity**: Rather than naively repurposing single-turn datasets, MINT applies a three-step filtering pipeline—running GPT-3.5 to remove instances solvable within two turns, then stratified sub-sampling—yielding only instances that genuinely require multi-turn interaction. This is a concrete methodological improvement over prior work that draws random subsets without verifying multi-turn necessity.

- **Human-validated GPT-4 feedback simulation**: The paper provides head-to-head human evaluation evidence showing 91.2% of GPT-4 feedback is rated as helpful as or better than human-written feedback, and GPT-4 vs. human feedback yields nearly identical downstream task performance (32.7% vs. 33.6% SR). This directly supports the claim that GPT-4 simulated feedback is a valid, reproducible proxy for human feedback.

- **Diagnostic detection of training-data artifacts**: The benchmark reveals that Vicuna models emit escaped underscores (`\_`) due to ShareGPT artifacts present in 15% of training examples, and that CodeLLaMA-Instruct overfits to the `[PYTHON]` token on 100% of code tasks. These concrete, reproducible findings demonstrate the benchmark's diagnostic value beyond performance ranking.

- **Demonstration that feedback-providing ability is orthogonal to task-solving ability**: The paper shows (Table 3) that CodeLLaMA-34B-Instruct, despite being the worst task-solver, provides feedback improving GPT-3.5, while GPT-3.5-16k (a strong task-solver) degrades GPT-3.5's performance by -10.4%. This is a clear, quantified finding with implications for multi-agent system design.

## Weaknesses

### Fatal

None.

### Major

- **The headline claim that SIFT/RLHF "generally hurt multi-turn capabilities" rests on a confounded comparison and is inconsistently caveated.** The paper compares *base* models (pre-trained, raw-continuation generators) against their *instruct*/*chat* counterparts (trained to follow conversational directives) on a protocol that explicitly requires following complex formatting instructions (`<execute>` tags, proposing solutions, respecting turn limits). The paper standardizes prompts across variants (lines 76–77), but this is a partial control: base models with in-context examples are executing a fundamentally different task (few-shot pattern matching) than instruction-tuned models that have been trained to parse and follow user directives. The finding that base models outperform instruction-tuned counterparts on *this specific protocol* may reflect that prompt-based adaptation works better for base models than SIFT/RLHF works for instruction-tuned models on this benchmark—not that SIFT/RLHF "generally hurt multi-turn capabilities." The paper's own exceptions (Vicuna-7B, Lemur-70b-chat), both fine-tuned on multi-turn ShareGPT data, actually support this alternative explanation: the key variable may be fine-tuning *data composition*, not the SIFT/RLHF technique itself. While the paper hedges in its discussion (line 184: "it's hard to conclude that RLHF in general hurts model performance"), the **abstract** (line 13) and **introduction bullet** (line 41) present the claim without sufficient caveat, creating a misleading headline that exceeds what the evidence supports.

- **No confidence intervals, error bars, or any statistical significance reporting on any result.** With 586 instances across 8 datasets and 20 LLMs, per-dataset comparisons are based on very few examples. The paper reports success rates as point estimates without measures of variance. Fine-grained comparative claims (e.g., "Claude-instant-1 surpasses Claude-2 as k increases to 3," line 166; "open-source models fall behind best commercial closed-source models," line 165) cannot be assessed for reliability. While compactness is a design goal, the paper does not demonstrate that the resulting measurements are statistically stable enough to support the specific rank-order and magnitude claims it makes.

### Minor

- **The filtering step (running gpt-3.5-turbo and excluding instances solved within 2 turns) calibrates benchmark difficulty to a single model.** This means the benchmark's composition is implicitly dependent on gpt-3.5-turbo's capabilities and blind spots. A different filtering model might yield a substantially different set of "challenging" instances. No sensitivity analysis is provided to assess this dependence.

- **The "ability to leverage natural language feedback" is actually the ability to leverage *GPT-4-generated* feedback.** GPT-4 is an exceptionally capable feedback provider. A model's performance with weaker, noisier, or more unpredictable human feedback might look very different. While the human validation shows GPT-4 feedback is a reasonable proxy, the paper's framing (title, abstract, Sec. 3.3) presents the measured quantity as "ability to leverage natural language feedback" in general, which is narrower than claimed. Greater transparency about this scope limitation in the presentation of results would strengthen the paper.

### Trivial

None.

## Nice-to-Haves

- Reporting bootstrap confidence intervals or conducting significance tests on key comparisons (e.g., whether the Claude-instant-1 vs. Claude-2 crossover is reliable) would directly address the largest threat to the benchmark's credibility.
- A sensitivity analysis showing how results change if the GPT-3.5 filtering step were applied with a different model (e.g., GPT-4) would help assess the benchmark's robustness to the curation protocol.

## Removed Points

These points are flagged to be removed; treat them with caution.

- *Harsh critic: "Human evaluation sample size not reported in main paper."* — The paper references `\sref{sec:human-evaluation-details}` in the appendix, which the parser strips. Per hard rules, remove.
- *Harsh critic: "Feedback template and prompt not included in main paper."* — Same as above; referenced to appendix, stripped by parser. Remove.
- *Strength Finder: "Explicit cost accounting enabling accessible reproduction."* — This is a useful reporting detail but not a research strength of the paper's scientific contribution. The ~$100/LLM cost figure and token breakdown are factual information, not evidence of a novel finding or methodological advance. Demoted to factual reporting.
- *Harsh critic comments about the "lazy user" setting's binary feedback being a baseline.* — This is an observation about design, not a weakness. The paper frames it clearly as a minimal baseline, which is appropriate.
- *Harsh critic: "The paper's own exceptions (Vicuna, Lemur) actually support alternative explanation."* — This is used as reasoning within the Major weakness above, not a standalone weakness.

## Novel Insights

The most interesting observation to emerge from the reviews is the tension between the paper's strongest asset (a carefully validated, reproducible multi-turn evaluation framework) and its most marketable finding (SIFT/RLHF hurts multi-turn performance). The diagnostic artifact findings (ShareGPT underscore, CodeLLaMA `[PYTHON]`) are arguably more novel and better-supported than the SIFT/RLHF headline, and the paper would be stronger if it promoted these diagnostic capabilities as a primary contribution rather than the confounded SIFT/RLHF claim. The orthogonal feedback-providing/task-solving finding (Section 3.4) is also underplayed relative to the attention given to the SIFT/RLHF point.

## Suggestions

1. **Reframe the SIFT/RLHF finding to match the evidence.** Replace the abstract's "generally hurt multi-turn capabilities" with something like: "Among most model families tested, base versions outperformed instruction-tuned counterparts on this benchmark, with the notable exception of models fine-tuned on multi-turn conversation data." This version is fully supported and arguably more interesting.

2. **Add bootstrapped confidence intervals** to the main results (Tables 1 and 2). With 586 instances, this is computationally cheap and would substantially increase confidence in the reported rankings and comparisons.

3. **Report per-dataset breakdowns** alongside aggregate results to reveal where multi-turn capabilities differ across models (e.g., are some models strong at reasoning with tools but weak at code generation with feedback?).

4. **Acknowledge the GPT-3.5 filter dependence** as a limitation and, if feasible, include a robustness check with a different filtering model.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>