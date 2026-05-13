# Benign or Not-Benign Overfitting in Token Selection of Attention Mechanism

- Decision: Reject
- Scores: 6, 5, 5, 8, 5

## Abstract
Modern over-parameterized neural networks can be trained to fit the training data perfectly while still maintaining a high generalization performance.
This ``benign overfitting'' phenomenon has been studied in a surge of recent theoretical work; however, most of these studies have been limited to linear models or two-layer neural networks.
In this work, we analyze benign overfitting in the token selection mechanism of the attention architecture, which characterizes the success of transformer models. 
We first show the existence of a benign overfitting solution and explain its mechanism in the attention architecture.
Next, we discuss whether the model converges to such a solution, raising the difficulties specific to the attention architecture.
We then present benign overfitting cases and not-benign overfitting cases by conditioning different scenarios based on the behavior of attention probabilities during training. 
To the best of our knowledge, this is the first study to characterize benign overfitting for the attention mechanism.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
Authors investigate "benign overfitting" (where model generalizes as well as overfit the training data) for attention architecture. Benign overfitting has not yet been defined for transformers, so the authors take a first step by studying it in the context of token selection. They theoretically prove its existence and studies different training trajectories when it can happen.

### Strengths
- Novelty: Authors are first to study it for transformer models.
- Contributions seems to be rigorously proved.

### Weaknesses
 - Paper is challenging to follow.

Scope/Practicality of the paper seems limited as:
- Papers made various assumptions both while formulating the problem (like tokens being splitting nicely into three groups) and while defining the data. 
- Only synthetic data has been used.

### Questions
1. Please justify the use of synthetic data.
2. Does real data also adhere to the various assumptions made?

### Soundness
3

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
3

### Summary
This paper presents theoretical analysis of benign overfitting in transformer attention mechanisms, examining how these models can perfectly fit noisy training data while maintaining generalization capability. Authors have maintained that it is the first work to analyze benign overfitting in the attention mechanism of transformer models. Based on a set of assumptions, the work provides theoretical guarantee for token selection behavior and characterizes conditions for benign versus harmful overfitting. While the paper makes a novel theoretical contribution to understanding attention mechanisms, several critical limitations make it difficult to comprehend the full significance of this work. The highly simplified setting, strong assumptions, and lack of real-world validation raise concerns about the practical relevance of the findings. Here’s what this reviewer feels about the proposed method

### Strengths
Originality:
First theoretical analysis of benign overfitting in attention mechanisms and unique analysis of token selection behavior and how attention handles noisy labels. Several setting build on existing benign overfitting analysis frameworks

Significance: 
Good theoretical insights into transformer attention behavior but limited practical impact due to simplified setting and need for strong assumptions. Results may not translate to real-world applications and missing key transformer applications (e.g., next token prediction, multi-head attention)

Summary of Strengths:
1.	Novel theoretical contribution to understanding attention mechanisms 
2.	Clear mathematical analysis and proofs 
3.	Well-structured validation of theoretical findings 
4.	Potential implications for prompt-tuning applications based classification

### Weaknesses
1.	The proposed method has been implemented in a oversimplified setting with single-layer attention and binary classification through single prompt-tuning. Hence, it is difficult to give verdict that the method can be a general tool for understanding benign overfitting in transformers’ attention mechanism setting. The use of a single-layer attention mechanism, without considering multi-head attention or the complexities of deeper transformer architectures, limits the scope of the analysis. Furthermore, the binary classification task with a single prompt-tuning method does not capture the nuances of more complex tasks such as sequence generation or multi-class classification, which are common in real-world applications of transformers.
2.	Some assumptions in the paper seems very strong or unrealistic, for example, in the data distribution, a constant ratio of relevant tokens and weakly-relevant tokens in an input sequence is assumed, with experiment done on single relevant and irrelevant token in a sequence assumed. This may certainly differ in a real data distribution. The assumption of a constant ratio of relevant to weakly-relevant tokens, and the experimental setup using only single relevant and irrelevant tokens, is a significant simplification that does not reflect the variability and complexity of real-world data. This assumption limits the applicability of the theoretical results to scenarios where the distribution of relevant tokens is more complex and dynamic.
3.	Limited empirical validation on the proposed theories with only small synthetic data. The applicability of the proposed method is also unclear and there is not enough discussion on the scalability. The lack of empirical validation on real-world datasets and the reliance on small synthetic datasets raises concerns about the practical relevance of the findings. The paper does not adequately address how the proposed method would scale to larger datasets or more complex tasks, which is crucial for assessing its practical utility.
4.	This paper is a first step of understanding benign overfitting on attention mechanism, however, it is not clear from reading the paper the real motivation, applicability or significance of the analysis and understanding of benign overfitting in transformer attention mechanism. This should be addressed in the writing.

### Questions
Please refer to the weakness section.

### Soundness
3

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
This work studies benign overfitting and harmful overfitting in the token selection mechanism of the attention architecture. The theoretical analysis first shows the existence of the attention mechanism and then provides the convergence analysis. Conditions on benign and harmful overfitting are characterized theoretically.

### Strengths
1. The problem to solve is interesting and significant.

2. The provided theoretical analysis makes sense and seems solid.

### Weaknesses
1. The presentation is not satisfactory. 
i) In Introduction (line 52), it says Theorem 4.1 explains the mechanism in the token selection of attention architecture. However, I cannot find any related discussion around Theorem 4.1. ii) Assumptions A3-A6 can be presented as conditions needed in the theory instead of assumptions. iii) Section 4.3 mentions some challenges, but does not mention how this paper addresses them.

2. Equations 11 and 13 are indirect, which makes the results weak. Meanwhile, it seems it cannot be associated with Figures 3 (a) and (b) about $d$ and $|\mu||$. One way to improve is to further interpret Equations 11 and 13 in terms of $|\mu||$ and $d$.

3. No experiments on real-world datasets are conducted. 

4. Only $p$ is optimized, while other parameters are not changed, which makes the problem to solve less challenging.

### Questions
The legend in Figure 3 is confusing. There are five different lines but with the same name "irrelevant". Figure 3(a) shows that $W\_{-Y^*}$ is the largest in the attention weights, which seems contradictory to the sentence in lines 483-484.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper investigates the phenomenon of benign overfitting within the attention mechanism, marking the first study to do so. Specifically, the authors demonstrate the existence of benign overfitting solutions under certain conditions. They establish that both signal learning and noise memorization are essential for benign overfitting in token selection. Furthermore, they illustrate that benign overfitting can be achieved through gradient descent, given specific conditions. Theoretical findings are supported by experimental results.

### Strengths
1) The first work to perform theoretical analysis of benign overfitting in the attention mechanism.
2) The paper is well written.
3) Theoretical findings are supported empirically.

### Weaknesses
1) N/A

### Questions
1) Any practical takeaways from the analysis of the benign overfitting phenomenon for transformer-based models (especially about their training)?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper provides a theoretical understanding of the benign overfitting phenomenon within the framework of training Transformers. It demonstrates the existence of benign overfitting in the Transformer architecture and characterizes the conditions under which a gradient descent-based approach can converge to this benign overfitting regime, supported by theoretical guarantees.

### Strengths
Overall, this paper is well-written. (1) The motivation and problem formulations are clearly articulated. (2) The discussion of related works is thorough and supports the claim that this paper is the first to study benign overfitting in the context of the attention mechanism. (3) The theoretical results are reasonable and intuitive, with sufficient explanations and a detailed description of the assumptions.

### Weaknesses
The primary weakness lies in the assumption of a favorable initialization of \( v \) (as indicated in Lemma 3.1). I assume that the scenario in Lemma 3.1 simplifies to a fully connected neural network when \( p=0 \). Consequently, the results of Lemma 3.1 could be seen as a straightforward extension of existing findings. However, it is essential to clarify the conditions under which Lemma 3.1 holds. Specifically, it is unclear how the linear classifier \( \nu \) is initialized to align with the class signal, and what assumptions are made about the data distribution to ensure this alignment. Furthermore, the paper does not address the practical implications of this initialization, especially in scenarios where such a precise alignment is not achievable.

Additionally, if we assume such an effective initialization, it appears that this model performs sufficiently well even without the attention mechanism, which raises questions about the necessity of analyzing the attention mechanism. The paper does not adequately address the scenario where the attention mechanism does not contribute to improved performance, and it would be beneficial to see a comparative analysis of the model with and without the attention mechanism under similar conditions.

Furthermore, I did not find any results concerning \( W \), representing \( W_Q W_k \) in the attention layer. The paper focuses solely on the training dynamics of \( p \) while neglecting the training dynamics of \( W \), which is a critical component of the attention mechanism. The lack of analysis on \( W \) limits the scope of the theoretical results and raises questions about the completeness of the analysis. Finally, the training approach differs from standard Transformer training practices, as this paper requires \( W_v \) to be fixed from the start. The author should verify whether this approach is effective in real applications or if the insights are transferrable to practical scenarios. The paper lacks a discussion on the practical limitations of this fixed \( W_v \) approach and how it might affect the applicability of the theoretical results.

### Questions
N/A

### Soundness
3

### Presentation
3

### Contribution
2
