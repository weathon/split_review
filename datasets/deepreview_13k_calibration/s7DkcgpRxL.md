# Train Small, Infer Large: Memory-Efficient LoRA Training for Large Language Models

- Decision: Accept
- Avg Score: 6.20
- Scores: 8, 6, 3, 6, 8

## Abstract
Large Language Models (LLMs) have significantly advanced natural language processing with exceptional task generalization capabilities. Low-Rank Adaption (LoRA) offers a cost-effective fine-tuning solution, freezing the original model parameters and training only lightweight, low-rank adapter matrices. However, the memory footprint of LoRA is largely dominated by the original model parameters. To mitigate this, we propose LoRAM, a memory-efficient LoRA training scheme founded on the intuition that many neurons in over-parameterized LLMs have low training utility but are essential for inference. LoRAM presents a unique twist: it trains on a pruned (small) model to obtain pruned low-rank matrices, which are then recovered and utilized with the original (large) model for inference. Additionally, minimal-cost continual pre-training, performed by the model publishers in advance, aligns the knowledge discrepancy between pruned and original models. Our extensive experiments demonstrate the efficacy of LoRAM across various pruning strategies and downstream tasks. For a model with 70 billion parameters, LoRAM enables training on a GPU with only 20G HBM, replacing an A100-80G GPU for LoRA training and 15 GPUs for full fine-tuning. Specifically, QLoRAM implemented by structured pruning combined with 4-bit quantization, for LLaMA-3.1-70B (LLaMA-2-70B), reduces the parameter storage cost that dominates the memory usage in low-rank matrix training by 7.07× (8.21×), while achieving dominant performance gains over both the original LLaMA-3.1-70B (LLaMA-2-70B) and LoRA-trained LLaMA-3.1-8B (LLaMA-2-13B).

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper proposes LORAM, a memory-efficient training approach for Low-Rank Adaptation (LoRA) fine-tuning on large language models (LLMs). LORAM aims to reduce the memory burden during training by pruning the model parameters and then “recovering” them during inference. The technique includes an offline alignment process to minimize knowledge discrepancies between the pruned and original models, as well as integration with quantization to further optimize memory usage. Extensive experiments showcase LORAM’s performance across various tasks using models like LLaMA-2.

### Strengths
- LORAM aims to make LLM fine-tuning feasible on lower-memory devices, addressing a relevant challenge for the NLP community.
- The introduction of an alignment phase to handle pruning inconsistencies is conceptually innovative and could provide insights for future memory-efficient models.
- The authors conduct a broad range of experiments, which helps to illustrate LORAM’s performance across multiple tasks.

### Weaknesses
 - The paper contains frequent grammatical errors, inconsistent terminology, and formatting issues that detract from readability.
- The main technical idea—pruning during training and recovering for inference—lacks fundamental novelty and could be seen as an incremental step on existing methods rather than a breakthrough.
- The experimental setup would be more convincing with comparisons to simpler or standard pruning approaches, helping to illustrate LORAM’s distinct benefits more clearly.
- Testing LORAM beyond LLaMA models would make the approach more broadly applicable and better showcase its robustness across architectures.

### Questions
1. Could the authors provide specific examples of how LORAM compares to standard LoRA without any pruning? Same goes for QLORAM vs QLORA?
2. What influenced the choice of pruning ratios, and could different ratios impact the effectiveness of LORAM’s alignment step? Could the authors also clarify if any theoretical or empirical basis underlies the decision to use certain pruning ratios in LORAM? For instance, what drives the choice of an optimal parameter reduction ratio?
3. Are there cases where LORAM underperforms compared to standard LoRA? This would provide insights into LORAM’s limitations. As it is, I find it hard to wrap my head around the possibilities of LORAM winning in all scenarios.
4. How was the the alignment corpus chosen, and what effect does corpus size have on the performance of aligned models? 
5. How consistent are LORAM’s improvements across different tasks? Further analysis here would help illustrate LORAM’s potential.

### Soundness
3

### Presentation
1

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes “LoRAM,” a novel memory-efficient LoRA fine-tuning process that significantly reduces required storage by pruning base weights—an approach largely overlooked in prior LoRA research. To mitigate the discrepancy introduced by pruning, the authors introduce a recovery step to ensure alignment at inference time, thereby improving accuracy.

Compared to models with a similar effective parameter reduction ratio, LoRAM achieves a higher compression rate while demonstrating lower training/test loss and higher downstream accuracy on the LLaMA-2 family and LLaMA-3.1 models. Additionally, an ablation study shows that the proposed recovery and alignment steps contribute to improved training performance.

### Strengths
This paper introduces a novel approach to optimizing the heavy base weights in LoRA-based fine-tuning, an area not well-focused in existing LoRA studies. Moving beyond the widely studied quantization, the authors address the challenges of achieving high compression through pruning by introducing recovery and alignment steps, which help to offset pruning’s drawbacks and yield promising performance results. The method shows scalability potential, and the presentation and explanation are clear, making it easier to follow what might otherwise be a complex process. The experiments also appear to be thoroughly conducted.

### Weaknesses
- The paper lacks a discussion of the cost implications of the proposed method. Unlike standard one-stage LoRA fine-tuning, the multi-stage process in LoRAM may involve trade-offs in latency, but this is not adequately addressed. Given the focus on efficient training, a detailed comparison of memory and latency costs with baseline methods should be discussed. Specifically, the paper should provide a breakdown of the computational cost associated with the offline alignment phase, including the number of FLOPs, memory footprint, and time required. Furthermore, the online low-rank training phase should be analyzed in terms of its memory and latency costs, comparing it to standard LoRA fine-tuning under similar parameter reduction ratios. This analysis should include not just peak memory usage but also the latency and throughput during training and inference, considering the impact of the multi-stage process on overall efficiency.

- While the main table’s comparisons by compression ratio are understandable, the results should also include fine-tuning outcomes on same LoRAM’s target LLM, as seen in Figure 8. Including the performance upper bound of fine-tuning the same model without memory reduction would allow readers to better assess the trade-off between memory compression and performance. This is crucial for understanding the performance gap introduced by the pruning and recovery process. For instance, the paper should include results for fine-tuning LLaMA-2-13B with standard LoRA, alongside the LoRAM results, to quantify the performance degradation due to the proposed method. This comparison should be made for all models and datasets to provide a comprehensive view of the trade-offs.

- To elaborate on the need for comparison within the same model family: from the perspective of a model publisher, different sizes of LLMs are not just scaled versions but may be trained with distinct capabilities in mind, considering future usability (ex. LLaMA-3.1-8/70B vs. LLaMA-3.2-3B). Thus, comparing models with similar reduction ratios but different original capabilities may not be appropriate. For those who performing fine-tuning, it would be more informative to see how LoRAM compares to standard LoRA on the same model, as this would directly reflect the practical value of the method. (I’m open to counterarguments if there’s a rationale for this choice.)

### Questions
- Was a comparable grid search conducted for hyper-parameter tuning (learning rate, epochs) for both baseline LoRA and LoRAM? Fine-tuning can be sensitive to settings, so the degree of granularity in hyper-parameter tuning might impact the final performance.
- I am curious about whether this method would also yield effective results for domain-specific fine-tuning tasks.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper introduces LORAM, a training method that refines a pruned model by adjusting the low-rank pruned matrices and then reintegrates dimensionally restored low-rank matrices with the original model for inference. This approach greatly reduces memory demands from model parameters during training and enhances performance by utilizing all original parameters during inference. Consequently, LORAM effectively improves performance on devices with limited memory capacity. Extensive experiments across diverse pruning techniques, model sizes, and task domains demonstrate LORAM's effectiveness.

### Strengths
1. The paper is well-written and comprehensively analyzes various adaptations of the proposed method to accommodate different pruning techniques.
2. This paper conducted thorough experiments across various pruning algorithms, models of different sizes, and tasks.

### Weaknesses
1. The novelty of this paper is limited as the proposed approach essentially combines existing pruning techniques with LoRA.
2. The claim that LoRAM substantially reduces the number of trainable parameters compared to standard LoRA is somewhat misleading. In the case of unstructured or semi-unstructured pruned models, there is no actual reduction in trainable parameters, as noted in the paper. Meanwhile, the reduction in trainable parameters when fine-tuning structured pruned models is due to the smaller dimensions of these pruned models compared to the original model, rather than any change in the LoRA component, which remains the same as in standard LoRA.
3. Could you explain why, after fine-tuning, structured pruned models outperform semi-structured and unstructured pruned models? In previous studies, like SparseGPT, Wanda, and LLM-pruned, unstructured pruning has consistently shown the least accuracy degradation. However, in your case, the results seem to be the opposite after finetuning.

### Questions
Please refer to Weaknesses.

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
The paper proposes LoRAM, a memory-efficient training scheme that combines pruning, LoRA-based training on the pruned model and subsequent integration of the found solution back in the original model. This procedure yields significant memory reduction compared to LoRA-based fine-tuning, which in turn was already an improvement over the full-model fine-tuning.

Authors further observed that under aggressive pruning rates their method did not work well and identified that the main culprit is inconsistency between the pruned model used for training and the original model used for inference. To combat this, they train the pruned model on a relatively small corpus to achieve alignment, which is a one-shot offline process.

The effectiveness of LoRAM is evaluated across several model sizes, pruning algorithms, and tasks in different domains.

### Strengths
* The paper is fairly well structured and well written. Visualizations are quite helpful for quickly grasping the method.
* LoRAM enables training a 70B model on a GPU with only 20GB, which is an impressive result.
* The proposed method is complementary with other memory reduction techniques such as quantization and pruning strategies.

### Weaknesses
 * Some comparisons in Tables 1-3 seem unfair: It would be nice to include a baseline that uses the same total training time/compute as LoRAM (including alignment & LoRA-based fine-tuning of the pruned model), but for full fine-tuning of the original model. This is crucial for a fair comparison of the method's efficiency, as it's unclear if the gains are solely from the method or simply due to reduced training time. The current comparisons do not account for the computational cost of the alignment phase, which should be factored into the overall evaluation.
* Aside from the trivial “w/o FT” baseline, it seems that LoRA is the only method LoRAM is compared against. It would be nice to include more baselines from the literature. For instance, would be interesting to compare LoRAM to the respective pruning method used to see the effect of subsequent LoRA training. This would help isolate the impact of the LoRA training step after pruning, and determine if the performance gains are truly due to the proposed method or simply the combination of pruning and LoRA.
* The paper did not report the training speed LoRAM compared to LoRA and full-model fine-tuning. Having a comparison of wall-clock time and/or throughput (e.g. tokens/second) for LoRAM vs LoRA and full fine-tuning across a few model sizes would give a more complete picture of the trade-offs. Without this, it is difficult to assess the practical benefits of the method in terms of training time and resource utilization. The lack of this comparison makes it hard to determine if the memory savings come at the cost of significantly increased training time.
* It would greatly help to increase the reproducibility of this work by releasing the code.

### Questions
* In Figure 3 & 4, any reason for instability for QLoRAM-Rand & QLoRAM-Stru for 70B model when evaluated on Alpaca?
* Seems there is a typo in Table 3: 0.3415 should be 34.15

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This work proposes a memory-efficient training scheme for LLMs, named LoRAM. Based on an intuition that some parameters remain unchanged during finetuning, but are important during inference, the authors train a pruned model by updating the pruned low-rank matrices and then uses recovered matrices for inference. In this way, the parameters need to be finetuned can be largely reduced while achieving similar accuracy compared with previous LoRA methods.

### Strengths
-Memory efficient training is an important topic in LLM-related fields.

-This paper proposes an easy but effective method to reduce the number of parameters which need to be finetuned.

-The potential this sparsity-based method shows when combined with QLoRA seems a promising way for this field.

-The paper is easy to follow, experiments presented are good.

### Weaknesses
 -My major concern is that why cannot train small and infer small? Training small is convincing enough, but it sounds more reasonable to me that we train on the pruned model, and then also infer on that model. I think it is indispensable for this paper to show the certain benefits of inferring large over inferring small. Detailedly, experimental results (e.g. model accuracy or inference latency) are needed for the comparison of inferring small and inferring large, so that the inference design can be convincing.

-This idea is based on the intuition that some parameters remain unchanged during finetuning, but are important during inference, although the proposed method seems to work, there is no evidence to show the phenomenon and no theoretical analysis to show the reason of the phenomenon. What is the property of those unchanged weights? This paper will be much better with more effort on this part.

### Questions
-What is the training throughput of your method? Updating pruned parameters seems time-consuming generally.

### Soundness
3

### Presentation
4

### Contribution
3
