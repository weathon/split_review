# Towards Understanding Memory buffer based Continual Learning

- Decision: Reject
- Scores: 3, 3, 3, 6

## Abstract
Continual learning (CL) is a paradigm that adapts to and retains knowledge from a stream of tasks. Despite the growing number of experimental methods in CL, there is a lack of rigorous theoretical analysis, particularly in memory-based continual learning (MCL), which remains an open research area. In this paper, we theoretically analyze the impact of memory in CL and derive explicit expressions for expected forgetting and generalization errors under overparameterized linear models. We propose a detailed matrix decomposition of the data to distinguish between current and previous datasets, effectively decoupling the coupled data for different tasks. Additionally, we conduct a comprehensive mathematical analysis for scenarios with a small number of tasks and employ numerical analysis for larger task scenarios to evaluate the overall properties of expected forgetting and generalization errors. Compared with CL, our theoretical analysis suggests that (1) a larger memory buffer must be paired with a larger model to effectively reduce forgetting; (2) training with a larger memory buffer generalizes better when tasks are similar but may perform worse when tasks are dissimilar, while training with a large model can help mitigate this negative effect. Ultimately, our findings here sheds new light on how memory can assist CL in mitigating catastrophic forgetting and improving generalization.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
The paper seeks to theoretically analyze the impact of memory on continual learning in overparameterized linear models. To do this, the paper starts from error terms for forgetting and generalization defined in the ICML 2023 paper by Lin et al. for continual learning without a memory buffer. The present paper then extends these error terms for continual learning methods that use one of two memory buffers: 1) a buffer created using reservoir sampling (a partial rehearsal buffer) or 2) a buffer that stores all previous samples (a full rehearsal buffer).
The paper claims that these error terms lead to three conclusions:
1) “A larger memory buffer must be paired with a larger model to reduce forgetting effectively”;
2) “A sufficiently large model can lead to zero forgetting”;
3) “A larger memory buffer may improve generalization when tasks are highly similar but can degrade generalization when tasks are highly dissimilar.”

### Strengths
**Originality:** Theoretically analyzing the error bounds for forgetting and generalization in continual learning (overparameterized linear) models that use a memory buffer is novel. To the best of my knowledge, there do not currently exist any studies that examine this problem. The most related work is the ICML 2023 paper by Lin et al.

**Significance:** It is useful to study these error bounds for continual learning models that use memory buffers since this has become a predominant strategy for mitigating catastrophic forgetting in experimental works in the field. Theoretical bounds pave the way for a better understanding of experimental findings in the field. Although the error bounds are only derived for overparameterized linear models, future work could explore these bounds for other models like deep neural networks or non-linear models more broadly.

**Quality & Clarity:** While providing theoretical error bounds for the forgetting and generalization of memory-based continual learning methods is useful, the paper is lacking clarity and is difficult to follow. For example, there are several design choices that do not have clear justifications and the mathematical notation is inconsistent, which is expanded upon in the “Weaknesses” section below.

### Weaknesses
My biggest issue with the paper is the lack of clarity, which makes it difficult to evaluate the correctness and impact of the presented results. I will expand on several points related to this next.

- It is unclear what the meaning of a “task” is in the paper. The data vectors are said to be sampled from Normal(0,1), but then what is changing from one task to another? This is important for understanding the results. Moreover, the notion of “task similarity” is mentioned several times, including in the concluding findings from the theoretical analysis. However, “task similarity” is never mathematically defined. Are we assuming some bound on the difference between two matrices as their “similarity”? If so, this is not mentioned anywhere in the paper and remains unclear.

- The paper could benefit from more consistent mathematical notation. For example, in Section 3.1, W_T is defined as the set of linear ground truth vectors of all T tasks, but then the vectors of W_T are used to produce the output y=X^T w_t. However, y appears to be a prediction, not a ground truth, so this is unclear. Moreover, in Section 3.2.1, it is stated that “the memory buffer stores m_{t-1} samples” and also that we have “\hat{m}_{t-1}” tasks. The inconsistency of variables makes the math extremely difficult to follow. These are just a few examples.

- Another benefit could come from plain English explanations of theoretical results. The Remarks in the paper are useful for understanding the theoretical results, however, they are written in terms of math and it is unclear what their implications are for the study. These plain English explanations could help the reader better understand the lemmas, theorems, and remarks in the context of the broader continual learning field.

- There are several justifications for design choices missing. For example, there is an assumption that the number of samples for each task is equal (Assumption 1). Is this just to simplify notation? How do we know these results will hold for the more general case when each task does not contain the same number of samples? In Section 3.2.1, it is stated that “When t \geq 2, the memory buffer stores m_{t-1} samples for each of the previous t-1 tasks and 1 sample for each of the \hat{m}_{t-1} distinct tasks from the previous t-1 tasks.” Does this mean the buffer only stores 1 sample per task? If so, this is a very strong assumption and it is unclear why this was chosen.

In the study by Lin et al., there were empirical results with deep neural networks that demonstrated similar findings to the theoretical analyses performed for the overparameterized linear model. This was powerful to demonstrate that their theoretical results might hold for more complex models (like non-linear neural networks). It would be helpful to see a similar type of experimental analysis in the present paper to strengthen the theoretical findings.

### Questions
1. How is a “task” being mathematically defined? Why was this specific definition chosen?
2. How is “task similarity” being defined? Why was this specific definition chosen?
3. It would be helpful to see experimental results similar to those with a deep neural network from Lin et al. to enhance the theoretical findings in the present paper.
4. It would be helpful to have plain English explanations of the “Remarks” throughout the paper to better understand the findings.
5. It would be helpful to have more context about the study from Lin et al. so that the reader does not have to read excerpts from Lin et al.’s paper to understand the present paper.
6. In the Introduction, it is mentioned that the challenges for the present study consist of “the coupling of the data matrix and label vector”. What exactly does this mean?
7. What exactly was the setup used to produce the plots in Figure 1? Were Gaussians sampled multiple times to create different “tasks” and then the results averaged for the plots?

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper provides a theoretical investigation of replay based CL where each task is an overparameterized linear regression task, under two different scenarios, i.e., reservior sampling and a full replay where all previous data are stored. By deriving explicit forms of expected forgetting and generalization errors, the authors analyze the impact of memory size and model size on forgetting and generalization error, under the coupling with task similarity.

### Strengths
1. The theory for replayed based CL is very limited, and this paper provides the first explicit forms of forgetting and generalization error for two replay strategies.

2. Analysis are provided to understand the impact of memory.

### Weaknesses
1. No experimental studies are provided to justify the theoretical results. In particular, it is not clear if similar phenomenons can be observed in practice with neural networks and real datasets, which challenges the usefulness and importance of the theoretical results in this paper. And it is not clear how the theoretical results can help in practice.

2. It is not convincing that analyzing the full replay case is important here, as this replay strategy is barely used in practice.

3. The presentation needs to be improved. For example, it is not clear what the distinct tasks are in line 172. Figure 1 also needs to be more clear. The last sentence in Remark 6 also seems questionable, as these two figures are talking about generalization error instead of forgetting.

4. In section 4.1, the claims about the impact of memory size on forgetting are made only based on $F_2^2$, which seems not very rigorous. The reason is that, when changing the memory, from Theorem 1, most time the coefficient of $F_2^1$ will also change. And unlink the second that depends on task similarity, this first term cannot be very small.

5. It is not clear how the correlation between the replay samples and the model is handled. Specifically, the data stored in the replay buffer for task $t-1$ has already been used to train $w_{t-1}$. When this data is used to update the model at task $t$, the model $w$ should be corrected with $\hat{D}_t$. This sample-model correlation is a key challenge in analyzing replay-based CL, and it's not clear how this is addressed in the paper.

### Questions
Besides the weakness above, I have some further questions:

1. In the replay buffer, why not put samples for the same old task together? This may be convenient for analysis, but seems not standard.

2. How did you handle the correlation between the replay samples and the model? For example, data stored in the replay buffer for task $t-1$ have already been seen during the training of $w_{t-1}$. When using this data to update the model at task $t$, the model $w$ should be corrected with $\hat{D}_t$. Address this challenge is important to analyze replay-based CL, but I didn't see how this was particularly addressed in the paper.

3. In section 4.1, the claims about the impact of memory size on forgetting are made only based on $F_2^2$, which seems not very rigorous. The reason is that, when changing the memory, from Theorem 1, most time the coefficient of $F_2^1$ will also change. And unlink the second that depends on task similarity, this first term cannot be very small.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a theoretical analysis of memory-based over-parameterized linear continual learners. More specifically, the authors explicitly express the forgetting and generalization errosr when training a linear model with a MSE and memory mechanism. The authors derive various relation between memory size, dimension of the input and overall forgetting and generalization. Based on this analysis, the authors make various claim regarding the choice of model and memory size to minimize forgetting and maximum generalization.

### Strengths
- The motivation of proposing a theoretical framework to give a deeper understanding of memory-based methods is appreciated
- Some limitations have been rightfully addressed

### Weaknesses
# Weaknesses
- The introduction is very hard to read and introduces many undefined variables such as $T, s,  M_{max}, d$. The introduced challenges l.48 are unclear; therefore, the context introduction of this theoretical analysis is extremely confusing. I would advise the authors to give a more intuitive understanding of such challenges (i) and (ii). The bullet point contributions at the end of the introduction are appreciated.
- In 3.1, I do not understand the definition of the ground truth vectors $w_i$. Ground truth vectors should be $y_t$ but here they are vectors $w_i$ multiplied to the input to give the ground truth. I imagine that what the authors actually mean is that $w_i$ is the linear learned classifier? However, in that case $y_t$ is the prediction, not the ground truth. The notion of a 'ground truth vector' $w_i$ is particularly confusing, as it is not a directly observable quantity, but rather a parameter that defines the relationship between the input and the output. This should be clarified.
- The definition of reservoir sampling is confusing. Traditionally, the probability of selecting a sample to be put in memory is $\frac{|M|}{k}$ with $|M|$ the memory size and $k$ the stream index. Therefore when the authors write l166 "the probability of any example from the previous $t − 1$ tasks being in the buffer is equal", it does not correspond to reservoir sampling. The probability of being selected decreases over time.
- In 3.1 the diag operator is not defined
- According to 3.1, $X_t^T w_t^*$ is a scalar, however, in equation (1) it is multiplied by $M_{M_{max}}^l$ and the output is a scalar. How is that? Same remark for eq (2)
- Table 1 is never used in the text
- in 3.3, I believe the assumption corresponds to the features. Therefore, each element of $\hat{X}_t$ follows an isotropic Gaussian of mean 0 and variance 1. In that sense, each element of future tasks follows the exact same distribution as previous tasks, but the label is different. This seems unrealistic as in Continual Learning the distribution very likely changes over time from one task to the other. The assumption of identical feature distributions across tasks is a significant limitation, as it does not reflect the reality of most continual learning scenarios where task distributions shift over time. This assumption needs to be explicitly acknowledged and its impact discussed.
- I believe the authors consider a classification problem, however the training loss in (3) is most certainly more suited for a regression problem. The authors should also discuss the limitation of studying only one specific loss function. The choice of MSE loss is not justified, especially if the problem is indeed classification. The limitations of this choice should be discussed in detail, including how the analysis might change with other loss functions such as cross-entropy.
- In Theorem (1) the authors assume that $d > s + M_{max} +2$. But the value of $M_{max}$ can be very large
- $d$ is sometimes the dimension of the input (section 3.1), sometimes the number of parameters (Table 1). Even if a larger dimension implies more parameters, it would be more interesting to study the impact of over-parameterization, which does not seem to be the case in this paper. The inconsistent use of $d$ makes the analysis difficult to follow. It is crucial to clearly define whether $d$ refers to the input dimension, the parameter dimension, or both, and to maintain this definition consistently throughout the paper. The paper does not explore the impact of overparameterization in a meaningful way.
- How much is the overparameterized assumption important here? Could the same analysis apply otherwise? I believe this analysis makes a lot of sense when fine-tuning linear layers of pre-trained models, however this parallel is lacking in the current writing of the paper.
- An experimental validation of the proposed analysis seems necessary to me given the large amount of assumptions made throughout the entire paper.

# Typos
- l.149 lacks the dimension of $x_t$
- In Assumption 1, it should be $t \in [1, T]$

### Questions
See weaknesses

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper investigates the effect of memory buffer for linear models in continual learning. It considers two memory buffer settings, and theoretically derives the forgetting and generalization errors under linear models. Based on the theoretical results, the paper argues that a memory buffer can reduces forgetting and improves generalization under certain conditions, while may have the opposite effect under specific model size, task similarity and other factors.

### Strengths
1. Analyze the effect of memory buffers in continual learning is an interesting and important problem. 
2. Theoretically shows how the memory buffer size effects forgetting and generalization is clear. Meanwhile, analyzing simple cases like $T=2$ helps readers easily understand the relations among them. 
3. The paper is well structured.

### Weaknesses
1. The paper is not self-contained. The authors should introduce important previous works like [1], for instance, in the appendix or the main paper.  
2. For full rehearsal memory buffer setting, the optimization problem is same as the joint (multi-task) training. This is because in the last task $T$, the model is trained on all data and the problem is convex. The paper should discuss the relation between the results in Section 4.2 and joint training.
3. The paper should define "similarity" between tasks formally, which I believe is related to $||w_j^*-w_i^*||_2$. However, in **Remark 1**, it is unclear why the following statement holds true:
> ... This suggests that with a smaller memory buffer or a larger number of parameters, the model forgets less than without memory when all tasks are highly similar.
4. The connection between theories and memory selection is unclear. The paper only discusses one memory selection method: reservoir sampling-based memory buffer, which limits the generalization of findings to other settings.
5. In Section 3.2, why the memory buffer does not store the labels, and the labels are generated instead. Meanwhile, it is not clear why for reservoir sampling-based memory buffer, the labels are generated by Eq. (1).
6. The paper should have a notation table to sum up all the notations. It is hard to follow the paper since many notations are similar.
7. It is not clear where does the paper get the following conclusion, as stated in the abstract:
> ...  (1) a larger memory buffer must be paired with a larger model to effectively reduce forgetting;

### Questions
1. In Section 3.2, why the memory buffer does not store the labels, and the labels are generated instead. Meanwhile, it is not clear why for reservoir sampling-based memory buffer, the labels are generated by Eq. (1).
2. The paper should have a notation table to sum up all the notations. It is hard to follow the paper since many notations are similar. 
3. It is not clear where does the paper get the following conclusion, as stated in the abstract:
> ...  (1) a larger memory buffer must be paired with a larger model to effectively reduce forgetting;

### Soundness
3

### Presentation
2

### Contribution
3
