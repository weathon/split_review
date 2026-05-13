# Towards Making Linear Attention Usable

- Decision: Reject
- Scores: 3, 3, 3, 5

## Abstract
The original Transformer attention mechanism, based on Softmax, has time and memory complexities of $O(N^2D)$ and $O(N^2)$, where $N$ is the number of tokens and $D$ the dimension per attention head. As current LLM applications trend towards processing larger token sequences, and Transformers gain popularity in image, video, and audio processing, addressing this quadratic cost becomes imperative. Since the introduction of Transformers, numerous approaches have been proposed to linearize this scaling. One such method is Linear Attention, which captures all-to-all token pair attention in $O(ND^2)$ time. However, its drawback lies in its high memory footprint of $O(ND^2)$. While Linear Attention has shown promise in small-scale benchmarks, the high memory demand has prevented Linear Attention to be studied in context of large benchmarks and practical use cases. In this work, we demonstrate how to reduce the memory complexity to $O(ND)$ by approaching calculations from a novel perspective. Additionally, since Linear Attention does not compute the attention matrix directly, it precludes the use of traditional dropout. To address this, we introduce an alternative dropout mechanism. Our study confirms linear scaling in both wall-clock time and memory usage. We also compare our method with Flash Attention and conduct an ablation study on our proposed dropout alternative.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper attempts to make linear attention efficient and useable by reducing the memory consumption and introducing an alternative mechanism to dropout. Results show the usefulness of the proposed approaches, while maintaining the linear scaling in N in both wall-clock time and memory usage.

### Strengths
- The paper is well written and easy to follow.
- Interesting topic -- making linear attention efficient is of great interest to the research community.

### Weaknesses
 - The results are somewhat unsatisfactory, with only limited to a very small model. More experiments and analysis are needed to justify the effectiveness of the proposed method.
- What about practical usage? Can this method start from the pre-trained LLMs and directly convert them to efficient linear attention? Also, can it start from a LLM with linear attention and make it efficient through little amount of training or finetuning?
- Can this method scale to large models? Say, billion scale models. Authors at least perform experiments using 1-3B models.
- What about hardware efficiency of the proposed changes to the linear attention?

### Questions
I’d like to rate the current submission reject due to limited technical contributions and lack of convincing experiments. The paper needs significant changes including new experiments and possibly methodological improvements in justifying the practical use behind the proposed method.

### Soundness
2

### Presentation
2

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
This paper addresses two major limitations in current linear attention mechanisms. First, although existing approaches aim to reduce computational complexity to linear time, they still practically require O(ND²). To address this, this work proposes a method to lower the memory usage to O(ND). By deriving and computing the attention layer gradient analytically, this paper achieves this efficiency without relying on a differentiable programming library, thus avoiding the need to store variables for backpropagation. This work uses Factorization in both forward and backward passes and validates the reduced memory and time complexity in the context of attention layers and large language model training. Additionally, because linear attention doesn’t inherently compute an attention matrix, dropout cannot be directly applied. To overcome this, this work introduces an alternative mechanism that emulates the effect of dropout, with its effectiveness confirmed through an ablation study.

### Strengths
In terms of practicality, reducing memory cost is very crucial. If this work maintains comparable performance or minimizes the performance drop, it has impactful potential.

### Weaknesses
### Lacks of benchmarks
Although it shows memory and latency experiments by increasing token length, it didn't show common LLM benchmarks such as MMLU and GLUE or long-context LLM benchmarks such as n streaming books (PG19), Long Context Understanding (LongBench), and book summarization (Booksum).

### questions:
Same Weakness

### Questions
Same Weakness

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
This manuscript proposes two techniques to improve the practical efficiency of linear attention. One is the factorization of matrix multiplication, and the other is a modified dropout technique. Toy experiments show the effectiveness of the two techniques.

### Strengths
- The Motivation is clear.

- The theoretical derivation is detailed.

### Weaknesses
Overall, this manuscript is not ready for publication. My concerns are listed as follows:

- The technical novelty is limited. The first proposed method, matrix multiplication multiplication, is a standard operation in linear attention methods [1]. I see some novelty in the second dropout technique, but its effectiveness is validated only in small-scale experiments.

- The experiments are not convincing enough. One small model (Pythia-14M) is adopted, and only a training curve is presented. To make the results more convincing, it is recommended to conduct experiments on larger-scale models (both language and vision models should be included) and well-known benchmarks. The comparison should be the about the trade-off between efficiency and performance.

- The presentation needs substantial improvements. Some examples are listed as follows:.
  - In the introduction, the authors categorize linear attention methods into two lines of work:  Sparsified/localized Attention, and Kernel Separation. However, no references are cited here.
  - In the equations (e.g. eq1), the index subscriptions $i,n,j$ should not have bold fonts.
  - In Sec. 3.1, the FLOPs calculation example could be given by normal matrix presentations instead of a 3x3 toy example.
  - The derivaton in Sections 3&4 are too detailed and might distract readers from the main method. It is recommended to put detailed derivation process in the appendix, and present the major method in the main text.

### Questions
How does the proposed method compare with those RNN-like methods such as Mamba and RetNet?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper focus on reduce the space complexity of vanilla linear attention. To be specific, the authors change the order of some matrix multiplication in the forward pass of linear attention when the kernel is linear. The authors also provide a detailed derivation of the forward pass and backward pass. Because linear attention does not have a explicit attention map in the forward pass, the authors propose an alternative for the dropout regularization mechanism. Some testing experiments shows this method are indeed save the memory footprint, but the experiment is not abundant.

### Strengths
1. The topic of saving the memory footprint of linear attention is interesting. This is important while it seems few researcher have noticed.

2. The forward and backward derivation is also very clean.

3. An alternative for dropout is proposed, and the experiments in LRA and Tiny Stories datasets verifies its effectiveness.

### Weaknesses
 (1) After the forward and backward modification, althought the computational seems equivalent compared with linear attention, will the proposed method achieve the same performance is still unclear. The authors can check the RepVGG paper, which shows that equivalent computational may not produce the same performance.

(2) The paper only change is computing order of Linear Attn, and proposed a new dropout alternative. I think the novelty is limited.

(3) Lack of experiment.

    (3.1) for the time and memory scaling experiments (sec. 5.1). The authors only show one fixed number of head H, fixed head dim D, varying token length result experiment, and, one fixed token length N, varying head dim D experiment. I think the author should show more results on the H, D choices, since this experiment is training free, and whether the experiment results would show the same trend. Additionally, the only chosen one is weird. Since in ViT-Base H=12 and D=64, in DiT-S H=6 and D=64, I cannot find a popular model with H=16 and D=32.

    (3.2) For LLM experiment in Sec. 5.2, the author does not express the reason why they choose this model and this dataset. And they only show the loss curve (also the orange curve is not trained as long as the blue one is). No evaluation metric provided.

    (3.3) For the ablation study in Sec. 5.3, I do not get the point why the author do not provide these accuracy results in main results, but put them in ablation. The training hypermeter is also not clear. I have also check the LRA results in other papers (e.g. S4, by Albert Gu in ICLR 2022, https://arxiv.org/pdf/2111.00396). The results of LRA in the submission are far lower than this 2 years ago paper. And both the Softmax result and Linear(alt. drop.) results have different numerical range compared with the results in S4 paper.

(4) The experiment hyper-parameter is not described. That may be the reason why it cannot match the results in S4 paper. I think the authors should follow others setting, or explain why they choose a different setting.

(5)Minors:

    (5.1) wrong formula in line 90: f(x) = exp(q \cdot k / root(D)), while there is no x in the expression.

    (5.2) a latex bug in appendix D.1 (line 860) have not be fixed.

### Questions
1. In section 3.1, the final operation we need to calculate is 

[a_1, a_2, ..., a_n]^T  \times [b_1, b_2, ..., b_n] \times [d_1, d_2, ..., d_n]^T

If we compute the first \times first, there will be n^2+n^2 multiplications and n*(n-1) accumulations. If we compute the second \times first, there will be (n+n) multiplications and (n-1) accumulateions.

So the point sec 3.1 made it that, change the operation order will save FLOPs. Do I miss something?

2. The  new dropout alternative seems complicated. It seems no experiments discuss its complexity. Will it take much inference latency?

3. Overall, I give my initial rating as "marginally below the acceptance threshold". I hope the authors can solve my concerns as I mentioned in weakness and questions section.

### Soundness
2

### Presentation
2

### Contribution
2
