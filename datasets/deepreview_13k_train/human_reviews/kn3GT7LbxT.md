# Value Residual Learning For Alleviating  Attention Concentration In Transformers

- Decision: Reject
- Scores: 5, 3, 3, 3

## Abstract
Transformers can capture long-range dependencies using self-attention, allowing tokens to attend to all others directly. However, stacking multiple attention layers leads to attention concentration. One natural way to address this issue is to use cross-layer attention, allowing information from earlier layers to be directly accessible to later layers. However, this approach is computationally expensive. To address this problem, we propose Transformer with residual value (ResFormer) which approximates cross-layer attention through adding a residual connection from the values of the the first layer to all subsequent layers. Based on this method, one variant is the Transformer with single layer value (SVFormer), where all layers share the same value embedding from first layer. Comprehensive empirical evidence demonstrates ResFormer achieves equivalent validation loss with 10.4\% fewer model parameters and 13.6\% less training data compared to Transformer, while maintaining similar memory usage and computational cost. Besides, SVFormer reduces KV cache size by nearly half with only a small performance penalty and can be integrated with other KV-efficient methods, yielding further reductions in KV cache, with performance influenced by sequence length and cumulative learning rate. Further visualization results suggest that Resformer and SVFormer alleviate attention concentration in deeper layers through avoiding value-state drains and enhance representation across most layers.}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
Paper proposes SVFormer, a way to reduce the size of the KV cache in Transformers by almost 50%. The authors propose sharing the values from the first self-attention layer across all layers. They find that this outperforms other approaches that reduce the KV cache size and perform extensive ablations to find when SVFormer works.

### Strengths
- Paper is straightforward and easy to read. 
- It's interesting that values from the first layer can be used throughout the network for a small loss penalty. 
- Authors thoroughly discusses prior work and explains the contributions of this work. 
- Lots of ablations and experiments.

### Weaknesses
 - The paper leaves out many important details. See the "Questions" section for specifics.
- Results are not well organized, and appear to have contradictory findings. Fig. 13 (c) in particular shows that SVFormer only outperforms a vanilla transformer when they have 2M parameters, which is very small.  At 82M parameters, SVFormer already is worse than the baseline. Fig. 13 (d), 14, and 15 also indicate that SVFormer hurts loss. However, Fig. 6 shows that SVFormer does better at larger scales
- I don't like the practice of subtracting the transformer performance and showing the difference. It potentially (a) hides bad baseline performance, and (b) potentially hides the fact that the difference between methods is tiny compared to the overall training loss curve.

- Fig 4:
  - What model is this?
  - It seems very shallow -- only 6 layers?
  - These seem like such shallow models. Is “current mapping” Eq. 4 or Eq. 5?
- Eq. 8: why is the identity matrix  $J$ and not $I$?
- Effect of scale unclear:
  - Which figures correspond to the 700M parameter model described in 4.1.1?
  - How are the hyperparameters tuned for the baselines (especially the vanilla Transformer)?
  - Why is Fig. 6 (right) inconsistent with Fig. 13 (c) on the effect of model size?
  - Authors should show scaling laws to show much better or worse their method is they scale up their model. 
- L460: "SVFormer will always be gradually surpassed by vanilla attention during training while its training speed is much faster than vanilla attention." How much faster can it be during training?

### Questions
- Fig 4: 
  - What model is this? 
  - It seems very shallow -- only 6 layers?
  - These seem like such shallow models. Is “current mapping” Eq. 4 or Eq. 5?
- Eq. 8: why is the identity matrix  $J$ and not $I$?
- Effect of scale unclear:
  - Which figures correspond to the 700M parameter model described in 4.1.1?
  - How are the hyperparameters tuned for the baselines (especially the vanilla Transformer)?
  - Why is Fig. 6 (right) inconsistent with Fig. 13 (c) on the effect of model size?
  - Authors should show scaling laws to show much better or worse their method is they scale up their model. 
- L460: "SVFormer will always be gradually surpassed by vanilla attention during training while its training speed is much faster than vanilla attention." How much faster can it be during training?

### Soundness
2

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
2

### Summary
This manuscript presents a novel framework for approximating cross-layer attention. Within this framework, the authors introduce ResFormer as a practical implementation, demonstrating its effectiveness in mitigating attention concentration challenges. In addition, they propose SVFormer within the same framework, which further enhances efficiency by reducing the memory requirements for KV caching, thus lowering overall computational costs.

### Strengths
The manuscript proposes a framework for reducing the computational cost of cross-layer attention, offering a unified approach that integrates and extends existing methods, including NeuTRENO and DenseFormer.

### Weaknesses
1. The paper lacks discussion of prior work on the attention concentration problem and the connection to the over-smoothing issue addressed by NeuTRENO is unclear. A more detailed review of relevant literature would enhance clarity and better contextualize the impact of this work.
2. Using training loss as a criterion for comparing model performance is unconvincing (e.g. in Section 4.2, 4.3, 4.6), as it may not accurately reflect generalization. A more reliable evaluation metric, such as accuracy or perplexity on a separate validation set, would provide a clearer assessment of the model's effectiveness. The reliance on training loss is particularly problematic when comparing models with different architectures or regularization techniques, as these can affect the training loss without necessarily improving generalization performance. For instance, a model with stronger regularization might exhibit higher training loss but better performance on unseen data.
3. Minor comments:
- The term “gold attention matrix” in Section 4.3 should be clearly defined for better understanding.
- Right margin violated at line 659.
- Some references list only the first author; please ensure consistency in citation formatting.

### Questions
Could you provide a detailed comparison of training time and memory requirements for SVFormer and ResFormer relative to other baseline models? Such a comparison is crucial for understanding the extent to which these models benefit from the proposed framework.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper studies the problem of attention concentration in Transformers and proposes solutions that try to approximate cross-layer attention by incorporating the "value" from first layer into subsequent layers. There are two solutions: ResFormer that uses residual mapping and SVFormer that uses the same V across all layers. Experiments show that the proposed solutions perform better than baselines on language modeling tasks.

### Strengths
- The paper introduces a relatively new and important problem that affects existing Transformer architecture. This is useful towards understanding the dynamics and behavior of Transformers.
- The proposed solutions only require small changes to existing Transformer architecture. They can be immediately useful for many existing Transformer-based models.
- The paper provides a good analysis and ablation study on ResFormer and SVFormer that demonstrate their benefits over existing Transformer. Particularly, ResFormer is shown to be achieving higher token importance entropy (i.e., less attention concentration) than traditional Transformer.

### Weaknesses
 - The authors claim that cross-layer attention is useful at reducing the effect of attention concentration but it is unclear why this would be the case. This work is built on the premise that ResFormer approximates cross-layer attention and thus it is effective against attention concentration. But we do not really know that cross-layer attention provides such a benefit. The author should perform some analysis and/or small-scale experiment on a baseline that actually uses cross-layer attention to check its behavior against that of ResFormer.

- It is hard to disentangle the effects from: (1) reducing attention concentration; (2) ease of optimization in the proposed solutions. Using V in the form of residual mapping (ResFormer) or layer sharing (SVFormer) should make it easier to optimize network parameters during training. It may be possible that the accuracy improvements are largely attributed to the ease of optimization rather than attention concentration reduction. The authors should explain this.

- It would also be interesting to see how well the proposed methods work for non-language tasks and architectures like ViT (image recognition).

### Questions
- What are the reasons of using LLama-like architecture and SlimPajama dataset?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper presents ResFormer and SVFormer, two Transformer model variants that address challenges with deep Transformers, particularly attention concentration where deeper layers focus too much on fewer tokens. ResFormer incorporates a residual connection from the initial layer's values to subsequent layers, thus approximating cross-layer attention without heavy computational costs. SVFormer simplifies further by sharing the value embedding from the first layer across all layers, reducing memory usage by nearly half and accelerating training.

### Strengths
1. The paper offers an interesting twist on standard residual connections by applying them specifically to V instead of the usual hidden state H. This approach targets the common issues of over-smoothing and information loss in deep Transformers.

2. SVFormer aims to make Transformer models more efficient by sharing the same value embeddings across layers, reducing memory and computation needs. This design could help make large models faster and more practical for applications with long sequences.

### Weaknesses
1. **Problem Definition and Motivation**: The problem of "attention concentration" is not clearly defined or sufficiently justified. It is essential for the authors to establish a precise understanding of this issue and clarify why it is a significant challenge within Transformer architectures. Without a thorough introduction and motivation for addressing "attention concentration," it remains unclear what gap this work aims to fill, and the importance of resolving it is left ambiguous. Specifically, the paper does not adequately distinguish between attention concentration and related phenomena like over-smoothing or attention sinks, making it difficult to understand the unique problem being addressed. A more rigorous definition, potentially involving metrics to quantify attention concentration, is needed to establish the problem's significance.

2. **Novelty and Theoretical Basis**: The proposed approach largely resembles existing residual connections in Transformers, as seen in architectures like ViT and LLaMA. The primary difference with ResFormer appears to be the application of residuals to the value V alone, rather than to the hidden state H as in traditional models. However, this adjustment lacks theoretical grounding and rigorous analysis, especially with regard to the SVFormer, which further simplifies by removing layer-specific values. This simplification seems ad-hoc and trivial, as no theoretical guarantees or insights are offered to support the effectiveness or necessity of such changes. The paper needs to provide a more in-depth analysis of why applying residuals to the value component is beneficial and how it differs fundamentally from applying them to the hidden state. Furthermore, the simplification in SVFormer, which shares value embeddings across layers, requires a more robust justification beyond just memory savings.

3. **Experimental Setup and Comparisons**: The experiments are limited and do not provide a thorough benchmark. Although the models are trained on a LLaMA-like architecture, there is no comparative performance evaluation against other prominent Transformer-based or SSM-based models. Furthermore, there are no tests involving visual downstream tasks, which would have strengthened the claims of improvement in Transformers and provided a more comprehensive evaluation across different modalities, especially for encoder-only tasks. The paper should include a wider range of baselines, including state-of-the-art models, and explore performance on diverse tasks to demonstrate the general applicability of the proposed methods. The lack of visual downstream task evaluation is a significant oversight, especially given the potential of the proposed methods to improve attention mechanisms.

4. **Evaluation of Attention Mechanisms**: An essential part of evaluating any modification to Transformer architectures is understanding how the attention patterns differ from those in the vanilla Transformer. Although the paper discusses attention concentration, it does not provide visualizations or statistical analysis of the multi-head attention weights to demonstrate the proposed method's effect on attention distribution. Such an investigation is critical for validating the claims and understanding how the modifications impact attention dynamics. The paper needs to include detailed visualizations of attention maps and quantitative metrics to show how the proposed methods alter attention patterns and mitigate concentration. Without this, the claims about addressing attention concentration remain unsubstantiated.

### Questions
same as weakness

### Soundness
2

### Presentation
1

### Contribution
2
