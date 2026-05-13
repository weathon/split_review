# Learning Sequence Attractors in Recurrent Networks with Hidden Neurons

- Decision: Reject
- Scores: 3, 8, 5, 5

## Abstract
The brain is targeted for processing temporal sequence information. It remains largely unclear how the brain learns to store and retrieve sequence memories. Here, we study how recurrent networks of binary neurons learn sequence attractors to store predefined pattern sequences and retrieve them robustly. We show that to store arbitrary pattern sequences, it is necessary for the network to include hidden neurons even though their role in displaying sequence memories is indirect. We develop a local learning algorithm to learn sequence attractors in the networks with hidden neurons. The algorithm is proven to converge and lead to sequence attractors. We demonstrate that the network model can store and retrieve sequences robustly on synthetic and real-world datasets.  We hope that this study provides new insights in understanding sequence memory and temporal information processing in the brain.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a new binary RNN in which there is a hidden layer in between RNN transitions. They develop a learning rule for training the two weight matrices in the transition. They then train these RNNs on some simple sequences and show they can be learned.

### Strengths
The paper is clearly presented, and the work is original to my knowledge. My main concern is its significance (see below).

### Weaknesses
You can always add more neurons to solve these problems with a standard RNN. See Siegelmann and Sontag (1992). You’d need to actually show that the other RNNs can’t actually learn these sequences, but it’s clear that they could…(maybe not a size matched RNN, but a larger one could…)

You’re training a new network for each sequence? This is pretty extreme, and there are lots of much simpler ways of solving that problem (e.g. a HMM). 

In sum, it’s not really clear that the proposed method actually solves a real problem. You’d need to show it by comparing performance to other RNN architecture (as well as non sized matched networks). You’d also need to test against networks that don’t just have binary outputs. I understand that you would like to relate it to the brain, however the brain communicates in spike rates, not just a single spike…

### Questions
See weaknesses

### Soundness
2 fair

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors extend Hopfield networks by adding one hidden layer and together with their proposed learning rules, show that this architecture can store and retrieve binary sequences. They provide convergence guarantees and empirically demonstrate, on various toy and real world examples, that their network learns to store sequences and retrieve them even in the presence of (a particular type of) noise.

### Strengths
The paper provides a relatively simple extension to Hopfield networks and corresponding learning rules to store and retrieve sequences that works well, which is novel to my knowledge. The problem of being able to store and retrieve sequences is an important one, both for understanding biological brains and for machine learning. Therefore having such a method is very useful and significant for the community.

The paper provides convergence proofs and empirical evaluation on a variety of targeted and relevant tasks, which also makes the paper a high quality contribution to the community. I particularly found the specific examples provided to demonstrate the problems with storing sequences in a fully visible recurrent network very useful to understand the motivation behind their approach.

### Weaknesses
A discussion of the capacity of the proposed architecture is missing, and is pretty important to be able to meaningfully connect this approach with biology and apply it in machine learning. This, in my opinion, is the biggest weakness of the paper. Specifically, while the authors demonstrate the ability to store and retrieve sequences, they do not provide a theoretical or empirical analysis of how the network's capacity scales with the number of hidden units or the length of the sequences. This makes it difficult to assess the practical limitations of the approach. For example, it is unclear how many sequences of a given length can be reliably stored and retrieved, and whether there are trade-offs between sequence length and the number of stored sequences. 

The experiments section also does not have sufficient details about hyper-parameters ($ \eta, \tau$). The lack of specific values for these parameters makes it difficult to reproduce the results and to understand the sensitivity of the model to these parameters. The language and clarity of the exposition in the paper could be improved significantly.  See examples in "Questions".

### Questions
## Questions related to points mentioned above:
- How many times is each sequence presented to the model?
- What's the capacity of the model? How many sequences can it store?

## Clarity issues in the paper:
- The sign function and the Heaviside function seem to be identical the way it's been defined in the paper.
- The first sentence of Related work just lists a bunch of papers, which seems redundant, since these papers are explained later anyway.

### Minor:
Would have been useful to have Fig. 2 and Fig. 5 side by side for comparison. Merge the two figures perhaps?
Bar plots in Fig. 7 and 8 are hard to read. Having concrete values for each bar, and mentioning the specific values of $M$ and $T$ used would be very useful.

### Grammar/Language:

**Abstract**
- "The brain is targeted..." is not well formed.
- "We demonstrate our model..." -> "We demonstrate that our model..."

**Sec 1:**
- "as we experience the 'mental time travel'" -> "as we experience 'mental time travel'"
- "By a sequence attractor, it means"
- "The algorithm is proved to converge" -> "The algorithm is proven to converge"
- ...

There are many more. I would suggest passing the text through a grammar check.

### Soundness
3 good

### Presentation
2 fair

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Attractor networks can be considered all-to-all connected feedforward networks without any hidden layer. These ‘visible neurons’ must do both the computational and representational work simultaneously. This limits the expressibility of such networks, particularly for sequence attractors. This submission shows one way around this limitation is to add hidden neurons with a dedicated computational role and no (direct) representational role. A learning rule is introduced to learn the necessary parameters for these hidden neurons in the case of artificial and naturalistic data, with good recall shown.

### Strengths
Integrates some nice ideas to solve an identified problem.

### Weaknesses
*Novelty*

I question how or in what way this is new or different to past work (see question 2 below), and for that reason am concerned about novelty. However, my concern might be misplaced and I would appreciate the authors clarifying this point.

*Imprecise or incorrect statement*

From page 1: “the Hopfield model and related works typically only consider static attractors”

No, there exist many works looking at non-static attractors. Some of these are cited at the end of the first sentence in section 2 on page 2. A few additional examples include:

H. Gutfreund and M. Mezard. Processing of temporal sequences in neural networks. Phys. Rev. Lett., 61:235–238 1998.

Arjun Karuvally, Terrence Sejnowski, and Hava T Siegelmann. General sequential episodic memory model, ICML 2023.

Hamza Chaudhry, Jacob Zavatone-Veth, Dmitry Krotov, Cengiz Pehlevan, Long Sequence Hopfield Memory, NeurIPS 2023.

This statement is misleading as it implies a scarcity of work on sequence attractors, when in fact, there is a substantial body of literature addressing this topic. The cited examples, along with the provided ones, demonstrate that sequence learning in attractor networks is a well-explored area. The authors need to more accurately position their work within this existing landscape.

*Lack of comparisons and practical applications*

Previous work on encoding sequences in attractor networks have taken many different approaches. Additionally, there exist many methods for learning sequences in the machine learning literature. There is a lack of comparison with these prior methods. The absence of a thorough comparison makes it difficult to assess the advantages and disadvantages of the proposed approach relative to existing techniques. Specifically, the authors should compare their method against other sequence learning algorithms in terms of memory capacity, learning speed, and robustness to noise. Furthermore, the lack of practical applications limits the impact of the work. It is unclear how this approach could be used in real-world scenarios, which reduces its overall significance.

### Questions
1. Where is the evidence that the examples shown in Figure 2 cannot be generated by a network without hidden neurons?

2. How is your approach conceptually different to hierarchical attractor network architectures? E.g.,

Dmitry Krotov, Hierarchical Associative Memory, arXiv:2107.06446

Kunihiko Fukushima, A hierarchical neural network model for associative memory, Biological Cybernetics volume 50, pages105–113 (1984)

3. What is the memory capacity of this network? How does this depend on memory load?

4. In the second paragraph of the conclusion, there is some speculation that neurons in V1 with unknown function may be akin to the hidden neurons of this model. How would a neuroscientist test for this? How should the tuning properties be studied, i.e., what should be measured? Does there exist some structure(s) in the hidden neuron activity data from your own model which you would expect in the aforementioned V1 neurons?

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
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper introduces an algorithm to let a recurrent neural network learn sequences of patterns with convergence guarantees for the algorithm.
Furthermore, the importance of hidden neurons in the proposed architecture and activation function is shown for producing some of the sequences.

### Strengths
The effectiveness of the approach is demonstrated against two datasets, highlighting its applicability. The theorems and claims are sound.
Furthermore, the paper is well written and the contributions are clearly explained with possible implications of the work for neuroscience. These implications for neuroscience might provide a new perspective on the contribution of some neurons to neural computation.

### Weaknesses
### weaknesses:

\paragraph{Comparison of encoding efficiency to other methods/experiments}
The authors don't make considerable efforts to compare their work to previous ones relating to sequence encoding. There are many works on sequence learning, see for example [1]. Your work is a particular subclass of networks that can perform sequence-to-sequence processing (namely where you have a sequence with an single input and the start and zero inputs afterwards). Make comparison with other methods to measure the performance of your framework in terms of robustness to noise, memory capacity (number of recallable pattern sequences), etc. Specifically, a detailed comparison with other sequence learning models, including those capable of handling continuous inputs and those with different architectures, would provide a clearer understanding of the proposed method's advantages and limitations. It would be beneficial to see how the proposed method compares in terms of the number of learnable parameters, the length of sequences it can effectively learn, and its ability to generalize to unseen sequences.

\paragraph{Other experiments to demonstrate the effectiveness of the method}
The the demonstration contribution of this framework could benefit from some additional experiments. Experiments for effect of noise level of the first patter on the performance. Further, the paper doesn't address how inputs to the network influence the output or performance. Experiments that track performance of the networks as a function of injected noise during sequence generation would better demonstrate the usefulness of this framework for neuroscience. Specifically, it would be valuable to investigate how varying the magnitude and type of noise affects the network's ability to recall the correct sequence. Additionally, exploring the impact of different input patterns, such as varying the sparsity or the correlation between patterns, on the network's performance would provide further insights into the method's robustness and generalizability.

\paragraph{Figures}
Overall, the information in the figures is very low. For Figure 4 and 11 for example it is unclear what is to be gained from seeing the convergence of the algorithm, if it is not compared to other algorithms to see which converges in less epochs for example. A more informative approach would be to compare the convergence speed and stability of the proposed algorithm against other sequence learning algorithms under similar conditions. This would provide a quantitative measure of the algorithm's efficiency. For Figure 7 and 8 it would be beneficial to see how increasing $T$ influences retrieval success as $M$ and $N$ are changed. Specifically, plotting retrieval success as a function of $T$ for different values of $M$ and $N$ would reveal the relationship between these parameters and the network's capacity.

\paragraph{Some remarks on concepts and notation}
The section on the robustness hyperparameter is unclear. Better describe how the margin of the margin perceptron is related to the robustness here. Specifically, a more detailed explanation of how the margin parameter influences the network's ability to tolerate noise and variations in the input patterns would be helpful. Relating to the derivations: Why does such a $U^\star$ exist? After Equation (19): "due to (1)". Should this be "due to (17)"? There are a couple of unintroduced variables/notation. In Eq. (33) $q$ is appearing without introduction. Should this be $p$? Clarify step (32) to (33) in the derivation. In Eq. (39) $\Omega$ has not been introduced. Did you mean $O$?

\paragraph{Neuroscience implications}
The justification of the relevance of this work to V1 neurons is insufficient. The authors should justify why this particular activation function is a good model for V1 neural activity. Furthermore, the claim about unexplained V1 neural activity relies on the limit of the Heaviside activation function, for other activation functions hidden neurons would not be necessary. But more fundamentally, the authors seem to understand V1 neural activity dynamics in a very different way than the general con census. Although there is sufficient recurrence in V1, the main function of these neurons is not sequence generation. Hippocampal circuits (that are mentioned in the beginning of the paper) would be a better justification. Finally, for V1 neurons in particular, but for all subnetworks in the brain really, inputs are a very important contribution to the dynamics.

### Questions
What is the expressivity of the Heaviside function for a fixed $M$ and $N$ in terms of $T$?

On page 8, just above Figure 4, when is $M$ large enough? When is the solution the pseudo-inverse and when the transpose of $\mathbf{P}$? How can high-dimensional probability theory explain this?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
