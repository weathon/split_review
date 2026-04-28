# CAN - CONTINUOUSLY ADAPTING NETWORKS

- Decision: Reject
- Avg Score: 1.50
- Scores: 1, 1, 1, 3

## Abstract
Catastrophic forgetting is a fundamental challenge in neural networks that prevents continuous learning, which is one of the properties essential for achieving true general artificial intelligence. When trained sequentially on multiple tasks, conventional neural networks overwrite previously learned knowledge, hindering their ability to retain and apply past experiences. However, people and other animals can learn new things continuously without forgetting them. To overcome this problem, we devised an architecture that preserves significant task-specific connections by combining selective neuron freezing with Hebbian learning principles. Hebbian learning enables the network to adaptively strengthen synaptic connections depending on parameter activation. It is inspired by the synaptic plasticity seen in brains. By preserving the most important neurons using selective neuron freezing, new tasks can be trained without changing them. Experiments conducted on standard datasets show that our model significantly reduces the risk of catastrophic forgetting, allowing the network to learn continually.

## Human Reviews

## Human Reviewer 1

### Rating
1

### Rating Number
1

### Confidence
3

### Summary
In this paper, the authors attempt to address the continual learning problem by selectively freezing important neurons when training on a new task. In contrast to previous continual learning methods, important neurons are identified with Hebbian learning using a network of the same architecture. The model is then evaluated on a simple MNIST task and is shown to significantly outperform a vanilla model.

### Strengths
The idea of utilizing Hebbian learning to help the model continually learn is interesting, as Hebbian learning is a well-known synaptic plasticity rule in animals. Experiments might provide insights into why these mechanisms can help animals continually learn.

### Weaknesses
1. Overall the motivation behind the method is not well explained. The motivation behind Hebbian learning is to take inspiration from animals, but it is not clear to me why we want to use a separate network evolved with Hebbian learning to compute the importance score. It's unclear how this dual-network design is linked to biological continual learning. The paper does not sufficiently justify why a separate network, trained with a different learning rule, is necessary for identifying important neurons in the primary task network. A more detailed explanation of the underlying hypothesis is needed, specifically how Hebbian learning in a separate network is supposed to correlate with the importance of neurons in the main network trained with backpropagation.
2. More importantly, the experiments are way too lacking. The method is only tested on MNIST with 0-4/5-9 as two separate tasks and only compared to the vanilla network. The paper mentioned quite a lot of previous work but they are not compared as baselines. It's understandable that these bio-inspired methods might not surpass SOTA methods in the field but at least the method should be tested on a range of scenarios against some reasonable baseline. The experimental evaluation is severely limited, lacking comparisons to established continual learning methods. The choice of MNIST with a simple 0-4/5-9 split is not sufficient to demonstrate the effectiveness of the proposed approach. The absence of comparisons to other continual learning baselines makes it impossible to assess the relative performance of the method.

### Questions
In addition to the weaknesses mentioned above:
1. How is this linked to previous methods that also utilize important scores and what's the advantage of Hebbian learning here? I also expect more evidence that the computed importance score can actually identify important neurons, for example, how does the method compare to pre-assigning a set of neurons for each task?
2. How is the network tested on different tasks? Is the whole network used in each task or some mask is used even in the forward pass?

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
The paper connects the Hebbian learning with neuron freezing, computing neuron importance through a Hebbian layer and selectively freezing neuron weights based on importance scores. Subsequently, it uses hooks to selectively train and infer, effectively assigning different neurons for each task. The paper combines biological neural mechanisms with continual learning, providing some insights. However, it does not sufficiently summarize previous work, and the novelty of this idea is limited. Additionally, the figures and tables in the paper are quite rudimentary, lacking details on model training and testing. The results are not comprehensively compared with existing methods, which makes them unconvincing.

### Strengths
The paper connects the Hebbian learning with neuron isolation, selectively freezing neuron weights based on importance calculation, which provides some valuable insights.

### Weaknesses
1) While experiments demonstrate that Hebbian learning mechanism prevents catastrophic forgetting, it is not clear why (conceptually) this would be the case. In other words, why does association by activity select the nodes that are relevant for one task while excluding those that belonged to past ones? It may be my missing backgeound in the application of Hebbian learning, but I recommend authors to include a more detailed explanation of this part of the conceotual background for people who are lacking this background.

2) All experiments are basically the same measured with different metrics. One of the metrics would suffice.

3) Task identification and new task recognition is not a trivial task. Without this, it is questionable whether any method can be called to realize continual learning or not. (The authors mention that this is not a challenge they are tackling, but without this ffull continual learning setup the relevance of a destructive adaptation problem is questionable.)

### Questions
1. There have been many continual learning methods based on Hebb learnin before; what advantages does the proposed method have over these previous works? 
2. What are the specific implementations of the model training and testing process, and can they be described in detailed mathematical terms? 
3. Are there more comprehensive and detailed comparison results available in the paper?

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 3

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
The authors proposed a novel algorithm named “CAN” that can dynamically freeze weights to prevent catastrophic forgetting. CAN uses Hebbian rule to measure the importance of neurons with presented tasks. While the dynamic gating of gradient flow onto individual neurons may sound interesting, this study does not provide any convincing evidence that this algorithm can be used in modern deep learning models.

### Strengths
The use of Hebbian rule when evaluating the neurons' importance is interesting.

### Weaknesses
1. The authors did not provide specific details that are crucial for their study. Specifically, the second equation does not include any indices, which makes its interpretation difficult, and the architecture of a neural network used in this study is not specified. 

2. The authors split MNIST into two disjoint tasks. The experimental setup is too simple to evaluate the algorithm properly. 

3. Although multiple earlier studies used MNIST to evaluate continual learning algorithms, the authors did not provide any comparison to other studies.

### Questions
“CAN” evaluates the importance of individual neurons sequentially, but can the authors evaluate its complexity? Modern deep learning models have a massive number of neurons, and if CAN requires too much computations, it may not be practical.

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper provides a method to prevent catastrophic forgetting, with externally-defined task boundaries, using Hebbian learning to enable/disable neurons that were relevant for a prior task.

### Strengths
If there is a good conceptual reasoning behind the proposed use of Hebbian learning (see my comment on the matter under "weaknesses"), the direction explored in the paper may be promising.

### Weaknesses
1) While experiments demonstrate that Hebbian learning mechanism prevents catastrophic forgetting, it is not clear why (conceptually) this would be the case. In other words, why does association by activity select the nodes that are relevant for one task while excluding those that belonged to past ones? It may be my missing backgeound in the application of Hebbian learning, but I recommend authors to include a more detailed explanation of this part of the conceotual background for people who are lacking this background.

2) All experiments are basically the same measured with different metrics. One of the metrics would suffice.

3) Task identification and new task recognition is not a trivial task. Without this, it is questionable whether any method can be called to realize continual learning or not. (The authors mention that this is not a challenge they are tackling, but without this ffull continual learning setup the relevance of a destructive adaptation problem is questionable.)

### Questions
See point (1) above.

### Soundness
2

### Presentation
2

### Contribution
2
