# ATLAS: Automatic Local Symmetry Discovery

- Decision: Reject
- Scores: 6, 6, 3, 5, 6

## Abstract
Existing symmetry discovery methods predominantly focus on global transformations across the entire system or space, but they fail to consider the symmetries in local neighborhoods. This may result in the reported symmetry group being a misrepresentation of the true symmetry. In this paper, we formalize the notion of local symmetry as atlas equivariance. Our proposed pipeline, automatic local symmetry discovery (ATLAS), recovers the local symmetries of a function by training local predictor networks and then learning a Lie group basis to which the predictors are equivariant. We demonstrate ATLAS is capable of discovering local symmetry groups with multiple connected components in top-quark tagging and partial differential equation experiments. The discovered local symmetry is shown to be a useful inductive bias that improves the performance of downstream tasks in climate segmentation and vision tasks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper presents ATLAS (Automatic Local Symmetry Discovery), an approach for discovering local symmetries in various data forms.  The authors provide formal descriptions of the locality and equivariance of ATLAS, along with algorithms for discovering infinitesimal generators and discrete symmetries. Results from these experiments show that integrating the discovered symmetries into downstream models can enhance performance. Through experiments involving top-quark tagging, synthetic PDEs, MNIST classification, and climate segmentation, the authors demonstrate the effectiveness of ATLAS in discovering local symmetries and integrating them into gauge equivariant networks, leading to improved performance metrics.

### Strengths
1. The paper is well-motivated, presenting a new conceptual framework. The authors validate their approach across multiple tasks and demonstrate its effectiveness.

### Weaknesses
1. The definitions of Atlas Locality and Atlas Equivariance both contain the term "Atlas," an abbreviation for the authors' method, i.e., Automatic Local Symmetry Discovery. Defining a mathematical object using the abbreviation of a specific method is uncommon and could lead to confusion. Additionally, the authors do not clearly differentiate atlas locality from general locality, nor do they clarify how atlas equivariance differs from equivariance to conventional local transformations. The lack of clarity on how the 'atlas' framework relates to existing concepts of locality and equivariance makes it difficult to assess the novelty and generality of the proposed approach. Specifically, it is unclear if 'atlas locality' is simply a specific instance of locality defined on a manifold, or if it introduces a fundamentally new concept. Similarly, the distinction between 'atlas equivariance' and standard local equivariance needs to be rigorously defined, perhaps by contrasting it with existing notions of gauge equivariance or other forms of local transformation invariance.
2. While the authors emphasize the importance of local equivariance, many deep learning tasks, such as natural language processing and video understanding, exhibit long-range dependencies, highlighting the coupling of local and global equivariance. Is the proposed framework applicable in these scenarios? The paper does not address the limitations of focusing solely on local symmetries, particularly in contexts where global dependencies are crucial. For example, in video understanding, actions often involve both local motion and global scene context. Similarly, in NLP, understanding a sentence requires capturing relationships between words that are not necessarily local. The authors should discuss how their framework can be extended or adapted to handle such long-range dependencies or acknowledge its limitations in these areas.
3. The authors report only the final results of their complete method in each experiment, lacking ablation studies and fine-grained visualizations of features to provide a more credible explanation of their approach. The absence of ablation studies makes it difficult to understand the contribution of each component of the proposed method. For example, it is not clear how much performance gain is due to the symmetry discovery process versus the integration of these symmetries into the network architecture. Furthermore, visualizations of the discovered symmetries and their impact on feature representations would greatly enhance the interpretability and credibility of the results. Without these, it is hard to ascertain whether the method is truly discovering meaningful symmetries or simply overfitting to the training data.
4. The descriptions of experimental details are somewhat lacking, particularly concerning the discovery of symmetry and its integration with neural networks on specific datasets. The paper lacks sufficient detail on how the symmetry discovery process is implemented for each dataset. For instance, the specific choices of hyperparameters, the initialization of the symmetry discovery algorithm, and the criteria used to determine convergence are not clearly specified. Similarly, the integration of the discovered symmetries into the neural network architecture is not described in sufficient detail, making it difficult to reproduce the results. The authors should provide more precise details on these aspects to ensure the reproducibility and verifiability of their findings.
5. The paper conducts many experiments, and for the MNIST classification task, it projects the data onto a spherical space. What are the physical meanings or practical applications of this projection? The motivation for projecting MNIST data onto a spherical space is unclear and lacks a clear justification. It is not evident how this projection relates to the underlying symmetries the authors aim to discover. The authors should provide a more compelling rationale for this projection, perhaps by relating it to a specific physical model or a practical application where such a transformation is meaningful. Without this, the experiment appears somewhat artificial and detracts from the overall credibility of the method.
6. Although the paper provides the steps of the ATLAS algorithm, there is limited analysis on the time and space complexity of the algorithm. It is recommended to include this section to assess its feasibility for applications on large-scale datasets. The lack of a time and space complexity analysis makes it difficult to assess the scalability of the proposed method. The authors should provide a theoretical analysis of the computational cost of the algorithm, including the dependence on the size of the input data, the number of symmetries discovered, and other relevant parameters. This analysis is crucial for determining the feasibility of applying the method to large-scale datasets and real-world applications.

### Questions
see Weaknesses in the previous section

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This work proposed ATLAS to recover local symmetries (both continuous and discrete) from a dataset. By incorporating the symmetries discovered by ATLAS in a gauge equivariant CNN can lead to better performance and parameter efficiency.

### Strengths
1. The figures provided in the paper are of high quality, easy to understand

2. The algorithm proposed is straightforward and concise.

### Weaknesses
1. The motivation for discovering local symmetries through ATLAS is not clearly articulated. The current description is somewhat abstract, which may make it challenging for general readers to understand. It would be helpful to clarify what the symmetries represent in the context of the three experiments. Are these symmetries intended primarily to enhance performance in gauge-equivariant CNNs, or do they have a broader purpose? Specifically, the paper lacks a clear explanation of why learning local symmetries, as opposed to global symmetries, is crucial for the chosen tasks. The connection between the limitations of existing symmetry discovery pipelines and the need for ATLAS is not fully established. It is not clear why existing methods fail to capture the specific local symmetries that ATLAS aims to uncover.

2. While the three experiments in Section 5 provide concrete examples, the connections between group actions, cosets, and the datasets are not immediately apparent. It would be beneficial for the authors to explicitly state these connections within each experimental subsection to enhance clarity. For instance, in the heat equation experiment, the specific group action on the temperature field and how it relates to the discovered O(2) symmetry should be made explicit. Similarly, in the top-tagging experiment, the role of infinitesimal generators and the practical implications of the discovered cosets need further elaboration. The paper should clarify how these mathematical constructs manifest in the actual data and the physical systems being modeled.

3. The objective of the experimental section lacks clarity. If the primary goal is benchmarking, the comparisons with other methods appear limited. On the other hand, if the goal is to illustrate the advantages of local symmetries over global symmetries, it remains unclear how these local symmetries contribute to downstream tasks. Providing more specific insights into the role and utility of local symmetries in these tasks would improve the section’s effectiveness. The experiments should more clearly demonstrate the practical benefits of using the discovered local symmetries, beyond simply showing that they can be found. For example, how does incorporating these local symmetries improve the performance of downstream tasks compared to using global symmetries or no symmetry information at all? The paper needs to quantify the advantages of local symmetry in a more rigorous manner.

### Questions
See weakness

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper presents ATLAS, a method for discovering local symmetry. It defines atlas locality and atlas equivariance to formalize local symmetry. ATLAS is based on trained predictors, sequentially treating Lie algebra bases and coset representatives as learnable parameters, with the optimization objective being the equivariant loss $\mathcal{L}(\Phi_c(g \cdot x), g \cdot \Phi_c(x))$. It then compares the relationship between gauge equivariance and atlas equivariance. Experimental results demonstrate that this method can correctly identify local symmetry in the task.

### Strengths
This paper focuses on the unique problem of local symmetry discovery and formally defines atlas equivariance to distinguish between global symmetry and local symmetry. In addition to Lie algebra bases, ATLAS can learn coset representatives, thereby discovering discrete symmetry.

### Weaknesses
- I disagree with the core argument of this paper: previous methods for symmetry discovery could only find global symmetry rather than local symmetry. In Algorithm 1, the atlas $\mathcal{A}$ of the manifold $\mathcal{M}$ needs to be specified manually. However, after completing this step, we can treat the symmetry discovery for each chart $(U_c, \varphi_c)$ as separate subproblems, with their common symmetry being the atlas symmetry. These subproblems do not differ from global symmetry discovery, as mentioned in Definition 2, where each mapping $\Phi_c$ is globally equivariant. Therefore, previous methods for symmetry discovery can be naturally extended to the case of local symmetry. For example, we can apply LieGG [1] on each trained predictor $\Phi_c$, or apply LieGAN [2] on the data of each chart $\mathcal{D_c} = \{(X_i: U_c \rightarrow \mathbb{R}^{d_{in}}, Y_i: U_c \rightarrow \mathbb{R}^{d_{out}})\}_{i=1}^{n_c}$.

- ATLAS simply treats group generators as learnable parameters and optimizes the equivariant loss $\mathcal{L}(\Phi_c(g \cdot x), g \cdot \Phi_c(x))$. I think that this approach has limited contributions to the problem of symmetry discovery. It does not show significant advantages over previous methods and has some drawbacks. For example, compared with LieGG [1], which mathematically solves Lie algebra bases, ATLAS has poorer interpretability; compared with LieGAN [2], which directly discovers symmetries from datasets, ATLAS is highly dependent on the accuracy of trained predictors. Furthermore, in Appendix B, it is mentioned that the number of Lie algebra bases $k$ is determined by incrementally increasing from a minimum value. Will this lead to significant computational overhead when the true $k$ is large? If the norm of the weakest generator varies continuously, will changes in the set threshold also affect the final result for $k$?

- The reason why the method can work lacks rigorous explanation. See the first two questions for details.

- Suggestion on presentation: "atlas" refers to a collection of local regions or charts that cover a manifold, while "ATLAS" stands for automatic local symmetry discovery. The use of the same word, differing only in capitalization, may confuse readers.

### Questions
- Does Equation (3) in Section 4.2.1 (calculating the absolute value first and then the cosine similarity) have any practical significance mathematically? I am skeptical about whether it works in all cases. Can you provide a theoretical proof that when $\mathcal{L}_{str}(B)$ is minimized, the number of non-zero elements shared among different basis vectors is also minimized?

- In Section 4.2.2, when learning coset representatives, even though the number of random matrices $K$ is much larger than the actual number of cosets, will all these matrices converge to the strong symmetry embodied by the predictor $\Phi_c$? Formally, if for $\forall C \neq C_1, C_2$, we have $\mathcal{L}(\Phi_c(C_1 \cdot x), C_1 \cdot \Phi_c(x)) < \mathcal{L}(\Phi_c(C_2 \cdot x), C_2 \cdot \Phi_c(x)) \ll \mathcal{L}(\Phi_c(C \cdot x), C \cdot \Phi_c(x))$ (where we omit the normalization notation for brevity). In this case, it is possible that all matrices converge to $C_1$ while missing the symmetry corresponding to $C_2$.

- In Section 5.2, does the $\mathrm{SO}(2)$ transformation refer to rotating the entire field around the origin of the coordinate system, or does it refer to rotating each chart separately around its center point? In Figure 6b, which charts correspond to local predictors $\Phi_c$ that exhibit global symmetry?

- In the assumptions of Theorem 1, it is already mentioned that $M$ is $G$ gauge equivariant. Is it necessary to further elaborate that $M$ is $G$ equivariant in the third paragraph of the proof? When the manifold is Euclidean space, are gauge equivariance and equivariance naturally equivalent?

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
In this paper, the authors proposed a new method called atlas to capture symmetries in local neighborhoods. Local symmetries of a function is recovered by training local predictor networks and learning a Lie group basis to ensure the learned predictors are equivariant. To illustrate the efficacy of the proposed method, the authors experimented on a few well-designed tasks.

### Strengths
1. The problem of local symmetry may have some specific applications as the authors presented in the experiment section. The proposed method might be a good complement to the global sysmmetry discovery methods.

### Weaknesses
1. Motivation of this work is not well clarified. Since existing equivariant models can achieve global symmetries, then local symmetries are also guaranteed at the same time. The authors are encouraged to show important problems or areas where we do not care about global symmetries, but insteand local symmetries are more important.

2. Theoretically I am not seeing advantages of the proposed method over existing methods. The authors are encouraged to clarify novelty of this work and present more analysis on why the proposed method is superior to existing methods.

### Questions
1. Since Gauge equivariant neural networks could enforce local symmetries, what are the major differences between the proposed atlas and the Gauge equivariant neural networks? Does theorem 1 mean they are equivalent under certain conditions?   

2. In Algo.1 the authors train a predictor network for each chart. What are the scales of the chart? Talking about local symmetries, I assume the locality can be referred at different scales. It also depends on the problem/data themselves. 

3. What are the trade-offs when we optimize local symmetries using atlas? Do we lose global symmetries? How could we balance these two objectives?

4. Fig. 9, can the authors explain a little bit more on why the proposed method is superior to the LieGAN method? Visually the differences are subtle to me.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
Formalizing the notion of local symmetry as atlas equivariance, the authors proposed an automatic local symmetry discovery approach (ATLAS) to recover the local symmetries of a function using local predictor networks. They learned a Lie group basis to ensure that the predictors are equivariant, resulting in the discovery of local symmetry groups with multiple connected components. This approach was tested in experiments on top-quark tagging, synthetic partial differential equations, classification, and climate segmentation.

### Strengths
**S1.** The paper is very well-written and presented, with a well-defined motivation for studying local symmetries. 

**S2.** The development of a method to discover atlas equivariance in a given data distribution in the form of a Lie group is unique. 

**S3.** The experiments covered diverse datasets, including tasks like classification and segmentation, demonstrating the model's applicability across various domains.

### Weaknesses
 **W1.** The assumption of limiting the target group to a finite number of connected components requires further justification and additional experimentation, if possible. Lie groups can have an infinite number of components in some of the extensively researched areas like diffeomorphisms. I assume that this approach does not hold for such cases, which could limit the generalizability of the method to certain pre-defined knowledge. I would encourage the authors to shed more light on this limitation and to experimentally validate why the model might fail to converge, as they have suggested. Specifically, it's unclear how the method would handle situations where the local symmetries vary continuously, rather than being discrete components. The current approach seems to assume that the local symmetry group can be decomposed into a finite set of cosets, but this may not be true for many real-world scenarios. For example, if the local symmetry involves a continuous rotation, how would the method approximate this with a finite number of components? This limitation needs more rigorous discussion and empirical validation.

**W2.** As the downstream test results show very minor differences between the baselines and the proposed approach, what are the advantages of using this approach? Also, I would suggest the authors to experiment with some real-world image datasets. The current experiments, while diverse, do not convincingly demonstrate a significant advantage over existing methods. The small performance gains raise questions about the practical utility of the proposed method. It would be beneficial to see experiments on more complex and realistic datasets, such as those found in real-world image analysis, where local symmetries might play a more crucial role. The lack of substantial improvement in the downstream tasks makes it difficult to justify the added complexity of the proposed method.

**W3.** While the authors extensively focused on the inability of existing SOTA models to capture local neighborhoods, it would be great if the authors could experimentally compare them and validate this, specifically with models such as (Moskalev et al., 2022), (Dehmamy et al., 2021), LieGAN, and similar works that capture global symmetries. Comparing these models would effectively validate the authors' assumptions. The paper claims that existing methods fail to capture local symmetries, but this claim is not sufficiently backed by experimental evidence. A direct comparison with models that explicitly handle symmetries, both local and global, is necessary to validate this claim. Without such comparisons, it is difficult to assess the novelty and effectiveness of the proposed method relative to existing approaches. The lack of experimental validation against these specific models weakens the argument for the necessity of the proposed approach.

**W4.** I believe the incorporation of the symmetries discovered by ATLAS leading to parameter efficiency has not been validated. I request the authors to discuss how they ensure effective parameter efficiency with their proposed approach in the rebuttal. The claim of parameter efficiency needs to be rigorously demonstrated. It's not clear how the discovered symmetries directly translate into a more parameter-efficient model. The authors should provide a detailed analysis of the parameter counts and demonstrate that the proposed method indeed leads to a reduction in the number of parameters compared to baseline models, while maintaining or improving performance. Without this validation, the claim of parameter efficiency remains unsubstantiated.

**W5.** How can we randomly sample a localized function $\phi_c$ from $\phi$? Do we need to consider the random bias that might be introduced through the random sampling of $\phi_c$? Besides, is there any potential adversarial impact of the randomly sampled coefficient vector $\eta$ in terms of deriving the group element $g$?

**Minor**
- How the parameter $\epsilon$ is being selected? An ablation would be great to analyze the robustness of this parameter over the model's performance.

### Questions
I tried to cover most of my concerns and questions in the *Weaknesses* section. I kindly request the authors to review that section.

### Soundness
3

### Presentation
3

### Contribution
2
