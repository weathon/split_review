---
job_id: 0f7f73b9-3475-4eb4-a17e-973258d6ce06
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: NIvqiJ8R4J.pdf
paper: 5 PELICAN: Personalized Education via LLM-Powered Cognitive Diagnosis and Adaptive Tutoring
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope as an ML/NLP-for-education system paper centered on LLM-based adaptive tutoring, learner-state modeling, and dialogue planning.

## Minimum Quality
Pass ✅. The paper includes the expected core sections, presents a complete method and experiments, and is understandable enough for full review, although there are substantial concerns about rigor, novelty positioning, and evaluation validity that affect the score rather than triggering desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, review-targeting instructions, or other manipulative content in the provided paper text and figures.

# Expected Review Outcome:
## Summary
This paper proposes PELICAN, a two-stage LLM-based tutoring framework for personalized education. The first stage performs collaborative cognitive diagnosis over a manually constructed hierarchical knowledge tree using a successor-first questioning strategy and an expert-assistant-verifier pipeline; the second stage uses the estimated student state to drive adaptive tutoring, including a fast/slow strategy selector that simulates future dialogue paths before choosing a teaching strategy. Experiments on a Gaokao dataset, plus a human study with high school students, are used to evaluate diagnosis quality and tutoring effectiveness.

## Strengths
The paper tackles a meaningful problem. Many LLM tutoring papers stay at the level of "better prompting," whereas this work tries to explicitly model learner state and use that state to control tutoring behavior. That framing is valuable and relevant to the ICLR community, especially given increasing interest in interactive, personalized ML systems.

The two-stage decomposition is intuitive and easy to follow. Separating diagnosis from tutoring is a reasonable design choice, and **Figure 3** is genuinely helpful here: it makes the full pipeline, from question generation and diagnosis to response categorization, state update, strategy selection, and final response generation, much easier to understand than the prose alone. The left/right split in the figure also clarifies which components belong to assessment versus intervention.

The work includes multiple empirical views rather than a single headline number. In particular, **Table 1** evaluates the diagnosis stage separately from the tutoring stage, and **Table 2** reports both "hard" coverage/frequency metrics and GPT-based tutoring quality metrics. That decomposition is useful because it at least attempts to validate that the diagnosis module is not just decorative.

The ablation in **Table 3** is directionally useful. Even though I have concerns about the evaluation protocol, the results do suggest that both the diagnosis module and slow-thinking module contribute to the final behavior. Likewise, **Figure 4** is a good qualitative sanity check showing strategy usage shifts across different assumed cognitive levels, which is aligned with the paper's personalization claim.

The paper also makes an effort toward real-user validation. The human experiment with 169 students is a positive aspect, and **Table 6** provides some evidence that the gains are not confined to fully simulated settings.

The paper is fairly readable overall. There are grammatical issues and some sloppiness, but the high-level story is understandable.

## Weaknesses
I have several substantial concerns, and together they prevent me from viewing the paper as meeting the bar for ICLR main track in its current form.

1. **The central evaluation is heavily entangled with LLM simulation, which makes the core claims much less convincing than the paper suggests.**  
   A large fraction of the evidence comes from tutoring a simulated student played by GPT-4o, with state initialization and response generation described in Appendix G. In the main paper, the student model is treated almost like a faithful stand-in for a real learner, but that assumption is doing far too much work. The student simulator is explicitly conditioned on the target cognitive state and response type, and even receives a designed state updater. This creates a closed loop where the tutor and the simulated student share the same ontology, the same decomposition structure, and likely similar language priors. That setup can strongly favor a method like PELICAN, whose design also explicitly operates over the same knowledge tree and response categories.  
   This matters because the paper's main claim is about *personalized education*, not merely about generating dialogues that look pedagogically plausible under a friendly simulator. The human study helps somewhat, but it is too limited and too coarsely analyzed to fully compensate for the simulation-heavy evidence.

2. **The human evaluation is not strong enough to validate the broad claims made in the abstract and conclusion.**  
   The paper reports a real-world experiment with 169 high school students and 1335 reports (**Page 9, Table 6**), which sounds substantial at first glance. But the actual design leaves important questions unanswered. The unit of randomization appears to be at the question level, with one of six methods assigned to each tutoring episode (Appendix I.2). This means each student may contribute multiple reports under multiple conditions, but the analysis reported in the main paper does not account for within-student correlation, teacher/question difficulty effects, or subject-level heterogeneity. A plain one-way ANOVA on reports, as shown in Appendix Table 8/15, is not the right level of analysis for repeated-measures data.  
   This matters because the claimed margins in **Table 6** are modest for some metrics. For example, the success rate of PELICAN is 86.8% versus 86.5% for Stepwise, essentially tied, while the subjective gains could be partly driven by presentation style rather than genuine adaptivity. Without a mixed-effects analysis, per-student paired comparison, or at least confidence intervals in the main tables, the human evidence is weaker than the paper implies.

3. **The methodology is underspecified in several mathematically important places, especially around the knowledge-state update and slow-thinking search.**  
   The paper presents a number of equations, but the formalization is much less precise than it needs to be. For example, in Section 3.3.2, the paper says the knowledge state is updated based on the previous state and response type, but no explicit update rule is given. Formally, one would expect something like
   \[
   \hat K_u^{(t)} = U\!\left(\hat K_u^{(t-1)}, \mathrm{type}^{(t)}, h^{(t)}, sp_i\right),
   \]
   with at least a clear specification of when a node flips from 0 to 1 or from 1 to 0, and how ancestor/descendant constraints are enforced. Instead, the update mechanism is left as a verbal description, which is a problem because state tracking is one of the paper's central claims.  
   The slow-thinking algorithm is also only loosely defined. In **Equation (5)**, the leaf-node score is
   \[
   \text{score} = 1 - \lambda(d-1),
   \]
   which depends only on depth \(d\), not on any estimated probability of success, quality of explanation, consistency with student state, or uncertainty. Then the final strategy score is the sum over leaves associated with an initial action. This means the search objective is basically a hand-crafted preference for shallow successful simulated trajectories, but it is never justified as an estimator of actual tutoring utility. It is not even obvious that this is a sensible planning criterion under the stochastic dialogue simulator in **Equation (4)**.  
   There is also notation drift: \(\varphi = 0.4\) is given in implementation details on **Page 7**, but **Equation (5)** uses \(\lambda\). That is minor by itself, yet symptomatic of the lack of formal precision.

4. **What is called "slow thinking" is not well differentiated from a small prompt-based lookahead heuristic, and the paper overstates the algorithmic contribution.**  
   The prose around Section 3.3 suggests a deliberate planning procedure inspired by dual-system theory, but the actual algorithm in **Algorithm 1** is quite limited: after one round threshold \(M=1\), it expands top-\(m\) strategies, simulates teacher and student responses, and scores branches by shallow depth. With \(k=2\) and \(m=2\), this is a very small search. There is no principled rollout policy, no value function, no uncertainty treatment, no learned search prior, and no comparison to simpler alternatives such as reranking candidate strategies with a single reflection prompt or self-consistency.  
   This matters because the method contribution is supposed to be more than "we ask an LLM to think a bit harder." Right now, the difference between fast and slow modes is not algorithmically sharp enough, and the ablation evidence is not strong enough to establish that this particular tree-search formulation is the right design rather than one heuristic among many.

5. **The empirical setup is narrow, and the generalization claims are overstated relative to the evidence in the main paper.**  
   The main text experiments use a Gaokao dataset with only 184 questions across four subjects (**Page 6**). That is a very small benchmark for making broad claims about personalized tutoring. The conclusion says the system addresses "diverse, dynamic needs of students across various subjects and cognitive states," but the main evidence is still a small, curated question set with manually designed knowledge trees and a largely simulated student loop.  
   The paper gestures toward broader applicability, but in the main paper there is no cross-dataset validation, no long-horizon multi-session tutoring, no robustness study under noisy state estimates, and no evaluation on genuinely open-ended student responses at scale. For a system paper making strong claims about adaptive tutoring, this external validity gap is important.

6. **The knowledge tree construction relies on substantial manual effort and domain structure, which raises scalability concerns that are not confronted seriously enough.**  
   The method assumes that for each problem, relevant knowledge points can be extracted and organized into a hierarchical prerequisite structure. In the main paper this is presented as a clean setup, but Appendix B makes clear that comprehensive trees were manually built from syllabi and then reviewed by experts. Even if the manual error rate is low, this is a major hidden dependency.  
   This matters because the viability of the whole diagnosis stage depends on having the correct ontology and prerequisite graph. The paper is strongest in a setting where the curriculum is relatively structured and exam-oriented. It is much less clear how the method would work in messier domains, interdisciplinary questions, or settings where knowledge dependencies are not tree-structured. The tree assumption is not just an implementation detail, it is a core modeling assumption.

7. **The baselines are not strong enough to support the level of comparative claims made in the paper.**  
   In the tutoring stage, the baselines in **Table 2** are mostly prompt variants or adapted heuristic methods. There is no comparison to a stronger planning-style LLM baseline with access to the same decomposed steps and state representation but without the proposed search heuristic. For example, a fairer baseline would be: decompose into sub-steps, infer student type, then ask the model to deliberate over all candidate strategies in one shot and choose one, without the tree. Another important baseline would be diagnosis + tutoring without the manually defined strategy pool, to test whether explicit strategy labels themselves provide the gain.  
   In the diagnosis stage, **Table 1** reports very strong numbers for both No-Pipeline and PELICAN, with F1 93.08 versus 94.31. That is only a 1.23 point gain, and Avg_Round is essentially identical, 5.84 versus 5.83. The paper claims the pipeline is important, but on the main table the practical gain is quite small. The stronger evidence for the pipeline's utility is pushed to Appendix Table 10, but that was not integrated convincingly into the main discussion.

8. **Several reported results are internally awkward or insufficiently explained, which reduces confidence in the evaluation.**  
   The paper's tables deserve more scrutiny than they get. In **Table 2**, PELICAN is said to "significantly outperform" other methods, but significance markers are absent in the main paper, and the standard deviations shown for some GPT-based metrics are implausibly tiny, such as Suitability \(4.27 \pm 0.003\) and Overall \(4.33 \pm 0.003\). Given that these are subjective or LLM-judged quantities, such tiny variation suggests either averaging over a very large number of homogeneous ratings or a reporting issue; in either case, the paper should explain exactly what the variance is computed over.  
   **Table 3** is also strange. Removing diagnosis increases Inspiration from 4.30 to 4.48, and removing both diagnosis and slow-thinking still yields Overall 4.11, very close to the full model's 4.28. That does not match the narrative that these modules are central to the system. If the main benefit is concentrated in \(R_{\mathrm{coverage}}\) and \(F_{\mathrm{frequency}}\), then the paper should say so more clearly rather than implying broad superiority across the board.  
   There is also inconsistency between **Table 2** and **Table 3** for the full PELICAN row. In Table 2, PELICAN has \(R_{\mathrm{coverage}}=72.36\) and \(F_{\mathrm{frequency}}=72.06\), but in Table 3 the full model is listed as 54.84 and 61.47. If these are different experimental settings, that needs to be made explicit. As written, this reads like a major reporting inconsistency.

9. **The figure-based evidence is mostly illustrative rather than diagnostic, and in one case it exposes a limitation.**  
   **Figure 1** and **Figure 2** are stylized motivational cartoons, not evidence, which is fine, but the paper leans on them rhetorically as if they establish the weakness of standard LLM tutoring and the strength of the proposed method. More importantly, **Figure 5**, the case study, is too cherry-picked and too compressed to be persuasive. It shows that PELICAN can produce a more scaffolded interaction than some baselines on one example, but it does not reveal failure cases, misdiagnosis, or situations where the slow-thinking strategy actually changed the chosen action. A stronger case study would show the same initial state with and without slow-thinking, or diagnosis errors propagating into poor tutoring.  
   Also, **Figure 4** is directionally plausible, but without error bars or normalization details it is hard to know whether the observed strategy differences across cognitive levels are substantial or just artifacts of the prompting pipeline.

10. **The paper's positioning versus related work is incomplete, especially around LLM-based cognitive diagnosis and adaptive tutoring benchmarks.**  
   The related work section is quite thin for a paper trying to claim a specific advance in LLM-personalized tutoring. It cites Socratic tutoring and some cognitive diagnosis work, but the positioning remains broad and generic. The paper does not do enough to distinguish its contribution from contemporaneous efforts that combine learner-state estimation, adaptive feedback, and LLM-driven tutoring in closed-loop systems, nor does it engage with benchmark-style work studying whether LLM tutors genuinely exhibit adaptivity rather than merely fluent feedback.  
   This matters because the paper's claimed novelty depends on that distinction. Right now, the contribution feels like a plausible assembly of known ingredients, but the paper does not do enough comparative work to prove that its assembly is materially new or especially insightful.

11. **There are clarity and consistency issues throughout the paper.**  
   A few examples: the dialogue history in Section 3.1 is written as \(D_t=\{q^1,r^t,\ldots,q^t,r^t\}\), which appears to be a typo since the second element should presumably be \(r^1\); the abstract says "successor-first" without defining it until later; some variable names change across sections; and there are multiple grammatical errors and malformed references, including odd entries like "GUIDING" and "Planning" in the references. None of these alone is fatal, but collectively they make the paper feel less mature than it should be.

## Questions
1. The main paper reports strong gains in both simulated and human evaluations, but the simulated setup seems highly structured around your own knowledge ontology and student-state assumptions. Can the authors provide a cleaner separation between what is learned by the tutor and what is effectively built into the simulator? In particular, what happens if the student simulator is *not* given the same knowledge-tree decomposition or if student response categories are generated more freely?

2. Please clarify the discrepancy between **Table 2** and **Table 3** for the full PELICAN model. In Table 2, \(R_{\mathrm{coverage}}\) and \(F_{\mathrm{frequency}}\) are 72.36 and 72.06, while in Table 3 the full-model row is 54.84 and 61.47. Are these different datasets, different subsets, or different evaluation settings? This needs to be resolved clearly because it affects confidence in the reported results.

3. Can the authors provide an explicit formal update rule for the knowledge state, rather than only a verbal description? For example, what exact conditions cause a node \(v\) to flip from 0 to 1 or 1 to 0, and how are ancestor/descendant consistency constraints enforced after each update?

4. The planning objective in **Equation (5)** seems to depend only on branch depth. Why is
   \[
   \text{score} = 1 - \lambda(d-1)
   \]
   an appropriate surrogate for tutoring utility? Why not incorporate an estimated success probability, uncertainty, or quality score from the simulated student response? A rebuttal that explains the design rationale, and ideally compares this scoring rule against simpler alternatives, would increase my confidence.

5. Please provide more detail on the statistical analysis of the human study. Since each student can contribute multiple reports across conditions, did the authors run any repeated-measures or mixed-effects analysis? If not, can they provide one? This is important because otherwise the ANOVA may overstate effective sample size.

6. The evidence for the expert-assistant-verifier pipeline in **Table 1** is modest in the main paper, with only a small gap between No-Pipeline and PELICAN. Can the authors quantify how often diagnosis errors in No-Pipeline actually change downstream tutoring quality, rather than only reporting stage-1 diagnostic accuracy?

7. The method depends on manually constructed curriculum trees reviewed by experts. How much manual effort is required per new domain or curriculum, and what happens if the tree is imperfect or the knowledge dependencies are not strictly hierarchical? Some sensitivity analysis here would materially improve the paper.

8. A stronger set of baselines would help. Can the authors compare against a baseline that uses the same sub-task decomposition and state representation, but chooses the tutoring strategy via a single deliberate LLM selection step instead of the simulated teaching tree? That would isolate whether the gain comes from the search procedure specifically.

## Flag For Ethics Review
- Yes, Responsible research practice (e.g., human subjects, data release)

## Details Of Ethics Concerns
The paper reports a real-world experiment with 169 high school students, who are minors (**Page 9** and **Page 10**). The ethics statement says parental consent, student assent, anonymization, and institutional review procedures were used, which is good. My flag is therefore not based on evidence of misconduct, but on the fact that human-subjects research with minors deserves explicit ethics attention. I do not see a disqualifying issue from the paper text alone, but this part should receive standard ethics scrutiny.

## Soundness Rating
2: fair. The paper has a coherent system and nontrivial experiments, but the central claims are weakened by underspecified state updates, heuristic planning without strong justification, heavy reliance on simulator-based evaluation, and unclear statistical treatment in the human study.

## Presentation Rating
2: fair. The high-level organization is understandable and some figures, especially **Figure 3**, help, but the paper has multiple notation inconsistencies, insufficiently precise equations, thin related-work positioning, and at least one serious table inconsistency that should not have survived revision.

## Contribution Rating
2: fair. The problem is important and the two-stage framing is useful, but the actual contribution feels closer to a plausible engineering combination of known ingredients than to a clearly established advance, and the empirical evidence does not fully support the breadth of the claimed impact.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The paper is promising and addresses an important application area, but too many core issues remain unresolved, especially around evaluation validity, formal specification of the learner-state machinery, reporting consistency, and the gap between the claimed personalization advance and the evidence actually provided.

## Reviewer Confidence
4: confident. I am confident in this assessment, though not absolutely certain. I carefully checked the main method, equations, figures, and tables, and my main concerns are about rigor and evidence rather than a failure to understand the overall proposal.