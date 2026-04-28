# DyCAST: Learning Dynamic Causal Structure from Time Series

- Decision: Accept
- Avg Score: 5.75
- Scores: 6, 8, 6, 3

## Abstract
Understanding the dynamics of causal structures is crucial for uncovering the underlying processes in time series data. Previous approaches rely on static assumptions, where contemporaneous and time-lagged dependencies are assumed to have invariant topological structures. However, these models fail to capture the evolving causal relationship between variables when the underlying process exhibits such dynamics. To address this limitation, we propose DyCAST, a novel framework designed to learn dynamic causal structures in time series using Neural Ordinary Differential Equations (Neural ODEs). The key innovation lies in modeling the temporal dynamics of the contemporaneous structure, drawing inspiration from recent advances in Neural ODEs on constrained manifolds. We reformulate the task of learning causal structures at each time step as solving the solution trajectory of a Neural ODE on the directed acyclic graph (DAG) manifold. To accommodate high-dimensional causal structures, we extend DyCAST by learning the temporal dynamics of the hidden state for contemporaneous causal structure. Experiments on both synthetic and real-world datasets demonstrate that DyCAST achieves superior or comparable performance compared to existing causal discovery models.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The authors introduced the DyCAST algorithm to infer time-variant DAGs from nodal time series, considering both intra-slice and inter-slice dependencies among variables. They demonstrated its performance using both synthetic and real-world datasets and compared it with other causal discovery methods.

### Strengths
1. The authors addressed limitations of previous methods by considering both intra-slice and inter-slice dependencies among variables. 
2. They offered clear and plausible theoretical motivation for their DyCAST algorithm. 
3. The authors tested DyCAST's performance and compared it with previous methods.

### Weaknesses
 1. The authors tested their DyCAST algorithm on datasets with a limited number of variables, which restricts its applicability in real-world scenarios.
2. While incorporating inter-slice dependencies is beneficial, the inference requires more data to be effective.
3. The algorithm relies on multiple independent realizations (runs) of system dynamics (i.e., nodal time series). For instance, in the first synthetic dataset, there are only d=5 variables and T=7 time steps (i.e. 7 snapshots of DAG), yet it requires N=500 independent realizations for inference. This is unrealistic, as many real-world situations may only provide one trial or a single trajectory of each variable.

### Questions
1. The authors used traffic as a motivation and test example; however, traffic networks are not DAGs. Similarly, brain networks also contain many bidirectional edges and feedback cycles. How would the algorithm address situations where the underlying network is a directed graph rather than a DAG?  
2. How should the value of p (i.e., the order of time lag) be set in the algorithm? Is the ground truth for p assumed to be known for the inference process?  
3. How much additional data is needed for inference when considering both intra- and inter-slice dependencies? If unlimited data were available, many other factors could be incorporated into causal discovery. Thus, the amount of required data is critical for addressing general inverse problems. The authors should specify how many realizations are necessary to achieve a given performance for a specific problem defined by the number of variables and time steps. Additionally, if p is unknown during the inference process, the algorithm may require even more data (i.e., independent realizations).

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces DyCAST, a method for determining time-varying causal graphs using constrained neural ODEs. In particular, DyCAST determines the causal graph for a set of variables $\mathbf{X}_t$ as a linear combination of dynamic "intra-slice" causes, $\mathbf{X}_t \mathbf{W}_t$, and static "inter-slice" causes, $\sum\_{k=1}^P \mathbf{X}\_{t-k} \mathbf{A}\_k$, plus additive noise. The dynamics of $W_t$ are modeled as a constrained neural ODE, which is extended to a latent ODE using the encoder-process-decoder framework. The latent state models an autonomous system, but may be concatenated with the time $t$ in decoding for systems with periodic components. Finally, a sparsity penalty is added, and DyCAST is combined with CUTS(+), a Granger-causal method for time-varying inter-slice graphs. Extensive experiments are performed on some limited synthetic data and several real or simulated data sets, where DyCAST with CUTS(+) is typically the best-performing method in terms of AUROC and AUPRC.

### Strengths
- The issue of time-varying causal structure is under-addressed and practical problem. Using constrained neural ODEs is an elegant solution, and the results are impressive.
- The paper is well-written and introduces concepts from neural ODEs very well. The included illustrations are helpful, and the figures are instructive.
- Incorporating time-varying structures can be extremely interpretable in some scenarios. For example, I found Figure 6 very compelling, with causal influences smoothly following the time of day.

### Weaknesses
 **On the Combination With Other Methods**

The combination of DyCAST with CUTS+ is one of the more important contributions in the experiments section of the paper, but is not discussed much. This is especially difficult to me because CUTS+ is a Granger-causal method, and to the best of my knowledge does not actually learn what are referred to as "inter-slice" graphs, except in the trivial $p=1$ case.

It would improve the presentation of the paper to include more details of how DyCAST can be combined with other methods like CUTS+, and also how this changes the computational requirements and potential interpretations. Moreover, as an aside, the paper inconsistently refers to DyCAST-CUTS as using CUTS or CUTS+.

**A Lack of Ablation on Most Datasets**

As mentioned in the strengths, the performance of DyCAST is impressive, and it is apparent that it is beneficial in dynamic problems. That said, I find the ablation study in Section 4.1 very interesting, and would like to see a similar experiment in the NetSim and CausalTime experiments. In particular, from Table 1, it is clear that the latent state provides at least some benefit, even in static problems, but this isn't explored outside of the simplistic synthetic case. I view this as critical to understanding *why* DyCAST is successful.

**Minor Typos**

There are several typos throughout the manuscript; ones I noticed include:
- (Page 2, Line 085) NOTEATS should be NOTEARS.
- (Page 2, Line 087) DYNOTEATS should be DYNOTEARS.
- (Page 3, Line 124) I think $X_{t-k}^j$ should be bolded.
- (Equation 18) In the first summand, there is an $\rvert$ instead of $\rVert$.
- (Page 8, Line 398) NTS-NOTEATS should be NTS-NOTEARS.
- (Page 8, Line 398) TEDCI should be TECDI.
- (Page 10, Line 404) "In future" should be "In the future".
- (Page 13, Line 657) Erdős–R'enyi should be Erdős–Rényi.

**A Few Other Minor Points**

- (Related Work) The approach of CCM is of course much different than the proposed approach -- nevertheless, latent CCM (Brouwer et al., 2021) seems like a relevant application of neural differential equations to causal learning to be mentioned in related work. 
- (Implementation and Code) While I think the details in Appendix A would be sufficient to reproduce most of the paper's experiments, I hope that the authors consider releasing their code with a finalized version of the paper, as I think it strengthens the impact and reproducibility of the paper.

### Questions
- My main question, outlined in weaknesses, is **to what extent can the performance of DyCAST be attributed to the latent state**? For example, in Table 1, the latent state is shown to significantly improve performance; could similar ablation studies be performed in the other experiments?
- There is a brief mention of running time on page 7 ("moreover, DyCAST reduces the running time by more than 20% across various variable dimensions"). This claim is not particularly clear to me: **with respect to what is the running time reduced? At what variable dimension is this noticeable?** Similar claims are made in Appendix A.2.1, but without any specific figures. In general, I think it would improve the manuscript to report the run time of DyCAST with respect to the baselines.
- **What are implementation details for DyCAST-CUTS?** And how does this affect runtime? How are dynamic inter-slice graphs handled outside of the $p=1$ case?
- It seems like the most straightforward approach in the current framework for inter-slice dynamics would be another (independent?) neural ODE on $\mathbf{A}$. Is there a reason why this doesn't work?
- It seems surprising to me that the $F_1$ score is so insensitive to $r$ -- **how would the authors interpret this? Would they expect very small $r$ to be more detrimental in problems with faster dynamics?**
- The methods for comparison are different in NetSim and CausalTime datasets; for example, TECDI is included in NetSim but not CausalTime, and vice versa for LCCM. **Is there a reason for the differing benchmark methods in these sections?** Since both of these methods appear to be the closest competitors to DyCAST, it would be great to standardize the benchmarks, and include both TECDI and LCCM in all comparisons.

### Soundness
2

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
This work presents DyCAST, a novel framework leveraging Neural Ordinary Differential Equations (Neural ODEs) to learn dynamic causal structures, showing superior performance compared to existing models across various datasets.

### Strengths
1. The algorithm effectively supports dynamic contemporaneous structures.

2. The experimental results are compelling, though there are inconsistencies in the choice of baseline methods across different sections (see weaknesses).

### Weaknesses
1. While DyCAST claims to support dynamic intra-slice graphs, the ground truth causal graphs in the Netsim and CausalTime datasets do not contain such dynamics. Therefore, although I appreciate the results in Figure 6, I am concerned that the claim is not fully validated in the quantitative experiments. The synthetic dataset used to demonstrate dynamic intra-slice graphs is limited in scope, with only 7 dynamic graphs and 5 variables, which may not be representative of more complex real-world scenarios. The lack of a more extensive evaluation on datasets with known dynamic intra-slice ground truth limits the generalizability of this claim.

2. Several baseline methods are included in the CausalTime experiments but not in the Netsim experiments. Additionally, the baseline choices differ between the Netsim and Synthetic experiments. Is there a specific reason for this? If not, more baseline comparisons should be included. Specifically, the absence of methods like GC, CUTS+, and LCCM in the synthetic experiments, and TECDI in the Netsim experiments, makes it difficult to assess the relative performance of DyCAST across different settings. The varying choices of baselines across experiments also make it challenging to draw consistent conclusions about the method's strengths and weaknesses.

### Questions
1. As someone who is not an expert in Neural ODEs, I find the model presented in Equation (4) somewhat unconvincing. Why not learn $W_t$ based on the data at each time step? Are there theoretical justifications or ablation studies to support this modeling choice? If this matter is cleared up, I will be happy to raise my score.

2. Are there additional examples that demonstrate the necessity of dynamic intra-slice graphs?

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
4

### Summary
This manuscript investigates dynamic causal structure in time series using Neural ODEs, a topic of broad interest. The authors reformulate the problem of learning causal structures at each time step as finding the trajectory of a Neural ODE on a directed acyclic graph. Finally, simulations were performed on both synthetic and dynamical models to validate the proposed approach.

### Strengths
This paper proposes a method for identifying dynamic causal structure by learning their trajectory using L1 normalization. Both intra-slice and inter-slice structures are learned simultaneously. The method demonstrates higher performance compared to other approaches it is evaluated against.

### Weaknesses
The concept of using activity trajectories to identify causal structure seems intriguing. However, due to a lack of clarity, the novelty of the proposed method remains uncertain. The method is not well explained, particularly regarding the specific mechanisms by which the Neural ODE learns the dynamic causal structure. There are insufficient numerical experiments to support the proposed approach, especially concerning the scalability of the method to larger systems. Several key details are missing, such as a clear explanation of the time intervals between data points and the specific parameter settings for the experiments. The writing and certain claims need refinement, particularly regarding the comparison with existing methods and the practical applicability of the proposed approach. The use of Erdős–Rényi (ER) model for generating initial DAGs with negative weights is questionable and lacks justification, as it does not reflect real-world causal relationships. The manuscript also lacks a clear explanation of how the method handles different types of noise and varying time series lengths, which are critical for assessing its robustness.

### Questions
1)	The rationale of Eq.10. What would happen if the concatenation was removed? An ablation study addressing this would be helpful.
2)	Is this approach applicable to large-scale systems? The results presented in the manuscript only cover 5/50/100 nodes. 
3)	Line 182, is the correct phrasing "neural underlying ODE" or "underlying Neural ODE"?
4)	No information about the $\lambda$ parameter in Eq. 18. 
5)	Why do negative weights appear in Figure 3? This seems unreasonable and counterintuitive. Using a BA synthetic network might be more appropriate.
6)	How does the noise strength affect the performance of the proposed method?
7)	It is unclear why time steps are discussed, but time points are not mentioned. The causal structure detection largely depends on factors like the length of the time series considered, particularly the information at each time point. However, these key details are missing from the manuscript, which raises concerns about the accuracy and applicability of the proposed method.
8)	More rigorous numerical experiments are needed to substantiate the claims made. The current experiments are insufficient to demonstrate the robustness of the proposed method.
9)	I am confused why the authors mentioned time steps, but not mentioned time points at all. Causal structure detection is related to how much information, e.g., the length of time sequences you considered. All these important information is lacking. 
10)	I am surprised that the NetSim dataset includes 100 nodes. Can you provide more details about this dataset?
11)	Figure 5 requires sublabels, and in part (b), there seems to be an error (0, 30, 80, 00). Please review and correct it.

### Soundness
3

### Presentation
2

### Contribution
2
