# ROSA: Random Orthogonal Subspace Adaptation

- Decision: Reject
- Avg Score: 6.00
- Scores: 5, 5, 8

## Abstract
Model training requires significantly more memory, compared with inference.  Parameter efficient fine-tuning (PEFT) methods provide a means of adapting large models to downstream tasks using less memory. However, existing methods such as adapters, prompt tuning or low-rank adaptation (LoRA) either introduce latency overhead at inference time or achieve subpar downstream performance compared with full fine-tuning. In this work we propose Random Orthogonal Subspace Adapter~(ROSA), a method that outperforms previous PEFT methods by a significant margin, while maintaining a zero latency overhead during inference time. In contrast to previous methods, ROSA is able to adapt subspaces of arbitrarily large dimension. We demonstrate both theoretically and experimentally that this makes ROSA strictly more expressive than LoRA, without consuming additional memory during runtime.  As PEFT methods are especially useful in the natural language processing domain, where models operate on scales that make full fine-tuning very expensive, we evaluate ROSA in two common NLP scenarios: natural language generation (NLG) and natural language understanding (NLU) with GPT-2 and RoBERTa, respectively. We show that on almost every GLUE task ROSA outperforms LoRA by a significant margin, while also outperforming LoRA on NLG tasks.Our code will be made publicly available on acceptance.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a new finetuning method, called ROSA, for parameter-efficient fine-tuning. ROSA is short for random orthogonal subspace adapters that first factorize the parameter matrix W using singular value decomposition (SVD) and split it into smaller trainable matrices (A, B) and a larger fixed matrix (Wfixed). Gradients during back-propagation are calculated only with respect to (A, B). ROSA can maintain a low memory consumption in training as LoRA, while achieving better performance. The authors show that ROSA is better than LoRA theoretically and empirically. Experiments are performed with a few NLU and NLG tasks.

### Strengths
1. This paper proposes a new method to do parameter-efficient fine-tuning. The problem is important and the idea is interesting. 

2. The authors carry out theoretical analysis and mathematical proof. They also provide empirical proof with NLU and NLG tasks.

3. This paper is well-written and easy to follow.

### Weaknesses
1. The ROSA method has been published in ICML23 [1]. The main idea is similar. This paper provides a more solid theoretical analysis and compares ROSA with LoRA on a few NLU and NLG tasks. However, improvements do not appear to be significant.

2. I think more experiments are needed to verify the effectiveness of the proposed method. (1) I'm not very clear about the task selections in the experiment section.  For example, the QQP task is missing in GLUE tasks. Ablation studies are performed in two different tasks (CoLA and MRPC). In my opinion, both tasks use a small training set and the results always fluctuate a lot. (2) PEFT methods are always used for large models. It is necessary to check the performance of large models. (3) LoRA is particularly useful for image generation tasks such as SD models. Would you do more experiments in computer vision tasks?

3. As discussed in the limitation section, LoRA can be released as a plunge into using very large models. It provides great flexibility in the use and distribution of models. Therefore, ROSA's practicability is weaker than LoRA, which will limit the contribution of this work.

### Questions
1. I do not quite understand of the limitation 2 of LoRA. The authors claim that "Second, initializing the adapter AB to zero can be thought of as learning new representations from scratch separately from the pre-trained ones (φ(x) = Wx + ABx:= φpre-trained(x) + φtrainable(x)), rather than leveraging the pre-trained features the model already has to initialize the adapter." 

From my personal point of view, this design element is a boon rather than a limitation. It allows fine-tuning to start precisely from the pre-trained checkpoint, thus safeguarding the integrity of the pre-trained model. In the ROSA context, users do not need to initiate new parameters, as they can start training directly from the pre-trained checkpoint. Both methods are trained using pre-trained checkpoints. Therefore, I would not consider it a LoRA limitation. What are your thoughts?

2. A question about synthetic data experiments. As we know, LoRA is a method for finetuning, which means that the basic model is well-pre-trained. It assumes that the fine-ting tasks or domain adaptations can be achieved with a low-rank tuning. So I'm a bit confused about the synthetic data experiment. It can be shown that in some cases LoRA can not be optimized well. However, this is not the typical application of methods like LoRA.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces a new parameter-efficient adaptation scheme named ROSA: Random Orthogonal Subspace Adapters. The paper primarily targets the limited expressiveness of the existing PEFT methods and proposes a new adaptation scheme for increasing the expressiveness. The proposed fine-tuning strategy can be summarized as follows 1) For a pretrained model, low dimensional subspaces are obtained using SVD computation, 2) the optimization subspace is selected randomly, and the model is updated over the selected subspace for arbitrary iterations, 3) Further the pretrained model weights are again updated with the new weight approximations and new optimization subspace is again selected by considering random orthogonal subspaces obtained via SVD. The paper further shows that the proposed fine-tuning strategy is capable of fine-tuning pretrained weights to arbitrary target weights, making them as expressive as full-finetuning. 

Apart from theoretical analysis, the paper provides a detailed set of experiments over widely used Natural language understanding and natural language generation benchmarks. The empirical results show a performance comparison with other PEFT approaches as well as the fine-tuned version of the model, highlighting the performance obtained by the proposed fine-tuning strategy to perform comparable/better to the full finetuning of the pretrained model.

### Strengths
* The paper provides a detailed theoretical analysis of the proposed scheme and shows the increase in expressiveness of the proposed architecture, highlighting the limitation when compared to the existing PEFT approaches (specifically LORA). The theoretical results are also backed up with detailed experimentation on various NLU and NLG tasks. 
* The paper is well-written and compares the proposed method with LORA clearly. The primary components are the SVD initialization, orthogonality, and resampling. The paper also reports the ablation results, making the components justified and the study reliable for future research. 
* The paper clearly talks about the limitations of the proposed method, which include the storage requirement of keeping the entire model after adaptation over a domain. The primary advantage of the proposed scheme is the reduction in memory usage during training, making the models trainable with limited GPU memory with the added limitation of being usefull for only a single downstream task.

### Weaknesses
 * Since the entire model parameters are updated, it becomes crucial to consider a comparison with the full fine-tuning training strategy. If the convergence speed of the full-finetuning is not improved or comparable, the primary advantage of ROSA only relies on low memory usage for finetuning, which can also be achieved by other means like model sharding for faster training with a number of GPUs. 

* The paper compares the training time of one epoch of fine-tuning in Table 1, where the Epoch time of full finetuning, as reported, is ~157 seconds. When comparing with the proposed method, the Epoch time + Factorize Time also results in a similar time of ~153 seconds + 4 seconds, since at every epoch, a ROSA factorization step is performed, the overall finetuning time of the proposed method and the finetuning of the entire model is similar. If the convergence speed of the proposed method is similar (or lower) to finetuning, the primary motivation of PEFT approaches (less training time) turns out to be missing. I am not sure if I am missing something; however, if the entire model is updated (not keeping the source knowledge intact in terms of pretrained model parameters as done in other adapter-based approaches), the proposed method results in the same model performance as finetuning with no advantage of PEFT approaches. Moreover, as highlighted by the authors, this also limits the usage of the proposed technique for multi-task/domain adaptation.

### Questions
* The proposed scheme seems like an Alt-Opt optimization scheme, where the model is updated on a few of the selected low-rank subspace directions, keeping other subspace directions fixed for a single update and later iterating over different directions to update the entire model’s parameter space. More detailed discussion on similar lines would help understand the proposed method better. 

* A detailed analysis of the convergence rate with various PEFT methods, along with the full finetuning, would be required to obtain a transparent picture of the proposed PEFT technique. It would be interesting to observe if the proposed scheme helps converge with less variability and low sensitivity. 

Minor suggestions:
* In Figure 2, it would be good to make a comparison with full-finetuning, highlighting the comparison between the rate of convergence.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes Random Orthogonal Subspace Adapter (ROSA), a Parameter-efficient fine-tuning (PEFT) method that alleviates the expressivity limitation of previous solutions and does not incur extra latency overhead during inference. ROSA achieves this by iteratively decomposing weight matrices into low-rank trainable subspaces and orthogonal fixed subspaces and merging learned information. Their experiments show that ROSA outperforms LoRA on both GLUE and NLG tasks.

### Strengths
1. The paper observes and formally characterizes the expressivity limitation of SOTA PEFT method.
2. It sounds reasonable that the proposed ROSA method can expand the expressiveness.
3. ROSA does not incur large overhead for fine-tuning.

### Weaknesses
1. People are increasingly interested in LoRA than other PEFT methods because LoRA stores and loads a small number of task-specific parameters during inference. ROSA reintroduces this challenge, making it less practical than LoRA for inference.
2. The paper did not use real-world datasets to verify the expressive ability of ROSA. Considering that there are many real-world datasets suitable for regression experiments, there is no need to use synthetic data as in Section 4.1.

### Questions
Is it possible to perform some extra steps before merging to enforce orthogonality?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
