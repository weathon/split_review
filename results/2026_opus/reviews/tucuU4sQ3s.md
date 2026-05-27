Now let me write the consolidated review.

## Summary
NuSA-CL proposes a memory-free continual learning framework for CLIP-style vision-language models. For each task it computes the SVD of the current weight matrix, identifies a low-energy ("approximate null") subspace via a 95% spectral-energy cutoff, learns a LoRA-style update ΔW = U_n M V_n^⊤ strictly confined to that subspace, then merges ΔW back into the backbone. Evaluated on MTIL (full-shot and 5-shot) and Class-Incremental CIFAR-100 (10/20/50 steps), it claims the best efficiency-performance trade-off among storage-free PEFT methods while approaching storage-based SOTA at a fraction of the cost.

## Strengths
- **Strong efficiency/performance trade-off in the storage-free regime.** Table 1 shows NuSA-CL hits Transfer 68.6 / Avg 75.1 / Last 82.8 on full-shot MTIL with 1.5M params and 1.21 GPU-hours, outperforming storage-free LoRA (63.9/70.1/79.9) and MiLoRA (62.8/68.7/77.4) by 4-7 points on Transfer while matching or approaching the storage-based MoE-Adapters (68.9/76.7/85.0) with ~40× fewer trainable parameters and ~3× less wall-clock time. This is a concrete and substantial efficiency claim.
- **Scalability on long task sequences.** On 50-step CIFAR-100 (Table 3), NuSA-CL reaches Last 71.85 vs. the strongest baseline ZSCL at 67.36, a 4.5-point margin against a full-fine-tuning competitor, and the gap widens as sequence length grows (10/20/50 steps).
- **Ablation directly supports the central design choice.** Figure 3a shows the "Tail" (null-like) subspace yields the lowest forgetting across all tested ranks (e.g., 2.57% vs. 4.44% Top and 4.57% Random at r=128), and Table 4a shows that unfreezing U_n, V_n collapses Transfer from 68.58 → 62.60, supporting the "persistent constraint" framing.
- **Honest treatment of the theory's limits.** The closing paragraph of Sec. 4.2 explicitly states the bound is "in parameter space and should be viewed as a local stability condition rather than a full function-level guarantee" — the paper does not pretend Lemma 1 is more than it is.
- **Hyperparameter robustness and cheap initialization.** Table 4b reports <0.5% variation in Avg across ρ ∈ {0.80, 0.90, 0.95, 0.99} and an SVD initialization cost of <1 min vs. ~81 min for InflLoRA's data-dependent gradient-projection bank.

## Weaknesses

### Fatal
None.

### Major
- **Long-sequence comparison set in Table 3 omits the PEFT-CL competitors used elsewhere.** The CIFAR-100 10/20/50-step table — the experiment the paper relies on for its "long-sequence scalability" claim (Sec. 5.2) — is run only against LwF, iCaRL, LwF-VR, Continual-FT, and ZSCL. The natural competitor class for NuSA-CL (MoE-Adapters, DIKI, MiLoRA, InflLoRA) appears in Table 1 but is absent here. As written, the 4.4-point gap on 50-step CIFAR demonstrates dominance over full-fine-tuning baselines, not scalability against the PEFT-CL methods the paper positions itself against. Adding even one or two of these baselines would substantially strengthen the scalability conclusion.
- **The theoretical "interference bound" is genuinely parameter-space and does not bound functional forgetting.** Lemma 1 gives |⟨W, ΔW⟩_F| ≤ σ_{k+1}·‖M‖_F. σ_{k+1} is the *largest* singular value still inside the chosen subspace (the one just below the ρ-cutoff), not a small quantity, and ‖M‖_F grows during training. The paper acknowledges this honestly in the last paragraph of Sec. 4.2, but the abstract ("minimizes interference"), Sec. 3.2 ("mathematically guaranteed to be orthogonal"), and Sec. 4.2 ("principled mechanism for mitigating catastrophic forgetting") nonetheless frame the bound as load-bearing. The paper would be stronger if Sec. 4 either supplied a functional-output bound (e.g., empirically measured ‖ΔW·x‖ on prior-task feature distributions) or downgraded its language to "motivating sketch."

### Minor
- **Transfer score above zero-shot CLIP is not interpreted.** Table 2 reports NuSA-CL Transfer 68.1 on the 5-shot benchmark vs. zero-shot CLIP 65.3 (and full-shot Table 1 shows 68.6 vs. 65.3), i.e., training a strictly low-energy update on 10 prior tasks *improves* zero-shot accuracy on unseen tasks. This is a non-trivial and somewhat surprising result for a method whose narrative is "preservation, not improvement"; the paper treats it as unambiguous endorsement rather than unpacking the (plausible) positive-forward-transfer story.
- **The 5-shot margin over the strongest competitor is modest and rests on a re-implementation.** NuSA-CL beats †-InflLoRA by ~1.3 Transfer, ~1.4 Avg, and ~0.6 Last on the 5-shot MTIL benchmark (Table 2). The numbers are real but small, and †-InflLoRA is the authors' own port of InflLoRA to CLIP. The text describes this as "decisively outperforming InflLoRA," which is stronger than a 0.6–1.4 point gap on a single seed supports. No seed/variance information is provided.
- **The "effective rank rises from 57.9% → 58.8%" evidence (Fig. 2, Sec. 6.1) is presented more emphatically than the magnitudes warrant.** A ~1% shift in effective rank over 10 tasks is empirically real and consistent with the additive-knowledge story, but calling it "dynamically reshaping the parameter space" overreads the size of the effect.
- **The principal subspace recomputed each task can drift across the sequence.** Sec. 3.3 has W_t = U_p Σ_p V_p^⊤ + U_n(Σ_n + M)V_n^⊤, and the next SVD will not in general yield the same principal/null bases as the algebraic concatenation. The "core knowledge preservation" narrative would benefit from a sentence quantifying how much principal-subspace drift accumulates and whether it tracks ‖M‖.

### Trivial
- The "Train M & V_n" row in Table 4a freezes the column-space basis U_n but trains V_n; framing this as evidence of the "persistent constraint being critical" mixes the row-basis-freeze effect with the column-space restriction itself. A row-only vs. column-only freeze would be more diagnostic but is not essential.
- The SVD-efficiency line in Table 4b compares weight-only SVD (<1 min) against InflLoRA's data-dependent gradient-projection bank construction (~81 min). The 81× speedup is real but compares fundamentally different operations; a clarifying sentence about what each timing includes would make the comparison more informative than headline-flattering.

## Nice-to-Haves
- Repeat Table 3 with MoE-Adapters, DIKI, MiLoRA, and InflLoRA — the experiment that would convert "competitive on long sequences" into "competitive against the right class of long-sequence methods."
- Add an analysis quantifying how much of the optimal full-rank task update projects onto the bottom-rank subspace, which would directly address the central plasticity-vs.-stability tension surfaced in Sec. 6.2.
- Report multi-seed variance, especially for the 5-shot MTIL table where several wins are within 1–2 points.
- Replace or augment Lemma 1 with an output-space quantity such as empirical ‖ΔW · x‖ on cached prior-task features.

## Removed Points
These points are flagged to be removed — treat them with caution.

- *Strength: "Theoretical interference bound shows principled forgetting mitigation."* — Removed because the paper itself walks this back in Sec. 4.2; the strength is in tension with a verified weakness.
- *Weakness: "naive fine-tuning destroys >20 points of zero-shot ability ... is Continual-FT a deliberately weak baseline?"* — This is a calibration concern, not a specific identified problem, and the Continual-FT recipe matches prior CLIP-CL literature.
- *Weakness: Lemma 1 implicitly assumes U_n, V_n are exact SVD bases of the current W in the continual setting* — Demoted into the principal-subspace-drift Minor point; raising it as a separate "fatal" theoretical issue would double-count.
- *Strength: "important problem" / "interesting research question"* — Generic; removed.

## Novel Insights
None beyond the paper's own contributions. The Sec. 6.2 ablation honestly surfaces the stability–plasticity trade-off across both subspace choice and rank dimension, which is a useful contribution to interpret SVD-guided PEFT-CL methods, but the broader insight (low-energy subspace ⇒ low forgetting, sufficient capacity ⇒ task adaptation) is recognizable from MiLoRA and InflLoRA. The paper does add the persistent-constraint variant and the merge-and-recompute cycle, which is the cleanest articulation of those design choices we have in the storage-free PEFT-CL setting.

## Suggestions
- Run Table 3 with the missing PEFT-CL baselines (MoE-Adapters, DIKI, MiLoRA, InflLoRA at minimum) so the long-sequence claim is supported against the competitor class the paper positions itself against.
- Either (a) supplement Sec. 4 with an output-space measurement (e.g., ‖ΔW·x‖ on prior-task features) or (b) explicitly relabel Sec. 4 as "Theoretical Motivation" rather than "principled mechanism," and reword the abstract/Sec. 3.2 to match the disclaimers in Sec. 4.2.
- Add a paragraph explaining why a strictly low-energy update produces *better-than-zero-shot* Transfer; the most plausible (positive forward transfer between visually-related MTIL datasets) is in scope and would strengthen rather than weaken the paper's narrative.
- Report seed variance for at least the 5-shot MTIL table, where several wins are within the noise of typical CL re-runs.

## Evaluation
- *Originality:* Moderate. SVD-guided low-rank adaptation is a known idea (MiLoRA, InflLoRA, PiSSA); the novelty is the persistent constraint + recompute-and-merge cycle and adapting it specifically to the CLIP MTIL setting. Clean execution of a known idea rather than a conceptual jump.
- *Importance:* The storage-free, fixed-budget continual learning regime is well-motivated for VLM deployment, and the paper targets a recognized scalability concern.
- *Claim support:* Mostly solid. The headline efficiency claim is well-supported in Table 1. The long-sequence scalability claim is weaker because the competitor set in Table 3 is misaligned with the rest of the paper. The "minimizes interference" framing in the abstract is stronger than the parameter-space theory delivers.
- *Soundness of experiments:* MTIL full-shot and 5-shot, plus 10/20/50-step CIFAR, with consistent ablations on subspace choice, rank, energy cutoff, and modality. No seed variance, no PEFT-CL competitor in Table 3.
- *Clarity:* Good. The three-stage method (identify → constrain → merge) is well presented; Figures 2–3 are interpretable.
- *Value to community:* A practical, well-engineered storage-free PEFT-CL method with strong efficiency numbers and a useful ablation set. Below borderline acceptance in current form mainly because of the Table 3 competitor gap and the over-strong framing around the theoretical bound.

## Score and Decision

**Anchors retrieved:**

Round 1 (bracketing):
- `WM5G2NWSYC.md` (avg 2.00, Reject) — "Projected Subnetworks Scale Adaptation": parameter-projection meta-learning for CL; weak weak anchor — NuSA-CL is dramatically stronger empirically and conceptually.
- `JIlIYIHMuv.md` (avg 2.50, Reject) — LVLM-CL: weak anchor; NuSA-CL is much stronger.
- `gNoqEdT2wO.md` (avg 2.33, Reject) — Multimodal Class-Incremental Learning benchmark; benchmark paper, not directly comparable.
- `ZaudLwn0Hm.md` (avg 2.50, Reject) — Prototypical evolution for few-shot VLM; weak anchor.
- `sb7qHFYwBc.md` (avg 6.50, Accept) — **C-CLIP**: LoRA + contrastive distillation for CLIP CL. Closest analog. Comparable empirical scope; NuSA-CL has tighter theoretical framing and broader ablations, but C-CLIP introduces a benchmark and shows larger relative gains over baselines.
- `G9Ea7mlqGO.md` (avg 3.80, Reject) — Online CL with CLIP; weaker.
- `TLADT8Wrhn.md` (avg 6.25, Accept) — TiC-CLIP: large-scale benchmark for time-continual CLIP; different scope (benchmark + training recipe).
- `9aZ2ixiYGd.md` (avg 5.00, Accept) — Vision-language synergy for rehearsal-free CL; prompt-based, accepted with split scores.
- `1aF2D2CPHi.md` (avg 8.00, Accept) — Data-free distillation for CLIP customization; different topic.
- `3i13Gev2hV.md` (avg 8.00, Accept) — Hyperbolic VLM; out of scope.
- `gc8QAQfXv6.md` (avg 9.00, Accept) — Function vectors for CF in instruction tuning; stronger than NuSA-CL.
- `uAFHCZRmXk.md` (avg 8.00, Accept) — Modality gap in VLMs; out of scope.

**Round-1 bracket:** between 5 and 7. NuSA-CL is clearly stronger than the <3.5 anchors and clearly weaker than the 8+ anchors.

Round 2 (narrowing):
- `k9NYnsC4Mq.md` (avg 5.67, Reject) — **PROOF**: VLM CIL with frozen projections + fusion. Comparable scope. Reviewers flagged inference-mismatch and limited ablation. NuSA-CL has cleaner method, stronger efficiency story, slightly better ablations; comparable empirical strength.
- `rwmwFnmjAX.md` (avg 4.75, Reject) — Continual LLaVA; different setting.
- `G9qA1JZ0Sy.md` (avg 5.33, Reject) — LLaCA EMA-based MLLM CL; weaker comparable.
- `u3dHl287oB.md` (avg 5.67, Accept) — Analytical model for forgetting; different scope (theory paper).
- `Ll8PmgD0IB.md` (avg 6.00, Reject) — **Divide and Orthogonalize (LMSP)**: closest methodological analog (orthogonal-projection CL with theoretical analysis). Reviewers split 5/8/6/5. NuSA-CL has stronger empirical claims (VLM-scale, MTIL benchmark, efficiency numbers) than LMSP's smaller-scale CL benchmarks; somewhat comparable in theoretical depth.
- `DTqx3iqjkz.md` (avg 6.25, Accept) — Convergence of GD on continual linear classification; theory paper, different scope.
- `nAs4LdaP9Y.md` (avg 6.33, Accept) — Federated orthogonal training; comparable methodological lineage in a different setting.
- `ScI7IlKGdI.md` (avg 6.33, Accept) — Spurious forgetting in LM CL; different scope.
- `NIkfix2eDQ.md` (avg 6.20, Accept) — Deep Fourier features for plasticity; different scope.
- `Pin2kdWloe.md` (avg 5.75, Reject) — Multitask vs. CL; theory paper.
- `Hcb2cgPbMg.md` (avg 6.25, Accept) — Spectral regularization for CL; comparable methodological framing (spectrum-based CL), slightly more theoretical depth.

**Comparison verdict:** NuSA-CL is roughly comparable to PROOF (5.67, reject) and Divide and Orthogonalize (6.00, reject) — both have similar scopes and were rejected with mid scores. It is slightly weaker than C-CLIP (6.50, accept) because C-CLIP introduces both a benchmark and a method, and slightly weaker than Spectral Regularization (6.25, accept) which has a sharper theoretical contribution. The Table 3 competitor gap and the framing-vs.-theory mismatch on Lemma 1 keep it below the C-CLIP/Spectral Regularization tier; the strong efficiency numbers and clean ablations keep it above the LLaCA / Continual-LLaVA / G9Ea7mlqGO tier.

Calibrated final placement: ~5.5. Closer to the PROOF / LMSP cluster (5.67 / 6.00) than to C-CLIP (6.5) because the long-sequence comparison is misaligned with the rest of the paper and the theoretical framing outruns what Sec. 4 delivers.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>