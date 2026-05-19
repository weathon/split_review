- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 8, 6, 6
Now I have a thorough understanding of the paper and can verify each claim. Let me compose the consolidated review.

## Summary

This paper addresses the problem of detecting machine-generated texts (MGTs) from multiple LLMs using kernel-based maximum mean discrepancy (MMD). The authors identify that when MGTs come from diverse LLMs, the variance of the standard MMD estimator grows sharply, degrading detection. They propose MMD-MP, which removes the intra-class MGT similarity term \(k(y,y')\) from the MMD training objective, yielding a lower-variance proxy statistic (MPP). With the trained kernel, they develop paragraph-based (two-sample test) and sentence-based (single-instance detection) methods. Experiments across ChatGPT, GPT2, GPT3, GPT-Neo, and other LLMs show consistent improvements over baselines, with particularly strong gains (23–28% absolute) on detecting texts from unseen LLMs.

## Strengths

- **Identifies and empirically characterizes the high-variance problem in kernel MMD for multi-population MGTs.** Section 2.2 and Figure 1 clearly show that as the number of MGT populations \(q\) increases, MMD-D's variance grows sharply while test power degrades. The variance decomposition in Section 2.2 (line 137) and the empirical analysis in Section 2.3 (Figure 2) pinpoint that the intra-class term \(k_\omega(y,y')\) is the primary driver, directly motivating the proposed solution.

- **MMD-MP consistently outperforms MMD-D and other baselines across diverse settings.** On full-data paragraph detection (Table 1), MMD-MP beats MMD-D by up to ~6% test power. On limited data (Table 2), gains reach ~14–18%. On unbalanced data (Figure 3), gains are 7–14%. Most impressively, on **unknown LLM texts** (Tables 5–6), MMD-MP achieves a striking **23–28% absolute test-power gain** over MMD-D, demonstrating that the method yields a more transferable kernel that does not overfit to specific training MGT populations.

- **Clean, theoretically grounded solution with practical algorithms.** The proposed removal of \(k(y,y')\) is simple and intuitive. Proposition 1, Corollary 1, and Theorem 1 provide asymptotic distribution, test power, and uniform convergence guarantees for the MPP-based objective. Algorithms 1–3 give reproducible procedures for training, paragraph-based detection (2ST), and sentence-based detection (SID).

- **Synthetic data experiment (Section 5.1, Figure 4) isolates the effect of training-data variance.** Using a controlled four-center Gaussian mixture, the paper shows that MMD-MP's advantage grows precisely when the variance of the training data increases, directly supporting the variance-reduction narrative.

## Weaknesses

### Fatal
None.

### Major

- **Unsubstantiated claim about training–testing alignment.** The paper trains the kernel using the MPP statistic (which excludes \(k(y,y')\)) but tests using the full MMD (which includes \(k(y,y')\)). The paper states at line 316: *"Empirically, the performance of these two strategies is almost identical,"* but **no empirical evidence is provided anywhere in the paper to support this claim**. This is the paper's most significant gap. While the pragmatic rationale (MMD is non-negative under the null) is sound, the claim of near-identical performance between MPP-based testing and MMD-based testing with the MPP-trained kernel is a critical link in the argument that needs direct validation. Without it, the reader cannot fully assess whether the training objective aligns with the evaluation objective.

### Minor

- **No formal statistical significance tests.** Results are reported as means and standard deviations over 5 runs (Table 1 caption), but some comparisons show overlapping error bars (e.g., Table 1, ChatGPT+Neo-S: MMD-D \(86.44\pm1.07\) vs. MMD-MP \(89.63\pm1.94\)). Paired tests (e.g., paired t-test or Wilcoxon) over repeated splits would clarify whether the observed differences are statistically reliable, particularly when gains are modest.

- **Limited ablation isolating the specific design choice.** The paper compares MMD-MP against MMD-D, but no ablation isolates whether removing \(k(y,y')\) specifically is the critical factor. Alternatives such as (a) a variance-penalized version of full MMD (e.g., \(\text{MMD} / (\sigma + \lambda)\) without dropping terms) or (b) a version that removes \(k(x,x')\) instead of \(k(y,y')\) would sharpen the causal claim. Without these, the improvement could partly stem from incidental regularization effects.

- **Transfer experiments use only one training mix.** The strong transfer results (Tables 5–6) use a single training combination (ChatGPT, GPT2-S, GPT2-M). Varying the composition of training LLMs and testing on a broader set (e.g., models from different families or size scales) would strengthen the claim that MMD-MP's transferability is general, not tied to a specific training configuration.

- **t-SNE visualization (Figure 6) is qualitative.** The paper uses t-SNE plots to argue that MMD-MP produces better-separated features. A quantitative metric such as silhouette score or supervised nearest-neighbor accuracy would make this claim more rigorous.

### Trivial
- The main text omits some experimental details (e.g., learning rate, batch size, number of epochs, exact architecture of \(\phi_f\)), though these may be in the appendix.

- Some reported standard deviations are very small relative to the mean (e.g., Table 3, Likelihood: \(89.82\pm0.03\)), which could use a brief clarification on whether these are across folds or different random seeds.

## Nice-to-Haves
- A systematic sensitivity study varying the number of training populations \(q\) on a fixed test set, to directly demonstrate the relationship between population diversity and the advantage of MMD-MP.
- Comparison of training and inference computational cost between MMD-MP and MMD-D.
- A discussion of scenarios where MMD-MP may not help (e.g., single-population MGTs, or when the kernel poorly represents text).

## Removed Points
*These points were flagged by reviewers or extracted but are removed after verification — treat with caution.*

1. **"Theoretical analysis is circular."** Removed. The paper's theory (Corollary 1) analyzes the test power of \(\text{MPP} + R(S_\mathbb{Q})\), and Remark 2 explicitly explains how this relates to the MMD used at test time. The theory supports the training objective; it does not claim to directly prove the test-time behavior. Not circular.
2. **"Variance analysis is not rigorous — only from a single synthetic setting."** Removed. Figure 1 monitors real training runs (not synthetic data), and the synthetic experiment in Section 5.1 (Figure 4) is a separate, controlled validation. The variance decomposition and empirical observations in Sections 2.2–2.3 constitute a reasonable empirical analysis.
3. **"MMD-MP falls within 1 SD of MMD-D in some comparisons."** Removed. This cherry-picks one entry (ChatGPT+Neo-S in Table 1) while ignoring the consistent pattern across all settings. The overall evidence is strong across dozens of comparisons.
4. **"Discrepancy between paragraph and sentence limited-data gains."** Removed. Paragraph-based 2ST and sentence-based SID are fundamentally different tasks with different baselines, difficulty levels, and metrics (test power vs. AUROC). No inconsistency exists.
5. **"XSum dataset mentioned but not used."** Removed. Results may be in the stripped appendix.
6. **"Overstates novelty (pioneering optimization mechanism)."** Removed. The claim is scoped to MMD optimization *in the context of multi-population MGT detection*, which is a fair characterization.
7. **"Broken wrapfig / missing appendix proofs."** Removed per hard rules (parser artifacts and stripped appendix).
8. **"Missing hyperparameters" as a reproducibility concern.** Demoted to Trivial. The paper likely includes these in the appendix.
9. **Strength Finder strengths about "importance of the problem" and "sycophancy-like generic praise."** Removed. Only concrete, specific strengths are retained.

## Novel Insights

None beyond the paper's own contributions. The key insight — that the intra-MGT similarity term \(k(y,y')\) drives variance growth when training data comes from multiple populations, and that removing it during kernel optimization yields a more stable and transferable detector — is clearly stated by the authors. The reviews do not surface a new angle on the paper beyond what it already articulates.

## Suggestions

1. **Validate the training–testing alignment claim.** Provide a dedicated experiment comparing detection performance (on every dataset and model) when using MPP vs. MMD as the test statistic with the MPP-trained kernel. This would either confirm that the two are indeed "almost identical" (as claimed) or quantify the gap.
2. **Add a direct variance-reduction measurement.** Show per-epoch or per-run estimates of \(\hat{\sigma}^2_{\mathfrak{H}_1}\) on held-out test data for MMD-D vs. MMD-MP, complementing Figure 1 with real-text data and numeric summaries.
3. **Include an ablation study.** Compare MMD-MP against a version of full MMD trained with a variance-penalized objective (without dropping \(k(y,y')\)), and against a version that removes \(k(x,x')\) instead. This would isolate whether the removal of \(k(y,y')\) specifically is the critical design choice.
4. **Add statistical significance tests.** Report paired tests (e.g., paired t-test or bootstrap confidence intervals) for the main comparisons, especially where error bars overlap.
5. **Expand transfer evaluation.** Test transfer from different training LLM combinations (e.g., only small models, only large models) to a wider set of unseen LLMs to probe the generality of the transferability finding.
