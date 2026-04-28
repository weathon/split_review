# Instilling Inductive Biases with Subnetworks

- Decision: Reject
- Avg Score: 6.67
- Scores: 8, 6, 6

## Abstract
Despite the recent success of artificial neural networks on a variety of tasks, we have little knowledge or control over the exact solutions these models implement. Instilling inductive biases --- preferences for some solutions over others --- into these models is one promising path toward understanding and controlling their behavior. Much work has been done to study the inherent inductive biases of models and instill different inductive biases through hand-designed architectures or carefully curated training regimens. In this work, we explore a more mechanistic approach: \emph{Subtask Induction}. Our method discovers a functional subnetwork that implements a particular subtask within a trained model and uses it to instill inductive biases towards solutions utilizing that subtask. Subtask Induction is flexible and efficient, and we demonstrate its effectiveness with two experiments. First, we show that Subtask Induction significantly reduces the amount of training data required for a model to adopt a specific, generalizable solution to a modular arithmetic task. Second, we demonstrate that Subtask Induction successfully induces a human-like shape bias while increasing data efficiency for convolutional and transformer-based image classification models.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors present a new approach called Subtask Induction, which involves extracting specific problem-solving abilities from trained neural networks. They achieve this by isolating a subnetwork responsible for a particular task within a larger neural network and initializing another network with only these subnetwork weights, leaving the rest randomly initialized. The authors demonstrate subtask induction on an arithmetic task and image classification on a novel dataset, Mean-pooled ImageNet, which requires networks to learn shape information rather than texture information. The approach is an interesting demonstration that (1) these subnetworks exist and can be extracted and transferred to new networks, (2) SGD learns to use these subnetworks, and this leads to more efficient learning on new tasks.

### Strengths
I really enjoyed this paper - it takes the observation from the mechanistic interpretability literature that deep networks learn subnetworks to solve specific tasks and uses it to derive a simple method for extracting these subnetworks (essentially by optimizing a sparsity mask over the parameter on a distribution of problems that only require the subnetwork) and then they randomly initialize the remaining weights of a network and train on a second task that requires the shared skill. The results on the arithmetic task provide a proof of concept, but vision experiments are particularly interesting because they show that these subnetworks can be discovered in real data, provided you have dataset which allows you to extract this.

### Weaknesses
The requirement for a dataset like mean-pooled imagenet to extract the subnetwork significantly constrains how widely applicable this paper is as a method---it essentially requires you know the task in advance and how to specify it with examples that are sufficiently different from typical examples in the training set---but I still think that it is an interesting demonstration.

I would have liked to see some examples of where it fails: for example, if you don't have a clear separation between IID samples and the target task, I would expect it would struggle. Specifically, the method relies on the ability to isolate a subnetwork by training on a distribution of problems that *only* require that subnetwork. If the training data for the subtask is not sufficiently distinct from the data used for the primary task, it's unclear if the extracted subnetwork would represent a generalizable skill or just a memorization of the specific training examples. This is a critical limitation that needs further exploration. For example, if one tried to extract a subnetwork using a dataset that was simply a subset of the original training data, it's likely that the extracted subnetwork would not provide any benefit when transferred.

### Questions
1. Did you study any tasks for which Subtask Induction performs poorly? 
2. If so, what are the characteristics of those tasks?

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose Subtask Induction, a way of implanting inductive bias by identifying a subnetwork that performs a specific task, and only training the rest of the model. The idea is that the rest of the model is forced to learn, bounded to performing that specific (wanted) task. The method is tested on two problems. The first one is the reconstruction of a discrete mathematical operation, and the second is image classification on 16-class ImageNet. In both cases Subtask Induction obtains better perfomances in situations where the inductive bias was necessary and that were hard to learn for a model where this was not instilled.

I lean towards acceptance because:
- The idea of inducing a specific inductive bias is intriguing and deserves to be discusses in a wider context. Similarly to transfer learning, one could imagine collections of pretrained subnetworks that are specifically tailored towards a task, or that avoid some specific spurious correlation.
- The paper is well-written and easy to follow, and the code is well-documented. 

I score the paper as a 6, which I reserve myself to lower if some of the answers to my questions are not satisfactory or if some other reviewer.

The reason for not giving a higher score is because though the idea is nice, (i) it is hard to visualize how this method could be actually implemented efficiently and (ii) the evidence is purely empirical, and the set of experiments is not very extensive. The reason why it is not too extensive is that it is hard to devise suitable testing situations, which sends me again to point (i).

### Strengths
- The method can potentially help solving, in the long run, problems related to spurious correlations, out-of-domain generalization, and more. 

- A well-documented code is made available through an anonymous link.

### Weaknesses
 - The method is valid for one subtask, but extending it to more than one is non trivial and perhaps not possible, since the subnetworks could either overlap or occupy the whole network (in which case we would just be doing transfer learning). It's unclear how the method would handle multiple subtasks simultaneously, as the identified subnetworks might interfere with each other, or simply end up covering the entire network, thus negating the benefits of subtask-specific training. This limitation significantly restricts the practical applicability of the method to scenarios requiring multiple inductive biases.

- It is not easy to identify the subnetwork of a model that performs a subtask. I see this as a major limitation, but it doesn't seem impossible to me that in the future there could be some solutions. The process of identifying a subnetwork that performs a specific task is not straightforward, and the paper does not provide a clear methodology for this. The current approach relies on training binary masks, which can be computationally expensive and may not always converge to an optimal subnetwork. The lack of a systematic approach for subnetwork identification is a major hurdle for the practical use of this method.

- The method relies on finding a subnetwork, which seems a very intensive work. The process of finding a subnetwork requires training binary masks, which is computationally intensive and requires significant resources. This makes the method less practical for large-scale models or complex tasks. The paper does not discuss the computational cost of subnetwork identification, which is a crucial factor for evaluating the feasibility of the method.

- The method is validated on a limited number of tests. If on one side it is hard to find real-life examples (the authors had to resort to an adhoc dataset), they could at least have tried with some other mathematical operations (and there, architectures since in principle the method should apply to any architecture, even e.g. MLPs). The empirical evaluation of the method is limited to two specific problems, and it is not clear how well it would generalize to other tasks or datasets. The authors could have explored a wider range of mathematical operations and model architectures to provide more comprehensive evidence of the method's effectiveness. The lack of diverse experiments makes it difficult to assess the robustness and generalizability of the method.

### Questions
- Can the authors elaborate on the difference between their method and transfer learning? The two seem very similar to me, and transfer learning would be the limit for very big subnetworks.

- In transfer learning, we fine tune by first freezing the model and training only the last layer, and then training the whole model with a very small learning rate. Here, the second step was deliberately removed in order to enforce the subtask. Could a second step of fine tuning help?

- Is the dataset available at this point? I cannot find where it is written.

- Could it be possible to benchmark this method on datasets for spurious correlations?

- What do the found subnetworks look like? Are they restricted to a single layer? Are they dense blobs? How many paths do they comprise?

- How does the method deal with dropout? With dropout there are no (or fewer) preferential paths, so I would assume the subnetworks would be much bigger.

- The subnetwork can only be transferred without varying the architecture, right? E.g. there cannot be a subnetwork which is only made of two layers, and I plug these two layers into my model. Is this right? Or, if I understood wrong, how is the subnetwork transferred when the architecture changes?


Other minor things:
- Figure 1 is not referenced in the text
- typo on page 13: implementatione
- In section 3.1/2 it is sort of obvious that the masks are trained on well-trained models (instead of e.g. models at initialization) but it is not explicitly written
- I would put a parenthesis before the modulo operators, because I was initially confused. For example, I would write

### Soundness
2 fair

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper discusses the problem of injecting inductive bias into a network, via the proposed subtask induction method. In particular, using an auxiliary subtask dataset, the authors first identify a subnetwork that achieves the subtask and use it as the initialization for another network, which is subsequently trained for a closely related downstream task. To show the effectiveness of the method, this paper conducted two sets of experiments: an arithmetic computation with decoder-only transformers, and a vision experiment.

### Strengths
Overall the problem statement is quite interesting and the presentation is very clear and easy to follow.

### Weaknesses
I found the motivation to be a little lacking. The authors mentioned mechanistic interpretability, however, it is unclear to me (based on the current writing) why we should care about such interpretability. I would encourage the authors to give some examples to demonstrate how it can be used in reality. For example, what are some scenarios in which we can accurately define subtasks (in the vision experiment you mention shape vs texture, I understand that the problem is extensively studied, but it is also kind of artificial)?

I am also concerned about the experimental setup of the vision experiments. Specifically, the comparison in Figure 5 seems unfair, as the Subtask Induction models are initialized with ImageNet pretrained weights. It's unclear if the performance gain is solely due to the subtask induction or simply the pretraining. A more controlled experiment would involve finding a subnetwork from a randomly initialized network that performs well on the mean-pooled ImageNet. Furthermore, the right figure in Figure 5 shows no change in accuracy after the subnetwork transfer, which is quite surprising. It would be helpful to know if the subnetwork weights were frozen after the transfer. If not, it would be interesting to see if the accuracies on the mean-pooled ImageNet increase with further training.

Finally, the description of each row in Table 1 is not detailed enough. It's not clear how the data augmentation is performed for the 'model+DA' case, and whether the 'model+pretrained' case involves finetuning only the last classification layer. If so, it would be important to specify the details of this finetuning process. The current description makes it difficult to understand the differences between these baselines.

### Questions
1. For the GPT2 experiment, did you use their pre-trained weights, or did you train everything from scratch?
2. If you tokenize the integers from {0, ..., 999} with GPT2tokenizer, 181 of them are actually tokenized into 2 tokens (for example, 521->'5', '21'). If the original tokenizer is used, I would suspect the model cannot really learn the underlying equation (this may also be why you need many disambiguous examples).
3. How does the number of ambiguous examples affect the accuracy? Does the performance decrease with more examples?
4. In the first paragraph in section 5.3, to confirm, you discover pretrained ResNet18 and ViT, are they pretrained on only ImageNet? If you have a randomly initialized ViT/RN, can you still discover a subnetwork that works well on Mean-pooled ImageNet? 
5. What is the training setup of Figure 5? Did you train every model on 213k images of the 16-class ImageNet? The comparison looks a little unfair to me, as the Subtask Induction models have been pretrained (maybe on the original ImageNet? This question is related to the previous point). A more fair comparison will be that you find a subnetwork from a randomly initialized network that performs well on the mean-pooled imagenet.
6. In the right figure in figure 5, the accuracies don't change.  Is this because you froze the subnetwork's weights after transferring? If you don't freeze the weights, will the accuracies on mean-pooled imagenet increase?
7. Can you also give the detailed setup of each row in Table1? My current understanding is: model+subtask induction = model pretrained on all original ImageNet, find subnetwork using the mean-pooled data, then continually train using 213k 16-class imagenet. model from scratch is trained to perform 16-class classification directly. model+DA and model+pretrained are where I get confused: a) how exactly is the data augmentation performed? and b) is "model+pretrained" where you finetune only the last classification layer? If so, how exactly is the last-layer finetuned?

miscellaneous: table caption should be on top; paragraph on top of section 4.3 'diambiguation'->'disambiguation'.

I'm happy to raise my rating if the authors can address my concerns.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good
