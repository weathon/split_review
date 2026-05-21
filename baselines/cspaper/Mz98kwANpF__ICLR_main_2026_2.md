---
job_id: d6dd5c05-15ab-4cb7-ab35-85ce3b202435
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: Mz98kwANpF.pdf
paper: Align, Don’t Divide: Revisiting the LoRA Architecture in Multi-Task Learning
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, focusing on parameter-efficient fine-tuning, multi-task learning, representation alignment, and adaptation of large language models.

## Minimum Quality
Pass ✅. The paper contains the expected scientific components, including Abstract, Introduction, Related Work, Method, Experiments, Results, and Conclusion; while I have technical concerns about novelty, theory, and evaluation, these are review-stage issues rather than desk-reject-level defects.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, suspicious instructions to automated reviewers, or other manipulative content in the provided manuscript text and figures.

# Expected Review Outcome:
## Summary
This paper revisits the common design choice in multi-task LoRA methods that uses multiple adapters or multiple routed heads to isolate task-specific knowledge. The authors first present empirical observations suggesting that a simplified multi-head variant without routing, M-LoRA, performs better despite exhibiting much higher inter-head similarity, and that a single standard LoRA with larger rank can be competitive with multi-component alternatives.

Motivated by this, the paper proposes Align-LoRA, a single-adapter LoRA trained with an auxiliary alignment loss on the low-rank representation produced by the shared down-projection matrix \( \mathbf{A} \). The paper evaluates KL- and MMD-based variants across several LLM backbones and task collections, and also presents a generalization-bound-style analysis intended to justify why reducing inter-task representation discrepancy should improve multi-task generalization.

## Strengths
1. The paper asks a worthwhile question. The central challenge to the prevailing "more heads, more routing, more specialization" intuition in multi-task LoRA is interesting and relevant. Even if I am not fully convinced by all causal claims, the paper does put useful pressure on an increasingly complicated design trend in PEFT.

2. The empirical observation in Section 3 is thought-provoking. In particular, **Figure 2** on Page 4 and **Table 1** on Page 5 together make a concrete point: R-LoRA achieves lower inter-head cosine similarity than M-LoRA, yet M-LoRA attains the best average performance among the compared multi-head variants. That combination does support the narrow claim that "more diverse heads" is not automatically better in the tested setup.

3. The parameter-efficiency angle is practically relevant. The discussion around mergeability and inference overhead is sensible, and the contrast between routed multi-head designs and a single mergeable adapter is easy to appreciate. **Figure 1** on Page 3 is a useful high-level schematic for this architectural distinction, and it helps the reader understand what family of methods the paper is trying to simplify away.

4. The paper includes comparisons across multiple base models rather than only one, which is better than a single-backbone story. **Tables 2, 3, 4, and 5** indicate that the authors did attempt to test the idea on Qwen and LLaMA families, and on both transfer-style evaluation (BBH) and in-domain multi-task evaluation.

5. The reported gains of the KL-based Align-LoRA variant are not trivial in the main tables. For example, in **Table 4** on Page 8, A-LoRA-K improves over M-LoRA on all three listed backbones while using a similar or smaller trainable-parameter percentage. Likewise, in **Table 5**, A-LoRA-K is consistently strongest on average for both Qwen2.5-3B and Qwen2.5-7B. If these results hold under careful tuning and repeated runs, they would make the method practically interesting.

6. The hyperparameter sensitivity result is at least directionally helpful. **Figure 3** on Page 9 suggests that the method is not working only at one razor-thin value of \( \lambda \), and it also hints at the over-alignment regime the authors discuss.

## Weaknesses
1. **The novelty is weaker than the paper claims, and the framing overstates how much of a conceptual shift this is.**  
   The proposed method is, at its core, a standard LoRA trained with an auxiliary distribution-matching regularizer applied to task-conditioned latent features. That is a reasonable idea, but the jump from this to "a new direction for multi-task PEFT" on Pages 2 and 10 feels inflated. Alignment losses based on KL/MMD are classic tools in domain adaptation and representation learning, and the paper itself explicitly cites that lineage in Section 5.1. What is new here is mainly the placement of that loss inside LoRA's shared low-rank space, not the underlying principle. That is not nothing, but it is more incremental than the paper's rhetoric suggests.

2. **The paper's core mathematical formulation is underspecified in important ways, which makes the method harder to verify or reproduce from the main paper alone.**  
   In Section 5.1, Equation (4) defines the aligned representation as
   \[
   \phi_{T_i}(\mathbf{x}) = \mathbf{A}\cdot X_{T_i},
   \]
   but \(X_{T_i}\) is called "contextualized embeddings" without clarifying whether this is a token-level matrix, a pooled hidden state, the input to each adapted linear layer, or something else. If \(X_{T_i}\) is sequence-valued, then the representation whose Gaussian statistics are computed is not well-defined. Are the authors averaging over tokens, over batch elements, over positions, or over all adapted modules? This matters because the empirical distribution being aligned changes drastically depending on that choice.  
   The same issue affects Equation (5): the paper says each task distribution is modeled as \(\mathcal{N}(\mu_i, \mathrm{diag}(\sigma_i^2))\), but it never writes the actual closed-form symmetric KL used in training, nor how variances are regularized for numerical stability. In practice, diagonal-Gaussian KL requires terms like
   \[
   D_{\mathrm{KL}}(p_i\|p_j)=\frac{1}{2}\sum_d \left[\log\frac{\sigma_{j,d}^2}{\sigma_{i,d}^2} -1 + \frac{\sigma_{i,d}^2 + (\mu_{i,d}-\mu_{j,d})^2}{\sigma_{j,d}^2}\right],
   \]
   and the implementation details are not cosmetic here. Small-batch estimates of \(\sigma^2\) can be noisy or degenerate, especially with many tasks and low-dimensional rank spaces. The paper never explains how this is handled.

3. **The batching/training protocol needed for the alignment loss is not clearly specified, and this is not a small omission.**  
   Equation (5) sums over all task pairs \((T_i,T_j)\), which implicitly assumes that each optimization step has batch statistics available for multiple tasks at once. But the main paper does not say whether training uses mixed-task mini-batches, synchronized per-task sub-batches, memory queues, or some other estimator. Without that information, \(\mathcal{L}_{\text{align}}\) is operationally incomplete. If a batch contains examples from only one task, Equation (5) cannot even be computed. This is exactly the kind of missing training-objective detail that affects both reproducibility and the credibility of the reported gains.

4. **The theoretical analysis is not convincing in its current form, and parts of it appear mathematically shaky.**  
   The main-paper bound on Pages 9 to 10 is presented as a central theoretical justification, but it is too abstract to support the strength of the claimed conclusions. More concerningly, the appendix-level derivation, which the main paper relies on, includes steps that are at best unjustified and at worst incorrect. For example, the identity in Appendix F.4.2,
   \[
   \sum_{i=1}^{M}\Delta(\mathcal{D}_i,\hat{\mathcal{D}})=\frac{1}{2M}\sum_{i=1}^{M}\sum_{j=1}^{M}\Delta(\mathcal{D}_i,\mathcal{D}_j),
   \]
   is not a generic property of KL divergence or MMD as stated. For KL in particular, replacing divergence to a mixture/centroid distribution by average pairwise KL is not an equality in general. Likewise, the confidence-term merger in Appendix F.5,
   \[
   \frac{1}{M}\sum_{i=1}^{M}\sqrt{\frac{\log(M/\delta)}{n_i}} \le \sqrt{\frac{\log(M/\delta)}{n_{\text{total}}}},
   \]
   goes in the wrong direction under standard inequalities; averaging \(1/\sqrt{n_i}\) does not become smaller than \(1/\sqrt{\sum_i n_i}\) in the way claimed. Since the main theorem on Page 10 depends on these reductions, I do not think the theoretical section currently provides reliable support. This matters because the paper repeatedly cites the theory as confirmation of the method's mechanism, not just as loose intuition.

5. **Several empirical comparisons confound architecture, rank, and parameter budget, so the conclusions are not as clean as the paper claims.**  
   This issue shows up repeatedly in **Tables 2, 3, 4, and 5**. For example, in **Table 4**, LoRA uses rank 10, M-LoRA uses rank 4, and A-LoRA variants use rank 8, with slightly different trainable parameter percentages. That means improvements there combine two effects, architecture/training loss and total adaptation capacity. Similarly, in **Table 3**, the single-adapter LoRA baseline is strengthened by increasing rank from 4 to 10, but HydraLoRA, R-LoRA, and M-LoRA are kept at rank 4. This does support the claim that higher-rank single-adapter LoRA can be competitive, but it does not isolate whether Align-LoRA's gains are due to alignment per se versus a more favorable rank/budget choice. A stronger comparison would hold parameter count and rank-space dimensionality more tightly fixed across methods, or at least include A-LoRA at the exact same rank/parameter budget as the strongest LoRA baseline.

6. **The causal story around M-LoRA is too confident relative to the evidence shown.**  
   Section 3.3 argues that the combination of router removal and multi-head dropout turns specialists into collaborators and explains M-LoRA's gains. But this explanation is mostly post hoc. **Table 1** only includes HydraLoRA, HydraLoRA without router, R-LoRA, and M-LoRA. That is not enough to isolate the claimed interaction. If the key hypothesis is "router removal + retained multi-head dropout" then the decisive ablation would include at least: R-LoRA without dropout, M-LoRA without dropout, and perhaps a variant with fixed uniform routing but the same computational graph. Without these, the collaborative-ensemble explanation is plausible storytelling, not evidence.

7. **The paper overgeneralizes from relatively narrow task selections to broad claims about multi-task PEFT design.**  
   The five-task set in Section 3 and the eight-task benchmark in Section 5.2 are useful, but they are still modest slices of the possible multi-task landscape. The paper makes strong claims that architectural isolation is broadly unnecessary and that task-shared representations are the more effective direction. That conclusion may hold in these benchmarks, but it is not established as a general principle. In fact, the paper itself acknowledges the risk of over-alignment in **Figure 3**, and Appendix I.1 explicitly notes that representations should not become identical. So the story is already more nuanced than the main narrative admits.

8. **Presentation is uneven, and some tables/figures hide important details instead of clarifying them.**  
   The writing is readable overall, but several places are sloppy enough to matter. On Page 4, the text says "component diversity are essential"; elsewhere notation flips between \(\dot{\mathcal{D}}_i\), \(\hat{\mathcal{D}}_i\), and \(\bar{\mathcal{D}}\)/\(\tilde{\mathcal{D}}\). The method description relies heavily on appendices for basic operational details. **Table 5** is particularly frustrating because the columns are labeled only as Task1, 2, 3, ..., 8 in the main paper, forcing the reader to cross-reference the appendix to know what is being measured. That makes it harder to interpret where Align-LoRA helps most and whether the gains are concentrated in particular reasoning types.

9. **The figure-based evidence for representation alignment is visually suggestive but scientifically weak in the current form.**  
   **Figure 5** in the appendix is used to support the claim that task representations become closer under Align-LoRA. But t-SNE can easily manufacture apparent clustering or overlap depending on perplexity, initialization, and random seed. Since no quantitative measure accompanies this figure in the main paper, it is closer to an illustration than evidence. If the authors want alignment itself to be a key mechanistic claim, they should report actual pre/post task-discrepancy values, such as mean pairwise KL or MK-MMD in the learned \( \mathbf{A} \)-space, and correlate those with downstream performance.

10. **The experimental reporting lacks uncertainty estimates, which is problematic given the size of several reported improvements.**  
    Across **Tables 1 to 5**, results are presented as single numbers with no standard deviation, confidence intervals, or multi-seed ranges. Some reported margins are small, especially in the BBH tables and in the rank-comparison tables. Without repeated runs, it is hard to know which gains are robust and which may be noise from optimization stochasticity, task sampling, or prompt/evaluation variance. This is especially important when the paper's main thesis depends on relatively fine distinctions between closely related LoRA variants.

## Questions
1. Please specify exactly how \( \phi_{T_i}(\mathbf{x}) \) in **Equation (4)** is computed in practice. Is \(X_{T_i}\) a token-level matrix or a pooled vector? If token-level, how do you aggregate over sequence positions and over layers/modules before estimating \(\mu_i\) and \(\sigma_i^2\)?

2. How is **Equation (5)** computed during training? Does every step contain examples from all tasks, or do you use per-task sub-batches inside a global batch? If tasks are imbalanced, how are pairwise alignment terms weighted? A precise algorithmic description here would substantially increase confidence.

3. Please provide the explicit closed-form symmetric KL objective actually implemented, including any variance floor or \(\epsilon\)-stabilization. Without that, the optimization problem remains underspecified.

4. Can you provide multi-seed results, at least for the key comparisons in **Tables 1, 4, and 5**? Mean \(\pm\) standard deviation over 3 to 5 runs would help determine whether the reported improvements are statistically meaningful.

5. The theory section is currently too loose to support strong claims. Can you either:  
   (a) substantially tighten the proof and correct the problematic equalities/inequalities, or  
   (b) reframe the theory as intuition and stop presenting it as confirmation that Align-LoRA "theoretically" outperforms multi-component variants?  
   A careful response on the validity of the derivation could materially affect my confidence.

6. To support the mechanistic claim in Section 3.3, can you add ablations for M-LoRA without dropout, and R-LoRA without dropout, while keeping other factors fixed? That would directly test whether the observed gain truly comes from the claimed "collaborative ensemble" effect.

7. Can you add a comparison where Align-LoRA and vanilla LoRA are matched exactly in parameter count and rank-space dimensionality, rather than approximately? This would make the case that the gain comes from alignment rather than from capacity allocation much stronger.

8. Since the paper emphasizes representation alignment, please report quantitative alignment diagnostics, for example average pairwise KL/MMD between task distributions before and after training, rather than relying mainly on **Figure 5** and t-SNE plots.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No specific ethics concerns are evident from the main paper. The work studies PEFT and multi-task adaptation methods for LLMs, and does not introduce a dataset collection protocol, human subjects study, or deployment claim that raises an immediate ethics-review flag based on the submitted manuscript.

## Soundness Rating
2: fair. The empirical results are suggestive, but key methodological details of the alignment loss are underspecified, and the theoretical analysis is not reliable in its current form.

## Presentation Rating
2: fair. The paper is readable and the high-level motivation is clear, but several critical details are deferred or ambiguous, notation is inconsistent, and some tables are not reader-friendly.

## Contribution Rating
2: fair. The paper asks a relevant question and reports interesting observations, but the method is a relatively incremental alignment regularizer and the evidence does not fully justify the breadth of the claimed paradigm shift.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted.  
The paper contains an interesting empirical challenge to multi-head LoRA orthodoxy and a practically relevant single-adapter alternative, but the combination of limited methodological novelty, underspecified training objective, unconvincing theory, and not-yet-definitive empirical isolation leaves it short of ICLR bar for me in its current form.

## Reviewer Confidence
4: confident. I am confident in this assessment, though not absolutely certain. I carefully checked the paper's equations, tables, and figures, and my main uncertainty is about implementation details that are not fully specified in the manuscript.