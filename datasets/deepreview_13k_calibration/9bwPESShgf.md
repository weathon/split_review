# TranSpa: Towards Efficient Structured Sparse Training for Transformers

- Decision: Reject
- Avg Score: 4.25
- Scores: 3, 3, 5, 6

## Abstract
Transformers have emerged as the backbone neural network architecture in today's AI applications. Due to their high complexity, sparsifying transformers, at both pre-training and fine-tuning stages, is very attractive for lower the training and inference costs. In this paper, we propose TranSpa, an efficient structured sparse training approach for language and vision transformers. Unlike prior works focusing on individual building blocks, TranSpa fully considers the correlation between the weight matrices and their component rows/columns, and performs the coupled estimation and coupled sparsification. To achieve that, TranSpa introduces the use of new granularity when calibrating the importance of structural components in the transformer and removing the insignificant parts. Evaluations across different models, in both pre-training and fine-tuning scenarios, demonstrate the effectiveness of the proposed approach. TranSpa can bring $1.6\times$ size reduction with $0.6$ lower perplexity when training GPT-2 model from scratch. It also enables $1.6\times$ training speedup over the existing sparse pre-training method. For training sparse LLaMA-1B from scratch, our approach reduces GPU memory usage by 50\%, decreases training time by 21\%, and achieves a $1.6\times$ speedup in inference throughput while maintaining model performance. Experiments of applying TranSpa for fine-tuning tasks also show significant performance improvement with respect to model accuracy and pruning cost reduction.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes TranSpa, an efficient structured sparse training approach for transformers. Experiments on various models in pre-training and fine-tuning show significant improvements in training speed, accuracy, and cost reduction compared to existing methods.

### Strengths
TranSpa proposed Coupled Estimation and coupled sparsitifation in Sec 3. With inspiration from tSVD, TranSpa implements structured pruning which can be easily translated into real acceleration. 

TranSpa brings weights reduction and speedup in training and inference, e.g., 1.6× size reduction and 0.6 lower perplexity for GPT - 2, and 50% GPU memory usage reduction and 1.6× inference throughput speedup for LLaMA - 1B. TransPa also demonstrates better performance when scaling to llama-2-7b fine-tuning tasks.

### Weaknesses
While the authors applied TransSpa on various architectures (GPT-2, Llama-1b, DeiT), the results are not entirely convincing:

- Table 1 compares TransSpa with the GPT-2 baseline. However, GPT-2's training epochs are twice as many, and the authors don't provide evidence that the TransSpa model has fully trained and converged with half the epochs. This weakens the credibility of the claimed training speedup.
- Table 2 lacks crucial comparisons with PEFT methods for LLM training. The LoRA series is missing data on memory and training time. Additionally, it's unclear why LoRA has the same number of parameters as the baseline.
- Table 3 shows that TransSpa significantly underperforms on small tasks like Winograd (69 → 60), while many studies have shown LoRA can achieve similar performance to Full-FT. This raises concerns about the pre-training results, which are typically considered more challenging than quick 1–3 epoch SFT.
- Table 5 switches to the much smaller CIFAR-10 dataset, despite Table 3 showing comparisons on ImageNet. This inconsistency raises questions about the quality of the loss curve on ImageNet.

The method of TranSpa is not complex, however, why and how it can preseve accuracy compared to full FT is not fully discussed in the paper

### Questions
see comments above

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors propose a novel granularity, called "coupled weight matrix", to evaluate the importance of structural components within a model and apply structured sparsity based on component importance. The "coupled weight matrix" refers to a pair of weight matrices, such as $W_AW_B$. By removing the less important rows of $W_A$ and columns of $W_B$, the authors introduce sparsity into the model.

### Strengths
1. A novel granularity is proposed to evaluate the importance of structural components, offering broader perspective on model optimization.
2. Experimental results appear promising, demonstrating that this approach can effectively accelerate training and inference by utilizing structured sparsity and achieve high performance.

### Weaknesses
1. In Eq. 5, the latter part $\left (0.5 \operatorname{erf} \left ( Y_1 / \sqrt{2} \right ) \odot X W_{in} \right ) W_{out} \neq 0.5 \operatorname{erf} \left ( Y_1 / \sqrt{2} \right ) \odot X \left (W_{in} W_{out} \right )$. Consequently, $W_{in}$ and $W_{out}$ do not fit the definition of "coupled weight matrix." 
2. Most models incorporate position embedding in Multi-Head Attention.  For example, the attention mechanism in LLaMA can be formulated as $\operatorname{softmax}\left(\frac{X_Q \boldsymbol{W}_i^Q ROPE \left(X_K W_i^K\right)^{\top}}{\sqrt{e}}\right) X_V W_i^V$, where $ROPE$ represents a rotation matrix with an an angle determined by the relative positions of two tokens. Thus, $W^Q$ and $W^K$ do not constitute a "coupled weight matrix."  
3.  In current models, such as LLaMA or Mistral, the definition of FFN is $FFN(X)=(XW_{up}\odot silu(XW_{gate}))W_{down}$. Authors didn't discuss this common structure in the article and I do not observe a "coupled weight matrix" within this FFN.

### Questions
- I note that your experiments include LLaMA. How did you identify the "coupled weight matrix" within LLaMA's FFN?

### Soundness
1

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors propose TranSpa, an efficient structure sparsification method accelerating both training and inference of transformers. TranSpa couples weight matrices, estimates their importance accordingly, and removes coupled row/col pairs in each coupled weight matrix. The proposed method is evaluated across different scenarios, including pre-training, fine-tuning and inference. Experimental results demonstrate that TranSpa effectively speedup up transformer training and inference while maintaining the performance.

### Strengths
- This work proposes to consider the importance of weight matrices by couples and removes row/col pairs in coupled weight matrices, improving the performance.
- It is carefully written.
- Experimental results demonstrate a significant reduction on training time and memory usage.

### Weaknesses
- The experimental section lacks some details. For example, Table 1 presents training times but omits FLOPs savings, while Table 2 provides Flops savings without showing time savings.
- The training times for sevearl baselines, such as Monarch in Table 1, are missing, complicating the comparison of baseline performance and TranSpa.
- The estimation of weight importance is based on loss, as outlined in Eq. (6). It's unclear how importance evaluation and sparsification are conducted when there is no loss during inference.

### Questions
- Can you clarify how to evaluate the importance of weights and conduct sparsification during inference?
- In Table 1, why are some pre-training experiments are conducted on 8 cards while others use 4 cards? This inconsistency makes it inconvenient to derive time savings.

### Soundness
3

### Presentation
3

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
The paper introduces TranSpa, an efficient structured sparsification method tailored for transformers used in both language and vision AI models. Unlike previous methods that focus on individual transformer components, TranSpa considers the correlations between weight matrices and their rows and columns, applying a coupled sparsification approach. By introducing a new granularity level, TranSpa selectively removes less significant parts of the transformer, optimizing its structure and reducing computational costs. Empirical results demonstrate that TranSpa achieves a 1.6x reduction in model size with minimal accuracy loss (0.6 perplexity increase) in GPT-2 training from scratch, and offers a 50% memory reduction and a 1.6x training speedup for sparse LLaMA-1B models.

### Strengths
1.Innovative Sparsification: By considering correlations within weight matrices, TranSpa’s coupled sparsification maintains essential model structure.

2.Efficient Granularity: TranSpa’s new granularity method enables precise pruning of less critical parts, optimizing model efficiency.

3.Resource Savings: TranSpa reduces GPU memory usage by 50% and speeds up training by 21% in large models like LLaMA-1B, addressing scalability.

4.Versatile Application: Effective in both pre-training and fine-tuning stages, TranSpa adapts well across various training scenarios.

### Weaknesses
1.One limitation of this paper is that, while it emphasizes the correlation between weight matrices, it does not verify whether this correlation exists only between adjacent weight matrices. Further analysis is needed to confirm if non-adjacent matrices also exhibit correlations, as this could impact the effectiveness and generality of TranSpa’s sparsification approach.

2.A limitation of this paper is the lack of time complexity analysis for key computations, such as compute v and compute $\hat{I}$. Including these analyses would clarify the computational overhead introduced by TranSpa and provide a more comprehensive understanding of its efficiency.

### Questions
Please see the weaknesses

### Soundness
3

### Presentation
3

### Contribution
3
