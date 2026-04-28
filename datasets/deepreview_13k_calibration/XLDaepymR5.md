# Scalable Back-Propagation-Free Training of Optical Physics-Informed Neural Networks

- Decision: Reject
- Avg Score: 5.83
- Scores: 6, 3, 6, 6, 6, 8

## Abstract
Physics-informed neural networks (PINNs) have shown promise in solving partial differential equations (PDEs), with growing interest in their energy-efficient, real-time training on edge devices. Photonic computing offers a potential solution due to its high operation speed.
However, the lack of photonic memory and the large footprint of current photonic devices prevent training realistic-size PINNs on photonic chips. This paper proposes a completely back-propagation-free (BP-free) and highly salable framework to enable training real-size PINNs on silicon photonics platforms. Our approach involves three key innovations: (1) a sparse-grid Stein derivative estimator to avoid the BP in the loss evaluation of a PINN, (2) a dimension-reduced zeroth-order optimization via tensor-train decomposition to achieve better scalability and convergence in BP-free training, and (3) a scalable on-chip photonic PINN training accelerator design using photonic tensor cores. We validate the performance of our numerical methods in both low- and high-dimensional PDE benchmarks. Through circuit simulation based on real device parameters, we further demonstrate the significant performance benefit (e.g., real-time training, huge chip area reduction) of our photonic accelerator. Our framework addresses the fundamental challenges of photonic AI and will enable real-time training of real-size PINNs on photonic chips.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces a BP-free training framework for physics-informed neural networks on photonic hardware. The authors propose a sparse-grid Stein estimator to replace BP in loss evaluation; a tensor-compressed zeroth-order (ZO) optimization method to improve scalability, and scalable photonic accelerator design aimed at real-time PINN training. Through simulations on low- and high-dimensional PDE benchmarks, the paper demonstrates the efficacy of these methods in reducing training time and chip area requirements.

### Strengths
Strengths:

1.	The proposed method largely reduce the dimensionality in zeroth-order ONN training, thus can train realistic PINN model using sampling-based ZO optimizer.

2.	Compared to prior methods, it shows faster convergence and better error.

3.	The training process considers hardware nonideality, e.g., quantization, noises.

### Weaknesses
Weaknesses:

1.	Besides training from scratch, if there is a pretrained digital PINN model, how does the mapping efficiency of the proposed method compared to prior methods. This is also an actual deployment use case.

2.	What is the detailed photonic accelerator setting, e.g., core size, etc. Noticed the training parameters in Table 3 are different, especially L2ight has very few parameters. What could be this reason? Is it possible to keep a similar parameter size by modifying the model settings and comparing the training algorithm itself? Now the effect of #params and training methods are mixed.

3.	Any experiments on different TT-ranks? How does that impact the model expressivity compared to dense NNs? What is the trade-off between trainability and model expressivity?

### Questions
1.	Besides training from scratch, if there is a pretrained digital PINN model, how does the mapping efficiency of the proposed method compared to prior methods. This is also an actual deployment use case.

2.	What is the detailed photonic accelerator setting, e.g., core size, etc. Noticed the training parameters in Table 3 are different, especially L2ight has very few parameters. Is it related to the overly large sub-matrix size? How about using 8x8 matrix blocks so the diagonal still has enough parameters to train?

3.	Any experiments on different TT-ranks? How does that impact the model expressivity compared to dense NNs? What is the trade-off between trainability and model expressivity?

4.     Is there any hardware implementation difficulty for the assumed tensorized ONN TONN with complicated signal crossings?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
In this paper, the authors aim to address the on-chip training problem for a photonic accelerator specific to PINN by using a BP-free method. The authors propose two-level methods, including a sparse grid Stein derivative estimator that uses samples to estimate gradient in a zeroth-order way, followed by a way to reduce the dimensionality of the weight matrix to improve ZO performance. The paper tries to approach the accuracy of the traditional BP-based method on a toy neural network but still has 2x worse error with their method.

### Strengths
Strength:
* A complete evaluation from algorithm to chip, and consider some realistic constraints, e.g., resolution limits.

### Weaknesses
Weakness
* First, the papers' main methods are both not new but borrow from other domains without many new contributions/modifications. For example, the low-rank compression with tensor-train is not new. Also the sparse-grid method is also a typical method in the PDE domain.
* Second, some claims are not accurate. For example, a photonic accelerator will not build a huge chip directly for a 128x128 array. Instead, it also blokifies the large weight matrix into a small one and implements on-chip. Therefore, the claim in Sec.4 is not right. Especially regarding implementing the NxN matrix, it is infeasible for partial PINNs.
* Third, the implementation of baselines might be wrong, as your understanding of vanilla ONN may not be right. Could you provide more details about how to train an ONN with ZO-based methods like FLOPS and L2ight? What is the photonic tensor core size?
* Fourth, the used model, 3-layer MLP, is a toy example. The model itself is not optimized for PDE tasks; it may be overfitting or have many pruning opportunities. This can be observed from Tabl2. Applying compression leads to much better accuracy on harder task, 20dim-HJB, meaning the model parameters are highly redundant.
* Fifth, the ZO performance is 5x worse than using the FO method (Table. 2) on the harder task, weakening the claims of the paper.

### Questions
Questions
* Could you try a harder task and use a more optimized, less-overparametrized PINN model for PDE?

### Soundness
2

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
4

### Summary
In this work, the authors propose a back-propagation-free framework along with the appropriate design for physics-informed training, targeting the real-time training of real-size Physics-Informed Neural Networks (PINNs) deployed on photonic chips. The proposed method allows one to reduce the required MZIs without sacrificing performance, thus reducing the footprints of the applied components, potentially enabling the scalability of optical neural networks in higher-dimensional architectures and tasks. More specifically, the proposed training framework includes a sparse grid Stein derivative estimation that allows to obviate backpropagation as well as a dimension-reduced zeroth-order optimization via tensor-train decomposition. This, according to the authors, improves the convergence of optimization and scalability, enabling end-to-end training on the chip. In turn, the paper introduces two photonic accelerator designs, one implementing the whole model on a single chip and the other using a single photonic tensor core with time multiplexing. The authors validate the convergence of the proposed training framework in two tasks, presenting numerical experiments that demonstrate the competitive performance that the proposed method achieves in contrast to the backpropagation baseline. Finally, the paper presents some evidence on hardware implementation, including footprint size and training latency time, as acquired from simulation experiments.

### Strengths
The paper deals with a highly relevant and challenging task, such as the training and scalability of optical neural networks, proposing a numerical training framework that is accompanied by a photonic accelerator design. The proposed tensor compressed zeroth-order optimization approach shows that not only it allows us to reduce the required MZIs but it is also experimentally demonstrated that benefits the convergence of the model.

With the integration of Strain derivative estimation and the proposed compressed tensor zeroth order optimization that reduces the zeroth order gradient variance, the paper reports significant improvements in contrast to existing on-chip backpropagation-free optical neural networks training lowering simultaneously the required MZIs.

### Weaknesses
Although, as the paper presents an optical inference engine it lacks critical details regarding the overall architecture and computational performance. For example, the authors mention in the supplementary material that the phase $\phi$ is uniformly quantized to 8 bit in the simulation but they do not comment on the rate at which such bit resolution can be achieved. Even state-of-the-art optical devices facing low SNRs, especially at high computational rates, significantly affecting the effective bit resolution.  

The interconnection between the Digital Control System and TONN is not discussed in a sufficiently detailed way. Do additional devices (such as photodiodes) are needed and do they introduce any further noise to the overall setup? 

Synchronization of the Digital Control System and TONN introduces significant additional overhead, increasing the latency of the proposed architecture ($\approx500$ ns /epoch). This is further exaggerated because of the tensor compression which factorizes the weights, significantly increasing the calls on the Digital Control System. This potentially hinders the high inference speed in higher-dimensional tasks. Introducing a complexity analysis with reference to the iterations per epoch and calls to the TONN inference engine will provide further insights regarding the scalability of the proposed method. In my opinion, since the paper targets the scalability of back-propagation-free training, the authors should further discuss the unavoidable overhead that is introduced by tensor compression and further analyze the reported latency $t_{DIG}$ in A.4.2. 

Although the sparse-grid stain derivative estimator significantly reduces the number of nodes needed in contrast to the samples needed in Monte Carlo estimation, the paper does not provide any convergence and cost complexity analysis for the proposed method. Taking into account the significant fabrication losses that intrinsically exist in optical devices, a convergence analysis on the ideal optimization case would strengthen the scalability claim of the authors. Without theoretical guarantees or experimental evaluation, the claim that “Our results can be easily extended to solve image and speech problems on photonic and other types of edge platform” sounds stronger than what the paper can support, considering the fabrication imperfections and the fact that it presents only simulation results in 20-dimensional task, which is much smaller than MNIST benchmark, for example.

### Questions
In what computational rate do the applied components of the proposed TONN support such a high effective bit resolution?

### Soundness
4

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
3

### Summary
This paper proposes a back-propagation-free (BP-free) method for efficiently training physics-informed neural networks (PINNs) on real-time edge devices. The method focuses on utilizing optical neural networks (ONNs) in photonic computing to solve high-dimensional partial differential equations (PDEs). Traditional PINN training is computationally expensive, especially for real-time training on edge devices. To address this challenge, the authors introduce three main innovations:

1. They utilize a sparse-grid(SG) Stein derivative estimator to calculate derivatives in the loss function without the need for back-propagation. This enables efficient evaluation of the PINN loss function without complex high-order derivative calculations or Automatic differentiation.

2.  They adopt Tensor-Train (TT) decomposition for low-rank tensor compression, and zeroth-order (ZO) optimization to reduce parameter dimensionality and improve scalability and convergence. These allow faster convergence even for high-dimensional PINNs by reducing the computational burden associated with parameter updates.

3. They propose a scalable on-chip photonic PINN accelerator design that utilizes photonic tensor cores to achieve real-time training without back-propagation. This design enhances energy and area efficiency, enabling fast, real-time operation on edge devices compared to conventional GPU-based training.

The paper validates this framework by testing on high-dimensional PDEs such as the Black-Scholes and 20-dim Hamilton-Jacobi-Bellman equations, demonstrating performance improvements through simulations on actual photonic devices.

### Strengths
### Strengths

1. The authors identified memory issues that arise during the training of PINNs on traditional photonic chips. To address this, they introduced a BP-free approach instead of the back-propagation method and utilized TT decomposition to reduce memory usage. This enabled real-time, high-dimensional PINN training on photonic chips and improved computational efficiency, accelerating the convergence rate.


2. They proposed two design options that can be applied according to specific needs in photonic computing, enhancing system performance. The on-chip photonic accelerator proposed by the authors efficiently uses existing photonic MAC devices, which occupy a large area, to maintain energy efficiency even in large-scale PINN training. The advantages of this design were experimentally demonstrated compared to conventional ONNs in terms of MZI number, footprint, and latency.

### Weaknesses
### Weaknesses

1. Although the authors claimed memory and computational efficiency for their proposed method, details on time per epoch, total convergence time, and number of epochs until convergence were not provided, aside from accuracy in the experiments. It is unclear how the proposed method compares to existing methods in terms of actual training time and resource utilization, which are critical for evaluating its practical applicability.

2. Additional experiments on other commonly used PDE datasets, such as Navier-Stokes, Darcy flow, and Burgers' equation, are needed beyond Black-Scholes and 20-dimensional HJB. The current evaluation is limited to a specific set of PDEs, and it is not clear how the method would generalize to other types of problems with different characteristics.

3. The authors did not provide an explanation for the criteria used to determine "convergence," which is a key aspect of their experiments. In Figure 5, it appears possible that different convergence criteria could be applied depending on the epoch. The lack of a clear convergence criterion makes it difficult to assess the reliability and reproducibility of the results.

4. The figures presenting the experimental results are too small, and the associated information or explanations are limited. The small size and limited explanations make it challenging to interpret the results and draw meaningful conclusions.

5. Detailed settings and environment information used in the experiments were not provided (e.g., code, chip information). This lack of information makes it difficult to reproduce the results and evaluate the method's performance under different conditions.

### Questions
### Questions

1. As mentioned in Weakness 2, are there any experiments conducted on other datasets?

2. As raised in Weakness 3, what criteria did the authors use to determine the point of convergence?

3. Could you provide more information on the efficiency and memory aspects of the experiments? (e.g., memory usage, time per epoch, the time and number of epochs each method took to converge, etc.)

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors design a computational training framework to train hardware realizations of all-optical neural networks (ONNs).  As opposed to previous work, which treated the forward pass, the contributions provided in this paper allow for completion of the framework by adding the backward pass via a gradient estimation approach, thus enabling training to occur in hardware. The details of the methodology are designed considering the physical constraints of the optical hardware, namely the large area footprints of MZIs and the difficulty to store memory in the optical domain (which necessitates electro-optical (EO) conversion in other works).

Gradient approximation methods are difficult to scale on larger networks due to dimension-dependent errors. Two novel aspects are thus introduced in this paper to allow this to work: 
 
(1) a sparse-grid Stein derivative estimation method which addresses dimension-dependant gradient estimation error
 
(2) To further suppress the dimension-dependant gradient estimation error, they suggest a tensor-compressed variance reduction approach to reduce the dimensionality of the problem, thus achieving better convergence

They compare their designs with a standard ONN accelerator. TONN-1 (fully on-chip) reduces both the footprint and latency of the photonic network as compared to previous, standard ONN designs. TONN-2 (where matrices are decomposed into tiles, requiring some storage of intermediate results and thus EO conversion)  further reduces the hardware footprint at the cost of increased latency from re-using the photonic tensor core multiple times and storing intermediate results.

### Strengths
The paper is very well written and organized, and information is presented concisely. The results would be useful to other researchers working on software for ONNs. Without being an expert in the field of optical hardware, I find the results novel. Many of my initial questions (for example, the latency calculations) are answered in the appendix.

### Weaknesses
Throughout most of the paper, I was also questioning why the focus was on PINNs, and whether there was anything that prevented it from applying more generally. The authors have answered this in the last sentence of the conclusion (although I still think the focus on PINN applications is a bit unnecessary).

The applications demonstrated are on relatively “toy” problems. Epoch vs. loss plots are only shown for one example in each case. Different network sizes are not tested. Overall, the demonstrated results are fairly minimal, only barely enough to show that the method works. More extensive results would be nice to really flesh out the work and show that the method is useful.

-In Table 1, why does the sparse-grid Stein estimator perform better than automatic differentiation?

### Questions
-In Table 1, why does the sparse-grid Stein estimator perform better than automatic differentiation?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 6

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper mainly discuss the BP-free training scheme of PINNs on photonic devices. The major contributions include 1) sparse grid stein derivative estimator for BP-free loss evaluation. 2) tensor decomposition for better scalability and 3) photonic accelerator design with photonic tensor cores. 
Overall, the paper is well written, with a good technique discussion, novelty, and comprehensive experiments. I would recommend proceeding with publication upon addressing some minor comments.

### Strengths
1. Two-level BP Free PINN Training with sparse-grid and tensor-compressed variance reduction reduces memory footprint and improves convergence.
2. Hardware design, and emulation with comprehensive performance evaluation.
3. Detailed and clear contents that explain each proposed contribution's underlying idea.

### Weaknesses
1. More PDE/ODE case studies might be a plus to demonstrate the generality of the method. e.g. navier-strokes equation. heat spread equations. Also, there could be finer 2D/3D mesh grids in certain applications, and the proposed method scale to these problems is a question mark.  
2. I might miss some parts, but It would be better to discuss how the contributions in the paper relate to PINN itself. This is a top-level comment, on why PINN executed on photonic chips. I am trying to understand are the proposed techniques specifically effective on PINNs, or just some general method that can be applicable to any light-weight neural networks. To my understanding, PINN vs general NNs, there would be extra computing of the derivatives described in the governing equations. 
3. In 3.2.1 how are the ranks chosen during tensor decomposition?

### Questions
Please refer to the weakness section.

### Soundness
3

### Presentation
4

### Contribution
3
