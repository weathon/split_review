---
job_id: f0688976-9c28-4cf3-9299-108d272e75f8
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: ikthqd3qF4.pdf
paper: Precision Without Labels: Detecting Cross-Applicants in Mortgage Data Using Unsupervised Learning
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is squarely about unsupervised evaluation/model selection for anonymous record linkage, with theoretical guarantees and large-scale empirical validation, which fits ICLR topics in unsupervised learning, learning theory, and ML applications.

## Minimum Quality
Pass ✅. The paper has the core ingredients of a research submission, including abstract, introduction, methodology, simulation experiments, empirical results, and conclusion; while the related-work positioning is thinner than it should be, the submission is complete enough to review on the merits.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find any hidden prompts, suspicious instructions to automated reviewers, or other manipulative content in the provided paper text or figures.

# Expected Review Outcome:
## Summary
This paper studies how to evaluate and tune unsupervised anonymous record linkage models without labeled data. The core idea is to exploit a structural constraint, namely that one individual can realize at most one positive outcome, to derive observable lower bounds on precision and relative recall from the predicted clusters themselves. The authors instantiate the framework with hierarchical clustering on confidential HMDA mortgage application data to identify repeated applicants across lenders, and report a preferred specification with an estimated 92.3% precision.

## Strengths
The main strength is that the paper tackles a real and difficult problem: model selection and evaluation in record linkage settings where labels are unavailable. The use of domain structure, specifically the "at most one origination" constraint, is a sensible and practically useful angle, and the paper articulates clearly why this is valuable for privacy-constrained or cross-institutional datasets.

The paper is also commendably scalable. The HMDA application is not a toy example, it is a 65.5 million application dataset, and the authors do at least make an effort to discuss computational feasibility in Section 2.1 and Appendix B. For an ICLR audience, it is useful to see that the proposed criterion is not just theoretically stated but actually used to choose among many model specifications at realistic scale.

Some of the visualizations are effective. **Figure 1** and **Figure 2** do a good job of explaining the partition-then-cluster pipeline and the role of the threshold $\varepsilon$ in complete-linkage agglomerative clustering. In particular, **Figure 2** makes the truncation idea very concrete and helps the reader understand why a single dendrogram can support multiple $\varepsilon$ values without recomputing clustering. This is one of the clearer parts of the paper.

The simulation section is also directionally helpful. **Figure 3a** shows the true precision curve as a function of $\varepsilon$, and **Figure 4a** shows the implied precision bound from the proposed theory. The qualitative similarity between these two panels supports the paper's central intuition that multiple-originations-per-cluster can serve as a usable proxy for linkage quality. Likewise, **Table 2** in the appendix, although limited, shows that the lower bound tracks the true precision fairly closely in the "with date" simulation, which gives some evidence that the bound is not vacuous in the authors' stylized setting.

Finally, the application domain is meaningful. If the method works as advertised, identifying cross-applicants in mortgage data could indeed support downstream fairness, shopping-behavior, and market-monitoring analyses.

## Weaknesses
1. **There is a serious mathematical/sign inconsistency in the key bound on Page 5, and it directly affects the central evaluation quantity.**  
   After discussing the removal of clusters with multiple originations, the paper states a "new lower bound on the precision of our algorithm" as
   \[
   \Pr[\text{False}] \geq \frac{1-\Pr[\text{Mult}]/p^2}{1-\Pr[\text{Mult}]}. \tag{1}
   \]
   This cannot be right as written. Precision is $\Pr[\neg \text{False}]$, not $\Pr[\text{False}]$, and the right-hand side is near 1 in the numerical examples, so it clearly behaves like a lower bound on precision rather than on false positive rate. The empirical counterpart in Equation (2),
   \[
   \Pr[\widehat{\text{False}}] \geq \frac{1-\hat p_m/\hat p^2}{1-\hat p_m} = \hat\alpha(\theta),
   \]
   has the same issue, yet later $\hat\alpha(\theta)$ is explicitly treated as a lower bound on precision in Corollary 1 and Corollary 2. This is not a cosmetic typo, because $\hat\alpha(\theta)$ is the core object used for model selection throughout the paper, including the interpretation of **Figure 4** and **Figure 5**. The authors need to correct the event being bounded, re-derive the post-filtering expression carefully, and ensure all subsequent notation is consistent.

2. **The central assumptions are much stronger and more fragile than the paper acknowledges, especially in the actual HMDA setting.**  
   Assumption 1 on Page 3 states independence of origination decisions across borrowers:
   \[
   \Pr[O_{im}=1 \mid O_{jl}=1] = \Pr[O_{im}=1], \quad i\neq j.
   \]
   But the algorithm intentionally creates partitions where records share highly specific attributes such as census tract, property type, occupancy, loan purpose, race, sex, age, loan type, and co-applicant status, see Page 8. Within such narrow partitions, origination outcomes across distinct borrowers are plausibly correlated through local market conditions, underwriting standards, regional shocks, and lender composition. If this dependence is positive, then $\Pr[\text{Mult}\mid \text{False}]$ can differ materially from the stated lower-bound logic, and the resulting precision guarantee may be miscalibrated. The paper calls Assumptions 1 and 2 "not very strong" on Page 5, but that is not convincingly argued. At minimum, the paper should discuss why these assumptions are plausible after such aggressive partitioning, and how violations would bias the bound.

3. **Assumption 2 is under-motivated and not obviously appropriate for the quantity it is used to bound.**  
   Assumption 2 requires that
   \[
   \Pr\!\left[\sum_m O_{im}=1 \mid n_i=k+1\right] \geq \Pr\!\left[\sum_m O_{im}=1 \mid n_i=k\right], \ \forall k.
   \]
   This monotonicity in the number of submitted applications is doing important work in Lemma 1, but it is not empirically checked and is not clearly justified in the mortgage-shopping context. A borrower who submits more applications could be systematically weaker, more rate-sensitive, or rejected more often, which cuts the other way. The application-level origination process is a combination of approval, timing, and borrower choice, so monotonicity in $n_i$ is not automatic. Since the theorem's usefulness depends on this assumption, the paper needs either a stronger domain justification, a sensitivity analysis, or a theorem under alternative weaker conditions.

4. **The experimental evaluation is too insular, because the paper evaluates only one clustering family and essentially no competing unsupervised evaluation schemes.**  
   The method is presented as "method-agnostic" in the Introduction and Section 2, but empirically the paper only instantiates complete-linkage agglomerative clustering with hand-designed distances. There is no comparison to other linkage strategies, even simple ones such as nearest-neighbor matching within partitions, density-based clustering, or learned similarity scoring followed by thresholding. More importantly, for the evaluation problem itself, the paper does not compare its lower-bound criterion against existing unsupervised record-linkage or entity-resolution evaluation approaches. This weakens the "first work" positioning. There is relevant prior work on unsupervised evaluation of entity resolution and linkage quality estimation that should be discussed and, ideally, benchmarked against, rather than treating the space as empty.

5. **The literature positioning is incomplete for a paper whose central claim is about unlabeled evaluation of record linkage.**  
   The manuscript contains no dedicated related work section, and the introduction cites almost no directly comparable prior work on unsupervised linkage evaluation. In particular, there is prior literature on unsupervised evaluation of entity resolution / record linkage without ground truth, including work by Nanayakkara et al. on unsupervised evaluation of entity resolution, Franke et al. on estimating linkage quality without labels, and theory on the microclustering regime such as Johndrow et al. These are not minor omissions, because they bear directly on the claimed methodological contribution: observable precision/recall estimation without labels. Even if the present paper's structural-constraint approach is distinct, the reader needs a careful comparison to understand what is genuinely new here, what is weaker or stronger than prior methods, and where the method sits in that literature.

6. **The model-selection story is less principled than advertised because the distance functions are largely hand-crafted and weakly justified.**  
   On Page 8 and in **Table 1**, the authors consider 96 combinations of distances and tolerances. However, the candidate distances include ad hoc constructions such as "Penalize Exact" and "Reward Exact" with hard-coded constants like $55$ and threshold $7$, see Appendix B. There is little explanation of where these choices come from, whether they were tuned on the same data, or whether the results are sensitive to them. **Table 1** makes this issue particularly visible: the search space is not a clean family of metric-learning choices, it is a bag of manually engineered heuristics. That does not invalidate the application, but it weakens the scientific contribution because the paper's empirical success may depend as much on bespoke distance engineering as on the proposed unlabeled evaluation criterion.

7. **The main empirical application provides no ground-truth validation, only indirect diagnostics, so the headline 92.3% precision remains hard to trust.**  
   I understand that labeled identities are unavailable by construction, but the paper could still provide stronger validation. For example, it could evaluate on a subset with external linkage signals, synthetic perturbations, or controlled holdouts. Instead, the main paper relies on the theoretical bound and qualitative diagnostics. **Figure 5** shows a precision-sample-size frontier, but the points are unlabeled, so the reader cannot tell which specific $(d,\varepsilon)$ choices are driving the frontier or whether neighboring points correspond to stable behavior versus fragile heuristics. The orange "knee" argument is plausible, but visually it is still a judgment call. Given that the entire application rests on selecting one operating point from this frontier, the evidence feels thinner than the confident conclusion suggests.

8. **Several presentation and notation choices make the technical argument harder to follow than necessary.**  
   There is recurrent slippage between clusters, applications, and applicants. For example, on Page 5, $N^+(\theta)=TP(\theta)+FP(\theta)$ is described as "the number of applications the classifier flags as cross-applicants", but elsewhere positives appear to be clusters rather than applications. This matters because recall and sample size are interpreted using $P_{\text{tot}}$, the number of true cross-applicants, not true positive applications. The unit of analysis needs to be stated consistently. Similarly, Equation (3) on Page 8 writes
   \[
   d(x_j,x_{j'}) \leq \left(\sum_{s=1}^r d_s(x_{sk},x_{sj})^2\right)^{1/2} \leq \varepsilon,
   \]
   where the indices switch between $j,j',k$ in a confusing way. These are small notation issues individually, but they accumulate in a paper whose main contribution is a derivation.

9. **The simulation evidence is helpful but not sufficiently stress-tested.**  
   The simulation appears designed to be congenial to the method: applicants submit near-identical applications, extra applications weakly increase the chance of one origination, and the relevant covariates are exactly the ones used for clustering. This is acceptable for illustration, but it does not probe failure modes. For instance, what happens if originations are correlated across borrowers, if shopping intensity is negatively associated with success, if non-identical legitimate repeat applications exist, or if partitions include more near-collisions? **Figure 3** and **Figure 4** show encouraging behavior in one stylized setting, but one friendly simulation is not enough to establish robustness.

10. **The claimed recall contribution is weaker than the framing suggests.**  
    Corollary 1 gives
    \[
    \text{Recall}(\theta) \geq \hat\alpha(\theta)\frac{N^+(\theta)}{P_{\text{tot}}},
    \]
    but $P_{\text{tot}}$ is unknown, so the paper can only rank specifications by a quantity proportional to the lower bound, not compute recall itself in the real application. This is acknowledged, but the abstract and introduction at times make the contribution sound stronger than it is. What is actually observable is a relative ordering criterion, not an absolute recall lower bound in the application. The distinction is important and should be stated more plainly.

11. **The paper repeatedly leans on appendix-only evidence for claims that matter in the main narrative.**  
    For example, the simulation recall value of 92% at the preferred specification is justified via "also see Table 2 in the Appendix" on Page 7, and the application validation is deferred to Appendix C. Since the main paper is where acceptability should be judged, the strongest empirical support for the chosen model should not be mostly offloaded to the appendix.

## Questions
1. Please correct Equations (1) and (2) on Page 5. Are these intended to be bounds on $\Pr[\neg \text{False}]$ / precision after dropping multi-origination clusters, rather than bounds on $\Pr[\text{False}]$? A clean derivation in the rebuttal would materially increase my confidence, because this quantity is central to all model selection and to **Figures 4 and 5**.

2. How sensitive is the precision lower bound to violations of Assumption 1? In particular, can the authors provide either a theoretical sensitivity result or an empirical diagnostic showing whether origination outcomes of distinct borrowers are approximately independent within the very fine partitions used in the HMDA application?

3. Can the authors justify Assumption 2 more concretely in the mortgage context, or show an alternative bound that does not require monotonicity of $\Pr(\sum_m O_{im}=1 \mid n_i=k)$ in $k$? Even a weaker theorem with weaker guarantees might be preferable if the assumptions are more credible.

4. The paper claims method-agnosticism, but only one clustering family is tested. Can the authors provide evidence that the proposed criterion is useful beyond complete-linkage HAC, for example by using it to choose among at least one substantively different linkage model?

5. Please clarify the unit of evaluation throughout Section 2. Are $TP,FP,N^+$ defined over clusters, applicants, or applications? The text seems to switch units. A precise definition would make Corollaries 1 and 2 much easier to assess.

6. Can the authors discuss prior work on unlabeled record-linkage / entity-resolution evaluation more explicitly and contrast their structural-constraint approach with those methods? A careful positioning statement could change my assessment of originality.

7. **Figure 5** would be much more informative if the frontier points were annotated by distance family and $\varepsilon$. Can the authors provide that mapping, or a compact table of the non-dominated frontier points? That would help judge whether the selected operating point is stable and interpretable.

8. For **Table 1**, where do the hand-coded constants and thresholds come from, especially the "Penalize Exact" and "Reward Exact" definitions? Were these chosen before looking at the precision frontier, or iteratively refined? A clearer explanation is important to rule out hidden tuning.

## Flag For Ethics Review
- Yes, Privacy, security and safety  
- Yes, Discrimination / bias / fairness concerns

## Details Of Ethics Concerns
The paper uses confidential HMDA data to infer repeated mortgage applicants in a sensitive lending domain, see Section 4.1. Even though the paper does not release identities, the goal is still to reconstruct latent person-level linkage from anonymized records, which raises privacy concerns in principle. The downstream applications discussed on Page 9 also explicitly involve discrimination and fairness analysis in mortgage lending. I do not view these as reasons to reject the paper, but they are relevant enough that an ethics review would be appropriate, especially around privacy safeguards, possible re-identification risks, and responsible use of inferred linkages in lending analysis.

## Soundness Rating
2: fair. The core idea is interesting and some arguments are plausible, but the central post-filtering precision equations contain a serious sign/event inconsistency, key assumptions are strong and insufficiently justified for the application, and the empirical support is narrower than the paper's claims.

## Presentation Rating
2: fair. The paper is readable overall and some figures are helpful, but notation is inconsistent in several important places, the derivation around Equations (1)-(3) needs cleanup, and the related-work positioning is underdeveloped.

## Contribution Rating
2: fair. The problem is important and the structural-constraint perspective is potentially useful, but incomplete positioning against prior unlabeled record-linkage evaluation work, together with limited comparative experiments, keeps the contribution below the bar I would expect for ICLR.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The paper addresses a worthwhile problem and has a promising core idea, but the current version has too many unresolved issues in the main technical formulation, assumptions, and empirical positioning for me to support acceptance confidently.

## Reviewer Confidence
4: confident. I am confident in my assessment, though not absolutely certain. I carefully checked the main equations and the overall logic, but some appendix details and domain-specific assumptions could still benefit from author clarification.