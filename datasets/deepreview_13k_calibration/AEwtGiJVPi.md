# OwLore: Outlier-weighed Layerwise Sampled Low-Rank Projection for Memory-Efficient LLM Fine-tuning

- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 5, 6, 5

## Abstract
The rapid advancements in Large Language Models (LLMs) have revolutionized various natural language processing tasks. However, the substantial size of LLMs presents significant challenges in training or fine-tuning. While parameter-efficient approaches such as low-rank adaptation (LoRA) have gained popularity, they often compromise performance compared to full-rank fine-tuning. In this paper, we propose \textit{Outlier-weighed Layerwise Sampled Low-Rank Projection} \textbf{\textit{(OwLore)}}, a new memory-efficient fine-tuning approach, inspired by the layerwise outlier distribution of LLMs.
Unlike LoRA, which adds extra adapters to all layers, OwLore strategically assigns higher sampling probabilities to layers with more outliers, selectively sampling only a few layers and fine-tuning their pre-trained weights. To further increase the number of fine-tuned layers without a proportional rise in memory costs, we incorporate gradient low-rank projection, further boosting the approach’s performance. Our extensive experiments across various architectures, including LLaMa2, LLaMa3, and Mistral, demonstrate that OwLore consistently outperforms baseline approaches, including full fine-tuning. Specifically, it achieves up to a 1.1\% average accuracy gain on the Commonsense Reasoning benchmark, a 3.0\% improvement on MMLU, and a notable 10\% boost on MT-Bench, while being more memory efficient. OwLore allows us to fine-tune LLaMa2-7B with only 21GB of memory.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes the combination of the following two techniques:
- Outlier-Weighed Sampling (OWS): a heuristics for stochastic & selective layer wise fine-tuning.
- GaLore: a low-rank-update optimization method family proposed by Zhao _et al._ (2024).

Comparing against Full FT, GaLore, and LoRA, both OWS and OwLore (OWS + Galore) are competitive while keeping peak memory usage lower than 1/2 of Full FT.

### Strengths
The paper presents an effective and memory-efficient fine-tuning method that is competitive. Empirical evaluation spans multiple datasets.

### Weaknesses
1. Presentation seems a bit confusing. This paper first introduces OWS as a technique but in Tables 4-7 it is listed as OwLore (full-rank). Selective layer freezing / GaLore are distinct techniques. And I think the presentation would be clearer if their respective contributions are separately evaluated.
2. Paper could be strengthened if more LISA-D experiments are included. From Table 1 it seems the even simpler heuristics of favoring shallower layers is already effective - is Eq 2 really necessary? Including LISA-D as one of the baselines in Tables 4-7 will help answer this question.

### Questions
What are the # of trainable parameters of methods compared in this paper?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces Outlier-weighed Layerwise Sampled Low-Rank Projection (OwLore), a memory-efficient fine-tuning method for large language models. OwLore improves performance by focusing on layers with higher outlier distributions and selectively fine-tuning those layers. It also employs gradient low-rank projection to enhance efficiency further. Experimental results show that OwLore outperforms baseline methods, achieving significant accuracy gains on benchmarks like Commonsense Reasoning, MMLU, and MT-Bench.

### Strengths
- The proposed method achieves better performance with lower memory requirements.
 - The proposed OwLore includes a novel evaluation of outlier of weights in each layer, hence enable an effective selection algorithm.
 - Incorporating GaLore, further decrease the memory requirements.

### Weaknesses
 - The only contribution of the paper is the metric of how to evaluate the outlier in weights, which is kind of marginal.
- The paper should elaborate why this kind of evaluation is useful, where the idea comes from.
- The author should not only just focus the experiments on how much memory is saved, but also, how much the hyperparameter in OwLore affects the performance.
- The paper should provide some insights from the methods that why combine selection and GaLore con boost performance. Why from the results the two methods are compatible.


In my opinion, a research paper being accepted should propose a novel, interesting methodology, give a clear explanation of where this idea comes from and why it results in such a form, and also demonstrate the effectiveness of the designs and how they relate with intuition.
Maybe the author could detail why the outlier matters so much and why they use such a function to evaluate this.

For the hyperparameter ablations, maybe the tau? and also gamma? Does the method excel at different combinations of hyperparameters? This is one key experiment and the result will show whether the method is superior.

An ablation study can be added to the paper to decompose the contribution of the designs, or just the authors share the insight for this.

Overall, given all this, the paper is not that kind of paper qualified to be accepted, and there are a lot of experiments and analyses that need to be included in the paper, and also the authors' explanation of the results. In my opinion, you can only do so many things with methodology design, and the thing that really matters are those ideas from the experiments from whatever designs which this paper lacks.

### Questions
N/A

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper "OWLORE: Outlier-Weighed Layerwise Sampled Low-Rank Projection for LLM Fine-Tuning" presents a memory-efficient fine-tuning approach for large language models (LLMs). The proposed method, OwLore, introduces an outlier-weighted sampling strategy, focusing on layers with a higher concentration of outliers, which are considered more critical for fine-tuning (though more insights can be provided on why? See weakness). Unlike previous methods such as LISA, OwLore selectively fine-tunes layers based on their outlier distribution, and to further enhance memory efficiency, it uses a gradient low-rank projection for these layers. Experimental results show that OwLore outperforms both full fine-tuning and baseline methods in terms of memory efficiency and accuracy across benchmarks, including Commonsense Reasoning and MT-Bench.

### Strengths
The authors present a straightforward method to reduce the memory costs of fine-tuning large language models. They propose a more effective layer sampling strategy than the uniform approach used in the LISA baseline, selecting pretrained layers based on a targeted sampling method. Additionally, to further increase the number of pretrained layers involved in fine-tuning without raising memory costs, they incorporate GaLore-based gradient low-rank projection. While the method itself may not be highly innovative, the combination of these techniques is intriguing. Experimental results indicate consistent improvements across various datasets and baseline methods.

### Weaknesses
1. Importance of Outlier Weights for Fine-Tuning: Why are outlier weights more important for fine-tuning? Lines 91-94 lack supporting evidence. The statement that “we assign higher sampling probabilities to layers with a greater concentration of outliers, essentially forming a rich-get-richer phenomenon, substantially improving the fine-tuning performance” requires additional justification.

2. Unclear Rationale for the Choice of Outlier Score: The rationale behind the choice of outlier score is unclear.

3. The results presented are not fully convincing without detailed hyperparameter settings for the baseline methods, including the number of iterations for each method. It is particularly unclear why full-model fine-tuning is less effective than the proposed approach, which uses gradient low-rank projection and fine-tunes only five layers instead of the full model. Claims such as “our method outperforms full fine-tuning by a large margin” are potentially misleading, as the gains reported are relatively modest and may fall within standard deviation. Further clarification is needed on why OwLore (Full-Rank) is less effective than OwLore with gradient low-rank projection. Additionally, how does OwLore (Full-Rank) with a gamma setting applied to five layers compare directly to the proposed method? Memory costs should not increase significantly and warrant examination.

4. Comparative Performance of LoRA and Iteration Counts: How does LoRA with rank 16 perform? It would also be useful to know the number of iterations used for LoRA compared to other methods, as it might perform better with longer training durations.

5. It would be more informative to compare with GaLore, with the rank set to 128, similar to OwLore with gradient low-rank projection.

6. LISA Performance and Suggested Ablation Study: Since OwLore with gradient low-rank projection uses five layers, it would be insightful to examine how LISA performs with five layers under the same conditions. If LISA is expected to require more memory, consider conducting an ablation study on OwLore using gradient low-rank projection but without the outlier score, employing uniform sampling across five layers.

7. I request the authors to run the experiments on table 4 for 5 different seeds and provide the standard deviation. Furthermore, please provide the statistical significance test on the results.

### Questions
See above.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes OwLore, a novel method for updating LLM layers using a sampling-based strategy. Specifically, layers with a higher concentration of outliers have an increased probability of being updated. OwLore also incorporates gradient low-rank projection to further reduce memory costs. Extensive experiments across various architectures on commonsense reasoning, MMLU, and MT-Bench demonstrate the effectiveness of OwLore.

### Strengths
1. The method is well-motivated, with a novel and intuitive outlier-based sampling strategy.

2. Experiments using several LLMs, including Llama2, Llama3 and Mistral, across various tasks like commonsense reasoning, MMLU and MT-Bench confirm the effectiveness of the approach, boosting performance over baselines without increased memory cost.

3. The code for OwLore is available, supporting reproducibility and further exploration.

### Weaknesses
1. OwLore may lead to increased time costs, as the outlier ratio for layers must be computed with each update. However, the experiments do not include a comparison of time costs, which seems unfair to baseline methods, especially PEFT methods that do not use sampling. Even with sampling based methods like LISA, its random sampling strategy will likely lead to less time cost than OwLore. Including time cost metrics would provide a more balanced comparison and highlight the efficiency trade-offs of OwLore. Furthermore, the method's reliance on calculating outlier scores before each update introduces a computational overhead that needs to be explicitly quantified and compared against the computational gains achieved through selective layer updates. The paper should provide a detailed breakdown of the time spent on outlier score calculation versus the time spent on actual parameter updates, especially when compared to methods like LoRA which do not require such pre-processing steps.

2. In Figure 4.4, the finetuning loss curve is not converging, with an even sharper drop in the last few optimization steps, making the analysis in this section less convincing. Furthermore, a similar pattern is also observed in Figure 5. The lack of convergence in the loss curves raises concerns about the stability and reliability of the fine-tuning process. The sharp drop in loss at the end suggests that the model might be overfitting to the training data during the final iterations, which could negatively impact its generalization performance on unseen data. The paper should include more detailed analysis of the loss curves, including metrics such as validation loss, to demonstrate that the model is not overfitting and that the reported performance gains are robust.

### Questions
1. In Figure 2, it appears that the last (bottom) layer does not have a high outlier score in OwLore, while the LISA paper indicates that the bottom layer should have a higher importance score and is consistently optimized. What might account for this discrepancy between LISA and OwLore?

2. In Line 215, the phrase "rich-get-richer" likely means that layers sampled and fine-tuned more frequently will, in turn, accumulate more outliers. This creates a feedback loop where layers with more outliers are sampled more often, which then leads to even more outliers in those layers. Could the authors clarify if this effect is intended?

### Soundness
3

### Presentation
3

### Contribution
3
