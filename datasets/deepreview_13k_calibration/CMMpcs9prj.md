# Towards Faster Decentralized Stochastic Optimization with Communication Compression

- Decision: Accept
- Avg Score: 6.60
- Scores: 5, 6, 6, 8, 8

## Abstract
Communication efficiency has garnered significant attention as it is considered the main bottleneck for large-scale decentralized Machine Learning applications in distributed and federated settings. In this regime, clients are restricted to transmitting small amounts of compressed information to their neighbors over a communication graph. Numerous endeavors have been made to address this challenging problem by developing algorithms with compressed communication for decentralized non-convex optimization problems. Despite considerable efforts, current theoretical understandings of the problem are still very limited, and existing algorithms all suffer from various limitations. In particular, these algorithms typically rely on strong, and often infeasible assumptions such as bounded data heterogeneity or require large batch access while failing to achieve linear speedup with the number of clients. In this paper, we introduce \algname{MoTEF}, a novel approach that integrates communication compression with {\bf Mo}mentum {\bf T}racking and {\bf E}rror {\bf F}eedback. \algname{MoTEF} is the first algorithm to achieve an asymptotic rate matching that of distributed \algname{SGD} under arbitrary data heterogeneity, hence resolving a long-standing theoretical obstacle in decentralized optimization with compressed communication. We provide numerical experiments to validate our theoretical findings and confirm the practical superiority of \algname{MoTEF}.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a novel approach MoTEF to achieve an asymptotic rate matching that of distributed SGD under arbitrary data heterogeneity by adding momentum tracking and error feedback technique, solving a theoretical obstacle in decentralized optimization with compression. This paper conducts numerical experiments to illustrate the effectiveness of MoTEF.

### Strengths
1. MoTEF achieves the convergence rate matching distributed SGD without strong assumptions, such as bounded gradient or global heterogeneity bound. It is an important improvement in distributed optimization with compression.
2. MoTEF supports arbitrary contractive compressors (variance-bounded estimate) without unbiasedness.
3. Extension MoTEF to the stochastic setting can achieve an improved rate with variance reduction.
4. This paper proposes theoretical analysis under the PL condition.

### Weaknesses
1. The comparison needs to be more clarified and detailed. Especially, the total communication complexity is important in optimization with compression. Most compression algorithms can only reduce the communication overhead of single-step iteration, but cannot reduce the total communication overhead required for convergence. It is necessary to discuss it in detail. Specifically, the analysis should consider the interplay between the compression parameter, the convergence rate, and the resulting total communication cost. A more thorough discussion of how the proposed method's communication cost scales with the problem dimension, the number of nodes, and the desired accuracy is needed. It would be beneficial to see a comparison with other compressed decentralized methods, highlighting the trade-offs in terms of communication and convergence speed.
2. Though the numerical experiments are enough to illustrate the effectiveness of MoTEF, more evidences in practical problems are necessary. For example, a lightweight training on transformers instead of only MLP. The current experiments are limited to relatively simple models and datasets. It is crucial to demonstrate the performance of MoTEF on more complex tasks, such as training deep neural networks on large-scale datasets or applying it to real-world decentralized learning scenarios. The experiments should also include a wider range of compression techniques and hyperparameter settings to fully evaluate the robustness and applicability of the proposed method.

### Questions
1. Though the proof is clear enough, I am interested in the insight of the construction of the  Lyapunov function. Adding an overview of the technique before the theoretical results is better.
2. It is a valuable study. If the author explains my concerns, I would like to improve my score.

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
This paper studies decentralized stochastic optimization with communication compression. It introduces the momentum tracking technique with error feedback, and achieves the first linear speedup convergence rate under the standard assumptions. Numerical experiments are conducted to validate the theoretical findings.

### Strengths
1. It combines momentum tracking and error feedback to attain an effective compressed decentralized algorithm.

2. It achieves the first linear speedup convergence rate for decentralized algorithms with contractive compressors.

### Weaknesses
1. The novelty seems a little bit limited. The main idea and analysis techniques seems to be a direct extension of the centralized algorithm EControl (Gao et.al., 2024) to decentralized settings. Specifically, the core algorithmic components, such as the momentum tracking and error feedback mechanisms, appear to be adapted from existing centralized methods without significant conceptual breakthroughs in their decentralized application.

2. The insight behind the proposed algorithm is not well clarified. Why does the combination of the momentum tracking and error feedback result in the linear speedup rate? It is encouraged to discuss how the algorithms are developed and highlight the insight. The paper lacks a clear explanation of how the interplay between momentum and error feedback specifically addresses the challenges of decentralized optimization with compression. The intuition behind why this particular combination leads to linear speedup, as opposed to other potential combinations, is missing.

3. The dependence on the network topology, as the authors have discussed, is much worse than decentralized algorithms without compression. This significantly limits the practical applicability of the proposed method in scenarios with sparse or poorly connected networks. The theoretical analysis highlights a strong dependence on the spectral gap of the network, which could lead to significantly slower convergence in real-world settings where ideal network connectivity is not guaranteed.

### Questions
1. Please highlight the challenges in analysis and algorithmic developments compared to the EControl algorithm (Gao et.al., 2024).

2. Please have an in-depth discussion on how the algorithm is developed. Why does the combination of the momentum tracking and error feedback result in the linear speedup rate?   

3. If there is no communication compression and error feedback, does your algoithm reduce to the pure momentum tracking algorithm? How does this momentum tracking algorithm compare with the well-known gradient tracking algorithm in convergence rate?

4. In your Theorem 1, if the network is fully connected, i.e., rho=1, how does your algorithm compare with state-of-the-art centralized compressed algorithm such as EControl, Error-feedback with momentum, and NEOLITHC?

5. The numerical studies are a little bit trivial. In your MLP task, what dataset did you use? Can you evalaute your algorithm over more realistic tasks, such as ResNet on Cifar10?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes MoTEF which achieves faster asymptotic convergence rate on decentralized optimization with communication compression, without using strong assumptions such as bounded gradient, bounded heterogeneity or unbiased compression. A variance-reduction version called MoTEF-VR is also introduced. Ablation studies show that MoTEF enjoys linear speed-up and is robust to network topology. Numerical experiments show that MoTEF performs better than Choco-SGD and BEER.

### Strengths
1. This work achieves the fastest asymptotic convergence rates with weakest assumptions.
2. The presentation is neat and clear.

### Weaknesses
1. The improvement on theoretical convergence result is not significant. Compared to CEDAS, it seems that the only improvement is removing the need for an additional unbiased compressor. To better illustrate this improvement, it is expected to validate whether using contractive compressors are more efficient than using unbiased ones. Otherwise, maybe the authors can compare the full convergence complexity (instead of the asymptotic one only) to address the theoretical improvement.
2. The numerical experiments are not persuasive enough. The compared baselines are Choco-SGD and BEER, which are in 2022 or earlier, and their convergence rate is clearly worse than SOTA as illustrated in Table 1. In contrast, CEDAS that seems closer to SOTA convergence rate is not compared. Maybe the authors can make the experimental results more solid by adding more baselines like CEDAS and DeepSqueeze. Furthermore, the experiments should compare the algorithms in terms of communicated bits, not just iterations, since the communication cost per iteration may differ significantly between algorithms.

### Questions
1. Can the authors better illustrate the advantage of MoTEF against CEDAS both theoretically and empirically? For example, in what sense using contractive compression is better than unbiased compression, and whether MoTEF can perform better than CEDAS?
2. The result for CNN seems missing. Please make sure to include both the results and the implementation details.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
Compression has become a key technique in federated learning to address the primary bottleneck of communication efficiency. This paper introduces a new algorithm, MoTEF, designed for decentralized federated learning with communication compression. The distinctive features of MoTEF include integration with model compression, moment tracking and error feedback altogether.

The authors provide a convergence analysis showing that MoTEF achieves some of the best expected results, notably without requiring heterogeneity assumptions. They discuss convergence for general non-convex functions and for functions that satisfy the PL condition (a broader condition than convexity). Additionally, they present a moment-based variance reduction variant of MoTEF.

Theoretical insights into the algorithm are explored through comparisons with existing bounds, as well as through numerical experiments.

### Strengths
It is impressive that the authors prove a convergence bound for such a complex algorithm without assuming a specific degree of data heterogeneity. Their other assumptions are also reasonable. Although the bound has a suboptimal dependence on \rho, their experiments demonstrate that the algorithm’s sensitivity to \rho can actually be much lower, offering valuable insights to the community.

The presentation is excellent, with comprehensive discussions that thoroughly compare their results to existing work.

### Weaknesses
More explanation to what Algorithm MoTEF actually does can improve the paper. From what is is written, it seems the algotihm just puts togther all the previous tricks into one place.  

One minor suggestion: while the authors say "The codes to reproduce our synthetic experiment can be accessed here", the URL is provided at the end of page 9.

### Questions
Can you elaborate which of the three trick (GT, moment, error feedback) helps remove the data heterogeneity of the paper?   

Can you simplify the bounds in (11)? In particular, there seems to be a tradeoff on \alpha among the second term, third term, fourth term. In other words, can you provide a unifying bounds that incorporates these three terms?

### Soundness
4

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
4

### Summary
The authors propose new algorithms for decentralized nonconvex optimization with heterogeneous functions, communication compression, and calls to stochastic gradients.

### Strengths
As far as I know, the state of the art as summarized in the paper and Appendix A is correctly presented. The contributions are important, as nonconvex decentralized optimization is a timely topic with a wide range of applications.

### Weaknesses
My main concern is the following. In Table 1, it is stated that convergence is established with respect to E[||nabla.f(x_out)||] for an appropriately chosen x_out, which as its name suggest should be constructed and output by the algorithm. However, the main result, Theorem 1, is established for x_out = bar{x}_t for a random t. The problem is that bar{x} is the average of the local variables x_i, which is not available! So you only prove one half of a valid convergence statement. The second half is that the method achieves a consensus, which in your case corresponds to Omega_3 converging to zero. Reasoning on bar{x} violates the conditions of decentralized optimization, where communication is assumed to be possible only through the network edges, and with compression. The convergence analysis should demonstrate that the algorithm's output, which is a set of local variables, achieves a small gradient norm and that these local variables are close to each other, meaning that consensus is achieved. The current analysis only shows the first part for an unaccessible average.

Is x_out = bar{x}_t used in the experiments? In that case this is clearly unfair to the other methods which do not use this unaccessible oracle.

Minor comments on the state of the art:
* The paper about LEAD by Liu et al. "Linear convergent decentralized optimization with compression" has been published at ICLR 2021.
* The title "Randcom: Random communication skipping method for decentralized stochastic optimization" of the paper arXiv:2310.07983 has changed

### Questions
Does it follow from Lemma 1 that in the conditions of Theorem 1, Phi^{t+1} <= Phi^t? This would imply that all quantities in (8) remain bounded (ideally, they would be proved to tend to zero).

### Soundness
3

### Presentation
3

### Contribution
3
