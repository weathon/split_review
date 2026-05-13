# lpNTK: Better Generalisation with Less Data via Sample Interaction During Learning

- Decision: Accept
- Scores: 6, 6, 8

## Abstract
Although much research has been done on proposing new models or loss functions to improve the generalisation of artificial neural networks (ANNs), less attention has been directed to the impact of the training data on generalisation.
In this work, we start from approximating the interaction between samples, i.e. how learning one sample would modify the model's prediction on other samples.
Through analysing the terms involved in weight updates in supervised learning, we find that labels influence the interaction between samples.
Therefore, we propose the labelled pseudo Neural Tangent Kernel (lpNTK) which takes label information into consideration when measuring the interactions between samples.
We first prove that lpNTK asymptotically converges to the empirical neural tangent kernel in terms of the Frobenius norm under certain assumptions.
Secondly, we illustrate how lpNTK helps to understand learning phenomena identified in previous work, specifically the learning difficulty of samples and forgetting events during learning.
Moreover, we also show that using lpNTK to identify and remove poisoning training samples does not hurt the generalisation performance of ANNs.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposed to incorporate label information into the Neural Tangent Kernel (NTK) and designed a kernel called lpNTK to study the interaction between training examples. The author suggested classifying the relationships between a pair of examples into three types --- interchangeable, unrelated, and contradictory --- based on the angles between the vectors represented in lpNTK. The author then used these concepts to analyze some phenomena and techniques of learning dynamics, such as learning difficulty, forgetting, pruning, and redundancy. The observations and analyses were supported by experiments on the MNIST and CIFAR10 datasets.

### Strengths
Disclaimer: I'm not very familiar with the literature and some technical details of NTK. I might be biased because other reviews are visible to me before I write mine.

- The learning dynamics and learning difficulty is an important problem in many subfields of machine learning. The author provided nice theoretical tools for it based on NTK.
- Incorporating label information is useful for analyzing many supervised learning tasks in a more fine-grained way. The use case of data pruning is reasonable and convincing. I believe that the proposed tools can be used to deepen our understanding of some methods for learning from noisy/imbalanced data.
- This paper is well structured. The author raised intuitive hypotheses, asked clear questions, and then conducted reasonable experiments to verify them.
- The author contextualized this paper well and discussed related work sufficiently.

### Weaknesses
 - Maybe it's because I'm unfamiliar with the literature, but I feel that this paper can benefit from mathematically clearer definitions of some terms such as interaction and learning difficulty.
- The author stated that "contradictory samples are rare in practice" but didn't explain why. I suspect that it's because the MNIST and CIFAR10 datasets used in experiments are relatively clean, and there are few ambiguous training examples. The conjectures in C.3 were nice, but I would expect more solid explanations or explorations. The lack of exploration into the causes of contradictory samples limits the practical implications of the work, as it's unclear when the proposed analysis would be most relevant.
- The author did not discuss much about the limitations of this work. Specifically, the computational cost of calculating the lpNTK, which scales quadratically with the number of samples and the square of the parameter dimension, is a significant practical limitation that should be addressed. Furthermore, the assumption that the model's behavior can be well approximated by NTK theory is not always valid, and the paper should discuss the potential impact of this assumption on the results.

Minor issues:
- Section 2.1: the abbreviation $\mathbf{z} \in \mathbb{R}^K$ is misleading because I think $\mathbf{z}$ is a $\mathbb{R}^K$-valued function, not just a vector.
- Rigorously, a simplex with $K$ values is $(K-1)$-dimensional, i.e., it should be $\Delta^{K-1}$.
- Since many methods for noisy label learning and selective prediction (classification with rejection) heuristically make use of the learning dynamics, it would be convincing to apply lpNTK to those applications. However, those can be future work directions.

### Questions
- It is not completely clear to me why it is reasonable to fix the similarity matrix $\mathbf{K}$. Isn't it that a pair of training examples can be similar or dissimilar during different stages of training? How can we obtain the model that performs the best on the validation set in applications like data pruning?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper enhances the Neural Tangent Kernel by integrating label information, which offers a more nuanced understanding of the interaction between samples compared to the existing eNTK method. The authors explore the relationship between lpNTK and eNTK, and use vector angles to classify samples into interchangeable, unrelated, and contradictory categories. This novel categorization facilitates a 'data-centric' improvement in model training. The idea is interesting, but there lack baselines to validate their proposed method.

### Strengths
1. The integration of label information into the Neural Tangent Kernel (NTK) represents a novel approach that enhances the characterization of sample interactions during optimization. And the sign approximation also makes sense.  
2. The application of the proposed lpNTK is both reasonable and beneficial. It effectively validates the utility of lpNTK's mapping functions (vectors), demonstrating their practical effectiveness.

### Weaknesses
I have the following concerns:
1. Concerning Theorem 1, the authors assert that 'the gap between lpNTK and eNTK will not be significantly different.' However, this seems contradictory to subsequent analysis and empirical studies presented. The paper's central theme appears to be the integration of label information for a more nuanced understanding of sample relationships. If the lpNTK kernel closely resembles the original eNTK, could the authors clarify how this supports the stated claim? Specifically, the theorem should clarify the nature of the 'not significantly different' claim, and how it relates to the practical utility of the proposed lpNTK. A more precise bound or analysis would be beneficial, perhaps discussing the conditions under which the difference becomes practically relevant.
2. The categorization of samples into three groups mirrors the 'data-IQ' framework in Seedat et al. (2022), which also segments samples into easy, ambiguous, and hard categories. Data-IQ assesses prediction error and confidence throughout the training process, a concept seemingly echoed in this paper. I recommend that the authors draw comparisons with this methodology to highlight distinct aspects and contributions of their work. It would be helpful to clarify how the proposed method differs from Data-IQ in terms of the underlying mechanisms and the types of insights each approach can provide. For example, does lpNTK offer a more direct measure of sample interaction, while Data-IQ focuses on individual sample difficulty based on learning dynamics?
3. There lack baselines to validate the effectiveness of the proposed method for measuring sample similarity. For instance, the influence function is a known technique for understanding relationships between samples during training. A comparison with such established methods would provide a more robust validation of the proposed approach. It is crucial to demonstrate that lpNTK provides unique insights beyond what existing techniques like influence functions can offer. This comparison should include an analysis of the computational cost and the type of information each method provides, such as the sensitivity of model predictions to individual training samples.
4. It would be beneficial if the authors could include a computational complexity analysis of the lpNTK. This information would be crucial for understanding the practicality and scalability of the proposed method in different settings. The analysis should consider the dependence on the number of samples, the dimensionality of the data, and the number of parameters in the model. Such analysis would help to understand the limitations of the proposed method in terms of computational resources and applicability to large datasets.

### Questions
Please refer to Weaknesses.

### Soundness
2 fair

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper aims to study the interaction between samples in supervised learning from a learning dynamics viewpoint. To that end, the authors propose a the labeled pseudo Neural Tangent Kernel (lpNTK), a new adaptation of the NTK which explicitly incorporates label information into the kernel. First, lpNTK is shown to asymptotically converge to the empirical Neural Tangent Kernel (eNTK). Then, the authors demonstrate how lpNTK helps to understand phenomena such as identifying and interpreting easy/hard examples and forgetting events. Finally, the paper shows a case study in which lpNTK is used to improve the generalization performance of neural nets in image classification via pruning and de-biasing.

### Strengths
- The paper's main conceptual contribution of incorporating label information into the NTK is novel and interesting!
- The connection to sample difficulty and forgetting events is an interesting use-case for the lpNTK and allows us to connect sample difficulty with training dynamics.
- I found it pretty interesting that lpNTK allows for pruning and simultaneous utility improvements. This could open up another connection to selective prediction (learning a high-confidence subset of the distribution).
- Related work appears sufficiently discussed.

### Weaknesses
 - Should Eq (1) contain the sign operator wrapped around the last factor? In Section 2.2, it is stated that the paper does not use the whole error term but only the sign as shown in Eq (2). I am also not sure I was able to follow the explanation as to why the magnitudes should not matter. Could the magnitude be useful for ranking, especially in early training stages where error magnitudes are likely more diverse?
- Although Figure 2 and the displayed evolution of distinct FPC clusters is insightful, I was wondering whether additional visualizations of the lpNTK would have been possible? For instance, could the authors visualize the kernel matrix itself or some of its spectral properties over the course of training? This might reveal more about the dynamics of the kernel's evolution.
- The results in Table 1 showing the forgetting events don't seem particularly impressive (especially on MNIST). Am I missing something here? The reported accuracy gains seem marginal, and it's unclear if the lpNTK is providing a substantial advantage over simpler methods for identifying forgetting events.
- It would have been great if the authors had provided a visualization of some of the pruned samples. Are there any patterns present in pruned examples in particular? Are these samples consistently noisy, ambiguous, or otherwise difficult to classify? Examining the characteristics of these pruned samples could strengthen the paper's analysis.
- It is evident that the authors tried really hard to fit the paper into the page limit. There are formatting artifacts in terms of very little vspace throughout the paper, especially towards the end of the paper (pages 7-9). I would strongly encourage the authors to reduce dangling words instead of resorting to these very evident formatting tricks.

### Questions
- Have the authors considered drawing connections between interchangeable and contradictory samples and forging / machine unlearning [1], i.e. by training on a specific point we could plausibly say that we have also optimized for another datapoint? 

Other questions embedded in Weaknesses above.

I am willing to increase my score as part of the discussion phase if the authors can address my concerns.

References:

[1] Thudi, Anvith, et al. "On the necessity of auditable algorithmic definitions for machine unlearning." 31st USENIX Security Symposium (USENIX Security 22). 2022.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
