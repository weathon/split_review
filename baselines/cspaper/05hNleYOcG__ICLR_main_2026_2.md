---
job_id: 86094e9e-dcd9-48e5-b3cb-5d310a1e6d01
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: 05hNleYOcG.pdf
paper: PLAGUE: Plug-and-Play Framework for Lifelong Adaptive Generation of Multi-Turn Jailbreaks
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope through LLM safety, multi-turn red-teaming, lifelong learning, and agentic ML systems.

## Minimum Quality
Pass ✅. The paper contains the expected scientific sections, including Abstract, Introduction, Related Work, Method, Experimental Setup, Results/Discussion, Conclusion, and Ethics Statement; despite notable weaknesses in rigor and clarity, it clears the minimum bar for full review rather than desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not detect hidden prompts, suspicious reviewer-directed instructions, or other manipulative content in the provided paper text.

# Expected Review Outcome:
## Summary
This paper presents PLAGUE, a modular framework for generating multi-turn jailbreak attacks against black-box LLMs. The framework decomposes attack generation into three phases, Planner, Primer, and Finisher, and augments them with reflection, backtracking, conversation summarization, and a retrieval-based long-term memory of successful past strategies. The paper evaluates PLAGUE on HarmBench against several frontier target models and reports higher attack success rates than prior single-turn and multi-turn baselines under a six-query target-model budget.

## Strengths
The paper addresses a timely and important problem. Multi-turn jailbreaks are genuinely underexplored relative to single-turn attacks, and the focus on black-box, API-accessible models is practically relevant.

The modular framing is useful. Even if many ingredients are not individually new, organizing them into a Planner, Primer, and Finisher decomposition gives a reasonably clear lens for comparing prior attacks and for asking which components matter. **Figure 1** helps here, because it makes the pipeline concrete, especially the separation between long-term strategy retrieval, context-building in the Primer, and the final goal-conditioned Finisher. This figure does real explanatory work, rather than just decorating the method section.

The empirical evaluation is broad in terms of target models. **Table 2** includes OpenAI o3, o1, DeepSeek-R1, Claude Opus 4.1, and Llama 3.3 70B, which is a stronger spread than many papers in this space. The reported gains on difficult models such as o3 are substantial under the paper’s own evaluation pipeline, and the Claude-specific plug-and-play experiment in **Table 4** is a sensible demonstration of the claimed modularity.

The ablation trend is one of the stronger parts of the paper. **Table 3** shows a mostly monotonic improvement when adding backtracking, reflection, planning, and retrieval on top of GOAT. Even though I have concerns about the exact evaluation setup, this table at least attempts to localize where the gains come from, rather than relying entirely on headline numbers.

The paper also makes a reasonable effort to discuss efficiency, not just attack rate. **Figure 2** and **Table 5** attempt to relate performance to turn count and total model calls, which matters in practice for black-box red-teaming.

## Weaknesses
1. **The core novelty claim is overstated, and the paper reads more like a strong systems integration of existing attack components than a clearly new scientific advance.**  
   The method combines planning, reflection, backtracking, retrieval from memory, summarization, and existing finishers such as GOAT/Crescendo. The paper itself repeatedly emphasizes that prior methods “seamlessly fit” into the framework and that PLAGUE can “plug and play” these modules. That is not inherently bad, but it does make the contribution more incremental than the framing suggests. In **Section 3** and **Figure 1**, the architecture is mainly a composition of familiar agentic patterns, not a fundamentally new attack principle. This matters because the paper repeatedly positions itself as a state-of-the-art attack framework, but the scientific question then becomes: what exactly is new beyond engineering aggregation and prompt design? The current paper does not cleanly isolate that.

2. **The evaluation protocol is too entangled with the method’s own internal scorer, which makes the reported gains harder to trust as evidence of true attack superiority.**  
   A central issue is that the attack uses a rubric-based scorer during search, and final reporting also uses judge models with modified prompts. On **Page 5**, the method introduces a rubric scorer \(\mathbb{R}\) used for feedback. On **Page 7**, the paper states that the StrongReject score is computed using a “slightly modified version” of the original prompt. On **Page 7**, it also says the authors select the attempt among \(K\) attempts using the highest rubric score to calculate ASR@K. This creates a strong coupling between the optimization signal and the reported outcome. If the attack is effectively tuned to do well under this specific scorer, then improvements in **Table 2** may partly reflect better exploitation of the paper’s own evaluation pipeline rather than better attack quality in a broader sense. This is not a small technicality, because the entire headline claim rests on those numbers.

3. **The “apples-to-apples” baseline comparison is not actually apples-to-apples in several places.**  
   The baseline section on **Page 7** describes multiple modifications to prior methods: GOAT is run with a changed evaluation environment, without attack history, and with early stopping based on the paper’s rubric; ActorBreaker is reduced to \(K=2\) actors; Crescendo has explicit backtracking counts removed and maximum turns capped at six; AutoDAN-Turbo is reconfigured for six rounds and two lifelong iterations. Once so many baselines are altered, it becomes hard to know whether **Table 2** reflects fair comparative performance or comparative performance under a custom evaluation-and-search scaffold that is more naturally aligned with PLAGUE. This matters a lot because the strongest claims in the paper are relative claims. A weaker but fair comparison is preferable to a stronger but heavily customized one.

4. **Several algorithmic details are underspecified or inconsistent across the main text and pseudocode, which hurts reproducibility and technical clarity.**  
   There are multiple examples:
   - In **Section 3.4** on **Page 6**, the Primer threshold is described as \(7/10\), while in **Algorithm 2** on **Page 14** this appears as `if score >= 7.0`.
   - In **Section 3.5** on **Page 6**, the Finisher says scores lower than \(3/10\) trigger backtracking and success is declared above \(8/10\), but **Algorithm 3** on **Page 14** uses success `if score > 9.0` and a lower branch `else if score ≤ 2.0`. Those are not the same decision rules.
   - The text says evaluation during intermediate steps is handled by the rubric scorer \(\mathbb{R}\), but **Algorithm 2** and **Algorithm 3** use the “Evaluator model \(\mathbb{J}\)” for per-step scores, which conflicts with **Section 3.2** where \(\mathbb{R}\) is introduced specifically for reflection analysis.
   
   These are not cosmetic issues. The thresholds and which model performs scoring affect search dynamics and final attack rates, so discrepancies here directly affect soundness.

5. **The mathematical formulation is thin and in places imprecise.**  
   The ASR definition on **Page 5** is written as
   \[
   ASR(\mathbb{J})=\frac{1}{P}\sum_{i=1}^{P}\mathbb{J}(p_i,\mathbb{MT}_i).
   \]
   This only makes sense if \(\mathbb{J}\) outputs a scalar score in a consistent range, but the paper uses both binary-ASR and StrongReject-style continuous scores. The notation collapses these distinct settings into one undefined functional form. More importantly, on **Page 7**, the paper defines \(ASR@K\) by selecting “the attempt from the \(K\) turns that receives the highest score from the rubric scorer,” which is not standard ASR but a best-of-\(K\) judged-success statistic. That is closer to a search-with-reranking metric than a plain attack success rate, and the notation should say so explicitly.

   There is also a concrete formula issue in **Equation (1)** on **Page 23**:
   \[
   \text{Diversity}_{\text{Embedding}}=1-\frac{1}{\binom{|S_p|}{2}}\sum_{x_i,x_j\in S_p,i>j}\frac{\phi(x_i)\cdot\phi(x_j)}{||\phi(x_i)||^{2}||\phi(x_j)||^{2}}.
   \]
   If this is meant to be cosine similarity, the denominator should be \( \|\phi(x_i)\|\,\|\phi(x_j)\| \), not the product of squared norms. As written, the similarity term is not cosine similarity and changes scale in a way that depends on embedding norms. Since **Figure 3** relies on this diversity measure, the metric definition should be corrected.

6. **The retrieval and lifelong-learning component is not convincingly validated as “lifelong learning” rather than a small retrieval heuristic.**  
   The memory bank \(\mathbb{R}^{\{+\}}\) stores successful strategies indexed by goal embeddings, with at most two retrieved examples and a similarity threshold of 0.6, as described in **Section 3.3.1** on **Pages 5–6**. That is retrieval-augmented prompting, but calling this “lifelong learning” is a stretch unless the paper demonstrates accumulation over time, resistance to forgetting, adaptation under distribution shift, or any measurable learning curve across tasks. The current evidence is mainly the final row in **Table 3**, where adding RSS improves results relative to the same configuration without RSS. Useful, yes. But that is far short of establishing the richer claims about evolution and lifelong learning made in the Introduction and Method sections.

7. **The evidence for diversity improvements is weak and partially relegated outside the main empirical narrative.**  
   The paper claims planning improves diversity and highlights integration with ActorBreaker’s planner. However, diversity is not part of the central benchmark table, and the main paper only briefly mentions this. **Figure 3** shows diversity scores, but it is in the appendix-style material and uses the potentially mis-specified metric in **Equation (1)**. Even setting the formula issue aside, the paper does not clearly quantify the ASR-diversity tradeoff in the main results. If diversity is a major motivation, it needs first-class evaluation, not a side plot.

8. **Some claimed causal interpretations are stronger than the evidence supports.**  
   On **Pages 8–10**, the paper makes statements such as reflection being the largest contributor for o3, backtracking being the most significant factor for Claude, or Claude being aligned specifically on GOAT samples or strategy libraries. The first type of claim is somewhat supported by **Table 3**, though still only within one scaffold; the second type, especially the explanation about why Claude resists GOAT, is speculation. The paper should distinguish observed ablation trends from mechanistic explanations. Right now the discussion sometimes drifts from “we observed” to “this is because” without sufficient evidence.

9. **Presentation quality is uneven, with several places where the writing or formatting creates avoidable confusion.**  
   There is duplicated ActorBreaker row in **Table 2**. The prompt sections on **Pages 15–20** are messy, with malformed formatting and some broken JSON / code block presentation, especially in the Primer prompt section. The pseudocode uses inconsistent variable names, for example \(H_t\), `target_history`, \(\mathbb{H}_{\mathbb{T}}\), and \(\mathbb{H}_{\mathbb{A}}\) without a clean unified notation. These issues collectively make the paper feel less polished than it should be for ICLR.

10. **The paper does not sufficiently separate optimization budget from total system cost.**  
    The six-turn target-model budget is useful, but the actual attack uses multiple additional model calls, including attacker, scorer, evaluator, planner, summarizer, and embedding modules. **Table 5** is a step in the right direction, but the framing elsewhere still emphasizes “within six turns” in a way that can read as if total cost is nearly matched. For practical black-box red-teaming, total system inference cost matters, not just target-query count. The paper should foreground this more clearly.

11. **Related-work positioning is incomplete around alternative search-based multi-turn attackers.**  
    The paper compares mainly against GOAT, Crescendo, ActorBreaker, AutoDAN-Turbo, X-Teaming, and FITD. That is a decent set, but the paper’s broader framing, especially around systematic exploration of attack trajectories, would benefit from stronger discussion of other search-oriented multi-turn methods. This matters because the paper’s main claim is not just “one more attack,” but a general framework for adaptive exploration. The current related-work section underplays that broader context.

## Questions
1. The most important clarification concerns evaluation. Can the authors report final performance using an evaluation protocol that is fully decoupled from the internal rubric scorer \(\mathbb{R}\), including selecting the final attempt without rubric-based reranking? For example, what happens if one evaluates only the final conversation turn or a uniformly chosen finishing attempt, judged by an external evaluator not used anywhere inside the search loop? This would significantly increase my confidence that the gains in **Table 2** are not largely scorer-induced.

2. Please reconcile the inconsistencies between **Section 3.5** and **Algorithm 3**. Is success triggered at \(>8/10\) or \(>9/10\)? Is the refusal / backtracking threshold \(<3/10\) or \(\le 2/10\)? Similarly, in the Primer, is the intermediate evaluator \(\mathbb{R}\) or \(\mathbb{J}\)? A precise, unified specification is necessary.

3. Can the authors provide a cleaner decomposition of what is actually new? In particular, what performance is obtained by:  
   (i) planner + primer + finisher with no retrieval,  
   (ii) same with retrieval,  
   (iii) same with reflection,  
   (iv) same with summarization removed?  
   **Table 3** is helpful, but more systematic component isolation would sharpen the paper’s core contribution.

4. Please clarify whether the memory bank is built online during evaluation on the same 200 HarmBench goals, and if so, in what order. If strategies extracted from earlier evaluated goals are later reused for semantically similar held-out goals from the same benchmark, that has implications for how one should interpret generalization versus within-benchmark adaptation.

5. The diversity formula in **Equation (1)** appears incorrect if it is intended to be cosine-based. Can the authors confirm whether the denominator should be \( \|\phi(x_i)\|\,\|\phi(x_j)\| \)? If so, do the diversity rankings in **Figure 3** change when computed correctly?

6. In **Table 2**, there is a duplicated ActorBreaker row. Is this just a formatting error, or are there missing results that were intended to appear there?

7. Since **Figure 2** suggests performance plateaus at six turns, can the authors provide the corresponding variance or confidence intervals? The current figure shows point estimates only, and the paper mentions averaging over three runs.

## Flag For Ethics Review
- Yes, Potentially harmful insights, methodologies and applications  
- Yes, Responsible research practice (e.g., human subjects, data release)

## Details Of Ethics Concerns
The paper explicitly develops and operationalizes stronger jailbreak methods for harmful-content elicitation. This is a legitimate safety research direction, but the deployment risk is obvious because the method is directly usable for bypassing safeguards. The concern is especially relevant because the paper includes substantial methodological detail, including attack prompts, multi-stage decomposition, and a worked example attack in **Appendix D / Pages 24–31** that provides a concrete harmful-use pathway.

A second concern is responsible release. The ethics statement on **Page 11** argues for open access to prompts and code, but the paper does not discuss controlled release, staged access, or any misuse-mitigation plan. Given the reported effectiveness on frontier models, the release decision deserves closer scrutiny than the current one-paragraph treatment.

## Soundness Rating
2: fair. The empirical results are substantial and the ablations are useful, but evaluation entanglement, baseline modifications, and algorithm/specification inconsistencies weaken confidence in the central comparative claims.

## Presentation Rating
2: fair. The paper is readable overall and **Figure 1** is helpful, but notation inconsistencies, pseudocode/text mismatches, malformed prompt formatting, and some table issues materially hurt clarity.

## Contribution Rating
2: fair. The paper tackles an important problem and offers a useful modular perspective, but the scientific novelty beyond combining known agentic attack ingredients is limited, and the evidence does not fully support the broader lifelong-learning framing.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted.  
The paper is interesting, practically relevant, and stronger than many purely anecdotal jailbreak papers, but I do not think the current version fully supports its strongest claims. The main concerns are not cosmetic, they affect novelty, fairness of comparison, and interpretability of the reported gains. With a cleaner evaluation protocol, tighter algorithmic specification, and more honest scoping of the contribution, this could become a significantly stronger paper.

## Reviewer Confidence
4: confident. I am confident in this assessment, though not absolutely certain. It is unlikely, but not impossible, that I missed some subtle implementation detail or intended clarification behind the scorer/evaluator distinctions.