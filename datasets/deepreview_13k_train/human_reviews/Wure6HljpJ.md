# CoSDA: Continual Source-Free Domain Adaptation

- Decision: Reject
- Scores: 3, 3, 5, 3, 5, 3

## Abstract
Without access to the source data, source-free domain adaptation (SFDA) transfers knowledge from a source-domain trained model to target domains. Recently, SFDA has gained popularity due to the need to protect the data privacy of the source domain, but it suffers from catastrophic forgetting on the source domain due to the lack of data. To systematically investigate the mechanism of catastrophic forgetting, we first reimplement previous SFDA approaches within a unified framework and evaluate them on four benchmarks. We observe that there is a trade-off between adaptation gain and forgetting loss, which motivates us to design a consistency regularization to mitigate forgetting. In particular, we propose a continual source-free domain adaptation approach named CoSDA, which employs a dual-speed optimized teacher-student model pair and is equipped with consistency learning capability. Our experiments demonstrate that CoSDA outperforms state-of-the-art approaches in continuous adaptation. Notably, our CoSDA can also be integrated with other SFDA methods to alleviate forgetting. \looseness=-1

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a simple continual SFDA framework, where a teacher-student framework is applied. The teacher model provides the hard labeling for the student model, and the student model will be penalized with the divergence from the teacher hard label, as well as a mutual information maximization regularization. There are extensive experiments compared to other SFDA methods and the baselines.

### Strengths
1. The paper is well organized with sufficient background introduction.
2. The paper provides illustrative figures and diagrams for readers to better understand their proposal.
3. The paper conducts extensive experiments on DomainNet, OfficeHome and VisDA, which are the main DA datasets, and show fair performance on those SFDA tasks.

### Weaknesses
1. The proposed method lacks novelty in terms of the framework design. For example, the teacher-student architecture has been proposed from the self-supervised learning framework, e.g., MoCo. The mix-up is another already invented technique to augment both the input space and the label space. The consistent loss has been utilized in those above mentioned methods already.

Meanwhile, the mutual information maximization is a widely applied regularization technique during representation learning. Combining all, I think the novelty of the design is hard to justify.

2. The paper claims continual SFDA, where from the method design, there is no specific module is designed to deal with the model catastrophic forgetting issue, except accepting the teacher model’s hard label to measure the KL divergence from the student prediction on the mixed up sample. 

The teacher model is leveraging exponential averaging, but the student model is not in any manner distilled from the teacher model. The model weights forgetting is not addressed in any technical design.

3. Across the compared methods, the proposed CoSDA does not show advantageous results over the other methods. For example, in Table 1, CosDA is not compellingly better than EdgeMix, where actually many of the DA protocols EdgeMix shows better results.

In Table 2, CosDA even combined with some other modules, such as NRC or AaD, is not better than AaD. This suggests that the proposed way does not achieve as advantageous performance as the state-of-the-art methods.

### Questions
Please refer to the weakness session for more detail.

### Soundness
2 fair

### Presentation
3 good

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
The paper focuses on mitigating catastrophic forgetting in the context of source-free domain adaptation. The authors take several steps to address this challenge, including re-implementing existing methods and introducing a novel approach called CoSDA, which leverages a teacher-student model to achieve continuous adaptation. Specifically, the authors introduce a consistency loss based on KL-divergence to transfer knowledge from the teacher network to the student network. They also employ a KL-divergence-based regularization loss to stabilize training with Mixup augmentations. Additionally, the authors present two distinct optimization strategies for updating the teacher and student networks.

### Strengths
1. The motivation for using Mixup for the data augmentation is clear and well-described.

2. Extensive experiments and ablation studies are performed.

### Weaknesses
## Majors

1. I have concerns regarding the formulation of consistency loss which is the main contribution of the work. Equation 1 is confusing. From my understanding, $h_{\psi}(\tilde{x})$ should refer to the output logits from the student network. If so, minimizing the divergence between two distributions from different mathematical spaces does not make any sense.  To be specific, $\tilde{p}$ is a softmax probability vector with each element in the range [0,1], while $h_{\psi}(\tilde{x})$ has elements ranging from negative infinity to positive infinity. The use of the same notation '$h$' for both logits and probabilities is confusing and misleading, as they belong to distinct mathematical spaces. This lack of notational clarity makes it difficult to understand the core contribution of the paper.

2. Please add an ablation study to demonstrate the potential issue of the proposed consistency loss collapsing. My suspicion is that this collapse occurs due to the divergence between two distinct mathematical spaces. The current ablation study does not adequately address the potential for collapse, which is a critical concern given the formulation of the consistency loss.

3. In batch normalization, the mean and variance are computed based on the activations within each mini-batch, which is a subset of the entire dataset. The statistics are calculated separately for each mini-batch as the model processes the data during training. This is what allows batch normalization to adapt to the statistics of the current batch and helps in stabilizing and accelerating training. However, the authors mentioned that their mean and variance are calculated based on the whole dataset for batch normalization, which does not make sense. As per my understanding, the moving average mean and variance are computed by accumulating the mean and variance from each batch using an exponential moving average formula ($\alpha*\mu_{moving} + (1-\alpha)*\mu_{i}$). The moving average mean and variance are not the mean and variance of the whole dataset. The lack of clarity on batch normalization in the paper raises concerns about its overall quality. The description of batch normalization is not consistent with standard practices, and the authors need to clarify how they are implementing it.

4. I may have a misunderstanding regarding the evaluation settings; however, based on my interpretation of the paper, it appears that the proposed method does not demonstrate significant improvements over the baseline approaches in terms of target domain classification accuracies. I kindly request the authors to provide a more detailed explanation or consider revising the experiment section for improved clarity on this matter. The presentation of the experimental results makes it difficult to assess the effectiveness of the proposed method, and the authors need to clarify how the results demonstrate the claimed improvements.

## Minors

1. The proposed work appears to be closely aligned with federated learning. I am curious about the authors' motivation for framing this work as a sequence of source-free domain adaptation. To me, the workflow seems to have stronger connections to federated learning rather than source-free domain adaptation. Thus, the literature on federated learning should be given.

3. typos: 3.1 ”to consist with” -> “to be consistent with”

### Questions
1. In the second paragraph of the introduction, the authors mentioned that “SFDA also allows for spatio-temporal separation of the adaptation process since the model training on source domain is independent of the knowledge transfer on target domain”. What does the spatio-temporal separation refer to? 

2. In Equation 1, is h_{\psi}(\tilde{x}) referring to the logits or the softmax probabilities? If it represents the logits, it raises a question regarding the use of KL-divergence between two distributions: \tilde{p}, which is a softmax probability vector with each element in the range [0,1], and h_{\psi}(\tilde{x}), which has elements ranging from negative infinity to positive infinity.

3. I do not quite understand the in-sequence evaluation settings. From the result tables, the authors listed, most baselines perform better without the proposed methods. Then, how could the readers evaluate the effectiveness of the proposed methods?

### Soundness
1 poor

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes a new method for continual source-free domain adaptation (CoSDA), which transfers knowledge from a source-domain trained model to multiple target domains without accessing the source data. CoSDA uses a dual-speed optimized teacher-student model pair and consistency learning to mitigate forgetting and improve adaptation. CoSDA also incorporates mutual information loss to enhance robustness to hard domains. The paper evaluates CoSDA on four benchmarks and shows that it outperforms state-of-the-art methods in both single-target and multi-target sequential adaptation scenarios.

### Strengths
1. The proposed method is simple yet efficient. 
2. The experimental results are extensive, including a comparison of various baselines on different datasets. The results prove the effectiveness of the proposed method.
3. Theoretical analysis and proofs are provided as necessary.

### Weaknesses
1. The technique contribution is somewhat limited. The proposed method can be easily derived from existing methods. For example, the idea of the teacher-student framework[1] and the mix-up strategy[2] for continual source-free domain adaptation is nothing new. Specifically, the use of a teacher-student model with different update speeds, while effective, is not a novel concept in itself, and its application to this specific problem seems like a straightforward extension of existing work. The consistency loss, while a common technique, doesn't introduce a significant leap in methodology. The mutual information loss, while potentially beneficial, also builds upon well-established information-theoretic principles, and its novelty in this context is not clearly demonstrated.
2. There is a need for deeper experiments. Could the authors test their proposed method on a variety of adaptation sequences, especially those that are more complex, instead of relying solely on one fixed combination sequence? In real-world scenarios, sequential target data might span a longer duration and encompass a wider range of distributions. For instance, the authors could establish longer sequences with more diverse domain shifts to evaluate the method for mitigating forgetting. The current experiments do not fully explore the robustness of the method under more challenging conditions, such as highly dissimilar target domains or longer sequences of adaptation tasks.
3. In continual source-free domain adaptation. A primary challenge lies in managing the tradeoff between adapting to target domain and preventing the forgetting of previous domains. However, the proposed methods give limited attention to this challenge. The tradeoff is achieved through the EMA momentum m within a teacher-student learning framework in this paper. Thus, a hyper-parameter experiment of m should at least be conducted. The paper lacks a thorough analysis of how the momentum parameter affects the balance between adaptation and forgetting. A sensitivity analysis of this parameter is crucial to understand the method's behavior and provide practical guidance for its application. Without this analysis, it is difficult to assess the robustness of the method to different parameter settings.

### Questions
see above

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper studies the well-established problem of source-free unsupervised domain adaptation (SFDA) in a *continual learning* setting. While existing approaches on SFDA focus exclusively on target domain performance, the authors propose a new method, CoSDA, that not only enhances target domain adaptation but also preserves the source domain performance. The core idea revolves around using a student-teacher framework, where the teacher model is updated via EMA (exponential moving average) of the student model weights to prevent forgetting. The mixup augmentation is used to drive the learning process via consistency regularization between the pair of networks, and a mutual information maximization loss is also added to obtain better pseudo-labels. Experiments are shown on four classification benchmarks: DomainNet, OfficeHome, Office31, and VisDA. Beyond single target adaptation, results are also shown on multi-target adaptation (where the domains appear sequentially) to highlight the continual learning capabilities of the framework. When compared to existing works on SFDA and Test-Time Adaptation (TTA), CoSDA achieves both higher accuracy and good robustness against forgetting.

### Strengths
1. The problem statement is quite relevant for practical applications of domain adaptation methods. Most of the literature on domain adaptation focuses on target domain performance without any concern for source-domain performance. On the contrary, this paper tries to remedy this overlooked aspect in domain adaptation. This is quite an important problem since data can come from any domain during inference.

### Weaknesses
1. The proposed CoSDA approach lacks novelty and bears a *significant* similarity to CoTTA [1]. CoTTA tackles the closely related problem of test-time adaptation (TTA) and utilizes the exact same concept of a student-teacher framework trained using consistency regularization. CoSDA simply replaces the general augmentation set in CoTTA with mixup. The authors do compare with CoTTA and mention that "... CoTTA (Wang et al., 2022) ensures knowledge preservation by stochastically preserving a subset of the source model’s parameters during each update" but fail to mention this other crucial aspect of this paper which is directly related to their method. The inclusion of the mutual information regularization loss for better pseudo-labels is also borrowed directly from a previous SFDA approach SHOT [2]. Finally, the claimed student-teacher EMA framework is very common is the SFDA literature, [3, 4], none of which are mentioned in the paper.

2. A primary goal of this work is to prevent catastrophic forgetting of previously seen domains, however, there is no discussion of existing continual learning approaches and what distinguishes this work from these papers.

3. The experiments on sequential target domains (Sec 4.3) is limited, despite being a prominent claim of this paper: (a) the max number of domains is only 4, while TTA methods experiment with up to 15, and (b) no experiments on effects of a domain being repeated.

### Questions
1. Why was mixup chosen as the preferred augmentation? Are there experiments with other augmentations? The authors mention that mixup can be applied to other domains (NLP, Audio), but no evidence is provided to prove the efficacy of CoSDA on other domains, let alone more challenging tasks on images, such as semantic segmentation. 

2. How does the performance vary with the number of unlabeled samples per domain?

3. CoTTA utilizes a stochastic restore of the source weights since it tackles the more challenging TTA setup (performing adaptation with very few images) -  was this removed in the experiments? Furthermore, how well does CoSDA perform on the TTA benchmarks?

### Soundness
2 fair

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The submission investigate continual source-free domain adaptation task, where a source pretrained model is continually adapted to a sequence of unlabeled target domains, without the access to all old domains (source and old target domains). The submission proposes several general methods to address this challenging task, which could be easily combined with the existing source-free domain adaptation methods.

### Strengths
- The investigated continual source-free domain adaptation task has more practical value, as the adapted model is expected to keep good performance on all old domains after adapting to a new target domain. Also in the proposed method, domain ID is not needed which makes the method more readily deployed in the real world application.

- The proposed method is relatively simple, which only contains a mixup consistency loss with teacher-student architecture, a mutual information maximization loss, along with a BN statistics updating trick. Thus, the method is quite general, and could be easily combined with the existing source-free domain adaptation method, which is proved in the experimental section.

- The experimental sections are detailed, which cover several benchmarks, and reproduce lots of existing method for the continual source-free domain adaptation setting.

### Weaknesses
Although the studied new setting is of high practical value, and the experiments are abundant, the major concern is that the proposed method(s) is not new/novel, the proposed modules are quite popular in the related areas.

- Teacher-student architecture where teacher model is the EMA between old teacher model and the current student model, this technique is popular in almost every transfer learning topic.

- Usage and discussion of mutual information maximization. As the paper mentioned, MI is proved to be very efficient in unsupervised clustering task [1], which is a similar topic to source-free domain adaptation. Also, AaD also discuss MI and relate it with several other different methods.

- BN updating trick. Actually one paper in continual learning gives a thorough investigation about how BN influence the continual learning performance, with a short conclusion that the running statistics heavily biased towards the current task, which may influence the performance on the old task. In turn, BN statistics are also important for the current task, as mentioned in GSFDA that simply forwarding with the test data once before adaptation could improve the performance. The author could add some discussions with the above mentioned methods, as in the proposed way the teacher model has more information about the old domain while the student model focus on the statistics on the current domains.

### Questions
Overall, the paper is sound and address a new but practical new task, as well as providing detailed experimental analysis. However, I think the proposed method is somehow incremental, as mentioned in the weakness part, and I do not really get some new and interesting insights from this submission.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 6

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This study introduces a novel context in the realm of continual SFDA, a specific case within unsupervised domain adaptation. It focuses on the sequential adaptation of a robustly trained source model to multiple unlabeled target domains. The authors pinpoint the issue of catastrophic forgetting prevalent in current domain adaptation techniques and skillfully reconfigure existing baselines to function in this innovative setting. Subsequently, they present a teacher-student consistency learning approach designed to attenuate the effects of forgetting, thereby facilitating efficient adaptation across multiple targets sequentially. The empirical evidence provided substantially corroborates the assertion that this methodology not only enhances performance but also significantly curtails issues related to catastrophic forgetting.

### Strengths
1. It is happy to see that this manuscript reimplements previous SFDA approaches within a unified framework and conducts a realistic evaluation of these methods under the continual SFDA settings.
2. For the most part, the writing is clear and easy to understand.

### Weaknesses
1. I'm primarily concerned about the relevance of the continual SFDA setting. The manuscript restricts its experiments to synthetic tests on established UDA benchmarks, raising questions about the practical value of continual SFDA in real-world applications. In actual practice, it seems feasible to merge all target domains into a single large one and adapt the source model accordingly. Additionally, identifying or defining the source and target domains in real-world applications is already a challenging task, complicating the applicability of this approach.

2. Another concern pertains to the originality of CoSDA, as it appears to amalgamate various existing strategies, including the teacher-student model, mixup, and information maximization. While the use of the exponential moving average method is a common and sensible strategy to prevent overfitting, the rationale behind employing mixup and information maximization to tackle this issue isn't clear or intuitive. The specific implementation details regarding how these components interact and contribute to mitigating catastrophic forgetting are not sufficiently elaborated, making it difficult to assess the novelty of their combination.

3. Lastly, the presentation of results in the tables is somewhat overwhelming and perplexing. The abundance of statistics, compounded by the use of multiple colors, makes it difficult to interpret the data and grasp the essential outcomes. Simplifying these tables for clarity and ease of understanding would be highly beneficial.

Some typos in this manuscript: 
1. "by by consolidating data"
2. "In this section, We ..."

### Questions
1. What are the practical applications for continual SFDA in the real world?
2. In real-world scenarios, how can we gather multiple domains that exhibit distribution shifts?
3. Considering the era of large-scale models, what is the actual importance of continual SFDA? Specifically, if the source model is an extensive visual foundation model, is there a real need to sequentially adapt this model across various target domains?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
