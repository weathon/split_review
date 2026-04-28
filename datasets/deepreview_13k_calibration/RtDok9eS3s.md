# Simplifying Transformer Blocks

- Decision: Accept
- Avg Score: 7.33
- Scores: 6, 8, 8

## Abstract
A simple design recipe for deep Transformers is to compose identical building blocks. But standard transformer blocks are far from simple, interweaving attention and MLP sub-blocks with skip connections \& normalisation layers in precise arrangements. This complexity leads to brittle architectures, where seemingly minor changes can significantly reduce training speed, or render models untrainable.

In this work, we ask if the standard transformer block can be simplified? Combining signal propagation theory and empirical observations, we motivate modifications that allow many block components to be removed with no loss of training speed, including skip connections, projection or value parameters, sequential sub-blocks and normalisation layers. In experiments on both autoregressive decoder-only and BERT encoder-only models, our 
 simplified transformers emulate the per-update convergence speed and performance of standard transformers, while enjoying 16\% faster training throughput, \& using 15\% fewer parameters.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work presents a thorough investigation into the complexity of standard transformer blocks, questioning the necessity of various components commonly included in their design. Through a combination of signal propagation theory and empirical observations, the authors propose a simplified transformer architecture that maintains performance levels while offering benefits in terms of training speed and model parameter count.
The paper challenges the conventional wisdom of transformer design by systematically evaluating the impact of removing certain elements, such as skip connections, projection or value parameters, sequential sub-blocks, and normalization layers. The experimental results, as reported, demonstrate that these simplifications do not detrimentally affect the training speed and can lead to a 15% increase in training throughput and a similar reduction in parameter count.

### Strengths
- As the work mentions, this is the first work which has simplified the transformer architecture with training throughput gains. Previous works which have tried to simplify transformer architectures have led to increase in training speeds.
- The paper is overall well written. The authors discuss each design choice in detail, which helps in understanding the motivation behind the simplifications proposed.
- The authors have appropriately discussed the limitations of their work.

### Weaknesses
 - One weakness is that the results are limited to smaller models of size ~100M. It is not clear if the results would scale to bigger models. 
- Moreover, the authors only consider GLUE benchmark for downstream evaluation. It would be nice to include a more comprehensive evaluation across different task categories like classification, generation or reasoning.

- The authors mention that there is a Pre-LN and a Post-LN block and the Pre-LN work is more popular because Post-LN suffers from training instability. Is this phenomenon observed in the signal propagation literature only or all the current LM works also use this Pre-LN variant?
- The authors mention “our simplified transformers match the per-update training speed and performance of standard transformers, while enjoying 15% faster training throughput”. If the parameters are being reduced, why isn’t the per update speed faster? And, why is the throughput faster?
- On page 3, the authors mention skipless transformers are slower than those with skip connections. Why is that?
- Are there any settings (data or tasks) where this simplified transformer does not work as well compared to the standard transformer?
- What are the limitations of the proposed simplifications in terms of model expressiveness and capability?
- What is the size of the model which has 18 blocks and 768 hidden dimensions?
- In section 4,1 what is the motivation from going from SkipInit to ShapedAttention? Another question is since this work is adding identity addition to value and projection matrices, in what way this is simpler than the residual connection?

### Questions
- The authors mention that there is a Pre-LN and a Post-LN block and the Pre-LN work is more popular because Post-LN suffers from training instability. Is this phenomenon observed in the signal propagation literature only or all the current LM works also use this Pre-LN variant?
- The authors mention “our simplified transformers match the per-update training speed and performance of standard transformers, while enjoying 15% faster training throughput”. If the parameters are being reduced, why isn’t the per update speed faster? And, why is the throughput faster?
- On page 3, the authors mention skipless transformers are slower than those with skip connections. Why is that?
- Are there any settings (data or tasks) where this simplified transformer does not work as well compared to the standard transformer?
- What are the limitations of the proposed simplifications in terms of model expressiveness and capability?
- What is the size of the model which has 18 blocks and 768 hidden dimensions?
- In section 4,1 what is the motivation from going from SkipInit to ShapedAttention? Another question is since this work is adding identity addition to value and projection matrices, in what way this is simpler than the residual connection?

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
This paper studies how to simplify the self-attention block in transformer models. Some modifications are made based on several interesting and empirical findings:
- This first is that, while somewhat similar to prior work, this paper points out that the skip connection in the self-attention subblock could be removed, without loss of training speed.
- The second is that the value and projection parameters in the sub-attention blocks could be fixed to the identity matrix, which reduces two parameterized matrices.
- Third is that the MLP sub-block skip connection could also be removed in the parallel MHA and MLP structure.
- The forth is that all normalization layers could be removed given that the proposed block has already taken the effect of normalization into account (to some extent?).

### Strengths
- Some interesting findings revealing the underlying working mechanism of the attention sub-block in the self-attention is reported. These findings, despite being empirical, also lead to a simplified self-attention block. It provides valuable insignts on how to design an efficient self-attention block. The community would like to see it.
- The paper did a good job explaining the step-by-step simplification flow and have provided sufficient reasons/experiments to discuss why.
- The paper is very well written, which is a pleasant read.

### Weaknesses
 - Some critical designs in the proposed block are from existing literatures, e.g., the shaped attention (Noci et al. 2023) and the parallel structure (Wang & Komatsuzaki, 2021) of MHA and MLP sub-blocks.
- While the block is simplified, the benefits of the simplification is not significant. The simplified transformers only match the per-update training speed and performance of standard transformers. While being 15% faster and having 15% fewer parameters, some part of the throughput gain is due to the use of the parallel structure by (Wang & Komatsuzaki, 2021). The actual throughput gain from the proposed simplifications, excluding the parallel structure, is not clearly quantified.
- The removal of normalization somewhat contradicts between the analysis and approaches. In Sec. 4.4, it says that the normalization layers are unnecessary, but it quickly comments that the normalization still has benefits and is still used in experiments. This somehow leads to a confusion of read. The analysis focuses on signal propagation at initialization, while the experiments are conducted on trained models, making the connection between the two less clear.
- The performance of the simplified block slightly falls behind the standard Pre-LN and Parallel in Table 1, which means in practice the community may not use the proposed simplified block. The reported results do not convincingly demonstrate a clear advantage of the proposed simplified block over existing architectures, especially considering the minor performance drop.

### Questions
Depite the weaknesses, I generally like this paper as it does provide some deep insights of the self-attention mechanism. I also have a few additional questions that expect the authors to reply:
- The simplification is mostly carried out in the context of skipless self-attention block. Why the block is preferred to be skipless? Is there any benefits? From the view of signal propagation theory, the skip connection benefits propagation, particularly for deeper models, and does not violate the philosophy of simplicity,.
- From Fig. 19, the pre-LN block performs worse when setting values and projections to identity. An intuition is provided, but I am not totally convinced by this intuition. In fact, I see the performance difference is almost negligible. It seems OK to set the values and projections to identity in the standard attention block with skip connection. This also reduces the number of parameters.
- Why is the performance SAS-P, no norm not reported? Is the training failed or the performance is significantly lower? In fact, I would suggest that the block can preserve the normalization layers to keep the consistency between analyses and experiments.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper undertake a critical study of several components of the transformer block, with aim of simplifying the block. The authors utilize shaped attention (identity-preserving attention initialization), and scaling the MLP block to remove the value and projection matrices, and all the skip connections from transformers. The authors do detailed ablations of all variations/modifications and scaling factors, as well as studying the impact of layernorms and skip connections. The changes are studied on pre-training for GPT and BERT models, and downstream finetuning for BERT on GLUE. The proposed changes result in models with comparable/better performance compared to vanilla models, with improved training speed and fewer params.

### Strengths
1. The approach is well grounded on related work (SkipInit/Shaped-attention, residual scaling, etc.), and presents strong natural extension of them.
1. Completely removing the Value and Projection Matrices and skip connections offers strong simplifications.
1. The authors method achieves parameter saving and training speedup, while also resulting in simpler blocks. The training speedup could perhaps be further optimized with better implementation/variations.
1.  The experiments presented are thorough and well-motivated. They cover a wide range of variations/ablations, multiple different models, and multiple tasks.

### Weaknesses
1. The authors acknowledge that their experiments are in the range of smaller models (100M-300M). It will be interesting to see if the gains carry to larger models. Specifically, the observed benefits in training speed and parameter reduction might not scale linearly, and could diminish or even reverse with larger model sizes, where different bottlenecks may emerge. The computational overhead of attention mechanisms, for example, could become more pronounced in larger models, potentially negating the benefits of simplified blocks.

2. Most of the experiments are conducted on training for only 650M tokens. 650M is a low number of tokens, compared to even "compute-optimal" tokens suggested by chinchilla for the model sizes the authors use. It will be important to see if the proposed method falls behind on training for longer. That being said, Figure 8 was trained for 2B, and BERT ones for 5B. It is unclear if the simplified blocks would maintain their performance advantage, or if the vanilla transformer blocks would eventually surpass them given sufficient training data. The initial gains observed might be transient, and the long-term convergence properties of the simplified blocks need further investigation.

3. The sequence length is somewhat unorthodox at only 128 - A smaller sequence length will "weaken" the ability of attention. Perhaps this could be why value projection matrices could be dropped? It is unclear how the proposed method will perform for longer sequence lengths. The reduced context window might mask potential issues with the simplified attention mechanism. The effectiveness of removing the value and projection matrices might be contingent on the limited sequence length, and it's crucial to test the method with longer sequences to ensure its robustness.

4. No downstream evaluation of the GPT model.

### Questions
1. By initializing attention $\beta$ as 1, but MLP $\beta_{FF}$ as $\frac{1}{\sqrt{L}}$, this results in the FFN blocks "contributing" $\frac{1}{\sqrt{L}}$ as much to the output as compared to the attention block, correct? If yes, Perhaps an interesting experiment could be decreasing the dimensions $4d$ of the MLP block when using the proposed SAS-P method - the motivation being that if the MLP block is not contributing as significantly, perhaps it can use fewer params. This could perhaps lead to significant speedups and parameter savings.
1. Were any downstream fine-tuning experiments conducted for GPT, like GLUE for BERT? It will help make paper stronger if downstream performance also remains similar/better. 

Minor presentation suggestions (the authors need not respond to these) - 
1. In Figure 7, some exponential smoothing should be applied to the MLM loss (or ideally, eval loss over multiple batches should so be plotted which will be hopefully much more stable.) 
1. In Figure 6 , it is difficult to distinguish the plots as many of the lines overlap/intersect significantly. Perhaps some of the lines could be omitted, or separate chart provided in supplementary.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good
