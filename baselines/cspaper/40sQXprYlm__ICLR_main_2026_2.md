---
job_id: 6b4cd2bc-4562-457c-840e-0d45d3bebb16
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: 40sQXprYlm.pdf
paper: Towards Distributed Neural Architectures
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, focusing on conditional computation, adaptive neural architectures, representation learning in vision and language, and interpretability of learned routing patterns.

## Minimum Quality
Pass ✅. The submission contains the necessary components of a research paper, including abstract, introduction, methodological description, experiments, quantitative results, qualitative analysis, and conclusion. While I have substantial concerns about empirical strength, positioning, and methodological clarity, these are review-level weaknesses rather than desk-reject issues.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, suspicious instructions targeting automated reviewers, or other manipulative content in the provided paper text.

# Expected Review Outcome:
## Summary
This paper introduces distributed neural architectures (DNA), a modular routed architecture in which tokens or patches can traverse dynamically chosen sequences of modules, potentially including attention, MLP, or full transformer blocks. The paper studies DNAs in both ImageNet classification and language modeling on FineWeb-Edu, argues that the framework generalizes several conditional-computation paradigms such as MoE and adaptive depth, and provides qualitative analyses of emergent routing, path distributions, specialization, parameter reuse, and compute allocation.

## Strengths
The paper aims at a genuinely interesting architectural question: whether one can move beyond fixed layer-wise transformer pipelines to more flexible token-dependent computation graphs. This is a worthwhile direction for ICLR, especially because it cuts across conditional computation, representation learning, and interpretability.

I appreciated that the paper does not only present a mechanism but also tries to analyze what the trained models are doing. The qualitative analyses are one of the stronger parts of the submission. In particular, **Figure 1** is useful as a conceptual overview of the proposed architecture from both the module and token perspectives, and the later qualitative panels in **Figure 1(e,f)** give a concrete sense of what the authors mean by “path specialization”. Even if I am not fully convinced by all of the interpretability claims, the paper at least makes a real effort to interrogate the learned routing behavior rather than stopping at benchmark numbers.

The vision experiments are reasonably broad for a first paper on this idea. The training curves and routing visualizations in **Figure 2** help show that the models are trainable, and the bottom row of **Figure 2** does communicate an important empirical pattern, namely that routing seems relatively dense early and more distributed later. That observation is one of the more concrete takeaways in the paper.

The language experiments include both pretraining loss and a small set of downstream zero-shot evaluations. **Table 3** is especially helpful here because it shows a somewhat nuanced picture rather than cherry-picked wins: the top-2 DNA improves over the GPT-2 baseline on some metrics and validation loss, while top-1 underperforms. That kind of mixed result is actually informative and more credible than an all-win table.

Another positive point is that the paper attempts to study compute allocation rather than only accuracy. The skip-enabled variants and analyses in **Figure 5** for vision, plus the corresponding language discussion in Section 4.3, reflect an effort to connect routing to efficiency and not just representational flexibility.

Finally, the paper is ambitious in scope. It covers vision and language, top-1 and top-2 routing, compute-skipping variants, and additional experiments where transformer blocks are split into attention and MLP submodules. Even though this breadth also contributes to some weaknesses below, the overall ambition is notable.

## Weaknesses
I found the paper interesting but not yet convincing as an ICLR main-track contribution. My concerns are mostly about empirical support, comparison fairness, and methodological/specification clarity.

1. **The central empirical claim of being “competitive” is only weakly supported, and in vision it is arguably overstated.**  
   The abstract and introduction repeatedly frame DNAs as competitive with dense baselines, but the actual evidence is mixed. In vision, **Table 1** and **Figure 2** suggest that the main top-1 DNA is below ViT-small in accuracy, while the top-2 skip model appears close but not clearly stronger, and it also changes model width and embedding dimension. The top-1 DNA has more total parameters than ViT-small, 34M vs 22M in **Table 1**, while matching only the active parameter budget. That is not an apples-to-apples comparison if the headline message is architectural superiority or even parity under comparable resources. A system with substantially more total capacity but similar active compute is a different tradeoff point. This matters because the paper’s pitch is not just “we can train something”, but “this is a meaningful alternative to standard architectures”. Right now the evidence is closer to feasibility than competitiveness.

2. **The baseline selection and resource matching are not strong enough to isolate the value of the proposed architecture.**  
   This issue appears in both domains. For vision, **Table 1** compares DNAs to a single ViT-small baseline, but the DNA variants differ in total parameter count, active parameter count, width, and number of modules. For language, **Table 2** and **Table 3** compare top-2 DNA with 433M active params / 603M total params against GPT-2 medium with 406M total params. Again, the comparison is not clean. The top-2 DNA does better than GPT-2 on several metrics in **Table 3**, but it also has more active parameters and far more total parameters. If the claim is about better use of compute or more flexible computation, I would expect stronger controlled baselines, for example: same active FLOPs, same total parameters, same training compute, or a Pareto curve. Without that, it is too easy to attribute gains to scale or altered capacity allocation rather than the DNA mechanism itself.

3. **The paper makes broad generalization claims relative to MoE, MoD, parameter sharing, early exit, etc., but does not adequately differentiate what is actually new versus what is inherited from prior conditional-computation literature.**  
   Section 2 and Appendix B argue that DNA is a generalization of multiple routed or sparse-compute paradigms. Conceptually that is plausible, but the paper does not sharply identify which capabilities are truly unavailable in prior architectures, and which are simply recombinations of known ingredients: token-level routing, top-\(k\) selection, identity/skip modules, sparse attention induced by routing subsets, and modular blocks. This weakens the novelty positioning. More importantly, the experimental section does not compare against strong representatives of these families, despite the paper explicitly positioning DNA as a superset of them. If the framing is “generalization of mixture-of-X”, then the burden is to show either a clearly new functional regime or a compelling empirical benefit from that generalization. I did not see that demonstrated cleanly.

4. **The method description is underspecified in places, especially around routing/training, and this makes it harder to judge correctness and reproducibility.**  
   The core update in **Equation (1)** is not fully clear. The notation mixes token-specific and module-specific quantities in a way that is easy to misread:
   \[
   \mathbf{h}^{(s+1,t)}=\mathbf{h}^{(s,t)}+\sum_{i\in \mathrm{top}\text{-}k_*(\rho^{(s)}_i)} \rho^{(s)}_i\left(M_i^t(\mathbf{h}^{(s)}_i)-\mathbf{h}^{(s,t)}\right).
   \]
   Here, \(\rho^{(s,t)}\) is defined just above as the routing distribution for token \(t\), but in the sum the paper writes \(\rho^{(s)}_i\), dropping the token index. The set \(\mathrm{top}\text{-}k_*(\rho^{(s)}_i)\) is also awkwardly defined, and it is unclear whether this is top-\(k\) for token \(t\), top-\(k\) over modules globally, or a shorthand for the token-specific chosen indices. Since the entire architecture hinges on token-wise routing, this indexing ambiguity is not cosmetic. It affects how one interprets the forward pass, gradient flow, and whether the update is a convex combination or a residual mixture over chosen modules. This should be rewritten much more carefully, for example with explicit token-indexed selected set \(\mathcal{I}^{(s,t)}=\mathrm{TopK}(\rho^{(s,t)})\), followed by
   \[
   \mathbf{h}^{(s+1,t)}=\mathbf{h}^{(s,t)}+\sum_{i\in \mathcal{I}^{(s,t)}} \tilde{\rho}^{(s,t)}_i\left(M_i(\mathbf{h}^{(s)}_i)_t-\mathbf{h}^{(s,t)}\right),
   \]
   and a clear statement of whether \(\tilde{\rho}\) is renormalized after top-\(k\) truncation.

5. **The treatment of hard top-\(k\) routing and optimization is not sufficiently explained.**  
   In Section 2.2 the routers use softmax probabilities, then “the routing decision is made by sampling with hard top-\(k\).” But the paper does not explain the training estimator for this discrete decision. Is the top-\(k\) operation treated with a straight-through estimator, is the hard mask only used in the forward pass while gradients flow through the soft weights, or is there some other surrogate? This is a central optimization detail, not an implementation footnote. The paper says modules and routers are optimized jointly and cites prior work for signal/gradient propagation, but that does not resolve the missing explanation for the discrete gate. Because trainability is one of the paper’s core claims, the absence of a precise routing-gradient description materially reduces confidence.

6. **The compute-efficiency mechanism via the bias trick is heuristic, and its objective relation is unclear.**  
   **Equations (2) and (3)** introduce bias terms that alter top-\(k\) selection toward identity modules, with the biases decoupled from autograd. This is an interesting engineering choice, but the paper then uses it to support claims about learned compute allocation. The problem is that the optimization target is not written as a principled loss with a compute regularizer; instead it is an external control rule:
   \[
   b_i^{(s)}(t+1)=b_i^{(s)}(t)+u\cdot \mathrm{Sign}\left(rk\bar c^{(s)}(t)-\sum_{i\in \mathrm{Id}} c_i^{(s)}(t)\right).
   \]
   There are several issues here. First, the update is discontinuous and global, which may create unstable or oscillatory behavior. Second, the notation is confusing because the left-hand side updates a single \(b_i^{(s)}\), but the right-hand side sums over all identity modules. Third, the relationship between \(r\), target skip fraction, and realized compute is not derived. Fourth, because the biases are explicitly outside autograd, the resulting “learned compute efficiency” is partly imposed by a hand-designed controller rather than learned end-to-end from a scalar objective. This matters because the paper’s framing suggests a unified trainable architecture, while the actual skipping behavior depends on a fairly ad hoc side mechanism.

7. **Some of the interpretability claims are much stronger than what the presented evidence warrants.**  
   The paper repeatedly states that paths, routing choices, and compute allocation are “human-interpretable.” In places this feels overstated. For example, in **Figure 3** the patch examples for selected path ranks are visually suggestive, but the evidence is anecdotal and based on a few hand-picked paths. It is not clear how stable these semantic groupings are across seeds or how much they exceed what one would get from a simpler clustering of patch embeddings. The paper itself notes in Section 3.2 and Appendix G.2 that even a randomly initialized model can cluster patches in nontrivial ways. That is an important caveat that directly weakens the claim that the observed path organization reflects meaningful emergent semantics due to training. Similarly, the “sentence-level attention” interpretation for punctuation paths in language, discussed around **Figure 1(f)** and **Figure 8**, is plausible but not rigorously validated.

8. **The power-law path distribution result is intriguing but underdeveloped, and some of the narrative around it is too casual.**  
   **Figure 1(c,d)** shows path rank-frequency plots and notes that even random models exhibit an approximate power law with exponent around \(-1\). This is actually a potentially important observation, because it suggests the path-distribution phenomenon may arise at least partly from combinatorial structure or initialization, not from learned specialization. Yet the paper does not really follow through on that implication. If random routing/path composition already gives a similar law, then the mere existence of a power law is not compelling evidence of emergent structure. The paper should separate “power-law path frequencies” from the more meaningful question of what changes after training, such as concentration, semantic purity, mutual information with labels, or module specialization statistics.

9. **The efficiency story is not convincing from a systems perspective, and the paper itself partially concedes this.**  
   The main text and Appendix A state that the current implementation is slower and uses more memory than dense baselines due to dynamic sequence lengths and attention-mask generation. That honesty is appreciated, but it also means the practical case for DNA as an efficiency method is currently weak. In a paper strongly motivated by inference efficiency, this gap matters. The experiments mostly show reduced nominal active compute or parameter reuse, not end-to-end speedups or hardware-efficient execution. For ICLR, proof-of-concept is acceptable, but then the efficiency claims should be framed more carefully as architectural potential rather than demonstrated practical savings.

10. **The language evaluation is too limited to support broad claims.**  
    The language models are trained for 21B tokens, and **Table 3** reports validation loss plus a small set of zero-shot tasks. This is useful, but still fairly narrow given the ambition of the paper. More importantly, the top-2 gains are modest and uneven, while the skip-enabled model degrades noticeably on several tasks relative to the shallower GPT-2 baseline. For instance, in **Table 3**, top-2 (30% skip) performs worse than GPT-2 (30% shallower) on several downstream tasks and much worse on Wiki perplexity. That weakens the narrative that the model “learns to use less compute with minor effects on performance.” In language, the effect is not minor by the table shown.

11. **There is a mismatch between the broad conceptual claims and the relatively narrow experimental regime.**  
    The paper speaks about DNAs as a general architecture class with arbitrary module types, communication patterns, and future co-designed distributed infrastructure. But the actual experiments use fairly constrained router placement, a capped number of steps, mostly transformer-like modules, and in practice some hard-coded dense backbone layers. I do not object to studying a restricted instance, but then the claims should be narrower. As written, the paper sometimes sounds like a general theory of distributed architectures, whereas the evidence is for a particular family of routed transformer variants.

12. **Presentation quality is uneven, with several unclear phrases, notation issues, and occasional overclaiming.**  
    There are many places where the exposition is rough. A few examples: Section 2.1 says “Any token can traverse any series of modules in any order”, but the architecture later imposes step-indexed routers and a finite \(s_{\max}\), which is much more structured than “any order”. Section 3.2 contains multiple awkward or ambiguous sentences, for example “each patch follows a patch described by 12 integers”, which seems to be a typo for “path”. Appendix A says “the complete set of hyperparameters reported in Fig. 1” while the actual tables/hyperparameters are elsewhere. These are not fatal, but they accumulate and reduce confidence that the paper has fully pinned down the method.

## Questions
1. **Can the authors provide a cleaner and fully explicit formulation of the routing/training mechanism in the rebuttal?**  
   In particular, please restate **Equation (1)** with consistent token/module indices, define the selected set for each token unambiguously, and explain exactly how gradients are handled through hard top-\(k\) routing during training. A precise statement here would substantially increase my confidence in soundness and reproducibility.

2. **How much of the observed improvement comes from architecture versus resource changes?**  
   A very helpful rebuttal would include controlled comparisons at matched total parameters, matched active parameters, or matched training FLOPs, especially for the strongest language result in **Table 3**. Right now the positive result for top-2 DNA is hard to attribute cleanly.

3. **Can the authors quantify specialization beyond cherry-picked visualizations?**  
   For example, for the claims associated with **Figure 3**, **Figure 8**, and **Figure 1(e,f)**, can you report a path-purity metric, label mutual information, or some seed-stability measure? This is important because the paper itself notes that random models also induce nontrivial grouping.

4. **What exactly should the reader conclude from the power-law path plots in Figure 1?**  
   Since random models show a similar exponent, is the claim that training changes the semantics of paths rather than the rank-frequency form itself? If so, that distinction should be made much more clearly.

5. **For the skip mechanism, can the authors clarify whether it should be understood as optimizing a constrained objective or as an external control heuristic?**  
   If there is an implicit objective corresponding to **Equations (2) and (3)**, spelling it out would improve the paper. If not, the claims about end-to-end learned compute efficiency should be softened.

6. **Can the authors provide actual efficiency measurements, even if preliminary?**  
   Wall-clock throughput, memory footprint, or latency comparisons against the dense baselines would help calibrate how much of the efficiency claim is conceptual versus practical.

7. **In Table 3, the skip-enabled language model appears to incur more than a minor performance drop on several tasks.**  
   Can the authors clarify whether this is expected, whether the skip target was aggressively set, and whether there is a Pareto curve showing more moderate compute reductions?

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics concerns are apparent from the main paper. The work studies architectural design and standard vision/language datasets, and I did not identify a paper-specific ethical issue that would require separate ethics review.

## Soundness Rating
2: fair. The paper appears technically plausible and includes nontrivial experiments, but several central claims are only partially supported, important methodological details around routing optimization are underspecified, and the empirical comparisons are not controlled tightly enough to fully validate the advocated conclusions.

## Presentation Rating
2: fair. The paper is readable and the figures are often informative, but the exposition is uneven, some notation and equations are ambiguous, and the novelty/positioning relative to prior conditional-computation work is not articulated sharply enough.

## Contribution Rating
2: fair. The paper explores an interesting direction and offers useful qualitative observations, but the current evidence supports “promising proof of concept” more than a clearly established contribution at ICLR standard.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted.  
The idea is interesting and the qualitative analyses are often engaging, but the current version does not yet make a sufficiently rigorous empirical or methodological case. My main reasons are unclear optimization/routing specification, insufficiently controlled baselines, and claims that are a bit broader than what the evidence supports.

## Reviewer Confidence
4: confident. I am confident in this assessment, though not absolutely certain. I am familiar with the relevant literature on conditional computation, sparse routing, and transformer variants, and I checked the main technical claims and experiments carefully, but some implementation details are not fully specified in the paper.