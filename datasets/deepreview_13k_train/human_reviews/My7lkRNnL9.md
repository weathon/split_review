# Forward Learning with Top-Down Feedback: Empirical and Analytical Characterization

- Decision: Accept
- Scores: 8, 8, 5, 5

## Abstract
``Forward-only'' algorithms, which train neural networks while avoiding a backward pass, have recently gained attention as a way of solving the biologically unrealistic aspects of backpropagation.
  Here, we first address compelling challenges related to the ``forward-only'' rules, which include reducing the performance gap with backpropagation and providing an analytical understanding of their dynamics. To this end, we show that the forward-only algorithm with top-down feedback is well-approximated by an ``adaptive-feedback-alignment'' algorithm, and we analytically track its performance during learning in a prototype high-dimensional setting. Then, we compare different versions of forward-only algorithms, focusing on the Forward-Forward and PEPITA frameworks, and we show that they share the same learning principles. Overall, our work unveils the connections between three key neuro-inspired learning rules, providing a link between ``forward-only'' algorithms, \textit{i.e.,} Forward-Forward and PEPITA, and an approximation of backpropagation, \textit{i.e.,} Feedback Alignment.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Forward-only learning algorithms are an alternative to backpropagation (BP), which are potentially more biologically plausible, more memory efficient, and more computationally efficient.
Two of these forward-only learning algorithms are Forward-Forward (FF) and PEPITA, the Present the Error to Perturb the Input To modulate the Activity learning rule; both algorithms rely on two forward passes to learn, rather than a forward and a backward pass.
However, the learning dynamics of these algorithms are not well understood, and both still include components that are biologically implausible.
In this work, the authors offers an explanation of how PEPITA learns by connecting them to feedback alignment.
They then use their insight to improve the performance of PEPITA by combining it with weight mirroring, a technique to improve performance of feedback alignment, as well as weight decay and activity normalization.
Finally, they propose PEPITA-time-local, an alternative learning rule that improves the biological plausibility of PEPITA by keeping updates local in time (in addition to space), at the cost of some accuracy.

### Strengths
- This paper exposes a novel connection between feedback alignment and forward-only algorithms. This connection is particularly interesting because both type of algorithms have improving biological plausibility as a principal goal; exposing underlying relationships may mutually benefit researchers for both types of algorithms. In fact, the authors have already taken a step in this direction, by empirically showing that weight mirroring, a technique developed for feedback alignment, can also be used to improve the performance of PEPITA.
- As the authors also point out, while forward-only learning algorithms have gained traction in recent years, and are gradually catching up to the performance of backpropagation on increasingly complex tasks, theoretical understanding of their learning dynamics is mostly lacking; work that shed light on how forward-only learning works is very welcome.
- The experiments performed are extensive, and the results are convincing.

### Weaknesses
 - The theoretical analysis focuses only on shallow 2-layer networks, and I’m uncertain that the Adaptive Feedback rule can be easily extended to analyze deeper networks, as the error signal has to pass through multiple hidden layers either forwards (forward-only) or backwards (feedback alignment). This limits the applicability of the analysis, making it disjoint from the experimental results on multi-layer PEPITA networks. The analysis provides insights into the alignment phenomenon in the specific case of a single hidden layer, but it does not address how this alignment might evolve or be maintained in deeper architectures. This is a significant limitation, as many of the benefits of deep learning come from the ability to learn hierarchical representations across multiple layers. The lack of theoretical support for multi-layer networks makes it difficult to understand the fundamental mechanisms that drive the performance of PEPITA in these more complex settings.


### Questions
- Figure 3 shows the performance of PEPITA-Hebbian, PEPITA + weight decay, and PEPITA + weight mirroring on CIFAR-10. Do the same trends hold for MNIST and CIFAR-100?

- I’m a bit confused on how much the PEPITA-Hebbian approximation impacts the accuracy of the model. Figure 3a shows that the impact is very small on CIFAR-10, maintaining over 50% accuracy on CIFAR-10 for 1, 2, and 3 hidden layers, but in Figure S1 the accuracy of a 1-layer PEPITA-TL model drops to around 40%. Could you explain why this is? If this is due to hyperparameter differences, how well would a non-TL PEPITA model compare in performance under the same hypersparameters/conditions as those used for Figure S1?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper connects several forward pass-only learning methods as biologically plausible alternatives to backprop, analyses their performance and error dynamics, and also proposes Hebbian and temporally local approximations for one of those methods.

### Strengths
1. The paper is well-written and does a good job articulating its aims and contributions.
2. The paper provides a theoretical link between several algorithms, and derives error dynamics (for a simple problem) for one of them. 
3. The Hebbian/anti-Hebbian approximation works as well as the PEPITA algorithm, which is a good sign for bio plausibility (of both PEPITA and FF, since they work similarly).

### Weaknesses
1. Performance on CIFAR10/100 of algorithms is lacking compared to backprop (although surprisingly much less so for CIFAR100). This performance gap would likely increase for larger networks, and it's unclear if the observed scaling trends would hold. Specifically, the reported accuracies are significantly lower than what is typically achieved with backpropagation, raising concerns about the practical applicability of these methods in more complex scenarios. The paper should include an analysis of the scaling behavior of these algorithms with respect to network depth and width to better understand their limitations.

2. No experiments with convnets, and I haven't found a justification for that. Since cifar10/100 performance gets much better with introducing convolutions (for backprop), it'd be interesting to look at the performance gap there. The lack of convolutional network experiments is a significant omission, as these architectures are crucial for image-related tasks. The authors should provide a clear rationale for not including them and ideally present results on convolutional architectures to demonstrate the generalizability of their findings.

### Questions
If I understand correctly, PEPITA-TL differs from PEPITA-Hebbian by one feature: the anti-Hebbian error term is computed for the updated weights. Based on that, I have two questions:
1. Would performance of both algorithms match if we reduce the learning rate of PEPITA-TL? Intuitively it should, since the anti-Hebbian error terms would match.
2. Can we consider PEPITA-Hebbian temporally local since it's a long-term plasticity rule? Since the network is trained with two passes over the same input, the PEPITA-TL approximation adds the first Hebbian term immediately after the first forward pass, so 10s/100s of ms. This would be too short for long-term Hebbian changes (as far as I know), so in your model you can treat both parts of the update rule as if they happen for the same network state -- meaning that PEPITA-Hebbian would be temporally local. (I guess you can account for short-term plasticity as a result of the first forward pass (so non-Hebbian changes proportional to input activity only).)

Small comments:
1. Tab1 should have PEPITA-Hebbian performance too.
2. The appendix can be included in the main pdf in this conference.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper analyzes the Present the Error to Perturb the Input To modulate the Activity (PEPITA) learning algorithm, showing its connection to Direct Feedback Alignment (DFA) as well as Forward-Forward (FF) algorithm with negative samples being the “modulated” samples in PEPITA. Some empirical experiments also study PEPITA on deeper networks and with several techniques.

### Strengths
This paper studies the connections between several biologically more plausible algorithms, providing insights from empirical and analytical perspectives.

### Weaknesses
1. I think this paper requires a clearer definition of the considered “forward-only” algorithms. In the abstract, it is defined as “avoiding a backward pass”. However, PEPITA, different from local FF, indeed requires a direct global error feedback to inputs. If PEPITA is considered as “forward-only”, is DFA also “forward-only”, as it shares the similar form of direct global error feedback without layer-by-layer BP? In the sense of “forward-only” algorithms, I don’t think PEPITA is parallel to FF with local learning.

2. In Table 1, why the considered rule has a much worse performance? It is unclear why we should consider it as it does not introduce additional properties over several algorithms while being worse. Additionally, what’s the detailed definition for “local” and “activity freezing”? For PEPITA, it requires global error feedback to inputs, and storage of activations of the first forward propagation until the second forward propagation ends. Why it is considered “local” and solving “activity freezing”? And why PEPITA outperforms DFA in these aspects?

3. In Section 3.1, the similarity to DFA only holds for the first layer. It is unclear for other layers (Eq. (4)).

4. In Section 4, the networks are still quite shallow and experimental results are quite poor. DFA can scale to large datasets and networks [1], and WM also scales to large-scale scenarios [2].

5. Some derivations are not strict and may be contradictory. For example, in Section 3 and Section 5, it is assumed for several times that $Fe$ is much smaller than $x$ so it can be ignored. In Section 5, however, it is also assumed that the “modulated” samples can be used for negative samples in the FF framework. If the modulation is small enough, why can it formulate a valid negative sample? This largely reduces the reliability of the connection between PEPITA and FF.

Overall, I think there is no enough contribution in empirical or theoretical perspectives.

### Questions
1. In Section 3.2, what’s the difference between the analysis and previous analyses for DFA?

2. In Section 5.1, what’s the connection of the derivation with contrastive Hebbian learning [1] or equilibrium propagation [2], which also takes the form of Hebbian and Anti-Hebbian phases?

[1] Equivalence of backpropagation and contrastive Hebbian learning in a layered network. Neural Computation, 2003.

[2] Equilibrium propagation: bridging the gap between energy-based models and backpropagation. Frontiers in Computational Neuroscience, 2017.

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper provides further analysis of the PEPITA learning rule, a biologically-inspired "forward-only" approach to train neural networks by replacing the backward pass with another forward pass. In connects PEPITA theoretically to two other biologically-inspired approaches, namely an adaptive version of Feedback Alignment and Forward-Forward. Additionally, the paper explores how the initialization of the feedback weights and applying techniques like weight decay, activation normalization, and weight mirroring can improve PEPITA's performance. The experimental findings demonstrate minor improvements through normalization and weight mirroring.

### Strengths
- Biologically-inspired and forward-only training approaches are a relevant and timely topic. 
- It would be very useful to unify the multitude of different approaches into a common framework. By connecting three major biologically-inspired approaches, this paper takes an important step towards that goal. 
- Given the still-remaining gap between backpropagation and forward-only approaches, analyzing and improving their performance is essential for their practical relevance.
- Section 4.2 gives a well-structured summary of the experimental results. It would have been nice, to include a discussion of the impact of weight decay, activation normalization, and weight mirroring

### Weaknesses
 - The experimental improvement and evaluation of PEPITA on their own offer only limited novelty. However, together with the analysis connecting PEPITA, FA, and Forward-Forward, this paper amounts to a considerable contribution.
- experimental evaluation:
 - only small, fully-connected networks, not that suited to more complex vision datasets
 - only image classification (MNIST, CIFAR10, CIFAR100)
 - no experimental comparison to Forward-Forward
 - only minor improvements in accuracy
- Minor Issues:
 - Figures can be a bit hard to read
  - in Fig 2 (especially 2b) the overlap of PEPITA and AFA is hard to see without zooming in
  - Fig 3 would benefit from more contrasting colors
 - the references to Figure 2c in the last paragraph of Section 3.2 seems to be mismatched with the actual order of subfigures in Figure 2
 - Table 1, line 1 seems to have the wrong citation for FA
 - Spelling:
  - in contribution (vi) "analitically"
  - in the last sentence of Section 1: "gpus" should probably be in uppercase, i.e. "GPUs"

### Questions
- Which approach do the authors considers their primary contribution? Table 1 the authors refer to PEPITA-TL as "ours" yet this is only discussed briefly in Section 5.1 and left mostly to future work.
- Why are the combinations "weight-decay + normalization + WM" and "weight-decay + normalization + no WM" missing in Table 2? Can weight decay and activation normalization not be combined?
- In Figure 3c: shouldn't pre-mirroring increase the alignment (thus decreasing the angle) before the first epoch? Yet, in Figure 3c, all three lines seem to start at the same value.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
