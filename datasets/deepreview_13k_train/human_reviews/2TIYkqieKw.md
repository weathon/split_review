# DICE: Data Influence Cascade in Decentralized Learning

- Decision: Accept
- Scores: 6, 6, 6

## Abstract
Decentralized learning offers a promising approach to crowdsource computational workloads across geographically distributed compute interconnected through peer-to-peer networks, accommodating the exponentially increasing compute demands in the era of large models. However, the absence of proper incentives in locally connected decentralized networks poses significant risks of free riding and malicious behaviors. Data influence, which ensures fair attribution of data source contributions, holds great potential for establishing effective incentive mechanisms. Despite the importance, little effort has been made to analyze data influence in decentralized scenarios, due to non-trivial challenges arising from the distributed nature and the localized connections inherent in decentralized networks. To overcome this fundamental challenge, we propose DICE, the first  framework to systematically define and estimate Data Influence CascadEs in decentralized environments. 
DICE establishes a new perspective on influence measurement, seamlessly integrating self-level and community-level contributions to capture how data influence cascades implicitly through networks via communication. 
Theoretically, the framework derives tractable approximations of influence cascades over arbitrary neighbor hops, uncovering for the first time that data influence in decentralized learning is shaped by a synergistic interplay of data, communication topology, and the curvature information of optimization landscapes.
By bridging theoretical insights with practical applications, DICE lays the foundations for incentivized decentralized learning, including selecting suitable collaborators and identifying malicious behaviors.
We envision DICE will catalyze the development of scalable, autonomous, and reciprocal decentralized learning ecosystems.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper proposes the DICE framework for measuring the cascading propagation of data influence
in decentralized learning networks. Decentralized learning enables large-scale model training
through distributed computation, yet the lack of effective incentive mechanisms can lead to unfair
contributions and malicious behavior among nodes. The DICE framework introduces data influence
cascades (DICE-GT and DICE-E), which respectively measure the direct and indirect influence of data
within the network, addressing the limitations of existing data influence measurement methods in
decentralized environments. Experiments validate the consistency and accuracy of DICE across
various network topologies and demonstrate its potential in practical applications like anomaly
detection and collaborator selection

### Strengths
1. The DICE framework is the first to systematically measure the cascading propagation of data
influence in decentralized learning environments, providing an effective method to assess data
contributions among nodes and filling a gap in data influence evaluation within decentralized
networks.
2. The experiments cover different network topologies (such as ring and exponential graphs) and
datasets (such as MNIST, CIFAR-10, and CIFAR-100), validating the applicability and consistency
of the DICE framework across various scenarios.
3. The DICE framework provides accurate contribution measurement, laying the foundation for
designing fair and effective incentive mechanisms in decentralized learning systems, with the
potential to foster equitable collaboration within decentralized networks.

### Weaknesses
1. Figure 1 lacks legend information, making it difficult to understand.
2. The performance differences of the DICE framework under different parameters (such as learning rate, batch size, etc.) have not been thoroughly discussed. It is recommended to add parameter sensitivity experiments to demonstrate the impact of different parameter selections on the
performance of the DICE framework, thereby enhancing its practicality.

### Questions
See weaknesses

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes a method for quantifying the impact of data points in decentralized machine learning settings. The influence is measured not only at immediate neighbors but the entire network. This method can be useful for machine unlearning  or to develop new incentive mechanisms.

### Strengths
-  The paper is well-organized, with clear definitions, figures, and explanations that make the methods and results easy to follow.
- The paper provides a solid theoretical framework, supported by rigorous proofs and analyses.

### Weaknesses
 - Need for more details about the practical use of this technique: While the authors use LLMs as one of the examples in the introduction, it might not be the best example to use in this case. It hard to see how this research addresses a practical problem or application that has real-world significance, or how this framework would be relevant for practitioners.
- Link with other papers that use gradient to cluster clients should be added, particularly interesting and relevant in the collaborator choice part.  
- Experiments seem non-exhaustive and many details are missing to replicate the experiments. For instance, no indication on what the anomaly is vs normal client. This is particularly important when using gradients. I expect that the framework would perform differently if the anomaly is label flipping vs if it was noisy features. Additionally, evaluation of the impact of batch size would be particularly important for both scalability and compatibility among clients.

### Questions
1) Please motivate the approach with practical use-cases. 
2) Please discuss link with clustered federated learning, in particular techniques that use gradients to cluster clients. 
3) Please provide all necessary details to replicate the results.
4) Please evaluate the impact of batch size (smaller and larger values), to show the scalability of the technique and its robustness in showing the compatibility among clients.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes DICE as a framework for measuring data influence cascades in decentralized environments. The framework explains how data influence propagates through the communication network, emphasizing the interaction between the original data and the network structure in shaping data influence within decentralized learning. The experimental results show that the first-order approximation of the “gold standard” for evaluating data influence in decentralized environment can approaching the truth, and this framework can used for detecting mislabeled anomalies.

### Strengths
1. This paper summarizes previous work on measuring data influence and highlights the gaps in applying these methods to distributed scenarios.
2. This paper proposes a sound “gold standard” and its first-order approximation to quantify individual contributions in decentralized learning.

### Weaknesses
1. The experiments are weak, and Section 5.3 is unfinished.
2. The notation η^t in Theorem 1 is previously appears as η_t in Algorithm 1.

### Questions
Please see weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3
