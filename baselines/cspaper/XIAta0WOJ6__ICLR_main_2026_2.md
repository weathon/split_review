---
job_id: 043ae6f1-5f14-484a-b651-7a996b6ee360
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: XIAta0WOJ6.pdf
paper: Faster Gradient Methods for Highly-Smooth Stochastic Bilevel Optimization
main_score_norm: 0.8
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, specifically optimization and learning theory for stochastic bilevel optimization, with relevance to meta-learning and hyperparameter optimization.

## Minimum Quality
Pass ✅. The paper contains the expected components, including abstract, introduction, methodological development, complexity analysis, lower bound, experiments, and conclusion; it also presents a concrete algorithm, formal claims, and quantitative results. While there are notable limitations in empirical scope and some exposition issues, these do not rise to the level of a desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, suspicious instructions to automated reviewers, or other manipulative content in the provided paper text.

# Expected Review Outcome:
## Summary
This paper studies stochastic bilevel optimization in the nonconvex-strongly-convex setting under standard stochastic gradient assumptions, and focuses on improving the sample complexity of fully first-order methods. The main idea is to reinterpret F$^2$SA as a forward finite-difference approximation of the hyper-gradient, then generalize it to an F$^2$SA-$p$ family using higher-order finite differences under higher-order smoothness in the lower-level variable $y$, yielding an upper bound of $\tilde{\mathcal O}(p\epsilon^{-4-2/p})$. The paper also provides an $\Omega(\epsilon^{-4})$ lower bound via reduction from single-level stochastic optimization, and includes experiments on a bilevel logistic regression benchmark.

## Strengths
1. The paper has a clear theoretical contribution. The reinterpretation of F$^2$SA through the lens of finite-difference hyper-gradient approximation, especially Eq. (8) and Eq. (9) in Section 3.1, gives a clean conceptual bridge between penalty-based first-order bilevel methods and numerical differentiation. This is not just cosmetic, it directly motivates the proposed F$^2$SA-$p$ family.

2. The main complexity improvement is meaningful and technically interesting. Theorem 3.1 gives a progression from the known $\tilde{\mathcal O}(\epsilon^{-6})$ regime toward $\tilde{\mathcal O}(\epsilon^{-4})$ as $p$ grows, which addresses a natural open question raised by the gap to the single-level lower bound. The dependence $\tilde{\mathcal O}(p\epsilon^{-4-2/p})$ is easy to interpret and captures the benefit of higher-order smoothness in a transparent way.

3. The lower-bound discussion is useful and strengthens the story. Theorem 4.1 is not extremely deep in construction, since it uses a separable reduction, but it does serve an important role: it shows that the paper is not merely improving an upper bound in a vacuum. This improves the paper’s scientific value because the upper and lower results are presented as part of one coherent complexity picture.

4. I appreciated that the paper is explicit about the assumptions and where the gains come from. Section 2.2 does a decent job distinguishing this setting from stochastic Hessian assumptions, mean-squared smoothness, and jointly higher-order smoothness assumptions. This makes it easier to see what is actually new here.

5. Table 1 is helpful as a compact summary of the complexity landscape. In particular, the comparison between prior F$^2$SA rates and the new F$^2$SA-$p$ rate makes the claimed improvement legible at a glance. I also appreciate that the table exposes the nontrivial condition-number dependence instead of sweeping it under the rug.

6. Figure 1, although limited in scope, does support the claim that higher-order variants can be practically competitive on the chosen learn-to-regularize benchmark. In the left panel, the F$^2$SA-$p$ curves consistently sit below the original F$^2$SA curve in test loss over much of training, and in the right panel they generally reach higher test accuracy than the original first-order variant. So the figure is at least directionally consistent with the theoretical message that better finite-difference approximations can help.

7. The paper has some nice technical details that are easy to miss on a superficial read. For example, Lemma 3.1 is presented in a form that directly interfaces with vector-valued quantities, and the algorithmic discussion around odd versus even $p$ is thoughtful rather than purely asymptotic. The remark that F$^2$SA-2 may be especially appealing because the per-iteration number of lower-level problems does not increase relative to F$^2$SA is practically relevant.

## Weaknesses
1. The empirical section is too thin relative to the ambition of the theoretical claims. The paper’s main message is about complexity improvement for stochastic bilevel optimization under higher-order smoothness, but Section 5 evaluates only one main benchmark in the main paper, namely logistic regression on 20 Newsgroups, with a fixed inner-loop length $K=10$ and $T=1000$ outer steps. This is simply not enough to establish that the proposed family is robustly useful, or even to understand when higher $p$ helps versus hurts. Figure 1 shows one task and one evaluation axis, but it does not probe sensitivity to noise, dimensionality, condition number, or lower-level curvature. Since the whole paper is about a tradeoff between approximation order and oracle cost, the lack of broader empirical stress-testing matters.

2. The experiments do not align tightly with the theoretical metric. The theory is entirely about SFO complexity to reach an $\epsilon$-stationary point, whereas Figure 1 reports test loss and test accuracy versus number of outer-loop iterations. That is a perfectly reasonable practical metric, but it is not a good proxy for the claimed complexity improvement because different methods have different per-iteration costs. In particular, F$^2$SA-$p$ solves multiple lower-level problems per outer iteration, and the text itself emphasizes this. So plotting only against outer-loop iterations is potentially misleading. A more honest presentation would include performance versus total stochastic oracle calls, or at least wall-clock time, especially because the main claimed advantage is sample complexity. As it stands, Figure 1 is suggestive but not well matched to the theorem statements.

3. Table 1 is informative but also exposes an unresolved issue that the paper somewhat underplays, namely the large condition-number dependence. The proposed upper bound in Table 1 is $\mathcal O(p\kappa^{9+2/p}\epsilon^{-4-2/p})$, while the lower bound shown there is only $\Omega(\epsilon^{-4})$ and does not reflect comparable $\kappa$ dependence. The text does acknowledge this gap, but the practical significance of the result is therefore narrower than the headline may suggest. If $\kappa$ is moderate or large, the asymptotic gain in $\epsilon$ may be partly overwhelmed. This matters because bilevel problems are often ill-conditioned in practice.

4. The paper relies on a fairly strong higher-order smoothness assumption in $y$, and the practical reach of that assumption is not convincingly justified. Assumption 2.5 requires high-order Lipschitz continuity of derivatives of $\nabla f$ and $\nabla g$ with respect to $y$. The examples on Pages 4 to 5 focus on logistic-regression-based hyperparameter tuning with smooth parameterizations such as softmax and diagonal exponentials, which are indeed favorable. But this is a relatively special corner of bilevel optimization. The paper gestures to broader machine learning applications in the introduction, including adversarial training and reinforcement learning, yet the high-order smoothness requirement seems much less plausible there. This weakens the practical significance of the claimed acceleration.

5. Some mathematical statements are too compressed to be easy to validate from the main paper alone. A central one is Lemma 3.2 on Page 7, which states that $\frac{\partial^{p+1}}{\partial \nu^p \partial \mathbf{x}}\ell_\nu(\mathbf{x})$ is $\mathcal O(\kappa^{2p+1}\bar L)$-Lipschitz in $\nu$, derived from the high-dimensional Faà di Bruno formula. That is exactly the kind of result carrying most of the technical burden, because it plugs directly into the finite-difference error guarantee and then into Theorem 3.1. But in the main paper this appears almost as a black box. I am willing to believe the appendix contains the details, but the main text gives very little intuition for why the derivative growth scales as $\kappa^{2p+1}$ and why the required assumptions are sufficient. For a theorem-driven optimization paper, this is a nontrivial exposition weakness.

6. There are some notation and presentation glitches that make the technical narrative rougher than it should be. A few examples: on Page 8, Theorem 3.1 refers to the class $\mathcal F^{nc\cdot\kappa}(L_0,\dots,L_{p+1},\mu,\Delta)$, which appears inconsistent with Definition 2.2 and looks like a typo; there are multiple notational inconsistencies around $\bar L$, $\tilde L$, and the function-class superscripts; Eq. (9) appears to be missing a left delimiter in the displayed fraction; and some references are malformed in the bibliography. None of these are fatal, but in a theory paper they add friction and make it harder to carefully verify the claims.

7. The lower bound is useful, but it is also somewhat limited in what it tells us about the proposed upper bound. Theorem 4.1 uses a fully separable construction with $f(\mathbf x,\mathbf y)\equiv f_U(\mathbf x)$ and a quadratic lower-level function. This is enough to transfer the single-level $\Omega(\epsilon^{-4})$ hardness, but it does not engage with the specific structural challenges introduced by hyper-gradient approximation or with the higher-order smoothness assumptions that motivate F$^2$SA-$p$. So while the theorem supports a general floor on complexity, it does not really explain whether the residual gap for small $p$, or the heavy $\kappa$ dependence, is an artifact of the analysis or an inherent difficulty of bilevel structure.

8. The algorithmic tradeoff around choosing $p$ is underdeveloped. The paper says that higher $p$ improves the finite-difference truncation error, but also requires solving more lower-level subproblems per iteration and presumably increases sensitivity to stochastic noise. This is visible already in Algorithm 1, where the sum over $j=-p/2,\dots,p/2$ directly increases work. Yet the paper gives almost no practical guidance for selecting $p$, and Section 5 does not really isolate the sweet spot. Figure 1 includes $p\in\{2,3,5,8,10\}$, but there is no accompanying analysis of why some orders are better than others, or whether performance degrades once noise amplification outweighs approximation benefits.

9. The presentation of Algorithm 1 leaves some implementation-relevant details underspecified. For instance, in line 6 and line 11 the paper says “sample random i.i.d indexes”, but the exact stochastic oracle usage is a bit murky, especially regarding whether the same samples are shared across all $j$ values or not. Likewise, line 13 uses $F_x(\mathbf x_t,\mathbf y_{t+1}^j;\xi_t^x)$ and $G_x(\mathbf x_t,\mathbf y_{t+1}^j;\zeta_t^x)$ inside the $j$-sum, but the indexing notation suggests shared randomness where one might have expected independent samples per $j$. This may be intentional for variance reasons, but the paper should say so explicitly because it affects both analysis and reproducibility.

10. The normalized outer update in Algorithm 1, line 14, is somewhat unusual for this context and deserves more justification in the main text. Remark 3.1 says the normalization helps control the change of $\mathbf y_{j\nu}^*(\mathbf x_t)$ and simplifies analysis, and claims that standard gradient steps should also work via more involved analysis. That may be true, but this is not a minor cosmetic choice. If the algorithm analyzed in the theorem is not the natural practical variant used in prior F$^2$SA work, the paper should do more to explain the effect of normalization on convergence behavior and practical performance.

11. The experimental comparison is missing some ablation detail that would be very valuable. Since the proposed contribution is specifically the finite-difference order, I would have liked a table reporting per-method oracle cost, chosen $\nu$, and the effect of fixing the same oracle budget across $p$. Right now Figure 1 gives the impression that larger $p$ is often better, but without a budget-matched comparison that impression is not scientifically very sharp.

## Questions
1. The most important missing experimental clarification is this: can the authors report results versus total stochastic oracle calls, not just outer-loop iterations, for all methods in Figure 1? Since Theorem 3.1 is fundamentally an SFO-complexity statement, this would substantially increase my confidence that the empirical section is aligned with the theory.

2. Can the authors provide more practical guidance on how to choose $p$? In particular, what criterion should a practitioner use to decide between F$^2$SA, F$^2$SA-2, and higher-order variants such as $p=5,8,10$? If there is a bias-variance or truncation-noise tradeoff, please spell it out.

3. For Algorithm 1, are the stochastic samples in line 11 shared across all $j$ values inside the estimator $\Phi_t$, or should there be separate samples indexed by both $i$ and $j$? Please clarify the intended oracle model and whether sample sharing is important for the analysis.

4. Theorem 3.1 depends on the bound in Lemma 3.2. Could the authors add more intuition in the main paper for why $\frac{\partial^{p+1}}{\partial \nu^p \partial \mathbf{x}}\ell_\nu(\mathbf{x})$ scales with $\kappa^{2p+1}$, and which terms in the implicit differentiation chain dominate this growth? A short sketch would make the result much easier to digest.

5. In Figure 1, some higher-order variants appear close to one another. Do the authors observe diminishing returns beyond $p=2$ or $p=3$ in practice? If so, that would be worth discussing explicitly, because it may be the practically relevant takeaway even if the asymptotic theorem allows arbitrary $p$.

6. Could the authors add a compact ablation table giving, for each tested $p$, the effective per-iteration SFO cost and the best selected hyperparameters $(\eta_x,\eta_y,\nu)$? That would materially improve reproducibility and help interpret the empirical tradeoffs.

7. The paper claims in Remark 3.1 that the guarantees should also hold for standard, non-normalized gradient steps with a more involved analysis. Is there at least a partial argument or empirical evidence supporting that claim? This point matters for understanding whether normalization is merely a proof trick or a genuinely necessary algorithmic choice.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No ethics concerns identified from the paper. The work is a theoretical optimization paper with standard benchmark experiments and does not raise clear issues around privacy, fairness, safety, or human subjects.

## Soundness Rating
3: good. The technical direction is well motivated, the central claims are plausible and mostly well supported, and the theorem-lower-bound pairing is coherent. My main reservation is that some key technical ingredients are too compressed in the main paper and the empirical validation is narrower than the breadth of the claims.

## Presentation Rating
3: good. The paper is readable and the high-level story is clear, but there are enough notation inconsistencies, compressed derivations, and underexplained design choices that I cannot rate the presentation as excellent.

## Contribution Rating
3: good. The paper makes a meaningful contribution to stochastic bilevel optimization theory by connecting fully first-order penalty methods to higher-order finite differences and improving the known complexity under stronger smoothness assumptions. The contribution is real, though somewhat narrowed by the strength of the assumptions and limited empirical depth.

## Overall Rating
8: Accept, good paper (poster). I think this is a solid theory paper with a clean conceptual insight, a meaningful upper-bound improvement, and a useful lower-bound complement. The empirical section is too light and the exposition could be sharper in a few key places, but the core contribution is strong enough that I would support acceptance.

## Reviewer Confidence
4: confident. I am confident in the overall assessment and familiar with the surrounding optimization literature, though I did not independently verify every hidden technical step that is deferred outside the main paper.