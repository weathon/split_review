---
job_id: ba4dccd0-4c37-42db-9296-b06e4d7fab75
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: qPbDM5L8tE.pdf
paper: CORAL: Contact-Rich Adaptive LLM-based Control for Robotic Manipulation
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅ This paper is clearly within ICLR scope, at the intersection of robotics, planning/control, foundation models, and neuro-symbolic ML systems for contact-rich manipulation.

## Minimum Quality
Pass ✅ The paper contains the expected core sections, namely Abstract, Introduction, Related Work, Methodology, Experiments, Results/Analysis, and Conclusion. While I have substantial concerns about methodological completeness, mathematical specification, and empirical support, these rise to the level of a weak submission rather than an automatic desk reject.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅ I did not find evidence in the provided paper text of hidden prompts, instructions to reviewers, or other manipulative content targeting automated reviewing.

# Expected Review Outcome:
## Summary
This paper proposes CoRAL, a modular framework for contact-rich robot manipulation that combines pose tracking, VLM-based physical parameter estimation, LLM-generated cost functions and contact strategies, a retrieval-based memory unit, and MPPI with reactive feedback control. The paper argues that this decomposition enables zero-shot execution on contact-rich tasks without teleoperated action datasets, and evaluates the approach in simulation on six tasks plus ablations over memory, refinement, role separation, and pose tracking.

## Strengths
The paper tackles a meaningful problem. Contact-rich manipulation is exactly where many current end-to-end VLA systems look brittle, and the paper makes a reasonable case that explicit planning and reactive control are useful here.

The modular decomposition is conceptually appealing. In particular, the separation between geometric state estimation, semantic/physical prior estimation, symbolic strategy generation, and low-level control is easy to understand and, at least at a high level, well motivated by the failure modes of monolithic VLAs.

I appreciated that the paper does not just claim “LLM for robotics” in the abstract, but maps the LLM output into concrete planner artifacts, namely a cost function and a contact strategy. That is a more actionable integration than many papers that stop at language plans.

**Figure 2** is one of the clearer parts of the paper. It makes the nested inner/outer loop structure understandable, especially the distinction between fast reactive retries and slower high-level refinement. This figure helps the reader see the intended algorithmic flow much better than the text alone in Sections 3.2 to 3.4.

The ablations are directionally useful, even if incomplete. **Table 1** does suggest that some components matter materially: removing pose tracking collapses performance, and removing refinement hurts the more sequential tasks. The very poor performance of **CoRAL (Unified VLM)** in Table 1, while not yet fully isolated experimentally, at least supports the authors’ central design claim that role separation is not arbitrary.

The qualitative task panel in **Figure 3** is also useful. It gives a quick view of the task diversity, including multi-stage pushing-plus-grasping, constant-force pushing, and wall-assisted flipping. This is important because the central claim is not merely generic manipulation, but manipulation with contact structure and strategy.

## Weaknesses
I have quite a few concerns, and several of them affect the paper’s scientific value rather than just polish.

1. **The main empirical claim is stronger than the evidence presented.**  
   The paper repeatedly frames CoRAL as a robust zero-shot framework for “complex, dynamic, and contact-rich manipulation” with improved explainability and adaptability, but the main experiments in Section 4 are limited to **simulation only** with **10 trials per task** on **6 tasks**. That is simply not enough to support the broader claims. The issue is not that simulation is invalid, it is that the rhetoric overshoots the evidence. For instance, the abstract and Introduction emphasize robustness and real-world adaptability, but the actual evaluation is in robosuite/MuJoCo only, with fixed robot morphology and a very small task set.  
   Why this matters: for a method whose central difficulty is bridging semantic reasoning to physical interaction, external validity is the whole ballgame. With only this evaluation, I can conclude “promising in a narrow simulated setting,” not “robust framework” in the stronger sense the paper suggests.

2. **The comparison to state-of-the-art VLA baselines is not very fair or very informative.**  
   In **Table 1**, OpenVLA and $\pi$-style baselines are evaluated using released LIBERO checkpoints, including on custom tasks such as T1, T4, T5, and T6 that are obviously outside the distribution of those checkpoints. The paper then uses their failure to support claims about the superiority of the proposed modular reasoning approach. That is not a clean comparison. You are partly measuring out-of-distribution failure of pretrained imitation policies, not just architectural inferiority.  
   The problem is especially visible because the paper itself acknowledges that T1/T4/T5/T6 are custom contact-rich tasks designed to be hard for collision-avoidant planners and standard VLAs. That can be a useful stress test, but it cannot carry the full burden of the paper’s main comparison. A stronger study would either adapt baselines more carefully, compare to planner-augmented alternatives, or at least include stronger contact-aware learned baselines.  
   Why this matters: if the baseline setup is weak, the headline “significantly outperforms SOTA” becomes much less persuasive.

3. **The method is mathematically underspecified in several places, and the equations are more illustrative than operational.**  
   This is a serious issue. In Section 3.2, **Equation (2)** is introduced as an illustrative example of the LLM-generated cost, but the paper simultaneously claims that the LLM is “free to introduce any cost terms constructible from the available state, pose, and action variables.” This means the actual optimization problem solved at test time is not well specified in the main paper. What exact grammar or API constrains valid cost generation? What variables are always available? How are malformed, unsafe, or dimensionally inconsistent costs handled? None of this is formalized.  
   Similarly, **Equation (3)** defines contact points via tangent vectors and a region radius, but the main paper does not explain where the centers $c_j$, radii $e_j$, normals, or tangent frames come from in implementable detail. The appendix gives some code-level intuition, but the main method still leaves this underdefined.  
   In Section 3.3, **Equations (4) to (6)** give a generic MPPI update, but the relation between the free-form LLM-generated code and the required running cost $q(x_t,u_t)$ is not mathematically pinned down. There is also no discussion of what happens if the generated cost depends on non-Markovian signals, discontinuous logic, unavailable simulator internals, or latent quantities not in the tracked state.  
   Why this matters: the central claimed contribution is the LLM-generated planner objective. If that piece is underspecified, it is hard to assess reproducibility, correctness, and even what exactly is being compared.

4. **The “online adaptation” mechanism is presented as if it performs principled system identification, but the actual mechanism is heuristic and not rigorously validated.**  
   Section 3.4 states that the LLM updates world parameters such as mass and friction based on failed executions. **Figure 4** then shows mass correction over time, and the text claims convergence “remarkably close” to the true values. But this is only a single qualitative adaptation plot for one parameterized scenario, with no systematic evaluation of estimation error, stability, sensitivity to initialization, or frequency of harmful corrections.  
   There is also a conceptual gap: updating mass and friction from short-horizon execution history is an inverse problem with obvious non-identifiability issues. Different combinations of friction, mass, controller gains, and contact geometry can produce similar trajectories. The paper does not acknowledge this ambiguity, does not formalize assumptions, and does not show that its corrections are reliable beyond anecdotal cases.  
   Why this matters: the paper leans heavily on adaptation as a distinguishing feature. Right now it looks more like an LLM-powered heuristic retry loop than a validated online identification method.

5. **The memory unit is too vague to evaluate scientifically.**  
   In Section 3.2, memory retrieval is summarized by **Equation (1)**, but that equation is purely symbolic. The paper says the system retrieves similar successful experiences using RAG and that “the LLM embeds the current task into a latent semantic space,” yet there is no real specification of the key ingredients: what is stored exactly, what embedding model is used, what similarity metric or retrieval index is used, how “sufficiently similar” is decided, whether retrieval can fail safely, and whether memory entries are task-specific code snippets or abstract plans.  
   The empirical evidence in **Table 1** shows some benefit from memory, for example on T1 and T6, but the design remains too underspecified for the reader to know whether this is a robust mechanism or just a lightly engineered nearest-neighbor cache.  
   Why this matters: memory is advertised as one of the main contributions, yet it is not described at the level expected for reproducible research.

6. **The presentation around explainability is overstated relative to what is shown.**  
   I agree that modular systems are often more inspectable than end-to-end policies, but “explainability” here mostly means the LLM emits natural-language rationales and Python-like cost functions. That is not the same as demonstrating faithful explanations of behavior. The discussion on Page 10 says the model can “articulate why it failed and what it is doing to correct its plan,” and refers to “Appendix ??”, which is itself a red flag that the exposition is unfinished.  
   The example in the appendix, shown as **Figure 6** there, is a plausible natural-language diagnosis, but this does not establish that the explanation is causally faithful rather than post hoc narration. The paper never evaluates explanation correctness or usefulness with any metric or user study.  
   Why this matters: explainability is one of the paper’s repeated selling points. At the moment it is mostly an intuition, not a demonstrated result.

7. **The quantitative evidence in Table 1 is mixed, and some of the paper’s framing glosses over that.**  
   **Table 1** is more nuanced than the narrative suggests. Yes, CoRAL beats the VLA baselines on several custom contact-heavy tasks, but it also underperforms the **Expert FSM** baseline quite substantially across most tasks, including on the very tasks that are supposed to showcase strategic structure. For example, on T1 the full method gets **4/10**, versus **8/10** for Expert FSM; on T6 it gets **7/10** versus **9/10**. Completion times are also often much worse than simpler baselines.  
   This is not fatal, and I do not expect a zero-shot method to beat carefully engineered FSMs. But the paper should be more candid that the current system is still far from expert task-specific control, especially on the hardest settings. The T1 result is particularly uncomfortable given that it is used repeatedly as a showcase task, yet the full system succeeds in less than half of trials.  
   Why this matters: the contribution is interesting, but the actual level of performance is not yet as strong as the prose implies.

8. **Several implementation and notation details are inconsistent or confusing, which hurts confidence.**  
   There are multiple small-but-important issues: the paper compares against $\pi_{0.5}$ in text but **Table 1** lists **$\pi0.3$**; T3 is called “Pick and Place in Clutter” in Section 4 but “Pick+Place Chitter” in **Table 1**; the references contain multiple suspicious year/format inconsistencies; and the appendix has quite a bit of corrupted or garbled text. On Page 10, “Appendix ??” appears unresolved.  
   These are not just cosmetic. In a paper making fairly intricate systems claims, sloppiness in naming and cross-referencing lowers confidence that the experiments and components are fully under control.

9. **The core ablations do not isolate causality as cleanly as the paper claims.**  
   The role-separation claim is interesting, but the **Unified VLM** ablation in **Table 1** bundles multiple changes into one variant. It is not clear whether the failure comes from model capacity, prompting, API behavior, poor interface design, or genuinely from the conceptual decision to separate roles. Likewise, “w/o Refinement” disables a large bundle of adaptation behaviors, including both parameter updates and plan rewriting, so we cannot tell what actually matters most.  
   The paper also discusses the contact-strategy ablation largely through appendix visualizations (**Figure 5** there), but there is no corresponding systematic main-text table over multiple tasks.  
   Why this matters: the central scientific claim is about which architectural choices matter. The current ablation suite points in a direction, but does not nail the case down.

10. **There is no serious analysis of computational feasibility in the main paper, despite runtime being central to the proposal.**  
    The main paper states **$K=200$**, horizon **$H=50$**, CPU rollout, and GPT-4o-based modules, but leaves the practical control-rate implications mostly to the appendix limitations section. For an approach combining tracking, simulation-based MPPI, and occasional LLM/VLM calls, runtime is not a side issue. It determines whether the framework is usable beyond slow, forgiving tasks.  
    **Figure 2** suggests a nested feedback architecture that sounds responsive, but the main paper does not quantify inner-loop frequency, end-to-end action latency, or failure cases caused by delayed updates.  
    Why this matters: the paper’s claims about reactive adaptation are hard to interpret without a main-text runtime characterization.

## Questions
1. The biggest clarification I need is about the exact interface from the LLM to the planner. What is the formal schema of admissible cost functions and what safeguards are enforced? In particular, can the authors specify which state variables are always exposed to generated code, how invalid code is handled, and whether there is any normalization or unit checking before MPPI consumes the cost?

2. Can the authors provide a more rigorous description of the memory module beyond Equation (1)? What embedding model is used, what keys/values are stored, how similarity is computed, what retrieval threshold is used, and how often retrieval hurts rather than helps?

3. For the online parameter adaptation claims around mass and friction, can the authors provide quantitative results over many trials rather than a single illustrative case in Figure 4? For example, average parameter estimation error before/after adaptation, success rate as a function of initialization bias, and whether updates ever diverge or oscillate.

4. The current comparison to OpenVLA and $\pi$-style models is not fully convincing for the custom contact-rich tasks. Could the authors either add stronger contact-aware learned baselines or more carefully justify why the chosen checkpoints constitute a fair comparison for T1/T4/T5/T6?

5. The role-separation claim would be stronger with cleaner ablations. Can the authors disentangle whether the poor **Unified VLM** results are due to prompt/interface design, model overload, or the conceptual separation itself? Right now the ablation is too bundled.

6. Since **Table 1** shows the full method still clearly below the Expert FSM on several tasks, I would like a more candid discussion of where the gap comes from. Is it mostly perception error, poor cost synthesis, insufficient contact strategy proposal, or MPPI limitations?

7. A practical question: what is the actual control/update rate of the inner loop in the reported setup, and how often is the outer-loop LLM adaptation triggered during successful episodes?

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics concerns are evident from the submission itself. The work is evaluated in simulation and does not raise immediate issues requiring dedicated ethics review based on the material presented.

## Soundness Rating
2: fair. The core idea is plausible and some empirical evidence supports it, but several central claims are only partially substantiated, and the method specification is too incomplete in key places.

## Presentation Rating
2: fair. The high-level story is understandable and some figures are helpful, but the paper has notable issues in notation, cross-referencing, consistency, and precise methodological exposition.

## Contribution Rating
2: fair. The paper has an interesting systems idea, namely using LLMs to synthesize planner objectives and contact strategies for contact-rich control, but the current empirical and methodological support does not yet justify a stronger contribution score.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted.  
I see the appeal of the idea, and there is a real seed of contribution here. Still, the paper is currently too underspecified and too lightly validated for me to support acceptance at ICLR main track. The strongest version of my criticism is: the paper sells a principled neuro-symbolic control framework, but in its current form it reads more like a promising prototype with encouraging simulation results than a fully convincing scientific account.

## Reviewer Confidence
4: confident. I am confident in this assessment, though not absolutely certain. The topic is close to my expertise, and I checked the methodological and experimental details carefully, but some implementation specifics remain unclear from the paper.