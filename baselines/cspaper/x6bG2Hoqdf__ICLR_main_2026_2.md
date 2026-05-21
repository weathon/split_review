---
job_id: 6e87aa81-a385-46e3-88cf-5f2be5b25dd6
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: x6bG2Hoqdf.pdf
paper: CALM: Co-evolution of Algorithms and Language Model for Automatic Heuristic Design
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, combining reinforcement learning, optimization, code-generating language models, and hybrid neuro-symbolic/evolutionary search for automated heuristic design.

## Minimum Quality
Pass ✅. The submission contains the expected scientific components, including abstract, introduction, related work, methodology, experiments, quantitative results, and conclusion/discussion, and it presents a nontrivial methodological contribution with substantial empirical evaluation; while I have technical and experimental concerns, they do not rise to the level of a desk reject.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden instructions, suspicious prompt injection attempts, or manipulative text targeting automated reviewers in the provided paper content.

# Expected Review Outcome:
## Summary
This paper proposes CALM, a framework for automatic heuristic design that combines prompt-level evolutionary search over heuristics with on-the-fly reinforcement learning fine-tuning of the underlying language model using GRPO. The method introduces several prompt operators, a collapse mechanism to escape stagnation, and a reward function based on relative heuristic improvement, and it is evaluated on OBP, TSP, CVRP, and OP against hand-crafted, neural, and recent LLM-based AHD baselines.

## Strengths
The main strength is the paper’s clear attempt to move beyond the now-common “fixed LLM + prompt evolution” setup. The conceptual shift in **Figure 1** is useful and largely accurate: prior pipelines are depicted as evolving only heuristics through prompt engineering, while CALM adds a learnable model-update loop via GRPO. This figure does real explanatory work, not just decoration, because it clarifies what the authors view as the missing axis in prior AHD systems, namely adaptation of the generator itself rather than only adaptation of the prompt context.

The empirical scope in the main paper is reasonably broad. The authors evaluate on four optimization settings with somewhat different solver interfaces, OBP and step-by-step TSP, plus ACO-based CVRP and OP. This is better than a one-task demonstration, and it helps support the claim that the method is not narrowly engineered for a single benchmark.

There are several strong quantitative results. In **Table 1**, the local Qwen+GRPO version of CALM improves the average OBP gap to **0.71%**, outperforming both the API-based baselines and EvoTune under the same compact local model family. This is one of the cleaner result tables in the paper because the margin is not just on one scale, it is sustained across several test sets. In **Table 2**, CALM is competitive on TSP and improves notably over other LLM-based methods, especially at \(N=200\), where the local GRPO variant reaches **13.41%** gap. In **Table 3**, the local GRPO variant is particularly convincing on CVRP, where it beats all listed LLM-based baselines at all three scales, and on OP at \(N=100\) and \(N=200\), where the gains over prior LLM-based methods are material.

The ablations are better than average for this line of work. **Table 4** does not only remove GRPO, it also probes reward variants, collapse configurations, and operator removals. Even if not all conclusions are fully airtight, this table substantially improves the paper over a pure benchmark-comparison submission. In particular, the GRPO ablation is important: “local, w/o GRPO” is consistently worse than “CALM (local, w/ GRPO)” on both OBP and OP, which supports the core claim that numerical guidance matters.

The training dynamics plots in **Figure 2** are also useful. For both CVRP and OP, the curves show that CALM starts behind some stronger API-based baselines but improves steadily and overtakes them later. That visual trend is important because it supports the paper’s narrative that model adaptation is not merely a cosmetic addition. The figure would be even stronger with more uncertainty reporting or more tasks, but it still provides meaningful evidence.

I also appreciate that the paper is trying to be compute-conscious. Running a 7B INT4 model with low-rank fine-tuning on a single 24GB GPU is a practical design choice, and the manuscript is unusually explicit about the resource setting instead of hiding behind large proprietary systems.

## Weaknesses
1. **The central empirical claim is somewhat blurred by unequal model backends and budgets, which makes the “beats stronger API-based models” narrative less clean than the paper suggests.**  
   The main text repeatedly contrasts local Qwen2.5-7B-INT4+GRPO with API baselines using GPT-4o-mini or GPT-3.5-turbo, but the comparison is not a pure method comparison because CALM changes both the search framework and the trainability of the generator. The paper partly acknowledges this on **Page 6**, but the framing still overstates the causal attribution. In **Tables 1 to 3**, there are effectively two CALM variants, an API version “w/o GRPO” and a local version “w/ GRPO”, while many baselines are fixed-model API systems. This makes it difficult to isolate whether the gain comes from RL fine-tuning, from the particular operators, from repeated sampling with \(G=4\), or simply from a more favorable search/evaluation loop. The ablation in **Table 4** helps, but it is only on OBP and OP, and still does not fully normalize query count versus heuristic evaluation count across all methods. For a paper whose main thesis is that co-evolving the model matters, cleaner apples-to-apples comparisons are essential.

2. **The reward formulation in Section 4.3 is under-justified and mathematically awkward in ways that matter for stability and interpretation.**  
   In **Equation (3)**, the relative gap
   \[
   \Delta(h_{\mathrm{new}},h_{\mathrm{t\_base}})=\mathrm{clip}\left(\frac{|g(h_{\mathrm{new}})-g(h_{\mathrm{t\_base}})|}{\min\{|g(h_{\mathrm{new}})|,|g(h_{\mathrm{t\_base}})|\}},0,1\right)
   \]
   is unusual. Using the minimum absolute score in the denominator can inflate the normalized gap when either score is near zero, and the clipping to \([0,1]\) then saturates many differences into the same reward regime. That may be acceptable as a heuristic, but the paper never explains why this denominator is preferable to a more standard relative-improvement form such as \((g_{\text{new}}-g_{\text{base}})/(|g_{\text{base}}|+\epsilon)\). This matters because the whole RL signal depends on this quantity.  
   The issue gets sharper in **Equation (4)**. Duplicate heuristics are detected via equality of performance, “if \(\exists h\in H\) such that \(g(h)=g(h_{\mathrm{new}})\)”. Equal score is not equivalent to duplicate heuristic, especially on discrete or noisy tasks. Conversely, semantically duplicate code with slightly different floating-point outcomes would be treated as non-duplicate. Since the reward is meant to encourage novelty, the paper should not conflate novelty with exact score mismatch. This is not a cosmetic concern, it changes what the RL policy is being optimized to produce.

3. **The GRPO usage is described at a high level, but the actual training signal at the token level remains conceptually shaky for this problem.**  
   On **Pages 4 to 5**, the authors motivate injection and replacement by arguing that full-response rewards get misattributed to all tokens uniformly, and that finer operators help GRPO localize useful changes. I agree with the intuition, but the paper does not really show that the resulting token-level credit assignment is improved in practice. The argument is mostly narrative. Since **Equation (1)** is standard sequence-level RL with token-wise likelihood ratios, the burden here is to demonstrate that the operator design actually reduces reward dilution or variance. Right now, the claim that these operators make GRPO “more effectively identify the contribution of individual structural changes” is plausible but not evidenced directly. A more convincing paper would include statistics on edit locality, response feasibility, or advantage variance under different operators.

4. **The collapse mechanism is interesting, but in the main paper it reads more like a heuristic gadget than a well-validated component.**  
   The collapse rule in **Section 4.2** triggers when \(\mathrm{random}(0,1)<c_n\delta_0\) or \(c_n\ge C\), and **Equation (2)** provides an approximation for expected time to collapse. The issue is not that the derivation is wrong in spirit, it is that the approximation is disconnected from the actual search process. The calculation assumes a simple rising hazard independent of search state, but in the real system \(c_n\) is coupled to operator choice, model adaptation, and population content. So the analytical expectation mainly characterizes the hand-designed timer, not the search behavior of CALM. This would be fine if the paper were modest about it, but the main text gives it more weight than it deserves. Also, **Table 4** only explores a few settings on two tasks, and the mechanism’s interaction with the RL-updated model is not dissected. The component may help, but the paper does not yet tell me when it helps, why it helps, or whether a simpler restart policy would perform similarly.

5. **Several conclusions drawn from the results are stronger than what the tables actually support.**  
   For example, in **Table 2** on TSP, CALM is not uniformly best among LLM-based API baselines; the API CALM variant is slightly worse than MCTS-AHD at \(N=50\) and \(N=100\), and only better at \(N=200\). The text on **Page 7** is mostly fair, but elsewhere the narrative can sound more sweeping than the table supports. Similarly, in **Table 3** for CVRP under the API setting, CALM is not the best among listed methods, MCTS-AHD is slightly better at all three scales. So the strongest support for the paper’s thesis really comes from the local GRPO variant, not from the verbal-gradient design alone. That distinction should be stated more cleanly, because otherwise the reader is asked to infer a broader win than the results justify.

6. **Generalization is still fairly narrow, despite the paper’s language about transfer to new scales.**  
   The experiments mostly test nearby scale changes within the same synthetic task families. Yes, there are out-of-domain sizes, and that is useful, but the distributions are still generated by the same protocols. This matters because the paper positions CALM as a framework that internalizes characteristics of successful heuristics and improves future generations in a reusable way. The evidence provided is weaker than that claim. **Figure 2** shows training-time best-so-far curves on the same problem family, not cross-distribution robustness. **Tables 1 to 3** are all within-family evaluations. A stronger paper would test either a changed instance distribution, changed solver parameters, or transfer of a fine-tuned model across tasks in the main text, rather than leaving such discussion mostly outside the central evaluation.

7. **The presentation has multiple notation and exposition problems that make the paper harder to trust than it should be.**  
   There are many small but consequential issues: malformed text around **Equation (1)** and some surrounding prose on **Page 3 to 4**; ambiguous wording such as “better on any same instance” in prompt templates; inconsistent operator naming between “replacement”, “modification”, and “rewrite”; and several places where symbols or formatting are broken. The algorithm description in Appendix C also appears partially corrupted, though I am not using the appendix to judge validity. More importantly for the main paper, the distinction between “duplicate heuristic”, “equal performance”, and “novel heuristic” is never made precise, despite being central to the reward function. Presentation is not fatal here, but it is clearly below the bar of a polished top-tier methodological submission.

8. **The practical cost argument is incomplete in the main paper.**  
   The paper emphasizes that CALM runs on a single 24GB GPU, which is good, but the main text does not sufficiently quantify the extra cost of repeatedly fine-tuning the model during search relative to fixed-model baselines. This matters scientifically because the claimed improvement is not free, and readers need to understand the quality-versus-compute trade-off. The appendix apparently includes timing breakdowns, but the main paper only gives high-level runtime remarks. Since efficiency is part of the claimed appeal, a compact cost comparison in the main paper would materially strengthen the case.

9. **The paper’s literature positioning is decent, but still a bit selective around the broader design space of hybrid numerical-symbolic AHD.**  
   The related work cites many recent AHD papers, which is good, but the method would benefit from more explicit comparison to other approaches that combine LLM-guided search with nontrivial numeric adaptation or memetic refinement. The current positioning makes CALM sound more isolated than it really is. This does not negate the contribution, but it weakens the paper’s argument that the proposed combination is uniquely motivated and sufficiently differentiated.

## Questions
1. The biggest issue I would like clarified is the reward design in **Equations (3) and (4)**. Why is the denominator in \(\Delta\) chosen as \(\min(|g(h_{\mathrm{new}})|,|g(h_{\mathrm{t\_base}})|)\) rather than \(|g(h_{\mathrm{t\_base}})|+\epsilon\) or another more standard normalization? Please explain the intended behavior when one score is near zero, and whether saturation due to clipping is common in practice.

2. In **Equation (4)**, duplicate detection is implemented by equality of performance with an existing base heuristic. Is that really what you use, or is there also code-level or AST-level duplicate filtering? If it is only score equality, please justify this choice, because equal score is not equivalent to duplicate heuristic.

3. Can the authors provide a more controlled decomposition of gains among: (i) GRPO fine-tuning, (ii) \(G>1\) grouped sampling, (iii) the new operators, and (iv) the collapse mechanism? **Table 4** is useful, but it does not fully isolate these effects across all tasks.

4. For the operator argument on **Pages 4 to 5**, can you provide evidence that injection/replacement actually improve credit assignment or search efficiency, for example by reporting feasibility rate, average edit distance from parent heuristics, or breakthrough frequency per operator?

5. The local GRPO variant is strongest on CVRP and OP. Why is the gain on TSP comparatively modest in **Table 2**? Is this mainly because the TSP seed heuristic is already strong, because the step-by-step decision interface is less amenable to your operators, or because the RL signal is noisier there?

6. Since **Figure 2** is central to the “co-evolution helps over time” story, it would help to know whether the trajectories are robust across random seeds and across all four tasks. Could the authors comment on whether similar patterns hold for OBP and TSP?

7. If possible in rebuttal, please provide a concise wall-clock comparison between CALM and at least one strong fixed-model baseline under matched query budgets, ideally in the main-text setting rather than only in supplementary analysis. That would increase my confidence that the extra RL loop is justified by the quality gains.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics concerns are apparent from the paper. The work uses synthetic optimization benchmarks and heuristic generation, with no human subjects or sensitive personal data in the main experimental setup.

## Soundness Rating
3: good. The core empirical claims are supported reasonably well by the presented experiments and ablations, but there are important issues around reward specification, attribution of gains, and scope of generalization that keep this from an “excellent” soundness score.

## Presentation Rating
2: fair. The overall structure is clear and **Figure 1**, **Figure 2**, and **Tables 1 to 4** are useful, but the paper has enough notation issues, malformed text, and underspecified definitions that the presentation falls short of being fully polished.

## Contribution Rating
3: good. Jointly evolving prompts and the underlying LLM for AHD is a meaningful contribution, and the empirical results make it worth sharing with the ICLR community, even though the methodological analysis is not yet as deep or clean as it could be.

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected. The paper has a real idea, solid results, and better-than-average ablation for this area. I remain skeptical about some of the reward design choices and about how cleanly the gains are attributed, but overall I think the contribution is interesting enough and empirically strong enough to clear the bar, narrowly.

## Reviewer Confidence
4: confident. I am confident in the assessment and familiar with the relevant area; I checked the main technical claims and empirical evidence carefully, though some implementation-level details remain underspecified in the paper.