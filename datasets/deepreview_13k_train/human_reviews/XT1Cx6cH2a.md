# DAPE V2: Process Attention Score as Feature Map for Length Extrapolation

- Decision: Reject
- Scores: 6, 5, 5

## Abstract
The attention mechanism is a fundamental component of the Transformer model, contributing to interactions among distinct tokens, in contrast to earlier feed-forward neural networks. In general, the attention scores are determined simply by the key-query products. However, this work's occasional trial (combining DAPE and NoPE) of including additional MLPs on attention scores without position encoding indicates that the classical key-query multiplication may limit the performance of Transformers. 
In this work, we conceptualize attention as a feature map and apply the convolution operator (for neighboring attention scores across different heads) to mimic the processing methods in computer vision. Specifically, \textbf{the main contribution of this paper is identifying and interpreting the Transformer length extrapolation problem as a result of the limited expressiveness of the naive query and key dot product, and we successfully translate the length extrapolation issue into a well-understood feature map processing problem.} 
The novel insight, which can be adapted to various attention-related models, reveals that the current Transformer architecture has the potential for further evolution.  Extensive experiments demonstrate that treating attention as a feature map and applying convolution as a processing method significantly enhances Transformer performance.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors propose to improve the extrapolation abilities of Transformer models beyond their training sequence length by building upon the previously introduced method of data-adaptive positional encodings (DAPE). The authors find that replacing DAPE’s standard MLP through a convolutional MLP further improves performance.

### Strengths
**Originality & Significance:**   
- The authors slightly expand on the insights of the original DAPE paper and provide new results on the original and their improved variant 

**Quality:**   
- Experiments conducted across two datasets in comparison with multiple popular ‘positional embedding’ methods, including NoPE, RoPE, CoPE, ALiBi, Kerple and FiRE
- Insights into how the computational complexity is affected are provided, as well as results for three model sizes

**Clarity:**  
- The paper is mostly easy to read; 
- Graphs and tables are clearly labeled and easy to interpret

### Weaknesses
 _TL;DR: While I appreciate the work the authors have put into the manuscript and their experiments, the main ‘methodological’ novelty facilitating the approach has already been presented in the original DAPE paper. The authors’ addition of using a convolution instead of an MLP (i.e. replacing a 1x1 conv with a 1x3 conv, combined with inconsistent improvements) combined with the manuscript in its current state is in my opinion not enough to pass the bar for ICLR;_

- Minor ‘methodological’ addition to existing DAPE, with results varying from ‘improvement’ to ‘decrease in performance’ – see questions.
- Insufficient (no) discussion of limitations, although inconsistencies can be easily seen from the presented results – see questions.
- Interpretation on an in-sight level of results obtained with different method (FIRE, ALiBi, etc.) could be significantly extended
- Minor: Quality of Manuscript in terms of wording/preciseness of statements

### Questions
**Main concerns, questions & potential improvements:**  
- Most results (in fact, almost all) are reported with for ‘Kerple’, which seems to work well (e.g. Figure 2, Figure 3, and Figure 3) in combination with DAPEv2;  
However, when looking at the ‘broader’ applicability in Figure 5, it quickly becomes clear that results across the board are much more inconsistent!   
-> e.g. ALiBi: ALiBi performs well on its own for training seq-len 128, is improved by DAPE-ALiBi – but significantly worse for DAPEv2; 
The manuscript however states that DAPE-1x3 ‘consistently improves performance’, which is incorrect and should be discussed (including insights)
- Appendix E / Section 4.8 shows results for DAPE with kernel-size 1 and 3 – I assume ‘1’ is the classic DAPE, and ‘3’ the v2?   
If so, again – results vary a lot in terms of which one is better for which task and combined with which ‘pe-method’, and I don’t see this discussed in the manuscript appropriately. 
- General: A wider discussion of the limitations would significantly help any reader/user, and I’d suggest the authors consider being upfront about these and provide the reader with helpful guidance (Similarly when using DAPEv2 with FIRE, while there is some improvement, it still ‘diverges’ quickly)

- I’d like the authors to include actual insights based on their experiences and the background knowledge of working with these different approaches (FIRE, ALiBi, Kerple, etc.) – e.g. is one generally preferable? If not, what are the situations you would recommend combining DAPEv2 with any particular one of these?
- In Figure 6, although the model can cheat, I’d be curious why the authors think that the DAPEv2-ALiBi becomes significantly less stable (than both non-cheating and original-non-cheating) 

Additional comments:
- I’d suggest the authors replace some of the references through the seminal works in their introduction in terms of how Transformers have made an impact (e.g. noting CV but not citing ViT/DeiT isn’t good research practice, as these authors should be acknowledged)
- I’d like to suggest the authors to check and potentially slightly rework the manuscript in terms of preciseness of their wording; While I am aware this might be due to language barrier, there are multiple instances where statements are misleading/confusing/too general, e.g. 
  - Abstract: ‘[…] contributing to interactions among distinct tokens, in contrast to earlier feed-forward NNs’ -> This is not really true/correct, as any FFN can establish interactions between elements of data – e.g. a CNN establishes the same over a local window in a sequence, etc.; 
  - L 49: ‘rendering the outputs non-sensical’ -> In the context of NLP, the output will still be a valid word and hence ‘sensical’, the architecture simply loses its ability to learn relationships over a sequence and reverts back to sets/bag-of-words; Also note: The authors discuss “Transformers” in general, and there actually are multiple use cases where Transformers are used on set-based problems
  - …


---
## Update post-rebuttal: 
Some of my concerns have been addressed, and I am therefore increasing my score slightly from 5 to 6 -- but it still remains a borderline case to me.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces an incremental change over the prior work DAPE (Zheng et al., 2024), by extending the MLP used in the attention to 1x3 convolution. This small change achieves improvement over multiple experiment settings.

### Strengths
- The paper is clearly written.
- Extending the MLP in DAPE’s attention model to 1x3 convolution achieves improvement over multiple experiments.

### Weaknesses
 - The major concern is this paper only introduces an incremental change over DAPE, I.e. extending the MLP in attention model to 1x3 convolution. In addition, compared to the gap between DAPE and other baselines, the gap between this paper and DAPE is relatively small.

 - This paper could be written in a more straightforward way, by directly showing the difference between it and DAPE, and highlighting why it is crucial. Readers may have confusion about the contribution of this paper and DAPE.

 - Line 126: It is hard to buy the insight: *Transformer’s length extrapolation ability is limited by the expressiveness of the naive query-key dot product.* This conclusion is drawn by showing DAPE without position encoding still achieves improvement. But there exists another explanation as follows. Transformer’s length extrapolation ability is limited due to the lack of accurate position encoding. MLP in DAPE implicitly learns the spatial information from the dot product of query and key, thus improving the performance. And extending MLP to 1x3 convolution can further improve encoding the spatial information.

 - Discussion about an important reference is missing. “On Translation Invariance in CNNs: Convolutional Layers can Exploit Absolute Spatial Location” (in CVPR 2020), by Osman Semih Kayhan and Jan C. van Gemert. It found that the boundary effects operate even far from the image boundary, allowing the network to exploit absolute spatial location all over the image. This may help explain why convolution introduces more gains.

### Questions
Please see weaknesses (especially the third one).

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
This paper extends DAPE and proposes a new approach to address the Transformer long context extrapolation problem by treating attention scores as feature maps. The authors conceptualize attention mechanisms akin to image processing techniques, utilizing convolutional operations on attention scores across different heads. This methodology, inspired by methods in computer vision, enhances Transformer performance on extrapolation tasks across multiple lengths, both in theoretical underpinnings and through empirical validation. It has outperformed some popular position embedding methods such as RoPE and NoPE.

### Strengths
+ The application of convolution on attention maps to improve relative position encoding in large language models is both novel and inspiring. The use of convolution, a fast and efficient operation, allows for seamless integration into existing frameworks.

+ The proposed method demonstrates strong performance on the length extrapolation task, outperforming established techniques such as RoPE and NoPE, which underscores its effectiveness.

### Weaknesses
 - The paper suffers from poor writing and organizational structure. Basic variables such as X, W_Q, and W_K​ are not adequately explained as the context, despite that Transformers are quite popular. Specifically, the lack of explicit definitions for these fundamental components of the Transformer architecture makes it difficult to follow the proposed method's integration. The reader is left to infer the roles of these variables, which is not ideal for a technical paper.

- Confusing Arguments: 
1) Line 181-182 states: "The result of DAPE-NoPE (the Zheng et al. (2024) only combine DAPE with ALiBi, Kerple and FIRE but not with NoPE or RoPE)." This sentence is confusing and seems disconnected from the preceding context. The statement implies a limitation of prior work without clearly establishing why this limitation is relevant to the current study. 2) Line 191-192 mentions: "potentially hindering the evolution of next-generation Transformer models," which lacks clarity and context. The argument is presented without sufficient justification, making it unclear why the current Transformer architecture is considered limiting. 3) Line 198 states: "RoPE first computes the classic attention scores of key-query multiplication with RoPE." This description is unclear and requires further elaboration. It does not specify how RoPE is incorporated into the attention score calculation, leaving the reader unsure of the exact mechanism.

- The authors fail to adequately explain the rationale and motivation for applying convolution to embed position information, abruptly transitioning to technical details without sufficient context. The connection between convolution and positional encoding is not well-established, and the reader is left wondering why this specific operation was chosen.

- The current popular solution for long-context extrapolation is to fine-tune RoPE-based LLMs on long-context data, which is not addressed in the baseline comparisons. The absence of comparisons against fine-tuned RoPE models limits the practical relevance of the proposed method. It is unclear whether the method offers any advantage over a more straightforward fine-tuning approach.

- There is no discussion of computational efficiency metrics such as FLOPS, which would be valuable for assessing the proposed method's practicality. Without this information, it is difficult to determine the feasibility of the proposed method for real-world applications.

- The benchmarks employed in the study are limited, reducing the generalizability of the findings. The exclusive use of synthetic datasets does not provide sufficient evidence that the proposed method is effective in real-world scenarios.

### Questions
Could the authors elaborate on "Proposition 1: Transformers incorporating convolution operations can perform associative recall tasks without the need for positional encoding"? The rationale behind this proposition is unclear and requires further explanation.

### Soundness
3

### Presentation
1

### Contribution
2
