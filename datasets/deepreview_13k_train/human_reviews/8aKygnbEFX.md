# Hybrid Fine-Tuning of LLMs: Theoretical Insights on Generalized Smoothness and Convergence

- Decision: Reject
- Scores: 3, 5, 5, 3

## Abstract
Applying either Parameter-Efficient Fine-Tuning (PEFT) or full fine-tuning to Large Language Models (LLMs) often results in its inherent limitations.  To overcome this issue, we propose a novel "hybrid fine-tuning" approach that jointly updates both  LLMs and PEFT modules  using a combination of zeroth-order and first-order optimization methods. To analyze this approach, we develop a theoretical framework centered on the concept of "hybrid generalized smoothness", which accounts for the heterogeneous nature of the optimization landscape in joint LLM and PEFT training. We provide a rigorous convergence analysis for the convergence of SGD algorithm under multiple learning rates and demonstrate its effectiveness through extensive empirical studies across various downstream tasks and model architectures. Our work not only offers a solution to the practical challenge of LLM fine-tuning but also contributes a broader theoretical foundation for analyzing hybrid optimization problems in machine learning.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper proposes to combine a zero-order method with a parameter-efficient fine-tuning technique for LLM fine-tuning. Experiments test the effectiveness. The paper is not well written.  There is no technical and theoretical contributions.


----
I appreciate the authors' response, but the paper still requires further conciseness and the necessary experiments. I raise my score, but currently, the paper cannot reach the threshold of ICLR.

### Strengths
- Combining a zero-order method with a parameter-efficient fine-tuning technique for LLM fine-tuning is a feasible approach.

- The convergence of the proposed method is discussed in this paper.

- This paper test the effectiveness of the proposed method on small datasets.

### Weaknesses
 - The paper lacks technical contributions. The paper combines a zero-order method with a parameter-efficient fine-tuning technique for LLM fine-tuning. However, it provides no specific details on how to integrate the network weight updates from both approaches and lacks analysis or testing. For example, one obtains $\Delta W_1$ and $\Delta W_2$ to update the network weight $W$ by the zero-order method and a parameter-efficient fine-tuning method, respectively. How to update $W$ with $\Delta W_1$ and $\Delta W_2$ in the end? The only distinction made is that each approach uses a different learning rate, which does not enhance the hybrid methodology.

- The paper fails to offer theoretical contributions, as most lemmas and theorems are derivable from (Li et al., 2024). The paper does not clarify why its proofs and conclusions cannot be directly applied for theoretical analysis or what challenges arise from its application. There is no theoretical contribution if only the processes of proofs are slightly different.

Haochuan Li, Jian Qian, Yi Tian, Alexander Rakhlin, and Ali Jadbabaie. Convex and non-convex
optimization under generalized smoothness. Advances in Neural Information Processing Systems,
36, 2024.

- Additionally, the experiments are weak. The experimental setup, comparison methods, and discussion of results indicate inadequate training of the authors in scientific research. It is a reasonable choice to directly repeat the experiments in MeZO.

### Questions
- This paper proposes a hybrid approach combining zero-order full parameter fine-tuning with first-order parameter-efficient fine-tuning. So the comparison of memory and wall-clock time is very important. However, it lacks experimental verification and discussion.

- The experiments lack strength, and the datasets are limited in size and quantity. Given that MeZO's experimental setup is utilized, it would be beneficial to fellow its experiments.

- It should give the results of the first-order methods SGD or Adam as references.

- The methods in Table 1 do not align with those discussed in the experimental details. Please either cite the relevant papers in Table 1 or include the corresponding methods in the experimental details subsection.

- The statement above Eq. (2) is incorrect. The equations of one-side and two-side gradient estimators are different and cannot be expressed by one equation.

- The zero-order optimizer used in all experiments needs to be explained. The first-order optimizer used in parameter-efficient fine-tuning also needs to be explained.

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
Applying either Parameter-Efficient Fine-Tuning (PEFT) or full fine-tuning to Large Language Models (LLMs) often results in its inherent limitations. To overcome this issue, this paper proposes a novel "hybrid fine-tuning" approach that jointly updates both LLMs and PEFT modules using a combination of zeroth-order and first-order optimization methods.

### Strengths
Applying either Parameter-Efficient Fine-Tuning (PEFT) or full fine-tuning to Large Language Models (LLMs) often results in its inherent limitations. To overcome this issue, this paper proposes a novel "hybrid fine-tuning" approach that jointly updates both LLMs and PEFT modules using a combination of zeroth-order and first-order optimization methods.

### Weaknesses
The combination of PEFT and full fine-tuning seems to be a trivial trick.
The core of this paper is using zeroth-order algorithm to achieve full fine-tuning and Adam to PEFT.
Though this is an effective method, this combination seems so trivial.

### Questions
No

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work introduces a hybrid fine-tuning paradigm, a novel approach that addresses the limitations of both full fine-tuning and traditional parameter-efficient fine-tuning (PEFT) methods. By integrating zero-order optimization for large language models (LLMs) with first-order optimization for PEFT modules, this method achieves an effective balance between adaptability and computational efficiency.

### Strengths
The novel hybrid generalized smoothing concept expands classical optimization theory to account for the heterogeneous dynamics of joint training between large language models (LLMs) and parameter-efficient fine-tuning (PEFT) methods. This approach is versatile, applicable to hybrid fine-tuning, layer-wise fine-tuning, and models incorporating trainable external modules.

### Weaknesses
My primary concern lies with the performance of the proposed method. In the experiments, it does not significantly surpass the baseline methods. Additionally, beyond the vanilla zeroth-order SGD, other advanced zeroth-order methods are available, as discussed in [1]. I suggest that the authors incorporate these alternative methods as baselines to further validate the effectiveness of their approach.

### Questions
1. Why is it not feasible to train each module sequentially with distinct learning rates? Are there any specific benefits to mixing them within the same training phase?
2. In the second part of Figure 3 in Appendix D.2, why does the accuracy rate of hybrid tuning show a decreasing trend over time steps?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a hybrid fine-tuning approach, that combines regular LLM fine-tuning and PEFT. The proposed method uses first order methods to tune the peft modules, and uses zero-th order methods to tune original parameters. The authors derive convergence rate of the proposed method under the hybrid generalized smoothness assumptions. Empirical results are provided to validate the proposed method.

### Strengths
1. The paper is well written and easy to follow. 
2. The authors provide convergence analysis as well as empirical results of the proposed algorithm. 
3. The observation on learning rate size is interesting to me.

### Weaknesses
1. Lack of novelty. The proposed hybrid fine-tuning seems to be a direct combination of zeroth-order algorithms and PEFT algorithms. It is basically running this two algorithms at the same time. The only difference is to use different learning rate for different part of parameters, which seems not novel enough for me, since it is a commonly known fact and well accepted practice that PEFT algorithms requires larger learning rate compared with full parameter fine-tuning. I can provide some references if necessary.

2. The theoretical contribution is not significant. Though this paper spends a lot of work to derive convergence guarantees for the proposed algorithm, the algorithm is actually a variant of SGD with zero-th order noise, with different learning rate for different coordinates, whose convergence guarantee is not fundamentally different from what is well studied in the zero-th order optimization literature. The proposed hybrid generalized smoothness is just a fine-grained version of regular smoothness, by treating different coordinates separately, which I do not think introduces paradigm shift compared with regular smoothness. 

3. The empirical results are insufficient. The experiments are conducted on three small scaled downsampled dataset. These datasets are too easy for the pretrained models that have billions of parameters that are used in the experiments. I think the current results are not sufficient to demonstrate the superiority of the proposed algorithm.

### Questions
1. What is the point of random shuffling in Algorithm one?

2. Do you also record the memory and computation cost of the hybrid method. It will be interesting to see these results beyond just accuracy comparison.

### Soundness
2

### Presentation
3

### Contribution
1
