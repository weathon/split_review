# Unconstrained Robust Online Convex Optimization

- Decision: Reject
- Avg Score: 5.75
- Scores: 6, 6, 5, 6

## Abstract
This paper addresses online learning with ''corrupted'' feedback. Our learner is provided with potentially corrupted gradients $\tilde g_t$ instead of the ''true'' gradients $g_t$. We make no assumptions about how the corruptions arise: they could be the result of outliers, mislabeled data, or even malicious interference. We focus on the difficult  ''unconstrained'' setting in which our algorithm must maintain low regret with respect to any comparison point $\||u\|| \in \mathbb{R}^d$. Perhaps surprisingly, the unconstrained setting is significantly more challenging as existing algorithms suffer extremely high regret  even with very tiny amounts of corruption (which is not true in the case of a bounded domain). Our algorithms guarantee regret $ \||u\||G (\sqrt{T} + k) $ when Lipschitz constant $G \ge \max_t \||g_t\||$ is known, where $k$ is a measure of the total amount of corruption. When $G$ is unknown and incur an extra additive penalty of $(\||u\||^2+G^2) k$.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper studies unconstrained OCO with adversarial corruptions. The auhors provide algorithms that ensures $O(||u||G\sqrt{T}+||u||Gk)$ regret bound, where $k$ is the number of corruptions. They also provide matching lower bounds.

### Strengths
The problem:

This paper is the first to study unconstrained OCO with adversarial corruptions, which is a new and novel problem. 

The motivation is clear and makes sense to me, as in practice we indeed might only able to observe biased gradients. 

The contribution:

The authors successfully provide an algorithm which is of order $O(||u||G\sqrt{T}+||u||Gk)$ for the case when G (the upper bound for gradient) is known, which matches the optimal rate for parameter free OCO when the number of corruptions $k=O(\sqrt{T})$. There is also a lightly worse bound for the case where $G$ is not known. Finally, the authors also a matching lower bound for this problem. 

The presentation: 

The paper is in general easy to follow, and the main ideas of the methods are well explained.

### Weaknesses
 The problem:

The problems studied here is a combination of the well-studied unconstrained OCO and OCO with corruption. Note that OCO with stochastic corruption has been studied, and many key ideas of this paper are motivated by them. 
 

The methods:

The main technique used here to deal with corrupted gradients is very similar to that in Zhang & Cutkosky (2022). To be more specific, similar to the stochastic setting, the regret of this problem can be decomposed into two terms: one "easy" term, e.g., the first term in (6), a standrd OLO problem with bounded gradient, and one "bias" term (e.g., the second term in (6), which related to the gap between the clipped gradient and the true gradient). For the bias term, by basic Cauchy-Swhurz inequality (eq. (7)), one can notice that it is dominated by max_t ||\w_t||, that is, the max norm of the decisions. The same term also appears in  Zhang & Cutkosky (2022) (page 4, the NOISE term). Following Zhang & Cutkosky (2022), the authors introduced the same surrogate loss. 


The presentation: 

2) In Sections 4 and 5, the authors sometimes use ||\cdot||| to denote the norm, sometimes use |\cdot| (e.g., compare (5) and (7)). Please make it clear in the begining of Section 4 that the discussion is for W=R, but it can be extended to R^d. 

3) Line 215 "(in fact, potentially exponential in t)": I am not sure about the meaning of this sentence. Note that this paragraph is about regret decomposition, and no algorithm is discussed. So why it can exponential in t? The same sentence appears in Zhang & Cutkosky (2022) (first sentence in Page 5), but in Zhang & Cutkosky (2022) it makes sense there because it is in a different context (discussing an algorithm).

### Questions
In Section 4.2, can the authors provide some more explanations on how the lower bound is proved?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors study online convex optimization under corrupted gradient feedback in an unconstrained domain. The proposed algorithm requires prior knowledge of "a measure of total corruption" $k$ and achieves a regret bound of $\mathcal{O}(|| u || G (\sqrt{T} + k))$ for any comparator $u$, assuming the gradient norm bound $G$ is known for the uncorrupted rounds. If $G$ is not known, they propose a filtering approach to guarantee a regret bound of $(|| u ||^2 + G^2) k$. They also provide matching lower bounds (up to logarithmic factors) for any choice of $u$.

### Strengths
The paper is well-written, effectively motivating the problem and clearly articulating the associated challenges. The techniques and results are presented in an understandable and clear manner. The work draws significant inspiration from two existing works: it leverages the composite loss function method from Zhang & Cutkosky (2022) to manage large corrupted gradients and employs filtering techniques from van Erven et al. (2021) to address unknown bounds on the gradient norms of uncorrupted rounds. Especially the proposed work is able to reduce the space complexity of filtering techniques of van Erven et al. (2021).

### Weaknesses
In my view, the reliance on established techniques impacts the overall novelty of the work. Specifically, the major technical tools employed are well-known, which somewhat limits the innovative contribution. It would significantly strengthen the paper if the authors could elaborate on the primary technical innovations in Section 4.1. In particular, it would be helpful to clarify how their approach in this section differs from or improves upon the methods presented by Zhang & Cutkosky (2022). The use of the composite loss function, while effective, is not a novel contribution in itself, and the paper would benefit from a more detailed explanation of how it is adapted or extended in this specific context of corrupted gradient feedback. Furthermore, while the filtering technique from van Erven et al. (2021) is acknowledged, the paper could delve deeper into the specific challenges of applying this technique to the online convex optimization setting with corrupted gradients and how the authors overcome these challenges beyond simply reducing space complexity. The paper would be stronger if it highlighted the specific modifications or insights that make the filtering approach suitable for this problem.

### Questions
Please see the previous section.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper studies algorithms with good regret guarantees in a modification of the classical (unconstrained) online convex optimization setting where (roughly, since the definition is more nuanced) $k$ of gradients can be arbitrarily corrupted.  Previous work either studied stochastic corruptions and/or a setting where the feasible set of the algorithm/player is bounded. When the algorithm knows a bound $G$ on the norm of the gradients, this paper shows an algorithm whose regret guarantee against a comparator $u$ is (roughly) only a additive factor of $\tilde{O}(Gk \lVert u \rVert)$ worse compared to the regret guarantees of optimal algorithms in the uncorrupted setting. Furthermore, this paper also shows an algorithm that has similar regret guarantees even without prior knowledge of $G$, with an extra penalty of $\tilde{O}((\lVert u\rVert^2 + G^2)k)$ in the regret. Finally, the paper also provides matching lower bounds for the case of known $G$.

### Strengths
- The paper finds a natural problem with a clear technical difficulty: handling adversarially corrupted gradients in *unconstrained* problems in online convex optimization. It was surprising that this problem was not previously studied outside of the stochastic case;
- The definition of $k$ is simple yet nicely covers two slightly different notions of robustness in OCO simultaneously;
- The final regret bounds are asymptotically optimal, and the matching lower bounds show that we cannot improve the bounds by much;

### Weaknesses
 - I believe one of the main weaknesses of this paper is presentation. The first algorithm (for known $G$) heavily builds on the work of Zhang and Cutkosky (2022). This is not a problem by itself, but the paper does not do a great job os describing the main modifications needed , and I found myself relying on reading the other paper to understand the main ideas of the algorithm, which is not ideal. For the case of unknown $G$ the authors seem to combine (and improve on) different ideas from previous work. However, the presentation is convoluted, and it is hard to understand both the algorithm and the main technical contributions (I will expand on this in the questions);

- The examples are not great: the first one is not interesting (at least from what I could understand), since the reduction of OCO to stochastic optimization is almost just matter of taking expectations of the OCO guarantees. And for the second example I could not understand whether the results the papers gets are interesting or not since there is no discussion on what kinds of results exist on the literature of the area already;

- At some points in the main text there is a confusion between working in 1D and general dimension, which makes the description of the algorithms and results very confusing;


- The description of the algorithm for known G (Section 4) lacks clarity regarding the specific modifications made to the algorithm of Zhang and Cutkosky (2022). It is unclear whether the techniques are identical, with only a reformulation of the problem, or if there are substantial differences in the algorithm itself. This ambiguity makes it difficult to assess the novelty of this section.

- The Distributed Robust Optimization (DRO) application is not well-placed in the literature. The connection to the work of Namkoong and Duchi (2016) is not clearly established, and it is not clear how the results of this paper compare to the existing results in the area. The discussion of the DRO application lacks a clear comparison with existing results, making it hard to understand the relevance of the application.

### Questions
I believe if the authors could help clarify a few of the key ideas and contributions in the algorithm, it could help me and the other reviewers better appreciate your work. 


- **The case of known $G$**: The algorithm in this case is a modification of ideas proposed by Zhang and Cutkosky (2022). However, it is not clear from the paper what are the key differences between the analysis in the stochastic case done by Zhang and Cutkosky and the one done in this paper. 

I know the space constraints play into this, but reading pieces of Zhang and Cutkosky (2022) clarified many pieces of the algorithm for me that were not clear from the algorithm. A small example: on line 6 of Algorithm 1 we need to find a point $w_t$ that satisfies an equation, but the paper never discusses computational complexity or, more importantly, why a solution to this is guaranteed to exist. This is luckily done by Zhang and Cutkosky (2022), but it is not even discussed in the paper. My question for the authors here is: could you briefly explain what are the key modifications to the algorithm and/or analysis from the stochastic case from Zhang and Cutkosky to this adversarial corruption setting? If the algorithm is barely different from their algorithm for sub-exponential noise, it would be even more interesting and should even be clarified in the paper, because then a contribution of the paper would be showing that the same algorithm also works for this seemingly harder case!

- **The case of unknown $G$**: This case seems to be about estimating $G$ on-the-fly, doing so by using the algorithm for known $G$ with a couple of ideas from previous work (an improvement on the filtering strategy from van Erven et al., 2021, and the Epigraph Based regularization from Cutkosky and Mhammedi, 2024). This was a section that was quite hard to understand, and I have a few questions in the hope of better understanding the contributions of this section.

1) On the paragraph starting on line 399, you mention you improve on the original Filter strategy. Besides the memory usage, are there other improvements? Are these improvements crucial for the algorithm? (i.e., a black-box use of Filter could lead to similar bounds?)

2) When using the Epigraph-based regularization the paper also uses a reduction from e Cutkosky & Orabona (2018) to maintain the constraints, but it seems that this reduction is explicitly written into the algorithm. Is the use of this reduction the same described by  Cutkosky & Mhammedi (2024), section 3.3? If not, what are the main differences? Also, since this is a reduction, couldn't algorithm 2 be described in two steps (such as the different protocols in Cutkosky & Mhammedi, 2024)? I think this would simplify the presentation greatly;

- **Confusion in the description of the algorithm**: On eq. 5, $\tilde{g}_t^c$ might be a scalar or a vector, depending on the case. I think you meant to present this only for the 1D case. This is a key definition for the algorithm, so it is important for it to be correctly described.

- **On the second example**: Are there comparisons with results in the area of DRO that can help us understand the relevance of the application of this results to this problem?

### Soundness
3

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper considers the problem of online linear optimization with possibly corrupted gradients in an unbounded domain. For this problem, the authors further investigated two setups: known gradient upper bound $G$ and unknown $G$. For the first case, the authors obtained an $O(\|u\| G (\sqrt{T} + k))$, where $\|u\|$ denotes the norm of the unknown comparator that appeared in the definition of regret, and $k$ serves as an upper bound for the number of corruptions or the magnitude of corruptions. Note that the number $k$ is known prior to the algorithm. The authors have also provided a corresponding lower bound to prove the optimality of the obtained guarantee. For the unknown gradient norm upper bound, the authors obtained the above regret with an additive $(\|u\|^2 + G^2) k$ overhead. Finally, the authors have also applied their results to the applications of stochastic convex optimization with corruptions and DRO to validate the effectiveness.

### Strengths
The paper considers the meaningful problem of online learning with corruption. Advances in this problem can enhance the robustness of online algorithms. The presentation is clear and easy-to-follow. The example in Figure 1 is intuitive and well-motivating. The proof sketch in Section 4 is clear, intuitive, and easy to understand for readers without much background knowledge in this field. The obtained result for the known gradient norm upper bound case is optimal.

### Weaknesses
I am not an expert in online learning in the unbounded domain. As a result, I did not check the correctness of the proofs in this paper. The proof sketch in Section 4 is clear, as I have stated in the 'Strengths' part, and thus easy to follow. However, the analysis becomes much more complicated in the unknown gradient norm upper bound case. The current statements from Pages 8 to 10 are quite complicated and confusing. Actually, this part looks more like a draft or some proof that should be deferred to the appendix.  The current presentation is quite confusing for me. I suggest that the authors could revise this part to emphasize more about the exact difference in the analysis from that in the first case, but not state the proof once again. Specifically, the transition from the known gradient bound case to the unknown case lacks clear motivation and explanation. The introduction of the additional terms and the modified update rule in the unknown case are not sufficiently justified, making it difficult to grasp the core intuition behind the analysis. The presentation of the proof in the unknown gradient case feels like a dense sequence of inequalities without clear guidance on the underlying logic. This makes it hard to understand why the specific steps are taken and how they lead to the final result. The lack of intermediate explanations and connections to the known gradient case makes the analysis feel disconnected and hard to follow.

### Questions
1. The paper [1] also considered some kind of corruption. Specifically, they studied the case where the strong convexity of online functions can be corrupted or degenerated to the convex case, and they used universal online learning algorithms to solve this problem. I think [1] is related to this paper in terms of corruption and can be introduced in the related work section.

2. I was wondering how strong the assumption of knowing $k$ is. Actually, since $k$ serves as an upper bound for both the corruption number and the corruption magnitude. Knowing it seems to be a pretty strong assumption. Can the authors provide further explanations on this issue? I also suggest that the authors could add more explanations about it in the revised version.

3. Can eq.(5) be simply rewritten as $\tilde{g}_t^c = \min\\{h_t, \|\tilde{g}_t|\\}$? The current version seems pretty complicated but not very necessary.


References:

[1] Contaminated Online Convex Optimization

### Soundness
3

### Presentation
3

### Contribution
3
