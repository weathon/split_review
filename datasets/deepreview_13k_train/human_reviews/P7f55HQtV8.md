# QuaDiM: A Conditional Diffusion Model For Quantum State Property Estimation

- Decision: Accept
- Scores: 6, 8, 6, 6

## Abstract
Quantum state property estimation (QPE) is a fundamental challenge in quantum many-body problems in physics and chemistry, involving the prediction of characteristics such as correlation and entanglement entropy through statistical analysis of quantum measurement data. Recent advances in deep learning have provided powerful solutions, predominantly using auto-regressive models. These models generally assume an intrinsic ordering among qubits, aiming to approximate the classical probability distribution through sequential training. However, unlike natural language, the entanglement structure of qubits lacks an inherent ordering, hurting the motivation of such models. In this paper, we introduce a novel, non-autoregressive generative model called \textbf{QuaDiM}, designed for \underline{\textbf{Qua}}ntum state property estimation using \underline{\textbf{Di}}ffusion \underline{\textbf{M}}odels. QuaDiM progressively denoises Gaussian noise into the distribution corresponding to the quantum state, encouraging equal, unbiased treatment of all qubits. QuaDiM learns to map physical variables to properties of the ground state of the parameterized Hamiltonian during offline training. Afterwards one can sample from the learned distribution conditioned on previously unseen physical variables to collect measurement records and employ post-processing to predict properties of unknown quantum states. We evaluate QuaDiM on large-scale QPE tasks using classically simulated data on the 1D anti-ferromagnetic Heisenberg model with the system size up to 100 qubits. Numerical results demonstrate that \model outperforms baseline models, particularly auto-regressive approaches, under conditions of limited measurement data during training and reduced sample complexity during inference.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes QuaDiM, a new framework based on diffusion models that learns the ground state of quantum systems conditioned on system parameters and enables quantum property estimation. QuaDiM uses a transformer-based architecture, where at inference time, measurement outcomes are first generated as continuous-valued hidden vectors and then decoded into discrete values. Numerical experiments are performed on 1D anti-ferromagnetic Heisenberg model up to $100$ qubits and predicted properties include correlation and entanglement entropy.

### Strengths
* The paper is very readable, with clear and understandable notations and easy-to-follow reasoning across the paper.
* The proposed methods achieve SOTA performance on predicting correlation and entanglement entropy on 1D anti-ferromagnetic Heisenberg model with a reasonably large system size, justifying the effectiveness of the proposed approach.

### Weaknesses
 * While the motivation for using non-autoregressive models is briefly discussed in the introduction, there could be more discussion and empirical evidence to support the claims about the sub-optimal performance of auto-regressive methods. While the measurements are not like language, the underlying physics model can still have some order structure (like a chain) and locality information is often important. Therefore, it's not completely obvious why diffusion models are necessarily better. Specifically, the paper lacks a detailed analysis of how the pre-defined factorization order in autoregressive models affects their ability to capture long-range correlations and entanglement, especially given the chain-like structure of the Heisenberg model. A more thorough comparison, perhaps by varying the factorization order in autoregressive models and observing its impact on performance, would strengthen the argument for diffusion models.
* QuaDiM lacks machine learning technical novelty. The conditional diffusion model are already well studied in the literature and the used score neural network seems to be standard transformer as well. Given that ICLR is a ML conference, it would be more interesting to see applications and inspiration that can be drawn from QuaDiM to more general problems. The paper does not explore the potential of QuaDiM to address more general machine learning tasks beyond quantum property estimation. For instance, it would be interesting to see if the learned latent representations could be used for transfer learning or other downstream tasks in different domains.
* The experimental setup are not clearly presented. For example, the generation protocol of system parameter $x \in \mathbb{R}^{L - 1}$ is not described in the experiments section, not to mention the training and test set splitting process. This makes it hard to understand under what level QuaDiM extrapolates to "unseen parameters". The paper needs to provide more details on how the system parameters are generated, including the specific distribution used and the range of values. Additionally, the splitting of the dataset into training and testing sets should be clearly defined, including the number of samples in each set and whether the test set represents a true out-of-distribution scenario.
* The experiment design is relatively weak. It would be interesting to consider more complicated property estimation problems, such as the estimation of entanglement negativity, two site observables with long ranges in between, or even the estimation of system parameters in the Hamiltonian. Second, it would be more convincing if QuaDiM is examined on a more complicated physics model, such as some with non-trivial long-range entanglement. It would be more convincing if the extrapolation of QuaDiM to critical state of the physics model could be tested and examined. The current experiments focus on relatively simple properties of the 1D Heisenberg model. The paper should explore more complex properties, such as entanglement negativity or long-range correlation functions, to demonstrate the full potential of the proposed method. Furthermore, testing the model on more complex quantum systems with long-range entanglement or near critical states would provide a more rigorous evaluation.
* The benchmarks are not representative enough. For example, [1-3] are also works that model quantum states that should enable property estimation as downstream tasks, but are not discussed or compared.

### Questions
* Can you discuss more on in what cases diffusion models would be strictly better than auto-regressive models, in the quantum state modeling setting?
* I am not completely clear on how continuous latent vectors generated by QuaDiM are decoded back into measurement outcomes. Can you elaborate more on this?
* Why QuaDiM will generate measurements consistently sampled from a valid quantum state without violating structure constraints. How is this enforced in the learning algorithm?
* Does QuaDiM extrapolate to unseen system parameter $x$ distribution, likely with disjoint support as the training distribution, e.g., trained on $x \in [0, 0.8]$, tested on $x \in [0.9, 1]$?
* Can you comment on QuaDiM's training efficiency? First, it seems that a relatively large $M_{in}$ is required for learning one ground state to good accuracy, also $M_{out}$ is not a small number as well. Can $M_{in}$ and $M_{out}$ be improved? Second, how many distinct pairs of (ground state, measurements) are needed for learning the mapping between Hamiltonian parameter and system ground state correctly, and how does this scale with the number of qubits?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces QuaDiM, a non-autoregressive diffusion model for quantum state property estimation (QPE). Unlike traditional autoregressive approaches that impose a (potentially biased) sequential ordering on qubits, QuaDiM treats all qubits equally through an iterative denoising process. The model is evaluated on the 1D anti-ferromagnetic Heisenberg model for systems up to 100 qubits, demonstrating superior performance in predicting correlation and entanglement entropy compared to baseline methods, especially with limited measurement data.

### Strengths
1. The proposed method of using diffusion model for quantum state tomography is novel. The paper effectively adapts diffusion models to quantum systems by introducing a token embedding function that maps discrete measurement outcomes to continuous features, allowing seamless integration with the diffusion process.
2. The method seems to scale well to large systems. The model demonstrates strong performance on systems up to 100 qubits, which is significant for quantum computing applications.

### Weaknesses
1. While the paper mentions T=2000 denoising steps, there's no ablation study on how the number of steps affects performance versus computational cost.
2. The paper fixes the embedding dimension at d=128 without analyzing how different dimensions affect the model's performance and computational requirements.
3. The paper only considers Pauli-6 POVM, while evaluations on other POVM measurements may be beneficial. Specifically, the choice of Pauli-6 POVM, while convenient for implementation on NISQ devices, may not be the most informative for all quantum states, and the model's performance with other POVMs should be investigated to assess its robustness and generalizability.
4. Although the authors made reasonable efforts, it is unclear to non-physicists how wave functions become probability distributions. Adding a section in the appendix discussing POVM measurements is preferable.

### Questions
1. How does the choice of diffusion schedule (β_t values) affect the model's performance? Would adaptive scheduling improve results?
2. The paper uses Pauli-6 POVM measurements. How would the model perform with other measurement bases, and could this be made basis-independent?
3. Could the authors comment on if the model can be used to obtain the log probabilities of each measurement outcome?
4. POVM probabilities can be non-physical. Does the model always learn physical solutions?
5. Could the model be modified to predict other quantum properties beyond correlation and entanglement entropy? What architectural changes would be needed?

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
This paper addresses the challenge of Quantum state property estimation (QPE) in quantum many-body physics, focusing on predicting characteristics like correlation and entanglement entropy from measurement data. The authors introduce QuaDiM, a non-autoregressive generative model using diffusion models, which avoids the need for an intrinsic qubit ordering and treats all qubits equally and unbiasedly. QuaDiM learns to map physical variables to ground state properties during offline training and can sample from learned distributions for unseen variables to predict unknown quantum states. Empirical results on the 1D anti-ferromagnetic Heisenberg model with up to 100 qubits show that QuaDiM outperforms baseline models, particularly auto-regressive approaches, under limited training data and reduced inference sample complexity.

### Strengths
I am not an expert in quantum physics, so I can only provide my insights from the perspective of general generative models.

First of all, the paper provides empirical evidence that models like diffusion models, which can capture the correlations between qubits, can outperform sequential-based models such as transformers and RNNs. This observation is an important finding in itself and can potentially steer research focus in the relevant AI4Science area.

### Weaknesses
As mentioned earlier, I would like to raise some concerns from a generative model perspective:

Figure 3 is not informative to me; I can barely discern any difference between QuaDiM and LLM4QPE visually.

Based on Figure 2, the methodological novelty appears limited.

Could you please provide details about the computational resources used for the experiments? For example, the number of GPUs used, the training time, and the model size.

It would be beneficial if the authors could provide the standard deviation over seeds in Tables 1 and 2.

Minor typo:

Line 72: there is a double 'the'.

### Questions
Please correct me if I was wrong in terms of my previous comments :)

### Soundness
3

### Presentation
3

### Contribution
1

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes Quantum State Property Estimation using Diffusion Models (QuaDiM), a conditional diffusion model designed to learn and generate distributions of quantum states and accordingly quantum properties, for a given Hamiltonian parameter, from measurement data. Traditionally, auto-regressive models have been used for this task, modeling the quantum state array as a sequential structure despite the lack of inherent sequential ordering in quantum states. Unlike these approaches, QuaDiM denoises and shapes all states in the array simultaneously, as is typical in diffusion models, allowing it to effectively capture non-sequential interactions between spatially separated states. The proposed structure essentially includes an embedding that allows discrete quantum states to be treated as continuous diffusive evolution within a (conditional) diffusion model. The authors validate that the proposed QuaDiM outperformed existing main models, including RNN-based models and LMM4QPE, for large-scale quantum problems (e.g., L = 100).

### Strengths
- The proposed QuaDiM outperforms the baselines based on sequential models, e.g., RNN-based and transformer-based ones. It is intriguing, especially to handle very large-scale quantum states (e.g., L = 100) as a benchmark. 

- The paper is generally well-written.  I am not an expert in quantum computing, but I was able to follow this paper well and found it interesting to read.

### Weaknesses
 - This paper is essentially an application paper that applies a diffusion model combined with a text embedding structure to the task of quantum state property estimation. It effectively addresses an interesting topic in the field of quantum computing through appropriate structural selection; however, it is uncertain whether this topic is broadly interesting to the ICLR audience.

- I am not fully convinced why a diffusion model is the most suitable choice for the (non-sequential) quantum property estimation task. To me, this task fundamentally seems to be manageable by other generative models, such as conditional VAEs, GANs, or energy models. The authors mention that these generative models can only handle a single specific quantum state and cannot generalize to unseen states, but I am curious why a diffusion model is capable of generalizing to unseen states. While it is true that diffusion models demonstrate superior performance in terms of both fidelity and diversity, achieving high performance for diffusion models generally requires a large amount of training data. Therefore, the authors would clarify why the proposed QuaDiM would be particularly beneficial for quantum state property estimation, compared to other generative models, in a practical setting (e.g., limited observation as the authors mentioned).

- The authors claim that the primary motivation behind the proposed QuaDiM model is to eliminate the sequential handling of quantum states present in existing models. However, QuaDiM employs an embedding function to represent discrete quantum states as continuous variables, following the approach in [1], which uses token and positional embeddings commonly used in text generation. It seems that this embedding, originally designed for text generation, inherently carries a sequential bias, which makes the motivation and effectiveness of the proposed QuaDiM less convincing to me.

- The authors should explicitly mention the number of parameters and training time of the models used to ensure a fair comparison. Although this is not a critical issue, the network architecture and number of parameters of the main competitor, LLM4QPE, and the proposed QuaDiM appear to be nearly identical.

- Some minor issues: In Table 2, for L = 70, M = 100 and QuaDiM (ours), is the result 0.0597 correct? Line 048, Fig. 2? Line 072, the the?, ...

### Questions
- Could the authors clarify why diffusion models have a suitable structure for learning non-sequential quantum state estimation compared to other generative models?

- Could the authors explain why the embedding method used in QuaDiM has a structure suitable for non-sequential quantum state estimation?

### Soundness
3

### Presentation
3

### Contribution
3
