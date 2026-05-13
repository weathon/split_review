# What Does It Mean to Be a Transformer? Insights from a Theoretical Hessian Analysis

- Decision: Accept
- Scores: 6, 8, 5, 8, 8

## Abstract
The Transformer architecture has inarguably revolutionized deep learning, overtaking classical architectures like multi-layer perceptrons (MLPs) and convolutional neural networks (CNNs). At its core, the attention block differs in form and functionality from most other architectural components in deep learning--to the extent that Transformers are often accompanied by adaptive optimizers, layer normalization, learning rate warmup, and more, in comparison to MLPs/CNNs. The root causes behind these outward manifestations, and the precise mechanisms that govern them, remain poorly understood. In this work, we bridge this gap by providing a fundamental understanding of \textit{what distinguishes the Transformer from the other architectures --- grounded in a theoretical comparison of the (loss) Hessian.} Concretely, for a single self-attention layer, \textbf{(a)} we first entirely derive the Transformer's Hessian and express it in matrix derivatives; \textbf{(b) }we then characterize it in terms of data, weight, and attention moment dependencies; and \textbf{(c)} while doing so further highlight the important structural differences to the Hessian of classical networks. 
Our results suggest that various common architectural and optimization choices in Transformers can be traced back to their highly non-linear dependencies on the data and weight matrices, which vary heterogeneously across parameters. Ultimately, our findings provide a deeper understanding of the Transformer’s unique optimization landscape and the challenges it poses.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper derives and analyzes the Hessian matrix of a single Transformer self-attention layer. It examines how the Hessian depends on the data, the weights, and the attention mechanism's internal moments. The Hessian is found to be highly non-linear and varies significantly across different parts of the self-attention layer. This variation is caused by the way data enters the attention mechanism as keys, queries, and values. It is also due to the softmax function and how the attention mechanism's query and key components are parameterized. These factors create complex relationships between the data, weights, and the Hessian. The authors believe this analysis helps explain why Transformers have a unique optimization landscape. They also suggest it explains why certain architectural choices, such as using adaptive optimizers and layer normalization, are beneficial for training Transformers.

### Strengths
- This paper tackles an important theoretical question regarding the dynamics of Transformers by directly analyzing the Hessian. 
- A thorough theoretical derivation and analysis like this is novel and provides a valuable new perspective. 
- The categorization of Hessian dependencies offers a structured framework for understanding the complex interactions within the architecture.
- The derivations appear sound and are presented with sufficient detail. 
- The exploration of how different Transformer components impact the Hessian adds depth and rigor to the study.
- The paper is well written and is generally a pleasure to read. The authors incorporate the existing literature nicely. While the Hessian structure is inherently complex, the authors have made a good effort to explain the key takeaways in an accessible way.

### Weaknesses
 - The paper analyses only single layer, without saying much about multi-layer.
- A lot of important aspects are not addressed, e.g. multi-layer, role of residual connection in the Hessian, multi-head attention. Additionally, can you comment on the implications of (W_V) often being a low-rank matrix with rank (d_k)?
- The paper doesn't have a solid narrative and rather presents a reader with a bag of tricks. See some of the examples in the Question section below. It also makes claims that are not justified, e.g. that it can help  explaining the performance gap between Adam and SGD in lines 516-519.
- To strengthen the paper's narrative, the author should have started with the analysis of the gradient before delving into the Hessian, since it is much simpler. Comparing and contrasting the properties of the gradient and Hessian could provide a more comprehensive understanding.

### Questions
- In Figure 3, several plots show a mismatch between the predicted and observed Hessian scaling. The top right plot in Figure 3a doesn't display a prediction at all. Could the authors elaborate on these discrepancies?
- Some analysis is presented more like a log book without explaining why is it important. For example, what are the key takeaways from Figure 4? More broadly, could the authors clarify the overarching message and how the different analyses contribute to it?
- The paper claims to provide a Hessian-based perspective on the performance gap between Adam and SGD, referencing Ahn et al. (2023). However, this explanation isn't explicitly provided in the paper. Could the authors elaborate on this point and clarify how their analysis explains this performance gap?

### Soundness
4

### Presentation
4

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper compares the self-attention Hessian to classical networks such as CNN to better understand the unique optimization landscape  of self-attention based transformer architectures. The paper provides a understanding self-attention from hessian perspective, which is an interesting line to understand the inner workings of transformers. The empirical experiments on digit addition task validates the theoretical observations by considering CE loss.

### Strengths
1. The paper makes an attempt to understand self-attention based models using hessian analysis. This allows authors to compare transformers with architectures such as CNN.

2. The empirical evidence on digit addition task framed as next token prediction task validates the theoretical observations.

### Weaknesses
1.  The paper is not well written and is difficult to follow.

2. Authors should clearly state how their observations leads to better understanding of self-attention. It will also be beneficial for the readers if author mentions the consequences of their observations, such does it lead to better interpretability, or sparse attention or stable training.

3. In section 4.2 author discuss alternative to standard query-key parameterization and discusses change in loss landscape when single matrix W_{QK} is used instead of W_{Q}W_{K}^{\top}. Authors should discuss it briefly about how this change effects the overall performance in transformers, does it even make any difference in terms of overall performance for specific task or does it have any effect on interpretability of self-attention.

### Questions
Please answer the questions mentioned in previous section.

### Soundness
3

### Presentation
2

### Contribution
4

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper derived the expression of the Hessian of one self-attention layer and discussed how the special structure of Hessian makes transformer special.

### Strengths
- This paper provides a detailed expression of the Hessian of self-attention, which might be useful for the community for the theoretical understanding of Transformers.
- The presentation is good. I especially appreciate that the authors write different symbols in different colors.

### Weaknesses
 - Except the expression of the Hessian, I don't see any deep and detailed analysis in this paper. For example, the authors claim that understanding the structure of Hessian can help understand the optimization of Transformers, such as why Transformers have to be trained by Adam(W). However, I don't see any detailed discussion on this point in the paper. I would like to see a deeper discussion showing that how the stucture of Hessian derived in this paper connects to real Transformer behaviours.
- This whole analysis is based on a single-layer self-attention. it is unclear how this analysis (or the conclusions drawn from this one-layer model) can possibly extend to deeper models.

### Questions
See Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This work derives the Hessian of Transformers to analyze the data dependence of different components in attention and to compare Transformers with other classical models.

### Strengths
$\bullet$ The derivation of the Hessian of Transformers provides a new framework of analyzing the dynamics of different components of self-attention.

$\bullet$ The discovery of the data dependencies among key, query, and value matrices is fundamental for future works, both in theoretical understanding and practical applications.

### Weaknesses
1. The omission of the $\textbf{F}$–functional Hessian blocks ($\delta_{XY}$) weakens the overall results, as the influence of $\delta_{XY}$ on the Hessian remains unclear, and there is no detailed discussion about its role. Specifically, the paper does not explore how the magnitude of $\delta_{XY}$ relative to other terms in the Hessian affects the overall data dependence analysis. If $\delta_{XY}$ contains significant data dependencies, neglecting it could lead to an incomplete understanding of the Hessian's behavior.

2. The analysis is focused on a single self-attention layer and does not extend directly to more complex and practical Transformer architectures. The results are insightful but could benefit from further extensions to deeper, more realistic Transformer models. The paper lacks a discussion on how the derived Hessian properties propagate through multiple layers, and how the interplay between different attention layers might affect the overall Hessian structure. This limits the applicability of the findings to real-world scenarios where Transformers are typically composed of multiple layers.

3. There is no empirical comparison between Transformers and MLPs/CNNs. Including such empirical comparisons would make the findings more compelling and straightforward to interpret. Without a direct comparison, it's difficult to assess whether the observed data dependencies are unique to Transformers or are also present in other architectures. This comparison is crucial to highlight the specific advantages or disadvantages of Transformers in terms of data dependence.

### Questions
1. How do you justify the omission of $\delta_{XY}$ in Equation (5)? If the elements of $\delta_{XY}$ are significantly larger than those of $X$, wouldn't the dependency on $X$ in Equation (5) become trivial?

2. Could you clarify the experimental settings used for Figure 4? You mentioned that Softmax significantly reduces the magnitude of the query Hessian block entries, but this effect isn't very apparent in Figure 4.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper is interested in deriving the full expression of the Hessian for a single self-attention layer, wrt the learned matrix parameters of query, key and values. The hessian is decomposed into two terms, the outer product and functional hessians, and their expressions are respectively given in Theorems 3.1 and 3.2. Then, the paper analyzes the dependence on the data and how different components of the architecture affect the hessian, such as the softmax activation or the position of the layer normalization.

### Strengths
- **Originality**: To my knowledge, this is the first paper deriving the full expression of the hessian for the self-attention operation.
- **Significance**: As mentioned in the conclusion of the paper, this work can serve as foundation for better understanding the role of the self attention operation in Transformers. As discussed and shown throughout the paper, the self attention layer has a singular behavior compared to better-understood convolutional or feed-forward layers in neural networks.   
- **Quality**: Although I did not check all the proofs in details, a lot of work has been put to derive Theorems 3.1 and 3.2. The experiments presented in Figure 3 also validates to some extent the theoretical results obtained, in terms of dependence to the training data of two of the diagonal terms.
- **Clarity**: I appreciated the color-coding of the terms within equations throughout the paper. It makes the reading and understanding of the results easier.

### Weaknesses
 - **Clarity**: The links between the empirical results shown in the various figures and the insights derived from the expressions of the Hessian are not always clear. For instance, the experiments and what is plotted in Figure 1 are never described.  Specifically, it is unclear how the histograms in Figure 1a relate to the theoretical derivations, and what the x-axis represents. Similarly, the full Hessian visualization in Figure 1b lacks context regarding the color scale and the specific matrix blocks being visualized. The lack of clarity in the experimental setup makes it difficult to assess the validity of the claims.
- **Quality**: It is difficult to evaluate the validity of all theoretical insights derived from the hessian since the settings of the experiments are not always described. More specifically, settings behind experiments to obtain Figure 1, Figure 3 and Figure 4. For example, the specific architecture used (e.g., number of layers, hidden dimensions), the optimization algorithm, and the loss function are not specified. This lack of detail makes it challenging to reproduce the results and verify the theoretical claims. Furthermore, the choice of dataset and its characteristics are not mentioned, which is crucial for understanding the behavior of the Hessian.


### Questions
- I would be interested in having more details about the settings of the experiments leading to the figures shown in the paper, more precisely for Figure 1 and Figure 4, and the dashed lines in Figure 3. What is exactly plotted ? What kind of data were used to obtain these ? How does it confirm the insights derived from the theoretical derivations ?
- In Figure 3b, what does "the dashed lines correspond to the trend estimated from the data points by the linear regression coefficient" mean ? Can the authors describe the setting behind this experiment and how the dashed lines are obtained ?
- In Figure 3, all the trends in dashed lines are linear, even though the order of the dependence is changing. This makes me think that the range of values considered for $\sigma$ is too small to clearly evaluate whether the empirical dependence are following the theoretical ones. Can the authors discuss that, and if possible, show results with a bigger range of values for $\sigma$ ?

### Soundness
3

### Presentation
3

### Contribution
3
