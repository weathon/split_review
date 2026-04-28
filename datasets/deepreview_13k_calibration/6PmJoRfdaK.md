# LongLoRA: Efficient Fine-tuning of Long-Context Large Language Models

- Decision: Accept
- Avg Score: 7.00
- Scores: 6, 8, 8, 6

## Abstract
We present LongLoRA, an efficient fine-tuning approach that extends the context sizes of pre-trained large language models (LLMs), with limited computation cost.
Typically, training LLMs with long context sizes is computationally expensive, requiring extensive training hours and GPU resources. For example, training on the context length of 8192 needs 16$\times$ computational costs in self-attention layers as that of 2048.
In this paper, we speed up the context extension of LLMs in two aspects. On the one hand, although \textit{dense global} attention is needed during inference, fine-tuning the model can be effectively and efficiently done by \textit{sparse local} attention. The proposed shifted sparse attention~(S$^2$-Attn) effectively enables context extension, leading to non-trivial computation saving with similar performance to fine-tuning with vanilla attention. Particularly, it can be implemented with only \textit{two lines of code} in training, while being optional in inference. On the other hand, we revisit the parameter-efficient fine-tuning regime for context expansion. Notably, we find that LoRA for context extension works well under the premise of trainable embedding and normalization. {LongLoRA combines this improved LoRA with S$^2$-Attn.}
LongLoRA demonstrates strong empirical results on various tasks on Llama2 models from 7B/13B to 70B. LongLoRA extends Llama2 7B from 4k context to 100k, or Llama2 70B to 32k on a single 8$\times$ A100 machine. LongLoRA extends models' context while retaining their original architectures, and is compatible with most existing techniques, like Flash-Attention2. In addition, we further conduct supervised fine-tuning with LongLoRA and our long instruction-following LongAlpaca dataset.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors propose a new method for adapting pretrained large language models (LLMs) to longer sequence lengths with a focus on efficiency. Prior works are either costly, due to requiring full fine-tuning of the language model or loose performance. The authors show that combining Low Rank Adaptation (LoRA) with sparse local attention provides improves efficiency while preserving performance. For LoRA, the authors note that a simple and cheap modification to LoRA, un-freezing embedding and normalization layer parameters, can prevent LoRA from loosing performance as sequence lengths increases. For sparse local attention, they employ a simple heuristic of splitting attention into independent groups of 2048 tokens. By overlapping groups within each layer at different attention heads, they ensure information flow between groups and are able to preserve performance at a level close to the much costlier full attention.

### Strengths
- The authors propose an extremely simple method, that performs well and is applicable to existing pretrained models

### Weaknesses
 - The authors only evaluate perplexity and retrieval setting

 - The authors do not provide sufficient detail on the group size selection for the sparse local attention mechanism. While they mention a 25% heuristic for an 8192 sequence length, it's unclear how this scales to longer sequences or if it is optimal. The lack of ablation studies on group size for different target sequence lengths is a significant gap.

 - There is a lack of clarity on how model FLOPs were estimated. The authors should provide a detailed explanation of the method or formula used, including whether it accounts for both training and inference, and the specific operations included in the calculation.

### Questions
- Have you done experiments / ablation on optimal group size for different target sequence lengths? It seems you have derived that setting the group size to 25% of target sequence length is reasonable for 8192 sequence length, but it is unclear whether this 25% heuristic or a constant group size translates to longer sequence lengths.
- There are multiple ways to estimate model flops. Please provide the method / formula you used for Table 10.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces a novel approach to extend the context length of transformer-based language models. The approach consists of two main ideas: 1) split the context into smaller subgroups and conduct attention in each group individually; 2) adapt the model to make use of this new attention approach via parameter-efficient fine-tuning with LoRA.

The authors conduct experiments with the Llama2 model family using models with 7B, 13B, and 70B parameters and compare their newly proposed approach to several baselines. In terms of perplexity, their proposed approach is able to maintain performance even when extending the context size by a factor of 16. 

Beyond language modelling, the authors evaluate their method in a retrieval setup (finding a hidden key in a long sequence of text), demonstrating its improved performance over baselines.

### Strengths
- The proposed method builds on previous work and shows strong empirical results on long lange language modelling and a retrieval task
- The proposed approach is conceptually simple and can be implemented in a few lines of code (as demonstrated by the authors)
- The proposed approach can be combined with existing approaches for context extension such as positional interpolation 
- The authors provide a detailed discussion of related work

### Weaknesses
 - The efficiency aspect of the could could be more prominently discussed in the main body of the paper
- The presentation of the work could be improved. See below for suggestions

- I had difficulties understanding Figure 3. It would help if you add indices and annotations to the matrices in this plot. Additionally, it could be helpful to draw a (visual) connection between the blue matrices on the left and the attention patterns on the right. 
- Be more consistent about the usage of $S^2$, shift short attention, LoRA+, and LongLoRA. Make it more explicit that LongLoRA = $S^2$ attention + LoRA.
- Table 7 is a great candidate for a line plot. 
- When pointing to results in the Appendix, make sure to reference a specific section in the Appendix. 
- The "attention patterns" ablation feels repetitive. How is it different from the "consistency to full attention" discussion in Section 3.2?
- In the section on retrieval-based evaluation you mention that your model is "somehow" able to handle longer context. What does this mean?

- You mention several times that the original standard self-attention can be retained at inference time. It would be helpful to provide more details on that. Also, Table 2 is mentioned as evidence for that. It would be helpful to elaborate more about the results in this table. 
- Table 3: What about an additional baseline that trains LoRA + embeddings?

### Questions
**Presentation**

- I had difficulties understanding Figure 3. It would help if you add indices and annotations to the matrices in this plot. Additionally, it could be helpful to draw a (visual) connection between the blue matrices on the left and the attention patterns on the right. 
- Be more consistent about the usage of $S^2$, shift short attention, LoRA+, and LongLoRA. Make it more explicit that LongLoRA = $S^2$ attention + LoRA.
- Table 7 is a great candidate for a line plot. 
- When pointing to results in the Appendix, make sure to reference a specific section in the Appendix. 
- The "attention patterns" ablation feels repetitive. How is it different from the "consistency to full attention" discussion in Section 3.2?
- In the section on retrieval-based evaluation you mention that your model is "somehow" able to handle longer context. What does this mean?

**Experiments**

- You mention several times that the original standard self-attention can be retained at inference time. It would be helpful to provide more details on that. Also, Table 2 is mentioned as evidence for that. It would be helpful to elaborate more about the results in this table. 
- Table 3: What about an additional baseline that trains LoRA + embeddings?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a method to perform LLM context extension with less memory and wall-clock time than existing methods. Their main modifications to improve efficiency are (1) training on local rather than global attention using the shift-short attention pattern, (2) using LoRA, and (3) modifying the norm and embedding layers in addition to the self-attention and feed-forward layers. The resulting method performs similarly to full fine-tuning.

### Strengths
(1) The method seems useful and impactful, and the evaluation is thorough with strong results.

(2) The authors perform very thorough ablations and isolate key design decisions (attention shift, modifying the norm & embedding layers) that enable the method to match full fine-tuning.

(3) The paper is well-written.

### Weaknesses
No major weaknesses.

### Questions
(1) While this is somewhat outside the scope of this paper, I would be curious about comparisons to methods that involve training a long-context LM from scratch.

(2) I am a bit confused why regular LoRA and LoRA+ (Table 11) use the same amount of memory. Does S^2-Attn reduce memory usage as well, or only flops?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
this paper proposes some computationally efficient methods to continue finetuning a pretrained model to support longer context. The paper proposed a modification for localized attention to support longer context by shifting the subgroups during finetuning. The paper also experimented with LoRA for long-context adaptation.

### Strengths
1. the paper is well written and easy to follow. the proposed approach is a simple method that can adapt LLM for longer context without too much compute.
2. the paper has good ablation to show that LoRA on embedding and normalization is important for long-context adaptation.

### Weaknesses
1. the paper only evaluated on retrieval and perplexity. It would be good to evaluate on other generative tasks that require longer context.
2. the improvement on perplexity doesn't seem super consistent in Table. 4

### Questions
1. Have you tried evaluating on any generative tasks?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
