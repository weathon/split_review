# Expressivity of Neural Networks with Random Weights and Learned Biases

- Decision: Accept
- Scores: 6, 8, 6, 6

## Abstract
Landmark universal function approximation results for neural networks with trained weights and biases provided impetus for the ubiquitous use of neural networks as learning models in Artificial Intelligence (AI) and neuroscience.
  Recent work has pushed the bounds of universal approximation by showing that arbitrary functions can similarly be learned by tuning smaller subsets of parameters, for example the output weights, within randomly initialized networks. 
  Motivated by the fact that biases can be interpreted as biologically plausible mechanisms for adjusting unit outputs in neural networks, such as tonic inputs or activation thresholds, we investigate the expressivity of neural networks with random weights where only biases are optimized.
  We provide theoretical and numerical evidence demonstrating that feedforward neural networks with fixed random weights can be trained to perform multiple tasks by learning biases only. We further show that an equivalent result holds for recurrent neural networks predicting dynamical system trajectories. Our results are relevant to neuroscience, where they demonstrate the potential for behaviourally relevant changes in dynamics without modifying synaptic weights, as well as for AI, where they shed light on multi-task methods such as bias fine-tuning and unit masking.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
Previous work has investigated the expressivity of feed-forward neural networks (FNNs) when only subsets of parameters are trained (ie. only the output layer, normalization parameters, etc…). In the same vein, the authors introduce a method of training feed-forward neural networks by randomly sampling fixed weights and subsequently learning only the biases, termed bias learning. They provide theoretical and empirical evidence that demonstrates that FNNs trained through bias learning can approximate any continuous function on compact sets - meaning that they are theoretically as expressive as fully-trained FNNs.

They start with a theoretical treatment of bias learning where they carefully define their terms and introduce their theorems. A simplified version of the rigorous proof is as follows: 1) Train a fully connected network (N1) where the weights are constrained to lie in some fixed range. 2) Create a new network (N2) by randomly sampling the hidden neuron weights from the fixed range in 1. 3) After sufficient sampling, there exists a subnetwork of neurons in N2 that is ‘identical’ to the neurons in N1. 4) By training the biases, the outputs of neurons outside of this subnetwork can be removed, leaving N1 from N2 bias training. They provide a similar proof for recurrent neural networks (RNNs).
Next, the authors provide empirical evidence supporting their theory and explore the expressivity of bias-learned networks. They do this in multiple ways, including performing multi-task learning with bias learning in 7 tasks (MNIST, KMNIST, Fashion MNIST, etc.), comparing bias learning and mask learning in FNNs, and applying bias learning on an RNN trained on both an autonomous and non-autonomous dynamical system. The main takeaways are as follows: 1) multi-task bias learning leads to emergence of task-specific functional organization revealed by clusters of activation patterns measured by task variance, 2) compared to mask learning, bias learning had less sparse solutions and higher unit variance values, 3) bias learning in RNNs can succeed in time-series forecasting of non-linear dynamical systems with high enough gains.

### Strengths
- Overall, there is strength in its novelty of proving that bias learning in neural networks can have high expressivity that performs almost as well as a fully-trained network. This is significant because bias learning trains fewer parameters than a full network.
- Nature of bias learning is more behaviorally relevant in the context of tonic inputs, intrinsic cell parameters, threshold adaptation, and intrinsic excitability
- The theoretical proofs are very thorough, and backed up by numerical proofs.

### Weaknesses
 - In response to bias learning having fewer parameters to learn, no data was shown on training time
- Little background was given on mask learning (the mask learning section was also super short - felt less developed relative to other parts of the paper). This is important because two of their highlights in the results relate to mask learning.
- Makes claims (i.e. lines 253 - 259, lines 418-420) that could have been easily backed up by data, but were not.
- Figure 1 color scheme is weird
- Practically, not sure how exciting this is (i.e. other models can do what this model does - it's just that they use a different approach)
- The work seems highly related, in spirit, to neural tangent kernel approaches and other methods that consider wide NNs, but no references to that work were made.

### Questions
N/A

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors show that both feedforward and recurrent neural networks can act as universal function approximators for functions and dynamical systems respectively, even when only biases are learned. They propose an alternative proof for the theorem that masking is all you need (Strong Lottery Ticket Hypothesis), and extend that and the bias result to RNNs approximating dynamical systems. They authors demonstrate their results using simple simulations, and discuss relevance to AI and neuroscience.

### Strengths
The authors connect well to the neuroscience and AI/ML literature and explain the proofs in an intuitive manner. 
The extension to RNNs and dynamical systems is also commendable as these often receive reduced attention in the ML community.
The issue with the "gain" g in the weight distribution is well brought out.

### Weaknesses
The section 3.3.2 on the Lorenz system is not clearly written and the architecture and external input to the network are not clear. 

At first glance, the result seems to be a simple extension of the masking theorem of Malach et al 2020.  The difference with that proof should be made clear.

In Section 3.3.2 - The authors write RNN, but then say that the recurrent state is given? Also what is provided as an external input? Is it the recurrent state? The difference between the 'standard' and the 'self-sustained' networks is not clear. To me the self-sustained way is the standard, and if somehow the recurrent state is provided (at each time step?), then the network is just acting as a feedforward network. Then in this case, I suspect that to actually use the RNN (usual self-sustained way) to learn the dynamics, the authors would need a lot more units.

The authors have not explained how (positive & negative) biases may arise in neuroscience if not by synaptic weights. As they mention threhsold changes etc. change the neural gain (and possible have a strongly non-linear effect). What about the role of inhibition and other brain areas switching parts of the network on and off?

### Questions
In Section 3.3.2 - The authors write RNN, but then say that the recurrent state is given? Also what is provided as an external input? Is it the recurrent state? The difference between the 'standard' and the 'self-sustained' networks is not clear. To me the self-sustained way is the standard, and if somehow the recurrent state is provided (at each time step?), then the network is just acting as a feedforward network. Then in this case, I suspect that to actually use the RNN (usual self-sustained way) to learn the dynamics, the authors would need a lot more units.

The authors have not explained how (positive & negative) biases may arise in neuroscience if not by synaptic weights. As they mention threhsold changes etc. change the neural gain (and possible have a strongly non-linear effect). What about the role of inhibition and other brain areas switching parts of the network on and off?

The authors should bring out the differences between their proof and the Malach et al proof.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In this work, the authors prove a universal approximation result for the expressivity of neural networks with frozen weights but trainable biases. In particular, they build upon well-known universal approximation results of feedforward and recurrent architectures, and show via a simple mask learning-like argument that sufficiently large networks with randomly chosen weights can be constructed to approximate any function (feedforward) or finite-time trajectory (recurrent). They conduct experiments comparing fully trainable architectures to bias-learning variants, demonstrating that bias-only learning can achieve reasonable performance on some simple tasks.

### Strengths
The main expressivity results shown are well-explained and seem mathematically tight. Considering that these results made use of a reduction to mask learning problems, the authors also do a good job discussing the relationship between their findings and those of the mask learning literature.

### Weaknesses
A crucial aspect of this work with regards to its practical relevance is how large a bias-trained network needs to be to achieve similar performance to a fully trained network. Surely the scaling is better than the extreme network expansions constructed for the existence proofs, but how much better? The authors allude to performance as a function of trainable parameter count scaling similarly to fully trained networks, and thus only needing quadratic scaling in layer width, but they only evidence this explicitly with comparisons to mask learning networks, which in my view are also less expressive than standard networks (for fixed number of parameters). I would like to see a more detailed investigation of this question. For example, could the authors extrapolate from the MNIST experiments (Fig. 1a) whether the required scaling is indeed quadratic? I imagine this scaling would also depend significantly on the task difficulty and the frozen weight initialization. 

Overall, the tasks the authors used to demonstrate efficacy of bias-only learning seemed restrictively simple, by the standards of both the machine learning and computational neuroscience literature. In particular, for the RNN experiments, only simple 1D pattern generation tasks were considered. I would be interested in seeing how biased-trained RNNs perform on simple "cognitive" tasks often used to assess task-trained RNNs in the computational neuroscience literature (e.g., interval timing, delayed match-to-sample). For example, I imagine that any task that requires the construction of many stable fixed points could be quite difficult for bias-learning RNNs, and might require prohibitive scaling of network size compared to fully-trained counterparts (e.g., N-bit flip flop).

### Questions
See above.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
Note: I’m not an expert in the field of pruning and universality.
The authors show that random neural networks with trained biases are universal approximators. This is shown both for feedforward and recurrent networks. The authors use an argument that is similar to masking, and use negative biases to implement the masking. Numerical simulations show that several benchmarks reach similar performance when training biases or training weights as well.

### Strengths
The questions of pruning, masking and universality are all important questions for neuroscience and machine learning. In neuroscience, it is known that many cell-autonomous adaptation mechanisms exist (e.g., spike threshold adaptation), and the wide distributions of firing rates hint that these properties could be a form of long-term plasticity as well.
Proving universality results has opened the door for more application-oriented research in the past. The combination of mathematical proofs with systematic simulations and a wide literature review is a strength.

### Weaknesses
My main concern is the scaling of network size, which seems exponential and is also missing from the main text. The results of Malach et al 2020 suggest that masking is weaker than weight-pruning, unless the size of the network is exponential. If I understand correctly, I expect a scaling of (R/eps)^n. Because there are n independent event with probability (R/eps). Line 944 (appendix) states a scaling, which by approximating log(1+z)=z is indeed (1/eps)^(n^2). Given this large scaling, and the results of Malach et al that with polynomial scaling neuron-pruning is weak, it seems strange that bias learning is as strong as weight learning. Indeed – the actual numerical results do not show comparable performance. As the tasks become harder, the gap widens. Also when controlling for the number of learned parameters, bias learning is still weaker.



### Questions
1.	Definition 2: bounded by gamma?
2.	Line 186 large hidden layer width. Can you provide a rough estimate? What is the scaling? I assume it is roughly (R/eps)^n. In Malach et al, the size was polynomial. If I understand correctly, line 944 gives such scaling, and by approximating log(1+z)=z it is indeed (1/eps)^(n^2).
3.	Fig E2. It is hard to compare what happens from 5000 parameters or so. Perhaps a logarithmic or ratio plot would help.
4.	Fig E2 – fully trained was still better than bias-only, even when controlling for parameter number. Do you know why this is? Is this related to the main concern raised above?
5.	Line 304. Correlation between TV and bias. Was this computed for every unit, and then averaged within each cluster?
6.	Line 304 If the theory is aligned with training, then the number of units should be much higher than simply the square of fully trained network. If Figure E2 suggests otherwise, then why expect the mechanism of the proof to hold? Further – what are the values of biases? Are some of them extremely low – effectively shutting down neurons?
7.	Correlation values between mask and bias – what is the correlation between different realizations of the training process?
8.	Line 461 – similar scaling in RNN and FNN. Figure E2C shows that the fully trained saturates at 64^2 parameters. The bias trained network is shown up to 64^2 parameters, so we can’t see whether fully-trained RNNs with less than 64^2 parameters behaves similarly to FNN.
9.	Line 462 stability in larger windows. Perhaps I didn’t understand this, but is this really stability or simply more test sets? Because the network is fed the true dynamics, is there a meaning to larger windows?
10.	Figure 4C – How does the fully trained network generalize in this scenario?
11.	Line 481 – I think some discussion of scaling should go into the main text, even if the proof is in the appendix.
12.	Line 483 – task-selective clusters similar to fully trained. This was not shown. Specifically, quantification of how task-selective are bias-trained vs. fully-trained networks.

### Soundness
3

### Presentation
4

### Contribution
3
