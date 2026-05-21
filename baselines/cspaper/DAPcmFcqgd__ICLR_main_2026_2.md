---
job_id: 841e17a7-c10a-410a-b8b6-ebbf320fd08f
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: DAPcmFcqgd.pdf
paper: MoEP: Compact and Efficient Sparsity with Modular Expert Paths
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, focusing on sparse / modular transformer architectures, routing, and language representation learning under fixed parameter budgets.

## Minimum Quality
Pass ✅. The submission contains the expected scientific components, including abstract, introduction/background, methodology, experimental setup, quantitative results, and conclusion/discussion. While there are notable issues in clarity, positioning, and empirical validation, these do not rise to the level of a desk reject.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, reviewer-targeted instructions, or other manipulative content in the paper text or figures.

# Expected Review Outcome:
## Summary
This paper proposes MoEP, a decoder-only sparse language model architecture that combines two routing mechanisms under a fixed parameter budget: token-level top-$k$ routing across parallel transformer blocks, and MoE-style shrink/grow projection blocks between high- and low-dimensional hidden spaces. The main empirical study is conducted on the BabyLM strict-small track, where the authors compare MoEP and a MoEP-SwiGLU variant against GPT-2-style and BabyLM baseline models, and analyze training dynamics via checkpoint-based evaluation curves.

## Strengths
The paper explores an interesting design point that is under-discussed relative to standard FFN-level MoE, namely layer-level routing through parallel transformer blocks while attempting to keep total parameter count fixed. That is a reasonable and potentially useful question: can one obtain some of the benefits of sparse conditional computation without paying the usual total-parameter explosion of conventional MoE?

The high-level architectural idea is easy to grasp from **Figure 2**. In particular, the shrink $\rightarrow$ routed parallel stack $\rightarrow$ grow pattern makes the intended compute pathway quite clear, and the figure helps distinguish the two sources of sparsity better than the text alone. Likewise, **Figure 1** does a useful job contrasting the proposed layer-level placement with attention/FFN-level expert placement, which helps readers understand what the paper is actually changing.

The paper targets a constrained-data, constrained-compute regime rather than another large-scale benchmark arms race. Even though this also becomes a weakness for significance claims, there is still some value in studying compact sparse architectures in the BabyLM setting, especially if the goal is to test whether routing helps sample efficiency at small scale.

The quantitative results in **Table 1** suggest that MoEP is at least competitive in this narrow evaluation setting. Relative to the authors' own GPT-2 baseline, MoEP improves the reported macro average from 48.10 to 49.00 and shows especially large gains on Entity Tracking and WSC. The model also appears to outperform the listed Hugging Face GPT-2 baseline. These are not huge margins, but they are non-zero and directionally supportive of the paper's central claim that fixed-budget sparsity can be viable.

The checkpoint analyses in **Figures 3-5** are helpful as diagnostic evidence. Even if the analysis is fairly lightweight, the plots support the authors' claim that MoEP learns differently from the dense GPT-2 baseline, with earlier gains on some tasks and different stability profiles over training.

## Weaknesses
1. **The empirical scope is too narrow to support the broader claims made in the introduction and conclusion.**  
   The paper repeatedly frames MoEP as a meaningful alternative to the standard dense-to-sparse scaling trend in LLMs, for example in the abstract and **Section 1**, but all evidence comes from a single small-data BabyLM setup with approximately 10M words and models around 28M parameters (**Page 6**, **Table 2**). This matters because the central motivation of sparse routing is usually about compute-quality tradeoffs at scale, where routing behavior, specialization, optimization instability, and communication patterns look very different from a BabyLM strict-small setting. The authors themselves acknowledge in **Section 6** that it is unclear whether the relative performance would persist when scaling model size and training data. That caveat is important, but it also substantially limits the scientific reach of the paper. As written, the work demonstrates at most a promising small-scale architecture variant, not convincing evidence for a generally useful sparse modeling direction.

2. **The gains are modest and the comparison story is muddled, especially in Table 1.**  
   The paper says MoEP "outperformed all BabyLM strict-small baseline models" (**Page 2**), but **Table 1** does not cleanly support that statement. The listed GPT-BERT baselines achieve much higher macro averages, e.g. 54.10 and 53.65, than MoEP's 49.00. The text on **Page 6** then narrows the claim by emphasizing AoA inclusion/exclusion and by saying GPT-2 is the primary comparison point, but this is not handled consistently. This is a serious presentation and scientific issue because the headline claim overstates what the presented table shows. Also, some models include AoA and others do not, and the table caption describes "two macro averages" while only one "Avg" column is visible in the table. The evaluation framing therefore feels slippery rather than rigorous. If the intended claim is "MoEP beats GPT-2-like baselines under matched parameter budget," then the paper should say exactly that and present a table that directly supports it.

3. **The method description leaves key implementation details underspecified, especially around routing and aggregation.**  
   In **Section 3.3**, the paper states that the router applies token-level top-$k$ selection among $P$ parallel blocks and that "the routed inputs are summed up together." This is too vague for a core architectural mechanism. Are router logits softmax-normalized before top-$k$? Are selected block outputs weighted by normalized gate probabilities, by raw scores, or equally averaged/summed? Is there any capacity constraint per block? How is dispatch implemented during training and inference? Similar issues arise in **Section 3.2** for the MoE shrink/grow blocks. The paper says experts are selected with top-$k$ gating, but does not define the routing function mathematically. A minimal specification would include something like
   \[
   g(x)=\mathrm{TopKSoftmax}(W_r x), \qquad y=\sum_{e=1}^{E} g_e(x)\, f_e(x),
   \]
   or an explicit hard-routing alternative. Without that, the method is not fully reproducible from the main paper, and it is difficult to reason about whether the comparisons are fair or whether the architecture is closer to sparse weighted ensembling versus true conditional execution.

4. **The loss formulation in Equations (2) and (3) is under-motivated and possibly inconsistent with the stated objective.**  
   The balancing term is defined in **Equation (2)** as
   \[
   \mathcal{L}_{\text{balance}}=-\sum_i p_i \log p_i,
   \]
   and then added in **Equation (3)** with positive coefficients:
   \[
   \mathcal{L}=\mathcal{L}_{\text{CE}}+\lambda^{\text{block}} \mathcal{L}_{\text{balance}}^{\text{block}}+\lambda^{\text{expert}} \mathcal{L}_{\text{balance}}^{\text{expert}}.
   \]
   If training minimizes $\mathcal{L}$, adding the negative entropy term with a positive $\lambda$ encourages *lower* entropy, not higher entropy, unless the authors intended to maximize entropy through the sign convention. The text says the purpose is to avoid collapse and encourage stable utilization, which usually implies encouraging more uniform usage. As written, the sign is confusing at best and possibly wrong. At minimum, the authors need to clarify whether they optimize $+\sum_i p_i \log p_i$, or equivalently subtract entropy, or whether the optimizer is maximizing this term. This is not a cosmetic issue, because it directly affects the stated anti-collapse mechanism.

5. **The paper does not isolate which component is actually responsible for the reported gains.**  
   MoEP combines several changes at once: reduced hidden dimension in the middle stack, parallel block structure, top-$k$ block routing, top-$k$ expert routing in shrink/grow projections, and a balancing regularizer. Yet there is no ablation disentangling these factors. A key missing comparison would be a parameter-matched dense parallel model with the same shrink/grow dimensionality changes but *without* sparse routing. Another needed baseline is MoEP with $k=P$ or dense averaging over all blocks, to test whether the gain comes from modularity versus sparsity. Similarly, the impact of the auxiliary loss coefficients is never studied. This omission matters because the current results do not show that sparse modular routing, rather than just architectural reallocation of parameters, is the main source of improvement.

6. **The paper claims improved learning efficiency, but the evidence is weak and partially confounded by checkpoint selection.**  
   The authors state in the abstract and **Section 5.1** that MoEP accelerates learning and extracts useful patterns earlier. The supporting evidence is mainly the checkpoint plots in **Figures 3-5** and the claim that the best MoEP checkpoint occurs earlier than MoEP-SwiGLU. However, the dense GPT-2 baseline is also reported to peak at 30M words (**Page 6**), which undercuts the claim of superior sample efficiency relative to the main baseline. Moreover, the final model is chosen based on the best evaluation checkpoint, and the paper does not clearly distinguish validation-based selection from test-like benchmark inspection. The plots are interesting, but as presented they do not strongly establish a learning-efficiency advantage over GPT-2.

7. **There are signs of evaluation protocol weakness, especially around model selection.**  
   On **Page 6**, the authors say they saved checkpoints, ran "fast evaluation" on all checkpoints, and selected final model weights from the checkpoint with the best evaluation performance. It is not clear whether this "fast evaluation" used a held-out validation set or benchmark tasks that overlap with the final reported evaluation. If the same BabyLM evaluation suite was used for checkpoint selection and final reporting, that is a methodological problem. The paper needs to explicitly state what data/tasks were used for model selection, and whether any test or benchmark metrics informed checkpoint choice. Right now the wording is loose enough to raise concern.

8. **The literature positioning is incomplete for the specific claim of modular sparse routing.**  
   The related work covers many MoE and PEFT papers, but it misses some closely relevant modular sparse transformer work. In particular, a stronger comparison and discussion against modular sparse language models such as **ModuleFormer** would help situate what is truly new here. More broadly, the paper cites several large MoE systems, but the novelty claim remains blurry because MoEP is essentially a combination of top-$k$ routing and parallel blocks under a fixed budget. The paper needs a sharper articulation of what prior layer-level or modular routing papers cannot already do, and why this exact design is scientifically distinct rather than just an intuitive recombination.

9. **The fixed-parameter-budget claim is not handled consistently across model variants.**  
   The abstract and introduction emphasize adding sparsity "while keeping the total parameter count fixed." Yet **Table 2** shows MoEP-SwiGLU at 38M parameters versus 28M for GPT-2 and MoEP. That weakens the paper's messaging, because one of the two proposed variants does not satisfy the flagship constraint. If the fixed-budget claim applies only to the baseline MoEP variant, the paper should clearly limit that claim rather than presenting both under the same umbrella.

10. **Presentation quality is below ICLR standards in its current form.**  
   The paper is readable overall, but there are many grammatical issues, typos, and terminology inconsistencies that accumulate into genuine ambiguity. Examples include inconsistent notation in **Section 3.3**, where the set of parallel blocks is written as $\{B_1,\dots,B_K\}$ even though the number of blocks is denoted by $P$; "Layer" and "Layer Block" are used inconsistently; "lambda learning weight" in **Equation (3)** is not properly defined; and several baseline/model names in **Table 1** appear misspelled or inconsistent ("GTP-29", "casual" instead of "causal", "SwGLU" vs "SwiGLU"). These are not merely stylistic nits. In a routing paper, notation precision matters because readers need to understand exactly what is being gated, at what granularity, and with which normalization.

11. **The figures used for qualitative analysis are suggestive but not sufficiently tied back to quantitative conclusions.**  
   **Figures 3-5** show smoothed deviation from task means over training, but the y-axis statistic is unusual and not very interpretable without a clearer definition. Why is deviation from task mean the right normalization, and how does it relate to actual benchmark performance? The plots visually suggest different learning dynamics, but because the paper does not report variance across runs, confidence intervals, or seed sensitivity, these curves could easily reflect noise, especially in a small-data regime. The figures are useful as exploratory diagnostics, but they are not strong evidence for the paper's broader claims about learning behavior.

## Questions
1. Please clarify the exact routing computation for both the shrink/grow MoE blocks and the parallel layers.  
   Concretely, what are the router logits, how is top-$k$ applied, are selected experts/blocks weighted by normalized probabilities, and is the final output a weighted sum, unweighted sum, or average? A precise mathematical definition of the forward pass would substantially increase my confidence.

2. Please clarify the sign convention in **Equations (2) and (3)**.  
   If $\mathcal{L}_{\text{balance}}=-\sum_i p_i \log p_i$ is added to a minimized objective with positive $\lambda$, it appears to encourage lower entropy rather than balancing. Is there a typo in the equation, a missing minus sign in **Equation (3)**, or some other convention being used?

3. What exactly was used for checkpoint selection on **Page 6**?  
   Was the "fast evaluation" run on a held-out validation set, on a subset of BabyLM tasks, or on the official evaluation suite? If benchmark tasks informed model selection, that would materially affect the strength of the empirical claims.

4. Can the authors provide ablations that isolate the role of routing?  
   The most important missing comparisons, in my view, are:  
   (a) parameter-matched dense parallel blocks without routing,  
   (b) MoEP with dense use of all blocks,  
   (c) MoEP without the auxiliary balancing loss,  
   (d) sensitivity to $k$, $P$, and $E$.  
   Even a compact version of these in rebuttal would help determine whether the reported gains are really from sparse modular expert paths.

5. How should **Table 1** be interpreted given the apparent discrepancy between the text and the listed GPT-BERT macro averages?  
   Please rewrite the claim precisely and, if needed, provide separate tables for "excluding AoA" and "including AoA" so that the comparison is unambiguous.

6. Do the reported improvements hold across multiple random seeds?  
   In this small-data regime, single-seed differences of around 0.5 to 1.0 macro points may not be very stable. Evidence of variance would be very helpful.

7. Since **Table 2** shows MoEP-SwiGLU has 38M parameters, can the authors clarify whether the fixed-parameter-budget claim applies only to MoEP and not to the SwiGLU variant?  
   This should be made explicit in the abstract and contributions if so.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No specific ethical concerns stood out from the paper. The work is a standard language modeling architecture study on an established benchmark, and the paper does not introduce a distinctive safety, privacy, or human-subjects issue beyond ordinary concerns associated with language model research.

## Soundness Rating
2: fair. The core idea is plausible and some empirical evidence is provided, but key methodological details are underspecified, the balancing loss formulation is questionable as written, and the experimental evidence is too limited to fully support the paper's broader claims.

## Presentation Rating
2: fair. The high-level idea is understandable and the main figures help, but the writing contains many inconsistencies, ambiguous claims, and notational issues that materially reduce clarity.

## Contribution Rating
2: fair. The paper explores an interesting compact-sparsity design point and shows some encouraging BabyLM results, but the novelty relative to modular/routed transformer literature is not sharply established and the empirical scope is too narrow for a stronger contribution rating.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The idea is interesting and there is a real signal here, especially the attempt to study fixed-budget sparsity rather than simply scaling total parameters. However, the current submission overclaims relative to the evidence, does not sufficiently specify key routing details, has a potentially problematic loss formulation, and lacks the ablations needed to isolate the source of gains. With tighter methodology and clearer positioning, this could become a stronger paper.

## Reviewer Confidence
4: confident. I am confident in the overall assessment and carefully checked the method description, equations, figures, and main experimental claims, though some implementation details are missing from the paper and prevent absolute certainty.