# Fine-Tuning Attention Modules Only: Enhancing Weight Disentanglement in Task Arithmetic

- Decision: Accept
- Avg Score: 6.25
- Scores: 8, 3, 6, 8

## Abstract
In recent years, *task arithmetic* has garnered increasing attention. This approach edits pre-trained models directly in weight space by combining the fine-tuned weights of various tasks into a *unified model*. Its efficiency and cost-effectiveness stem from its training-free combination, contrasting with traditional methods that require model training on large datasets for multiple tasks. However, applying such a unified model to individual tasks can lead to interference from other tasks (lack of *weight disentanglement*). To address this issue, Neural Tangent Kernel (NTK) linearization has been employed to leverage a ''kernel behavior'', facilitating weight disentanglement and mitigating adverse effects from unrelated tasks. Despite its benefits, NTK linearization presents drawbacks, including doubled training costs, as well as reduced performance of individual models. To tackle this problem, we propose a simple yet effective and efficient method that is to finetune the attention modules only in the Transformer. Our study reveals that the attention modules exhibit kernel behavior, and fine-tuning the attention modules only significantly improves weight disentanglement. To further understand how our method improves the weight disentanglement of task arithmetic, we present a comprehensive study of task arithmetic by differentiating the role of the representation module and task-specific module. In particular, we find that the representation module plays an important role in improving weight disentanglement whereas the task-specific modules such as the classification heads can degenerate the weight disentanglement performance.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper presents a method that fine-tunes only the attention modules of models to enhance weight disentanglement in task arithmetic. Task arithmetic is a training-free approach that enables new tasks by linearly combining the weights of a task-specific model with those of the original model. Building on NTK studies on kernel behaviour, the proposed method introduces an approximate kernel behaviour test to verify that attention modules exhibit this characteristic. The authors validate their hypothesis by fine-tuning only the attention modules in CLIP models, showing that this approach outperforms other fine-tuning strategies as well as the original NTK-initialization method.

### Strengths
The paper is well-organized and clearly written. The authors thoughtfully introduce relevant prior work, providing clear definitions and context for task arithmetic, weight disentanglement, and their associated challenges. Each argument is well-supported, with compelling visualizations that reinforce the method's performance. The progression from motivation to methodology is logical and engaging.

### Weaknesses
The paper has no prominent weaknesses. Here are some other open questions:

1. Contribution of Individual Attention Modules. 
While the method targets attention modules to achieve weight disentanglement, it remains unclear whether each module contributes equally to task performance. In large models, which may have over 100 billion parameters, understanding the relative contribution of each attention module could make the approach more efficient, possibly allowing for sparse fine-tuning of only the most impactful modules. An analysis or ablation study on the importance of individual modules could provide further insights into how weight disentanglement varies within the attention layers.

2. Generalizability to Non-Attention-Based Architectures. 
While the method demonstrates promising results on attention-based models, it would be useful to discuss the potential for generalizing this approach to non-attention architectures, such as convolutional or Mamba-based models. Would the same strategy apply effectively, or would alternative fine-tuning techniques be required for architectures without attention mechanisms? Providing an outlook on this point could help extend the paper's relevance across a wider variety of model architectures.

### Questions
See the weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper addresses task interference issues in task arithmetic, which arise when combining weights from multiple tasks into a single unified model. To tackle this issue, it uses Neural Tangent Kernel (NTK) linearization and trains only the attention layers in the transformer to reduce training costs. Through several experiments, the paper demonstrates the efficiency of the proposed approach and explains task arithmetic by distinguishing the roles of the representation module and the task-specific module.

### Strengths
1. The paper is easy to follow and provides clear explanations of essential concepts, making it easier to understand both the proposed approach and the fundamentals of task arithmetic.

### Weaknesses
1. The paper appears to be a naive combination of prior work, specifically [1] and [2], with modifications focused on training parameter selection (e.g., training only the attention layers in transformers), which limits its novelty.

2. The main contribution claimed by the authors—asserting that weight disentanglement primarily arises from the representation module while the effectiveness of task arithmetic is constrained by task-specific components—is not well-supported. Additional ablation studies, analysis, or theoretical support are needed to substantiate this claim. Depending on interpretation, the proposed contribution may be a trivial insight already known in the fields of task arithmetic or multi-task learning.

3. The experiments are quite limited, as many related works cited by the authors are missing from the experimental results, particularly in Tables 2 and 3. This omission reduces the validity of the proposed method.

4. The paper's theoretical contributions rely heavily on [2], which limits its originality and overall contribution.

### Questions
Refer to the weaknesses section.

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a new method to enhance weight decoupling in task arithmetic by fine-tuning only the attention module in the Transformer model. This method improves the weight decoupling ability of the unified model while maintaining the performance of individual models, thereby improving the performance of task arithmetic.

### Strengths
Innovation: The proposed method of fine-tuning only the attention module is innovative in the field of task arithmetic and can effectively solve the weight decoupling problem.
Experimental design: The experimental part covers multiple data sets and tasks, enabling a comprehensive evaluation of the effectiveness of the proposed method.
The results are remarkable: the method proposed in the paper achieves better performance than existing techniques on multiple benchmarks.

### Weaknesses
Parameter sensitivity analysis: The paper mentions the effect of the choice of α coefficient on performance, but does not provide a detailed sensitivity analysis. It is recommended to add experiments on the effect of the choice of α coefficient on model performance.

Computational resource consumption: The paper mentions the efficiency advantage of the proposed method, but does not provide a direct comparison with existing methods in terms of computational resource consumption. It is recommended to add analysis in this regard, especially memory and time consumption in actual deployment.

### Questions
While the paper mentions some related work, the relationship to existing methods could be discussed in more detail, especially the latest advances in model fusion and weight interpolation.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The authors propose to improve the performance of weight-interpolation-based model merging methods such as Task Arithmetic by finding a sub-module within the deep neural networks. I strongly agree with this idea because, for existing work based on NTK linearization, the model's performance on individual downstream tasks has been compromised in order to achieve better performance in multi-task model merging. This trade-off is usually unacceptable in practical applications, where ensuring performance on downstream tasks is paramount for fine-tuning. However, there are some typos and minor mistakes in this manuscript, which need to be addressed to improve the overall clarity and professionalism of the document.

Therefore, I would like to assign this manuscript an overall score of 6, indicating that it requires minor revisions. However, **I am open to raising the score if the authors address the specific concerns and suggestions outlined in my detailed review.**

### Strengths
1. The motivation of this study is clear. The authors seek to identify a subset of parameters that can undergo non-linear fine-tuning while retaining linear characteristics, such as those observed in NTK linearization. Consequently, the attention modules, particularly the linear layers within them, are selected for this purpose.
2. The experimental results presented in Figure 3 demonstrate the validity of the proposed method.
3. Models of varying sizes (ViT-B-32, B-16 and L-14) are employed for experimental evaluation.
4. The authors conduct experiments on both the vision domain and NLP tasks.

### Weaknesses
1. The task arithmetic presented in Definition 1 (lines 167-175) deviates from standard practice. In the original paper [1], task arithmetic is defined as $\theta_{unified} = \theta_0 + \lambda \sum_{i=1}^T \tau_i$, employing only a single scaling factor. Otherwise, it should be explicitly stated as task-wise AdaMerging [2]. The current formulation, with task-specific scaling factors, is not the standard approach and requires more justification, especially since the experiments are conducted with a single scaling factor. This discrepancy between the definition and the experimental setup needs to be addressed.
2. Missing scaling factor of task vectors in lines 52-53 and lines 353-357. The absence of the scaling factor in these equations makes the formulation incomplete and potentially misleading. The scaling factor is crucial for controlling the magnitude of the task vectors and, therefore, needs to be explicitly included in all relevant equations.
3. Is the summation symbol missing on the right-hand side of Eq.(1) (lines 196-199)?
$$ RHS = \sum_{t=1}^T \dots $$
The lack of a summation symbol on the right-hand side of the equation makes it mathematically incorrect. The equation should clearly indicate that the contributions from all tasks are summed.
4. In lines 400-401, the "disentanglement error" was first proposed by Ortiz-Jimenez et al. (2024). The authors should explicitly cite the original source when introducing this concept to give proper credit to the original authors.
5. Recent work on deep model fusion is missing from the related literature section. The authors may refer to these surveys [3,4,5] for additional information. The related work section should include a more comprehensive overview of recent advancements in deep model fusion to provide context for the proposed method.
6. A minor suggestion: The results for NLP tasks (Table 4) should be included in the main text. The inclusion of these results in the main text would improve the readability and accessibility of the paper.
7. The ablation study in Appendix B.4 is not mentioned in the main text. Consider including it in the main text. The ablation study provides valuable insights into the proposed method and should be highlighted in the main text.

### Questions
1. The differences between Definition 2 in the manuscript and the original definition in Ortiz-Jimenez et al. (2024) remain unclear. Could the authors elaborate further on these differences?

### Soundness
3

### Presentation
2

### Contribution
3
