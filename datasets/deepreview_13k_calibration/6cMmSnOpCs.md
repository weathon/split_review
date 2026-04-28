# ScaLearn: Simple and Highly Parameter-Efficient Task Transfer by Learning to Scale

- Decision: Reject
- Avg Score: 5.75
- Scores: 8, 5, 5, 5

## Abstract
Multi-task learning (MTL) has shown considerable practical benefits, particularly when using language models (LMs).
While this is commonly achieved by learning $n$ tasks under a joint optimization procedure, some methods, such as AdapterFusion, divide the problem into two stages: (i) task learning, where knowledge specific to a task is encapsulated within sets of parameters (\eg adapters), and (ii) transfer, where this already learned knowledge is leveraged for a target task. % in consideration. 
This separation of concerns provides numerous benefits (e.g., promoting reusability). %(a principle of green AI) --> Introduction
However, current two-stage MTL introduces a substantial number of additional parameters.
We address this issue by leveraging the usefulness of linearly scaling the output representations of source adapters for transfer learning.
We introduce \modelours, a simple and highly parameter-efficient two-stage MTL method that capitalizes on the knowledge of the source tasks by learning a minimal set of scaling parameters that enable effective %knowledge 
transfer to a target task. % and combining the \emph{scaled} representations without requiring additional parameters. % and combines them
Our experiments on three benchmarks (GLUE, SuperGLUE, and HumSet) and two encoder LMs show that \modelours %, in addition to facilitating the benefits of two-stage MTL, 
consistently outperforms strong baselines with a small number of transfer parameters ($\sim\!0.35\%$ of those of AdapterFusion).
Remarkably, we observe that \modelours maintains its strong abilities even when further reducing parameters, achieving %similarly 
competitive results with \emph{only 8 transfer parameters} per target task.
Our proposed approach thus demonstrates the power of simple scaling as a promise for more efficient task transfer.}

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces a new method for two-stage parameter-efficient multi-task learning called ScaLearn. It builds on prior work that fusing Adapters, and shows that a simpler parameterization of the source-task mixing module works well. It does this by replacing the attention mechanism in (Pfeiffer et al)[https://arxiv.org/abs/2005.00247] with a simpler task-vector or task-scalar parameterization.

### Strengths
- The paper is clearly written, and is generally easy to follow. 
 - The method is simple, well-motivated, and works well. 
 - In my opinion, the method proposed in this paper should have been a baseline in the original [Pfeiffer et al](https://arxiv.org/abs/2005.00247) paper that introduced AdapterFusion. Unfortunately it wasn't, so this paper is valuable in that it shows that attention could be unnecessary to fuse adapters, and simple task-vectors or task-scalars may be sufficient.

### Weaknesses
 - I don't think this is a glaring weakness, but I do think the paper could benefit from more diverse source/target tasks, especially sequence-generation tasks. It could be possible that the simpler ScaLearn parameterization doesn't work as well for different configurations of source and target tasks. I don't particularly see why *both* GLUE and SuperGLUE had to be included, it might have been better to replace one of them with a different benchmark if resources are/were the constraint. 
 - Some paragraphs are very long and hard to parse (e.g. "Models and Baselines" on page 6), and could be written in a more organized manner in my opinion.

### Questions
- Did the authors try other parameterizations of the fusion module? For example, a low-rank MLP per task instead of a vector per task would be a step towards finding a sweet spot (if it exists) between attention-based fusing and ScaLearn. It's also not clear to me whether a task-vector-per-layer would be better than an MLP-shared-across-layers. This paper essentially shows that what should have been a baseline in [Pfeiffer et al](https://arxiv.org/abs/2005.00247) works very well, which is valuable, but I think expanding the study to include a larger range of parameterizations (starting from ScaLearnUniform++ → low-rank MLPs → efficient attention variants) would make this paper much stronger and be a conclusive piece of work on fusing Adapters. Of course this is not necessary to be a solid paper, but definitely worth considering and discussing in the paper in my opinion.

### Soundness
4 excellent

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
This article presents a new two-stage multitask learning method called SCALEARN, which achieves knowledge transfer by learning the output representation of scaling the source task. The proposed approach achieves high parameter efficiency and strong performance, and can avoid problems such as task interference and data privacy. The authors conduct extensive experiments on three benchmark datasets, e.g., GLUE, SuperGLUE, and HumSet, using RoBERTa and XLM-R as pre-trained language models. The experimental results demonstrate that ScaLearn and its variants outperform strong baselines on various tasks, and also perform well in a few-shot setting.

### Strengths
- ScaLearn achieves transfer learning on downstream tasks by scaling and combining the output representations of the source task adapter. This approach has high scalability and low parameter overhead. The idea is simple and technically sound.
- In the third section of the paper, the authors analyze the effects of scaling output representations in transfer learning: scaling output vectors is an effective method for controlling the (partial or full) activation of the knowledge contained in an adapter module and the optimal weights do not necessarily sum up to 1. This provides a new approach for “how to leverage modular knowledge to learn new tasks”. The investigation effectively supports the paper’s claims.
- Experiments are very extensive and thorough, including a variety of tasks, architectures, datasets (GLUE, SuperGLUE, HumSet), and strong baselines beyond vanilla dropout. Both standard transfer learning and few-shot transfer learning are reported, accompanied by in-depth ablation studies. The experiment and analysis are well organized.

### Weaknesses
 - Analysis limited to adapter-based methods. Unclear how well it will perform to other PEFT architectures (e.g. Prompt Tuning).
- To my best knowledge, IA3 [1] achieves stronger fine-tuning performance by scaling the weighted activations in the activation layer using learned vectors. This is similar to your method, but I did not find it in the PEFT baselines you compared.
- It seems that many source tasks are closely related to each other. I would suggest authors use benchmarks such as CrossFit [2] to do a more large-scale analysis, where the transferring is more challenging as some source tasks can be relatively less related to the target tasks.
- For the second stage during training, the output representations of multiple source adapters are scaled and combined, which reminds me of MoE (Mixture of Experts), where each source adapter corresponds to an expert. It is a well-known phenomenon that learnable MoE can lead to overfitting and collapse. However, in your method, it seems that this issue does not arise. Could the authors explain the specific reasons behind this?

### Questions
Please respond to the concerns listed in weaknesses.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a method for transferring previously learned knowledge (in the form of adaptors) from different source tasks to a given target task. The main idea of the paper is to propose a new method that is more parameter-efficient compared to the previous methods. Their method ScaLEARN learns a vector that scales the outputs of the adaptors of the source tasks and then adds these outputs together before passing them to the next layer. They propose some variants of this method that share these activation scaling parameters and across layers, or across the dimension to reduce the parameter count even further. They compare their work with AdaptorFusion methods from 2021.

### Strengths
S1. The problem being studied in the paper is becoming increasingly important in the scenarios of large language models. 

S2. The method reduces the parameter requirement compared to the AdaptorFusion paper. Moreover, some variants of the method (ScaLearnUniform++) are extremely parameter efficient while they perform similarly to adaptor-fusion and the basic method ScaLearn.

### Weaknesses
W1. The experimental section is not very strong and is missing some very strong baselines, relevant settings, and analysis. Please refer to the questions below.

W2. The paper is slightly harder to read, the motivation and the analysis on scaling part was not very clear to me until I read section 4 about the method.

### Questions
**For Me to Improve My Score (Most to least important)**

Q1: The only modular composition baseline in this paper is AdaptorFusion from 2021, which is quite old now and there have been other works that tackle the same problem from different angles that should act as baselines here. [1] Combining Modular Skills in Multitask Learning, [2] AdapterSoup: Weight Averaging to Improve Generalization of Pretrained Language Models, and [3] Multi-Head Adapter Routing for Cross-Task Generalization. And the baseline methods used in these papers. 

Q2: The experimental setup used in the paper can be significantly improved by studying this problem on good seq2seq zero-shot models like T0, or maybe LLaMA family models and then comparing the zero-shot performance, few-shot performance, and the performance obtained via this kind of composition of learned modules. 

Q3: How is the classification layer for the target task finetuned? In Table 1 and everywhere in the paper, it seems like you do not count these parameters when counting for the number of trainable parameters. Can you clarify this if the classifier parameters are also learned on each source task then this needs to be clarified throughout the paper. 



**Other Questions**

Q4: The experiments in the paper should add IA3 () as a baseline. IA3 paper shares very high similarity to the proposed method, the ScaLEARN method is like adapting source task adapter modules using IA3 on a downstream task. Hence, for all the experiments, IA3 would be a good baseline as it would learn a lower number of parameters than ScaLearn. However, I don't suspect it to perform better than the presented method as it is leveraging source adaptors.

Q5: At multiple places, the paper talks about how the scaling coefficient does not need to sum to 1 and I agree that for ScaLearn this might be the case however, I am not sure if there is enough evidence in the paper, to claim that this is how it should be for all other methods and this has been talked about at multiple places in the paper as a new finding. It can be that for the other methods having a constraint on summing to 1 might be better than not having it. Hence, this is a method-specific detail and should not be portrayed as a general finding that we should not have a summation constraint. I might have missed something here and I will willing to take this comment back in light of evidence.


I looking forward to the rebuttal and will update my score if some of my main concerns are addressed. I really like the simplicity of the method however I would like it to be more rigorously tested against other baselines and experimental setups.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a new method for task transfer by aggregating the output representations of source task models with some weighted sum, where the weight is either applied on each coordinate or on the entire representation. They claim that this method is more parameter efficient than the previous method which trains a separate adapter for each task, and show that the performance is slightly better.

### Strengths
- The idea is simple yet seems to be something that people haven’t tried before.
- The algorithm both improves parameter efficiency and also the performance, which is quite nice.
- The paper is well written and the algorithm details are carefully explained.

### Weaknesses
 - The improvement in the performance is quite marginal. In table 3, it looks like the proposed method is only slightly better than previous algorithms.
- I believe that the focus of the algorithm is the parameter efficiency. However, I’m not very convinced that this is an important improvement, given that the adapter anyways is already having much fewer parameters than the original models. Isn’t it true that the key bottleneck is the model size itself?
- It would be good if the authors can include experiments beyond NLP tasks to show the generality of their method.

### Questions
- In table 3, the version of the ScaLearn that achieves best performance varies a lot across tasks. Why is this the case? Can you provide some intuition around when would each version work better?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
