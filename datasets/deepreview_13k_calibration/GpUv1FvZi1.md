# Towards counterfactual fairness thorough auxiliary variables

- Decision: Accept
- Avg Score: 6.00
- Scores: 8, 5, 3, 8

## Abstract
The challenge of balancing fairness and predictive accuracy in machine learning models, especially when sensitive attributes such as race, gender, or age are considered, has motivated substantial research in recent years. 
Counterfactual fairness ensures that predictions remain consistent across counterfactual variations of sensitive attributes, which is a crucial concept in addressing societal biases. 
However, existing counterfactual fairness approaches usually overlook intrinsic information about sensitive features, limiting their ability to achieve fairness while simultaneously maintaining performance.
To tackle this challenge, we introduce \textbf{EXO}genous \textbf{C}ausal reasoning (EXOC), a novel causal reasoning framework motivated by exogenous variables. It leverages auxiliary variables to uncover intrinsic properties that give rise to sensitive attributes. Our framework explicitly defines an auxiliary node and a control node that contribute to counterfactual fairness and control the information flow within the model. Our evaluation, conducted on synthetic and real-world datasets, validates EXOC's superiority, showing that it outperforms state-of-the-art approaches in achieving counterfactual fairness.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This work aims to address the issue that previous methods ignored the intrinsic information in the exogenous variable U that does not lead to discrimination in predicting labels, leading to degraded performance. They propose a new causal graph with latent variables S' and S''.

### Strengths
- The proposed framework allows a trade-off between utility and fairness by adjusting the strength of the correlation between S' and S''.
- In linear cases, they provide bounds on the counterfactual fairness error to show the benefit of S'. They also provide an analysis with unknown functions in the causal graph.
- Strong empirical performance across different datasets and settings.
- Ablation study on \gamma and S'' supported the analysis in Section 3.

### Weaknesses
 - The proposed method heavily rely on the assumed causal graph in Fig. 1 (b). I wonder how general this causal graph can be. Specifically, the assumption that all sensitive information is mediated through S' and S'' seems quite strong. It's unclear if this framework can handle scenarios where sensitive attributes have more complex, non-mediated effects on the outcome, or where there are other confounding variables not captured by the proposed graph. The method's reliance on this specific causal structure could limit its applicability to real-world datasets with more intricate relationships.
- The experiments are only conducted on two small tabular datasets. This raises concerns about the scalability and generalizability of the proposed method. The performance on small datasets might not translate to larger, more complex datasets with higher dimensionality and more intricate relationships between variables. The lack of experiments on diverse datasets, including those with non-tabular data, makes it difficult to assess the robustness of the method.

### Questions
1. How is validation/model selection performed for the experiments?
2. Why do the authors only consider S' and S''? Is there any other latent variable that can be considered in that are not in the causal graph of Fig. 1 (b)?

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
2

### Summary
This paper introduces the EXOC framework, a causal model leveraging auxiliary and control nodes to enhance counterfactual fairness while maintaining predictive accuracy. It shows improved fairness compared to existing methods, validated on both synthetic and real-world datasets.

### Strengths
1) EXOC introduces a new approach by utilizing auxiliary variables to capture latent information, improving counterfactual fairness and accuracy, which is new to my knowledge
2) Demonstrates competitive accuracy and fairness on benchmark datasets, outperforming prior models. Though in many cases the improvement is only with accuracy or fairness, not as impressive as claim in the intro.

### Weaknesses
1) The paper does not adequately explain the process for tuning hyperparameters, particularly within the causal structure. Specifically, the role of hyperparameter 𝛾 in balancing fairness and accuracy is crucial, yet the approach to fine-tuning this balance remains unclear. And I am wondering if a efficient tuning strategy exist as it involves a tradeoff.
2) The causal diagram in Figure 1, illustrating the roles of auxiliary nodes S' and control nodes S'' , lacks practical grounding. The authors could strengthen their framework by providing realistic examples or settings in which these nodes causally impact the system in a way that aligns with the proposed structure. This would improve interpretability and offer a clearer justification for the chosen causal relationships.
3) Apart from above two, a major weakness I would point out is the experiment section:

Although synthetic data is a valid approach, as we could assume a groundtruth, Generating synthetic data with a Variational Auto-Encoder (VAE) introduces additional assumptions and potential challenges, such as ensuring the VAE accurately represents counterfactual distributions. The authors do not report VAE performance metrics or provide convincing examples of generated counterfactuals, which makes it difficult to verify if the synthetic data truly captures the desired counterfactual fairness properties. Without this validation, the reliability of the synthetic evaluation is unclear.

Both the use of real-world and synthetic datasets is very limited. For example, other commonly used fairness benchmarks include insurance dataset, Crime dataset. More datasets would strengthen the validation and help demonstrate EXOC’s assumption robustness across diverse real-world settings.

### Questions
1) Could you provide more details on the approach to tuning hyperparameters, especially γ, within the causal structure? How sensitive are your fairness and accuracy results to changes in this parameter, and what guidelines would you recommend for tuning it on different datasets?

2) Could you offer a practical, real-world scenario where the auxiliary node S′ and control node S′′ would interact causally in the manner illustrated in Figure 1? Examples or applications with concrete causal relationships would help clarify the intended structure and interpretability of the model.

3) Why did you choose a VAE for synthetic data generation over more conventional methods in fairness literature? Additionally, could you provide performance metrics or examples demonstrating the validity of the VAE-generated counterfactuals?

### Soundness
2

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
This paper aims to achieve counterfactual fairness through the introduction of auxiliary variables $S’$ and control node $S’’$.

### Strengths
The introduction of auxiliary variables $S’$ and control node $S’’$ is interesting.

### Weaknesses
 - The authors assert in the introduction part that their framework can "enhance fairness without compromising accuracy." However, the evidence supporting this claim is not readily discernible in the paper. A clearer demonstration or justification of this statement is needed.

- The methodology section lacks clarity in several areas. For instance, in lines 199-201, the statement "As $\alpha(s*−s)$ is the counterfactual parity that plays a more important role than the standard deviation, we showcase that δa>δb" is not intuitively clear. Additionally, there is no distinction between probability inference and causal inference, leaving the reader confused about the framework. Furthermore, the rationale behind choosing $S''$ over $\hat{Y}$ is unclear. Lines 345-350 do not provide enough context or reasoning.  

- The experimental results raise several questions. Specifically, why does the EXOC model outperform the Full model in accuracy when $\gamma=1$ on the Law School dataset? This outcome appears coincidental, and further analysis or explanation is necessary.

- The paper does not include comparisons with other models aimed at achieving counterfactual fairness, such as mCEVAE (Pfohl et al., 2019) [1], DCEVAE (Kim et al., 2021) [2], ADVAE (Grari et al., 2023) [3], or CFGAN (Xu et al., 2019) [4]. A comparison with these established methods is necessary for evaluating the effectiveness and innovation of the proposed framework.

### Questions
Please refer to the weaknesses above.

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper presents a novel framework called EXOC designed to achieve counterfactual fairness using auxiliary variables. By introducing an auxiliary node and a control node, the framework uncovers information from intrinsic properties that previous works have overlooked. EXOC demonstrates improved counterfactual fairness and offers finer control over the flow of intrinsic information, enhancing both fairness and accuracy. The framework is evaluated on synthetic and real-world datasets, showing superior performance compared to state-of-the-art models in terms of both counterfactual fairness and accuracy.

### Strengths
1. The theoretical analysis is compelling. The authors first outline an ideal model scenario, clearly demonstrating improved counterfactual fairness. They then extend their analysis beyond these assumptions to broader contexts, showing consistent performance improvements. The connection to information flow is creative, highlighting how the presence of $U$￼ leads to information leakage from $K$￼to $S$￼, while introducing $S'$￼ helps regulate the flow from ￼$S$ to $Y$￼.

2. The visual representations in Figure 2 effectively illustrate the impact of the control node. The clear differentiation between ￼$P(\hat{S})$ and $P(S)$￼ offers a fresh perspective on fairness issues, making the framework’s approach to counterfactual fairness more intuitive.

3. The paper is well-written, with clear and coherent presentation of research concepts. The experiments are thorough and well-designed, providing strong evidence to support the effectiveness of the proposed framework.

### Weaknesses
The introduction could be more comprehensive by including additional related works. While the authors discuss counterfactual fairness within the ML domain, there is a growing body of research that could complement the current submission, such as:

[1] Garg, Sahaj, et al. “Counterfactual fairness in text classification through robustness.” Proceedings of the 2019 AAAI/ACM Conference on AI, Ethics, and Society, 2019.

[2] Madras, David, et al. “Fairness through causal awareness: Learning causal latent-variable models for biased data.” Proceedings of the Conference on Fairness, Accountability, and Transparency, 2019.

[3] Zuo, Zhiqun, Mahdi Khalili, and Xueru Zhang. “Counterfactually fair representation.” Advances in Neural Information Processing Systems 36, 2023.

Including these references would strengthen the discussion of related works.

In Section 3.2.1, the authors provide an example to illustrate improvements in counterfactual fairness, further extended in Section 3.2.2. However, some aspects of the explanation could be clearer—please see the questions below for more details.

It is not clear why the authors chose a probabilistic model to implement the causal model, given that deterministic models (e.g., MLPs with activation functions) are often effective for inference tasks.

Some experimental settings and hyper-parameters could be better reported to ensure clarity and reproducibility.

### Questions
1. The introduction of causal functions involves the presence of $U$, but its specific contribution to the analysis is unclear. I also have concerns about the path analysis in your framework, as it appears to condition on specific paths (e.g., $\pi_{\vartheta}$￼ and $\pi_{b}$). Could other unconsidered paths also affect counterfactual fairness? If so, could these alternative pathways introduce unintended changes to fairness outcomes? How does your framework address or mitigate these potential effects?

2. Deterministic models like MLP and ResNet-50 are widely used due to their simplicity and effectiveness in optimization. Could you clarify the rationale for opting for probabilistic models and probabilistic inference in this context? Additionally, please elaborate on the relationship between probabilistic inference and causal inference in your framework. How do these two forms of inference interact, and what benefits does this interaction offer for achieving fairness and accuracy?

3. The trade-off between fairness and accuracy is well-documented in fairness research, often implying that gains in accuracy come at the cost of fairness. Could you elaborate on how controlling information flow differs from managing this trade-off, and provide justification for the distinction?

### Soundness
4

### Presentation
3

### Contribution
3
