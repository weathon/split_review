---
job_id: 05751b10-28bc-41f4-b73d-4bca44c2e1a2
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: jZcWBV3Pis.pdf
paper: Evaluating the Robustness of Chinchilla Compute-Optimal Scaling
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is squarely about large-scale learning, empirical scaling laws, and robustness of compute-optimal training prescriptions for language models, which fits ICLR’s scope in general machine learning and learning theory/empirical analysis.

## Minimum Quality
Pass ✅. The submission has the necessary scientific structure for this kind of empirical re-evaluation paper, including abstract, introduction, related work, methodological analysis, quantitative results, and discussion; while I have concerns about novelty and evidential strength, these are review-level issues rather than desk-reject-level flaws.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find any hidden prompts, suspicious reviewer-targeting instructions, or other manipulative content in the provided paper text.

# Expected Review Outcome:
## Summary
This paper revisits the robustness of the Chinchilla compute-optimal scaling results from Hoffmann et al. (2022). The authors first identify an ambiguity in the model parameter counts used in Chinchilla, showing that three plausible interpretations of parameter count differ by up to 15.2%, and then refit the standard Chinchilla loss law under those alternatives. They further perform a sensitivity analysis by perturbing parameter counts in four structured ways, multiplicative, additive, systematic bias, and log-normal noise, and study the effect on the fitted scaling-law parameters and the implied compute-optimal tokens-per-parameter ratio.

## Strengths
The paper asks a useful and well-motivated question. Chinchilla remains a widely used heuristic in practice, so checking whether its conclusions are fragile to ambiguities in model-size accounting is a relevant contribution even if the paper is mostly a re-analysis rather than a new method.

The empirical finding in **Figure 2** is the paper’s strongest point. The top row shows that the fitted parameters \((\hat E, \hat A, \hat \alpha, \hat B, \hat \beta)\) remain fairly similar across the three parameter-count interpretations, and the bottom row directly targets the headline practical question by plotting the compute-optimal \(D/N\) ratio against compute. This is exactly the right figure to include, because it connects the bookkeeping ambiguity from Section 2 to the actual downstream prescription practitioners care about.

The paper also does a good job of making the parameter-count discrepancy concrete rather than merely hand-wavy. **Table 1** is useful here: it places Chinchilla’s reported values side by side with the “standard formula” and “best fit formula” counts, and makes clear that the disagreement is not anecdotal but systematic across the model family. Likewise, **Figure 1** is effective in visualizing that the standard formula disagrees for all \(50/50\) models, while the ad hoc “best fit” formula reduces but does not eliminate the mismatch.

The perturbation taxonomy in Section 3 is reasonably intuitive. **Figure 3** helps by showing the geometry of the four perturbation families before the reader is asked to interpret their consequences. That figure supports the paper’s central framing better than a purely symbolic description would have.

The paper is generally readable, and the narrative from “there is an ambiguity” to “does the Chinchilla recommendation survive?” is easy to follow. For a short empirical re-examination paper, the central story is coherent.

## Weaknesses
1. **The core empirical conclusion is weaker than the rhetoric suggests, because the paper mainly shows robustness under perturbations of the independent variable \(N\), not robustness of the underlying compute-optimal scaling claim itself.**  
   The paper repeatedly claims to provide “renewed confidence” that Chinchilla is a “durable guide” and a “practical blueprint” (**Abstract**, **Page 1-2**, **Discussion on Page 9**). But the analyses only perturb model parameter counts while keeping the same original loss measurements and the same Chinchilla functional form \(L(N,D)=E+A N^{-\alpha}+B D^{-\beta}\) in **Equation (4)**. This means the paper is testing a fairly narrow notion of robustness: sensitivity to model-size bookkeeping. It does not probe robustness to the more consequential issues raised in the literature, such as experimental design, optimizer dependence, training horizon choices, data quality, or misspecification of the separable power-law form itself. That matters because the conclusion is framed broadly, while the evidence addresses a much narrower target.

2. **The “best fit formula” in Section 2 is under-justified and somewhat ad hoc.**  
   In **Equation (3)**, the authors replace the attention multiplier \(4\) with \(5\), which indeed improves agreement with reported parameters. But the paper never gives a principled architectural reason for this choice. Was an extra projection matrix omitted? Is there an implementation-specific detail? Or is this simply the coefficient that minimizes discrepancy on the observed table? As written, it reads like a reverse-engineered fit to reported numbers rather than a faithful reconstruction of the architecture. This is not fatal for the main result, since the paper’s main claim is that the choice barely matters, but it weakens the interpretation of Section 2. In fact, the paper treats the “best fit” parameterization almost as if it were a legitimate third interpretation, when it is closer to a descriptive interpolation rule.

3. **The statistical evidence for “no meaningful change” is not very strong, because the comparisons are largely visual and bootstrap-based without sharper hypothesis testing or practical-effect criteria.**  
   On **Page 4**, the authors state that none of the five fit parameters differed significantly across parameter interpretations, referring to **Figure 2**. But the evidence shown is primarily overlapping bootstrap intervals. Overlap of error bars is not a strong statistical argument for equivalence, and the paper does not define a practical equivalence margin either. Similarly, the bottom row of **Figure 2** shows visibly different slopes, \(-0.572\), \(-1.049\), and \(-1.248\) per decade, yet the paper concludes that the trend “remains constant” around 20. That is directionally plausible, but it is being sold with more certainty than the presented analysis really warrants. If the main contribution is robustness, then formalizing what counts as a “meaningful” deviation is important.

4. **Some mathematical exposition is sloppy or internally inconsistent, which is avoidable in a paper whose main object is a fitted equation.**  
   There are notation inconsistencies between Sections 3 and Appendix C. In **Equation (6)** on **Page 5**, the perturbed parameters are denoted \(\tilde N_i = c_m N_i\), but on **Page 7** the discussion switches to \(\hat N_i\) and then to \(\hat{\bar A}\), \(\hat{\bar \alpha}\) without prior clean definition. Similar notation drift appears for the additive and systematic perturbations, alternating between \(\hat N_i\) and \(\tilde N_i\). For a paper centered on perturbation formulas, this matters because it makes the derivations harder to audit.  
   There is also a mismatch between what is argued in the main text and what is truly established there. For instance, **Section 3.3** states that \(\hat{\alpha}=10^{-0.46}\cdot s^{-1}\) with \(R^2 > 0.999\), but this is an empirical curve fit to fitted estimates, not a theorem. The analytic expression in **Appendix Equation (25)** is \(\hat \alpha = \alpha/s\), which is conceptually cleaner. The paper would be stronger if it consistently distinguished exact algebraic consequences from empirical regressions on bootstrap outputs.  
   More broadly, **Equation (5)** is not really an equation in the technical sense, it just states the heuristic “\(\approx 20\)”. Since the rest of the paper derives the actual compute-optimal ratio as a function of fitted exponents, the exposition would benefit from putting the derived formula, essentially **Appendix Equations (16)-(17)**, in the main text instead of presenting the heuristic as if it were the mathematical object of study.

5. **The sensitivity analysis is interesting, but the perturbation ranges are only weakly tied to realistic sources of error, so the practical significance is murky.**  
   For example, in **Section 3.1**, the multiplicative perturbation sweeps \(c_m\) from \(10^{-3}\) to \(10^{3}\), which is far beyond any plausible model-parameter miscount. The additive perturbation in **Section 3.2** uses constants on the order of \(10^{6.6}\) to \(10^{7.6}\), and the noise analysis in **Section 3.4** pushes \(\sigma\) up to \(10^{2}\), producing NaNs and near-unidentifiability. These extreme settings may be acceptable for stress-testing, but then the paper should be much clearer that this is a mathematical stress test rather than an empirical claim about realistic ambiguity in Chinchilla-like accounting. As written, the practical takeaway gets blurred: robustness to absurd perturbations is not necessarily the same thing as robustness in realistic scaling-law practice.

6. **The paper does not sufficiently engage with whether the observed robustness is partly a consequence of limited identifiability in the underlying fit.**  
   The introduction itself references concerns about wide confidence intervals, and **Figure 2** indeed shows large uncertainties. But the paper then interprets lack of movement under perturbations as evidence of stability, without seriously considering the alternative explanation that the model is simply weakly identified. If a fit has broad uncertainty, many parameterizations can look “robust” because the confidence region is already large. This is especially relevant for the headline result that the three slopes in **Figure 2** differ but are dismissed because of uncertainty. The paper needs a sharper discussion of whether robustness here means genuine invariance or merely poor sensitivity due to underdetermined fitting.

7. **The contribution is somewhat incremental relative to existing Chinchilla replication and reconciliation work, and the paper’s positioning does not fully articulate what is fundamentally new.**  
   The paper uses existing Chinchilla data and existing fitting code from Besiroglu et al. (**Page 4**), and its main results are re-fits plus synthetic perturbation studies. That can still be publishable if it produces a genuinely clarifying insight, but the manuscript currently overstates the conceptual leap. The strongest genuinely new point is the ambiguity in the parameter counts from Table A9. After that, much of the paper becomes a sensitivity sweep around an already fixed framework. I wanted a more precise articulation of what new scientific understanding this adds beyond “the fit is not too brittle to one kind of bookkeeping issue.”

8. **The results figures are informative, but some of the paper’s main claims should have been supported by tables with explicit numerical comparisons rather than only plots.**  
   This is particularly noticeable for the central robustness claims around **Figure 2** and **Figure 5**. The paper reports some slope numbers in the text, but it does not provide a compact table of fitted parameter estimates, standard errors, and differences across perturbation families or parameter-count interpretations. For a paper arguing “no meaningful change,” a small results table quantifying effect sizes would be much more convincing than relying primarily on visual inspection of wide intervals.  
   Relatedly, **Table 1** is helpful for model-size discrepancies, but there is no analogous table summarizing the actual downstream scaling-law fit outputs across the three interpretations. That omission makes it harder to audit the practical magnitude of the reported robustness.

9. **There is some imprecision in how the paper connects its perturbations to real architectural counting conventions.**  
   In **Section 3.2**, additive constants are motivated by inclusion or exclusion of embeddings. But embedding parameters are not truly an architecture-independent constant across arbitrary model families; they depend on vocabulary size and model dimension. In the specific Chinchilla family, vocabulary is fixed, so the simplification is understandable, but the text sometimes speaks as if additive perturbations are a general abstraction of embedding inclusion/exclusion. That generalization is too loose.

10. **The paper’s practical recommendation is broader than what was actually validated.**  
    The conclusion on **Page 9** says the work should give practitioners “even greater confidence” in Chinchilla’s prescription. That is too sweeping. At most, the paper shows that under one family of published Chinchilla training runs, the fitted recommendation is not highly sensitive to several redefinitions of \(N\). It does not validate Chinchilla across modern regimes with different data mixtures, optimizer choices, architectural families, or inference-aware objectives. The paper would be stronger, and more credible, with a narrower concluding claim.

## Questions
1. For the “best fit” formula in **Equation (3)**, can the authors provide a principled architectural explanation for the factor \(5\) in the attention term? If this is purely reverse-engineered from Table A9, please say that explicitly. My confidence would increase if the paper clearly separated “architecturally motivated interpretation” from “descriptive fit to reported counts.”

2. Can the authors define a quantitative robustness criterion for the main claim “do not meaningfully change”? For example, what maximum change in \(\hat\alpha,\hat\beta\), or in the slope of the compute-optimal \(D/N\) curve, would count as scientifically meaningful? Right now the paper mostly relies on overlapping intervals and visual inspection.

3. Could the authors add a small table, in the main paper, listing the fitted \((\hat E,\hat A,\hat\alpha,\hat B,\hat\beta)\) and uncertainty for the three parameter interpretations shown in **Figure 2**? This would make the central empirical claim easier to assess than the current plot-only presentation.

4. The paper repeatedly interprets large uncertainty as making strong conclusions difficult, especially in **Page 4** and **Section 3.4**. Can the authors discuss more directly whether the apparent robustness could partly reflect weak identifiability of the fitted scaling law, rather than true invariance of the compute-optimal prescription?

5. For **Section 3**, what perturbation ranges do the authors consider realistic versus purely stress-test settings? A brief calibration against plausible parameter-counting errors in actual Transformer accounting would make the practical implications much clearer.

6. Since **Equation (4)** is the backbone of the entire analysis, can the authors justify more explicitly why robustness to perturbations in \(N\) should be interpreted as robustness of Chinchilla itself, rather than robustness of one specific separable power-law fit? A discussion of model misspecification would help.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
None.

## Soundness Rating
2: fair. The empirical analysis is generally competent and the main computations seem plausible, but several central claims are broader than the evidence presented, and the statistical/mathematical exposition is not sharp enough for higher confidence.

## Presentation Rating
3: good. The paper is readable and the figures are generally useful, especially Figures 1 to 3, but notation drift and the lack of a compact numerical results table limit clarity.

## Contribution Rating
2: fair. The parameter-count ambiguity is a worthwhile observation, and the sensitivity analysis is somewhat informative, but the contribution feels closer to a targeted robustness check than a substantial advance in the scaling-laws literature.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The paper asks a relevant question and contains a useful re-analysis, but the contribution is narrower and less conclusive than the framing suggests, and the evidence does not fully support the paper’s broad “renewed confidence” message.

## Reviewer Confidence
4: confident. I am confident in this assessment, though not absolutely certain. The paper is in an area I know well, and I checked the main equations, figures, and empirical claims carefully.