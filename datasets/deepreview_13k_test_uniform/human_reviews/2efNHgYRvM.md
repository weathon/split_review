# On the Identification of Temporal Causal Representation with Instantaneous Dependence

- Decision: Accept
- Scores: 8, 8, 8

## Abstract
Temporally causal representation learning aims to identify the latent causal process from time series observations, but most methods require the assumption that the latent causal processes do not have instantaneous relations. Although some recent methods achieve identifiability in the instantaneous causality case, they require either interventions on the latent variables or grouping of the observations, which are in general difficult to obtain in real-world scenarios. To fill this gap, we propose an \textbf{ID}entification framework for instantane\textbf{O}us \textbf{L}atent dynamics (\textbf{IDOL}) by imposing a sparse influence constraint that the latent causal processes have sparse time-delayed and instantaneous relations. Specifically, we establish identifiability results of the latent causal process based on sufficient variability and the sparse influence constraint by employing contextual information of time series data. Based on these theories, we incorporate a temporally variational inference architecture to estimate the latent variables and a gradient-based sparsity regularization to identify the latent causal process. Experimental results on simulation datasets illustrate that our method can identify the latent causal process. Furthermore, evaluations on multiple human motion forecasting benchmarks with instantaneous dependencies indicate the effectiveness of our method in real-world settings.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes IDOL, a framework for achieving identifiability in sequential latent variable models with instantaneous dependencies. The authors establish identifiability up to permutation of the latent variables and demonstrate that the underlying causal graph can be identified up to its Markov equivalence class (if this interpretation is correct). They thoroughly discuss the limitations of their assumptions in comparison to recent works, which helps underscore the significance of the proposed framework.

An estimation method is also introduced, with experiments on synthetic data verifying the theoretical results, while real-world experiments highlight the importance of incorporating instantaneous dependencies.

Edit: All the major concerns have been addressed in the rebuttal, and hence I have raised my score to 8.

### Strengths
- The manuscript is clear in terms of motivating the problem and introducing the theoretical framework.
- Incorporation of instantaneous effects into sequential latent variable models is a very significant contribution.
- The paper discusses limitations of the assumptions in comparison to recent works.
- The experiments with real-world data motivate the incorporation of instantaneous effects.

### Weaknesses
**Minor Concerns**
- **Computational Complexity:** The sparsity constraint introduced in Eq. (11) seems to introduce significant computational complexity to the algorithm. The paper would benefit from a more detailed analysis regarding this. For example, would it be possible to compute wall-clock times (in training) for IDOL in comparison the proposed baselines?
- **Scalability to High-Dimensional Data:** The authors acknowledge limitations with respect to high-dimensional data, which can restrict the application to real-world scenarios. An experiment to understand how high-dimensional one can go with IDOL would be ideal to support your point to understand how high one could go for IDOL.

**Major Concern: Theory Section Clarity and Limitations**

The paper’s theoretical claims, particularly around identifiability, would benefit from clarification to avoid potential misunderstandings regarding the nature of identifiability achieved. It appears that IDOL identifies the latent Markov Network rather than the true causal graph for the instantaneous component of the latent dynamics. This is an important distinction, as conditional independence relations allow only for the identification of the Markov equivalence class, not the directed causal structure itself. However, the presentation throughout the paper, especially in the introduction, experiments (such as Figure 4), and conclusions, may lead readers to infer that IDOL identifies the causal graph rather than the Markov network.

To address this issue, the authors could consider the following changes:

- **Introduction (around line 89):** Indicate that the identifiability of the instantaneous structure in IDOL is only up to a Markov equivalence class, clarifying that IDOL does not identify the directions of edges in the instantaneous part.
- **Figure 1c Modification:** Consider modifying Figure 1c to remove the arrow pointers from edges, signaling that the result is a Markov network rather than a causal graph when discussing identifiability (this might make sense in terms of theory, but not from a data generation perspective).
- **Conclusion:** Mention the Markov equivalence class limitation explicitly. This would open a path for further research to extend the identifiability result from Markov equivalence to the full causal structure, especially given the promising empirical results observed in Figure 4.

The following specific statements in the theory section could be revised to improve clarity and accuracy:

- lines 130-132: “the latent causal relations are also immediately identifiable because conditional independence relations fully characterize instantaneous causal relations in an instantaneous causally sufficient system”. I don’t think this line is correct without any additional assumptions. Conditional independence relations only provide the Markov equivalence class, not the exact causal graph, without further assumptions. Rephrasing this to accurately reflect the distinction between the Markov equivalence class and the causal graph would strengthen the theoretical foundation.
- lines 171-172: Could you indicate whether $p_{c_t}$ refers to the marginal distribution $p(c_t)$ or the conditional distribution $p(c_t|z_{t-2})$?
lines 165-188: For better readability, could you indicate $c_t \in R^{2n}$ in your example? Otherwise, at first glance it reads as  $\{z_{t,i}, z_{t-1,i} \}$ for $c_{t,i}$ in Theorem 1.
- line 217: Would it be better to use $\emptyset$ to refer to $\Phi$ as an empty set?
- line 230: Could you define “isomorphic” for Markov networks? A footnote or reference to the Appendix suffices.

### Questions
- line 41: do you mean “mixing function” instead of “mixture function”?
- lines 332, 386 and 387: Notation. You are using $\mathcal{L}$ and $L$ interchangeably. Could you revise this?
- If I am not mistaken, your identifiability theory does not obtain the causal graph, but a markov equivalence of it (please correct if mistaken). Yet apparently, the synthetic experiments suggest that you estimate the instantaneous causal graph with 100% accuracy (Figure 4, bottom left). Could you provide some explanation for this? For example, is it possible that your assumptions allow for stronger identifiability results that are overlooked in the presented theory?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The paper presents a framework, IDOL (identification of instantaneous Latent Dynamics), for identifying temporally causal representation with instantaneous dependencies. IDOL employs a sparse latent process assumption, which is more adaptable to real-world data. The framework is validation through extensive experiments on both synthetic and rea-world human motion datasets.

### Strengths
The paper introduces a novel approach to identifying temporally causal representations in time series data with instantaneous dependencies. This approach addresses a gap by proposing a sparse latent process assumption that is more practical for real-world applications than previous assumptions. 

Extensive evaluations are performance to demonstrate the effectiveness of the proposed approach.

The paper is well-organized. The use of illustrative figures helps clarify the complex concepts.

### Weaknesses
Providing further discussions on the possibility of extending IDOL to handle high-dimensional data can be beneficial. 

Given the limitation due to the dependency on invertible mixing processes, providing guidelines for real-world applicability would add value.

### Questions
How does IDOL handle cases where the latent process sparsity assumption is only partially met? 

Could the authors clarify the computational complexity of IDOL compared to baselines, especially for high-dimensional data? 

Are there specific real-world scenarios where IDOL might struggle due to non-invertible mixing processes?

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
3

### Summary
This paper introduces a framework called IDOL (Identification framework for Instantaneous Latent dynamics) to enhance temporally causal representation learning for time series data with instantaneous dependencies. Traditional approaches for identifying latent causal processes in time series data often assume that the latent causal variables lack instantaneous interactions, limiting real-world applicability. IDOL addresses this limitation by applying a sparsity constraint on causal influences, allowing for both time-delayed and instantaneous dependencies in latent variables. The IDOL frameworkassumes a sparse influence within latent causal processes, allowing both time-delayed and instantaneous relations. Unlike prior methods that require data interventions or predefined groupings to achieve identifiability, IDOL elies on this sparse latent structure alone, making it highly applicable to scenarios where interventions are impractical. The framework’s theoretical foundation is built on leveraging sufficient variability and temporal contextual information, establishing identifiability through a combination of variational inference and sparsity regularization. This enables the model to accurately reconstruct latent variables and the underlying causal relationships without complex external assumptions.

### Strengths
The proposed IDOL framework moves beyond traditional methods that often rely on grouping of variables or direct interventions, by introducing a sparse influence assumption to capture the natural sparsity in many real-world datasets. This approach is novel in handling instantaneous dependencies without requiring interventions or grouping. Furthermore, the paper demonstrates rigorous theoretical and empirical quality, supported by a well-founded identifiability proof and a solid mathematical framework. Experimental validation on both synthetic and real-world human motion datasets further underscores the robustness and reliability of the model, showcasing its ability to accurately identify causal relationships and achieve high predictive accuracy is synthetic and real-world datasets. The paper is overall clearly written and easy to follow. Overall, this work is significant for the field, since causal discovery for time series with instantaneous effects is an important open problem.

### Weaknesses
The model assumes an invertible mixing process to reconstruct latent causal structures, which may not always be feasible in real-world data. In some scenarios, particularly in non-linear and noisy environments, this assumption could lead to inaccurate or incomplete latent representations, potentially undermining the model’s performance and causal interpretability. Furthermore, IDOL’s effectiveness heavily depends on the assumption of a sparse latent process. In cases where this sparsity assumption does not hold (i.e., when the causal structure is dense or complex), IDOL’s performance degrades, as demonstrated in the experiments. This sensitivity suggests that the framework may be less robust in scenarios where latent processes are highly interconnected.

### Questions
Can you please comment on the performance of your method in noisy environments and low-sample regimes?

### Soundness
3

### Presentation
3

### Contribution
3
