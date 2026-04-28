# Learning Label Distribution with Subtasks

- Decision: Reject
- Avg Score: 4.75
- Scores: 5, 5, 6, 3

## Abstract
Label distribution learning (LDL) is a novel learning paradigm that emulates label polysemy by assigning label distributions over the label space. However, recent LDL work seems to exhibit a notable contradiction: 1) some existing LDL methods employ auxiliary tasks to enhance performance, which narrows their focus to specific domains, thereby lacking generalization capability; 2) conversely, LDL methods without auxiliary tasks rely on losses tailored solely to label distributions of the primary task, lacking additional supervised information to guide the learning process. In this paper, we propose $\mathcal{S}$-LDL, a novel and minimalist solution that partitions the label distribution of the primary task into subtask label distributions, i.e., a form of pseudo-supervised information, to reconcile the above contradiction. $\mathcal{S}$-LDL encompasses two key aspects: 1) an algorithm capable of generating subtasks without any extra knowledge, with subtasks deemed valid and reconstructable via our analysis; and 2) a plug-and-play framework seamlessly compatible with existing LDL methods, and even adaptable to derivative tasks of LDL. Experiments demonstrate that $\mathcal{S}$-LDL is effective and efficient. To the best of our knowledge, this represents the first endeavor to address LDL via subtasks. The code will soon be available on GitHub to facilitate reproducible research.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a novel Label Distribution Learning (LDL) framework called S-LDL, which solves the problem of label ambiguity by constructing subtasks. S-LDL generates pseudo-supervised information by dividing the label distribution of the main task into subtask label distributions, to enhance the model's generalization ability and ability to utilize additional data. This method does not require additional domain knowledge, can seamlessly integrate with existing LDL methods, and is suitable for LDL-derived tasks.

### Strengths
1.This paper proposes a new learning paradigm that enhances LDL by constructing subtasks, an innovative approach that can improve the model's understanding of label distribution.
2.S-LDL does not rely on specific domain knowledge, giving it good generalization ability and allowing it to be applied across different domains.

### Weaknesses
1.Although S-LDL reduces reliance on additional training data through the construction of subtasks, the generation and optimization of subtasks may increase the computational burden, especially on large-scale datasets. The paper does not provide a detailed analysis of the computational overhead associated with subtask generation and optimization, making it difficult to assess the practical scalability of the approach. For instance, the time complexity of the subtask generation process should be explicitly stated with respect to the number of data points and the dimensionality of the label space. Furthermore, the optimization process for each subtask may require significant resources, especially if the subtasks are complex or numerous.
2.The performance of S-LDL may be sensitive to parameter selection, such as the number and weight of subtasks, which may require additional adjustments and validation. The paper lacks a systematic study on the impact of these parameters on the overall performance of S-LDL. For example, the optimal number of subtasks might vary significantly depending on the dataset characteristics, and the method for determining the weights of each subtask is not clearly justified. Without a comprehensive sensitivity analysis, it is difficult to determine the robustness of the proposed approach.
3.Although this paper proposes the S-LDL framework, there are some shortcomings in theoretical analysis, especially in the in-depth exploration of the rationality and optimality of subtask construction. The paper does not provide a formal proof or theoretical justification for why the proposed subtask construction method is optimal or even effective. There is no discussion of the conditions under which the subtask label distributions can accurately reconstruct the original label distribution, and no analysis of the potential for error accumulation during the subtask generation process.

### Questions
please see the weaknesses above.

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
4

### Summary
This paper proposes S-LDL, which partitions the label distribution of the primary task into subtask label distributions, i.e., a form of pseudo-supervised information, to solve existing problems in LDL.  This paper also conducts several experiments to demonstrate that S-LDL is effective and efficient.

### Strengths
1. This work is the first one endeavoring to address LDL via subtasks.
2. This work conducts abundant experiment to show the effectiveness of S-LDL.

### Weaknesses
1. There is room for improvement in the structure and content organization of this paper.Expanding the fifth chapter to more clearly elaborate on deep S-LDL could be beneficial. The analysis about subtask construction in the fourth chapter does not seem to serve its intended purpose, and the reasons for this view will be detailed below.
2. The two definitions introduced in Section 4.1, "Validity Analysis," are not formally utilized, and the relevant analysis is conducted solely through experiments, which makes it appear somewhat lacking in rigor. Specifically, the definitions of information rate and mask valid rate are presented, but they do not directly contribute to any theoretical results or proofs. The analysis relies entirely on empirical observations, which weakens the theoretical foundation of the proposed method.
3. The proof in Section 4.2, "Reconstructability Analysis," seems to yield a distribution that meets the “sum to one” condition, but I do not fully understand why this distribution must necessarily be the original distribution. The proof shows that the reconstructed distribution sums to one, but it does not demonstrate the uniqueness of the solution or why this specific reconstruction is the only possible outcome. This lack of clarity undermines the claim that the subtask distributions can accurately recover the original label distribution.

### Questions
The concept of deep regime S-LDL appears to be quite similar to Error-Correcting Output Codes (ECOC). I would like to know if the subtasks can only be applied within LDL, or if they can be utilized in other contexts as well?

### Soundness
2

### Presentation
2

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
The authors proposed a new methodology called S-LDL for label distribution learning problems. The algorithm first constructs subtasks without any extra knowledge and proposes a plug-and-play method framework based on the pseudo-supervised information from subtasks. Experiments demonstrate that S-LDL is effective and efficient.

### Strengths
The authors propose a novel method for LDL by partitioning the primary task into multiple subtasks. This method needs no additional auxiliary tasks and provides different views of the primary task distribution, rendering the mixture of distributions more traceable. Moreover, they propose a new aggregation method to be seamlessly compatible with existing LDL methods, and adaptable to derivative tasks of LDL.

### Weaknesses
1. Lack of theoretical explanation concerning the proposed subtask construction method.

2. Lack of experiments showing that the S-LDL method is a better learning paradigm than other ensemble methods based on subtasks when both methods use the same subtask construction method. 

3. Section 5 " S-LDL OF THE DEEP REGIME" is not very well-written. It should be clarified which variables are obtained by subtask construction and which variables are learned by minimizing Equ. (9).

4. The motivation of Eq. (1) is still not well explained in the paper. The two terms in Eq. (1) need clearer illustration. For example, a theoretical analysis of the resulting subtasks under extreme values of $\lambda$ such as $\lambda \to 0$ and $\lambda \to \infty$ would be beneficial for demonstration.

5. The choice of $\lambda = 0.2$ is not well justified. From Figure 1(a), the optimal value of $\lambda$ seems closer to $0.1$.

6. The authors introduce the definition of information rate and mask valid rate but no theoretical results are established concerning them.

### Questions
1. Can you provide some insights or explanation about Equ.(1)? Why minimizing Equ.(1) can yield diverse subtasks? Is Equ.(1) related to some existing pairwise similarity metrics or is it proposed by yourselves? 

2. Could you show the superiority of minimizing Equ. (1) to learn the subtasks over other methods to partition the label space empirically and/or theoretically? In experiments, can you conduct an ablation experiment to compare your Equ. (1) with existing subtask construction methods (e.g., random sampling label space)? 

3. Could you compare your method with other subtask-based ensemble methods when both use the same subtask construction method (I.e. minimizing Equ. (1))?  

4. If I understand correctly, you train $\phi$, $\psi$, and $\omega$ simultaneously. If I did not, how did you train $\phi$ guided by subtasks separately?

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
This paper studies the label distribution problem. This paper argues that the recent LDL work seems to exhibit a notable contradiction: 1) some existing LDL methods employ auxiliary tasks to enhance performance, which narrows their focus to specific domains, thereby lacking generalization capability; 2) conversely, LDL methods without auxiliary tasks rely on losses tailored solely to label distributions of the primary task, lacking additional supervised information to guide the learning process. This paper proposes to solve the contradiction by subtasks.

### Strengths
The idea of using subtasks in LDL seems to be a novel strategy.

### Weaknesses
The representation of this paper is weak. First, this paper does not clearly illustrate the auxiliary task and subtask. Without a clear definition, it isn't easy to get the core idea of this paper. Specifically, the distinction between an 'auxiliary task' and a 'subtask' remains unclear. It's not evident how a subtask differs from a standard auxiliary task, or why it is uniquely suited to address the limitations of existing LDL methods. Second, this paper does not explain why the auxiliary tasks will not address the first key issue: satisfying the non-negative and sum-to-one constraints. To my knowledge, those two constraints can easily be satisfied. Just name a few. For instance, a simple softmax layer can ensure these constraints. The paper needs to articulate why existing methods for enforcing these constraints are insufficient and why the proposed subtask approach offers an advantage beyond simply satisfying these constraints. Those unclear representations render it difficult for the reviewer to understand the core idea of this paper.

The experimental comparison is weak, as most compared methods were published several years ago.

### Questions
See the weakness.

### Soundness
2

### Presentation
1

### Contribution
2
