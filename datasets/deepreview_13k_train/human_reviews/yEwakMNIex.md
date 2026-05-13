# Unified Neural Solvers for General TSP and Multiple Combinatorial Optimization Tasks via Problem Reduction and Matrix Encoding

- Decision: Accept
- Scores: 6, 8, 6, 5

## Abstract
Various neural solvers have been devised for combinatorial optimization (CO), which are often tailored for specific problem types, ranging from TSP, CVRP to SAT, etc. Yet, it remains an open question how to achieve universality regarding problem representing and learning with a general  framework. This paper first proposes RedCO, to unify a set of CO problems by reducing them into the general TSP form featured by distance matrices. The applicability of this strategy is dependent on the efficiency of the problem reduction and solution transition procedures, which we show that at least ATSP, HCP, and SAT are readily feasible. The hope is to allow for the effective and even simultaneous use of as many types of CO instances as possible to train a neural TSP solver, and optionally finetune it for specific problem types. In particular, unlike the prevalent TSP benchmarks based on Euclidean instances with 2-D coordinates, our focused domain of general TSP could involve non-metric, asymmetric or discrete distances without explicit node coordinates, which is much less explored in TSP literature while poses new intellectual challenges. Along this direction, we devise two neural TSP solvers with and without supervision to conquer such matrix-formulated input, respectively: 1) MatPOENet and 2) MatDIFFNet. The former is a reinforcement learning-based sequential model with pseudo one-hot embedding (POE) scheme; and the latter is a Diffusion-based generative model with the mix-noised reference mapping scheme. Extensive experiments on ATSP, 2DTSP, HCP- and SAT-distributed general TSPs demonstrate the strong ability of our approaches towards arbitrary matrix-encoded TSP with structure and size variation. Source code and data will be made public.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a unified neural solver framework called RedCO, which uses problem reduction techniques to map different combinatorial optimization (CO) problems to the general Traveling Salesman Problem (TSP) format. Two novel neural solvers, MatPOENet and MatDIFFNet, are introduced to handle matrix-encoded inputs and solve these problems efficiently. This work aims to extend neural combinatorial optimization beyond specific problem types by providing a scalable solution for problems like asymmetric TSP (ATSP), directed Hamiltonian cycle problems (DHCP), and 3-Satisfiability (3SAT).

### Strengths
- The introduction of MatPOENet and MatDIFFNet, which use Transformer-based and diffusion-based models, respectively, showcases the application of advanced neural network structures to solve matrix-encoded TSP problems.

- The RedCO framework offers a novel approach by unifying different combinatorial optimization (CO) problems through reduction to a general TSP format. This reduction expands the scope of neural solvers to tackle diverse problem types in a single architecture.

- RedCO's capability to handle non-metric, asymmetric, and discrete TSP instances, unlike traditional Euclidean-focused TSP solvers, significantly broadens its applicability.

- The RedCO framework is designed to incorporate various solver types, including existing methods like DIMES, showing the framework's modularity.

### Weaknesses
 - While the framework performs well for medium-scale problems, its efficiency and feasibility for large-scale, real-world instances (e.g., with tens of thousands of nodes) are not thoroughly demonstrated or tested. Specifically, the paper lacks a detailed analysis of how the computational complexity of the proposed neural solvers scales with increasing problem size. The reported experiments do not sufficiently explore the limits of the approach in terms of node count, edge density, and the resulting computational time and memory requirements.

- The use of complex neural models like MatPOENet and MatDIFFNet makes it difficult to understand the inner workings and decision-making processes of these solvers. More interpretability features or case studies would be beneficial. The paper does not offer insights into which features or patterns in the input matrix are most influential in the model's decision-making. This lack of transparency hinders the ability to diagnose potential biases or limitations in the model's performance.

- The paper mainly focuses on synthetic data for testing, with limited discussion on how the models would handle real-world problem instances that could have different statistical properties. The synthetic data generation process is not fully detailed, making it difficult to assess whether the generated instances accurately reflect the complexities and distributions of real-world problems. This raises concerns about the generalizability of the results.

- There is little exploration into how the proposed solvers manage noisy or incomplete data, which is common in practical applications. The paper does not investigate the sensitivity of the models to perturbations in the input matrix, such as missing entries or corrupted edge weights. This is a critical aspect for real-world applicability, where data is often imperfect.

- The MatDIFFNet, while powerful for certain problem types, is computationally intensive, which may hinder its use for larger instances or require additional optimization strategies. The paper does not provide a detailed breakdown of the computational cost associated with each step of the diffusion process, which makes it difficult to identify potential bottlenecks and areas for optimization.

### Questions
1. When converting various combinatorial optimization problems to TSP instances, are there cases where the reduction process fails or underperforms due to problem characteristics? How does the method handle these instances?

2. Given that MatDIFFNet has longer inference times due to complex diffusion steps, are there plans to optimize the model architecture or algorithm to improve inference speed and computational efficiency?

3. In multi-task training, does the interaction between different tasks lead to performance drops in any specific task? Is there a clear mechanism in the model to handle task weight allocation and interdependencies?

4. How robust are MatPOENet and MatDIFFNet when the input data contains noise or incomplete information? Were there any robustness tests conducted?

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
4

### Summary
Authors propose RedCO, to unify a set of CO problems by reducing them into the general TSP form featured by distance matrices. RedCO demonstrates the potential to efficiently train a neural TSP solver using a diverse range of CO instances, and can also be adapted to specialize for specific problem types.

### Strengths
1. The paper is well-written and easy to understand.
2. As far as I know, this is the first study attempting to create a general framework for learning various COPs in a reduction manner.
3. The experiments conducted are thorough, and the results effectively showcase the framework's capability to handle arbitrary matrix-encoded TSPs.

### Weaknesses
1. The organization of the experimental section is lacking. With seven research questions (RQs) presented, the lack of clear categorization makes this part of the paper somewhat difficult to navigate. The RQs are not clearly linked to specific experiments, making it hard to understand which results address which question. A more structured approach, perhaps by grouping experiments under each RQ or using a table to map experiments to RQs, would greatly improve readability.
2. The results for DIFUSCO and T2T are not included. It is noted that MatDIFFNet performs well on 3SAT problems, which is developed upon DIFUSCO and T2T. The absence of these results makes it difficult to assess the true contribution of MatDIFFNet, especially given its reliance on these methods. Including these results would provide a more complete picture of the framework's performance and allow for a more direct comparison.
3. While the specific problem reduction is detailed in Appendix A, it would be helpful to have a more detailed introduction to the reduction principles and the applicable COPs. Specifically:
   - What types of COPs (or what properties must COPs have) can be reduced to a general TSP? It's unclear what the limitations of the proposed reduction are. Are there specific characteristics of COPs that make them unsuitable for this reduction? A discussion of these limitations is necessary.
   - What considerations should be taken into account when performing this reduction? The reduction process seems non-trivial, and it's not clear what the key considerations are to ensure that the reduced TSP accurately reflects the original COP. A more detailed explanation of the reduction process, including potential pitfalls and best practices, would be beneficial.

### Questions
1. Table 2 shows that MatPOENet and MatDIFFNet outperform LKH in solving 3SAT problems, but they tend to produce worse results in most other scenarios. Could you provide some explanations for this?
2. How does RedCO perform on standard TSPs (Symmetric TSPs)?
3. In line 268, the POE is based on $f(x) = 1/cosh(100x)$, can you give more introduction of the empirical function?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper presents an interesting approach to dealing with multi-task CO by transforming several CO problems into equivalent TSPs. This paper also proposes two new solvers, MatPOENet and MatDIFFNet, to solve the following TSP.

### Strengths
1. This article is well-written and reasonable.
2. The author has carried out abundant experiments and discussions.

### Weaknesses
I think this article has two major weaknesses that should be considered.
1. This paper adopts a quite special modeling approach, and its applicability is worrying. I doubt the effectiveness of reducing multi-CO problems into the general TSP form featured by distance matrices. 
According to Fig. 1, you show that NP problems can be transformed into SAT, I am concerned if this part can be proved. For some problems, the transformation into TSP is itself an NP problem if you want to maintain the Found Rate ``FR`` (e.g., CVRP, as mentioned in Appendix D.2.4, ``first clustering points and then solving each cluster as a TSP`` will harm the FR), and even if it can be transformed into TSP, the time complexity of such transaction may increase dramatically.
2. Some of the experiments in this paper are not clearly described. I tried my best to find out but it is still not clear what the exact settings of the * version, single, and mixed in Table 2 are.

### Questions
1. MatDIFFNet is trained on 8 NVIDIA H800 80GB GPUs with Intel Xeon (Skylake, IBRS) 16-core CPU is super computational resource consuming, I am curious about the ablation experiments on computational resources.
2. The test questions in the article experiments are too limited, this article mentions applicability for ``P ≤P general TSP or P in matrix format (VC, Clique, VRPs, FFSP, MIS, etc.)`` etc., I would highly recommend to introduce evaluations on more CO problems to respond to my concerns on applicability.
3. In Line 1137, you mention that ``Also, they generally evaluated their proposed methods on no larger than 100 nodes of TSP/VRP instances, with a major emphasis of methodological innovations rather than eager pursuit of scalability at sheer engineering level.`` What means the sheer engineering level? Also, it seems that this paper also mainly focuses on no larger than 100 nodes. Please provide a clear explanation.
4. This paper uses a unique test problem design, which I think requires the authors to implement more comparative algorithms (e.g., GOAL, MVMOE) on the problems they cover for experimental validation.
5. The results in Table 5 are not sufficient to illustrate performance on larger-scaled data, I think you should provide experiments without the aid of an external process to explore whether the model has the ability to scale up. Also, this paper does experiments on scales of 20-100, and I doubt that it makes sense to compare methods that address large-scale CO problems such as GLOP.

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This article focuses on multi-task CO problems, proposes a solution method that is general for several CO problems and presents two efficient solvers.

### Strengths
1. The Problem reduction of this paper has theoretical support.
2. The proposed methods of this paper has advantages in terms of effectiveness.

### Weaknesses
1. The RedCO approach proposed in this paper is not intuitively applicable to a wide range of CO problems. I think the value of multi-task CO should be reflected in its applicability to most CO problems.
2. The contribution of this paper is weak, translating these problems into a TSP is not a new idea and TSP solver is quite well developed.

### Questions
1. In RQ2 you show a comparison of solution times and results with the LKH method. The reason you showed efficiency in this experiment compared to LKH seems to come entirely from superior performance on the 3-SAT problem. I don't think it is fair to take Average L in this case. I am more curious as to why LKH performs poorly on the 3-SAT problem and where MatPOENet and MatDIFFNet excel in this problem. Can you provide a visual example to help me understand this result intuitively?
2. For solving efficiency, I think this paper should be compared more with Gurobi for efficiency. I am very curious about the results of this part. I also suggest you add time as reference in Table1.
3. I am having trouble understanding the specific N and d settings for variants in the ii) part of RQ3 and especially in Table 4. I need more explanation about it.
4. What is the significance of MatDIFFNet? Based on the results so far (ignoring the future work you mentioned) it looks like its lagging behind in performance and efficiency as well as training efficiency. I would suggest deleting this section or putting it in the appendix. Also The authors say in RQ7 that MatDIFFNet has the potential for more accurate solution space for larger scale instances while mentioning in the limitation that ``MatDIFFNet has the potential for direct solving of larger instances but is currently yet to be implemented.`` But I can't find any evidence for this. But I can't find any evidence for this , please explain this.

### Soundness
3

### Presentation
3

### Contribution
3
