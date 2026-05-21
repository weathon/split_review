---
job_id: d5ddbe3f-63b3-4557-b742-85361d5d40a6
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: nxmBUymHIQ.pdf
paper: LoLoRA: Locally Fine-Tuned Low Rank Adapters
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, focusing on parameter-efficient fine-tuning, optimization, representation learning in transformers, and memory-efficient training for language and multimodal models.

## Minimum Quality
Pass ✅. The submission contains the expected scientific components, including abstract, introduction, related work, method, theory, experiments/results, and conclusion; while I found several important methodological and presentation weaknesses, they do not rise to the level of an immediate desk reject.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, suspicious reviewer-targeting instructions, or other manipulative content in the provided paper text or figures.

# Expected Review Outcome:
## Summary
This paper proposes LoLoRA, a variant of LoRA in which the \(A\) adapter is updated locally during the forward pass using gradient-free or local learning rules, while \(B\) is still trained with backpropagation. The goal is to reduce activation-memory requirements relative to standard LoRA, while avoiding the performance drop often observed when \(A\) is simply frozen as in LoRA-FA. The paper also provides a theoretical analysis of optimal \(A\) under a random regression model, motivating PCA-like subspaces and connecting the method to EVA-style initialization, followed by experiments on GLUE, GSM8K via MetaMathQA fine-tuning, LLaVA visual instruction tuning, and Alpaca ablations.

## Strengths
The paper tackles a practically relevant problem. Reducing activation memory in adapter tuning is important, and the proposed direction, updating \(A\) locally without retaining its input for backward, is a reasonable and technically interesting angle beyond simply freezing \(A\).

I appreciate that the method is conceptually simple. **Figure 1** does a good job showing the distinction between standard LoRA, LoRA-FA, and LoLoRA: in particular, the diagram makes the central engineering claim very clear, namely that LoLoRA keeps \(B\) in the normal backprop loop while moving \(A\) to a forward-pass local update path. That visualization is one of the clearest parts of the paper and helps the reader understand where the claimed memory savings come from.

The paper also makes a decent effort to connect the algorithm to a mathematical rationale rather than presenting it as a pure training trick. The asymmetry between \(A\) and \(B\) in Theorems 4.4 and 4.5, at least at a high level, is a useful perspective and aligns with the experimental emphasis on subspace choice for \(A\).

The experiments span multiple settings, not just one cherry-picked benchmark. The inclusion of text understanding, reasoning, and multimodal fine-tuning is a positive sign, and the ablation tables are useful. In particular, **Table 6** is valuable because it compares several local rules for updating \(A\), rather than only presenting the authors’ preferred variant. The observation that HPCA, HPCA with one-batch SVD initialization, and AE perform similarly, while SoftHebb degrades, gives some insight into which local rules are actually viable.

The paper is also commendably candid in some places about the empirical outcome. For example, the summaries around **Tables 1 and 2** explicitly admit that standard LoRA remains strongest on GLUE, which is more honest than overselling minor differences.

## Weaknesses
I have several concerns, and taken together they substantially weaken the case for acceptance.

1. **The empirical story is weaker than the paper’s framing suggests, and the main method rarely demonstrates a convincing win over simpler alternatives.**  
   The abstract and introduction frame LoLoRA as mitigating the trade-off between memory reduction and quality degradation relative to freezing \(A\). However, in the actual main results, LoLoRA is usually either similar to or slightly worse than strong frozen-\(A\) baselines, and it does not consistently close the gap to standard LoRA. On GLUE, **Tables 1 and 2** show that LoLoRA HPCA is below standard LoRA on most tasks and is not clearly better than LoRA-FA (uniform). For example, on CoLA it is \(66.3\) versus \(67.9\) for LoRA-FA (uniform) and \(69.6\) for LoRA; on MNLI it is \(90.3\) versus \(90.6\) and \(90.8\); on QQP it is \(90.6\) versus \(90.8\) and \(91.7\). This is not a minor detail, it directly undercuts the paper’s main pitch that local online adaptation of \(A\) materially improves over freezing.  
   The reasoning result in **Table 3** is also not very discriminative: LoLoRA HPCA ties LoRA-FA (EVA) at \(0.829\), so the gain seems to come primarily from a better subspace, not necessarily from online local adaptation. In **Table 4**, LoLoRA HPCA is again close to LoRA-FA and slightly behind LoRA (EVA) on perplexity and loss. Overall, the method looks promising but not clearly better than simpler alternatives.

2. **The comparison is not yet strong enough to isolate whether the contribution is “local online learning” or merely “better initialization/subspace selection”.**  
   The paper’s theoretical narrative says the right subspace for \(A\) matters, and the method aims to track that subspace online. But in the experiments, that distinction is not cleanly demonstrated in the main paper. The strongest baseline for the same thesis would be “good initialization of \(A\), then freeze”, especially EVA-style baselines, and indeed those baselines are often just as good or better. For example, in **Table 3**, LoRA-FA (EVA) and LoLoRA HPCA are tied. In **Table 5**, EVA is the best LoRA-FA initialization across ranks. This makes it hard to tell whether LoLoRA adds value beyond reproducing what an informed initialization already gives.  
   A more convincing evaluation would need a direct measurement of the incremental benefit of online updates over a strong initialization, ideally with matched compute, matched rank, and matched memory. Right now the paper implies that non-stationarity makes online updates useful, but the core main-text tables do not demonstrate a robust gain from that mechanism.

3. **The memory savings, while real, are modest and not always compelling relative to the added algorithmic complexity.**  
   The paper emphasizes memory efficiency, but the reported savings are not dramatic in the main results. In **Table 3**, extra memory goes from 30 GB to 26 GB, roughly a 13 percent reduction. In **Table 4**, the reduction is from 24.6 GB to 24.1 GB for LoLoRA HPCA, which is tiny in absolute and relative terms. The GLUE summary claims up to 20 percent less GPU memory, but the main paper does not provide a direct cost-benefit analysis showing when these savings are enough to justify introducing a second training mechanism with its own optimizer state and hyperparameters.  
   This matters because the central trade-off is not only quality versus memory, but also implementation complexity, hyperparameter sensitivity, and runtime. The paper does report runtime in **Table 4**, but does not deeply analyze whether LoLoRA is a better practical operating point than LoRA-FA plus a strong initialization.

4. **The theoretical model is highly stylized, and the bridge from theory to the actual fine-tuning setting is weaker than the paper suggests.**  
   The core result, **Theorem 4.4**, assumes a random regression matrix \(\Delta W_0\) with i.i.d. Gaussian entries and analyzes
   \[
   L(A,B)=\mathbb{E}\frac12\|\tau-BAz\|^2,
   \]
   where \(\tau=\Delta W_0 z\).
   Under that model, optimal \(A\) depends on principal eigenspaces of \(\Sigma_{zz}\). This is mathematically fine as a toy model, but it is a very strong assumption and strips away precisely the structure that matters in real downstream adaptation, namely task-dependent alignment between the target operator and the pretrained model’s representations. If \(\Delta W_0\) is isotropic Gaussian, then the only informative object left is \(\Sigma_{zz}\), so a PCA conclusion is not too surprising.  
   The issue is not that the theorem is false under its assumptions, but that the paper leans on it quite heavily as motivation for the algorithm in actual LLM fine-tuning. The resulting conclusion feels narrower than advertised: the theorem mostly justifies PCA-type \(A\) under a target-agnostic isotropic prior, not under realistic task-conditioned fine-tuning dynamics.

5. **There are mathematical presentation issues and at least one derivational problem that make the theory section harder to trust as written.**  
   The notation is inconsistent across the paper. On **Page 3**, LoRA is first introduced in the general rectangular case on Page 1 as \(B\in\mathbb{R}^{n\times r}\), \(A\in\mathbb{R}^{r\times m}\), but then on Page 3 the paper states “for notational convenience, throughout this paper we assume all matrices are square” and writes \(A\in\mathbb{R}^{r\times n}\), \(B\in\mathbb{R}^{n\times r}\). This convenience is understandable, but several statements then blur whether conclusions depend on square layers or not. Since real transformer projections are not all square in general, the paper should be clearer about which results are dimension-agnostic and which are not.

   More importantly, in the proof of **Theorem 4.4** in Appendix A.1, the displayed rewrite of the loss appears inconsistent. The loss in Equation (2) is
   \[
   L(A,B)=\mathbb{E}\frac12\|\tau-BAz\|^2,
   \]
   but the proof then rewrites
   \[
   L=\frac12\mathbb{E}\|\tau-\Delta W_0 z\|^2,
   \]
   which substitutes \(\Delta W_0 z\) where \(BAz\) should be. That is not a cosmetic typo, it is a substantive change of the optimization variable inside the objective. The subsequent algebra tries to recover the dependence on \(BA\) through optimality conditions, but as written the derivation is sloppy enough that I cannot verify the proof from the main text with confidence. A similar issue appears in Appendix A.2 for Theorem 4.5, where the same type of rewriting occurs.  
   Since the theory is one of the main advertised contributions, these derivations need to be written much more carefully.

6. **Algorithm 1 leaves important implementation details underspecified, which affects reproducibility and even interpretation of the method.**  
   On **Page 4**, Algorithm 1 states:
   1. \(u \gets Az\)  
   2. \(g_A^{\mathrm{loc}} \gets \mathrm{LocalRule}(A,z,u)\)  
   3. update local optimizer state  
   4. step on \(A\)  
   5. \(h \gets Wz + Bu\)
   
   This ordering is unusual and potentially important. Because \(u\) is computed before the update of \(A\), the forward contribution \(Bu\) uses the pre-update \(A\), while the state of \(A\) after the layer has changed for future tokens/batches. That is a valid choice, but the paper never discusses why this order is preferable, whether using post-update \(A\) was tested, or how sensitive performance is to this design.  
   Also, “LocalRule” is too abstract in the main paper. For HPCA, the exact update used at scale matters: is the rule equivalent to Oja/SNL with normalization, with running centering, with per-token or per-batch statistics, with stop-gradient through \(u\), and how is it aggregated across sequence positions and batch elements? These details are partly scattered outside the core method description, but for a method paper the main text should specify the actual update equation at least once. As written, the central local learning rule is underspecified.

7. **The optimization and evaluation protocols are not fully satisfying, especially for fair model selection across methods.**  
   The paper states in **Section 5.2** that GSM8K was evaluated every 0.2 epoch and “the best result is reported for each method.” This raises a concern about model selection on the test benchmark. If GSM8K Platinum is the final evaluation set, then selecting the best checkpoint by repeated test evaluation inflates the result. The paper does not mention a validation split for this experiment or a separate held-out selection criterion. This is not necessarily fatal if clarified, but as written it looks too close to test-set-based model selection.  
   More broadly, the paper tunes different learning rates per method in Appendix Table 9, which is fair in principle, but then the computational budget for hyperparameter search is not reported. Since one of the claimed advantages is practical efficiency, the full tuning burden matters. A method that requires additional optimizer and local-learning hyperparameters but only matches a frozen-\(A\) baseline is less compelling than the tables alone suggest.

8. **The claims around consistency and superiority are overstated relative to the evidence.**  
   The conclusion says that HPCA “consistently outperforms standard LoRA-FA in two out of three experimental setups.” That sentence is doing a lot of work. First, the paper has more than three empirical sections if one includes ablations. Second, even in the three main scenarios, the margins are often tiny and sometimes statistically overlapping. Third, the strongest baseline in some settings is LoRA-FA (EVA), not standard LoRA-FA (uniform), and against that baseline LoLoRA is often tied or worse.  
   This matters because the paper’s practical recommendation depends on whether LoLoRA clearly dominates simpler alternatives. The current evidence is closer to “competitive under some settings” than “preferred method”.

9. **The paper’s relation to prior work is incomplete in one important respect.**  
   The paper discusses EVA, PiSSA, asymmetry of \(A\)/\(B\), local learning, and LoRA-FA, which is good, but the literature review on initialization strategies for very low-cost LoRA seems incomplete. There are other recent works on theoretically motivated initialization or update-approximation-based initialization that are directly relevant to the same question, namely how to choose a good low-rank subspace without paying full fine-tuning cost. This omission makes the positioning feel narrower than it should be.  
   I do not think the paper is unaware of the area, but the current related work section still leaves the novelty boundary somewhat blurry.

10. **Some of the most compelling evidence is pushed outside the main paper, while the main paper itself does not fully close the argument.**  
   The paper’s story about non-stationarity and online tracking of the optimal subspace is plausible, and the supplementary figures on chordal distance are helpful for intuition. However, this is exactly the mechanism that should justify LoLoRA over EVA-style freeze-after-initialization baselines, and yet the main paper does not show that argument cleanly enough through primary task metrics. If the mechanism is central, more of that evidence needed to be in the main paper rather than serving as supporting intuition elsewhere.

## Questions
1. In **Section 5.2**, how exactly was checkpoint/model selection performed for the GSM8K Platinum result in **Table 3**? If the “best result” was chosen by repeated evaluation on the test set every 0.2 epoch, that is problematic. Please clarify whether a separate validation set or another criterion was used for model selection.

2. Can the authors provide the explicit local update equation used for HPCA in the main text, including centering, normalization, batching across tokens, and whether the update is applied per token, per sequence, or per batch? Right now Algorithm 1 is too abstract for the central method.

3. What happens if the ordering in Algorithm 1 is changed so that \(A\) is updated before computing \(u=Az\), or equivalently \(u\) is recomputed after the local update? I would like to know whether the chosen ordering is essential or just an implementation convenience.

4. The theory in **Theorem 4.4** assumes \((\Delta W_0)_{ij}\stackrel{i.i.d.}{\sim}\mathcal{N}(0,\sigma^2)\). Can the authors explain more concretely why this prior is informative for downstream fine-tuning, rather than merely forcing the answer to depend only on \(\Sigma_{zz}\)? A short discussion of what aspects of the conclusion are expected to survive beyond the isotropic Gaussian setting would increase my confidence.

5. Please address the apparent proof issue in Appendix A.1 and A.2 where the loss
   \[
   \frac12\mathbb{E}\|\tau-BAz\|^2
   \]
   is rewritten as an expression involving \(\tau-\Delta W_0 z\). If this is a typo, it should be fixed carefully; if not, I do not follow the derivation. A corrected derivation would materially improve my view of the technical soundness.

6. Can the authors provide a cleaner comparison between LoLoRA and “strong initialization then freeze” under matched memory and matched tuning budget? For example, LoRA-FA (EVA) versus LoLoRA HPCA, with confidence intervals and perhaps learning curves in the main paper. Right now the main tables suggest frequent ties.

7. Since the memory gains in **Table 4** are small, can the authors clarify in which regime LoLoRA is expected to be practically preferable over LoRA-FA? A more explicit wall-clock and memory trade-off discussion would help.

8. A more direct experiment on the claimed non-stationarity mechanism would be valuable. For example, can the authors correlate performance improvements with a measurable drift of the optimal subspace, or show that LoLoRA helps more in layers/tasks with greater subspace drift?

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics concerns are apparent from the paper itself. The work is a methodological study on memory-efficient fine-tuning and does not introduce obvious new risks beyond those already associated with large language and multimodal models.

## Soundness Rating
2: fair. The paper has a plausible method and some useful experiments, but the theoretical derivations are not fully convincing as written, the empirical evidence does not robustly support the stronger claims, and at least one evaluation protocol detail needs clarification.

## Presentation Rating
2: fair. The paper is readable at a high level and Figure 1 is helpful, but the mathematical exposition is loose in places, the core local update is underspecified, and several claims are phrased more strongly than the tables justify.

## Contribution Rating
2: fair. The problem is relevant and the idea is interesting, but the current evidence suggests a modest contribution: LoLoRA is often competitive rather than clearly better, and much of the practical benefit can plausibly be attributed to subspace choice rather than the proposed online local adaptation itself.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The paper is thoughtful and tackles an important systems/optimization issue, but the current version does not yet make a strong enough empirical or theoretical case that LoLoRA is the preferred solution over simpler frozen-\(A\) baselines with good initialization.

## Reviewer Confidence
4: confident. I am familiar with LoRA-style PEFT methods and local-learning literature, and I checked the main equations, algorithms, figures, and tables carefully, although I did not independently re-derive every omitted proof detail.