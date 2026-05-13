# Learning Structured Representations by Embedding Class Hierarchy with Fast Optimal Transport

- Decision: Accept
- Scores: 5, 6, 8, 6, 8

## Abstract
To embed structured knowledge within labels into feature representations, prior work~\citep{zeng2022learning} proposed to use the \textbf{C}o\textbf{p}henetic \textbf{C}orrelation \textbf{C}oefficient (CPCC) as a regularizer during supervised learning. This regularizer calculates pairwise Euclidean distances of class means and aligns them with the corresponding shortest path distances derived from the label hierarchy tree. However, class means may not be good representatives of the class conditional distributions, especially when they are multi-mode in nature. To address this limitation, under the CPCC framework, we propose to use the Earth Mover's Distance (EMD) to measure the pairwise distances among classes in the feature space. We show that our exact EMD method generalizes previous work, and recovers the existing algorithm when class-conditional distributions are Gaussian. To further improve the computational efficiency of our method, we introduce the \textbf{O}ptimal \textbf{T}ransport-CPCC family by exploring four EMD approximation variants. Our most efficient OT-CPCC variant, the proposed Fast FlowTree algorithm, runs in linear time in the size of the dataset, while maintaining competitive performance across datasets and tasks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper aims to improve classification by incorporating similarities among classes. These semantic relationships between labels are introduced into the original problem as a regularizer. The paper assumes a hierarchical structure in the labels. Building on the work of Zeng et al. (2022), the authors replace Euclidean distances between class means with optimal transport (OT) distances between label distributions. To reduce the computational burden of OT distance, they use a modified version of a tree-based method called FlowTree, which relies on a predefined tree structure. The paper also introduces a differentiable method for training with their tree-based OT distance. Experimental results for the classification problem using the OT-based regularization method show improvements compared to the method in Zeng et al. (2022). However, the proposed FastFT regularization falls behind the performance of some other OT-based methods.

### Strengths
- The paper employs optimal transport (OT) distance to measure the distributions of labels rather than relying solely on the distance between class means. By capturing distributional differences, this approach aims to provide a more nuanced measure of class similarity.

- To address the high computational complexity typically associated with OT distance, the authors implement a tree-based approximation method. This approach enables more efficient computation while maintaining the benefits of OT-based similarity measures.

- Experimental results demonstrate that accounting for the distributional nature of labels enhances performance in tasks such as classification and class representation learning. This distribution-based approach proves beneficial in capturing class relationships more effectively than mean-based methods.

### Weaknesses
 - Theorem 3.2 appears to be a key contribution, as it establishes that Algorithms 1 and 2 can approximate the Earth Mover's Distance (EMD). However, the proof is vague and leaves several critical points open to interpretation. I found it challenging to follow the complete argument leading to the stated approximation result. Specifically, the connection between the flow update rules in Algorithm 1 and the tree-based optimal transport in Algorithm 2 is not rigorously established. The proof sketch should explicitly demonstrate how the simplified 1D flow in Algorithm 1 is equivalent to the more complex tree-based flow in Algorithm 2, given the augmented tree structure. A more detailed proof sketch could greatly enhance clarity and strengthen the manuscript.

- Similarly, while Lemma 3.4 provides the derivative of the EMD, the result itself is relatively straightforward. More importantly, it is unclear whether the same derivative result directly applies to FastTree. The paper states that the flow matrix P is constant with respect to model parameters, but it does not explicitly show how this constant flow matrix interacts with the gradient calculation when using the FastTree approximation. A formal proof confirming that this result holds for FastTree, including a detailed derivation of the gradient with respect to model parameters, would significantly enhance the paper's contribution and rigor.

- Another issue arises with the reliance on an assumed ground-truth tree structure. In most cases, this ideal tree is unknown or impractical to obtain, even if the underlying assumptions hold. As a result, multiple approximated trees may be used instead. The paper does not adequately address how gradient computations would handle these varied approximations, which is an important practical consideration. Specifically, the paper should discuss how the choice of different tree structures impacts the learned representations and the stability of the training process. The lack of a clear strategy for handling multiple tree approximations raises concerns about the robustness and generalizability of the proposed method.

- Finally, a literature review on learning label representations, accompanied by illustrative examples, would provide valuable context and motivation for the study. This would help readers appreciate the importance of this approach within the broader scope of label representation learning.

### Questions
See  the Weakness section.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper extends the work (Zeng et al. 2022) for learning structured representation by introducing the Earth Mover's Distance (EMD) to measure the pairwise distances among classes in embeddings. Moreover, a so-called Fast FlowTree algorithm is proposed to improve the computation efficiency, which is linear in the size of the dataset. Experiments show promising results.

### Strengths
+ It extends the $\ell_2$ norm based Cophenetic Correlation Coefficient (CPCC) (Zeng et al. 2022) to OT-CPCC by introducing EMD, which is essentially equivalent to assign different importance to each pair of data points when computing the gradients.
+ It presents a linear time approximation algorithm to solve the OP problem for learning the hierachical representation.
+ Extensive experiments are provided.

### Weaknesses
1.  To replace the $\ell_2$ distance between two class-centroids, the EMD is introduced based on representing class label by all samples in the class. If the number of samples in each class is large, then solving a single EMD is expensive in time cost. Notice that the distances are computed for pairwise classes, thus the times to compute EMD is quadratic to the number of classes. If the number of classes is large, then it is extremely expensive to compute the EMD based hierarchy information among embeddings.  While different approximation methods can be used, it is not clear about the computation cost, compared to the baseline methods. Specifically, the paper lacks a detailed analysis of the computational complexity of the proposed Fast FlowTree algorithm in relation to the number of classes and the number of samples per class. The practical implications of this computational cost, especially for large-scale datasets with numerous classes, are not sufficiently addressed. A more rigorous comparison with the computational cost of the $\ell_2$ based method is needed, including a breakdown of the time spent on different steps of the algorithms.

2. In Table 3, the preciseness of hierachical information listed show that in most cases, the presented FastFT based method cannot beat the $\ell_2$ norm based method. How to interprete the results in Table 3?

### Questions
1. While different approximation methods can be used, it is not clear about the computation cost, compared to the baseline methods. 
 
2. In Table 3, the preciseness of hierachical information listed show that in most cases, the presented FastFT based method cannot beat the $\ell_2$ norm based method. How to interprete the results in Table 3? 

3. Using AIC to estimate the number of modality of the classes sounds interesting.  Is there any more intuitive evidence to support the existence of multi-mode in feature distribution? Or,  whether the identified multi-mode classes could be visualized by e.g., t-SNE or UMAP?

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
2

### Summary
This paper presents a method for learning structured representations by embedding class hierarchies using Optimal Transport (OT) in the Cophenetic Correlation Coefficient (CPCC) framework. Traditional methods use Euclidean distances between class means to represent hierarchical information, which can be inaccurate for multi-modal distributions. The authors propose using Earth Mover’s Distance (EMD) to address this limitation and introduce Fast FlowTree (FastFT), a computationally efficient OT approximation algorithm for CPCC that operates in linear time.

### Strengths
The proposed algorithms are novel and scalable. The proposed method leads to performance improvements across multiple datasets. The work is impactful for applications needing hierarchical class embedding.

### Weaknesses
1. I feel section 3.3 can be simplified by moving some derivations and technical discussion to the appendix. 
2. Label embedding methods have been employed in extreme classification (see datasets: http://manikvarma.org/downloads/XC/XMLRepository.html). The authors may want to experiment on those datasets to verify scalability and compare to existing embedding methods.

### Questions
see Weaknesses

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper addresses the challenge of embedding hierarchical structures in feature representations for supervised classification tasks. It builds upon existing work that uses the Cophenetic Correlation Coefficient (CPCC) to enforce hierarchical structure alignment but innovates by employing the Earth Mover’s Distance (EMD) within this framework. The authors also propose a new, efficient algorithm, Fast FlowTree (FastFT), to approximate EMD in linear time, making it feasible to apply OT-based regularization to large datasets.

### Strengths
1. The paper is well-written and easy to follow.
2. The paper makes a theoretical extension by generalizing CPCC with EMD, allowing the model to handle more complex, non-unimodal distributions that Euclidean-based methods struggle with. This extension is theoretically sound and shows how OT can capture nuanced hierarchical structures in data.

### Weaknesses
1. The improvement of FastFT and EMD, which appears to be the paper’s key contribution, is modest on empirical datasets, showing less than a 1% gain on average across three random seeds. This marginal improvement in accuracy raises questions about the practical significance of the proposed method, especially considering the added complexity of EMD and its approximation. The gains should be more substantial to justify the shift from simpler methods.
2. The computation time for empirical datasets is not reported. This omission makes it difficult to assess the practical applicability of the proposed method, especially given the known computational cost of EMD. Without concrete timing results, it is hard to evaluate the efficiency of the FastFT approximation compared to both the exact EMD and other alternatives.
3. The paper is a follow-up to the CPCC work by Zeng et al. (2022), with the addition of EMD. The novelty of introducing Fast FlowTree is somewhat limited. While the use of EMD is a theoretical contribution, the practical impact of FastFT, as an approximation algorithm, needs further justification, especially given the modest empirical gains.

### Questions
While the paper proposes FastFT for computational efficiency, can the authors provide a clear comparison of computation time on empirical datasets?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper tackles the problem of structured knowledge embedding in supervised learning, i.e., how to enforce that representations encode structures in the label space. An example of structure in label space is when labels are hierarchical (e.g., dog -> husky, bulldog, etc). Previous work has considered comparing class-conditional distributions through the Euclidean distance of the mean of their samples. However, as the authors remark, this choice is restrictive as it does not really capture all the information of a distribution (e.g., multi-modality, covariances, etc). The authors propose using the EMD to compare these class-conditionals, improving the learning of representations.

---

__Post-Rebuttal__

The authors did a good job on the rebuttal, and addressed all of my concerns. I also praise the initiative of running further experiments with the Bures-Wasserstein metric, which proved to be too computationally heavy for the task at hand (since $d \gg n$).

Overall, this is a strong submission, so I decided to increase my score from __6. Marginally above the acceptance threshold__ to __8. Accept, good paper__.

### Strengths
- The ideia is good. OT makes a good contribution to the considered problem, especially concerning how distributions are compared and embedded in the tree structure.

- The authors present a solid analysis of how to extend the $\ell_{2}$-CPCC framework to OT, especially concerning differentiating through linear programming.

- The authors' experiments show a solid improvement over previous framework under a variety of ways of computing Wasserstein distances.

### Weaknesses
 - In Table 1 (Sec 2.2), I do not think that these complexities are straightforward to derive. Can the authors point to the reasoning to their derivation? For instance, EMD's complexity is tipically $\mathcal{O}(n^{3}\log n)$ instead of $\mathcal{O}(n(d+n^{2}\log n))$.

- While I got what the authors are trying to express with prop. 3.1, and the result is true if stated correctly, I think the authors could rephrase it for better clarity. First, "$\ell_{2}$ for Gaussians" is not mathematically correct, since the $\ell_{2}$ norm or distance is defined for vectors. The closest term to this expression would be an $L_{2}$ norm or distance between probability distributions, but it is not equivalent to the $\ell_{2}$ distance between the means. I propose that the authors change the statement to "EMD reduces to $\ell_{2}$ distance between the means". Other ways of rephrasing this are possible, see my suggestions and questions below. Likewise, an appropriate reference to (Takatsu, 2011) would be interesting.

- In table 4, the objective "Flat" is not explained. From the overall context, I guess this corresponds to learning with no structure tree, but this is not clear to me.

### Questions
# Suggestions

- In Sec. 2.2, I suggest the authors to comment more specifically on the complexity of OT and its variants. I get that this is somewhat done in Table 1, but I did not find any references to this table. I think a clear discussion on the text would be beneficial (and, of course, a reference to the table).

- For better uniformity and clarity, the authors might want to change references to the EMD as a distance in favor of $2-$Wasserstein distance, which is what is actually used in the paper. For instance, in most tables the authors use EMD and terms involving the Wasserstein distance (TWD or SWD).

- In section 3.3, when authors are comparing the gradients of $\ell_{2}-$CPCC and OT-CPCC, I think the authors can make 2 further links, if they agree with the following discussion. First, the comparison of distributions' centroids can be understood as computing the MMD, with a linear kernel, between those distributions. This can further make the link with other probability metrics, and arguably, OT yields a richer geometry than this simplistic choice. Second, if one chooses to approximate OT through the Sinkhorn algorithm, letting the entropic regularization penalty $\epsilon \rightarrow +\infty$ leads to the trivial coupling $P_{ij} = 1/nm$. In this case, OT-CPCC boils down to the $\ell_{2}-$CPCC algorithm, modulo a scaling factor on the gradients. The authors can also cite (Feydy et al, 2019) which discusses these relations in depth.

# Questions

I have only one question, which I detail below.

Proposition 3.1 left me wondering if it would not be possible to run OT-CPCC with a parametric approximation of the classes through Gaussian measures. This way, instead of calculating EMD between classes, one would use the Bures-Wasserstein metric,

$\mathcal{W}_{2}(P,Q)^{2}  = \lVert \mu\_{P} - \mu\_{Q} \rVert\_{2}^{2}  +  Tr(\Sigma\_{P} + \Sigma\_{Q} - 2(\Sigma\_{P}^{1/2}\Sigma\_{Q}\Sigma\_{P}^{1/2})^{1/2}).$

With this approach, you could trade the complexity with respect the number of samples to a complexity with respect number of dimensions, which may be desirable depending on the problem at hand. Some authors have used this in other contexts (e.g., (Alvarez-Melis and Fusi, 2020)).

Furthermore, stressing the idea that class-conditionals are multi-modal, GMMs could be fit on these conditionals, then compute Mixture-Wasserstein (Delon and Desolneux, 2020) distances between the class-conditionals.

### Soundness
4

### Presentation
4

### Contribution
3
