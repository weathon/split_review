---
job_id: 7cbf30a4-0919-4052-844e-00c78dea4460
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: 1E4Bltg6Xb.pdf
paper: Learning Dynamics Feature Representation via Policy Attention for Dynamic Path Planning in Urban Road Networks
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope through reinforcement learning, learning on graphs, representation learning for planning, and an autonomy/path-planning application.

## Minimum Quality
Pass ✅. The paper includes the expected scientific components, namely abstract, introduction, related work, methodology, experiments, results, and conclusion, and it presents a coherent empirical study. While I have substantial concerns about novelty, theoretical support, and experimental rigor, these do not rise to the level of a desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, suspicious reviewer-directed instructions, or other manipulative content in the provided paper text or figures.

# Expected Review Outcome:
## Summary
This paper studies state representation for reinforcement learning in dynamic path planning on urban road networks. The proposed Dynamics Feature Representation (DFR) framework progressively compresses full graph dynamics into a task-relevant subgraph using a pre-trained distance-based “policy attention” module, and then into node-centered local features using an $n$-hop neighborhood intersection. The paper evaluates DFR with DQN, PPO, and GCN+DQN on three OpenStreetMap-derived urban graphs, reporting better planning quality, smaller feature dimensionality, and faster planning time than using all dynamic features.

## Strengths
The paper addresses a relevant problem. In dynamic path planning, the state design question is indeed central, and the paper correctly highlights the tension between using the whole graph dynamics and using overly myopic local observations. This is a reasonable problem formulation for RL-based planning on large urban networks.

The proposed decomposition is intuitive and easy to understand. The combination of task-level pruning followed by agent-centric local extraction is conceptually clean. In particular, **Figure 3** helps communicate the intended pipeline well: it makes clear how the static shortest-path policy is used to form a task-relevant subgraph and how the $n$-hop extraction further narrows the representation around the current node. Even though I have concerns about the assumptions behind this design, the figure itself is useful and supports the paper’s main methodological narrative.

The empirical direction is practically motivated. Testing on three different urban graphs, shown in **Figure 4**, is better than demonstrating the method on a single toy map. The paper also evaluates DFR with multiple RL backbones rather than coupling it to just one algorithm, which is helpful for showing that the idea is intended as a representation layer rather than a bespoke learner.

The ablation section is one of the more useful parts of the paper. **Figure 6** gives a concrete view of how the hyperparameters $k$ and $n$ affect GAP, success rate, and compactness. The heatmaps make the trade-off visible, and the bottom-row training curves suggest that neighborhood size does affect learning dynamics, not just final metrics.

The paper claims substantial efficiency gains, and this is an important practical angle. The discussion around planning time and feature compactness is meaningful because the whole motivation of DFR is to reduce online computational burden. Even though I would have preferred a clearer numerical presentation than the current figure-heavy format, this aspect is aligned with the paper’s stated goals.

## Weaknesses
My main concern is that the central scientific claim is stronger than the evidence supports. The paper repeatedly argues that DFR yields a state representation that is “sufficient,” “Markovian,” or preserves the optimal policy approximately, see **Equations (6), (7), and (8)** on Pages 5–6. However, these are stated as desiderata rather than established results. There is no theorem, no bound, and not even a precise definition of the approximation relation in
\[
\pi^*(v^t,v_g;W_t') \approx \pi^*(v^t,v_g;W_t), \quad
\pi^*(v^t,v_g;W_t'') \approx \pi^*(v^t,v_g;W_t'), \quad
\pi^*(v^t,v_g;W_t'') \approx \pi^*(v^t,v_g;\mathbf W_{:T}).
\]
What is the metric on policies here, action disagreement, value loss, regret, or something else? Without that, the PSR-based discussion on Page 6 is more motivational than theoretical. In fact, the text says this grounding “guarantees” compactness and sufficiency, but the paper does not prove such a guarantee. This matters because the method’s main selling point is exactly that the compressed state remains decision-sufficient. Right now, that is asserted, not demonstrated.

Relatedly, several mathematical and modeling details are inconsistent or overstated. In **Equation (1)** on Page 3, the path is defined as $p=\langle v_{(0)},\dots,v_{(n)}\rangle$, but the summation is written as $\sum_{k=1} w(p_k,p_{k+1};t_k)$, which appears off by one relative to the path indexing and should presumably run over edges from $k=0$ to $n-1$. In Section 3.2 on Page 4, the MDP is called “deterministic,” yet a full stochastic transition kernel $T(s_{t+1}\mid s_t,a_t)$ is introduced and used in **Equations (3) and (4)**. The action space is declared as $\mathcal A \subseteq \mathbb R^m$ but then instantiated as a discrete set $\{0,1,\dots,n_a\}$, which is inconsistent. There is also notation drift between $v^t$ and $v_a^t$. These are not merely cosmetic issues, because they reduce confidence that the formal setup was carefully checked. I was also unconvinced by the statement on Page 4 that using classic DRL algorithms allows the optimal value function $V^*(s)$ to be “uniquely determined” and that DQN estimates “until convergence to $V^*(s)$.” For nonlinear function approximation, that is far too strong.

A third issue is the justification for the policy-attention mechanism itself. The key design choice in Section 4.3 is to build the task-relevant subgraph from the top-$k$ shortest paths under a static distance-only policy $\pi_d^*$. The paper argues that distance is a fundamental constraint, so those paths retain critical edges for dynamic planning. That is plausible as a heuristic, but the argument is weak for a dynamic travel-time objective. In congested networks, the time-optimal route may deliberately deviate far from the distance-optimal paths, especially under incidents or temporally localized congestion. The paper does not provide evidence that the dynamic optimum is likely to lie within or near the top-$k$ static shortest-distance paths. This matters directly to scientific validity, because if the oracle route frequently leaves the selected subgraph, then DFR is not just compact, it is lossy in a way that can systematically bias the policy. The ablation in **Figure 6** partly explores sensitivity to $k$, but it does not answer the more basic coverage question: how often does the dynamic shortest-time path remain inside the policy-attention subgraph as a function of $k$?

The empirical evaluation is also narrower than it needs to be to support the paper’s broader claims. The paper compares each RL algorithm using DFR versus using all dynamics, but it does not compare against simpler or more targeted representation baselines. For example, there is no local-only baseline with matched dimensionality, no shortest-path corridor heuristic without RL pretraining, no random subgraph baseline, and no graph-attention alternative that would test whether the gains come from the specific DFR construction or from any strong dimensionality reduction. The inclusion of GCN+DQN is helpful, but it is still another RL backbone, not a competing state abstraction strategy. Because the central contribution is representation design rather than a new RL optimizer, the baseline set should be built around alternative representations, not only around alternative RL algorithms.

The experimental protocol is under-specified in several important ways. On Pages 7–8, the paper says each episode corresponds to a new scenario and that source and goal nodes are randomly sampled, but it is not clear how training, validation, and test scenarios are partitioned. Are the reported results measured on held-out source-goal pairs, held-out dynamic sequences, or the same distribution used during training? How were $k$ and $n$ selected for the main experiments outside the ablation? Was there any validation split, or were these choices made after inspecting test performance? These details matter because, in route-planning tasks on fixed graphs, leakage across train and test distributions can make generalization look better than it is. I am not accusing the authors of leakage, but the current writeup is too vague to rule it out.

The results presentation is weaker than the paper needs. The main quantitative comparison in **Figure 5** uses triangle plots over $1-\mathrm{GAP}$, SR, and $1-\mathrm{CR}$, with the triangle area used as an overall summary. This is visually catchy, but scientifically it is not ideal. Triangle area is not a standard metric, the axes are on different semantic scales, and the figure makes it hard to read exact numerical differences. More importantly, the paper does not provide a conventional results table with the actual numbers for all methods across all datasets, nor does it report variability across random seeds. Since the paper’s claims are about “significant improvement” and “remarkable acceleration,” the absence of a clear tabular summary with means and standard deviations is a real issue. **Figure 5** suggests DFR helps, but the reader should not have to reverse-engineer exact gains from radar-like shapes. The same criticism applies to the planning-time claims on Page 9, which are given in prose without a table that separates online planning cost, feature extraction cost, and backbone-specific overhead.

Finally, some figures are less informative than the text assumes. **Figure 1** is supposed to illustrate the correspondence between path nodes and the dynamics sequence, but it mainly provides a timeline cartoon and does not clarify the key modeling ambiguity of whether edge costs are sampled at departure time, arrival time, or some other synchronization rule. That ambiguity feeds directly into **Equation (1)** and the DPP objective. **Figure 2** gives a high-level schematic of policy interaction with dynamics, but it does not actually explain what feature tensor is input to the policy network in the AD or DFR settings, which is an important omission for reproducibility.

## Questions
1. Please make the approximation claims in **Equations (6)–(8)** precise. What notion of $\approx$ is intended, value difference, policy disagreement, suboptimality gap, or something else? If there is no formal guarantee, I recommend softening the wording substantially and reframing these equations as design goals rather than established properties.

2. Can you quantify the coverage of the policy-attention subgraph? Specifically, for each $k$, what fraction of the oracle dynamic-Dijkstra paths lie entirely within the selected subgraph $G'$? This would directly test whether the distance-based preselection is retaining the right parts of the graph.

3. Please clarify the train/validation/test protocol. Are source-goal pairs, dynamic sequences, and episodes separated across splits? How were $k$ and $n$ chosen for the main experiments? A precise answer here would increase my confidence in the empirical claims.

4. Can you compare DFR against simpler representation baselines with similar dimensionality, such as local $n$-hop features without policy attention, shortest-path corridor heuristics without RL pretraining, or randomly sampled subgraphs of matched size? Right now the empirical evidence does not isolate whether DFR itself is responsible for the gains.

5. Please provide a standard numeric results table for each region and method, including Mean GAP, SR, CR, PT, and variance across multiple seeds. This is important because **Figure 5** is too aggregate to judge practical effect sizes reliably.

6. In Section 3.2, do you really intend the environment to be deterministic? If so, why use stochastic transition notation throughout? If not, please correct the formulation and also moderate the claims about DQN converging to the unique $V^*$.

7. For **Equation (1)**, please clarify the indexing and the exact time semantics: is the cost of edge $(p_k,p_{k+1})$ evaluated at departure time $t_k$, and how is $t_k$ determined from prior traversal times?

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No ethics concerns that require escalation are apparent from the paper. The work uses road-network data and simulated dynamic costs, and I did not identify human-subject, privacy, or safety claims that require special review based on the main text.

## Soundness Rating
2: fair. The empirical direction is reasonable and the method is implementable, but several technical claims are overstated, the formalism has inconsistencies, and the experiments do not yet support the stronger sufficiency/Markov claims.

## Presentation Rating
3: good. The paper is generally readable and the high-level idea comes through, especially in **Figures 3 and 6**, but the formal exposition is sloppy in places and the quantitative presentation would benefit from standard tables and clearer protocol details.

## Contribution Rating
2: fair. The problem is worthwhile and the proposed combination is practical, but the conceptual novelty is moderate and the evidence does not yet establish a contribution strong enough for a clear ICLR accept.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted.

## Reviewer Confidence
4: confident. I am confident in my assessment, though not absolutely certain. The core RL/path-planning setup is within my expertise, and I checked the main equations, figures, and empirical claims carefully.