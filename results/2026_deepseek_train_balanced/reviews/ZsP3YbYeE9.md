Now I have all the information needed. Here is the final consolidated review.

---

## Summary

This paper proposes DoT (Diversity of Thoughts), a framework that modifies reflection-based LM agents (building on Reflexion) by (a) generating *k* diverse reflections in one shot to reduce redundancy and (b) adding a task-agnostic memory bank that stores and retrieves successful trajectories for cross-task knowledge transfer. Experiments on code generation benchmarks (HumanEval, MBPP, LeetCodeHardGym) across multiple LLMs show consistent improvements, with the most notable result being a 7.5%+2.5% Pass@1 gain on LeetCodeHardGym (Claude Sonnet 3.5) where both Reflexion and LATS fail to improve at all, alongside a 4× cost reduction versus LATS.

## Strengths

- **Quantified motivation for the redundancy problem.** The paper does not just assert that reflections are repetitive — it measures average pairwise cosine similarity (Table 9) and documents reflection counts and token usage (Table 1), giving the motivation an empirical foundation. This is a concrete, replicable diagnosis of a genuine limitation in Reflexion/LATS.

- **LeetCodeHardGym result is genuinely compelling.** Both Reflexion and LATS achieve zero performance gains over the base model on this hard benchmark, while DoT achieves 7.5% net improvement and DoT-bank adds another 2.5% (Table 6). This is a clear empirical finding that diversity-driven exploration unlocks gains precisely where existing reflection methods plateau. The simultaneous 4× cost reduction versus LATS is a meaningful Pareto improvement.

- **LATS bug discovery.** The paper identifies and corrects a bug in the official LATS implementation ("num success" incremented even for incorrect solutions) and reports both buggy and corrected numbers (Table 5). This strengthens the fairness of the comparison and provides a useful community service.

- **Evaluation across diverse model families.** Results are shown for Llama-3.1 8B/70B, GPT-3.5, GPT-4, GPT-4o, GPT-4o-mini, and Claude Sonnet 3.5 (Tables 4, 8), with larger relative gains on less powerful models. This rules out model-specific artifacts.

- **Controlled comparisons for design choices.** The paper compares one-shot vs. iterative sampling for diverse reflections (Table 11) and random vs. cosine-similarity retrieval for the memory bank (Table 10), providing useful empirical guidance within DoT's design space.

## Weaknesses

### Fatal

None.

### Major

- **Missing ablation that isolates the core mechanism.** The paper does not compare Reflexion + an explicit diversity prompt against standard Reflexion. Without this baseline, we cannot determine whether DoT's gains come from (a) the specific one-shot diverse-reflection mechanism the paper proposes, (b) simply asking the LLM to "be diverse" (a generic prompt change), or (c) having more reflection tokens per iteration. The one-shot vs. iterative comparison (Table 11) is within DoT's own design space and does not answer this question. This is the central technical claim of the paper, and it is underdetermined by the evidence.

  *Evidence in the paper:* Section 2.1 (line 51) describes M_dr as generating k diverse reflections "using an explicit prompt." Section 3.3.3 compares one-shot vs. iterative generation, but no experiment compares "Reflexion + diversity prompt" against "Reflexion" directly. The paper cites Hayati et al. (2024) that one-shot prompting can produce diverse outputs, but this further suggests the technique is known, not novel.

- **Game of 24 result is severely underspecified.** The paper claims a 13% improvement by integrating diversity into ToT (Section 3.3.4, Table 7). The description is one sentence: "This was achieved through explicit prompting and by passing previously generated thoughts through context." The exact ToT baseline accuracy, the number of trials, variance, whether ToT hyperparameters (beam width, value function) were held identical, and the actual prompts used are all absent. Given that ToT is a substantially different framework (search-tree-based with state value estimation), this key claim about modularity cannot be evaluated as reported.

  *Evidence in the paper:* Lines 308-310: "We enhanced the Tree of Thoughts (ToT) framework by incorporating diversity into the thought sampling strategy. This was achieved through explicit prompting and by passing previously generated thoughts through context."

- **"State-of-the-art" claim is not supported by the comparisons.** Line 34 states "We achieve state-of-the-art results," but the experimental comparison is limited to Reflexion and LATS. For HumanEval, many contemporary methods (various prompting strategies, code-specific models) report Pass@1 > 90%. Without situating the results against the broader code generation landscape, this claim is an overreach.

  *Evidence in the paper:* The paper compares against Base model, Reflexion, and LATS only (Tables 4, 5, 6, 8). No comparison against methods like CodeT, self-consistency baselines with diverse prompts, or other memory-augmented reasoning systems.

### Minor

- **Statistical reporting is vague for the main claims.** Line 255 states "we repeat select experiments three times and report statistically significant findings in Section 3.3.1.2.4" — but what "select" means is undefined, and the referenced section appears garbled. None of the main results tables carry confidence intervals or standard deviations (the only STD reported is in the diversity metric analysis, Table 9). Without variance information, it is impossible to assess whether the reported deltas (e.g., "up to 4% gain" for DoT-bank over DoT) are statistically meaningful.

- **No comparison against other diversity-promoting methods.** The related work discusses DIV-se and FoR, but neither is included as an experimental baseline. Since the paper's thesis centers on diversity being valuable, comparing against these methods would significantly strengthen the claims.

- **The dedicated memory-bank ablation (Table 10) would benefit from including a "no memory bank" row.** While the DoT vs. DoT-bank comparison exists in Table 4, the ablation study in Section 3.3.2 only varies the retrieval method and number of examples, without a zero-example baseline row for direct reference.

- **The paper does not discuss whether the diversity prompt might trade correctness for diversity.** If the model is explicitly prompted to generate diverse reflections, some reflections may become less accurate or relevant, potentially degrading rather than improving performance. This risk is not addressed in the limitations section.

### Trivial

- The relationship between "task-id" indexing and "docstring embedding" retrieval (lines 53, 280) could be clarified. It appears docstring embeddings are stored alongside trajectories and used for retrieval, while task-ids serve as unique keys — a brief clarification would help reproducibility.

## Nice-to-Haves

- Giving Reflexion an equivalent memory bank (same retrieval method, same number of examples) would cleanly separate the contribution of the memory mechanism from the diverse reflections that populate it.
- Reporting the exact prompts used for the diversity instruction and the Game of 24 modification would aid reproducibility.
- Discussing the risk of data contamination when the model learns from its own successful trajectories (amplifying biases, limiting generalization to OOD tasks) would strengthen the limitations section.

## Removed Points

These points were flagged by reviewers but are removed or demoted for the reasons given:

- **"Core contribution is just prompt engineering"** — Too dismissive. The paper proposes a framework integrating multiple components (one-shot diverse reflections + memory bank) with consistent empirical evaluation. The diversity mechanism is part of a larger system, not a standalone prompt tweak.
- **"Memory bank creates an uncredited advantage over baselines"** — The paper explicitly evaluates DoT *without* the memory bank as a separate condition (Table 4), so the incremental contribution of the memory bank is observable. The critic's complaint about "cannot extract numbers from images" is a formatting artifact, not a methodological flaw.
- **"Cost comparison is carefully framed"** — The paper transparently discloses that DoT is 1.4× more expensive than Reflexion. This is not a weakness.
- **"Algorithm ambiguities (garbled text)"** — The garbled text in Algorithm 1 ("1123:: GGeenneerraattee") is a parser/OCR artifact, not present in the original submission.
- **"Missing comparison against BoT" (from Strength Finder strengths about generic importance)** — The paper discusses BoT in Section 4 and explains the conceptual difference. An empirical comparison would strengthen the paper but is not a missing requirement given the paper's scope.

## Novel Insights

None beyond the paper's own contributions. The key insight — that measuring and enforcing diversity in self-reflections can unlock performance where existing methods plateau — is the paper's own contribution, and the reviews do not surface an additional novel observation.

## Suggestions

1. **Add a controlled ablation: Reflexion vs. Reflexion + diversity prompt vs. DoT (one-shot diverse)** at the same iteration budget. This is the single most important missing experiment and would isolate whether DoT's specific mechanism drives gains or simply asking for diversity suffices.
2. **Substantially expand the Game of 24 reporting** — include the base ToT accuracy, all hyperparameters, the exact prompts used, number of trials, and variance.
3. **Add confidence intervals or standard deviations to the main results tables** (Table 4, 6, 8) for at least 3 runs.
4. **Remove or qualify the "state-of-the-art" claim** — replace with language like "competitive with or better than the reflection-based baselines we compared against" unless a broader comparison is conducted.
5. **Add at least one diversity-enhancing baseline** (e.g., a temperature-sampling variant of Reflexion, or self-consistency with varied prompts) to help contextualize the improvement.

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>