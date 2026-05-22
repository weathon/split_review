Now let me write the consolidated final review.

---

## Summary

This paper challenges the dominant multi-component LoRA paradigm for multi-task learning. Through three empirical studies, the authors show that: (1) a simplified multi-head baseline (M-LoRA) with high inter-head similarity outperforms diversity-focused variants like HydraLoRA and R-LoRA, contradicting the assumption that head diversity is critical; (2) simply scaling the rank of a single standard LoRA matches or exceeds the performance of complex multi-component architectures; and (3) adding an explicit representation-alignment loss (KL divergence or MK-MMD) to a high-rank LoRA — dubbed Align-LoRA — yields further improvements while maintaining the practical advantage of zero inference overhead (mergeable weights). The paper proposes that learning task-shared representations is a more effective path than architectural separation of task-specific knowledge.

## Strengths

- **Directly challenges a prevailing assumption with concrete negative evidence.** Table 1 and Figure 2 show that M-LoRA, which removes the dynamic router and achieves the *highest* inter-head similarity (median ≈ 0.85), *outperforms* HydraLoRA and R-LoRA (75.45% vs. 74.04% and 74.67% average). This is a clean counterexample to the "diversity is necessary" premise.

- **Shows that multi-component architectures may be unnecessary via a simple control experiment.** Tables 2–3 demonstrate that a standard single-adapter LoRA with increased rank matches or exceeds all tested multi-adapter and multi-head variants (e.g., LoRA rank=10 at 49.51% vs. R-LoRA at 49.51% and HydraLoRA at 49.12% on Qwen2.5-7B/BBH). This is an elegantly simple question that directly interrogates the value of architectural complexity.

- **Align-LoRA shows consistent improvements across model families and scales.** The method is validated on LLaMA2 (7B/13B), LLaMA3-8B, and Qwen2.5 (3B/7B/14B) — six model variants across two families. A-LoRA-K achieves the highest scores on the BBH benchmark (Table 4) and on the 8-task in-domain benchmark (Table 5) while using *fewer* trainable parameters than multi-component baselines. The consistent performance of both KL-divergence and MK-MMD variants confirms that the alignment principle is metric-agnostic.

- **Practical advantage: zero inference overhead.** Unlike multi-component methods whose routers and multiple heads cannot be merged, Align-LoRA's weights are mergeable into the backbone — a concrete, deployment-relevant advantage.

- **Hyperparameter robustness.** Figure 3 shows stable gains across λ ∈ [0.01, 0.50], peaking near λ=0.10, indicating the method is not brittle to the alignment strength.

## Weaknesses

### Major

- **No statistical significance reporting anywhere in the paper.** All results (Tables 1–5) are reported from single runs without error bars, standard deviations, or confidence intervals. The improvements of Align-LoRA over LoRA are often in the range of 1–2 percentage points (e.g., 50.28% vs. 48.36% on Qwen2.5-7B BBH). Without variance estimates, the reader cannot assess whether these gains are significant or could arise from random variation. This is the single most impactful weakness in the evaluation.

- **Missing rank-matched ablation for the alignment loss.** In Tables 4 and 5, Align-LoRA (rank=8, 0.20% params) is compared against standard LoRA (rank=10, 0.25% params). A standard LoRA with rank=8 — matching Align-LoRA's parameter budget — is not included. Without this comparison, the improvement cannot be cleanly attributed to the alignment loss vs. being partially a byproduct of rank or training dynamics. The cross-table inference (Table 3 suggests LoRA^8 ≈ 46.66% on a *different* training setup, so not a substitute for a direct comparison in the same table) partially addresses but does not resolve this.

### Minor

- **The dropout mechanism in M-LoRA is asserted but not ablated.** The paper claims that multi-head dropout is the critical factor transforming heads into "collaborators" (Section 3.3), but M-LoRA without dropout is never evaluated. The evidence comes from comparing HydraLoRA "w/o Router" (which drops ~0.5 pp), but HydraLoRA lacks the multi-head dropout initialization that M-LoRA inherits from R-LoRA. This is a clean ablation that should be straightforward to run.

- **The theoretical bound (Section 5.3) provides limited added insight.** The bound is a standard multi-task/domain-adaptation bound (cf. Ben-David et al. 2006), with the distribution discrepancy term replaced by the alignment objective. It does not model the LoRA low-rank structure or PEFT dynamics specifically, so it offers conceptual motivation rather than novel theoretical machinery.

- **The narrative from M-LoRA to Align-LoRA is somewhat underspecified.** The paper argues that M-LoRA's high similarity supports a "shared representations" hypothesis, then proposes Align-LoRA as an operationalization. But M-LoRA achieves high similarity through structural simplification (removing the router), not through explicit alignment. The logical chain is plausible but the connection from "high similarity happens" to "explicitly enforcing similarity helps" is not directly validated by the M-LoRA experiments alone. (The appendix does show M-LoRA+Align improves further, which strengthens this link; this could be elevated to the main text.)

### Trivial

- None of substance.

## Nice-to-Haves

- Including a standard LoRA (parameter-matched) directly in Table 1 would strengthen the foundation of the M-LoRA analysis, though the paper's narrative structure (Section 3 focuses on multi-head variants, Section 4 introduces LoRA) is a reasonable design choice.
- A per-task performance breakdown before and after alignment (to study negative transfer) would deepen the analysis.
- Wall-clock training time comparison (beyond the FLOPs in Appendix D) would be useful for practitioners.

## Removed Points

The following points from the inputs were moved here with justifications:

- **"Missing standard LoRA baseline in Table 1" (Harsh Critic #1):** The paper's Section 3 is scoped to comparing multi-head architectures (HydraLoRA, R-LoRA, M-LoRA) to study the diversity paradox. The standard LoRA comparison is introduced in Section 4 as a separate, logically sequenced question ("is the multi-head structure itself necessary?"). This is a deliberate narrative structure, not a gap. However, including LoRA in Table 1 would marginally strengthen the paper; moved to Nice-to-Haves.
- **Criticism about the theoretical bound being "not novel":** The bound is indeed standard, but this is common practice in the field — many papers include such bounds for theoretical motivation without claiming novelty in the bound itself. The paper claims the bound as a *justification* for the method, not as a novel theoretical result. This is noted in Minor weaknesses but downgraded from the critic's framing.
- **"The ablation of HydraLoRA 'w/o Router'... the paper claims the opposite":** The critic's reading was confused — the paper correctly reports that performance drops (74.04 → 73.58) and says "causes its average performance to drop." The critic's remaining point about missing M-LoRA w/o dropout ablation is valid and retained in Minor weaknesses.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Add statistical rigor.** Run all main experiments (at least Tables 1, 4, 5) with 3–5 seeds and report means ± standard deviations. This is essential for a paper whose improvements are in the 1–3 pp range.
2. **Include LoRA^8 in Tables 4 and 5** to provide a clean, budget-matched ablation for the alignment loss. This single addition would substantially strengthen the central claim.
3. **Add M-LoRA without dropout to Table 1** to directly confirm the mechanism story.
4. **Elevate the M-LoRA+Align experiment (Appendix I) to the main text** to tighten the narrative arc from M-LoRA to explicit alignment.

## Score and Decision

**Round 1 bracket:** [4.5, 6.5]. The paper is clearly stronger than the weak-band anchors (UnoLoRA [3.0], ALLoRA [3.33], DLP-LoRA [3.0], MORE [4.0]) which were rejected for limited novelty, poor evaluation, or very restricted experimental scope. It is clearly weaker than the strong-band anchors (HiRA [8.0], Partial Linearization [7.0]) which have more thorough evaluation and cleaner ablations.

**Round 2 narrowing:** Compared against PaLoRA (avg 5.5, accepted) — the paper under review has a stronger central thesis (directly challenging an established paradigm rather than proposing an incremental method on top of it) and broader empirical validation (6 model scales vs. 2), but shares similar gaps in statistical reporting. Compared against C-Poly (avg 6.0, accepted) — the paper under review has a more provocative finding but somewhat less thorough ablation analyses. Compared against Seeded LoRA (avg 5.0, rejected) — the paper under review has a stronger, more grounded thesis and more comprehensive experiments.

**Final calibration anchors consulted:** UnoLoRA (3.0, Reject), DLP-LoRA (3.0, Reject), ALLoRA (3.33, Reject), MORE (4.0, Reject), LoraHub (5.33, Reject), PaLoRA (5.5, Accept), C-Poly (6.0, Accept), Partial Linearization (7.0, Accept), HiRA (8.0, Accept), Seeded LoRA (5.0, Reject).

The paper makes a genuine contribution by empirically challenging a prevailing assumption in multi-task PEFT and proposing a simple, effective alternative. The experiments are broad in scope (6 models, 2 families, multiple tasks/benchmarks) and the results consistently support the central thesis. However, the evaluation lacks statistical rigor (no multiple seeds, no error bars) and one key ablation (rank-matched LoRA baseline for Align-LoRA) is missing, which weakens the attribution of improvements to the proposed mechanism. These issues are addressable in revision but currently prevent the paper from being a strong accept.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>