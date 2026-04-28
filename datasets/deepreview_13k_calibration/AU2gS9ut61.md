# A differentiable brain simulator bridging brain simulation and brain-inspired computing

- Decision: Accept
- Avg Score: 5.40
- Scores: 6, 6, 8, 1, 6

## Abstract
Brain simulation builds dynamical models to mimic the structure and functions of the brain, while brain-inspired computing (BIC) develops intelligent systems by learning from the structure and functions of the brain. The two fields are intertwined and should share a common programming framework to facilitate each other's development. However, none of the existing software in the fields can achieve this goal, because traditional brain simulators lack differentiability for training, while existing deep learning (DL) frameworks fail to capture the biophysical realism and complexity of brain dynamics. In this paper, we introduce BrainPy, a differentiable brain simulator developed using JAX and XLA, with the aim of bridging the gap between brain simulation and BIC. BrainPy expands upon the functionalities of JAX, a powerful AI framework, by introducing complete capabilities for flexible, efficient, and scalable brain simulation. It offers a range of sparse and event-driven operators for efficient and scalable brain simulation, an abstraction for managing the intricacies of synaptic computations, a modular and flexible interface for constructing multi-scale brain models, and an object-oriented just-in-time compilation approach to handle the memory-intensive nature of brain dynamics. We showcase the efficiency and scalability of BrainPy on benchmark tasks, and highlight its differentiable simulation for biologically plausible spiking models.%, and discuss its potential to support research at the intersection of brain simulation and BIC.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors introduced a package called BrainPy. It inherits the JAX and provides support for brain simulation and SNN training. Overall, the package is interesting and useful in the stated scenarios.

### Strengths
1. It demonstrates the improvement in efficiency. 
2. It provides the support for both neuroscience and DL research.

### Weaknesses
1. The package itself is more like a collection of course scripts rather than a Python package. Thus I suggest that the authors improve the engineering quality and documents for the current package.

2. The comparison to existing methods is not sufficient. For example, there are existing tools like SpikingJelly for SNN. The simulation of neurons is also not sufficiently new. Thus the unique character of the current package could also be strengthened. 

3. I am not quite sure about the standard of package paper for ICLR. From my own understanding, the contribution and optimization to system design can be clarified in a more clear way as well.

### Questions
Please see the weakness.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces a brain simulator named BrainPy, which is designed to bridge the gap between brain simulation and brain-inspired computing (BIC). This paper describes the infrastructure implementation that facilitates flexible, efficient, scalable, and biological detailed brain simulations. It also describes an example project that employs this BrainPy to construct a biologically plausible spiking model to demonstrate the differentiable simulation capability of this tool.

### Strengths
- Clear presentation. Comprehensive comparisons with existing tools.
- Leverages modernized tooling such as Jax and XLA, provides a user-friendly interface, and is compatible with various computing hardware.
- Technical complexity and thoughtful designs that optimize speed and memory usage.

### Weaknesses
 - Despite the exciting endeavor towards bridging the gap between brain simulators and BIC libraries, this paper appears to have limited relevance to this conference due to the lack of original theories or empirical evidence.
- Quantitative comparisons with BIC libraries seem to be missing.
- While the paper takes the stance of bridging brain simulators and DL frameworks, discussions about deep learning models seem to be missing.

### Questions
- What might be the biological evidence that supports the design of parameter sharing within the "AlignPre" and "AlignPost" projections?
- How does BrainPy's speed and scalability compare to CARLsim, another brain simulator known for efficient and large-scale brain simulations?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors develop a new framework, brainpy, which allows to run (biophysically realistic) networks of neurons in a differentiable manner, thereby allowing integrations with deep learning (DL) frameworks. In addition, since it is implemented in JAX, it supports JIT compilation.

### Strengths
I think this is an important and potentially impactful work. The paper is well written, the figures are clear, and the authors carry out many empirical experiments to demonstrate the abilities of brainpy.

### Weaknesses
The paper has the following major weaknesses:

1) It does not evaluate the cost of compilation. How high is the cost of compilation compared to the runtime? Is this a clear disadvantage as compared to, e.g., NEURON? Does the compilation speed depend on whether CPU or GPU are used? How does it scale with the number of neurons?

2) In section 4.2, the authors claim that there method is significantly more memory-efficient than others. Maybe I am misunderstanding this, but: do the gains that the authors claim here stem from an assumption that the connectivity matrix is low-rank? How else would they possibly be able to store connections of 86 Billion neurons?

Minor: 

1) I believe that it would be good if the authors clarified that all JIT capabilities are due to the fact that brainpy relies on JAX, and are not implemented from scratch. Section 4.5 reads as if the authors implemented this themselves.

2) The statement `It is important to note that this hierarchical composition property is not shared by other brain simulators.` is not true, see for example NetPyNE.

### Questions
No questions.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
1

### Rating Number
1

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors present a programming framework that enables fast and differentiable implementation of simulations of brain circuits and similar computing systems.  The framework achieves major speed and memory benefits by taking advantage of the sparsity of these circuits in space, and in time for the case of spiking neurons.

### Strengths
This is a very valuable contribution to the world of brain simulation, which seems likely to find a lot of users due to its speed and differentiability.

### Weaknesses
No major weaknesses identified.  

I am new to ICLR reviewing so I don’t know how well this work fits within the remit of the conference.  However it is certainly a very valuable contribution to computational neuroscience.

Presumably the JIT weight generation only works for random weights, not those learned by synaptic plasticity rules?

More detail on differentiability in spiking networks would be useful.  Equation (28) isn’t clear: neither x nor spike’ are defined, and is width the same as V_th?   As well as this, a more basic question:  do the computational benefits of sparse activity carry through to the derivatives?  For example, even if two neurons are connected with zero weight, the derivative of the objective function with respect to this weight need not be zero.

### Questions
Presumably the JIT weight generation only works for random weights, not those learned by synaptic plasticity rules?

More detail on differentiability in spiking networks would be useful.  Equation (28) isn’t clear: neither x nor spike’ are defined, and is width the same as V_th?   As well as this, a more basic question:  do the computational benefits of sparse activity carry through to the derivatives?  For example, even if two neurons are connected with zero weight, the derivative of the objective function with respect to this weight need not be zero.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper describes a package for building brain-inspired trainable network models. It is build around JAX and provides efficient just-in-time compiled code for CPUs, GPUs and TPUs. Compared to classic simulators for biological neural networks, models implemented in BrainPy benefit from auto-differentiation, and compared to standard machine learning frameworks, BrainPy provides an environment focused on building bio-inspired models with e.g. spiking interactions and detailed synaptic/neuronal dynamics.

### Strengths
- The manuscript describes a substantive library which is in an advanced stage of development.
 - It is correct that there is a need for an extensive and modern framework for training larger biological network models. The described package is therefore a significant; demonstrating its capabilities + speed comparisons to other libraries is a useful contribution.

### Weaknesses
 - Except for Fig.5 A/B dealing with matrix multiplication, the figures vary the network/system size on a linear scale, and not over several orders of magnitude. This does not seem suitable to demonstrate the scaling behavior for these network models.
- There does not seem to be a demonstration of distributed simulation/training of a large-scale model on a CPU or GPU cluster.
- In section 4 the package is at length described as efficient, extensive, scalable, etc. without really getting into the concrete design and implementation. In particular, after reading this section I did not end up with a clear picture of the package structure and components. Maybe the description could be shortened, or made more concrete.

### Questions
Due to limited time I'd like to state clearly that I did not do an in-depth review of all parts of the manuscript.

Probing a subset of the results, I did not find a concrete description of the simulations underlying Fig.4C in the supplementary material. Especially, I wondered why the NEST version used by the authors is 2.20 instead of the more recent 3.x versions, and I could not find the corresponding code implementing the NEST simulation, or generally creating Fig4C, in the files supplied. 

On p.8 it is mentioned concerning Fig 5C that the E/I network was scaled up to 4 million neurons with 80 synapses each. In biological networks, the (local) connectivity is typically significantly more dense, with hundreds or thousands of synapses per neuron.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good
