# LLM Pruning and Distillation in Practice

- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 6, 3

## Abstract
Structured pruning with knowledge distillation is a potent combination for obtaining small language models (SLMs) with significantly fewer training tokens and compute resources compared to training from scratch. In this work, we investigate how this strategy can be effectively applied in instances where access to the the original pretraining dataset is restricted. We introduce a new *teacher correction* phase before distillation which lets the teacher model adjust to our specific data distribution using a lightweight fine-tuning phase. We apply this strategy to compress the Mistral NeMo 12B and Llama 3.1 8B models to 8B and 4B parameters, respectively, using pruning and distillation. We explore two distinct pruning strategies: (1) depth pruning and (2) joint hidden/attention/MLP (width) pruning, and evaluate the results on common benchmarks from the LM Evaluation Harness. The models are then aligned with NeMo Aligner and further tested for instruction following, role-play, math, coding and function calling capabilities. This approach produces the state-of-the-art Mistral-NeMo-Compressed-8B (\MNMinitron for brevity) model from Mistral NeMo 12B, and a compelling 4B model from Llama 3.1 8B.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper studies the combination of structural pruning and knowledge distillation to obtain compressed and performant language models with higher throughput. The paper proposes a "teacher correction" to allow for lightweight finetuning of the teacher model (a llama-3.1-8B or mistral nemo 12B). The step is proposed with the goal of adapting the distribution of the teacher to the domain of the finetuning data before the distillation step to a smaller model. Furthermore, the paper uses different saliency metrics to compute importance of depth and intermediate mlp/attention/width dimension and sort the teacher in order of importance, before applying pruning. In addition, the paper also explores different saliency metrics for improved depth pruning. The pruned models are evaluated on a wide variety of commonsense, math and instruction tuning tasks.

### Strengths
Experiments
- The paper evaluates the proposed teacher correction scheme on different models (llama-3.1-8B and mistral nemo 12B) for a more thorough study of effectiveness of distillation (pre-corrected or continuously corrected)
- Detailed evaluation of gains from different components random student initialisation, importance sorting and knowledge distillation
- Exhaustive evaluation on different tasks

Writing
- Paper is written in an easy to understand manner in most parts

Originality and significance 
- While most parts of the paper are similar to/derive from observations in [1], the empirical investigation into precise gains by each of the components is interesting and significant. 

[1] Muralidharan, S., Sreenivas, S.T., Joshi, R., Chochowski, M., Patwary, M., Shoeybi, M., Catanzaro, B., Kautz, J. and Molchanov, P., 2024. Compact language models via pruning and knowledge distillation. arXiv preprint arXiv:2407.14679.

### Weaknesses
Originality and Significance
- A lot of this work is similar to  [1], including importance sorting, architecture selection procedure, distillation loss
- Domain adaptation of a teacher is also studied in [2] for BERT like models and I don't find the proposed teacher correction to be significantly different from the idea of adapting a teacher to a specific domain on interest
- The idea of dropping last contiguous layers (except the last layer) have been studied in [3] and the scheme chosen here is similar to the scheme chosen in the paper. Is my understanding correct and could the authors present the key differences/observations here?

Experiments
- Check questions section, I think the paper would benefit a lot from adding comparisons to similar small sized models, trained from scratch. 

Clarity
- While the paper is written in an easy to understand manner in most parts, I am lacking a cohesive story of the overall approach of the paper. Could the authors provide an algorithm describing the final/best performing choices for pruning+distillation? 
- Could you elaborate on the following points which are ambiguous/unclear : 167-168, what are the architecture related learnings, how was the student designed?  Line 133-134, which calibration set is used, does the domain of the calibration set matter? "continuously corrected teacher", is not defined properly in the paper, is the teacher periodically updated? line 312-313, what is the general scheme used for pruning different teachers, which contiguous layer indices are to be dropped?

Scaling to larger models
- As per my understanding the paper studies only full fine-tuning (FFT) of the teacher model, for teacher correction. However, this does not scale to larger models (eg: llama-3.1-70B) due to memory/compute constraints and hence cannot exploit larger/better teacher models.
- While the authors do mention the possible use of Parameter-Efficient-Fine-Tuning (PEFT) schemes like LoRA[4] and Galore[5], I think given the focus of the paper on large language models, generalisability of the observations in the paper for PEFT schemes on even larger language models, should be studied in detail. 

Code and Reproducibility
- The models are finetuned and distilled on a proprietary dataset, how do the observations translate to public datasets eg: openwebtext or finetuning datasets like alpaca, commonsense170k, math10k?
- The paper does not release the code and experimental pipeline for their work and I encourage the authors to do this to increase the impact and adoptability of their work.

### Questions
- Given the newly released llama-3.2-1b and llama-3.2-3b and ministral-3b models, could the authors compare against these model families?
- I currently lack a concrete answer to the question : Does a (student) model pruned and distilled from a larger model outperform a (student) model of similar size trained from scratch on a pretraining dataset? Could the authors elaborate on their observations here? 
- Have the authors tried to replace full-fine-tuning with PEFT techniques like LoRA[1] and Galore[2]? If yes do the observations about distillation and importance sorting hold there?
- Could the authors provide on-device latency gains using the pruned models eg: on a A100/H100?

I am willing to raise my score if the authors adequately respond to my questions and the weaknesses pointed out above.

[1] Hu, E.J., Shen, Y., Wallis, P., Allen-Zhu, Z., Li, Y., Wang, S., Wang, L. and Chen, W., 2021. Lora: Low-rank adaptation of large language models. arXiv preprint arXiv:2106.09685.

[2] Zhao, J., Zhang, Z., Chen, B., Wang, Z., Anandkumar, A. and Tian, Y., 2024. Galore: Memory-efficient llm training by gradient low-rank projection. arXiv preprint arXiv:2403.03507.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper addresses an increasingly important challenge in the field of large language models (LLMs): how to effectively compress models when access to the original training data is restricted. The authors present a practical approach combining structured pruning and knowledge distillation, introducing several notable innovations in the process. The key contributions include a novel "teacher correction" phase for adapting the teacher model to target dataset distribution, an improved depth pruning saliency metric based on downstream task performance, and empirical validation through compression of Mistral NeMo 12B to 8B and Llama 3.1 8B to 4B parameters.

### Strengths
- The paper introduces teacher correction as an innovative solution for compressing models without original training data access - a common industry challenge with proprietary models. The approach is elegantly simple yet effective, requiring only ~100B tokens for adaptation and integrating smoothly into existing distillation pipelines. This practical focus makes the method immediately valuable for real-world applications.
- The results show impressive efficiency gains with the MN-COMPRESSED-8B achieving SOTA performance using 40× fewer training tokens, and LLAMA 3.1-COMPRESSED-4B showing competitive results with 150× fewer tokens. The method delivers significant speedups (2.7× for depth pruning, 1.8× for width pruning) while maintaining strong performance across diverse tasks including reasoning, coding, and instruction following.

### Weaknesses
 - The performance degradation observed in the compressed models is substantial, especially considering the modest compression ratios achieved. When compressing Llama 3.1 8B to 4B parameters (only a 2x reduction), the MMLU performance drops notably from 65.3% to 60.5% with width pruning, or even lower to 58.7% with depth pruning. This performance drop is particularly concerning when viewed against recent developments in the field - for instance, MobileLLM-350M demonstrates that it's possible to achieve comparable performance to LLaMA-v2 7B in specific tasks with a model that's 20 times smaller. The fact that this paper shows significant performance degradation with just 2x compression, while requiring additional fine-tuning, makes the proposed approach less compelling for practical applications.

- The evaluation of the method's effectiveness is hampered by insufficient baseline comparisons. The authors should have compared their approach against a broader spectrum of existing compression techniques, including various pruning approaches, quantization methods. Specifically, a comparison against methods that also utilize knowledge distillation would be beneficial to isolate the impact of the proposed teacher correction and depth pruning saliency metric.

- The paper's experimental scope is also notably limited. While the authors validate their approach on two recent and popular models (Mistral NeMo 12B and Llama 3.1 8B), they don't explore more aggressive compression scenarios such as creating sub-1B parameter models, which would be particularly valuable for resource-constrained deployments. Furthermore, the evaluation is limited to a relatively small set of downstream tasks. A more comprehensive evaluation across a wider range of tasks, including more specialized domains, would provide a more robust assessment of the method's generalizability.

### Questions
- Why Winogrande was chosen over other potential downstream tasks?
- How sensitive is the method to the choice of downstream task for depth pruning?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper explores the practical application of structured pruning and knowledge distillation to compress large language models (LLMs) efficiently. The main goal is to create smaller models with fewer parameters while maintaining performance, even when the original pretraining dataset is unavailable. To achieve this, authors proposed

**Teacher Correction**: A novel phase where the teacher model is fine-tuned with a small amount of new data to adapt to the specific distribution of the target dataset. This improves the distillation process when the original training data is inaccessible.

**Pruning Strategies**: Authors explored two pruning strategies, including depth pruning and width pruning with their proposed importance measurement for each component.

### Strengths
1. The authors provide their base model on Hugging Face, and based on this, the results seem promising.

2. Teacher correction can improve the effectiveness of distillation when the original data is unavailable, as demonstrated with Llama 3.1 8B and Mistral NeMo 12B.

3. The authors propose a new method for measuring importance in pruning, but there seems to be a lack of comparison with other methods for evaluating LLM importance.

### Weaknesses
1. This paper does not follow the ICLR 2025 style guidelines, which could be a serious reason for desk rejection.

2. The overall writing is somewhat unclear. I believe the writing could be improved, and some details in the paper also need enhancement, including the proper use of \citep and \citet, as well as capitalization at the beginning of sentences.

3. The reasoning behind the improvement from teacher correction is not very clear. Even though it is a crucial component of the work, it seems to only apply to a single case. I recommend that the authors provide more analysis or experiments demonstrating the effectiveness of teacher correction across different models or datasets. This would help establish whether the improvement is generalizable or limited to a specific case.

4. Overall, the main components of the paper—distillation and pruning—appear to overlap significantly with previous works, particularly Sheared LLaMA, which first proposed efficient training using distillation and pruning. However, the paper does not cite this work.

### Questions
1. There are several methods for measuring the importance of layers, including SLEB, Shortened LLaMA, and ShortGPT. For a stronger publication, I suggest that the authors include a comparative analysis section that directly compares their proposed importance measurement method with these existing methods on a common set of metrics or benchmarks.

2. Is there any empirical validation for the authors' argument: "We hypothesize this is due to the change in the distribution of sub-word tokens across the original dataset the teacher model was trained on versus the dataset being distilled on"? I recommend that the authors provide quantitative evidence of the token distribution differences between datasets and demonstrate how these differences correlate with the effectiveness of teacher correction.

### Soundness
2

### Presentation
1

### Contribution
2
