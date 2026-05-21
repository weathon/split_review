---
job_id: 9b0ee422-92f8-4272-adbb-d6e099ae657d
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: cmzeMZNsmm.pdf
paper: Revisiting Prompt Optimization With Large Reasoning Models—A Case Study on Event Extraction
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within general machine learning and language-related learning systems, focusing on prompt optimization, black-box search, and evaluation of large reasoning models on structured prediction tasks.

## Minimum Quality
Pass ✅. The submission contains the expected core sections, presents a coherent methodology and empirical study, and does not exhibit a fatal methodological flaw such as obvious test leakage or unsupported central claims severe enough to warrant desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, reviewer-targeted instructions, or other manipulative content in the provided paper text.

# Expected Review Outcome:
## Summary
This paper studies whether large reasoning models still benefit from prompt optimization, using end-to-end event extraction as the main case study. The authors evaluate DeepSeek-R1 and o1, alongside GPT-4o and GPT-4.5, as both task models and prompt optimizers inside an MCTS-based framework, and also test transfer to Geometric Shapes and NCBI Disease NER. The main reported findings are that LRMs benefit from prompt optimization, and that LRMs, especially DeepSeek-R1, are stronger prompt optimizers than the compared LLMs.

## Strengths
The paper asks a timely and concrete question. The framing is easy to understand: if reasoning-oriented models are supposedly better at following under-specified instructions, do they still need prompt optimization, and are they themselves better prompt optimizers? That is a useful empirical question.

The experimental matrix is reasonably comprehensive within the paper’s chosen scope. The authors vary both the task model and optimizer model, and they do so under a unified framework, which makes the comparison cleaner than many prompt-engineering papers where the prompting strategy, inference setup, and base models all change at once.

I appreciated that the paper does more than report one headline number. In particular, **Table 1** is informative because it lets the reader inspect both within-model gains from prompt optimization and cross-optimizer differences. The trend that DeepSeek-R1 as optimizer is often strongest is visible across several rows, and the inclusion of depth-1, depth-5, dev, and test blocks gives a better picture than a single aggregate result would.

There is some useful qualitative analysis. **Table 2** gives concrete examples of what different optimizers actually change in the prompt, and this supports the paper’s claim that LRMs tend to add more actionable extraction heuristics and exception handling, while LLMs emphasize formatting and general instructions. Even if one may debate how general these examples are, this table at least connects the quantitative gains to an interpretable mechanism.

The figures are also helpful in parts. **Figure 4** usefully visualizes the depth-wise optimization trajectories, and the claim that DeepSeek-R1 tends to yield faster and more stable convergence than GPT-4.5 is at least directionally supported by the curves and variance bands there. **Figure 5(a)** is another good addition, since the survival-curve view is more informative than only showing best-case prompts; it suggests that DeepSeek-R1 is not merely producing a single lucky prompt, but a denser set of stronger prompts.

The paper is generally well organized. The task setup in **Figure 2** and the optimization loop in **Figure 3** make the workflow understandable without forcing the reader to reconstruct it from prose alone.

## Weaknesses
1. **The main contribution is largely an empirical benchmark around an existing optimization framework, and the paper somewhat oversells this as a broader methodological conclusion.**  
   The optimization engine is essentially inherited from PromptAgent-style MCTS, as acknowledged in **Section 3.2** and **Algorithm 1** in the appendix. What is new here is mainly the evaluation target, the model swap, and the comparative study. That can still be publishable, but then the bar for experimental rigor and scope becomes higher. Right now, the paper’s central take-away, namely “LRMs still benefit from prompt optimization and are better optimizers,” is interesting but narrower than the framing suggests. The paper occasionally writes as if it has established something general about LRMs, while most of the evidence comes from one structured IE setup plus two relatively small auxiliary tasks.

2. **The event extraction evidence is based on a heavily reduced and non-standard subset of ACE05, which weakens external validity.**  
   On **Page 4**, the authors state that ACE05 originally has 33 event types, but they restrict the study to only 10 because longer prompts become hard for the models to handle. This is understandable as an engineering constraint, but scientifically it matters a lot. The paper is effectively studying prompt optimization under a simplified schema regime. That makes the conclusion less about event extraction in general and more about event extraction after substantial task pruning. Since the paper repeatedly emphasizes that EE is “complicated” and “structured,” this reduction undercuts the strength of that claim. The same concern is visible in **Figure 2**, where only two events are shown, and the whole setup looks manageable precisely because the ontology has been narrowed.

3. **The optimization and evaluation protocol is vulnerable to overfitting to a very small development set, especially given repeated search and best-node selection.**  
   In **Section 4.1**, the dev set is only 100 examples, and on **Page 5** the authors state, “we report results only from the best-performing prompt nodes in each model’s search trajectory.” In **Section 3.2**, the reward is computed on the held-out dev set, and the best prompt is selected based on dev-set performance. With MCTS depth up to 5, multiple expansions per node, and repeated rollout-based updates, this is effectively a nontrivial amount of search against a tiny dev set. The test results in **Table 1** do help, but they do not fully remove the concern, because the entire search and model selection process is still tightly coupled to that small dev sample. This matters because prompt search can exploit annotation quirks and metric instability quite aggressively.

4. **The paper does not provide uncertainty estimates or repeated-run variability for the core quantitative comparisons in the tables.**  
   This is a serious omission for a paper whose main claims are comparative and often hinge on modest gaps. For example, in **Table 1**, differences such as 36.98 vs 36.90, or 37.74 vs 37.58, are discussed substantively in the text, but there is no sense of variance over runs, prompt-search seeds, or API stochasticity. The optimizer uses temperature sampling, as stated in **Appendix A.6**, and the system includes multiple stochastic components, so single-number reporting is not enough. **Figure 4** includes some variance visualization across depths, which is good, but the main benchmark tables should also include either standard deviations across independent optimization runs or some statistical robustness analysis.

5. **The methodology has several underspecified details that are important for interpreting the reward signal and the MCTS dynamics.**  
   The mathematical presentation in **Section 3.2** is not fully consistent with the appendix. In the main text, the reward is defined as  
   \[
   r_t = \mathcal{R}(s_t, f_t),
   \]
   “based on averaged F1 scores across EE subtasks ... on a held-out development set after editing \(\mathcal{P}_t\) with feedback \(f_t\).”  
   But in **Algorithm 1** on **Page 13**, the reward stored after expansion is  
   \[
   r(s_t,f_t)\gets \mathcal{R}(\hat{A}_{batch},A_{batch}),
   \]
   which instead looks like a batch-level reward computed from predictions and gold labels, not a dev-set evaluation of the edited prompt. Those are not the same object. This is not a cosmetic notation issue; it changes the state-action semantics of the MCTS. Is the reward based on the sampled training batch, on the dev set, or on some combination? The paper should define the reward unambiguously as something like
   \[
   r_t = \mathcal{R}_{\text{dev}}(\mathcal{M}_{task}; \mathcal{P}_{t+1})
   \]
   or
   \[
   r_t = \mathcal{R}_{\text{batch}}(\hat{A}_{batch},A_{batch}),
   \]
   and then explain how that interacts with node selection and backpropagation. Right now the core optimization objective is blurry.

6. **Algorithm 1 is not really standard MCTS as written, and the discrepancy between the claimed search structure and the actual implementation is not resolved clearly enough in the main paper.**  
   In **Section 4.1**, the authors say that “in each depth of rollout, we expand the parent node by three child expansions.” But **Algorithm 1** stores a single feedback action in \(A(s_t)\gets \{f_t\}\) upon expansion, which reads more like one sampled action per unexpanded node than three explicit children. The selection equation also maximizes over feedback objects \(f\in A(s_t)\), yet the text elsewhere describes actions as prompt edits and states as prompts. The mapping between “feedback,” “action,” and “child prompt” is muddled. Since the main contribution is empirical, the optimization backbone must at least be crisply specified. Otherwise it is hard to know whether differences come from better prompts, different branching behavior, or simply different stochastic generation by the optimizer model.

7. **The comparison across models is confounded by unequal deployment conditions, particularly for DeepSeek-R1.**  
   On **Page 5**, the authors note that DeepSeek-R1 is deployed locally and quantized to 2.5 bits, while the others are accessed via APIs. This is not automatically invalid, but it complicates interpretation. Quantization may change both task-model behavior and optimizer behavior, and local serving may differ in decoding constraints, truncation behavior, and token accounting. Yet the paper still makes fairly direct statements that LRMs outperform LLMs as task models and optimizers. Those claims should be toned down or better controlled. At minimum, the paper should discuss how much of the comparison is architectural/model-family versus deployment setup.

8. **The use of output token counts in Table 1 is under-analyzed, even though efficiency is part of the claimed story.**  
   **Table 1** includes “#Output Tokens,” and one immediately sees an enormous gap between LRMs and LLMs, with o1 and DeepSeek-R1 producing far longer outputs. That matters because prompt optimization quality and test-time cost are intertwined here. A method that improves AC by several points while generating 10 to 30 times more output tokens is not directly comparable to a cheaper alternative. The paper hints at this in **Section 5** and with **Figure 5(b)**, but it never really turns it into a fair efficiency-quality analysis. This omission is especially noticeable because the paper claims LRMs are stronger optimizers and stronger task models, but not whether they are stronger under matched inference budgets.

9. **The “generalization beyond event extraction” evidence is too thin to support the stronger generality claims.**  
   The additional tasks in **Table 3** are welcome, but they are limited. Geometric Shapes is a toy symbolic reasoning benchmark, and NCBI Disease NER is a relatively constrained extraction task. Using only self-optimization there, rather than the full cross-model optimizer matrix used for EE, also makes the extension partial. As a result, the statement in the abstract and conclusion that the findings “generalize to tasks beyond event extraction” is a bit too broad for the actual evidence presented. A more accurate claim would be that the trend appears on two additional tasks.

10. **The qualitative analysis is suggestive, but parts of it are not as rigorous as the paper presents them.**  
    **Figure 5(c)** provides an error categorization for DeepSeek-R1 with different optimizers, but the methodology behind these categories is not described in enough detail in the main paper. Are these categories mutually exclusive? Were they manually annotated? Over how many examples? Without that, the chart risks reading more like an illustrative diagnostic than solid evidence. Similarly, **Table 2** is informative, but it focuses on the best prompt for one task model, DeepSeek-R1, which may exaggerate optimizer-specific stylistic differences.

11. **Some exposition and notation choices are sloppy enough to hurt trust.**  
    There are several avoidable issues: “full MSTC” on **Page 6** appears to be a typo for MCTS; in **Section 3.2**, the reward notation conflates prompt states, feedback, and evaluation signals; in **Figure 5**, the caption says there are panels (a), (b), and (c), but the layout across pages is awkward and harder to follow than it should be. None of these alone is fatal, but together they create friction in a paper whose scientific contribution depends heavily on careful experimental bookkeeping.

12. **The literature positioning around event-extraction-specific prompting is thinner than it should be.**  
    The paper cites several general prompt optimization works and some zero-shot IE works, which is good. However, for a paper centered on event extraction as the flagship case study, the discussion of prior prompt-based or prompt-tuned event extraction methods is still fairly limited. This matters because some of the gains here may reflect rediscovering task-specific guideline engineering that the event extraction community already knows matters. The paper should position itself more explicitly against event-extraction-specific prompting and prompting-for-IE papers, not only black-box prompt search papers.

## Questions
1. Please clarify the exact reward used in search. In **Section 3.2**, reward appears to be dev-set performance after editing the prompt, while in **Algorithm 1** it appears to be batch-level training reward, \(\mathcal{R}(\hat{A}_{batch},A_{batch})\). Which one is actually used during node expansion, selection, and backpropagation? A precise definition would increase my confidence substantially.

2. How many independent optimization runs were performed per model-optimizer pair, with different random seeds or sampling seeds? If the reported numbers in **Table 1** and **Table 3** come from a single run, please provide run-to-run variance. This is particularly important because several claimed differences are small.

3. Can the authors report how performance changes when using more of ACE05, or at least more than 10 event types? I understand the context-window constraint, but the current subset choice makes it hard to know whether the conclusions hold in a less curated setting.

4. Can the authors disentangle quality from cost by reporting AC versus total generated tokens, or a fixed-budget comparison? **Table 1** suggests major token-efficiency differences between LRMs and LLMs, and this could materially change how one interprets “better optimizer” or “better task model.”

5. What exactly is being averaged in the reward across TI, TC, AI, and AC? Is it an unweighted arithmetic mean of four F1 scores, or something else? Since the paper focuses primarily on AC in the results discussion, it would help to know whether the optimizer is directly targeting AC or a multi-metric objective.

6. In **Figure 4**, what is the source of the variance bands? Different search runs, different batches, or different sampled prompts within one tree? Please define this clearly.

7. For **Figure 5(c)**, how were the error categories assigned, and were they multi-label or single-label? A short annotation protocol and the number of analyzed errors would make this figure much more convincing.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No specific ethics concerns are raised by the paper as written. The work evaluates prompting strategies on standard NLP benchmarks and does not appear to involve sensitive human-subject experimentation or release of risky artifacts in the main paper.

## Soundness Rating
2: fair. The empirical study is interesting and the central trend is plausible, but key methodological details around the reward definition, search protocol, variance, and external validity are not supported strongly enough for a higher soundness score.

## Presentation Rating
3: good. The paper is generally readable and includes useful figures and tables, but there are important notation inconsistencies and some confusing methodological exposition.

## Contribution Rating
2: fair. The paper offers a useful empirical case study and some practical insights, but the novelty is limited and the scope of the conclusions is narrower than the framing suggests.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The paper is timely and contains worthwhile observations, especially the comparative evidence in **Table 1**, the qualitative prompt analysis in **Table 2**, and the convergence plots in **Figure 4**. Still, the combination of limited methodological novelty, a reduced ACE setup, unclear reward/search specification, and lack of robustness estimates leaves me unconvinced that the paper is ready for ICLR in its current form.

## Reviewer Confidence
4: confident. I am confident in the assessment and checked the experimental and methodological details carefully, though there remains some uncertainty because the optimization procedure is not specified as clearly as it should be.