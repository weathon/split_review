---
job_id: b73e698f-d042-4bd6-85d4-6e7e1e67c7ca
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: cZFgsLq8Gs.pdf
paper: DeepScientist: Advancing Frontier-Pushing Scientific Findings Progressively
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, focusing on autonomous ML research systems, Bayesian optimization-style search, LLM-based agents, evaluation infrastructure, and applications across modern AI tasks.

## Minimum Quality
Pass ✅. The submission contains the required components, namely abstract, introduction, related work, method, experiments, results/analysis, and conclusion/discussion, and it presents enough technical and empirical material to warrant full review rather than desk rejection, despite several important weaknesses.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, reviewer-targeted instructions, or other obvious manipulative content in the provided paper text.

# Expected Review Outcome:
## Summary
This paper presents DeepScientist, an autonomous multi-agent system for long-horizon, goal-directed scientific discovery on compute-intensive AI tasks. The system is framed as a Bayesian optimization loop over candidate research programs, with a persistent Findings Memory, an LLM surrogate model that scores ideas, and a UCB-style acquisition rule to decide which hypotheses to implement and validate. Empirically, the paper studies three AI tasks, agent failure attribution, LLM inference acceleration, and AI text detection, and reports that DeepScientist discovers methods surpassing the chosen human baselines while also analyzing the large-scale search trajectory and the quality of the resulting AI-generated papers.

## Strengths
1. The paper asks an ambitious and relevant question for the ICLR community, namely whether an autonomous system can sustain goal-directed progress on nontrivial ML tasks rather than producing isolated one-off ideas. That framing is broader than a standard “agent benchmark” paper and is scientifically interesting.

2. The system-level design is reasonably clear at a high level. In particular, **Figure 2** on **Page 4** does a good job of visualizing the closed-loop workflow across hypothesis generation, implementation/verification, and analysis/reporting, and it makes the role of the persistent Findings Memory easy to understand. This figure materially helps the reader distinguish the proposed setup from simpler “generate one idea, run one experiment” pipelines.

3. The empirical scope is larger than in many recent AI-scientist-style papers. The authors do not only report end metrics, they also expose search statistics, success rates, and execution-time distributions. **Figure 4(a-c)** on **Page 8** is useful here: panel (a) conveys the severe funnel from ideas to validated progress, panel (b) highlights that the selection strategy matters, and panel (c) makes the runtime distribution concrete. Even if I have concerns about interpretation, the paper benefits from showing the process rather than only final wins.

4. The paper includes multiple types of evaluation instead of just task performance. The comparison in **Table 2** on **Page 7** and the human review study in **Table 3** on **Page 7** attempt to assess paper quality, not only benchmark scores. I do not fully trust all of these assessments, but the attempt to evaluate the research artifacts themselves is a worthwhile addition.

5. The three application case studies are diverse. Agent attribution, inference acceleration, and text detection stress rather different aspects of the system, and this is preferable to evaluating on a single friendly domain.

6. Some visual evidence supports the “progressive search” story. **Figure 5** on **Page 9** is a useful qualitative illustration of how the AI text detection ideas evolve from the initial point toward multiple later “progress ideas,” instead of appearing as isolated random jumps. This does not prove causality, but it does support the narrative that the system revisits and extends its own findings.

## Weaknesses
1. The central “Bayesian optimization” formulation is much thinner than the paper claims, and this matters because it is presented as the core methodological contribution. On **Pages 4-5**, the surrogate model \(g_t\) is just an LLM assigning integer scores \(V=\langle v_u, v_q, v_e\rangle\), and the acquisition rule in **Equation (1)** is
\[
I_{t+1}=\arg\max_{I\in \mathcal{P}_{\text{new}}}\big(w_u v_u+w_q v_q+\kappa v_e\big).
\]
This is not really a standard UCB derivation, because there is no calibrated predictive mean/uncertainty model over a shared search space, no posterior update, and no notion of uncertainty estimated from observations in the BO sense. The paper even labels \(v_e\) as \(\sigma(I)\), but \(v_e\) is just another LLM-produced heuristic score, not an uncertainty estimate arising from a probabilistic surrogate. Also, the annotation under **Equation (1)** says both terms are “Exploitation Term,” which appears to be a mistake, but more importantly it hints at conceptual looseness. Why this matters: a major part of the paper’s claimed scientific framing is that discovery is formalized as BO, yet the actual mechanism is much closer to heuristic scalarization of LLM judgments plus greedy selection. The paper would be stronger if it simply stated this more modestly, or if it provided a real BO instantiation.

2. The notion of “fully autonomous” or “end-to-end autonomy” is overstated relative to the actual experimental protocol. On **Page 5**, the paper says “Three human experts supervise the process to verify outputs and filter out hallucinations.” On **Page 11**, the ethics statement says “all results ... have undergone rigorous human verification,” and **Appendix F** further notes that all experimental results were manually inspected by human supervisors. Those may be reasonable safeguards, but they materially complicate the headline claim that the system autonomously advances scientific frontiers. This is not a semantic nitpick. If humans are filtering, verifying, and effectively deciding which outputs count as authentic, then the scientific credit assignment between agentic search and human intervention becomes blurred. A stronger paper would quantify exactly where human intervention occurs, how often it changes outcomes, and whether the reported five successful papers would still emerge under a truly blind autonomous pipeline.

3. The empirical evidence for the system-level contribution is suggestive but still not cleanly isolating what actually makes DeepScientist work. The paper repeatedly attributes success to the Findings Memory plus the BO-style selection strategy, but the ablation evidence is limited. **Figure 4(b)** on **Page 8** compares the selection strategy to random sampling, which is a very weak baseline. That does not tell us whether the gains come from memory retrieval, from surrogate scoring, from the specific UCB scalarization, from the use of stronger coding models, or from human-supervised curation of baselines and environments. Relatedly, **Figure 6** on **Page 10** is used to argue a near-linear scaling law, but the study changes the number of parallel GPU instances while also relying on shared synchronization and distinct limitations assigned to each path. This design entangles compute scale, search diversification, and memory sharing. Why this matters: the paper’s central contribution is a system recipe, so component-level attribution is essential. Right now, the evidence mostly shows that the whole stack plus a lot of compute can eventually find improvements, not which ingredients are scientifically responsible.

4. The strength of the reported task improvements is uneven, and the paper sometimes overstates the significance of modest gains. In **Figure 3(c)** and the performance summary table on **Page 6**, the LLM inference acceleration result is from 190.25 to 193.90 tokens/s, a **1.9%** improvement. That may still be useful, but the paper wraps it into broad claims about “autonomously redesigning core methodologies” and “progressively surpass human SOTA” in a way that reads stronger than the actual evidence for that task. By contrast, the text detection and failure attribution gains are much larger. This heterogeneity should be discussed more honestly. Similarly, the text-detection storyline in **Figure 1** on **Page 1** is visually persuasive, but it compares a two-week autonomous run to “three years of cumulative human research,” which is a loaded framing because the human and AI research settings are not normalized for access to prior literature, code, compute utilization, or task-specific starting points. The figure is rhetorically effective, but scientifically it is too easy to over-interpret.

5. The paper-quality evaluation in **Table 2** and **Table 3** on **Page 7** is interesting but not strong enough to support some of the conclusions drawn in Section 4.2. **Table 2** is based on DeepReviewer-14B, an automatic reviewer created by the authors’ broader research line, and the number of papers per system is very small and potentially curated, as the table note itself acknowledges. **Table 3** uses three human reviewers for five papers, which is better, but the mean ratings are not especially strong: two papers are above 5.5, while two are at 4.33. Yet the text says the system’s average rating “closely mirrors the average of all ICLR 2025 submissions.” That is numerically true in the narrow sense of 5.00 vs 5.08, but it is not clear this is a meaningful or stable conclusion from such a small, custom review exercise. Why it matters: this section is used to argue that the outputs are not just benchmark hacks but publishable scientific artifacts. The evidence is not yet robust enough for that claim.

6. The task selection and baselines raise external-validity concerns. **Table 1** on **Page 5** lists three starting methods chosen for frontier status and supervisability, but all three tasks are still in a narrow band of LLM-centric AI problems where fast feedback, public code, and benchmark metrics are available. The paper itself partially admits this on **Pages 8-10**, noting that low success rates would make many slower scientific domains impractical. That is fair, but it undercuts some of the broader rhetoric in the abstract and conclusion about AI achieving frontier scientific discovery in general. The paper would be better framed as a strong result on a specific class of software-centric ML research problems, not as evidence for a broad shift in scientific discovery.

7. Several mathematical and methodological details are underspecified enough to hinder careful verification. A few examples:
   - On **Page 4**, the system retrieves Top-\(K\) findings from memory, but the retrieval objective, relevance scoring, and failure modes are not specified in the main paper.
   - In **Equation (1)** on **Page 5**, the candidate set is written as \(\mathcal P_{\text{new}}\), which suggests selection only among newly generated hypotheses. But the surrounding text also implies the system reasons over all records in memory. It is unclear whether previously generated but not yet implemented ideas can be reconsidered, or whether the acquisition is only over the current batch.
   - The mapping from LLM judgments to \(v_u, v_q, v_e\in\{0,\dots,100\}\) is entirely prompt-defined and subjective, but there is no main-paper discussion of calibration or consistency. If \(v_e\) is intended to stand in for exploration bonus, some justification is needed for why an integer “exploration value” from an LLM behaves like uncertainty.
   - The claimed fixed choice \(w_u=w_q=\kappa=1\) is presented as “task-agnostic,” but without evidence this is not just an arbitrary design decision.
   These details matter because the paper repeatedly presents the search strategy as principled rather than heuristic.

8. There are also presentation issues that, while not fatal alone, do affect trust in a paper making very broad claims. The references section contains multiple obvious inconsistencies and malformed entries, for example the citation to Wolters et al. on **Page 14** is about compute-in-memory architectures rather than retrieval, which seems unrelated to the retrieval model cited on **Page 4**. There are also duplicated or oddly formatted references and a garbled appendix placeholder on **Page 24**. In a paper whose core message is scientific rigor and autonomous paper production, these errors are not a good look.

## Questions
1. Can the authors disentangle the contribution of the major system components with stronger ablations in the main paper? In particular, I would like to see comparisons of:  
   (i) no Findings Memory,  
   (ii) Findings Memory without surrogate scoring,  
   (iii) surrogate scoring without the UCB-style acquisition,  
   (iv) random selection from the same candidate pool, and  
   (v) repeated implementation attempts on top-ranked ideas.  
   This would materially increase confidence that the claimed system design, not just brute-force search plus strong coding models, drives the results.

2. Please clarify the exact optimization domain in **Equation (1)**. Is the acquisition computed only over the newly generated set \(\mathcal P_{\text{new}}\), or over all pending “Idea Findings” in \(\mathcal M_t\)? If previously generated ideas can be revisited, the equation should reflect that. If not, then the method is much more myopic than the prose suggests.

3. What is the precise operational meaning of \(v_e\) in **Equation (1)**? If it is not an uncertainty estimate in the BO/UCB sense, I would strongly encourage the authors to avoid the UCB terminology or to provide evidence that \(v_e\) correlates with something measurable, such as novelty relative to retrieved memory or variance across multiple surrogate judgments.

4. Can the authors quantify the impact of human supervision on the reported findings? For example, how many candidate results were filtered out by humans, how often did humans override the system’s conclusions, and would the final five papers still emerge under a protocol where humans only verify after the run is complete?

5. For the LLM inference acceleration task, the gain in **Figure 3(c)** and **Page 6** is only 1.9%. Did the authors run multiple seeds or repeated measurements to assess variance? Without uncertainty estimates, it is hard to judge whether this is a robust algorithmic gain or a narrow benchmark fluctuation.

6. Regarding the “near-linear scaling” claim from **Figure 6** on **Page 10**, can the authors provide the actual data points, variance across repeated runs, and a comparison to serial scaling under fixed total compute? Right now the figure is interesting, but the claim feels stronger than the evidence shown.

7. The paper quality evaluation in **Table 2** and **Table 3** is provocative, but can the authors provide a more cautious interpretation? In particular, what would make them confident that these papers are genuinely publishable beyond matching a numerical average on a small custom review exercise?

## Flag For Ethics Review
- Yes, Potentially harmful insights, methodologies and applications  
- Yes, Responsible research practice (e.g., human subjects, data release)

## Details Of Ethics Concerns
The paper itself appropriately raises two nontrivial issues in the ethics statement on **Page 11**.

First, there is clear dual-use risk. A system designed to autonomously search, implement, and validate improvements over existing baselines could be repurposed toward harmful domains, including malware, offensive cyber tools, or other dangerous research directions. The authors mention red-teaming and refusal behavior of the underlying models, which is good, but the core methodology is general enough that this remains a meaningful ethics consideration.

Second, there is a responsible-research concern around automated paper generation and the academic ecosystem. The authors explicitly note the risk of proliferating scientifically weak but plausible-looking papers and say they will not open-source the “Analyze & Report” module. That concern is real and directly relevant to this submission because the work evaluates AI-generated papers and claims near-conference-level quality. Systems like this could increase submission volume and reduce signal if deployed without strong human verification and accountability.

## Soundness Rating
2: fair. The core empirical claims are partially supported, but the central BO/UCB framing is looser than advertised, component attribution is insufficient, and some conclusions are stronger than the evidence.

## Presentation Rating
2: fair. The high-level story is understandable and several figures are helpful, but the paper is over-claiming in places, some equations and methodological details are underspecified, and there are noticeable citation/reference quality issues.

## Contribution Rating
3: good. Despite my criticisms, the paper tackles an important problem, presents a substantial system effort, and offers evidence that autonomous goal-directed research agents can make progress on meaningful AI tasks.

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected. The paper is ambitious, relevant, and empirically substantial, and I do think the community should see it. At the same time, the methodological framing is looser than claimed, the autonomy story is not as clean as the headline suggests, and the ablations are not yet strong enough for an unqualified endorsement.

## Reviewer Confidence
4: confident. I am confident in my assessment, though not absolutely certain. I am familiar with the surrounding literature and carefully checked the main methodological claims and empirical evidence, but some task-specific details would benefit from author clarification.