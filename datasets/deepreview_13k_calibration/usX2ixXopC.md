# Measurement information multiple-reuse allows deeper quantum transformer

- Decision: Reject
- Avg Score: 4.00
- Scores: 5, 3, 5, 3

## Abstract
The current era has witnessed the success of the transformer in the field of classical deep neural networks (DNNs) and the potential of quantum computing. One naturally expects that quantum computing can offer significant speedup for the transformer. Recent developments of quantum transformer models are faced with challenges including the expensive cost of non-linear operations and the information loss problem caused by measurements. To address this issue, this paper proposes a scheme called measurement information multiple-reuse (MIMR). MIMR enables the repeated utilization of intermediate measurement data from former layers, thus enhancing information-transferring efficiency. This scheme facilitates our quantum vision transformer (QViT) capable of achieving exponential speedup compared to classical counterparts, with the support of many parameters and large depth. Our QViT model is further examined with an instance of 86 million parameters, which halves the requirements for tomography error compared to the one without MIMR. This demonstrates the superior performance of MIMR over existing schemes. Our findings underscore the importance of exploiting the value of information from each measurement, offering a key strategy towards scalable quantum deep neural networks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents a method for leveraging quantum circuits and their properties to enhance the performance of transformers on a quantum computer. The authors additionally propose utilizing mid-circuit measurements, which serve as a quantum analogue to deep residual connections, as a strategy to construct deeper quantum circuits.

### Strengths
1. Fair story and reasonable thought to replace traditional network module operations with quantum gates.
2. Use quantum gates to enhance computational efficiency within transformer architectures.
3. Leverage mid-circuit measurement information to construct deeper quantum transformers.

### Weaknesses
1. Lack of Novelty: The approach of replacing mathematical operations with quantum gates is not novel, as this concept has been widely explored and documented, notably in the qBLAS library. The paper does not present significant innovation beyond these existing approaches, which diminishes its contribution to the field.

2. Limited In-depth Consideration: While the authors propose using residual connections within quantum circuits—an idea inspired by classical neural network architectures—this adaptation requires more critical evaluation. In classical settings, residual connections support the training of deeper models; however, applying this concept to quantum circuits entails significant challenges. Specifically, implementing residual connections in quantum circuits would necessitate re-preparing the quantum states following mid-circuit measurements, which imposes a substantial computational burden. This could potentially negate the speed advantages typically offered by quantum computing. The primary challenge, as acknowledged in quantum computing literature, for training deep quantum circuits relates to the fact that deeper quantum circuits can approximate more easily Haar random quantum states.

Additionally, the concept of residual connections within quantum circuits has already been explored, as evidenced in [1]. The paper would benefit from a clearer discussion of how its approach differs from or builds upon prior work in this area.

### Questions
Could you provide a more detailed theoretical explanation on how this approach might enable the training of deeper models within a quantum framework, despite the additional requirements for state re-preparation? This clarification would strengthen the justification for the proposed method.

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper proposes a measurement information multiple-reuse (MIMR) strategy to enhance quantum transformer models, specifically developing a quantum vision transformer (QViT). The MIMR method addresses limitations in quantum deep neural networks by reusing intermediate measurement information across layers, which mitigates information loss and improves efficiency in both forward pass and backpropagation.

### Strengths
1. The introduction of the MIMR scheme addresses a key bottleneck in quantum deep learning—information loss due to limited intermediate measurements. By reusing measurement information, the paper offers a fresh solution to build deeper quantum neural networks.

2. This work did a lot of experiments in image classification. It shows their method's effectiveness in such a task. This practical focus adds value to the proposed method, as it directly showcases the model's utility.

### Weaknesses
1. In this paper, the authors state that they are proposing a quantum transformer. However, as far as I understand, what they are proposing is a hybrid quantum-classical transformer. As Figure 2 shows, the method keeps converting the tensor between quantum and classical states. Therefore, authors may make this more clear and precise. Specifically, the frequent conversions between quantum and classical representations raise concerns about the true quantum nature of the computation. The authors should clarify the proportion of computation that is genuinely quantum versus classical, and whether the quantum components offer a demonstrable advantage over classical equivalents given the overhead of these conversions.

2. The method keeps converting the tensor between quantum and classical states. Will such conversions be time-consuming? This concern is not adequately addressed by simply stating that the $l_{\infty}$ sampling algorithm is used. The practical overhead of these conversions, including the sampling process and the classical processing of sampled data, needs to be quantified and compared to the computational cost of the quantum operations themselves. It's unclear if the claimed logarithmic scaling of the sampling algorithm is sufficient to offset the overall cost of these conversions.

3. In this work, the authors did not implement their method on a real quantum computer. There are a lot of quantum computers available for use, such as the IBM Quantum Cloud Platform (IBM-Q). It is not clear how the authors implemented QVit. It looks like they are just doing the simulation instead of running the method on the actual quantum machine, but it is not clear how the simulation is implemented. The lack of experimental validation on actual quantum hardware is a significant limitation. The simulation details are vague, and it's unclear if the simulation accurately captures the nuances of quantum hardware, such as gate errors and decoherence. Without such validation, the practical relevance of the proposed method remains questionable.

4. In quantum computing, the quantum noise is a very critical problem. However, there is no discussion about the quantum noise. This problem is significant when converting the tensors from a quantum state to a classical state. The absence of any discussion on quantum noise is a major oversight. The conversion from quantum to classical states is particularly susceptible to noise, which can significantly degrade the accuracy of the computation. The authors need to address how their method handles or mitigates the effects of quantum noise, especially during the measurement and sampling processes.

5. Authors use pre-trained QViT, but it is not clear which dataset was used for pre-trianing. This lack of transparency regarding the pre-training dataset hinders reproducibility and makes it difficult to assess the generalizability of the results. The authors should clearly state the dataset used, its size, and any preprocessing steps applied.

6. The application is limited. Only image classification is discussed. Since it is about the transformers, the application in language processing is also important. The narrow focus on image classification limits the impact of the work. Given the versatility of transformers, the authors should discuss the potential of their method for other applications, such as natural language processing, and provide some preliminary results or at least a theoretical discussion on how it could be adapted.

### Questions
1. Are you running the simulation? Can you please make it more clear that how do you implement the network? Have you used Qiskit or another quantum library?

2. The method keeps converting the tensor between quantum and classical states. Will such conversions be time-consuming?

3. How does the quantum noise affect this work? How do you reduce the effect of the quantum noise?

4. Which dataset is used for pertaining?

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors provide a multiple-resued mechanism to mimic the residual connections. Based on this, the author constructed a Vision Transformer model with large parameters and representation power. The model's performance shows that training a large and deep quantum neural network becomes possible using this technique.

### Strengths
The paper is well written in narrative. The diagrams are clear and the background introduction is concise.

### Weaknesses
A review of the current method is lacking. In recent years, the research about quantum transformers and the mimicking of residual connections in quantum neural networks have been boosted. For example:
https://arxiv.org/abs/2406.04305
https://arxiv.org/abs/2209.08167
https://researchportal.hbku.edu.qa/en/publications/resqnets-a-residual-approach-for-mitigating-barren-plateaus-in-qu

Therefore, the novelty of this work is subtle.

### Questions
1. Please add some related work about residual connections in quantum neural networks.

2. Could you explain the difference between the "Multiple reuse" strategy with the available quantum residual connection implementation?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper introduces quantum vision transformers (QViTs), an implementation of vision transformers on fault-tolerant quantum computers, leveraging quantum tools for linear algebra. The implementation details follow somewhat Kerenidis et al [1], which introduces a similar scheme, but applying to quantum convolutional neural networks instead.

In addition to the implementation of QViTs, the authors propose a scheme called measurement information multiple-reuse (MIMR). In [1]  the measurement of one quantum layer is passed to the next quantum layer to allow for information sharing between quantum layers. This current work proposes that the measurement of all previous layers is provided as an input to all subsequent quantum layers.

The authors investigate the impact of MIMR on mitigating tomography errors across a range of benchmarks, investigating both the output of quantum layers vs baselines with no tomography error and also the overall accuracy of the resulting architectures. 

[1] [Kerenidis et al, ICLR 2025](https://iclr.cc/virtual_2020/poster_Hygab1rKDS.html)

### Strengths
1. The implementation of MIMR is new, to my knowledge.
2. MIMR seems to provide performance benefits compared to single-information reuse.
3. The authors provide a detailed appendix including basics on quantum computing and discussions on implementation of individual layer forward and backward passes.

### Weaknesses
1. The query complexity presented in Theorem 3.1 can be better discussed and investigated. As written in the main text, the quantum query complexity goes as $O(ld^2\mathrm{polylog}(n)/\epsilon\delta^2)$ whereas classical goes as $O(lnd(n+d)\mathrm{log}(1/\epsilon))$. The text is quick to point out the quantum advantage in $n$, but does not fully discuss the quantum disadvantage at small values of $\epsilon$ and $\delta$. In practice, in remains unclear whether a QViT will be operating in the limit of large $n$, or small $\delta$ or $\epsilon$. These points are not discussed sufficiently nor investigated numerically. Consequently, the motivation for QViTs seems speculative at this stage.
2. The title, which states that MIMR allows for deeper quantum transformers, seems unjustified. Experiments are done with respect to different degrees of tomography errors, and do not vary depth.
3.  Experiments seem to only be conducted for a single random seed. It would be better to provide several runs of each experiment and present means and standard deviations or similar.
4. The benefit of MIMR is seemingly at very specific range of range of values: at $\delta=0$, single-reuse and multiple reuse are presented as identical. At $\delta=0.004$, multiple reuse performance also breaks down. It seems that the specific values at which MIMR might provide a benefit are $\delta \in \{0.002, 0.003\}$. Results for $\delta=0.001$ are not presented. This seems a particularly narrow range compared to the [work that establishes $l_\infty$ tomography](https://iclr.cc/virtual_2020/poster_Hygab1rKDS.html), which considers values of $\delta$ up to $0.1$.
5. The motivation of the work remains unclear. Since it relies on a host of quantum technologies not currently convincingly implemented (QRAM, amplitude encoding, $l_\infty$ tomography). Convincing error mitigation is currently not even demonstrated despite having been the subject of intense research. The techniques required seem even more involved: it seems quite plausible that transformers might not be of research interest by the time (if ever) this architecture is practically implementable on a real device.

### Questions
Suggestions:
1. Run experiments over multiple random seeds and report aggregated performance metrics.
2. An investigation over a wider range of $\delta$ would be beneficial to demonstrate the efficacy of MIMR. For example, [Kerenidis 2020](https://iclr.cc/virtual_2020/poster_Hygab1rKDS.html) considers values of $\delta=0.01$ and $\delta=0.1$. The range of values in this work seem small in comparison, and thus seem to be operating closer to a regime where the quantum advantage over classical in query complexity is diminished.
3. Provide a fuller discussion on where quantum might have an advantage over classical for QViTs, explaining clearly the tradeoffs between $\epsilon$, $\delta$ and $n$.
4. The long-term view of such quantum models should be made clear to ICLR readership, who are likely not quantum computing specialists. It is unclear when (or even if) tools like QRAM, tomography and amplitude encoding might be available on a practical device.
5. The idea of MIMR seems applicable to multiple architectures. Choosing to demonstrate it on a lightweight architecture and a simpler task seems to me to provide better opportunity to fully investigate its efficacy. By the time quantum computers can implement QViTs as presented, I think it's likely that the ML research community might have moved past transformers anyway. I appreciate this is a major change which is likely not implementable during the review period, but I do believe it would lead to a stronger and more general piece of work, in that it would allow MIMR to be presented as a general strategy as opposed to one pertaining to QViTs.
6. If stating that MIMR allows for deeper transformers, then there should be some numerical results with various transformer depths demonstrating the positive impact of MIMR vs single reuse.

### Soundness
2

### Presentation
2

### Contribution
2
