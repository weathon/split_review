Now I have all the information needed. Let me produce the final consolidated review.

## Summary

KOR-Bench introduces a benchmark designed to evaluate LLM reasoning while minimizing reliance on pre-trained domain knowledge — a principle the authors term "knowledge orthogonality." The benchmark spans five categories (Operation, Logic, Cipher, Puzzle, Counterfactual), each with 25 manually modified rules and 10 questions per rule (1,250 total). The paper evaluates 30+ chat and base models, revealing substantial performance gaps (e.g., O1-Preview at 72.88% vs. GPT-4o at 58.00%) and provides detailed analyses including stepwise prompting for Cipher bottlenecks, self-correction dynamics, and complex task processing.

## Strengths

1. **Well-motivated and timely concept.** The paper identifies a genuine limitation of existing benchmarks — conflating memorized knowledge with genuine reasoning — and proposes a concrete design principle ("knowledge orthogonality") to address it. The five-category taxonomy (new symbols, new concepts, new execution rules, new frameworks, new story contexts) is thoughtfully constructed and covers diverse reasoning modalities.

2. **Large and consistent performance gaps reveal discriminative power.** KOR-Bench produces striking separations: O1-Preview (72.88%) and O1-Mini (70.16%) far outpace Claude-3.5-Sonnet (58.96%) and GPT-4o (58.00%), with the gap widening dramatically on Cipher (82.80% vs. 42.80%) and Puzzle (36.80% vs. 16.80%). This demonstrates that the benchmark measures capabilities beyond what standard evaluations capture. The comprehensive evaluation across 30+ models (including base models) provides a detailed performance landscape.

3. **Insightful beyond-accuracy analyses.** The stepwise prompting analysis of Cipher tasks identifies specific bottlenecks (Rotation, Conditional Filling, Conditional Reading at ~100% error rates) — a granular diagnosis that gives actionable guidance for improving spatial-manipulation reasoning. The self-correction experiment (optimal gains at 2 rounds, +10.36% on average) and the Complex Task Processing evaluation (multi-rule/multi-question settings) add depth beyond point estimates.

4. **Careful answer-format design and evaluation.** The paper uses five distinct answer formats (NR, ME, TR, MC, SD) matched to each task category and employs SymPy for mathematical expression comparison — a pragmatic approach that balances rigor with the diversity of reasoning outputs.

## Weaknesses

### Fatal
None.

### Major

1. **The central claim of "knowledge orthogonality" is not empirically verified.** The paper states (lines 37, 86) that rules are "independent of the domain-specific knowledge the model is exposed to during pre-training" and "do not appear in common pre-training data," but provides no systematic verification — no contamination analysis (e.g., n-gram overlap with known training corpora, probing experiments, or membership inference). The design rationale for each category (modifying operations, adjusting ciphers, etc.) is a plausible argument, but it is not a substitute for evidence. This matters because the benchmark's core differentiator is its claim to isolate reasoning from knowledge. Without verification, a reader cannot assess whether high performance reflects genuine rule-following or partial pattern-matching from pre-training exposure — especially for Counterfactual tasks built on known fictional works. **This is a structural gap: it weakens the paper's central contribution and cannot be fully resolved without additional experiments.**

### Minor

2. **No statistical reliability measures for fine-grained comparisons.** With 1,250 total questions (250 per category, 10 per rule), many model pairs differ by only 1–2 percentage points (e.g., Claude-3.5-Sonnet at 58.96% vs. GPT-4o at 58.00%). The paper reports no confidence intervals, significance tests, or per-rule variance. This makes it difficult to determine which observed differences are meaningful, especially for closely ranked models. While this is common practice in many benchmark papers, the paper's emphasis on fine-grained rankings (including bold/underline for 1st/2nd/3rd) invites scrutiny that the current statistics cannot fully support.

3. **Some interpretive claims go beyond what the data supports.** The claim that "Claude-3.5-Sonnet is more accurate in understanding and applying rules, while GPT-4o is better at handling tasks that require in-depth analysis and creative thinking" (line 181) is presented as a finding but is a post-hoc interpretation of small per-category differences. Both models achieve nearly identical overall accuracy (58.96% vs. 58.00%), and the per-category gaps (e.g., Claude +14.8% on Logic, GPT-4o +9.6% on Cipher) are consistent with task-specific strengths but do not cleanly map to the abstract traits invoked.

4. **No human baseline.** Without human performance on a sample of tasks, it is difficult to calibrate difficulty: a low model accuracy could mean the task is genuinely hard for reasoning, or that the rule descriptions are ambiguous. A human baseline (even a small set) would strengthen the validity of the benchmark as a reasoning test.

5. **The effect of rule length is not analyzed.** Rules vary from 51 to 4,572 characters across categories (Table 1). Whether longer rule texts overload context windows or confuse models is a natural question that is not addressed. This is especially relevant for the Counterfactual category (avg. 4,572 chars) where performance is uniformly high (70–92%), and the Cipher category (avg. 2,436 chars) where performance varies dramatically.

### Trivial
- The "Avg. R Len" and "Avg. Q Len" in Table 1 report characters; tokens would be more informative for LLM evaluation.
- The table descriptions (e.g., Tables~\ref{operation_rule_description}–\ref{counterfactual_rule_description}) are referenced but their content is absent from the parsed text — presumably present in the original submission's appendix.

## Nice-to-Haves
- A simple contamination probe (e.g., perturbing superficial details of a subset of rules and checking whether accuracy is affected) would substantially strengthen the core claim.
- Reporting per-rule variance (e.g., box plots or standard deviations across the 25 rules per category) would clarify whether overall scores are driven by a few easy rules or reflect consistent ability.
- Expanding the stepwise bottleneck analysis beyond Cipher to Puzzle or Logic tasks would deepen the paper's diagnostic contributions.

## Removed Points
These points are flagged to be removed; treat them with caution.
- *"Prompt section is truncated/incomplete, affecting reproducibility"* — The prompt content (Section 4.1) is clearly garbled in the parser extraction. This is a text-extraction artifact, not an author omission. The evaluation methodology (regex parsing, SymPy, custom scripts) is described at a reasonable level, and the paper commits to releasing the full codebase.
- *"The paper does not explain why lower real-life answer ratios are better"* — The paper actually explains this clearly: questions are "crafted to deviate from real-life answers" (line 122), and the table caption states "lower proportions being better" (line 268). The text also notes the decreasing trend with model quality (line 279).
- *"Table 2 is hard to parse due to formatting artifacts"* — Formatting artifacts from PDF extraction; the original table is standard.
- *"The Counterfactual task tests recall of fictional universes, not reasoning"* — The questions present the fictional world's rules in the prompt context and ask for counterfactual answers that deviate from real life; this is a reasoning task by design. The broader contamination concern (whether models have seen these works) is already covered under Major weakness #1.
- *"Missing appendix/proofs/references"* — Parser strips these; they exist in the original submission.

## Novel Insights
Beyond the paper's own contributions, the reviews surface an important tension: the paper's core innovation (knowledge orthogonality) is a **design claim** rather than an **empirically verified property**. This is a recurring challenge in the benchmark community — how to verify negative claims about what models have *not* seen — and KOR-Bench would benefit from adopting or adapting recently developed contamination detection methods (e.g., benchmark decontamination via n-gram analysis, or behavior-based tests like the perturbation probe suggested above). The stepwise prompting analysis, while limited to Cipher, provides a template for how to diagnose *where* reasoning breaks down rather than just reporting aggregate scores — a methodological contribution that could be applied broadly.

## Suggestions

1. **Add a contamination analysis.** The single most impactful improvement: take a random subset of rules/questions, perturb surface-level details (renaming symbols, changing numbers, rotating ciphers differently), and check whether accuracy changes. If models are genuinely reasoning from the rule description, surface changes should have little effect; if they are pattern-matching, accuracy would drop. Alternatively, compare model rankings on KOR-Bench vs. a knowledge-heavy benchmark (e.g., MMLU) to show divergence.

2. **Report confidence intervals or bootstrapped error bars** for overall and per-category scores, especially for closely ranked models.

3. **Add a small human baseline** (e.g., 5–10 educated participants on a stratified sample of 50 questions) to calibrate task difficulty.

## Score and Decision

The paper proposes a genuinely useful benchmark concept and backs it with broad evaluation and thoughtful analyses. However, the central claim — that the benchmark achieves knowledge orthogonality — is asserted but not verified, which weakens the paper's main differentiator. The remaining issues (statistical reliability, interpretive overclaiming, no human baseline) are standard for a conference submission and addressable. I see a well-motivated, valuable contribution that needs one round of strengthening on its core claim before it fully delivers on its premise.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>