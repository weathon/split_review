# Sufficient conditions for offline reactivation in recurrent neural networks

- Decision: Accept
- Scores: 5, 6, 6, 6

## Abstract
During periods of quiescence, such as sleep, neural activity in many brain circuits resembles that observed during periods of task engagement. However, the precise conditions under which task-optimized networks can autonomously reactivate the same network states responsible for online behavior is poorly understood. In this study, we develop a mathematical framework that outlines sufficient conditions for the emergence of neural reactivation in circuits that encode features of smoothly varying stimuli. We demonstrate mathematically that noisy recurrent networks optimized to track environmental state variables using change-based sensory information naturally develop denoising dynamics, which, in the absence of input, cause the network to revisit state configurations observed during periods of online activity. We validate our findings using numerical experiments on two canonical neuroscience tasks: spatial position estimation based on self-motion cues, and head direction estimation based on angular velocity cues. Overall, our work provides theoretical support for modeling offline reactivation as an emergent consequence of task optimization in noisy neural circuits.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This submission seeks to model the reactivation of brain activity during periods of quiescence using task-optimized network. The paper develops some mathematical formalisms to show that under certain assumptions, recurrent neural networks trained to perform a task develop denoising dynamics. 

While there are some interesting ideas presented in this submission, overall it feels that the results presented in the current version are preliminary and not surprising.

### Strengths
— Understanding the neural mechanisms underlying reactions/replays is an important question.

-- The paper seeks to analyze RNNs trained to perform a class of tasks theoretically, which is a somewhat rare excise in this literature. 

— The mathematical analysis of the loss function used in the training and the connection to the Langevin dynamics, while under somewhat strong assumptions, remain interesting.

### Weaknesses
1. A number of relevant studied were not cited and discussed. This include work using RNNs and attractor dynamics to model the replay and theta sequences in the hippocampus, e.g.,
Hopfield, John J. "Neurodynamics of mental exploration." Proceedings of the National Academy of Sciences 107.4 (2010): 1648-1653.
Kang, Louis, and Michael R. DeWeese. "Replay as wavefronts and theta sequences as bump oscillations in a grid cell attractor network." Elife 8 (2019): e46351.
Chu, Tianhao, et al. "Firing rate adaptation affords place cell theta sweeps, phase precession and procession." bioRxiv (2022): 2022-11.

The paper also misses several pieces work in training RNNs to study the grid cells systems and HD systems.
Cueva, C. J., & Wei, X. X. (2018). Emergence of grid-like representations by training recurrent neural networks to perform spatial localization. ICLR.
Uria, B., Ibarz, B., Banino, A., Zambaldi, V., Kumaran, D., Hassabis, D., Barry, C. and Blundell, C., (2020). The spatial memory pipeline: a model of egocentric to allocentric understanding in mammalian brains. BioRxiv, pp.2020-11.
Cueva, C.J., et al (2020). Emergence of functional and structural properties of the head direction system by optimization of recurrent neural networks.ICLR.

2. The main results are not surprising after considering what we know so far on this topic. Prior work has shown that training the RNNs to perform path integration or angular integration task leads to networks that exhibit attractors dynamics that is similar to continuous attractor models. Furthermore, it is well known that attractor dynamics can perform denoising. Thus it is not surprising that RNNs trained on these previous studied tasks can perform denoising. 

It should also be noted that prior work has further characterize the rate of diffusion along the low-d manifold, e.g., see Fig 6 of the following paper: 
Burak, Y. and Fiete, I.R., 2009. Accurate path integration in continuous attractor network models of grid cells. PLoS computational biology, 5(2), p.e1000291.


3. As described in the paper, the trained network follows diffusion dynamics when the stimulus turned off. This is naturally expected because the diffusion of network state on a low-d manifold. This would result in brownian-motion like trajectory. Furthemore, the replay trajectories observed in the hippocampus typically described by a systematic drift towards one direction (e.g., in linear or circular tracks), not diffusive dynamics. Can the authors be more explicit about the experimental data they were modeling?

4. One more point that confuses me—the authors stated “we found that even trajectories generated by networks that were not trained in the presence of noise, and also were not driven by noise in the quiescent phase, still generated quiescent activity distributions that corresponded well to the active phase distributions. ” This seems to argue against the denoising dynamics, and make the usefulness of the mathematical analysis questionable.

5. The mathematical analysis relied on a set of approximations and assumptions, which were not well justified.

### Questions
Would it be possible to discuss more explicitly how their results are connected or supported by the empirical data? In particular, how is the “diffusive reactivation” related to neural data?

 The mathematical analysis relies on a number of assumptions, to the extent that it is difficult to judge whether the conclusion would actually be applicable to the numerical experiments. Can these assumptions be justified or better motivated (beyond the sake of mathematical convenience)?

### Soundness
2 fair

### Presentation
2 fair

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
The authors develop a theoretical framework for understand why offline reactivation occurs in recurrent neural networks. In particular, the authors argue that neural noise during awake states is essential for the emergence of faithful and varied reactivation of neural trajectories during quiscience (i.e. in absence of external stimuli).

### Strengths
- the paper is generally well written
- the mathematical theory is well presented and interesting (as far as I'm aware it is novel, but I am not certain of this)
- offline reactivation should be of interest both to machine learning and neuroscience researchers; the paper does make some theoretical and experimental headway into why/how it occurs

### Weaknesses
 - perhaps this is not in the scope of the paper, but the authors do not provide any theoretical/numerical support for the functional benefit of offline reactivation. The authors mention other works which demonstrate that it may aid the formation of long-term memories, schema, planning. Do the theoretical/numerical results in this paper support these possibilities, or any one in particular?
- Relatedly, a key feature of this study is that the RNNs considered are noisy during awake states. It's unclear to me exactly why this is necessary. The authors "found that even trajectories generated by networks that were not trained in the presence of noise, and also were not driven by noise in the quiescent phase, still generated quiescent activity distributions that corresponded well to the active phase distributions"; is the point that there's more space exploration with noise, giving rise to a functional benefit? Or that somehow the introduction of noise better captures observed neural data? Furthermore, the fact that the distributions match does not necessarily mean that the individual trajectories are meaningful or explore the state space effectively; this point requires further clarification.
- I found the link between the theoretically optimal solution for update dynamics and the actual application of RNNs somewhat unclear. Are we to take that (presumably backprop-trained) RNNs employ update dynamics similarly to the theoretical solution; is it biologically reasonable for e.g. equation 18 to be implement by an RNN? If so, is it possible to show that they do; e.g. by comparing these recurrent inputs to the optimal solution? If not, are the experimental results relevant to the theory? The paper would benefit from a more detailed analysis of how the learned RNN dynamics relate to the theoretical optimal dynamics.
- Relatedly, perhaps this is overly harsh, but I also do not find the result that RNNs without stimuli visit similar states as with stimuli very surprising. The claim that the *distribution* of states is similar is more interesting, but it is still not clear whether individual trajectories in the quiescent phase are meaningful or simply noisy fluctuations around a learned attractor.
- The authors suggest an interesting discrepancy in experimental prediction for their noise-based theory of offline reactivation and generative modeling; specifically, that "while generative models necessarily recapitulate the moment-to-moment transition statistics of sensory data, our approach only predicts that the stationary distribution will be identical". I am confused by this statement and not sure if it is true. Is that to say that the proposed model would not encode sensory transitions but would simply replicate the overall probability distribution of sensory states? I would find this surprising for an RNN whose recurrent weights are trained on sensory data; that is, I would suppose that the RNN weights would themselves somehow capture transition statistics of the task variables (e.g. maybe this is valuable as a kind of denoising effect on noisy observations). Perhaps I am wrong though

### Questions
- In section 2.1 it may be relatively obvious that p denotes probability, but I would still clarify this
- In equation 15 it's a bit odd to provide a new definition for L_{noise} having just defined it previousply with the D term involved
- the delta t is given as 0.02. What's the unit, seconds?
- I would recommend a limitations section

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors demonstrate that training network dynamics on an upper bound of the cost function for learning a function of an input stimulus in the presence of network noise results in network dynamics that separate into a denoising component and a signal integration component.  Furthermore, they provide conditions such that, in the absence	of input, the network will reproduce typical states of the (learned function of the) input stimulus.  Notably, this strictly requires the input noise to be different in the quiescent vs input-driven cases.  The authors demonstrate numerical simulations in which networks reflect these results.

### Strengths
This paper does a nice job of outlining how the cost function can be deconstructed into two components, the denoising component and the signal integration component.  The idea of replay being a result of signal integration in the presence of noise is an interesting one, and the authors present a simple mechanism whereby this can arise. This is a contribution to an important question in neuroscience.  The theoretical approach, results, and the numerical experiments are well described and supported.

### Weaknesses
The paper is potentially confusing to some readers in that the presentation (and the numerical experiments if I have followed) regard training a network with a fixed nonlinearity and trainable weight parameters (i.e. a typical RNN) but the theoretical analysis considers not a fixed nonlinearity, but rather the space of all possible dynamics that could govern the system.  I suspect this may misdirect some readers regarding the basic argument (possibly me as well).  

Training a regular RNN on the cost function, L, of course, does not guarantee anything about the cost function L_upper, so one must make some additional assumptions about the structure of the network dynamics, namely something akin to demanding that the space of permissible dynamics admits the derived minimum of L_upper.  In the case of the numerical experiments, the authors use ReLU and decompose the input to the nonlinearity into a recurrent part and a signal integration part, which should approximately allow for the decomposition that leads to L_upper.  One needs to add an argument that this decomposition is reasonable for certain classes of RNNs. E.g. If the network is in the active regime, the ReLU doesn't contribute much and then the composition amounts to considering the activity updates from the recurrent part and the input part separately.  One could make a similar argument about sigmoids.  In short, the authors should, I think, be direct about the assumptions on the RNN necessary for their theory. 

Regarding the quiescent state, I think the authors are perhaps a little too cavalier with the fact that, strictly speaking, the noise term must change in order to guarantee replay.  As presented at the moment, it feels to this reader like a weakness that is not adequately addressed.  The authors should either supply 1) a reason to believe this sort of change happens in real networks or 2) a demonstration that the deviations are not sufficient to qualitatively change the main result.  There is also the possibility that this is an opportunity for the authors.  The deviations from perfect replay if the noise does not change amount to a prediction, and one which may have computational advantages (e.g. facilitating exploration in terms of a planning algorithm).

### Questions
Last sentence of the introduction:  I think "ecologically" should be "ethnologically"

Questions:

- Does this work for more general RNNs (more general nonlinearities, interactions between recurrence and signal integration, etc.)?

- Is there reason to believe the noise distribution changes in the quiescent state?

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper proposes a training algorithm for continuous-time RNN integration in the presence of noise that relies on an upper bound for the loss that is split into a denoising and a tracking part. It is then shown for a angular and a motion velocity integration task that the noise compensation dynamics induce diffusive reactivations in a quiescent state.

### Strengths
The paper introduces a novel method of task-optimization for RNNs that rely on an upper bound for the loss that is split into two parts: the first term optimizes for denoising and the second term is optimized for tracking the signal. This is the first paper that discusses the contribution of learning in the presence of noise to have implication to reactivations.
Through this framework a new perspective is proposed on reactivations in the brain being the consequence of the presence of noise.
Finally, this framework provides interpretability to the system that solves an integration task in terms of what part of the dynamics corresponds to denoising the systems and which to integrating instantaneous changes of the state variable.
The effectiveness of the approach is demonstrated against a couple of integration tasks highlighting its applicability. The theorems and proofs are sound.
Furthermore, the paper is well written and the contributions are clearly explained with possible implications of the work for neuroscience.
These implications for neuroscience might provide a new perspective on how neural dynamics that implements neural integration might be decomposed into a denoising and an integrating component and how networks that learn in the presence of noise then exhibit reactivations.

### Weaknesses
It is unclear what is meant with tuning of the value of $\tau$. Is this for a fixed noise level? Or is it chosen as the optimal for all used noise levels for training?

\paragraph{Figures}
Use some transparency in Figure 1 f and e so that overlapping points are visible. At the moment it is unclear what proportion of the points is hidden behind the first layer and what their distribution is.


\paragraph{Contribution}
The the demonstration contribution of this framework could benefit from some additional experiments.
Comparison to training without noise and added noise in quiescent state is missing.
Comparison to other ring attractor/head direction models is missing.

Finally, some of the implications of the proposed framework require more justification.
The conclusion that reverse replay could be explained by diffusive reactivations seems like a stretch and should be substantiated better. 
Also, reactivations such as replay are not the type of reactivations that are found in the networks in the paper (this is admitted in the paper) even though the introduction is discussing those for a large part.

\paragraph{Noise}
The fact that training without noise resulted in erratic output trajectories might be explained by the statistics of the input. 
Does the used input static reflect best what happens in animal behavior?
It would be good to compare the statistics of state sequences and reactivation sequence on the level of the sequences themselves.
Because in terms of optimality of exploration erratic trajectories might be more optimal to fully explore, see for example McNamee (2021). But see also Supplementary Figure A.1 (a) vs (e) that seems to show that a network that  has been trained without noise (e) explores a bigger part of the state space than a network that has been trained in the presence of noise (a).

Finally, the claim that even with the addition of noise the failure of exploration could not be corrected (page 8, middle) should be better substantiated with a comparison based on distributions rather than just example trajectories (currently Suppl.Fi. A.1e-f is used as justification).


McNamee, D.C., Stachenfeld, K.L., Botvinick, M.M. and Gershman, S.J., 2021. Flexible modulation of sequence generation in the entorhinal–hippocampal system. Nature neuroscience, 24(6), pp.851-862.

### Questions
How is the bias exactly defined for figure 2?
In Figure 2, what distribution are random networks sampled from? Further, what does it mean that a random network s trained and tested in the presence of noise (as would be implied in the column $\text{R}^\sigma$).


Why is the kernel density estimate the best (or a good) way to compare trained networks?

How does the final trained network in terms of its parameters compare to the full greedily optimal dynamics?
How do different trained networks compare to each other in terms of the reactivation statistics?

Is it truly a ring attractor that solves the angular integration task? On the given time scale it could be the case that the solution is provided by a line attractor that gets mapped to the ring by $D$.

In Equation (17) is the optimum unique?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
