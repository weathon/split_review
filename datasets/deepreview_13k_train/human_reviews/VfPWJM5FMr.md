# ColA: Collaborative Adaptation with Gradient Learning

- Decision: Reject
- Scores: 6, 5, 3

## Abstract
A primary function of back-propagation is to compute both the gradient of hidden representations and parameters for optimization with gradient descent. Training large models requires high computational costs due to their vast parameter sizes. While Parameter-Efficient Fine-Tuning (PEFT) methods aim to train smaller auxiliary models to save computational space, they still present computational overheads, especially in Fine-Tuning as a Service (FTaaS) for numerous users. We introduce Collaborative Adaptation (ColA) with Gradient Learning (GL), a parameter-free, model-agnostic fine-tuning approach that decouples the computation of the gradient of hidden representations and parameters. In comparison to PEFT methods, ColA facilitates more cost-effective FTaaS by offloading the computation of the gradient to low-cost devices. We also provide a theoretical analysis of ColA and experimentally demonstrate that ColA can perform on par or better than existing PEFT methods on various benchmarks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work proposed a method termed ColA, for efficiently adapting a pretrained model for a downstream task. In particular, the proposed method assumes an auxiliary set of parameters, which are used to parametrize auxiliary functions, that take the hidden representation of a layer and transform it by adding a computed delta shift, before it is fed as input to the next layer.

To avoid having to store and update the parameters of these light-weight auxiliary models on the GPU, this work proposes a "Gradient Offloading" strategy, wherein gradients with respect to the change in hidden representations are offloaded to the CPU, and a gradient update with respect to the auxiliary parameters model parameters is computed (and potentially updated) offline on the CPU. The proposed ColA method is model-agnostic, and can be adapted to any set of auxiliary models. Moreover, the weights of the pretrained model themselves are never altered during fine-tuning.

The authors propose ColA for offering Fine-Tuning as a Service (FTaaS) in commercial settings. The idea is that ColA can be used to provide mass personalization of foundation model fine-tuning for users. Users can own their own set of auxiliary parameters used to update the hidden representations of the pretrained network during the forward pass, and can share in the computational update of these auxiliary parameters in a federated-learning style manner.

Extensive numerical experiments are provided on the following tasks
* Sequence Classification -> RoBERTa (base) on GLUE
* Sequence to Sequence Modelling -> BART (base) on Financial Phrase Bank, WikiSQL, DART
* Causal Language Modelling -> GPT2 with instruction tuning on Dolly

comparing the following methods
* full fine-tuning
* LoRA
* AdaLoRA
* IA3
* Prompt Tuning
* Prefix Tuning
* P-Tuning

and comparing the following set of auxiliary weights for their proposed ColA method
* Low Rank
* Linear
* MLP

### Strengths
### Originality
* Novelty of ColA: The main innovation in ColA is the ability to compute updates to auxiliary parameters offline. Previous approaches for efficient model adaptation include: Fine-tuning Adapter layers, which place learnable layers in-between existing learnable layers; Low-Rank Adaptation (LoRA), which introduce two low-rank matrices to parametrize the updates of pretrained weigh matrices; and Prefix Tuning, which prepends sequence of learnable tokens as input to the network. Conceptually, ColA can be used with many of these strategies, and unlocks the ability to compute the auxiliary parameter updates offline.

### Clarity
* The paper is well written and sufficiently easy to follow given all the technical components introduced.

### Significance
* The proposed Fine-Tuning as a Service (FTaaS) framework is interesting in my personal opinion, and likely to be of increasing relevance to the ICLR community. Of notable interest is the intersection of this framework with Federated Learning, which has also been proposed for model personalization, but perhaps in more general settings (i.e., without placing constraints on adapting a small set of auxiliary parameters for a large frozen foundation model).

### Weaknesses
Weaknesses
* Not clear how to align proposed method with other optimization strategies (i.e., beyond gradient descent)
* Still need to forward/backward propagate the model K times for K users; i.e., the decoupled gradient computation and adaptation does not address this issue
* To compute the change in hidden state at some layer $m < M$, you need to have first computed the hidden state at layer $m-1$. Since this computation is carried out on the GPU (server); it appears as though you either need to eventually send the local model to the server and place it on device, or you have numerous iteration rounds between the server and client to compute a single forward pass, and send the targets for an offline update of the auxiliary parameters.
* While it is claimed that the offline update is equivalent to the online update of auxiliary parameters, this does not seem to be the case in practice (based on training curves, gradient magnitudes, and performance compared to non-offloaded computations on considered tasks)
* It is not clear to me how memory is actually saved by offloading gradients with respect to the small set of auxiliary parameters to the CPU, and to what degree training is slowed down due to this offloading.


* Minor error; page 4. I believe you mean the gradient of the auxilary parameters $\nabla w_{1:M}$
* Minor error; page 5. I believe you mean $\nabla \delta h^t_m = g^t_m(x^t_m)$

### Questions
* How much memory do you actually save by offloading gradients with respect to the small set of auxiliary parameters, and what is the increase in training time due to the offloading and recompilation phase? Please include logs comparing ColA to baselines in terms of memory, forward time, backward time, and number of host-device transfers.
* Could you please clarify why the ColA LoRA updates (the best performing CoLA setting in Sequence Classification tasks) are not strictly equivalent to non-offloaded LoRA updates?

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
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a new fine-tuning method to reduce GPU computational and memory costs. Specifically, the method offloads the gradient update to the auxiliary variable from a GPU to a CPU. The authors provide theoretical analysis to justify its correctness. Based on this new learning method, the authors further introduce a collaborative learning framework. Experiments on RoBERTa and BART demonstrate the effectiveness of the proposed method.

### Strengths
-	The proposed method is simple and easy to implement.
-	Efficient fine-tuning is an important topic.

### Weaknesses
 - The motivation and advantages of moving gradient update to CPU are unclear. Specifically, it is not clear why offloading the update of auxiliary variables to the CPU is beneficial, given the potential communication overhead between the GPU and CPU. The paper does not adequately explain the trade-offs between computational speed on the GPU versus memory savings on the CPU, especially since the gradient computation still occurs on the GPU.
- The relationship between the proposed gradient learning and collaborative adaption is unclear. The paper introduces a gradient learning method and then mentions collaborative adaptation, but the connection between these two concepts is not well-established. It's unclear how the proposed gradient learning method facilitates or enhances collaborative adaptation. The problem setup for collaborative adaptation is also not clearly defined.
- The experiments do not include collaborative adaption. Although the paper discusses collaborative adaptation, the experimental section only focuses on single-model fine-tuning. This makes it difficult to evaluate the effectiveness of the proposed method in the context of collaborative learning, which is a key aspect of the paper's claims.

### Questions
-	As far as I understand, the key contribution of the proposed method is to offload the update for the auxiliary variables w to a CPU, rather than a GPU. After reading the paper, it is still unclear to me why this is desirable. Can the authors explain the motivation and advantages of doing so?
-	In Proposition 2, the model is assumed to be linear. How is this result related to the case considered in the paper where the model is a pretrained neural network?
-	It is unclear how the proposed gradient learning method related to collaborative adaptation. Why is gradient learning important for collaborative adaptation? What is the problem setup of collaborative adaptation in this paper?
-	The paper focuses on collaborative adaptation, but the experiments do not seem to include collaborative adaptation.
-	The communication cost between GPU and CPU is unclear.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a fine-tuning framework to improve the storage efficiency of parameter-efficient fine-tuning methods. Specifically, the proposed method proposes Gradient Learning to decouple the computation of the gradient of the model weights and the gradient of hidden features. For example, the main forward and backward pass through the model only calculates the gradient of the hidden features, and the calculation of the gradient of the model weights can be off-loaded to another low-cost device with an auxiliary quadratic loss. The main benefit is that the main forward and backward pass no longer needs to calculate the gradient of the model weights, which supposedly saves storage on the main device.

### Strengths
* **Gradient Learning is Novel**: the idea of decoupling the calculation of the gradient of the model weights and the gradient of hidden features seems novel. The paper also theoretically demonstrates the equivalence between the proposed decoupled update and the conventional update rules.

### Weaknesses
 * **Why is the method parameter-free?**: even though the proposed model offloads the update of adapter weights to a different device, it does not make it parameter-free. It is not very convincing to claim the fine-tuning method to be parameter-free. The core issue is that while the gradient computation for adapter weights is moved to another device, these weights still exist and are updated, thus the method is not truly parameter-free in the sense of not having any trainable parameters during the main forward and backward pass on the primary device.

* **Actual memory footprint not clear**: while the model claims to save storage on the main device, e.g., the GPU, the paper does not report the actual memory footprint during the forward and backward passes on the GPU. Compared to the small number of trainable parameters in LORA/adapters, the hidden feature maps and their gradients utilize the most memory. Offloading the gradient computation of the trainable parameters seems to only marginally improve memory usage on the main device. It would be great to see how much memory is actually saved on the main device by using the proposed decoupled update. The paper should provide a detailed breakdown of memory usage, including the memory consumed by hidden states, gradients of hidden states, and the adapter parameters, both with and without the proposed method. This would allow for a more accurate assessment of the method's memory efficiency.

* **Time efficiency not reported**: the method involves an update on a second low-cost device, e.g., a CPU. The paper does not discuss the impact on training time efficiency. The time taken to transfer gradients to the secondary device, perform the update, and transfer the updated parameters back to the main device should be considered. The paper should also discuss the potential for parallelization and asynchronous updates to mitigate the overhead of using a secondary device. A quantitative analysis of the end-to-end training time, including the time spent on both devices, is crucial for evaluating the practical viability of the method.

* **Some method components are not very relevant**: the discussion on parameter merging is not very relevant to the main proposed method. It is also not clear which experiments underscore the benefits of user collaboration as claimed in the contribution. Overall, the components of parameter merging and user collaboration seem tangential to the proposed method and are not well analyzed through experiments. The paper should focus on the core contribution of decoupled gradient computation and provide a more thorough analysis of its benefits and limitations. The discussion of parameter merging and user collaboration should be either more directly tied to the core method or removed to streamline the paper's focus.


Minor:
* The number of trainable parameters of Co1A in Table 2 is much smaller than that of LORA. Is this a typo?

### Questions
* Could the authors comment on the parameter-free property of the method? 
 
* Could the authors report on the actual memory usage and savings on the main device? 

* Could the authors provide a discussion, preferably quantitatively, of the impact on the time efficiency?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
