# FedSKU: Defending Backdoors in Federated Learning Through Selective Knowledge Unlearning

- Decision: Reject
- Scores: 6, 5, 5, 8

## Abstract
Federated Learning (FL) has been found to be vulnerable to backdoor attacks, which involve an adversary uploading manipulated model parameters to deceive the aggregation process. Although several defenses have been proposed for backdoor attacks in FL, they are typically coarse-grained, as all of the methods process the uploaded model as a whole by either removing them or adding noises. In this paper, we propose a more fine-grained approach by further decomposing the uploaded model into malicious triggers and useful knowledge, which can be separately processed for improved performance. Specifically, our approach, called FedSKU, enables backdoor defense through \textbf{S}elective \textbf{K}nowledge \textbf{U}nlearning. We draw inspiration from machine unlearning to unlearn the malicious triggers while preserving the useful knowledge to be aggregated. Consequently, we accurately remove the backdoor trigger without sacrificing any other benign knowledge embedded in the model parameters. This knowledge can be further utilized to boost the performance of the subsequent aggregation. Extensive experiments demonstrate its superiority over existing defense methods.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose FedSKU, a defense mechanism that detects and selectively unlearns harmful backdoors in uploaded models. They introduce a pre-aggregated trigger recovery scheme to efficiently train a trigger pattern generator, reducing training overhead in the FL system. They also designed a dual distillation method for selective knowledge unlearning.

### Strengths
1. The paper emphasizes that pre-aggregation in the model inevitably preserves certain malicious features. They designed the method based on this insight that can effectively reduce the Federated Learning (FL) training overhead from the trigger generator.
2. The suggested method extracts valuable knowledge from backdoored clients, providing a novel defense method against backdoors while preserving competitive global accuracy.
3. The experiments are comprehensive, encompassing varying numbers of malicious clients, initialization parameters, and convergence comparisons among others.

### Weaknesses
1. The "pre-aggregated" process lacks clarity. Also, it would be better to discuss the federated aggregation method on the main page rather than in the appendix.

2. While it's acceptable that FEDSKU has a marginally lower GACC compared to DNN unlearning methods like BAERASER and NAD, given their excessively high ASR indicates unsuccessful defense, it would strengthen the claim about ‘'take the essence and discard the dross' if the author could elucidate why DNN unlearning methods have superior GACC.

### Questions
1. In Figure 2, it appears that two backdoored models exist, but only one is detected. This setup could be confusing due to the absence of the "pre-aggregates" step in the Trigger recovery process. It might be clearer if the framework depicted the detection of multiple backdoored models, thereby illustrating the details of "pre-aggregates" and showing that each backdoored model has a corresponding surrogate.

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper addresses the vulnerability to backdoor attacks that manipulate model parameters to deceive the aggregation process. Unlike existing defenses that employ coarse-grained methods, this research takes a more nuanced approach. The authors propose a novel technique called FedSKU, which involves decomposing the uploaded model into two distinct components: malicious triggers and useful knowledge.

### Strengths
- The concept of selective unlearning represents a novel and compelling advancement in comparison to the coarser-grained defenses commonly used.
- Through extensive evaluation across various datasets, the method demonstrates superior performance in accuracy compared to state-of-the-art defenses, all while keeping the increase in attack success rate at a negligible level.
- The inclusion of convergence analysis and ablation studies offers valuable insights into the inner workings of the method.

### Weaknesses
- The method proposed hinges on anomaly detection for identifying malicious clients. It's important to note that this approach has its limitations; attackers may find ways to evade detection. The authors should delve deeper into this aspect for a more comprehensive discussion.
- The paper lacks an in-depth analysis of the computational overhead associated with trigger recovery and unlearning.
- The experiments conducted on non-iid settings are not as extensive as one might expect.

### Questions
- The effectiveness of the unlearning process can be influenced by various factors, including model complexity, available data volume, and the complexity of the information to be forgotten. How can we ensure that unlearning remains effective after anomaly detection?
- How does the computational overhead of the trigger recovery and unlearning process change as the number of clients increases?
- Instead of performing unlearning, wouldn't it be more efficient to simply exclude the detected malicious clients from the training process?
- Given the potentially large number of participating clients in Federated Learning, how can we guarantee that the proposed method remains effective despite the high computation overhead?

### Soundness
3 good

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
The paper proposes a backdoor defense technique in federated learning (FL) by
first identifying the possible trigger via trigger inversion, and then unlearn
the trigger from the model. The unlearning is done by distillation, assuming a
set of public dataset.

### Strengths
From writing aspect, the paper is easy to follow and understand. Its method description is clear.

Experiment show that the method is very effective, compared with existing
methods.

### Weaknesses
The used technique in this paper, trigger inversion and distillation, do to seem
to be significantly different from existing work. For example, its inversion
method is leveraging MESA (Qiao et al., 2019). I am not sure about the
novelty and significance of the technique.

There is no clear threat model in the paper. For example, both the trigger
recovery and unlearning require certain public data. But what types of public
data? There are various backdoors that work on a subset of inputs or outputs
labels. Does this method work on all these attacks? Based on my understanding, I
do not think it can cover all backdoor attacks. However, without a clear threat
model clarifying the assumptions, I have no information to leverage -- so does
the paper itself.

What does the method guarantee? Namely, will the proposed unlearning method be
"exact" or "approximate"? 

Another line of work, e.g., FedRecover, that tries to recover from poisoning
attacks without the need to recover the trigger (and is also not limited to
backdoors), and also guarantees the recovered model is similar to the one
trained on non-poisoning data with a practical difference bound. The paper
should also include a discussion and comparison on that.

### Questions
See above.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a new method called FedSKU (Federated Selective Knowledge Unlearning) to defend against backdoor attacks in federated learning. Compared to existing coarse-grained defenses that either completely remove suspected malicious models or add noise, FedSKU takes a more fine-grained approach by decomposing the model into the malicious trigger and useful knowledge. It recovers the trigger pattern using a novel pre-aggregation scheme for efficiency. Then it uses a dual distillation process to unlearn the trigger while preserving only clean knowledge in a surrogate model. This allows aggregating the useful knowledge from malicious models.

Experiments on image datasets like CIFAR-10/100 and Tiny ImageNet validate FedSKU. It improves accuracy by up to 6.1% over defenses like FLAME and Krum, with negligible increase in attack success rate (<0.01%). FedSKU also outperforms extensions of other unlearning methods like BAERASER and NAD to federated learning. Overall, FedSKU effectively utilizes knowledge from malicious models to improve accuracy while defending backdoor attacks.

### Strengths
1. Proposes a novel selective unlearning framework FedSKU that decomposes models into triggers and useful knowledge for fine-grained backdoor defense in federated learning.
2. Designs efficient techniques like pre-aggregation scheme for trigger recovery and dual distillation loss to selectively unlearn triggers while retaining useful knowledge.
3. Achieves significant accuracy gains over prior defenses like FLAME and Krum on CIFAR and Tiny ImageNet datasets, with marginal increase in attack success rate.
4. Outperforms extensions of other unlearning methods like BAERASER and NAD to federated learning scenario.
5. Comprehensive experiments analyzing impact of non-IID data, ratio of malicious clients etc.

### Weaknesses
1. Accuracy improvements are higher on CIFAR than Tiny ImageNet - I think more analysis are needed for why FedSKU works better on certain datasets and if this could be a sign of generalization difficulties.
2. No major limitations of the approach have been discussed.

### Questions
1. The pre-aggregation scheme for efficient trigger recovery makes sense intuitively, but more details or intuition could be provided on why aggregating backdoored models retains the malicious triggers reliably.
2. For unlearning using dual distillation, how sensitive is the performance to the hyperparameters like the distillation temperature? Was there any tuning done to set the hyperparameters?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
