# LoRA Dropout as a Sparsity Regularizer for Overfitting Reduction

- Decision: Reject
- Scores: 6, 3, 5, 6, 3

## Abstract
Parameter-efficient fine-tuning methods, represented by LoRA, play an essential role in adapting large-scale pre-trained models to downstream tasks. 
However, fine-tuning LoRA-series models also faces the risk of overfitting on small training datasets, and there's still a lack of theoretical guidance and practical mechanisms to control overfitting on LoRA-based PEFT methods. This paper introduces a novel dropout-based sparsity regularizer for LoRA, dubbed LoRA Dropout, which mitigates overfitting by applying refined dropout to LoRA's low-rank matrices.
We establish a theoretical framework that models dropout in LoRA as a sparse fine-tuning process and derive a generalization error bound under this sparsity regularization.
Theoretical results show that appropriate sparsity can tighten the gap between empirical and generalization risks and thereby control overfitting. We further enhance the sparsity patterns in conventional dropout methods and propose an innovative LoRA Dropout method for more precise sparsity regularization to achieve better overfitting reduction. 
Furthermore, we introduce a test-time ensemble strategy and provide theoretical evidence demonstrating that the ensemble method can further compress the error bound and lead to better performance. 
Extensive experiments on various NLP tasks validate the effectiveness of our LoRA Dropout framework in improving the model's performance.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces LoRA Dropout, a refined dropout strategy applied to the rows and columns of LoRA's low-rank matrices, which enhances sparsity patterns without significant computational overhead. Additionally, the authors propose a test-time ensemble strategy that aggregates outputs from different dropout instances, further improving generalization. Experiments on NLP tasks like GLUE and SQuAD benchmarks demonstrate that LoRA Dropout significantly narrows the training-test loss gap and enhances model performance and generalization.

### Strengths
1. The paper is well-executed, with thorough theoretical analysis supporting the proposed method.
2. The paper is generally clear and well-structured, making it accessible to readers familiar with PEFT and regularization techniques.

### Weaknesses
1. Theoretical Assumptions and Generalizability
The theoretical framework relies on specific assumptions such as η-Lipschitz continuity and positive semi-definiteness of the Hessian matrix. These conditions may not universally apply to all language models or downstream tasks, making the theoretical guarantees less generalizable. Specifically, the assumption of positive semi-definiteness of the Hessian is quite strong and may not hold in the highly non-convex loss landscapes typical of deep learning models. This limits the applicability of the theoretical analysis to scenarios where these assumptions are valid, which may not be common in practice.
2. Computational Efficiency and Practicality
The paper acknowledges that sampling multiple dropout instances during training and testing increases computational costs but lacks quantitative evidence on the extent of this overhead. Without this data, it is difficult for practitioners to evaluate the feasibility of adopting LoRA Dropout in real-world applications. The absence of detailed profiling data, such as the increase in training time per epoch or the inference latency, makes it hard to assess the practical implications of the proposed method.
3. Experimental diversity
Although relevant experiments have been conducted in Lora and AdaLora, their effectiveness in other Lora variants has not been demonstrated. The lack of experiments on other LoRA variants, such as LoRA+ or VeRA, raises concerns about the general applicability of the proposed dropout method across the broader family of low-rank adaptation techniques.

### Questions
1. Can the authors provide more clarity on the assumptions made for the theoretical analysis, specifically the \eta-Lipschitz continuity and the positive semi-definiteness of the Hessian? Are there common NLP models or settings where these conditions do not hold?
2. Could the authors provide more detailed quantitative data on the computational overhead introduced by sampling multiple dropout instances during training and testing? How significant is the increase in training and inference time compared to the original LoRA or other baselines?
3. Can the author provide more experiments on other variants of Lora to demonstrate the effectiveness of the proposed Loradropout framework? E.g., LoRA+, VeRA, LoRA- fa.
4. What is the difference between the author's Lora dropout method and other existing dropout methods, such as DropKey, DropAttention, and HiddenCut.

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
This paper investigates effectiveness of dropout for parameter-efficient fine-tuning (PEFT) methods, specifically LoRA. This topic has been investigated before. The authors first present an analysis about the effect of dropout (with Bernoulli noises) to the loss and generalization error of the learning algorithm. The authors show that a suitable use of dropout rate can reduce generalization error, which is similar with the existing understanding about dropout in ML. The authors then propose a new way (called LoRA dropout) to enclose dropout in LoRA (and LoRA-based variants). Different with prior methods, LoRA dropout applies dropout for the rows or columns of the tunable low-rank matrices. Furthermore, the authors propose an ensemble method for the inference phase, borrowing the idea of MC dropout. Such an ensemble can boost performance of LoRA dropout. Finally, the authors did an extensive experiment to evaluate performance of their method, in comparison with related baselines. The empirical results suggest that their new method can often perform better than the baselines on different benchmarks and tasks. This is really encouraging.

### Strengths
**Originality:**
This paper proposes the use of dropout for the rows or columns of the tunable low-rank matrices in LoRA, which is practical and overcomes the memory limitation of some prior dropout methods. Furthermore, an ensemble method is proposed for the inference phase to further boost quality of PEFT.

**Quality:** 
The experimental results suggest that the proposed method can work well.

**Clarity:**
The writing is quite easy to follow.

**Significance:**
The proposed method seems to work well, which potentially is significant to many practical applications.

### Weaknesses
Despite some encouraging empirical results, many concerns arise from the current presentation. Those concerns are mostly for their theoretical analysis and writing. Each will be discussed below.

**For the theory:**

- The authors use algorithmic stability to analyze generalization error of dropout training. They analyze a regularized loss, which uses Bernoulli dropout in the regularization term. I am not sure that LoRA dropout training can be easily formulated as minimizing this simple regularized loss. Hence, some of their theoretical understandings may not apply to LoRA dropout.

- The main theoretical understandings are mostly originated from Proposition 2.2 which analyzes point-wise hypothesis stablity of a learning algorithm. However, there are many concerns about correctness and meaning of this proposition: 

    - Closeness between $\mathbf{\theta}_L (\mathbf{S}^i)$ and $\mathbf{\theta}_L (\mathbf{S})$ is *not defined* clearly. Such quantity is very important to derive their result, and should play a significant part in the stability constant. The authors ignored this part completely in their proof, causing a big question about the goodness/meaning of their result. Furthermore, the use of a Taylor approximation in the proof, specifically around line 728, introduces a significant error term, $O(\| \theta_L(S) - \theta_L(S^i) \|^2)$, which is completely ignored, rendering the subsequent analysis unsound. The approximation is only valid for very close points, and the authors treat it as exact, which is a critical flaw.
    - The assumption about $\eta$-Lipschitzness of the loss is very important for their analysis and result. Such Lipschitzness seems to be w.r.t the model parameters. However, the authors did not clearly specify it. More importantly, the magnitude of $\eta$ should affect significantly to the bound on generalization error in Theorem 2.4. Nonetheless, the authors did not discuss how large $\eta$ is in practice. For big models, e.g., Llama2, $\eta$ might be very large. If so, their error bound in Theorem 2.4 will be vacuous or meaningless.
    - The assumptions about $\eta$-Lipschitzness and closeness should be translated to the training algorithm. Those assumptions are really strong, and may not fit well with practice. 
    
- Proposition 3.1 claims that their ensemble classifier should have smaller error than the average error of the whole classifier family. However, the statement and the proof of this proposition have a big mismatch. Their proof in Appendix A.2 assumes that the loss is convex w.r.t. the model parameters. Such an assumption is entirely different from that in Proposition 3.1. More importantly, such an assumption is **unrealistic** for deep neural networks, since it is well-known that the training loss for DNNs is often nonconvex. Therefore, their interpretation from this proposition seems not to be well-supported. The use of Jensen's inequality to move the loss inside the expectation is only valid for convex functions, and this condition is not met for typical deep learning loss functions with respect to model parameters.

**For the writing:**

- Some notations are used without definition, e.g., $\mathbf{\theta}_L$
- Some important concepts or assumptions are not defined explicitly, e.g. "closeness" and $\eta$-Lipschitzness. 
- Some mistakes appear in Eq. (1) and (3). The authors misused the function and problem definitions.
- The loss function in Lemma 2.3 seems wrong.
- The empirical and expected losses in Lemma 2.3 and Theorem 2.4 seem wrong. Should they represent the loss for a learning algorithm?

### Questions
- Can the authors specify how significantly can "closeness" affect the stability constant in Proposition 2.2? Is closeness small for LoRA Dropout?
- How large is $\eta$? Is this small for your pretrained models?

### Soundness
1

### Presentation
1

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
The paper proposes a dropout method for LORA fine-tuning which amounts to using dropout on the implicit hidden layer that sits in the middle of the low rank adapters. This is supported by questionable theoretical arguments and solid empirical evaluation.

### Strengths
* The idea is simple and makes a lot of sense.

* The empirical evaluation is comprehensive and convincing. In particular, I like figure 5 because it shows that the authors have identified a key question and are bringing a satisfactory answer.

### Weaknesses
The theoretical part (section 2) is weak and confuses the message of the paper.  

* First, equation (1) is nonsensical. This constraint trivially implies that \delta\theta=0.  This can be fixed by using an inequality constraint instead (i.e. the constraint is less than an arbitrary constant C whose choice is related to the choice of lambda in the dual formulation). The core issue is that the expectation of the squared L2 norm of the masked parameter update, where the mask is a Bernoulli random variable, simplifies to a scaled L2 norm of the parameter update itself. This means the constraint is simply enforcing a scaled L2 regularization, and the dropout parameter p acts as a simple multiplier on the regularization strength, offering no insight into the effect of dropout itself.

* Second, theorem 2.4 does not rely on the presence of dropout, and therefore does not say much about dropout at all. The actual argument (lines 189 to 193) could have been made without this theorem. Therefore the theoretical development of section 2 seems irrelevant to the question at hand and distracts rather than inform the reader. The theorem's result is essentially a bound on the generalization gap that includes a term proportional to the L2 norm of the parameter update, which is controlled by the regularization parameter. The dropout parameter, when interpreted as a regularization multiplier, simply scales this term, providing no specific insights into the mechanism of dropout.

* Finally the dropout scheme discussed in section 2 (equation 3) is different from the scheme proposed in section 3.2 and used in the experiments (as explained by the authors in section 3.2). This further weakens the theory of section 2.  The theoretical section discusses a general dropout on the parameter space, but the practical implementation uses a structured dropout on the low-rank matrices, which is a very different operation. This mismatch makes the theoretical analysis not directly applicable to the actual algorithm, further diminishing its value.

The paper would be as readable and informative if section 2 were replaced by developing the argument of lines 189 to 193 in the context of the actual dropout algorithm (the one of section 3.2). This would make the paper lighter but better overall.  Alternatively it may be possible to make theorem 2.4 dependent on the presence of dropout, preferably in the form used in the experiments. That would save the theoretical section.

### Questions
* Can the statement of theorem 2.4 depend on the presence of dropout (preferably in the form used in the experiments) and show that dropout contributes to reducing the generalization gap?

* What is the practical cost of the test time ensembling (in the experimental results)?

* In figure 4, what is the rank used for LORA-dropout?  This is important to grasp the meaning of the dropout rate.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper builds upon Low-Rank Adaption (LoRa) by introducing a dropout-based sparsity regulator to mitigate overfitting. The authors provide empirical evidence for signs of overfitting with LoRa and derive a generalisation error bound under sparsity regulation Their method drops rows and columns from both tuneable low-rank parameter matrices and maintains efficiency with an ensemble of losses with different dropout instances. Further, model inference is improved by an ensemble strategy compressing the error bound. Finally, all claims are empirically evaluated in Natural Language Understanding, Question Answering, and Instruction Tuning.

### Strengths
* The idea is empirically and theoretically well motivated.
* The improvements of DeBERTaV3 and LLaMA2-7B on GLUE, SQuAD, MMLU, and Vicuna-Eval benchmarks are statistically significant.
* The presentation is clear and easy to follow.

### Weaknesses
 * The evaluation is focused on smaller and nowadays partially outdated models. The paper would benefir from more recent models.
* The ablation is missing test-statistics and standard deviations and is conducted on different, smaller datasets.
* The runtime increases drastically (For example, 18min -> 60min on CoLa).
* It is not clear, how model size further impacts runtime and efficiency as more parameters are involved. As inference time is very crucial it would be beneficial to explore this in more detail and give reccomendations.

### Questions
* Why did you decide to only DeBERTaV3 and LLaMA2-7B (for just one task) to validate your claims?
* Why did you conduct the ablation analysis only on MRPC and CoLA?
* How would the runtime look like for larger, state-of-the-art language models? Do you expect a similar increase in runtime and is this feasible in practive?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper proposes LoRA Dropout, a novel sparsity regularization technique that applies dropout to the low-rank matrices in LoRA-based fine-tuning methods to mitigate overfitting, offering both theoretical analysis and practical improvements across various NLP tasks.

### Strengths
1. I endorse the decision to exclude dropout from the rank dimension in the design of the method.
2. LoRA Dropout can help existing methods like LoRA achieve better performance.

### Weaknesses
1. Line 49-50, the sentence is written in bold. Does it relate to the motivation of this paper and LoRA Dropout? If so, what is the relationship between "high rank overfitting" and LoRA Dropout? Can LoRA Dropout alleviate the overfitting issues caused by a high-rank LoRA model?

2. Following up on the first question, I do not believe that AdaLoRA addresses the high-rank overfitting problem as stated. Instead, AdaLoRA aims to allocate different ranks to weights based on their importance, which is unrelated to the issue of high-rank overfitting. If the authors claim that AdaLoRA can resolve this issue, further explanation is required.

3. The motivation of this paper is unclear, and the introduction lacks logical coherence. In essence, the introduction's logic could be simplified to: high-rank causes overfitting, AdaLoRA mitigates this issue but is insufficient, and Dropout can address it, but without solid theoretical support. It appears that the fundamental problem this paper seeks to address is how to theoretically prove that Dropout can solve the high-rank overfitting issue. However, this is not the case. Could the authors clarify the true motivation behind this work?

4. I do not consider this manuscript to offer a theoretical analysis of the LoRA optimization process with dropout. First, the whole section 2 is quite similar to that in [1], the two main conclusions (Eqs. 5 and 7) differ from the formula 6 and 7 in [1] merely by a change in variables. The proofs in this paper is also heavily similar to those in [1]. Second, Eq. 1 in this paper can be transformed into Eq 1 in [1]. Therefore, they are essentially the same problem. Third, the conclusions drawn in Section 2 (lines 186-193) are, in fact, consistent with the analysis of the effects of sparsity in [1]. Dropout can be viewed as a specific form of sparsity, and therefore, the relationships proven in this section are already encompassed by the analysis in [1]. In conclusion, due to the similarity in proofs and the correlation between dropout and sparsity, I do not find Section 2 to be meaningful. The authors could have simply referenced the conclusions from [1] instead of reproducing the proofs from [1] and presenting them as their own contribution.

5.  While the method itself is not complex, it demands almost double the training time (Table C.2).

typos:
1. Line 13. faces
2. Line 212. bold delta W. Besides, the use of the symbol “delta W” in this paper is inconsistent.
3. Line 526. introduce
4. Table D.1 caption. dataset.
5. Table C.2 duplicated “on”
6. Table1 and 2 caption. Dropout
7. Line 436. between
8. Line 173, 909. Respectively

The writing of this paper gives the impression that it was completed rather hurriedly.

### Questions
1. Line 48-49, “these models typically tend to maintain a relatively high rank to ensure sufficient expressive power”. Indeed, as seen in many papers, with rank of 2,  LoRA series usually can achieve comparable performance to fully fine-tuning. Even fine-tuning LLAMA-7B, some methods can achieve comparable performance with rank=4. 

2. What is the rank setting in NLU tasks? Additionally, how should the LoRA Dropout rate be configured? The original LoRA already includes a dropout rate—does it also play a role during training in this context?

3. Line 228, “which is equivalent to masking random columns..” LoRA Dropout indeed masks random columns and rows of Delta W. Why does masking rows improve performance? What would the outcome be if only rows were masked? 

4. Line 240-243, “Additionally, performing dropout…sparsity in our framework.” I have a question: while I acknowledge that sparsity is important for fine-tuning, why is it necessary to increase the sparsity of delta W when designing LoRA Dropout? After all, more sparsity does not always equate to better performance.

### Soundness
2

### Presentation
2

### Contribution
1
