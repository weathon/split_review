---
job_id: a26018b5-45c6-4b75-af4b-95f085d38b38
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: ck0aZTAnwK.pdf
paper: Pre-training under Infinite Compute
main_score_norm: 0.8
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, focusing on language model pre-training, scaling laws, optimization under data constraints, ensembling, regularization, and data efficiency.

## Minimum Quality
Pass ✅. The submission contains the expected scientific components, including abstract, introduction, related work, methodological development, experiments, quantitative results, discussion, ethics, and reproducibility. While I have several concerns about extrapolation, asymptote estimation, and some mathematical/formal imprecision, these are not fatal flaws and the paper clearly exceeds the minimum bar for scientific completeness and rigor.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find any hidden prompts, suspicious instructions to automated reviewers, or other manipulative content in the provided paper text.

# Expected Review Outcome:
## Summary
This paper studies language model pre-training in a regime where data is fixed and compute is effectively unconstrained. On a 200M-token web-text setup, the authors show that standard data-constrained strategies, mainly more epochs and larger models, eventually overfit, while aggressively tuned regularization restores monotone parameter scaling and enables asymptote-based evaluation of recipes. They further argue that ensemble scaling achieves a better loss asymptote than single-model parameter scaling, show that parameter scaling and ensembling can be composed, and provide additional evidence via data-scaling extrapolation, distillation, continued pre-training, and downstream evaluations.

## Strengths
1. The paper asks a timely and well-motivated question. The framing, namely what to do when compute grows faster than available text, is important and relevant for the community. The focus on fixed-data, unconstrained-compute pre-training is a useful complement to the usual Chinchilla-style compute-optimal perspective.

2. The empirical study is extensive for the main claim. The paper does not stop at a single intervention, but systematically compares standard epoching/parameter scaling, tuned regularization, ensemble scaling, joint scaling, distillation, and downstream transfer. This breadth gives the paper more value than a narrowly scoped “weight decay helps” story.

3. The observation that substantially larger weight decay is needed in this regime is interesting and practically useful. In **Figure 3** and the accompanying tuned-hyperparameter table on **Page 4**, the optimal weight decay rises from \(0.8\) at 150M to \(3.2\) at 600M/1.4B, which is far from conventional pre-training defaults. Even if the exact values are setup-dependent, the qualitative message is strong and actionable.

4. The paper does a good job using figures to support its core narrative. In particular, **Figure 2** on **Page 3** is effective: the left panel makes the overfitting-from-epoching point visually obvious, and the right panel shows that simply scaling parameters under a standard recipe yields very small gains and even reversals. Likewise, **Figure 4** on **Page 5** is persuasive in illustrating that scaling the number of independently trained members can produce a lower asymptote than scaling a single model’s size.

5. The asymptote-based viewpoint is a meaningful conceptual contribution. Evaluating recipes by the limiting value of a monotone scaling law, instead of by fixed compute, is a natural reframing for the stated regime. This is not merely cosmetic, because it changes what is being optimized and compared.

6. The paper provides nontrivial evidence that the validation-loss improvements are not completely detached from task performance. **Figure 9** on **Pages 8–9** shows a fairly consistent ordering between lower validation loss and lower average downstream error, and **Table 5** on **Page 35** gives a more granular picture. For example, the regularized 1.4B model improves the average score from 54.14 to 60.73 over the unregularized 1.4B model, and the 300M/600M/1.4B ensembles show further gains as \(K\) increases.

7. The distillation results are a useful practical bridge. **Figure 8** on **Page 8** shows that some of the ensemble gain can be compressed into a much smaller student, which matters because otherwise the proposal would be easy to dismiss as purely inference-cost inflation. The fact that the distilled 300M student can beat the regularized single-model asymptote is a strong practical result.

8. I appreciated that the paper openly discusses limitations of architecture choice and asymptote noise in the appendix, and that the main paper generally avoids grandiose theoretical overclaiming. The tone is mostly empirical and appropriately cautious in some places.

## Weaknesses
1. The central claims rely heavily on extrapolated asymptotes fit from very few points, and this is more fragile than the main text acknowledges. For the regularized recipe, the main asymptote in **Section 3** is fit from only four parameter counts, 150M, 300M, 600M, and 1.4B, using
\[
\hat{\mathcal{L}}_{D,N} = \frac{A_D}{N^{\alpha_D}} + E_D.
\]
Similarly, the ensemble and joint-scaling claims rely on nested power-law fits over small grids, see **Figure 5** on **Page 6**, **Figure 6** on **Page 6**, and **Figure 7** on **Page 7**. This matters because the headline claims, such as 3.43 vs 3.34 vs 3.17 asymptotes and especially the “\(5.17\times\) data efficiency” number, are not direct observations, they are products of stacked extrapolations. When conclusions hinge on differences of a few tenths in loss after multi-stage fitting, the paper should be much more careful in the main body about uncertainty quantification, confidence intervals, fit sensitivity, and alternative functional forms. The appendix admits the asymptotes are noisy, but the main paper still presents them rather cleanly and decisively.

2. The mathematical formalization of the ensemble likelihood is sloppy enough to create confusion about what objective is actually being evaluated. In **Appendix D.1** on **Page 27**, the paper defines
\[
\operatorname{LogitAvg}(M_{i\in[K]})(x) \propto \exp\left(\frac{1}{K}\sum_{i\in[K]}\log(M(x))\right).
\]
As written, this expression ignores the index \(i\) inside \(M(x)\), and more importantly it conflates averaging logits with averaging log probabilities. If the ensemble is truly averaging logits tokenwise before softmax, then the sequence likelihood is not generally proportional to the exponential of the average log-likelihoods. If instead the authors mean geometric averaging of model probabilities, that is a different ensemble definition. Since the paper’s loss comparisons are based on this object, the formal definition should be corrected. At minimum, the notation should distinguish token-level logits \(z_i(x_t\mid x_{<t})\), token probabilities \(p_i(\cdot\mid x_{<t})\), and the induced sequence likelihood under the chosen combination rule.

3. The claim in **Section 4.3** that the order of limits does not matter is only justified under a strong monotonicity assumption, and the paper does not really establish this where it matters. The text states that as long as
\[
f(N,K) := \min_H \mathcal{L}(\mathcal{E}_{\mathcal{A}}(D,N,K,H))
\]
is monotone in \(N\) and \(K\) with the other fixed, the order of limits is irrelevant. But the main paper also says that for ensembles they cannot fully find locally optimal hyperparameters and instead use the heuristic of doubling epochs and halving weight decay. This undermines the empirical basis for monotonicity of the actual optimized function \(f\). In other words, the object whose monotonicity is needed is the fully tuned optimum over \(H\), yet the object being estimated in practice is partly heuristic. This gap matters because the double-limit construction is one of the paper’s main conceptual claims.

4. The architecture confound around the 1.4B model is not minor. On **Page 23**, **Table 2** shows the 1.4B model has only 16 layers, compared to 24 layers at 600M, meaning the scaling trajectory is not a clean family with fixed aspect ratio. The paper itself acknowledges in **Appendix C.5** on **Page 27** that the 1.4B model “trades depth for width” and that this was only recognized later. This matters directly because the main parameter-scaling law in **Figure 3** and several key asymptotic fits use this point. If one of only four data points is architecturally off-family, then the fitted exponent and asymptote are less trustworthy. The rebuttal appendix apparently adds 1.5B and 3.2B checks, which is useful context, but the main-paper evidence remains weaker than the central claims would ideally require.

5. The paper’s novelty is somewhat mixed. The main empirical interventions, strong regularization, ensembling, and distillation, are classic tools. The paper’s strongest claim is really about their role in a specific regime and about asymptote-based evaluation. That is still interesting, but the manuscript sometimes edges close to overselling simplicity as discovery. For example, the result that independent ensembles outperform a single model at fixed total parameter budget in a data-limited regime is plausible from long-standing variance-reduction and multi-view intuitions, and the paper’s own related work already cites classical and recent ensembling literature. I do think the combination and regime study are publishable, but the paper should position itself more as a careful empirical reframing than as a fundamentally new algorithmic direction.

6. The downstream validation is encouraging but still narrow relative to the breadth of the claims. In the main paper, **Section 7** and **Figure 9** evaluate only PIQA, SciQ, and ARC-Easy. **Table 5** on **Page 35** confirms the gains, but these are all relatively lightweight benchmarks and close in style to pre-training-eval probes for small models. If the paper wants to argue that its interventions “generalize to downstream benchmarks” in a broader sense, the evidence in the main paper is limited. This matters because some interventions that improve validation perplexity under repeated-data regimes can distort calibration, diversity, or instruction-following in ways that would not show up here.

7. The comparison protocol is not always fully fair when the quantity of interest changes across sections. In **Section 4**, the paper justifies treating an ensemble’s total parameter count as \(NK\) because forward-pass FLOPs are approximately linear in parameter count. That is reasonable for rough comparison, but it sweeps away important inference-side differences, including memory footprint, parallelization assumptions, latency, and serving complexity. This matters because some statements, especially around “better to train multiple smaller models instead of a single larger model,” can be read too broadly. The result is valid for validation loss under their unconstrained-compute framing, but much less so as a practical recommendation unless one also accepts unconstrained inference compute.

8. The hyperparameter search procedure is stronger than ad hoc tuning, but its guarantees are overstated. In **Appendix C.1** on **Pages 23–24**, the paper defines locally optimal hyperparameters over a discrete neighborhood and says that under certain assumptions they are also globally optimal, giving coordinatewise convexity-like intuition. In a setup where the tuned variables include learning rate, epoch count, and very large weight-decay changes on a discrete grid, this assumption is doing a lot of work. The main text repeatedly uses phrases like “correctly tuning regularization,” which sounds stronger than what is actually established. Since many conclusions depend on these tuned frontiers, the paper should more clearly separate “best found under a local discrete search” from “optimal.”

9. Some important parts of the presentation are more intuitive than precise. For instance, the use of “data efficiency” via interpolation from a fitted data-scaling law in **Section 5.1** is not invalid, but it can give a false sense of direct measurement. The quantity \(\frac{D'}{D}\) is model-based and inherits all extrapolation assumptions. Likewise, in **Figure 1** and **Figure 7**, the visual presentation of “\(5.17\times\) less data” reads quite definitive, while it is actually several layers removed from direct observation. The paper would benefit from visually and verbally distinguishing observed wins from fitted/extrapolated wins much more sharply.

10. There are a few concrete clarity and notation issues. The objective in **Section 2** is written as \(\mathcal{L}_D^*=\min_H \mathcal{L}(\mathcal{A}(D,H))\), but elsewhere the algorithm clearly depends on \(N\), \(E\), and possibly seed \(Z_i\). The notation is not wrong if \(H\) subsumes everything, but then later formulas often expose some variables and hide others inconsistently. Similarly, the ensemble formalization mixes algorithmic notation and model notation in ways that make the derivations harder to verify than necessary.

## Questions
1. The main conclusions depend on fitted asymptotes. Could the authors provide uncertainty estimates for the asymptote values in **Figures 3, 4, 5, 6, and 7**, for example via bootstrap over seeds, leave-one-point-out sensitivity, or fits under alternative functional forms such as \(A N^{-\alpha}+E\) vs \(A(N+B)^{-\alpha}+E\)? This would materially increase my confidence in the claimed ranking of recipes.

2. Relatedly, how robust is the ordering regularized single-model asymptote \(>\) ensemble asymptote \(>\) joint-scaling asymptote if one removes the 1.4B point from the fits, given the architecture mismatch noted around **Table 2** and **Appendix C.5**? A response on this would be very helpful.

3. Please clarify the exact definition of the ensemble predictor. Is inference done by averaging token logits before softmax, averaging token probabilities, or geometrically averaging sequence probabilities? The formula in **Appendix D.1** appears inconsistent with “average their logits” in the main paper.

4. For the double-limit argument in **Section 4.3**, can the authors be more explicit about what empirical evidence supports monotonicity of
\[
f(N,K)=\min_H \mathcal{L}(\mathcal{E}_{\mathcal{A}}(D,N,K,H))
\]
given that the ensemble hyperparameters are not fully optimized and instead partly selected by heuristic? If monotonicity only holds for the heuristic family explored, that is a weaker claim and should be stated as such.

5. In **Table 5** on **Page 35**, some ensemble improvements are modest and occasionally uneven across tasks, especially at smaller \(K\) or across model sizes. Could the authors provide per-task calibration or variance analyses, not just accuracy, to show whether the gains reflect better language modeling generally versus benchmark-specific effects?

6. The continued pre-training results in **Table 1** are intriguing, especially the \(K=8\) ensemble beating the 73B-token baseline. Can the authors clarify how much of that gain is attributable to ensembling versus lower batch size and epoching, and whether the same asymptote logic is expected to transfer to CPT in a principled way rather than by analogy?

7. The paper argues that heavy weight decay is crucial. Did the authors test whether other regularizers, such as dropout, label smoothing, data noising, or unique reshuffling every epoch, could produce similar monotone scaling? Even negative results would improve the scientific value by clarifying whether weight decay is special or just the best among tried baselines.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
The paper discusses increased compute use in **Section 11**, but I do not see a paper-specific ethics issue that requires dedicated ethics review beyond ordinary considerations for language-model pre-training research.

## Soundness Rating
3: good. The empirical work is substantial and most core observations are supported, but some of the strongest claims depend on fragile extrapolations, partially heuristic tuning, and a few formal imprecisions.

## Presentation Rating
3: good. The paper is generally clear, well organized, and supported by effective figures and tables, but some notation and mathematical definitions, especially around ensembles and asymptotic claims, need tightening.

## Contribution Rating
4: excellent. Despite the concerns above, I think the paper makes a meaningful contribution by reframing evaluation for fixed-data, compute-rich pre-training and by demonstrating a compelling empirical recipe built from regularization, ensembling, and distillation.

## Overall Rating
8: Accept, good paper (poster). I have real reservations about the asymptotic extrapolation story and would like the mathematical formalization to be cleaner, but the empirical findings are strong enough, the question is important enough, and the practical takeaways are useful enough that I would support acceptance.

## Reviewer Confidence
4: confident. I am confident in the overall assessment and checked the main empirical and mathematical claims carefully, though some conclusions hinge on extrapolation rather than directly observed regimes.