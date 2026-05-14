## Summary

PLAGUE is a modular framework for multi-turn LLM jailbreak attacks that decomposes the attack into three phases: Planner (generates a plan and retrieves successful past strategies from memory), Primer (builds adversarial context across turns with backtracking and reflection), and Finisher (delivers the final harmful query). The framework is plug-and-play, allowing components from existing attacks (GOAT, Crescendo, ActorBreaker) to be swapped in. Evaluated on frontier models including OpenAI o3, Claude Opus 4.1, and DeepSeek-R1, PLAGUE achieves strong attack success rates—81.4% SRE on o3 and 67.3% on Opus 4.1—with controlled query budgets and comprehensive ablations.

## Strengths

- **Modular three-phase architecture with validated component contributions.** The Planner→Primer→Finisher decomposition is clearly motivated (Section 3) and ablations in Table 3 show incremental gains from each component: backtracking, reflection, planning, and retrieval, cumulatively raising SRE on o3 from 0.587 (base GOAT) to 0.814.

- **Strong empirical results on genuinely frontier models.** PLAGUE achieves 81.4% SRE on OpenAI o3 and 67.3% SRE on Claude Opus 4.1 (Table 2, Table 4), representing 32% and 40% relative improvements over the previous best baselines. Results span five leading models with both SRE and binary-ASR metrics.

- **Plug-and-play modularity convincingly demonstrated.** Switching the Finisher from GOAT to Crescendo for Opus 4.1 lifts SRE from 0.465 to 0.673 (Table 4), and integrating ActorBreaker's planner improves diversity by ~15% with negligible ASR loss (Figure 3). This directly validates the claimed flexibility.

- **Comprehensive ablation reveals model-dependent vulnerability patterns.** Table 3 shows that for o3 the largest gain comes from reflection (+0.149 SRE), while for Opus 4.1 backtracking is critical (+0.174 SRE). This is an actionable insight for understanding different models' safety weaknesses.

- **Efficiency maintained despite added components.** Table 5 shows PLAGUE's total LLM calls are comparable to Crescendo and within one turn of GOAT, despite the extra Planner phase. The attack scales linearly with turns before plateauing at six (Figure 2).

## Weaknesses

### Fatal

None.

### Major

- **"Lifelong learning" claim is not substantiated.** The paper repeatedly describes PLAGUE as a "lifelong-learning" framework (title, abstract, Section 2.3, Section 3.3.1) and claims strategies "can be retrieved as references during future attacks" enabling the agent to "evolve and improve" (line 414-415). However, the only evidence provided is a static comparison: adding retrieval (RSS) raises ASR in Table 3. No learning curve analysis is presented—e.g., ASR as a function of goals processed, or a comparison of a memory-free agent vs. one with growing memory across a sequence of goals. The memory bank is initialized with two static examples (line 319), and there is no demonstration that performance improves as strategies accumulate across a run. The "lifelong learning" label is an overclaim relative to what is actually shown.

- **Attacker model for baselines is not explicitly documented.** The paper states DeepSeek-R1 is the "primary Attacker model across all our experiments" (line 432), but the Baselines subsection (lines 465-489) never confirms that GOAT, Crescendo, ActorBreaker, and AutoDAN-Turbo were each run with DeepSeek-R1 as their attacker LLM. Since attack success depends on attacker model capability, this ambiguity weakens confidence in the headline comparison in Table 2. While it is plausible (and likely) that the same attacker was used throughout, the paper must state this explicitly.

### Minor

- **ASR@2 protocol clarity.** The paper uses ASR@2 (selecting the best of two runs; line 458-462) and states K=2 for all experiments. However, the description for baselines varies: GOAT is described as stopping early "if a high rubric score is obtained in early iterations" (line 471), which is an intra-run efficiency measure, not an independent-run protocol. ActorBreaker's K=2 is tied to its actor count (line 474-476). While the paper likely applied ASR@2 equitably, the documentation does not make the per-baseline protocol explicit enough for the reader to independently verify equivalence.

- **Score threshold discrepancy.** Section 3.5 (line 397) states the Finisher marks success when the rubric score exceeds 8/10, but Algorithm 3 (Appendix A.1, line 1045) checks `score > 9.0`. These thresholds are inconsistent and should be reconciled.

- **Evaluator model differs from standard StrongReject.** The paper uses Qwen3-235B-A22B-fp8 as the evaluator (line 432) rather than the GPT-4-based judge used in the original StrongReject work (Souly et al., 2024). No validation or justification is provided for this substitution. While Qwen3-235B is a capable model, the paper would benefit from a brief comparison or at minimum an explicit acknowledgment of the change.

### Trivial

- Table 2 duplicates the ActorBreaker row.

## Nice-to-Haves

- A learning-curve analysis showing ASR as a function of accumulated memory bank size would substantiate the lifelong-learning framing.
- Explicit per-baseline documentation of the attacker LLM used.
- A sensitivity analysis varying the attack budget would strengthen efficiency claims.
- More qualitative examples of attack trajectories (beyond the single example in Appendix D), including failure cases, would help readers understand PLAGUE's behavior patterns.

## Removed Points

These points from the input reviews were considered but removed:

1. **"Attacker model for baselines is not specified — this invalidates the entire comparison" (Harsh Critic, Issue 1).** *Downgraded to Major, not Fatal.* The paper does state DeepSeek-R1 is used "across all our experiments," and there is no positive evidence of asymmetry. This is a documentation gap, not a proven methodological flaw. The comparison is plausible and the concern is addressable in a rebuttal.

2. **"ASR@2 may not be equitably applied to baselines" as a fatal evidential flaw (Harsh Critic, Issue 2).** *Removed as Fatal, kept as Minor.* The paper explicitly states K=2 for all experiments. The concern about single-rollout for GOAT conflates intra-run early stopping with inter-run independent attempts. There is no evidence the protocol was applied asymmetrically; the paper just needs to be clearer.

3. **"The claim that PLAGUE is the first multi-turn attack to feature a lifelong-learning component may ignore AutoRedTeamer."** *Removed.* AutoRedTeamer (Zhou et al., 2025) is cited in the paper and acknowledged as using "lifelong attack integration." Whether PLAGUE is "first" is a minor priority dispute that does not affect the paper's technical contribution.

4. **"The Primer phase mirrors mechanisms already present in Crescendo and GOAT; no ablation isolates the Planner from the Primer."** *Removed.* Table 3 does isolate the Planner (GOAT+BT+R vs. GOAT+BT+R+P), showing a +0.012 SRE gain on o3 and +0.029 on Opus 4.1. The contribution is incremental but measured.

5. **"Removing backtracking counts from Crescendo and disabling history in GOAT may handicap baselines."** *Removed.* The paper provides justification (line 469-471): "Through extensive ablation, we also observe that the impact on GOAT's performance with and without an attack history is negligible." This is a reasonable justification given the goal of controlled comparison.

6. **"The rubric scorer reliability relative to StrongReject's GPT-4-based judge is not addressed" (Harsh Critic).** *Kept as Minor, not removed.* This is a legitimate point but is weakened since Qwen3-235B is a strong model and the paper uses the same evaluator for all methods, so the relative comparison is preserved. Kept as minor for documentation completeness.

7. **All formatting, typo, and presentation nitpicks from the Harsh Critic.** *Removed per hard rules.*

8. **"The abstract overstates the contribution" / "overclaims impact."** *Removed as generic.* These are judgment calls, not specific, verifiable weaknesses. The verified "lifelong learning" overclaim is captured in the Major weakness above.

9. **Strength Finder claims about "state-of-the-art" and "novel framework" that are purely evaluative.** *Kept only the evidence-backed versions.* Generic claims like "this is important" are not included as standalone strengths.

## Novel Insights

None beyond the paper's own contributions. The reviews did not surface a synthesis or perspective that the paper itself does not already articulate.

## Suggestions

- Replace "lifelong learning" with more accurate terminology (e.g., "retrieval-augmented memory" or "experience replay") throughout the paper, or add a learning-curve experiment showing ASR improvement as the memory bank grows.
- Add one sentence in the Baselines subsection explicitly confirming the attacker LLM used for each baseline (e.g., "All baselines use DeepSeek-R1 as the attacker LLM").
- Clarify the ASR@2 protocol for each baseline: how many independent full attack runs were performed, and how the best run was selected.
- Fix the score threshold discrepancy between Section 3.5 (8/10) and Algorithm 3 (>9.0).
- Add a brief note justifying the use of Qwen3 as StrongReject evaluator instead of GPT-4, or validate with a small correlation study.

## Score and Decision

**Anchor comparison:**

| Anchor | Avg Score | Decision | Comparison to PLAGUE |
|--------|-----------|----------|---------------------|
| SEMA (`6eSNG1VNkl.md`) | 5.00 | Accept (Poster) | SEMA evaluates weaker models, uses RL for attack generation. PLAGUE has broader frontier-model evaluation and more baselines, but shares the pattern of strong results + some documentation gaps. |
| GRAF (`f9BuANYtJf.md`) | 4.40 | Reject | GRAF had a fundamental methodological flaw (fabricating target responses). PLAGUE has no comparable fatal flaw. |
| CoaxChain (`6yCZEruFu9.md`) | 3.50 | Reject | Weaker baselines, less comprehensive evaluation, AFA generalizability concerns. PLAGUE is substantially stronger. |
| Morpheus (`11z2ZV85eV.md`) | 5.00 | Reject | Both have strong empirical results and agent-based designs. Morpheus was critiqued for limited novelty (primarily prompt engineering) and small evaluation set (50 behaviors). PLAGUE uses full HarmBench (200 samples) with broader model coverage but has the "lifelong learning" overclaim. Comparable quality. |
| ADJ (`ilnKzaQSCh.md`) | 5.50 | Accept (Poster) | ADJ has strong theoretical contributions (game theory, convergence proofs) but significant practical efficiency concerns. PLAGUE lacks theory but has stronger empirical validation and practical deployability. |
| "Attacker Moves Second" (`7B9mTg7z25.md`) | 6.00 | Reject | Strong paper on adaptive attack evaluation methodology, higher-quality contribution. PLAGUE is a tier below in terms of conceptual depth. |

PLAGUE sits between GRAF (4.40, rejected for fatal flaw) and ADJ (5.50, accepted poster with theoretical depth). It has no fatal methodological flaw, evaluates on frontier models with strong results, and provides useful modularity—but the "lifelong learning" overclaim and documentation gaps prevent it from being clearly above the 5.0 tier. **Score: 5.0.**

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>