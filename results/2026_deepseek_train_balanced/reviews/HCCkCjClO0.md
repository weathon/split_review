## Summary

This paper proposes Online Weight Approximation (OWA), which uses Legendre-polynomial-based online function approximation (Gu et al., 2020) to model the trajectory of each neural network weight across continual learning tasks. At test time, given a task ID, OWA reconstructs task-specific weights from a compact set of N coefficients per weight (memory O(pN) instead of O(pT)), avoiding catastrophic forgetting. Experiments on incrementally permuted datasets (domain-incremental, T=100) show strong results, while results on class-split datasets (CIFAR-100, CUB-200) are mixed.

## Strengths

- **Novel application of online function approximation to continual learning.** The core idea — compressing weight trajectories via Legendre-polynomial online approximation — is genuinely novel within CL and distinct from regularization, architectural, and replay families. The theoretical derivation (Theorem 2.1, ODE coefficient dynamics) is mathematically grounded, and the τ-independence property (Proposition 3.1 / Eq. 7) is elegant.

- **Strong empirical results on incrementally permuted datasets.** On Incrementally Permuted MNIST, Fashion-MNIST, and CIFAR-10 (T=100 tasks each), OWA with N=20 matches or exceeds the local-last accuracy and achieves +14–34% gains over replay (Section 4.1, Table 1). These results provide genuine evidence that the method works when weight trajectories are smooth — the setting the method was designed for.

- **Honest reporting of limitations.** The paper transparently reports that OWA underperforms replay by 3–12% on low/medium-budget CUB-200 Split and acknowledges the challenge of abrupt domain shifts (Section 4.2). This candor increases credibility for the positive results.

## Weaknesses

### Fatal
None.

### Major

- **Setting mischaracterization: "class-incremental" results are actually task-incremental.** The abstract and contribution (ii) claim the method works on "class-incremental problems," and Section 4.2 is titled "CLASS INCREMENTAL/SPLIT DATASETS." However, the method requires task IDs at test time (Section 2, line 65: *"we will assume that either the ID of the task is available or that we are able to infer it"*). In standard continual learning taxonomies, providing task IDs at inference defines *task-incremental* learning, not *class-incremental* learning — the latter requires the model to predict across all classes seen so far without knowing which task produced the sample. These are fundamentally different in difficulty. The paper's reported results on Split CIFAR-100 and Split CUB-200 therefore demonstrate task-incremental (not class-incremental) capabilities on class-split data. This mislabeling inflates the claimed contribution.

- **Replay baseline is practically non-functional in the class-split experiments.** The memory-equivalence formula n = N·p/d (Section 4, line 114) is technically correct on storage bytes but produces pathologically small buffers in the class-split setting. For CIFAR-100 Split: ResNet18 in transfer learning (only the last FC layer, p ≈ 51,300), images upscaled to 224×224 (d = 150,528). For N=2, the replay buffer holds n = (2 × 51,300) / 150,528 ≈ **0.68 samples total** across all 20 tasks. Even for N=10, it holds ≈3.4 samples. This is not "a powerful replay strategy" (abstract) — it is a crippled baseline that can barely function. The claimed +6–26% gains over replay in Table 2 are gains against a method with essentially zero working memory. On the permuted datasets (where d/p ratios are more favorable), the issue is less severe, but the abstract and conclusion do not differentiate.

- **No comparison against any established continual learning method.** The paper compares only against vanilla sequential fine-tuning and a uniform replay baseline. The Related Work (Section 5) discusses EWC, SI, MAS, HAT, PackNet, Progressive Neural Networks, iCaRL, GEM, DER++, and others at length — yet none appear as baselines. The claim that OWA "can be readily applied in conjunction with most regularization-based methods" is speculative without experiments. For a paper claiming "effectiveness and superiority" (abstract), the absence of any comparison to methods from the field it addresses is a critical omission that prevents the reader from calibrating OWA's performance against standard approaches.

### Minor

- **"Matching single-task performance" claim lacks per-task evidence.** The paper compares OWA's **average** accuracy across all tasks to the "local last" accuracy (a model trained and tested on the last task alone). While informative for domain-incremental settings where tasks are similarly difficult, an average across 100 tasks matching one task's local accuracy does not rigorously demonstrate per-task parity. Per-task accuracy breakdowns would substantiate the claim that OWA "closes the gap with locally learnt models" (conclusion).

- **Central smoothness assumption is not empirically verified.** The method's foundation is that weight trajectories are smooth enough for low-order Legendre approximation (Theorem 2.1 requires the approximated function to be continuous). The paper's resolution — that a continuous interpolant always exists (line 78) — is a mathematical existence statement, not an empirical check. The approximation quality depends on actual smoothness, which the paper acknowledges matters (line 105: *"only if the difference between |w_i^{k+1} - w_i^k| is sufficiently small"*) but never measures. This leaves the theory disconnected from the experiments.

- **Scalability is unaddressed.** The OWA update (Eq. 7) involves an O(p·N²) matrix-vector product per update step (one N×N matrix multiply per weight). For models with millions of parameters, this cost is substantial. No training time, inference time, or complexity analysis is reported, despite the method being described as "efficient."

- **Only incrementally permuted datasets are used, not standard Permuted MNIST.** The paper uses only the "incrementally permuted" variant (100-pixel changes per task), which is *designed* to produce smooth distribution shifts. Standard Permuted MNIST (random permutations per task) would test the method under abrupt, large-magnitude shifts — a more informative stress test of the continuity assumption.

### Trivial

- **No initialization/warmup described for the first-task update.** At k=1, Eq. 7 involves a factor of k⁻¹ = 1, but no coefficient initialization or warmup strategy is specified.
- **"Local last" accuracy is defined only in figure captions and table footnotes, not in the main text**, making its precise meaning ambiguous on first read.

## Nice-to-Haves

- An algorithmic summary or pseudocode would substantially aid reproducibility, especially for the coefficient update scheduling (π_j^α policy) and weight-reconstruction procedure.
- An ablation study of the update frequency (π_j^α) would clarify the trade-off between approximation quality and computational cost.

## Removed Points

These points were flagged by the reviewers but are removed from the main review with justifications:

- *"Proposition 3.1 is stated but never used"* — While formally true, the property explains the τ-independence of Eq. 7, which is useful context. Not a weakness.
- *"Only 3 seeds used"* — Standard practice in CL. Not a weakness.
- *"No pseudocode or algorithmic summary"* — The method description is mathematically clear. This is a nice-to-have, not a weakness.
- *"The update policy π_j^α is never formally defined"* — It is sufficiently described (π≡1 for permuted, "updating 10 times per task" for class-split). A formal definition would be cleaner but the absence is not a meaningful weakness.
- *"The 'class-incremental' vs 'task-incremental' distinction is acknowledged in Section 2"* — The paper does say "task incremental learning" in Section 2 (line 65), but then contradicts this by labeling Section 4.2 as "CLASS INCREMENTAL" and claiming class-incremental results in the abstract and contributions. The inconsistency is the problem; the acknowledgment does not resolve it.
- *Strength Finder: "Substantial improvements over replay under carefully matched memory budgets"* — The "carefully matched" framing is misleading for class-split settings (buffer < 1 sample). The strength is retained but caveated in the summary; the claim is not fully endorsed as written.

## Novel Insights

The reviews reveal a fundamental tension in the paper: the method's core theoretical assumption (smooth weight trajectories that can be approximated by low-order Legendre expansions) is most justified in the incrementally permuted setting, which is precisely where the empirical results are strongest. Conversely, the method struggles precisely where the theory is least justified (abrupt class-split shifts). This alignment between theoretical scope and empirical success is actually a strength of the paper's internal consistency — but the paper undercuts itself by claiming "class-incremental" results that it cannot substantiate. A reframed paper that honestly positions OWA as a method for gradual-domain-shift task-incremental learning, with an explicit discussion of when the smoothness assumption holds and when it breaks, would present a more coherent and defensible contribution.

## Suggestions

1. **Reframe the paper's claims honestly.** Clearly position the method as task-incremental learning (which the method actually requires), and remove or qualify the "class-incremental" labeling. The abstract already says "provided that the task identities can be estimated" — lean into this framing consistently.
2. **Revisit the replay comparison.** Either (a) use a more meaningful memory-equivalence strategy for class-split settings (e.g., matching on total storage bytes is correct but practically misleading when the buffer holds <1 sample), or (b) remove the "powerful replay strategy" language and acknowledge the limitation.
3. **Add at least one standard baseline.** Even a single established method (e.g., EWC or a basic replay-based approach like ER with equivalent memory) would dramatically improve the reader's ability to calibrate OWA's practical value.
4. **Empirically verify smoothness.** Measure per-weight differences between consecutive tasks (‖w^{k+1} - w^k‖) and reconstruction error on held-out tasks to ground the central assumption.
5. **Add standard Permuted MNIST** as a stress test for the continuity assumption.

## Score and Decision

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>