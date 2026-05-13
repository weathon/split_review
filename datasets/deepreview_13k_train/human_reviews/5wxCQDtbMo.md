# Rethinking Efficient 3D Equivariant Graph Neural Networks

- Decision: Accept
- Scores: 8, 3, 6, 10

## Abstract
Understanding complex three-dimensional (3D) structures of graphs is essential for accurately modeling various properties, yet many existing approaches struggle with fully capturing the intricate spatial relationships and symmetries inherent in such systems, especially in large-scale, dynamic molecular datasets. These methods often must balance trade-offs between expressiveness and computational efficiency, limiting their scalability. To address this gap, we propose a novel Geometric Tensor Network (GotenNet) that effectively models the geometric intricacies of 3D graphs while ensuring strict equivariance under the Euclidean group E(3). Our approach directly tackles the expressiveness-efficiency trade-off by leveraging effective geometric tensor representations without relying on irreducible representations or Clebsch-Gordan transforms, thereby reducing computational overhead. We introduce a unified structural embedding, incorporating geometry-aware tensor attention and hierarchical tensor refinement that iteratively updates edge representations through inner product operations on high-degree steerable features, allowing for flexible and efficient representations for various tasks. We evaluated models on QM9, rMD17, MD22, and Molecule3D datasets, where the proposed model consistently outperforms state-of-the-art methods in both scalar and higher-degree property predictions, demonstrating exceptional robustness across diverse datasets, and establishes GotenNet as a versatile and scalable framework for 3D equivariant Graph Neural Networks.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper introduces GotenNet, a Geometric Tensor Network, that advances molecular representation learning by addressing computational challenges in 3D graph neural networks. GotenNet's novel tensor embedding strategy eliminates the need for complex irreducible representations and Clebsch-Gordan transformations, enhancing computational efficiency while preserving model expressiveness. Its Geometry-Aware Tensor Attention mechanism enables refined edge representations, capturing complex geometric relationships for better molecular property predictions. Additionally, the Hierarchical Tensor Refinement approach allows the model to adapt across scales, accommodating both broad patterns and detailed molecular features. Evaluated on benchmark datasets such as QM9 and Molecule3D, GotenNet consistently outperforms existing methods, demonstrating robustness and scalability.

### Strengths
1. The paper presents a novel framework, GotenNet, which innovatively combines geometric tensor representations with advanced attention mechanisms. This approach addresses the expressiveness-efficiency trade-off in 3D graph modeling, a challenge that has been inadequately tackled in prior works.
2. The paper is well-structured and clearly articulates the problem being addressed, the proposed solutions, and the significance of the findings.

### Weaknesses
1. **Comparison of computational complexity with previous methods**: Could you provide details on the model size, as well as training and inference times, in comparison with existing methods? This information would help highlight GotenNet’s computational efficiency relative to other models in the field.

### Questions
Please see the weakness part.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposed a new network archtiecture that is SE(3) equivariant and builds on Transformers and previous works on equivariant Transformers. The results on various datasets show good performance and speedup.

### Strengths
1. The experimental results are great and intensive.

### Weaknesses
1. The writing of the paper should be greatly improved. Please see "Questions" below.
2. The paper does not discuss why the proposed architecture differs from other works and why this is better in terms of accuracy and efficiency even though the results are seemingly good. Also a reference implementation would be great to make sure the better results are reproducible.
3. The proposed architecture should be simplified (partially because of the way it is presented).
4. The comparison is somewhat unfair. For example, on QM9, this work trains the proposed model for 1,000 epochs while some previous works only train for 300 epochs. Besides, the batch size is 32 on QM9 (some previous works are 128), and smaller batch sizes on QM9 can sometimes lead to better results.

### Questions
> Writing

1. I think the title is too general. We can always rethink something and make them more efficient. Be very specific to your proposed method.
2. Line 16 -- 18: Mention what is the difference from previous works clearly.
3. Line 22 -- 23: Mention the datasets you tested so that readers can know the scale of experiments in this work.
4. Figure 1: I think the x and y axes are similar. Also mention which direction is better.
5. Line 62: What is "this" in "Some recent works have sought to address this by..."? Make sure the sentence is clear.
6. Line 113: Equivariant networks model translational "invariance".
7. Line 159: "Effective Representations" -> too general. Be specific to what makes it effective.
8. Figure 2: Please double checkt the errors in the caption.
9. Line 195 -- 215: Better to link to existing literature since they are similar to (or basically the same as) vector spaces of irreps.
10. Line 220 -- 221: The notation of h, r, t has no meaning and should be replaced by other variables that directly reflect what they are presenting.
11. Line 263: $z$ denotes the "one-hot encoding" of the atomic number.
12. Section 3.3: This is unclear. It would be better to first mention the high-level concept and then go to the details. Also state the differences from previous works.
13. Line 323 or Equation 8: This is essentially an SO(3) linear layer. It would be great to link to previous works.
14. Line 373: Geoformer Wang et al. -> make sure the format of citation is correct.
15. Figure 3: Mention the dataset you tested.
16. Line 423: "The" proposed method
17. Line 448: I don't get the definition of Scalability in the paper. Should be better to use "Evaluation on Efficiency"?

> Question 

1. Line 66 -- 67: How do you define scalability? I think that means you invest more compute, you always get better results. Efficiency should be the correct term to use if you are saying some models are slow or take much memory.
2. Table 1: Somewhat hestitated to trust the results here. From the method section, it is unclear to me what are the differences that can improve the results. Besides, it would be great to discuss some potential oversmoothing, which prevents deeper networks from performing better.
3. It would be good to report training time for completeness.
4. Have you conducted any experiments on materials/catalyst datasets? I think OC20 IS2RE dataset would be good to test given the compute requirement is not that high and the train/val/test splits are well-defined.

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The importance of equivariance in neural networks has become ubiquitous
in machine learning research. Neural networks operating on input features
with certain symmetries, such as rotations, translation and permutation
predict with higher certainty and better quality if the architecture respect
these symmetries. In Graph Neural Networks equivariance with respect to
permutation of the nodes has been the foundation upon which a plethora
of ML approaches have been developed. The authors present a deepening
of this paradigm, by combining the success of transformers, permutation
invariance and E(3) equivariance and distilling these three components into
an architecture for molecular learning. The main contribution of the paper
is the development of Geometry Aware Tensor Attention layer that defines
an E(3) equivariant transformer layer for both node and edge embeddings. A
strong highlighted advantage is computational speed, compared to architectures
using Chlebsch-Gordan decompositions or architectures based on irreducible
representation.

Through a thorough set of experiments, the authors show that their
architecture, GotenNet, is able to outperform a wide variety of benchmarks on
molecule property predictions. Their overall performance and scaling in terms
of computations is also shown.

### Strengths
The paper presents a rather strong experimental section showing that the
authors have taken the time to set up a good set of experiments. In particular
the fact that all comparison partners have been retrained and compared to
three versions of the model shows dedication to the and has been a pleasure
to read. The experiments addressing the inference times is an important
complementary addition, since often there is a rather steep tradeoff between
practicality and usability, where better performance on metrics is achieved
through exponential increases in parameter count or long inference times. To
see both good results and good inference time / scalability is reassuring to
the reviewer. The introduction of geometric tensors as a replacement of CG
coefficient and the computation irreducible representation is a novel and
original viewpoint which combined with the favorable tradeoff between good
performance and accuracy is an impactful contribution. Writing is clear,
concise and easy to follow.

### Weaknesses
Since the reviewer is not too familiar with the literature, the current
writing makes it somewhat hard to compare to the current available literature.
For instance, what would be the comparable difference between GotenNet and an
equivariant transformer (such as equiformer) or the Graph Attention Networks.
Is the current architecture a mix of the two? In that sense some more context
might be good in the introduction or overview of related work.

The paper as written in its current form is of great quality, and could be
potentially be further strengthened through the incorporation of the points
above and by addressing the questions below in a section discussing the current
limitations of the method and potential future avenues of research. For
instance it seems that the current method is _specifically_ tailored to the
prediction of molecule properties and how would that generalize? Another
point to potentially discuss is how this method would extend beyond $E(3)$
and $SE(3)$ equivariance (maybe scaling for instance) and/or if the method
would generalize to point clouds (where this line of work is also highly
relevant). Since the paper is already of great quality addressing these
topics in the rebuttal would be sufficient, however addressing them in the
revision would be beneficial for the reader.

### Questions
Some questions: 

-  How  does  the  current architecture  generalize  to  different tasks? As
presented, it  would work only on  molecule type graphs, is it also possible to
generalize the architecture to for instance social  networks or  other types
of graphs? In  other words,  how general  is the  method.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
10

### Rating Number
10

### Confidence
5

### Summary
This paper propose a novel Geometric Tensor Network (GotenNet) to address  trade-offs between expressiveness and computational efficiency. The core of this model is to use inner-product in Eq. (9) to avoid  tensor products or CG coefficients.
***

In order to better explain my comments and facilitate the understanding of the author, other reviewers, and AC, I will sort out the timetable of related models that are not mentioned in the article, mainly involving the following references:
1. SE(3)-Transformer [a] (in NeurIPS 2020): In Eq. (11) of [a], the calculation of attention $\alpha$used $\bf{q}^\top\bf{k}$, which sum all inner-products of high-degree steerable features together.
2. SE(3)-Transformer implemented by e3nn [b]: See code below
```python
dot = o3.FullyConnectedTensorProduct(irreps_query, irreps_key, "0e")
...
exp = edge_weight_cutoff[:, None] * dot(q[edge_dst], k).exp()
```
And the main difference is the module $\texttt{o3.FullyConnectedTensorProduct}$, which introduces different learnable weights to each inner-product. However, now the model still uses tensor products to generate the key and value pair and is limited by efficiency.

3. ViSNet [c] (in Nature Communications: 05 January 2024, preprint at arXiv:2210.16518): In Eq. (6-7) of [c], authors introduced the connection between inner-products and Legendre polynomials (though a mathematical common sense). But in methodology, they only use the 1st-degree steerable features (Cartesian vectors) to build their models.

4. SO3KRATES [d] (in Nature Communications: 06 August 2024, preprint at arXiv:2309.15126): The SO3KRATES technique in Eq. (14), CG coefficient used in such form, but is equivalent to the inner-products of high-degree steerable features. This paper proposed an Euclidean transformer and achieved nice performance in property prediction tasks (e.g. rMD17 and MD22).

5. HEGNN [e] (in NeurIPS 2024, preprint at arXiv:2410.11443): During studying symmetric geometric graphs, the authors proposed a equivariant GNN model that uses the scalarization trick (i.e., inner product) to introduce high-degree steerable features in Eq. (6) of [e], and pointed out the connection between this approach and SO3KRATES. They used a method similar to Deepsets and Legendre polynomials to prove that this method can recover the information of all angles between each pair of edges, achieved good performance in dynamics tasks (e.g. N-body and MD17), and demonstrated that the introduction of high-degree steerable features can make the model more robust.

[a] SE(3)-Transformers: 3D Roto-Translation Equivariant Attention Networks

[b] https://docs.e3nn.org/en/stable/guide/transformer.html 

[c] Enhancing geometric representations for molecules with equivariant vector-scalar interactive message passing

[d] A Euclidean transformer for fast and stable machine learned force fields

[e] Are High-Degree Representations Really Unnecessary in Equivariant Graph Neural Networks?

In subsequent comments, I will use the names of the above models without citation.

---
> **[First Comment, Rating 3, Confidence 5, with 4/1/4 of Soundness/Presentation/Contribution]**

The model and experiment in this paper are excellent and deserve a clear acceptance or even an award (8-10), but the terrible presentation of this version is totally unworthy of such an achievement. If the author can improve the presentation, I will be very happy to increase the score in the rebuttal. I am very confident that this is a paper that will have a profound impact on the entire field, so I hope it will be accepted in a very perfect manner.

>**[Second Comment, Rating 10, Confidence 5, with 4/2/4 of Soundness/Presentation/Contribution]**

The authors have provided a sincere and thoughtful response, addressing most of my concerns. The remaining questions, primarily related to experimental hyperparameters (e.g. higher-degree steerable features), would likely require significant time to resolve and may not be feasible during the rebuttal period, which I fully understand. Regarding the shortcomings in the presentation originally raised, the revised version has been significantly improved, and the motivation and logic are now clearer and more coherent. Although the presentation still needs further improvement, it is no longer worth over-focusing on during the discussion. Overall, these minor details do not detract from the paper’s value. I therefore give a **strong accept** recommendation.

### Strengths
For the increasingly important discipline of AI for Science, dealing with equivariance is undoubtedly very important. According to the classification of [f], there are two mainstream models: scalarization-based models and high-degree steerable models. The timeline I introduced in the summary (and this article) is actually doing something very valuable, that is, bridge the gap between these two types of models.

In fact, the only papers that truly achieve this are SO3KRATES, HEGNN, and GotenNet (this paper). Although the core formulas of these three works are equivalent, their publication dates are close together—especially since HEGNN's preprint appeared after the ICLR submission deadline. I believe this is merely a case of normal concurrent discovery, and therefore I recognize the originality of this paper. Moreover, equivariance is a very strong constraint, and I would even guess that this form is the only feasible form, which makes the contribution seem small in terms of formula form, but in fact it is a very important contribution.

Moreover, these three works exhibit significant differences. Both SO3KRATES and GotenNet employ equivariant attention, but the inner product formulation used in GotenNet is more concise and yields far better results than SO3KRATES. While both HEGNN and GotenNet point out the inner product formulation, HEGNN’s contributions lie more in theoretical research and model framework, with experiments focusing on dynamical problems, creating a complementary relationship with GotenNet. From my perspective, although GotenNet is on par with these two other works and shares an equivalent formulation, its superior performance makes it an excellent contribution.

[f] A Survey of Geometric Graph Neural Networks: Data Structures, Models and Applications

### Weaknesses
I think the whole article is amazingly good except for the presentation, and there is no major weakness. Here I mainly give the shortcomings of the presentation that I think need to be improved. For other parts (such as models and experiments), there are only some suggestions for the author to choose whether to adopt (see questions).

> **W1. Lack of a good review of relevant literature.**

This article should introduce several works in the timeline I sorted out in the summary section, especially SO3KRATES and HEGNN, which should be introduced in detail. The results of SO3KRATES should be added to the experimental results for easy comparison (although GotenNet outperform SO3KRATES).

For models such as eSCN and EquiformerV2 that use spherical activation functions, a simple comparison should be made. For example, the use of Fibonacci grid requires a large number of sampling points, which brings a large constant in complexity, resulting in a theoretical complexity of $\mathcal{O}(L^3)$, which is actually quite time-consuming (and this can only achieve qusi-equivariance).

> **W2. Weird math definitions and confusing math symbols.**

I don't know what the meaning of Def. 1, Theo. 1-2 in the main text is. I think it is just to make it look like there is some theory. Theo. 3 and Prop. 1, which have some meaning, are too trivial. They can be explained in one sentence: "The product of an invariant scalar and other steerable features does not change its equivariant form." However, the key initialization by spherical harmonics is not only placed in the appendix, but also a clear formula is not given (while Eq. (11) in SO3KRATES and Eq. (5) in HEGNN are clearly written). I suggest replacing this with a discussion of the model architecture. In fact, it is a very valuable point to explain why GotenNet performs so much better than SO3KRATES with a similar architecture. Theoretical analysis may be very difficult, so it is not required, but it would be great if the authors could come up with some engineering tricks.

Moreover, this article will surely have many followers in the future, and a good symbolic system will help future generations understand. The number of superscripts is sometimes one, sometimes two (though it has been explained), and the letters that appear are similar (the $l$ for the number of layers and the $L$ for high-degree steerable features are used at the same time), which is confusing. In addition, the current symbolic representation cannot well show which are invariant scalars and which are high-degree steerable features. It is recommended that the author adopt the HEGNN symbol system (e.g. using $\Delta\boldsymbol{h}$ to represent inter-layer updates, and using fonts such as $\tilde{\boldsymbol{v}}^{(l)}$ to represent $l$-degree steerable features).

> **W3. Others.**

- It is recommended to unify the terminology of the article, such as high-degree steerable features, and not to mix order and degree, otherwise it always gives readers the feeling that the authors are studying multi-body interactions. 

- There are too many crossing lines in Fig. 2 (b-d), which makes it very difficult to understand. Can it be simplified?

- The rotation matrix $R$ in Line 879 (in fact, it should be emphasized that it is an orthogonal matrix) should be the Wigner-D matrix $\boldsymbol{D}^{(l)}(r)$. In addition, the inversion factor should be multiplied according to the parity of the vector itself. For details, refer to [g].

### Questions
Before anything else, is the author willing to provide an anonymous link to the project as soon as possible (this will not affect my subsequent rating increase) so that the results can be reproduced? 

> **Q1. Why use the same weight for steerable features of different degrees (in Eqs. (7) and (11))? Can they be different?**

Note that there are several formula items: $o\_{ij}^d\circ r\_{ij}^{[1,L\_{max}]}$, $o\_{ij}^t\circ h\_{j}^{l,[1,L\_{max}]}$, $m\_2\circ h^{l,[1,\hat{L}\_{max}]}\bf{W}\_{vu}$. They seem to be multiplied by the same coefficient. Steerable features of different degrees represent different orthogonal bases, so their weights should not be the same (as HEGNN does). Can the authors change it to have different weights for each degree and test the performance of the corresponding model?

> **Q2. Why does Eq. (9) use a permutation-invariant operator?**

The results of different degrees should be ordered, so there seems no need for permutation invariance. What are the benefits of using permutation-invariant operations?

> **Q3. Is it possible to explore the expressive power of GotenNet using high-degree steerable features?**

One of the great benefits of this model is that the complexity grows slowly with the feature degree. Can authors show the experimental results of using higher-degree features (e.g. $L\_{\max}\in\\{6,8\\}$)? In fact, similar HEGNN and EquiformerV2 have demonstrated the benefits of using such higher-degree features.

> **Q4. Is it possible to explore the expressive power of GotenNet on large-scale geometric graphs and dynamics tasks?**

Is it possible to add speed attributes like EGNN so that GotenNet can be applied to dynamics tasks? In addition, it is easy to associate the fast multipole method with the possibility that high-degree representations may have good effects on large-scale geometric graphs. Can the authors try the effect of GotenNet on large-scale geometric graphs (e.g. 100-body in HEGNN)?

> **Q5. Is it possible to test the effect of $L\_{\max}=1$?**

Although the benefits of high-degree steerable features are obvious, in many cases a low-degree model is good enough. Can authors give a case where only Cartesian vectors ($L\_{\max}=1$) are used?

> **Q6. Is it possible to provide an e3nn version of GotenNet implementation later?**

From the full text, I guess the author may not know the e3nn library, which can easily implement the interaction of multi-channel high-degree steerable features. I believe it will be easier for everyone to follow the work of this article. However, this project may be very large, and I hope the author can provide this version after the article is accepted.

### Soundness
4

### Presentation
2

### Contribution
4
