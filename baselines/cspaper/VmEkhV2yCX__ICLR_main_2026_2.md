---
job_id: 0f07f5e8-ff77-4a2a-98a3-acbb8ed9de03
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: VmEkhV2yCX.pdf
paper: Front-Loading Reasoning: The Synergy Between Pretraining and Post-Training Data
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅ The paper is clearly within ICLR scope, focusing on large-scale language model training, reasoning, pretraining/post-training allocation, and reinforcement learning for reasoning.

## Minimum Quality
Pass ✅ The paper contains all core components, including abstract, introduction, methodology, experiments/results, related work, and conclusion, and it presents substantial empirical evidence rather than a thin technical report. While I have concerns about some claims and experimental controls, these are review-level weaknesses, not desk-reject-level defects.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅ I found no evidence in the paper text or figures of hidden prompts, reviewer-targeting instructions, or other manipulative content.

# Expected Review Outcome:
## Summary
This paper studies when reasoning data should be introduced in the LLM training pipeline, comparing reasoning-rich pretraining against reasoning-heavy SFT under controlled token budgets. The authors pretrain several 8B models from scratch with different reasoning data mixtures, then apply SFT and RL, and conclude that reasoning data is most effective when front-loaded into pretraining, with diversity mattering more during pretraining and quality mattering more during SFT.

## Strengths
The main strength is the scale and ambition of the empirical study. Training multiple 8B models from scratch for 1T tokens, then systematically crossing them with several SFT datasets and an RL stage, is a serious experimental investment. Even if one debates some of the framing, the paper does provide more evidence than the usual “one recipe, one model, one benchmark” style paper.

The paper asks a genuinely useful question for the community: not merely whether reasoning data helps, but how to allocate it across phases. That is a practical question for modern LLM pipelines, and the paper frames it in a way that could influence data curation strategies.

I found the central empirical pattern reasonably consistent across the presented tables. In **Table 1** on Pages 6 to 7, the jump from $\mathcal{M}_{\mathrm{base}}$ to $\mathcal{M}_{\mathrm{LDQ}}/\mathcal{M}_{\mathrm{LMQ}}$ is large on math and code while general-purpose reasoning stays roughly flat, which does support the authors’ claim that early reasoning exposure mostly changes reasoning-intensive capabilities rather than broad language competence. Likewise, **Table 4** on Page 8 is a useful ablation because it directly addresses the “catch-up” hypothesis, and the stronger pretrained models remain ahead even when the baseline gets doubled SFT epochs.

The asymmetry claim, diversity for pretraining and quality for SFT, is supported better than I expected. **Table 5** and **Table 8** are particularly informative here. In **Table 5**, large mixed-quality SFT data performs much worse than the smaller high-quality SFT data, despite the opposite pattern in pretraining. In **Table 8**, naively doubling $\mathcal{D}_{\mathrm{LDQ}}$ during SFT barely helps overall and hurts math materially, while the answer-length-filtered variant performs much better. This is a concrete and useful empirical takeaway.

The paper also does a good job visually summarizing its thesis. **Figure 1** on Page 2 is not just decorative, it succinctly communicates the proposed allocation principle, namely quantity/diversity earlier and quality later, and maps cleanly onto the experiments in Sections 2 and 5. That figure helps the reader keep track of a fairly large design space.

Presentation is generally clear. The paper is easy to follow at a high level, the datasets are named consistently, and the distinction among $\mathcal{D}_{\mathrm{LDQ}}$, $\mathcal{D}_{\mathrm{SHQ}}$, $\mathcal{D}_{\mathrm{LMQ}}$, and $\mathcal{D}_{\mathrm{ALF}}$ is understandable.

## Weaknesses
1. **The paper’s optimization framing in Section 2 is more rhetorical than operational, and the math is underspecified in ways that matter.**  
On **Page 3**, Equations (1) and (2) present the problem as
\[
(\mathcal{D}_{\text{res}}^{\text{PT*}},\mathcal{D}_{\text{res}}^{\text{SFT*}})=\arg\max \mathcal{P}(\theta_{\text{final}})
\]
subject to a budget $\mathcal{B}=|\mathcal{D}_{\text{res}}^{\text{PT}}|+|\mathcal{D}_{\text{res}}^{\text{SFT}}|$.
This reads like a constrained optimization problem, but the paper never actually defines the search space, the unit of “budget” consistently, or a procedure for solving the stated objective. In practice, the experiments do not optimize over arbitrary allocations, they compare a small number of hand-chosen dataset mixtures and stages. Even more importantly, the budget notation is muddy: Equation (2) uses dataset size notation $|\cdot|$, while the actual pretraining control later on **Page 4** is in *tokens* with a fixed 80B reasoning-token budget, and SFT is described on **Page 5** in *samples* (“4.8M reasoning samples”). This is not a minor notation nit, because the paper’s central slogan is “token counts are controlled” and yet the formalism mixes samples and tokens without a clean definition of equivalence. If the authors want the optimization view, they should define budget in tokens, specify the mapping from samples to tokens, and be explicit that the paper studies a discrete subset of feasible allocations rather than solving the argmax.

2. **The claim of a “reasoning-free” or weak-reasoning baseline is not as clean as the narrative suggests.**  
The base pretraining corpus on **Page 3** already includes mathematics and code sources and is taken from NVIDIA (2025b). So $\mathcal{M}_{\mathrm{base}}$ is not a model trained on purely generic natural language with no reasoning exposure; it is a model trained on a very strong modern corpus that already contains substantial structure useful for reasoning. This matters because several conclusions are phrased in a sharp way, for example that “reasoning must be introduced early” or that later SFT “cannot recover” a weak foundation. But the actual comparison is not “no reasoning in pretraining” versus “reasoning in pretraining,” it is closer to “general modern pretraining corpus with some math/code content” versus “the same corpus plus extra reasoning-style QA/CoT data in late pretraining.” That is still interesting, but the interpretation is narrower than the paper’s rhetoric.

3. **Data contamination and overlap risks are not addressed, despite the paper relying on public reasoning-heavy datasets and benchmark suites with known overlap sensitivity.**  
This is the biggest practical concern for me. The training data and evaluation sets live in closely related ecosystems: math, code, science QA, long-CoT corpora, and public web-derived pretraining sources. Yet the main paper does not discuss contamination checks, deduplication against evaluation benchmarks, or overlap between the SFT/pretraining corpora and the test sets such as GSM8K, MATH-500, AIME24/25, HumanEval/MBPP, MMLU-Pro, and GPQA. Given the very large gains in **Table 1**, **Table 10**, and **Table 3**, contamination is not something that can be waved away. This matters especially because the paper’s strongest claims concern *where* reasoning skill is learned, and contamination could mimic durable advantages if one stage simply has more direct benchmark-adjacent exposure.

4. **The RL section is too narrow relative to the strength of the paper’s final claims.**  
The title, abstract, and **Figure 1** all suggest a story that compounds “through reinforcement learning,” but the actual RL evidence in the main paper is very limited. **Table 3** on Page 7 reports only two models, $\mathcal{M}_{\mathrm{base}}+\mathrm{SFT}_{\mathrm{SHQ}}+\mathrm{RL}$ and $\mathcal{M}_{\mathrm{LMQ}}+\mathrm{SFT}_{\mathrm{SHQ}}+\mathrm{RL}$. That is essentially a single cherry-pick between two extremes, not a systematic RL study. If RL is supposed to be part of the main conclusion, I would expect at least more than one pretraining backbone and more than one SFT recipe to survive into the RL stage. As written, the RL result is suggestive, but the paper overstates it as “definitive impact” and “conclusive evidence.”

5. **Some of the causal interpretation is too strong for what are still largely observational ablations over a few dataset recipes.**  
The paper repeatedly uses language like “critical,” “cannot be fully replicated,” “dictates the final performance ceiling,” and “proving” the catch-up or overfitting hypotheses false. That is too aggressive. The experiments show that, under the chosen models, datasets, schedules, and budgets, some early reasoning injections outperform later ones. They do not establish a universal impossibility result for late-stage specialization. This is particularly important because the explored design space is limited: one main model size, one main architecture family, fixed 600B + 400B pretraining schedule, a single SFT sample budget, and limited RL comparisons.

6. **The repeated-data issue is underexplained and could materially affect the interpretation.**  
On **Page 4**, the paper states that when a reasoning dataset is small, it is repeated so that the model sees the same total volume of reasoning tokens, and $\mathcal{D}_{\mathrm{SHQ}}$ is only 1.2M samples. Then on **Page 5**, all models are finetuned on 4.8M reasoning samples, but the paper does not clearly state whether $\mathcal{D}_{\mathrm{SHQ}}$ is repeated during SFT as well, how often examples recur, or whether any anti-memorization safeguards are used. This matters because one of the paper’s more interesting claims is that repeated exposure across phases reinforces instead of overfitting. **Figure 2** in the appendix is offered as support, but that figure is just a small grouped bar chart showing that a model seeing $\mathcal{D}_{\mathrm{SHQ}}$ in both phases beats the one seeing it only in SFT. Without variance, broader controls, or memorization diagnostics, that is not enough to settle the question. It is a plausible hypothesis, but not convincingly demonstrated.

7. **The paper does not report uncertainty estimates, seed variation, or statistical reliability for many headline differences.**  
This is not fatal, but it weakens confidence in some of the finer-grained conclusions. Large differences like those in **Table 1** and **Table 10** are probably real, but the paper also makes much of smaller gaps, for example the latent advantage of $\mathcal{M}_{\mathrm{LMQ}}$ over $\mathcal{M}_{\mathrm{LDQ}}$ in **Table 4**, or the modest gains from $\mathcal{D}_{\mathrm{ALF}}'$ in **Table 8**. Without confidence intervals, multiple training runs, or at least some discussion of run-to-run variance, it is hard to know which deltas deserve strong interpretation.

8. **The novelty is meaningful but somewhat narrower than the paper advertises.**  
The contribution is primarily a large-scale empirical comparison of data allocation strategies, not a new learning algorithm, objective, or theory of reasoning. That is fine, but the wording “first systematic study” is hard to assess and probably too broad. The related work in Section 6 does cover several mid-training and instruction-pretraining papers, but the positioning would be stronger if the authors were more explicit about what exactly is new: is it the from-scratch scale, the phase allocation framing, the specific asymmetry result, or the durability through RL? Right now those are blended together a bit too conveniently.

9. **Some tables reveal trade-offs that the main narrative underplays.**  
For instance, **Table 7** on Page 9 shows that increasing the pretraining reasoning ratio from 20% to 40% helps reasoning benchmarks after SFT but *hurts* instruction following, dropping INSSFT AVG from 49.82 to 44.81. Likewise, **Table 8** and **Table 17** show that narrower long-CoT SFT helps reasoning while weakening instruction-style control. The paper mentions this, but the abstract and conclusion still read as if “more front-loaded reasoning” is broadly beneficial. The actual message is more conditional: it improves many reasoning tasks, but alignment-style breadth can degrade.

10. **A few presentation details are sloppy enough to create friction.**  
There are several typos and notation inconsistencies, for example “rearch questions” on **Page 5**, inconsistent capitalization of LLM/llm, and some table labels like SCIENCEFT/SCIENCESFT/CODEFT that shift slightly across tables. Also, **Table 2** collapses all 12 SFT runs into two averages, which hides substantial heterogeneity that only becomes visible later in **Tables 10 to 13**. I would strongly prefer the more granular table to be promoted into the main story earlier, because the average-only presentation makes the empirical picture look cleaner than it is.

## Questions
1. The paper’s central budget argument mixes tokens in pretraining and samples in SFT. Can the authors restate the full experimental design using a single budget unit, ideally tokens, and report the approximate token counts used during each SFT condition? This would make Equation (2) and the “controlled token counts” claim much more convincing.

2. How exactly is repetition handled for $\mathcal{D}_{\mathrm{SHQ}}$ in both pretraining and SFT? Since $\mathcal{D}_{\mathrm{SHQ}}$ has only 1.2M examples, but SFT uses 4.8M samples, please specify whether examples are repeated, shuffled across epochs, truncated, or otherwise transformed. This matters a lot for the interpretation of the redundancy and overfitting claims.

3. Did the authors perform any contamination or overlap checks between the pretraining/SFT corpora and the evaluation sets, especially GSM8K, MATH-500, AIME24/25, HumanEval/MBPP, MMLU-Pro, GPQA, and LiveCodeBench? Even a rough deduplication or benchmark-string filtering analysis would increase my confidence materially.

4. For the RL stage, why are only two end-to-end models shown in **Table 3**? If compute limited broader RL coverage, it would still help to explain why these two were selected and whether intermediate cases, such as $\mathcal{M}_{\mathrm{LDQ}}+\mathrm{SFT}_{\mathrm{SHQ}}+\mathrm{RL}$, follow the same trend.

5. Can the authors provide run-to-run variability for at least a few key configurations? The stronger claims about latent effects and subtle dataset-quality differences would be more credible with either multiple training seeds or evaluation confidence intervals.

6. The paper argues that longer answers in $\mathcal{D}_{\mathrm{ALF}}$ indicate higher quality reasoning. Can the authors provide stronger evidence that answer length is a useful proxy beyond anecdotal intuition? For example, reporting quality annotations, teacher model provenance, or error rates would help disentangle “long” from merely “verbose.”

7. The base corpus already contains mathematics and code data. Can the authors narrow their claim accordingly and clarify that the study is about *additional reasoning-style supervision in pretraining*, rather than an absolute absence/presence of reasoning in the base corpus?

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
None beyond the standard concerns associated with large-scale LLM training on web-derived corpora. The paper does not present a specific ethics issue that requires dedicated ethics review based on the main text.

## Soundness Rating
3: good. The experimental program is substantial and many conclusions are directionally supported, but important issues remain around contamination control, repeated-data handling, and the strength of the causal claims relative to the actual evidence.

## Presentation Rating
3: good. The paper is generally readable and well organized, with helpful figures and tables, but some notation, table aggregation choices, and overclaiming hurt clarity.

## Contribution Rating
3: good. This is a useful empirical contribution on training-data allocation across pretraining and post-training, though it is more of a large-scale systematic study than a fundamentally new method.

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected. The paper addresses an important question and backs it with unusually extensive experiments, and the pretraining-versus-SFT asymmetry is a meaningful takeaway. I am still uneasy about contamination, repetition, and some overstrong claims, so this is not a comfortable accept, but I lean positive because the empirical signal is substantial and likely valuable to the community.

## Reviewer Confidence
4: confident. I am familiar with the relevant LLM pretraining/post-training literature and checked the main experimental logic and equations carefully, though I obviously did not reproduce the large-scale runs.