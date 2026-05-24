Now I have all the information I need. Let me compose the final consolidated review.

---

## Summary

This paper formalizes the all-day multi-scenes lifelong vision-and-language navigation (AML-VLN) problem and proposes Tucker Adaptation (TuKA), a parameter-efficient fine-tuning method that represents multi-hierarchical navigation knowledge as a 4th-order tensor. TuKA uses Tucker decomposition to decouple shared navigation skills (core tensor, encoder, decoder) from scene-specific and environment-specific expert vectors. A decoupled knowledge incremental learning (DKIL) strategy combines EWC on shared components with expert consistency constraints and orthogonal optimization to mitigate catastrophic forgetting. The authors also contribute the AllDay-Habitat benchmark, extending Habitat with three physically-grounded imaging degradation models (low-light, overexposure, scattering). The resulting agent, AllDayWalker, achieves 65% average SR across 24 sequentially learned tasks with only 11% average forgetting rate, outperforming a comprehensive suite of LoRA-based continual learning baselines.

## Strengths

- **Novel high-order tensor formulation for PEFT in VLN.** The core idea — using a 4th-order Tucker decomposition to explicitly decouple scene-expert and environment-expert dimensions from shared navigation knowledge — is genuinely innovative. Unlike prior LoRA variants confined to two-dimensional matrix parameterizations, TuKA naturally captures the multi-hierarchical structure inherent in the AML-VLN problem. The tensor-to-matrix alignment via modal products (Eq. 3) is a clever resolution of the dimensional mismatch between high-order tensors and LLM weight matrices.

- **Strong empirical results with comprehensive baselines.** AllDayWalker achieves 65% average SR vs. 56% for the best LoRA-based baseline (SD-LoRA), with an average forgetting rate of only 11% vs. 23% for O-LoRA (Tables 1, 2). The comparison suite is thorough: 12 different methods spanning vanilla LoRA, MoE-LoRA variants, orthogonal regularization, and test-time adaptation approaches. The consistent advantage across all 24 tasks and four evaluation metrics (SR, SPL, OSR, and their forgetting counterparts) provides convincing evidence.

- **Well-designed ablations supporting architectural choices.** Figure 8 demonstrates that a 4th-order tensor consistently outperforms a 3rd-order variant across all 20 simulation tasks, directly validating the benefit of decoupling scene and environment dimensions. Table 3 quantifies the contribution of shared components: removing the shared core tensor G drops SR from 65% to 55%, confirming that shared navigation knowledge consolidation is essential.

- **Systematic benchmark construction.** The AllDay-Habitat platform (§4) synthesizes degraded environments using well-specified imaging models (atmospheric scattering, low-light sensor physics with shot/read noise, overexposure with saturation clipping). This provides a controllable, reproducible testbed grounded in real imaging physics, going beyond simple data augmentation.

- **Generalization evidence.** Table 5 shows AllDayWalker achieving 55% average SR on six completely unseen scene-environment combinations, outperforming BranchLoRA (40%) and SD-LoRA (39%) by a wide margin. The 30-task extension (Table 4) demonstrates stability under increased task load.

## Weaknesses

### Fatal

None.

### Major

- **Single task ordering with no error bars or multi-seed reporting.** The paper states that "the order of tasks is randomized" (Figure 6 caption) but reports only one trajectory of 24 tasks without standard deviations, confidence intervals, or results averaged over multiple random orderings. In continual learning, task order can substantially influence forgetting and final performance. This is a genuine concern for assessing whether the reported margins are robust. That said, the computational cost of training a 7B-parameter LLM sequentially across 24 tasks on 8 GPUs makes full multi-seed replication expensive, and other evidence (consistent 4th-order > 3rd-order advantage across all 20 tasks in Figure 8, generalization to unseen scenarios in Table 5, stability under 30-task extension in Table 4) provides partial robustness support. This weakness prevents the experimental evidence from being conclusive without being fatal.

### Minor

- **Parameter budget comparison deferred to appendix.** The paper states that trainable parameters are kept comparable and provides rank/expert hyperparameters in the main text (e.g., LoRA r=6, MoE-LoRA r=16 with K=8, TuKA r1=r2=8, r3=r4=64), but the actual per-method parameter counts are in Appendix C (stripped in this submission format). Since the paper explicitly acknowledges and addresses this with an appendix table, and the hyperparameter choices suggest a good-faith effort at fairness, this is a presentation issue rather than a methodological flaw. Readers cannot verify parameter parity from the main text alone.

- **No evaluation of expert retrieval accuracy.** Section 3.4 describes a CLIP-based cosine-similarity matching mechanism to select scene and environment experts at inference time without task IDs. This is a practical and well-motivated design, but the paper provides no diagnostic on retrieval accuracy or its impact on navigation success. Since retrieval errors would degrade the generalization results in Table 5, an ablation quantifying retrieval precision would strengthen confidence in real-world deployability.

### Trivial

- **Forgetting metric definition is present but could be clearer on first read.** Eq. 13 and the accompanying text define F-SR_t relative to M-SR_t, where M-SR_t is the performance from jointly training on tasks 1 through t. This is an oracle upper bound; the metric is well-defined. The occasional negative forgetting values (e.g., -3% at T14, -4% at T20 in Table 2) reflect cases where the sequential learner with anti-forgetting mechanisms outperforms joint multi-task training — a legitimate and informative outcome, not an error. The definition is in the paper; a one-sentence clarification that M-SR_t uses joint (not sequential) training would preempt confusion.

## Nice-to-Haves

- **Computational overhead analysis.** The Tucker decomposition introduces a core tensor and modal products that add per-layer computation. A brief discussion of inference latency or FLOPs relative to LoRA baselines would help practitioners assess deployment tradeoffs, especially for real-time navigation.

- **Scoping of the "all-day" claim.** The paper covers four illumination/degradation conditions (normal, low-light, overexposure, scattering). Real-world all-day operation involves additional factors (dynamic lighting, weather, object motion). A clearer bounding of the tested conditions would prevent overclaiming without weakening the contribution.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Harsh critic claimed the forgetting metric is "ambiguous" and "difficult to interpret" with negative values being "unusual."** *Removed.* The metric is defined at Eq. 13 and the surrounding text: M-SR_t is performance from training on tasks 1 through t jointly. Negative values are meaningful (sequential with anti-forgetting can outperform joint training) and are not an error. The definition is present in the paper.

- **Harsh critic claimed that BranchLoRA and SD-LoRA are "not designed for zero-shot test-time selection" making the generalization comparison "not entirely equitable."** *Removed.* The generalization experiment (§5.3, Table 5) evaluates all methods under the same protocol — test on unseen scenarios and select the best-matching weights. TuKA's CLIP-based retrieval is a feature of the method, and baseline methods also need to select weights somehow. All methods face the same challenge; the comparison is fair.

- **Harsh critic questioned whether cited models/benchmarks exist ("real-world data only covers normal and low-light conditions").** *Removed per hard rules.* All cited artifacts are assumed to exist. The paper explicitly includes real-world data as a strength, not a limitation, and acknowledges the coverage.

- **Strength Finder claimed "Task-agnostic expert retrieval for deployment" as a standalone strength.** *Downgraded.* The mechanism is well-designed but retrieval accuracy is not evaluated, limiting this as a fully-supported strength. Moved to supporting context rather than a primary strength.

- **Harsh critic's Section-by-Section note about tensor factorization related work in computer vision and computational cost discussion.** *Moved to Nice-to-Haves.* These are reasonable suggestions but not weaknesses in the paper as written.

## Novel Insights

The key insight emerging from this work is that representing multi-hierarchical task knowledge as a high-order tensor — with explicit dimensions for scene and environment — enables more effective continual learning than matrix-based adapters that conflate these hierarchies. The Tucker decomposition provides a natural framework for this: the core tensor captures shared navigation skills, while factor matrix rows serve as disentangled expert vectors that can be independently frozen, inherited, or orthogonalized during incremental learning. This structural decoupling is what drives the dramatically lower forgetting rates compared to even sophisticated LoRA variants that attempt similar shared-specific decompositions but are limited to two-dimensional representations.

## Suggestions

- If computationally feasible, run the lifelong learning benchmark with 2–3 additional random task orderings and report mean ± std across all metrics. This single addition would substantially strengthen the paper's evidential basis. Even reporting variance across the per-task results (e.g., the spread visible in Table 1) would help.
- Add a retrieval accuracy diagnostic for the CLIP-based expert matching in §3.4, even if brief — e.g., top-1 accuracy of scene/environment expert selection on the held-out generalization tasks.
- Bring the key parameter-count comparison from Appendix C into the main paper as a concise table, so readers can verify parameter parity without consulting the appendix.
- Consider adding a one-sentence clarification after Eq. 13 explicitly stating that M-SR_t is obtained via joint (multi-task) training on tasks 1 through t, not sequential training.

## Score and Decision

**Round 1 bracket:** The paper was placed between 5.5 and 7.5 based on comparison with GSA-VLN (6.40, similar domain — VLN scene adaptation), FLoRA (5.75, Tucker decomposition for PEFT), and the Function Vectors paper (9.00, deep theoretical CL analysis, clearly stronger).

**Round 2 narrowing:** Compared against TAIL (6.20, PEFT for continual imitation learning), FLoRA (5.75), GSA-VLN (6.40), C-CLIP (6.50), and SLM (6.50). The paper has more methodological novelty than TAIL (genuine new architecture vs. benchmarking existing PEFT methods), more focused application and stronger results than FLoRA, and a more comprehensive evaluation with stronger results than GSA-VLN.

**Anchor comparison summary:**

| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| GSA-VLN (2oKkQTyfz7) | 6.40 | R1/R2 | Similar VLN domain; our paper has more novel method and more baselines |
| TAIL (RRayv1ZPN3) | 6.20 | R2 | PEFT for continual control; less novel (tests existing methods), single benchmark |
| FLoRA (OALIb8oNfl) | 5.75 | R2 | Tucker decomposition for PEFT; less focused application, weaker LLM results |
| C-CLIP (sb7qHFYwBc) | 6.50 | R2 | Multimodal continual CL; comparable tier |
| SLM (mz8owj4DXu) | 6.50 | R2 | Continual learning for LMs; comparable tier |
| Function Vectors (gc8QAQfXv6) | 9.00 | R1 | Deep theoretical CL analysis; clearly stronger |
| LVLM-CL (JIlIYIHMuv) | 2.50 | R1 | Weak CL evaluation; clearly weaker |
| Decoupled CRL (Q1Hr9dVfDS) | 3.00 | R1 | Weak RL CL method; clearly weaker |

The paper sits above the 6.0–6.5 cluster due to genuine methodological novelty (4th-order Tucker for lifelong VLN is more innovative than benchmarking PEFT methods or straightforward Tucker application), comprehensive evaluation (12+ baselines, 24 tasks, 4 metrics), and a useful benchmark contribution. The single-task-ordering limitation prevents it from reaching the 7.5+ tier where evidence would be fully conclusive and theoretical depth would distinguish it.

**Final score: 7.0.**

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>