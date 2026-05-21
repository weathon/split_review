---
job_id: 3df15b46-953f-46b8-9c57-35822c1655c5
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: Rt9SeEAMWv.pdf
paper: Stability, Complexity and Data-Dependent Worst-Case Generalization Bounds
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is squarely within ICLR scope, specifically learning theory, optimization, and data-dependent generalization analysis for stochastic learning algorithms.

## Minimum Quality
Pass ✅. The submission contains the expected scientific components, including abstract, introduction, technical development, experiments, results/discussion, and conclusion; while there are important weaknesses in assumptions, exposition, and empirical validation, the paper clears the minimum bar for full review rather than desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, reviewer-targeting instructions, or other obvious manipulative content in the provided paper text and figures.

# Expected Review Outcome:
## Summary
This paper studies worst-case generalization over data-dependent random sets, with a focus on optimization trajectories rather than a single final iterate. The main contribution is a new notion of random set stability for stochastic algorithms, which is then used to derive expected worst-case generalization bounds involving a standard Rademacher complexity term over the observed random set and a stability parameter, thereby avoiding the mutual-information terms that appear in prior random-set/topological bounds. The paper further instantiates the framework to recover intrinsic-dimension and topological complexity bounds without information-theoretic terms, and provides experiments on ViT/CIFAR-100 and GraphSAGE/MNISTSuperpixels to estimate the resulting quantities and study the interaction between stability and topological complexity.

## Strengths
1. The paper tackles a real limitation in the recent literature on data-dependent worst-case generalization bounds, namely the dependence on mutual information terms that are difficult or impossible to compute in practice. Replacing that dependence by a stability parameter is a meaningful conceptual shift, and the paper makes a reasonable case that this tradeoff is worth studying.

2. The framing around random sets is broad enough to unify several settings. Examples 1.1 to 1.4, especially the reduction to singleton outputs and fixed hypothesis classes, help situate the proposal within classical learning-theoretic perspectives. Corollaries 3.5 and 3.6 are useful sanity checks because they show the framework recovers familiar stability and Rademacher-style bounds in limiting cases.

3. The central technical result, Lemma 3.4 on Page 5, is potentially useful beyond the specific topological applications. The form
\[
\mathbb{E}\big[G_S(\mathcal{W}_{S,U})\big] \le 2\,\mathbb{E}[\mathbf{Rad}_{\tilde S_J}(\mathcal{W}_{S,U})] + 2J\beta_n
\]
provides a clean interpolation between stability-dominated and complexity-dominated regimes through the choice of \(J\). That interpolation is one of the more interesting ideas in the paper.

4. The paper does try to connect the abstract stability notion back to more classical algorithmic stability. Lemma 3.2 and Corollary 3.3 are helpful in that respect, because without such a bridge Assumption 3.1 would feel even more detached from existing theory.

5. The empirical section makes a genuine effort to estimate the ingredients of the bounds rather than only reporting correlations. Table 1 on Page 9 is useful because it reports \(\beta_n\), the observed worst-case gap \(G_S(\mathcal{W}_{S,U})\), and the resulting estimated bound side by side. Even though the bounds are loose, the table at least attempts an end-to-end quantitative check rather than stopping at a narrative claim.

6. Figure 1 is effective at conveying the motivating intuition. The left panel clearly illustrates the distinction between classical single-iterate stability and trajectory-level stability, and the right panel gives a concrete empirical picture of \(\beta_n\) decreasing with \(n\), which is central to the paper’s theoretical story.

7. Figures 2 and 3 are also relevant to the paper’s main thesis. The increasing slope with larger \(n\), if reliable, does visually support the claim that the interaction between stability and topological complexity becomes more pronounced as sample size grows. I appreciate that the figures separate ViT and GraphSAGE rather than collapsing everything into one plot.

## Weaknesses
1. **The main stability assumption is very strong, and the paper does not do enough to clarify its scope or practical meaning.**  
   Assumption 3.1 on Page 5 quantifies over **any** data-dependent selection \(\omega\) of \(\mathcal{W}_{S,U}\), and requires the existence of a map \(\omega'\) such that for all \(z\in\mathcal Z\) and all datasets differing by \(J\) points,
   \[
   \mathbb{E}_U\!\left[\left|\ell(\omega(\mathcal{W}_{S,U},S),z)-\ell(\omega'(\mathcal{W}_{S',U},\omega(\mathcal{W}_{S,U},S)),z)\right|\right]\le \beta_n J.
   \]
   This is not a benign extension of standard stability. It is a uniform matching condition over arbitrary selections from a random set, and it is not obvious that it should hold for realistic deep learning trajectories except in very restricted settings. The paper says this is “implied by Definition 2.1” via Lemma 3.2, but that implication is only shown for **finite trajectories built from individually stable iterates** plus global \(L\)-Lipschitzness of the loss in \(w\). That is much narrower than the generality suggested in the introduction. In particular, the submission repeatedly markets the framework as broadly applicable to “practically used optimization algorithms”, but the theory provided in the main paper does not substantiate that breadth. This matters because the paper’s central promise is practical computability without intractable terms; if the replacement assumption is itself hard to verify or only valid in special cases, the practical gain is less compelling.

2. **There is a noticeable mismatch between the generality of the claims and the actual guarantees proved in the main text.**  
   The introduction and contributions emphasize worst-case generalization bounds for stochastic optimization trajectories and “the first fully computable topological bounds for practically used optimization algorithms” on Page 3. But the most concrete applicability statement in the main text is Corollary 3.3, which treats projected SGD under \(L\)-Lipschitz, \(G\)-smooth losses and step sizes \(\eta_k\le c/k\) with \(c<1/G\). The experiments, however, use Adam/AdamW-style training for ViT and GraphSAGE, not projected SGD, and no theory in the main paper justifies Assumption 3.1 for Adam-like dynamics. This is a serious gap between theory and practice. The paper effectively estimates a proxy of the stability parameter for optimizers that are outside the proven scope, then interprets the results as supporting the theory. That is weaker than it sounds and should be presented much more cautiously.

3. **The core lemma is only in expectation, which substantially limits the interpretation of the resulting worst-case bounds.**  
   The object of interest is already a worst-case-over-trajectory quantity,
   \[
   G_S(\mathcal{W}_{S,U}) = \sup_{w\in\mathcal{W}_{S,U}} (\mathcal R(w)-\widehat{\mathcal R}_S(w)),
   \]
   yet Lemma 3.4 and all main downstream results only control its expectation. The paper acknowledges this limitation only briefly in the conclusion on Page 10, but in practice this is not a small detail. For a worst-case quantity, an expected bound can be significantly less informative than a high-probability bound, especially if the distribution over trajectories has heavy tails or rare bad events. This matters because the paper frequently emphasizes practical computability and meaningful guarantees; expected bounds are mathematically valid, but their operational value for model selection or reliability claims is weaker than the framing suggests.

4. **Several mathematical details in the main text are underspecified or internally awkward, which makes it harder than necessary to verify the claims.**  
   A few examples:
   - In Definition 3.1 on Page 4, the notation for the selection \(\omega_0(\mathcal{W}_{S,U},S')\) is introduced as a “random variable” arising from a deterministic mapping. The measure-theoretic intent is understandable, but the exposition is imprecise and mixes deterministic selectors with random realizations in a confusing way.
   - Assumption 3.1 defines \(\omega':\mathrm{CL}(\mathbb{R}^d)\times \mathbb{R}^d\to\mathbb{R}^d\), but the displayed condition uses \(\omega'(\mathcal W_{S',U},\omega(\mathcal W_{S,U},S))\), so the role of the second argument is as a reference point in \(\mathbb R^d\). This is quite nonstandard and needs more intuition. As written, the assumption feels reverse-engineered to make the proof work.
   - Lemma 3.4 requires \(n=JK\), and Theorems 4.3 and 4.4 assume “without loss of generality” that \(\beta_n^{-2/3}\) is an integer divisor of \(n\). This is not really without loss of generality. It is a discretization convenience, and the paper should state the rounded version cleanly in the main text rather than sweeping divisibility issues aside. The appendix later says “up to a slight change in the constant”, but the main theorem statements should not hide this.
   - Theorem 4.4 defines \(K_{n,\alpha}:=2(2L_{S,U}\sqrt n/B)^\alpha\), while Lemma B.3 in the appendix states \(K_{n,\alpha}:=2(2L\sqrt n/B)^n\), which appears inconsistent and likely a typo. Given that this constant enters the logarithm inside the bound, such notation errors are not harmless. They undermine confidence that the theorem statements were checked carefully.

5. **The proof presentation around Lemma 3.4 is too brittle for a central result, and some notation appears inconsistent across the appendix derivation.**  
   In the appendix proof on Pages 18 to 19, the datasets/laws alternate between \(\mu_\varepsilon\), \(\mu_z\), and \(\mu_s\), and the notation switches between \(\mathcal W_S\), \(\mathcal W_{S,U}\), and conditional laws \(\rho_S\) without a clean setup. There are also lines where arguments to \(\omega\) and \(\omega'\) appear malformed, for example
   \[
   \omega'(\mathcal W_{S_k,U}, \omega(\mathcal W_{S,U}), S)
   \]
   in one line versus the types declared earlier. I can infer the intended argument, but for a theory paper built around one main symmetrization lemma, this level of notational slippage matters. It makes it harder to separate genuine ideas from proof engineering.

6. **The empirical estimation of the stability parameter is only a loose proxy for the quantity in Assumption 3.1, and the optimism of the estimate undercuts the strength of the empirical conclusions.**  
   Section 5 explicitly says the estimation “necessarily leads to an optimistic estimation” of \(\beta_n\), because the supremum over \(Z\in\mathcal Z\) is replaced by evaluation on a finite held-out set. In the appendix, Algorithm 1 actually computes an average over evaluation points first, then a row-wise minimum, then a maximum over rows. This is already quite far from the exact definition in Assumption 3.1, which involves existence of a matching selector \(\omega'\), a supremum over \(z\), and expectation over algorithmic randomness. The paper is honest that it uses an approximation, but then the claims in Section 5 become correspondingly weaker. In particular, the statement on Page 9 that the experiments “strongly support Theorem 4.4” is overstated, because the key theoretical quantity is not actually measured, only a favorable surrogate is.

7. **The experimental validation is narrow and does not sufficiently isolate the contribution of the proposed framework.**  
   The experiments are limited to two model-dataset pairs, both in relatively controlled fine-tuning settings after convergence. There is no comparison against prior information-theoretic random-set bounds, no ablation showing what happens if one uses only \(\beta_n\) versus only topological complexity versus both, and no study of how sensitive the conclusions are to the trajectory length \(T\), the subsampling of 1500 points from 5000 iterations, or the choice \(J=50\) in the stability estimation. Since the paper’s headline claim is not merely theoretical novelty but practical computability and empirical relevance, this lack of ablation matters a lot.

8. **Table 1 does not support the “tightness” narrative as strongly as the paper suggests.**  
   On Page 9, Table 1 reports bounds that are roughly one order of magnitude larger than the observed worst-case generalization gaps. For example, for ViT with \(\eta=10^{-4}, b=64\), the observed gap is \(10.24\times 10^{-2}\) while the bound is \(104.43\times 10^{-2}\), about a \(10\times\) factor. Similar gaps appear across the table. I agree these are not vacuous because they remain below 100% for 0-1 loss, but calling them “reasonable tight” is too generous. The table shows non-vacuity in some regimes, not tightness. More importantly, because the bound estimate uses Massart’s lemma and an optimistic \(\beta_n\) proxy, the numbers do not really validate the sharpness of the theory itself, only the rough scale of one relaxed bound estimator.

9. **The figure-based empirical claims are plausible but overstated relative to what the figures show.**  
   Figures 2 and 3 on Page 9 show scatter plots of \(\mathbf E^1\) against generalization gap, with subgroup-specific Pearson correlations. The visual trend that slopes become steeper with larger \(n\) is suggestive, but the plots also show substantial scatter and declining correlations at larger \(n\), especially for GraphSAGE. The text says these results “strongly support Theorem 4.4”, but the figures are correlational and subject to many confounders, including learning rate, batch size, trajectory sampling, and optimizer dynamics. At best, the figures provide exploratory evidence consistent with the theorem’s qualitative prediction. They do not strongly validate the quantitative form of the bound.

10. **The paper’s positioning against prior work is incomplete in one important dimension: what is lost by removing the information-theoretic term is not analyzed carefully enough.**  
   The paper does say on Page 8 that its bounds may have a slower convergence rate, but the discussion is too shallow. A more honest comparison would spell out when the tradeoff is favorable: if prior bounds involve an intractable but potentially much smaller IT term, and the new bounds replace it with a stability multiplier \(\beta_n^{1/3}\), then there are regimes where the new result is cleaner but significantly weaker. Right now the narrative leans too heavily toward “we removed the bad term”, without equally emphasizing the cost in rate, assumptions, and scope.

11. **Presentation quality in the main paper is uneven, with several typos and notation issues that are distracting in a technical submission.**  
   Examples include “Due the dependence” on Page 2, “enounced” on Page 5, “particluar” on Page 6, and several notation inconsistencies in the appendix around \(\mu_\varepsilon\), \(\mu_z\), and \(\mu_s\). These are not individually fatal, but collectively they make the paper feel less polished than it should be for a theory-heavy ICLR submission.

## Questions
1. The biggest issue for me is the practical scope of Assumption 3.1. Can the authors give a clearer, concrete class of stochastic deep learning algorithms, beyond projected SGD under smooth Lipschitz assumptions, for which the assumption can be justified or at least plausibly argued? In particular, what is the intended status of the Adam-based experiments relative to the theory?

2. Can the authors provide a cleaner and more intuitive explanation of the selector pair \((\omega,\omega')\) in Definition 3.1 and Assumption 3.1? Right now it reads like a technical device. A toy example showing exactly how \(\omega'\) is constructed and what it means geometrically would increase my confidence substantially.

3. In Theorem 4.4 and Lemma B.3, the constant \(K_{n,\alpha}\) appears inconsistent. Is this a typo, and if so, what is the correct expression? Please also check whether any downstream theorem statement depends quantitatively on that constant.

4. How sensitive are the empirical findings to the proxy used for \(\beta_n\)? For example, if one varies the held-out evaluation set size, the number of replaced samples \(J\), or the trajectory subsampling rate, do the conclusions in Table 1 and Figures 2 to 3 remain stable?

5. Could the authors add an ablation that compares:  
   (a) bound estimate using only the stability term,  
   (b) only the complexity term surrogate,  
   (c) the combined bound?  
   This would help determine whether the topological quantities add explanatory value beyond \(\beta_n\) alone.

6. The current results are in expectation. Is there any realistic path, even under stronger assumptions, toward high-probability bounds in this framework? Even a short discussion would help clarify the long-term significance of the approach.

7. For Table 1, please quantify the ratio \(\text{Bound}/G_S(\mathcal W_{S,U})\) explicitly and avoid describing the results as “tight” without qualification. Would the authors agree that “non-vacuous in several settings but still substantially loose” is a more accurate characterization?

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
The paper is primarily theoretical and uses standard public datasets and models. I did not identify a paper-specific ethics concern that requires escalation based on the content provided.

## Soundness Rating
2: fair. The technical direction is interesting and some results appear plausible, but the central assumption is strong, the proof exposition has notation inconsistencies, and the empirical validation only indirectly supports the stated theoretical claims.

## Presentation Rating
2: fair. The paper is readable at a high level, but important definitions are opaque, several theorem statements are awkwardly phrased, and there are enough notation/typo issues to hinder careful verification.

## Contribution Rating
2: fair. The idea of replacing information-theoretic terms by a stability-based framework for random sets is worthwhile, but the current paper overstates applicability and practical validation relative to what is actually established in the main text.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted.  
I see genuine promise in the random-set stability perspective and in the interpolation result of Lemma 3.4, but the submission currently has too many substantive issues for me to recommend acceptance: the main assumption is stronger and less transparent than advertised, the practical scope is narrower than the framing suggests, the theorem/proof presentation needs tightening, and the experiments do not convincingly validate the claimed practical advantage. This is closer to a solid workshop or strong revision paper than a fully convincing main-track ICLR acceptance in its current form.

## Reviewer Confidence
4: confident. I am familiar with learning theory, stability-based generalization, and the recent literature on data-dependent/topological generalization bounds, and I checked the main claims and derivations carefully, though some appendix details remain hard to verify because of presentation issues.