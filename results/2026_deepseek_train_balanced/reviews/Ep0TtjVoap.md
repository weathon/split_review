## Summary

This paper proposes ToRA, a family of open-source LLMs trained to interleave natural language reasoning with program-based tool use (code execution, symbolic solvers) for mathematical problem solving. The training pipeline has two stages: (1) imitation learning on GPT-4-synthesized interactive trajectories, and (2) output space shaping, which expands the training set with self-sampled valid trajectories and teacher-corrected invalid ones. The method achieves strong results across 10 mathematical reasoning datasets, with CodeToRA-34B reaching 50.8% on MATH (the first open-source model above 50%) and ToRA-7B surpassing WizardMath-70B.

## Strengths

- **Format ablation controls for data quantity and isolates format effects.** Figure 5 compares Rationale-only, Program-only, and Tool-integrated formats using equal training data sizes. The interleaved format outperforms Program-only by 6.7% (LLaMA-2) and 9.8% (GPT-4) on MATH — both conditions have tool access, so this comparison directly measures the benefit of interleaving, not just tool access. This is the paper's strongest single piece of evidence for its central design claim.

- **Output space shaping ablation cleanly isolates the correction effect.** Figure 6 compares three conditions: (a) no shaping, (b) sampling only, (c) sampling + correction. Conditions (b) and (c) both use "up to 4 additional trajectories per problem," so data volume is controlled. The finding that correction adds ~1.8% absolute improvement over sampling alone (4.5% vs. 2.7%) is a clean, well-designed ablation.

- **Strongest open-source results on MATH at time of submission.** ToRA-7B achieves 44.6% on MATH (surpassing WizardMath-70B's 22.6%), and CodeToRA-34B reaches 50.8% — competitive with GPT-4-Code (51.8%). These are concrete, verifiable numbers against published baselines.

- **Manual error analysis provides an honest characterization of remaining challenges.** The paper annotates 100 failure trajectories on MATH, finding that 38% stem from incorrect reasoning steps, 21% from diagram misinterpretation, and 28% from tool-use issues. This provides a grounded research agenda for future work.

- **Library-usage analysis adds interpretability.** Figure 7 breaks down which Python libraries are used per MATH subtopic (e.g., `sympy.solvers` for Algebra, `rational` for Geometry), showing readers *how* the model uses tools, not just that it performs better.

- **Out-of-distribution generalization is explicitly tested.** TabMWP results show ToRA-70B reaching 74.0% while WizardMath-70B underperforms its base model (49.8% vs. 57.5%), providing evidence that tool-integrated reasoning generalizes better than rationale-only SFT.

## Weaknesses

### Minor

- **The "format" comparison conflates two factors.** The paper presents the 29.0% improvement of Tool-integrated over Rationale-only as a format comparison, but this improvement reflects both the change in reasoning format AND the addition of tool access. The Rationale-only model has no external computation; the Tool-integrated model can execute arbitrary Python/sympy. The paper reports this number alongside the 6.7% improvement over Program-only (where both have tool access) without explicitly noting that the 29.0% figure bundles two separate factors. While the paper does not misrepresent the data, the framing treats all three comparisons somewhat equivalently when they are not.

- **The "13%-19% absolute improvements" claim is over-aggregated.** This figure compares ToRA to prior open-source models that differ in base architecture, training data, and inference procedure. The claim is listed as observation (1) in the main results without caveat that it aggregates across heterogeneous, non-controlled comparisons. The individual numbers in the tables are informative, but the headline range (13%-19%) conflates the method's contribution with base model choice, data overlap, and other confounds.

- **No variance estimates reported.** All main results use greedy decoding (which eliminates sampling variance at inference), but the training pipeline involves nucleus sampling for trajectory generation and correction. No results are reported across multiple training seeds or sampling seeds. A measure of stability — even a simple single-seed check — would strengthen the evidence.

- **Error analysis sample size is small.** The manual annotation covers 100 trajectories (~2% of the MATH test set). No confidence intervals or inter-annotator agreement statistics are reported. This limits the informativeness of the categorical breakdown (38% reasoning errors, 21% diagram issues, etc.).

### Trivial

- **Correction procedure details are underspecified.** The paper states that invalid trajectories are corrected by "enumerating possible preceding portions" (line breaks as truncation points) and having a teacher model complete them, but does not specify the stopping criterion for the enumeration (e.g., how many prefixes are tried before giving up, or whether the best completion is selected by answer correctness).

## Nice-to-Haves

- The format ablation could be extended beyond MATH to GSM8k, SVAMP, or TabMWP to test whether the interleaving advantage generalizes.
- Comparison with inference-time techniques like self-consistency (Wang et al., 2022) applied on top of ToRA would clarify whether the gains are complementary.
- A systematic breakdown of tool-call error rates across the full test set (rather than only 100 samples) would be valuable.
- A brief discussion of the computational cost of the full pipeline (GPT-4 API calls + 64× sampling per training question) would aid practical reproducibility.

## Removed Points

- **Output space shaping confounded with data volume (Harsh Critic point 2):** Removed as a claimed weakness. The paper's Fig 6 ablation *does* control for data volume between sampling-only and sampling+correction conditions — both use "up to 4 additional trajectories per problem." The critic's concern about the imitation learning baseline having less data than shaping conditions is acknowledged but the paper does not claim otherwise; the controlled comparison is between conditions 2 and 3.
- **Toolformer comparison missing (Harsh Critic):** The paper cites Toolformer in Section 4 and its result appears in a table (stripped by PDF parser). This is a parser artifact, not a paper omission.
- **No related work section (Harsh Critic):** The parser stripped the appendix and references. The original submission contains these sections.
- **Missing appendix/proofs (Harsh Critic):** Parser artifact.
- **Various formatting/style nitpicks:** Parser artifacts, not author errors.
- **Strength Finder's generic strengths about "important problem" etc.:** Removed — these are generic and not specific to the paper's content.

## Novel Insights

None beyond the paper's own contributions. The reviews surface real framing concerns and experimental gaps but do not reveal a novel analytical lens that the paper itself lacks.

## Suggestions

1. **Rephrase the format ablation discussion** to explicitly separate what the Rationale-only vs. Tool-integrated comparison tells us (benefit of tool access + interleaving) from what the Program-only vs. Tool-integrated comparison tells us (benefit of interleaving alone, cleanly). The numbers are there; the framing needs precision.
2. **Add a caveat to the "13%-19%" claim** noting that it aggregates across heterogeneous baselines and is not a controlled measurement of the method's standalone contribution.
3. **Add variance information** — at minimum, note whether a single seed was used, or report results across 2-3 seeds for a representative configuration.
4. **Provide confidence intervals or a larger annotation sample** for the error analysis, or explicitly note the limitation.

## Score and Decision

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>