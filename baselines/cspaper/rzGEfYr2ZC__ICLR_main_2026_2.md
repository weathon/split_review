---
job_id: 4892e540-a155-4f40-85ea-a83f765b2b32
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: rzGEfYr2ZC.pdf
paper: Don’t Be Greedy, Just Relax! Pruning LLMs via Frank-Wolfe
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, it studies post-training pruning for LLMs through a convex optimization and Frank-Wolfe lens, which directly fits optimization and large-scale machine learning.

## Minimum Quality
Pass ✅. The paper contains the expected scientific components, including abstract, introduction/related work, methodology, experiments with quantitative results, theory, and conclusion; despite several important issues, it meets the minimum bar for non-desk-reject review.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, suspicious instructions to automated reviewers, or other manipulative content in the provided paper text and figures.

# Expected Review Outcome:
## Summary
This paper studies layer-wise post-training pruning for LLMs by relaxing the binary mask-selection problem to a convex program over the convex hull of sparse masks, and solving the relaxation with Frank-Wolfe. The proposed method, SparseFW, is presented as a projection-free alternative to greedy pruning criteria such as Wanda and RIA, with support for unstructured and semi-structured sparsity. The paper provides empirical results on several GPT-style models and an approximation result relating the rounded relaxed solution to the original combinatorial mask-selection objective.

## Strengths
The paper has a clear central idea, replacing greedy one-weight-at-a-time reasoning with a convex relaxation of the mask problem and solving it using Frank-Wolfe. This is a reasonable and technically motivated perspective, and the paper does a good job connecting the feasible set in Equation (10) to a simple sparse LMO in Equation (12). The use of FW is not just name-dropping, the projection-free structure is actually aligned with the mask polytope considered here.

I appreciated the effort to reinterpret Wanda and RIA through the lens of single-step greedy optimization in Section 2.1, especially the derivation from Equation (4) to Equation (5), and the observation that Wanda’s saliency can be viewed as the exact solution to a single-coordinate pruning subproblem without reconstruction. Even if one may debate how far this reinterpretation goes, it helps sharpen the paper’s conceptual contrast against greedy baselines.

The implementation discussion in Section 2.3 is practically useful. Precomputing \(G = XX^\top\) and \(H = WG\) is a sensible engineering step, and the paper explains why this matters for calibration at long sequence lengths. This part makes the method more credible as a scalable layer-wise procedure rather than a purely abstract optimization proposal.

The empirical evaluation spans multiple reasonably modern LLM families, which is better than showing results on a single architecture. In **Table 1** there are several meaningful gains, especially at higher sparsity. For example, at 60% sparsity, SparseFW improves LLaMA-3.1-8B perplexity from 21.53 (Wanda) to 17.97 and improves zero-shot accuracy from 48.08 to 51.92; similar trends appear for Gemma-2-9B and Qwen2.5-7B. The gains are not universal, but the aggregate picture is directionally favorable, particularly for zero-shot accuracy.

The figures are useful and generally support the claimed mechanism. **Figure 2** is especially informative because it shows that the optimization is not merely improving one or two matrices, the per-layer local objective is reduced across many layers and matrix types. Likewise, **Figure 3** provides a useful sense of the iteration/sample tradeoff and suggests that the method is not completely brittle to calibration choices. **Figure 4** is also helpful because it visualizes the gap between improving the continuous relaxed objective and the degradation introduced by thresholding; that figure actually makes one of the paper’s own limitations visible, which I appreciate.

The paper does not oversell the local-global mismatch. The authors explicitly acknowledge in Section 2.3 and again in the conclusion that optimizing the local pruning objective alone is not sufficient, and that vanilla FW can hurt perplexity. That honesty is important here.

## Weaknesses
1. **The practical method that works well is materially different from the method that is theoretically motivated, and this gap is central rather than cosmetic.**  
   The clean story in the introduction is that the paper solves the relaxed mask selection problem with Frank-Wolfe and rounds the result. However, the actual practical recipe described on **Page 6, Section 2.3** says that unconstrained FW often yields worse final perplexity than Wanda, and that the method only works reliably after *fixing a fraction of high-Wanda-saliency weights as unprunable*. This is not a small tweak. By the authors’ own description, the best consistent performance occurs at \(\alpha = 0.9\), meaning 90% of the retained weights are dictated by Wanda and only the remaining 10% are optimized by FW. That substantially changes the contribution: in practice, the method is closer to “Wanda plus local refinement on a small subset” than to a standalone convex alternative to greedy pruning. This matters scientifically because the headline claim is about replacing greedy heuristics with a better relaxation-based optimizer, but the main empirical success actually depends on preserving a very strong greedy prior.

2. **The main paper omits the ablation that is most necessary to interpret the method, namely the dependence on \(\alpha\), and the appendix evidence substantially weakens the core claim.**  
   The main text states on **Page 6** that \(\alpha=0.9\) works best and that \(\alpha=0\) consistently underperforms baselines, but the relevant quantitative evidence is deferred to **Table 2 in the appendix**. Even taking the appendix claims at face value, this creates a serious interpretation problem: full FW, the cleanest realization of the proposed optimization principle, is often worse than the baseline. Moreover, the appendix table shows that the effect of \(\alpha\) is nontrivial and architecture-dependent. For instance, for DeepSeek-7B at 60% sparsity, the best value in **Table 2** is still worse than Wanda (12.21 or 11.99 etc. versus Wanda 11.44), so the practical story is much less uniform than the main paper suggests. This matters because without surfacing this ablation in the main paper, readers can easily overestimate how much of the final gain comes from Frank-Wolfe itself.

3. **There is a concrete algorithmic inconsistency in Algorithm 1, and it is not a minor typo because it affects the update validity.**  
   On **Page 5**, the text states “Throughout this work, we stick to the learning rate schedule \(\eta_t = \frac{2}{t+2}\).” But in **Algorithm 1, line 5 on Page 6**, the update is written as \(\eta_t \gets \frac{\pi}{t+2}\). If taken literally, \(\eta_0 = \pi/2 > 1\), which violates the convex-combination interpretation of the FW update in Equation (9) and can leave the feasible region. The appendix algorithm uses \(\frac{2}{t+2}\), so there is clearly an inconsistency between the main algorithm and the surrounding theory/text. This is exactly the kind of issue that should not survive in a paper built around a specific optimization algorithm.

4. **The warm-start story is mathematically muddled in the main algorithm, because the first FW step discards the warm start.**  
   In **Algorithm 1**, the method is described as starting from a binary warm-start mask \(M_0\). But with the stated FW schedule \(\eta_0=\frac{2}{2}=1\), the first update gives \(M_1 = V_0\), which completely overwrites \(M_0\). So the warm start has no effect after one iteration in the vanilla algorithm. That is directly at odds with the way the experimental setup is described in **Table 1**, where results are reported as “SparseFW (Wanda)” and “SparseFW (RIA)” as if the warm start meaningfully influences optimization. Presumably the practical variant with fixed coordinates preserves some warm-start information, but then that should be the main algorithm in the paper, not a simplified version whose first step nullifies the initialization. This matters because it obscures what is actually being compared in the experiments.

5. **The theoretical guarantee is only partially aligned with the method actually used in experiments, and the presentation of the theorem in the main paper is too loose to support the advertised claim.**  
   The introduction claims “combined with the convergence guarantees of FW, rounding the relaxed solution to integrality yields an approximate solution to the original combinatorial problem.” In the main paper, **Lemma 1 on Page 8** is stated informally and depends on \(Q\), but the full theorem in the appendix is for the row-wise formulation and for a point \(m^\varepsilon\) satisfying \(\sum_j m^\varepsilon_j = k\). The deployed practical method in Appendix B additionally fixes coordinates via \(\overline{M}\), effectively optimizing over a reduced feasible set. The main paper does not explain whether the theorem still applies to that constrained practical variant, which is the one actually needed for competitive perplexity. So the theory supports a simplified version, while the experiments rely on a modified version. This weakens the claim that the paper offers a theoretically justified practical pruning method.

6. **The approximation bound is very weak and the paper does not explain when it is informative in realistic LLM layers.**  
   In **Equation (13) of the appendix / Lemma 2**, the additive term scales like
   \[
   2\lambda_{\max}(Q)\Big(\min\{k,r\} + \sqrt{2r\min\{k,r\}}\Big),
   \]
   and in the high-sparsity regime becomes
   \[
   2\lambda_{\max}(Q)\Big(k + \sqrt{2d_{\text{in}}k}\Big).
   \]
   For typical LLM layer widths, this can be enormous. The paper never quantifies \(\lambda_{\max}(Q)\) or the resulting magnitude of the bound on actual layers, so the theorem is more of an existence statement than a meaningful performance guarantee. That is not inherently fatal, but then the abstract/introduction should be more restrained about “strong theoretical justification.” Right now the rhetorical weight of the theorem is larger than its practical interpretability.

7. **The empirical comparisons are not fully persuasive because the paper excludes a key strong baseline for end-task performance.**  
   On **Page 7**, the paper explicitly decides not to compare to reconstruction-based methods such as SparseGPT because those methods do not solve the same mask-selection objective. I understand the methodological rationale, but the paper simultaneously makes broad practical claims about final perplexity and zero-shot accuracy on LLM pruning. Once the claim is about end performance, omitting a major post-training pruning baseline becomes much harder to justify. The reader is left comparing against Wanda and RIA only, even though reconstruction-based methods are part of the actual competitive landscape for LLM pruning. This matters because improved optimization of the local objective is only valuable insofar as it translates into competitive final model quality.

8. **Some of the empirical gains in Table 1 are mixed enough that the narrative in the text feels smoother than the actual evidence.**  
   The paper says SparseFW “generally performs on par with or better than the baselines” in perplexity and “consistently outperforms” on zero-shot accuracy. The accuracy statement is roughly supported, but the perplexity side is more uneven. In **Table 1**, SparseFW is worse than Wanda in several cells, such as LLaMA-3.1-8B at 50% sparsity with Wanda warmstart (10.21 versus 10.09), DeepSeek-7B at 60% with both warmstarts (11.99 and 12.41 versus Wanda 11.44), and Qwen2.5-14B at 2:4 with Wanda warmstart (11.82 versus Wanda 11.37). These are not edge cases if the paper is claiming broad superiority. The text should separate “improves the local objective” from “improves end-task performance,” because the latter is demonstrably less robust.

9. **The paper leans heavily on the local pruning error, but the figures themselves expose a mismatch that is not sufficiently resolved.**  
   **Figure 2** shows substantial relative reduction in per-layer reconstruction error, in some layers very large reductions. However, **Figure 4** shows that continuous-mask optimization and thresholded-mask performance diverge for a long stretch, and the threshold residual remains clearly nonzero even after many iterations. Combined with the admission on **Page 6** that vanilla FW can worsen perplexity, the figures underscore that minimizing the relaxed local objective is not tightly coupled to the final pruning goal. In other words, the paper convincingly shows success on the proxy objective, but the proxy is not shown to be reliably faithful. This matters because the entire method is built around improving that proxy.

10. **The treatment of related work and positioning is somewhat selective.**  
   The paper positions itself primarily against Wanda, RIA, and SparseGPT-like greedy methods, and cites prior FW-for-sparsity work such as Miao et al. (2022) and Zimmer et al. (2025). But the distinction between “FW for pruning/training sparse networks” and “FW for post-training LLM mask selection” could be articulated much more clearly. As written, the paper risks sounding more different from previous FW-based sparsification work than it actually demonstrates. I do not think the paper is merely a repackaging, but the novelty case would be stronger with a more explicit comparison to prior FW sparsification formulations and why the present mask-polytope setup is materially different.

11. **Presentation is decent overall, but there are several notation and exposition issues around the core algorithm/theory interface.**  
   Examples include the inconsistent learning rate noted above, the switch between matrix-wise and row-wise formulations without always making the mapping precise enough, and the fact that the theoretical object \(Q\) is only clarified after the informal lemma. On **Page 8**, the text says \(Q\) “represents the Hessian of the objective function,” but the reader has to go to the appendix to see the exact row-wise definition \(Q=\mathrm{Diag}(w)XX^\top \mathrm{Diag}(w)\). For a theory-forward paper, the main paper should make these correspondences cleaner.

## Questions
1. The most important clarification is about the practical role of \(\alpha\). Could the authors move the \(\alpha\)-ablation from the appendix into the main paper and explicitly quantify, across models, how often \(\alpha=0\) underperforms the warmstart and how much of the gain remains when \(\alpha\) is small? This would substantially change my confidence in the claimed contribution.

2. Does the approximation guarantee still hold, perhaps after a straightforward modification, for the practical variant in **Appendix B** where a fixed mask \(\overline{M}\) is imposed and FW only optimizes over the remaining coordinates? If yes, please state the corresponding feasible set and theorem. If not, the paper should be more explicit that the theory does not cover the empirical method that performs best.

3. Please clarify the learning-rate inconsistency between **Page 5** and **Algorithm 1, line 5** on **Page 6**. Is \(\eta_t = \frac{2}{t+2}\) the actual schedule used in experiments? If so, please correct the main algorithm. If not, please explain how feasibility is preserved when \(\eta_t > 1\).

4. Relatedly, with \(\eta_0 = 1\), vanilla FW gives \(M_1=V_0\), which appears to erase the warm start. How then should one interpret “SparseFW (Wanda)” versus “SparseFW (RIA)” in **Table 1**? Is the distinction entirely due to the fixed set \(\overline{M}\), or is a different initialization/update used in practice?

5. Since the paper makes claims about final perplexity and zero-shot accuracy, can the authors provide at least one comparison to a strong reconstruction-based baseline such as SparseGPT on the same models/sparsity settings? Even one or two representative rows would help calibrate practical competitiveness.

6. Can the authors report the wall-clock/runtime or FLOP overhead per layer relative to Wanda and RIA? **Figure 3** suggests many iterations may be beneficial, but the actual computational tradeoff is not quantified in a way that helps judge practicality.

7. The theorem depends on \(\lambda_{\max}(Q)\). Can the authors estimate this quantity on a few representative layers and show whether the bound is remotely informative numerically, or whether it should be viewed as purely qualitative?

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No specific ethics concerns arise from the paper beyond standard dual-use considerations for efficient deployment of language models, and nothing in the submission appears to require separate ethics review.

## Soundness Rating
2: fair. The optimization formulation is meaningful and several derivations are useful, but the algorithmic inconsistency in Algorithm 1, the gap between the theoretical method and the practical variant, and the incomplete empirical comparison weaken confidence in the central claims.

## Presentation Rating
3: good. The paper is generally readable and well organized, with informative figures and tables, but there are important clarity issues around the exact practical algorithm, the warm-start interpretation, and the theorem-to-experiment connection.

## Contribution Rating
2: fair. The idea of applying a convex relaxation and Frank-Wolfe to layer-wise LLM mask selection is interesting, but the strongest empirical results depend heavily on freezing most of the mask using Wanda, which makes the practical contribution feel narrower than the framing suggests.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted.  
There is a real idea here, and the paper is more thoughtful than a routine pruning tweak. However, too much of the practical success seems to come from a Wanda-based safeguard rather than from vanilla FW itself, and the theory does not cleanly cover the version of the method that actually works best. Add the Algorithm 1 inconsistency, the warm-start ambiguity, and the lack of comparison to a stronger end-performance baseline, and I end up slightly below the bar for ICLR main track in its current form.

## Reviewer Confidence
4: confident. I am confident in the assessment, though not absolutely certain. I carefully checked the main derivations, algorithms, figures, and tables, but I did not verify every appendix-level proof detail line by line beyond consistency with the main claims.