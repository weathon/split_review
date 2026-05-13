# Diffusion Transportation Cost for Domain Adaptation

- Decision: Reject
- Scores: 6, 3, 6, 5, 6

## Abstract
In recent years, there has been considerable interest in leveraging the Optimal Transport (OT) problem for domain adaptation, a strategy shown to be highly effective. 
However, a less explored aspect is the choice of the transportation cost function, as most existing methods rely on the pairwise squared Euclidean distances for the transportation cost, potentially overlooking important intra-domain geometries.
This paper presents Diffusion-OT, a new transport cost for the OT problem, designed specifically for domain adaptation. By utilizing concepts and tools from the field of manifold learning, specifically diffusion geometry, we derive an operator that accounts for the intra-domain relationships, thereby extending beyond the conventional inter-domain distances.
This operator, which quantifies the probability of transporting between source and target samples, forms the basis for our transportation cost. 
We provide proof that the proposed operator is in fact a diffusion operator, demonstrating that the cost function is defined by an anisotropic diffusion process between the domains.
In addition, to enhance performance, we integrate source labels into the operator, thereby guiding the anisotropic diffusion according to the classes.
We showcase the effectiveness of Diffusion-OT through comprehensive experiments, demonstrating its superior performance compared to recent methods across various benchmarks and datasets.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a novel transportation cost function, termed Diffusion-OT, for the Optimal Transport (OT) problem in the context of domain adaptation. Diffusion-OT leverages concepts from diffusion geometry and manifold learning to account for both intra-domain and inter-domain relationships. The proposed cost function is derived from a composite diffusion operator that consists of three diffusion steps: within the source domain, across domains, and within the target domain. By incorporating source label information into the diffusion process, Diffusion-OT can guide the anisotropic diffusion according to class labels. Experiments on various benchmarks demonstrate that Diffusion-OT outperforms competing methods, achieving state-of-the-art results on non-Euclidean data.

### Strengths
1. The proposed Diffusion-OT cost function is a novel approach that goes beyond the traditional squared Euclidean distance used in OT for domain adaptation. It considers both intra-domain and inter-domain geometries.
2. Experimental results show that Diffusion-OT achieves superior performance compared to baseline and recent OT-based methods across multiple datasets, demonstrating its effectiveness in domain adaptation tasks.

### Weaknesses
1. The first concern is the complexity and computational cost. The composite diffusion operator involves multiple steps and may lead to higher computational cost compared to simpler cost functions. The computational complexity of the proposed method, especially when dealing with large-scale datasets, is not fully discussed. Specifically, the paper does not provide a detailed breakdown of the time complexity for each step of the diffusion process, making it difficult to assess the practical scalability of the approach. For example, the matrix multiplications involved in the diffusion process can be computationally expensive, and the paper lacks a discussion on how these operations scale with increasing data size. Furthermore, the memory requirements for storing the intermediate matrices are not addressed, which is a crucial factor when dealing with high-dimensional data.

2. Theoretical analysis limitations: While the paper provides theoretical analysis, it mainly focuses on the asymptotic behavior of the diffusion operators. A more rigorous analysis of the convergence properties and error bounds of the proposed method would strengthen the theoretical foundations. The paper does not provide any guarantees on the convergence of the proposed method to an optimal solution, nor does it offer any analysis of the error bounds of the approximation. This lack of theoretical guarantees makes it difficult to assess the robustness and reliability of the method, especially in scenarios where the data distribution is complex or noisy.

3. Incomplete analysis of failure cases: Although the authors admit the limitation of the proposed method is its assumption that both source and target domains reside in the same space. The authors do not provide detailed analysis of failure cases. As a result, we cannot clearly evaluate the negative impact when applying the proposed method in the real-world applications where the domains have substantially different underlying structures. This could limit the generalizability of the proposed method. For instance, the paper does not discuss how the method would perform if the source and target domains have significantly different dimensionality or if the underlying manifolds are topologically distinct. A more thorough investigation of these scenarios is needed to understand the limitations of the proposed approach.

### Questions
See weaknesses.

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
5

### Summary
This paper proposes a domain adaptation method based on optimal transport. A diffusion optimal transport model is leveraged to construct a transport cost function between samples, in which intra-domain local geometry is introduced. The experiments are conducted on simulated and benchmark datasets to evaluate the performance of the proposed method.

### Strengths
1. In general, the paper is well-organized and easy to follow.

2. Both synthetic and real-world datasets are used in the experiments.

### Weaknesses
1. It is not new to introduce intra-domain geometry for domain adaptation. Intra-domain geometry has been widely considered in optimal transport and domain adaptation. For example, the Gromov-Wasserstein discrepancy considers transport between two metric spaces, and intra-domain geometry is involved in the construction of the metric. This has been introduced for cross-domain applications, as shown in [a][b].

2. Section 1 states that the weights in ETD and RWOT are learned, rather than directly derived from the data as in Diffusion-OT, which limits their applicability to deep learning. This statement is questionable. Intuitively, it is usually a good strategy to learn some properties such as weights or distance from data, which can adaptively extract geometric information involved in data and enhance the performance. Different from the learning strategy, the proposed method adopts a pre-defined approach to obtain a transport cost. The pre-defined paradigm may not obtain good performance if the adopted approach is not appropriate for real-world data.

3. Section 4 states that unsupervised domain adaptation implies that both domains are supported on the same hidden manifold. This assumption is vague. Domain shift could come from different marginal distributions, different conditional distributions, or some other factor. What is the specific assumption adopted in the submission? A detailed discussion should be provided.

4. The compared methods are out-of-the-date. Domain adaptation is an active area with many advances in recent years. It is easy to find state-of-the-art methods published recently as the comparison, such as (but not limited to) [c][d], which are also optimal transport-based methods for domain adaptation.

5. The results on Office-Home are lower than the results shown in [c]. Does the difference come from a different backbone model? If so, it is encouraging to adopt a better backbone to evaluate the performance of the methods.

6. It would be better to evaluate the impacts of the hyper-parameters $\epsilon$ used in the Gaussian kernel functions.

### Questions
1. Section 4 states that unsupervised domain adaptation implies that both domains are supported on the same hidden manifold. This assumption is vague. What is the specific assumption adopted in the submission? A detailed discussion should be provided.

2. It would be better to conduct more state-of-the-art methods.

3. The results on Office-Home are lower than the results shown in [a]. Does the difference come from a different backbone model? If so, it is encouraging to adopt a better backbone to evaluate the performance of the methods.

4. It would be better to evaluate the impacts of the hyper-parameters $\epsilon$ used in the Gaussian kernel functions.

### Soundness
2

### Presentation
3

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
A novel transport cost, Diffusion-OT, is proposed in this paper for OT problem. By utilizing concepts of diffusion geometry, the authors derive an operator to quantify the probability of transporting between source and target samples. The authors give proof that the cost function is defined by an anisotropic diffusion process between the domains. Experiments show the superior performance of the proposed cost.

### Strengths
A new transportation cost, Diffusion-OT, is proposed which enables the learning of the geometries and relationships both between and within the two domains by considering both inter-domain distances and intra-domain structures. 
By incorporating source label information into the cost, the proposed method is compatible with any OT solver and problem formulation.
Experiments demonstrate the effectiveness of the proposed method.

### Weaknesses
The results in Tab.1 and Tab.2 do not include all baseline methods, for example, results of  RWOT and ETD did not appear in the VisDA experiment. The absence of these results makes it difficult to fully assess the performance of the proposed method against the state-of-the-art. Specifically, the lack of RWOT results on VisDA is a notable omission, given its relevance as a competitive baseline in domain adaptation. Furthermore, the improvement on the digits dataset is relatively small, raising questions about the practical significance of the proposed method on simpler tasks where standard OT costs may already perform adequately. It's unclear if the added complexity of Diffusion-OT justifies the marginal gains observed in such cases.

### Questions
Does the proposed method has generalization on more general Universal Domain Adaptation tasks？Cause the Universal Domain Adaptation setting is more widely existing in practice.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents Diffusion-OT, a transport cost designed for the optimal transport (OT) problem with a focus on domain adaptation. Specifically, the authors adopt concepts from manifold learning, i.e., diffusion geometry, to derive an operator that captures intra-domain relationships. This operator quantifies the probability of transporting samples between the source and target domains, forming the foundation of the transportation cost.  Comprehensive theoretical proofs and extensive experiments demonstrate the effectiveness of the proposed method.

### Strengths
1.	This paper presents a graph-based transport cost that accounts for both cross-domain distances and intra-domain structures.
2.	Incorporating theoretical concepts from diffusion processes enhances the depth and rigor of the proposed method.
3.	Empirical results demonstrate the effectiveness of Diffusion-OT across various scenarios, indicating its practical applicability.

### Weaknesses
1.	The motivation of this paper is unclear. In the Introduction section, the authors state that “one aspect that remains relatively unexplored is the selection of the transportation cost function”, but they fail to provide compelling reasons for the need to investigate this aspect. Moreover, the authors do not analyze the advantages and disadvantages of existing methods, further diminishing the clarity of the research motivation. Specifically, the introduction lacks a discussion on why commonly used costs like the squared Euclidean distance are insufficient for domain adaptation tasks, and what specific limitations they present in capturing the underlying data manifold structure. A more detailed analysis of these shortcomings would strengthen the motivation for exploring alternative cost functions.
2.	The literature review is notably limited, lacking engagement with significant recent advancements in optimal transport and domain adaptation. This paper mainly compares with related works before 2023. It would benefit from a comparison and discussion of additional recent studies, such as [1-5]. The review should include a more thorough discussion of how these recent methods address similar challenges and how the proposed method differs or improves upon them. For example, a discussion of the specific advantages and disadvantages of graph-based methods versus other approaches would be beneficial.
3.	Why does the proposed method exhibit inferior performance compared to RWOT on the MNIST-USPS dataset? More discussions are required. The paper should provide a more in-depth analysis of the factors contributing to this performance discrepancy. This could include an examination of the specific characteristics of the MNIST-USPS dataset that might favor the RWOT approach, or a discussion of potential limitations of the proposed method in this particular scenario.
4.	The recent method SPA [2] demonstrates superior performance compared to the proposed methods in the Office-Home (75.3% v.s 72.43%) and VisDA (87.7% v.s 78.56%) datasets. What advantages does the proposed method offer compared to traditional domain adaptation techniques? The paper should clarify the specific scenarios where the proposed method is expected to outperform existing domain adaptation techniques, and provide a more detailed discussion of the trade-offs involved. A more comprehensive comparison with state-of-the-art methods is needed to justify the contribution of the proposed method.
5.	The proposed method involves several hyperparameters(e.g., \lamda, \epsilon). Conducting ablation studies on these hyperparameters would provide valuable insights into the sensitivity of the proposed method and its performance. The paper should include a detailed analysis of how the performance of the proposed method varies with different hyperparameter settings, and provide guidelines for selecting appropriate values for these parameters.

### Questions
Please see above.

### Soundness
2

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
4

### Summary
This paper focuses on the methodological aspect of optimal transport (OT) for domain adaptation. A major motivation is that existing OT works rarely consider the construction and impact of cost functions, which is generally crucial for the property of the OT measure and its induced transport plan. To deal with this limitation, this work proposes a diffusion-based cost formulation, which endows the transport cost with the property of cross-distribution propagation. The theoretical result shows that the proposed cross-domain diffusion operator indeed characterizes the cross-domain discrepancy and intra-domain diversity. Experiments are conducted on standard domain adaptation datasets to evaluate the proposed method.

### Strengths
+ The motivation for improving OT from the perspective of the cost function is technically sounded.

+ Theoretical results that show the implications of constructed diffusion operator is reasonable. 

+ The empirical improvement over other OT-based domain adaptation methods on several benchmarks.

### Weaknesses
1. The relation between the diffusion process and OT should be further clarified; besides, it seems that there are fundamental issues in the validity of OT with designed cost.

2. The implications of diffusion operator for distribution shift correction could be improved, e.g., the superiority of proposed cost design is not sufficiently explained in the current manuscript.

3. The details for the optimization procedure could be improved; the comparison experiment for method validation should contain more hard transfer tasks.

### Questions
**Concerns**

Q1. As far as I understand the Diffusion-OT, the key difference between it and existing OT works is that Diffusion-OT introduces the composition of stochastic matrices, i.e., ‘source to source transition’, ‘source to target transition’ and ‘target to target transition’, to construct the cost function. However, it seems that there are no explanations on what special properties are ensured by the Diffusion-OT from OT’s view, e.g., JDOT measures the joint distribution discrepancy, POT/UOT relaxes the strict constraints under severe shift scenarios. Some justifications are appreciated.

Q2. Is the constructed cost function $C=-log(S)$ still a metric? Since the metric property is necessary to ensure the validity of OT. Besides, if it is a metric, which kind of discrepancy does it characterize (e.g., joint/conditional/marginal distribution discrepancy)? 

Q3. Prop. 1 shows that the diffusion operator $S$ can reflect the cross-domain discrepancy and intra-domain diversity from the view of LB operator. However, it seems that there is no guarantee that the proposed method can control the diffusion process, i.e., suppress cross-domain divergence and enlarge the intra-domain divergence. Therefore, it is hard to understand the learning process and the properties of the proposed method. Detailed discussion on the optimization and learning procedure would be helpful to improve the clarity.

Q4. In the diffusion operator $S$, the three stochastic matrices are construed with distance-based kernel function on original space $\mathcal{X}$, e.g., Eqs. (4)-(5). Should they be formulated in representation space $\mathcal{Z}$? If so, are the representations considered variables under the optimization process? What are the learning principle and its intuitive goal for the diffusion operator $S$?  An in-depth analysis of the diffusion mechanism in the learning process is high expected.

Q5. Though this work achieves improvements over some existing OT methods, the comparison seems insufficient. On the one hand, some advanced OT methods that have similar goals/ideas to the proposed methods are omitted, e.g., key-point guided OT [a], mask OT [b], and general cost function [c]. Especially, considering the label-guided graph construction in Eq. (11), it indeed has the same idea as the mentioned works. On the other hand, the experiment could be extended to larger and harder datasets, e.g., DomainNet. 

**References**

[a] Xiang Gu, Yucheng Yang, Wei Zeng, Jian Sun, and Zongben Xu. Keypoint-guided optimal transport with applications in heterogeneous domain adaptation. In NeurIPS, 2022.

[b] Jiying Zhang, Xi Xiao, Long-Kai Huang, Yu Rong, and Yatao Bian. Fine-tuning graph neural networks via graph topology induced optimal transport. In IJCAI, 2022

[c] Asadulaev, A., Korotin, A., Egiazarian, V., Mokrov, P., & Burnaev, E. Neural Optimal Transport with General Cost Functionals. In ICLR, 2024.

### Soundness
2

### Presentation
3

### Contribution
2
