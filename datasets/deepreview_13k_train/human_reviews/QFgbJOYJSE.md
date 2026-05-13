# State Space Models are Provably Comparable to Transformers in Dynamic Token Selection

- Decision: Accept
- Scores: 6, 5, 6, 6

## Abstract
Deep neural networks based on state space models (SSMs) are attracting significant attention in sequence modeling since their computational cost is significantly smaller than that of Transformers. While the capabilities of SSMs have been demonstrated through experiments in various tasks, theoretical understanding of SSMs is still limited. In particular, most theoretical studies discuss the capabilities of SSM layers without nonlinear layers, and there is a lack of discussion on their combination with nonlinear layers. In this paper, we explore the capabilities of SSMs combined with fully connected neural networks, and show that they are comparable to Transformers in extracting the essential tokens depending on the input. As concrete examples, we consider two synthetic tasks, which are challenging for a single SSM layer, and demonstrate that SSMs combined with nonlinear layers can efficiently solve these tasks.  Furthermore, we study the nonparametric regression task, and prove that the ability of SSMs is equivalent to that of Transformers in estimating functions belonging to a certain class.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper theoretically studies the expressive power of State Space Models (SSMs) and compares them with transformers. This papers consider three representative tasks in language modeling: input coping, associative recall, and non-parametric regression. For each task, this paper gives an architectural configuration on model depth, width, vocabulary size, weight norm/sparsity, etc. that can accomplish the task up to a given precision. In particular, the SSM architectures considered in this paper involve nonlinear layers, which are shown to improve the expressiveness of SSMs by enabling dynamic token selection.

### Strengths
+ The topic of this paper is both timely and important. SSMs have become increasingly popular and are widely used in many language and vision applications. Providing theoretical guarantees for these models is therefore crucial.

+ The paper is well-written, with precise and clear mathematical notations and definitions. While the claims are intricate, they are supported by comprehensive explanations and well-motivated interpretations.

+ The synthetic tasks considered in the theoretical analysis are popular yet insightful choices for analyzing language models. The results are solid and offer valuable insights into the comparative strengths of different sequence architectures. I reviewed the proofs for Theorems 3.1 and 3.2, and they appear correct.

### Weaknesses
 - The assumptions in this paper appear to deviate from practical scenarios. Specifically, the paper assumes that the convolutional filter formed by SSMs has a defined "window size," whereas in practice, this window size is often as large as the sequence length. This discrepancy limits the direct applicability of the theoretical results to real-world SSM deployments, where long-range dependencies are crucial. Additionally, it relies on a particular parameterization of SSMs (Lns 151–152) that has not been commonly adopted in real-world applications, making it difficult to assess the practical relevance of the findings.

- While the piecewise smooth function class is convenient for theoretical comparison with prior work, it would be helpful to provide more background on this assumption. In particular, the authors should relate this function class to practical scenarios, explaining how the piecewise gamma-smooth function class aligns with real-world applications. The lack of connection to real-world data distributions makes it challenging to interpret the practical implications of the theoretical results.

- The results in the paper seem more pertinent to understanding how combining convolution and nonlinear MLPs can perform synthetic sequence tasks while being not closely and directly related to the SSM models. The analysis focuses on a specific architecture combining SSMs with FNNs, which makes it unclear whether the observed performance gains are due to the SSM component itself or the overall architecture. This makes it difficult to isolate the specific contributions of SSMs.

- The paper's proof techniques and settings closely resemble those in [1]. It remains unclear how SSMs differ from transformers in solving comparable tasks with similar complexity. Furthermore, Lemma 5.1 seems disconnected from the proofs of earlier results, failing to elucidate the underlying mechanism that distinguishes SSMs from transformers. The lack of clear differentiation from existing work diminishes the novelty and impact of the paper.

- A minor point: the analysis highlights a potential technical contribution, suggesting that nonlinear layers play an essential role in SSMs. This claim would be more convincing if supported by empirical evidence.

### Questions
1. In HiPPO theory [1], the authors demonstrate that certain parameterizations of A, B, C in SSMs can guarantee long-range modeling capabilities. Do the authors see any connection between the proposed parameterization (Lines 151–152) and the HiPPO framework, or similar properties in modeling long-range dependencies?

2. This paper focuses on input-independent SSMs. However, as shown in [2], data-dependent convolution can significantly enhance associative recall performance. Do the authors believe that the use of multi-layer SSMs with nonlinearity is sufficient to compensate this performance gap?

3. The proofs of Theorems 1 and 2 appear to follow a similar structure. Does this imply that the underlying network construction could be shared between the two results?

[1] HiPPO: Recurrent Memory with Optimal Polynomial Projections

[2] Zoology: Measuring and Improving Recall in Efficient Language Models

### Soundness
4

### Presentation
4

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper provides a theoretical investigation into the capabilities of State Space Models (SSMs) compared to Transformers in their ability to dynamically extract tokens based on the input. The authors prove that SSMs combined with Feedforward Neural Network (FNN) layers can achieve performance comparable to Transformers in three cases: input copying, associative recall, and nonparametric regression.

### Strengths
- The paper establishes a rigorous theoretical foundation, demonstrating that SSMs combined with FNNs can emulate the dynamic token selection mechanism of Transformers. This theoretical analysis bridges a gap in understanding the potential of SSMs in sequence modeling.

- The paper evaluates the proposed method across multiple tasks—input copying, associative recall, and nonparametric regression—showing that SSMs can achieve performance on par with Transformers.

### Weaknesses
 - The paper is challenging to read due to dense technical details. It would be helpful if the authors could include a figure or remark after each theorem to illustrate the reasoning and provide an intuitive explanation.

- The input-independent SSMs used in this paper are somewhat outdated, given recent developments in selective SSMs (e.g., Mamba) and their variants. Additionally, the authors compare a combination of SSM and FNN with only the self-attention component of Transformers. This comparison may not be entirely fair, as the strength of a Transformer block lies in the combination of self-attention and FNN layers.

- A deeper comparison of the results presented here with those in [A] is necessary. In fact, the authors of [A] consider a more general version of selective SSMs, called Generalized State Space Models (GSSMs), which includes SSMs with FNN as a subclass. The results in [A] show that GSSMs do not outperform Transformers on tasks such as input copying, whereas the current paper suggests a different perspective.

### Questions
- Could the authors clarify the differences between the results in this paper and those presented in [A] (see weaknesses)?

- Could the authors discuss the difficulty of generalizing these results to selective SSMs?

- In Line 405, could the authors explain the origin of the expression inside the big-O notation?

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
3

### Summary
This paper explores the performance comparison between state space models and transformers in dynamic token selection. The study shows that the ability of SSMs combined with  FNNs to extract key tokens is comparable to that of transformers.

### Strengths
- The article presents a novel perspective by demonstrating that the combination of SSMs with nonlinear layers can simulate the dynamic token selection mechanism of transformers.
- It provides a detailed theoretical proof with a rigorous mathematical derivation process.
- The proposed theory is validated through experimental results.

### Weaknesses
 - There is a lack of relevant experiments to validate the theoretical effectiveness, with the only experiments conducted on DNA base sequences. More experiments in settings such as LLMs are needed.
- The integration of SSMs and FNNs may increase the model's complexity, which could impact training and inference times. Specifically, the introduction of FNNs before and after the SSM layer, while potentially enabling dynamic token selection, adds parameters and computational overhead that might not be justified by the performance gains, especially when considering the potential for increased training time and memory consumption.
- Although the article compares SSMs with transformers, it does not discuss comparisons with other sequence models, such as RNNs or LSTM. This omission is significant because RNNs and LSTMs have established performance characteristics and computational trade-offs, and a comparison would provide a more comprehensive understanding of the relative strengths and weaknesses of the proposed approach.

### Questions
- Are there additional experimental results, for instance, would applying the improvements to Mamba enhance model performance?
- Are there any ablation study results demonstrating the effectiveness of adding FFNs?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work presents a theoretical investigation into the capabilities of State Space Models (SSMs) for dynamic token selection. While previous research has established that standalone SSM layers exhibit inferior performance compared to Transformers, the authors demonstrate that SSMs combined with Fully-connected Neural Networks (FNNs) achieve comparable capabilities in dynamic token selection. The theoretical contributions are substantiated through rigorous mathematical analyses across three fundamental scenarios: input copying, associative recall, and non-parametric regression.

### Strengths
1. **The paper is well-motivated:** while prior theoretical works focus on standalone SSM layers and their limitations compared to Transformers, the authors insightfully observe that practical architectures combine SSMs with FNN layers and raise the important question in [page 2, line 77].
2. **Theoretical rigor:** The paper presents a rigorous theoretical analysis to demonstrate their claims, grounded in well-established mathematical foundations with detailed proofs.

### Weaknesses
1. **Lack of empirical validation:** The paper lacks sufficient experimental evidence for its theoretical claims. As the paper did not discuss whether SSMs can be optimized efficiently (limitation section), there are serious concerns whether SSMs can actually demonstrate comparable dynamic token selection capability to Transformers in practical scenarios, or at least in synthetic tasks which they studied theoretically (input copying, associative recall). Specifically, the theoretical analysis does not address the practical challenges of training SSMs, such as vanishing gradients or instability, which could prevent the theoretical capabilities from being realized in practice. The absence of experiments leaves open the question of whether the theoretical parameter counts translate to actual performance gains.

2. **Imbalanced analysis of scenarios:** Among the three scenarios (input copying, associative recall, and non-parametric regression) studied in this paper, the paper allocates excessive attention to non-parametric regression, which is less central to the paper's primary contribution - SSMs' dynamic token selection capabilities. A more concise treatment of non-parametric regression would have allowed for deeper analysis of the more fundamental scenarios. The non-parametric regression analysis, while mathematically rigorous, seems tangential to the core argument about dynamic token selection, and its inclusion detracts from a more focused exploration of the primary claims.

3. **Unjustified choice of non-parametric regression:** The choice of non-parametric regression as a case study for demonstrating the dynamic token selection capabilities of SSMs requires further justification. This analysis appears loosely related to the paper's main contribution and occupies a disproportionate amount of space. While valuable, it would be more suitable as a separate study. The authors should either better justify this choice or focus on more relevant scenarios that directly showcase dynamic token selection capabilities of SSMs. The connection between piecewise smooth functions and dynamic token selection is not clearly established, and it is not obvious how this analysis contributes to the understanding of SSMs' ability to select relevant tokens in sequence processing tasks.

4. It seems that the problem setting of this paper (Section 2, Appendix A) for theoretical analysis overlooks the structural constraints of the state matrix A (e.g., diagonal or other structured forms) that enable efficient SSM training, which was one of the key points for the practical success of SSMs. While prior work [1] analyzing generalized SSMs without structural constraints was suitable for claiming SSM limitations, this paper's goal of establishing SSM-Transformer comparability requires considering these practical aspects. Consequently, without incorporating the structural constraints, the theoretical claims may not translate to implementable architectures in practice. The analysis should consider the impact of these structural constraints on the parameter efficiency and training dynamics of SSMs.

5. The theoretical foundation appears inconsistent: while the paper references the theoretical results from [1] which analyzes a single SSM layer [page 2, line 84], the current analysis assumes two SSM layers with additional FNN layers [page 5, line 222] (please correct me if I'm wrong). As the superior performance of (multi-layer) SSM+FNN over (single-layer) standalone SSM is self-evident (adding layers naturally increases modeling capacity), the current theoretical analysis alone offers limited practical insights. The paper would benefit from extended theoretical analyses in terms of architectural design choices, such as comparing SSM, SSM+FNN, and Transformer architectures under equal parameter budgets. Furthermore, an examination of optimal parameter allocation between SSM and FNN components under fixed budgets would be valuable.

### Questions
1. This paper theoretically compares input copying capabilities against [1] and associative recall capabilities against [2]. However, unlike [1] and [2] which provide comprehensive experimental validations, this paper lacks empirical results. To substantiate the theoretical findings, the authors should provide **experimental results** comparing the performance of (i) SSM, (ii) SSM+FNN, and (iii) Transformer on both input copying and associative recall tasks.
2. **The choice of non-parametric regression** as a case study for demonstrating the dynamic token selection capabilities of SSMs **requires further justification.** This analysis appears loosely related to the paper's main contribution and occupies a disproportionate amount of space. While valuable, it would be more suitable as a separate study. The authors should either better justify this choice or focus on more relevant scenarios that directly showcase dynamic token selection capabilities of SSMs.
    * Instead of non-parametric regression, the paper would benefit from extending its theoretical analysis to the synthetic tasks introduced in Mamba [3] - a seminal work that has become one of the most representative studies in the SSM literature. Specifically, its **selective copying** and **induction heads** tasks align with input copying and associative recall capabilities, respectively. Including these analyses would strengthen the connection between the paper's theoretical framework and contemporary SSM research.
3. It seems that the problem setting of this paper (Section 2, Appendix A) for theoretical analysis **overlooks the structural constraints of the state matrix A** (e.g., diagonal or other structured forms) that enable efficient SSM training, which was one of the key points for the practical success of SSMs. While prior work [1] analyzing generalized SSMs without structural constraints was suitable for claiming SSM limitations, this paper's goal of establishing SSM-Transformer comparability requires considering these practical aspects. Consequently, without incorporating the structural constraints, the theoretical claims may not translate to implementable architectures in practice. Please correct me if I'm wrong.
4. The theoretical foundation appears inconsistent: while the paper references the theoretical results from [1] which analyzes a single SSM layer [page 2, line 84], the current analysis assumes two SSM layers with additional FNN layers [page 5, line 222] (please correct me if I'm wrong). As the superior performance of (multi-layer) SSM+FNN over (single-layer) standalone SSM is self-evident (adding layers naturally increases modeling capacity), the current theoretical analysis alone offers limited practical insights. The paper would benefit from **extended theoretical analyses in terms of architectural design choices,** such as comparing SSM, SSM+FNN, and Transformer architectures under equal parameter budgets. Furthermore, an examination of optimal parameter allocation between SSM and FNN components under fixed budgets would be valuable.

  
  

[1] Repeat after me: Transformers are better than state space models at copying  
[2] Laughing hyena distillery: Extracting compact recurrences from convolutions  
[3] Mamba: Linear-Time Sequence Modeling with Selective State Spaces

### Soundness
3

### Presentation
2

### Contribution
2
