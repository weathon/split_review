# MambaTS: Improved Selective State Space Models for Long-term Time Series Forecasting

- Decision: Reject
- Avg Score: 5.60
- Scores: 5, 6, 3, 8, 6

## Abstract
In recent years, Transformers have become the de-facto architecture for long-term sequence forecasting (LTSF), but faces challenges such as quadratic complexity and permutation invariant bias. A recent model, Mamba, based on selective state space models (SSMs), has emerged as a competitive alternative to Transformer, offering comparable performance with higher throughput and linear complexity related to sequence length. In this study, we analyze the limitations of current Mamba in LTSF and propose four targeted improvements, leading to MambaTS. We first introduce variable scan along time to arrange the historical information of all the variables together. We suggest that causal convolution in Mamba is not necessary for LTSF and propose the Temporal Mamba Block (TMB). We further incorporate a dropout mechanism for selective parameters of TMB to mitigate model overfitting. Moreover, we tackle the issue of variable scan order sensitivity by introducing variable permutation training. We further propose variable-aware scan along time to dynamically discover variable relationships during training and decode the optimal variable scan order by solving the shortest path visiting all nodes problem during inference. Extensive experiments conducted on eight public datasets demonstrate that MambaTS achieves new state-of-the-art performance.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper introduce MambaTS, a new time series forecasting model based on selective state space models. In order to tackle multivariate forecasting, the timeseries patches of each variable is unrolled in a certain order to form a single sequence. One key innovation of the paper is a method for estimating the causal relationship between variables during training via random walk without return.

### Strengths
The paper propose a strategy to apply Mamba to to multivariate ts forecasting and achieves empirical result comparable to SOTA.

### Weaknesses
1. The proof in Proposition 2 does not make sense to me. I am not sure the whole concept of random walk on a casual graph with certain cost is well defined in the paper.
2. The proposed method claims to leverage the causal dependency between the variables and thus is more suitable in the multivariate setting. However, it does not seems to have a large advantage over chanel independent PatchTST, which is univariate forecasting method.

### Questions
I don't see why a random permutation is equivalent to a random walk. Line 324 says "K − 1 transition tuples ${(v_1, v_2),(v_2, v_3), · · ·(v_{K−1}, v_K)}$ are derived". I wonder what prevent the authors from deriving K(K-1)/2 tuples, so that each $(v_i, v_j), i<j$ is included?

### Soundness
2

### Presentation
2

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
This paper introduces MambaTS, an architecture for long-term time series forecasting that models global dependencies efficiently with a linear scan, avoiding the computational challenges of self-attention. The Variable-Aware Scan along Time (VAST) mechanism dynamically infers causal relationships among variables using random walks and determines an optimal scanning order through heuristic path decoding. This design achieves scalability and adaptability, particularly for complex, high-dimensional datasets with unknown causal structures.

### Strengths
- MambaTS reduces computational complexity from quadratic O(K^2) to linear O(K) by leveraging a topologically ordered linear scan, making it suitable for high-dimensional time series data.
- VAST enhances adaptability by inferring causal relationships in the absence of explicit causal graphs, using random walks to approximate dependencies and mitigate the need for exhaustive pairwise calculations.

### Weaknesses
Reliance on heuristic optimization for scanning order yields sub-optimality:
- The variable-aware san along time (VAST) employs the asymmetric traveling salesman problem (ATSP) to determine the optimal scanning order, relying on heuristics like simulated annealing to address its NP-hard nature. Although heuristics provide feasible solutions, this dependency introduces inconsistency, as different approximations may affect the accuracy of variable ordering (in case of complex, dense inter-variable connections)
- Extra experiments on alternative heuristic approaches such as genetic algorithms (that are powerful in navigating NP-hard problems) could reveal a more stable and efficient approach. In the same vein, additional experiments measure how different heuristic methods affect the resulting scanning order and, subsequently, forecasting accuracy. This can help users determine if any heuristic consistently produces a favorable scanning order.

Convergence guarantee or confidence interval is not covered in causal estimation which lacks usability:
- Proposition 2 lacks formal guarantees for convergence speed, raising questions about the robustness of causality inference in finite settings. Without clear bounds on the number of walks required, the approach may yield only approximate estimates, especially when practical constraints limit the number of walks. This limitation affects the consistency and reproducibility of causal estimation results, as reliance on empirical averaging may not ensure reliable causal inference across varied dataset structures. 
- It might be helpful to introduce a stopping rule based on convergence metrics (e.g. average change in transition costs), or introduce confidence intervals on causality estimates to users to give insight into the stability of causal inferences under finite computational budgets, where both suggestions seem to be beyond the scope of this study. I hope the authors consider usability in the future works.

### Questions
The paper offers a well-reasoned and innovative approach to time series forecasting, with theoretically sound propositions and a practical methodology that balances computational efficiency with modeling accuracy. While the heuristic reliance on VAST and scalability issues in dense graphs present limitations, the model’s strengths in efficiency, adaptability, and architectural design make it a valuable contribution. MambaTS is especially promising for high-dimensional and complex time series data, though further work is recommended to address heuristic dependency and enhance robustness in varied causal structures. Overall, it's a solid and innovative work on time-series forecasting, effectively incorporating causality in a computationally efficient and scalable manner.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes MambaTS, a selective state-space model for long-term time series forecasting (LTSF) that addresses the computational limitations of Transformers by leveraging causal relationships across variables and time with a single linear scan.

### Strengths
1. LTSF presents a compelling and complex challenge.
2. The experiments are thorough but still lack some essential details.

### Weaknesses
1. **Lack of Experimental Details:** Important implementation details are missing, such as patch length, the value of beta in Equation 7, and whether the random walk on variables is conducted K-1 times per epoch (meaning  k-1 more training time cost than one epoch).
2. **Efficiency Concerns:** Theoretical complexity analysis in Table 5 lacks practical runtime comparisons. Given that MambaTS requires K-1 iterations to estimate causal relationships, its efficiency is questionable.
3. **Incomplete Ablation Studies:** The paper introduces the TMB (with dropout replacing the original convolution), but no ablation study compares TMB and the original Mamba block, leaving its impact on performance unclear.
4. **Limited Explanation in Variable-Aware Scanning:** Section 5.2 does not clearly explain whether K-1 transitions are sufficient to estimate all variable orders, or if consistency (e.g., v1 always preceding vk) is assumed.
5. **Limited Benchmarking:** Two commonly used datasets (ETTh1, ETTm1) are missing, which reduces the generalizability of the results.
6. **Code Availability:** No code is provided, limiting reproducibility.
7. **Unpersuasive SOTA Claims:** Results in Table 2 are questionable. For example, our reimplementation of PatchTST (using official configurations) achieved better results than the reported MambaTS performance on ETTm2 (input length 720). Specifically:
   - ETTm2_720_96.log: 0.1632, 0.2555
   - ETTm2_720_192.log: 0.2167, 0.2942
   - ETTm2_720_336.log: 0.2679, 0.3282
   - ETTm2_720_720.log: 0.3521, 0.3798

   These results suggest MambaTS may not definitively outperform all baselines, especially as no code is available for direct comparison.
8. **Notation Issue:** The meaning of \( I \) in Equation 7 is unclear.
9. **Inference Process Detail:** Section 5.2 lacks details on the inference process for Variable-Aware Scan Along Time.

### Questions
1. How is the patch length chosen, and does it vary across datasets?
2. Could the authors clarify the random walk process and the number of epochs used in variable scanning?
3. Why were benchmarks ETTh1 and ETTm1 not included?

### Soundness
1

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
3

### Summary
The paper introduces MambaTS, an improved selective state space model for long-term time series forecasting. The model leverages a novel method for variable-aware scanning along time (VAST) to model global dependencies in a time series with variable missing rates and different intervals. By utilizing a combination of causal graphs and shortest path solutions, MambaTS addresses the limitations of previous Transformer-based models which often struggle with high computational costs and inefficient handling of long-range dependencies.

### Strengths
1. The introduction of VAST and the use of causal graphs for modeling dependencies offers a unique solution to efficiently process long-term dependencies in time series data with linear complexity.
2. The model is tested across various public datasets, demonstrating superior performance compared to existing state-of-the-art models. This not only validates the efficacy of MambaTS but also showcases its versatility in handling different types of time series data.
3. MambaTS significantly reduces the computational cost traditionally associated with long-range forecasting models like Transformers by avoiding the quadratic complexity of the self-attention mechanism.

### Weaknesses
1. The effectiveness of the model heavily depends on the accuracy of the causal graphs. Incorrect or incomplete causal relationships can lead to suboptimal forecasting results, which the paper does not extensively address in terms of robustness against poor graph structure
2. While the model shows high efficiency and effectiveness, the paper lacks a thorough discussion on scalability, especially in scenarios with exceedingly large datasets or highly complex variable relationships.
3. There is a need for a comparison of the model’s performance with other SOTA methods, such as Onefitsall, TimeLLM etc.

### Questions
See weakness.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents MambaTS, an LTSF model addressing Transformers' self-attention complexity and bias by using causal relationships for global dependency modeling. The author designs variable-aware scan along time to get variable causal relationships and also Temporal Mamba Block to avoid causal convolution. The experimental results show that MambaTS outperforms several state-of-the-art models.

### Strengths
1. It is interesting to see another new work on mamba for time series forecasting. In my view, some properties of mamba are fit for time series and it's an interesting direction to explore more. 
2. The authors propose several designs to tailor mamba for time series application, which has its merits.

### Weaknesses
1. The clarity of the paper needs to be improved. In some parts, I cannot fully understand, such as the cost of a random walk without return. Specifically, the paper does not clearly define how the cost is calculated from the training loss and distributed across transitions. It's unclear how this cost is used to update the matrix P, and how the initial matrix P is set up. Also what is the cost from node i to node j, and how we can get this in the first iteration
2. Some claims have no support/evidence. For example, the authors mention that the random walk without return is a promising approach to estimate causal links. I would like to know the reason, e.g., any citations/proofs. The paper lacks a clear explanation of why a random walk without return is suitable for estimating causal links, and it does not provide any theoretical or empirical justification for this claim. It's not clear how this approach can capture the directionality of causal relationships.
3. The experiments seem not comprehensive. The authors only compare MambaTS with 7 baselines. There are a few more after iTransformer, which are worth to be compared. E.g., ModernTCN [1], UniTST [2], TSLANet [3]. The paper should include a more comprehensive comparison with recent state-of-the-art models to properly benchmark the performance of MambaTS. The current set of baselines is not sufficient to demonstrate the superiority of the proposed method.

### Questions
1. In proposition 1, the assumption is that the causal graph exists. What if it doesn't exist? And is there any support on the random walk without return is a promising approach to estimate causal links? 
2. What is the definition of cost C and how we can get/set it empirically (e.g., the cost from node i to node j)?
3. Proposition 2 indicates that theoretically the causal relationships can be estimated without infinite random walks with return. I would like to ask how many walks are required empirically. And also the time spent? 
4. In Eq (6), how we can get the p^{(0)}? 
5. In my view, another major difference between MambaTS and iTransformer is that MambaTS model the dependencies on both time and variables, while iTransformer mainly on variables. I would like to know how this contributes to eventual performance. Because UniTST [1] is also modeling the dependencies on both time and variables dimensions, but with Transformer architecture. How does MambaTS compare with UniTST? 

Reference:

[1] UniTST: Effectively Modeling Inter-Series and Intra-Series Dependencies for Multivariate Time Series Forecasting.

### Soundness
2

### Presentation
1

### Contribution
2
