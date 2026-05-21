---
job_id: 383aa383-91ff-4088-98ff-095ad23beedc
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: Rip3EJc4nx.pdf
paper: High-Fidelity Pruning for Large Language Models
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, focusing on model compression and pruning for large language models, with relevance to efficient large-scale learning and language representation models.

## Minimum Quality
Pass ✅. The submission contains the expected core components, including abstract, introduction, related work, methodology, experiments, quantitative results, and conclusion. While I have concerns about novelty, mathematical precision, and empirical completeness, these issues do not rise to the level of a desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not detect hidden prompts, reviewer-targeted instructions, or other manipulative content in the provided paper text and figures.

# Expected Review Outcome:
## Summary
This paper proposes HFPrune, a structured pruning method for LLM MLP blocks that replaces the conventional one-hot cross-entropy criterion in Taylor-based neuron importance estimation with the entropy of the model output distribution. The method computes neuron scores using first-order Taylor expansion of output entropy, prunes low-scoring hidden neurons in MLP layers, and then applies brief LoRA fine-tuning. Experiments on LLaMA and Qwen models report better zero-shot accuracy than several pruning baselines, along with lower pruning-time cost than SDMPrune.

## Strengths
The paper is easy to follow at a high level, and the core idea is simple enough that one can understand the intended mechanism quickly. In particular, **Figure 2** gives a useful overview of the pipeline, from targeting the MLP hidden neurons to computing importance scores and structurally removing neurons from the SwiGLU MLP. The architectural focus on MLP pruning is sensible for deployment-oriented compression, since those layers indeed dominate parameter count in many LLMs.

The proposed criterion is operationally lightweight compared with self-distillation-based scoring. The paper makes a reasonable practical point that entropy does not require a separate teacher model, and **Table 5** supports the efficiency claim fairly clearly: HFPrune is consistently faster and uses less peak memory than SDMPrune across the listed models. This is one of the more convincing parts of the paper, because the claim aligns well with the algorithmic design.

The empirical section is broader than many pruning papers in terms of model families. The method is tested on multiple LLaMA and Qwen variants, and the reported gains over SDMPrune are mostly consistent in **Tables 1, 2, and 3**. The ablation in **Table 6** is also valuable because it attempts to isolate the effect of the criterion itself without post-pruning fine-tuning, which is closer to the paper’s main methodological claim.

I also appreciate that the authors attempt to validate the “distribution fidelity” story directly rather than only through downstream task accuracy. **Table 7** at least moves in the right direction by measuring JS distance and Top-15 Jaccard similarity between dense and pruned output distributions. Even though I have reservations about the interpretation, this is a better design choice than asserting “better distribution preservation” without any direct measurement.

## Weaknesses
1. **The central conceptual claim, “entropy preserves the full prediction distribution,” is overstated and not well justified mathematically.**  
   The paper repeatedly argues, starting in the Introduction on **Pages 1-2** and again in **Section 4.2**, that using the scalar entropy
   \[
   \mathcal{C}_H(x)=-\sum_{j=1}^{V} p_j(x)\log_2 p_j(x)
   \]
   somehow leads to pruning that “minimizes the change of the global prediction distribution.” This is a much stronger statement than what the objective actually supports. Entropy is a one-dimensional functional of the distribution. Many very different distributions can have the same entropy. Therefore, minimizing first-order changes in entropy does **not** imply preserving the distribution itself, nor even preserving its top-ranked tokens. This matters because the whole motivation of the paper hinges on the idea that cross-entropy is too narrow while entropy is holistic. In reality, entropy is more holistic than one-hot CE in one sense, but it is still a very lossy summary of \(p\), not a fidelity metric between pre- and post-pruning distributions. The text should be much more careful here. A more defensible statement would be that entropy provides a label-free uncertainty-sensitive scalar criterion, not that it directly preserves the full predictive distribution.

2. **The derivation and notation around the importance score are imprecise, and in places mathematically inconsistent.**  
   In **Equation (2)** on **Page 4**, the paper uses
   \[
   \Delta \mathcal{L}_i \approx -\frac{\partial \mathcal{L}}{\partial h_i} h_i
   \]
   for neuron ablation. This is the usual first-order Taylor heuristic, fine. But then in **Equation (4)** on **Page 5**, the paper writes the final importance score as
   \[
   \mathcal{I}_i(x)=\frac{1}{|\mathcal{D}_{\text{calib}}|}\sum_{x\in\mathcal{D}_{\text{calib}}}\left|\frac{\partial \mathcal{C}_{H}(x)}{\partial h_{i}(x)}h_{i}(x)\right|.
   \]
   This is inconsistent notation: the left-hand side depends on \(x\), but the right-hand side averages over all \(x\in\mathcal{D}_{\text{calib}}\), so the result should be dataset-aggregated and no longer indexed by a single input. It should presumably be \(\mathcal{I}_i\), not \(\mathcal{I}_i(x)\). The same sloppiness appears in the surrounding paragraph, which first defines \(\mathcal{I}_i(x)\) as an input-level quantity and then reuses the same notation for the average. This may look minor, but it is exactly the core scoring rule of the method. If the main criterion is not stated cleanly, it becomes harder to assess correctness and reproducibility.

3. **The argument against self-distillation is incomplete and somewhat misleading as presented.**  
   On **Page 2**, the paper claims that self-distillation suffers from a “more critical defect” because the initial distillation loss is zero, leaving no gradient for the initial importance scoring. That statement depends heavily on the exact formulation of the distillation objective, how the teacher and student are instantiated, and whether the student is parameter-tied to the dense model during scoring. The paper does not formalize this argument. If the critique is essential to the motivation, it should be stated with an explicit objective showing where the zero gradient arises. Otherwise, it reads more like a rhetorical contrast than a rigorous limitation of the prior method.

4. **The empirical evaluation is useful but still incomplete for supporting the paper’s stronger claims.**  
   Most comparisons in **Table 3** are only against SDMPrune for the Qwen models, and the paper explicitly says it focuses on “the previous best methods” for brevity. That is convenient for the authors, but not ideal for evaluation. Once the paper claims “consistently outperforms existing pruning methods” in the abstract and introduction, the burden is higher. The stronger claim would require broader baselines across all major settings, not only a subset. Likewise, there is no comparison to unstructured or semi-structured strong pruning baselines, and no comparison to simpler saliency variants such as magnitude-plus-activation heuristics on the exact same experimental setup. This matters because the observed gains are not huge in all places, and the field is crowded with closely related pruning heuristics.

5. **The main gains are modest in several key tables, and the paper tends to overstate them.**  
   In **Table 1**, HFPrune improves average zero-shot accuracy over SDMPrune by only \(0.8\) points at 20% pruning and \(0.7\) at 30% pruning. In **Table 7**, the distribution-fidelity improvements are even smaller: JS distance goes from \(0.243\) to \(0.241\) at 20% and from \(0.362\) to \(0.353\) at 30%; Top-15 Jaccard goes from \(0.439\) to \(0.445\) and from \(0.588\) to \(0.595\). These are directionally favorable, but they are not the kind of margins that justify language like “better preserves intrinsic knowledge” without uncertainty estimates, repeated runs, or variance bars. The paper reports point estimates only. Given the small deltas, it is hard to know whether the advantage is robust or just run-to-run noise, especially after a fine-tuning stage.

6. **The fine-tuning protocol muddies attribution of gains to the pruning criterion itself.**  
   The headline results in **Tables 1-4** are after LoRA fine-tuning on LaMini, as described in **Section 5.1** on **Page 6**. This makes the practical story reasonable, but it weakens causal attribution: some fraction of the advantage may come from interaction with the recovery recipe rather than from better initial pruning scores. The authors try to address this with **Table 6**, which I appreciate, but the retraining-free ablation is only shown on one model family and still uses relatively limited evidence. Since the claimed contribution is specifically the importance criterion, the paper should spend more effort separating “better saliency” from “better end-to-end system after recovery.”

7. **There are multiple exposition and reproducibility issues in the experimental setup.**  
   Several details that matter are either missing or relegated vaguely. For example, **Section 5.1** says “Further implementation details, including specific hyperparameters, are available in the Section A.1 of appendix,” but the review standard here should not rely on the appendix for core reproducibility. In the main paper, I do not see enough detail on how gradients are accumulated across tokens and sequences, whether entropy is computed at every token position or only next-token positions, how padding or sequence truncation is handled in the backward pass, whether importance scores are normalized across layers, and whether pruning is done in one shot or iteratively. **Algorithm 1** on **Page 5** is too high level to resolve these issues. For a gradient-based pruning paper, these are not cosmetic implementation details, they can materially change the scores.

8. **The justification for pruning only MLPs is somewhat underdeveloped and the ablation in Table 8 is not as decisive as the text claims.**  
   The introduction argues that attention-head pruning is too coarse and risky, motivating exclusive MLP pruning. That is a plausible engineering choice, but **Table 8** does not fully isolate the conclusion. It compares “attn&mlp” against “mlp”, but does not normalize for equivalent FLOPs reduction, parameter reduction, or granularity differences in a way that makes the comparison especially clean. Also, if the paper wants to claim a method for “high-fidelity pruning for LLMs” rather than just “entropy-based MLP neuron pruning,” the restriction of the method to a single submodule family narrows the contribution.

9. **The qualitative evidence is not very persuasive and at times undermines the strength of the narrative.**  
   The paper refers to qualitative distribution visualizations in **Figures 3-6** and claims they “visually confirm” the quantitative results. Looking at these figures, the story is mixed. In **Figure 3**, the IE-pruned model is indeed often closer to the original than the CE-pruned one for some prominent tokens, but there are also visible token-level deviations, and the comparison depends strongly on which tokens are included in the Top-15. **Figure 5** is even less compelling: the distributions of prominent tokens differ substantially across all three models, and the superiority of the entropy-based version is not visually obvious enough to support such strong wording. These figures are fine as illustrative examples, but the text oversells them.

10. **Presentation quality is uneven, with repeated claims and several writing issues that hurt precision.**  
   The manuscript is readable overall, but there is a lot of repetition of the same slogans, such as “modeling holistic predictions,” “all potential predictions,” and “minimizing the change of the global prediction distribution,” especially across **Pages 2, 4, and 5**. Repetition would be less problematic if the formal story were sharper, but here it substitutes for rigorous justification. There are also small but noticeable inconsistencies and typos, for example “fully represent holistic predictions” in the caption/text around **Figure 1**, inconsistent model names in the Qwen tables, and unclear wording such as “the initial distillation loss is zero” without mathematical support. These issues do not make the paper unreadable, but they do make the contribution feel less mature than it could be.

11. **The literature positioning is only partially convincing.**  
   The related work section mentions entropy-based pruning in other contexts, but the paper still presents the entropy criterion as if it were a more substantial conceptual leap than it actually is. Given how many pruning papers already modify saliency criteria, the burden is not just to say “ours uses entropy instead of CE,” but to explain why this particular scalar is the right one among other label-free or distribution-aware options, such as KL-based teacher-free surrogates, confidence margins, logit-energy criteria, or Fisher/Hessian-informed approximations. The paper does not really answer that, beyond intuition.

## Questions
1. The paper’s main wording suggests that entropy-based Taylor pruning “minimizes the change of the global prediction distribution.” Can the authors either justify this formally, or soften the claim? In particular, can they explain why preserving a scalar entropy functional should be expected to preserve the distribution itself, rather than only some aspect of its uncertainty?

2. Please clarify the exact definition of the scoring rule in **Equation (4)**. Should the left-hand side be \(\mathcal{I}_i\) rather than \(\mathcal{I}_i(x)\)? Also, is the score accumulated over all token positions in each 1024-token sequence, or only the final next-token prediction? This point is central to reproducibility.

3. How exactly is \(\nabla_{h(x)} \mathcal{C}_H(x)\) computed in practice for causal LM inputs? Is entropy computed at every position and summed, averaged, or sampled? Are tokens weighted equally? A concrete formula for the sequence-level objective used during calibration would materially increase confidence.

4. For the comparison to self-distillation on **Page 2**, can the authors provide the exact objective that leads to the claimed zero-gradient problem at initialization? Right now this criticism is asserted, but not demonstrated.

5. Can the authors report variance across multiple pruning and fine-tuning runs, at least for the key comparisons in **Tables 1, 6, and 7**? Because several reported gains are small, confidence intervals or standard deviations would help determine whether the advantage is robust.

6. Can the authors provide stronger direct evidence that entropy, rather than recovery fine-tuning, is driving the gains? For example, more no-tuning ablations on additional model families, or correlations between score ranking and actual ablation damage.

7. Why is the method restricted to uniform per-layer pruning ratios in **Algorithm 1**? Since the whole pitch is about fidelity, I would expect some layers to be much more entropy-sensitive than others. Did the authors try layer-adaptive sparsity allocation, or at least analyze score distributions across layers?

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics concerns are apparent from the paper itself. The work studies model compression for deployment efficiency and does not introduce a new dataset or human-subject protocol in the main paper.

## Soundness Rating
2: fair. The core method is plausible and the experiments are reasonably broad, but several central claims are stronger than what the math and evidence actually support, and key implementation details of the scoring objective are underspecified.

## Presentation Rating
2: fair. The paper is understandable at a high level, with useful diagrams such as **Figure 2**, but the writing is repetitive and imprecise in several important places, especially around the formal meaning of the entropy objective and the exact scoring rule in **Equation (4)**.

## Contribution Rating
2: fair. The paper offers a practically useful pruning variant and some empirical gains, but the conceptual advance over existing Taylor-based pruning criteria feels incremental, and the evidence does not fully justify the stronger distribution-fidelity framing.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The idea is practical and the empirical results are decent, but the paper overclaims what entropy is optimizing, the formulation is not as crisp as it needs to be, and the improvements, while consistent, are not strong enough to offset the novelty and rigor concerns for ICLR main track.

## Reviewer Confidence
4: confident. I am confident in this assessment, though not absolutely certain. The pruning setup and empirical findings are clear enough to evaluate, and I checked the core equations and tables carefully, but some missing implementation details limit absolute certainty.