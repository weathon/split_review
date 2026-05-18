Now I have a thorough understanding of the paper. Let me construct the consolidated review.

---

## Summary

This paper proposes DISTA, a test-time adaptation method that uses an auxiliary knowledge-distillation loss on clean unlabeled source data to accelerate adaptation when the test stream reveals limited data per step. The key idea is to take a second gradient step on samples from the source distribution, distilling the original pretrained model's predictions to prevent overfitting while speeding convergence. The method is evaluated across episodic, continual, and federated protocols on ImageNet-C and ImageNet-3DCC, reporting gains of 1.5% (episodic) and 6% (continual) over EATA.

## Strengths

1. **Consistent SOTA results across multiple evaluation protocols.** DISTA outperforms EATA on ImageNet-C under episodic (+1.5%), continual (+6%), and federated (+6%) evaluation (Tables 1, 3, 5), and these gains hold on ImageNet-3DCC (+8% continual, Table 4). The consistency across protocols strengthens the empirical case for the approach.

2. **Robustness to architecture and batch size.** Figure 2b shows DISTA improves over EATA by >15% at batch size 8, and Figure 2c shows gains across ResNet-18, ResNet-50-GN, and ViT (7% over SAR on ViT). This demonstrates the method is not narrowly tuned to a single configuration.

3. **Lookahead analysis provides a useful diagnostic tool.** Section 2.1 introduces a lookahead metric (Eq. 3) that empirically demonstrates that auxiliary tasks on source data can accelerate adaptation on corrupted data, even with a simple entropy objective. This provides foundational evidence for the paper's core thesis.

4. **Orthogonality to different TTA bases is validated.** Table 6 shows that adding the auxiliary-task recipe (with entropy minimization on source data) improves both Tent (+0.6%) and SHOT (+4%), indicating the auxiliary-task concept generalizes beyond DISTA's specific distillation formulation.

5. **Computational tradeoff is explicitly characterized.** Figure 2a shows a smooth performance-compute Pareto frontier: with 50% of the auxiliary updates (1.5× compute instead of 2×), DISTA still beats EATA by 1.4%, and a parallel-update variant eliminates the latency overhead. This gives practitioners practical deployment options.

## Weaknesses

### Fatal
None.

### Major

1. **Missing ablation: the effect of the distillation objective is not isolated from the effect of the extra gradient step on source data.** DISTA differs from EATA along multiple dimensions simultaneously: (a) using source data for a full second gradient update (rather than parameter-space regularization), (b) applying a distillation objective on that second step, and (c) using a different data-selection scheme for the source batch. The paper does not include a controlled comparison that isolates dimension (b) — specifically, running DISTA's framework with the distillation loss replaced by entropy minimization on source data, keeping all other components (data selection, optimizer, batch size, alternating scheme) identical. Without this ablation, the reported gains cannot be cleanly attributed to the distillation objective versus simply having an extra optimization step on any auxiliary data. The orthogonality experiment (Table 6) partially addresses this by showing entropy-minimization auxiliary improves Tent/SHOT, but it does not directly compare distillation vs. entropy within DISTA's own pipeline (which includes EATA-style data selection, a different base method, and the distillation loss on clean data). *Evidence from the paper:* lines 77–85 describe the DISTA objective, lines 183–193 discuss computational cost but not objective-type ablation, and Table 6 tests a different setting (Tent/SHOT without EATA's selection mechanism).

2. **The claim that distillation is a "better and more powerful auxiliary task" than entropy minimization is not directly supported by the experiments.** Section 2.1 shows lookahead for entropy-on-source (Figure 1a) and Section 2.2 shows lookahead for distillation-on-source (Figure 1b), but the two are not overlaid or compared on the same scale. The accuracy gains in the main tables compare DISTA (distillation + extra step + EATA-style selection) against EATA (no extra step), not DISTA with distillation vs. DISTA with entropy. The paper states "we propose a better and more powerful auxiliary task" (line 77) but the experimental design does not isolate the auxiliary objective as the independent variable. *Evidence:* Figure 1a and 1b use different y-axis ranges and different setups; Table 1 compares DISTA (distillation auxiliary) against full methods (EATA, Tent, etc.), not against "DISTA with entropy auxiliary on source."

### Minor

1. **No discussion of limitations or failure cases.** The paper does not discuss scenarios where storing source data is infeasible, the size of the required source-data buffer, or how staleness of the stored source data affects performance as the model adapts. Given that the method's applicability depends on having access to clean source-domain samples, this omission limits the paper's practical framing. *Evidence:* The conclusion (Section 5) recapitulates results without a limitations paragraph.

2. **The lookahead metric's connection to final accuracy is not established.** Section 2.1 defines lookahead as the improvement in entropy on the corrupted batch after the auxiliary step. While the paper reports accuracy gains later, there is no direct evidence that higher lookahead values correlate with lower error rates. The two are presented as logically connected but never empirically linked. *Evidence:* Equations 3 and surrounding text (lines 62–68) define the metric; the accuracy results in Tables 1–5 are discussed separately without mapping to lookahead values.

### Trivial
None (all identified issues are addressed in other tiers).

## Nice-to-Haves
- An ablation comparing DISTA with distillation vs. DISTA with entropy minimization on source data, keeping data selection and optimizer identical.
- An ablation replacing the source batch with a second corrupted batch from the stream (same compute, same optimizer, no source data) to test whether clean source data or simply more gradient steps drives the gains.
- Confidence intervals or error bars for the federated evaluation results (Table 5), which involve client splits and may have variability.

## Removed Points

The following points from the inputs have been removed or substantially weakened after cross-checking against the paper:

- **"Baselines do not access source-domain data"** (Harsh Critic, Critical Issue #1): This is factually incorrect. The paper explicitly states (line 48): *"EATA (Niu et al., 2022), for instance, leveraged D_s for calculating the anti-forgetting regularizer."* EATA, the primary baseline, does access source data. The core concern about the extra gradient step is retained (see Major weakness #1), but the framing that baselines see "only the corrupted stream" is removed.

- **"Federated evaluation compounds the unfair advantage"** (Harsh Critic, Experiments 4.3): This is speculative. The federated evaluation compares all methods under the same source-data conditions (DISTA uses source data, EATA also uses source data for its regularizer). No evidence is provided that the relative gain is inflated.

- **"EATA's data selection is brittle at small batch sizes; the observed gain could be from the second update step"** (Harsh Critic, Ablation 4.4.2): The paper itself notes this (line 204): *"the data selection process of EATA hinders its effectiveness for small batch sizes, allowing Tent to outperform it, but our proposed auxiliary task seems to mitigate the same effect for DISTA."* The authors are transparent about this dynamic. The criticism does not add new information.

- **"Statistical significance missing"** (Harsh Critic, Missing Parts): Standard in TTA evaluation (single-run, deterministic evaluation). Reasonable to request for the federated setup but not a meaningful weakness.

- Various generic strengths from the Strength Finder (e.g., "this paper addressed an important problem") removed as they are superficial or generic.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the need for a controlled ablation separating the distillation objective from the extra gradient step, but this is a well-understood experimental design requirement rather than a novel insight about the method itself.

## Suggestions

1. Add the critical ablation comparing distillation vs. entropy minimization as the auxiliary objective inside DISTA's own framework (same data selection, batch size, optimizer). This is the single highest-leverage experiment to strengthen the paper's central claim.
2. Add an ablation that uses a second corrupted batch (from the stream) instead of a clean source batch for the auxiliary step, to distinguish the benefit of clean source data from the benefit of an extra gradient step on any data.
3. Briefly discuss the practical footprint: how many source samples are stored, how stale they can become before performance degrades, and what happens when source data is unavailable.

## Score and Decision

The paper proposes a sensible and well-motivated idea, backed by substantial experimentation across multiple benchmarks and protocols. The core weakness is that the contribution of the *specific* distillation objective (vs. simply having an extra gradient step on source data with any objective) is not isolated experimentally, leaving the paper's strongest claim partially undersupported. This is a significant but not fatal gap — the method as a whole is validated, and the orthogonality experiment (Table 6) provides partial evidence. With the missing ablation addressed, this would be a strong paper. In its current form, it is a solid contribution that would benefit from revision.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>