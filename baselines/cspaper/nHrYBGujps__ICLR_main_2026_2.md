---
job_id: e2c3b8fc-d668-432c-b8f5-b71f5a442c90
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: nHrYBGujps.pdf
paper: BIRD-INTERACT: Re-Imagining Text-to-SQL Evaluation via Lens of Dynamic Interactions
main_score_norm: 0.8
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope as a machine learning benchmark and evaluation framework for interactive, agentic text-to-SQL systems, with relevance to language models, agents, benchmarking, and human-AI interaction.

## Minimum Quality
Pass ✅. The paper contains the expected components for a benchmark paper, including abstract, introduction, benchmark construction and methodology, evaluation settings, experiments, quantitative results, related work, and conclusion. While I have several substantive concerns about external validity, metric design, and some underspecified choices, these are not fatal flaws that warrant desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not detect hidden prompts, suspicious reviewer-directed instructions, or other manipulative content in the provided paper text and figures.

# Expected Review Outcome:
## Summary
This paper introduces BIRD-INTERACT, a benchmark for interactive text-to-SQL evaluation that moves beyond static single-turn or fixed-transcript settings by combining executable databases, metadata, hierarchical knowledge bases, and a function-driven user simulator. The benchmark supports two evaluation modes, a protocol-guided conversational setting ($c$-Interact) and an agentic tool-use setting ($a$-Interact), and covers CRUD-style tasks with ambiguous first sub-tasks, follow-up sub-tasks, and executable test-case based evaluation. The paper also reports baseline results for several frontier LLMs and analyzes interaction behavior, including memory grafting, interaction test-time scaling, and simulator reliability.

## Strengths
The main strength is the problem formulation. The paper identifies a real gap in current text-to-SQL evaluation, namely that strong single-turn performance does not tell us much about whether a model can resolve ambiguity, recover from errors, and maintain state over evolving user goals. This is a useful and timely benchmark direction.

The benchmark design is fairly comprehensive. Compared with prior static conversational datasets, the paper combines multiple ingredients that matter in practice: executable DB environments, state-changing operations, external knowledge, ambiguity injection, follow-up tasks, and a user simulator. The inclusion of CRUD, not just SELECT-only BI queries, is a meaningful broadening of scope.

I found **Figure 1** helpful as a high-level illustration of the intended interaction loop. It makes concrete the paper’s central claim that the relevant unit of evaluation is not just one utterance mapped to one SQL query, but a staged process involving clarification, execution feedback, and follow-up requests. Likewise, **Figure 3** is one of the more effective parts of the presentation, because it clarifies the difference between $c$-Interact and $a$-Interact, the action interfaces, and the reward consequences of debugging. For a benchmark paper, this kind of operational clarity matters.

The function-driven simulator is a sensible engineering choice. The paper is right to worry about leakage and uncontrolled behavior in pure LLM simulators. The two-stage parser-generator design is not algorithmically deep, but it is practically motivated and, based on the presented evidence, useful.

The empirical results do support the claim that this benchmark is difficult. **Table 2** is convincing in showing that even the strongest tested models have low end-to-end success, especially on follow-up subtasks. The split by BI versus DM is also informative: the gap suggests the benchmark is not merely hard because it is long-horizon, but because BI-style reasoning with business semantics remains brittle.

The simulator analysis is a genuine plus. **Figure 6** and **Table 3** provide at least some evidence that the proposed simulator is more robust and more aligned with humans than a baseline LLM simulator. Many benchmark papers hand-wave simulator quality; this one makes a concrete attempt to validate it.

The paper is generally ambitious in scope. It is not just a dataset dump, it also defines interaction protocols, budget-aware settings, executable evaluation, and behavioral analyses such as memory grafting and action-distribution profiling.

## Weaknesses
1. **The benchmark’s realism is partly undercut by a simulator design that is grounded in the ground-truth SQL, which creates a tension between controllability and ecological validity.**  
   This issue is visible already in the main paper. On **Page 4**, the authors state that each injected ambiguity is paired with a corresponding SQL snippet from the ground-truth query as a clarification source. On **Page 5**, the simulator is described as using annotated GT SQL and clarification sources to generate responses. Then Appendix D explicitly says the simulator is additionally provided with the reference SQL to generate accurate clarifications. I understand why this is done, but this means the “user” is not merely simulating user intent, it is partially acting as a controlled interface to the gold solution. That is good for reproducibility, but it makes the benchmark less representative of real users, who usually do not know the exact latent SQL semantics of their own request. This matters because one of the paper’s headline claims is greater realism. In its current form, the benchmark is better described as a controlled interactive evaluation environment than as a high-fidelity proxy for human interaction.

2. **The empirical validation of the simulator is useful but still too narrow to justify the stronger realism claims.**  
   The paper presents **Figure 6** and **Table 3** as evidence that the simulator is robust and aligned with humans, but the evidence is limited in important ways. First, the human-alignment study in **Section 6** uses only 100 randomly sampled tasks and evaluates correlation of model success rates under humans versus simulators. A high Pearson correlation across seven systems is encouraging, but it is a coarse metric. It does not show that turn-level responses are human-like, nor that the clarifications themselves are behaviorally realistic. Two simulators could induce similar aggregate success rates while differing substantially in conversational dynamics. Second, the USERSIM-GUARD evaluation is itself judged by another LLM, which is a reasonable expedient but not a definitive validation. So the paper has evidence for guardrail effectiveness, but not yet enough evidence for the stronger claim that it “restores realism” in the interaction loop.

3. **The comparison between $c$-Interact and $a$-Interact is interesting, but the protocols are not normalized enough for strong conclusions about model capabilities across modes.**  
   In **Section 4.1** and **4.2**, the two modes differ not only in interaction freedom but also in action spaces, budget accounting, and reward structure. In $c$-Interact, the budget is the number of clarification turns, $\tau_{\mathrm{clar}} = m_{\mathrm{amb}} + \lambda_{\mathrm{pat}}$, while in $a$-Interact$,$ the total budget is \(B = B_{\mathrm{base}} + 2m_{\mathrm{amb}} + 2\lambda_{\mathrm{pat}}\) with heterogeneous per-action costs. On top of that, the reward functions differ between the two settings, as defined in Appendix F. As a result, statements like “interaction mode emerged as the decisive factor” in **Section 5.1** are too strong, because the paper is not varying only the interaction mode. It is varying several design choices simultaneously. A cleaner comparison would hold reward structure and effective information budget as constant as possible.

4. **The metric design is asymmetric and hard to interpret across settings, especially the normalized reward.**  
   In **Section 2** and Appendix F, SR is straightforward, but the normalized reward is much more ad hoc. For $c$-Interact, the reward distinguishes first-pass success and post-debugging success using fixed values \(0.7, 0.5, 0.3, 0.2\), while for $a$-Interact the reward collapses to \(1.0, 0.7, 0\). This means normalized reward is not the same construct across settings. It is not just a rescaling, it encodes different preferences over trajectories. The paper then discusses SR and NR together in **Section 5.1**, but because the reward is setting-dependent, cross-setting reward comparisons become muddy. This matters because the paper uses reward to support behavioral conclusions, yet the reader cannot easily disentangle whether differences are due to model behavior or to the scoring definition.

5. **Some of the core mathematical formalization is too loose for a paper that repeatedly leans on formal task definitions.**  
   The formalization in **Equation (1)** on **Page 3** writes
   \[
   u_i^t=\mathcal{U}_\gamma(h_i^{t-1},q_i,\mathcal{E}), \quad
   s_i^t=\mathcal{S}_\theta(h_i^{t-1},u_i^t,\mathcal{E}), \quad
   h_i^t=h_i^{t-1}\oplus \langle u_i^t,s_i^t\rangle.
   \]
   This is fine as a sketch, but it does not actually model the two evaluation settings later described. In $a$-Interact, the system interacts with a tool environment using a structured action space, not merely with a user utterance \(u_i^t\). In other words, the variable \(u_i^t\) is overloaded: sometimes it is a user message, sometimes the environment observation after a tool call, sometimes execution feedback. The history concatenation operator \(\oplus\) is also described as “text concatenation in prompt,” which is implementation-specific and elides the structured state. If the paper wants a formal task definition, it should define a trajectory over observations, actions, and environment states explicitly, perhaps with \(o_t, a_t, e_t\), especially since database state changes after DML/DDL are central to the benchmark.

6. **There are also technical inconsistencies around the success-rate definition for follow-up tasks.**  
   In **Section 2**, the paper says SR is “the proportion of sub-tasks completed successfully” and that subsequent sub-tasks are released only after successful completion of first sub-tasks. In Appendix F, \(\text{SR}_j=\frac{1}{N}\sum_{i=1}^{N}\mathbb{I}[\mathcal{T}_{i,j}(\sigma_{i,j})=\texttt{True}]\) is defined over all \(N\) tasks for both \(j=1,2\). But for sub-task 2, many trajectories terminate before \(q_{i,2}\) is even issued. The current formula implicitly counts all unreached second subtasks as failures, which may be acceptable, but then it is really a cumulative task-level success metric, not a conditional follow-up accuracy. This distinction matters for interpretation of the low follow-up SRs in **Table 2**. It would help to report both cumulative SR and conditional SR given that sub-task 2 was reached.

7. **The evidence for the budget-awareness and ITS claims is suggestive rather than fully convincing.**  
   The ITS story in **Section 5.2** and **Figure 4** is interesting, but the paper goes a bit too far in naming an “ITS Law.” The curves shown in **Figure 4** are limited to a small number of patience values and a few models on the LITE set. Some models do not exhibit strong monotonic scaling, and “can match or even surpass idealized single-turn performance” is a very strong statement for what is essentially a descriptive observation under one benchmark design. This should be framed as an empirical trend or hypothesis, not a law.

8. **The memory grafting analysis is intriguing but causally ambiguous.**  
   In **Section 5.2** and **Figure 5**, GPT-5 improves when given ambiguity-resolution histories from stronger communicators. That is a nice observation, but the interpretation that GPT-5 mainly suffers from “deficiency in interactive communication abilities rather than its core generation capability” is not fully established. The grafted histories provide additional task-relevant information, not just a better communication schema. So the experiment conflates communication quality with information transfer. A stronger test would compare grafted histories against matched synthetic histories with equivalent information content but different style, or against oracle compact clarifications.

9. **Several important experimental choices are under-ablated.**  
   For a benchmark paper, design sensitivity matters. Yet the main paper gives very little ablation on: the ambiguity injection process itself, the relative proportions of ambiguity types, the effect of knowledge masking versus user-query ambiguity, the one-debugging-attempt rule, and the chosen action costs in $a$-Interact. **Table 1** reports average ambiguities per task and interaction counts, and **Figure 2** illustrates knowledge chain breaking, but there is no main-paper ablation showing how much each ambiguity source contributes to difficulty or how stable rankings are under different budget/cost schedules. This makes it harder to know whether the benchmark measures robust interactive competence or sensitivity to a particular protocol design.

10. **The baseline methodology is adequate for a benchmark paper, but not as strong as the paper’s breadth would warrant.**  
    The authors evaluate seven strong models, which is good, but all experiments are single runs with deterministic decoding, as stated in **Section 5** and Appendix I.3. Determinism helps reproducibility, but it does not remove all variance because API-backed models can change over time and interaction trajectories can be brittle to formatting details. More importantly, there is limited method diversity in the baselines. The paper mostly evaluates general-purpose LLMs with prompts, while a benchmark of this kind would benefit from at least one stronger agentic or text-to-SQL-specific scaffold per setting in the main paper. Otherwise, low scores may partly reflect weak adaptation rather than benchmark difficulty.

11. **Presentation quality is uneven, and in places the writing makes stronger claims than the evidence supports.**  
    There are many awkward or ungrammatical phrases in the main paper, for example “This evidence demonstrates the critical importance of matching interaction modes to model-specific capabilities” in **Section 5.1**, or “designed personally” on **Page 8**, or several inconsistent names and typos across the appendix tables and figures. These are fixable, but the issue is not just style. The writing occasionally over-asserts causal explanations from correlational evidence. Also, **Figure 4** is conceptually important, but the multi-panel presentation is hard to parse in the paper body without more explicit panel references. The red-versus-blue mode comparison is useful, but the reader has to work harder than necessary to map each subplot to the narrative claims.

12. **There is a minor but real inconsistency around human-subject involvement and ethics reporting.**  
    The ethics statement on **Page 11** says “This work does not involve crowdsourcing or research with human subjects,” yet **Section 6** describes human experts interacting with 7 system models on 100 sampled tasks, and Appendix Q describes 10 experts evaluating 300 data points. I am not alleging misconduct here, but this is plainly human evaluation. The statement should be corrected and clarified, including whether this fell under exempt internal expert evaluation or required any institutional review determination.

## Questions
1. The strongest concern for me is the simulator’s dependence on ground-truth SQL. Can the authors clarify, in the main paper, what exactly is exposed to the simulator at inference time for each action type, and whether they can quantify how much performance changes if simulator answers are restricted to natural-language annotations only, without AST retrieval from gold SQL segments? A controlled ablation here would increase my confidence in the benchmark’s external validity.

2. Please clarify the intended interpretation of follow-up SR in **Equation (2)** and **Table 2**. Is follow-up SR cumulative over all tasks, counting unreached second subtasks as failures, or conditional on reaching the second subtask? I strongly encourage reporting both. That would make the difficulty decomposition much cleaner.

3. For the comparison between $c$-Interact and $a$-Interact, can the authors justify more explicitly why the reward functions and budgets differ across settings? If the goal is to compare interaction paradigms, a discussion of effective budget parity or a normalization analysis would help.

4. The memory grafting result in **Figure 5** is interesting, but it currently does not separate “better interaction style” from “more complete information.” Do the authors have any evidence, even qualitative, that the gain is due to communication strategy rather than simply getting the right clarifications injected into the context?

5. Can the authors provide a stronger main-paper sensitivity analysis for the $a$-Interact action costs in **Table 9**? Right now, some behavioral conclusions, especially about overuse of `submit` and `ask`, may depend quite a bit on the chosen cost schedule.

6. Since the benchmark is positioned as realistic and practical, it would help to know the failure modes of the simulator on human-written clarifications beyond aggregate correlation. Do the authors have turn-level examples where the simulator diverges from humans, and are these concentrated in AMB, LOC, or UNA cases?

7. Please clarify whether the human studies described in **Section 6** and Appendix Q were considered human-subject evaluation under your institution’s policies, or whether they were internal expert assessments exempt from review. This should be stated consistently in the ethics section.

## Flag For Ethics Review
- Yes, Responsible research practice (e.g., human subjects, data release)

## Details Of Ethics Concerns
The paper includes human expert interaction/evaluation in at least two places: **Section 6** reports human experts interacting with 7 system models on 100 sampled tasks, and Appendix Q reports 10 experts evaluating 300 data points. However, the ethics statement on **Page 11** says the work “does not involve crowdsourcing or research with human subjects.” That wording appears inaccurate or at least incomplete. This is not a claim of serious ethical violation, but the paper should clarify the nature of these human evaluations, whether they were internal expert assessments, and whether any institutional review or exemption applied.

## Soundness Rating
3: good. The benchmark construction and experimental methodology are largely reasonable, and the central claims are supported at a useful benchmark-paper level, but several conclusions are stronger than the evidence strictly warrants, especially around realism, cross-mode comparability, and some behavioral interpretations.

## Presentation Rating
3: good. The paper is generally understandable and includes useful figures and tables, but the writing is uneven, some formalization choices are loose, and a few core concepts and metrics need cleaner explanation.

## Contribution Rating
4: excellent. Despite the concerns above, this is a substantial benchmark contribution. It broadens interactive text-to-SQL evaluation in a way that is likely to be useful to the community, and it goes beyond a narrow dataset release by providing executable environments, protocols, and simulator analysis.

## Overall Rating
8: Accept, good paper (poster). I have several substantive reservations, mainly about simulator realism, metric comparability, and under-ablated design choices. Still, the benchmark addresses an important gap, the scope is meaningful, the empirical package is strong enough for a benchmark paper, and I expect the resource to be valuable for the community.

## Reviewer Confidence
4: confident. I am confident in the overall assessment and familiar with the relevant text-to-SQL and interactive-agent benchmarking literature, though some implementation details would benefit from clarification in rebuttal.