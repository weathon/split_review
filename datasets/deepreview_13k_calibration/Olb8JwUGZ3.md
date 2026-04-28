# When and how are modular networks better?

- Decision: Reject
- Avg Score: 4.25
- Scores: 3, 3, 8, 3

## Abstract
Many real-world learning tasks have an underlying hierarchical modular structure, composed of smaller sub-functions. Traditional neural networks (NNs), however, often ignore this structure, leading to inefficiencies in learning and generalization. Leveraging known structural information can enhance performance by aligning the network architecture with the task’s inherent modularity. In this work, we investigate how modular NNs can outperform traditional dense networks by systematically varying the degree of structural knowledge incorporated. We compare architectures ranging from monolithic dense NNs, which assume no prior knowledge, to hierarchically modular NNs with shared modules, which leverage sparsity, modularity, and module reusability. Our experiments demonstrate that incorporating structural knowledge, particularly through module reuse and fixed connectivity, significantly improves learning efficiency and generalization. Hierarchically modular NNs excel in data-scarce scenarios by promoting functional specialization within the modules and reducing redundancy. These findings suggest that task-specific architectural biases can lead to more efficient, interpretable, and effective learning systems.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper investigates how modular neural networks can outperform traditional dense networks by varying the degrees of structural knowledge used. They compare monolithic and hierarchically modular neural networks on boolean functions and MNIST-based modular tasks. They analyze generalization performance, training efficiency (FLOPs required for training), and factors that influence generalization in modular networks. The experiment results show that incorporating structural knowledge, especially via module reuse and fixed connectivity, helps improve learning efficiency and generalization.

### Strengths
* The experiment results are comprehensive across various architectural designs with varying levels of structure knowledge, comparing their generalization performance and training efficiency. 
* They discover specific design choices for modular networks that help generalization for boolean functions and MNIST-based modular tasks.

### Weaknesses
 * The paper needs much better contextualization relative to prior works. Each architectural choice—such as learning inter-module connectivity and modular sharing—should be supported with citations of relevant papers. Are these established approaches for designing modular networks, or are they introduced by the authors? Furthermore, are Boolean function and MNIST-based tasks standard evaluation protocols for modular networks? 
* The paper lacks proper citations in several sections. The design choice for the Boolean function and MNIST-based task follows the approach in [1] and should be cited accordingly.
* Their experiments are limited to MLPs on boolean functions and MNIST, which are relatively simple architectures and tasks. It is unclear how the findings of this paper would generalize to more complex architectures and problem settings. 

### Questions
It is mentioned in the weakness section.

### Soundness
3

### Presentation
2

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
The paper explores how modular neural networks (NNs) can outperform traditional dense NNs, especially when tasks have an underlying hierarchical structure. The authors compare different types of NNs, from dense and sparse monolithic models to modular networks that incorporate various levels of task-specific structural information. They show that modular networks, especially those designed to reuse modules or with fixed connectivity, perform better in terms of learning efficiency and generalization, particularly when data is limited.

### Strengths
1.The paper provides a detailed comparison of several NN architectures and clearly shows when modular networks have an advantage.

2. The paper takes a solid scientific approach exhaustively covering the different ways in which hierarchical modularity can be achieved (random, learnable, fixed). 

3.The paper is backed with controlled & thorough experiments on simple tasks such as Boolean functions and the MNIST dataset, where the underlying modularity is known.

### Weaknesses
A major limitation with prior work in hierarchical modular architectures is that such approaches haven't been shown to be effective on more complex tasks. In general, it seems that that, at scale, the inductive bias of hierarchical modularity may limit the models and choosing instead to use a less-constrained architecture, trained with more data, leads to better efficiency. This is the key message of the bitter lesson. While this systematic study is indeed very helpful in confirming when simple hierarchically modular inductive biases can enable more-efficient learning and / or better generalization, the challenge of understanding if this approach can scale still limits the practicality of this work.

### Questions
Covered in weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper explores how incorporating structural knowledge about a learning task into a neural network can significantly improve the learning efficiency and generalisation of the model compared to a dense end-to-end model. The task explicitly focuses on Hierarchical Binary Functions. The paper demonstrates that on increasingly more Hierarchical structured tasks, using modular structured networks can improve generalisation ability while reducing training and being performant in data-limited settings, outperforming conventional dense end-to-end models.

### Strengths
Very straightforward and coherent paper; clearly, time was taken to set up, analyse, and present the results. Very enjoyable to read. 

Although the task is simple, it highlights and showcases how incorporating the structural knowledge of the task can lead to significant performance increases.

**More specific**

Figure 1 is beneficial in understanding the different types of models explored. 

Clear and well-explained experiment details. That makes sense for the hypothesis being tested.

The mean and standard deviation are reported.

Future work looks very interesting and has a neat direction to take the work.

### Weaknesses
The MNIST Binary task- is a little confusing at first. Please add a walkthrough of the task to the appendix to aid readers' understanding. Specifically, it would be beneficial to clarify how the binary classification is performed on the MNIST digits, what specific digits are used, and how the hierarchical structure is imposed on this task. A more detailed explanation of the input data and the target output for this task is needed to ensure clarity.

The abstract (lines 23-24) states how this can lead to more interpretable learning. However, the body of the paper needs to explore or mention this again. Could the authors please add a section/paragraph clarifying how this leads to more interpretable networks? The paper should elaborate on the specific mechanisms that make the modular networks more interpretable than their dense counterparts. For example, are the modules learning specific features or sub-functions, and how can these be analyzed to understand the network's decision-making process?

**MISC**

Line 29-30: the wrong type of citation \citep{} should be used instead, unless quoting directly, then put quote marks around the text "".

Figure 1: The Purple box is not defined in the figure. What is it?

Figure 4: The first figure does not show the Monolithic with 25% Density; this figure is also hard to read; about the text, it is hard to see that the modular neural network "30%, 7.1%, and 5.9% of the weights of monolithic dense NNs for depths 1, 2, and 3" it would be nice to have a graph of the parameter counts, for each architecture.  It is difficult to discern the exact parameter counts from the current figure. A separate graph or table detailing the number of parameters for each architecture at different depths would greatly improve the clarity of the results.
Questions:

Line: 412 "Generalization on Seen Digit Combinations: Figure 7bb" the letter "b" is repeated. It should be Figure 7b.

### Questions
See weakness and in addition:

Could you explore more Hierarchical Tasks, it would be interesting to see how the networks perform on 4 and 5 depth tasks, and how this method scales? 

Are you able to interpret what the reusable modules are doing and how this compares to the dense neural network?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This work compares monolithic and modular neural networks on tasks based on hierarchical composition of boolean operations. The authors highlight that in this regime with limited available data, modular systems especially with ground-truth connectivity pattern generalizes considerably better than monolithic models. The tasks considered in the work are further extended to include an image classification sub-task through the MNIST dataset. The main contributions of the work highlights that in this task regime, modular systems outperform monolithic ones in low data regime, with further benefits when the connectivity structure is known and when modules are reused. Additionally, such benefits hold even with fewer parameters, as modular networks (and reusable patterns) reduce total parameter count.

### Strengths
- The authors construct controlled tasks with known connectivity patterns to evaluate if modular systems work well, and if they uncover the structure of the task.
- The proposed methodology of modular systems, with structural inductive biases and reusability, outperforms monolithic systems.

### Weaknesses
 - One of the biggest weakness of this work is that the kind of modularity and compositionality tested in this work is extremely limited. Unlike prior work [1,2] where modularity is really considered at a multi-task level, the considered work only trains each architecture on a single task which has limited and easier to discover modular structure as opposed to conditional modularity$-$ for example, if the authors trained a single model to perform a lot of different boolean tasks based on some task identification (eg. one-hot encoding or text descriptor) and saw a modular system considerably outperforming monolithic ones, that would be more of a testament of its performance benefits.

 - Additionally, the authors consider an extremely toy setup of modularity where the modular structure to be leveraged is not even input dependent (eg. different inputs need to be routed differently). In contrast, they look at just static selection procedures$-$ static selection of connectivity pattern, input selection and module selection.

 - The authors highlight the benefits of modular architectures on tasks with known modular connections by essentially including the known information about the task in the network architecture (eg. connectivity pattern, module details like the output should be one number, etc.). This really brings an important question of how transferable are the results from this work to more general-purpose hierarchical and modular tasks.

 - Finally, the Appendix shows that monolithic models are able to catch up to modular ones with increasing training data. Combining this information with the fact that the authors only consider this very specific class of toy tasks, it is extremely unclear how transferable the conclusions are. It would be much more convincing if the authors test their approach on some more complex tasks (eg. object centric learning, multi-task or few-shot learning problems, etc.). 

 - Furthermore, they could try boolean functions of increasing complexity$-$ like 100 input bits with larger depth and conditioning on some one-hot vector to describe different functional forms of the ground-truth.

 - The authors should also test their method on tasks that operate beyond interactions of just two bits. What about ternary interactions and other higher order mechanisms?

### Questions
- Do the authors see the same kind of benefits when the modules output vectors in some latent space, as opposed to scalars?
- Have the authors considered any task that is either not synthetic or not extremely controlled (where it is easy to introduce a modular architecture that ties closely to the ground-truth), to really evaluate the benefits of modularity in a more general manner?

### Soundness
3

### Presentation
2

### Contribution
2
