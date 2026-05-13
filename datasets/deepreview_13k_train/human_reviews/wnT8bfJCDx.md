# Explaining Modern Gated-Linear RNNs via a Unified Implicit Attention Formulation

- Decision: Accept
- Scores: 6, 5, 6, 8

## Abstract
\vspace{-4pt}
Recent advances in efficient sequence modeling have led to attention-free layers, such as Mamba, RWKV, and various gated RNNs, all featuring sub-quadratic complexity in sequence length and excellent scaling properties, enabling the construction of a new type of foundation models.
In this paper, we present a unified view of these models, formulating such layers as implicit causal self-attention layers. The formulation includes most of their sub-components and is not limited to a specific part of the architecture. The framework compares the underlying mechanisms on similar grounds for different layers and provides a direct means for applying explainability methods. Our experiments show that our attention matrices and attribution method outperform an alternative and a more limited formulation that was recently proposed for Mamba. For the other architectures for which our method is the first to provide such a view, our method is effective and competitive in the relevant metrics compared to the results obtained by state-of-the-art Transformer explainability methods. Our code is publicly available. %Our code is attached as a supplement.

\vspace{0.5em}
\hspace{.35em}
\includegraphics[width=1.25em,height=1.png}\hspace{

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper studies the problem of sequence modelling. The authors aim to provide a unified framework of the recent attention-free methods such as Mamba and RWKV. The paper presents empirical results to validate the proposed unified framework.

### Strengths
- The unified framework makes it easier to study and compare the different sequence modelling algorithms.
- It is important for the community to learn about such work.
- The experimental results are interesting.

### Weaknesses
Although it is hard to evaluate such approaches empirically, interpretability-based metrics are not very conclusive in general.

### Questions
- What is the best method to evaluate the unified framework beside the interpretability analysis?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces a unified framework that reformulates various gated recurrent neural network (RNN) architectures, such as Mamba, RWKV, and Griffin, into implicit causal self-attention layers. This reinterpretation aims to make these models more interpretable by constructing attention-like matrices for use in visual and NLP explainability tasks. Experimental evaluations demonstrate that this approach achieves competitive performance in robustness and attribution metrics, though prior work has already suggested that certain gated models, including Mamba, are attention-based.

### Strengths
The paper offers a clear explanation of how implicit attention could be used to interpret gated RNNs, making it accessible to readers interested in explainability across model types.

By applying the framework to both NLP and vision tasks, the authors demonstrate its cross-domain relevance.

### Weaknesses
Previous work has already conceptualized models like Mamba as attention-like, meaning that simply reinterpreting these gated RNNs under an implicit attention framework may not be largely novel.

The paper does not thoroughly compare its implicit attention framework with existing interpretability tools for gated RNNs.

### Questions
A critical question is: given that previous work has noted the attention-like properties of models such as Mamba, what specific benefits does the implicit attention framework offer over these prior interpretations?

What are the current explainability methods or metrics for modern gated-linear RNNs and how's the comparison between them and attention matrices?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper writes out gated recurrent architectures such as Mamba, RKWV, and Griffin as causal self-attention layers. The main objective of this is to increase interpretability, which is tested through perturbation and segmentation tests.

### Strengths
In my view, this is a pretty complete paper. From my understanding, the authors present an extension of the paper Ali et al. (2024) to include additional architectural components in the linearization and not just the S6 mechanism considered before. The authors show that the model improves interpretability through visualizations and a set of both perturbation and segmentation tests. The ablation gives quite a lot of strength to their arguments, but I am not so familiar with these types of explainability results so I am not able to comment on the details.

### Weaknesses
While the authors have explored the interpretability side of things extensively, I was wondering if it would be worth comparing the performance of the linearized models compared to its recurrent counterparts when trained on some small datasets?

### Questions
See above

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper tries to provide an implicit self-attention formulation for most state-of-the art non-transformer sequence models (known as Gated Linear RNNs) such as Mamba, Griffin, RWKV, and ReNet. In this way, it can exploit techniques used in attention explainablity to explain these new models.

Compared to the closest work (Ali et al, 2024), which only formulates the S6 layer in Mamba, the main contribution of paper is:
- Formulating more layers with implicit self-attention and propose a unified and more accurate attention-based representation for all the SOTA gated linear RNNs.

Other contributions include:
- Introducing new explainablity technique for these models leveraging the self-attention formulation
- Showing performance of their explanations and attributions by purturbation testing and segmentation.
- Showing their proposed formulation can give attributions which can further used in some performance-enhancing techniques (based on in-context learning) for large language models.

### Strengths
- Covering multiple models including most popular modern non-transformer sequence models.
- Evaluating the performance of the resulting attributions in multiple quantitate experiments and down-stream tasks (across both vision and NLP).
- Showing the impact of various sub-layers in the ablations study

### Weaknesses
 - In their ablation study, the authors could discuss the trade-off between the time explainability and more accurate formulation/explainability.

- The main baseline paper (Ali et al, 2024) has not been published yet. So, it is hard to evaluate this paper. Actually, the performance of the model in downstream tasks such as segmentation and attribution-based performance-enhancement helped me to have better evaluation of the proposed method.

### Questions
mentioned above.

### Soundness
3

### Presentation
4

### Contribution
3
