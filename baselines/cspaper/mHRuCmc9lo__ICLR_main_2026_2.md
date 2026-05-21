---
job_id: 8bde45ab-83e1-40e2-9a7a-4a30ee20896d
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: mHRuCmc9lo.pdf
paper: Robust Decision Making With Partially Calibrated Forecasts
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, sitting at the intersection of uncertainty quantification, learning theory, calibration, and decision-making under uncertainty.

## Minimum Quality
Pass ✅. The paper contains the expected components, namely Abstract, Introduction, related-work discussion, a methodological/theoretical development, experiments with quantitative results, and a conclusion/limitations section; despite some technical and empirical limitations, it meets the minimum bar for a full scientific submission rather than a desk reject.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find any hidden prompts, suspicious instructions targeting automated reviewers, or other manipulative content in the provided paper text or figures.

# Expected Review Outcome:
## Summary
This paper studies how a downstream decision maker should act when forecasts satisfy only partial calibration guarantees, rather than full calibration. The authors formulate a minimax robust decision problem over all conditional expectations consistent with a chosen class of calibration tests $\mathcal H$, derive a dual characterization of the resulting optimal decision rule for finite-dimensional $\mathcal H$, and show that if $\mathcal H$ contains the decision-calibration tests, then the minimax-optimal policy collapses to the usual plug-in best response. The paper also instantiates the framework for self-orthogonality induced by squared-loss training and for bin-wise calibration, and provides a small empirical study on two regression datasets.

## Strengths
1. The paper asks a meaningful question that is easy to motivate and relevant to trustworthy ML: if full calibration is too strong or intractable in high dimensions, what should a decision maker do with weaker calibration guarantees? This is a good problem formulation, and it connects calibration to downstream action selection in a more explicit way than much of the prior literature.

2. The main conceptual result, namely that decision calibration is already enough to recover plug-in best-response optimality in the authors’ minimax sense, is interesting. The “collapse” from a potentially rich hierarchy of robust policies to simple plug-in behavior at the level of decision calibration is the paper’s sharpest insight, and it gives a clean interpretation of decision calibration beyond regret-style guarantees.

3. The paper is strongest in Sections 3 and 4, where it provides a reasonably unified optimization view. Theorem 3.1 gives a useful decomposition of the robust policy into: (i) computing dual multipliers, (ii) solving a pointwise inner minimization for $q^\star(v)$, and (iii) best responding to $q^\star(v)$. Even though some technical details need tightening, the overall structure is clear and potentially useful.

4. The decision-calibration specialization is well motivated and practically relevant. In particular, Theorems 4.1 and 4.2 give a fairly crisp operational message: once the calibration test class contains the decision regions $\{\mathbf{1}_{R_a}\}_{a\in\mathcal A}$, extra calibration constraints do not further change the minimax-optimal decision rule. That is a nice and interpretable theorem.

5. Proposition 4.4 is a good attempt to connect the framework to something that could arise “for free” from standard pipelines, rather than requiring explicit post-processing. This makes the paper less purely abstract and helps explain why a robust policy under weak moment constraints might matter in practice.

6. The presentation of the big-picture interpolation is effective. **Figure 1** on Page 4 communicates the intended spectrum from “maximally conservative” to “maximally aggressive” as $\mathcal H$ grows, and **Figure 2** on Page 7 usefully contrasts the generic interpolation intuition with the paper’s stronger “sharp transition” claim at decision calibration. These figures are schematic rather than technical, but they do help the reader parse the paper’s central story.

7. The experimental table, while limited, is at least aligned with the theory. **Table 1** on Page 10 shows the intended tradeoff: under i.i.d. evaluation the plug-in rule is slightly better, while under the adversarial evaluations the robust rule is better. The pattern is consistent across both Bike Sharing and California Housing, which lends some support to the minimax interpretation.

## Weaknesses
1. The paper’s main theorem is presented as a fairly general minimax characterization, but some key functional-analytic and optimization details are under-specified in the main text, and the appendix does not fully resolve them. In **Theorem 3.1** and its proof in Appendix A (Pages 13 to 14), the argument invokes Sion’s minimax theorem over measurable policies $a(\cdot)$ and measurable maps $q:[0,1]^d\to[0,1]^d$, while asserting compactness/convexity properties of these infinite-dimensional objects. The proof states that $\mathcal Q$ is “nonempty, convex, and compact,” but no topology is specified under which the set of measurable functions is compact, and compactness is not immediate. This matters because the claimed existence of a saddle point and the finite-dimensional dual characterization depend on a valid interchange of max and min plus strong duality. As written, the result reads stronger than what is actually justified in the main paper.

2. Still on the optimization side, the proof of **Theorem 3.1** says the objective is “concave in $a$” in Appendix A, Page 13, because it is “a pointwise maximum over linear functionals in $a$ on the compact set $\mathcal A$.” That statement is at best unclear and at worst incorrect under the paper’s own setup. The policy variable is an arbitrary measurable mapping into $\mathcal A$, not obviously a convex vector space element, and $\mathcal A$ itself is often treated as a finite action set elsewhere. The authors may be able to repair this by avoiding Sion and directly using the separability of $\max_{a(\cdot)} \mathbb E[u(a(f(X)),q(f(X)))]$, but as written the mathematical route is shaky. Since the theorem is the backbone of the paper, this is not a cosmetic issue.

3. The ambiguity set $\mathcal Q$ in **Equation 4** on Page 4 and the robust objective in **Equation 5** are defined using expectations over the unknown distribution of $X$. This makes the framework population-level and distribution-dependent in a way that is somewhat glossed over when the paper emphasizes efficient computability. The “efficiently computable” claim in Section 3 is only really meaningful after these expectations are replaced by empirical estimates or a known forecast distribution, but that bridge is not formalized in the main paper. In other words, the theory gives a characterization of the population minimax solution, but the paper often sounds closer to an implementable algorithm than it actually specifies.

4. The empirical section is much narrower than the scope suggested by the theory. The paper motivates high-dimensional and multiclass calibration issues in the introduction, and the strongest theorem is about decision calibration in general action-dependent decision regions. However, **Section 5** only evaluates two scalar regression tasks with $d=1$, a small finite action set, a very simple utility $u(a,y)=\alpha ay-C(a)$, and a single weak calibration class $\mathcal H=\{h(v)=v\}$ induced by squared-loss self-orthogonality. There is no experiment involving decision calibration itself, no multiclass setting, and no demonstration of the sharp transition emphasized in **Figure 2**. This mismatch weakens the practical evidence for the paper’s headline claims.

5. The experimental comparisons in **Table 1** are not fully convincing as evidence of broad practical usefulness. The robust policy is evaluated under a “worst-case for robust” adversary and the plug-in policy under a “worst-case for plug-in” adversary, and the paper highlights that the robust policy wins in each policy’s own worst-case setting. But that is very close to the theoretical construction, so it is not a difficult empirical hurdle. More importantly, the gains in **Table 1** are numerically modest, for example $0.410$ vs $0.402$ on Bike Sharing under the robust adversary and $0.164$ vs $0.160$ on California Housing, while the nominal i.i.d. degradation is also visible. Without stronger baselines or more realistic shifts, it is hard to tell whether the robust policy is meaningfully useful beyond confirming the minimax setup by construction.

6. The experiments omit several baselines that would materially strengthen the paper. For example, in the interpolation story around **Figure 1**, the two extremes are plug-in best response and a fully conservative constant minimax action, but **Table 1** reports neither the constant minimax baseline nor any post-hoc recalibration baseline such as bin-wise calibration from **Proposition 4.5**. Since Section 4 explicitly presents bin-wise calibration as a practical instantiation, it is odd that the experiments do not include it. This omission matters because it leaves the reader unable to assess whether the proposed robust rule is better than simpler conservative alternatives.

7. The interpretation of the “sharp transition” is somewhat overstated in the main text relative to what is actually shown. **Figure 2** visually suggests a clean phase transition at decision calibration, but the formal claim is only that once $\mathcal H$ contains the decision-calibration tests, plug-in is minimax optimal. The paper does not establish that decision calibration is in any sense necessary for that collapse, nor does it characterize how often non-decision-calibrated classes still yield plug-in optimality for a given utility. So the picture is a sufficient-condition story, not a complete threshold characterization. This is still a good result, but the rhetoric around “sharp transition” is a bit stronger than the formal scope.

8. Several claims in Section 4 depend critically on almost-everywhere arguments and tie-breaking conventions that are not surfaced clearly enough in the main text. In Appendix A, the proof of **Theorem 4.2** adds a footnote specifying deterministic tie-breaking so that the regions $R_a$ are measurable. That is important, because overlaps of decision regions can otherwise complicate the partition argument. Given how central these regions are to the paper, this should be explicit earlier, ideally when $R_a$ is first defined on Page 6.

9. The paper leans heavily on exact calibration constraints in the main narrative, even though exact calibration is often unrealistic in finite samples. I appreciate that Appendix B discusses approximate $\mathcal H$-calibration, but the main paper does not integrate those results into the framing or experiments. This is particularly noticeable because the experiments on Page 10 say the MLP “approximately satisfies” $\mathcal H$-calibration and then use calibration data to estimate population quantities, but there is no quantitative report of the calibration error nor any empirical sensitivity analysis showing whether the robust policy remains preferable as those moment constraints are violated. Given that partial calibration is the whole premise, approximate versions deserve more prominence.

10. The exposition is mostly readable, but there are several presentation blemishes that reduce polish. There are typos and formatting glitches, for example “$a_{\mathrm{BH}}$” on Page 3 appears to be a typo for $a_{\mathrm{BR}}$, “Equation equation 1” on Page 4, and some visibly mangled spacing in the theorem statements on Page 7. These are not fatal, but they make a theory paper feel less carefully checked than it should.

## Questions
1. For **Theorem 3.1**, can the authors provide a cleaner statement of the exact optimization space and assumptions needed for minimax interchange and strong duality? In particular, under what topology is $\mathcal Q$ compact, and if compactness is not actually needed, can the theorem be reproved in a way that avoids this issue? A rebuttal that cleanly repairs this point would significantly increase my confidence.

2. Can the authors clarify whether the “sharp transition” language is intended as a purely sufficient statement, or whether they believe decision calibration is in some stronger sense minimal for plug-in minimax optimality? If it is only sufficient, I would encourage softening the phrasing around **Figure 2** and the surrounding text on Page 7.

3. Why not include at least one experiment directly about decision calibration, which is the paper’s most prominent theoretical message? Even a toy multiclass setting where $\mathcal H$ is enlarged from empty, to self-orthogonality/bin-wise, to decision calibration, would make the interpolation and collapse in **Figures 1 and 2** much more concrete.

4. In **Table 1**, what exactly is the optimization problem used to construct the “worst-case for robust” and “worst-case for plug-in” test distributions, and how sensitive are the results to estimation error in the calibration moments? A more explicit description would help separate theory confirmation from practically meaningful robustness.

5. The experiments state that the forecaster approximately satisfies $\mathcal H=\{h(v)=v\}$ calibration due to **Proposition 4.4**. Could the authors report the empirical value of the moment violation
\[
\left\|\frac{1}{n}\sum_{i=1}^n f(x_i)\bigl(y_i-f(x_i)\bigr)\right\|
\]
on the calibration split, and perhaps show how decision quality changes when this quantity is large versus small? That would make the approximate-calibration story much more tangible.

6. Since **Proposition 4.5** gives a particularly simple robust rule for bin-wise calibration, why is it absent from the experiments? Including it would help readers judge whether the more general dual-derived robust policies offer value beyond simple calibration-based aggregation.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
The paper is theoretical and uses standard public tabular datasets. It discusses high-stakes applications such as healthcare, finance, and law in motivation, but does not deploy or evaluate in such settings, and I did not find a concrete ethics issue requiring escalation.

## Soundness Rating
2: fair. The core ideas are plausible and several results are interesting, but the main minimax/duality theorem currently has technical gaps or under-specified assumptions that lower my confidence in the full strength of the claims.

## Presentation Rating
3: good. The paper is generally readable and well organized, and the main message comes through, but there are a number of proof-level clarifications and presentation glitches that should be fixed.

## Contribution Rating
3: good. The decision-theoretic framing of partial calibration, especially the plug-in optimality result under decision calibration, is a meaningful contribution, though the empirical support is limited and the technical execution needs tightening.

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected. The paper contains a genuinely interesting theoretical perspective and at least one result that I expect many readers will remember, namely the collapse to plug-in best response under decision calibration. However, the current version underserves its own theory with a somewhat shaky optimization proof and underserves its own ambition with a very limited empirical section. I lean positive because the central idea is strong enough to matter, but I do not think the submission is a clean accept without clarification.

## Reviewer Confidence
4: confident. I am confident in the overall assessment and familiar with the calibration/decision-making literature, though I would like the authors to tighten the main minimax proof to remove the remaining ambiguity.