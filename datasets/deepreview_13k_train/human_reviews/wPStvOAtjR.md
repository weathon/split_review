# LAMDA: Two-Phase Multi-Fidelity HPO via Learning Promising Regions from Data

- Decision: Reject
- Scores: 5, 5, 6, 5

## Abstract
Multi-fidelity hyperparameter optimization (HPO) combines data from both high-fidelity (HF) and low-fidelity (LF) problems during the optimization process, aiding in effective sampling and preliminary screening. To enhance its performance, approaches that incorporate expert knowledge or transfer ability into the HPO algorithm have demonstrated their superiority, while such domain knowledge or abundant data from multiple similar tasks may not always be accessible. Observing that high-quality solutions in HPO exhibit some overlap between high- and low-fidelity problems, we propose a two-phase framework $\texttt{Lamda}$ to streamline the multi-fidelity HPO. Specifically, in the first phase, it searches in the LF landscape to identify the promising regions of LF problem. In the second phase, we leverage such promising regions to construct reliable priors to navigate the HPO. We showcase how the $\texttt{Lamda}$ framework can be integrated with various HPO algorithms to boost their performance, and further conduct theoretical analysis towards the integrated Bayesian optimization and bandit-based Hyperband. We demonstrate the effectiveness of our framework across $56$ HPO tasks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces Lamda, a two-phase multi-fidelity hyperparameter optimization (HPO) framework designed to improve the efficiency of HPO by leveraging low-fidelity (LF) evaluations to identify promising regions in the search space. In the first phase, Lamda conducts a search in the LF landscape to locate regions where high-quality solutions are likely to exist. This is achieved using the Tree-structured Parzen Estimator (TPE) method to model the probability density functions (PDFs) of promising and inferior solutions, with the Overlapping Coefficient (OVL) used to measure the convergence of the promising region distribution.

In the second phase, the promising regions identified from the LF evaluations are transferred to guide the search in the high-fidelity (HF) landscape. This is done by modifying the sampling distribution to focus more on these promising regions, thereby reducing the need to explore the entire search space exhaustively at HF, which is computationally expensive.

### Strengths
Efficiency: Lamda reduces the computational cost of HPO by focusing HF evaluations on promising regions identified through LF evaluations, avoiding unnecessary exploration of less promising areas.

Versatility: The framework is versatile and can be integrated with a variety of existing HPO methods.
Empirical Validation: Extensive experiments on diverse benchmarks show that Lamda outperforms baseline methods, indicating its practical effectiveness across different domains and tasks.

### Weaknesses
Lack of Significant Novelty: The approach primarily combines existing techniques in a straightforward manner. The idea of using LF evaluations to guide HF searches is not entirely new in the field of multi-fidelity HPO. Specifically, the use of TPE for modeling the search space and the concept of transferring knowledge from low to high fidelity are well-established. The paper does not introduce a fundamentally novel mechanism for this transfer or a new way to model the low-fidelity landscape, which limits its overall contribution to the field.

Dependence on Overlapping Regions: The effectiveness of Lamda hinges on the assumption that promising regions in LF and HF landscapes overlap significantly. While the paper presents results on datasets with varying degrees of overlap, the core mechanism relies on this assumption. The paper does not provide a clear analysis of how the performance degrades as the overlap decreases, nor does it offer any adaptive strategies to mitigate the impact of poor overlap. This dependence limits the applicability of the method in scenarios where the low-fidelity landscape is a poor proxy for the high-fidelity one.

### Questions
Overlap Assumption Validity:

Question: How does Lamda perform in scenarios where the promising regions of LF and HF landscapes do not significantly overlap? Have you tested the method on tasks where this assumption is invalid?

Parameter Sensitivity Analysis:

Question: Can you provide more insight into the sensitivity of Lamda's performance to its hyperparameters, such as the weight 
𝑤 w and threshold 𝛾? Are there guidelines or adaptive strategies for selecting these parameters?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This work aims to overcome the drawbacks of popular hyperparameter optimization (HPO) methods that lead to wasted computational resources, namely the exhaustive exploration of the entire search space and expensive high-fidelity (HF) evaluations. The paper proposes a two-phase multi-fidelity (MF) framework for HPO called LAMDA (Learning promising regions from data) to address these issues. The framework can be integrated into existing HPO techniques.

Based on the observation of overlapping high-performing regions between low-fidelity (LF) and HF landscapes, in the first phase, the algorithm learns promising regions from evaluations of the LF landscape. In the second phase, these learned promising regions are leveraged to more efficiently explore the HF landscape in the actual HPO process, thereby avoiding the waste of resources in less promising regions.

The paper contains an empirical evaluation of the proposed method combined with several state-of-the-art HPO methods (PriorBand, BOHB, MUMBO, BO) and random search as a baseline. On a total 36 benchmarks (tabular, surrogate and real) the paper demonstrates that the proposed method leads to substantial improvement.

Overall, I think the paper leaves more open questions than it convinces me that LAMDA is a great method that should be used in practice. While the idea is surprisingly simple, the paper does not show why previous multi-fidelity methods do not work as advertised (e.g., conduct too much exploration, or require evaluations on the highest fidelity), it is unclear how to implement the method (substantial details and the actual implementation are missing), and the experiments also lack detail and should be extended by a few recent benchmarks.

### Strengths
* The paper empirically demonstrates the effectiveness of the proposed method across various HPO tasks and HPO techniques. Additionally, the paper offers a theoretical analysis for Bayesian optimization and Hyperband.
* The proposed method can be integrated into existing HPO techniques, such as prior-based and bandit-based methods, as well as Bayesian optimization (BO).
* Although the approach introduces several hyperparameters that need to be tuned, the paper proposes specific values and demonstrates in experiments that the impact of the hyperparameters on performance is minor.

### Weaknesses
 * The work claims that it overcomes the limitations of existing multi-fidelity methods, which require exhaustive searches across the entire search space (Reference: Table 1). However, the proposed method (LAMDA) still necessitates an exhaustive search of the LF landscape, using the learned promising regions only for searches in the HF landscape. Approaches like MFBO or bandit-based methods similarly leverage LF evaluations to focus HF evaluations on promising areas. For instance, BOCA already proposes using cheap low fidelity experiments to identify promising regions for HF experiments (“Therefore, one may use cheap low fidelity experiments with small (N, T ) to discard bad hyper-parameters and deploy expensive high fidelity experiments with large (N, T ) only in a small but promising region.” [1]). 
While LAMDA may offer greater efficiency with this approach, the claim that the overall idea would be new (Reference: ”To address these challenges, we propose leveraging LF problems to identify promising regions for the HF problem.” [Row 93-94]) and that it would eliminate the need for exhaustive searches across the entire search space (Reference: Table 1) is not true.
* The paper implies to have initially observed that promising solutions in HPO tend to overlap between LF and HF evaluations. (References: “We have observed that high-quality solutions in HPO exhibit some overlapping between high- and low-fidelity problems.” [Rows: 14-15], “This strategy is inspired by our observation of overlapping promising regions between high- and low-fidelity HPO problems.” [Rows: 96-97]). However, this observation is not new at all and serves as the basis for many existing publications on MF-HPO [3 (Figure 1), 1, 2]. Also, if this is proposed as a novel, key observation, the paper should dedicate a section to describe and analyze this behavior.
* The paper leaves many open questions regarding the experimental setup (see questions below).

## Minor criticisms (putting them here as there is no field for extra comments):
* There is a typo on row 103: "quirky."
* Figure 10 is quite small and displays multiple overlapping curves, making it difficult to read clearly.
* Lines 204–205 are ambiguously phrased, suggesting that the overlapping coefficient could only be 0 or 1. This should be rephrased to clarify that it can also take intermediate values.
* The paper Swersky et al. (2013) is about multi-tasking Bayesian optimization. It contains a two-fidelity setting, but are you sure that you did not mean "Freeze-Thaw Bayesian Optimization" (Swersky et al. (2014))?

### Questions
* It is stated that the framework can be integrated with existing HPO techniques. However, especially for the multi-fidelity techniques used in the paper, such as BOHB, it is not clearly explained how LAMDA is integrated. It is very unclear how this could be done, as BOHB itself is a multi-fidelity method that can make use of low and high fidelities. The paper should be extended to contain a per-method discussion on how LAMDA is integrated to make it easier for the reader to understand this.
* Following up on the previous question, why does the proposed method outperform existing multi-fidelity methods? The existing multi-fideliy method are made to **not** explore the high fidelity in much detail (but this paper claims they do), and I think this warrants further discussion, as I do not understand why BOHB etc would not perform well on these problems. Source code of the method would increase my trust in the proposed method and its evaluation.
* Again, following up on the previous two questions: How does the proposed method compare against https://proceedings.mlr.press/v89/song19b.html ?The method by Song et al. appears to be closely related and targets the same problem.
* The experiment section (4.) does not specify the fidelity levels used in the experiments. While Appendix C (Tables 3 and 4) provides a fidelity range for some experiments, it does not clearly indicate the specific fidelity levels applied.
* Have you observed settings where the computational expenses introduced in the first phase do not outweigh the rewards in the second phase? If so, were you able to characterize those settings to indicate when the application of the proposed method is less meaningful?
* Why not use more recent benchmarks, such as the ones used in DYHPO, Quicktune, DPL? Also, since the paper mentions DPL, please make sure to cite it, as well as other BO methods you mention (e.g., TURBO). It is great that you are using 33 different benchmark tasks, but using a decision tree benchmark (rpart) to demonstrate a multi-fidelity hyperparameter optimization method at ICLR appears to be out of place.
* Have you thought about or observed failure modes in the proposed probability distribution used to guide the HPO process (Equation 6)? For instance, in complex HF landscapes with several local minima, augmenting the density learned on the fly with the density from the first phase search might shift the sampling distribution away from sufficiently good but not optimal solutions in the early phases, deteriorating anytime performance.
* What Bayesian Optimization library is used in the experiments? It would be great if you could add references to the other baselines, too (There it is less ambiguous, but for BO, it is really ambiguous what library you used). In any case, it would be important to use a state-of-the-art library, for example, HEBO.
* How much is the lower fidelity explored in practice? I think it would be important to add a figure on when the method moves from the lower to the higher fidelity.
* Why would it be sufficient to only update the PDF of promising regions? Is it because in the TPE sampler new hyperparameter settings are only sampled from the KDE describing the promising regions?
* How does the proposed overlap coefficient compare to the one proposed in https://arxiv.org/abs/2212.06751?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces LAMDA, a two-phase multi-fidelity hyperparameter optimization framework that enhances efficiency by identifying promising regions in low-fidelity landscapes and focusing high-fidelity searches within these areas. This approach reduces computational costs and can integrate with existing methods, improving their performance. While it offers flexibility and data-driven insights, it relies on accurate low-fidelity approximations and may require complex integration. Key questions include its performance with poor LF approximations and sensitivity to parameter choices.

### Strengths
1. By concentrating on promising regions, Lamda effectively reduces both the computational cost and time required for hyperparameter optimization.

2. The framework can be integrated with various existing methods, like Prior-Based, Bandit-Based and MFBO methods, enhancing their effectiveness.

3. Unlike methods that depend on expert knowledge, Lamda learns to identify promising regions from data, allowing it to adapt to diverse scenarios. This underscores its data-driven nature.

### Weaknesses
1. The performance of Lamda may hinge on the accuracy with which the low-fidelity (LF) landscape (first phase) reflects the high-fidelity (HF) landscape, owing to the two-phase search framework. Specifically, the method's reliance on identifying 'promising regions' in the LF space introduces a critical dependency. If the LF approximation is poor, the identified regions may not correspond to actual promising areas in the HF space, leading to suboptimal performance. This is particularly concerning in scenarios where the LF approximation is a simplified model or an early stopping of the HF training, which may not capture the nuances of the HF landscape.

2. Section 2.3 states that "Lamda plays as a booster." Consequently, integrating Lamda with existing multi-fidelity hyperparameter optimization methods may necessitate substantial modifications and fine-tuning. The claim that Lamda acts as a 'booster' implies a seamless integration, but the practical implementation might require significant adjustments to the sampling strategies of existing methods. This could involve modifying acquisition functions or altering the exploration-exploitation balance, which are not trivial tasks and could introduce new hyperparameters that need careful tuning.

3. The computational overhead associated with implementing the two-phase search strategy, as well as the method's sensitivity to parameters such as the overlapping coefficient and the weights utilized in the second phase of the search, have not been thoroughly addressed. While the paper claims efficiency gains, the cost of the initial LF search and the subsequent HF refinement needs to be analyzed in detail. Furthermore, the method's performance could be highly sensitive to the choice of parameters like the overlapping coefficient, which determines how much the LF search influences the HF search, and the weights used in the second phase, which control the balance between exploration and exploitation. A lack of robustness to these parameters would limit the practical applicability of the method.

### Questions
1. In line 186, from a mathematical accuracy perspective, should the definitions of $\mathcal{S}_{pro/inf}$ include the case where $f_l(x) = y^*$

2. In line 294, how does the definition $f_\mathcal{D}^*=\min\limits_{\langle x, f_h(x)\rangle\in\mathcal{D}}f_h(x)$ contribute to the overall framework? Does this consideration potentially overlook the significance of $x$?

3. Could you provide a detailed explanation of the results presented in Table 2, as referenced in line 402?

There seem to be some typos:

1. In line 289, $\sigma_f^2(x)$ should be corrected to $\sigma_f^2(\tilde{x})$.

2. In line 298, there seems to be a pair of unnecessary parentheses $( )$ in $\langle(x^i,f_h(x^i))\rangle$.

3. In line 291 and 296, "equation 7" should be formatted as $(7)$.

4. In Theorem 2, what does $2_B^k$ refer to in line 322?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The paper performs multi-fidelity hyperparameter optimization by identifying promising regions in the low-fidelity landscape followed by searching the regions in the high-fidelity landscape.

### Strengths
The original idea seems to be novel.

The paper is well-written.

### Weaknesses
The paper lacks experiments comparing the proposed method with existing multi-fidelity HPO frameworks.


### Questions
Could this framework be applied to gradient-based hyperparaemter optimization methods?

### Soundness
3

### Presentation
3

### Contribution
3
