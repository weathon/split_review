# Don't Pre-train, Teach Your Small Model

- Decision: Reject
- Scores: 3, 3, 1, 5

## Abstract
In this paper, we reconsider the question: What is the most effective way to train a small model? A standard approach is to train it from scratch in a supervised manner on the desired task for satisfactory results at a low cost. Alternatively, one can first pre-train it on a large foundation dataset and then finetune it on the downstream task to obtain strong performance, albeit at a much higher total training cost. Is there a middle way that balances high performance with low resources? We find the answer to be yes. If, while training from scratch, we regularize the feature backbone (and optionally task-specific head) to match an existing pre-trained one on the relevant subset of the data manifold, a small model can achieve similar or better performance than if it was completely pre-trained and finetuned. We achieve this via a novel knowledge distillation loss based on the Alignment/Uniformity theory of contrastive learning by Wang & Isola (2020), which we use to transfer the knowledge of the task dataset augmented with synthetic inputs generated from existing pre-trained diffusion models. Across 6 image recognition datasets, utilizing pre-trained convolution and attention-based teachers from public model hubs, we show significant improvements to small model performance at a slightly higher cost than supervised learning from scratch. Seeing as our method can hold its weight against, and often surpass, the pre-training regime, we refer to our paradigm as: Don’t Pre-train, Teach (DPT).

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper revisits the optimal approach to training small models and proposes a middle ground between traditional supervised training from scratch and the resource-intensive pre-training followed by finetuning. By regularizing the feature backbone of a model being trained from scratch to align with an existing pre-trained model, and using a knowledge distillation loss rooted in the theory of contrastive learning, the authors demonstrate good performance for small models across six computer vision datasets.

### Strengths
* The question of effectively training small models is crucial in the drive for resource-efficient methodologies. This paper's approach is commendable for addressing this challenge.
* The proposed training method is based on the solid theory and is well embedded into related work. Comparison to recent SoTA is highly appreciated.

### Weaknesses
 * While the technical progress in efficient model training is appreciated, the delta to existing works is rather small, leading to limited novelty.
* The claim of general applicability might benefit from a more diverse testing. Relying on only 6 computer vision datasets and a handful of teacher-student architectures narrows the perspective. It is unclear if the method would generalize well to other modalities or tasks beyond image classification. The limited range of architectures tested also raises concerns about the robustness of the method across different model families (e.g., recurrent networks, graph neural networks).
* The variability in the results, as seen in Fig. 4 and Tab. 2, 3, 5, and 6, makes it challenging to draw clear conclusions. The results provided in the appendix (Tab. 5 and 6) show better performance of CRD++. S-LP is not defined in the text. The lack of clear trends and the seemingly inconsistent performance across different settings make it difficult to assess the true effectiveness of the proposed approach.
* It would be helpful to have clarity on the number of experiments behind each reported measurement and the inclusion of standard deviations. The absence of statistical significance measures makes it difficult to determine whether the observed differences in performance are meaningful or simply due to random variations.
* "small models" and cost considerations need to be clearly defined. The paper seems not to account for certain factors that contribute to the total cost, such as training the existing pre-trained models. The definition of 'small' is vague, and it is not clear what the computational budget is for the method. The cost of obtaining the pre-trained teacher model is also not considered, which is a significant factor in real-world applications.
* How does the method compare to NAS or pruning (given limited space or a constraint on the inference time)? The reviewer believes the problem of training a "small model" for a specific domain needs a more holistic approach. Considering both learning methods and architectural choices, might offer a more comprehensive solution for edge and mobile devices. The proposed method looks at the problem in a limited way by considering training / data aspects only. The paper does not address the trade-offs between the proposed method and other model compression techniques, such as network pruning or neural architecture search, which are also crucial for resource-constrained environments.
* While synthetic samples do enhance performance, it remains unclear if baselines are also exposed to them during training, raising questions about fairness in comparisons.

### Questions
See weaknesses.

### Soundness
2 fair

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a new method on training small models without pre-training them on large datasets. The authors first use a pre-trained teacher model that is fine-tuned for the desired task and regularise the student model to match its behaviour via a contrastive-based knowledge distillation loss. Showing that the proposed method, called Don’t Pre-train, Teach (DPT), the authors claim that it can achieve similar or better performance than pre-training and finetuning while saving significant resources and time.

### Strengths
1. The paper is well-written and easy to understand.

2. The method proposed in this paper is technically sound to me.

### Weaknesses
 **1. Absence of crucial references and an insufficient comparison with state-of-the-art methods in knowledge distillation.**

While the author has touched upon various studies in the domain of knowledge distillation, the discussion appears to be incomplete. For example, works such as [1, 2] that delve into efficient (pre-)training via knowledge distillation techniques, have already revealed that knowledge distillation can be used as an effective technique to boost the training efficiency for tasks including image classification, object detection and semantic segmentation. 

In a closely related domain, active knowledge distillation can, to a degree, achieve the objectives set by the authors, making it imperative to discuss and compare with studies like [3]. Specifically, the paper should address how the proposed method handles the challenge of 'forgetting' previously learned information, a key concern in active learning scenarios, and whether the method is robust to the selection of synthetic data, given that the quality of synthetic data can vary significantly.

**2. The observation offered by the authors in this paper is not novel to me.**

Considering these pertinent studies listed above, the main contribution of this paper, *i.e.* employing distillation for expediting the training process, doesn't strike me as particularly novel. One new aspect of this paper is the authors' use of solely synthetic data for distillation. However, this shift in data source doesn't seem substantial enough to stand as the core contribution for a paper published at ICLR. The paper lacks a clear articulation of how the use of synthetic data offers advantages beyond simply reducing the reliance on real data, especially given that the generation of high-quality synthetic data is itself a complex and computationally intensive task.

**3. The experimental results presented in this paper are somewhat underwhelming to me.**

In light of the benchmarks set by leading methods in the realm of knowledge distillation, the performance depicted in this paper feels somewhat middling. For instance, when employing ResNet-18 as the student and ResNet-50 as the teacher, [1] manages to attain 82.22% in a mere 16 GPU hours. In contrast, this paper's proposed technique takes over 24 GPU hours to reach a modest 75.8%. A more thorough analysis of the computational cost-benefit is needed, considering not just the training time, but also the resources required for synthetic data generation. Furthermore, the paper should include a more detailed ablation study on the impact of different synthetic data generation strategies and their effect on the final model performance. While I concede that there might be nuances that make a direct comparison slightly skewed, it remains necessary for the authors to validate their approach in comparable scenarios and surpass at least one of the aforementioned studies. One experiment that might be needed is to merge the real and synthetic data and then apply the proposed method of this paper to see whether the proposed method can surpass the previous works in knowledge distillation.

### Questions
See weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
1

### Rating Number
1

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes distillation from a pretrained model finetuned on a target task at hand alongside training on additional synthetic data from a large generative model in order to train a smaller, equi- or even higher-performant model. They also propose a variation of existing contrastive distillation motivated by the uniformity & alignment objective proposed in Wang et al. 2020.
Leveraging large-scale pretrained models both as teacher and for data generation, the authors show strong performance gains for smaller base models (MobileNetV2 & ResNet18).

### Strengths
The paper is overall well structured and presented, being consequently easy to parse and understand.

### Weaknesses
I have several large issues with this work, which primarily stem from the lack of novelty.

* In particular, the proposed scenario, in which one distills from a teacher model which was pretrained ahead of time before being adapted to the target task at hand, is essentially just the standard distillation setting with the ONLY difference being that the teacher starts from pre-training. 

* Are there any significant differences in the insights gained or the difficulties surrounding the distillation process that require such a separate treatment (beyond the fact that distillation from teachers that were pretrained ahead of time is in itself not novel)? 

* Furthermore, the proposed distillation objective appears very derivative of contrastive distillatio proposed in Tian et al. 2020. It would be important if the authors provided a stronger differentation here.

* Similarly, the use of synthetic data to help train a model is orthogonal and not novel, and has been studied to significant extend, particularly with recent improvements in large-scale generative modeling as the authors also note in their related works. However, just deploying this to the task of Knowledge Distillation is an insufficient contribution.

* Beyond the lack of novelty, the experiments are also unfortunately quite lackluster - for a claim that involves applicability to "any pretrained teacher model", only testing on two teachers does not provide sufficient breadth. In addition, I'm not sure if the provided results are comparable - is synthetic data also used for the base finetuning of the teacher models, which are then claimed to be outperformed by the student using large-scale synthetic data? 

* Adding to that, just training a linear probe on top of a teacher is insufficient exploration into teacher finetuning to claim sufficient adaptation to a target task at hand, particular when distribution shifts are larger.

* Finally, I have some issues regarding formulations used in this paper, starting at the title iself, which is contradictory to what is actually proposed, as the introduced setup does leverage pretraining TO teach and for synthetic data generation. Beyond that, the authors sell knowledge distillation as the primary means for suitable model deployment on edge devices to leverage smaller architectures, disregarding research into model quantization, pruning, etc. It would be great if this could be contextualized better.

### Questions
In order for me to raise my score, the issues with respect to the lack of novelty as listed above have to be addressed, alongside a discussion about the significance and relevance of the experimental results.

### Soundness
3 good

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a way to effectively train smaller models when pretrained model for particular architecture is not available off-the-shelf.  There are three main components to their approach (1) fine-tune teacher model on desired task using linear probing (2) use contrastive learning to distill specific knowledge from teacher to student model (3) use artificially generated samples using generative models to get performance boost. They demonstrate that the above approach is beats student model pretrained and linearly probed both in terms of accuracy and GPU days.

### Strengths
- Combines different approaches in literature to create a recipe for training smaller models in the era of large models.
- Proposes a contrastive learning based training technique which might be helpful when we don't have pretrained models available for certain specific architectures.
- The paper is well written and easy to understand.

### Weaknesses
 - Baselines considered for experiments seems weaker. I would have liked to see the comparison between student model which is pretrained and fully fine tuned vs DPT (2x).
- Datasets considered in the paper are such that we can easily use generative model to create more data. The approach might not give good performance in cases where we don't get good images using generative models.

### Questions
- From a practical standpoint where do you think this method might be helpful? Because of the models considered in the paper have pre-trained counterparts available off-the-shelf i.e cost of pretraining is already paid and you only need to fine tune these models to downstream tasks.
- In this case synthetic data generation is a key step in boosting performance. In some datasets generative models might not be able to do good job in adding more synthetic data. Would the approach usefulness fail here?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
