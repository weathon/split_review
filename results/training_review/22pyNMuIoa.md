Now I have all the evidence needed. Let me construct the final review.

## Summary

This paper introduces PromptAgent, a prompt optimization framework that formulates prompt search as a strategic planning problem solved via Monte Carlo Tree Search (MCTS). The key innovation is using error feedback from the base model's mistakes as actions, guided by an LLM's self-reflection, to iteratively inject domain-specific knowledge into prompts. The method is evaluated on 12 tasks spanning BBH, biomedical, and general NLP domains, showing consistent improvements over human-written prompts, Chain-of-Thought prompting, and Automatic Prompt Engineer (APE).

## Strengths

- **Novel formulation of prompt optimization as a strategic planning problem using MCTS.** The paper is the first to introduce MCTS with principled lookahead and backtracking for prompt optimization. The ablation study (Table 5) directly validates this design: MCTS outperforms Monte Carlo, Beam, and Greedy search on all 5 tested tasks, with 5.6% relative improvement over the best alternative — strong evidence that the planning architecture is the source of gains, not just the error-feedback mechanism.

- **Error-feedback-based action generation provides a principled way to inject domain knowledge.** Unlike prior methods relying on paraphrasing or random edits, PromptAgent collects errors from the base model on training samples and uses LLM self-reflection to generate constructive error feedback. The qualitative trace for NCBI (Figure 4 in the paper, numbered Figure 6 in the original) shows how this progressively injects biomedical domain knowledge (e.g., avoiding inheritance patterns, recognizing abbreviations), raising F1 from 0.521 to 0.645. This directly substantiates the claim of emulating human trial-and-error refinement.

- **Consistent empirical improvements with substantial margins across diverse domains.** PromptAgent achieves an average absolute improvement of ~9.5% over CoT on BBH (0.802 vs. 0.707), 7.3% over APE on domain-specific tasks, and 9% over APE on general NLP tasks. These margins are large enough that the core empirical finding — that strategic planning with error feedback produces better prompts than existing methods — is clearly supported even without statistical tests. The evaluation covers 12 tasks across 3 distinct domains, lending breadth to the findings.

- **Exploration efficiency analysis demonstrates concrete practical advantage.** Figure 2a plots accuracy vs. number of prompts explored, showing PromptAgent consistently achieves higher accuracy with fewer explored prompts than greedy search variants and APE. This is a genuine practical benefit: the method is both more effective and more computationally efficient.

## Weaknesses

### Fatal
None.

### Major

- **No variance or statistical significance reporting in main results.** All accuracy/F1 results in Tables 1–3 are reported as point estimates without standard deviations, confidence intervals, or significance tests. While the temperature-0.0 evaluation setting mitigates base-model stochasticity, the optimization process itself involves stochasticity from batch sampling and optimizer LLM generation (temperature 1.0). The paper uses the word "significantly" (e.g., "significantly outperforms"), which is not justified without statistical testing. The convergence analysis (Figure 2b) does report mean and variance across tree depth for one task, but this does not substitute for run-to-run variance on the final results. This is the paper's most significant methodological weakness.

- **The GPT Agent baseline is insufficiently specified.** The paper describes it as a ChatGPT plugin ("AI Agents") with GPT-4 that "similarly sample[s] similar model errors and ask AI Agents plugin to rewrite the prompt." No details are given about the plugin's internal algorithm, configuration, iteration count, or how it was adapted to the task. Without this information, the comparison is difficult to interpret, and the baseline's poor performance (e.g., 0.125 F1 on NCBI) may reflect a poor adaptation rather than a genuine limitation of non-strategic methods. This weakens the claim that PromptAgent's advantage over "GPT Agent" demonstrates the necessity of strategic planning.

### Minor

- **Key hyperparameter values for the MCTS expansion step are not reported.** The paper mentions `expand_width`, `num_samples`, and `depth_limit` and says "we explore three settings" but never reports what these settings were, which one was selected, or how sensitive results are to these choices. While the exploration of three settings suggests some tuning, the lack of disclosed values impairs reproducibility and makes it impossible to assess whether results are robust to these choices.

- **Transferability to weaker models (PaLM 2) shows mixed results that are not fully explained.** PromptAgent underperforms baselines on 5/12 tasks when transferred to PaLM 2 (e.g., Object Counting: 0.320 vs. APE 0.378; TREC: 0.230 vs. Human 0.380). The paper acknowledges this briefly but provides no analysis of why some tasks fail. While the paper correctly notes that "less advanced...LLMs may not adeptly grasp the subtleties of these expert-level prompts," a more detailed analysis of failure cases would strengthen the transferability claims.

- **Exploration efficiency analysis uses an incomplete cost metric.** Figure 2a measures "number of prompts explored" but does not account for the additional LLM calls required for error-feedback generation (optimizer calls per node) and reward evaluation. A cost comparison that accounts for total API calls would be more informative, though the qualitative advantage is still clear.

### Trivial

- The ablation study covers only 5 tasks. The authors acknowledge the computational budget constraint, but expanding this to more tasks would strengthen the claim that MCTS planning is consistently superior.

- Only one full MCTS trajectory trace is shown (NCBI). Showing traces from other domains would provide stronger evidence that the method consistently produces expert-level prompts across tasks.

## Nice-to-Haves

- An ablation that replaces error-feedback actions with generic rewrites (paraphrasing, instruction to "improve" without error collection) would isolate the specific contribution of the self-reflection component.
- Testing with a weaker optimizer (e.g., GPT-3.5 as optimizer) would demonstrate that the method does not require the strongest available LLM.
- Reporting confidence intervals or running multiple seeds (even 3) would substantially strengthen the empirical foundation. Given the temperature-0.0 evaluation and the large margins on many tasks, this is mitigable in a revision.

## Removed Points

These points were removed per meta-reviewer guidelines; they are listed here for completeness only and should be treated with caution.

- **"Missing OPRO / missing related works"** — Removed per policy: the meta-reviewer cannot independently verify whether OPRO exists or was omitted, and identifying missing references is outside the reviewer's scope.
- **"Expert-level not rigorously defined"** — Removed: the paper provides comparisons against human prompts, a qualitative analysis showing richer prompt structure, and performance improvements. The claim is sufficiently supported for an empirical paper.
- **Action generation "critically underspecified"** — Weakened from the original harsh framing. The paper provides a clear two-step process description and references to meta-prompts m₁ and m₂, which are standard content for an appendix (and the appendix was stripped by the parser). The core mechanism is described conceptually; the missing details are typical for a main paper.
- **"Paper claims superior transferability despite mixed results"** — The paper explicitly acknowledges that PaLM 2 "performance drops dramatically" and claims superiority on "7/12 tasks," which is factually accurate. The paper does not overclaim; this criticism mischaracterizes the authors' own transparency.

## Novel Insights

Beyond the paper's own contributions, a noteworthy observation from this review is that the paper's strongest evidence for the "strategic planning" claim is not the raw performance numbers (which could theoretically be explained by any number of factors) but the ablation study (Table 5) showing MCTS consistently outperforms Monte Carlo, Beam, and Greedy search **when all use the same error-feedback mechanism**. This experimental design — holding the action generation constant while varying only the search algorithm — cleanly isolates the contribution of MCTS-based planning. It is a model of how to design ablation studies in this area. Conversely, the weakest link in the paper's evidence chain is the GPT Agent baseline, which conflates a different search method with a different action generation mechanism, making it impossible to attribute its poor performance to any specific deficiency.

## Suggestions

1. **Add confidence intervals or run multiple seeds.** Even 3 seeds with standard deviations reported for the main result tables would address the most significant weakness. The margins are large enough on many tasks that this is unlikely to change the conclusions but is essential for rigor.
2. **Disclose the hyperparameter sweep results.** Report the three settings explored for `expand_width`, `num_samples`, and `depth_limit`, and indicate which was selected. A brief sensitivity analysis showing that results are not highly sensitive to these choices would be valuable.
3. **Better specify the GPT Agent baseline** or replace it with a more standard and verifiable baseline (e.g., a simple iterative rewrite baseline without MCTS but with error feedback, which already exists in the search ablation).
4. **Include failure analysis on PaLM 2.** Even a brief discussion of why certain tasks (e.g., TREC, Object Counting) see degraded performance would strengthen the transferability analysis.
5. **Report complete meta-prompts** (m₁, m₂) — likely already in the appendix but ensure they are present in the camera-ready version.

## Score and Decision

This paper introduces a well-motivated and novel approach to prompt optimization, with a clean formulation (MDP + MCTS), a principled action mechanism (error feedback), and broad empirical evaluation across 12 tasks spanning three domains. The core claims are supported by the ablation study and the large performance margins on the main experiments. The weaknesses — primarily the lack of variance reporting and some underspecified details — are significant but not fatal; they are addressable in a revision without altering the paper's conclusions. The paper represents a genuine advance over existing prompt optimization methods.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>