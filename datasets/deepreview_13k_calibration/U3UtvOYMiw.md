# Seeded LoRA: Collaborative Fine-Tuning Through Seed Initialization of Adapters

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 5, 5

## Abstract
Parameter-Efficient Fine-Tuning (PEFT) methods facilitate the cost-effective adaptation of pretrained language models to specific tasks and domains. These methods have enabled the open-source community to develop thousands of specialized models tailored to various domains and tasks. Collaborative Fine-Tuning (CoFT) is the paradigm that seeks to merge these specialized models into a single model -- often a routed Mixture-of-Expert (MoE) model -- to achieve better generalization across domains and tasks. However, current CoFT models require a post-merge fine-tuning stage to successfully combine existing models, making CoFT approaches inaccessible to users who lack fine-tuning expertise. In this work, we introduce Seeded LoRA, a novel CoFT approach that does not require post-merge fine-tuning thus enabling plug-and-play PEFT adapter merging. Seeded LoRA significantly outperforms LoRA and MoE LoRA (MoLoRA) approaches, improving by an average of 7 percentage points across a battery of 16 zero-shot tasks and we find that the main benefit from Seeded LoRA comes from mitigating task interference during finetuning. Seeded LoRA works by initializing a model before fine-tuning using a generic seed expert low-rank adapter which was finetuned on a small random subset of the finetuning data such that subsequent fine-tuning runs are initialized in the same optimization subspace. This process enables the integration of any combination of independently fine-tuned models through simple averaging of expert adapter outputs. We show that averaging, or routing with assigning equal probability weights to each expert, is equivalent to grouped convolution, explaining its effectiveness. Additionally, we study subtle routing failures in post-merge fine-tuning and highlight that Seeded LoRA can alleviate most routing failures, making it a suitable base method for future routed CoFT approaches.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
Seeded LoRA is proposed to improve the performance of LoRA without post-merging fine-tuning. The method can be divided into 2 steps:
1. Random sample 5-10% of SFT training data to train seed LoRA weights.
2. The weights trained in step 1 are used to do task-specific fine-tuning separately to get N expert models.
- At inference time, the inference results from each LoRA module are aggregated through the arithmetical average and added with the original LLM weights to get the final inference results.
Experiments showed that this method achieved better performance when compared with the original LoRA and MOE LoRA with router mechanism.

### Strengths
This work proposes Seeded LoRA as a multitask fine-tuning method without post-merging fine-tuning. The method is composed of 2 steps:
1. Random sample 5-10% SFT training data to train a seed LoRA module to be used as common ground for task-specific fine-tuning.
2. Use the LoRA weights from step 1 to fine-tune LLM on multiple tasks separately
- At inference time, the outputs from each LoRA module are aggregated through simple averaging and sent to the decoder without post-tuning to generate the results.
Experiments showed the proposed method is better than the original LoRA or MOE LoRA method with a routing module.

### Weaknesses
 - Novelty seems to be limited. As is cited in the paper, the work seems to be a simple adoption of the model soup method [1] from whole model fine-tuning to LoRA fine-tuning. In the original paper, multiple model candidates are averaged to generate better model parameters. Here we simply replace the whole LLM weights with the LoRA module weights.
- Experiments seem to be insufficient. For example, the LoRA weights from different experts are averaged arithmetically. Intuitively, for different tasks, the weights of each expert should be different during aggregation. Even without a routing module, a set of learnable weights might be helpful to improve the final inference performance. Furthermore, the hyperparameter settings for each task-specific LoRA fine-tuning are not discussed. It is highly likely that each task would benefit from different learning rates, batch sizes, or other optimization parameters. This could significantly impact the performance of the final averaged model and should be explored more thoroughly.

### Questions
- The current setup is also connected with MAML (model agnostic meta-learning [2]), which is targeted at learning a set of initialization weights, and for each downstream task, only a few examples will be sufficient to achieve good performance. Instead of random sampling, is it possible to apply the idea of MAML here to find the best seed LoRA weights?

[2]Finn, Chelsea, Pieter Abbeel, and Sergey Levine. "Model-agnostic meta-learning for fast adaptation of deep networks." International conference on machine learning. PMLR, 2017.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces a novel method for collaborative fine-tuning that eliminates the need for costly post-merging fine-tuning, typically required to enhance the accuracy of merged models. The authors contribute by demonstrating that initializing a model within the same optimization subspace ensures that domain- or task-specific fine-tuning preserves this shared subspace. Consequently, the final model can be obtained as a straightforward average of experts, rather than relying on complex routing mechanisms, as seen in mixture-of-experts (MoE) models. The authors named their method Seeded LoRA.

The authors propose seeding the initial model using a random subset of datasets from multiple tasks, then creating a mixture of experts using their proposed approach. Experimental results demonstrate that this method surpasses alternative techniques, including LoRA and MoLoRA.

### Strengths
Strengths of the paper:

1. *Conceptual Foundation of the Approach*: **Seeded LoRA** is based on the concept of ensuring a shared optimization subspace across different tasks. This alignment allows the weights of the fine-tuned models to be linearly combined, resulting in a model resembling a mixture-of-experts (MoE) without complex routing mechanisms.

2. The Proposed Framework is **simple** to understand and **intuitive**. 

3. Experiments showing the efficacy of the proposed approach are shown on LLaMa 2, using a variety of tasks including inference, reasoning, and QA. 

4. Limitations and applications of the proposed method are well documented.

### Weaknesses
These are some Weaknesses in my opinion:

1. Results are currently presented on only one model, and that is an older version of LLaMa. It would strengthen the paper to include evaluations on newer models, such as LLaMa 3, Vicuna, or Bloom, or even on smaller models like RoBERTa with fine-tuning instead of instruction tuning. Testing across 1-2 additional open-source models that support fine-tuning or instruction tuning could provide a broader and more relevant context for the findings.

2. Unfair comparisons, especially LoRA(mixture). Please check the question below regarding this weakness.

3. Limited ablation studies. Impact of the percentage(5% vs 10%, mentioned in the paper but no experiments) of seed dataset, different datasets used in seed dataset(using a subset of dataset not data samples for seeding), biased sampling(sampling more from one dataset than other), etc etc. There are a bunch of parameters that can affect the performance of the proposed method which are not shown. Refer to Question 2 for more details of this weakness.

### Questions
These are some of the areas that weren't very clear to me or results didn't make sense:

1. When fine-tuning with LoRA (mixture), are you using a single adapter, or does the number of adapters match LoRA (individual)? Explaining in more detail would clarify the doubt.

Based on the results, I guess that it is a single adapter is used for the entire LoRA (mixture) dataset, with an increased rank. However, this may not provide a fair comparison, as the diverse gradients from different tasks could impact model performance, with the sampling strategy and dataset ratio playing significant roles in final accuracy. This might explain why the model shows zero accuracy on mathematical tasks. Instead, I suggest a variant of LoRA (individual) in which all LoRAs are applied simultaneously during fine-tuning on the mixture dataset. Would this approach allow each LoRA to automatically specialize for distinct tasks during convergence? even if it doesn't, I think this would be a fair comparison.

2. While I agree that initializing or seeding the model with a dataset can yield better initializations, isn’t a trained model already positioned within an optimized subspace? How, then, would additional seeding impact performance? Furthermore, wouldn't a new seed be necessary whenever a new dataset or task is added to the mixture?

(a) A crucial ablation study would be to evaluate performance on out-of-distribution datasets. Here, I’m referring to datasets outside the current mixture but within the same task scope, such as other inferences or QA sets. This would clarify whether re-seeding is essential for a new dataset of the same task.

(b) For a completely new task, however, I would certainly expect that re-seeding would be required, but proving that with an ablation would make the experiment section stronger. Assess the impact of adding new datasets or tasks to the mixture without re-seeding. These experiments would provide valuable insights into the robustness and generalizability of the Seeded LoRA approach.



3.I am uncertain about the purpose of Section 7, as it seems to add little beyond what was already covered in Seeded LoRA. The section does not enhance my understanding of why Seeded LoRA offers a distinct advantage. Moving this content to the Appendix may be more appropriate, as the findings appear to be either known or intuitive enough to understand without a dedicated section.

### Soundness
3

### Presentation
2

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
This paper introduces Seeded LoRA, a novel Collaborative Fine-Tuning method that eliminates the need for post-merge fine-tuning of large language models. Specifically, Seeded LoRA generates a generic seed expert LoRA that is fine-tuned on a small random subset of the dataset, which is then used to initialize other downstream task LoRAs. Extensive experiments on natural language processing benchmarks demonstrate the effectiveness of Seed LoRA.

### Strengths
The idea of the proposed Seeded LoRA seems to be simple and effective. The analysis of routing failures in MoLoRA is also impressive. The paper is well-written and easy to follow.

### Weaknesses
1. The paper should discuss how CoFT relates to and differs from multi-task/continuous learning, which also aims for improved model performance. A summarizing table could emphasize the necessity of the CoFT task.

2. In Dataset-Specific Expert fine-tuning, does the seeded LoRA recognize the dataset during training (thereby updating domain-specific LoRA)? If so, it may introduces extra information about data distributions, making comparison unfair in Table 1. Specifically, the method uses dataset attribute information to determine which samples belong to which dataset, which is not available to methods like MoLoRA. This gives the proposed method an unfair advantage, as it leverages explicit dataset labels during training, while MoLoRA operates without such information. While supplementary experiments explore unsupervised domain discovery, the potential for MoLoRA to benefit from similar dataset information remains unaddressed, making the comparison incomplete.

3. The authors' approach of using the same subspace for initializing task-specific LoRAs opposes O-LoRA's method of using orthogonal subspaces and merging them after continued learning. More discussion and comparison with O-LoRA are needed.
[1] EMNLP24 Orthogonal Subspace Learning for Language Model Continual Learning

### Questions
Please see the weakness section.

### Soundness
3

### Presentation
3

### Contribution
2
