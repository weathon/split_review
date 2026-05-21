---
job_id: a44fc584-42bb-48f3-9a76-369334d7edd2
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: 1j0ormf8uI.pdf
paper: Conformalized Survival Counterfactual Prediction for General Right-Censored Data
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, combining uncertainty quantification, conformal prediction, causal inference, and survival modeling for healthcare.

## Minimum Quality
Pass ✅. The submission contains the expected core components, including abstract, introduction, related work, method, theory, experiments, results, and discussion; despite several technical and clarity concerns, it clears the bar for full review rather than desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find any hidden prompts, manipulative instructions, or suspicious content targeting automated reviewers in the provided paper text.

# Expected Review Outcome:
## Summary
This paper studies lower predictive bounds for counterfactual survival times under general right-censoring. The main idea is to reduce the counterfactual survival calibration problem to a weighted conformal prediction problem over uncensored individuals in a treatment arm, using a weight based on \(\gamma(x)=p(W=w,e=1\mid X=x)\), and then to construct treatment-specific lower prediction bounds from censored quantile regression plus weighted conformal calibration. The paper also states an exact marginal validity result up to weight-estimation error, an asymptotic doubly robust guarantee, and empirical results on synthetic data and a lung cancer dataset.

## Strengths
1. The paper tackles an important problem. Reliable uncertainty quantification for counterfactual survival predictions under censoring is a meaningful and difficult setting, and the focus on lower predictive bounds is practically motivated for high-stakes clinical decisions.

2. The proposed reduction to weighted conformal calibration over the \(\{W=w,e=1\}\) subset is conceptually reasonable and, at a high level, offers a plausible route to handling the covariate shift between \(P_X\) and \(P_{X\mid W=w,e=1}\). Equation (3) makes the target density ratio explicit, which helps connect the method to weighted conformal inference under shift.

3. The paper does try to go beyond pure algorithmics by providing formal guarantees. In particular, Theorem 4.1 gives a finite-sample bound of the form
\[
\mathbb{P}(T(w)\ge \widehat L_{N,n}^{(w)}(X)) \ge 1-\alpha - \tfrac12 \mathbb{E}_{X\sim P_{X\mid W=w,e=1}}|\mathfrak D(X)-\omega(X)|,
\]
which is a concrete statement tying coverage degradation to density-ratio estimation error. Even though I have concerns about exposition and some notation around this theorem, the paper is at least aiming at a precise and testable claim, rather than making only heuristic arguments.

4. The experiments cover both synthetic and real data, and the synthetic section probes several censoring settings instead of a single toy example. In **Figure 1**, the method appears to achieve coverage close to the nominal \(90\%\) level across the six settings while often attaining larger relative LPB than several baselines. This figure is useful because it presents the central tradeoff directly, coverage in the top row and informativeness in the bottom row, rather than showing only one metric.

5. The real-data section is clinically motivated and the treatment-stratified presentation in **Figure 4** is easy to parse. The top row checks empirical coverage, while the bottom row reports LPB by treatment regime. Even if causal interpretation should be handled cautiously, this figure does illustrate the intended downstream use case of the method.

6. **Table 1** is a helpful sanity check for the \(\tau\)-optimization idea. It shows that the optimized \(\tau^\*\) does not collapse to the nominal \(\alpha\), and that the corresponding LPB is modestly larger than using \(\tau=\alpha\), while coverage remains in a sensible range. This at least supports the claim that the optimization over \(\tau\) may improve informativeness.

## Weaknesses
1. The paper repeatedly overstates “exact” validity in a way that is not fully supported by its own theorem statements. The abstract and introduction emphasize an “exact miscoverage guarantee” and “exact marginally valid LPB,” but **Theorem 4.1 on Page 6** gives
\[
1-\alpha - \tfrac12 \mathbb{E}|\mathfrak D(X)-\omega(X)|,
\]
not exact \(1-\alpha\) coverage unless the estimated weight equals the true density ratio. This is an important distinction, not semantics. As written, the main theorem supports exact validity only in the oracle-weight case, and approximate validity otherwise. The title, abstract, and contribution bullets should be much more careful here.

2. The core derivation around **Equation (1) on Page 5** is hard to follow and contains notation/logic issues that matter for correctness. For example, the display mixes \(\bar q_\alpha^{(w)}\), \(\widehat q_\alpha^{(w)}\), \(V(\bar T,X)\), and conditioning statements in a way that is not cleanly consistent. Step (iii) is justified by Lemma A.1, but in the main text it is only said to be “derived by the proof of Lemma A.1,” which is not sufficient when that inequality is central to the reduction. If the reduction from the target counterfactual coverage event to the weighted observed-data event is the whole crux of the paper, this step needs to be airtight in the main paper, not hidden behind a vague pointer.

3. There are several notation inconsistencies that make the method harder to trust than it should be. A few examples:
   - On **Page 4**, the nonconformity score is defined using \(\bar q_\tau^{(w)}\), but the text around it fluctuates between \(q_\tau^{(w)}\), \(\widehat q_\tau^{(w)}\), and \(\bar q_\alpha^{(w)}\).
   - The definition of \(c_{1-\alpha}^{(w)}(\tau)\) is malformed: \(c_{1-\alpha}^{(w)}(\tau)\coloneqq \inf_c\{\mathbb{P}(V^{(w)}(X_i,\widetilde T\le c)\ge 1-\alpha\}\) is not syntactically correct as written.
   - In **Algorithm 1**, the notation \(V_t^{(w)}\), \(V^{(w)}\), \(\bar p_i(x)\), \(\Omega(x)\), \(\gamma(x)\), and \(\bar T_{N,n}(X,\tau)\) is inconsistent with the body text. Step 7 has a malformed summation index and a quantile expression that is difficult to parse.
   These are not cosmetic issues because the paper’s central object is a carefully defined weighted conformal quantile; if the notation is slippery, reproducibility and verification suffer.

4. The treatment of the target quantity itself is conceptually blurry. The stated goal on **Page 3** is coverage under \(\mathbb P_{X,T(w)}\), namely
\[
\mathbb P(T(w)\ge \hat L_{N,n}^{(w)}(X))\ge 1-\alpha,
\]
but **Theorem 4.1** is stated under \((X,T(w))\sim \mathbb P_X\times \mathbb P_{T(w)\mid X,e=1}\), and **Theorem 4.2** similarly involves \(P_{T(w)\mid X,e=1}\). Since \(e\) is defined from the observed outcome process, conditioning counterfactual outcomes on \(e=1\) needs much clearer justification. The paper informally uses \(T=\tilde T\) when \(e=1\), but that only applies to factual observed outcomes in the selected subset, not automatically to the full counterfactual target distribution. This mismatch between the stated estimand and the theorem statements needs to be resolved carefully.

5. The “doubly robust” claim is not positioned convincingly enough relative to what is actually proven in the main paper. **Theorem 4.2 on Pages 6-7** is asymptotic, depends on technical assumptions A1/A2, and is introduced via Appendix Corollary B.4. That is much weaker than the broad claim in the abstract that “our procedure is doubly robust against model misspecification.” The assumptions in A2 are also quite nonstandard-looking in presentation, especially the requirement
\[
\lim_{N\to\infty}\left[\frac{\mathcal E_N(X)}{\bar\gamma_N(x)}\right]
=
\lim_{N\to\infty}\left[\frac{\mathcal E_N(X)}{\gamma(x)}\right],
\]
which is written as if equality of two limits is itself an assumption. This needs clearer interpretation and justification. As written, the double robustness story feels more advertised than demonstrated.

6. The empirical section is useful but not yet strong enough for the paper’s central claims. In **Figure 1**, the coverage differences between methods are often fairly small, and the gains in relative LPB depend on the setting. The paper claims “exact statistical guarantees” and “less conservative LPBs,” but the experiments do not really isolate when the gain comes from exact reweighting versus simply using different calibration subsets or different quantile-model behavior. More ablations centered on the weight model would matter a lot here because the theory and method hinge on \(\gamma(x)\).

7. Relatedly, the method is extremely sensitive in principle to estimation of \(\gamma(x)=p(W=w,e=1\mid X=x)\), but the main paper gives very limited visibility into this component. The classifier used is a random forest, but there is no diagnostic for calibration/quality of \(\hat\gamma\), no distribution of estimated weights, and no failure analysis for near-positivity violations. This matters because overlap issues are not hypothetical in the real dataset. **Table 4 on Page 28** shows substantial imbalance for some regimens, especially concurrent chemotherapy (\(p(W=1)=0.88\)) and others with skewed treatment allocation. In such settings, \(1/\hat\gamma(x)\) can become unstable, which directly affects the weighted conformal quantiles.

8. The real-data causal interpretation is too aggressive given the assumptions and the evidence presented. The paper repeatedly connects higher LPB to “better clinical benefits” and personalized treatment selection, but the real dataset is retrospective and the key identification assumption is strong ignorability,
\[
\{T(1),T(0)\}\perp\!\!\!\perp (W,C)\mid X
\]
from **Assumption 3.1**. This bundles treatment ignorability and censoring independence together and is very strong in observational oncology data. The paper does mention this limitation in the discussion, but the conclusions in **Section 5.2** still read too close to treatment-effect claims from an observational benchmark.

9. The literature positioning is thinner than it should be on robustness-oriented conformal survival methods. The paper cites several survival conformal works, but given how prominently it claims double robustness and exactness under right-censoring, I expected a sharper comparison to recent doubly robust conformal survival analysis and to other weighted conformal methods under censoring/covariate shift. As written, the distinction from adjacent robust conformal survival approaches is not fully articulated.

10. Some empirical claims are overstated relative to what the figures show. For example, **Figure 3** is used to argue robustness to outliers, but the performance of all methods degrades as outlier severity increases, and the comparison is based on a single synthetic setting with one kind of perturbation. That is a useful stress test, but not enough to support a general robustness claim.

11. The paper’s presentation quality in the experimental section is uneven. **Figure 2** is cited as a multi-treatment extension, but in the main paper it is barely discussed beyond a short paragraph. The small number of trials there, and the lack of more detailed statistical summaries, make it hard to judge whether the treatment ranking is stable or just noise. Likewise, several important experimental details are deferred to the appendix, leaving the main paper somewhat under-specified.

12. There are multiple typographical and exposition issues that cumulatively hurt readability: malformed equations, inconsistent use of \(\epsilon\) versus \(e\) in theorem statements, and some awkward phrasing such as “under-treated general right-censored data setting.” Any one of these would be minor, but together they make the paper harder to audit than it should be for a theory-heavy submission.

## Questions
1. Please clarify precisely what claim of “exact” validity you want the reader to take away. Is the intended statement exact coverage only when \(\mathfrak D=\omega\), and otherwise a finite-sample lower bound with an estimation-error term as in **Theorem 4.1**? If so, the abstract and introduction should be rewritten to reflect that distinction.

2. Can you rewrite the derivation leading to **Equation (1)** in a cleaner theorem-lemma style in the main paper? In particular, please spell out the exact event whose probability is upper bounded, the role of Lemma A.1, and the conditions under which the passage from \(T(w)\) to \(\widetilde T\) on the \(\{W=w,e=1\}\) subset is valid.

3. What is the exact target distribution in your guarantees: \(\mathbb P_X\times \mathbb P_{T(w)\mid X}\) or \(\mathbb P_X\times \mathbb P_{T(w)\mid X,e=1}\)? This is currently inconsistent across the problem statement and theorems. A careful clarification here would substantially affect my confidence.

4. Please explain the practical meaning of assumption A2 in **Theorem 4.2**, especially the condition in **Equation (5)**. How should a reader interpret that equality of limits, and why is it the right condition for the advertised doubly robust behavior?

5. How stable are the estimated weights in the real dataset? A rebuttal with simple diagnostics, for example histograms or quantiles of \(1/\hat\gamma(X)\), effective sample size, or the proportion of very small \(\hat\gamma(X)\), would increase confidence considerably, especially given the treatment imbalance visible in **Table 4**.

6. Can you provide an ablation where the same quantile regressor is used but the weighting model is varied or intentionally misspecified, and then report how coverage changes? This would directly test the central mechanism of the method more convincingly than the current comparisons.

7. In **Figure 1**, some coverage differences are small while LPB differences vary by setting. Could you add statistical uncertainty summaries or paired significance-style comparisons across trials? Right now it is hard to tell which observed improvements are robust.

8. For the real-data claims in **Figure 4** and **Figure 5**, I would strongly encourage more careful language distinguishing predictive benchmarking from causal treatment-effect conclusions. Are you willing to tone down these interpretations?

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
The paper uses anonymized retrospective clinical data and explicitly states ethics approval in the paper. I do not see an ethics issue that requires special escalation based on the provided content. That said, the paper should be more cautious in causal interpretation of observational treatment comparisons, but this is a scientific validity issue rather than a separate ethics-review trigger.

## Soundness Rating
2: fair. The paper has a reasonable high-level idea and some technical support, but the central derivation, target estimand, and “exact validity” claims are not presented cleanly enough for me to view the technical case as fully solid.

## Presentation Rating
2: fair. The structure is standard and some figures are helpful, but notation inconsistencies, malformed equations, and imprecise theorem framing significantly reduce clarity.

## Contribution Rating
2: fair. The problem is important and the weighted conformal counterfactual-survival angle is potentially useful, but the contribution is weakened by overstated claims, unclear positioning, and only moderately convincing empirical support.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The paper addresses an important problem and has some promising ingredients, but in its current form I do not think the theory-to-claim alignment and presentation are strong enough for a clear accept recommendation.

## Reviewer Confidence
4: confident. I am confident in the assessment and checked the main equations, theorem statements, tables, and figures carefully, though some appendix-level technical details are sufficiently messy that absolute certainty would be too strong.