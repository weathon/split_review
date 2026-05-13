# SiGeo: Sub-One-Shot NAS via Information Theory and Geometry of Loss Landscape

- Decision: Reject
- Scores: 5, 3, 3, 5, 5

## Abstract
Neural Architecture Search (NAS) has become a widely used tool for automating neural network design. While one-shot NAS methods have successfully reduced computational requirements, they often require extensive training. On the other hand, zero-shot NAS utilizes training-free proxies to evaluate a candidate architecture's test performance but has two limitations: (1) inability to use the information gained as a network
improves with training and (2) unreliable performance, particularly in complex domains like RecSys, due to the multi-modal data inputs and complex architecture configurations. To synthesize the benefits of both methods, we introduce a ``sub-one-shot" paradigm that serves as a bridge between zero-shot and one-shot NAS. In sub-one-shot NAS, the supernet is trained using only a small subset of the training data, a phase we refer to as ``warm-up." Within this framework, we present SiGeo, a proxy founded on a novel theoretical framework that connects the supernet warm-up with the efficacy of the proxy. Extensive experiments have shown that SiGeo, with the benefit of warm-up, consistently outperforms state-of-the-art NAS proxies on various established NAS benchmarks. When a supernet is warmed up, it can achieve comparable performance to weight-sharing one-shot NAS methods, but with a significant reduction ($\sim 60$\%) in computational costs.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a joint use of the zero-cost and loss metrics for NAS search, aiming to reduce the computational cost of One-Shot NAS and enhance the stability of the Zero-Cost method. The authors also improve upon the shortcomings of the ZiCo metric and validate the proposed approach through experiments on multiple datasets.

### Strengths
- The research motivation is clear and well-defined.
- The application of the proposed method in the field of recommender systems is commendable, addressing practical needs.

### Weaknesses
 - The paper lacks significant innovation. The concept of Sub-One-Shot has already been mentioned in Prenas, and this paper does not bring many additional insights.
- The improvement upon the ZiCo metric seems to be inconspicuous, and the contribution appears to be limited. Moreover, the experimental results in Table.2 are very similar to those of ZiCo.
- The paper lacks a comparison with Prenas in the experimental evaluation.

### Questions
Please see the Weaknesses.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper the authors propose a zero-cost proxy for NAS that is composed by 3 terms, namely the average gradient estimate divided by the gradient standard deviation, a Fisher-Rao norm and the training loss. The first terms is the same as the ZiCo zero-cost proxy, and the 2 other terms are included as an extension that takes into consideration the training dynamics in the non-zero-cost proxy regime. The authors evaluate their method in standard image classification benchmarks, as well as some recommended systems datasets.

### Strengths
- The theoretical motivation for proposing SiGeo is valid.

- The paper is easy to read and well-written.

- The empirical results show comparable or better performance previous ZC proxies.

### Weaknesses
 - Most of the paper is providing a lot of theory that is already well known in the deep learning community. Then it is using that to add a Fisher-Rao norm and training loss to the ZiCo [1] ZC proxy. This is a marginal contribution and not novel enough in my opinion for the paper to be over the acceptance threshold.

- The improvements are also marginal compared to ZiCo based on the empirical evaluations reported in the paper.

- The authors should also consider evaluating their ZC proxy on NAS-Bench-Suite-Zero [2], that contains more diverse benchmarks than the image classification ones the authors evaluated on.

- No code available.

### Questions
- I am puzzled how valid is the theory regarding the generalization and convergence of neural networks in the case of NAS with inheritance of the one-shot model weights. Can the authors say a few more words on this?

- What is the standard deviation of multiple runs for the reported metrics in the experiments section?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes SiGeo, a new proxy to conduct neural architecture search. The main contributions include some theoretical insights, upon which the proxy is designed. Numerical experiments validate the efficacy of the proposed method.

### Strengths
- The paper is written well and easy to follow.
- The way of using theorem to design proxy makes sense.

### Weaknesses
My main concerns are

- Too strong/wrong assumptions.  The foundations of their theorems, e.g., A3-A4, are rarely held for DNNs. For examples, there exists a lot operators in the search space that results in non-differentiability. Specifically, ReLU activations, max-pooling, and argmax operations are not differentiable everywhere, violating the assumption of differentiability in A3. Meanwhile, the Hessian matrix being positive-definitive implies the objective function as convex at least while is non-convex for Deep learning. This assumption, A4, is particularly problematic as it restricts the analysis to a local region around a minimum, which is not representative of the overall loss landscape. In addition for A2, the authors used $\ell_1$-norm to bound point in a ball, which is wrong since the domain is not a ball at all under $\ell_1$ norm.

- Wording is a bit big. The paper is titled as information theory, yet I did not find a specific area that actually leverages it significantly, except the usage of Fisher information matrix, while is commonly used as an alternative to Hessian matrix in other literatures.

- Theorem is not necessary for the proxy designs. I would expect that the theorem could indeed provide some novel insights to design some unique and innovative proxy. However, the present proxy seems quite standard for me that researchers should be able to design it out without deriving theorem under strong assumptions beforehand. The use of the Fisher information matrix and its trace as a proxy is not particularly novel, and the theoretical justification does not seem to lead to any unique or non-obvious design choices. The theorems, while mathematically correct under the stated assumptions, do not provide a compelling reason for the specific proxy used.

### Questions
See the weakness.

### Soundness
1 poor

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes to employ sub-one-shot NAS to trade off the zero-shot  and one-shot NAS. Furthermore, this paper designs a novel proxy called SiGeo, which is based on the information	 and geometry of the loss landscape. SiGeo can achieve better performance	on CV tasks compared with zero-shot NAS and on the RecSys domain with less computational costs compared with one-shot NAS.

### Strengths
1. This paper provides the theoretical analysis of SiGeo by jointly considering the minimum achievable training loss and generalization error. 
2. The sub-one-shot NAS framework can be better than zero-shot NAS, and can also consume	 less search cost than one-shot NAS.

### Weaknesses
1. The proxy is mainly borrowed from ZiCo, so the novelty is not enough.
2. The experimental results show no significant gain, especially compared with ZiCo on CV tasks.

### Questions
1. The theoretical verification in Figure 2 is mainly conducted on a two-layer MLP-ReLU network, so whether this theory applicable to more complex networks? For example, for the architectures in NAS-Bench-201, what about the ranking consistency when warming up with 0%, 10%, and 40% data?
2. The experiments on the CV task only consider the zero-shot settings. What about the performance when involving SiGeo proxy under the sub-one-shot NAS framework?
3. Similarly, in the RecSys experiments of Figure 3, the zero-shot NAS with SiGeo should also be compared.
4. Can the SiGeo proxy search for more complex networks on ImageNet, such as in the MobiletNet search space or the Transformer search space?
5. Since when $\lambda_2$ and $\lambda_3$ in Formula (7) are set to zero, SiGeo is simplified to ZiCo. Can other existing zero-shot proxies also improve performance by adding the two items?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces the sub-one-shot paradigm that connects zero-shot and one-shot NAS through information theory and the geometry of loss landscapes. It proposes a proxy metric called SiGeo and a theoretical framework that connects the supernet warm-up with the efficacy of zero-cost proxy. Experimental results show that SiGeo exhibits good consistency on NAS benchmarks and performs comparably to one-shot NAS in recommendation systems.

### Strengths
1. SiGeo can connect the performance evaluation of zero-shot and one-shot NAS.
2. The paper provides theoretical analysis from the perspectives of convergence and generalization.
3. The authors provide theoretical empirical justification and experimental validation in the field of recommendation systems.

### Weaknesses
1. One concern is the novelty of the paper. SiGeo feels like a combination proxy of ZiCO, FR norm, and loss functions. The integration of these components, while potentially useful, lacks a clear demonstration of unique properties or advantages beyond what could be achieved by combining existing methods. Specifically, the paper doesn't sufficiently articulate how SiGeo's specific combination of gradient mean, variance, and Fisher-Rao norm provides a fundamentally new perspective on the loss landscape compared to using these components in isolation or in other combinations.

2. SiGen is Sub-One-Shot, but the authors did not use the warm-up to analyze the correlation and search accuracy in the main experiments, including NAS Benchmarks and CIFAR-10/CIFAR-100. As the authors mentioned, SiGen is equivalent to a simplified ZiCO without warm-up, so the performance improvement in Tables 2 and 3 is also marginal. The lack of a thorough investigation into the impact of the warm-up period on the proxy's effectiveness is a significant oversight. The paper should have included experiments that systematically vary the warm-up duration and analyze its effect on the correlation between SiGeo scores and actual network performance. Without this analysis, the claim that SiGeo leverages information acquired during the warm-up remains unsubstantiated.

3. It would have been preferable to conduct experiments on NAS-Bench-201 benchmark and ImageNet dataset. The absence of results on NAS-Bench-201, a widely used benchmark for NAS algorithms, limits the generalizability of the findings. Similarly, the lack of experiments on the ImageNet dataset, a standard benchmark for image classification, makes it difficult to assess the practical relevance of SiGeo in real-world scenarios.

### Questions
1. It seems a bit inconsistent that SiGeo utilizes both gradient mean and variance since Theorem 1 only provides gradient variance in the bound.
2. Theorem  2 only offers a lower bound analysis. It would be better to provide an upper bound analysis of $L(\hat{\theta}^*)$.
3. In section 4.2, is there a trade-off between a longer warm-up period (e.g., 60%, 80%) and consistency of SiGeo, or does a longer warm-up period consistently improve consistency?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
