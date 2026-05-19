- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 8, 6, 6
Now I have all the information I need. Let me carefully compose the consolidated review.

---

## Summary

This paper introduces LintSeq, a parameter-free algorithm that refactors existing programs into sequences of static-error-free, insertions-only code edits using a linter to guide backward sampling and the Unix diff operator to compute text diffs. By finetuning autoregressive LMs on these synthetic edit sequences (rather than whole programs), the authors demonstrate consistent improvements in the coverage–samples tradeoff across six models from three families (Gemma 2, Phi-3, Llama 3.1) and two custom-pretrained TinyCodeLMs. The linter ablation experiment isolates the error-free property of LintSeq edits as a causal driver of improvement.

## Strengths

1. **Novel algorithm for generating synthetic edit data without LLMs or commit data.** The LintSeq algorithm (Section 2.2) is parameter-free, requires only CPU, and produces edit sequences from existing programs without relying on any LLM or human-annotated commit history. This directly addresses the scarcity of open-source edit sequences noted in the abstract and is a genuine methodological contribution.

2. **Consistent improvements across model families and scales.** Finetuning on LintSeq data yields higher pass@k coverage on HumanEval and MBPP for every tested model — Gemma 2 (2.6B, 9B), Phi-3 (3.8B, 14B), Llama 3.1 (8B), TinyCodeLM (150M, 400M) — as shown in Figure 3. The gains increase with k, culminating in +20% (±3%) absolute pass@50 on HumanEval and +12% (±2%) on MBPP averaged across models. This directly supports the paper's claim that edit sequence finetuning improves the coverage–samples tradeoff.

3. **Clean linter ablation that controls for dataset size and format.** The ablation study (Section 3.5, Figure 4) replaces linter-guided sampling with random line deletions while keeping the number of edit sequences per example (s=5) identical. Linter removal reduces pass@50 on HumanEval from 22.6% to 17.7% for TinyCodeLM-150M and from 26.8% to 22.0% for TinyCodeLM-400M. Because this comparison holds dataset size constant, it cleanly isolates the error-free property of LintSeq edits as the driver of improvement.

4. **Clean testbed via custom-pretrained tiny LMs.** Pretraining TinyCodeLM-150M and TinyCodeLM-400M from scratch (Section 3.1) on code-skewed data ensures no data contamination from prior instruction or edit data, strengthening causal interpretation of finetuning results.

5. **Practical impact demonstrated.** TinyCodeLM-LintSeqInstruct (150M) achieves pass@1/pass@10 of 12.8/20.6 on HumanEval (Table 1), outperforming Codex 85M (8.2/12.8) and AlphaCode 89M (4.3/12.2), and matching or exceeding models with roughly twice its parameters.

## Weaknesses

### Fatal
None.

### Major

1. **Dataset size confound in the central comparison (baseline vs. LintSeq).** The baseline dataset contains 88,900 instruction+program pairs; LintSeq generates s=5 sequences per pair, yielding 444,500 training examples (Section 3.2). Both models are finetuned for the same number of optimizer steps (Section 3.3), so the LintSeq model sees 5× more unique examples. The reported improvements (e.g., +20% pass@50) could therefore be driven, at least in part, by increased data volume rather than the edit-sequence representation per se. The paper does not acknowledge this confound. An ablation that subsamples the LintSeq data to match the baseline size, or synthetically expands the baseline data to 444,500 examples, is needed to attribute the gains specifically to the edit-sequence format. *Why it matters*: This is the primary empirical claim of the paper, and the confound weakens the strength of the attribution. The paper should either provide the controlled experiment or explicitly reframe the contribution as a data augmentation method (where the increase in data volume is part of the benefit).

2. **Incommensurable comparisons to prior models in Tables 1 and 2.** The paper reports "temperature-tuned" results for TinyCodeLM-LintSeqInstruct and compares to published numbers for Codex, AlphaCode, CodeT5+, and others (Tables 1 and 2). The evaluation protocol used by the paper (temperature=1, top-p=0.95, n=50) likely differs from the protocols used in the original papers (e.g., Chen et al. 2021 report Codex results at temperature 0.8; Li et al. 2022 use temperature 0.7 with much larger sample counts). The paper does not specify whether prior-model numbers were re-evaluated under a shared protocol or taken verbatim from publications. If taken verbatim, observed superiority could be an artifact of different sampling conditions. *Why it matters*: This weakens the "state-of-the-art" claim for the on-device model class. The publisher's note on reproducibility advises against accepting such comparisons at face value.

### Minor

1. **Diversity is inferred from pass@k but not directly measured.** The paper claims improved output diversity from edit-sequence training (Sections 1, 5, and the error-rate analysis in Section 3.5), but this is inferred solely from pass@k curves. While pass@k is a reasonable diversity proxy under independent sampling, direct metrics (e.g., pairwise embedding similarity, number of unique functional solutions per problem) would substantially strengthen the diversity claim. The paper itself provides an error-rate analysis showing LintSeq models produce more static errors despite higher coverage (Figure 5) — this pattern is interpreted as evidence of diversity but is not directly validated.

2. **No sensitivity analysis for the s hyperparameter.** The only hyperparameter in LintSeq is s (number of edit sequences per program), set to s=5 throughout without justification. A sweep over s (e.g., 1, 3, 5, 10) would show how many edit sequences are needed for downstream gains and whether more sequences hurt due to redundancy.

3. **Linter configuration is underspecified.** The paper uses `pylint` (line 172) but does not specify which checks are enabled. "Static errors" could range from syntax errors to style violations. Reproducing the generation pipeline requires this information. The publisher's note on reproducibility flags this as a concern.

4. **No breakdown of error types in Figure 5.** The error-rate analysis shows overall static error frequencies but does not categorize error types (syntax vs. import vs. undefined variable). Such a breakdown could clarify whether LintSeq models produce riskier solutions or simply become less reliable in specific ways.

### Trivial

- The "remove all affected lines" description in the backward sampling algorithm (Section 2.2, line 85) could be slightly more precise, but is clear enough for reproduction given the overall algorithmic description.
- The inference cost analysis uses FLOPs estimates (Figure 1 teaser) without wall-clock times or GPU-hour measurements. FLOPs-based comparison is standard, but the cost-parity claim ("similar cumulative cost to sampling once from... Llama 3.1 405B") would benefit from a brief caveat.

### Nice-to-Haves

- A sweep over temperature values for the repeated sampling experiments would show whether the improvement holds across a range of temperatures, though using the same temperature (=1) for controlled within-pair comparisons is already a valid approach.
- Testing on longer-program benchmarks (beyond HumanEval/MBPP's short solutions) would bound potential concerns about edit sequence length degrading quality for longer programs.
- Comparing to a baseline that uses explicit single-edit prompting (repeatedly prompting a model to insert one line at a time) could further isolate the benefit of the teacher-forced multi-edit representation.
- Direct wall-clock or GPU-hour measurements would strengthen the cost-competitiveness claim.

## Removed Points

- **"The abstract states the +20% improvement without caveat about 5× data."** This point is partially valid and has been merged into Major Weakness 1. The abstract does not mention dataset sizes, but the paper transparently reports them in Section 3.2. The issue is acknowledged in the Major weakness above.
- **"Speculative fatal flaw: if normalization were X, reported values would be impossible."** Not present in this review; no action needed.
- **"Pure formatting nitpicks."** None were retained.
- **"Missing related works"** — not included as per instructions.
- **"Missing appendix content, proofs, references"** — not included as per instructions (parser strips these; they exist in the original submission).
- **Strength Finder's generic strengths removed:** "This paper addressed an important problem" and similar generic statements are dropped. The retained strengths are concrete and evidence-grounded.
- **The harsh critic's claim that the confound is "fatal"** is downgraded to Major because (a) the linter ablation controls for dataset size and shows that edit sequence quality matters, and (b) the paper's contribution includes the data augmentation aspect as part of the method — the improvement from having more varied training examples from the same programs is still a finding that supports the method's utility.

## Novel Insights

None beyond the paper's own contributions. The reviews did not surface an insight that the paper itself does not already express.

## Suggestions

1. **Run the controlled dataset-size ablation.** Subsample LintSeq data to 88,900 examples (or expand baseline to 444,500 via repetition/augmentation) and repeat the main comparison. If the improvement holds, the confound is eliminated. If it shrinks, report the breakdown honestly and reframe the contribution accordingly.
2. **Either re-evaluate prior models under a shared protocol, or explicitly caveat the comparisons** in Tables 1 and 2 as "published numbers, not re-evaluated under identical conditions."
3. **Add direct diversity metrics** (e.g., number of unique correct solutions per problem, average pairwise edit distance) to support the diversity claim.
4. **Report the pylint configuration** used for data generation. Publish a configuration file or specify the exact checks enabled.
5. **Add a brief sensitivity analysis for s** (e.g., s ∈ {1, 3, 5, 10}) in an appendix, or at minimum justify the choice of s=5 with one data point.
