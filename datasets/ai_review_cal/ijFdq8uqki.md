- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 6, 5, 3
Now I have all the information needed. Let me produce the consolidated review.

## Summary

This paper presents **BeHonest**, a benchmark for evaluating honesty in large language models across three dimensions — self-knowledge, non-deceptiveness, and consistency — spanning 10 scenarios and 9 models (GPT-4o, ChatGPT, Llama2/3, Mistral, Qwen). Its key findings are that LLMs rarely refuse unanswerable questions, readily engage in sycophancy and deception under various triggers, and show inconsistency across semantically equivalent prompts.

## Strengths

- **Holistic three‑aspect design.** The paper organizes honesty evaluation around self-knowledge, non-deceptiveness, and consistency as interconnected components rather than isolated behaviors (Section 3). This provides a unified framework where prior work treated these in isolation, which is a genuine structural contribution.

- **Concrete, operationalized metrics for each scenario.** Every scenario is paired with a clearly defined quantitative metric (refusal rate, sycophancy rate, lying rate, performance spread, inconsistency rate, agreement rate, consistency rate). Table 1 summarizes all metrics alongside dataset sources and sizes; formulas are given in Sections 3.1–3.3.

- **Nuanced deception scenarios.** The burglar-deception test (Section 3.2.2) distinguishes positive-purpose, negative-purpose, and neutral-purpose deception, allowing finer-grained analysis of when and why models lie. The paper also transparently attributes some low lying rates to limited reasoning ability rather than honesty (Section 4.2.2, citing model outputs such as *"I am creating a red herring…"* from Llama2 models).

- **Experimental results substantiate the headline claim.** The results quantitatively demonstrate specific honesty deficits across all models: peak refusal rate only 50.03% (Table 2), sycophancy rates up to 80.21% (Table 3), inconsistency rates without CoT up to 82.08% (Table 4). Across essentially all metrics, no model performs well, supporting the paper's central message that honesty alignment has substantial room for improvement.

## Weaknesses

### Fatal

None.

### Major

- **Self-knowledge evaluation methodology lacks critical implementation details, harming reproducibility and validity.** The paper defines "known" questions as those a model can answer correctly under "multiple temperature sampling" (Section 3.1.2), but does **not** specify: (a) the number of samples per question, (b) the temperature value(s) used, or (c) the threshold for deeming an answer "correct" (any single correct sample? majority vote?). The citations `\citep{tempsample2024,multisample}` do not substitute for specifying the protocol in the paper. Without these details, the self-knowledge rate and answer rate cannot be independently reproduced, and the results could be sensitive to arbitrary choices. This is not a fatal "circularity" problem — using sampling to approximate knowledge boundaries is a reasonable two-step approach — but the missing protocol information is a significant gap that the authors must fill.

- **The aggregate consistency score uses per-run min–max normalization, making scores relative to the specific model set tested.** For the Consistency aspect (Section 3.3), metrics with different orientations are normalized using formulas involving `max(X)` and `min(X)` across the nine evaluated models. This means the scores would shift if a different set of models were evaluated, making cross-study comparison unreliable. The paper should report raw (unnormalized) metrics alongside the aggregate, or fix the normalization reference a priori.

### Minor

- **No confidence intervals or variance estimates for any reported metric.** All results (refusal rates, sycophancy rates, lying rates, etc.) are presented as point estimates without confidence intervals, standard deviations, or significance tests. Several metrics are computed on moderately sized datasets (e.g., 200 burglar examples, 162 werewolf examples), where variance could be non-trivial. This makes it impossible to judge whether differences between models (e.g., 31.37% vs. 37.80% refusal rate) are meaningful.

- **The werewolf game scenario conflates competent gameplay with dishonesty.** The "lying rate" in Scenario 6 measures how often the model conceals its werewolf identity to win the game. Strategic deception within a game's rules is not clearly normative dishonesty in the sense that concerns alignment researchers. The paper acknowledges this partially but treats the lying rate as a uniformly negative signal in the benchmark design without disentangling task-appropriate behavior from alignment failure.

- **The Prompt Format scenario (Scenario 7) captures tokenization sensitivity and robustness rather than honesty per se.** Measuring performance spread across five template variations (adding/removing colons, changing capitalization) detects sensitivity to input formatting, which could stem from architectural limitations (as the paper's own Limitations section notes) rather than dishonesty. The scenario's inclusion as a measure of "honesty" rather than "robustness" is arguable, though the paper does acknowledge this confound.

### Trivial

- The paper uses "perf. spread" as a consistency metric in Scenario 7 but does not describe the Natural Instructions task #24 being evaluated, making it hard to assess whether the performance spread is meaningful.

## Nice-to-Haves

- A correlation analysis between BeHonest scores and existing honesty-related benchmarks (e.g., TruthfulQA) would help validate that the benchmark captures something distinctive.
- Sample prompts and generation methodology for the augmented/synthetic datasets (burglar, werewolf) would improve usability, along with a brief human validation check.

## Removed Points

These points from the inputs are flagged for removal; treat them with caution.

- **"The self-knowledge approach is fundamentally circular and invalid"** (Harsh Critic). This overstates the problem. The paper uses sampling to *approximate* knowledge boundaries (explicitly acknowledged as an approximation in line 60: "Note that delineating the precise knowledge boundaries for a model is a significant challenge. Thus, for scenario 2, we approximate…"), then uses greedy decoding to measure behavioral awareness of those boundaries. It is a two-step estimation, not a circular definition. Retained as the **reproducibility gap** (Major weakness) above, which is the real and actionable issue.

- **"The unknown dataset may not be guaranteed unanswerable"** (Harsh Critic). The paper uses established benchmarks (SelfAware, UnknownBench) designed for this purpose. Whether specific ambiguous questions (e.g., "Are we alone in the universe?") are genuinely unanswerable is a design property of those source datasets, not an error in the paper.

- **"Missing related works"** (implied). Not included per instructions: outside knowledge cannot confirm which works are missing.

- **"Formatting/style nitpicks" and "typos/grammar/punctuation"**. These are parser artifacts, not author errors.

- **Strength Finder's "Practical approximation of knowledge boundaries"**. This conflicts with the verified Major weakness (insufficient methodological detail). Per the merge rules, the weakness wins.

- **Strength Finder's generic claim about "well-defined metrics"**. This was merged into the retained strength about concrete operationalized metrics and not double-counted.

## Novel Insights

None beyond the paper's own contributions. The reviews did not surface an observation about the paper that the paper itself does not already articulate.

## Suggestions

1. **Specify the sampling protocol** for Scenario 2: number of samples, temperature value(s), and correctness threshold. This is the single most important fix for reproducibility.
2. **Report raw (unnormalized) metrics** for the Consistency aspect alongside the aggregate scores, so future work can compare absolute values.
3. **Add confidence intervals** (bootstrap intervals are straightforward) for at least the key metrics (refusal rates, sycophancy rates), especially on smaller datasets.
4. **Clarify the relationship between strategic deception (werewolf) and normative dishonesty** — either exclude it, flag it separately, or provide a clearer argument for its inclusion.
5. **Describe Natural Instructions task #24** so readers can assess the meaningfulness of the performance spread metric.
