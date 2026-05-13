# HiQ-Lip: A Quantum-Classical Hierarchical Method for Global Lipschitz Constant Estimation of ReLU Networks

- Decision: Reject
- Scores: 5, 5, 3, 6, 3

## Abstract
Estimating the global Lipschitz constant of neural networks is crucial for understanding and improving their robustness and generalization capabilities. However, precise calculations are NP-hard, and current semidefinite programming (SDP) methods face challenges such as high memory usage and slow processing speeds. In this paper, we propose $\textbf{HiQ-Lip}$, a hybrid quantum-classical hierarchical method that leverages Coherent Ising Machines (CIMs) to estimate the global Lipschitz constant. 
We tackle the estimation by converting it into a Quadratic Unconstrained Binary Optimization (QUBO) problem and implement a multilevel graph coarsening and refinement strategy to adapt to the constraints of contemporary quantum hardware. 
Our experimental evaluations on fully connected neural networks demonstrate that HiQ-Lip not only provides estimates comparable to state-of-the-art methods but also significantly accelerates the computation process. 
In specific tests involving two-layer neural networks with 256 hidden neurons, HiQ-Lip doubles the solving speed and offers more accurate upper bounds than the existing best method, LiPopt.
These findings highlight the promising utility of small-scale quantum devices in advancing the estimation of neural network

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors propose a hybrid quantum-classical algorithm for estimating the $L_\infty \rightarrow L_1$ Lipschitz constant of a fully-connected neural network. This is achieved by converting the Lipschitz constant estimation problem into an equivalent cut-norm problem which can be solved efficiently on a quantum device with the so-called Quadratic Unconstrained Binary Optimization (QUBO) model. Due to hardware limitations of current quantum devices, a graph coarsening and refinement strategy is used to break the problem into subproblems that can be handled by about 100 qubits.Their experiments show significant speed up in computation time for 2-5 layer MLPs over existing $L_\infty \rightarrow L_1$ Lipschitz estimation approaches.

### Strengths
- This is the first work of my knowledge to utilize quantum hardware models to accelerate Lipschitz constant estimation and is interesting in concept. The graph coarsening and refinement strategy appears to be a novel contribution of theirs which seems generally useful.

- The computation times reported for 3-5 layer networks show two orders of magnitude speed up over GeoLip while only being slightly more conservative. This is a promising result.

- The paper is generally well-written and the theory is accessible to most readers.

### Weaknesses
 -Although the methodology is interesting in concept, the results for 1-5 layer MLP model trained on MNIST are not very intriguing from a practical standpoint. The paper would be stronger if there was some evidence for making progress in some down-stream application such as certified-robustness of the MNIST classifier. In that case, there are currently 1-Lipschitz regularized layers which can already achieve very good robustness results for large CNNs trained on MNIST [Prach 2022, Araujo 2023].

-I feel that the community is not practically limited by scales of 3-5 layers shown in the paper. In my opinion the current challenges in Lipschitz estimation are more for larger scale models like ResNets trained on ImageNET with the goal to achieve some non-trivial certified robustness for classification. At this scale it's more of a memory limitation issue for solving SDPs (which can also be broken into sub-problems). At this scale, I’m concerned that the quantum hardware limitations are going to make the bounds too conservative. There might be more potential for GPU acceleration on classical computers [Wang 2024].

- It's difficult to interpret the computation times presented in the paper since each algorithm is supposedly using a different computing architecture. Since HiQ-Lip is a hybrid quantum-classical algorithm, is it using the same classical architecture as the baselines with an additional simulated 100 qubits? I think this practical aspect requires more explanation somewhere in the paper.

### Questions
- Could this balance of bound conservativeness and faster computation speed also be achieved if we approach smaller subproblems with classical approaches? I wouldn’t expect it to be as drastic as the HiQ-Lip, but it might make the classical computation times much more reasonable for the scales presented in the paper.

- The paper refers to the paper (Bartlett et al., 2017) as justification for the improved scaling constant. It would be helpful to point to a specific result in that paper since there is no other discussion in the paper about where it comes from or how it's derived.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
In this paper, the authors introduce HiQ-Lip, a hybrid quantum-classical hierarchical method for estimating the global Lipschitz constant of neural networks. The problem of Lipschitz constant estimation is first transformed into a QUBO problem. Subsequently, this QUBO problem is solved hierarchically on Coherent Ising Machines (CIMs) to accommodate the system size supported by quantum devices. Experimental results on multi-layer perceptrons (MLPs) demonstrate that their method provides estimations comparable to classical state-of-the-art methods while requiring less computation time.

### Strengths
1. The work is the first attempt to employ quantum computing to handle the task of Lipschitz constant estimation.
2. The hierarchical strategy for solving large-scale QUBO problems makes it possible to apply HiQ-Lip on small-scale devices.
3. The simulation results show the advantage of HiQ-Lip in computation time.
4. The presentation of this paper is clear.

### Weaknesses
1. As the paper primarily focuses on applying quantum computing to global Lipschitz constant estimation, it is uncertain whether the ICLR community will find this topic compelling. The connection to core machine learning problems such as generalization or adversarial robustness is not immediately obvious, and the paper does not sufficiently motivate why a quantum approach is necessary or advantageous for this specific task.
2. The paper lacks discussion on the theoretical guarantee about the approximation ratio of the hierarchical strategy to the global optimal of original QUBO. Without a formal analysis, it's difficult to assess the quality of the solutions obtained, especially given that the hierarchical approach introduces approximations. The absence of theoretical bounds makes it unclear how far the obtained solution is from the true Lipschitz constant.
3. The experimental results are derived entirely from simulations under ideal conditions, without consideration for practical aspects of quantum devices such as finite shots, device noise, and limited coherence time. These non-ignorable imperfections could significantly impact the quality of solutions obtained from quantum algorithms in practice. The simulation results do not provide a realistic assessment of the method's performance on actual quantum hardware, which is crucial for validating the practical applicability of the approach.

### Questions
1. The experimental setup described in Section 6 lacks clarity, particularly regarding the software and hardware configurations used.
2. How is the computation time for HiQ-Lip determined? Since the experiments are conducted on a simulated CIM, how is the time for the quantum computation component accounted for?
3. Comparing Table 4 with Table 2 reveals that networks with a larger number of layers appear to require less time for estimation than two-layer networks, which contradicts my expectations. Can you provide a more detailed explanation of this phenomenon?
4. A more comprehensive explanation of the coefficients used for 3- to 5-layer networks (i.e., HiQ-Lip MP B) would be appreciated.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper aims improving the scalability of SDP-based Lipschitz estimation of neural networks via developing HiQ-Lip, a hybrid quantum-classical hierarchical method that relies on Coherent Ising Machines (CIMs). The authors convert the problem into a Quadratic Unconstrained Binary Optimization (QUBO) problem and claim that this is more adaptable to the constraints of contemporary quantum hardware. Finally, the authors provide some experiments on fully connected neural networks on MNIST to show that their method is comparable to GeoLip but accelerates the computation process for such relatively small scale problem.

### Strengths
1. The idea from this paper is new and original.

2. The perspective on using small-scale quantum devices for Lipschitz estimation of neural networks is new.

### Weaknesses
The scale of the experiments is quite small. Recently, for l_2 Lipschitz bounds, the SDP method has already been scaled to ImageNet by the following paper:

Zi Wang et.al. (ICLR2024):  On the scalability and memory efficiency of semidefinite programs for Lipschitz constant estimation of neural networks.

  The authors seem not aware of the above result which achieves scalability to ImageNet. The authors studied the l-infinity case here, but the scale is on the MNIST level.  This makes me think the contribution by the authors is very incremental in comparison to the original GeoLip paper. A few ways to make the contributions more significant include: 1. demonstrate the proposed method on large scale networks; 2) extend the method for more network structures, e.g. implicit models, residual network, etc. The current work focuses on fully connected networks, which are relatively simple architectures. The method's applicability to more complex architectures, such as convolutional networks or transformers, is not demonstrated. Furthermore, the paper does not provide a detailed analysis of the computational complexity of the proposed method, especially in comparison to existing SDP-based approaches. This lack of analysis makes it difficult to assess the practical benefits of the proposed method beyond the specific experimental setup presented.

### Questions
1. Is it possible to scale the proposed method for larger networks?

2. In the l2 case, LipSDP has been extended for implicit networks (R1, R2), residual networks (R3) and more general structures (R4). See the following papers:

 [R1]: Revan et.al. Lipschitz bounded equilibrium networks.

 [R2]: Havens at al. Exploiting connections between Lipschitz structures for certifiably robust deep equilibrium models. NeurIPS 2023

 [R3]: Araujo et.al. A unified algebraic perspective on Lipschitz neural networks. ICLR 2023.

 [R4]:  Fazlyab et. al. Certified robustness via dynamic margin maximization and improved lipschitz regularization. NeurIPS 2023

  It will be very interesting if the authors can address more general network structures for the l-infinity case. Can the authors comment on the possibility of such extensions?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper addresses the problem of finding the global Lipschitz constant of ReLU neural networks using a hybrid quantum-classical hierarchical method. The problem of estimating the global Lipschitz constant of a ReLU neural network is converted into a Quadratic Unconstrained Binary Optimization (QUBO) problem. To address address the issue of limited number of qubits, the paper proposes a new HiQ-Lip algorithm that works by first translating the structure of the neural network into a graph with each node representing a neuron and edges representing the connection strengths, employing graph coarsening to reduce the number of nodes by merging them until the resulting QUBO can be solved directly on a small quantum-annealing based computer, then solving the QUBO and finally mapping the approximate solution from the coarse graph back to the original graph by solving optimization subproblems. The paper finally presents experiments with a two-layer neural network with varying number of hidden neurons and deeper networks with varying number of layers and shows that HiQ-Lip doubles the solving speed of and provides more accurate upper bound (using GeoLip as gold standard) compared to the existing best method LiPopt for two-layer networks and GeoLip for multi-layer networks.

### Strengths
One of the strengths of the paper is that it presents a systematic and scalable way to frame the neural network global Lipschitz constant estimation problem as a QUBO that can be solved with a limited number of qubits. This approach could be adapted to other problems related to neural networks such as neural network training or neural network verification. The experimental approach is also very sound as the authors compared with a number of different methods to estimate the global Lipschitz constant such as GeoLip, LipOpt, Matrix Product (MP), Sampling and Brute Force (BF) and tried two-differnt scaling . The time comparison with LipOpt and GeoLip show that the approach offers time-savings.

### Weaknesses
This paper doesn't take into account the latest state-of-art in terms of Quantum Annealers (QA) such as DWave Advantage System (https://www.dwavesys.com/solutions-and-products/systems/) that have ~5000 qubits. They limited themselves only to 100 qubits and simulated CIM. They could have scaled out to larger number of qubits and explored what is the tradeoff between using larger number of qubits versus the graph coarsening/refinement strategy in terms of time saving or estimation quality. Given that larger of qubits are available, what is the value of the graph coarsening/refinement approach? There is a lack of assessment on how much performance degradation arises from graph coarsening and refinement. The paper also lacks a detailed analysis of the impact of the graph coarsening and refinement steps on the final Lipschitz constant estimate. Specifically, it's unclear how the merging of nodes during coarsening affects the accuracy of the solution, and whether the refinement process fully recovers the information lost during coarsening. The experimental evaluation does not provide a clear picture of how the approximation quality changes with the number of coarsening and refinement steps, and how this relates to the size and structure of the neural network being analyzed. Furthermore, the paper does not explore the limitations of the proposed approach in terms of the depth of the neural networks. While the authors mention that deeper networks pose challenges, there is no discussion on the specific limitations of the proposed method for deeper architectures, or how the graph coarsening strategy might need to be adapted to handle the increased complexity of deeper networks.

### Questions
1. Any reason why you didn't consider Quantum Annealers (QAs) with larger number of qubits such as DWave Advantage system that have ~5000 qubits? Could you potentially work with larger neural networks given up to 5000 qubits?  
2. Are all the experiments limited only to 100 qubits or variables? Have you thought about how varying the limit on the number of qubits affects the quality of the estimation?  
3. Have you thought about whether there are limits in terms of the size of the neural networks that you can use this approach with? 
4. If you use this approach with neural networks of size larger than the ones considered in the experimental evaluation and fix the maximum number of qubits to 100, can you quantify the performance degradation from the additional graph coarsening and subsequent refinement through experiments or theory?
5. In all your experiments, the estimates of the global Lipschitz constant come close to GeoLip's estimates, have you tried to increase the size of the neural network in terms of number of hidden neurons or number of layers till either your approach fails to give close estimates to GeoLip? I would expect some performance degradation with larger neural networks due to inexact nature of estimation using graph coarsening/refinement.

### Soundness
4

### Presentation
4

### Contribution
1

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This study presents HiQ-Lip, a hybrid quantum-classical hierarchical approach for estimating the global Lipschitz constant of neural networks. The methodology involves reformulating the Lipschitz constant estimation as a Quadratic Unconstrained Binary Optimization (QUBO) problem, making it suitable for quantum algorithmic solutions. To address the limitations of current quantum devices, the authors introduce a multilevel graph coarsening and refinement strategy, enabling the adaptation of neural network structures to quantum hardware constraints. Empirical evaluations are conducted to validate the effectiveness of the proposed methods.

### Strengths
1. The estimation of Lipschitz constants in neural networks is an important problem in deep learning research, with implications for model robustness and generalization.

2. Applying quantum algorithms to deep learning remains an understudied domain, offering potentially promising avenues for exploration, particularly in light of the increasing sophistication of quantum computing devices.

### Weaknesses
1. Novelty is limited: The conversion of the Lipschitz constant problem to QUBO and mixed-norm formulations was established in [1]; the application of CIM to QUBO was known. The primary algorithmic contribution, a graph coarsening and refinement strategy, is a heuristic and lacks theoretical guarantees. The authors do not provide a clear analysis of how the coarsening and refinement impacts the approximation quality, especially in relation to the original optimization problem. Specifically, the method lacks a bound on the approximation error introduced by the graph coarsening, which is crucial for understanding the trade-off between computational efficiency and solution accuracy.

2. The baseline comparison is insufficient: Authors claim that current SDP methods face challenges such as high memory usage and slow processing speeds. This is true for generic SDP solvers. However, recent advancements in SDP methods have significantly improved efficiency for deep networks and convolutional architectures. For example, [2] has improved the SDP for very deep networks, and [3] has extended the SDP resolution to convolutional networks. Although these works focus on $\ell_2$ Lipchitz constant estimation, I don't see why they cannot be extended to $\ell_\infty$ Lipschitz constant. [1] has pointed out that there are no fundamental differences between $\ell_2$ and $\ell_\infty$ SDPs. The authors need to provide a more rigorous justification for why these advanced SDP methods cannot be adapted or compared against in the $\ell_\infty$ setting, rather than relying on the general limitations of generic SDP solvers.

3. The evaluation methodology raises concerns: HiQ-Lip demonstrates inferior precision compared to GeoLIP [1], with improvements primarily in runtime. However, runtime comparisons are implementation and architecture-dependent and do not account for more efficient, tailored SDP solvers (see above). Additionally, the reported runtimes exhibit inconsistencies, with more complex networks (Net3-Net5) showing significantly shorter processing times than simpler ones (Net2), casting doubt on the reliability of the performance metrics. For example, HiQ-Lip for Net-2 takes 30 seconds, while solving Net3 only takes 6.5 seconds. The authors should provide a detailed breakdown of the runtime, including the time spent on graph coarsening, quantum simulation, and refinement, to better understand the source of these inconsistencies. Furthermore, the lack of clarity on the hardware used for the experiments makes it difficult to assess the validity of the runtime comparisons.

### Questions
1. As far as I can tell, the evaluation was conducted on a simulated CIM rather than actual quantum hardware. Are all experiments run on the same architecture? I did not find this clarification in the paper. Clarification on the uniformity of the experimental setup across all evaluations is necessary for ensuring reproducibility and accurate interpretation of results, especially since the advantage of HiQ-Lip mostly comes from runtime.

2. Given that GeoLIP's foundations in Grothendieck inequalities and the Unique Games Conjecture (UGC) suggest the difficulty of improvement within polynomial time, the precision similarity between HiQ-Lip (on simulated CIM) and GeoLIP on two-layer networks raises intriguing questions. Could the authors explain this similarity? This could imply a consistent performance on similar problems, such as the cut-norm problem, and might have crucial theoretical implications, for example, regarding the validity of the UGC.

### Soundness
2

### Presentation
3

### Contribution
2
