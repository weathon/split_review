---
job_id: cb65fc65-05e1-4c3c-b465-039af42031e4
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: dbYvP2BKCM.pdf
paper: Causal Effect Estimation with Learned Instrument Representations
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅ This paper is clearly within ICLR scope, specifically causal reasoning and representation learning for causal effect estimation.

## Minimum Quality
Pass ✅ The paper contains the expected components, including abstract, introduction, related work, methods, experiments, quantitative results, and discussion. While I have substantial concerns about the technical claims and empirical support, these rise to the level of a regular review rather than a desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅ I did not detect any hidden prompts, manipulative instructions, or suspicious content targeting automated reviewers in the provided paper text or figures.

# Expected Review Outcome:
## Summary
The paper proposes ZNet, a neural architecture that decomposes observed covariates \(X\) into a learned confounder representation \(C=f(X)\) and a learned instrument representation \(Z=g(X)\), with the goal of producing representations that satisfy the standard instrumental variable conditions of relevance, exclusion restriction, and unconfoundedness. The learned representations are then used as inputs to downstream IV estimators such as TSLS, DeepIV, and DFIV. Experiments on semi-synthetic datasets derived from IHDP evaluate instrument recovery, latent instrument recovery, and downstream ATE/CATE estimation.

## Strengths
The paper tackles a meaningful problem. In many observational settings, valid instruments are unavailable or unclear, so trying to construct useful instrument-like representations from observed features is an interesting direction with clear practical motivation.

The architectural idea is easy to follow. In particular, **Figure 3** gives a reasonably intuitive view of how \(\Phi\), \(f\), \(g\), and \(\pi\) interact, and how the learned \(Z\) and \(C\) are plugged into downstream IV estimators. This is one of the clearer parts of the paper.

I also appreciated that the paper does not stop at one synthetic regime. The evaluation spans several regimes, including disjoint, mixed, latent, and no-candidate settings, with both linear and non-linear variants. That breadth is helpful for stress-testing the intended use cases, even if I have concerns about what can actually be concluded from those experiments.

There is some useful empirical evidence that the method can recover known instruments when they are artificially embedded in the data. For example, **Figure 5(a,b)** and the corresponding discussion in Section 6.2 suggest that in the linear mixed-candidate setting the learned \(Z\) is correlated with the true instrument coordinates \(X13,X14,X15\), and **Figure 5(c)** provides at least a basic ablation that indicates the full objective matters for this recovery behavior. Even though I am not convinced this establishes IV validity, it does support the narrower claim that the representation captures signal related to treatment-driving variables under the authors’ data construction.

The paper compares against several relevant IV-generation baselines, not just downstream causal estimators. That is the right experimental framing for the stated contribution.

## Weaknesses
I have several substantial concerns. The main issue is that the paper repeatedly speaks as if the proposed losses make \(Z\) into a valid instrument, but the actual constraints enforced are much weaker than the IV assumptions they are supposed to stand in for.

1. **The core identification logic is much too weak for the claims being made.**  
   The paper’s central move is to replace the IV assumptions with empirical moment-style constraints such as \(\mathrm{Cov}(g(X),e_Y)=0\), \(\mathrm{Cov}(g(X),f(X))=0\), and \(\mathrm{Cov}(T,g(X))>0\) in Section 3 and Section 5.1. But IV validity is not equivalent to these low-order correlations being small or large. In particular:
   - Relevance is a conditional dependence condition, \(Z \not\!\perp T \mid C\), not merely nonzero marginal correlation or predictiveness.
   - Exclusion restriction is a structural statement that \(Z\) affects \(Y\) only through \(T\), not something implied by \(\mathrm{Cov}(Z,C)=0\) plus \(C\) being predictive of \(Y\).
   - Unconfoundedness is \(Z \perp e_Y \mid C\), not unconditional zero covariance with a residual proxy.
   
   This matters because the paper’s headline claim, on **Page 10**, that “Solutions to the ZNet loss minimization problem will always give a representation that serves as an instrument” is far stronger than what the objective can justify. Zero covariance is not independence, unconditional relations are not conditional ones, and matching a few moments does not define a valid SCM. This is not a nitpick; it directly undermines the scientific claim that the method “learns instruments” rather than merely learns treatment-predictive latent features.

2. **Lemma 1 and its use are not convincing as a justification of instrumental unconfoundedness.**  
   The proof on **Page 4** is problematic. The step
   \[
   \mathbb{E}[Z\cdot \mathbb{E}[e_Y\mid X,T]] = \mathbb{E}[Z]\cdot \mathbb{E}[e_Y\mid X,T]
   \]
   is not valid as written because \(\mathbb{E}[e_Y\mid X,T]\) is a random variable measurable with respect to \((X,T)\), not a constant. More generally, from
   \[
   \mathrm{Cov}(Z, e_Y-\mathbb{E}[e_Y\mid X,T])=0
   \]
   one obtains
   \[
   \mathrm{Cov}(Z,e_Y)=\mathrm{Cov}(Z,\mathbb{E}[e_Y\mid X,T]),
   \]
   not automatically \(0\). The Gaussianity assumption \(Z\sim \mathcal N(0,\sigma^2)\) does not rescue this derivation. As presented, Lemma 1 appears incorrect, and since it is the explicit basis for Constraint 1 and losses (5)-(6), this is a serious flaw rather than a cosmetic proof gap.

   Relatedly, the claim on **Page 6** that “As \(L_{Z \nearrow e_Y}^{PC}\) approaches 0, satisfaction of Constraint 1 and thereby instrumental unconfoundedness is reached” is not supported by the math.

3. **Several equations/objectives are underspecified or inconsistent for vector-valued representations.**  
   The method learns multi-dimensional \(C\) and \(Z\), for example 10-dimensional \(Z\) in Section 6.2, but losses such as **Equation (4)** and **Equations (7)-(9)** are written as if \(PC(A,B)\) is defined for scalar variables. It is not explained in the main paper how Pearson correlation is computed between a vector \(C\) and scalar \(Y\), between vector \(C\) and vector \(Z\), or between vector \(Z\) and binary \(T\). Is this averaged over dimensions, maximized over dimensions, applied after a projection, or computed via canonical correlation? The appendix hints at averaging PCs across dimensions, but the training objective in the main text remains ambiguous.

   This matters because the exact way these penalties are computed changes the optimization problem materially. For example, minimizing average pairwise correlations between coordinates of \(Z\) and \(C\) is not the same as enforcing multivariate independence of the representations. Likewise, \(PC(Z,T)^2\) for a vector \(Z\) has no standard scalar meaning without a precise definition.

4. **The exclusion-restriction surrogate is not well justified and may actively fail.**  
   In Section 3 and Section 5.1, exclusion is encouraged by making \(C\) predictive of \(Y\) and forcing \(Z\) to be decorrelated from \(C\). This does not prevent \(Z\) from carrying outcome-relevant information not shared with \(C\). If \(X\) contains a feature that affects both \(T\) and \(Y\) through a nonlinear pathway but happens to be weakly correlated with the learned \(C\), the objective has no principled mechanism to exclude it from \(Z\). The F-test shown in **Figure 6(b)** is also too weak to support the stronger causal claim. “Not additionally helpful in predicting \(Y\)” in one fitted regression is not the same as satisfying exclusion restriction. At best, it is a heuristic diagnostic.

5. **The experimental tuning procedure is hard to trust and may induce circular evaluation.**  
   On **Page 6**, hyperparameters for IV-generation methods are tuned to maximize the instrument F-statistic and minimize correlation between learned \(C\) and \(Z\). For causal inference methods, the paper tunes to minimize MSE of the model’s ATE against a nearest-neighbors ATE and factual outcome error. This raises several issues:
   - It is unclear on which split these objectives are computed. The paper gives train/validation/test splits on **Page 7**, but the tuning description does not explicitly say that model selection is done only on validation data.
   - Using a nearest-neighbors ATE proxy to tune a causal estimator is methodologically delicate, because it effectively injects an auxiliary estimator of the causal target into model selection. The paper does not justify why this proxy should rank models in a way consistent with true causal performance.
   - Maximizing F-statistic while selecting a representation called an “instrument” risks preferring strong but invalid instruments, especially when validity is only weakly proxied by low correlations.

   Since the empirical story is a major part of the paper, these ambiguities matter.

6. **The results are mixed, and the paper overstates superiority.**  
   The text claims superior or broadly best performance, but **Table 1** is more uneven than the narrative suggests. ZNet is often competitive, but not consistently best. Examples:
   - In the linear mixed dataset, ZNet+TSLS has an ATE error of \(0.437\), which is worse than TrueIV+TSLS at \(0.263\), and ZNet+DFIV is \(0.655\), worse than several alternatives.
   - In the non-linear disjoint dataset, ZNet+TSLS is \(0.524\), noticeably worse than TrueIV+TSLS at \(0.266\), and DeepIV with ZNet is also not best.
   - In the no-unobserved-confounding settings, the advantage over TARNet is not systematic, which is important because in those regimes an IV construction method should not be expected to dominate standard treatment-effect estimators.
   
   The paper does mention that performance is “comparable” in places, but the discussion on **Pages 9-10** still reads more triumphantly than the evidence warrants. A more honest framing would be that ZNet is often competitive on the authors’ synthetic regimes, with no clear consistent win across all downstream estimators and settings.

7. **The empirical evaluation is entirely synthetic or semi-synthetic, which is a serious limitation for a paper making claims about broad utility in observational settings.**  
   The datasets are all generated from IHDP covariates with synthetic structural equations, as described in Section 6.1. That is useful for controlled evaluation, but it means the method is tested only in worlds where the authors decide what a latent instrument looks like and what correlations hold. This is especially problematic because the entire pitch is about automatically constructing instruments when none are known. Without at least one real application, it is hard to assess whether the learned \(Z\) is anything more than a simulation-specific artifact. The statement in the abstract that the method can be used “regardless of whether the assumption of unconfoundedness is satisfied” is much too broad relative to the evidence provided.

8. **The comparison to prior work is incomplete at the conceptual level.**  
   The related work section lists prior IV-generation approaches, but the differentiation is somewhat superficial. The paper repeatedly contrasts “learning SCMs” with “learning variational distributions,” yet what is actually optimized here is still a representation-learning objective with empirical penalties, not a verified SCM recovery procedure. That distinction is rhetorically sharper than methodologically established. I would have liked a more precise discussion of what, concretely, ZNet can guarantee or diagnose that AutoIV/VIV/DVAE.CIV cannot.

9. **Some figure-based evidence is weaker than the text implies.**  
   **Figure 4** shows a normalized confusion matrix for recovery of a latent categorical instrument after K-means and relabeling. This demonstrates some cluster alignment, but because the clustering and relabeling are post hoc, it is a fairly forgiving metric. It does not tell us whether the learned representation is valid for IV estimation, only that it can recover partition structure under the authors’ simulation. Similarly, **Figure 6(c)** reports low average absolute correlations between \(U\) and \(Z\), but the values are not near zero in any absolute sense, and more importantly, low marginal correlation with the simulated \(U\) is still weaker than the causal conditions required for IV validity.

10. **Presentation issues remain in the core technical exposition.**  
   The writing is generally readable, but several key claims are stated too categorically. Examples include “The derived IV \(g(X)\) will automatically be unconfounded” on **Page 4**, and the already-mentioned statement on **Page 10** that any solution to the loss minimization problem yields a valid instrument. These are not just overstatements; they can mislead readers about what the method establishes. There are also notation issues, for example switching between \(\varphi,\phi,\varphi'\) and using \(X\), \(C\), and subsets of \(X\) in ways that blur whether \(C=f(X)\) is meant to preserve all confounding information relevant to both treatment and outcome.

## Questions
1. The most important issue is the correctness of **Lemma 1** on Page 4. Can the authors provide a correct derivation, or state a revised lemma with sufficient assumptions under which minimizing
   \[
   \mathrm{Cov}\!\left(Z,\, Y-\mathbb{E}[Y\mid X,T]\right)
   \]
   implies anything close to \(Z \perp e_Y \mid C\)? As written, I believe the proof is invalid. A convincing rebuttal here would meaningfully affect my confidence.

2. Please define precisely how \(PC(A,B)\) is computed when \(A\) and/or \(B\) are vector-valued, as in \(PC(C,Y)\), \(PC(C,Z)\), and \(PC(Z,T)\) in **Equations (7)-(9)**. Is it an average over coordinates, a canonical correlation, a learned projection, or something else? This needs to be explicit in the main paper.

3. Can the authors clarify the exact model-selection protocol on train/validation/test splits? In Section 5.3, are the Bayesian optimization objectives computed exclusively on validation data? If not, the reported test results would be difficult to interpret.

4. What is the rationale for tuning causal estimators against a nearest-neighbors ATE proxy? Why should this proxy be expected to select the model with the best true ATE on the synthetic data? A rebuttal should explain why this does not introduce circularity or bias in favor of certain methods.

5. Could the authors provide a more restrained statement of what ZNet guarantees? In particular, do they agree that the current losses only enforce empirical surrogates for IV assumptions rather than the assumptions themselves? If not, please explain the missing theoretical step.

6. The paper would be stronger with more diagnostic analyses of failure modes. For instance, in **Table 1**, when ZNet underperforms TrueIV or even some competing learned-IV methods, what property of the learned \(Z\) appears responsible: weak relevance, residual dependence with \(U\), downstream estimator instability, or something else?

7. If space permits in revision, a real-data case study would significantly improve the paper. Even without ground-truth causal effects, demonstrating the behavior of the learned \(Z\) in a realistic observational setting would help support the paper’s practical claims.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
None beyond standard caution for causal claims in applied domains. The paper does not appear to raise a specific ethics issue that requires escalation.

## Soundness Rating
2: fair. The empirical setup is nontrivial and the paper contains useful experiments, but the central technical justification is weakened by incorrect or unsupported arguments, especially around Lemma 1 and the mismatch between the enforced losses and actual IV assumptions.

## Presentation Rating
2: fair. The paper is readable and figures such as **Figures 3, 5, and 6** are helpful, but the main technical exposition is underspecified in important places and several claims are overstated.

## Contribution Rating
2: fair. Learning instrument-like representations is an interesting problem and the empirical direction is potentially useful, but the current paper does not convincingly establish that the learned representation is a valid instrument rather than a heuristic proxy, and the evidence is not strong enough for a stronger score.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The paper addresses an interesting problem and has some promising empirical results, but the core theoretical justification is significantly weaker than the paper claims, and the experiments do not fully close that gap.

## Reviewer Confidence
4: confident. I am confident in the main concerns, especially the mathematical issue around Lemma 1 and the gap between the surrogate losses and the claimed IV guarantees, though some implementation details are not fully specified in the paper.