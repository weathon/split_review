---
job_id: da67a97f-e37a-485c-8483-f032fcf5d635
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: AB3jM3iMaW.pdf
paper: Self-Exploring Language Models for Explainable Link Forecasting on Temporal Graphs via Reinforcement Learning
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, at the intersection of learning on graphs, reinforcement learning, LLM reasoning, and explainable prediction on temporal graphs.

## Minimum Quality
Pass ✅. The submission contains the expected core components, including abstract, introduction, related work, method, experiments, quantitative results, qualitative analysis, and conclusion; despite several important weaknesses, it meets the minimum threshold for full review rather than desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, reviewer-targeting instructions, or other manipulative content in the paper text or visible figures.

# Expected Review Outcome:
## Summary
This paper proposes ReaL-TG, an RL-based framework for explainable link forecasting on temporal graphs using LLMs. The method constructs a text-form temporal context graph with a temporal random-walk selector (T-CGS), prompts an LLM to produce both reasoning traces and predicted destination nodes, and fine-tunes the model with GRPO using an outcome-based reward based on answer F1. The paper also introduces an evaluation protocol combining ranking metrics, including a proposed penalized MRR, with an LLM-as-a-Judge setup to assess the quality of generated reasoning.

## Strengths
The paper tackles an interesting and timely problem: bringing explainable, text-generating models to temporal graph forecasting without relying on textual node semantics. That setup is well motivated in Sections 1 and 2, especially the concern that textual attributes can leak information from pretraining, and the choice to use anonymized TGB graphs makes the evaluation cleaner than many prior LLM-on-graph papers.

I appreciate that the paper is not just another “prompt an LLM on a graph” story. The method combines three components in a coherent way: temporal context selection, QA-style forecasting, and RL fine-tuning with free-form reasoning traces. Even if some parts are not fully nailed down, the overall framing is more thoughtful than a simple prompting baseline.

The use of real TGB datasets rather than tiny synthetic graphs is a real plus. Table 1 shows that the evaluation covers several datasets with nontrivial involved node and timestamp counts, and the inclusion of unseen graphs is useful for probing transfer claims. The paper also makes a reasonable attempt to compare against both LLM baselines and traditional temporal-graph methods.

Some of the empirical gains are substantial. In Table 2, ReaL-TG-4B improves markedly over its base Qwen3-4B model on the combined score, from 0.375 to 0.552 in MRR and from 0.339 to 0.508 in pMRR. The gains on unseen datasets are especially notable, for example on uci and enron. Even allowing for concerns about the exact evaluation design, these are not tiny deltas.

The paper also deserves credit for not entirely sweeping reasoning quality under the rug. Table 3 explicitly reports faithfulness, logical consistency, and answer-explanation alignment, rather than claiming that high ranking metrics automatically imply good explanations. That is a healthier framing than what many LLM reasoning papers do.

The figures help communicate the intended workflow. Figure 1 is effective at giving the high-level picture of the training and evaluation pipeline, and Figure 2 is genuinely helpful for understanding how T-CGS prioritizes temporal neighbors through termination probabilities. Figure 3 also makes the prompting format concrete, which is important here because the whole setup depends on constrained answer extraction and explicit `<think>` / `<answer>` structure.

The qualitative examples in Figures 7 and 8 are also useful, not as proof, but as illustrations of what the authors claim RL changes in practice. In particular, the examples support the claim that the fine-tuned model is less likely to spiral into repetitive self-reflection than the base Qwen3-4B.

## Weaknesses
1. **The paper’s central claim about “explainable” forecasting is stronger than what the method actually guarantees.**  
   The RL reward in Equation (1) depends only on the final predicted node set, not on the reasoning trace at all. This means the optimization objective has no direct incentive for truthful, causal, or minimally sufficient explanations. At best, the model is encouraged to produce answers that score well, while the explanation is generated as an unconstrained side product. The authors acknowledge reward hacking in Section 5.2 and Appendix L, which is already a warning sign that the method can learn answer-producing shortcuts divorced from sound reasoning. This matters because the paper repeatedly markets the system as producing explanations that “directly justify” predictions, but the actual training signal does not enforce that property.

2. **The LLM-as-a-Judge evaluation is interesting but not yet strong enough to support the paper’s explanation-quality claims.**  
   Section 4 defines faithfulness, logical consistency, and answer-explanation alignment, but the judge itself is another LLM prompted with a long instruction template shown in Figure 4. This leaves several unresolved issues. First, the paper does not establish robustness of judgments to prompt wording, judge choice, or sampling variance. Second, the “alignment” score uses faithfulness judgments from the same judge, so errors can compound. Third, the human validation in Section 5.2 is only on 50 samples, which is far too small relative to the full evaluation set for strong claims about reliability. The paper is trying to solve a hard problem, but the current evidence still leaves a large gap between “judge scores correlate somewhat with annotators on a small sample” and “the explanations are genuinely trustworthy.”

3. **The mathematical presentation around the core metrics and RL objective is sloppy enough to undermine confidence.**  
   There are several notation and formulation issues in Equations (2) and (3). In Equation (2), the objective appears malformed: the expectation is over \(\{O_i\}_{i=1}^{s}\) in the displayed expression, but the text later uses \(g\) rollouts; the summation indices mix \(s\), \(q\), and \(g\); there is also a factor \(1/\theta\) in front of the sum, which makes little sense dimensionally and is almost certainly not intended as written. The notation \(\pi_{\theta_{\mathrm{All}}}\) versus \(\pi_{\theta_{\mathrm{ALL}}}\) is inconsistent as well. These are not cosmetic issues, because Equation (2) is the core training objective.  
   Equation (3) has a similar problem. The formula uses \(\eta_m^{\text{gt}}\) as though it were a scalar in \(\sum_{m=1}^{M}\eta_m^{\text{gt}}\) and \(\sum_{s=1}^{\eta_m^{\text{gt}}}\), even though the text defines it as a set. The intended quantity is presumably \(|\eta_m^{\text{gt}}|\). Again, this is fixable, but in the current form it is mathematically incorrect or at least seriously underspecified. For a paper that introduces a new metric and relies on RL optimization, this level of imprecision matters.

4. **The proposed pMRR is not sufficiently justified, and its relation to standard ranking evaluation is awkward.**  
   In Section 4, pMRR is created by assigning score 1.1 to over-generated nodes and score 1 to predicted correct nodes. This is described as “can be any number \(>1\),” which is precisely the problem. If any value greater than 1 works, then the metric is under-motivated and somewhat arbitrary. The induced ranking is also extremely coarse because all predicted positives share the same score. So pMRR is not measuring calibrated ranking quality in a conventional sense; it is more like a handcrafted penalty layered on top of a binary predicted set. This does not make it useless, but the paper should be more careful about what the metric captures and what it does not. As currently written, the metric feels tailored to the output format rather than principled as a ranking measure.

5. **The filtering and query construction procedure raises concerns about evaluation realism and possible selection bias.**  
   In Section 3, training queries are skipped if the T-CGS-selected context graph does not contain all ground-truth answers or if the context graph exceeds 600 links. Section 5 says evaluation data are filtered using the “same principles.” This means the reported task is not generic temporal link forecasting, but forecasting under a curated regime where the answer is guaranteed to be visible in the selected context and the context is kept within manageable size. That is a much easier and narrower problem than the broad framing suggests. It particularly matters because the core claim is about real-world temporal graphs. If the method only works after excluding cases where the retrieval stage misses answers or the context is too large, then the bottleneck has effectively been outsourced to data curation.

6. **The gains may be partly attributable to retrieval design and task reformulation rather than the RL framework itself, but the paper does not isolate these effects well.**  
   T-CGS could be doing much of the heavy lifting. Figure 2 illustrates that the algorithm explicitly prioritizes recent, reachable historical nodes, and the prompt in Figure 3 then asks the LLM to reason over that curated subgraph. Yet there is no main-paper ablation against simpler retrieval strategies, such as most-recent neighbors, fixed-hop neighborhoods, uniform temporal sampling, or even a random subset matched for context size. Without this, it is difficult to tell whether the main contribution is RL-based reasoning improvement or just smarter context selection. Likewise, a supervised fine-tuning baseline on the same prompts and answers would be an important control, since the paper currently attributes improvements to RL without demonstrating that standard SFT would not achieve most of them.

7. **The comparison to traditional temporal-graph methods in Table 4 is weaker than the narrative suggests.**  
   Table 4 is presented as evidence that ReaL-TG-4B outperforms strong traditional methods, but the setup is not really apples-to-apples. The TGNNs are timed out after 24 hours for some datasets, which means the table mixes actual scores with missing values under a compute budget constraint rather than a clean methodological comparison. More importantly, the paper explicitly notes that ReaL-TG is evaluated on uci and enron as unseen graphs, whereas TGNNs are trained directly on those datasets and are therefore seen-graph models. That asymmetry actually helps the authors rhetorically, but it also means the tasks are not matched. I am also not convinced that default hyperparameters for all TGNN baselines are sufficient for a strong head-to-head claim, especially when the proposed method itself includes multiple carefully chosen components and filtering steps.

8. **The paper’s novelty claim is somewhat overstated relative to cited prior work.**  
   The paper repeatedly frames itself as the first framework for explainable and effective link forecasting on real-world temporal graphs via RL. The exact combination may indeed be new, but the relevant ingredients are already quite populated: LLMs for graph reasoning, RL for graph reasoning, ICL-based temporal graph forecasting, and explainable temporal reasoning methods are all cited in Sections 1 and 2. This makes the contribution feel more like a specific synthesis of existing ideas for a new setting than a major conceptual departure. That is still publishable if the evidence is strong, but the current writing sometimes oversells the degree of methodological distinctiveness.

9. **There are internal inconsistencies and clarity issues throughout the presentation.**  
   A few examples: the paper alternates between “Real-TG” and “ReaL-TG”; Table 3 labels the third reasoning metric as \(\delta_u\), whereas Section 4 defines \(\delta_a\) for answer-explanation alignment; there are multiple typos and malformed expressions in the T-CGS description on Page 4, including the neighborhood notation and normalization term. These issues accumulate. They are especially problematic in a paper that depends on careful definitions, custom metrics, and a nonstandard evaluation setup.

10. **The empirical scope is decent but still not enough to fully support broad claims about transfer and practical usability.**  
    The paper uses six TGB datasets and 4,246 evaluation examples after filtering, which is respectable, but the training set for RL consists of only 1,000 sampled queries from four datasets. That makes it hard to know whether the reported transfer is robust or if the model is tuning itself to a fairly narrow benchmark style. Table 2 looks strong overall, but performance is uneven, most notably on flight, where ReaL-TG-4B remains weak in absolute terms. If the framework is meant to be a generally useful temporal graph forecasting approach, a deeper breakdown by dataset characteristics, answer multiplicity, context size, or temporal sparsity would be valuable.

11. **The explanation examples are suggestive but also reveal a somewhat shallow reasoning pattern.**  
    In Figures 7, 8, and 13, the successful ReaL-TG outputs often reduce to “look at the recent interactions of the source node, then choose the most recent or frequent destination.” That may well be effective on many benchmark cases, but it raises the question of whether the model is actually learning rich temporal graph reasoning or mostly a stylized recency/frequency heuristic. Since the reward is purely outcome-based, this would not be surprising. The paper should probe this more directly with controlled analyses rather than relying on anecdotal case studies that naturally highlight favorable behavior.

12. **The human evaluation section is underpowered and under-described for the claims it carries.**  
    Section 5.2 reports five annotators and 50 examples, which is a start, but there is no discussion of inter-annotator agreement beyond variances of aggregated scores. Variance is not agreement. It also remains unclear how examples were sampled, whether annotation was blind to model identity, and how disagreements were resolved. Since the paper leans on this section to validate both the model’s reasoning quality and the judge’s reliability, the methodological detail here is too thin.

## Questions
1. The biggest issue for me is the mismatch between “explainable reasoning” as a claim and the purely outcome-based reward in Equation (1). Can the authors provide evidence that the reasoning trace itself causally contributes to prediction quality, rather than being a post-hoc narrative attached to an answer optimized for F1? For example, does masking or perturbing reasoning tokens during generation measurably change answer quality, or can the model obtain similar reward while emitting low-information traces?

2. Please clarify Equation (2) carefully. What are the correct rollout and summation indices, what is the intended factor in front of the token average, and how exactly is \(Adv_{i,j}\) broadcast across tokens? Right now the displayed objective appears inconsistent with the prose.

3. Please also correct Equation (3) and define pMRR more rigorously. Why is assigning score \(1.1\) to false positives the right construction, and how sensitive are results to this constant? If any value \(>1\) works, please show that the conclusions are stable.

4. An important missing ablation is retrieval. How does T-CGS compare, in the main paper, against at least a few simpler alternatives such as recency-only neighbors, fixed-hop most-recent subgraphs, or random context matched in size? This would help determine whether the gains come from RL or from a strong handcrafted context selector.

5. Can the authors include a supervised fine-tuning baseline on the same prompts and answers, without RL? Right now it is hard to separate the effect of GRPO from simply adapting the base model to the task format.

6. The data filtering deserves a much more transparent accounting. What fraction of candidate train and test queries are removed by the condition that all ground-truth answers must already appear in the selected context graph? This number is critical for understanding the practical coverage of the method.

7. For Table 4, can the authors give a fairer comparison budget or a more explicit caveat around the timeout-based TGNN results? As written, the comparison is interesting but not conclusive.

8. For the human evaluation in Section 5.2, please report stronger annotation statistics, such as pairwise agreement or a standard reliability coefficient, and clarify whether evaluators were blind to system identity.

A strong rebuttal for me would focus less on repeating headline gains and more on disentangling retrieval, task curation, and RL, while tightening the metric and objective definitions.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
The paper includes a brief ethics statement on potential hallucinations and overreliance in safety-critical settings. I do not see a specific ethics violation in the work as presented. The main concerns are scientific rather than ethical, namely whether the explanations are sufficiently faithful and whether the evaluation protocol overstates trustworthiness.

## Soundness Rating
2: fair. The empirical results are interesting and some claims are supported, but core parts of the methodology and evaluation remain underspecified or insufficiently validated, especially the RL objective presentation, the custom metric, and the explanation-faithfulness claims.

## Presentation Rating
2: fair. The high-level narrative is understandable and several figures are helpful, but there are too many notation errors, inconsistencies, and imprecise definitions for a paper introducing custom objectives and metrics.

## Contribution Rating
2: fair. The paper explores a relevant and potentially useful direction, but the evidence does not yet justify the stronger claims about explainable temporal graph reasoning and practical superiority over alternatives.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted.  
The paper is ambitious and has several appealing ideas, especially the real-world TG setting, the QA formulation, and the attempt to evaluate reasoning traces. However, the current version overclaims explainability relative to what is actually optimized, does not sufficiently isolate the source of its gains, and contains enough mathematical and methodological looseness that I do not think it is ready for ICLR main track in its present form.

## Reviewer Confidence
4: confident. I am confident in this assessment, though not absolutely certain. The paper is in an area I know well, and I checked the main methodological and evaluation details carefully, but a few implementation specifics remain in the appendix rather than the main text.