# Model merging with SVD to tie the Knots

- Decision: Accept
- Scores: 8, 5, 6, 6

## Abstract
Recent model merging methods demonstrate that the parameters of fully-finetuned models specializing in distinct tasks can be combined into one model capable of solving all tasks without retraining. Yet, this success does not transfer well when merging LoRA finetuned models. We study this phenomenon and observe that the weights of LoRA finetuned models showcase a lower degree of alignment compared to their fully-finetuned counterparts. We hypothesize that improving this alignment is key to obtaining better LoRA model merges, and propose \name{} to address this problem. \name{} uses the SVD to jointly transform the weights of different LoRA models into an aligned space, where existing merging methods can be applied. 
    In addition, we introduce a new benchmark that explicitly evaluates whether merged models are general models.
    Notably, \name{} consistently improves LoRA merging by up to 4.3\% across several vision and language benchmarks, including our new setting.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper titled "Model Merging with SVD to Tie the Knots" explores the challenge of merging Low-Rank Adaptation (LoRA) finetuned models. While model merging has shown success in combining fully-finetuned task-specific models, the same methods often fail when applied to LoRA finetuned models due to misaligned weight structures. To address this, the authors introduce KnOTS, a technique that employs Singular Value Decomposition (SVD) to align LoRA model weights, thereby improving the effectiveness of existing merging methods. KnOTS demonstrates up to a 4.3% improvement in merging performance across vision and language benchmarks. Additionally, the paper presents a new benchmark for assessing the generality of merged models, which evaluates their performance on a joint dataset combining multiple tasks.

### Strengths
1.  The concept of using SVD to align model weights for improved merging is novel and practical, addressing a previously unexplored limitation in merging LoRA models.
2. The paper is generally well-structured, with clear descriptions of both the KnOTS methodology and experimental setups.

### Weaknesses
1. It would be beneficial if the authors could validate the effectiveness of the method on larger LLMs, such as LLaMA and Qwen2, for more in-depth evaluation.
2. Although the method is effective, the improvements are limited.

### Questions
Please check the weakness.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper "Model Merging with SVD to Tie the Knots" proposes KnOTS, a method to improve merging of LoRA-finetuned models, which traditionally struggle with alignment compared to fully-finetuned models. KnOTS uses SVD to align task-specific updates into a shared space, making it easier to merge LoRA models effectively with existing techniques. The authors also introduce a benchmark to test whether merged models generalize across tasks, showing that KnOTS boosts merging performance by up to 4.3% across various benchmarks in vision and language.

### Strengths
* Model merging, specifically for LoRA models, is an interesting and cutting-edge field, with related techniques being widely proposed and explored in recent years.
* KnOTS shows excellent performance across both vision and language tasks, enhancing merged model effectiveness and enabling better generalization on the newly introduced benchmark for multi-task data.

### Weaknesses
* As far as I know, merging LoRA models using SVD is not a new technique; implementations have long been available in some open-source libraries and are widely used. Therefore, the innovation in this paper is questionable and appears limited. I'd like to know what are the differences and advantages of the techniques proposed in this paper compared to the SVD-based merging techniques in these libraries?

* The experimental work in this paper is insufficient and does not meet a certain standard; more experimental data is needed to support the authors' announced conclusions. Additionally, the writing quality needs improvement.

### Questions
See in Weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a new technique to merge the parameters of different LoRAs onto the same model weights. The authors first show that CKA representations better align with the ability to merge model weights, both for fully fine-tuned approaches as well as LoRA-based ones. Then, they propose to use SVD to align the subspaces of different LoRAs. After doing so, the resulting matrices can be merged into a single model by applying previous techniques. The authors show that their approach better merges LoRA weights into a single model, for both vision tasks and language tasks.

### Strengths
1. The authors show that CKA representations seem to align with model merging abilities, without some limitations given by orthogonality approaches.
2. The authors propose to merge the LoRA weights after SVD, and showcase better performance than using existing full-rank approaches.
3. The authors propose to evaluate merged models on a multi-task benchmark that they obtained by combining the individual datasets in Ilharco et al. (2023).

### Weaknesses
1. While the performance of KnOTS-TIERS is usually significantly better than TIERS, it is not the case for DARE-TIERS. This is not discussed in the paper, and it would be good to understand this behavior.
2. While the CKA alignment given by using KnOTS is significantly better than by the original LoRA weights, the performance improvements (e.g. on DARE-TIERS) are less pronounced, leaving the reader wondering whether CKA is indeed a good-enough metric for weight alignment.
3. The authors should down-weight their “novelty” contributions towards creating a new benchmark by simply putting together the datasets of a previous benchmark. The benchmark itself is a contribution of the paper, but not one that the reviewer feels should be stressed as much. For example, you could present it as a useful extension rather than a major novel contribution.

### Questions
1. Can you analyze and discuss potential reasons for the discrepancy in performance gains between KnOTS-TIES and KnOTS-DARE-TIES?
2. Why is the better CKA alignment given by KnOTS not resulting in better performance with KnOTS-DARE-TIERS? Are there additional analyses you could run to better understand the relationship between CKA alignment and performance across different merging method?
3. Can you provide more insights into why row-wise KnOTS does not work?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces a method called KnoTs which provides a strategy for merging LoRA modules. First the authors show that centered kernel alignment (CKA) between activations of LoRA modules is not as high as that of fully fine-tuned models, demonstrating the need for developing methods specially for merging LoRA modules. They propose to perform SVD on the task updates and perform merging operation on V matrix in the SVD which is known to contain task specific information. First they show that CKA on these V matrix is high and this would eventually help in improving merged model performance. They run experiments on both vision and language tasks to demonstrate the effectiveness of the method and their method achieves better normalized accuracy in comparison to other SOTA methods specially designed for merging fully fine-tuned models.

### Strengths
* CKA analysis provided in the beginning to show misalignment of weights in LoRA provides good motivation to develop specialized method for merging LoRA trained models.
* Proposes a merging method for combining LoRA modules using SVD decomposition on weight update matrix. Shows improvements over different merging baselines for both vision and language tasks. 
* KnoTs demonstrates superior scalability compared to other methods, particularly as the number of merged models increases.

### Weaknesses
* This method doesn't allow merging of LoRA modules with different ranks.
* The datasets used in this work are selected to ensure strong baseline performance, where models like ViT and Llama already demonstrate high zero-shot accuracy. This high initial performance makes it challenging to quantify the specific gains achieved through the proposed method.
* Multi-task trained performance should be considered as one of the baseline to understand how far is the merging performance from multi-task performance.

### Questions
* What is the motivation for performing merging operation on V matrix from SVD?
* Does the author believe that merging methods would have a greater negative impact if the base model’s zero-shot performance were lower?
* Is it possible to compare merged models performance to multi-task model performance on all the datasets?

### Soundness
3

### Presentation
3

### Contribution
2
