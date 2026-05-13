# Structural Pruning of Large Language Models via Neural Architecture Search

- Decision: Reject
- Scores: 6, 5, 3

## Abstract
Large language models (LLMs) mark the state-of-the-art for natural language understanding. 
However, their large size poses challenges in deploying them for inference in real-world applications, due to significant GPU memory requirements and high inference latency.
This paper explores weight-sharing based neural architecture search (NAS) as a form of structural pruning to find sub-parts of the fine-tuned network that optimally trade-off efficiency, for example in terms of model size or latency, and generalization performance. 
Unlike traditional pruning methods with fixed thresholds, we propose to adopt a multi-objective approach that identifies the Pareto optimal set of sub-networks, allowing for a more flexible and automated compression process.
Our NAS approach achieves up to 50% compression with less than 5% performance drop for a fine-tuned BERT model on 7 out of 8 text classification tasks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposed weight-sharing-based NAS to compress fine-tuned pre-trained LLMs by slicing subnetworks. By utilizing a multi-objective approach, they can find the Pareto optimal set of architectures that balance model size and validation error. The NAS approach achieves up to 50% compression with less than 5% performance drop for a fine-tuned BERT model on 7 out of 8 text classification tasks.

### Strengths
The paper has detailed literature research and multiple baseline models for comparison and the selected topic is very important given that LLM is more and more important in our everyday life. Improving the LLM efficiency is critical.

The paper also provided in-depth ablation study.

### Weaknesses
When looking the metrics, it seems the newly proposed NAS model mainly performs better when the model is pruned heavily. The model inference time is not the best when compared with other models.

In Figure 4, the graph shows: On 7 out of 8 dataset the new NAS strategy is able to prune 50% with less than 5% drop in performance (indicated by the dashed line) in performance. It seems more than 1 datasets dropped more than 5% when pruning 50% of parameters?

### Questions
In Figure 4, the graph shows: On 7 out of 8 dataset the new NAS strategy is able to prune 50% with less than 5% drop in performance (indicated by the dashed line) in performance. It seems more than 1 datasets dropped more than 5% when pruning 50% of parameters?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper studys a important research direction for NAS: structural pruning using NAS. The paper explores weight-sharing based neural architecture search (NAS) as a form of structural pruning to find sub-parts of the fine-tuned network that optimally trade-off efficiency. Authors valicate the effectiveness of the proposed method for fine-tuned BERT models.

### Strengths
The writing of this paper is commendable as it is well-structured and easily comprehensible.  I believe that utilizing Neural Architecture Search (NAS) for pruning structured architectures is one of the crucial research directions in the field of NAS. This paper provides detailed experimental evidence of the effectiveness of their approach, particularly on the GLUE benchmark.

### Weaknesses
One significant aspect that requires attention is the performance on the GLUE benchmark. It is worth considering an alternative branch of NAS, which involves directly searching for new architectures using distillation techniques for fine-tuned models such as AdaBERT, TinyBERT, and NAS-BERT. These methods have demonstrated the ability to achieve 50% pruning without any notable performance degradation and even achieve an impressive 80% reduction in parameters with minimal impact on performance. It would be beneficial to include and discuss these baselines in the paper. Moreover, it would be interesting to explore the potential combination of the proposed methods with these existing models and highlight the advantages of the proposed approach. I believe that incorporating these insightful discussions would greatly enhance the paper.

### Questions
See weakness.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper suggests integrating weight-sharing NAS for the compression of pre-trained language models. This approach consists of three components: a weight-sharing super-network trained using the sandwich rule in conjunction with an in-place knowledge distillation (KD) strategy; a sub-network selection based on the Pareto front; and a varied search space, extending from a larger scope with masks applied to each head/neuron to a smaller scale focusing solely on the quantity of heads, units, and layers.

### Strengths
1. **NAS's Role in Compressing BERT**: A practical application for NAS is in the compression of BERT.
2. **Method Advantages for Sub-Network Selection**: This technique facilitates a multi-objective search for choosing multiple sub-networks, unlike earlier methods which allowed only single-network pruning and selection at a time.

### Weaknesses
1. **No experiments on LLM, but the topic of this paper is about LLM**. The title of the paper suggests a focus on Large Language Models , leading me to expect analyses or experiments involving LLMs like LLaMA, or at least T5-large, especially since the terms 'LLM' are predominantly used in the paper rather than 'language model' or 'pre-trained language model'. However, upon delving into the experimental section, it's surprising to find that the actual experiments exclusively involve **BERT**. There is no mention of LLMs in the experiment, nor is there any comparison or discussion on how the application of Neural Architecture Search might differ between LLMs and PLMs. The absence of experiments on models beyond BERT significantly limits the generalizability of the findings and raises questions about the practical applicability of the proposed method to the intended target of LLMs. The paper needs to clarify whether the method is expected to scale to LLMs, and if so, what specific challenges might arise and how they would be addressed. 

2. **More Baselines are needed**. The authors appear to have selected some baselines that may be relatively less challenging to outperform, such as Retraining-Free Pruning and self-defined baselines. Retraining-Free Pruning, focusing on rapid compression of BERT without retraining, isn't directly comparable with the methods in this paper, which involve around 12 hours of training (as indicated by 50,000 seconds in Figure 5) on the MNLI dataset. Moreover, the proposed method underperforms DistillBERT in more than half of the datasets (including MRPC, COLA, SST2, QNLI, MNLI). Other baseline methods are self-created, and there's a notable omission of any recent advancements in structural pruning methods for BERT in the past five years (e.g., DynaBERT, CoFi). Comparison with those methods are needed. Additionally, the related work section only references four papers on structural pruning for BERT, whereas the authors could have expanded their literature scope by referring to a broader survey[1] on this topic. The lack of comparison with state-of-the-art structural pruning techniques makes it difficult to assess the true novelty and effectiveness of the proposed NAS-based approach. The performance against DistillBERT, which is a well-established baseline, further highlights the need for more robust comparisons.

3. **Missing Important Comparison**. The paper misses an essential comparison with another study[2] that also employs NAS for compressing BERT. Given the relevance and slight methodological variation (NAS applied to pre-trained versus fine-tuned BERT) between the two studies, a comparison seems crucial. Both papers aim to achieve compression in downstream tasks, yet this paper lacks experimental evidence or analysis showing whether its method offers any advantages over the other one. This comparison is particularly pertinent since the approach to compression, whether on a pre-trained or fine-tuned model, could lead to different outcomes, and their exploration is essential for a comprehensive understanding. The absence of this comparison leaves a significant gap in the evaluation of the proposed method's contribution to the field.

### Questions
Could you clarify the process used to calculate the runtime for each technique as shown in Figure 5? The RFP (Retraining-Free Pruning) paper mentions that pruning takes merely 0.01 hour, approximately 36 seconds. However, in your study, this duration extends to about 20,000 seconds. What factors contribute to this substantial discrepancy in runtime measurements?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
