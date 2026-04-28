# Solving Token Gradient Conflict in Mixture-of-Experts for Large Vision-Language Model

- Decision: Accept
- Avg Score: 6.40
- Scores: 6, 6, 8, 6, 6

## Abstract
The Mixture-of-Experts (MoE) has gained increasing attention in studying Large Vision-Language Models (LVLMs). 
It uses a sparse model to replace the dense model, achieving comparable performance while activating fewer parameters during inference, thus significantly reducing the inference cost. 
Existing MoE methods in LVLMs encourage different experts to handle different tokens, and they usually employ a router to predict the routing of each token. 
However, the predictions are based solely on sample features and do not truly reveal the optimization directions of tokens. 
This may lead to severe optimization interference between different tokens assigned to an expert. 
To address this problem, this paper proposes a novel method based on token-level gradient analysis, \textit{i.e.}, \textbf{S}olving \textbf{T}oken \textbf{G}radient \textbf{C}onflict (STGC).
Specifically, we first use token-level gradients to identify \textit{conflicting tokens} in experts. 
After that, we add a specialized loss tailored to eliminate conflicts among tokens within each expert. 
Our method can serve as a plug-in for diverse Large Vision-Language Models, and extensive experimental results demonstrate its effectiveness.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces an approach to improve the Mixture-of-Expert(MOE) by eliminating token-level gradient conflict during training. The gradient of the token is compared with the average gradient to decide the conflict tokens. A Conflict Elimination Loss (CEL) is proposed as a regularization term to encourage the reassignment of conflicting tokens. The results on various model setting and tasks validate the effectiveness of proposed method.

### Strengths
- The paper is well-written and easy to follow. The motivation for solving token-level gradient conflict during training MOE is sound to me.
- The proposed CEL can serve as a direct plug-in to improve the training of MOEs.
- A consistent improvement can be observed in Table 2 and 3, and the proposed STGC can be applicable to a wide range of model and data settings.
- The evaluation of gradient consistency in Figure 3 also provides further evidence to account for the improvement.

### Weaknesses
 - It would be better to illustrate the distribution of cosine similarity between gradients of all tokens and the averaged gradient for better understanding.
- Since the average gradient is dynamically changing during training, is it possible that some tokens do not conflict with a specific expert but become conflicting after several steps of training? It would be helpful to understand how the conflict status of tokens evolves over training.
- Why only the Large Vision-Language Model (LVLM) setting is considered? It is unclear if the proposed method is applicable to other modalities or tasks.

- Some minor points:
  - Figure 3b: better label the x-axis with "Training Step"
  - In TL;DR, a novel loss.
  - Figure A in supplementary: part of the figure is not visible

### Questions
- Will it introduce additional training costs for the computation of the gradient and similarity?
- It would be better to provide some analysis on the distribution of expert loadings for better understanding.

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
This paper identifies conflicting token as one of the major problem in MoE-based LVLM training. Furthermore, the author propose a novel Conflicting-Elimination-Loss to resolve the conflict. By applying the proposed loss, it provides performance improvements over baseline.

### Strengths
(1) The proposed approach is novel and is effective in improving the model performance.
(2) Resolving conflicting-token demonstrates a strong correlation with improvement of the performance, which makes it a seemingly good metric to study MoE.
(3) Thorough empirical results are provided to illustrate the effectiveness of the method. Sensitivity analysis are provided to show the robustness of the method.

### Weaknesses
 (1) Visualization on the routing mechanism of the trained model should be studied to provide insights into the trained model. By conducting such visualization, we might be able to know better why the proposed method can yield performance improvements. In addition, this could also validate the proposed method would still effectively utilize every one of the expert, instead of collapsing into only using one expert.
(2) It seems that the optimization process of the proposed CEL is not very stable (as in Figure 3(a)), the reviewer wonders whether this would be a problem when scaling up to larger scale.
(3) Computational overhead should be provided to ensure the proposed method does not incur too much overhead. This added study can show whether the proposed method is promising in terms of scaling up to large scale.

### Questions
See weakness section.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors make a very interesting and useful observation regarding the inconsistency/randomness in gradient direction for tokens routed to a particular expert in the Mixture of Experts framework. They then propose adding a loss term that aims to align the expert-wise token gradients to the expert-wise mean gradient over all tokens. The results presented by the authors suggest that the gradient alignment correlates with better performance, and also provide ablations showing that their method actually gets the token gradients to align.

### Strengths
**Relevance**

Routing has been a difficult task, which is pertinent to the Mixture of Experts framework. However, the understanding and analysis of the router predictions has been lacking in the literature. I believe this paper takes a significant step towards identifying and addressing a potential issue that leads to hindrance in learning in the MOE framework. The authors define the notion of a conflicting token, and then addresses it well using their proposed method, comprehensively justifying the performance in a variety of scenarios.

**Presentation**

I enjoyed reading the paper, it was easy to follow (except some parts listed in weaknesses), introduces the problem well, and presents detailed results and ablations to justify their proposed method. I specifically appreciate the statistical verification in Figure 3 along with the results which indicates that token conflict is actually a problem and resolving it leads to better performance.

**Practicality**

The section on memory considerations and the engineering tricks for reducing memory overheads is very helpful and leads to a much practical implementation of the proposed method.

### Weaknesses
I will combine and list the weaknesses and questions here.

**Practical Implementation**: While sec A in the supplementary compares the practical implementation with the heavy one in terms of Pearson correlation coefficient between the similarity metrics, I believe additional considerations 
- a quantitative measure of the memory overhead reduction (if not possible then a qualitative measure)
- performance difference on an actual dataset
could make the claim of practicality even stronger. Specific experiments or analysis in the main paper that quantifies the memory savings and any potential trade-offs in performance when using their practical implementation versus the full gradient computation would be helpful.

**Token Conflicts after STGC**: Fig 3 indicates the increase in gradient alignment over the course of the training process, but it would be interesting to understand the tokens that remain conflicting even after STGC. What proportion of the total tokens stay conflicting? Can something be reasoned about this behaviour? Along with the mean gradient consistency, it would be good to report the std deviations as well. It might also be worth tracking the proportion of total tokens that stay conflicting over the course of training. The authors' insights and justifications on this consideration would be useful.

**Conflict Elimination Loss**: Eqn 8 proposes the loss term, and the results do indicate its efficacy, but a more detailed motivation for the particular form of the loss could be useful. Specifically, why is $z_{moe}'(t_n)$ set to $-z_{moe}(t_n)$. Are there other forms that were considered, or insights into why this particular expression works would help.

**MOE Motivation**: The authors work with the assumption that MOE frameworks reduce interference between tokens from diverse data. However, there have been previous works that mention that it is not always the case. Particularly, [1] and [2] suggest that MoE does not necessarily lead to diverse data going to different experts, or observe weak correlation of router decisions with diversity. Additionally, [3] presents a MoE variant that works against this assumption, and uses nested experts. It would be helpful to suggest how STGC could be utilized in such scenarios. It might be useful to include a discussion section in the paper that explicitly addresses these alternative perspectives on MoE behavior 
- how STGC relates to or differs from these other findings, and 
- how STGC could be adapted or extended to work with different MoE variants like nested experts.

### Questions
Please see the weaknesses section for questions as well.

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
4

### Summary
The paper introduces Solving Token Gradient Conflict (STGC), a method to address interference between tokens within experts in Mixture-of-Experts (MoE) models for Large Vision-Language Models (LVLMs). STGC uses token-level gradient analysis to identify conflicting tokens and a regularization loss to optimize token routing, reducing interference and improving model performance. Experiments show STGC's effectiveness across diverse datasets, especially with larger data diversity. The method serves as a plug-in for existing MoE-based LVLMs. The study highlights the importance of managing token interference in MoE architectures and provides a novel approach to enhance their performance in vision-language tasks.

### Strengths
1. Routing is the key problem when training MoE and this paper targets this important problem to reduce interference between tokens within an expert in MoE models by using token-level gradient analysis.
2. The method demonstrated significant performance improvements on various vision-language benchmarks, indicating its effectiveness in enhancing model capabilities.
3. STGC is designed as a plug-in, which means it can be easily integrated into existing MoE-based LVLMs without the need for fundamental architecture changes.

### Weaknesses
1. The paper primarily focuses on the empirical validation of the STGC method. While the experimental results are promising, there could be a more in-depth theoretical analysis to understand the underlying principles and limitations of token gradient conflicts and how STGC addresses them. Specifically, the paper lacks a formal definition of 'token gradient conflict' and a mathematical justification for why the proposed regularization loss effectively mitigates this conflict. The analysis should delve into the properties of the gradient space and explain how STGC alters the gradient landscape to improve routing.
2. The paper mentions the reduction in inference cost but does not discuss the potential increase in training cost due to the additional computations required for token-level gradient analysis. The computational overhead of calculating and storing token-level gradients, especially in large models, could be significant and should be quantified. The paper should provide a detailed breakdown of the computational resources required for STGC, including memory and time costs, and compare them to the baseline MoE model.
3. The paper demonstrates the effectiveness of STGC on vision-language tasks. However, it is not clear how well these findings generalize to other domains or tasks outside of vision-language models. The method's applicability to other modalities, such as audio or time-series data, is not explored. Furthermore, the paper should discuss potential limitations of STGC in scenarios with different data characteristics or model architectures.

### Questions
Can you provide an analysis of the training costs?

### Soundness
3

### Presentation
2

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
This paper proposes a novel approach to address token interference in Mixture-of-Experts (MoE) architectures for Large Vision-Language Models (LVLMs). While MoE improves computational efficiency by activating only a subset of experts during inference, token interference within the same expert remains a challenge. The authors introduce Solving Token Gradient Conflict (STGC), which leverages token-level gradient selection to detect conflicting tokens and implements a conflict elimination loss to optimize token routing, thereby mitigating interference. The proposed method serves as a plug-and-play solution for various LVLM architectures. Empirical results substantiate the effectiveness of the approach, demonstrating significant improvements across multiple datasets.

### Strengths
* **Novel Perspective on Token-Level Interference:** The paper introduces an insightful perspective on token interference by analyzing conflicting optimization directions among tokens assigned to the same expert, which is an important and under-explored issue.
* **Direct and Effective Methodology:** The method efficiently identifies conflicting tokens through comparisons between individual token gradients and the global average gradient within experts. The regularization loss improves routing by discouraging conflicting tokens from remaining with the same expert.
* **Comprehensive Experiments:** The experimental results are extensive and validate the proposed method’s effectiveness. The evaluations across diverse datasets highlight the robustness and general applicability of the approach.

### Weaknesses
 * **Clarification on Gradient Conflict Hypothesis:** The authors assert that the learning of conflicting tokens increases the loss of most other tokens within the same expert. However, it is counterintuitive since conflicting tokens should be relatively few, making the directions of parameter optimization align with the global average gradient of all tokens in the expert. It is unclear how the magnitude of the conflicting token's gradient compares to the average gradient, and whether the conflicting token's gradient is strong enough to cause a net increase in loss for the other tokens. Clarifying this assumption with a more detailed analysis of gradient magnitudes and their impact would improve the paper's clarity.
* **Handling Conflicting Tokens Across Experts:** The paper suggests redistributing conflicting tokens to different experts. However, it is unclear how the method ensures that these conflicting tokens do not cause conflicts with tokens in other experts. The method lacks a mechanism to evaluate the potential for new conflicts when reassigning tokens, and it is not clear how the algorithm avoids cascading conflicts where a token is repeatedly reassigned. A more robust approach would consider the gradient landscape of other experts before reassigning tokens.
* **Questioning the Gating Network’s Learning Capabilities:** It remains unclear why the gating network fails to learn an optimal distribution for the conflicting tokens. Given that each expert should ideally handle tokens with similar characteristics, why would the gating network assign such divergent tokens to the same expert? The paper does not explore the underlying reasons for this behavior, such as the feature space of the gating network or the potential for the gating network to be optimized in conjunction with the conflict resolution mechanism. A deeper analysis of the gating network's behavior is needed to understand the root cause of the issue.

### Questions
All relevant questions are included under the “Weaknesses” section. If the authors can address these concerns adequately, I will consider increasing my rating.

### Soundness
3

### Presentation
3

### Contribution
3
