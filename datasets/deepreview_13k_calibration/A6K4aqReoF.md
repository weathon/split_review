# Stateful Dynamics for Training of Binary Activation Recurrent Networks

- Decision: Reject
- Avg Score: 3.75
- Scores: 1, 3, 8, 3

## Abstract
The excessive energy and memory consumption of neural networks has inspired a recent interest in quantized neural networks. 
Due to the discontinuity, training binary neural networks (BNNs) requires modifications or alternatives to standard backpropagation, typically in the form of surrogate gradient descent. Multiple surrogate methods exist for feedforward BNNs; however, their success has been limited when applied to recurrent BNNs, but successful when used in binary-like spiking neural networks (SNNs), which contain intrinsic temporal dynamics. We show that standard binary activation approaches fail to train when applied to layer with explicit recurrent weights, and present a theoretical argument for the necessity of temporal continuity in network behavior. By systematically incorporating mechanisms from SNN models, we find that integrative state enables recurrent binary activation networks to reach similar performance as floating-point approaches, while explicit reset and leakage terms do not affect performance. These results show how spiking units enable the training of binary recurrent neural networks and identify the minimally complex units required to make recurrent binary activations trainable with current surrogate methods.

## Human Reviews

## Human Reviewer 1

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
This manuscript discusses experiments with various quantization strategies to binarize activations of neural models, particularly recurrent. The authors have included in the list of strategies SNN training by seeing the LIF neuron model as yet another binary yet stateful activation function, and conclude that it is a very effective approach for quantization of recurrent networks but they assess that decay, and reset/refractoriness do not really play any influential role.

### Strengths
I could not identify any, i am sorry.

### Weaknesses
I find that this manuscript lacks basic understanding of SNNs, does not have a clear scope, and the experimentation lacks depth and structure. Instead, in many parts the authors just re-discover basic concepts or properties about SNNs and recurrent networks.

First and foremost the authors claim that "Binary activation NNs have only been reported for feedforward topologies" (!), when practically every SNN network is a binary activation recurrent network.

The authors also claim as a contribution that state allows to train binary activation recurrent networks, but well isn't that obvious, the state is responsible for the recurrent behavior to begin with ?

What the authors claim to be temporal instability treatise for recurrent layers (in section 4.1), is really just a discussion about the smoothness of the gradient, or am i missing something?

What the authors call different training methods are really one method, only THE backprop (BP) method, and instead they look at different strategies for quantizing (binarizing) activations using BP in-training. In these strategies they test various combinations of statefulness/statelessness, approximations of firing functions (heavyside, noisy heavyside, and hard sigmoid converted to heavyside progressively), and surrogates of the gradients of the binary firing function (actually just one the STE with different gains). However, the combinations are not exhaustively examined but rather haphazardly chosen.

Although the authors claim contributions relevant to recurrent networks, the experiments carried out are not with temporal tasks but rather all spatial. They are also executed in a way (the inputs are not provided sequentially but in a single timestep) that the authors only observe the step response of the models (as dynamical systems) and not the temporal integration of the data dynamics, which makes no sense to me.

Moreover the results they present in two tables hardly support their claimed contributions, in different datasets different strategies give the best results, and it is by no means decisive that statefulness attains the best result (but then again also the tests are not temporal either).

Finally, exactly because the choice and design of experiments (with non temporally integrated stimulus) I would not expect to see any effect from decay or refractoriness, so I wonder what makes the authors conclude that these play not role whatsoever in general ?

Additionally

In l-099 the authors try to justify they choice for centering the activation functions, without explaining why is that relevant.

In l-100 the authors talk about literature standards without explaining what standards they refer to.

In Table 2 the difference between CNN-RNN and CRNN has not been explained

The SOT benchmark is not explained clearly

### Questions
See the Weaknesses section.

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
The paper investigates the impact of recurrence as an inductive bias in binarized neural networks, revealing that recurrence leads to temporal instability when using modern surrogate gradient methods, in contrast to spiking neural networks. Furthermore, it demonstrates that integrating local dynamic states, similar to those in spiking neural networks, enhances temporal stability in recurrent binarized neural networks.

### Strengths
1. **Innovative Application of Spiking Neural Network (SNN) Concepts**
   - Introducing elements from SNNs, like pre-activation state, leakage, and reset mechanisms, is an innovative approach to handling binary activations in RNNs. 

2. **Exploration of Multiple Training Methods**
   - The paper systematically compares several training strategies (surrogate gradient descent, probabilistic surrogates, and progressive sharpening), showing a thoughtful approach to exploring solutions for BARNNs.

3. **Comprehensive Experimental Setup**
   - The use of three distinct tasks—image classification, keyword spotting, and small object tracking—demonstrates the versatility of the proposed methods across different types of temporal and spatial data. 

4. **Potential for Hardware Implementations**
   -  This is valuable in the context of real-world deployment, where binary networks and reduced precision can offer efficiency gains, particularly for embedded or neuromorphic systems.


With these strengths, the paper lays a foundation for further exploration and potential practical applications in energy-efficient temporal modeling.

### Weaknesses
 - **Equation Nomenclature and Legibility**: 
   - Equations in the paper are difficult to follow due to inconsistent or unclear notation. Key variables are not defined consistently, and some choices create ambiguity. For instance, in Equation 8, it’s unclear if the layer is intended to be interpreted as a stacked ConvRNN. Additionally, the same variable, ‘y’, is used across both the spiking neural network (SNN) and binarized ConvRNN contexts, which conflates distinct mechanisms and makes tracking the model dynamics challenging.

- **Unprincipled Approach in Section 4.1**: 
   - The demonstration of binarized recurrent network instability in Section 4.1 lacks theoretical grounding. Beyond the empirical results, the chosen edge case of a constant input does not convincingly justify the instability of these networks. Additionally, Figure 4.1 requires more explanation: it seems to show that the binary activation seems to reconstruct the input, unlike the SNN, could you provide further clarity on this. I am willing to adjust my score if further clarity on this figure is provided.

- **Lack of Focus**: 
   - The contributions are listed but lack clarity, and the paper attempts to address multiple aspects of binary recurrent network training without a clear focus. For example, the incorporation of pre-activation states, leak, and reset mechanisms are all discussed but without a strong, unified narrative explaining why each is necessary. This could be solved by strengthen the message and the structure of the paper. The paper could greatly benefit from clarity.

### Questions
See weaknesses which highlight some key questions. In particular, I'd like clarity on Figure 4.1, and Equation 8 in the manuscript.

### Soundness
2

### Presentation
1

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
Efficient recurrent processing is increasingly important for energy or memory-sensitive spatiotemporal processing tasks. RNNs with binarized activations (BARNNs) would provide increased efficiency. However, training binary recurrent RNNs is generally regarded as difficult in the existing literature.

The authors illustrate on a keyword spotting task that conventional BARNNs have non-smooth temporal gradients, while a floating point RNN and recurrent LIF spiking neural network (SNN) have smoother temporal gradients. The authors hypothesize that these smoother gradients are beneficial to learning.

The authors reproduce the difficulty of training BARNNs. They apply three existing methods: (1) surrogate gradients (STE), (2) probabilistic activations, and (3) sharpening activations over training. Importantly, the authors show that on a static-input task, CIFAR, BARNNs train comparably well compared to a floating-point baseline. In contrast, for spatiotemporal tasks SC and SOT, BARNNs do not train well compared to a floating-point baseline. Interestingly, however, in contrast to the 3 conventional BARNN methods listed above, the authors train a LIF SNN and achieve competitive task accuracy on all three tasks compared to a floating-point baseline. The authors identify the stateful accumulation, leaky, and reset mechanisms as potential explanators for the SNN’s advantage over the conventional BARNN methods.

The authors hypothesize that the stateful accumulation is responsible for the SNN advantage, so they add stateful accumulation to the pre-activations of the 3 conventional BARNN methods and recover competitive task accuracy with the LIF SNN and floating point baseline for SC and SOT tasks, for all but the sharpening method. This evidence supports the hypothesis regarding the critical role of stateful accumulation.

The authors also investigate how the leak and reset features of LIF SNNs affect SSNs trained using surrogate gradients. The authors train networks using surrogate gradients or probabilistic activations with stateful accumulation (integration), leak, and/or reset. The authors find that generally competitive task performance is maintained in all cases, and they conclude that the key ingredient for well-performing BARNNs is stateful accumulation (integration). Furthermore, the authors find that the distributions of trained parameters varies among the different configurations.

### Strengths
Significance.
This work makes a valuable connection between conventional binarized networks and spiking neural networks (SNNs). The connection is particularly valuable because it carefully uncovers “all you need” to get the benefit from SNNs in more conventional binarization approaches for recurrent networks – namely, stateful accumulation in preactivations (integration).

Originality. 
This work is the first I have seen that systematically compares conventional BARNN training methods for RNNs to SNNs on relevant spatiotemporal tasks.

Quality.
The author’s approach is generally clear, and their line of reasoning generally lucid.

Clarity.
The state goal and subsequent structure of the paper creates a clear narrative illustrating how the author’s reached their findings.

### Weaknesses
I noted the following weaknesses:

Notably, the SNN Eq (7) has an infinite-extent surrogate derivative, while Eqs (2) (3) and (4) for BARNNs have finite-extent surrogate derivatives. One confounding reason for why the SNN performs better on spatiotemporal tasks, in addition to the integrative state, is the infinite-extent surrogate derivative. Could this also be the reason why SNNs learn better than the conventional BARNN approaches? Or stated another why – why did the authors choose finite-extent surrogate derivatives for BARNNs and infinite-extent for SNN? Stated yet another way – is there a reason why this finite-vs-infinite extent distinction is irrelevant?

In section 4.1, the authors state that BARNNs are unstable through time. In what sense are they unstable - are the authors using ‘stability’ in some a technical sense? E.g., one could argue that the dynamics are in fact stable – they do not go to infinity nor negative infinity.  It would be helpful to clarify whether the authors are referring to a lack of smoothness in the temporal gradients, or some other form of instability.

I have trouble following the logic from line 313 to 341. For instance, why would activities propagate poorly in BPTT in the oscillatory example Eq 10?  The surrogate derivates are not zero, so as far as I can tell, gradients would propagate without issue. In line 325, why would taking the surrogate gradient of this patter with respect to the recurrent weights provide minimal information other than the relative value of the recurrent weights to the feedforward activity? In line 327, what’s a “real valued” BARNN? My understanding was that BARNNs had binary activations by definition. In line 338, “resulting in dense discontinuities in the input” – to what input do the authors refer? More generally regarding the choice of a single-neuron BARNN illustrative example – are there no averaging effects when many neurons are considered that could help smooth out binary activation oscillations?

### Questions
I asked the most salient questions above in the “Weaknesses” section. The questions that follow are more minor.

1.	To be clear, are all weights and integrative states floating point in this work? (Only activations are binary.)

2.	Why are the dense layers for SC and SOT not recurrent? 

3.	Is there anything that can be said about the hyperparameter selection process used in this work, to help justify that the conclusions drawn in this work are not an artifact of certain hyperparameter choices? (E.g., perhaps the reasoning sharpening did not work as well as other BARNN methods is because it requires different hyperparameter settings to perform well.)

4.	What is an autapse?

5.	Regarding line 402, the authors state distributions of leaks is beneficial. Did the authors use a distribution of leaks in this work? Were leaks trainable parameters?

Thank you for this fascinating work.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper deals with artificial neural networks with binary activations (BANNs). Spiking neural networks (SNNs) are a subset of BANNs. The authors investigate whether methods to train feedforward BANNs (e.g., surrogate gradient)  also work in a particular kind of recurrent BANNs: SNN with recurrent connectivity, with and without (leaky) integration. It turns out that these methods fail without (leaky) integration.

### Strengths
These results are new.

### Weaknesses
The scope of the paper is very narrow. Essentially, the authors take the sort of architectures that is typically used by the SNN community and show that the usual training methods (e.g., surrogate gradient) fail when removing the (leaky) integration (this is somewhat useful to know for the SNN community, but the vast majority of papers use integration anyway because it is useful to learn temporal dependencies). However, recurrent BANNs are a much broader class. For example, binarized GRU has been proposed (see SpikGRU by Dampfhoffer et al), as well as binarized LSTM (https://ieeexplore.ieee.org/abstract/document/7743581). So much more work would be needed to support their general claim that integration is necessary and sufficient to train recurrent BANNs.

Minor points:

* The SNN community always uses {0,1} activations, but the BANN community use {-1,1} most of the time. This should be discussed. In the experiments, the author restricts themselves to {0,1} activations. This again restricts the scope.

* The accuracy they reach is well below the SOTA (e.g., around 80% for GSC vs 95% here https://openreview.net/forum?id=4r2ybzJnmN)

* "g_L is a term which regulates the speed with which x_L decays to zero in the absence of inputs" tau_x already does that. One constant is enough.

* Eq 9: I think it should be dx_L / dt

* You may want to say that Eq 12 corresponds to the (non-leaky) Integrate and Fire (IF) neuron.

* Eq 13 bottom: I think it should be dx_L, not dx_L / dt

### Questions
>For networks with temporal dynamics, the entire image was presented for 16 timesteps and the network output was taken as activity on the final step.

It's more common to take the mean or max activity across timesteps. Have you tried?

### Soundness
1

### Presentation
2

### Contribution
1
