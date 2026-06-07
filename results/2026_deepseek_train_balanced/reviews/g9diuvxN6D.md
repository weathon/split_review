## Summary
This paper empirically evaluates the robustness of instruction-tuned LLMs to rephrased instructions. The authors collect 319 manually composed instructions from NLP graduate students for tasks in MMLU and BBL, and compare model performance when using these "unobserved" instructions vs. instructions seen during training. They find consistent performance degradation (averaging over 5 points) across three model families (Flan-T5, Alpaca, T0), and a striking result: an incorrect-but-observed instruction can outperform a correct-but-unobserved one. They also propose a soft prompt alignment method with a KL-divergence term to mitigate this issue, showing modest but consistent gains.

## Strengths
1. **Multi-model, multi-benchmark evaluation substantially broader than prior work**: The paper evaluates three model families (Flan-T5, Alpaca, T0) at multiple scales (80M–11B), using five instruction-tuning datasets, across ~71 test tasks. This is explicitly differentiated from the closest prior work (Gu et al., 2023), which evaluated only T5 on a single dataset with 12 tasks. Table 1 reports per-task-type accuracy deltas for all model variants, providing granular evidence of the robustness gap.

2. **Striking finding that incorrect-but-observed instructions outperform correct-but-unobserved ones**: Section 3.2 (Figure 3) shows that using an instruction from a *different* task (but with the same output format) yields higher accuracy than using an appropriate but unobserved instruction. This goes beyond documenting a robustness gap—it reveals that models may over-rely on pattern-matching to observed surface forms rather than interpreting instructions semantically. This is a novel empirical finding not reported in prior work.

3. **Full ablation of the proposed method providing clear evidence of mechanism**: The soft prompt alignment method (PT+KL) is evaluated with four ablation conditions (FT, FT+KL, PT, PT+KL) in Table 4. The results show that only the full combination of prefix tuning plus KL-divergence loss yields consistent improvements (e.g., Alpaca-7B on BBL unobserved improves by +3.7%, from 42.9 to 46.6). Table 5 further validates the mechanism by showing reduced representation distance between observed and unobserved instructions after alignment, with the largest accuracy gain (+4.2%) corresponding to the largest distance reduction (30.1 → 27.9).

4. **Ecologically valid test-instruction collection**: 319 instructions manually composed by 36 NLP graduate students for the target tasks, rather than relying solely on automated paraphrasing, providing a realistic assessment of how these models would perform when deployed by human users who naturally vary phrasings.

## Weaknesses

### Fatal
None.

### Major
None. The paper's core claim—that instruction-tuned models are sensitive to rephrasing—is well-supported by consistent evidence across models, benchmarks, and the adversarial experiment.

### Minor
1. **Instruction quality confound partially unaddressed in the main results**: The observed instructions (from instruction-tuning datasets, carefully designed by dataset creators) are compared against unobserved instructions written by NLP grad students. If the latter are less clear or less well-structured, the performance gap could partly reflect instruction quality rather than phrasing robustness. The adversarial experiment (Section 3.2, Figure 3) *does* address this by showing that an incorrect-but-observed instruction outperforms a correct-but-unobserved one, but this experiment covers only 7 BBL datasets and one model (Flan-T5-XXL). For the main 71-task results across all models (Table 1), the confound is not fully ruled out.

2. **Inconsistent task counts and unclear instruction collection numbers**: The abstract claims "over 80 unique tasks" and the conclusion says "75 tasks," but the actual evaluation uses 57 MMLU + 14 BBL = 71 tasks (line 191). The number of BBL tasks is inconsistently reported as 18 (lines 163, 173) versus 14 (line 191). Additionally, the paper states 12 graduate students were asked per task for 18+57=75 tasks (which would yield up to 900 instructions), but only 319 were collected. Table 2's "Unobserved Instructions" section shows only 160 unobserved instructions (20 for MMLU + 140 for BBL), which does not match the 319 total claimed. These inconsistencies need clarification.

3. **The "6.9 point drop" claim in the introduction is not clearly traceable**: Line 44 states that Flan-T5-XXL suffers a "6.9 point drop in absolute performance on average across large benchmarks." However, Table 1 shows Flan-T5-11B (XXL) with an overall drop of 2.2 points (61.4 → 59.2). The paper does not specify how 6.9 is derived, creating a mismatch with the primary results table.

4. **Key hyperparameter λ not reported or ablated**: The KL loss weight λ is introduced (line 550) but no specific values or sensitivity analysis are provided. Given the method's modest gains, understanding λ sensitivity is important.

5. **Soft prompt dimensions (d, n) never specified**: The method introduces soft embedding parameters ℝ^{d×n} (line 546), but neither the number of soft prompt tokens (n) nor their dimensionality (d) are reported.

6. **Method evaluated on only 2 of 3 model families**: The proposed method is tested on Flan-T5-3B and Alpaca-7B, but not on T0 (used in the main analysis section), leaving open questions about generalization across the full set of models studied.

7. **GPT-4 dependency creates reproducibility concerns**: The paraphrased instructions used for alignment are generated by GPT-4 (lines 612–613), whose outputs are non-deterministic. This is not discussed.

### Trivial
1. **Table 2 formatting is confusing**: The "Unobserved Instructions" sub-table uses column spans that make it unclear whether MMLU is being treated as 1 meta-task with 20 instructions or a different aggregation.

## Nice-to-Haves
- Having the same NLP practitioners write instructions for a small set of tasks *already in the training set* would provide a cleaner control for the instruction quality confound.
- Including statistical significance tests on the main results (Table 1) would strengthen the analysis, though the consistent direction makes the result clear.
- Analyzing what the learned soft prompts actually encode (e.g., do they shift representations toward a canonical "instruction" region?) would deepen the method contribution.
- Ablating λ values to assess sensitivity would strengthen the method evaluation.

## Removed Points
- "The proposed method improves robustness only modestly" (Harsh Critic): Removed because this is the authors' own honest characterization (line 688: "consistently (though modestly) improving"), not a flaw.
- "No statistical tests": Demoted to Nice-to-Have. Standard deviations are reported; the pattern is clear across all models.
- Various generic strength claims from Strength Finder (e.g., "addressed an important problem"): Removed as superficial or lacking specific evidence.
- Formatting/style nitpicks and speculative concerns about missing appendix content: Removed per filtering rules.

## Novel Insights
None beyond the paper's own contributions. The reviewers' analyses largely corroborate the paper's stated findings.

## Suggestions
- Clarify the task count discrepancy: reconcile "over 80," 75, and 71, and explain how 319 total instructions relate to the 12-per-task target.
- Clarify where the "6.9 point drop" figure comes from, or correct it if it's an error.
- Report λ values and the soft prompt dimensions (d, n) used in experiments.
- Consider evaluating the proposed method on T0 to match the scope of the analysis section.
- Add a brief discussion of GPT-4's non-determinism and its implications for reproducibility.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>