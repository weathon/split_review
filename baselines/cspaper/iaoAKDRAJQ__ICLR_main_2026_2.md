---
job_id: 32df4e2e-688d-462f-804f-bddacfc1f5a2
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: iaoAKDRAJQ.pdf
paper: A Tale of Two Geometries: Adaptive Optimizers and Non-Euclidean Descent
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is squarely in optimization and learning theory, with a focus on adaptive methods, non-Euclidean geometry, and nonconvex optimization, all well within ICLR scope.

## Minimum Quality
Pass ✅. The paper has a complete research structure for a theory paper, including abstract, introduction, related work, technical development, main results, and conclusion; while there are no empirical experiments, the submission is framed as a theoretical contribution and provides substantial theorem-level evidence.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, suspicious reviewer-directed text, or other manipulative content in the provided paper text and figures.

# Expected Review Outcome:
## Summary
This paper studies the relationship between adaptive optimizers and normalized steepest descent under non-Euclidean geometries, arguing that the two families rely on different geometric regularity conditions. The main technical claims are that adaptive smoothness, rather than standard norm smoothness, characterizes adaptive-method convergence in the nonconvex setting, that adaptive smoothness enables accelerated convex rates for adaptive methods, and that an analogous adaptive variance notion yields dimension-free stochastic guarantees for NSD that are impossible under standard variance assumptions.

## Strengths
The paper has a clear conceptual objective, namely to separate the geometry exploited by adaptive preconditioning methods from the geometry exploited by normalized steepest descent, even when the two algorithms can coincide algorithmically in special cases. That question is interesting, timely, and relevant to the recent optimizer literature around Adam, Lion, Shampoo, and Muon.

A genuine strength is the breadth of the unified framework. Algorithm 1 on **Page 5** covers cumulative, EMA, and weighted variants, and the discussion in **Section 3.1** ties this to diagonal AdaGrad/Adam, scalar AdaGrad-Norm, full-matrix AdaGrad, and one-sided Shampoo. Even if some parts are dense, the framework does create a common language for discussing these methods.

The main theorem-level contributions are substantial for a theory paper. In particular:
- **Theorem 3.1** and **Theorem 3.2** extend adaptive-smoothness-based guarantees to the nonconvex setting.
- **Theorem 4.3** gives an accelerated convex rate under adaptive smoothness.
- **Theorem 4.5** and **Theorem 4.7** provide an upper/lower-bound contrast for stochastic NSD under adaptive variance versus standard variance.

I also found **Lemma 3.3** to be the technical centerpiece of the paper. The matrix inequality route is nontrivial, and the distinction between commutative and noncommutative preconditioner classes is conceptually meaningful. The special-case improvement in **Lemma 3.3** for commutative \(\mathcal H\) explains why diagonal cases behave better than general structured preconditioners; this is one of the sharper insights in the submission.

The geometric picture around **Figure 1** is helpful. The left panel, showing the \(\ell_\infty\) unit ball as the intersection of diagonal-matrix-induced ellipsoids, and the right panel, showing the \(\ell_1\) dual ball as the union of dual ellipsoids, gives an intuitive explanation for the supremum/infimum duality in **Equation (4)**. For a paper this abstract, that visual is doing real work rather than serving as decoration.

The lower-bound side is another strength. Too many theory papers stop at upper bounds and hand-wave the necessity of assumptions. Here, the contrast between **Theorem 4.5** and **Theorem 4.7** is one of the more convincing parts of the paper, because it tries to show that adaptive variance is not just a stronger assumption in the trivial sense, but can buy qualitatively different rates.

Finally, the paper is well positioned around recent work by the same line of research and adjacent optimizer theory. The framing around adaptive smoothness versus standard smoothness is coherent and mostly consistent throughout the paper.

## Weaknesses
My main concern is that the paper sometimes overstates “precise characterization” while the actual statements are upper bounds with extra logarithmic and structural overheads. In the abstract and introduction, the language suggests that adaptive smoothness “precisely characterizes” convergence of adaptive optimizers. But in the main body, the guarantees in **Theorem 3.1**, **Theorem 3.2**, and **Theorem 4.3** all include nontrivial additional factors such as \(\log d\), \(\hat O(\log^2 d)\), stability terms involving \(\epsilon\), and the matrix quantity \(\|S_T\|_{\mathrm{op}}\). That is not a fatal issue, but the paper should be more careful in distinguishing “the rate depends on \(\Lambda_{\mathcal H}(f)\)” from “\(\Lambda_{\mathcal H}(f)\) precisely characterizes the complexity.” As written, the rhetoric is a bit stronger than the theorems comfortably support.

There are several clarity and notation problems in the mathematical exposition, and some are in core definitions rather than harmless typos. A concrete example is **Definition 2.4** on **Page 4**, where the second expression for adaptive smoothness uses \(\nabla^d f(\mathbf x)\), which appears to mean the Hessian but is not standard notation and is inconsistent with the surrounding text. Another example is the “Comparison between two smoothness notions” paragraph on **Page 5**, where the displayed equation is circular and apparently malformed:
\[
L_{\|\cdot\|_{\mathcal H}}(f)= \sup \frac{\|\nabla f(x)-\nabla f(y)\|_{H,*}}{\|x-y\|_H} \ge \sup \frac{\|\nabla f(x)-\nabla f(y)\|_{\mathcal H,*}}{\|x-y\|_{\mathcal H}} = L_{\|\cdot\|_{\mathcal H}}(f).
\]
As written, the leftmost and rightmost quantities are identical, and the middle ratio mixes \(H\) and \(\mathcal H\) in a way that does not match the preceding argument. This is not cosmetic, because the whole paper leans on the inequality \(L_{\|\cdot\|_{\mathcal H}}(f)\le \Lambda_{\mathcal H}(f)\). If the central comparison display is garbled, it undermines reader confidence in the surrounding formalism.

Relatedly, **Equation (3)** on **Page 3** is conceptually slippery. The paper “minimizes both sides” of an NSD guarantee over \(\mathbf H\), obtaining
\[
\inf_{\mathbf H}\min_t \|\nabla f(x_t)\|_{\mathbf H,*}
\le O\!\left(\sqrt{\frac{\Delta_0}{T}\inf_{\mathbf H} L_{\|\cdot\|_{\mathbf H}}(f)}\right).
\]
But the left-hand side is a post hoc infimum over norms after generating one trajectory \(\{x_t\}\), whereas the right-hand side is interpreted as saying Adam “automatically identifies the best diagonal norm.” Those are not the same logical statement. This is an important conceptual bridge in **Section 2.1**, and right now it is presented too casually. At minimum, the authors need to explain the quantifier order more carefully: is the comparison about a single trajectory, a best fixed geometry chosen before optimization, or an online adaptive mechanism?

The main algorithms are presented too noisily in the paper body. **Algorithm 2** and **Algorithm 3** on **Page 8** are especially hard to parse because several lines are visibly malformed, for example “\(g_t \leftarrow \nabla f_t^{\alpha_t,\bar x_t}(x_t)\) where \(f_t^{\alpha_t,\bar x_t}\) is in (8)” is partially garbled, and the NSD-with-momentum update shows “\(u_t\leftarrow \arg\max \{m_t,u\}\)” with formatting that obscures the actual optimization domain. For a theory paper whose novelty rests heavily on the exact update rules, this level of typesetting damage is a real presentation weakness.

The acceleration result in **Theorem 4.3** is interesting but rests on a fairly strong and somewhat awkward bounded-iterate assumption, namely \(\max_t \|x_t-x^*\|_{\mathcal H}\le D\). The paper acknowledges in **Remark 4.4** that \(D\) is unknown and then defers the projected fix to Appendix E.2. Since the accelerated guarantee is one of the flagship contributions in the main text, it would help to either present the projected version in the main paper, or at least discuss more explicitly how restrictive the unprojected assumption is. Right now, the theorem reads a bit like “acceleration is possible, provided you already know the radius of the region containing all iterates.” That matters because the practical and conceptual punchline of Section 4.2 depends on this result.

The stochastic story is interesting, but the noise assumptions are not as operational as the paper makes them sound. **Definition 4.1** introduces adaptive gradient variance by minimizing over \(\mathbf H \in \mathcal H\) with \(\operatorname{Tr}(\mathbf H)\le 1\), and then taking a supremum over all \(t\) and all \(x\). This is mathematically clean, but from a modeling standpoint it is a strong uniform assumption over the entire domain. The paper calls it a weaker assumption than bounded covariance in one sense, but for practitioners or even theorists trying to verify the assumption on concrete problems, it is not clear when \(\sigma_{\mathcal H}\) is finite, small, or estimable. This does not invalidate the theorem, but it does limit the usability of the result and should be discussed more candidly.

The paper lacks any empirical or even synthetic quantitative validation. I am not demanding a large-scale deep learning benchmark from a theory submission, but the absence of any small experiment, numerical sanity check, or even toy example is noticeable given the paper’s repeated claims about the “benefit” of adaptive smoothness and adaptive variance. A modest synthetic study could have illustrated, for example, a function where \(L_{\|\cdot\|_{\mathcal H}}(f)\) and \(\Lambda_{\mathcal H}(f)\) differ substantially, or a stochastic setting where adaptive variance predicts a dimension-free behavior while standard variance does not. Without that, the submission remains quite abstract, and readers are left to take the geometric conditions on faith.

There are places where the exposition blurs whether the comparison is algorithmic, analytical, or complexity-theoretic. For example, in the introduction and **Section 2.1**, the paper moves from “Adam without EMA coincides with NSD under the corresponding norm” to “adaptive optimizers and NSD exploit different smoothness notions.” That is a valid high-level message, but the exact sense of “exploit” is not always stable. Is the claim that the methods behave differently, that their known proofs require different assumptions, or that different assumptions are necessary for optimal rates? The paper uses all three flavors at different moments. Tightening this would improve both precision and impact.

The figure discussion is helpful, but **Figure 1** also exposes a missed opportunity. The figure only illustrates the diagonal \(\ell_\infty/\ell_1\) case, even though one of the paper’s main messages is a general theory for arbitrary well-structured preconditioner sets. Given how central the generalization beyond diagonal matrices is, a second visual or example for a noncommutative case would have strengthened the paper. As it stands, the only concrete picture readers get is the easiest commutative setting.

The paper has no quantitative results tables in the main text, which becomes a weakness for assessing empirical support and the practical significance of the theory. Since the central claims are about benefits such as acceleration and dimension-free dependence, the absence of even a small benchmark or ablation table means the reader cannot judge whether these benefits appear in any finite-sample regime or only at the level of asymptotic worst-case theory.

Finally, while the appendix is substantial, some claims in the main paper rely on deferred details enough that the main text occasionally feels like a compressed theorem catalog. For a paper with this many moving parts, the authors need to do more in the main text to guide the reader through what is truly new, what follows from prior frameworks, and where the delicate proof steps actually enter. Right now, the spicy version is: the paper has serious ideas, but it makes the reader work harder than necessary to verify that those ideas are stated correctly.

## Questions
1. In **Equation (3)** and the surrounding discussion on **Page 3**, can the authors clarify the quantifier order behind the “minimize both sides over \(\mathbf H\)” argument? As written, the left-hand side looks like a post hoc choice of norm after seeing the trajectory, which is weaker than saying the algorithm adaptively competes with the best fixed \(\mathbf H\). A precise statement here would materially increase my confidence in the conceptual bridge from NSD to adaptive smoothness.

2. Please correct and clarify the smoothness comparison display on **Page 5**. I suspect there is a typesetting error, but this is a core logical step in the paper. I would like the rebuttal to explicitly restate the intended inequality chain proving
\[
L_{\|\cdot\|_{\mathcal H}}(f)\le \Lambda_{\mathcal H}(f)\le d\,L_{\|\cdot\|_{\mathcal H}}(f),
\]
with notation consistent across norms and dual norms.

3. For **Theorem 4.3**, how essential is the assumption \(\max_t \|x_t-x^*\|_{\mathcal H}\le D\) in the unprojected algorithm? If the real intended result is the projected version in Appendix E.2, I would encourage the authors to surface that more prominently. In rebuttal, it would help to explain whether the main theorem should be interpreted as a proof sketch for the projected result, or as a meaningful standalone statement.

4. Can the authors provide one concrete class of examples where \(\Lambda_{\mathcal H}(f)\) is substantially smaller than \(d\,L_{\|\cdot\|_{\mathcal H}}(f)\), and one class where adaptive variance \(\sigma_{\mathcal H}\) is materially more informative than standard \(\|\cdot\|_{\mathcal H,*}\)-variance? Even a toy quadratic or synthetic covariance example would help anchor the theory.

5. In **Lemma 3.3**, the general noncommutative bound incurs extra logarithmic overhead through \(\|S_T\|_{\mathrm{op}}\). Is this believed to be an artifact of proof technique, or is some noncommutative penalty genuinely unavoidable? If the authors have any lower-bound intuition here, that would significantly sharpen the contribution.

6. The paper emphasizes that adaptive smoothness gives acceleration unavailable under standard \(\ell_\infty\)-smoothness. Can the authors clarify how much of this separation depends specifically on the lower bound cited from Guzmán and Nemirovski, versus the particular algorithmic structure of Algorithm 2? In other words, is the message “no first-order method can do better under standard smoothness,” or “our accelerated adaptive method needs adaptive smoothness”?

7. If the authors choose not to add experiments, I would still strongly encourage adding at least one worked numerical example or comparison table in the revision. Even a small synthetic demonstration would make the paper much easier to digest.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
None.

## Soundness Rating
3: good. The paper contains substantial technical development and the main claims are supported at the theorem level, but there are enough notation glitches, underspecified comparison steps, and strong assumptions in key results that I am not comfortable giving the top soundness score.

## Presentation Rating
2: fair. The high-level motivation is clear, and **Figure 1** helps, but several central equations and algorithm blocks are garbled or ambiguous, and the main text is denser than it should be for a paper making a broad conceptual claim.

## Contribution Rating
3: good. The paper makes a meaningful theoretical contribution to optimizer theory and non-Euclidean analysis, especially through the unified view and the separation results, though the lack of empirical grounding and some overstatements keep it from a higher score.

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected. The core ideas are strong and the theorem package is valuable, especially for the optimization theory community, but the presentation needs tightening and the paper would benefit from either clearer main-text exposition or minimal supporting experiments/examples.

## Reviewer Confidence
4: confident. I am familiar with optimization theory and non-Euclidean first-order methods, and I checked the main arguments carefully, though I did not fully verify every appendix proof line by line.