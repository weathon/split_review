# Augmenting Transformers with Recursively Composed Multi-grained Representations

- Decision: Accept
- Avg Score: 6.25
- Scores: 6, 8, 5, 6

## Abstract
We present ReCAT, a recursive composition augmented Transformer that is able to explicitly model hierarchical syntactic structures of raw texts without relying on gold trees during both learning and inference. 
Existing research along this line restricts data to follow a hierarchical tree structure and thus lacks inter-span communications.
To overcome the problem, we propose novel contextual inside-outside (CIO) layers, each of which consists of a top-down pass that forms representations of high-level spans by composing low-level spans, and a bottom-up pass that combines information inside and outside a span. The bottom-up and top-down passes are performed iteratively by stacking CIO layers to fully contextualize span representations. By inserting the stacked CIO layers between the embedding layer and the attention layers in Transformer, the ReCAT model can perform both deep intra-span and deep inter-span interactions, and thus generate multi-grained representations fully contextualized with other spans.
Moreover, the CIO layers can be jointly pre-trained with Transformers, making ReCAT enjoy scaling ability, strong performance, and interpretability at the same time. We conduct experiments on various sentence-level and span-level tasks. Evaluation results indicate that ReCAT can significantly outperform vanilla Transformer models on all span-level tasks and recursive models on natural language inference tasks. More interestingly, the hierarchical structures induced by ReCAT exhibit strong consistency with human-annotated syntactic trees, indicating good interpretability brought by the CIO layers.}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposed to augment the Transformer architecture with a contextual inside-outside layer (CIO). The CIO layer model explicitly the recursive syntactic compositions. The CIO layer goes in between the embedding layer and the self-attention layer. The author proposed a new variant of the inside-outside algorithm with contextualization ability. The CIO layer allows modeling of the inter-span and intra-span interactions. Experiments show that the proposed method outperforms the plain Transformer models on span-level tasks. It also outperforms recursive models on natural language inference tasks. The CIO also has good interpretability since it has strong consistency with human-annotated syntactic trees.

### Strengths
The author proposed a novel method that include the recursive syntactic composition information into the Transformer architecture. The method is verified to be effective, especially for span-based tasks, by experiments with

### Weaknesses
As authors pointed out, the CIO layer can be expensive. I'm also wondering how is the effect. Specifically, what is the computational overhead of the dynamic programming involved in the inside-outside algorithm, and how does this scale with sequence length? It would be beneficial to see a more detailed breakdown of the time and memory costs associated with the CIO layer, compared to a standard Transformer layer. Furthermore, while the paper demonstrates strong performance on span-level tasks, it's not clear how the CIO layer impacts performance on tasks that are not explicitly span-based, such as text classification or generation. It would be helpful to see a more comprehensive evaluation across a wider range of tasks to fully understand the generalizability of the proposed method.

### Questions
1. It would be interested to see if the gains still holds when we scale to larger models. (It is recognized it's not always possible/easy to experiment with a larger model.)
2. I'm wondering if the CIO layer can be trained at the finetuning stage so that we can still utilize a powerful pre-trained model and augment it with the CIO layer only at the finetuning stage.
3. This might be diverging or outside the scope of the paper, but I'm curious how tokenization would be affecting the effectiveness of the proposed method. For example, if it's byte or character-level vocabulary, do we observe a similar gain.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a syntax-augmented transformer based on producing span representations following the inside and outside traversals of a parse chart. Unlike existing methods following this idea (Fast-R2D2, DIORA), they incorporate cross-span contextualization. The resulting architecture is competitive with vanilla transformers on span-level and GLUE tasks while achieving strong grammar induction results.

### Strengths
(1) The method performs well compared to both transformers and Fast-R2D2 on span-level and sentence-level tasks, while also achieving strong grammar induction results.

(2) The method is evaluated on a wide range of tasks and compared to a wide range of baselines.

### Weaknesses
(1) As the authors mention, one of the main motivations for augmenting transformers with syntax is to improve compositional generalization (as well as potentially interpretability and controllability). Therefore, while the method does outperform transformers for span-level tasks, I think the results would stronger if there were experiments addressing these original motivations. Specifically, the paper lacks experiments that directly test the model's ability to generalize to novel combinations of syntactic structures or semantic meanings, which is crucial for demonstrating the benefits of syntax augmentation.

(2) While I understand that the method is inherently complex, I still think the methods section could be made a little clearer. For example, maybe a self-contained step-by-step summary of the algorithm at the end of the section would be helpful. The current description, while detailed, is difficult to follow, particularly regarding the interaction between the inside and outside passes and how cross-span contextualization is achieved. A more explicit algorithmic description, perhaps with pseudocode, would significantly improve clarity.

(3) While their method does outperform Fast-R2D2, the ideas feel very similar, limiting the scientific contribution of this work. As it stands, it feels a bit like a complex combination of ideas from Fast-R2D2 and DIORA, where the takeaway is a bit unclear. Is the key difference scalability, the use of transformers, pruning, cross-span communication, or all of the above? If the key difference is cross-span communication, why is that important and what are the specific changes in the algorithm that enable this difference? And are there ablation experiments that support the claim that cross-span communication is important?

(4) Related to (3), the paper would benefit from ablations to support the claims of why certain design decisions were effective. For instance, it's not clear how much each component of the proposed architecture contributes to the overall performance. Ablation studies focusing on the iterative up-and-down mechanism, the contextual outside pass, and the joint pre-training approach would provide valuable insights into the effectiveness of each component.

### Questions
(1) I find it a bit surprising that Fast-R2D2+Transformer is worse than Fast-R2D2 on GLUE (Table 3). Is there some intuition for why this is the case?

(2) Is there an ablation for ReCat without extra transformer layers?

(3) What are the model sizes for ours_{share} and ours_{noshare} in Table 2?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes contextual inside-outside (CIO) layers to explicitly model the syntactic structures of raw text in the encoding process of Transformers. The CIO layers are driven by a variant of the inside-outside algorithm proposed by DIORA (Drozdov et al. (2019) ). The authors leverage the linear neural inside algorithm proposed by R2D2 to prune cells that are unnecessary to encode during the bottom-up inside pass and propose to mix information from both inside and outside a span.

The benefits brought by CIO include (1) explicitly modeling syntactic structures without requiring parse tree annotations; (2) unlike previous work which only allows information flow within a span, CIO enables cross-span communications in a scalable way; (3) reducing the complexity of the inside-outside algorithm from cubic in DIORA to linear.

The major contributions are: (1) effectively combining ideas from two methods DIORA and R2D2 with innovative modifications. (2) introducing cross-span communication that breaks the information access constraint. (3) the experimental results on span-level tasks, natural language inference, and grammar induction demonstrate the effectiveness of the proposed method.

### Strengths
- Proposed an effective method to explicitly model the syntactic structure in the encoding process of transformers.

- It’s interesting to see that the Vanilla MLM can be used to replace the training objective of DIORA and the model can effectively learn the syntactic structure with the simple MLM objective.

- Results show that CIO can improve the transformer’s performance on span-based tasks and even help it to learn syntactic trees in an unsupervised manner.

### Weaknesses
 - Contribution is not significant: the proposed method is an effective way of combining ideas of the inside-outside algorithm from DIORA and node-pruning algorithm from R2D2 with modifications to fit them into the transformer framework and address some weaknesses in DIORA and R2D2 such as the lack of communication between spans.

- Efficiency is low: (1) as mentioned by the author, the computational load is many times higher than that of the vanilla Transformer model and the complexity of a single CIO layer is O(m2n). (2) If using fast-r2d2, the CIO layer needs a pre-trained top-down parser to predict a parse tree for a given sentence. This reliance on a pre-trained parser, even if integrated within the model, introduces an additional dependency and potential bottleneck.

- The major performance improvement is on Span-level tasks, and on sentence-level tasks ReCAT achieves worse performance compared with a vanilla transformer with similar size. On the structure-prediction task, ReCAT achieves similar performance compared with the previous method TN-PCFG. The limited gains on sentence-level tasks and structure prediction, especially considering the increased computational cost, raise questions about the practical utility of the approach beyond span-level tasks.

### Questions
- How do you deal with sub-word tokens: if a word is broken into multiple tokens, how do you handle them in the CIO layer?

- In 3.3, you mentioned “Specifically, we directly use the pretrained top-down parser to predict a parse tree for a given sentence and apply the trained Compose functions”, does this mean that your method requires a pretrained top-down parser?

- Is it necessary to train the Transformer from scratch in the experiments? One way of using CIO layers is to use them as adaptors which can be plugged into multiple transformer layers. Training a model from scratch can impose significant computational cost and it could be more efficient to harness the pretraining of existing Transformers instead of training from scratch.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes Recursive Composition Augmented Transformer (ReCAT), a model that aims to explicitly incorporate syntactic and structured trees into Transformers. The main change of ReCAT is the proposed contextual inside-outside (CIO) layers, which are inserted into a standard Transformer encoder right after the embedding layer. The CIO layer consists of the bottom-up and top-down modules. By stacking CIO layers, the iterative bottom-up and top-down layer-by-layer passes can unsupervisedly construct syntactic structures for the input sequence and produce contextualized representations for tree nodes.

By pre-trained with masked language modeling (MLM) and then fine-tuned, ReCAT was compared with Transformer-only methods and Fast-R2D2 and showed superior performance on multiple sentence-level and span-level tasks. Moreover, the syntactic trees induced by ReCAT exhibit strong consistency with human-annotated trees, proving that CIO layers can accurately learn syntactic structures.

### Strengths
- It is interesting and useful to augment transformers with multi-grained representations in an unsupervised manner.
- The proposed method is practical and effective based on the downstream task evaluation.

### Weaknesses
 - The paper is poorly written, with many notations without explanation. Figure 2 is a copy from Figures in Fast-R2D2, with an unclear caption.
- Lack of important details, e.g. the computational cost of the proposed layers, how to choose the number of layers, and the hidden dimension of the stacked CIO layers.
- It would be helpful to explain the main differences and advantages of the proposed method compared with related works, e.g. Fast-R2D2.

### Questions
- What are the advantages of the proposed method compared with Fast-R2D2?
- What is the computational cost and complexity of the proposed layers?
- How to choose the hyperparameters and the model configurations of the ReCAT models?
- Can the proposed method be incorporated and augmented to pre-trained models like BERT?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
