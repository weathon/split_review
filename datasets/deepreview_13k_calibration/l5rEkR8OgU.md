# Implicit Intermediate Supervision for Learning Complex Functions

- Decision: Reject
- Avg Score: 5.25
- Scores: 6, 5, 5, 5

## Abstract
Large Language models often rely on explicit intermediate step-by-step supervision, such as chain-of-thought, to solve complex tasks. However, this approach necessitates highly curated data and incurs increased inference time costs. In this study, we investigate the potential of implicit intermediate supervision as an alternative, focusing on multi-task and multi-label learning settings. We demonstrate that training on a dataset with a mixture of tasks allows the learner to utilize the solutions of simpler tasks as intermediate steps for solving more complex ones, reducing the reliance on curated data and explicit supervision. In the multi-label setting, the learner can leverage the signal propagated from easily inferred labels to learn targets that require more subtle computations. We present both theoretical and empirical evidence supporting the notion that neural networks can effectively harness such implicit supervision to tackle complex tasks. Our findings suggest that implicit supervision can shed light on how large language models learn complex tasks while potentially offering valuable insights into developing new versatile methods for solving intricate tasks in language modeling.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Intermediate supervision in the form of chain of thought reasoning traces has been a huge success in improving the reasoning abilities of large language models. However chain of thought requires using more compute at inference time, since the model has to generate many tokens to produce the chain of thought. This work explores an alternative approach, which involves training models in either the multi-task or multi-label setting. The idea being that training the model to complete simpler tasks can help it to learn to solve more complex tasks. They explore this on a simple parity task, which has been shown to be challenging to neural networks to learn, and on a math reasoning task and a code interpretation task. In each setting they observe that mixing simpler tasks into the dataset or defining a multi-label problem, helps the model to solve the more complex task. Without the additional supervision, the model either fails to learn at all or learns much more slowly. They also provide some theoretical results on their parity task. The results pain an interesting picture about why language model pretraining is so effective.

### Strengths
* They include both interesting theoretical and convincing empirical results
* Many of their tasks show a dramatic difference between with/without additional supervision, potentially making these tasks a good source for future work to further study
* Their results seem to hold across several tasks and on full transformer language models
* The paper is overall well presented

### Weaknesses
 * The tasks they study are a little bit toy, which makes them easy to study, but it is a little bit unclear if these findings transfer cleanly to the LM pretraining setting.
* They frame this as a replacement for chain of thought, and state that it saves on collecting full reasoning chains for supervision. However chain of thought prompting (the predominate way to get LM to output intermediate reasoning) only requires a handful of examples that can usually be written by a single person in a few minutes. Whereas their method would require collecting or synthesizing large datasets. I feel that a potentially more interesting framing could be around understanding how large scale pretraining (multitask) can enable LMs to learn tasks which are typically challenging for neural networks to learn on their own.

### Questions
* Hoes does model scale impact the results? Will larger models be able to learn more effectively from fewer examples of the simpler tasks?
* Are your models initialized from scratch or fine-tuned from pretrained weights?

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper focuses on intermediate supervision. Popular approaches mainly use explicit step-by-step supervision, whereas the authors investigate implicit step-by-step supervision. The motivation is that models can implicitly explore the structure of tasks, and easy tasks can benefit the understanding of hard tasks. The paper then proposes two settings, multi-tasks and multi-labels, and uses a synthetic parity learning problem and feed-forward network structure to theoretically justify the motivation. During experiments, authors conduct experiments on transformer architectures and other datasets to show the generality of the proposed approach.

### Strengths
1. The paper explains implicit intermediate supervision, which may help understand the large language model's capability of solving complex problems.
2. The paper provides both theoretical understanding and empirical justification. The experiments show the observation also applies to the Transformer architecture.

### Weaknesses
1. The theory is a bit limited to the specific synthetic task. Are there possibilities to extend the idea to support a more general case?
2. The experiments are based on synthetic datasets without realistic datasets. I think datasets that can be used in curriculum learning can be used here too, to justify the applicability of the proposed approach.

### Questions
Please see the weakness part.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a new supervision named implicit intermediate supervision for complex functions. Particularly the authors provide theoretical and empirical evidence to support the effectiveness of implicit supervision.

### Strengths
1. It is novel that the paper pays attention implicit intermediate supervision instead of explicit supervision to solve intricate tasks in language modeling, and it provides detailed proof of the notion.

2. The paper could also contribute to the understanding of how large language models learn complex tasks and may facilitate research on more efficient and effective training methodologies.

### Weaknesses
1. There is something wrong with the structure of this paper, for example, section 1.2 is named as Related Work, which is usually a separate chapter. Moreover, this paper losses the Conclusion part.

2. This paper does not contain an example to show the advantages of implicit supervision over explicit supervision, or an example that demonstrates how the implicit supervision work. So can the authors provide a figure in Section 1 that can make readers get your innovation quickly?

3. The authors point out that explicit intermediate step-by-step supervision is time consuming compared to the implicit supervision in abstract, but they do not provide experimental results to verify this view.

### Questions
Assuming that there are now n tasks, task 1, task 2, …, task n. Will the following scenario occur: training task 1 with data from task 1 to task i yields excellent results, but when training task 1 with data from task 1 to task i+1, the performance significantly deteriorates?

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this work, the authors explore the effect of explicit intermediate supervision on learning complex functions. Specifically, they find that training on a mixture of multiple tasks yields better results than training only on one task. Some theoretical and empirical results show the effects of a combination of two tasks. Their findings could imply better training schemes for language models.

### Strengths
1. This is an interesting work on the investigation of learning effects with a mix of tasks. Some theoretical and empirical evidence is shown for the learning effect. The results on a mixture of the Parity/Sum task are interesting 

2. They also empirically show that it is easier and faster for the learner if the signals from easily inferred labels to learn target are provided. Experiments on LEGO and code interpretation task are done.

3. Their findings on learning complex tasks contribute to the understanding of large language model learning and provide valuable insights for future related work on efficient training.

### Weaknesses
1. The theoretical results on the Parity/Sum task rely on some strong assumptions: bilinear parameterization and specific initialization (for example, v = 0). Under these assumptions, the gradient over the parity distribution samples is zero. This initialization constraint seems particularly restrictive and may not generalize to more realistic scenarios. The analysis hinges on this zero-gradient property, which limits the applicability of the theoretical results.

2. It would be beneficial to show more experimental results for various settings. Specifically, the performance on the Sum task when training with a mixture distribution is missing. Furthermore, exploring a wider range of mixture proportions, particularly with more Sum task samples and fewer Parity task samples (e.g., with p ranging from 0.5 to 1), would provide a more complete picture. Currently, Figure 1 only shows results with p ranging from 0.1 to 0.5, which is not sufficient to fully understand the trade-offs involved in mixing these tasks.

### Questions
Typo errors:

In section 2.2, the parameter W size should be R*{k x (n + 1)}, not R*{k x n + 1}.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good
