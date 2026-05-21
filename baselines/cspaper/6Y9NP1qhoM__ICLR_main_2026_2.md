---
job_id: c54bd08f-9a19-4d22-962a-7ccd230fa21f
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: 6Y9NP1qhoM.pdf
paper: Goal-Aware Identification and Rectification of Misinformation in Multi-Agent Systems
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, it studies robustness and safety of LLM-based multi-agent systems, introduces a benchmark dataset, and proposes a defense method involving graph-based localization and language-model reasoning.

## Minimum Quality
Pass ✅. The paper contains the core scientific components expected for this kind of submission, including Abstract, Introduction, Related Work, Method, Experiments, quantitative results, and Conclusion/Limitations, and it presents a coherent empirical study despite several methodological and clarity issues that affect strength rather than minimum viability.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, suspicious reviewer-targeting instructions, or other manipulative content in the paper text or figures.

# Expected Review Outcome:
## Summary
This paper studies misinformation injection in LLM-based multi-agent systems, focusing on covert false information that can propagate through inter-agent communication and degrade task performance. The authors introduce MISINFOTASK, a 108-instance benchmark for misinformation red-teaming in multi-agent settings, and propose ARGUS, a training-free two-stage defense that first localizes important communication channels and then applies goal-aware rectification through a corrective agent. Experiments across multiple LLM backbones and three attack types report reductions in misinformation toxicity and improvements in task success rate relative to attack-only and two baseline defenses.

## Strengths
The paper tackles an important and timely problem. Most recent MAS safety work emphasizes jailbreaks, prompt injection, or generic adversarial behavior, while this submission focuses specifically on misinformation that is semantically benign yet factually wrong. That is a meaningful threat model distinction, and the paper explains reasonably well in Section 1 and Section 2.3 why covert misinformation deserves separate study.

The introduction of MISINFOTASK is a useful contribution. The benchmark goes beyond one-shot QA style evaluations and attempts to model decomposable, multi-step tasks that require coordination among agents. The dataset description on Pages 3 and 18, together with the example in **Figure 8** and the sample task in **Figure 9**, makes the intended benchmark format concrete. In particular, Figure 8 is helpful because it shows that each task instance includes not just a task and label, but also tools, misinformation goals, misleading arguments, and ground-truth counterfacts. That design is aligned with the paper’s threat model rather than being a generic repurposed benchmark.

ARGUS is practically motivated. A training-free defense is attractive for deployment because it avoids retraining specialized detectors or GNNs each time the MAS or backbone LLM changes. The high-level pipeline in **Figure 3** is one of the clearer parts of the paper: it conveys the coupling between dataset setup, attack surfaces, and the two defense stages. Even though some technical details remain underspecified, the figure helps the reader understand how topology-aware localization and message-level rectification are supposed to interact over rounds.

The experiments cover several axes of variation: three attack types, four backbone models, multiple rounds, several topologies, and ablations. This breadth is valuable. **Table 1** is especially important here. It shows that ARGUS improves both MT and TSR over attack-only in nearly every setting and often over Self-Check and G-Safeguard as well. For example, on GPT-4o under prompt injection, TSR rises from 56.25 to 73.75 with ARGUS, and average TSR rises from 67.07 to 76.96. Even if one questions some of the evaluation methodology, the empirical pattern is at least directionally consistent.

The temporal analysis is also informative. **Figure 5** supports the central narrative that misinformation accumulates over rounds in undefended MAS, while ARGUS tends to suppress this growth. I appreciated that the authors did not only report endpoint metrics. Showing per-round MT trends is much more diagnostic for a propagation-focused claim.

The ablation in **Table 2** is another positive point. Removing dynamic localization or multi-turn correction noticeably hurts performance, which suggests the method is not merely benefiting from the presence of an extra agent. The “w/ Ground Truth” row is also a sensible upper-bound style sanity check.

## Weaknesses
1. **The evaluation protocol relies heavily on an LLM judge, but the scoring procedure is too underspecified for the central claims being made.**  
   The core metrics in **Equation (1)**, MT and TSR, both depend on `Score(O_k, g)` produced by an LLM judge, yet the main paper does not adequately specify the prompt, calibration, variance, or robustness of this judge. On Page 4 the paper says the score is in `[0,10]` and TSR is thresholded by $\theta_m$, but the actual threshold selection, sensitivity of conclusions to that threshold, and inter-run variability of the judge are not established in the main text. This matters because both headline contributions, “toxicity reduction” and “task success improvement,” are mediated entirely by this evaluator. If the judge is noisy or biased toward style rather than factual correctness, the central empirical claims weaken substantially. At minimum, the paper should report threshold sensitivity and some judge agreement study against human annotations on a subset.

2. **Several key equations in Section 4 are either ambiguous, inconsistent, or incomplete, which makes the method harder to verify than it should be.**  
   There are multiple issues here:
   - In **Equation (3)** on Page 5, the notation is inconsistent: the argmax is written over $e_i \in \mathcal{E}$ while the scored object is $\textsf{Score}_{topo}(e_{i\cdot})$. It should be explicit that this is over outgoing edges of source node $a_i$, something like  
     $$e_i^* = \arg\max_{e \in \{e_{ij} : (a_i,a_j)\in\mathcal E\}} \textsf{Score}_{topo}(e).$$
   - In **Equations (5) and (6)** on Page 6, the notation oscillates between $V'_{mis}$ and $V'_{goal}$. This is not a cosmetic issue, because these equations define the core semantic relevance score used for adaptive re-localization.
   - **Equation (6)** is awkwardly formed:  
     $$\texttt{Rel}(m,V'_{goal})=\max_{s\in m}\left\{\{0\}\cup \mathcal{S}(s,V'_{goal})\right\}\ \text{s.t.}\ \mathcal{S}(s,V'_{goal})\ge \theta_{sim}.$$  
     Since $\mathcal{S}(s,V'_{goal})$ is a scalar, the set expression is malformed. A cleaner definition would be  
     $$\texttt{Rel}(m,V')=\max_{s\in m}\max\{0,\mathcal S(s,V')\cdot \mathbf{1}[\mathcal S(s,V')\ge \theta_{sim}]\}.$$
   - **Equation (8)** says the frequency score for edge $e$ in round $r-1$ is $\texttt{count}(m_e(r))$, which appears off by one relative to the surrounding text.
   - Most importantly, the paper introduces a weighted sum $\texttt{Score}^r(e)$ using topological, relevance, and frequency terms, and later the appendix gives $\alpha,\beta,\gamma$, but the actual weighted-sum equation is missing from the main paper. Since adaptive localization is the main algorithmic novelty, omitting its explicit formula in the main text is a serious exposition problem.

3. **The defense is heuristic and potentially brittle against adaptive attackers, but the experimental design does not really stress-test that brittleness.**  
   ARGUS monitors only top-$k$ channels, with $k=N-1$ in the appendix. That makes the method vulnerable in principle to attackers that deliberately route misinformation through low-centrality or low-relevance edges until late in the interaction. The initial localization in Section 4.1.1 depends on edge betweenness centrality before any message content is observed, and the later adaptive re-localization depends on previously inferred misinformation goals. An attacker who varies phrasing, spreads weaker misinformation over multiple edges, or delays the strongest misinformation until after localization could plausibly evade the mechanism. This is not a hypothetical nitpick, because the paper’s own formulation in **Figure 3** and Section 4 assumes a fairly structured propagation pattern that aligns with monitored channels. The current experiments, however, inject misinformation once at the initial round and do not probe adaptive or evasive strategies. That leaves a significant gap between the proposed mechanism and the threat model suggested by the paper’s ambitions.

4. **The benchmark is interesting, but the dataset construction and validation are still too light in the main paper for a benchmark contribution.**  
   On Page 3 the dataset construction is summarized as seed examples, prompting, and manual filtering. On Page 18 there is category distribution, and **Figure 9** provides one example. However, the main paper does not provide enough information about annotation consistency, quality control, diversity of misinformation types, task difficulty calibration, or leakage risks from using GPT-4o to help synthesize benchmark entries. For a dataset paper, 108 tasks is also relatively small, so quality matters even more. The example in Figure 9 is useful, but one example cannot establish that the benchmark robustly covers the intended threat landscape. It would strengthen the paper to include in the main text at least a compact manual validation protocol and statistics on how often humans judged the misinformation arguments as plausible but false.

5. **The baseline selection is somewhat narrow, and the comparisons may not fully isolate what ARGUS is buying.**  
   The paper compares mainly against Self-Check and G-Safeguard. Those are reasonable starting points, but they are not enough to convincingly establish that ARGUS is the right way to use an additional monitoring agent. A stronger comparison would include simpler targeted interventions closer to the proposed design, such as: a random-edge monitoring agent, a centrality-only monitor without goal inference, a semantic-only monitor without topology, or a “rewrite every message” corrective agent. **Table 2** partially addresses component contribution, but it is still not a substitute for external baselines that match the deployment budget more closely. As written, one could argue that part of the gain comes simply from adding extra scrutiny and extra generated text rather than from the specific localization logic.

6. **Some empirical claims are stronger than what the presented evidence supports.**  
   The paper repeatedly uses broad language such as “robust defensive capabilities,” “high generalization,” and “successfully identified the misinformation's guiding direction with high accuracy.” Yet the evidence is still restricted to one synthetic benchmark, one MAS platform, and one LLM judge. **Figure 4** shows reasonably high goal-identification accuracy, but the setup for that accuracy is not sufficiently detailed in the main paper: what counts as a correct inferred misleading goal, how close paraphrases are treated, and whether the same judge is used again. Similarly, **Figure 6** shows transfer across five topologies, which is useful, but all of these are relatively stylized communication patterns under the authors’ own MAS implementation. The claims should be toned down or backed with stronger cross-platform evidence.

7. **Presentation quality is uneven, with several lapses that matter for scientific readability.**  
   There are repeated terminology inconsistencies such as “MISINFOTask,” “MisinfoTask,” and “MisinFoTask.” Figure captions and text occasionally overstate what is shown. **Figure 1** is visually intuitive, but the sentence “the latter’s characteristic enables it to readily circumvent conventional detection mechanisms” is confusing because the antecedent of “latter” in that paragraph is not always unambiguous. On Page 5, **Figure 3** labels the left side as “ARGUS dataset,” which seems to be a mistake for MISINFOTASK. Table formatting is also awkward. In **Table 1**, entries such as “4.54; 6.44” appear to encode means plus improvement deltas, but that format is nonstandard and initially hard to parse. The table becomes readable only after cross-checking surrounding text. These are fixable issues, but they add friction.

8. **The paper does not discuss defense cost and utility trade-offs in the main paper, despite this being important for a training-free online defense.**  
   The appendix cost table shows ARGUS adds API cost over both vanilla and attack-only settings. That is not surprising, but the main text barely quantifies the operational tax. This matters because the proposed method inserts a corrective agent into the communication process over multiple rounds, which may alter collaboration patterns and latency. A defense for MAS should be judged not only by corrected MT/TSR but also by overhead and interference with benign communication. The topology and round analyses in **Figures 5 and 6** would have been stronger if accompanied by explicit efficiency or latency measurements in the main text.

## Questions
1. For **Equation (1)**, what exact threshold $\theta_m$ is used to convert the LLM-judge score into TSR, and how sensitive are the headline improvements in **Table 1** to that threshold? A rebuttal with a sensitivity plot or a few alternate thresholds would increase my confidence.

2. Please explicitly provide the missing weighted-sum equation for adaptive localization in the main text, namely something of the form  
   $$\texttt{Score}^r(e)=\alpha\,\widetilde{\texttt{Score}}_{topo}(e)+\beta\,\widetilde{\texttt{Score}}_{freq}^{\,r-1}(e)+\gamma\,\widetilde{\texttt{Score}}_{rel}(e),$$
   and clarify whether each component is normalized before combination. Without normalization, the relative magnitudes of frequency and cosine similarity terms could dominate unpredictably.

3. In **Figure 4**, how is “accuracy of identifying misleading goals” defined? Is this exact-match against a canonical goal string, semantic match using another LLM judge, or human evaluation? If semantic matching is used, please specify the metric and threshold.

4. Can the authors provide a stronger budget-matched baseline, for example random-edge monitoring, topology-only monitoring, or semantic-only monitoring? This would help isolate whether ARGUS’s gains come from the particular localization strategy rather than simply adding an intervention agent.

5. How does ARGUS behave under a more adaptive attacker that spreads misinformation across multiple low-centrality edges, delays misinformation until later rounds, or paraphrases goals to avoid cosine-similarity based matching in **Equations (5)-(7)**? Even a small controlled experiment here could materially change my assessment.

6. For MISINFOTASK, can the authors clarify how many task instances were manually verified end-to-end, whether multiple annotators were involved, and whether there is any human validation that the injected arguments are genuinely persuasive while still false? This would strengthen the benchmark contribution substantially.

7. In **Table 1**, please clarify the meaning of the semicolon-separated numbers in baseline and ARGUS rows. My reading is “raw value; improvement over attack-only,” but the table caption should state this explicitly.

## Flag For Ethics Review
- Yes, Potentially harmful insights, methodologies and applications  
- Yes, Responsible research practice (e.g., human subjects, data release)

## Details Of Ethics Concerns
The paper studies how to inject misinformation into multi-agent systems through prompts, RAG stores, and tools, and releases a benchmark with plausible misleading arguments. This is defensible as safety research, but it still creates dual-use risk by operationalizing attack surfaces and supplying structured misinformation artifacts. The ethics statement on Page 11 acknowledges research-only usage, which is good, but the paper would benefit from more concrete safeguards around dataset release, attack prompt release, and misuse boundaries.

On responsible research practice, MISINFOTASK is partially LLM-generated and manually filtered, but the paper gives limited detail in the main text about curation standards, annotator process, or release controls. Since the benchmark contains crafted misinformation arguments designed to be persuasive, release design matters.

## Soundness Rating
3: good. The empirical study is reasonably broad and the main claims are directionally supported, but the evaluation depends too heavily on underspecified LLM judging and the method section has notable mathematical and algorithmic ambiguities.

## Presentation Rating
2: fair. The overall story is understandable and figures like **Figure 3** help, but notation inconsistencies, omitted formulas, table formatting issues, and imprecise wording materially weaken clarity.

## Contribution Rating
3: good. The problem framing is important, the benchmark is useful, and the proposed defense is practically motivated, though the novelty is more in the combination and evaluation setup than in a deeply grounded new methodology.

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected. The paper addresses a relevant and underexplored safety problem, introduces a potentially useful benchmark, and presents a practically deployable defense with encouraging results. However, the current version is held back by underspecified evaluation, heuristic methodology, and several technical clarity issues in the core equations and algorithm description.

## Reviewer Confidence
4: confident. I am confident in the overall assessment and checked the technical and experimental details with care, though some implementation specifics are missing from the main paper and limit absolute certainty.