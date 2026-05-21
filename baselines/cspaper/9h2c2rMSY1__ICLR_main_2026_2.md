---
job_id: c9094bc3-7ad7-4964-b86b-bd25bebb7b71
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: 9h2c2rMSY1.pdf
paper: Weighted Conformal Prediction for Time-Dependent PDEs
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, it studies uncertainty quantification and conformal prediction for ML surrogate models of time-dependent PDEs, with both theoretical and empirical components.

## Minimum Quality
Pass ✅. The paper includes the expected components, namely abstract, introduction, related work, technical development in Section 4, experiments in Section 5, quantitative results in Figure 3 and Table 1, and a discussion/conclusion in Section 6. While I have substantial concerns about assumptions, evaluation scope, and some technical and presentation details, these are review-level weaknesses rather than desk-rejection issues.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find evidence in the paper text of hidden prompts, reviewer-directed instructions, or other manipulative content targeting automated or LLM-based review systems.

# Expected Review Outcome:
## Summary
This paper studies conformal prediction for surrogate models of time-dependent PDEs under temporal distribution shift. The main technical points are, first, a result showing that in an infinite-dimensional function-space formulation, solution laws at times \(t\) and \(t+\delta\) can be mutually singular even for the heat equation, and second, a weighted conformal prediction approach for discretized linear PDEs where the time-dependent solution law is derived in closed form and used to compute likelihood-ratio weights. The paper also provides experiments on synthetic PDEs and a small pulsed-thermography dataset.

## Strengths
1. The paper tackles a real and important problem. The central issue, namely that exchangeability-based CP can fail badly for time-evolving scientific systems, is highly relevant for scientific ML and uncertainty quantification.

2. The function-space warning in **Theorem 4.1** is interesting and worth surfacing. The result makes a useful conceptual point: if one reasons directly with infinite-dimensional laws, “small” time shifts need not imply any meaningful closeness in total variation. That is a nontrivial caution for a literature that often speaks loosely about function-space operators and calibration as if those viewpoints transfer seamlessly.

3. The discretized linear-Gaussian derivation in **Theorem 4.2** is clean and easy to follow. Under the stated assumptions, the mean and covariance propagation
\[
\mu_t = e^{tA}\mu_0 + \int_0^t e^{(t-s)A}r(s)\,ds,\qquad
\Sigma_t = e^{tA}\Sigma_0 e^{tA^\top}
\]
is correct and directly enables closed-form weights in **Equation (1)**. I appreciated that the key proof is in the main text rather than being hidden away.

4. The paper does a good job visually motivating the phenomenon it is trying to address. **Figure 2** is particularly helpful: the top-row and bottom-row comparison makes the undercoverage story tangible, and it supports the paper’s claim that “just use a smaller time step” is not a reliable fix when instability grows over time. Even though this is an illustrative figure rather than a comprehensive experiment, it is one of the clearer parts of the paper.

5. The main synthetic results do show a consistent qualitative pattern. In **Table 1**, naive CP and LSCI often under-cover as the horizon grows, especially for more unstable settings, while WCP avoids blatant undercoverage by inflating or becoming infinite. This at least supports the paper’s narrow claim that weighting can protect coverage under the paper’s own generative assumptions.

6. The paper is generally readable. The high-level motivation is clear, the notation is mostly manageable, and the transition from impossibility in function space to recoverability in discretized space is conceptually coherent.

## Weaknesses
1. The paper’s strongest practical claim is overstated relative to what is actually established. On **Page 2**, contribution 2 says the method “enables exact coverage guarantees for PDEs without limiting assumptions on their time-dependent behavior.” That is too broad. The actual formal development in **Section 4.3** and **Section 4.4** requires a discretized **linear** PDE, a known discretization matrix \(A\), deterministic forcing \(r(t)\), and a parametric initial distribution for which the time-marginal density is available in closed form, with the main theorem stated for Gaussian initial conditions. This is not “without limiting assumptions”; it is a fairly restrictive and structured setting. The gap matters because the paper repeatedly frames itself as solving CP for time-dependent PDEs in general, but the guarantees are tied to a narrow subclass where the density ratio is analytically available.

2. There is a conceptual mismatch between the conformal formulation in **Section 3.1** and the actual prediction task in the experiments. Weighted CP in the Barber et al. setup reweights based on a covariate shift ratio \(p_{\text{test}}(x)/p_{\text{cal}}(x)\). In **Equation (1)** on **Page 7**, however, the weights are defined using \(\mathcal N(u_i;\mu_{t+\delta},\Sigma_{t+\delta})/\mathcal N(u_i;\mu_t,\Sigma_t)\), where \(u_i\) appears to be the PDE solution itself. The paper never cleanly specifies what is the “covariate” \(x\), what is the “label” \(y\), and what object the conformity score is computed on in the split-CP pipeline. In **Section 5**, the base model predicts future solutions from initial conditions, but the weighting is described on the law of the solution at each time point rather than on the law of the model input. This is not a cosmetic notation complaint, it matters for whether the weighted-CP guarantee actually applies to the implemented procedure. If the residual score is \(s(x,y)\) with \(x=u_0\) and \(y=u_t\), then one needs the correct Radon-Nikodym derivative over the exchangeable unit used by conformal calibration, not simply the marginal ratio on \(u_t\) unless that is the calibrated object.

3. Related to the previous point, the calibration object is underspecified enough that I cannot fully verify the validity claim. **Section 5** says the method is “based on a weighted version of Diquigiovanni et al. (2022)” and that the score is weighted according to **Equation (1)**, but it does not state:
   - the exact nonconformity score \(s_i\),
   - whether the score is computed from the residual \(\| \hat u_t - u_t\|_\infty\), the max absolute error over spatial grid points, or something else at each horizon,
   - whether weighting is applied to calibration samples only or calibration plus test point, as required by weighted split CP,
   - how ties and randomization are handled,
   - and, crucially, what criterion produces the “infinite band” outcome.
   
   The last point is especially important. In **Section 5, Evaluation**, the authors state that “our WCP method predicts infinite bands” when dissimilarity is too large, but there is no formal rule in the main paper saying when the weighted quantile becomes infinite or how this is encoded algorithmically. This is central to the empirical story and to the coverage interpretation, yet the implementation logic is absent from the main text.

4. The empirical evidence is too narrow for the breadth of the claims. The synthetic evaluation in **Section 5** uses essentially one family of 1D second-order linear PDEs with varying coefficients \(a,b,c\), one surrogate architecture, and only two baselines. There is no evidence on nonlinear PDEs, no evidence on advection-dominated or mixed boundary-condition settings beyond the narrow setup, and no experiment showing robustness when the analytical density is slightly misspecified. Since the method’s selling point is practical uncertainty quantification for time-dependent PDE surrogates, the current experiments feel like a controlled proof-of-concept rather than a convincing case for broader usefulness.

5. The baseline set is weak and under-positioned for a paper about non-exchangeable conformal prediction in time-dependent settings. The paper compares only to naive CP and LSCI in **Section 5**. Given the literature discussed in **Section 2**, and more broadly the time-series CP literature, the paper should compare against at least one stronger temporal reweighting or adaptive baseline beyond “naive” and a local-exchangeability method. As written, the comparison is somewhat stacked: one baseline is intentionally assumption-violating, the other is a method whose assumptions the paper argues are hard to verify. That does not by itself show that the proposed weighting is the right solution, only that two vulnerable alternatives can fail.

6. The presentation of the experimental results is selective in a way that inflates the apparent success of WCP. In **Figure 3** and throughout **Section 5**, coverages are omitted when infinite bands are reported, and in the text the authors emphasize that “WCP consistently meets its coverage guarantees.” But in **Table 1**, this picture is more nuanced. For example, for \(a=-0.0075, c=-0.5\), timestep 15, WCP coverage is reported as \(0.84\) with \(n_\infty = 86.4\%\), and for \(a=-0.01, c=-0.5\), timestep 10, WCP is \(0.88\) with \(n_\infty = 35.4\%\). These are not just stochastic blips, they indicate that the reported “non-trivial only” coverage can fall below nominal while a large fraction of samples have already been discarded into the trivial infinite-band bucket. This does not invalidate the method, but it does mean the practical message should be much more honest: WCP often preserves formal validity by refusing to give useful intervals. That is a very different claim from “the only method providing reliable coverage over time.”

7. The real-world experiment is not convincing as evidence for the main contribution. On **Page 10**, the paper says the method “achieves target coverage over all tested time steps,” but the actual real-data setup in **Appendix A.6** has only 19 samples total, split into 8 train, 1 validation, 7 calibration, and 3 test surfaces, then further converted into patches treated as identically distributed. That patching assumption introduces dependence, which the appendix itself admits. More importantly, the main text does not present a quantitative table for the real data, only a brief statement. Since the experimental claim in the abstract includes validation “on several time-dependent PDEs,” the real-world part is too small and too loosely described to substantially strengthen the paper.

8. Theoretical positioning is weaker than it looks because **Theorem 4.1** is conceptually interesting but operationally detached from the proposed method. The theorem is about mutually singular laws in an infinite-dimensional Hilbert-space setting for the heat equation with a very specific Gaussian prior. The actual method, however, is entirely finite-dimensional and uses spatial discretization from the start. So the paper builds substantial narrative weight on a theorem that is more of a cautionary observation than a technical foundation for the algorithm. I do not object to including it, but the current presentation oversells it as if it were the key reason the weighted discretized method is needed. In reality, one could motivate the weighted method directly from ordinary time-varying finite-dimensional distributions without invoking infinite-dimensional mutual singularity.

9. There are several mathematical and notation issues that reduce confidence in the rigor of the exposition:
   - In **Section 3.1**, the weighted CP description uses \(w_i \propto p_{\text{test}}(x_i)/p_{\text{cal}}(x_i)\), but the next sentence says the index ranges over all calibration data points and the target test point. The paper does not write the exact normalized weighted quantile formula or how the test-point weight enters, which is important for exact finite-sample validity.
   - In **Theorem 4.1** on **Page 6**, the notation \(\mathcal P_0 \sim \mathcal N(0,(I-\Lambda)^{-1})\) is sloppy; \(\mathcal P_0\) is a measure, not a random variable. It should say \(u_0 \sim \mathcal N(0,(I-\Lambda)^{-1})\) and \(\mathcal P_0\) is the induced law.
   - In **Remark 4.5** on **Page 8**, the paper claims asymptotic and “in some cases even non-asymptotic” guarantees for the original continuous-space solution by transferring discretized bands via numerical error bounds, but no theorem, bound, or formal statement is given in the main paper. This reads as a teaser rather than a substantiated claim.

10. The synthetic setup is somewhat engineered in favor of the paper’s narrative. On **Page 8-9**, the authors explicitly choose \(a<0\) because otherwise other CP methods “trivially cover at future time steps.” That is understandable for stress-testing, but it also means the evaluation largely focuses on unstable backwards-heat-like regimes where ordinary residual calibration is expected to struggle. A stronger paper would show both sides: regimes where standard CP is adequate, regimes where it fails, and a principled characterization of when WCP gives informative rather than merely valid-by-triviality intervals. As it stands, the study emphasizes failure modes of baselines without equally characterizing the informativeness limits of the proposed approach.

11. Some figures are more illustrative than evidentiary. **Figure 3** usefully summarizes coverage trends across parameter settings, but the dotted \(n_\infty\) curves are arguably the most important practical signal and are visually secondary to the coverage lines. This contributes to the paper’s optimistic framing. Similarly, **Figure 2** is effective as a toy illustration, but because it shows single examples rather than aggregated statistics, it should not carry so much argumentative weight in the introduction and related-work critique.

## Questions
1. Please specify the conformal pipeline precisely. What are the exchangeable units, what are \(x\) and \(y\), what exact nonconformity score \(s(x,y)\) is used, and what is the exact weighted split-CP quantile formula implemented? I would like to see the full main-text definition, not just a reference to a weighted version of Diquigiovanni et al. This would substantially increase my confidence in the validity claim tied to **Equation (1)**.

2. Why is the density ratio in **Equation (1)** written over \(\bm u_i\) rather than over the full calibrated object used by conformal prediction? If the prediction task is from \(u_0\) to \(u_t\), please explain formally why weighting only by the time-\(t\) solution marginal is sufficient for exact coverage. If there is a covariate-shift reduction or a conditional-score argument here, it needs to be stated.

3. What exactly triggers an infinite band in WCP? Is it a consequence of a weighted quantile becoming unbounded because the test-point weight dominates, a numerical safeguard, or an explicit abstention rule? A concise theorem or proposition clarifying when this happens would help a lot.

4. Can the authors add at least one stronger baseline for non-exchangeable sequential prediction, especially a reweighted or adaptive CP method not based on local exchangeability? Right now the empirical comparison is too narrow to establish that the proposed weighting strategy is competitive rather than merely valid under the paper’s handcrafted assumptions.

5. Can the authors report overall coverage including the infinite intervals, alongside the current “non-trivial-only” coverage? The current presentation obscures the tradeoff between validity and usefulness. A table showing, for each horizon, nominal coverage, non-trivial fraction \(1-n_\infty\), and average finite bandwidth conditional on finite bands would make the practical utility much clearer.

6. Please clarify the scope of the guarantee in **Remark 4.5**. If transfer from discretized bands to continuous-space bands is important, can you state at least one explicit theorem in the main paper for a concrete discretization scheme?

7. For the real-world thermography example, can you provide a main-paper quantitative summary rather than only a brief statement? Given the tiny number of surfaces and the patching heuristic, more transparency about uncertainty in that evaluation is necessary.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No specific ethics concerns based on the main paper. The applications are safety-relevant, which reinforces the importance of honest uncertainty quantification, but I did not identify dataset, privacy, or misuse issues that would require ethics escalation.

## Soundness Rating
2: fair. The core linear-Gaussian derivation is sound under its assumptions, but the connection between the weighted CP guarantee and the actual implemented prediction task is underspecified, and the empirical evidence is narrower than the claims.

## Presentation Rating
3: good. The paper is readable and the high-level story is easy to follow, but several key technical definitions are missing or too implicit, and some claims are framed more broadly than what the paper actually proves.

## Contribution Rating
2: fair. There is a useful and interesting idea here, especially the finite-dimensional weighting angle for time-dependent PDE surrogates, but the scope is limited, the empirical validation is not yet broad enough, and the practical contribution is weakened by frequent fallback to trivial infinite bands.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted.  
The paper has a solid core observation and a plausible method in a restricted setting, but the current version overclaims on generality, underspecifies the conformal machinery at the crucial point, and provides too narrow an empirical case to justify acceptance at ICLR. With a cleaner formal statement of the guarantee, stronger baselines, and more honest reporting of the validity-versus-utility tradeoff, this could become much more convincing.

## Reviewer Confidence
4: confident. I am confident in the overall assessment and checked the main mathematical development carefully, although I cannot fully verify the implementation details because the conformal pipeline is not specified precisely enough in the main text.