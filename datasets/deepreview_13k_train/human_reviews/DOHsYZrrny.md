# HiLoRA: High-frequency-augmented Low-Rank Adaptation

- Decision: Reject
- Scores: 6, 3, 5, 6

## Abstract
As large language models (LLMs) have demonstrated remarkable performance, parameter-efficient fine-tuning (PEFT) has emerged as an important paradigm. As a solution, low-rank adaptation (LoRA) freezes the pre-trained weights and introduces small learnable adapters instead of fine-tuning the full set of parameters. However, LoRA suffers from $\textit{catastrophic forgetting}$, where pre-trained knowledge is overwhlemed and forgotten as new information is learned. One cause of this issue is $\textit{implicit regularization}$, where deep learning models tend to favor more generalized solutions. This tendency leads to a significant increase in the largest singular values of the weights, which correspond to low-frequency components. To address this problem, we propose an advanced LoRA that balances the retention of pre-trained knowledge with the learning of new information. Since fine-tuning involves learning fine-grained details, which correspond to high-frequency information, we designed HiLoRA, a method that injects learnable high-frequency components into the pre-trained model. By leveraging the parameterized SVD and constraining singular values to appropriate levels, HiLoRA adapts to new tasks by focusing on the high-frequency domain with minimal change from the pre-trained weights. To evaluate the effectiveness of HiLoRA, we conduct extensive experiments on natural language understanding and question answering tasks. The results show that HiLoRA not only improves performance but also effectively retains pre-trained knowledge compared to baseline models.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In this paper, the authors proposed a new parameter-efficient fine-tuning (PEFT) approach with learnable high-frequency components while  constraining singular values to appropriate levels. Multiple experiments and ablation studies were conducted to show the effectiveness of the proposed method.

### Strengths
1. The motivation and formulation of the proposed HiLoRA makes sense and is technically sound to me.
2. The authors conducted extensive experiments on multiple datasets and showed improved performance over several baseline methods.
3. Ablation studies and sensitivity analysis were also conducted to show the effectiveness of the proposed approach.
4. Writing is good and easy to follow.

### Weaknesses
1. The performance improvement seems very small as shown in table 1 and 2 and sometimes even worse than baseline methods.
2. Are there any principles or rule or thumb for setting those hyper-parameters for different tasks/models?

### Questions
Overall, I think the HiLoRA proposed in this paper is novel and beneficial to the community. Please refer to the weakness section to prepare rebuttals on the performance and hyper-parameter setting.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
In this paper, the author proposes a new method to address the problem of catastrophic forgetting in LoRA fine-tuning. They suggest learning the adapter $\Delta W$ with small eigenvalues and validate their method across various downstream tasks.

### Strengths
1.	This paper describes the problem and method in detail.
2.	The authors validate the effectiveness on various downstream datasets.

### Weaknesses
1.  The definition of "frequency" in the paper is confusing and meaningless; low frequency and high frequency merely refer to the value of the eigenvalues. If the largest eigenvalue corresponds to pre-trained knowledge, why does an increase in the largest singular value during fine-tuning, as shown in Figure 1(a), lead to a decline in performance on the pre-training task? From Figure 1(a), it appears that they are either negatively correlated or unrelated.
2.  The novelty is limited. It is very similar to, including the implementation in Figure 7 and Equation (8). The only difference is that the $\Sigma$ matrix is learnable and clipped according to Equation (7). Additionally, in Table 2, HiLoRA performs worse than AdaLoRA, and the authors do not address the issue of forgetting in AdaLoRA.
3.  The motivation for investigating catastrophic forgetting in LoRA requires further explanation. When employing LoRA, my primary concern is its performance on specific downstream tasks. If I need to tackle multiple different tasks, I would prefer to use a general LLM or load various LoRA adapters through MultiLoRA.
4.  More comparisons are needed. The authors should include the results of PiSSA and MiLoRA in Table 2, and it needs to compare with methods such as DoRA, rsLoRA, and LoRA+. Furthermore, experiments should be conducted on larger LLM models, such as LLaMA.

### Questions
See Weaknesses.

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper addresses an intriguing issue—mitigating forgetting during fine-tuning of neural networks. It introduces a method focused on the fine-tuning of high-frequency components of pre-trained weights, claiming measurable improvements.

### Strengths
1.	This paper proposes a new sight for fine-tuning and tries to solve the forget problem in fine-tuning.
2.	It does reduce the accuracy loss on the pre-trained task.

### Weaknesses
1.The architecture diagrams in Figure 2 are unclear. To improve clarity, the implementation details of HiLoRA should be included in the main paper instead of relegated to the appendix.

2.The HiLoRA design lacks novelty.

3.The paper mentions, "U and V can be initialized with random r singular vectors of W0, or with U initialized to zero and V with a random Gaussian initialization." What initialization strategy was used in your experiments?

4.A deeper analysis of the relationship between the pre-trained task and the fine-tuning task in relation to the forgetting method would be beneficial. If the pre-trained and fine-tuning tasks are similar, does the forgetting problem still occur?

5.A scaling-up experiment, such as fine-tuning LLaMA-2-7B with Meta-Math and evaluating it on GSM8K, as in PiSSA, would be insightful.

6.Does this method remain effective when the rank increases?

7.Equations (6) and (7) should be introduced within Algorithm 1.

### Questions
see weaknesses

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents a method to mitigate the catastrophic forgetting of LoRA, by restricting the adaptation matrix to have singular values clamped to an upper bound.

### Strengths
* The authors tackle an important and meaningful topic that would be of interest to the community. PEFT is gaining more and more attention as the size of language models continues to grow.
* The results demonstrate that HiLoRA forgets less than LoRA, and some of its variants.

### Weaknesses
 * Line 190, authors should explain more why depth of 2 or greater results in a separation of values.
* Equation (6), line 244, I believe the shape of U should be d_1xr, Sigma should be rxr and V should be rxd2, unlike what is written.
* Tables 1 and 2 better include the model name in the table description. The two tables use a different model. 
* Table 1 shows that AdaLoRA has a lower average result than LoRA (On Roberta). However, in the original AdaLoRA paper that compared the two models on Deberta, AdaLora got better results. On other papers that compared the two on Roberta, AdaLora got better results. Are the results taken from other papers or calculated by the authors?
* Line 354, word Indicating should be with a small letter.
* Figure 4: In tables 1 and 2, authors compared 5 variants, and here only 4. AdaLoRA was omitted. The readers are interested to know the ‘forgetting’ property of AdaLoRA.

### Questions
* Equation (4), I can’t find the definition of i. Maybe it should appear as the index of the singular value on the left side, instead of n.
* Figure 4: The title says MRPC, however, in line 464 it says STS-B.

### Soundness
3

### Presentation
3

### Contribution
3
