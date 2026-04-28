# Transformer Meets Twicing: Harnessing Unattended Residual Information

- Decision: Accept
- Avg Score: 6.25
- Scores: 6, 6, 8, 5

## Abstract
Transformer-based deep learning models have achieved state-of-the-art performance across numerous language and vision tasks. While the self-attention mechanism, a core component of transformers, has proven capable of handling complex data patterns, it has been observed that the representational capacity of the attention matrix degrades significantly across transformer layers, thereby hurting its overall performance. In this work, we leverage the connection between self-attention computations and low-pass non-local means  (NLM) smoothing filters and propose the Twicing Attention, a novel attention mechanism that uses *kernel twicing procedure* in nonparametric regression to alleviate the low-pass behavior of associated NLM smoothing with compelling theoretical guarantees. This approach enables the extraction and reuse of meaningful information retained in the residuals following the imperfect smoothing operation at each layer. Our proposed method offers two key advantages over standard self-attention: 1) a provably slower decay of representational capacity and 2) improved accuracy across various data modalities and tasks. We empirically demonstrate the performance gains of our model over baseline transformers on multiple tasks and benchmarks, including image classification and language modeling, on both clean and corrupted data.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The over-smoothing problem in Transformers is a well-known phenomenon, where the outputs of different attention layers in a Transformer model are highly similar. This paper introduces Twicing Attention to address this problem, which uses low-pass NLM smoothing filters to tackle this problem. The core idea can be phrased as, instead of using the standard attention matrix $A$, to use $2A - A^2$.

### Strengths
1. The paper is relatively easy to follow and well-written.
2. The proposed "Twicing Attention" is simple and easy to implement.
3. Theoretical motivation and the mathematical details behind their motivation and choices have been provided.

### Weaknesses
1. The paper compensates for the simplicity of the core idea by over-explaining and being overly verbose. For example, most of the material on pages 7-8 can be summarised in 2-3 paragraphs. Even Algorithm 1 on page 8 is redundant and too verbose. The algorithm's objective is clear and simple: to compute $2A - A^2$. I don't think one needs 12 lines to explain that.
2. Instead, the paper could have added to its contribution through a more thorough study. E.g., one avenue for improvement would be to consider other candidates besides the $2A - A^2$ and then compare them in the considered benchmarks

### Questions
I would be grateful if the authors could respond and address the weaknesses. I am willing to increase my score if the authors could address the weaknesses.

### Soundness
3

### Presentation
3

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
The self-attention mechanism's representational capacity diminishes significantly across layers, and this oversmoothing effect is reducing overall performance. This paper introduces Twicing Attention, a novel mechanism that connects self-attention computations with low-pass non-local means smoothing filters. By employing a kernel twicing procedure, it alleviates the low-pass effects of NLM smoothing while preserving meaningful information from residuals. Twicing Attention offers slower decay of representational capacity and improved accuracy across different data modalities. Significant performance improvement brought by Twicing attention is observed in multiple tasks.

### Strengths
1. Novelty: The authors introduce the Twicing Attention mechanism to slow down the eigenvalue decay associated with representational collapse.
2. Theoretical Contribution: the authors provide mathematical validation for the Twicing Attention’s capability to retain information across layers.
3. Experiments: the authors evaluate their proposed methods on both language models and vision models.

### Weaknesses
1. Limited improvement: The gains in clean data settings (such as on ImageNet in Tab. 1) are modest. The reported improvements, while present, do not appear substantial enough to justify the added complexity of the Twicing Attention mechanism, especially given the computational overhead. A more significant performance leap would be expected for a novel approach of this kind.
2. Lack of comparison: the work does not compare its method with alternative solutions that address oversmoothing, such as regularization strategies. The absence of a direct comparison with established regularization techniques makes it difficult to assess the true value of Twicing Attention. It is unclear whether the observed performance gains are unique to this method or could be achieved by simpler, existing approaches.
3. Lack of ablations: the authors are suggested to consider applying the proposed method at different layer depths or intervals and evaluate their difference. The paper lacks a systematic investigation into the optimal placement of Twicing Attention within the network architecture. Without such an analysis, it is hard to determine the most effective way to integrate this mechanism into different model architectures.


### Questions
My question lies in the efficiency comparison (Tab. 4). Despite the fact that Twicing has the same complexity of $O(N^2 d)$ as claimed in the paper, it still increases the overhead by an additional 50% due to the extra matrix multiplication in line 7, Alg. 1. However, Tab. 4 indicates that implementing Twicing or not will not incur big difference on both speed and GFLOPs. What is the reason behind that? I would appreciate a more detailed efficiency analysis & comparison in the rebuttal phase if possible.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper propose the Twicing Attention, a novel attention mechanism that uses kernel twicing procedure in nonparametric regression to achieve slower decay of representational capacity and improved accuracy across various data modalities and tasks. And the design of this module builds on the study of the connection between self-attention and NLM smoothing filters. The method was tested on a public dataset, yielding promising results.

### Strengths
1. The paper is well-written, with clear expression of formulae and symbols, and will be highly readable.
2. The authors discuss the recurring problem of decay of representational capacity in Transformer, which has also been recognized as a manifestation of rank collapse in other studies. Instead of directly continuing the study of related work on rank collapse, the authors start with the NLM and try to gradually restore the cause of this phenomenon and again based on the proposed method that can alleviate this problem, the research angle is more interesting and also quite theoretical significance.
3. The author's description of the solution is complete and accompanied by thorough proofs, the process is clear and easy to understand, and the work done is very informative.

### Weaknesses
1. Admittedly, the authors' work is very rich and makes a very profound contribution at the theoretical level, but in my humble opinion, the authors' approach serves as a skillful level of reconciliation that moderates the rank collapse in depth, whereas a similar reconciliation skill is actually not uncommon in rank collapse-related research directions. I am not accusing the authors of not being innovative enough, but I hope that the authors can go further at the theoretical level and expand the sequence model that can really reduce the loss of information unlike the classical Transformer.
2. The author's research is more profound, but the experiments are less adequate, with too few test datasets and too few comparison methods. I tend to think that this is the result of too much time constraints, and I hope that the author will add more datasets as well as other experiments on the Transformer if there is enough time.

### Questions
1. For pure curiosity, I would like to ask what the authors think the performance of this method would be in more extreme cases, which in this case refers to two main scenarios: first, the performance on LLMs with a very large number of parameters. Second, on non-classical Transformer structures, such as Linear Transformer and other analogs.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces the Twicing Attention mechanism, drawing inspiration from established connections between self-attention and low-pass non-local means (NLM) smoothing filters. The authors demonstrate two key advantages of their proposed method: 1) a theoretically proven slower decay of representational capacity across transformer layers, and 2) improved performance on both vision and language tasks across multiple datasets. The paper's primary contribution lies in its theoretical framework. It first establishes that representation collapse in transformers stems from the inherent low-pass characteristics of NLM filters. The authors then provide proof showing that the twicing formulation ($2A^2-A$) offers superior theoretical properties compared to standard attention ($A$), particularly in preserving token diversity and meaningful feature representations.

### Strengths
- Theoretical foundation: The paper provides analysis connecting self-attention to NLM filters. 
- Fluent presentation flow: Messages of this paper are presented well, with well-demonstrated background knowledge and motivation.
- Empirical validation: The authors provide visualizations of attention heatmaps, which validates their claim that their method preserve the diversity of token representations

### Weaknesses
 - **Narrow Problem Framing**: The paper's central premise regarding "representation collapse" in transformers warrants closer scrutiny. Recent research has demonstrated that this phenomenon is not inherent to transformer architectures. For instance, DINO(Caron et al., 2021) demonstrates that self-supervised training can produce well-structured, diverse token representations in Vision Transformers. Furthermore, Darcet et al. (2024) provide evidence that apparent "collapse" may actually reflect a more nuanced information distribution pattern, where artifacts in attention heatmaps encode global information while non-artifact tokens maintain distinct representations, albeit with lower similarity to the CLS token.
- **Additional computational cost and marginal empirical improvements**: Performance increase in Table 4 is in trade of computational cost. Hardly can engineers be convinced to substitute the original attention with the proposed one.
- **Limited Evaluation Scope**: The authors report the empirical performance on classification tasks for vision models. Yet dense tasks such as segmentation are more direct and effective in evaluating the structure of patch representations produced by the method.

### Questions
- Visualizations on earlier layers and more heads of the transformers would help to strengthen your claim.
- Please refer to the weakness.
- I am open to increase my score if you alleviate my concerns.

### Soundness
3

### Presentation
3

### Contribution
2
