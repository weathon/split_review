---
job_id: 268ea4d9-feeb-447f-899e-48278f64d7ba
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: bxZUPQbvp0.pdf
paper: EconAgentBench: Economic Benchmarks for LLM Agents in Unknown Environments
main_score_norm: 0.2
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is a benchmark submission for LLM agents in sequential decision-making environments, which fits ICLR’s scope on datasets/benchmarks, agent evaluation, planning, and ML applications to economics.

## Minimum Quality
Pass ✅. The paper contains the expected core components for a benchmark paper, including Abstract, Introduction, Related Work, benchmark design/methodology, experiments with quantitative results, and Discussion. While I have substantial concerns about novelty, positioning, and empirical adequacy, these are review-level concerns rather than desk-reject issues.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find any hidden instructions, suspicious prompts targeting automated reviewers, or other manipulative content in the provided paper text and figures.

# Expected Review Outcome:
## Summary
This paper introduces EconAgentBench, a synthetic benchmark suite for evaluating LLM agents in three economic decision environments under partial information: procurement, scheduling, and pricing. In each environment, agents interact for 100 periods via tool use, must learn unknown environment parameters through exploration, and are evaluated at three difficulty levels. The paper reports results for several frontier models and argues that the benchmark remains unsaturated at the hard level while also enabling behavior-level analysis beyond aggregate scores.

## Strengths
The paper tackles an interesting and underexplored benchmark niche, namely multi-turn agentic decision-making in partially observed economic environments rather than static economic QA. That framing is meaningful, and the choice to focus on exploration, repeated interaction, and latent environment structure is better aligned with how many real deployment settings actually look than one-shot question answering.

I appreciated that the environments have explicit optimization structure and computable reference optima. For procurement and pricing in particular, the scoring rules are grounded in formal objectives rather than fuzzy task heuristics. This is a real strength for a benchmark paper because it makes the evaluation interpretable and reproducible.

The benchmark interface is lightweight and reasonably future-proof. The tool-use design in **Section 3.1** and the schematic in **Figure 1** clearly communicate the intended interaction loop: the agent alternates between information gathering, acting, and receiving structured feedback from the environment. **Figure 1** is simple, but it does help clarify the separation between the LLM agent, the tool layer, and the synthetic environment, which is important for understanding what exactly is being benchmarked.

The paper does a decent job making the environments scalable. The progression from Basic to Medium to Hard is concrete, and the benchmark instances are synthetically generated, which is useful for avoiding finite benchmark saturation and for enabling broader reuse.

The results in **Table 2** do show that the benchmark is nontrivial for current models. In particular, the hard settings are far from solved, and the three tasks appear to separate models differently, especially pricing versus the two stationary tasks. That qualitative separation is potentially useful to the community.

I also like that the paper goes beyond a single aggregate score and attempts behavioral analysis in **Section 4.3**. The metrics in **Table 3** such as budget utilization, best-so-far rate, and adaptability are not fully convincing as scientific evidence on their own, but they are directionally helpful and better than reporting benchmark scores alone.

## Weaknesses
1. **The paper’s novelty is not sufficiently established relative to very closely related benchmark work, including economic-agent evaluation in unknown environments.**  
   The core setup, synthetic economic environments, multi-turn tool interaction, hidden environment parameters, and three domains procurement/scheduling/pricing, reads as an incremental benchmark packaging rather than a clearly differentiated conceptual contribution. The related work section on **Page 2** positions the paper mostly against STEER, STEER-ME, VendingBench, and broad agent benchmarks, but that is not enough. The paper needs a much sharper explanation of what is genuinely new in benchmark design, not just what tasks are included. As written, the contribution risks being “three synthetic environments plus model comparisons.” For ICLR, benchmark papers usually need either a much stronger methodological advance in evaluation design or a much stronger empirical study demonstrating why this benchmark changes what we know. Right now, the paper does not quite clear that bar.

2. **The empirical study is too thin for the paper’s strongest claims, especially given the broad conclusions about capability differences and “economically meaningful insights.”**  
   The central evaluation uses only **12 instances per difficulty level** in **Section 4.1** on **Page 7**, and then reports averages in **Table 2**. That is a small sample size for a benchmark paper making comparative claims across several models and several tasks. The paper reports one significance statement, namely that Hard scores are lower than Basic scores with one-sided Welch’s t-test, but does not provide confidence intervals, standard deviations, per-task significance for most pairwise model comparisons, or any multiple-comparison correction. This matters because several of the interpretive claims in **Section 4.2** and **Section 4.3** rely on ranking models whose differences are not obviously robust. For example, in **Table 2**, the pricing difference between GPT-4.1 (66.8) and Gemini 2.5 Pro (62.8), or between GPT-5 (58.9) and Claude 3.5 Sonnet (58.7), may well be noise at this scale. The paper presents these as meaningful model-specific patterns without enough uncertainty quantification.

3. **The benchmark design choices are often under-justified, and some choices make the tasks look somewhat arbitrary rather than representative of economic decision-making.**  
   For procurement, the utility function in **Equation-like definition on Page 4**,  
   \[
   f(z_1,\ldots,z_n)=\prod_{i=1}^k \left(\sum_{a_j\in A_i} e_j z_j\right)^{1/k},
   \]
   is mathematically neat, but the paper gives very little argument for why this specific Cobb-Douglas-style aggregation is the right benchmark stress test, beyond “substitutes within category, complements across categories.” Likewise, the scheduling task reduces to finding a stable matching from blocking-pair feedback, and pricing uses a nested logit model with changing \(\alpha_i\). Each is reasonable in isolation, but the paper overstates the breadth of economic coverage. These are stylized textbook structures, not obviously representative slices of modern economic decision environments. That matters because the paper repeatedly frames the benchmark as reflecting “realistic usage of LLM agents in economic scenarios” in the **Abstract**, **Introduction**, and **Discussion**, which is stronger than the evidence supports.

4. **The mathematical exposition has several clarity problems, and in a benchmark paper this matters because the environments themselves are the main contribution.**  
   There are multiple notation and presentation issues that make careful verification harder than it should be. In pricing on **Page 6**, the nested logit demand equation mixes category-level and product-level notation in a way that is easy to misread. Specifically, the denominator term uses \(D_{j'}:=\sum_{g_k\in G_j}\exp(\cdots)\), where the index definition appears inconsistent because \(D_{j'}\) is defined using \(G_j\) rather than \(G_{j'}\). I assume this is a typo, but for the core environment equation, these details matter. Similarly, the profit is defined as \(\pi_i := (p_i/\alpha_i - c_i) q_i\), which is unusual given that \(p_i\) was introduced as the price. If \(p_i/\alpha_i\) is intended to be the effective price entering utility and profit, that should be explained explicitly; otherwise this looks dimensionally odd and can confuse what the action variable actually means.  
   In scheduling on **Page 5**, the score is
   \[
   1 - \frac{\#\text{blocking pairs in final matching}}{\mathbb{E}_{\mu \sim \text{unif. random matching}}[\#\text{blocking pairs in }\mu]},
   \]
   but the denominator is estimated by Monte Carlo only in the appendix. In the main paper, the reader is left without a sense of variance, stability, or why this is the most appropriate normalization. These are not fatal errors, but they weaken confidence in the benchmark specification because the equations are the benchmark.

5. **The comparison protocol across models is not fully fair or sufficiently controlled.**  
   All models are queried at temperature 1 according to **Section 3.2** on **Page 3**, with the same generic prompts and notes tools. The authors present this as neutral and fair, but in practice, different model families have very different sensitivities to temperature, tool-use formatting, and prompt wording. A benchmark is not automatically fair because the same scaffolding is used for all models. It may instead privilege models that happen to be more robust to this exact interaction setup. The authors acknowledge in **Discussion** that prompts and scaffolding are simple and not optimized, but they still use the resulting rankings to draw fairly strong capability conclusions. A stronger paper would either justify why this setup is a good standardized protocol, or include at least limited robustness checks beyond the narrow Gemini procurement prompt experiment in the appendix.

6. **The “economic insights” analysis in Section 4.3 is weaker than advertised and often amounts to post hoc descriptive storytelling.**  
   **Table 3** reports budget utilization, best-so-far rate, and adaptability. These are interesting diagnostics, but the claims built on them are much stronger than the evidence. For example, on **Page 8**, the paper states that Claude’s stronger procurement performance relative to other non-reasoning models can “likely be explained” by higher budget utilization. But this is only a correlation over seven model points, with no causal analysis, no variance bars, and no demonstration that the metric is independently predictive across instances. Similarly, in pricing, the paper admits that manual inspection mostly shows simple heuristics, which is honest, but then the “adaptability” metric is too coarse to support much beyond that. The analysis is suggestive, not yet scientifically persuasive. Benchmark papers often benefit from behavioral diagnostics, but here the diagnostics are not rigorous enough to support the interpretive weight placed on them.

7. **A key baseline is missing from the main experimental narrative, and its absence materially changes how one reads the results.**  
   The main paper presents the scheduling task as challenging for LLMs, which is true from **Table 2**. However, the appendix states that a natural heuristic inspired by blocking-pair fixing achieves 100 on Basic, 98.1 on Medium, and 76.0 on Hard. That is a very important contextual baseline, especially because many models in **Table 2** perform dramatically worse than that heuristic. This baseline should not be buried outside the main paper. Without it, the reader might interpret the benchmark as mostly measuring deep strategic reasoning; with it, one might instead suspect that many models fail to discover a fairly natural local-improvement procedure. That distinction is scientifically important.

8. **The figures beyond Figure 1 are not integrated into the main scientific argument, and one of them indirectly exposes fragility rather than robustness.**  
   The scatter plots in **Figure 2** show very high variance and substantial outliers across prompt variants and difficulty levels for Gemini 1.5 Pro in procurement. The text on **Page 14** says this serves as a prompt robustness check, but visually the figure suggests the opposite, namely that with only 12 runs per condition, outliers substantially influence both score and exploration rate. The message from **Figure 2** is not “robustness” so much as “results are noisy and unstable at this sample size.” Since the main paper repeatedly interprets small model differences, this figure should have made the authors more cautious throughout.

9. **The claim of “arbitrary difficulty scaling” is overstated.**  
   The paper says in the **Abstract**, **Section 3.4**, and **Discussion** that the benchmarks allow difficulty scaling to arbitrarily high levels. In practice, the paper only validates scaling through increasing instance size and reports three levels. But scaling instance size does not necessarily preserve the same skill being measured, nor does it guarantee smooth hardness progression for LLM agents rather than merely bigger contexts or more tool-output parsing. For example, in procurement, moving to Hard changes not just \(n\) and \(k\) but also the support of the effectiveness scores and the deal-generation parameters; in pricing, higher difficulty mainly means more products. These are reasonable benchmark knobs, but “arbitrary difficulty scaling” is a strong claim that is not really established in the main paper.

10. **Presentation quality is uneven, with many typos/inconsistencies that are distracting in a benchmark paper.**  
   Table and tool names are inconsistent across pages, for example “getprevious_purchase_data” versus “get_previous_purchase_data”, “get-budget”, “get Attempt_number”, “getprevious Attempts_data”, and “get_attempt_number”. These inconsistencies appear in **Table 1** on **Page 3** and later prompt/tool definitions. The stationary/non-stationary description on **Page 4** also contains what appears to be a mistake: “to earn a perfect score in a non-stationary environment, it suffices for the LLM agent to identify and take an optimal action once,” even though the surrounding paragraph is discussing stationary environments, and the very next paragraph says non-stationary environments require repeated optimal actions. This kind of sloppiness is not cosmetic here, because the benchmark interface and scoring definitions are the core artifact.

## Questions
1. The paper’s conclusions would be much more convincing with uncertainty estimates. Can the authors report per-model confidence intervals or standard errors for all entries in **Table 2** and **Table 3**, plus statistical tests for the model rankings emphasized in **Sections 4.2 and 4.3**? In particular, which pairwise differences remain significant after correcting for multiple comparisons?

2. Can the authors explain more clearly how this benchmark differs from the closest prior benchmark-style work on LLM agents in unknown economic environments? I am not asking for a generic “ours has three tasks” answer. I would like a direct comparison table against the most similar prior efforts, clarifying what is actually new in benchmark design, evaluation protocol, or scientific findings.

3. For the pricing environment on **Page 6**, please clarify the exact semantics of the action variable and profit equation. Why is profit written as \((p_i/\alpha_i - c_i)q_i\) rather than \((p_i-c_i)q_i\)? Also please check the indexing in the definition of \(D_{j'}\), which currently appears inconsistent.

4. Why was temperature fixed at 1 for all models in **Section 3.2**? Did the authors try any lower-temperature or protocol-robustness evaluations for at least a subset of models? If rankings are highly sensitive to this choice, that would weaken the benchmark’s claims about comparative capability.

5. The scheduling heuristic baseline described in the appendix seems important. Can the authors include it in the main paper and discuss explicitly what the benchmark is measuring beyond the ability to discover a local blocking-pair repair heuristic?

6. For procurement and scheduling, why is the final score based on best action or final action respectively, rather than a measure that explicitly rewards efficient exploration? Since the benchmark is motivated by learning in unknown environments, it would be useful to understand whether the scoring rules inadvertently reward one-shot luck or late-stage exploitation more than systematic information gathering.

7. The paper claims the environments are “realistic” economic scenarios. Could the authors narrow or better justify this claim? What concrete real decision processes are each synthetic environment intended to proxy, and what aspects are intentionally abstracted away?

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
None beyond ordinary benchmark-use caveats. The paper studies agent behavior in synthetic economic environments and does not appear to involve human subjects, sensitive personal data, or direct deployment claims requiring dedicated ethics escalation.

## Soundness Rating
2: fair. The benchmark setup is coherent and mostly technically plausible, but several central claims are supported by limited empirical evidence, some equations/definitions need clarification, and the behavioral conclusions are stronger than what the presented analysis firmly supports.

## Presentation Rating
2: fair. The paper is readable overall, but there are enough notation issues, inconsistencies, and under-explained design choices that clarity suffers, especially because the environment definitions themselves are the main contribution.

## Contribution Rating
1: poor. The direction is relevant, but the paper does not sufficiently establish a clear methodological advance over closely related benchmark ideas, and the empirical study is not strong enough to elevate the work to a compelling benchmark contribution for ICLR.

## Overall Rating
2: Reject, not good enough. The paper is organized around an interesting problem and contains a usable benchmark artifact, but in its current form it feels too incremental and too lightly validated for ICLR. The main issues are weak novelty positioning, thin experimental support for broad claims, and insufficiently rigorous analysis of what the benchmark actually measures.

## Reviewer Confidence
4: confident. I am confident in this assessment and carefully checked the benchmark definitions, equations, tables, and the main experimental claims, though I may still have missed some details that would benefit from rebuttal clarification.