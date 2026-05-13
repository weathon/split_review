# Data-Aware Training Quality Monitoring and Certification for Reliable Deep Learning

- Decision: Reject
- Scores: 3, 3, 5, 3

## Abstract
Deep learning models excel at capturing complex representations through sequential layers of linear and non-linear transformations, yet their inherent black-box nature and multi-modal training landscape raise critical concerns about reliability, robustness, and safety, particularly in high-stakes applications. To address these challenges, we introduce YES training bounds, a novel framework for real-time, data-aware certification and monitoring of neural network training. The YES bounds evaluate the efficiency of data utilization and optimization dynamics, providing an effective tool for assessing progress and detecting suboptimal behavior during training. Our experiments show that the YES bounds offer insights beyond conventional local optimization perspectives, such as identifying when training losses plateau in suboptimal regions. Validated on both synthetic and real data, including image denoising tasks, the bounds prove effective in certifying training quality and guiding adjustments to enhance model performance. By integrating these bounds into a color-coded cloud-based monitoring system, we offer a powerful tool for real-time evaluation, setting a new standard for training quality assurance in deep learning.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
This paper introduces YES training bounds, a framework for real-time, data-aware certification and monitoring of neural network training. The framework evaluates data utilization efficiency and optimization dynamics, providing insights into training progress and detecting suboptimal behavior. The paper validates the YES bounds using synthetic and real data experiments, offering a tool for certifying training quality and guiding performance enhancements.

### Strengths
The proposed system's clarity is enhanced by the color-coded cloud-based monitoring system, which makes it intuitive for practitioners to interpret training status visually.

### Weaknesses
This paper has over-claimed its applicability, especially in model robustness and safety. None of the experiments discuss model safety and robustness. Accepting this paper unchallenged may send the wrong signal that the proposed method for enhancing model safety or robustness has been vetted, which it has not due to the omissions of related experiments.

### Questions
- Can you clarify how the YES training bounds directly contribute to improvements in model robustness and safety?

### Soundness
1

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper presents a heuristic for convergence diagnostics in multi-layer perceptrons that is data-aware. The authors propose to use solve a OLS-like linear problem for each layer to determine what a reasonable, but suboptimal weight matrix for each layer is. They then propose a traffic light system that compares training loss to this heuristic.

### Strengths
S1: Convergence diagnostics is a worthwhile problem to study. The criticism of local, curvature based convergence diagnostics is justified and hence, providing a empriical, yet strategic "benchmark" framework is an interesting approach.

S2: The proposed method is simple and readily accessible, even to a non-specialist audience, that is likely to benefit most from "training support".

### Weaknesses
 
**Motivation**

W1: I am sceptical of the utility of a "standardization of training practices in deep learning" (L078). The author's more detailed account that "The proposed YES [is] a promising pathway toward establishing a benchmark for the AI industry, regulators, and users alike" (L070) is vague and does not provide concrete details on _how_ this is valuable. For instance, the authors could provide examples or consult recent legislation on this issue. The connection between the proposed method and actual safety or regulatory needs remains unclear. It is not sufficient to claim that better training leads to safer models; this requires a more detailed argument and empirical support.

W2: Prior work is not properly cited. In fact, only a single paper (Oymak et al.) on neural network optimisation / convergence diagnostics is cited. The lack of a thorough literature review makes it difficult to assess the novelty and significance of the proposed method. There are many existing techniques for convergence diagnostics and optimization that should be acknowledged and compared against.

**Presentation**

W3: The Appendix is missing.

W4: The language and notation for the main results is not always clear. Examples:

- Eq 3 uses $\mathbf{Y}_k$ without ever defining it before. I suggest the authors provide a clear definition first.
- First paragraph in Section 4.1 is not clear (L183 - 189). Same for L245-L253.
- The paper describes a theoretical optimal model, the actual model, and the "bounding" model obtained by setting weights through the pseudoinverse. It is not always clear which of these models weight matrices or activations belong to.
- It is not clear what "intermediate states", "intermediate mappings", "intermediate points" are.

W5: The authors are inconsistent in their claims and tend to overstating their contributions. While the authors state at times that their method is a "sanity check", they later state:

- "[...] can attest that the training is not proper." (L205)
- "The answer (YES or NO) will provide immediate relief as to whether training has been meaningful at all" (L211)
- "The reason is simple: heuristics outperform random, and optimal beats heuristic" (L521) or L534 to L536.
- "These bounds aim to provide a qualified answer to the question as to whether a neural network is being properly trained by the data: YES or NO?" (L179).
- "cloud unequivocally indicate suboptimality" (L085). This is a very strong statement, for which there is no supporting evidence.
A more precise account of the contributions and limitations would be appropriate as well as fewer absolute statements without justification. The authors should avoid making claims that their method is definitive or universally applicable without sufficient evidence.

W6: The proposed method is a _heuristic_ not a certificate, which typically describes provable statements that can be asserted about a model. The authors should clarify that their method provides an empirical benchmark, not a formal guarantee of convergence or optimality. The term "certificate" is misleading in this context.

W7: The authors are overstating the impact to the safety of models. This work predominantly cites literature on ML safety, but does not set out a clear path how their work impacts safety, how it can establish trust and how it will help regulators. The statement "This standardization could play a crucial role in fostering trust and accountability within the AI ecosystem." lacks proper justification. The connection between the proposed training diagnostic and real-world safety concerns is not clearly established. The authors need to provide concrete examples or scenarios where their method would directly improve the safety of AI systems.

**Method**

W8: Using a linear model as baseline during training as bechnmark is common practice (when appropriate). The main insight seems to be the prediction of the target from each intermediate layer. I disagree with the authors statement: "A sensible but sub-optimal approach" (L185) and do not see sufficient justification for this statement. The authors state: "it has also been observed in various machine learning problems that after extensive training (resembling what we can describe as optimal training), the output of some inner layers become something meaningful to domain experts" (L255-258), for which they do not provide sources. The claim that projecting from intermediate layers is a sensible but suboptimal approach requires more justification and empirical evidence. The authors should provide examples or references to support this claim.

W9: layerwise OLS solutions are a very basic heuristic that do not mark significant contributions to the ML community. One can trivially, see that this bound becomes vacuous, even for single layer models when replacing ReLU with sigmoid (i.e. regard data-generating model $\sigma(AX+e)$ where $A$ has large values.) The authors need to address the limitations of their method, especially when using different activation functions. The fact that the bound can become vacuous under certain conditions is a significant weakness that needs to be discussed.

W10: At times, the authors do not provide sufficient proof or citation when making non-trivial statements.

- "Given a judicious selection of ... the latter should provide a tighter error bound compared to the YES-0 bounding approach" (L252). What is a judicious selection? Such claim should be supported by a theorem or a more detailed analysis.
- L255-258 as cited above. The lack of rigorous justification for these claims undermines the credibility of the proposed method. The authors should provide either theoretical proofs or empirical evidence to support their statements.

W11: The authors solely focus on the train loss, when in practice the test loss is most relevant in learning problems. The lack of consideration for test loss is a major limitation. The authors should explain how their method relates to generalization performance and provide empirical results on test datasets.

**Experiments**

W12: The paper describes experiments on 2 small toy data. This is not enough to extrapolate to real impact. There are various regression and classification datasets that seem like suitable tests for this method. In particular, Boston / California Housing Prices, SVHN, CIFAR-10(0) or TinyImageNet. Convergence diagnostics will become more relevant the more complicated the loss landscape and the more non-linear the problem gets. At the same time the proposed bound will become more vacuous in these settings. A detailed discussion of this would be of interest. Larger, more complex, and high-dimensional datasets are important to judge the potential impact of this method. The experimental evaluation needs to be significantly expanded to include more realistic and challenging datasets.

W13: The authors do not compare their method against diagnostics baselines. For instance, fitting a simple one-layer linear model, or discussing other strategies for convergence diagnostics. A comparison with existing convergence diagnostics methods is necessary to demonstrate the advantages and limitations of the proposed approach. The authors should include a discussion of how their method compares to other techniques.

W14: Figure 3 stops before models are converged.

**Minor**

MW1: It is community standard to have pdf links between in-text citation and the bibliography. This would be appreciated. Citations should be in round parantheses when not not part of the sentence's grammatical structure, e.g. (Goodfellow et al., 2016).

MW2: Figure 3: should share X and Y axis.

MW3: The lack of algorithm boxes, makes it difficult to follow the exact procedures described.

### Questions
Q1: Could the authors please clarify L090-L092: "They do not produce varying certification results across different training realizations, even when initialized identically or following similar optimization paths."

Q2: Why would randomness (L088-L095) be such an issue?

Q3: $\mathbf{Y}_{k}$ is never defined. What does it denote?

Q4: Could the authors clarify L245-L253. How does one obtain the YES-SIGMA bound precisely?

Q6: How will the YES cloud help regulators?

Q7: Is there a formalism to justify why projecting from each layer to $Y$ is reasonable?

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper introduces YES training bounds, a framework for real-time, data-aware certification of training, which aims at assessing the quality of model training. Specifically, these bounds evaluate the efficiency of data utilization and optimization dynamics. The depth and non-linear activation functions of models are taken into consideration. Experimental validation on synthetic and real data demonstrates the effectiveness of the bounds in certifying training quality.

### Strengths
1. The discussed topic is interesting, which focuses on monitoring the training quality and progress. With the proposed bounds, users could better control the optimization, which could benefit the community.
2. By considering the specific structure and properties of training data, the proposed YES bounds could provide tailored and precise evaluations of training performance.
3. Some experiments on image denoising task demonstrate the effectiveness of the proposed bounds.

### Weaknesses
1. No detailed discussion of relevant works, which makes it difficult to situate this paper. Some discussions of relevant optimization works are missing, such as [a, b].
2. The contribution of this paper could be overclaimed. YES bounds are introduced to indicate the training quality. Although the authors claim that the proposed training bounds aim at improving the reliability, robustness, and safety of models, it is difficult to see how the YES bound can be utilized for such a purpose. The connection between the proposed bounds and downstream model performance is not clearly established.
3. This paper discusses the scenario of non-direct paths in Section 4.2.1, however, it is difficult to see how the enhanced bounds that involve intermediate points can tackle this issue. The explanation lacks clarity on how these intermediate points are selected and why they would lead to tighter bounds.
4. Another concern lies in the evaluation, it is unclear whether the proposed training bounds can be generalized to different CV and NLP applications, such as image generation via diffusion, VQA via LLaVa, etc. The experiments are limited to a denoising task and do not demonstrate the broad applicability of the method.
5. It is also unclear how the proposed training bounds can motivate new research works or provide insights into this field. The paper does not clearly articulate the potential impact on the broader research community.

### Questions
1. Please discuss the relevant work in the field of optimization and clarify the novelty of this paper.
2. Please clarify the contribution and explain the application of YES bounds in the field of model robustness and reliability.
3. Please explain why the enhanced bounds in Section 4.2.2 can tackle the issues discussed in Section 4.2.1.
4. Please provide more evaluation on different CV/NLP tasks to highlight the generalization of the proposed bounds.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper explores the challenge of monitoring the quality of training for deep learning models. The paper proposes a method based on upper bounds for the training loss, estimated using linear projections from different layers during training. The authors show that comparing the training loss with the estimated bounds can provide real-time insights into the quality of the training procedure, facilitating the intervention in case of ineffective or sub-optimal training.

### Strengths
The idea of using linear projections as a weak model to compute upper bounds on the training loss is interesting and original. 

The method is well-described and easy to understand. Mathematical proofs are easy to follow.

Getting insights on the training process beyond the local optimization perspective might be a promising and relevant direction for the future of ML optimization.

### Weaknesses
* The paper only analyzes small networks with FeedForward architecture and only Linear layers. It is not clear how the procedure could be applied to practical architectures such as ResNet or Transformers. Additionally, there are no concrete details about the architectures used. I assume all hidden layers have the same dimensionality as the input and output, but this should be clearly stated. I suggest the authors extend their experiments to more complex architectures and to include a detailed description of the architectures used (e.g. a table with the number of layers, number of hidden neurons per layer, activation functions).
* The tasks used for training the networks are not clearly explained. It is not clear what is the input and output of the models, what is the loss function and whether the trained models can achieve any significant generalization power. In particular, for the 1D Signal Denoising task, it is unclear how the random signal drawn from $N(0,1)$ could be recovered after applying noise drawn from $N(0,0.2)$. I would like to see more detailed explanations regarding the tasks and the training setup.
* The practical image recovery experiment in the Appendix does not seem to have real practical applications. My understanding is that the model is specifically trained to recover one image after it has been corrupted, which would require full access to the uncorrupted image during training. If this is correct, then this example has no more practical applicability than the synthetic data tasks. It is also unclear how the network is constructed and what are its inputs and outputs. I suggest adding some more detailed explanations about the training and the model architecture.
* The paper presents no analysis of the running time of the proposed method. It is unclear how the method will impact the training time of the model under real-time conditions. It would be interesting to see a comparison of training times with and without the YES bounds computation and an analysis of how the computational overhead scales with model size (I would expect the costs of estimating higher order YES bounds to significantly increase for very deep models).
* The utility of the proposed method concerning train-test generalization is only presented in the Appendix. I consider that this experiment should be presented in the main body of the paper, as ultimately the purpose of training models is generalization to unseen test data. However, it is unclear how well the model is able to generalize in this case: Figure 4 clearly shows a correlation between the evolution of the training and testing losses, but the minimum value of the test loss is similar to the starting value of the training loss, hinting towards very poor generalization capabilities. This is very likely caused by the low correlation between train and test data, so repeating the experiment on real-world data might show more favorable results. Additionally, this experiment does not present any training details (learning rate, batch size, train/test split ratio etc.).

**Minor points**
* Algorithm 1 should have the model as input along with the training data.

**Formatting**
* The Appendix should be part of the main pdf, not as a separate document
* References to Sections, Figures, Tables, Equations and Citations should have hyper-ref links for better navigability.
* Multiple citations are not well integrated into the text, for example: Line 031 should read “... transformations (LeCun et al.2015, Goodfellow et al. 2016).” which can be achieved by using the \citep{} command. Line 041 should read “Oymak & Soltanolkotabi (2019) theoretically demonstrate …” which can be achieved by using the \citet{} command.
* Line 050 has an unmatched parenthesis after YES.
* Figures 3,4 should have a clear ordering for the learning rates (instead of 1e-3, 1e-2, 1e-4). Subfigure labels for Figures 3,4,5 would also facilitate understanding.

### Questions
1. Please address my comments in the Weaknesses section.
2. The experiments show that sometimes the training gets stuck in loss plateaus while in the yellow region. Is there any action that one might take to avoid or overcome this obstacle, other than waiting for the loss to drop? 
3. It is not clear how Deep Unfolding Networks are relevant in the context of this paper, as they are only briefly mentioned in section 4.2.1, without sufficient explanation, and then never mentioned again. Can you give a more detailed explanation?

### Soundness
2

### Presentation
2

### Contribution
2
