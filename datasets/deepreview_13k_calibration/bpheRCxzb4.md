# Measuring Information in Text Explanations

- Decision: Reject
- Avg Score: 6.50
- Scores: 8, 8, 5, 5

## Abstract
Text-based explanation is a particularly promising approach in explainable AI, but the evaluation of text explanations is method-dependent. We argue that placing the explanations on an information-theoretic framework could unify the evaluations of two popular text explanation methods: rationale and natural language explanations (NLE). This framework considers the post-hoc text pipeline as a series of communication channels, which we refer to as ``explanation channels''. We quantify the information flow through these channels, thereby facilitating the assessment of explanation characteristics. We set up tools for quantifying two information scores: relevance and informativeness. We illustrate what our proposed information scores measure by comparing them against some traditional evaluation metrics. Our information-theoretic scores reveal some unique observations about the underlying mechanisms of two representative text explanations. For example, the NLEs trade-off slightly between transmitting the input-related information and the target-related information, whereas the rationales do not exhibit such a trade-off mechanism. Our work contributes to the ongoing efforts in establishing rigorous and standardized evaluation criteria in the rapidly evolving field of explainable AI.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper explores a novel, information theoretic approach for evaluating natural language explanations. Both rationale-based and natural language-based explanations are considered.  The paper speaks of an "explanan" - the "product" (as opposed to the process) that is the explanation.  The inputs and outputs of the any explanan can be reduced to a fixed dimension representation by conventional text embedding tools, to which mutual information approximations can be applied.  These are two - one input based, the "relevance"; and the other output-based, the "informativeness." 

In summary by considering these two measures as information channels, the paper finds that relevance is related to traditional measures of relevance, and informativeness is related to the explanans' reasoning.

### Strengths
Text-based explanation is a nascent field for which this paper offers a novel attempt.   The paper shows the feasibility of applying mutual information measures, noting that currently it is "still unknown whether these tools can be used to examine information scores." The paper's demonstration of the feasibility of using various approximations to mutual information in this case is novel. The use in practice of these measures for evaluation is a worthwhile contribution. The entire field of natural language model evaluation is a developing area, unlike the mature methods used in supervised machine learning that have propelled that field forward.

### Weaknesses
The conclusions are modest, and give limited insight.  Despite this the approach has promise, as it plows new ground in an area where there is limited success today.

It is not clear how the dataset - benchmark, the "silver labels" and the language models come together in the experiments. The experiments section does not describe the process  - how is evaluation applied?

### Questions
It is not clear how the dataset - benchmark, the "silver labels" and the language models come together in the experiments. The experiments section does not describe the process  - how is evaluation applied?

### Soundness
3 good

### Presentation
2 fair

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors propose a framework that considers the post-hoc text pipeline as a series of communication channels. They quantify the information flow through these channels and facilitate the assessment of explanation characteristics, quantifying two information scores: relevance and informativeness. They illustrated the proposed information score measures by comparing them against traditional evaluation metrics.

### Strengths
- the paper is original - we found only a paper with some similar concepts used in a different context
 - the authors tackle a relevant problem and propose a framework to evaluate the informativeness of text explanations. Furthermore, the framework contemplates a high degree of automation, making it feasible to deploy in production settings.
 - the authors propose measuring two key aspects of the explanations: relevance and predictive informativeness.
 - we consider the paper to be of good quality: they performed a good overview of related work, all of the claims are supported with experimental results, acknowledged limitations, and ensured the presentation is clear.

### Weaknesses
 - the structure of how experiments and results are reported can be improved. In particular, it would be helpful if the authors list the experiments performed, listing rationale behind the experiment, the procedure, aims, metrics, and other aspects of relevance.



### Questions
We consider the paper interesting and relevant. Nevertheless, we would like to point to the following improvement opportunities:
Data and Experiments
   	- We encourage the authors to restructure Section 4 and Section 5 to describe better (a) the original data they have and (b) the experimental design (rationale behind the experiment, procedure, aims, metrics, etc.). In the current manuscript, it seems most of the experimental design is described in the "Data and Materials" section, while the "Experiments" section resembles more to "Results and Evaluation".
   	- Why do the authors report Spearman and not Kendall correlation? Did they check for the Spearman correlation assumptions?Figures: 
  - Figure 4: the authors provide two plots with identical descriptions, but from the caption, they seem to refer to different concepts (one should reflect informativeness, while the second reflects rationale)?

### Soundness
3 good

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
This paper proposes to view text explanations in an information theory based framework. This paper focuses on the rationale and NLE types of text explanations for text classification (specifically the e-SNLI dataset). After formulating the investigated cases within the information theory based framework, the authors propose to measure the mutual information (1) between the input and the explanan (called relevance score) and (2) between the explanan and the target (called informativeness score), and analyze the correlation among the proposed relevance score, informativeness score, and multiple proposed silver labels. The goal of this paper, to my understanding, is to propose the relevance and informativeness scores for future explanation evaluation.

### Strengths
* The way of forming the text explanation within the information theory framework is interesting.
* The experiments have included three embedding models: RoBERTa, OpenAI, Cohere, to test the generalizability of the proposed relevance and informativeness scores, which highly depends on the used embeddings.
* The experiments have considered two often-seen types: the rationale, which is defined to include the tokenwise explanation, and the NLE, which is defined to be explaining the input-target relationship via natural language description.

### Weaknesses
 * The writing can be improved: The goal of this paper can be more clear. I was lost in the middle of the paper and wondered (1) which parts are used for evaluation and (2) what are they truly evaluating for? I could only realize the goal after reading through the whole paper and gave it a guess.
* This paper claims to unify the evaluation of rationale and natural language explanations. Unification would make me expect the proposed evaluation method can evaluate them in a good standing. However, the results turn out the proposed metrics do not have a consistent meaning for human interpretation and meanwhile there is no user study to validate this. This lack of human validation is a significant gap, especially when dealing with natural language explanations where human understanding is paramount. The paper does not provide sufficient evidence that the proposed metrics align with human judgments of explanation quality.
* From the results, the most consistent part is that the proposed relevance score I(X;E) is correlated with the type overlap ratio and embedding similarity. Nonetheless, since explanan often includes (similar) words in the input, the result is not giving new insights. The high correlation with lexical overlap and embedding similarity raises questions about the novelty and utility of the proposed relevance score. It seems that the score is primarily capturing surface-level similarity rather than deeper semantic relevance. Furthermore, the paper does not explore the potential limitations of using embedding similarity as a proxy for relevance, which could be problematic in cases where semantically relevant words are not close in embedding space.

### Questions
* Is there a reason for choosing embeddings for computing the entropy? What do the authors think about using the probability distribution to compute the entropy?
* Please add proper reference to the statistics in the paper:
  *In section 4.3: Where are the statistics for the statement “On the explanations in natural language, most inter-score correlations are low, indicating that these scores measure a diverse collection of aspects.”? The authors have pointed to Appendix A.5, but it could be better to point to Figure7. Also, I would suggest this statistics be moved to the main content.
  * In section 5.1: How do the authors compute the statistics “The reasoning category scores can explain 16% and 21% of the variance in the estimated I(Y ; E) for OpenAI and RoBERTa on NLE (18% and 19% for rationale), and no more than 15% for any other categories.”?
  * In section 5.2: The authors do not put any reference to statistics in this section. I guess the authors are referring to Figure 4, 5, and 6. I would also suggest Figures 5 and 6 be moved to the main content. To comprise the paper space, I would think that prompt templates and discussion about multimodal can be moved to appendix.
* I would suggest changing the naming of “informativeness” in the GPTScore evaluation items. This term is the same as the proposed “informativeness score I(Y;E)”, so can cause confusion.
* Why is there no “informativeness” from Table1 in Figure3’s x-axis?
* I would suggest changing the order of x-axis in Figure3 to match the order of them in Table1.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
1 poor

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a framework for evaluating textual explanations (rationale and free-text rationale).

But I still have several questions about this paper.

1. The authors use the method of mutual information to assess the information of two text explanations, which is a common and intuitive practice. My confusion lies in how the authors estimate this mutual information. As far as I understand, using InfoNCE to estimate mutual information should require training. What is the training data? What is the training process?


2. I notice that the authors have compared several mutual information estimators in the appendix, such as club, smile, InfoNCE. Here I still have questions about the club method. According to the paper of club, the value estimated by club should be higher than the real mutual information, and thus it should be higher than the value estimated by InfoNCE, how do the authors judge that the value estimated by InfoNCE is more accurate?


3. Why use V-information instead of the traditional mutual information method?

4. Does this method depend on the accuracy of the mutual information estimator? What are its advantages over other evaluation methods (e.g., traditional metrics for evaluating NLE (rouge))?

5. In summary, I think this paper has limited innovation and usefulness.

Finally, for ICLR submissions, the appendix could be placed after the main text, not separately in the supplementary material.

### Strengths
See Summary for details.

### Weaknesses
This paper presents a framework for evaluating textual explanations (rationale and free-text rationale).

But I still have several questions about this paper.

1. The authors use the method of mutual information to assess the information of two text explanations, which is a common and intuitive practice. My confusion lies in how the authors estimate this mutual information. As far as I understand, using InfoNCE to estimate mutual information should require training. What is the training data? What is the training process?


2. I notice that the authors have compared several mutual information estimators in the appendix, such as club, smile, InfoNCE. Here I still have questions about the club method. According to the paper of club, the value estimated by club should be higher than the real mutual information, and thus it should be higher than the value estimated by InfoNCE, how do the authors judge that the value estimated by InfoNCE is more accurate?


3. Why use V-information instead of the traditional mutual information method?

4. Does this method depend on the accuracy of the mutual information estimator? What are its advantages over other evaluation methods (e.g., traditional metrics for evaluating NLE (rouge))?

5. In summary, I think this paper has limited innovation and usefulness.

### Questions
See Summary for details.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
