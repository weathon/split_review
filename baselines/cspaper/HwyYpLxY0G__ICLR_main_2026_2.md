---
job_id: db3156aa-a1d2-4c06-9b2a-2d3376f50603
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: HwyYpLxY0G.pdf
paper: Aligned Textual Scoring Rules
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope through learning theory, optimization, LLM-based evaluation, and ML applications to language and education, with a mechanism-design flavored but still ML-relevant contribution.

## Minimum Quality
Pass ✅. The paper contains the core components expected of a research submission, including abstract, introduction, related work, method, implementation details, experiments, and quantitative results; while some sections are thin and the empirical scope is limited, this does not rise to a desk-reject level.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, suspicious reviewer-targeting instructions, or other manipulative content in the paper text or figures.

# Expected Review Outcome:
## Summary
This paper studies how to align provably proper textual scoring rules with exogenous preference signals, such as instructor scores or LLM-judge scores, in the ElicitationGPT framework of Wu and Hartline (2024). The main proposal, Aligned Scoring Rule (ASR), optimizes over the class of separate proper scoring rules to minimize squared error to a reference score while preserving properness under the reduction from text to rubric-point reports. Empirically, the method is evaluated on peer-grading datasets and compared against constant-score and non-aligned ElicitationGPT baselines.

## Strengths
The paper tackles a meaningful problem. The tension between incentive compatibility and preference alignment is real, especially for textual evaluation, and the paper addresses it in a direct way rather than pretending that “LLM-as-judge” scores are automatically truthful. That framing is valuable.

The core optimization problem is simple and reasonably interpretable. Restricting to separate scoring rules over know-it-or-not reports makes the parameterization tractable, and the resulting objective in **Equation (2)** is easy to understand. In particular, the per-dimension parameterization with only six variables per dimension does make the search space transparent.

The paper does a decent job connecting the proposal to prior elicitation work, especially the reduction framework of Wu and Hartline (2024) and the optimization perspective from Li et al. (2022). I appreciated that the paper is not claiming to invent textual elicitation from scratch, but instead to optimize within a proper subclass.

There is some interpretability benefit in the proposed decomposition. The visualization in **Figure 7** is one of the more persuasive parts of the submission, because it shows that different rubric dimensions receive visibly different learned curvature / informativeness patterns. Even though this analysis is only qualitative, it helps make the method less of a black box than direct LLM grading.

The empirical gains against the specific baselines considered are large. In **Table 1**, ASR improves substantially over EGPT(AV) and EGPT(MV) on both references. For example, with instructor score as reference, the reported squared loss drops from 9.541 for EGPT(AV) to 1.730 for ASR, and Pearson correlation rises from 0.294 to 0.717. On the paper’s own target, namely “fit a proper score to a noisy preference-based score,” these are nontrivial improvements.

The presentation of the basic scoring-rule geometry is reasonably intuitive. **Figure 1** and **Figure 2** help explain how properness is enforced in the ternary know-it-or-not setting, and they are more useful than the surrounding prose alone.

## Weaknesses
1. **The main contribution is quite incremental relative to the base framework, and the paper does not do enough to show that the increment is scientifically substantial.**  
   The central move is: take the ElicitationGPT reduction, restrict to separate proper scoring rules, and fit them to a reference signal by minimizing MSE under properness constraints. That is a sensible extension, but from the main paper it looks much closer to “optimization over an existing proper family” than to a new elicitation framework. This matters because the empirical and theoretical evidence would need to be especially convincing to justify the contribution at ICLR main-track level, and I do not think the paper clears that bar. The paper itself positions the method as following the computation framework of Li et al. (2022) and the reduction of Wu and Hartline (2024), which further reinforces that the novelty is mainly in the objective choice and application.

2. **The properness guarantee is largely inherited, but the paper’s own optimization objective is not analyzed in a way that clarifies what is actually being optimized statistically or behaviorally.**  
   In **Section 3.2**, the objective is to minimize  
   \[
   \mathbb{E}_{(\mathbf r,\boldsymbol\theta,s)}\left[\left(S(\mathbf r,\boldsymbol\theta)-s\right)^2\right]
   \]
   subject to properness. However, the paper never really discusses what happens when the reference score \(s\) is noisy, biased, miscalibrated, or inconsistent across assignments. Since the entire point of ASR is to approximate a potentially non-proper and noisy score with a proper one, the statistical target matters a lot. Right now, the method is essentially “project the reference onto a constrained scoring-rule class,” but the paper never formalizes this projection view, nor does it discuss identifiability, sample complexity, or overfitting risk. This is not a small omission, because the optimization could simply memorize quirks of a small dataset while still being proper by construction.

3. **The claim of convex optimization is presented too casually, and the optimization details are underspecified.**  
   The paper states in **Corollary 3.4** that Optimization Problem 2 is convex, and then says “Since optimization problem 2 is convex, we optimize with the gradient descent algorithm over samples” (**Page 7**). A few issues here:
   - The population objective in **Equation (2)** is convex in the score variables because it is a squared affine function, yes, but the paper never explains how the boundedness constraint  
     \[
     \sum_{i\in[m]} S_i(r_i,\theta_i)\in[0,1],\quad \forall \mathbf r,\boldsymbol\theta
     \]
     is enforced in practice. This is a finite but potentially large family of linear constraints over all \((\mathbf r,\boldsymbol\theta)\), and the implementation is not described in the main paper.
   - If the method is optimized “over samples,” then the paper should clarify whether it solves the exact empirical convex program, uses projected gradient descent, penalized constraints, or some other constrained optimizer. Gradient descent on a constrained convex problem is not a complete algorithmic description.
   - More importantly, the optimization variables are the table entries \(S_i(r_i,\theta_i)\), but the paper never specifies the training/validation protocol for selecting stopping or regularization, which matters given the small dataset.  
   The convexity statement itself is plausible, but the optimization methodology is too thinly specified for a paper whose main contribution is an optimization procedure.

4. **There is a notation and formulation sloppiness issue in the mathematical exposition.**  
   Several places are loose enough to make the formal setup harder to trust than it should be:
   - In **Definition 2.3** on **Page 4**, the notation alternates between \(S_{\mathbf p}\), \(S_p\), and \(S\), and the domain/codomain notation is inconsistent with the surrounding text.
   - In **Definition 2.6** and **Definition 2.7** on **Page 5**, the dimensional indexing alternates between \(m\) and \(n\): the text says \(S:[0,1]^m\times[0,1]^m\to[0,1]\), but then writes \(S(r_1,\ldots,r_n;\cdot)\). This is minor-looking, but in a paper centered on multi-dimensional elicitation, indexing consistency matters.
   - In **Definition 2.8**, the max-over-separate rule is defined using  
     \[
     i=\arg\max_{i'} \mathbb E_{\theta_{i'}}[S_{i'}(r_{i'},\theta_{i'})].
     \]
     The expectation is not fully specified with respect to which distribution, presumably the agent’s belief or prior/posterior mean on that coordinate. That ambiguity is important because “favorite dimension” is central to how the mechanism behaves strategically.
   - In **Definition 3.1**, “\(\Pr[\hat r_i\neq r_i\mid R]\leq 1/2\)” is called non-inverting, but if \(\hat r_i\in\{0,1,\bot\}\), then “\(\neq\)” conflates inversion with any error. If the report is ternary, an NA prediction is not the same as flipping 0 to 1.  
   None of these alone is fatal, but together they create the impression that the formalism was not polished carefully enough.

5. **The empirical evaluation is too narrow to support the broader claims.**  
   The experiments use peer grading data from two undergraduate algorithms classes, covering 22 assignments, each with only 6 to 8 submissions and 6 to 8 peer reviews per submission (**Page 8**). This is a very specific, small, and structured environment. The paper repeatedly talks about aligned textual scoring rules more generally, but the empirical support is almost entirely “this works on one peer-grading setup where rubrics cluster nicely.” That gap matters because the method critically depends on summarization into stable rubric points and on the know-it-or-not assumption. It is not obvious that the same behavior would hold in less templated text evaluation settings.

6. **The baseline set is too weak for the claims being made.**  
   In **Table 1**, ASR is compared against a constant predictor and two non-aligned ElicitationGPT variants, EGPT(AV) and EGPT(MV). These are relevant baselines, but they are not enough. The paper’s framing is alignment with instructor or LLM-judge scores, so one would expect comparison to straightforward predictive baselines that ignore properness, such as linear regression or a simple supervised predictor from rubric-point features. Without such baselines, it is hard to tell whether ASR is good because the properness-constrained design is effective, or simply because almost any fitted model over extracted rubric features would beat the non-aligned V-shaped rules by a mile.  
   This point is especially important because **Figure 4** shows that ASR is nearly linearly related to the reference score. That is consistent with success, but it also raises the question of whether the problem is mostly just supervised score fitting on structured features. The paper does not answer that.

7. **The evaluation protocol is not sufficiently detailed to rule out leakage or overly optimistic fitting.**  
   The paper reports MSE and correlations in **Table 1**, but the main text does not clearly explain whether the summarization oracle, prior estimation, and ASR optimization are fit strictly on training data for each assignment or whether some components are reused across evaluation. Since summary points are derived from instructor reviews for each cluster and the prior \(p_i\) is computed from observed instructor reviews in the cluster (**Algorithm on Page 6**), the exact train/test split is crucial. If the summary points and priors for a test item are derived using all instructor reviews including the held-out target, that is not an apples-to-apples evaluation of generalization. I am not saying leakage definitely occurred, but the main paper leaves this too implicit.

8. **The strongest qualitative figures are not yet leveraged rigorously.**  
   **Figure 7** is interesting, but it is relegated to the appendix and only used for anecdotal interpretation. If interpretability is a real claim of the paper, then there should be some systematic analysis: do dimensions identified as “important” correlate with instructor-designated rubric importance, or with predictive power, across assignments? Right now the figure is visually suggestive, not evidential. Similarly, **Figure 3** shows only moderate agreement between instructor score and LLM-judge score, with Pearson correlation 0.5540. That is not terrible, but it is far from enough to support strong claims that the LLM-judge score can act as a robust substitute. The paper’s wording on **Page 8** feels more confident than the figure warrants.

9. **The paper overstates what the regression plots show.**  
   In **Figure 4**, the authors say the regression line predicting the reference score from ASR is “nearly the identity function.” Visually, the line may be close, but this is a weak diagnostic by itself. A flexible model can have a reasonable regression line even with substantial dispersion, and the violin-like distributions in the figure still show noticeable spread. The stronger evidence is actually **Table 1**, but even there the MSE values are hard to interpret without knowing the exact scale normalization and variance of the target within each split. This is a good example where the paper reaches for a punchy qualitative claim instead of tighter quantitative interpretation.

10. **The central assumption is strong and insufficiently justified beyond this dataset.**  
    **Assumption 2.2** on **Page 4** says the agent’s posterior on each summary point is either \(0\), \(1\), or the prior \(p_i\). This know-it-or-not assumption is doing a lot of work, because it reduces the report space to \(\{0,1,\bot\}\) and makes the optimization feasible and interpretable. But the justification is mostly “in our peer grading dataset, we observe that textual reports either express a state being 0 or 1, or have no information.” That is a dataset-specific observation, not a robust modeling principle. It severely limits the generality of the contribution and should be treated as such. I wanted to see either a quantitative validation of this assumption or at least an ablation showing what breaks when more graded uncertainty is allowed.

11. **The implementation of the language oracles is elaborate but not convincingly validated.**  
    **Section 4** and **Appendix A** provide many prompt details, which is appreciated, but the paper assumes the oracles are good enough without giving task-level QA accuracy, clustering stability, or inter-model sensitivity in the main text. Since the whole reduction depends on summarization and QA turning text into rubric states, oracle misspecification is not peripheral, it is central. The paper cites inherited robustness guarantees, but the empirical pipeline could still be brittle in practice. The lack of oracle-quality diagnostics makes it hard to know whether the reported improvements are robust or just one prompt stack working on one educational domain.

12. **The paper’s claims about LLM-judge scalability and robustness should be toned down.**  
    On **Page 8**, the paper argues that LLM-judge score can serve as a substitute for costly and noisy instructor score, “improving the scalability and the robustness of the peer grading system.” But **Figure 3** only shows moderate correlation, not strong agreement, and the appendix notes model dependence for GPT vs Gemini. The claim should be narrowed to “potentially useful proxy in this dataset,” not generalized as if reliability were established.

## Questions
1. Please clarify the exact train/validation/test protocol in the main paper. For each reported number in **Table 1**, were the summary points, priors \(p_i\), and ASR parameters learned strictly without access to the instructor review or score of the test example? A very explicit pipeline description would increase my confidence substantially.

2. How exactly is the constrained optimization in **Equation (2)** solved in practice? Is this an exact convex program, projected gradient descent, or gradient descent with penalties? How are the boundedness constraints enforced, and over which set of \((\mathbf r,\boldsymbol\theta)\) combinations?

3. Can the authors provide a stronger justification for **Assumption 2.2**? Ideally, quantify how often peer reviews exhibit genuine uncertainty that is not well represented by \(\{0,1,\bot\}\). If such cases exist, how sensitive is ASR to this misspecification?

4. The current baselines are all truthful mechanisms or trivial constants. Could the authors compare against simple non-proper supervised baselines over the same extracted rubric features, such as linear regression or a small tree / MLP, purely as predictive references? This would help isolate the cost of properness and the value of the constrained design.

5. For **Figure 7**, can the authors give a quantitative interpretability analysis rather than a single case study? For example, do the learned “important” dimensions align with independent instructor judgments of rubric importance across assignments?

6. How sensitive are the results to the language oracle implementation? Since the pipeline uses summarization, polarity reversal, clustering, and QA, even a small ablation, such as alternative clustering prompts or a different QA model, would help separate methodological gains from prompt engineering artifacts.

7. For **Definition 2.8**, what is the precise expectation used in the \(\arg\max\) selection for max-over-separate, and under what belief is the favorite dimension chosen? Please make this explicit.

8. Theorem-wise, the paper inherits properness guarantees from Wu and Hartline (2024), but what additional theorem is actually new here beyond convexity of the optimization program? If there is a stronger characterization of the optimal separate aligned rule, that would materially strengthen the contribution.

## Flag For Ethics Review
- Yes, Privacy, security and safety  
- Yes, Responsible research practice (e.g., human subjects, data release)

## Details Of Ethics Concerns
The paper uses peer grading data from undergraduate courses, including instructor reviews and student peer reviews (**Section 5.1**). The main text does not clearly discuss anonymization, consent, institutional approval, or data governance for using student educational records in LLM-based processing. I am not alleging misconduct, but because the work involves student-generated text and instructor evaluations, a brief clarification on privacy handling, de-identification, and responsible use would be appropriate.

There is also a mild deployment-risk issue: the paper motivates truthful and aligned scoring for peer grading, but LLM-mediated scoring of student feedback can affect educational outcomes. Since **Section 5.2** discusses replacing or substituting instructor score with LLM-judge score, the paper should more explicitly note the risk of model bias or inconsistency when deployed in real classrooms.

## Soundness Rating
2: fair. The central construction is plausible and the empirical results support some of the paper’s narrower claims, but the methodology and evaluation protocol leave important unanswered questions, especially around optimization details, split protocol, oracle dependence, and scope of generalization.

## Presentation Rating
2: fair. The paper is readable overall, and some figures are helpful, but the mathematical notation is inconsistent in several places, important implementation details are deferred or underspecified, and some claims are stated more strongly than the evidence justifies.

## Contribution Rating
2: fair. The problem is interesting and the optimization of proper scoring rules toward reference alignment is useful, but the advance over prior textual elicitation work appears incremental, and the empirical evidence is too narrow to establish a broad contribution for ICLR.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The paper is promising and addresses a worthwhile problem, but in its current form I do not think it provides enough methodological depth, empirical breadth, or rigor in evaluation to justify acceptance at ICLR. The biggest issue is not that the idea is bad, it is that the paper does not yet convincingly separate “proper supervised fitting on one narrow benchmark” from a broadly useful advance in aligned textual elicitation.

## Reviewer Confidence
4: confident. I am confident in the assessment and familiar with the elicitation / scoring-rule and ML evaluation themes, although a few implementation details are too underspecified in the main paper to verify every aspect completely.