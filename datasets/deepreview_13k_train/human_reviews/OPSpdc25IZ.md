# DS-LLM: Leveraging Dynamical Systems to Enhance Both Training and Inference of Large Language Models

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
The training of large language models (LLMs) faces critical computational cost challenges, hindering their scaling toward AGI and broader adoption. With model sizes doubling approximately every 3.4 months and training costs surging from 64 million USD for GPT-4 in 2020 to 191 million USD for Gemini Ultra in 2023, the economic strain is unsustainable. While optimizations like quantization provide incremental improvements, they fail to address the fundamental bottleneck. In this work, we propose DS-LLM, a novel framework leveraging dynamic system (DS)-based machines, which exploit Natural Annealing to instantaneously converge to minimum energy states, enabling orders-of-magnitude gains in efficiency. Unlike traditional methods, DS-LLM maps LLM components to optimization problems solvable via Hamiltonian configurations and utilizes DS machines' continuous electric current flow for hardware-native gradient descent during training. We mathematically demonstrate the equivalence between existing LLMs and DS-LLMs and offer a viable approach to build a DS-LLM from a trained conventional LLM. Evaluations using different sizes of models showcase orders of magnitudes speedup and energy reduction on both training and inference, while maintaining consistent accuracy. Furthermore, we provide detail analysis and discussion on the potential challenges and solutions of this emerging computing diagram, aiming to provide a solid foundation for future research.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces DS-LLM, a novel framework that employs Dynamical System (DS)-based machines to optimize the training and inference processes for Large Language Models (LLMs). By incorporating an electrodynamics-based model and a Natural Annealing process, DS-LLM dramatically reduces the computational costs associated with these models. The approach is mathematically and empirically validated, demonstrating significant speedups and energy reductions without sacrificing accuracy compared to conventional LLMs.

### Strengths
1. The paper pioneers the use of DS machines in the context of LLMs, leveraging their inherent Natural Annealing processes to optimize both training and inference, which is both novel and potentially transformative for the field.
2. The reported results show a 1,090× speedup and a 102,559× reduction in energy during training, along with a 127× speedup and a 37,545× reduction during inference. These improvements are substantial and address critical cost and efficiency barriers in LLM deployment.
3. The evaluation is thorough, with tests across multiple models and datasets demonstrating that DS-LLM achieves comparable accuracy to traditional LLMs. This thorough testing helps validate the practicality of the proposed approach.

### Weaknesses
1. While the paper demonstrates impressive theoretical and simulated results, the practical implementation of such systems might be challenging due to specialized hardware requirements. To better understand the feasibility, could you discuss specific hardware requirements, potential adoption challenges, and necessary adaptations to existing ML infrastructures for implementing DS-LLM? The discussion should include the types of materials needed for the DS machines, the precision requirements for manufacturing, and the expected cost scaling for larger systems. Furthermore, the paper should address the potential for integration with existing digital systems, considering the need for specialized interfaces and data conversion methods.
2. The paper discusses the theoretical and simulated benefits of DS machines but lacks concrete examples of these machines being implemented in real-world scenarios. The paper should include a discussion of the specific challenges in translating the simulated results to real-world performance, such as noise sensitivity, thermal management, and variations in component characteristics. It would also be beneficial to include a discussion of the current state of DS machine technology, including the maturity of fabrication processes and the availability of commercial components.

### Questions
1. Can you provide specific examples of Dynamical System-based machines being used in real-world applications? 
2. What are the main challenges in integrating DS machines with the existing computational infrastructures used for LLMs?
3. Could you provide more specifics about the Finite Element Analysis (FEA) software emulator used for the DS machine simulations? 
4. How closely do the results from the FEA simulations align with what you would expect from real hardware implementations? Are there any known discrepancies or performance variations between the simulated outcomes and actual hardware tests?

### Soundness
2

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
3

### Summary
This work proposes a method for mapping LLM inference and training to Ising machines (which the authors refer to as "dynamical system machines"). They build upon existing work that introduces a room temperature Ising machine built with CMOS technology and work that maps graph learning problems to these substrates. The resulting DS-LLM is orders of magnitude more energy efficient than conventional hardware.

### Strengths
The problem tackled in this paper—the energy consumption of LLMs—is both timely and well-motivated. The approach taken by the authors is unique and the results appear quite significant. The methodology is clearly explained despite covering a broad range of background fields.

### Weaknesses
 - Evaluation of inference improvements focus on a comparison against GPUs instead of low-precision, quantized implementations for edge devices. For example, comparing against low-precision CPU inference implementations (https://arxiv.org/pdf/2311.00502) or novel edge devices (https://arxiv.org/pdf/2409.15654, https://arxiv.org/pdf/2305.18691)
- There is no discussion of the possible limitations which is extremely relevant for ICLR readers as they may not be familiar with the hardware used in this paper. In particular, focus on scalability issues (like described in Question 1) or model flexibility issues (are there operations that would be difficult to map to the proposed substrate, and are all existing transformer variants mappable?).
- Small suggestion: the introduction would be clearer if the authors removed hyperbolic/unnecessary language surrounding the capabilities of natural annealing
    - e.g. Line 067: "Recently, Dynamical-System-based (DS) machines have emerged as a promising solution of such, which leverages nature itself as a computer!"
    - Paragraph on Lines 077-090 can be shortened as it mostly restates the previous paragraph with longer phrasing. Instead, simply state that no existing framework maps LLMs to DS machines, the prior work is specific to graph learning, and the difference in computation and scale between LLMs and graph learning poses a challenge for finding such a mapping.

### Questions
1. The prior work on NP-GL utilized relatively small graphs, resulting in circuits with 100s of nodes. This is not the case for a transformer model where the number of nodes is much larger. Is it possible to manufacture Ising machines at this scale? If not, would we need to rely on a multi-chip solution?
2. The description of back-propagation implemented on the Ising machine is not clear. What is computed by the auxiliary circuit and what is computed by the Ising machine? Is there a separate "reverse" network for computing gradients? If so, how are the reverse and forward networks kept aligned (typically referred to as the "weight transport problem" in brain-inspired learning settings)?
3. Does the time and energy evaluation refer to the total training / inference time over the full dataset or a single sample?
4. Does your proposed hardware solution perform training with batches? If not, wouldn't the total training time be prohibitive?

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
2

### Summary
This paper proposes a novel approach for constructing large language models (LLMs) using analog dynamic system (DS) machines, offering an alternative to conventional CMOS-based hardware. The authors present two methods for mapping existing Transformer-based models onto DS machines, thoroughly analyzing key components within Transformers to facilitate a complete transformation compatible with DS architecture. The proposed DS-based models achieve significantly faster training and inference times, along with notably reduced energy consumption compared to traditional CMOS-based systems.

### Strengths
* The paper introduces a creative application of analog DS machines for LLM construction, advancing research on energy-efficient AI model deployment.
* By analyzing and adapting key Transformer components for DS architecture, the authors provide a clear methodology for how LLMs can be mapped effectively, which contributes to the feasibility of DS-based machine learning.
* The substantial reductions in training and inference time and energy consumption demonstrate the practical advantages of DS machines over CMOS for LLMs.

### Weaknesses
 * The paper could benefit from a broader benchmarking analysis that includes different LLM sizes. 
* While DS machines are promising in terms of efficiency, their limitations (e.g., stability and precision constraints) are not fully discussed.

### Questions
* As LLMs scale up, are additional considerations or modifications necessary for DS machines to handle larger model architectures effectively?

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
2

### Summary
This paper proposes a novel approach to training and inference for large language models on dynamic systems, a new type of computing mechanism. Inference is facilitated through Hamiltonian configurations of the dynamic system machines, whereas training necessitates additional analog hardware for gradient computations. The authors assert that their approach yields substantial benefits in terms of speedup and energy reduction compared to traditional GPU-based methods.

### Strengths
(1) New computing paradigm. The authors explore the use of DS machines, a novel computing paradigm for both training and inference of large language models, a timely contribution given the substantial resources currently consumed by LLM pretraining.

(2) Significant gains. The authors claim 1000x speedups and 100,000x energy reduction for training while maintaining consistent model accuracy.

(3) Mathematically rigorous. Although the reviewer may not have understood every detail, the problem formulation of LLM inference into Hamiltonian and Natural Annealing in dynamical systems appears mathematically solid and promising.

### Weaknesses
 (1) **Lack of clear differentiation from prior work**: One of the major contributions of using dynamical systems for machine learning appears to be extremely similar to prior work [1]. The reviewer struggles to understand the significant differences and contributions of this work compared to [1], particularly given that some graph neural networks in [1] also employ attention mechanisms. A clearer explanation of the novelty and significance of this work is necessary. Specifically, the paper does not adequately articulate how the proposed mapping of LLM computations onto a Hamiltonian system fundamentally differs from prior efforts that also leverage dynamical systems for optimization or learning tasks. The core distinction between directly fitting data to a Hamiltonian, as in [1], versus mapping a pre-existing deep neural network architecture onto a dynamical system, needs to be more clearly defined. The paper should clarify whether the novelty lies in the specific mapping method, the use of a particular type of dynamical system, or a combination of both, and how this differs from prior work that also uses dynamical systems for machine learning.

(2) **Inadequate consideration of circuit non-idealities**: The training process relies on specialized analog circuits to achieve gradient calculations and backpropagation. However, analog circuits are prone to non-idealities such as thermal noise and non-linearity [2]. The authors seem to overlook these non-idealities and their potential impact on model accuracy. Furthermore, the exponential approximation using Taylor expansion in Section 3.3 lacks justification, and the choice of a 3rd-order expansion is not fully explained. The authors should provide more insight into how this choice affects model accuracy and hardware requirements. The paper should include a more detailed analysis of how these non-idealities, such as thermal noise, device mismatch, and non-linearities, would affect the accuracy and stability of the training process. The justification for using a 3rd-order Taylor expansion needs to be supported by experimental results or theoretical analysis demonstrating its sufficiency and the trade-offs between accuracy and hardware complexity. The paper should also discuss how the choice of a 3rd-order expansion affects the precision of gradient calculations and the overall convergence of the training process.

(3) **Limited analysis of model scalability**: The authors conduct analysis on model sizes of 124M, 355M, and 1.3B, but recent works have demonstrated the importance of scaling up model sizes, such as the 405B model in llama3. Can the authors provide more theoretical analysis or insight into how the speedups and energy consumption scale with the size of the models? The paper needs a more in-depth discussion of the practical limitations of scaling this approach to extremely large models. The analysis should include a discussion of how the required hardware resources, such as chip area and power consumption, scale with model size, and whether a single-chip implementation would be feasible for models with hundreds of billions of parameters. The paper should also address the potential communication overhead and synchronization challenges that would arise in a multi-chip implementation for large-scale models.

(4) **Unfair/Unclear comparisons**: The authors compare their energy calculations to A100 GPUs (800W), but the basis for the claimed 1000x speedup is unclear. Specifically, did the authors consider the latest techniques for fully utilizing GPU resources, such as vLLM[3]? Moreover, was batched inference used, considering that only 1.3B models were tested? It is unclear how/why this was not done, as four 40GB A100s would not be required for 124M models, for example. Especially in terms of LLM inference benchmarking, what is the comparision results on meaningful metrics, such as Time to First Token (TTFT),Token Generation Rate , and Energy in Token/KWh [4,5].? The paper needs to clarify the experimental setup used for the GPU comparisons, including the specific GPU model, software libraries, and optimization techniques employed. The paper should address whether the GPU performance was measured using optimized libraries like vLLM or a more basic implementation. The paper should also clarify whether batched inference was used for the GPU benchmarks, and if not, why not, as this would significantly impact the reported speed and energy consumption. The paper should also include a comparison on metrics such as Time to First Token (TTFT), Token Generation Rate, and Energy per Token, which are more relevant for evaluating the performance of LLMs.

### Questions
**Regarding novelty and differentiation from prior work**

1. Can you provide a detailed comparison of your work with [1], highlighting the specific contributions and differences in your approach?
How does your use of dynamical systems for machine learning improve upon or depart from existing methods, particularly those that also employ attention mechanisms?
2. What are the key advantages of your approach over prior work (and other emerging compute alternatives such as compute-in-memory), and how do you demonstrate these advantages in your experiments?

**Regarding circuit non-idealities**

1. How do you plan to address the potential impact of thermal noise and non-linearity in analog circuits on model accuracy?

2. Can you provide a justification for the exponential approximation using Taylor expansion in Section 3.3, and explain why a 3rd-order expansion was chosen?How does the choice of Taylor expansion order affect model accuracy and hardware requirements, and can you provide experimental or theoretical evidence to support your choice?

**Regarding model scalability**

1. Can you provide a theoretical analysis of how your approach scales with increasing model sizes, such as those demonstrated in recent works (e.g., 405B model in llama3)?How do you expect the speedups and energy consumption to change as model sizes increase, and what are the implications for hardware requirements? Can you provide additional experiments or simulations to demonstrate the scalability of your approach?

**Regarding comparisons and metrics**

1. Can you clarify the basis for the claimed 1000x speedup, and provide more details on the experimental setup and metrics used?

2. Did you consider using the latest techniques for fully utilizing GPU resources, such as vLLM[3], and if not, why not? Why was batched inference not used, particularly for smaller models (e.g., 124M), and how would this affect the energy calculations and comparisons with A100 GPUs?

3. In terms of LLM inference/training benchmarking, what is the comparision results on meaningful metrics, such as Time to First Token (TTFT), Token Generation Rate, and Energy (Token/KWh).

4. Can the authors also compare with (to a rough level) on dynamical systems with other emerging computing candidates (as introduced in the second paragraph of the introduction), such as quantum computing, optical computing, computing in memory etc? 

**Minor recommendations**: The abstract of the paper consists of 3 paragraphs and is quite long, can the authors abbreviate the abstract into a single paragraph to breifly explain the papers novelty and contributions?

### Soundness
2

### Presentation
3

### Contribution
2
