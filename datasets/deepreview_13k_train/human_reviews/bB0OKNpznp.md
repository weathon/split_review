# A Quantum Circuit-Based Compression Perspective for Parameter-Efficient Learning

- Decision: Accept
- Scores: 6, 6, 6, 6, 6

## Abstract
Quantum-centric supercomputing presents a compelling framework for large-scale hybrid quantum-classical tasks. Although quantum machine learning (QML) offers theoretical benefits in various applications, challenges such as large-size data encoding in the input stage and the reliance on quantum resources in the inference stage limit its practicality for tasks like fine-tuning large language models (LLMs). Quantum parameter generation, a novel approach of QML, addresses these limitations by using quantum neural networks (QNNs) to generate classical model weights (parameters) exclusively during training, thereby decoupling inference from quantum hardware. In this work, we introduce Quantum Parameter Adaptation (QPA) in the framework of quantum parameter generation, which integrates QNNs with a classical multi-layer perceptron mapping model to generate parameters for fine-tuning methods. Using Gemma-2 and GPT-2 as case studies, QPA demonstrates significant parameter reduction for parameter-efficient fine-tuning methods, such as Low-Rank Adaptation (LoRA), while maintaining comparable or improved performance in text generation tasks. Specifically, QPA reduces the number of  parameters to $52.06\%$ of the original LoRA for GPT-2 with a slight performance gain of $0.75\%$, and to $16.84\%$ for Gemma-2, with a marginal performance improvement of $0.07\%$. These results highlight QPA’s ability to achieve efficient parameter reduction without sacrificing performance in the quantum parameter generation framework. This work showcases the potential of quantum-enhanced parameter reduction, offering a scalable quantum-classical solution for fine-tuning LLMs while preserving the feasibility of inference on classical hardware.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors propose a novel quantum circuit-based algorithm, termed Quantum Parameter Adaptation (QPA), aimed at generating parameters for classical neural networks. This approach seeks to enable parameter-efficient learning of pre-trained deep learning models by reducing the number of training parameters while preserving model performance. Specifically, they utilize a quantum neural network with tunable parameters to produce a quantum state, whose amplitude under a specific basis is processed by a classical multi-layer perceptron to generate parameters with desired properties (e.g., low rank) for fine-tuning methods. Empirical experiments are conducted on two pre-trained models, Gemma-2 and GPT-2, demonstrating that QPA achieves significant parameter reduction for fine-tuning methods like Low-Rank Adaptation (LoRA), while maintaining or improving performance in text generation tasks.

### Strengths
1. The authors present the Quantum Parameter Adaptation algorithm, which innovatively applies quantum devices to train classical machine learning models. This exploration opens up a new paradigm in quantum machine learning, shifting the focus from using quantum circuits solely as learning models to leveraging them for generating parameters in classical models. This shift in roles between quantum and classical computers enhances the efficiency of classical-quantum hybrid algorithms.
2. The application of QPA to practical large-scale models such as GPT-2, resulting in improved performance and parameter reduction compared to traditional classical fine-tuning methods, is commendable.

### Weaknesses
1. The authors assert that one motivation for proposing QPA is to mitigate the high computational costs associated with existing fine-tuning approaches by reducing the number of parameters. However, extracting amplitude information from quantum states and training the quantum neural network can be highly computationally intensive due to the inherent challenges of quantum systems and the barren plateau phenomenon. This could introduce significant computational costs during each training epoch, making a fair comparison between QPA and classical fine-tuning methods difficult. Specifically, the process of performing quantum measurements to obtain the probability amplitudes, which are then fed into the classical MLP, adds a layer of computational overhead not present in purely classical methods. Furthermore, the optimization of the quantum circuit parameters, especially with increasing numbers of qubits, can be significantly more challenging than optimizing classical neural network parameters due to the complex landscape of the loss function in quantum systems.
2. Additionally, as I understand it from convergence theory, the number of parameters required for a quantum neural network to represent an arbitrary quantum state scales with the dimension of the quantum system, specifically $4^n$. Thus, to represent a parameterized quantum state for an arbitrary vector of dimension $r(d+k)$—the dimension of the low-rank weight matrix $\Delta W=BA$ —the quantum circuit would also need to have parameters on the order of $r(d+k)$. In this regard, QPA may not achieve any significant parameter reduction compared to completely classical fine-tuning methods. This is because the quantum circuit, in essence, needs to encode at least as much information as the low-rank matrix it is generating, which means that the parameter count in the quantum circuit will scale similarly to the size of the low-rank update matrix, negating the purported advantage of parameter reduction. The claim that QPA achieves parameter efficiency needs more rigorous justification, given this theoretical scaling.

### Questions
1. Could the authors provide experimental results comparing the performance of QPA with baseline methods while maintaining the same computational complexity?
2. Could the authors elaborate on the impact of the barren plateau phenomenon in the training of quantum neural networks, particularly concerning the optimization of large language models (LLMs) with 1 billion parameters, which necessitates a substantial number of qubits?

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
This paper introduces quantum parameter adaptation, a quantum parameter generation algorithm that uses quantum neural networks and classical multi-layer perceptrons to generate parameters to help fine-tune classical machine learning models.

### Strengths
Strengths:
   - Interesting idea (albeit one that has been done before to some extent) pushed further than in past work. Smartly gets around some of the known issues with QML, like the issue with expensive inference.
   - Brings related work closer to the forefront of classical ML by applying their method to Gemma-2 and GPT-2. 
   - Good use of MLPs and batching to reduce parameter counts.

### Weaknesses
Weaknesses:
   - Misleading claims about fault-tolerant quantum computation: The paper makes several misleading claims about fault-tolerant quantum computing (FTQC) which have the potential to make an uniformed reader think that universal FTQC is right around the corner. It’s not. For instance, the information in the second footnote is wrong. IBM has not demonstrated 12 logical qubits with 288 physical qubits. They’ve discovered a quantum error correcting code with that property. However, actually implementing that code in practice is going to be very hard! Moreover, running this paper’s parametrized quantum circuit (PQC) in a FT manner is going to be very expensive! The PQC requires small-angle Y rotations, which are extremely costly! The authors should more clearly address the challenges of implementing their approach with FTQC, including the overhead of error correction and the specific gate requirements.
   - No serious discussion of the impact of noise: The paper completely sidesteps the issue of noise. This is especially concerning when the approach is outperformed by classical competitors in the noiseless setting on certain problems. The authors need to provide a more detailed analysis of how their method performs under realistic noise models, and should consider how noise might affect the optimization landscape of the quantum circuit.
   - No theoretical performance guarantees. Not necessarily bad, but it’s not great when you don’t have amazing experimental results (the paper has no experimental results, just simulations). The lack of theoretical guarantees makes it difficult to assess the true potential of the method. It would be beneficial to include some analysis of the convergence properties of the quantum parameter adaptation algorithm, even if it is under simplified assumptions.
   - I am not sold at all on their approach to using synthetic data to get around the issue of having finitely many shots…generative models are expensive to train too! The authors should explore alternative methods for dealing with the finite measurement problem, or at least provide a more thorough justification for their choice of using generative models.


Some minor nitpicks:
   - It is an open question if quantum computing excels in optimization. Change the claim in your introductory paragraph, or at least soften it.
   - “This hybrid approach is especially promising in quantum machine
learning (QML), where it can enhance the training and fine-tuning of large models.” Also not evident that QML can help with the training or fine-tuning of large models. Isn’t that the whole point of this paper? Temper this claim.

### Questions
- Does this technique have any utility if you always need to perform a full strong simulation of the quantum circuits? Either because it is not robust to noise or because you can’t get away with finite measurements.
   - Have you tried running your method on actual quantum hardware? If not, why not?
   - How expensive would it be to implement your method in a fault-tolerant manner?
   - It is unclear to me how much this work pushes the sota forward. For instance, how does it differ from the other cited works? “Using the gradient computation and parameter update rule, the parameter generation process of QPA
has been applied to image classification with convolutional neural networks (CNNs) (Liu et al.,
2024b;a; Liu & Chen, 2024), flood prediction (time series) with long short-term memory (LSTM)
models (Lin et al., 2024), and policy gradient reinforcement learning in CartPole and MiniGrid
environments (Liu et al., 2024c).”
   - How expensive is it to update the gradient on real hardware?
   - What compute was used to produce the paper? What was the total wall clock time? How does that compare to the classical methods used?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposed quantum parameter adaptation (QPA), a method that combines quantum systems with classical models to enhance parameter-efficient fine-tuning in machine learning, especially for LLMs like GPT-2 and Gemma-2. Unlike traditional quantum machine learning methods that require quantum hardware for both training and inference, this approach uses quantum resources exclusively during the training phase to generate parameters for classical models, eliminating the need for quantum hardware at inference. This design enhances scalability and resource efficiency on classical hardware, addressing practical deployment concerns.

### Strengths
QPA achieves significant reductions in the number of trainable parameters required for fine-tuning LLMs while maintaining performance, making it highly relevant for parameter-efficient learning. This reduction makes the method resource-efficient and feasible for real-world application. In addition, the paper presents an elegant integration of quantum and classical computing. The authors demonstrate QPA’s effectiveness on state-of-the-art LLMs, contributing meaningfully to the rapidly advancing field of LLM research.

### Weaknesses
From my understanding, the quantum component of QPA does not appear to harness the inherent advantages of quantum machine learning. Since the quantum state must be fully characterized before classical post-processing, this process typically requires full quantum state tomography, involving an exponential number of measurements with respect to the number of qubits. This requirement is likely more computationally intensive than classical simulation, eliminating any quantum advantage. In this regard, QPA might better be described as a quantum-inspired algorithm rather than a quantum machine learning algorithm, as it does not appear to yield a speed-up or other quantum advantages over classical simulations. The authors themselves acknowledge in Appendix B that modeling the quantum state using a classical generative model could offer a more practical alternative. Furthermore, the method's reliance on full quantum state tomography, which scales exponentially with the number of qubits, presents a significant practical bottleneck. Even if the final parameters are used in a classical model, the training phase requires a computationally expensive quantum simulation, which undermines the practical benefits of the approach. The paper does not adequately address how to mitigate this exponential scaling, which is a critical issue for the scalability of the proposed method. The use of CNOT and RY gates further restricts the exploration of the full Hilbert space, limiting the potential of the quantum component.

### Questions
1.	Would the algorithm perform equally well if the quantum component were replaced with a classical system? Since the role of the parameterized quantum circuit here is to produce an intermediate hidden state, could a classical neural network serve as an alternative? Given the challenge of barren plateaus in quantum machine learning, a classical neural network might avoid these issues and potentially improve performance.
2.	Is there potential to reduce the need for full quantum state tomography in QPA? Could approaches like quantum shadow tomography, which require only partial measurement data, be used to extract sufficient information from the quantum state while reducing computational costs?
3.	The current parameterized quantum circuit design relies on CNOT and RY gates, which restrict the quantum state to real values and consequently limits the Hilbert space it explores. Have the authors experimented with more complex circuits to explore the full Hilbert space, and if so, does this yield performance improvements?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces Quantum Parameter Adaptation (QPA), a novel approach for parameter-efficient learning that combines quantum neural networks (QNNs) with classical machine learning to generate parameters for fine-tuning large models. The QPA method utilizes quantum circuits to generate classical model weights, allowing for significant parameter 
reduction without compromising performance, as demonstrated with Gemma-2 and GPT-2 case studies. The method enables practical use of quantum machine learning by decoupling quantum hardware requirements from the inference phase, thus making inference feasible on classical systems. The results show that QPA can effectively reduce the number of parameters required for methods like Low-Rank Adaptation (LoRA), while maintaining or improving model performance, indicating its potential as a scalable and efficient quantum-classical hybrid solution for large-scale learning tasks.

### Strengths
1. The paper proposes the Quantum Parameter Adaptation (QPA) method, which is a new method that combines  quantum neural networks (QNN) with classical multi-layer perceptrons to generate The parameters of the fine-tuning method demonstrate the efficiency in parameter reduction. 
2. QPA separates quantum computing from the inference stage, allowing the model to perform inference without  relying on quantum hardware, greatly reducing deployment complexity and thus having practical application value for classical hardware inference. 
3. Experimental results show that QPA can significantly reduce the number of parameters while maintaining or slightly improving model performance. In contrast, methods such as LoRA, DoRA,  and Prefix Tuning (PT) are highly efficient in parameters. The performance in learning tasks is not as good as QPA, highlighting its high efficiency. 
4. The authors extend the QPA method to large models such as GPT-2 and Gemma-2, significantly expanding the scope of previous quantum parameter generation studies. 
5. QPA allows flexible exploration of different parameter configurations, improving its 
adaptability in different models and parameter efficient fine-tuning (PEFT) methods.

### Weaknesses
 1. The study assumes that the measurement probability is exact and does not consider noise, which may not accurately reflect the situation where a finite number of measurements are required in the actual quantum hardware environment. Although the impact of this limitation on performance is discussed, the problem is not completely solved. It is possible to consider introducing some simulated noise models to verify the robustness of the proposed QPA.
2. The paper mentions that QPA uses RY and CNOT gates to build quantum circuit ansatz, but lacks a detailed explanation of why this ansatz structure is chosen. It is recommended that the author add a detailed argument for the choice of ansatz and compare the effects of different quantum gate combinations to ensure the rationality of the current choice.
3. The method uses the gradient obtained from quantum measurements, which may introduce additional complexity in the training process, especially when implemented on actual quantum hardware, due to the presence of parameter offsets and measurement noise.
4. The paper mentions that the theoretical analysis of the convergence behavior, trainability and learnability characteristics of QPA will be addressed in future research, which shows that there is a gap in the current understanding of the long-term effectiveness of QPA.
5. More shortcomings can be found in the Questions section.

### Questions
1. Lack of comparison with other rotation gates: The author mainly chose the combination of RY gate and CNOT gate, but there is a lack of detailed comparative analysis in the article. Why is the RY gate more suitable for this specific task, while the RX and RZ gates are not good enough? The author needs relevant experiments to verify the advantages of the RY gate over other gates.
Rationality of the selection of rotation gates: RX, RY and RZ gates are all single-bit rotation gates, why does RY have a better effect in this scenario? Is there a clear mathematical or experimental basis to show that the efficiency and effect of the RY gate in quantum parameter generation is better than RX or RZ? If not, does this mean that the author's choice of the RY gate is more based on experience rather than theoretical support?
2. Performance in noisy environments: Although the RY gate is considered to perform better in capturing the rotation characteristics of quantum states, quantum hardware has noise and errors in actual operation. Have you compared the robustness of different rotation gates in actual quantum hardware? Especially when considering quantum noise, is the RY gate still the best choice? At the same time, the performance of QPA in actual quantum hardware remains to be considered.
3. Lack of discussion on time complexity: Although QPA performs well in reducing the number of parameters, the paper lacks a detailed discussion on the running time of the quantum circuit when generating parameters. Does the generation and measurement process of the quantum circuit bring additional time overhead? Does this additional time complexity offset the improvement in training efficiency brought by parameter reduction?
Compared with the classical PEFT method, is there a significant time overhead in the process of QPA using quantum circuits to generate parameters? Do these differences have a significant impact on the practical application of models at different scales? In practical applications, the time efficiency of the model is one of the important considerations. Even if the number of parameters is reduced, if the time complexity of the quantum circuit is high when generating parameters, this may affect the efficiency and scalability of the overall system. The author should provide more quantitative analysis to evaluate the overall cost-effectiveness of the QPA method in terms of time and computing resources.

4. In more complex scenarios, how does QPA compare to traditional QML methods? : The paper shows the efficiency of QPA in reducing parameters of large models such as GPT-2 and Gemma-2. However, how does QPA perform when extended to larger models such as GPT-3 or larger? Does quantum parameter generation encounter scalability issues in such scenarios?

5. Best choice of parameter configuration: How to determine the best block size (nmlp) and number of QNN repetitions (L) for different PEFT methods? Is there a general method to determine these hyperparameters for other models?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents a novel approach for quantum parameter generation aimed at providing a quantum-classical solution for fine-tuning LLM's parameters.  Authors conduct simulation on benchmark datasets to assess performance compared to traditional fine-tuning techniques like LoRA and DoRA. Results indicate improvements in reducing the number of parameters while maintaining or surpassing the performance of existing PEFT methods.

### Strengths
The authors introduce an new framework that aims to bridge the gap between classical machine learning and quantum computing.

### Weaknesses
1. Efficiency Concerns: The proposed quantum parameter generation method, while designed to reduce the need for quantum hardware during inference, still relies heavily on quantum neural networks (QNN) during training. This raises critical questions regarding the efficiency of the overall process. Specifically, the optimization of quantum neural network parameters is prone to challenges such as barren plateaus, which can significantly hinder the training process. The authors do not sufficiently address how these issues may impact the efficiency of fine-tuning parameters of classical large models, particularly given the complexities associated with high-dimensional optimization landscapes typical of QNN.

2. The inputs of the mapping model necessitates a precise value of the corresponding measurement probabilities of the basis of quantum states. Typically, these probabilities can only be approximated through repeated measurements and averaging, which introduces another layer of complexity. The need for multiple measurements raises concerns regarding the time overhead involved. The paper does not adequately discuss the potential delays that may arise from extensive measurement requirements, especially in the context of noisy intermediate-scale quantum (NISQ) devices where measurement fidelity can be compromised by inherent noise. Furthermore, the implications of limited measurement shots on the accuracy of estimated probabilities and the subsequent effect on LLM's fine-tuning are not sufficiently explored.

Although the authors mention the limitations of finite measurement shots in Appendix B, the reviewer believes that providing sufficient experimental results, including finite measurements and noise-affected simulations, is essential for demonstrating the feasibility of the proposed method in the paper.

### Questions
Reviewer would be grateful if the authors could discuss the following: 

Given that the primary idea of this paper aims to leverage the exponential dimensionality of quantum states to represent the parameter space of LLMs. There exists a parallel in tensor network [1,2] theory that serves a similar purpose: the most successful application of tensor networks in physics has been to approximate exponentially large vectors arising in quantum mechanics.
 
The question is that might it also be feasible to explore the application of tensor network's theories and methodologies as an alternative to the currently resource-constrained and large-scale unavailable quantum computing? 

Additionally, could the authors utilize certain theoretical insights (e.g. from tensor network research) to investigate why the proposed method achieves superior performance compared to traditional fine-tuning techniques such as LoRA and DoRA, rather than relying solely on empirical evidence? 

This discussion could significantly enhance the theoretical underpinnings of the paper and provide a more robust framework for understanding the advantages of the proposed approach.

[1] Stoudenmire E, Schwab D J. Supervised learning with tensor networks[J]. Advances in neural information processing systems, 2016, 29.

[2] Liu Z, Yu L W, Duan L M, et al. Presence and absence of barren plateaus in tensor-network based machine learning[J]. Physical Review Letters, 2022, 129(27): 270501.

### Soundness
2

### Presentation
3

### Contribution
2
