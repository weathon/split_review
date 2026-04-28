# Compressed Decentralized Learning with Error-Feedback under Data Heterogeneity

- Decision: Reject
- Avg Score: 1.67
- Scores: 3, 1, 1

## Abstract
Decentralized learning distributes the training process across multiple nodes, enabling collaborative model training without relying on a central server. Each node performs local training using its own data, with model updates exchanged directly between connected nodes within a given network topology. Various algorithms have been developed within this decentralized learning framework and have been proven to converge under specific assumptions. However, two key challenges remain: 1) ensuring robust performance with both a high degree of gradient compression and data heterogeneity, and 2) providing a general convergence upper bound under commonly used assumptions. To address these challenges, we propose the *Discounted Error-Feedback Decentralized Parallel Stochastic Gradient Descent (DEFD-PSGD)* algorithm, which efficiently manages both high levels of gradient compression and data heterogeneity, without sacrificing communication efficiency. The core idea is to introduce controllable residual error feedback that effectively balances the impact of gradient compression and data heterogeneity. Additionally, we develop novel proof techniques to derive a convergence upper bound under relaxed assumptions. Finally, we present experimental results demonstrating that DEFD-PSGD outperforms other state-of-the-art decentralized learning algorithms, particularly in scenarios involving high compression and significant data heterogeneity.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes compressed decentralized algorithm with the aim to control the error due to data heterogeneity. The proposed algorithm DEFD-PSGD applies compressed model updates and therefore is able to perform exact model gossip under compressed communication.

### Strengths
DEFD-PSGD is a novel algorithm in the sense that it synchronizes model parameters by applying compressed model updates, unlike prior works [Koloskova et. al., 2019] which consider applying compressed model gossip.

### Weaknesses
- The convergence guarantee only holds for a restricted range of $\beta$, where $\beta$ is the relative error of contractive compressor. This is non-standard, especially along the line of work of [Koloskova et. al., 2019], [1], [2], [3] from additional references below. The authors need to provide a more thorough justification for this restriction, as it limits the applicability of the proposed algorithm. It is unclear why the analysis cannot be extended to the full range of $\beta \in (0, 1)$, potentially by introducing a dependence on the parameter $\gamma$ or other relevant parameters. The current restriction on $\beta$ significantly weakens the theoretical contribution compared to existing methods. 
- Under the context of nonconvex optimization, [3] is a more accurate reference than [Koloskova et. al., 2019] for mentioning CHOCO-SGD because [3] provided the convergence of CHOCO-SGD on nonconvex objective while [Koloskova et. al., 2019] only considered convex objective.

(**Notations**)
- In equations (2), (6), (10), $\nabla f(\frac{X_t {\bf 1}_n}{n})$ should be $\|\nabla f(\frac{X_t {\bf 1}_n}{n}) \|^2$ instead.
- The constants $a,b,c,\mu$ are not defined in or before Theorem 1.
- In line 243 "neightbors" should be "neighbors".



### Questions
(**Additional References**)

Along the line of compressed decentralized algorithms for tackling data heterogeneity, I suggest the following two references that should be covered in the related works. [1] is an algorithm with large batch stochastic gradient tracking (see Theorem 4.2 of [1]) while [2] is an algorithm with constant batch stochastic gradient tracking (see Appendix B of [2]). Gradient tracking algorithms are known to converge without assuming a uniform bound on the similarity between local and global objective gradients.

(**About Comparison to CHOCO-SGD**)

The paragraph **Comparison between DEFD-PSGD and CHOCO-PSGD** is confusing and here is my point of view:

- I assume that the authors are referring CHOCO-SGD in [3] as equivalent to CHOCO-PSGD in Algorithm A.1. Otherwise, the comparison and discussion made between DEFD-PSGD and CHOCO-PSGD are not meaningful becuase DEFD-PSGD should be compared against CHOCO-SGD. However, it is not clear how to show the equivalence of Algorithm A.1 to CHOCO-SGD in [Koloskova et. al., 2019] or in [3]. So I request the authors to show a formal proof of equivalence explicitly. (A similar comparison between two error-feedback schemes is studied in [4], where Algorithm 1 in [4] has a similar error-feedback mechanism as CHOCO-SGD while Algorithm 4 in [4] has a similar error-feedback mechanism as DEFD-PSGD.)

- CHOCO-SGD is an algorithm proved to converge under any degree of data heterogeneity, for instance, their analysis in [Koloskova et. al, 2019] and [3] only assume bounded stochastic gradient and does not impose assumption on data heterogeneity. Therefore, the claim `so that when data is highly heterogeneous, the CHOCO-PSGD may diverge` in line 389 is not theoretically supported. I suggest the authors to provide more evidence for supporting the claim or revise the discussion.

- The experiment results in Figure 2 of [2] suggests that CHOCO-SGD shows slow convergence in heterogeneous distribution of MNIST. This does not match with the claim of this paper in Figure 1 which states that CHOCO-SGD cannot converge under heterogeneous data. I encourage the authors to conduct additional experiments on a similar setup of [2], to gather more insights about CHOCO-SGD and address the divergence of CHOCO-SGD with more solid evidence such as what parameter tuning is used.

- The experiment result would be more convencing if a comparison is made between DEFD-PSGD and [1], [2] on heterogeneous data setting.


(**About Data Heterogeneity**)
- Can the authors provide more insights on how DEFD-PSGD mitigates data heterogeneity through the analysis result? For instance, please explain how does the algorithm react to difference values of $\epsilon$ and whether that effectively tackles with the data heterogeneity error in terms of the convergence bound. 
- It would be more convincing if the experiment result can be presented with different levels of data heterogeneity (different Dirichlet parameter $\alpha$) in the same plot and demonstrate how different algorithms react to the error of data heterogeneity.

(**About Consensus Error**)
- I suggest the authors to include a convergence bound on the consensus error in the main text and discuss how does DEFD-PSGD benefits from using an exact synchronized model gossip communication. This will provide more insight about the advantage of DEFD-PSGD, e.g., whether the dependence on $\epsilon$ is better than other algorithms (such as Theorem 4 in [Lian et. al., 2017]) in terms of consensus error bound.

[1] Haoyu Zhao, Boyue Li, Zhize Li, Peter Richtárik, and Yuejie Chi. BEER: Fast $\mathcal{O} (1/T)$ Rate for Decentralized Nonconvex Optimization with Communication Compression, 2022.

[2] Chung-Yiu Yau, Hoi-To Wai. DoCoM: Compressed Decentralized Optimization with Near-Optimal Sample Complexity, 2022.

[3] Anastasia Koloskova, Tao Lin, Sebastian U. Stich, Martin Jaggi. Decentralized Deep Learning with Arbitrary Communication Compression. 2020.

[4] Peter Richtárik, Igor Sokolov, Ilyas Fatkhullin. EF21: A New, Simpler, Theoretically Better, and Practically Faster Error Feedback, 2021.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
This paper proposes a detentralized optimization algorithm with communication compression called DEFD-PSGD, which applies the error-feedback mechanism. Under certain assumptions, DEFD-PSGD is shown to converge exactly. In numerical experiments, DEFD-PSGD is shown to perform better than CHOCO-PSGD.

### Strengths
1. The algorithm is simple and clear.
2. The theoretical convergence rate matches D-PSGD.
3. The proposed algorithm performs better than other baselines in the experiments.

### Weaknesses
1. The compared baselines are sub-optimal. By comparing with baseline algorithms DCD-PSGD and CHOCO-PSGD, which are from 2019 and earlier, it's not proper to claim that DEFD-PSGD "outperforms other state-of-the-art decentralized learning algorithms". CEDAS in 2023 has already beaten CHOCO-PSGD by a large margin.
2. The assumptions used in the theoretical analysis are too strong. Specifically:
i) Bounded gradient divergence: The use of this assumption seems to contradict with the aim to optimize with data heterogeneity. The error-feedback mechanism is often employed to mitigate the impact of compression, not to enforce a small-heterogeneity setting. The assumption of bounded gradient divergence effectively limits the applicability of the algorithm to scenarios with similar local gradients, which is not the typical use case for decentralized learning.
ii) Unbiased stochastic compression & Bounded compression error: Assuming both unbiasedness and a bounded compression error of $\beta\le1$ is overly restrictive. Typically, compressed algorithms operate under either unbiasedness or a variance bound on the compression operator. Requiring both significantly limits the choice of compression operators and contradicts the goal of achieving a high degree of gradient compression. For example, many effective compression techniques like top-k sparsification are biased but achieve high compression ratios, and would not be covered by the current analysis.

### Questions
1. Could the reviewers illustrate how to design a compressor with a high degree of compression that satisfies both unbiasedness and a bounded compression error of $\beta\le 1$?
2. As in weakness 1, can the authors compare the proposed algorithm with more recent baselines, such as CEDAS?
3. As in weakness 2, why the assumptions seem contradict with high compression degree and large data heterogeneity? Please correct me if I'm wrong.

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 3

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
The paper investigates compressed decentralized learning in the presence of data heterogeneity, revealing limitations in existing algorithms when both gradient compression and data heterogeneity are high. To address these issues, the authors propose the DEFD-PSGD algorithm, designed to handle substantial gradient compression and data heterogeneity effectively, while maintaining communication efficiency. The authors provide theoretical analyses and validate their approach through numerical experiments.

### Strengths
This paper identifies a key challenge in the existing literature: the inability to handle both a high degree of gradient compression and significant data heterogeneity simultaneously.

### Weaknesses
Overall, this paper is not well-written and has several significant limitations, detailed as follows:

1. The proposed algorithm is impractical due to its high memory requirements. Specifically, the algorithm requires each node to store the model weights $\{x^{i,j}\}_{j \in \mathcal{N}_i}$ for all its neighbors, as seen on the left-hand side of line 4 and the right-hand side of line 7 in Algorithm 1. This poses a significant limitation. With large models reaching billions of parameters, even a single set of model weights requires substantial memory. For instance, storing one copy of a 175-billion-parameter model demands over 350GB, making the storage of neighbors' weights prohibitively memory-intensive and leading to notable hardware inefficiencies. Most existing compressed decentralized algorithms do not require each node to store neighbors' weights; see baseline algorithms like DCD-PSGD (Tang et al., 2018) and Choco-SGD (Koloskova et al., 2019). Moreover, other compressed decentralized methods, including those listed below [C1–C3], also avoid storing neighbors' weights. Thus, this requirement presents a strong limitation of the proposed algorithm.


2. While the authors claim that their convergence analysis is based on the most commonly used assumptions (see Contribution 2), this is unfortunately not the case. The authors assume that the compressors are both unbiased and contractive (i.e., $ \beta < 1 $; see the last two conditions in Assumption 1), which is rarely encountered in the literature. Typically, existing work assumes compressors are either unbiased—such as random sparsification [C4] and random quantization [C5]—or contractive, with top-$ K $ compression as an example, but do not assume them to hold simultaneously. Very few compressors satisfy both unbiasedness and contractiveness simultaneously. For instance, as shown in [C6], the random sparsification compressor [C4] is unbiased but has $ \beta = d/k - 1 $ where $ d \gg k $, and random quantization [C5] is unbiased with $ \beta > 2 $. Another common unbiased compressor, natural compression [C6], has $ \beta = 9/8 > 1 $. None of these widely used unbiased compressors meet the assumptions in this paper. Consequently, the assumptions here are restrictive and unlikely to hold in practical scenarios. This is another strong limitation. The standard assumption is to assume either unbiased or contractive compressors, but not both, see Assumption 3 and 4 in [C2].

3. The presented convergence results are weak. The convergence rate in (10) does not clarify the effects of network topology and the compression factor $\beta$. In contrast, existing literature, such as [C3], explicitly characterizes the influence of network topology and compression. Additionally, this paper appears unfamiliar with many state-of-the-art decentralized algorithms, including those listed in Table 1 of [C3]. Compared to these established algorithms, I do not observe clear advantages of the proposed approach's convergence rate. Moreover, it is important to note that the proposed algorithm relies on highly restrictive assumptions, such as simultaneous unbiasedness and contraction, along with bounded gradient dissimilarity. By comparison, [C2] and [C3] do not rely on these restrictive conditions.

4. The simulations are trivial. First of all, the tested top-K and the random quantization compressors do not satisfy the simulation unbiasedness and contraction property. Second, the baselines are trivial, more advanced baselines are in [C2, C3] as well as those listed in Table 1 of [C3]. Third, it is very strange that compressed algorithms on Cifar-10 can only achieve accuracy below 70%. The typical accuracy is above 90%.

### Questions
1. Consider revising the algorithm design to eliminate the storage requirement for neighbors’ model weights. Existing algorithms avoid this need, and its inclusion here may render the algorithm impractical.

2. Please consider removing either the unbiasedness or the contractive assumption. Existing algorithms typically do not require both.

3. The coefficient $\beta$ is generally a fixed constant determined by the choice of compressor. For example, random sparsification yields $\beta = d/k - 1$, and random quantization results in $\beta > 1$. Why, then, do you assume that $\beta$ can be as small as you want? See your assumptions on the range of $\beta$ in Theorem 1, Corollary 1, and Corollary 2.

4. In Corollary 2, please clarify how network topology and the compression factor $\beta$ influence the convergence rate. Additionally, please compare your convergence rate with that of [C2, C3] and the algorithms listed in Table 1 of [C3], and explicitly outline the advantages of your algorithm.

5. Consider constructing compressors that simultaneously satisfy both the unbiased and contractive assumptions, and use these in your simulations. Additionally, please include more baseline comparisons beyond Choco-SGD and DCD-PSGD. Finally, clarify why your CIFAR-10 simulations yield low accuracy.

### Soundness
1

### Presentation
2

### Contribution
1
