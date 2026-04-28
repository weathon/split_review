# Learning Graph Invariance by Harnessing Spuriosity

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
Recently, graph invariant learning has become the _de facto_ approach to tackle the Out-of-Distribution (OOD) generalization failure in graph representation learning. They generically follow the framework of invariant risk minimization to capture the invariance of graph data from different environments. Despite some success, it remains unclear to what extent existing approaches have captured invariant features for OOD generalization on graphs. In this work, we find that representative OOD methods such as IRM and VRex, and their variants on graph invariant learning may have captured a limited set of invariant features. To tackle this challenge, we propose LIRS, a novel learning framework designed to Learn graph Invariance by Removing Spurious features. Different from most existing approaches that _directly_ learn the invariant features, LIRS takes an _indirect_ approach by first learning the spurious features and then removing them from the ERM-learned features, which contains both spurious and invariant features. We demonstrate that learning the invariant graph features in an _indirect_ way can learn a more comprehensive set of invariant features. Moreover, our proposed method outperforms the second-best method by as much as 25.50% across all competitive baseline methods, highlighting its effectiveness in learning graph invariant features.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces LIRS, a framework designed to improve Out-of-Distribution (OOD) generalization in graph representation learning by decoupling spurious and invariant features. The authors propose a two-step approach: (1) identifying and removing spurious features using a biased infomax principle, and (2) isolating invariant features through a class-conditioned cross-entropy loss. This method is positioned as an alternative to learning invariant features directly from graph representations, offering a new perspective on handling spurious correlations in graph learning.

### Strengths
- The paper is well-structured and easy to follow, with clear motivation for the proposed approach.

- The strategy of first learning and removing spurious features is an interesting and novel perspective on OOD generalization in graph learning. This decoupling of spurious and invariant features is a unique contribution to the field, offering a potential advantage over direct approaches.

### Weaknesses
 - The two-stage process introduces additional complexity in the learning pipeline, which may increase computational costs and practical challenges. A more detailed discussion of potential trade-offs, such as time complexity and training efficiency, would be beneficial. Specifically, the paper lacks a rigorous analysis of how the biased infomax step scales with graph size and feature dimensionality. The computational overhead of identifying and removing spurious features, especially in large graphs, is not thoroughly addressed. Furthermore, the paper should clarify whether the two-stage approach introduces any instability or convergence issues compared to single-stage methods.

- The novelty of the contribution could be clearer, as parts of the method bear resemblance to existing work, particularly in the use of biased infomax and cross-entropy loss. A deeper comparison with related approaches, such as OOD-GCL or EQuAD, would strengthen the paper. The paper needs to articulate more precisely how the proposed biased infomax differs from standard infomax in the context of graph representation learning. The specific modifications and their impact on feature disentanglement should be detailed. Additionally, the paper should provide a more nuanced discussion on the limitations of cross-entropy loss for invariant feature learning and how the proposed alternative addresses these limitations.

### Questions
- How does the multi-step process of identifying and removing spurious features impact overall model efficiency? Have any time or resource costs been benchmarked compared to existing methods?

- Can the authors provide a more detailed explanation of how LIRS differs from related works like EQuAD or OOD-GCL?

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
3

### Summary
This paper proposes LIRS, a learning framework designed to Learn graph invariance, which consists of: a) The biased infomax principle, and b) The class-conditioned crossentropy loss, which elicit effective spuriosity learning and invariant learning respectively, aiming to learn more invariant features. Different from most existing approaches that directly learn the invariant features, LIRS takes an indirect approach by first learning the spurious features and then removing them from the ERM-learned features.

### Strengths
1.  The structure of the paper is clear and easy to follow.
2.  The paper conducts comprehensive experiments to demonstrate the performance of proposed method.

### Weaknesses
1.  The novelty seems limited. The core idea of LIRS is three parts, i.e., graph Invariance learning by removing spurious features, the biased infomax principle, and the class-conditioned cross-entropy loss. However, the first part is inspired by [1], the second part seems to be a combination of SCL[2] and DGI[3], the third part is the generalized cross-entropy (GCE) method[4]. The technical contribution is a little weak. It is recommended that the author provide a clearer description of the contribution.
2.  The proposed LIRS requires training the GNN encoder twice, which is more cost than the end-to-end methods. It is recommended that the authors provide an overall time cost.
3.  LIRS takes an indirect approach by first learning the spurious features by self-supervised and then removing them from the ERM-learned features. OOD-GCL[5] proposes a contrastive learning module with invariance regularization so that spurious correlations between latent factors in graph representation can be eliminated and OOD predictions in downstream tasks can be achieved. It is suggested that the authors analyze and compare OOD-GCL that directly learns invariant representations by self-supervised.

### Questions
See the Weaknesses

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
2

### Summary
This paper presents LIRS (Learning graph Invariance by Removing Spurious features), a novel framework for improving Out-of-Distribution (OOD) generalization in graph representation learning. It critiques existing methods like IRM and VRex for capturing only limited invariant features. Instead of directly learning invariant features, LIRS first identifies and removes spurious features from those learned via Empirical Risk Minimization (ERM). The framework utilizes the biased infomax principle for learning spurious features and a class-conditioned cross-entropy loss for isolating invariant features. This work offers a robust approach to enhancing OOD generalization in graph learning.

### Strengths
1. The paper is well-written and easy to follow.
2. The strategy of decoupling invariant and spurious features is common in the field, but learning the spurious features first before removing them offers a new perspective. This approach provides a novel way to tackle the challenges of OOD generalization in graph representation learning.

### Weaknesses
Complexity: The process of first identifying spurious features and then removing them may introduce additional complexity in the learning pipeline. Discussing the computational efficiency and potential challenges in this two-stage process would be useful for understanding the trade-offs involved.

### Questions
Is there an analysis of how the multi-step process in this indirect learning approach affects the overall results? Additionally, during empirical training, what observations did you make? If the final performance does not improve, how would you analyze the sources of performance issues?

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
This paper presents a graph invariant learning method based on spurious feature learning, termed LIRS. The authors argue that directly learning invariant features is challenging, prompting them to first learn spurious features in order to decouple them from graph representation to get the invariant parts, thus this approach necessitates training the encoder for two times, separately. They introduce a learning objective called bias infomax for the spurious feature encoder, and a loss function $L_{inv}$ designed to encourage the encoder to learn invariant features. The authors validate the effectiveness of both loss functions through theoretical analysis. 


However, I find the theoretical feasibility of $L_{inv}$  to be somewhat questionable (see the question part). Additionally, the proposed method appears to be more complex than standard graph invariant learning methods, yet there is no discussion of its efficiency (e.g., time complexity or reported training times), which raises concerns for me. Therefore, I rated it a 5, anticipating that the authors will address my issues, which may prompt me to reconsider my score.

### Strengths
1. I agree that learning invariant features indirectly is intuitively likely to be easier and achieve better performance than a direct approach.

2. The authors provide some experimental analysis to support its motivation, as well as some theoretical analysis to justify the two optimization objectives.

3. Good experimental performance.

### Weaknesses
1. The author lacks a clear description of the differences between this method and the existing methods. As far as I know, for example, EQuAD, which the author has cited many times, I checked the article and found that the model pipeline of LIRS is very close to it, and the differences seem to be only whether utilize bias infomax and the definition of $s$ in $L_{inv}$.

2. Missing details about the model, such as how to optimize bias infomax? As far as I know mutual information is hard to calculate, how does GSAT get the subgraph? Why choose this approach?

3. About $L_{inv}$, I think it's implemented using cross entropy, $\hat{s}^{i}$ is the prediction of the environmental label ${s}^{(i)}$ by using $\hat{h_G}$ , and look forward to by minimizing the cross entropy to make prediction closer to real label. Intuitively, i don't think this is helpful for learning invariant learning, because if the learned representation is the invariant feature, I don't think $\hat{h_G}$ should be able to predict the correct  ${s}^{(i)}$, since it should only be related to labels. Mathematically speaking, the authors claim in Proposition 7 in the Appendix that minimizing $L_{inv}$ is equivalent to maximizing the conditional entropy $H(s^{(i)}|\hat{h_G^i})$, 
which I doubt is valid. Known $L_ {inv} $ is cross entropy, we have a $H(s^{(i)}|\hat{h_G^i})$ = $H(s^{(i)},\hat{h_G^i})$-$H(\hat{h_G^i})$ .Minimizing the cross-entropy loss ($H(s^{(i)},\hat{h_G^i})$) fails to maximize the conditional entropy.

4. LIRS requires multi-step training and involves multiple models (GSAT,SVM, etc.). Is it less efficient than existing graph-invariant learning models?

### Questions
1.  About $L_{inv}$, I think it's implemented using cross entropy, $\hat{s}^{i}$ is the prediction of the environmental label ${s}^{(i)}$ by using $\hat{h_G}$ , and look forward to by minimizing the cross entropy to make prediction closer to real label. Intuitively, i don't think this is helpful for learning invariant learning, because if the learned representation is the invariant feature, I don't think $\hat{h_G}$ should be able to predict the correct  ${s}^{(i)}$, since it should only be related to labels. Mathematically speaking, the authors claim in Proposition 7 in the Appendix that minimizing $L_{inv}$ is equivalent to maximizing the conditional entropy $H(s^{(i)}|\hat{h_G^i})$, 
which I doubt is valid. Known $L_ {inv} $ is cross entropy, we have a $H(s^{(i)}|\hat{h_G^i})$ = $H(s^{(i)},\hat{h_G^i})$-$H(\hat{h_G^i})$ .Minimizing the cross-entropy loss ($H(s^{(i)},\hat{h_G^i})$) fails to maximize the conditional entropy.
2. LIRS requires multi-step training and involves multiple models (GSAT,SVM, etc.). Is it less efficient than existing graph-invariant learning models? 
3. What is the difference between you and the existing method (EQuAD)? Is LIRS an incremental improvement version of it?

### Soundness
2

### Presentation
3

### Contribution
2
