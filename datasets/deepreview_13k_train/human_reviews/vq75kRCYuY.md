# SOLO: Surrogate Online Learning at Once for Spiking Neural Networks

- Decision: Reject
- Scores: 5, 3, 5, 3

## Abstract
Spiking Neural Networks (SNNs) show promise as energy-efficient models inspired by the brain. However, there is a lack of efficient training methods for deep SNNs with online learning rules that mimic biological systems, particularly for deployment on neuromorphic computing substrates. In this paper, we propose Surrogate Online Learning at Once (SOLO) for SNNs, which utilizes several surrogate strategies that could be implemented in a hardware-friendly manner. By exploiting expanded spatial gradient from only the final time step of forward propagation, SOLO achieves low computational complexity while maintaining comparable accruacy and convergence speed. Moreover, the update rule of SOLO takes the simple form of three-factor Hebbian learning, which could enable online on-chip learning. Our experiments on both static and neuromorphic datasets show that SOLO achieves performance comparable to conventional learning algorithms. Furthermore, SOLO is hardware-friendly, offering robustness against device non-idealities and sparse access during write operations to memory devices.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes a surrogate online learning method-SOLO, to efficiently train spiking neural networks. The main idea is to consider a backward path only at the final step, which disentangles the temporal dependencies of the conventional BPTT-type training method. The authors show that by doing so, the performance on several benchmark tasks does not decrease significantly, while largely reducing the required memory and training time. This shows the potential to be implemented in the neuromorphic hardware in the future.

### Strengths
- The paper is well-written, with very clear illustration on the motivations, methods and implementations. 
- The paper proposes a new way to efficiently train spiking neural networks, and this method shows the potential to solve the on-chip learning challenge of neuromorphic chips.

### Weaknesses
 - The paper, however, lacks of a enough investigation and comparison with the existing methods. Aiming to cut the temporal dependencies to optimize the SNN training is not a new idea [ref. 1-3], what are the main differences (except for the “last time step” part) compared with them? For instance, the intrinsic idea, the approximation way, even the three-factor-rules part are quite similar as in [1]. Specifically, the paper should elaborate on how SOLO's approach to approximating the gradient differs from methods like surrogate gradients used in [1], and whether the specific form of the three-factor rule introduces any novel computational advantages or disadvantages. A more detailed analysis of the computational complexity and memory footprint compared to these existing methods, beyond just the reduction in temporal dependencies, is needed.
- The resulting performance decreases, if not significantly, still quite a lot, on many datasets. One might suspect the availability of this method in real use cases. The paper needs to provide a more thorough analysis of why the performance drops, including a breakdown of the types of errors that SOLO makes compared to BPTT or STBP. It should also discuss the potential limitations of the approach in terms of the network architectures and tasks it can effectively handle. For instance, does SOLO struggle more with certain types of temporal patterns or datasets, and if so, why?

### Questions
See the above weakness part.
In addition, in table 1 and table 2, the baseline performance looks not very high, e.g., for CIFAR 10, SNN SOTA is already close to 95% with 4-6 time steps, and CIFAR100 around 73%, but in these tables, these number are relatively low, could you explain the reasons?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes Surrogate Online Learning at Once (SOLO) for training SNNs in a hardware-friendly manner. It only leverages spatial gradient at the final time step for low computational complexity. Experiments are conducted on static and neuromorphic datasets to verify the effectiveness.

### Strengths
This paper considers online SNN training methods to promote online on-chip learning, which is an important topic.

### Weaknesses
1. The motivation to only consider the gradient at the last time step is not convincing enough, and the experimental results are quite poor. There is no formal/theoretical justification for the claim “we believe that the information of the accumulative neurons in the final time step could yield the most distinct and clear error value among all given time steps”. It is obvious that only considering spatial gradient for the last time step will lose a lot of information on previous time steps, and the experimental results indeed show a significant drop in accuracy, especially for neuromorphic datasets with temporal sequences. For static datasets, there is no temporal information and binary neural networks (or taking T=1 for SNNs) can easily work well, so experiments are not surprising or appealing. It is unclear what’s the advantage of the proposed method over existing online training methods [1,2].

2. The idea of the proposed method may, to some extent, be viewed as a special case of a recent work [3]. It proposes a method SLTT, which drops the temporal dependency of BPTT and only uses spatial gradients at each time step, and it further proposes a variant SLTT-k, which randomly samples k time steps for the spatial gradient. The method in this paper may be viewed as taking k=1 and fixing the considered time step as the last time step. However, this paper ignores gradients for previous time steps, leading to much poorer performance.

### Questions
1. It is not clear enough why pPLIF is more straightforward for hardware implementation than PLIF. If consider deploying trained models, $\beta$ for the current in PLIF can be absorbed into the weight. If consider training models, it is also unclear for pPLIF how the gradient for the learnable membrane time constant can be calculated on hardware.

### Soundness
1 poor

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes an online learning method for SNNs. A spiking neuron layer without firing is used to accumulate outputs. Then four surrogate strategies are proposed:
1. Using a boxcar surrogate function with only a 0/1 gradient.
2. Using an always-on gradient in loss.
3. Redefining the gradient of max pooling to propagate gradients to those elements that are not the maximum values in the pooling windows.
4. Using eligible traces to calculate gradient online.

The proposed methods are validated on some popular datasets.

### Strengths
As an online learning method, this paper achieves O(1) memory complexity, which is meaningful for the SNN community.

The proposed method is hardware-friendly and has the potential to be applied to neuromorphic chips.

### Weaknesses
The accuracy drops sharply in all datasets except for the toy MNIST dataset, which can not show the effectiveness of the proposed methods. I am afraid that the plain SNN with a simple Real Time Recurrent Learning method will get close performance to the proposed methods.

As a comparison, OTTT [1] is also an online training method and achieves much higher accuracy even on the challenging ImageNet dataset.

I do not understand the necessity of "surro2: Always-On beyond Spike Accumulation". The authors claim that they "ensuring error propagation across all classes". But the gradient to each class is not zero in most cases unless the neuron that represents a class outputs 0 at all time-steps when it is not the target class (or outputs 1 at all time-steps when it is the target class).

### Questions
I do not understand the necessity of "surro2: Always-On beyond Spike Accumulation". The authors claim that they "ensuring error propagation across all classes". But the gradient to each class is not zero in most cases unless the neuron that represents a class outputs 0 at all time-steps when it is not the target class (or outputs 1 at all time-steps when it is the target class).

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presents a novel training method called SOLO, which uses surrogate strategies to perform end-to-end learning with low computational complexity. It is easy to implement on neuromorphic hardware and is evaluated on various static and neuromorphic datasets. The method is compared with existing methods like BPTT, STBP, E-prop, and DECOLLE. The paper also demonstrates SOLO's robustness to hardware-related noises and reliability issues, making it suitable for deployment on neuromorphic computing substrates.

### Strengths
On-chip single-time backpropagation: SOLO is a surrogate online learning method that trains deep SNNs end-to-end using spatial gradients and surrogate strategies to reduce computational complexity and memory requirements. It also introduces a simple three-factor learning rule for online on-chip learning on neuromorphic hardware.



Hardware awareness: This algorithm considers too many compatibility issues between neuromorphic computing and SNN. It introduces neuron models like pPLIF and pPLI and uses hardware-friendly surrogate strategies like boxcar function and always-on pooling. The evaluation is done given the hardware-related noise.

### Weaknesses
The paper lacks clear theoretical justification for the proposed SOLO method, relying on empirical results and biological plausibility without mathematical analysis or proof of convergence.


Unfair comparison: The paper compares SOLO with offline methods like BPTT and STBP but does not compare it with the newest online methods like OTTT (Xiao et al., NeurIPS 2022), SpikeRepresentation (Meng et al., CVPR 2022), and so on.


Lack of clarity: Some of the mathematical expressions lack proper definition and notation. I am confused by some details.


Minor: the citation is not proper in the content. I think the author should use ‘\citep{}’ instead of ‘\cite{}’ most of the time.

### Questions
For equation 6, why is there item $\theta(U^\sim[t]-\theta^\sim_{th})$ rather than $\theta(abs(U^\sim[t]-\theta^\sim_{th})<p)$.



Why does pTRACE need a clamp function $k$? I think equation (5) really ensembles the proposed pPLI (equation (2)). Why don’t you simply use pPLI as a surrogate?



Please point out the difference between the current proposed SOTA online training methods and propagate-only-once training methods. Examples are OTTT (Xiao et al., NeurIPS 2022) and spike representation (Meng et al., CVPR 2022).



How do we implement SOLO on a neuromorphic platform when it has a float-point derivation?

[1] Xiao et al., Online Training Through Time for Spiking Neural Networks, NeurIPS 2022
[2] Meng et al., Training High-Performance Low-Latency Spiking Neural Networks by Differentiation on Spike Representation, CVPR 2022

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
