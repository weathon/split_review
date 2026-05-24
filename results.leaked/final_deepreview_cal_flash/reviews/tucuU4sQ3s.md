Now I have a thorough understanding of the paper. Let me write the final consolidated review.

## Summary

This paper proposes NuSA-CL, a memory-free continual learning framework for vision-language models (VLMs) that constrains low-rank weight updates to the approximate null space of the model's weight matrices. The method operates in a three-step cycle: SVD-based null space identification from the current weights, constrained adaptation within this null space via a trainable intermediate matrix M, and weight merging to maintain a fixed parameter budget. On the 11-task MTIL benchmark, NuSA-CL achieves 75.1% Avg accuracy / 82.8% Last accuracy using only 1.5M trainable parameters and 1.21 GPU hours, outperforming all other storage-free methods and rivaling storage-based approaches at a fraction of their cost. Ablation studies and spectral dynamics analysis provide empirical support for the method's design choices.

## Strengths

1. **Clean, novel, and well-motivated method.** The idea of deriving a null space from the weight matrix's own SVD (rather than from past data or gradients) and persistently constraining updates to it is a genuinely new approach in CL for VLMs. The three-step cycle (identify → constrain → merge) is clearly described and diagrammed. The distinction from prior SVD-guided PEFT methods (MiLoRA uses the low-energy subspace only for initialization; NuSA-CL enforces a persistent constraint throughout training) is clearly articulated in Section 2.3 and empirically validated in Table 4a.

2. **Exceptional efficiency–performance trade-off.** Table 1 shows that NuSA-CL uses 40× fewer parameters than MoE-Adapters (1.5M vs. 59.8M), zero additional storage, <2× less peak GPU memory (6.6 vs. 15.5 GB), and ~3× faster training (1.21 vs. 3.42 GPU-hours), while matching or approaching its performance (Transfer 68.6 vs. 68.9, Avg 75.1 vs. 76.7, Last 82.8 vs. 85.0). Against ZSCL (full FT), the savings are even more dramatic: 1.21 vs. 47.24 GPU-hours. This is a genuinely practical result.

3. **Strong empirical validation with decisive ablations.** (a) The subspace selection ablation (Fig. 3a) shows that *Tail* (null-like) directions yield consistently lower forgetting than *Top* or *Random* across all tested ranks — direct evidence for the core hypothesis. (b) The persistent constraint ablation (Table 4a) shows that unfreezing Uₙ, Vₙ drops Transfer from 68.58% to 62.60%, confirming that strict confinement to the null space is essential. (c) Robustness to the energy threshold ρ (Table 4b) is demonstrated over a wide range (0.80–0.999).

4. **Insightful spectral dynamics analysis.** Figure 2 provides direct empirical evidence that NuSA-CL accumulates knowledge by increasing effective rank across tasks (vision encoder: ~51.8% → ~52.4%), whereas LoRA and Full-FT remain static. The analysis of null-space exhaustion (Appendix Table 11 shows ~314 null directions remain in the most saturated layer after 10 tasks, >2× the update rank of 128) credibly addresses the concern about long-term capacity.

5. **Scalability on long task sequences.** On the 50-step CIFAR-100 benchmark (Table 3), NuSA-CL achieves 71.85% Last accuracy — a 4.4 pp improvement over ZSCL (67.36%) — and the advantage grows with sequence length (+1.0% at 10 steps → +4.4% at 50 steps). This directly supports the claim of lifelong scalability.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Transfer metric definition lacks explicit temporal context.** The paper defines Transfer as "the zero-shot accuracy on unseen tasks" (Section 5.1). While this is standard CL terminology (forward transfer on tasks not yet trained on in the sequence), the phrase "unseen tasks" could be misinterpreted as referring to tasks permanently held out from the training sequence. Table 2 reports per-dataset Transfer values for datasets that are in the training sequence (e.g., DTD, EuroSAT). Explicitly stating that Transfer measures forward transfer (accuracy on task t evaluated before training on it) and specifying the averaging protocol would eliminate any ambiguity. The definition given is sufficient for the CL community, but it could be tightened for broader readership.

2. **The theoretical link between the null-space constraint and forgetting is claimed in parameter space, not function space.** Lemma 1 and Theorem 2 bound parameter-space interference (⟨W, ΔW⟩_F). The paper correctly acknowledges (Section 4.2) that this is "a local stability condition rather than a full function-level guarantee" and that function-level bounds would require smoothness assumptions. However, the motivation sections (Abstract, Introduction) frame this as "minimizing interference" and "preserving zero-shot capabilities" — these are functional claims. The gap between the parameter-space bound and the actual forgetting phenomenon is acknowledged but not experimentally bridged. A direct correlation plot between ‖⟨W_{t-1}, ΔW_t⟩_F‖ and per-task accuracy drop would strengthen the causal link.

3. **The rank used for LoRA/MiLoRA baselines is not specified in the main text.** The paper states that "LoRA-based methods [were re-implemented] within a unified framework, applying adapters to both vision and text encoders with a consistent rank" (Section 5.1), but does not state what that rank is. Since NuSA-CL uses an effective rank of up to 128 (via r_max=128), it is important to know whether the LoRA baselines use a comparable rank or a lower one, as this directly affects the parameter count and expressivity of the comparison.

4. **No comparison with prompt-based continual learning methods.** The paper's scope ("storage-free," "fixed backbone parameter budget") excludes prompt-based methods (L2P, DualPrompt, CODA-Prompt, etc.) that require a growing prompt pool. This is a defensible scope choice, but it means the paper does not demonstrate competitiveness against one of the most active lines of CL research for ViTs/VLMs. A comparison under a strictly matched resource constraint (e.g., a shared prompt pool budgeted to match NuSA-CL's 1.5M parameters) would substantiate the broader performance claims.

### Trivial

1. **No task-order sensitivity analysis.** The MTIL benchmark is evaluated in a single fixed order. While the paper acknowledges this as future work (Section 7), evaluating 2–3 random orders is standard practice in CL and would strengthen the empirical claims, particularly for the spectral dynamics analysis.

2. **No error bars or statistical significance.** Results are reported as point estimates without standard deviations or confidence intervals. While single-run evaluation is common in large-scale CL benchmarks, this is worth noting for completeness.

## Nice-to-Haves

- Providing an empirical bridge between parameter-space interference and actual per-task forgetting (e.g., a scatter plot of ‖⟨W_{t-1}, ΔW_t⟩_F‖ vs. accuracy drop per task).
- Evaluating on a genuinely held-out zero-shot dataset (e.g., ImageNet) after the full MTIL sequence to directly verify the claim of zero-shot preservation.
- A table in the main text specifying the LoRA rank and other hyperparameter details for each baseline method.

## Removed Points

These points were raised by the reviewers but are removed or demoted for the reasons given:

- **"The Transfer metric makes the paper's central claim unverifiable"** (Harsh Critic, Critical Issue 1). Removed as overstatement. The definition "zero-shot accuracy on unseen tasks" in the context of a task-incremental benchmark is standard CL terminology. It refers to forward transfer — accuracy on a task before it is trained on. The MTIL benchmark was introduced by ZSCL (Zheng et al., 2023) and the same metric definition is used there. The ambiguity is minor, not evidential.
- **"The theoretical disconnect is a high-severity methodological gap"** (Harsh Critic, Critical Issue 2). Demoted to minor/acknowledged. The paper explicitly says (Section 4.2) that the results "should be viewed as a local stability condition rather than a full function-level guarantee" and "Deriving tighter, function-level forgetting bounds remains an interesting direction for future work." This is transparent scoping of a known limitation, not a flaw in the method.
- **"Missing prompt baselines is a critical fairness issue"** (Harsh Critic, Critical Issue 3). Removed as scope-mismatch. The paper explicitly targets methods that are "storage-free" with a "fixed backbone parameter budget." Prompt-based methods (L2P, DualPrompt, etc.) grow their prompt pool with tasks, violating both constraints. While a matched-resource comparison would be informative, the lack of one is not a flaw in a paper that clearly defines its scope.

## Novel Insights

The paper's spectral dynamics analysis (Figure 2) and the subspace selection ablation (Figure 3a) together form a genuinely insightful empirical contribution beyond what was strictly necessary to validate the method. Showing that NuSA-CL's effective rank *increases* across tasks (while conventional methods remain static) provides direct evidence for an *additive* learning dynamic rather than the overwriting behavior typical of fine-tuning. The subspace selection study — showing that the low-energy tail subspace consistently yields less forgetting than top or random subspaces across multiple rank budgets — cleanly isolates the null-space hypothesis. These analyses elevate the paper beyond a simple method-proposal.

## Suggestions

- Clarify the Transfer metric: add one sentence explicitly stating that it measures forward transfer (accuracy on the next task evaluated before training on it, averaged over all tasks in the sequence).
- Report the specific LoRA rank used for the re-implemented baselines (LoRA, MiLoRA) in the main text or in Table 1.
- Add a held-out zero-shot evaluation (e.g., ImageNet or a standard ZS benchmark) after the full MTIL training sequence to directly verify the zero-shot preservation claim.
- Consider including a comparison with prompt-based CL methods under a matched resource constraint (e.g., a shared prompt pool with total parameter budget ≤ 1.5M).
- Include task-order randomization over at least 2–3 seeds to assess robustness of the spectral dynamics findings.

## Score and Decision

Based on the calibration analysis:

**Round 1 (Bracketing):** Searched for CL VLM papers with null-space / orthogonal-projection concepts across three score bands. Weak anchors (avg ≤3.5): LVLM-CL (2.50), Projected Subnetworks (2.00), Multimodal CIL benchmark (2.33). Middle anchors (3.5–7.5): C-CLIP (6.50, Accept), TiC-CLIP (6.25, Accept), PROOF (5.67, Reject). Strong anchors (≥7.5): Compositional Entailment Learning (8.00), Two Effects One Trigger (8.00), Unlocking Function Vectors (9.00). Initial bracket: **5.5–7.0**.

**Round 2 (Narrowing):** Searched for CL null-space / orthogonal and memory-free CLIP papers in the (5.5–7.5) range. Comparative analysis:
- vs. **C-CLIP (6.50, Accept)**: NuSA-CL has a more novel method (data-agnostic null space vs. LoRA + distillation), stronger efficiency story (1.5M vs. 15.7M params), and deeper spectral analysis. Similar coverage of ablations. **NuSA-CL is comparable or slightly stronger.**
- vs. **TiC-CLIP (6.25, Accept)**: Different contribution type (method vs. benchmark), but similar quality tier. NuSA-CL's method-level novelty is higher, TiC-CLIP's benchmark contribution is orthogonal. **Comparable.**
- vs. **PROOF (5.67, Reject)**: NuSA-CL has a cleaner method, stronger empirical validation, and more transparent limitations. **NuSA-CL is clearly stronger.**

The paper has no fatal flaws, the weaknesses are minor and addressable, and the core contributions (novel method, strong efficiency, insightful analysis) are well-supported. The paper does not reach the "outstanding" tier (7.5+) but is a solid accept-level contribution. I place it between the C-CLIP (6.50) and the strong end of the middle band.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>