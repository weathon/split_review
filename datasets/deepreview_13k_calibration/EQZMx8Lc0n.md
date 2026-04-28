# RoCoFT: Efficient Finetuning of Large Language Models with Row-Column Updates

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 3, 6, 6

## Abstract
We propose RoCoFT, a parameter-efficient fine-tuning method for large-scale language models (LMs) based on updating only a few rows and columns of the weight matrices in transformers.
Through extensive experiments with medium size LMs like BERT and RoBERTa, and larger LMs like Bloom-7B, Llama2-7B and Llama2-13B, we show that our method gives comparable or better accuracies than state-of-art PEFT methods while also being more memory and computation-efficient. We also study the reason behind the effectiveness of our method with tools from neural tangent kernel theory. We empirically demonstrate that our kernel, constructed using a restricted set of row and column parameters, are numerically close to the full-parameter kernel and gives comparable classification performance. Ablation studies are conducted to investigate the impact of different algorithmic choices, including the selection strategy for rows and columns as well as the optimal rank for effective implementation of our method.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper introduces RoCoFT, a parameter-efficient fine-tuning (PEFT) method designed for large language models (LLMs) that updates only a subset of rows and columns in transformer weight matrices. This approach aims to retain model accuracy while reducing memory and computational requirements compared to traditional fine-tuning methods. RoCoFT achieves state-of-the-art or comparable results on tasks like GLUE, question answering, and summarization, as well as on benchmarks requiring common sense and mathematical reasoning. The authors analyze the method’s effectiveness through neural tangent kernel (NTK) theory, showing that kernels from RoCoFT are numerically close to full-parameter kernels, suggesting that fine-tuning a limited parameter subset preserves core model knowledge.

### Strengths
- The presentation is clear, and the paper is easy to follow, with only a few minor typos. 
- The proposed method, RoCoFT, is straightforward and demonstrates strong empirical performance.
- The results are reported across multiple tasks and base models, evaluated using various metrics, including memory usage, computation time, and accuracy. This is a good plus to the paper.

### Weaknesses
 - **Lack of Related Work Discussion**: One weakness of this paper is the limited scope of its related work discussion, focusing primarily on low-rank methods (e.g., LoRA). However, RoCoFT has a closer methodological resemblance to pruning and sparse fine-tuning methods, which are underrepresented in this review. In the parameter-efficient fine-tuning (PEFT) field, methods generally fall into either low-rank or subset of trainable parameter categories, so a more comprehensive comparison should include subset of trainable parameters finetuning baselines (or sparse fine-tuning), such as [1-8]. Adding a discussion of these methods in the related work section would strengthen the contextual foundation of this paper.

- **Need Additional Novelty Clarification**: The paper lacks a detailed discussion of how RoCoFT differs from existing sparse PEFT methods, such as those presented in [1-8]. Specifically, the method's novelty is not clearly established in relation to techniques that select subsets of parameters for fine-tuning based on criteria like gradient magnitude or Fisher information.

- **Lack of Baseline Comparisons**: While RoCoFT has similarities with pruning and sparse fine-tuning techniques, the paper currently lacks direct baseline comparisons to these methods. Including baselines from sparse fine-tuning methods in the experiments would offer a more balanced evaluation of RoCoFT's performance and efficiency. The absence of these comparisons makes it difficult to assess the true advantages of the proposed method.

- **Inclusion of More SOTA Models**: The experiments include recent models like DeBERTaV3 and LLaMA-2, which is commendable. However, the study would be more persuasive if it also incorporated newer state-of-the-art models (e.g., Llama3-8B, Llama3.1, Minstrel) to reflect the rapidly advancing field of pre-trained model performance. The current selection of models, while relevant, does not fully capture the cutting edge of LLM capabilities.

- **Typos**:
"prevailing paradiagm" should be corrected to "prevailing paradigm".
"state-of-art" should be "state-of-the-art".
"massive amount of text" should be "massive amounts of text".
"signficant savings" should be "significant savings".

- **Clarity of Baseline Model in Figures**: In Figure 2 and Figure 3 of Section 4, the efficiency comparisons are unclear because the base model for fine-tuning (used to report memory and time costs) is not specified. Similarly, Figure 5 lacks clarity on which base model was used for reporting average accuracy across different metrics. Including these model details would improve transparency in the experimental setup.

### Questions
-  **Discussion on Fisher Information**: Reference [5] uses empirical Fisher information to select the most efficient parameters for fine-tuning. It would be beneficial if the authors discussed the efficiency of this method relative to RoCoFT, as this comparison could highlight RoCoFT’s strengths and potential trade-offs.

-  **Memory Cost Clarification**: In fig.2, the author reports the memory cost for baselines and RoCoFT. However, the results are not easy to follow/understand. In LLM, since Adam optimizer is the most common optimizer, the memory cost for full Adam optimizer will be 2 times than the model weights. For instance In Llama-2-7B model, the model weight is 13.6G and the optimizer will cost 2*13.6GB. However, LoRA can reduce the optimizer memory cost to less than 1%. In Fig.2, the authors report the memory cost for RoCoFT and LoRA is still 2 times than the model weight, can you kindly discuss why is that?

- **percentage of trainable parameters**: In PEFT field, papers usually use percentage of trainable parameters to present the algorithm efficiency. Since in Figure2, Figure3 of Section4, efficiency comparison, the author didn’t clarify what is the fine-tuning base model author used to report all the memory and time cost. It’s also different to find In figure what is the fine-tuning base model author used to report the average accuracy for different metrics in figure 5. Can the author discuss the percentage of trainable parameters they use?

- **Implementation for Memory Reduction**: Low-rank methods like LoRA use additional trainable adapters, while sparse fine-tuning often applies binary masks to reduce memory. It would strengthen the paper if the authors elaborated on how the paper implement RoCoFT to achieve memory reduction and speedup compared to these existing techniques, and discuss it from the aspect of system. Do RoCoFT need to implement full forward and backward propagation for all parameters? Do RoCoFT will introduce more modules during the fine-tuning process? 

I would like to discuss the questions I raised regarding the weaknesses and concerns with the authors. If my concerns are adequately addressed, I would be willing to reconsider my rating.

**References**: 

[1] The Lottery Ticket Hypothesis: Finding Sparse, Trainable Neural Networks

[2] Parameter-Efficient Fine-Tuning without Introducing New Latency

[3] Sparse Matrix in Large Language Model Fine-tuning

[4] Parameter-Efficient Transfer Learning with Diff Pruning

[5] Training Neural Networks with Fixed Sparse Masks

[6] Scaling Sparse Fine-Tuning to Large Language Models

[7] Composable Sparse Fine-Tuning for Cross-Lingual Transfer

[8] Diff Pruning: Parameter-Efficient Transfer Learning with Diff Pruning

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
In this paper, the authors address the challenge of efficiently adapting a large language model to a new task. This problem, known as Parameter Efficient Fine Tuning (PEFT), has gained significant attention in recent years following Lora's success. The main observation in this paper is that training only a small subset of rows or columns of the original weight matrices is sufficient for attaining good performance on the new task. This means fine-tuning could be performed by updating a few parameters with no memory overhead (as required with Lora-style methods). This type of fine-tuning is evaluated on multiple datasets and using several base models. The results demonstrate that this approach is competitive with leading baselines.

### Strengths
The authors study an important problem in LLMs.

The method is relatively efficient and lightweight.

The evaluation covers multiple transfer tasks and several base models.

They provide an NTK based empirical evaluation that aims to explain the observed phenomenon.

### Weaknesses
The paper is not well written, multiple parts are not clear, and there are many typos.

In essence, the method presented in this paper was already presented in another paper [1].
In fact, in [1] the authors wrote:

“ We randomly sampled the same amount of parameters as in BitFit from the entire model, and fine-tuned only them (“rand uniform” line in Table 3). The results are substantially worse across all tasks; similar patterns are observed when the random parameters are sampled as complete rows/columns in the parameter matrices (“rand row/col” line in Table 3). “

Which basically indicates that the authors in [1] have already evaluated the procedure detailed in this paper and concluded that updating the bias terms (also known as fitbit) is better. 
The results by the authors demonstrate comparable results between single row/column updates and fitbit. In contrast, the authors in [1] demonstrated that row/column update does not work well in some datasets. Can the authors explain why there is a performance gap between the evaluation in [1] and what is reported in this paper?

Another problem, is that proper credit is not given to [1], which were the first to propose using row/column updates.

Even when ignoring the fact that this idea was already presented in [1], I can still see value in providing new insights about this row/column optimization scheme. But I don’t see the paper providing such new insights in its current form. The row/column selection strategy is pretty standard, and the evaluated selection schemes work as well as random selection.

The NTK perspective is also unclear; since it is primarily empirical, I don’t see what new intuition is gained from these evaluations. It is intuitive that changing only one raw/column from the entire matrix won’t change the NTK much, but also that a few steps of fine-tuning won’t. If anything, the authors should have also compared these kernels to the original kernel (before fine-tuning). If they are all similar to the original one (before fine-tuning), then I don’t understand what we gain from this insight.

In terms of presentation, the paper needs significant improvement. Currently, the results are presented without providing a clear explanation of the “method.” Specifically, the scheme for the selection of rows and columns is only described in the results section.

In the results, the authors detail methods termed 1-row and 3-row without explaining what those are.

Also, regarding the number of parameters, it seems that the 3-row uses 5 times the number of parameters as the 1-row. So, is it three rows vs. one? Something does not make sense here.

Why are the methods presented in Table 1 not included in all other tables?
For example, why isn’t Fitbit (which is the most related paper to this one) not included in Tables 2+3+4, figure 2+3?



Multiple typos:

 "paradiagm" -> "paradigm".
"mermory" -> "memory".
"signficant"  -> "significant".
"tranformer"  -> "transformer".

“computation-efficient”  -> “computationally efficient.”
In the abstract “our kernel…are numerically”-> should be *is* numerically

Several abbreviations are mentioned in the abstract without introducing what they mean: RoCoFT, PEFT..

No intuition about the selection is provided in the abstract.

Many times, two numbers are presented without explaining what they mean, for example, in line 203 85.65/90.61?! And in many cases, in the tables. This is not clear, even from the caption, which tries to explain what they mean.

In some cases, as shown in Table 1, FT is substantially worse than many low-rank methods, for example, in RTE. Doesn’t this suggest that there is severe overfitting?

In the optimal rank evaluation, the performance of the RoCoFT method is not consistent with the results of the same method presented in Table 1 (for this data, SST2).


Overall, I would recommend the authors rewrite the paper as an “insight paper”, which provides empirical evaluations that support a phenomenon, rather than a “method paper”. It would also be valuable to look into the dedicated scheme for selecting the rows/columns.

### Questions
In the results, the authors detail methods termed 1-row and 3-row without explaining what those are.

Also, regarding the number of parameters, it seems that the 3-row uses 5 times the number of parameters as the 1-row. So, is it three rows vs. one? Something does not make sense here.

Why are the methods presented in Table 1 not included in all other tables?
For example, why isn’t Fitbit (which is the most related paper to this one) not included in Tables 2+3+4, figure 2+3?





Multiple typos:

 "paradiagm" -> "paradigm".
"mermory" -> "memory".
"signficant"  -> "significant".
"tranformer"  -> "transformer".

“computation-efficient”  -> “computationally efficient.”
In the abstract “our kernel…are numerically”-> should be *is* numerically

Several abbreviations are mentioned in the abstract without introducing what they mean: RoCoFT, PEFT..

No intuition about the selection is provided in the abstract.

Many times, two numbers are presented without explaining what they mean, for example, in line 203 85.65/90.61?! And in many cases, in the tables. This is not clear, even from the caption, which tries to explain what they mean.

In some cases, as shown in Table 1, FT is substantially worse than many low-rank methods, for example, in RTE. Doesn’t this suggest that there is severe overfitting?

In the optimal rank evaluation, the performance of the RoCoFT method is not consistent with the results of the same method presented in Table 1 (for this data, SST2).


Overall, I would recommend the authors rewrite the paper as an “insight paper”, which provides empirical evaluations that support a phenomenon, rather than a “method paper”. It would also be valuable to look into the dedicated scheme for selecting the rows/columns.

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors proposed a simple fine tuning method for LLMs that updates only a few columns/rows in the base model. NTK regression-based analysis proposed to explain why single row/column updates work and extensive experiments were conducted to evaluate the method on diverse language tasks.

### Strengths
- The method is very simple but shows prominent results for some datasets
- The method was evaluated on large and diverse number of datasets
- Applying NTK regression to get explanation for why the method works - looks interesting

### Weaknesses
 - Limited novelty of the proposed method: the authors propose to update a few columns/rows in the base model and exploit the existing NTK regression method to explain it. The core idea of updating specific parameters in a large model is not entirely new, and the application of NTK regression, while interesting, feels like an incremental step rather than a significant breakthrough. The method lacks a strong theoretical grounding that would justify the specific choice of row/column updates over other parameter selection strategies.
- I don’t understand how the results in Table 5 are consistent with Table 1 so we can explain why the method works with NTK regression. In Table 5 the proposed method performs worse than FT while in Table 1 it is not the case. The discrepancy between these tables raises concerns about the validity of the NTK-based explanation. The experimental setup and the training regime should be clarified to understand why the results are inconsistent.
- In-place updates disable the behavior of the model as an adaptor. This is a trade-off that should be discussed while presenting 0 additional parameters. The inability to easily extract and reuse the updates as a separate adaptor limits the practical applicability of the method in scenarios where modularity and transferability are important.
- Missing explanation / intuition why the method fails on some datasets, e.g. MNLI, QNLI, RTE in Table 1. The paper lacks a detailed analysis of why the proposed method underperforms on certain datasets. A deeper investigation into the specific characteristics of these datasets and how they interact with the method would be beneficial.
- Missing additional recent LoRA-style baselines with low number of trainable parameters, e.g. [1-3] . The comparison with existing parameter-efficient fine-tuning methods is not comprehensive enough. The inclusion of more recent and competitive baselines is necessary to properly contextualize the performance of the proposed method.
- The efficiency gains are not significant compared to other LoRA-style methods, also it is not interesting since the number of trainable parameters is small for adapter-like methods. The paper does not provide a compelling argument for the efficiency gains of the proposed method. The reported improvements are marginal, and the method does not offer a substantial advantage over existing approaches.

### Questions
- I would like to see an experiment where no weights are updated in the pretrained model and only classification head is trained and how the obtained accuracy differs from the single-column/row adaptations.
- It is not clear from the Sec.4 if the setup of baselines in terms of hyper parameters is the same as of the proposed method. I’m concerned that the small differences in the evaluation between the proposed method and baselines stems from setup differences.

### Soundness
2

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
The authors propose a novel method named RoCoFT for parameter-efficient fine-tuning (PEFT). RoCoFT updates only a few rows or columns of the trained parameter matrices, achieving even lower complexity compared to existing PEFT methods. The effectiveness of RoCoFT is supported by neural tangent kernel (NTK) theory, as demonstrated by the authors. The empirical performance of RoCoFT is extensively evaluated on several benchmarks and compared with a large number of baselines.

### Strengths
1. The method is simple, straightforward, yet effective. The presentation is clear and easy to follow.

2. The performance comparison with baselines is extensive. Besides, the learnable parameters in RoCoFT are much less than existing methods, which is very useful.

3. As shown in ablation studies, the strategy of choosing rows and columns is robust and does not need much tuning.

### Weaknesses
1. The NTK analysis in Section 5 is not complete. The results in Tables 5 and 6 only include comparisons between RoCoFT, FT, and the pre-trained weights. However, if other methods, such as LoRA, also have a kernel that is empirically close to the full-parameter kernel, it becomes unclear why RoCoFT can achieve performance improvements over them. Similar experiments on other baselines should also be included. Specifically, the analysis should explore the kernel alignment of other PEFT methods with the full fine-tuning kernel, and not just their similarity to the pre-trained kernel. This is crucial for understanding the specific advantages of RoCoFT over other parameter-efficient approaches. Furthermore, the analysis should consider the initialization sensitivity of these methods, as different initialization schemes could lead to varying kernel alignments and performance outcomes.
2. Further explanation should be provided on why the few-shot learning performance is used as a downstream task for kernel comparison in Tables 5 and 6. Why are the performances in Tables 1, 2, and 3 not used for kernel comparison? The choice of few-shot learning for kernel analysis needs more justification. It's unclear why the kernel similarity on a small subset of data is representative of the full training set performance. A more detailed explanation is needed on how the kernel alignment on few-shot examples relates to the generalization performance on the full dataset. The analysis should also discuss the potential limitations of using few-shot learning for kernel comparison, especially if the kernel behavior changes significantly with more data.
3. The empirical improvement in memory costs in Figure 2 and training time costs in Figure 3 appears marginal, which is inconsistent with the large improvement suggested by Table 4. Please provide a detailed explanation. The discrepancy between the theoretical memory savings and the observed empirical gains needs to be addressed. The paper should discuss the overheads associated with the implementation, such as data loading, optimizer states, and other factors that might diminish the practical benefits of the method. A more thorough analysis of the memory and time costs, including a breakdown of the different components, is needed to reconcile these seemingly contradictory results.

### Questions
1. How are the two values in the "Avg." column computed in Table 1?

2. Can the row update and column update be used simultaneously? It seems to me that this simple strategy allows for more flexibility and enhanced performance.

### Soundness
2

### Presentation
3

### Contribution
3
