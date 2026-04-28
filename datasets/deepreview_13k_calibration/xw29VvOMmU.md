# LQ-LoRA: Low-rank plus Quantized Matrix Decomposition for Efficient Language Model Finetuning

- Decision: Accept
- Avg Score: 6.75
- Scores: 8, 8, 6, 5

## Abstract
\vspace{-3mm}
We propose a simple approach for memory-efficient adaptation of pretrained language models. Our approach uses an iterative  algorithm  to decompose each  pretrained  matrix into a high-precision low-rank component  and a memory-efficient quantized component. During finetuning, the quantized component remains fixed and only the  low-rank component is updated. We present an integer linear programming formulation of the quantization component which enables dynamic  configuration of quantization parameters (e.g., bit-width, block size) for each matrix given an overall target memory budget.  We further explore a data-aware version of the algorithm which uses an approximation of the Fisher information matrix to weight the  reconstruction objective during matrix decomposition. Experiments on finetuning RoBERTa and LLaMA-2 (7B and 70B) demonstrate that our low-rank plus quantized matrix decomposition approach (LQ-LoRA) outperforms strong QLoRA and GPTQ-LoRA baselines and enables aggressive quantization to sub-3 bits with only minor performance degradations. When finetuned on a language modeling calibration dataset, LQ-LoRA can also be used for model compression; in this setting our 2.75-bit LLaMA-2-70B model (which has 2.85 bits on average when including the low-rank components and requires 27GB of GPU memory) performs respectably compared to the 16-bit baseline. This work was completed while Han Guo was a visiting student at MIT.}
\vspace{-4mm}

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work proposes a new initialization scheme for doing fine tuning of Large Language Models (LLMs) that have been subjected to Post-Training Quantization (PTQ). The authors motivate their problem by first discussing (along with appropriate references) that the conventional initialization scheme for LoRA, in which the first low-rank adapter is initialized as a Gaussian matrix, and the second low-rank factor is initialized to a zero-matrix, is suboptimal when fine-tuning a PTQ model. The initialization scheme proposed in this paper considers a low-rank + quantized decomposition of the LLM weight matrices. Subsequently, the low-rank factors are used as initializations for fine-tuning.

Most of the paper discusses how to obtain this quantized + low-rank decomposition of the matrix. They do so using an alternating minimization algorithm, wherein the the low-rank component is obtained by computing the SVD of the error residual from the quantized matrix, and the quantized component is obtained by quantizing the error residual from just the low-rank component. This alternating algorithm is a heuristic, and it is terminated when the objective function value, i.e., the Frobenius norm error between the original matrix and its quantized + low-rank decomposition starts diverging (or is small enough).

In addition to this, the work also considers a dynamic bit allocation strategy across different layers, and formulate this problem as an Integer Linear Program. This is a constrained optimization problem, which minimizes the Frobenius norm reconstruction error subject to a total target bit rate. Moreover, they also propose a data-aware quantization strategy, wherein instead of treating each parameter weight equivalently, their sensitivity with respect to the loss function is evaluated using Fisher matrix, and an alternative objective function is minimized instead.

The authors convincingly do extensive numerical evaluations on several tasks, and identify that the predominant regime where their initialization provides benefits is where aggressive compression is required (eg., sub 4-bit quantization bit requirement per parameter).

### Strengths
The work provides a new initialization strategy for fine-tuning LLMs that have been subjected to post-training quantization. Conventional LoRA initialization schemes fail are suboptimal for aggressive quantization regimes, and it is this regime where LQ-LoRA proposed in this work provides an advantage.

The simplicity of this approach is appealing, and it can be readily used with existing quantization schemes in addition to the NormalFloat (NF) quantization scheme utilized in this paper. Proposed ILP formulation of dynamic bit allocation and the data aware variant are also quite interesting. The comprehensive numerical evaluations are also quite descriptive, and clearly identifies where LQ-LoRA performs better, and where it does not.

### Weaknesses
I have some concerns in mind (which are not drawbacks of the paper), but it would be nice if the authors addressed and/or discussed them:

1. One of the contributions of this work is the ILP formulation for dynamic bit allocation across layers. This dynamic configuration of quantization parameters (e.g., bit-width, block size) subject to a total target memory budget is quite interesting. Hardware-wise, the proposed strategy necessitates mixed-precision compute (i.e., different bits for different layers). Even without the ILP, the $Q + L_1L_2$ decomposition requires handling $Q$ is low-precision format, whereas $L_1$ and $L_2$ is high (original)-precision format (eg., $16$-bit). Moreover, the ILP formulation outputs bit-budget allocation at quite fine resolutions like $2$ or $3$-bits. My concern is that such low precision is not easily available as current hardware primitives, i.e.,we can find a $4$ bit GPU, but can we find a $2$ bit GPU? I understand that the simulations are done in PyTorch that provide the flexibility of finer precisions (the authors also mention this on Page 5, "Implementation"). It would be worth discussing that this is a significant bottleneck in the deployment of this scheme for actual benefits in hardware. Please note again that I do not see this as a significant drawback of this paper, but it is important that the authors acknowledge this.

2. There is a recent work on joint low-rank and quantized decomposition of a matrix:

"Matrix Compression via Randomized Low Rank and Low Precision Factorization" (Saha, Srivastava & Pilanci) (https://arxiv.org/abs/2310.11028)

This work derives Frobenius norm error bounds for the low-rank decomposition of a matrix, in which the low-rank factors are also quantized. LQ-LoRA considers the low-rank factors to be in high-precision. This work is complementary in the sense that the the low-rank factors of the LQ-LoRA decomposition can also be quantized (in case, the hardware is limited to low-precision only). This will also help in circumventing the mixed-precision hardware issue mentioned in point 1 above (i.e., now $W$, $L_1$, and $L_2$ -- all three can be in the same precision). The analyses techniques proposed in this work can also be used to upper bound the Frobenius norm error of LQ-LoRA in order to make it more theoretically principled.

I have a few questions:

1. The authors mention: "LoRA obviates the need to allocate memory for storing gradients and optimizer states" -- shouldn't it be stated as LoRA does not require us to store gradients for all parameters of the LLM, but only for the low-rank adapters, for which the number of parameters can be a fraction of the total number of LLM parameters?

2. Why did the authors choose NormalFloat instead of instead of a simple RTN quantization scheme? In principle, it seems that LQ-LoRA can be extended with any quantization scheme, if I'm not mistaken? And RTN has benefits over NF, such as no Gaussian modeling assumptions on the weights?

3. Where does the value $\delta = \frac{1}{2}\left(\frac{1}{30} + \frac{1}{32}\right)$ come from? Was it proposed in the NF paper? Does this value remain this same if more flexible quantization resolutions are considered (as is done in this paper in the ILP, but not probably in the NF paper)?

4. Page 3: How is NF quantization **lossless**?

5. In Fig. 1 (center), the weight matrices are just quantized using NF 3-bits, whereas on the right figure, a low-rank + quantized decomposition is obtained, where the quantization is again 3-bit. The caption says "LQ decomposition results in less quantization error". Is this a fair comparison in terms of the total memory requirement? Isn't it obvious that the right figure will have low error than center, since in the center, the residual from quantization error is approximated by a low-rank factorization in high-precision, whereas residual is not considered in the center?

6. In Alg. 1 pseudocode -- Does $B$ denote the quantization budget or the total number of blocks (as used in the main text)?

7. Page 6: What does it mean by: "weight matrix $\bf F$ has homogeneous rows or columns"? Please clarify in the main text.

8. Is Table 4 the data-aware or the agnostic variant? Also in Table 4: LQ-LoRA with rank $64$ on C4 has ppl $7.93$. unless I'm mistaken, shouldn't there be a corresponding $7.93$ value in Table 2 as well?

### Questions
I have a few questions:

1. The authors mention: "LoRA obviates the need to allocate memory for storing gradients and optimizer states" -- shouldn't it be stated as LoRA does not require us to store gradients for all parameters of the LLM, but only for the low-rank adapters, for which the number of parameters can be a fraction of the total number of LLM parameters?

2. Why did the authors choose NormalFloat instead of instead of a simple RTN quantization scheme? In principle, it seems that LQ-LoRA can be extended with any quantization scheme, if I'm not mistaken? And RTN has benefits over NF, such as no Gaussian modeling assumptions on the weights?

3. Where does the value $\delta = \frac{1}{2}\left(\frac{1}{30} + \frac{1}{32}\right)$ come from? Was it proposed in the NF paper? Does this value remain this same if more flexible quantization resolutions are considered (as is done in this paper in the ILP, but not probably in the NF paper)?

4. Page 3: How is NF quantization **lossless**?

5. In Fig. 1 (center), the weight matrices are just quantized using NF 3-bits, whereas on the right figure, a low-rank + quantized decomposition is obtained, where the quantization is again 3-bit. The caption says "LQ decomposition results in less quantization error". Is this a fair comparison in terms of the total memory requirement? Isn't it obvious that the right figure will have low error than center, since in the center, the residual from quantization error is approximated by a low-rank factorization in high-precision, whereas residual is not considered in the center?

6. In Alg. 1 pseudocode -- Does $B$ denote the quantization budget or the total number of blocks (as used in the main text)?

7. Page 6: What does it mean by: "weight matrix $\bf F$ has homogeneous rows or columns"? Please clarify in the main text.

8. Is Table 4 the data-aware or the agnostic variant? Also in Table 4: LQ-LoRA with rank $64$ on C4 has ppl $7.93$. unless I'm mistaken, shouldn't there be a corresponding $7.93$ value in Table 2 as well?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes LQ-LoRA, a method for fine-tuning LLMs in a memory-efficient manner. Each weight matrix is decomposed into a low-rank component and a quantized component. The paper makes three contributions relative to the previously proposed QLoRA paper (Dettmers et. al, 2023):
1) An iterative algorithm for initializing the quantized and low-rank components for approximating a weight matrix, to minimize the Frobenius approximation error.
2) An integer linear program for assigning the best quantization configuration to each weight matrix, under a specified total memory budget.
3) A data-aware quantization strategy, which assigns more weight during the matrix approximation to parameters that are more "important" according to the Fisher information matrix.

The paper shows that these methods yield meaningful improvements over baseline quantization methods, across experiments on (1) language modeling on C4 (Llama-2 model), (2) instruction tuning on OpenAssistant (Llama-2 model), and (3) fine-tuning on GLUE (RoBERTa-Large).

### Strengths
- Compressing a LLM by replacing each weight matrix into a quantized component (frozen) and low-rank component (which can be fine-tuned) is a great idea for attaining more memory efficient version(s) of a model.
- The proposed iterative initialization method (equation 2) is a natural and simple way to initialize the low-rank (16-bit) and quantized components for each weight matrix, that effectively reduces the approximation error of the method.
- The proposed methods give meaningful improvements over baselines (Table 2), across several tasks and model sizes.

### Weaknesses
 - The idea of decomposing a weight matrix into a low-rank component and a quantized component had already been proposed in QLoRA (Dettmers et. al, 2023).
- A few ablations / baselines could be added, to make clearer where the gains of the method come from. For example:
1) How important is the ILP to LQ-LoRA? Can you show the performance of LQ-LoRA without the ILP?
2) Can you show the performance of the regular LoRA method (no quantization), and also quantization (at different bit-rates) without LoRA, in Table 2?
- I found it unusual that while the quantization configurations were optimized extensively (chosen via ILP), the rank of the low-rank components was kept fixed at 64 for the vast majority of experiments (except for Table 4). Perhaps the rank could also be chosen with the ILP?

### Questions
- Is the only difference between QLoRA+ILP, and LQ-LoRA, the initialization?
- Does the ILP budget, as well as the "bits per param" column, also consider the low-rank components?

Suggestions:
- Can you normalize the y-axes in Figure 1 to be relative error $||X - (Q + L1*L2)||_F / ||X||_F$, to make it easier to interpret?
- Perhaps a Table version of Figure 3 would be helpful to better see how much memory is taken by the low-rank vs. quantized components. Discussing this issue earlier on and more prominently would be helpful for giving readers a better intuitive understanding of what components of the system take the most memory.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes LQ-LoRA, a memory-efficient LLM adaptation method that decomposes each pretrained matrix into a high-precision low-rank component and a memory-efficient quantized component. The algorithm is adapted from QLoRA and applied modification to solve the problem that zero initialization of the low-rank matrix may not be optimal when the fixed matrix is quantized. The method decomposes the matrix by an iterative algorithm and updates only the low-rank matrix weights during fine-tuning. Results showed that the proposed method outperforms QLoRA and LREC with similar bit compression rates.

### Strengths
-	The proposed method decomposes the pretrained matrix into a quantizable fixed matrix and low-rank matrix that is already optimized before fine-tuning starts, which contributes to improved accuracy.
-	The paper shows that LQ-LoRA can be used as a mixed quantization strategy, and also proposes a data-aware version of the algorithm, which enables users to flexibly set a target memory budget.
-	Results show that the proposed method can be generalized to different model families by showing outperforming results with RoBERTa and LLaMA.

### Weaknesses
 - The authors have introduced a method that employs an iterative algorithm for initialization. Can they provide insights regarding the computational latency associated with their approach?

- The authors assert the efficiency of LQ-LoRA based on empirical evidence, yet lack theoretical backing. To strengthen the credibility of the algorithm, a comparison might be beneficial, especially with methods that initialize the Q(W) + L1L2 matrix in a manner that closely mirrors the original pretrained matrix W. Consider, for instance, the use of GPTQ as a compensatory mechanism.

- It appears that this paper serves as an expanded or refined rendition of the Q-LoRA paper. As such, it seemingly inherits the same limitation, notably the inference overhead, given that this approach must fail to integrate the LoRA layer into an existing linear layer. 

- Similarly, I would like to raise a query about the paper's novelty. While this method undeniably enhances the current approach (Q-LoRA), from a PEFT perspective, there could be superior methods, particularly concerning inference challenges. On the topic of novelty, I await the insights of fellow reviewers.

### Questions
Included in the weakness.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors of the paper propose an iterative method to decompose a pre-trained weight matrix W into a quantized component $Q$ and a low-rank component $L_1L_2$, which encourages $Q + L_1L_2$ to approximate $W$ as much as possible. They also present dynamic configuration quantization via integer linear programming and a data-aware decomposition method by employing the Fisher information matrix.

### Strengths
The authors of the paper the first time tackles the issue that $Q + L_1L_2$ might not be equal to its original pre-trained weight matrix $W$. Moreover, they try to assign different configurations to each pre-trained weight matrix by utilizing integer linear programming.

### Weaknesses
It seems necessary that LQ-LoRA should be compared to the case when BRECQ, OPTQ, and/or FlexRound is used to quantize pre-trained weight matrices with $L_2$ initialized to zero. The reason why I bring this up is that if BRECQ, OPTQ, and/or FlexRound is employed for $q(\cdot)$, $X(q(W) + L_1L_2)$ would be approximately equal to $XW$ because all their objectives are designed to minimize the difference between $ Xq(W)$ and $XW$. Then, the need for the proposed data-aware decomposition method would be marginal. Although the authors mention that they stick to NF quantization, integer quantization can be also surely used in QLoRA. Furthermore, the experimental results of LREC 4-bit on MMLU almost match that of LQ-LoRA, which weakens the motivation for LQ-LoRA. The comparison with GPTQ-LoRA is insufficient, as GPTQ is a layer-wise optimization method. Block-wise optimization methods like BRECQ [1] and FlexRound [2] could potentially yield better results when combined with LoRA, making the motivation for LQ-LoRA less compelling without such comparisons.

### Questions
None

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
