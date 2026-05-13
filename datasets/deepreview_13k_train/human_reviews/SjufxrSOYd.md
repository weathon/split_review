# Invariant Graphon Networks: Approximation and Cut Distance

- Decision: Accept
- Scores: 8, 8, 8, 8, 8

## Abstract
Graph limit models, like graphons for limits of dense graphs, have recently been used as a tool to study size transferability of graph neural networks (GNNs). While most existing literature focuses on message passing GNNs (MPNNs), we attend to *Invariant Graph Networks* (IGNs), a powerful alternative GNN architecture. In this work, we generalize IGNs to graphons, introducing *Invariant Graphon Networks (IWNs)* which are defined using a subset of the IGN basis corresponding to bounded linear operators. Even with this restricted basis, we show that IWNs of order $k + 1$ are at least as powerful as the $k$-dimensional Weisfeiler-Leman (WL) test for graphon-signals and we establish universal approximation results for graphon-signals in $\mathcal{L}^p$ distances using *signal-weighted homomorphism densities*. This significantly extends the prior work of Cai & Wang (2022), showing that IWNs—a subset of their *IGN-small*—retain effectively the same expressivity as the full IGN basis in the limit. In contrast to their approach, our blueprint of IWNs also aligns better with the geometry of graphon space, for example facilitating comparability to MPNNs. We also highlight that, unlike other GNN architectures such as MPNNs, IWNs are *discontinuous with respect to cut distance*, which causes their lack of convergence and is inherently tied to the definition of $k$-WL. Yet, their transferability remains comparable to MPNNs.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
1

### Summary
This paper introduces Invariant Graphon Networks (IWNs), an extension of Invariant Graph Networks (IGNs), to analyze graphons (limit objects of dense graphs) and investigate their expressivity and continuity properties. IWNs leverage a subset of the IGN framework focused on bounded linear operators, allowing them to approximate graphon functions with an expressivity at least as powerful as the k-Weisfeiler-Leman (k-WL) test.

### Strengths
This paper introduces Invariant Graphon Networks (IWNs) as an extension of Invariant Graph Networks (IGNs) specifically tailored for graphons, significantly enhancing their expressive power and providing new universal approximation properties for graphon signals. The work advances the theory in graph neural networks by rigorously defining IWNs and aligning them with theoretical results through the introduction of signal-weighted homomorphism densities.
- The paper presents a thorough comparison of IWNs with existing graph neural networks, including Message Passing Neural Networks (MPNNs) and other IGNs, addressing size transferability and continuity aspects. It establishes that IWNs maintain at least the same expressive power as the k-Weisfeiler-Leman (k-WL) test, a known benchmark in GNN expressivity.
- The authors have provided extensive mathematical proofs.

### Weaknesses
The absence of empirical experiments and practical application scenarios is the key weakness of this work. Without empirical validation, it is difficult to gauge how IWNs perform on real-world datasets, whether the theoretical advantages translate into meaningful results, and how they compare to established GNN models in practice. IWNs could be applied in scenarios where we need to capture dense graph structures or analyze graphs of varying sizes, which could benefit from their extended expressivity and approximation capabilities.
- It is unclear whether the mathematical assumptions hold across diverse real-world datasets. This could limit the applicability of IWNs to more constrained datasets where these assumptions are valid. Specifically, the assumption that real-world graphs can be accurately represented as graphons, which are limits of dense graphs, needs further scrutiny. Many real-world networks exhibit sparsity and other structural properties that may not align well with the graphon framework. The paper does not address how the theoretical guarantees of IWNs would degrade when applied to graphs that deviate significantly from the graphon assumptions.
- IWNs are discontinuous with respect to the cut distance. This discontinuity implies that minor structural changes in the discrete graph could lead to significant output changes in the IWN, unlike Message Passing Neural Networks (MPNNs). This sensitivity to small perturbations is a major concern for practical applications where graphs are often noisy or subject to minor variations. The paper should provide a more detailed discussion on the implications of this discontinuity and potential mitigation strategies.
- Adapting IWNs to discrete graphs might involve computational overhead, as the model is designed for continuous graphon spaces rather than finite graphs. The paper does not provide a clear analysis of the computational complexity of applying IWNs to discrete graphs, especially in comparison to standard GNNs. This lack of clarity makes it difficult to assess the practical feasibility of using IWNs on large-scale graph datasets.

### Questions
Please see the weaknesses part.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper extends IGNs to the graphon-signal space by introducing Invariant Graphon Networks (IWNs). It provides a generalization of linear equivariant layers to measure spaces, specifically the unit interval [0,1]. The authors introduce signal-weighted homomorphism densities to extend the concept of homomorphism densities to graphon-signals. They prove expressivity results for IWNs, showing that IWNs of order $k+1$ are at least as expressive as $k$-WL for graphons and that they are universal approximators on any compact subset of graphon-signals. This extends the standard results from Maron et al. from graphs to graphons. The paper also discusses the continuity properties of IWNs, highlighting that they are discontinuous wrt the cut distance.

### Strengths
- The paper seems sound and the theoretical results extend the results from Cai & Wang (2022), Böker et al. (2023), and Levie (2023)
- The authors connect their work to previous studies, such as those by Cai & Wang (2022) and Levie (2023), situating their contributions within the broader context of graph(on) neural networks

### Weaknesses
 - It's not clear what the consequences for ML on graphs are
- The non-continuity of IWNs wrt to sampling is mentioned and proved, but it is not clear what consequences it has. Also, the authors mention it as a rather negative point, however, this is not clear to me. Do you have an example where this property hinders size generalization? Or is it rather a worst-case property that doesn't affect IGNs in practice?


### Questions
- Could you discuss your non-continuity results better? What do you think are the consequences?
- Also: how is it possible that the IWNs from Cai & Wang (2022) preserve convergence when sampling graphs from (sufficiently regular) graphon, but yours doesn't? Cai & Wang (2022)  also consider non-linearities, so is the reason that you consider graphon-signal?
- It appears that many results from Böker et al. (2023) and Levie (2023) were reproven using the same techniques for graphon-signal or IWNs. Could the authors discuss their technical contributions. 


## Additional Comments
While the theoretical results appear to be correct (I didn't check all proofs) and generalize some results on graphon neural networks, it is not clear what the broader impact or significance is. I believe answering some of my questions would help to understand this as a reader. I am happy to increase my score if that is done.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This work proposes Invariant Graphon Networks (IWNs), which is an extension of Invariant Graph Networks (IGNs) defined on discrete graphs, to *graphons*. They study its separation power in relation to the $k$-WL test and its approximation capability for functions defined on graphons with vertex features.

They extend the notion of homomorphism densities (which, in turn, is an extension of *homomorphism counting*) from plain graphons to graphons with vertex features, and show that this notion can be used to determine the $k$-WL separation power of graphon neural networks. They then use it to show that their construction yields architectures at least powerful as the $k$-WL test, which in turn implies that it has universal approximation power of functions defined on vertex-featured fraphons.

Notably, their construction is more economic than that of the discrete IGN counterpart, due to a reduced basis for linear layers, leading to slower asymptotic growth in the number of basis elements required.

Finally, they expose a fundamental limitation of IWNs, and thus of IGNs, in that they are discontinuous with respect to the cut distance, which limits their applicability, and in particular their generalization capability, in certain learning scenarios. This is unlike MPNNs, which are continuous w.r.t. the cut distance.

### Strengths
I believe this work offers significant contribution to the community, in that it provides useful theoretical tools to analyze neural networks on vertex-featured graphons, and these tools are already shown useful in this work in their universal approximation and their discontinuity results. The theoretical analysis of IWNs' separation power with the $k$-WL test could guide future architectural innovations or alternative GNN designs on graphons.

### Weaknesses
The paper does not provide numerical experiments. Nonetheless, it provides valuable theoretical contribution that can potentially explain empirical results, motivate the design of architectures and also lead to new theoretical insights on GNNs. While numerical experiments could have provided practical insights into the theoretical results, the theoretical results themselves have high potential for practical impact.

Ln. 140-141: "Note that $\delta_{\square} \leq \delta_p$." - Does it follow from the L1-Lp inequality? This could benefit a short explanation or a citation. The connection between the cut norm and the $L_p$ norm, while standard, could be made more explicit, especially since the cut norm is not as widely used as other metrics. A brief justification of why this inequality holds in the specific context of graphons would strengthen the argument. Furthermore, the implications of this inequality for the subsequent analysis should be highlighted.

Ln. 151: "If simple edges are further sampled..." - unclear definition of G(W,X). The description of how the random graph G(W,X) is generated is not sufficiently clear. It would be beneficial to explicitly state that each edge is sampled independently according to a Bernoulli distribution with a probability determined by the graphon function W evaluated at the corresponding node features. The current wording leaves room for ambiguity and could be misinterpreted. A more precise definition is needed to ensure the reader fully understands the sampling process.

Eq. (3), (4): Perhaps missing "as $n \to \infty$". The convergence in equations (3) and (4) should be explicitly stated as being in the limit as the number of nodes, $n$, approaches infinity. This is crucial for understanding the asymptotic nature of the results and should be included to avoid any potential confusion. Without this clarification, the equations could be misinterpreted as holding for any finite $n$, which is not the case.

### Questions
### Minor comments
1. Ln. 140-141: "Note that $\delta_{\square} \leq \delta_p$." - Does it follow from the L1-Lp inequality? This could benefit a short explanation or a citation.
2. Ln. 151: "If simple edges are further sampled..." - unclear definition of G(W,X).
3. Eq. (3), (4): Perhaps missing "as $n \to \infty$".


### Suggestions
1. Ln. 135-141: Some readers may not be familiar with the concept of cut distance. A brief explanation, perhaps as a short note or in a footnote, could benefit readers as well as help highlight your results on discontinuity.
2. An intuitive explanation for the cut-distance discontinuity, possibly with an illustrative example, could help comprehension.
3. Ln. 314 and the subsequent paragraph: To reassure the reader, I recommend stating explicitly that the dimension does not depend on $n$, and that the following theorem shows that this independence carries through to the case of graphons.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper studied Invariant Graphon Networks, a generalization of Invariant Graph Networks (IGN) from Maron (2018) to graphons. The authors show that Invariant Graphon Networks can be characterized using a subset of the IGN basis functions, due to additional discretization invariance. The authors proved that Invariant Graphon Networks of order $k+1$ are at least as powerful as the $k$-dimensional Weisfeiler-Leman test for graphons proposed in Böker (2023). These expressivity results extend the convergence results in Cai and Wang (2022), by making use of signal-weighted homomorphism densities as a new tool for the analysis. The authors show that Invariant Graphon Networks are typically discontinuous with respect to cut distance, in contrast to the continuity results of MPNNs defined on graphons (Levie 2023). This implies a negative result on the size transferability of IGNs.

### Strengths
1. The paper makes novel contributions on extending IGNs to graphons and studying their expressivity and continuity properties.

2 .The paper is clearly written and well motivated.

3. The notion of signal-weighted homomorphism densitiy is an interesting combination of the graphon-signal space in Levie (2023) and homomorphism densities in Böker (2023).

### Weaknesses
Practical consequences: The authors remark that since Invariant Graphon Networks (IWNs) are discontinuous with respect to the cut distance, IWNs can assign vastly different values to similar graph inputs (line 96). It will be nice to substantiate this remark using empirical evidence, either through observation made in existing works using IGNs or original experiment studies.

1. The definition of signal-weighted homomorphism densities (Defn 3.1) seems standard from the graphon literature, see for example homomorphism density on weighted graphs per equation 5-6 in [1], or various notions of homomorphism densities on multigraphs per chapter 17 in [2]. Can the authors remark the connections to these existing definitions?

2. Invariance under discretization: As stated in Lemma 4.3 and Lemma D.1, invariance under discretization implies the output $L(U)$ is constant almost everywhere. This also leads to a much smaller dimension of the space of linear equivariant layers in Theorem 4.2. Does it make sense to consider relaxing the notion of invariance under discretization (i.e., approximate invariance). Will the authors expect this leads to stronger expressivity results than those stated in Section 5?

3. Nontrivial IWN in Proposition 5.1: Proposition 5.1 (2) states that IWN is continuous with respect to the cut-distance if and only if the pointwise acitivation function is a linear function, where the authors treat it as "trivial" (Line 444). However, such linear IWN may not be trivial if the intermediate layers use higher-order tensors. Can the authors clarify this?

4. The effect of pooling: In the current definition of Invariant/Equivariant Graphon Networks (Defn 4.4), the network consists of linear equivariant maps interleaving with pointwise nonlinearity. In the original works by Maron et al. [3], [4], an invariant pooling operation is often used in practice. Can the authors comment on the role of pooling on the continuity property of IGNs?

### Questions
1. The definition of signal-weighted homomorphism densities (Defn 3.1) seems standard from the graphon literature, see for example homomorphism density on weighted graphs per equation 5-6 in [1], or various notions of homomorphism densities on multigraphs per chapter 17 in [2]. Can the authors remark the connections to these existing definitions?

2. Invariance under discretization: As stated in Lemma 4.3 and Lemma D.1, invariance under discretization implies the output $L(U)$ is constant almost everywhere. This also leads to a much smaller dimension of the space of linear equivariant layers in Theorem 4.2. Does it make sense to consider relaxing the notion of invariance under discretization (i.e., approximate invariance). Will the authors expect this leads to stronger expressivity results than those stated in Section 5?

3. Nontrivial IWN in Proposition 5.1: Proposition 5.1 (2) states that IWN is continuous with respect to the cut-distance if and only if the pointwise acitivation function is a linear function, where the authors treat it as "trivial" (Line 444). However, such linear IWN may not be trivial if the intermediate layers use higher-order tensors. Can the authors clarify this?

4. The effect of pooling: In the current definition of Invariant/Equivariant Graphon Networks (Defn 4.4), the network consists of linear equivariant maps interleaving with pointwise nonlinearity. In the original works by Maron et al. [3], [4], an invariant pooling operation is often used in practice. Can the authors comment on the role of pooling on the continuity property of IGNs?


References:

[1] Borgs, Christian, et al. "Counting graph homomorphisms." Topics in Discrete Mathematics: Dedicated to Jarik Nešetřil on the Occasion of his 60th Birthday. Berlin, Heidelberg: Springer Berlin Heidelberg, 2006. 315-371.

[2] Lovász, László. Large networks and graph limits. Vol. 60. American Mathematical Soc., 2012.

[3] Maron, Haggai, et al. "Invariant and Equivariant Graph Networks." International Conference on Learning Representations. 2018.

[4] Maron, Haggai, et al. "Provably powerful graph networks." Advances in neural information processing systems 32, 2019.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes the Invariant Graphon Network (IWN) architecture for graphons as an extension of the Invariant Graph Network GNN architecture for discrete graphs. The paper's results are framed as a more natural extension and generalization of the related work of Cai & Wong 2022. The authors provide an overview of the relevant graphon theory and an in-depth introduction to a novel signal-weighted homomorphism density concept, providing a comprehensive characterization of weak isomorphism of graphon-signals using this definition, as well as showing a convergence equivalence to cut distance convergence. A generalization of linear equivariant layers is then introduced, through measure-preserving functions rather than permutations in the discrete case. Several central theorems are shown about this function space, including invariance under discretization, construction of a canonical basis, and analysis of dimension. The IWN architecture is then built and proven to be an instance of an IGN-small network. Continuity with regard to $\delta_p$ is then shown, as well as lack of continuity for $\delta_{\square}$ unless the activation function is linear and thus expressivity is lost. Finally, expressivity of IWNs are shown in the sense that order $k+1$ IWNs are able to distinguish with the strength of $k$-WL for graphons.

### Strengths
- There is very thorough analysis of relation to previous work throughout this paper. This work's placement in the literature is clear.
- Original contributions are outlined clearly and presented in a cohesive framework.
- The ideas and results are very original, with several novel concepts defined. The definitions are shown to make sense through the strength of the theory, providing good evidence that these ideas are pointing toward a very useful framework.
- The proof sketch narration is generally clear, and the full proofs in the appendices are nicely written. It is clear there was a good deal of care taken toward ensuring the quality of presentation for these main results.
- In relation to the cited related works, the results shown in this paper are a significant contribution to the community.

### Weaknesses
 - The discussion of the $\delta_{\square}$ discontinuity limiting transferability seems like it could be more complete. Especially as the definitions leading to this point are novel, it seems important to justify this not being a product of a definitional choice that could be reworked and rather a facet of the true underlying problem. Reading the appendix helped clear up my confusions here, but it would be ideal for the section itself to contain just a bit more of that insight. Specifically, the core issue seems to stem from the fact that the cut distance, $\delta_{\square}$, is sensitive to small changes in the graphon that can drastically alter the homomorphism densities, while $\delta_p$ is more robust to these changes. This is a crucial point that needs to be emphasized more clearly in the main text, perhaps by providing a concrete example of a graphon where a small change in $\delta_{\square}$ leads to a large change in the output of the IWN, while the same change in $\delta_p$ does not. This would help the reader understand that the discontinuity is not an artifact of the chosen definitions, but rather a fundamental property of the cut distance in relation to the IWN architecture.
- Due to the heavy theoretical nature, this paper requires a very high degree of engagement to fully understand the stated results. It would be much easier to digest the main ideas on an initial reading with more time, even a short section, dedicated to showcasing some of the concepts you develop, perhaps in some experiments. While convergence experiments such as those in Cai & Wong 2022 are not relevant here, I think there are great possibilities for a showcase of the continuity result and the expressivity result which would really elevate the overall impact of the paper. For instance, visualizing how the IWN distinguishes between different graphons based on their homomorphism densities, or demonstrating the continuity of the IWN output with respect to $\delta_p$ by showing how the output changes as the input graphon is perturbed, would be very helpful. Without such examples, the reader is left to imagine the practical implications of the theoretical results, which can be challenging given the abstract nature of the concepts.

One small typo:
- In Section 6, Paragraph 1, the phrase "...that IWNs, as a subset their of IGN-small, retain..." appears. Removing the "their" would fix this.

### Questions
- You state that IWNs being only continuous for the weaker $\delta_p$ distances, combined with the lack of compactness, prevent the approach from being applied to the entire space. Is there anything interesting to be said about limited regions of this space under the $\delta_p$ distance? Is there any hope for an interesting bound in the $\delta_{\square}$ distance regardless of discontinuity, or is the behavior fundamentally unworkable?
- Have you attempted to build some toy examples of the model, even without any sort of training?

### Soundness
4

### Presentation
2

### Contribution
3
