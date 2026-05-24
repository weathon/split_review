Now I have a thorough understanding of the paper and the calibration anchors. Let me produce the final review.

---

## Summary

This paper formalizes the all-day multi-scenes lifelong vision-and-language navigation (AML-VLN) problem and proposes Tucker Adaptation (TuKA), a method that represents multi-hierarchical navigation knowledge (scene-level and environment-level) as a fourth-order tensor and decouples it via Tucker decomposition into shared core components and scene-/environment-specific expert vectors. The accompanying Decoupled Knowledge Incremental Learning (DKIL) strategy consolidates shared subspaces via EWC while constraining experts via orthogonal regularization. Built on StreamVLN/Qwen2-7B, the AllDayWalker agent achieves an average success rate of 65% across 24 tasks, substantially outperforming BranchLoRA (44%) and SD-LoRA (~52%), with an average forgetting rate of just 11%.

## Strengths

1. **Novel tensor-based formulation for multi-hierarchical knowledge.** TuKA is a genuinely novel technical contribution that moves beyond the two-matrix structure of LoRA/MoE-LoRA variants. By embedding navigation knowledge in a fourth-order tensor $\mathcal{X} \in \mathbb{R}^{a_l \times b_l \times M \times N}$ and applying Tucker decomposition (Eq. 2), the method explicitly decouples scene expertise ($U^3$) and environment expertise ($U^4$) while sharing core navigation skills ($\mathcal{G}, U^1, U^2$). The tensor-matrix alignment trick (selecting one row from $U^3$ and $U^4$ to reduce to a weight matrix, Eq. 3) is a clever solution to the dimensional alignment problem.

2. **Strong and consistent empirical results.** AllDayWalker achieves the highest SR on 22 out of 24 tasks in Table 1, with an average SR of 65% vs. the best baseline BranchLoRA at 44%. The forgetting rates (Table 2) are correspondingly low (avg. 11% F-SR vs. SD-LoRA at 18% and BranchLoRA at 36%). The results are stable when scaling to 30 tasks (Table 4), and generalization to unseen scenes (Table 5) shows a 15–16 point improvement over the best baselines.

3. **Comprehensive benchmark construction.** The AllDay-Habitat platform extends Habitat with three physics-based degradation models (atmospheric scattering Eq. 10, low-light Eq. 11, overexposure Eq. 12) to create 20 simulation tasks across 5 scenes × 4 environments, plus 4 real-world validation tasks. This is a significant engineering contribution that enables reproducible research on a practical problem.

4. **Solid ablation analysis.** Figure 8 shows that fourth-order tensors consistently outperform third-order tensors across all 20 tasks. Table 3 demonstrates the importance of sharing the core tensor $\mathcal{G}$ and encoder $U^2$ (SR improves from 53% to 65%). The paper also shows that extending from 24 to 30 tasks causes no significant degradation.

5. **Real-world deployment.** Validation on two real-world scenes under normal and low-light conditions (Table 5, G5–G6) demonstrates that the method transfers beyond simulation, which is uncommon in this area.

## Weaknesses

### Major

1. **No control over task-order effects in lifelong learning.** The paper states "the order of tasks is randomized" (Figure 6 caption) but reports results from a single run with no variance estimates or replication across multiple random orders. Lifelong learning performance is notoriously sensitive to task ordering; reporting results from one favorable order does not establish robustness. The headline claims in Tables 1–2 are uncalibrated against this source of variance. This is a genuine methodological gap for any lifelong learning evaluation.

2. **CLIP-based expert retrieval at inference is unvalidated.** The generalization experiments (Table 5) rely on selecting the correct scene expert $U^3[s,:]$ and environment expert $U^4[e,:]$ by matching CLIP features of the current observation to stored gallery features (Section 3.4). The paper provides no analysis of retrieval accuracy, no confusion matrix, no t-SNE visualization of feature separability across environments, and no ablation showing how performance degrades when retrieval is wrong. This is especially concerning because CLIP was not trained on degraded images (low-light, overexposure, scattering), making it an open question whether its features reliably distinguish "overexposed Scene A" from "normal Scene A." Since the retrieval mechanism is critical to the claimed generalization, its lack of validation is a significant gap.

### Minor

3. **Navigation loss gets only half the total weight with no sensitivity analysis.** The primary navigation objective has weight $\lambda = 0.5$, while $\lambda_1=0.2$ (EWC), $\lambda_2=0.2$ (consistency), and $\lambda_3=0.1$ (orthogonality) collectively account for the other half. This is an unusual design choice, and the paper provides no ablation or sensitivity analysis over $\lambda$ values to demonstrate that navigation performance is not suppressed by aggressive regularization.

4. **Forgetting metric is non-standard and conflates two effects.** The metric $F\text{-SR}_t = (M\text{-SR}_t - SR_t)/M\text{-SR}_t$ (Eq. 13) mixes (a) how much sequential learning degrades performance and (b) how strong the multi-task baseline is. A method that learns poorly from joint training (low $M\text{-SR}$) artificially makes the forgetting rate appear worse. The paper does not report the $M\text{-SR}$ values that are the denominator of this metric, making the forgetting numbers hard to interpret. Standard backward transfer (BWT) would be more informative and comparable with the literature.

5. **No sensitivity analysis on tensor ranks.** The ranks are set to $r_1=r_2=8, r_3=r_4=64$ without justification or sweep over alternatives. Given that these ranks control the capacity of the shared subspace vs. the expert subspaces, a sensitivity analysis would strengthen confidence that the decoupling (rather than capacity imbalance) drives the improvement.

6. **Only one backbone evaluated.** All experiments use StreamVLN with Qwen2-7B. Showing that TuKA transfers to a different backbone or vision encoder would substantially strengthen the generality claim.

### Trivial

7. **The paper does not explicitly state which transformer layers the adapter is applied to** (all attention weight matrices? FFN layers? a subset?). While this is likely standard (all attention projection matrices), stating it explicitly would improve reproducibility.

## Nice-to-Haves

- Reporting $M\text{-SR}$ values (the denominator of the forgetting metric) would make the forgetting numbers interpretable.
- A backward transfer (BWT) metric as a complement to the paper's own metric.
- A t-SNE/UMAP visualization of CLIP feature separability across the four environments.
- A discussion of limitations (e.g., what happens if CLIP retrieval fails, or if a new scene is visually near-identical to an old one but requires different navigation behavior).

## Removed Points

- **Parameter count comparability**: The harsh critic claimed parameter counts across methods are not comparable and provided speculative calculations. The paper explicitly states "To keep the number of trainable parameters comparable" and refers to Appendix C for full details. The critic's specific calculations are their own and cannot be verified. This point is removed per the rule against criticizing details deferred to the appendix.
- **Figure 2 confusion ("Step-by-step" and "Sequential" values identical)**: This is a parser artifact where colors were stripped and the table text was garbled. The original PDF likely presents this figure correctly. Removed per formatting artifact rules.
- **"The paper overstates the novelty of the problem formalization"**: This is an opinion, not a verifiable weakness. The AML-VLN setting is a genuine formalization that enables the work.
- **Claim that prior tensor methods "fundamentally fail to resolve the dimensional alignment problem" is too strong**: This is the paper's own positioning language; not a verifiable weakness about the paper's content.
- **Orthogonal constraint (Eq. 8) being "too strong"**: This is a design choice, not an error. The paper could ablate it, but the constraint is standard practice for decoupling expert subspaces.
- **General formatting/style nitpicks and requests for appendix content**: Removed per hard rules.

## Novel Insights

None beyond the paper's own contributions. The key insight — that multi-hierarchical navigation knowledge can be explicitly decoupled into distinct tensor modes (scenes, environments) via Tucker decomposition, and that the resulting structure enables effective lifelong learning — is well articulated in the paper itself. A subtle point that the reviews surface is the tension between the paper's elegant tensor formulation and the relatively heuristic retrieval mechanism it relies on for inference, which may point future work toward end-to-end learned retrieval or feature-space regularization for the CLIP gallery.

## Suggestions

- **Run 3–5 random task orders and report mean ± std** for the headline SR and F-SR. This is the single most impactful improvement for establishing the robustness of the claims.
- **Add retrieval accuracy analysis for the CLIP-based expert selection** on both seen and unseen scenes/environments. Report precision@1 and show a confusion matrix or t-SNE plot of the gallery features.
- **Add a sensitivity analysis on λ₁, λ₂, λ₃** (at minimum 2–3 alternative settings) to show that performance is not brittle w.r.t. regularization weight.
- **Report the M-SR values** that are the denominator of the forgetting metric, or supplement with standard BWT.
- **Add a rank sensitivity study** varying $r_3, r_4$ (e.g., 32, 64, 128) and $r_1, r_2$ (e.g., 4, 8, 16).

## Score and Decision

### Calibration Anchors

| Anchor ID | Avg Score | Round | Comparison to This Paper |
|-----------|-----------|-------|--------------------------|
| OyVRrKG8Dj (CogVLN) | 3.00 | R1 (low) | Rejected VLN paper; our paper is substantially stronger |
| fQTw3w3hnA (CoFiCL) | 3.00 | R1 (low) | Rejected continual learning for VLMs; our paper has stronger eval |
| rkTNAk3QSh (Dynamic Context Adapters) | 3.00 | R1 (low) | Withdrawn; not comparable |
| mDuton6Tg7 (Cross-Modal Alignment CL) | 3.00 | R1 (low) | Withdrawn; not comparable |
| pFh5ygjN3V (M³E) | 4.50 | R1 (mid) | Accepted poster on continual VLN; our paper is more comprehensive with greater novelty |
| PaYo96rjij (Lifelong Embodied Nav) | 6.00 | R1 (mid) | **Most comparable anchor.** Both tackle lifelong navigation with knowledge decoupling. Our paper has more novel technical contribution (Tucker vs. DE-LoRA) and more comprehensive evaluation, but has evaluation gaps (task-order replication, retrieval validation) that Uni-Walker does not. Comparable overall quality. |
| 9ktF3pwXi8 (End-to-End to Step-by-Step) | 4.67 | R1 (mid) | Rejected VLN paper; our paper is stronger |
| RnuB0Nlbd5 (JanusVLN) | 5.00 | R1 (mid) | Accepted poster on VLN with decoupled memory; different contribution type, our paper has more comprehensive lifelong evaluation |
| uqoKr4m8hl (Adaptive Rank Reduced Forgetting) | 5.00 | R2 (narrow) | Rejected continual learning for VLMs; our paper is stronger |
| T3Vc5fkTzV (KeepLoRA) | 5.50 | R2 (narrow) | Accepted poster on continual learning for VLMs; comparable quality, different domain |
| caDjycqDY2 (LLaVA-CMoE) | 5.50 | R2 (narrow) | Rejected continual MoE for LVLMs; our paper is stronger |
| mp0rPiYHPi (MetaTT) | 5.00 | R2 (narrow) | Rejected tensor-decomposition adapter; our paper applies tensor methods to a more challenging domain with stronger results |
| 0oHaazjMUX (LeSTD) | 5.50 | R2 (narrow) | Accepted poster on tensor decomposition for LLM compression; different application |
| kkBOIsrCXh (NavFoM) | 8.00 | R1 (high) | Foundation model paper; higher-scoring but on a different scale of contribution (cross-embodiment, cross-task) |

**Round 1 bracket**: (4.5, 7.0) — the paper is clearly stronger than the ~3.0 VLN papers and clearly weaker than the ~8.0 foundation-model-scale papers.

**Round 2 calibration (narrowing within bracket)**: The most directly comparable anchor is **Lifelong Embodied Navigation Learning (Uni-Walker) at 6.00**, which tackles the same problem with a similar philosophy (LoRA-based knowledge decoupling for lifelong navigation) and was accepted as a poster. Our paper matches or exceeds Uni-Walker on technical novelty (Tucker decomposition vs. DE-LoRA) and evaluation comprehensiveness (24+6 tasks vs. 18, plus real-world validation), but has evaluation gaps (no task-order replication, unvalidated retrieval mechanism) that Uni-Walker's reviews did not flag. Comparing to the next tier: the paper is clearly stronger than M³E (4.50, accepted poster) and KeepLoRA (5.50, accepted poster). The tensor-decomposition anchor MetaTT (5.00, rejected) validates that tensor-based adapters for PEFT are considered borderline-acceptable work, and our paper applies the concept more convincingly to a harder domain.

**Final score**: 6.0. The paper sits at the level of a solid poster: a genuinely novel technical idea with strong empirical results, held back from a higher score by the absence of task-order replication and the unvalidated retrieval mechanism — both fixable issues.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>