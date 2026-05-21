---
job_id: f0a0278c-9e44-4dbd-99c0-423a00d69a3e
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: UESTP6dR1K.pdf
paper: Automated Stateful Specialization for Adaptive Agent Systems
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, combining reinforcement learning style control, automated agent design, lifelong/stateful adaptation, and LAGENT-like systems for reasoning and coding benchmarks.

## Minimum Quality
Pass ✅. The submission contains the expected research components, including abstract, introduction/related work, methodology, experiments/results, discussion, and conclusion, and it presents a coherent empirical study with nontrivial methodological content. There are important clarity and rigor issues, but not of the desk-reject kind.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden instructions, suspicious embedded prompts targeting reviewers, or other manipulative content in the provided paper text and figures.

# Expected Review Outcome:
## Summary
This paper proposes ASPEC, a framework for automated design of stateful specialist agent systems. The method combines an offline discovery phase that evolves specialist operators, a cultivation phase that equips selected specialists with persistent memory through reflection, and an online "retain-then-escalate" meta-controller that decides whether to reuse the current architecture or invoke a more expensive architect to redesign it.

Empirically, the paper evaluates ASPEC on five benchmarks spanning math, QA, and code generation, and reports strong gains on expert-oriented tasks such as GPQA and SciCode, along with ablations on specialists, memory, and control policies.

## Strengths
1. The paper tackles a meaningful gap between static workflow search and fully per-query workflow generation. The framing, namely persistent specialists that can accumulate experience while still allowing query-level adaptation, is interesting and relevant to current automated agent design work.

2. The method is reasonably well modularized. The decomposition into specialist discovery, specialist cultivation, and a lightweight meta-controller is conceptually clean, and **Figure 1** helps communicate these three components effectively. In particular, the separation between the expensive architect and the cheaper controller is a useful systems design choice rather than a vague "agent does everything" story.

3. The empirical coverage is broader than many agent papers. **Table 1** includes five benchmarks across multiple domains and compares against hand-designed agents, multi-agent baselines, specialization methods, and automated architecture-search methods. On the face of the reported numbers, ASPEC is competitive across the board and strongest on GPQA and SciCode, which are the most persuasive tasks for the paper's specialization narrative.

4. The efficiency angle is a genuine positive. **Table 2** is one of the more informative parts of the paper because it goes beyond pure accuracy and compares training/inference tokens, cost, and wall-clock time. If these numbers are reliable, the result that ASPEC outperforms AFlow and MaAS on GPQA while using much lower training cost is practically meaningful.

5. The ablations are directionally useful. The left panel of **Figure 6** and the accompanying table show that removing specialist operators hurts both performance and cost, and removing the meta-controller preserves accuracy while increasing cost substantially. This supports the claim that both stateful specialists and the retain/resample mechanism matter, even if the exact attribution is not fully nailed down.

6. I appreciated the qualitative case study. **Figure 4** makes the specialist concept more concrete by showing lineage, the learned prompt, and example memory contents for a physics specialist. That is helpful for understanding what "specialization" actually means in this framework, instead of leaving it as an abstract label.

7. The paper is well motivated and generally readable. The introduction clearly positions the work between task-level architecture search and query-level adaptation, and the benchmark choice aligns with the paper's intended use case of expert reasoning.

## Weaknesses
1. The main methodological claims lean heavily on a formal RL/HRL framing, but the actual optimization problem is under-specified in the main paper.  
   On **Pages 3-4**, the paper defines the architect objective in **Equation 2** and the meta-controller objective in **Equation 4**, but the operational details needed to interpret these equations are missing or deferred. For example, the utility term \(U_t = U(\mathcal{G}_t; q_t, a_t)\) is introduced on **Page 3**, but the text says it is "with respect to the oracle \(a_t\)", which is confusing because \(a_t\) is also used for the controller action later. This is already a notation collision. More importantly, the paper never gives a concrete definition of \(U_t\) in the main text, nor how it is estimated for different tasks, nor how it interacts with delayed effects from retention. As written, **Equation 2** looks like a Bellman-style objective, but the architect itself is not trained with an RL algorithm in the main paper; it is an in-context LLM process. That makes the formalism feel aspirational rather than a faithful specification of the implemented method. This matters because the paper's central conceptual contribution is precisely the coordination between controller and architect.

2. The reward for the meta-controller is not fully specified in the main paper, and even the appendix leaves it only "conceptual."  
   In **Appendix E, Equation 7**, the reward is
   \[
   R_t = s_t \cdot w(a_t, \mathrm{sim}(q_t,\mathcal{G}_{t-1})) - \lambda C_t,
   \]
   but the weighting function \(w(\cdot,\cdot)\) is not defined. The text only says it "can be expressed conceptually" and gives monotonicity examples. That is not enough for reproducibility or for judging whether the controller is really learning the intended retain-versus-resample tradeoff. Since the ablation against heuristic gating is a major empirical claim in **Figure 6**, the exact reward shaping is not a minor detail. Different choices of \(w\) could make the controller trivially imitate a cosine-threshold policy or strongly bias toward resampling. At minimum, the paper should provide the exact formula, scaling, normalization of similarity, and the value of \(\lambda\) used in practice.

3. There are mathematical and notation issues that make the formal description harder to trust than it should be.  
   A few examples:
   - In **Equation 3** on **Page 4**, the state is \(s_t = (e_q(q_t), e_g(\mathcal{G}_{t-1}))\), but the graph encoder is described as a "bag-of-operators" with query-conditioned attention weights. The actual formula for those attention weights is omitted. Since this representation is central to the controller, the paper should state something like
     \[
     \alpha_i = \frac{\exp(\langle e_q(q_t), e_o(o_i)\rangle / \tau)}{\sum_j \exp(\langle e_q(q_t), e_o(o_j)\rangle / \tau)}, \quad
     e_g(\mathcal{G}) = \sum_i \alpha_i e_o(o_i),
     \]
     or whatever the implemented version is.
   - The specialist selection objective in **Section 3.1**, shown near **Figure 4** and formalized in **Equation 5**, is not properly presented in the main paper text. The equation is visually fragmented in the provided paper, and the diversity term appears as a cluster-based max aggregation, but key details are missing, such as whether clustering is over prompt embeddings, operator embeddings, or performance-weighted embeddings, and whether the optimization is solved greedily or exactly. Since the top-\(k\) cultivated specialists are determined by this criterion, the omission is consequential.
   - In **Algorithm 1** on **Page 19**, experience is stored as \((q_t,\mathcal{G}_t,S_t,C_t)\), while the body previously defines \(U_t\), not \(S_t\). In **Algorithm 2**, both \(p_t\) and \(P_t\) appear. These inconsistencies may look small, but in a paper already leaning on formalism, they accumulate and make it difficult to map equations to the actual procedure.

4. The empirical protocol is not fully convincing because model selection and tuning are not clearly separated from test evaluation.  
   **Appendix F, Table 3** states a train:test ratio of \(1:4\), with extremely small training sets, for example 89 training samples on GPQA and 33 on HumanEval. However, there is no validation split described for choosing the specialist pool size \(k\), sliding window \(m\), controller hyperparameters, reward weights, or prompt-generation settings. The sensitivity analysis in **Figure 6** suggests these choices matter. Without a clean validation protocol, it is hard to know whether the reported best settings were indirectly tuned on test performance. This does not necessarily invalidate the whole paper, but it weakens confidence in the magnitude of the gains, especially since many benchmarks have a few hundred test instances.

5. The gains, while promising, are not backed by uncertainty estimates or repeated-run statistics in the main benchmark table.  
   **Table 1** reports single numbers, often with small margins, for example ASPEC 62.8 vs EvoAgent 61.5 vs AFlow 61.3 on GPQA, and ASPEC 91.4 vs MaAS 91.6 on HumanEval. For LLM-agent systems with stochasticity in prompting, architectural sampling, and execution, these differences may or may not be robust. The paper only reports means over 4 runs in the sensitivity plots of **Figure 6**, but not for the headline comparisons in **Table 1** or **Table 2**. This matters because the central contribution is an adaptive lifecycle, not a deterministic algorithm, so variance should be expected. Confidence intervals or at least multi-seed averages would substantially increase trust.

6. The attribution of improvements to "stateful specialization" versus other ingredients remains somewhat blurry.  
   The component ablations in **Figure 6** are useful, but they do not cleanly isolate whether gains come from persistence of the architecture, prompt evolution, memory injection, or simply having more chances to search over architectures offline. For instance, "ASPEC w/o specialist memory" still scores 61.4 on GPQA versus 62.8 full ASPEC, while "ASPEC w/o specialist operators" drops to 57.4. This suggests that most of the gain may come from better prompt-specialized operators, not necessarily from the stateful memory accumulation emphasized in the title and abstract. Similarly, "ASPEC w/o meta-controller" is 62.7, essentially tied with the full model in accuracy but more expensive. That supports an efficiency claim for the controller, but not a strong effectiveness claim. The paper would be stronger with a sharper decomposition: persistent specialists without cultivation, cultivation without retention, retention without architecture redesign, and so on.

7. Some claims in the discussion overreach the evidence shown in the figures.  
   On **Page 7**, the text states that in the cross-benchmark analysis in **Figure 5** the ONLYSPEC configuration "matches or even slightly exceeds" the full system, implying transferred "T-shaped" reasoning strategies. But the figure shown in the main paper is quite limited and does not provide error bars, sample sizes, or benchmark-by-benchmark details sufficient to support a broad transferability interpretation. Similarly, the convergence claims around **Figure 7** on **Page 9** are qualitative. The visual clustering of prompt embeddings is suggestive, but not enough to conclude robust convergence behavior of the discovery process. A quantitative cluster agreement metric across runs would be more appropriate than relying on a scatter plot.

8. The comparison set is good overall, but some baselines appear to receive less than fully comparable treatment, and the setup description leaves room for concern.  
   In **Appendix B**, some baselines are said to use direct implementations from original repositories, while others are reimplemented or adapted to Gemini 2.0 Flash "for homogeneity." That is understandable, but the paper does not discuss whether those methods were tuned for this different backbone, or whether architecture-search methods like AFlow and MaAS were given the same search budget, prompt budget, and candidate operator space as ASPEC. Since **Table 2** makes strong efficiency claims, comparable budget accounting is essential. Otherwise, a lower cost may partly reflect a lighter search protocol rather than a better method.

9. The paper argues for a hierarchical RL interpretation, but the empirical evaluation of the controller does not actually test generalization in an RL sense.  
   The controller state in **Equation 3** depends only on the current query embedding and an embedding of the previous architecture. There is no explicit memory of longer history, despite the long-term specialization story. In practice this looks more like a learned gating heuristic than a rich MDP policy. That is not inherently a problem, but then the paper should tone down the HRL framing. The "rationality analysis" with confusion matrices in **Figure 8** is interesting, yet it compares against an LLM-as-gate proxy rather than against a true ground-truth policy. So the analysis is really about agreement with another heuristic, not policy optimality.

10. The exposition is decent at the narrative level, but some key implementation details are pushed too far out of the main paper.  
    The specialist prompts, judge prompts, and architect prompt templates in **Appendix G** are clearly important to the method. In a system where specialist identities and directives are themselves the "genetic material," these prompts are not incidental. The main paper currently reads as if the system is more algorithmically specified than it really is. For this kind of LLM-based agent work, prompt design is part of the method, and the reader should not need the appendix to understand core decisions.

## Questions
1. Please give the exact instantiated reward function for the meta-controller used in training, not just the conceptual form in **Equation 7**. What is the explicit formula for \(w(a_t,\mathrm{sim})\), what similarity normalization is used, and what is \(\lambda\)? This would materially increase my confidence in the controller results.

2. Please clarify the notation and implementation mismatch around **Equations 1-4** and **Algorithms 1-2**. In particular:
   - what exactly is \(U_t\),
   - why does **Equation 2** include \(V_{\pi_\theta}(s_{t+1})\) if the architect is not trained with a Bellman backup,
   - and are \(S_t\) / \(U_t\) / \(p_t\) / \(P_t\) simply typos or different quantities?

3. How were \(k\), \(m\), reward coefficients, and other hyperparameters selected? Was there a validation split separate from the reported test set? If not, please explain the tuning protocol and whether any test-set feedback influenced parameter choices.

4. Can the authors report multi-run means and standard deviations for **Table 1** and **Table 2**, especially on GPQA and SciCode? This is important because several claimed wins are within 1-2 points of strong baselines.

5. Can the authors disentangle the effect of statefulness more directly? For example, a comparison between:
   - discovered specialists without memory,
   - memory-enabled specialists without retention,
   - retained specialists with frozen prompts,
   - and dynamic per-query search with access to the same cultivated memories,
   would help establish what part of the gain truly comes from persistent specialization.

6. For the efficiency comparison in **Table 2**, were all methods run under matched candidate operator spaces, search budgets, and prompt/model settings? A more explicit accounting would help ensure the cost claims are apples-to-apples.

7. For the convergence discussion around **Figure 7**, can the authors provide a quantitative measure of across-run consistency, such as cluster purity, adjusted Rand index, or nearest-neighbor overlap of discovered specialists? The current evidence is visually suggestive but not yet rigorous.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
The paper mentions in **Section 6** that specialist memory cultivation could amplify training biases. That is a reasonable limitation to note, but based on the presented work, which evaluates on public academic benchmarks and does not include deployment on human-facing or sensitive applications, I do not see an ethics issue requiring escalation at review time.

## Soundness Rating
2: fair. The core idea is plausible and supported by a useful empirical study, but several technical components, especially the controller reward and formal RL framing, are under-specified, and the experimental protocol lacks enough detail to fully validate the strongest claims.

## Presentation Rating
3: good. The paper is generally readable, motivated, and reasonably structured, with helpful figures such as **Figures 1, 4, and 6**. However, important mathematical and algorithmic details are either inconsistent or deferred, which limits clarity.

## Contribution Rating
3: good. The paper makes a worthwhile contribution by pushing automated agent design toward persistent specialization with adaptive reuse, and the GPQA/SciCode results are interesting. The contribution would be stronger with cleaner attribution and more rigorous specification.

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected. The paper has a compelling problem formulation, a sensible systems design, and promising empirical results, especially on expert benchmarks and efficiency. However, the formalization and evaluation are not yet as tight as the paper's confidence level suggests, so my recommendation is positive but cautious rather than enthusiastic.

## Reviewer Confidence
4: confident. I am comfortable assessing the agent-design, LLM systems, and experimental aspects, and I checked the equations/algorithms closely, though some implementation-specific details remain unclear from the main paper.