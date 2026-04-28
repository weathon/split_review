# Generalizing to any diverse distribution: uniformity, gentle finetuning & rebalancing

- Decision: Reject
- Avg Score: 4.50
- Scores: 5, 5, 3, 5

## Abstract
As training datasets grow larger, we aspire to develop models that generalize well to any diverse test distribution, even if the latter deviates significantly from the training data.
    Various approaches like domain adaptation, domain generalization, and robust optimization attempt to address the out-of-distribution challenge by posing assumptions about the relation between training and test distribution. Differently, we adopt a more conservative perspective by accounting for the worst-case error across all sufficiently diverse test distributions within a known domain. Our first finding is that training on a uniform distribution over this domain is optimal. We also interrogate practical remedies when uniform samples are unavailable by considering methods for mitigating non-uniformity through finetuning and rebalancing. Our theory provides a mathematical grounding for previous observations on the role of entropy and rebalancing for \ood generalization and foundation model training. We also provide new empirical evidence across tasks involving \ood shifts which illustrate the broad applicability of our perspective.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper proposes the distributionally diverse risk to address the out-of-distribution generalization problem. The DD risk takes the similar formulation as the DRO risk with the uncertainty set captured by entropy. Based on the DD risk, the authors demonstrate the optimality of the uniform distribution. Experimental results validate the effectiveness of the proposed reweighting/rebalancing methods.

### Strengths
- The authors propose the distributionally diverse risk and derive risk bounds for the DD risk.
- The authors demonstrate the optimality of the uniform distribution under their uncertainty set characterized by the entropy.
- Various experimental results are given to support their methods.

### Weaknesses
Given the theoretical and experimental results, my major concerns include:
- Relationship with Distributionally Robust Optimization: The proposed DD risk has similar formulation as the DRO risk, and the only difference is that the authors use entropy to capture the difference between distributions. In DRO literature, there are works using $f$-divergence, Wasserstein distance, MMD distance, etc. For different distance metrics used in DRO, there are also works to derive the risk bounds (for example, see [1,2]). What is the advantage of this specific kind of distance metric? Why can it lead to better generalization performance compared with others? I would suggest the authors providing a more comprehensive illustration on this. Specifically, how does the choice of entropy as a divergence measure impact the resulting optimization problem and the generalization guarantees compared to other divergence measures? What are the specific scenarios where entropy might be a more appropriate choice than, say, Wasserstein distance, and vice versa? A more detailed discussion of these trade-offs is needed.
- As the authors demonstrate, the optimality depends on the "entropy" selected for the uncertainty set. And the result is more like: the uniform distribution is optimal if we consider this specific kind of DRO risk (or the DD risk). Can the authors demonstrate why this specific formulation is better? The paper presents the uniform distribution as optimal under the specific constraint of entropy-based uncertainty. However, it is not clear why this particular constraint is inherently superior or more relevant for real-world OOD generalization than other possible constraints. A more thorough justification is needed to show why this specific formulation leads to better generalization in practice, beyond the theoretical result that the uniform distribution is optimal under this specific constraint. What are the practical implications of this choice, and how does it compare to other possible formulations?
- As for the experiments on real-world datasets, can the authors demonstrate in detail how the density estimator is learned? (I read the appendix but found it is not so clear.) Are the embeddings coming from a pre-trained ResNet-50? How is the effect of the density estimator on other datasets? I think the density estimation itself may be as hard as the original prediction task. How can the authors guarantee that the learned estimator is good? And when it is bad, will it even hurt the model performance? The paper lacks a detailed analysis of the density estimator's performance. It is crucial to understand how the quality of the density estimation impacts the overall performance of the proposed method. The authors should provide metrics to evaluate the density estimator's accuracy and discuss how errors in density estimation might propagate to the final results. Furthermore, it is important to investigate the sensitivity of the method to the quality of the density estimator. How does the method perform when the density estimator is not well-trained, and what are the failure modes?
- What if there are noisy data? In the DRO literature, there is a phenomenon named "over-pessimism", i.e. the worst-case risk may be too unrealistic and thus hurt the model learning. I do think it will hold in the formulation proposed in this work. For example, when doing reweighting or rebalancing, what if some noisy data or outliers are given a much higher sample weight?

### Questions
Please refer to the weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper aims to address the challenge of out-of-distribution (o.o.d.) generalization in machine learning by proposing a framework centered around the concept of distributionally diverse (DD) risk, which aims to minimize the worst-case error across all sufficiently diverse test distributions within a known domain. The paper presents theoretical findings and practical remedies for training models that generalize well under any diverse test distribution. Key contributions include proving the optimality of training on a uniform distribution, analyzing the impact of non-uniformity through finetuning and rebalancing, and providing empirical evidence supporting the theory across various tasks involving distribution shifts.

### Strengths
1. The paper introduces a fresh perspective on OOD generalization by focusing on the DD risk, which is a significant departure from traditional domain adaptation and generalization approaches.

2. The theoretical analysis provides mathematical grounding for the optimality of training on uniform distribution and the impact of non-uniformity on generalization.

3. The paper offers practical solutions such as gentle finetuning and rebalancing to mitigate the effects of non-uniformity when uniform samples are unavailable, which are valuable for real-world applications.

4. With the development of basic models and large-scale models, it becomes increasingly important to maintain robustness when the distribution of training and test data is very different. The emphasis on uniform training in this paper provides new ideas for large model training. At the same time, fine-tuning and rebalancing strategies also have application potential in the actual training of basic models, providing an important reference for future basic model design and training optimization.

### Weaknesses
1. Given the problem formulation in this paper, the solution seems rather straightforward. The stated objective is to control "the worst-case error across all distributions with sufficiently high entropy." The approach borrows from TTA by adjusting the training distribution to control Distributional Discrepancy (DD). However, the paper does not adequately justify why DD is a truly reasonable metric and what practical physical interpretations it has in real-world applications. The connection between maximizing entropy and minimizing worst-case error is not clearly established, and it's unclear why this specific notion of distributional diversity is superior to other metrics used in domain generalization or robust optimization, such as those based on Wasserstein distance or f-divergences. The paper needs to provide a more compelling argument for why DD is the right objective to pursue for OOD generalization, especially given the existence of other well-established approaches.
2. The practical effectiveness of the proposed method is questionable. For example, in Tables 2 and 3, rebalancing does not show a significant improvement over ERM. The final performance gains seem to stem from various tricks (e.g., UMAP, label conditioning, etc.), which are inconsistently applied across different experiments. This suggests to me that the results might be due to data tuning rather than a genuinely effective method applicable to diverse scenarios. The inconsistent application of these techniques across datasets makes it difficult to isolate the impact of the core rebalancing strategy. Furthermore, the paper does not provide a clear ablation study to demonstrate the individual contribution of each of these tricks.
3. The quantitative analysis of different strategies is not in-depth enough. For example, there is no detailed data to support the applicability and effect of the rebalancing strategy under different types of distribution shifts. In addition, there is a lack of systematic analysis of the sensitivity of fine-tuning parameters (such as fine-tuning step size, number of iterations, etc.) and their effects. The paper should include a more comprehensive analysis of how the rebalancing strategy performs under different types of covariate shifts, and how sensitive the method is to the choice of hyperparameters. Without this, it is difficult to assess the robustness and reliability of the proposed approach.
4. The paper's presentation could benefit from several improvements. For instance, Table 2 references "UMAP" and Figure 3 mentions "WDL2" without providing explanations in the corresponding captions or within the main text. This lack of clarification might hinder reader comprehension.

### Questions
Please see weaknesses.

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
This paper addresses risk minimization conditioned on covariates, i.e., worst-case risk as named in the paper, by introducing the learning objective of distributionally diverse risk that considers the worst-case risk over high-entropy distributions. The paper proceeds to consider reweighted risk on uniform distribution as a surrogate for the distributionally diverse risk, which leads to the classic importance weighting technique. Experiments are conducted on datasets with prevalent covariate shift.

### Strengths
This paper follows a clear and logical organization:
1. Worst-case risk should be considered for prediction under covariate shift.
2. The distribution diverse risk is a good surrogate for the worst-case risk.
3. The risk on uniform distribution is a good surrogate for the distribution diverse risk.

The first point is an important objective and recognized challenge for covariate shift generalization. The paper has also well addressed the third point by (1) showing reweighting data towards a uniform distribution yields the lowest distribution diverse risk within the framework of reweighted empirical risk minimization (Theorem 3.1), and (2) studying the generalization gap between distribution diverse risk and uniform distribution risk at both population and sample levels (Theorems 3.2 and 4.3).

The paper also does a good work in explicitly acknowledging possible limitations, which improves overall clarity. For example, the author notes that Theorem 3.1 is less applicable to the setting of supervised domain adaptation, which is just fine because learning under uncertainty of target distribution is actually more challenging. But the statement helps accurately contextualize the results in the literature.

### Weaknesses
I am not convinced by the paper that the distribution diverse risk is a good surrogate for the worst-case risk. The introduction has a short explanation that high-entropy test distributions as considered by the distribution diverse risk reflect natural distribution shifts, and high-entropy training and test distribution empirically yield good generalization in literature, which will benefit from more detailed elaboration. In the current submission, I find the argument is not supported, or even contradicted by the theory.

The distribution diverse risk (DD) converges to the worst-case risk until $\gamma \to \infty$ (eq 4), when DD risk reduces to the worst-case over **all** possible distributions X. This asymptotic behavior is satisfied by a large family of "uncertainty sets" of test distributions, e.g., when the radius of the uncertainty set of Distributionally Robust Optimization (DRO) tends to infinity, or when we redefine DD as distributions with a differential entropy near any real value by a gap $\gamma$. This asymptotic argument does not address why  DD is superior to the alternative designs of uncertainty sets, in terms of a surrogate for the worst-case risk, which is pivotal for the position of this paper in the broad literature of OOD generalization under covariate shift, e.g., DRO [1].

It is also revealed in Theorem 3.2 that the DD risk scales with $\Omega(\gamma)$ as $\gamma \to \infty$, indicating that the DD risk cannot be estimated by uniform distribution risk at all when we actually consider the objective of worst-case risk. The author also acknowledges that the theorem only applies to $\gamma = O(1)$, contradicting the setup for the worst-case risk. Therefore, I interpret from the paper that the DD risk is another heuristic design of the uncertainty set of target distribution, as similar in DRO. However, a stronger theoretical or empirical reasoning for this design is expected in order to consolidate this paper.

Minor points:

1. Implications for LLM and foundation models (L61-69) in the introduction can be over-claimed since they are not supported by theory and the LLM-free experiments. Moreover, importance weighting in general is ineffective for over-parameterized models [2]. The intuition is that over-parameterized models interpolate the samples with an almost zero loss on each sample, corresponding to $\epsilon = 0$ in Theorem 3.1. In this case, the sample risk does not uniformly bound the population risk because there are infinitely many interpolators on training data among which most are not generalizable. In this case, considering the maximum risk of predictors does not make sense. As is also stated by the author, Theorem 3.1 does not consider the inductive bias of optimizers, but generalization for over-parameterized models are only possible when implicit regularization is imposed by the learner. 

2. 0-1 loss and the existence of a ground truth model $f^\star(x)$ is assumed throughout the theory. Combined together, they imply an impractically strong assumption that the classification task is noiseless, i.e. $f^\star(x)$ is binary rather than a probability, which is not even satisfied by the simple classic model of mixture of gaussians, which also appears as the first experiment.

3. Section 4.1 and 4.2 are less relevant to the sample-level analysis of the generalization behavior of DD risk. This is because the author characterizes the risk gap by the l1 distance between the empirical measure and the population measure. However, this distance $\delta(u,p)$ always equals 2 for any continuous measures u and discrete measures p, which makes eq. 8 ineffective when p is an empirical measure, the sum of n dirac measures. This happens to Theorem 4.1 as well. In fact, a standard PAC-Bayes bound will characterize the risk gap as the ratio between some divergence measure and a power of n. The absence of sample numbers in eq.8 and Theorem 4.1 cannot reflect the non-asymptotic behavior as $n \to \infty$.

4. ColoredMNIST is a dataset that contains large concept shift instead of covariate shift as claimed by the paper. This synthetic dataset flips the label of digits (y) with a probability that is correlated with the color (part of x, denoted by $x_2$). This correlation varies across splits, leading to concept shift ($y|x_2$ shift). If we denote the shape of the digits as $x_1$, the dataset features $y \not \perp x_2 | x_1$. This causes $y|x$ shift.

5. An exhaustive investigation of baselines is performed for ColoredMNIST. Reporting their results for iWildCam and PovertyMap can be more convincing. For example, the public benchmark of PovertyMap shows that the SOTA C-Mixup, some simple variant of Mixup in Table 3, is surprisingly effective (0.53 v.s. 0.47 as the best result in the paper).

### Questions
1. In theorem 3.2, what is the choice of $\alpha$ that minimizes the upper bound?

### Soundness
2

### Presentation
4

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a new learning framework for studying the out-of-distribution generalization. They construct the uncertainty set by using the entropy of the data distribution. They define the worst-case risk in this uncertainty set by Distributionally diverse (DD) risk. They build a series of theorems containing: A classifier optimized for the uniform distribution will yield the smallest DD risk; the generalization bound of DD risk under the zero-one loss. They further provide two ways to improve the generalization ability, fine-tuning with penalty and rebalance through weighting. They verify the effectiveness of the proposed method on IwildCam, PovertyMAp, and ColorMNIST datasets.

### Strengths
The proposed theoretical framework is novel. The paper is well written.

### Weaknesses
The experimental results are not solid enough to make a conclusion. Although rebalancing (UMAP-8, label cond., WDL2) achieves good performance in "-90%" and therefore performs well in average score, it remains unclear whether weight distance to initialization is practically effective, as no results for this metric are provided on other datasets in Tables 1 and 2. Furthermore, Tables 1 and 2 exclude many relevant baseline methods—such as ARM, which performs well on ColoredMNIST, as well as VREx, RSC, and others.

Additionally, there is no universal criterion for determining which method is best suited to practical application. The authors apply different modeling approaches (e.g., WDL2 for ColorMNIST and UMAP for PovertyMap) depending on the dataset, yet provide no general guidance on how to select methods for other contexts.

### Questions
Is uniform distribution best in real applications? I believe image data are located in the low dimensional manifold. Why does this uniform distribution help generalization?

### Soundness
2

### Presentation
2

### Contribution
2
