# A Parallel Multi-compartment Spiking Neuron For Multi-scale Sequential Modeling

- Decision: Reject
- Scores: 6, 5, 6, 3, 6

## Abstract
The human brain possesses remarkable abilities in processing sensory signals that exhibit complex temporal dynamics. However, brain-inspired Spiking Neural Networks (SNNs) encounter challenges when dealing with sensory signals that have a high temporal complexity. These challenges primarily arise from the utilization of simplified spiking neuron models, such as the widely adopted Leaky Integrate-and-Fire (LIF) model, which has limited capability to process temporal information across multiple time scales. Additionally, these spiking neuron models can only be updated sequentially in time, resulting in slow training processes that pose particular difficulties when dealing with long sequences. To address these issues, we propose a novel Parallel Multi-compartment Spiking Neuron (PMSN), which is derived from the cable model of hippocampus pyramidal neurons. The PMSN model captures the intricate interactions among various neuronal compartments, allowing multi-scale temporal information to be preserved and integrated for effective sequential modeling. Furthermore, the PMSN model has been meticulously designed to facilitate parallel training on GPU-accelerated machine learning frameworks. Our experimental results across numerous sequential modeling tasks demonstrate the superior performance of the proposed PMSN model compared with other spiking neuron models. Specifically, it exhibits enhanced classification accuracy, accelerated simulation, and favorable trade-offs between accuracy and computation cost.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Simplified spiking neuron models, such as LIF, have trouble with multi-scale sequence modeling, or learning tasks involving learning complex temporal dynamics. While others have developed methods to account for this, training speed and performance is still relatively subpar. In this paper, the authors utilize biological inspiration from hippocampus pyramidal neurons and their multi-compartmental modeling to design a new generalized multi-compartment model which allows for arbitrary numbers of compartments. They also introduce a parallel implementation of this model for faster training on GPU accelerated hardware while accounting for the reset mechanism, unlike previous works.

### Strengths
1) The new multi-compartment model performs better than other memory-enhanced models and single compartment models on sequence modeling tasks with relatively similar parameter counts on standard benchmarks.
2) The topic of better exploiting temporal dynamics during SNN training is important for their development.
3) The parallel implementation, especially accounting for reset, is an important and useful contribution as SNNs are generally slow to train and have yet to be parallelized effectively.

### Weaknesses
1) Regarding Figure 4: while the parallel model was compared to its serial implementation in terms of speed up, what is the ratio/training time difference between PMSN and PSN? If PSN is faster, since it is only a single compartment model, how significant is this difference? I am not referring to the computational cost but instead training acceleration only. It would be beneficial to see a direct comparison of training time per epoch, or total training time, between the PMSN and PSN models across the different sequence modeling tasks. This would provide a clearer picture of the overhead introduced by the multi-compartment structure and the effectiveness of the parallel implementation in mitigating that overhead. Specifically, it is unclear how much the parallel implementation truly accelerates the training of the multi-compartment model compared to a single compartment model, and whether this acceleration is significant enough to justify the added complexity.
2) Is the parallel implementation/methodology that incorporates the reset mechanism general enough to be applied to single compartment models? It would be useful to see a more detailed explanation of how the reset mechanism is implemented in the parallel framework, and how it can be adapted to other SNN models, especially single compartment models. This would help to clarify the generality of the proposed approach and its potential impact on the broader SNN research community. For example, can the same parallelization strategy be applied to other common single compartment models such as the leaky integrate-and-fire model with adaptive threshold?

### Questions
Please see above.

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors define a multi-compartment spiking neuron model that is able to process signals of "high temporal complexity".  Importantly, this model accounts for the spike reset mechanism.  The Parallel Multi-Compartment Spiking Neuron is inspired by hippocampal pyramidal neurons and admits a formulation that facilitates parallel training on GPUs.  The authors demonstrate the model's advantages in terms of performance and complexity.

### Strengths
The model and the approximations/trade-offs made are well-presented and clear.  Capturing complex temporal sequences is also a useful property.  A GPU accelerated model is of course an advantage in the modern day with the ubiquity of such hardware.

### Weaknesses
 The model is very specific, without any particular justification.  When one uses spiking networks, it is usually (in my experience) because one wants to model a spiking neuron system, but then choices of compartments are no longer arbitrary.  This is really a question of motivation for the paper that seems missing to me.  What problem are the authors solving?  Why does one need a spiking neuron model? Or is this particular spiking neuron model related to one in common use in circumstances unfamiliar to me?  If it is already related to a model in common use, then having a fast implementation is of some importance.

A related issue is that the models used for comparisons seem very limited (if one is only concerned with whether the model is a spiking model).  Many groups have been training spiking neural networks for a long time (Zenke & Ganguli 2018 is but one example).  If the multi-compartment model itself is not of particular importance, but I needed to train a spiking model, I could just as well use a network model from one of these groups.  Does the PMCS have advantages over those models?

### Questions
The main question I have (from above) is why this particular model?

### Soundness
3 good

### Presentation
3 good

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
The authors develop a new multi-compartment spiking neural model,
which is can be efficiently computed on GPUs, because 1) feed-forward
architecture is assumed, so that generated spikes at one time do not
effect the membrane potential in future and 2) the spiking activity is
decoupled from the membrane potential of all but the last compartment.
The authors show how the equations can be efficiently integrated and
compute on GPUs (as membrane potential evolution is just a linear
filter of the inputs). They compare the results on benchmarks
requiring long temporal integration of information, where typical SNNs
(in particular feed-forward SNNs based on simple
leaky-integrate-and-fire neurons) struggle, and show that the richer
compartmental dynamics indeed can capture long term information.

### Strengths
* Overall, it is a solid paper that suggests a new neuron model based on
compartments for SNNs trained with SGD, and shows in detail how to efficiently implement the
simulation in forward, backward, and gradient update. The idea of
dendritic computing is not new, however, it is largely restricted to
biological spiking networks instead of SNNs.

* Since the added dynamics is at the neuron-level (instead of synapse
level), and its efficient implementation, the additional computational
cost for simulating (or deploying on neuromorphic hardware) is
manageable.

### Weaknesses
 * The
implementation seems to require feed-forward structure as well as
positive inputs, which seems quite restrictive (in particular the
latter).

* The neuron model does not seem to
improve the benchmark results dramatically over other approaches in
all tasks (ie recurrent RNNs are similar for S-MNIST) and it thus
remains open how useful the model will be.



### Questions
* I don't follow why one can assume that $I(t)$ is always positive for
the ``parallel implementation of the output compartment with
reset''. In typical SNNs, the input current is given by $I(t)=WS(t-1)$
(without a synapse model) and the weights are positive or negative
real numbers, so in general, the inputs *can* be negative. Isn't that
assumed here? However, if negative inputs are allowed, then the floor
of the accumulated input with the threshold $\theta$ (in Eq 15) will
not result in the number of spikes over the time period. Maybe I am
missing something here. If only positive currents are allowed, it
should be discussed as it seems to be a major restriction. If so it
would be interesting to know what the impact of this step would be (on
the simulation speed) if not done in parallel to allow for negative
currents.

* It is not clearly stated whether the flux parameters and decay rates
of and between the compartments are learned with SGD?

* In the equations (eg Eq. 3) the neural indices are written as
super-script ($v^{i}$) which is easily confused with power. Better to
use subscripts or write $v^{(i)}$ to avoid confusion.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes the parallel multi-compartment spiking neuron (PMSN). The PMSN has n compartments, and only the last compartment can fire and reset. Thus, the neuronal dynamics of the first (n - 1) compartments can be paralleled easily. For the last compartment, the soft reset and the floor function are combined, which parallelizes the neuronal dynamics with reset. The performance and energy estimation are validated on temporal datasets.

### Strengths
1. Compared with the previous work PSN (Fang et al., 2023) which removes the neuronal reset, the PMSN can be parallelized with the neuronal reset. The ablation experiments show that the removal of neuronal reset decreases task performance.

2. The experiment results on sequential CIFAR are high, showing the advantage of the PMSN.

### Weaknesses
In section 5.3, only the speeds of serial and parallel implementation of the PMSN are compared.

The accuracy of the ImageNet dataset, which is an important benchmark for deep SNNs, is not reported.

### Questions
Can the authors provide a speed comparison between the PSN and the PMSN?

What are the theoretical FLOPs and memory consumption of the PMSN? I suggest that the authors provide a comparison between these two neurons. It would be better if a comparison between the memory consumption during training of an SNN with two neurons is provided.



--post rebuttal

Thanks for your response. It is clear that the PMSN is more similar to the sliding PSN rather than the PSN. I agree with reviewer 9iDX that the current model only applies to the last compartment. The accuracy of the model is lower than the compared PSN method on the ImageNet dataset. Also, it is a pity that the current implementation of the PMSN does not make full use of GPUs. 
Thus, I decide to keep my ranking.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose a new architecture for sequence modelling, based on multicompartment neuron dynamics. They then develop a method for parallel training of these systems and apply them to several benchmark tasks.

### Strengths
The experimental results seem very strong, significantly outperforming previous methods. In addition, the figures are clear and help the reader with understanding the content. Lastly, parallelizing the training of such spiking multi-compartment models in the temporal dimensions is novel (to my knowledge) and can be potentially impactful.

### Weaknesses
 **Soundness**

One of the main contributions of the paper, the parallel implementation of the algorithm, seems to hinge on the fact that they set beta_{n, n-1} to zero. What is the effect of this on the neuronal dynamics? Specifically, by eliminating the feedback from compartment *n* to *n-1*, does this not fundamentally alter the integrative properties of the multi-compartment neuron? Can this model still be considered biophysically realistic, given this constraint?

**Clarity**

Many parts of the paper are presented in an overly convoluted way. I believe that this paper would largely benefit from moving math that is not essential to understanding the context of the paper to the appendix, for example equations 17, 18, 19. The core ideas are obscured by the dense mathematical notation.

In addition, it would be valuable if the authors attributed a biophysical meaning to their learnable parameters. For example, what does it mean for the coupling strength between compartments to be learned? How does this relate to known biophysical mechanisms?

Finally, I fail to understand where equation 14 comes from (although I am not exactly from the field, maybe it is clear to other reviewers).

**Novelty**

I believe that the claims on novelty for the multicompartment model are a bit over-stated. At the very least should the authors cite some of the (decades of) work on multicompartment modelling and its numerical implementations (starting from Hines 1984). The voltage update equations (apart from the non-linear reset) are identical to those papers, and I think this should be clarified.

### Questions
See questions in the "weaknesses" section.

Page 6: I do not understand this sentence: `we force vs to reset to a level below the firing threshold, which bears closer resemblance with biological observations.` Why does this have closer resemblance to biological observations? Also closer than what other mechanism?

Lastly, the authors claim (even in the abstract) that their work is motivated by a cable model of cable model of hippocampus pyramidal neurons. Given that the model they eventually use is a 5-compartment cable without any particular dynamics, this choice of model seems extremely specific. What exactly is the reason to claim that the model is in any way "hippocampal" or even "pyramidal"?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
