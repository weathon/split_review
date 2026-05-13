# When Does Bias Transfer in Transfer Learning?

- Decision: Reject
- Scores: 8, 6, 3, 5

## Abstract
Using transfer learning to adapt a pre-trained ``source model'' to a downstream 
``target task'' can
dramatically increase performance with
seemingly no downside. In this work, we demonstrate that there can exist a downside
after all: bias transfer, or the tendency for biases of the source
model to persist even after adapting the model to the target class. Through a 
combination of synthetic and natural experiments, we show that
bias transfer both (a) arises in realistic settings (such as when pre-training
on ImageNet or other standard datasets) and (b) can occur even when the target dataset is
explicitly {\em de-}biased.
As transfer-learned models are increasingly deployed in the real world, our work highlights the importance of understanding the limitations of pre-trained source models

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper shows empirically that bias in the source distribution can transfer to downstream tasks. The work conducts experiments for backdoor attacks, synthetically controlled biases, and naturally occurring biases. The paper analyzes the effect of various experimental parameters such as weight decay and full network fine-tuning versus frozen features.

### Strengths
- The motivation and contributions are clear. Understanding how source datasets affect downstream performance, especially in the context of biases and backdoor attacks is highly relevant given how often pretrained models are used. 

- The experiments are extremely thorough, looking at various experimental parameters such as full network fine-tuning versus frozen encoder and the effect of weight decay. Various types of biases are analyzed such as backdoor attacks, natural biases, and synthetically induced biases. The experiments are performed with ImageNet as the source which is a reasonable scale and a common pretraining dataset. 

- The figures are illustrative and convey the main takeaways of the experiments.

- The theoretical toy problem is interesting and gives potential intuition for why bias may persist through fine-tuning. It would be nice to see experiments looking at whether over-parametrization affects the amount of bias transfer.

### Weaknesses
 - It would be useful to know how sensitive these conclusions are to fine-tuning hyper-parameters such as learning rate, momentum, and epochs.


### Questions
- Did you do experiments looking at the initial learning rate for fine-tuning and how that affects the amount of bias transfer? I would expect higher learning rates would lead to lower bias transfer. 

- Do you think these conclusions would hold for other pretrained models like SimCLR and CLIP?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors demonstrate how dataset-induced biases persist after fine-tuning a model, even if the target set does not contain those biases.
For this purpose, the authors designed experiments to introduce or amplify a specific bias and to gauge its presence on the target domain.
The authors explore three mitigation strategies of this bias, including full-network fine-tuning, weight decay, and de-biasing the target domain.

======
Update after rebuttal: I appreciate the additional analysis the authors provided to explain the role of weight decay in mitigating the bias. In its current form the explanation only applies to simple linear regression, and does not extend to a non-linear deep neural network.
Overall, I feel the authors made several points in their analysis which leave the reader with more questions than answers and wishing for more in-depth analysis.
However, given the importance of those points, I am raising my overall score.

### Strengths
- Studying bias transfer is important due to the heavy reliance on foundational models.
- The results are insightful and their implications are nontrivial.

### Weaknesses
 - The work is rather incremental to recent work in the literature, especially the work by Wang and Russakovsky [1]. I missed a reference to that work. The novelty would be more obvious e.g. had the authors demonstrated their results beyond the vision modality. See this recent survey for an overview of closely-related pieces of work, where a proper comparison would help highlight the novelty of the presented work https://arxiv.org/abs/2310.17626
- The mitigations explored seem preliminary or non-straightforward to replicate:
  - Full-network fine-tuning obviously has a better chance of reducing the bias in the pre-trained backbone, compared with a frozen backbone (where the bias mainly exists) + a linear head. 
  - The experiments about weight decay do not explain why it is helpful. Is it generally the case that regularization helps mitigate the bias? Is there something specific to weight decay that helps reduce the bias? What about other regularization strategies?
  - Modifying the target dataset to counter the bias seems helpful but it is not obvious how it can be done in the general case (e.g. beyond balancing the sample in different subgroups or reintroducing the backdoor attacks in the target dataset at random).

A few typos:
datapoints => data points
can substantially reduces 
adjusting [..] entirely eliminate => eliminates
with of people => with people

### Questions
- Would adversarial pre-training offer a good mitigation strategy as well?

- The authors mention that they "find that weight decay does not reduce bias transfer in the fixed feature transfer learning
regime, where the weights of the pretrained model are frozen.". How is weight decay applied to frozen weights?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper explores the transfer of biases as a result of transfer learning from the source dataset to the transferred models. For both natural and synthetically generated biases, it is shown with experiments that biases pre-existing in the pretraining data get transferred to the downstream tasks, even when the downstream dataset is balanced. The extent of the biases is lesser when finetuning is allowed into the entire network as compared to the case where only retraining the final layer is allowed.

### Strengths
1. The study is important, as using pretrained models to finetune on a downstream task is highly beneficial and a popular norm in the current times, hence understanding how the biases in the pretraining datasets creep into the downstream task is necessary to get unbiased predictions.
2. The paper explores multiple settings. They show what happens when the pretraining dataset is biased, where the biases can be both synthetic and natural.
3. The fact that biases are transferred even when the target dataset is debiased is very interesting.
4. Three simple methods have been discussed to reduce the effect of the biases - full network transfer learning, reducing weight decay, mitigate biases in the target dataset.

### Weaknesses
1. Novelty is a concern for this paper: all the observations in the paper are expected and not surprising. For example, isnt it obvious that the full network transfer learning setting will be less affected by the source biases than the fixed one?
2. I agree that identification of the problem is certainly important, and this paper does that - the authors demonstrate effectively how dangerous the pretraining data can be in terms of fairness. However, some mitigation strategies or atleast thoughts are expected. One of the solutions proposed is to use full network transfer learning. But if enough resources are not there for a model-user to finetune the entire network, the user has to rely on the fixed feature transfer learning - or settle for something in the model. How to solve the problem in that case?
3. Wang et al [1] suggest manipulating the finetuning data to reduce the biases. No suggestion is proposed by the authors.
4. For the synthetic bias case, what is termed as backdoor attack is simply adding a spurious correlation synthetcially to the dataset to increase/induce bias into it.

### Questions
We use pretrained models for a multitude of tasks. 
1. What if the pretraining and finetuning data are not entirely similar, and the latter has its own biases? Any suggestions or experiments for such a situation?
2. What happens when the latter is balanced?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors empirically investigate whether biases contained in a pre-trained DNN is transferred to a fine-tuned DNN, in different experimental settings. They confirmed that such biases are actually transferred in (1) synthetic settings using backdoor attacks, (2) synthetic settings with naturally introduced biases of class information (even with de-biased target datasets in fixed-feature setting), and (3) standard transfer learning scenarios on ImageNet.

### Strengths
- Their motivation is clear and writing is easy to follow.
- Their experimental scenarios are well-designed. In particular, the phenomenon of transferrability of backdoor attacks is new to me and seems intriguing, but less confident on its novelty since I'm not an expert of ML security.
- Their experiments are thoroughly conducted on vision datasets, and the results are convincing.

### Weaknesses
 - The novelty and contribution of their findings is limited. Previous works [1,2] already investigated such aspects of transfer learning, and some findings in this submission (particularly the bias transfer phenomenon in the scenario (2) and (3)) can be implied from their results.
- The definition of "bias" in this submission is unclear. It should be specified to discuss "bias" transfer in a possibly rigorous way. Also, I'm less confident whether backdoor attacks should be considerred as "bias", but the research direction of transferrability of such attacks itself should be new and encouraged.
- Discussions on previous works is not enough. The most related works [1][2] are not cited and not discussed. In relation to transferrability of backdoor attacks, I think [3] is one of very related works, but is not discussed. I recommend the authors to survey their previous works and make clear the novelty and contribution of this paper.

### Questions
1. What is the definition of biases in this paper? It should be specified first of all to discuss "bias" transfer.

### Soundness
3 good

### Presentation
3 good

### Contribution
1 poor
