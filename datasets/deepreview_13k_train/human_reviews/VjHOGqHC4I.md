# Enhanced Long LoRA Inspired Perceiver Architectures for Auto-Regressive Language Modeling

- Decision: Reject
- Scores: 3, 3, 5, 3

## Abstract
The Transformer architecture has revolutionized the Natural Language Processing field and is the backbone of Large Language Models (LLMs). The Transformer uses the attention mechanism that computes the pair-wise similarity between its input tokens to produce latent vectors that are able to understand the semantic meaning of the input text. One of the challenges in the Transformer architecture is the quadratic complexity of the attention mechanism that prohibits the efficient processing of long sequence lengths. While many recent research works have attempted to provide a reduction from $O(n^2)$ time complexity of attention to semi-linear complexity, it remains an unsolved problem in the sense of maintaining a high performance when such complexity is reduced. One of the important works in this respect is the Perceiver class of architectures that have demonstrated excellent performance while reducing the computation complexity. In this paper, we use the PerceiverAR that was proposed for Auto-Regressive modeling as a baseline, and provide three different architectural enhancements to it with varying computation overhead tradeoffs. Inspired by the recently proposed efficient attention computation approach of Long-LoRA, we then present an equally efficient Perceiver-based architecture (termed as Long LoRA Pereceiver - LLP) that can be used as the base architecture in LLMs instead of just a fine-tuning add-on. Our results on different benchmarks indicate much improved performance over the baseline PerceiverAR model, with the LLP showing impressive improvements compared to recent Transformer based models.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper focuses on the quadratic complexity issue of attention by proposing three architectures that combine PerceiverAR with LongLoRA, providing a trade-off between latency and performance. Specifically, these methods enhance historical information through (1) additional history vector, (2) chunk-wise history vector, and (3) token pooling-wise history vector. The authors pretrain three enhanced PerceiverAR LM in GPT-2 small-size on WikiText-103, with a context window size of 1024. Experimental results indicate that, at the same latent size, the three enhanced PerceiverAR model achieve lower PPL than the original PerceiverAR.

### Strengths
- The paper thoroughly reviews a series of approaches aimed at optimizing the quadratic complexity of attention.

### Weaknesses
 - The paper is somewhat disorganized, with an unclear main narrative and an excessive focus on related works. The three proposed methods appear somewhat trivial and lack core insights.
- The experimental section provides limited evidence of the effectiveness of the proposed methods, as it only compares against the original PerceiverAR model rather than full attention or other baselines discussed in the paper. Additionally, there is no comparison of performance on downstream tasks, nor sufficient ablation studies.
- The three PerceiverAR variants proposed involve trade-offs between performance and efficiency, but lack analysis and discussion on latency. 
- The writing and experimental sections are logically unclear and lack critical information, requiring substantial revision, as detailed in Questions. The paper is not suitable for acceptance at ICLR in its current form, and I recommend resubmission after major revisions.

### Questions
- Format: The citation format is incorrect; `\cite{}` should be `\citep{}`.

### Soundness
1

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper describes 3 extensions to PerceiverAR architecture: 
(1) adding history to latent state in each layer 
(2) the same as (1) but the attention on history part is splitted into n small segments  of length s with segment-wise attention
(3) history projected in small length p
(4) is similar to (2) but segments are shifted in the half of heads like in longLora

The first part is very similar to encoder-decoder, where encoder has only 1 layer with extra cost ( h x h+ h x l), where h is history length and l is latent length. In the second case, the cost is reduced to n x s x s + h x l . 
The 3rd option is equivalent to encoder with 1 layer and extra projection in the end.

### Strengths
The paper proposes 3 relatively minor variations of Perceiver AR + addition from longLora. The paper describes 3 extensions to PerceiverAR architecture:
(A) The first extension adds history to latent state in each layer.  This  is very similar to encoder-decoder, where encoder has only 1 layer with extra cost ( h x h+ h x l), where h is history length and l is latent length. 
(B) The second extension is similar to (1) but the attention on history part is splitted into n small segments  of length s with segment-wise attention to reduce the cost  to n x s x s + h x l . 
(C) 3rd extension is similar to (1) bur history is first to fixed  small segment p to reduce cost to pxp + p x l. The 3rd option is equivalent to encoder-decoder where encoder has 1 layer and extra projection in the end.
(LLP) Finally, authors add segments shifts to option B to  use overlapping segments . In this case whole sequence is used in auto-rergressive training.  

In the experimental part of the paper, authors compare baseline PerceiverAR with  4 proposed options.  LLP gives the best result, but the comparison with original Perceiver-AR is missing.

### Weaknesses
The paper demonstrates that LLP is better than Perceiver based versions. 
It is not clear 
*  how different LLP is from the LongLora architecture or from LongFormer by Beltagy 2020 https://arxiv.org/pdf/2004.05150. 
*  how LLP is related to Perceiver idea of compression long context into smaller  latent block:  I didn't find any latent block in the Fig. (3)  

Experimental part: 
the comparison of LLP with original Perceiver-AR is missing (see Table 10 in the original Perceiver AR paper: https://proceedings.mlr.press/v162/hawthorne22a/hawthorne22a.pdf )

Writing style. 
I would suggest  to combine section 1 (Introduction  ) and section (2 Related work and Contribution and remove the explanation how regular Transformer attentionw works (lines 47-78) .

### Questions
Do you use latent block in LLP? 
How LLP is different from the LongLora or from LongFormer by Beltagy 2020 https://arxiv.org/pdf/2004.05150?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper identifies two main drawbacks of the PerceiverAR architecture. The authors then propose three enhancements to the PerceiverAR architecture. The authors introduce the Long LoRA Inspired Perceiver (LLP) Architecture based on the concept of shifted sparse attention (S2 Attn) from LongLoRA. This approach splits the input sequence into overlapping segments and applies the PerceiverAR computation to consecutive pairs of half segments. This allows for efficient computation and information propagation throughout the entire context. The paper evaluates these enhanced architectures on the WikiText-103 dataset and compares their perplexity results. Model V1 performs the best among the enhancements, while Model V2 offers a more computationally efficient approach. The LLP architecture shows impressive perplexity results, indicating its effectiveness and computational efficiency. The authors conclude by highlighting the LLP architecture's benefits, achieving both efficient computation and impressive results due to its pairwise overlapping attention computation and information propagation. They suggest that the LLP architecture can be further enhanced by incorporating Long LoRA in the attention heads.

### Strengths
1. The paper provides a thorough overview of existing approaches for reducing attention complexity in Transformers.
2. The authors clearly identify the limitations of the PerceiverAR architecture, setting the stage for their proposed enhancements.
3. The authors propose three different enhancements, each with its own computational overhead trade-offs, providing flexibility for different use cases.
4. The LLP architecture offers an efficient and effective approach for handling long contexts by leveraging the concepts of LongLoRA and PerceiverAR.
5. The authors provide experimental results on a standard benchmark dataset, demonstrating the effectiveness of their proposed enhancements.
6. The paper discusses the performance of different architectures and analyzes the reasons behind the observed results.

### Weaknesses
1. The paper only evaluates the models on the WikiText-103 dataset. Evaluating the proposed architectures on other benchmarks, particularly those with longer-range dependencies, would provide a more comprehensive understanding of their capabilities. For instance, datasets like the Long Range Arena (LRA) benchmark, which includes tasks specifically designed to test long-context modeling, would be highly relevant. This would help assess whether the proposed LLP architecture truly excels at capturing long-range dependencies or if its performance is specific to the characteristics of WikiText-103.
2. While the authors compare their enhancements with the baseline PerceiverAR, they don't compare them with other state-of-the-art models for long-context modeling, which would strengthen the paper's claims. A comparison with models such as Transformer-XL, Longformer, or other recent architectures designed for long sequences would provide a better understanding of the relative performance of the proposed approach. Without such comparisons, it is difficult to assess whether the LLP architecture represents a significant advancement over existing methods.
3. The paper would benefit from more detailed ablation studies to understand the impact of different design choices in the proposed enhancements. For example, the effect of varying the overlap between segments in the LLP architecture, or the impact of different choices for the latent dimension in the Perceiver component, is not explored. Such studies would provide valuable insights into the sensitivity of the model to these hyperparameters and help identify optimal configurations.

### Questions
1. How does the choice of segment size affect the performance and computational efficiency of the LLP architecture? Are there optimal segment sizes for different datasets and tasks?
2. How well do the proposed enhancements integrate with other techniques for reducing attention complexity, such as local attention or sparse attention patterns?
3. How well do the proposed architectures generalize to other NLP tasks beyond language modeling, such as machine translation or text summarization?

### Soundness
3

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
This paper extends the PerceiverAR model by introducing three optimized versions aimed at improving the utilization of historical information. These enhancements address the issue of information loss that occurs due to compression into the latent space after the initial layer. Each enhancement involves trade-offs in computational efficiency. Experimental results on the Wikitext103 dataset demonstrate that the proposed model achieves lower perplexity compared to the PerceiverAR baseline.

### Strengths
This paper has implemented various optimization strategies based on PerceiverAR, resulting in lower perplexity on the Wikitext103 dataset compared to PerceiverAR.

### Weaknesses
1. **Limited experiments and baselines**. This paper only conducts experiments with PerceiverAR and the proposed model on the Wikitext-103 dataset. Furthermore, there is a lack of a substantial number of relevant baselines, such as Transformer[1], Transformer-XL[2], Compressive Transformer[3]. The paper only experiments with models of around 50M in size, which does not allow for validation of efficiency and effectiveness on larger models.
2. **Lack of key experiments**. The paper only presents theoretical computation times without offering practical runtime efficiency. It also lacks comparisons regarding model efficiency in real-world scenarios.
3. **Many grammar errors**. (1) line42- line44: "One of the reasons ~~for~~ (that) the CNNs are typically less effective in NLP is their limited receptive field because of the convolution operation."; (2) line68-line69: "Skip connections and layer normalization ~~is~~ (are) also used in each layer to stabilize the training of the Transformer."; (3) line137 - line138: "we attempt to improve upon these ~~short coming~~ (shortcomings) via different architectural enhancements in this paper"; and so on.

### Questions
N/A

### Soundness
1

### Presentation
1

### Contribution
1
