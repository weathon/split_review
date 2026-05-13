# DISCO: Efficient Diffusion Solver for Large-Scale Combinatorial Optimization Problems

- Decision: Reject
- Scores: 6, 6, 6, 5

## Abstract
Combinatorial Optimization (CO) problems are fundamentally important in numerous real-world applications across diverse industries, characterized by entailing enormous solution space and demanding time-sensitive response. 
Despite recent advancements in neural solvers, their limited expressiveness struggles to capture the multi-modal nature of CO landscapes.
While some research has shifted towards diffusion models, these models still sample solutions indiscriminately from the entire NP-complete solution space with time-consuming denoising processes, which limit their practicality for large problem scales.
We propose \textbf{\method}, an efficient \textbf{DI}ffusion \textbf{S}olver for large-scale \textbf{C}ombinatorial \textbf{O}ptimization problems that excels in both solution quality and inference speed. 
\method's efficacy is twofold: 
First, it enhances solution quality by constraining the sampling space to a more meaningful domain guided by solution residues, while preserving the multi-modal properties of the output distributions. 
Second, it accelerates the denoising process through an analytically solvable approach, enabling solution sampling with minimal reverse-time steps and significantly reducing inference time.
\method{}  delivers strong performance on large-scale Traveling Salesman Problems and challenging Maximal Independent Set benchmarks, with inference duration up to $5.28$ times faster than existing diffusion solver alternatives.
By incorporating a divide-and-conquer strategy, \method{}  can well generalize to solve unseen-scale problem instances off the shelf, even surpassing models specifically trained for those scales.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces DISCO, a diffusion-based solver optimized for large-scale combinatorial optimization (CO) problems, such as the Traveling Salesman Problem (TSP) and Maximal Independent Set (MIS). Unlike traditional diffusion models, DISCO focuses on constraining the solution space to enhance quality and employs an analytically solvable denoising approach, which speeds up the process. Its twofold strategy—guided sampling and efficient denoising—achieves significantly faster inference times while maintaining high solution accuracy. DISCO's multi-modal search approach also allows it to generalize effectively to unseen problem scales.

### Strengths
1.	DISCO significantly reduces inference times by introducing an analytically solvable denoising process and constraining the sampling space.
2.	The paper is well-written.

### Weaknesses
1.	The multi-modal graph search is presented as a crucial component of DISCO, with the paper asserting that its multi-modal output helps prevent sub-optimal solutions. However, the experiments do not thoroughly analyze the contribution of this module. It would be beneficial for the authors to include performance metrics with and without this module and detail the computational overhead incurred when it is enabled.
2.	The model's approach involves initially splitting the graph to find solutions, yet the problems tested (TSP, MIS) are inherently global, where localizing could risk sub-optimal outcomes. Could the authors clarify how this graph-splitting approach supports the model’s effectiveness in avoiding sub-optimal solutions for these global problems

### Questions
Please refer to the weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents DISCO, a novel algorithm developed to efficiently address large-scale combinatorial optimization (CO) problems. DISCO effectively manages the multi-modal complexity of CO landscapes, enabling swift solution generation and delivering high-quality results with notably fewer computational steps. Tested on extensive benchmarks, including large-scale Traveling Salesman Problems (TSP) and Maximal Independent Set (MIS), DISCO demonstrates state-of-the-art performance in both solution quality and inference speed.

### Strengths
1. DISCO achieves state-of-the-art results on large-scale TSP-10000 instances and challenging MIS benchmarks, demonstrating superior performance both in terms of solution quality and speed.

2. The proposed divide-and-conquer strategy effectively generalizes DISCO to solve large-scale problem instances, highlighting the method’s scalability and versatility.

3. Beyond the previous results, the paper extends experiment results on aspects of 1) [which I think is the most significant challenge for the supervised learning framework] illustration of the generalization ability of DISCO 2) comparison of the time consumption and computational workload of DISCO 3) add more powerful baseline T2T[1] as comparison. These empirical results further validates the solidness of the paper.

[1] T2T: From Distribution Learning in Training to Gradient Search in Testing for Combinatorial Optimization, NeurIPS 2023.

### Weaknesses
The graph search might lead to exponential growth in trial variance.The scalability might still remain an issue. The authors have claimed the issue in limitation and leave it as future research oppurtunity.

### Questions
From my perspective, the experiments are intensive enough to illustrate the effectiveness of the proposed method, and thus I have no more questions.

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
4

### Summary
This paper presents a new approach, DISCO, designed to efficiently solve large-scale combinatorial optimization  problems using diffusion models. DISCO addresses two primary challenges in current diffusion solvers: sampling from extensive NP-complete solution spaces and the time-intensive denoising processes. By incorporating solution residues, DISCO focuses on meaningful solution domains, maintaining the multi-modal properties of CO problems while reducing computational overhead. The model also employs an analytically solvable denoising process that significantly cuts down inference time. DISCO demonstrates notable performance improvements on tasks such as the TSP and MIS. The method generalizes well to unseen problem scales through a divide-and-conquer approach, sometimes surpassing models trained specifically for those scales.

### Strengths
1.	The idea of using a feasible solution as the residue constrain to guide the generation process sounds novel and reasonable. 
2.	Experimental results show that DISCO is both efficient and effective in solving large scale TSP problems.

### Weaknesses
1.	The novelty is limited. Solution residue is from [1] and multi-model is from [2]. Can you summarize the novelty of the proposed method?
2.	It is unclear why the residue term can lead to better solutions. Figure 1 is just an explanation of the intuition. More supporting analysis and evidence are needed.

[1] Liu, Jiawei, et al. "Residual denoising diffusion models." Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2024.
[2] Fu, Zhang-Hua, Kai-Bin Qiu, and Hongyuan Zha. "Generalize a small pre-trained model to arbitrarily large tsp instances." Proceedings of the AAAI conference on artificial intelligence. Vol. 35. No. 8. 2021.

### Questions
1.	“X_d can be obtained by connecting vertices in the graph in a sequential order to form a tour.” I think X_d may have a huge impact on the solutions. How to ensure that X_d always guides the correct search direction? In training and testing, X_d is different. How can you ensure the effectiveness of trained model on test data?
2.	MCTS shows better performance than sampling in existing works and Table 3. The authors claim that “Xia et al. (2024) highlight that the MCTS strategy (Fu et al., 2021) heavily relies on TSP-specific heuristics, and is less suited to other problem types.”, but they are still solving TSP in Table 1. It is not reasonable to choose sampling rather than MCTS.
3.	Why the authors choose TSP-5000, 8000, and 10000? Does the proposed method still work on TSP 100, 500, 1000?
4.	In Table 3, why ATT-GCN performs very bad on TSP-5000, 8000 but performs much better and faster on TSP-10000?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
Summary
This paper introduces DISCO, a diffusion-based solver for combinatorial optimization  problems, using denoising diffusion probabilistic models (DDPM) with added solution residues to restrict search space. The forward diffusion process maps ground-truth solutions to a mixture of noise and degraded solutions. The authors also propose an accelerated sampling approach with fewer steps based on decoupled diffusion models (DDM). Experimental results on TSP and MIS demonstrate that the proposed method achieves the improved solution quality and a faster sampling.

### Strengths
Strengths
The paper is well-structured and presents ideas in a clear, logical manner, and easy to read.
The proposed method demonstrates improvements on TSP and MIS.

### Weaknesses
Weaknesses
Incremental Innovation: While DISCO leverages DDPMs for CO problems with the inclusion of solution residues, the approach appears incremental. Prior work on CO tasks has explored conditioning on initial solutions, which limits the novelty here.
The technical methodology seems to follow the conventional DDPM structure closely. A clearer breakdown of the challenges specific to CO and the innovations made by DISCO would strengthen the contribution.
The proposed fast sampling process appears similar to existing DDM techniques, with limited innovation beyond adding residues. 
What is the performance (solution quality and sampling time) of the DIFUSCO baseline with DDM as sampler?
The performance improvement over DIFUSCO is marginal.
The claim regarding DISCO’s multi-modal property requires further justification. How this property enhances solution quality or contributes to CO performance is unclear without additional evidence or explanation.

### Questions
NA

### Soundness
3

### Presentation
3

### Contribution
2
