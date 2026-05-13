# S-TLLR: STDP-inspired Temporal Local Learning Rule for Spiking Neural Networks

- Decision: Reject
- Scores: 3, 6, 5, 6

## Abstract
Spiking Neural Networks (SNNs) are biologically plausible models that have been identified as potentially apt for deploying energy-efficient intelligence at the edge, particularly for sequential learning tasks. 
However, training of SNNs poses significant challenges due to the necessity for precise temporal and spatial credit assignment.
Back-propagation through time (BPTT) algorithm, whilst the most widely used method for addressing these issues, incurs high computational cost due to its temporal dependency.
In this work, we propose S-TLLR, a novel three-factor temporal local learning rule inspired by the Spike-Timing Dependent Plasticity (STDP) mechanism, aimed at training deep SNNs on event-based learning tasks. 
Furthermore, S-TLLR is designed to have low memory and time complexities, which are independent of the number of time steps, rendering it suitable for online learning on low-power edge devices.
To demonstrate the scalability of our proposed method, we have conducted extensive evaluations on event-based datasets spanning a wide range of applications, such as image and gesture recognition, audio classification, and optical flow estimation.
In all the experiments, S-TLLR achieved high accuracy, comparable to BPTT, with a reduction in memory between $5-50\times$ and multiply-accumulate (MAC) operations between $1.3-6.6\times$.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces a new learning rule for Spiking Neural Networks. This rule has low linear memory complexity and quadratic time complexity in terms of number of neurons. Moreover, the proposed learning algorithm incorporates a non-causal learning term,  inspired by Spike-Timing-Dependent Plasticity.

### Strengths
1) Evaluation is done on variety of tasks;
2) Paper is well-written and easy to follow.

### Weaknesses
My main concern is that the method considered in the paper (S-TLLR) is very similar to OTTT[1]: 

1) OTTT has the same learning rule as S-TLLR except that additionally S-TLLR leverages non-causality and few other minor differences. But this non-causal term doesn’t help S-TLLR consistently based on Fig. 2;
2) S-TLLR has the same time and memory complexity;
3) S-TLLR doesn’t outperform OTTT.

### Questions
1) Can the authors list all the differences between OTTT with S-TLLR methods?
2) In the paper, it is mentioned that OTTT applies learning rules at each forward pass, whereas S-TLLR enforces the learning rule at every fourth forward step. Could the authors test the performance if S-TLLR's learning rule was applied at each forward pass, similar to OTTT?
3) Can the authors do ablation study taking OTTT model as a reference starting point? The study would systematically integrate modifications that transition the model towards the S-TLLR approach.

### Soundness
2 fair

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces S-TLLR, a novel learning rule for Spiking Neural Networks (SNNs) aimed at efficient online learning on resource-constrained edge devices. S-TLLR draws inspiration from Spike-Timing Dependent Plasticity (STDP) and utilizes both causal and non-causal relationships for synaptic weight updates, maintaining constant memory and time complexity. Through extensive experimentation, the authors demonstrate that S-TLLR achieves comparable accuracy to traditional methods like BPTT but with significantly lower computational demands. The paper's contributions are highlighted by the improved generalization and performance of SNNs on a variety of event-based tasks—including image and gesture recognition, audio classification, and optical flow estimation—and the validation of S-TLLR's efficacy across multiple network topologies, marking a step forward in deploying energy-efficient intelligence in real-world applications.

### Strengths
1. S-TLLR is a groundbreaking approach that successfully trains SNNs with high efficiency, addressing the temporal and spatial credit assignment challenge that is inherent in such networks.
2.  By incorporating principles from STDP, S-TLLR aligns closely with biological neural processes, potentially unlocking more natural learning patterns and efficiencies.
3. S-TLLR successfully integrates both top-down modulation and the local algorithm.
4. The proposed learning rule maintains constant time and memory complexity, which is a significant advancement for deploying SNNs on edge devices where resources are constrained.

### Weaknesses
1. The complexity was estimated, but the real energy consumption/efficiency haven't been calculated/tested.
2. While BPTT could work on much deeper SNNs, how about S-TLLR? Could it be extended to larger models/datasets?

### Questions
Please see the weaknesses:
1. Could the energy consumption/efficiency be calculated/tested.
2. While BPTT could work on much deeper SNNs, how about S-TLLR? Could it be extended to larger models/datasets, such as CIFAR100?

### Soundness
3 good

### Presentation
3 good

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
This paper proposed an STDP-based learning algorithm that focuses on SNN training from the memory efficient perspective. The proposed algorithm has shown reduced complexity on the event-based dataset.

### Strengths
The proposed method shows reduced time complexity, it is natural that the STDP-based learning requires less memory compared to BPTT with gradient surrogation. The proposed algorithm seems hardware friendly with discrete operations.

### Weaknesses
 **W1:** Insufficient experiments: I understand that the event-based computer vision tasks are suitable for spiking neural networks, but I think the dataset reported in this paper is not comprehensive enough. In addition to the popular DVS-CIFAR10 and DVS-Gesture, N-CalTech101, and NCARs are also adopted in prior works [R1] as benchmarks. However, these results are missing in the paper. 

[R1] AEGNN: Asynchronous Event-Based Graph Neural Networks, CVPR, 2022.


**W2:** Since the proposed method claims that the conventional BNTT is memory expensive, it is important to demonstrate the memory-accuracy comparison between the proposed method and BNTT (e.g., GPU Memory) 

**W3:** Some recent papers and SoTA methods are not cited in this paper: 

[R2]: Temporal Efficient Training of Spiking Neural Network via Gradient Re-weighting

[R3]: Differentiable Spike: Rethinking Gradient-Descent for Training Spiking Neural Networks, NeurIPS'21

[R4]: Training High-Performance Low-Latency Spiking Neural Networks by Differentiation on Spike Representation CVPR 2022

**W4:** The methodology section should be elaborated more. Based on Figure 1, S-TLLR introduces the incoming gradient $\partial L / \partial y$ on top of discrete STDP. What is the theoretical advantage (or intuition) of doing that?

### Questions
Please refer to Weaknesses

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces a new learning rule to train spiking neural networks. The idea is based on a three-factor structure, but using BPTT and STDP as its components. The STDP-based eligibility trace function scales with $n$ and is temporally local (does not scale with $T$), which is an improvement over existing methods. This method, referred to by the authors as S-TLLR, has an additional non-causal component which scales with $n$, just like the causal component, and therefore does not affect its scaling with space and time. Experiments and benchmarks on numerous datasets reveal the advantage of this non-causal learning component.

I am generally positive about this work in regards to the new proposed method and how it improves training of spiking networks. I hope that authors can clarify any misunderstandings I may have in the weaknesses section and I am very willing to adjust my score in the rebuttal.

### Strengths
The theoretical scaling advantage is highly relevant and important to the spiking neural network community. Using an STDP-based eligibility trace function also lends to biological plausibility, which has relevance to neuroscience audiences.

### Weaknesses
I am doubtful of both main claims, on (1) temporal locality and (2) improvements from non-causal terms.

(1) The temporal locality property of this method is unconvincing. In Figure 1, my naive understanding is that it is possible to simply truncate both BPTT and STDP methods in the same way S-TLLR is truncated using equation (11). In other words, all methods can have temporal locality. The only way to truly claim that the proposed method does not scale with time, is by using both BPTT and STDP (and perhaps even other existing methods) with this truncation and see if S-TLLR learns faster or if other methods fail to learn the objective. 

(2) The improvement from non-causal terms is similarly highly confounded by the secondary activation functions in equations (14-17). Suggestions for fair experiments could be:
- universally use the same secondary activation function across all tasks, or use all 4 activation functions for all tasks
- apply the same activation functions to other methods

To be very clear, I understand that S-TLLR is compared across different values of $\alpha$ within the same secondary activation functions, but it is not clear if this behavior is task and function specific. For example, dataset A and secondary function X could give better results with non-zero $\alpha$, while dataset B with secondary function X or dataset A with secondary function Y has better results with $\alpha = 0$. 

(3) It is also not clear how the method works in the recurrent neural network task. If I were to incorporate causal recurrent gradients in Figure 1, that would correspond to red lines being drawn from $u[t]$ to $y[t-1]$ (and others), which means most terms with have red and blue lines in parallel.  

(4) The recurrent term in equation (1), while true and makes the equation general, simply disappears and lacks coherence and continuity with all future equations where the narrative centers around a feedforward network. For example, equation (4) has no recurrent term. This should be stated in the text somewhere or removed.

### Questions
Should blue terms in Figure 1 also extend beyond $t-2$ (with three dots) just like the red terms?

While theoretical scaling arguments are convincing, there are many factors underlying number of computations. How are the 1.1x, 4x and 10x claims actually made? Was it done by recording the number of floating point operations? More information is needed to substantiate these claims. The actual amount of time taken to train the networks is also an important metric to include as well.

### Soundness
2 fair

### Presentation
3 good

### Contribution
1 poor
