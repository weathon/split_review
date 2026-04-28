# Do We Really Need Parameter-Isolation to Protect Task Knowledge?

- Decision: Reject
- Avg Score: 3.67
- Scores: 5, 3, 3

## Abstract
Due to the dynamic nature of tasks, how deep networks can transition from a static structure, trained on previous tasks, to a dynamic structure that adapts to continuously changing data inputs has garnered significant attention. This involves learning new task knowledge while avoiding catastrophic forgetting of previously acquired knowledge. Continual learning is a learning approach aimed at addressing the problem of catastrophic forgetting, primarily by constraining or isolating parameter changes to protect the knowledge of prior tasks. However, while existing methods offer good protection for old task knowledge, they often diminish the ability to learn new task knowledge. Given the sparsity of activation channels in a deep network, we introduce a novel misaligned fusion method within the context of continual learning. This approach allows for the adaptive allocation of available pathways to protect crucial knowledge from previous tasks, replacing traditional isolation techniques. Furthermore, when new tasks are introduced, the network can undergo full parameter training, enabling a more comprehensive learning of new tasks. This work conducts comparative tests of our method against other approaches using deep network architectures of various sizes and popular benchmark datasets. The performance demonstrates the effectiveness and superiority of our method.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes a novel continual learning method that leverages pathway protection and graph matching for model fusion. The authors argue that simple model fusion of the previous and new models impairs performance, as different neurons are activated for different tasks in continual learning. To align these neurons, the authors apply graph matching, tailored separately for shallow and deep layers. They evaluated the proposed method in both CIL and TIL settings, demonstrating its effectiveness against baseline methods.

### Strengths
- The proposed method is well-motivated.
- The proposed method outperforms the recent baselines
- The authors evaluated the method on both CIL and TIL

### Weaknesses
- The method treats shallow and deep layers differently, but it is unclear what constitutes shallow and deep layers. This approach is heuristic, with no optimal solution for identifying these layers.
- The authors argue that "pathway protection is all you need"; however, this is an overstatement, as the proposed method still suffers from forgetting and clearly underperforms compared to memory-based methods. Pathway protection alone is insufficient.
- It is unclear how pathway protection differs from [1]. In [1], neurons (referred to as channels in this paper) are protected for each task, which in turn protects the pathways (i.e., connections between neurons).
- The proposed method performs significantly worse compared to [2]. In CIL settings, [2] achieves 65.1% and 60% accuracy on 10 splits and 20 splits of CIFAR-100, respectively, and 48.9% and 47.1% accuracy on 5 splits and 10 splits of Tiny-ImageNet, respectively, without a memory buffer. In TIL settings, it achieves 93.0% and 95.3% accuracy on 10 splits and 20 splits of CIFAR-100, respectively, and 68.4% and 74.1% accuracy on 5 splits and 10 splits of Tiny-ImageNet, respectively.

[1] Overcoming catastrophic forgetting with hard attention to the task, ICML 2018  
[2] A Theoretical Study on Solving Continual Learning, NeurIPS 2022

### Questions
Refer to the weakness

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes the concept of pathway protection for continual learning. The authors argue that the proposed approach allows for the adaptive allocation of available pathways to protect crucial knowledge from previous tasks, replacing traditional isolation techniques. Furthermore, when new tasks are introduced, the network can undergo full parameter training, enabling a more comprehensive learning of new tasks.

### Strengths
1. The authors address a crucial issue in continuous learning and pose an intriguing question about the necessity of parameter isolation to protect task knowledge. 

2. The experiments illustrate that the proposed method outperforms existing methodologies.

### Weaknesses
1. The rationale behind this work stems from the observation that current parameter isolation methods often hinder the acquisition of new task knowledge. Thus, the authors suggest pathway protection based on the sparsity exhibited by activation channels in deep networks. However, some parameter isolation methods are specifically tailored to leverage this sparsity. The clarification on how the proposed method avoids impeding the learning of new task knowledge remains ambiguous. 

2. The terms "pathway" and "channel" lack clarity. A precise definition of these concepts and a comparison with prior works such as Piggyback, Packnet, and MEAT [1] would enhance the understanding. The proposed method appears conceptually similar to these existing works. 

3. The language used in the paper is perplexing. For instance, in the abstract: "Given the sparsity of activation channels in a deep network, we introduce a novel misaligned fusion method within the context of continuous learning." The meaning of "misaligned fusion" and its relevance is unclear. 

4. Line #80~81: "Therefore, pathways protection is all you need." Such a statement lacks empirical support. It would be beneficial for the authors to provide more rigorous evidence beyond mere examples. 

5. Line #239~241: "Graph matching bears resemblance to a quadratic assignment problem (QAP) (Loiola et al., 2007), with the objective of establishing correspondences between the nodes in an image and the edges connecting these nodes." The reference to "nodes in an image" requires clarification. Additionally, line #246: "In our framework, a deep network is conceptualized as an image." The authors offer no elucidation on how a deep network can be likened to an image.  

Given the uncertainties raised, evaluating the work poses a challenge. The authors appear to lack sufficient writing and publishing experience. I will proceed with the review and reassess the work following a response from the authors.

### Reference:

[1] Meta-Attention for ViT-Backed Continual Learning, CVPR 2022.

### Questions
Please see the questions

### Soundness
2

### Presentation
1

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
The paper proposes a new method for incremental classification, via model fusion and graph matching. The paper  trains a new model for each task and then fuses models based on selected channels from the two models. Experimental results on cifar100 and TinyImageNet show improved results.

### Strengths
A new approach for incremental classification. 

Strong results on ResNet with CIFAR100 and TinyImageNet.

### Weaknesses
The paper is badly written, reading the text doesn't clarify many details. Some details are only mentioned in Figures.
 For example L1,L2, L3 L4 is only mentioned in the Figure. 

Appending and matching is not clarified clearly. I don't understand whether appending is different and what does it refer to. It is only mentioned later in the text.

Design choices are not motivated properly. 

Experiments discussions are quite poor, tables are not always mentioned in the results. Very wide claims are made without exactly discussing numerical results.

The main weakness is the title that is a strong argument against parameter isolation methods, while no analysis is made or strong evidence is shown against parameter isolation apart from weak experiments.

Most recent parameter isolation methods such as SPG and SPU are  designed for large models and this is where parameter isolation excels. To the contrary, only experiments on small convnets are shown.

### Questions
How does the method perform on Transformers?

### Soundness
1

### Presentation
1

### Contribution
2
