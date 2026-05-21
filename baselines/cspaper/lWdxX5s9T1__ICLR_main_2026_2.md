---
job_id: 0e0afba3-3490-4bfa-a3dc-c8873a177fbc
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: lWdxX5s9T1.pdf
paper: RADAR: Learning to Route with Asymmetry-aware Distance Representations
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, it studies representation learning and attention mechanisms for neural combinatorial optimization on vehicle routing problems, with a clear ML methodology component.

## Minimum Quality
Pass ✅. The paper contains the expected scientific structure, including abstract, introduction, related work, methodology, experiments, quantitative results, and conclusion. While I have substantial concerns about novelty, methodological clarity, and some mathematical/expositional points, these do not rise to the level of desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, suspicious reviewer-targeting instructions, or other manipulative content in the provided paper text and figures.

# Expected Review Outcome:
## Summary
This paper proposes RADAR, a neural framework for asymmetric vehicle routing problems that augments existing constructive solvers with two components: an SVD-based initialization of node embeddings from the asymmetric distance matrix, and Sinkhorn normalization in attention to replace row-wise softmax. The paper evaluates the approach on synthetic ATSP/ACVRP, a 16-task asymmetric VRP benchmark, and several real-world routing datasets, reporting improved performance over a range of neural baselines and some classical solvers under selected settings.

## Strengths
The paper addresses a practically relevant gap. Many neural VRP solvers are built around symmetric Euclidean assumptions, and the paper focuses directly on asymmetric distance matrices, which is a meaningful problem setting for deployment-oriented routing.

The method is easy to understand at a high level and modular. The two design choices, SVD-based initialization for static asymmetry and Sinkhorn-normalized attention for dynamic asymmetry, are simple enough that they could plausibly be transferred to other neural routing architectures. **Figure 1** is helpful here: it clearly separates the static component on the left from the dynamic attention modification on the right, and makes the paper’s intended decomposition of the problem into initialization versus message passing much easier to follow.

There is a good amount of empirical coverage in the main paper. The authors report results on synthetic ATSP and ACVRP across multiple scales, a multi-task benchmark over 16 asymmetric VRP variants, and real-world data. This breadth is a genuine strength, especially because the paper is not limited to one benchmark or one asymmetry construction.

Some of the quantitative gains are substantial. In **Table 1**, RADAR improves clearly over the strongest neural baselines in the ATSP generalization setting, especially at larger sizes, for example ATSP1000 where RADAR reports 4.13% gap versus 17.17% for ELG and 31.67% for ReLD. That pattern, if robust, supports the claim that the representation is helping cross-size generalization rather than merely overfitting to the training size.

The ablation in **Table 6** is also informative. It shows that both components contribute, and notably that Sinkhorn appears to account for a large fraction of the gain on large ATSP instances. This is useful because it prevents the paper from collapsing into a one-trick “just use SVD” story.

The real-world study is a positive addition. In **Table 3**, RADAR consistently beats the neural baselines listed across ATSP, ACVRP, and ACVRPTW, and **Table 4** provides a relevant analysis of the role of coordinates under asymmetry. Even though I have reservations about baseline breadth there, I appreciate that the paper does not stop at synthetic data.

## Weaknesses
1. **The claimed theoretical framing around “asymmetry-aware embeddings” is much weaker than the paper suggests, and in its current form it is close to a rephrasing of low-rank matrix factorization rather than a substantive theory.**  
   The central formal object is **Definition 1 on Page 4**, which says an embedding matrix \(X\) is asymmetry-aware with respect to \(D\) if there exist two distinct linear maps \(W_1, W_2\) such that
   \[
   \|XW_1(XW_2)^\top - D\|_F^2 \approx 0.
   \]
   This is extremely permissive. First, the “\(\approx 0\)” is undefined, so the definition has no precise content. Second, for any low-rank factorization of \(D\), one can package the factors into a larger \(X\) and choose selectors \(W_1, W_2\), which is exactly what the paper then does in **Equations (3)-(5)**. So the definition does not characterize anything specific to the proposed representation, nor does it show that the learned embedding used by the model will preserve asymmetry after the subsequent projection and encoder updates. The result is more “SVD gives a bilinear reconstruction” than “the model theoretically captures static asymmetry.” That distinction matters because the paper leans on this section to elevate what is otherwise a fairly straightforward engineering choice.

2. **The dynamic asymmetry argument for Sinkhorn normalization is under-justified, both mathematically and empirically.**  
   The core claim in **Section 4.2, Pages 5-6** is that row-wise softmax only makes \(A_{i,j}\) aware of node \(i\)’s neighborhood but not node \(j\)’s full neighborhood, and that Sinkhorn normalization fixes this by jointly normalizing rows and columns. I do not find this argument convincing as written. Column normalization imposes marginal constraints on the attention matrix, but that does not by itself imply that \(A_{i,j}\) now captures the “complete neighborhood structure” of \(j\). At best, it couples scores across destinations globally. This is a much weaker statement than the text suggests.  
   The empirical support is also thin in the main paper. **Table 6** shows that replacing softmax with Sinkhorn helps, but it does not isolate *why* it helps. It could be acting as a regularizer, discouraging attention collapse, rather than modeling “dynamic asymmetry” in the specific sense claimed. **Figure 8** in the appendix, comparing softmax and Sinkhorn attention maps, actually raises an uncomfortable question: the Sinkhorn map looks much more uniform, which may reduce attractor collapse, but uniformization is not automatically evidence of better directional reasoning. The paper needs a sharper argument and ideally a diagnostic more directly tied to asymmetry modeling.

3. **A key part of the method, namely the actual training objective and optimization protocol, is underspecified in the main paper.**  
   The main text describes the architecture and decoding procedure, but does not clearly state the learning objective. Is the model trained with REINFORCE, rollout baseline, imitation, or another objective inherited from the backbone? This is not a cosmetic omission. For neural routing papers, optimization details strongly affect performance and stability. The issue is especially important here because the paper changes the initialization and attention normalization, both of which can interact heavily with policy-gradient training. Relying on readers to infer “it probably follows MatNet” is not enough. This weakens reproducibility and also makes it harder to judge whether performance gains are due to the proposed representations or to training choices.

4. **There are nontrivial mathematical and algorithmic clarity issues in the formulation.**  
   A few examples:
   - **Equation (6) on Page 5** has a parenthesis mismatch and is not cleanly defined. More importantly, \(\operatorname{Sim}(X_i, X_j, D_{i,j}, D_{j,i})\) is left abstract in the main text, even though this function is central to how distance information enters attention.
   - In **Algorithm 2 on Page 6**, the Sinkhorn procedure is written as \(P \gets \exp(S)\) followed by alternating division by column and row sums. But the paper does not specify how masking of visited or infeasible nodes is handled in this normalization. In routing, masks are not optional; applying Sinkhorn to a matrix with forbidden entries is not equivalent to standard masked softmax. If masking is introduced later, does the matrix remain approximately doubly stochastic over feasible entries, or is that property broken?
   - The algorithm also ignores numerical stability. Directly exponentiating scores can overflow; most practical implementations use log-domain stabilization or at least score shifting. Since the paper sells Sinkhorn as a drop-in replacement for softmax, this omission is not minor.
   - The proof-like discussion around **Equations (3)-(5)** only shows reconstruction before the learned projection layer in **Algorithm 1, line 7**. After \(X_{\text{final}} = \text{Linear}(X)\), the exact reconstruction argument no longer applies unless extra conditions are imposed. The paper blurs that distinction.

5. **The novelty is somewhat incremental relative to what is actually implemented.**  
   Strip away the rhetoric, and the method is “initialize node features using a truncated SVD of the asymmetric distance matrix, then replace softmax with Sinkhorn in a MatNet-style attention module.” This is a reasonable combination, but it is not a major conceptual leap. The SVD part is a standard matrix factorization tool applied in an intuitive way, and the Sinkhorn part is a familiar doubly-stochastic normalization. The paper would be easier to endorse if it were more modest about this and positioned itself explicitly as a strong systems/empirical paper. Instead, the current framing suggests a deeper representational theory than is really delivered.

6. **Some experimental comparisons are less clean than they first appear.**  
   In **Table 1**, many baselines are retrained under the authors’ setup, sometimes with notable architecture changes. For example, ELG is explicitly adapted because it does not natively support asymmetry, and several methods are reported under z-score normalization chosen by the authors. The appendix later argues that z-score is generally competitive, but this still means the comparison depends heavily on a common reimplementation pipeline. That is acceptable in principle, but then the paper should be more careful in separating “comparison to prior methods” from “comparison to our reimplemented versions under our training recipe.”  
   There is also nomenclature sloppiness that does not inspire confidence, for example “ReLU+” appearing in **Table 1** where the intended baseline seems to be ReLD. That may be a typo, but when several baselines are adapted and retrained, such mistakes matter because they muddy what exactly was compared.

7. **The choice of the truncation rank \(k\) is not convincingly justified, and the justification that is given is somewhat concerning methodologically.**  
   On **Page 5**, the authors state that top-10 singular values capture around 85% of the matrix information, while 20 and 30 capture more, and that they choose top-10 as a trade-off between in-distribution and out-of-distribution generalization. The problem is that this sounds like the rank is selected based on observed OOD test behavior. If so, that is not clean model selection. More importantly, the paper does not provide a principled criterion relating rank to instance size, asymmetry level, or downstream task difficulty. **Figure 3** in the appendix gives some sensitivity analysis, but in the main paper the choice feels empirical and somewhat tuned to the benchmarks.

8. **The scalability story is not fully convincing for the very setting the paper emphasizes, namely realistic asymmetric distance matrices.**  
   The method assumes access to the full \(n \times n\) distance matrix and performs truncated SVD on it. That is workable at \(n \le 1000\), as shown, but the paper repeatedly emphasizes practical routing scenarios where only pairwise asymmetric costs are available. In real systems, those matrices can be expensive to store, expensive to query, and expensive to factorize. **Figure 4** and **Table 11** suggest that SVD is not dominant at the tested scales, which is useful, but the argument still feels too optimistic. The asymptotic memory footprint remains quadratic in \(n\), and there is no discussion of sparse, streaming, or partial-matrix variants. This matters because the paper’s practical motivation is one of its main selling points.

9. **The empirical section is broad but not always as decisive as the narrative suggests, especially with respect to classical solvers and real-world baselines.**  
   For synthetic ATSP and ACVRP, the neural gains are clear. But for the multi-task benchmark in **Table 2**, the average gap improvement from RF-NN to RADAR is modest, 1.99% to 1.33%, and the paper does not report variance or significance. On real-world data in **Table 3**, the baseline set is relatively narrow and partly inherited from another paper rather than re-run here under matched settings. Given the practical framing, I would have liked stronger comparisons to high-quality non-neural solvers where feasible, and more discussion of whether the remaining gap to classical methods is acceptable in deployment terms.

10. **Presentation quality is mixed despite generally readable prose.**  
   There are quite a few typos, notation inconsistencies, and overclaims. Examples include “ReLU+” vs. ReLD, “Runtime Ananlysis” on **Page 10**, and several places where the text says the model “theoretically captures” something that is only heuristically supported. Also, some figure-based analyses are visually suggestive but not especially rigorous. **Figure 2** shows initialization performance across sizes, but because it only reports final gap bars without uncertainty or matched compute, it supports the broad trend but not strong causal conclusions. This is not fatal, but it contributes to an overall sense that the paper is stronger empirically than analytically, while sometimes pretending otherwise.

## Questions
1. **Training objective and optimization details:** What is the exact learning objective used in the main experiments? Please state the training loss explicitly in the main paper, including any rollout baseline, entropy regularization, sampling policy, and how decoder trajectories are generated during training. This would substantially improve reproducibility and confidence.

2. **Masked Sinkhorn:** How exactly is masking handled in **Algorithm 2** during decoding and during encoder attention for infeasible or padded entries? If rows or columns are partially masked, does the resulting attention remain approximately doubly stochastic over the feasible support, or is the normalization only applied before masking? A precise formula would help.

3. **Strength of the theoretical claim:** Can the authors clarify what **Definition 1** is intended to prove beyond the existence of a truncated bilinear factorization of \(D\)? In particular, after the linear projection in **Algorithm 1** and subsequent encoder layers, what part of the “asymmetry-aware” property is preserved?

4. **Why does Sinkhorn help?** The current evidence in **Table 6** shows that it helps, but not why. Can the authors provide a more direct diagnostic that distinguishes “better asymmetry modeling” from “regularization / anti-collapse effect”? For example, do attention statistics correlate with directional structure or route quality in a way softmax does not?

5. **Rank selection:** How was \(k=10\) chosen in practice? Was the choice fixed using only training/validation data, or did OOD test performance influence it? A cleaner model-selection story would increase confidence.

6. **Fairness of baseline adaptations:** For the adapted baselines in **Table 1**, especially ELG and the various MatNet variants, can the authors clearly enumerate which changes were architectural necessities versus optional tuning decisions? This matters for interpreting the size of the reported improvements.

7. **Significance / variance in main tables:** Are the gains in **Tables 2-4** stable across random seeds? Reporting means with confidence intervals, at least for the main neural competitors, would strengthen the empirical case.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics concerns arise from the submission based on the main paper. The work focuses on algorithmic improvements for routing optimization. Standard caveats about downstream logistics and transportation applications apply, but I do not see a paper-specific ethics issue requiring escalation.

## Soundness Rating
2: fair. The core empirical claims are supported reasonably well, but several methodological details are underspecified, and the theoretical framing is weaker than the paper suggests.

## Presentation Rating
2: fair. The paper is readable and the main idea is understandable, but there are enough notation gaps, typos, and overstatements that the presentation falls short of being cleanly polished.

## Contribution Rating
2: fair. The paper addresses an important problem and shows useful empirical gains, but the conceptual novelty is modest and the scientific framing oversells what is, in essence, a relatively straightforward combination of known ingredients.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted.  
This is a useful and practically motivated paper with strong empirical breadth, and I can see why others may lean positive. Still, I think the current version overclaims on theory, underspecifies important parts of the method, and does not quite make the case that the contribution is more than a solid engineering combination with good benchmarking.

## Reviewer Confidence
4: confident. I am confident in the assessment and familiar with neural combinatorial optimization / routing papers, though I did not independently verify every implementation detail.