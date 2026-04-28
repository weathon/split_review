# Gradient-based inference of abstract task representations for generalization in neural networks

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 5, 6, 5

## Abstract
Humans and many animals show remarkably adaptive behavior and can respond differently to the same input depending on their internal goals. The brain not only represents the intermediate abstractions needed to perform a computation but also actively maintains a representation of the computation itself (task abstraction). Such separation of the computation and its abstraction is associated with faster learning, flexible decision-making, and broad generalization capacity. We investigate if such benefits might extend to neural networks trained with task abstractions. For such benefits to emerge, one needs a task inference mechanism that possesses two crucial abilities: First, the ability to infer abstract task representations when no longer explicitly provided (task inference), and second, manipulate task representations to adapt to novel problems (task recomposition). To tackle this, we cast task inference as an optimization problem from a variational inference perspective and ground our approach in an expectation-maximization framework. We show that gradients backpropagated through a neural network to a task representation layer are an efficient heuristic to infer current task demands, a process we refer to as gradient-based inference (GBI). Further iterative optimization of the task representation layer allows for recomposing abstractions to adapt to novel situations. Using a toy example, a novel image classifier, and a language model, we demonstrate that GBI provides higher learning efficiency and generalization to novel tasks and limits forgetting. Moreover, we show that GBI has unique advantages such as preserving information for uncertainty estimation and detecting out-of-distribution samples.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors introduce Gradient-Based Inference (GBI) of abstract task representations, a method that enables neural networks to infer and adapt task representations dynamically, promoting faster learning and better generalisation. Inspired by human adaptability—where task abstractions allow flexible responses to the same input depending on internal goals—their approach enables neural networks to infer and adapt task representations on the fly.

They frame the setting as an optimisation problem through variational inference, and their GBI uses backpropagated gradients to infer and adjust task representations in a neural network. Experiments in a range of domains including image classification and language modelling demonstrate benefits in learning efficiency, generalisation, and reduced forgetting, as well as its performance in uncertainty estimation and out-of-distribution detection.

### Strengths
- originality and contributions: This approach brings insights from cognitive science on human task learning and generalisation to deep learning. Their gradient-based inference (GBI) method introduced in the paper is novel, and seems to be an innovative application of gradients in task inference and adaptation beyond traditional optimization. Furthermore, by positioning GBI as a model capable of estimating uncertainty and detecting out-of-distribution samples, the work brings a fresh perspective and could potentially bring new insights to the field. 
 - significance: the problem setting is an important one: enabling artificial agents to flexibly to situations depending on their varying goals. The connections made to human and animal cognition and learning provide a solid foundation for this setting, grounding the approach in well-established principles of adaptive behaviour and task representation in human learning.
 - The paper demonstrates the effectiveness across varied tasks highlighting its potential as a versatile domain-agnostic approach. Overall their results demonstrate some promising advantages in learning efficiency, generalisation, and uncertainty estimation.
 - The inclusion of the code (via link to an anonymous repo) is appreciated for reproducibility and clarifying implementation details (however the repository would benefit from better organisation, see weaknesses).

### Weaknesses
 - motivation for gradient-based approach: the motivation for adopting a gradient-based approach could be clearer, as the paper does not sufficiently explain why gradients offer an advantage for task inference and recomposition over alternative methods. While gradient-based updates are obviously often employed in optimisation, it is less intuitive why they would be particularly effective in inferring abstract task representations or detecting out-of-distribution samples. A more thorough discussion grounding and comparing the gradient-based approach with other task inference methods, and meta-learning perspectives could help to clarify the benefits here. Specifically, the paper lacks a discussion on how the gradient-based approach avoids issues such as task abstraction misalignment, where the inferred task representation does not accurately reflect the current state of the network parameters. Furthermore, the paper does not adequately explore how this approach compares to methods that explicitly learn task embeddings or use attention mechanisms to infer task context.
 - The section on the one-step gradient update and maximal entropy initialisation could benefit from a clearer, more intuitive explanation. To improve clarity, the authors could add a visual schematic that illustrates the process step-by-step, and how a single gradient update shifts this initial state towards a more task-specific representation. The current explanation lacks detail on how the maximal entropy initialization is achieved and how it interacts with the subsequent gradient update to ensure effective task representation learning. A more detailed explanation of the mathematical underpinnings of this process would be beneficial.
 - Improving coherence: the paper would benefit from better coherence as the flow between sections feels disjointed. This makes it challenging to follow the core narrative. While each section presents important concepts mostly clearly, there is often a lack of clear transitions that tie ideas together leaving the reader to infer the connections. For example, the jump from theoretical discussions of gradient-based inference to experimental details seems abrupt, and then later suffers from limited explanation of how each experiment directly relates back to the proposed framework. A bit more introduction and summarisation at the beginning and end of sections, focused on tying each section to the core ideas would improve the flow of the paper. The paper would benefit from a more explicit discussion of how the experimental setup validates the theoretical claims made about GBI.
 - limited use of intuitive examples: incorporating a few straightforward examples or analogies could provide readers with a more accessible understanding of the contributions being presented. For instance, using a simple scenario (like inferring a task from partial information in an everyday context) could illustrate how the model operates based on gradient information to infer task information and provide useful uncertainty estimates. The current lack of such examples makes it difficult for readers to grasp the practical implications of the proposed method.
 - lack of comparison to important uncertainty estimation methods: while the paper claims advantages in OOD detection and uncertainty estimation, the results provided are not compared against established methods like ensemble approaches. The paper should include comparisons to Bayesian neural networks and other state-of-the-art uncertainty estimation techniques to properly contextualize the performance of the proposed method.
 - poorly organised code: to improve accessibility, the authors could streamline the repository, making it quicker and easier to connect model implementations with the methods and experiments described in the paper.

### Questions
- can the motivation for the gradient-based inference be described more clearly and intuitively? particularly, relating back to the problem setting and the limitations of existing methods.
 - how do the uncertainty estimates and OOD detection capabilities provided by the model compare to other approaches like ensembles or Bayesian neural networks?
 - given that the authors ground the problem setting and draw inspiration from human cognition and learning, do the authors feel their approach has biological plausibility at some level?

Overall, the discussed limitations hold it back from a higher score, however, the paper's originality and promising empirical results make it a interesting contribution. With a clearer exposition and better grounding/comparisons to other approaches, I would raise my score.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a method of incorporating a task obstruction process to improve the performance of neural networks. It considers the framework in which a likelihood function is maximized with respect to the network weights with task abstraction data included as inputs of contextual information in the training phase and the abstraction data is estimated via gradient descent in the test phase. It proposes a method of approximating the iterative optimization of task obstruction with a one-step gradient update. The proposal is based on insights from neuroscience about the roles played by intermediate abstraction in performing tasks and techniques in variational inference to handle contextual information with latent variables.

### Strengths
- A simple and effective method of approximating the iterative optimization of task obstruction is proposed. It is achieved by taking the maximum entropy point as the initial value and updating it with a one-step gradient update. The validity of this approximation is checked experimentally (Fig. 3G, H).

- Experiments show the superiority of the proposed method to the canonical classifier in OOD detection(Table 3, Fig 4A, B, C).

### Weaknesses
 - The training methods used in the experiments (sequence prediction by an RNN and data reconstruction by an autoencoder with its latent variables concatenated with contextual information) are not exactly the same as the one mentioned in Section 2 (MLE of the likelihood function (1)). It is not mentioned in the paper how the extensions to those variants do (or do not) affect the argument regarding the proposal in Section 2.

 - The purpose of the experiments comparing LSTM and GBI-LSTM (Fig. 2, Fg.3D,E, 5A,B,D) is not clear. It seems to me that they are just confirming the impact of the input of task labels for the sequence prediction problems with multiple tasks. It is preferable if this point is clarified in line with the motivations or expectations in Section 1 or Section 2.

 - Experiments imply that the canonical classifier may have better accuracy than the proposed methods (Table 2), but no reasoning for this is provided. It does not throw away the value of the superiority in OOD detection. Rather, the trade-off relation between them is worth a remark if it is confirmed to exist.

 - The following references are not found in the submission: (L357)"supplementary material". (L396)"Table S8"

### Questions
- Please consider the possibility of the clarifications mentioned in the weaknesses section.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
Inspired by cognitive science, the authors identify the lack of an efficient module for inferring the current task in current models. According to the authors, previous approaches to task inference do not meet the following two assumptions:
1. lack of efficient detection if the task has been repeated
2. lack of recomposing mechanism of previously learned tasks.
The authors propose an approach grounded in variational inference, using an expectation-maximization-like framework, and they demonstrate GBI’s effectiveness across synthetic, image classification, and language modeling tasks.

### Strengths
1. Clear and relevant objective. The aim of the work is clearly defined.
2. The authors provide code.
3. Experimental validation on various scenarios, from synthetic datasets to complex tasks (image classification and language modeling).

### Weaknesses
Although I appreciate that the authors examined their method on various scenarios, I am not sure if the complexity of these tasks is enough. For example, in OOD detection, adding a comparison of CIFAR10 vs SVHN datasets would be valuable. The current OOD experiments are limited to MNIST and fMNIST, which are relatively simple datasets. The lack of evaluation on more complex, real-world datasets makes it difficult to assess the practical applicability of the proposed method. Furthermore, the choice of using human-provided labels for task abstraction might limit the model's ability to generalize to scenarios where such labels are not readily available. The paper also lacks a thorough investigation into the sensitivity of the method to the quality of these task abstractions.

I am very curious about catastrophic forgetting matters. The authors gently mentioned this feature of their method, but it was only evaluated on the toy dataset; why? Could you provide more experiments in this area? The absence of a comprehensive evaluation on standard continual learning benchmarks is a significant gap. The paper does not explore how the method performs when faced with a sequence of tasks, and it is unclear how well the proposed approach mitigates catastrophic forgetting in more complex scenarios. The evaluation on the toy dataset is insufficient to demonstrate the method's effectiveness in addressing this critical issue.

### Questions
I am very curious about catastrophic forgetting matters. The authors gently mentioned this feature of their method, but it was only evaluated on the toy dataset; why? Could you provide more experiments in this area?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors propose a method called GBI to train a recurrent and convolutional neural network to infer the task category during test time. The inference is driven by gradient updates only at the task category layer, which can either be done iteratively or by approximating the maximal entropy point, while keeping the rest of the weights fixed. The authors demonstrated the benefits of this method across a variety of toy, image generation and language generation tasks in terms of a lower training loss. Additionally, the authors argue that once the model learns different task representations, only the task category layer needs to be optimized to decrease test or generalization error.

### Strengths
-- included anonymous code for replication
-- demonstrated generality of claim that using gradients to infer task category improves performance across 3 modalities, toy, vision and language tasks.
-- One step gradient update by symbolically estimating the optimal point seems to be novel. 
-- Gradient based inference improves interpretability during training (e.g. bayesian inference like estimation) and to identify OOD samples.

### Weaknesses
 -- Please include a diagram of the GBI-LSTM architecture for the toy and language tasks. Specifically which synapses are modified during training and inference time i.e. which is the task abstraction layer/weights z? (Pg 5, line 242)
-- The idea to optimize only the input representation weights instead of the entire model is not novel. This idea dates long back to the idea of learning schemas and adjusting new information to fit the prior learned template (Lampinen, McClelland 2020 PNAS; Kumar et al. 2024 arXiv 2106.03580).
-- the claim that GBI-LSTM shows no signs of forgetting compared to the LSTM is not strong. The baseline MSE performance is 0.24, which the GBI maintains for new datasets, but the deviation by LSTM does not seem to be significant (Table 1). Was a statistical test done to compare LSTM and GBI performance?
-- Why learning to infer task category improves learning and generalization in these tasks is unclear. Perhaps the authors can perform low dimensional analysis to show how the network learns to represent different datasets into non-overlapping subspaces and during inference, the network's activity converges towards a specific prior learned subspace or learns to compose them (Lin et al. 2024 arXiv 2309.04504)?
-- The authors argue that GBI improves generalization loss in language prediction task. Although the baseline LSTM shows consistent loss of 6.8 (I assume all model weights are fixed), the GBI loss starts off higher of around 6.95 and decreases to 6.6 over 100 optimization steps. Does the loss continue to decrease with longer optimization steps? If not, is a generalization loss of 6.6 significant compared to 6.8? 
-- Given that the models are an LSTM and not a large model, I thin it is reasonable to expect at least 30 seed runs instead of 4 as in Fig. 5D to increase the confidence in results, especially when the difference afforded by LSTM and GBI is small. 
-- Since the authors used LSTM for toy dataset, and a CNN for image, it would have been a solid contribution if the authors demonstrated GBI using a simple transformer architecture for language prediction instead of LSTM.


### Questions
-- Is the one-step gradient update method novel? Or was it developed prior?
-- giving task category as input should significantly reduce the training complexity of needing to infer the task (Kumar et al. 2022 Cerebral Cortex). Why was the difference in training loss not as apparent? Did the authors perform hyper parameter sweeps for the learning rate and number of units? It is easy to choose a set of hyper parameters where the distinction between LSTM and GBI is artificially similar. 
-- Why was LSTM chosen instead of GRU or a Vanilla RNN? Training an LSTM on the simple toy dataset might be an overkill. 
-- why is the ratio of shared units between LSTM and GBI different in the 0th binned training block (Fig. 2C)? They should aggregated such that the initialized activation is the same for comparison.

### Soundness
2

### Presentation
3

### Contribution
2
