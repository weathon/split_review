# Gradient Routing: Masking Gradients to Localize Computation in Neural Networks

- Decision: Reject
- Scores: 5, 6, 5, 5

## Abstract
Neural networks are trained primarily based on their inputs and outputs, without regard for their internal mechanisms. These neglected mechanisms determine properties that are critical for safety, like (i) transparency; (ii) the absence of sensitive information or harmful capabilities; and (iii) reliable generalization of goals beyond the training distribution. To address this shortcoming, we introduce \emph{gradient routing}, a training method that isolates capabilities to specific subregions of a neural network. Gradient routing applies data-dependent, weighted masks to gradients during backpropagation. These masks are supplied by the user in order to configure which parameters are updated by which data points. We show that gradient routing can be used to (1) learn representations which are partitioned in an interpretable way; (2) enable robust unlearning via ablation of a pre-specified network subregion; and (3) achieve scalable oversight of a reinforcement learner by localizing modules responsible for different behaviors. Throughout, we find that gradient routing localizes capabilities even when applied to a limited, ad-hoc subset of the data. We conclude that the approach holds promise for challenging, real-world applications where quality data are scarce.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper presents a new method for training networks called Gradient Routing (GR) with the goal of isolating capabilities to specific subregions of the network by controlling which network subregions are updated by which data points.

The paper shows applications for gradient routing towards a variety of settings and problems:

- The authors first show that by applying GR to an MNIST-autoencoder, it is possible to isolate the representation of digits 0-4 to the first half of an embedding and digits 5-9 to the second half. Additionally, the authors show that GR can be used for activation steering in language models. 

- The authors then propose to use GR for robust unlearning in already learned language models, via an approach called expand-route-ablate (ERA), where pretrained networks are expanded to include new subregions, some already learned capabilities are re-routed to new subregions, and then new subregions are ablated from the model, unlearning these previously learned capabilities from the network. Experiments show that ERA is successful in unlearning topics for small language models, even if only a fraction of "to-unlearn" samples are labelled.

- The paper then shows that vanilla GR can be successfully applied to learn a 0.7B language model that lacks specific harmful capabilities such as bioweapon related capabilities.

- Finally, the paper demonstrates an application of GR in reinforcement learning, to learn a policy that avoids certain target squares in a grid using a limited oversight signal to route gradients.

### Strengths
The proposed method of gradient routing is novel and interesting, and has applications for multiple important problems in safety and interpretability. 

Impressively, the proposed method enables forgetting undesirably capabilities even without labelling full forget sets.

### Weaknesses
 - The vanilla GR method requires splitting data into "retain" and "forget" sets before training begins, and then routing gradients during a potentially long and expensive training process. This limits applicability (except of the ERA method) and raises the question if GR is ever necessary for language model unlearning applications. If we knew the split during pretraining, why would we not simply omit the forget set during pretraining, learning the "pure" model considered in the paper?

- The ERA method requires more experiments and analysis/ablations to show why it works -- it is not clear why it is possible to introduce new network units, set low learning rate on old units for forget set samples, ablate the new units, and observe poor performance on forget set samples when running the old units. Is this a one-off result? Does this generalize to more tests and bigger models that may have more significant understanding of forget-set content?

- GR requires isolating each capability to a subset of examples before training and establishing network subregions for each capability, which may be challenging when there are lots of examples or lots of capabilities.

- The value of the contribution may be very limited due to the proposed method only being applicable in contrived settings: where we know what the undesirable capabilities are before training, and yet have only imperfect labeling (or "entangled capabilities") of data that correspond to those capabilities. The paper needs more motivation for why studying this setting is important.

- The experimental results do not appear to suggest that gradient routing meaningfully outperforms the baseline of data filtering in these settings. While Figs 10 and 11 show that ERA does outperform filtering when a low proportion of forget stories are labeled, the performance difference appears to be extremely marginal, and presumably the data filtering model has lower overall validation loss that may explain even that difference (and lower implementation complexity - no need for potentially expensive modifications to the pre-training method). As a result, I am unconvinced of the utility of gradient routing for the robust unlearning problem from the experimental results in the paper.

### Questions
Why does "absorption" happen? Is the absorption effect reliable across multiple settings?

Questions on the robust unlearning experiment
- In Fig 4(a), why does the validation loss increase with more training steps? Can we see what happens with a more realistic number of finetuning steps (say 1000)?
- Why does RMU appear to outperform ERA on the 4-stories task? Does it just have overall higher loss?
- In fig 4(b) it appears that post-finetuning retain set los is also increased. How much of the validation forget loss in ERA and RMU is just due to overall slightly worse models?

Is ERA expected to work when the pretraining model and dataset are big (such as for modern LLMs) and the representations in the original model have good understanding of the forget set?

### Soundness
2

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces gradient routing (GR), which allows localizing computation in neural networks by masking gradients based on data-dependent paths. GR controls gradient flow within specific network subregions, isolating capacities and enabling the model to focus on particular data features / tasks. It promotes modular network design, making it suitable for selective forgetting and scalable oversight in reinforcement learning and language models. GR is evaluated on MNIST, gridworlds, and language tasks to demonstrate that it can improve task-specific performance, support targeted unlearning, and improve model interpretability by maintaining distinct functionalities in different parts of the network.

### Strengths
- The paper makes a new contribution to the field: GR is a new method to control gradient propagation based on data, enabling modular learning within a network.
- GR can make neural networks more interpretable by designing which part of the network is responsible for a specific task;
- GR provides support for targeted unlearning and scalable oversight;
- Broad applicability of GR (and many interesting questions to spark future work);
- GR can reduce interference and improve accuracy on specialized tasks;
- The method helps to control data access in privacy-sensitive scenarios.

### Weaknesses
 - GR requires careful selection of mask weights, data subsets, and regions to localize. How should these be chosen? At least in its current form, the method faces difficulties scaling up to larger models.
- No comparison to similar methods mentioned that can also achieve localization (DEMix and Interchange Intervention Training, both mentioned in the text).
- Unclear relevance of GR to safety-critical applications mentioned in the paper. Demonstrating benefits in a high-stakes scenario would strengthen the paper.

### Questions
Q1: How the gradient masks are selected / initialized for different tasks / data samples / features? Are there meaningful heuristics that generally work well?

Q2: How to choose the network subregions that gradients should be routed through? Would certain architectures or tasks require a different approach to subregion selection? Have you experienced any achitecture-specific challenges?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work introduces gradient routing, a training method that enhances neural network safety by isolating specific capabilities within distinct network subregions. By applying data-dependent, weighted masks to gradients during backpropagation, gradient routing allows users to control which parameters are updated for particular data points. This approach achieves three main outcomes: (1) interpretable partitioning of representations, (2) effective unlearning by ablating targeted subregions, and (3) improved oversight of reinforcement learning by confining behaviors to distinct modules. The results indicate that gradient routing can localize capabilities even with limited data, suggesting its potential for complex, real-world applications.

### Strengths
1. This paper is well written and easy to follow.
2. The idea is simple and effective
3. The topic is really important for helping understand neural networks and learned representations.

### Weaknesses
1. My main concern is about the contributions. Similar ideas has already been proposed by previous papers
(1) Piggyback [1] and PackNet[2] tries to learn different tasks better with different subsets of the weights by leveraging a binary mask.
(2) Parameter efficient tuning method for Large language models(LLMs) such as lora[3], can efficiently learn different downstream tasks using different adaptor modules.

So the contributions of this paper are not enough.

2. Need more large scale experiments. Given the idea is not that new, only small scale experiments may not enough.

### Questions
1. Clarification of Contributions

 2. Choosing the Routing Strategy:
Since gradient routing relies on predefined, data-dependent masks, an essential question is how to select an effective routing strategy. Could the method involve dynamic routing decisions based on the characteristics of each input, allowing gradients to flow through particular layers or weights? Further clarification on decision criteria for different types of data would strengthen the approach's versatility and practicality.

3. Impact of Initialization and Routing Interactions:
Gradient routing may be influenced by the initialization of weights, particularly concerning the Lottery Ticket Hypothesis [1]. If certain weights are initially unproductive and specific inputs route gradients exclusively to these weights, it could hinder learning.


[1]. The Lottery Ticket Hypothesis: Finding Sparse, Trainable Neural Networks

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper proposes a gradient-routing training method for isolating capabilities to specific subregions of neural networks. We show that gradient routing can be used to (1) learn representations that are partitioned in an interpretable way; (2) achieve robust unlearning by ablating pre-specified subregions of the network; and (3) achieve scalable supervision of reinforcement learners by localizing modules responsible for different behaviors.

### Strengths
1. Based on the gradient, a training method is proposed to isolate the ability to a specific sub-region of the neural network.
2. Gradient routing has implications for safely deploying AI systems, especially in high-risk scenarios where black-box methods are not robust enough.

### Weaknesses
1. In Section 3, authors did not clarify the gradient routing, thus make this paper hard to understand. For example, how gradient mask is generated. Specifically, the mechanism by which gradients are selectively allowed or blocked from propagating to different parts of the network is not clearly defined. The lack of a precise description of the mask generation process makes it difficult to reproduce the results or to understand the underlying principles of the proposed method.

2. Authors did not clarify how gradient mask is generated. I hope you can provide the formula or pseudocode for the mask generation at line 178 of the pseudocode. The description at line 178 is insufficient, and the absence of a concrete mathematical formulation or a detailed pseudocode makes it challenging to grasp the exact implementation of the gradient mask. This lack of clarity hinders the reproducibility and further development of the method.

3. The MNIST dataset has too little data to prove the generalizability of the method. Experiments on more widely used datasets such as ImageNet and COCO can be more convincing. The MNIST dataset, being relatively simple, may not fully capture the complexities of real-world data. The method's performance on more complex datasets is essential to demonstrate its practical applicability and robustness.

### Questions
1. For representations learning, the gradient routing method can be applied to more common image classification tasks?
2. Can you provide a more detailed description in Section 3? 
3. Could you add a Certificate using the top half encoding for comparison in Section 4.1?

### Soundness
2

### Presentation
2

### Contribution
2
