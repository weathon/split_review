# Real-time design of architectural structures with differentiable mechanics and neural networks

- Decision: Accept
- Scores: 6, 6, 6, 8

## Abstract
Designing mechanically efficient geometry for architectural structures like shells, towers, and bridges is an expensive iterative process.
Existing techniques for solving such inverse mechanical problems rely on traditional direct optimization methods, which are slow and computationally expensive, limiting iteration speed and design exploration.
Neural networks would seem to offer a solution, via data-driven amortized optimization for specific design tasks, but they often require extensive fine-tuning and cannot ensure that important design criteria, such as mechanical integrity, are met.
In this work, we combine neural networks with a differentiable mechanics simulator to develop a model that accelerates the solution of shape approximation problems for architectural structures modeled as bar systems.
As a result, our model offers explicit guarantees to satisfy mechanical constraints while generating designs that match target geometries.
We validate our model in two tasks, the design of masonry shells and cable-net towers.
Our model achieves better accuracy and generalization than fully neural alternatives, and comparable accuracy to direct optimization but in real time, enabling fast and sound design exploration.
We further demonstrate the real-world potential of our trained model by deploying it in 3D modeling software and by fabricating a physical prototype.
Our work opens up new opportunities for accelerated physical design enhanced by neural networks for the built environment.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces a physics-in-the-loop scheme for the design of architectural structures. The authors here use a neural network(MLP) to learn the mapping from the desired structural shape to intermediate mechanical properties (bar stiffnesses) and then use a physics model to generate a physically feasible shape approximating the target.  The authors then apply this method to the design of masonry shells and cable towers,  comparing it with two neural network baselines: one trained to produce physically feasible shapes and the other trained to produce feasible shapes while also ensuring mechanical stability. Results on both these case studies show the proposed approach outperforming both these baselines and being on par with numerical optimization.

### Strengths
1. The idea of combining physics with ML for architectural design is promising, as it removes the need for generating costly training labels. Instead, the model can learn by integrating the physics model with inexpensive loss functions.
2. The out-of-distribution performance is also interesting, as it potentially reduces the need for extensive variability in the training data.

### Weaknesses
1. The case studies provided are relatively simplistic and do not reflect real-world applications. The physics model used is also quite basic, limiting the method's applicability in practical scenarios. Specifically, the use of a linear Finite Difference Method (FDM) for structural analysis restricts the method to scenarios where material and geometric nonlinearities are negligible. This is a significant limitation, as many real-world architectural structures exhibit complex behaviors that cannot be accurately captured by linear models. Furthermore, the low degrees of freedom (DOFs) in the examples do not demonstrate the method's scalability to more complex structures.
2. Additionally, as the authors acknowledge, even when trained, the proposed parameterization lacks flexibility and requires retraining whenever the design representation changes. This is a major drawback, as architectural design is an iterative process where the design representation often evolves. The need to retrain the model for each new parameterization makes the method less practical for real-world design workflows. The lack of a generalizable parameterization strategy limits the method's applicability to a narrow range of design problems.

### Questions
Overall, the paper is technically sound and proposes an interesting integration of ML and physics. However, there are some concerns as follows:

1. The proposed hybrid approach requires running the physics model during inference, likely increasing training costs. While the authors report inference time, the training time is not provided. Given the limited representational capacity of the network, it must be retrained whenever the design is re-parameterized (a likely scenario during conceptualization). Reporting training times would enable a better assessment of the method’s real-world viability; if training significantly exceeds the duration of several optimizations, direct optimization might be preferable.

2. Similarly, providing training time metrics for the other baselines would help clarify trade-offs and be useful in scenarios where slight accuracy losses are acceptable for performance gains.

3. From Fig.9 , the optimization initialized with the proposed method converges quickly as compared to the other initializations. This leads to an interesting question of how the NN initialized optimizations would perform. This approach would have the benefit of outputting a guaranteed local minima while avoiding the additional physics overhead during training. Including these results would enhance the paper's contribution to the community.

4. The case studies considered here have relatively low DOFs, and the physics relies on a linear FDM. The authors could discuss the viability of this approach for structures where linear FDM is inapplicable or for dynamic scenarios. In such cases—and even when FDM is applicable but the structure has much higher DOFs—would this approach remain feasible?

5. Furthermore, the variation in MLP and PINN inference times is puzzling. Since the input sizes remain constant, one would expect the inference times for the fully trained networks to be similar. Could the authors comment on this discrepancy?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This manuscript presents an interesting application of AE-type of network architecture to facilitate design and optimization of mechanical structures, mostly in (building) architectural structures. Although the method presented is mostly ad-hoc, the manuscript is well written, the proposed method appears sound, and the potential application is clearly indicated.

### Strengths
The paper is nicely written, although there are a few small details which could make the paper more understandable for neurips attendees, who may not have prior knowledge on the mechanical structure presented.

The method presented appears sound. The architecture as shown in Fig 1, leveraging JAX, makes intuitive sense.

### Weaknesses
Concerns to the paper:

1. Although it is not clearly explained, it appears that each trained model is closely related to the underlying architectural structure (masonry shells or cable-net tower). The question is whether the trained model is generalizable. Even for the shells, if $M$ (number of bars) and $N$ (the number of nodes) change, the model may have to be retrained. It's understandable that this does not reduce the practical value of the proposed method. However, the lack of generalizability across different structural configurations is a significant limitation that should be more explicitly addressed. The current architecture, using an MLP encoder, inherently ties the model to a specific input size, making it unsuitable for varying numbers of bars or nodes without retraining. This constraint limits the practical applicability of the method in scenarios where structural parameters are not fixed.

2. The runtime measurements have such large variances that they are not meaningful. The author(s) should consider changing the evaluation platform (macOS has many background processes and is not a good platform for benchmarking), and deploy better runtime measurement libraries. The reported variances make it impossible to draw any reliable conclusions about the computational efficiency of the proposed method. The lack of controlled benchmarking makes it difficult to assess the real-world performance of the model compared to existing approaches. The authors should use a dedicated benchmarking environment and more robust timing tools to provide meaningful performance data.

3. In line 200 in Eq. (3), the fact that $\tau$ can be used to specify minimal stiffness is very interesting. But there are no more follow-up discussion on this topic. The paper would benefit from a more detailed explanation of how $\tau$ influences the optimization process and the resulting structural designs. The implications of choosing different values for $\tau$ and its impact on the final structure's mechanical properties should be explored further. The current discussion is too brief to fully appreciate the significance of this parameter.

4. Structure of the paper: the decoder is not discussed in the main body of the paper, mostly in the appendices. This need to be fixed. The absence of a detailed discussion of the decoder in the main text makes it difficult for the reader to fully understand the model's architecture and its working principles. This lack of clarity hinders the overall understanding of the proposed method and its potential limitations.

### Questions
1. Does the term *fabrication requirements* imply that each bar in the shell examples has to follow additional constraints?
2. Provide more discussion on the usage of $\tau$ as pointed out in the previous section
3. Revise the manuscript to discuss the decoder in the main body of the manuscript.

Minor issues:
1. Define (or discuss) *mechanical integrity* and *mechanical efficiency* earlier in the manuscript. What do they exactly mean?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper combines neural networks with a differentiable mechanics simulator to develop a model that accelerates the solution of shape approximation problems for architectural structures modeled as bar systems. The proposed approach achieves better accuracy and generalization than the neural network approach and gets comparable accuracy to direct optimization. The two design domains are masonry shells and cable-net towers.

### Strengths
* The presentation of the approach is nicely structured, and the figures are clean and easy to understand. 
* As an application paper, the work demonstrates a nice implementation of combining a differentiable simulator (as the decoder) with a neural network (as the encoder). The authors also build a physical prototype (Figure 6) based on the output of the approach. It is highly unusual to take this extra step to build a physical prototype and should therefore be commended.
* The results successfully highlight how using the simulator ensures that the final design results in a pin-jointed structure where the resolved forces at the internal pins are at equilibrium.

### Weaknesses
 * The motivation for this approach is not entirely clear. The design pipeline appears to start with a $\tilde{\mathbf{X}}$ and then produces a set of stiffness values. These stiffness values, along with the boundary conditions are then fed to the mechanical simulator to result in the final design (presumably, with the neural network’s stiffness values):
    * In practice, how does one come up with a design $\tilde{\mathbf{X}}$? 
    * How does the simulator only require $\mathbf{p}$ and $\mathbf{b}$ for shape prediction? It seems like the simulator is missing information to build a shell with $N$ pins. 
* The cost of amortization (i.e. the number of direct optimization runs to build the data set for training) does not seem to be mentioned as a limitation of the approach. Are there instances in the real world where amortization of the optimization routine would be needed? For example, with a training set, it seems like 100 x direct optimization is required to train the model. This overhead would need at least 100 runs of the proposed approach to make it well-motivated. In a real design pipeline, how often would it be expected to call such a function? It already runs in less than 2 seconds for cable-net towers and around 6 seconds for the masonry shell. Is this this wall-clock time a problem in practice? If so, the paper would benefit from this written explicitly. 

Minor
* $p$ for norm and $\mathbf{p}$ for loads are a bit confusing in terms of notation.
* Suggestion: use test-time inference rather than inference for predictions, since inference can also refer to inference over parameters.

### Questions
* Are the authors going to be releasing the code? As an application paper, it would be beneficial to the community if they were.
* Does the chosen bar stiffness affect the loading on the design since a stiffer bar might lead to a heavier design? 
* Could you provide further clarification on how the stress direction is determined a-priori? 
* When training the neural network component, how is this loss accounting for permutation invariance with locations, or is there some implicit consistency in the ordering of the pin coordinates.
* What mechanism is in place to prevent the model providing excessively large stiffness values for all the bars?
* Could you explain why the masonry shell is modeled as a pin-jointed structure but is then physically built as a shell (and how the two structure types are related)?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors propose an AI-driven design algorithm for architectural structure that can generate mechanically feasible designs for bar systems according to a target geometry. Previous approaches such as pure neural networks cannot guarantee mechanical design requirements. Traditional direct optimization methods can satisfy mechanical criteria, however are inefficient. The authors propose a hybrid scheme, combining neural networks and mechanical simulators to achieve computational efficiency and satisfaction of mechanical constraints. The authors approach consists of a encoder-decoder neural network, where the decoder is replaced by a differentiable mechanical simulator. The encoder structure provides efficiency, while the decoder ensures the design satisfies mechanical constraints. Experimental results show that the authors method achieves satisfactory performance in terms of design and computational efficiency.

### Strengths
The paper presentation is very good, the motivation is clear, and the method is justified well. Experimental results are extensive. The authors also provide a real life sample designed from their algorithm, which the readers will find very interesting.

### Weaknesses
The authors could do some revision of the figure. In figure 1, it seems that 3 figures are simultaneously provided to the encoder network, although the text description indicates only one shape is provided. Please take care to avoid such confusion from readers. Also describe the dimension of the matrix K. In figure 3, it is hard to see how the x vectors are being updated. Zooming in and adding some texts will be better for understanding.

### Questions
See weakness section

### Soundness
3

### Presentation
3

### Contribution
3
