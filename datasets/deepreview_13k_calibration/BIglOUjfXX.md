# Forked Diffusion for Conditional Graph Generation

- Decision: Reject
- Avg Score: 4.00
- Scores: 3, 5, 5, 3

## Abstract
We introduce a novel score-based diffusion framework that incorporates forking for conditional generation. In this framework, a single  parent diffusion process is associated with a primary variable (e.g., structure), while multiple child diffusion processes are employed, each dedicated to a dependent variable (e.g., property). The parent process guides the co-evolution of its child processes towards segregated representation spaces. This approach allows our models to manage conditional information flow effectively, uncover intricate interactions and dependencies, and ultimately unlock new generative capabilities. Our experimental results demonstrate the significant superiority of our method over contemporary baselines in the context of conditional graph generation, highlighting the potential of forking diffusion for enhancing conditional generation tasks and inverse molecular design tasks.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper works on conditional graph generation via score-based generative model. Instead of directly input conditional properties as context to model inside generation, the paper proposes to use a separate variable to model each conditional property and jointly model them inside the score-based diffusion framework. The author tested it over many real-world datasets, including molecular datasets and generic graphs. The proposed method shows better performance to naive conditional diffusion models.

### Strengths
1. The proposed method is easy-to-follow, and the written is clear.
2. While being a simple extension via introducing additional variables for conditional properties inside diffusion process, the method shows better performance comparing to use these properties as context input directly. 
3. The author did a relatively comprehensive evaluation on many datasets and properties.

### Weaknesses
1. The proposed method is kind of a simple extension to current SDE diffusion models. There is not much technique improvement except introducing additional variables for these conditional properties inside the SDE process. The core idea of modeling conditional properties with separate variables, while intuitive, lacks substantial technical depth or novel insights into the underlying diffusion process itself. The method essentially adds more variables without fundamentally altering the diffusion mechanism, raising concerns about its overall contribution.
2. Most importantly, as the author just directly introducing these additional variables (with a simple conditional independent assumption among properties given the graph), the properties are not aligned with the intermediate graphs during the SDE process. This makes the method not very reasonable. For example, as there is no direct correspondance between graphs and properties, it is possible that the generated properties are not aligning with the generated graph. The alignment between property and graph at individual level is very important, all experiments don't have evaluation on this individual alignment. Only population-level MAE for these properties are evaluated. This lack of alignment is a critical flaw, as it undermines the core premise of conditional generation. The method could generate a graph with a specific property at the population level, but individual graphs might not exhibit the desired property, which is a significant limitation.
3. In the experiment of generic graph generation, I don't see a clear difference of the population-level MAE between the proposed method and naive baseline GDSS, which may indicates that the method is not very effective. The marginal improvement in performance over a baseline suggests that the method's effectiveness is questionable, especially when considering the added complexity of introducing additional variables. The lack of a substantial performance boost raises concerns about the practical utility of the proposed approach.
4. Table 6 shows the result over unconditional generation, although this is not the intention of the designed method, I'm curious why the baseline only include GDSS-seq instead of the original GDSS. The choice of baseline in this experiment is not well-justified, and it is unclear why the original GDSS was not included for comparison. This raises questions about the fairness and completeness of the evaluation.
5. Figure 3, ego-small should be the right one?

### Questions
1. Can you summarize what you want to prove inside Appendix A.2? I'm kind of confused as I believe the reverse SDE formulation is a well-known result that is directly used.

### Soundness
2 fair

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a forked diffusion model for conditional graph generation that introduces parent process and child processes to learn and generate graphs with desired properties. The contributions of this paper include introducing forking as a new technique for conditional generation, providing a rigorous mathematical framework using SDE, and demonstrating the versatility of the proposed forked diffusion with empirical evidence.

### Strengths
1.	The forked diffusion framework for graph generation is novel.

### Weaknesses
1. The motivation behind the proposal of forked diffusion is not clear in the introduction. While the categories of related work are presented, it is unclear what deficiencies these methods have compared to the proposed approach. Specifically, the introduction lacks a clear articulation of the limitations of existing conditional graph generation methods that the forked diffusion model aims to address. It is not sufficient to simply categorize related work; the authors need to pinpoint specific shortcomings in those methods that justify the introduction of a forked approach.
2. The related work is not comprehensive enough, as recent diffusion-based methods such as Digress [1], etc., have not been mentioned. The omission of recent and relevant diffusion-based graph generation methods weakens the paper's positioning within the current research landscape. A more thorough literature review is needed to establish the novelty and contribution of the proposed method.
3. Given the computational demands of the diffusion model, I believe that the application of the forked diffusion model to large-scale datasets may be even more challenging. The authors should compare the proposed model's training and generation efficiency with related work on large-scale datasets such as Guacamol. The paper should include a discussion of the computational complexity of the proposed forked diffusion model, and provide empirical evidence of its scalability, especially when compared to existing methods on large datasets.
4. In the conditional generation experiments, experiments on large-scale datasets and additional baselines for comparison should be included. Especially for the task of molecular generation, it would be beneficial for the authors to include recent methods such as DiGress [1], MiCaM [2], MolHF [3], etc. The experimental section lacks sufficient breadth and depth. The absence of comparisons with state-of-the-art methods on standard large-scale datasets limits the evaluation of the proposed method's performance and practical applicability.

### Questions
1. It is unclear why the molecular metrics results for the Zinc dataset are not presented in Table 3.
2. It is unclear why there is no comparison of unique metrics in Table 6.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work presents conditional diffusion framework for graph generation by proposing forked diffusion processes, that models the graph diffusion process as a single parent process over a primary variable (i.e., structure) and multiple child processes over dependent variables, further including additional context. This work provide experimental results on diverse graph generation tasks showing improved generation performance over continuous graph diffusion model GDSS and other generative models.

### Strengths
- This work propose new graph diffusion framework by modeling a system of joint diffusion processes with explicit dependency conditions, e.g., dependency of child variables on parent variable, and additional context. 

- The experimental results on diverse tasks demonstrate that FDP improves generation performance over other graph diffusion models, especially GDSS.

### Weaknesses
 - Explanation on key components lacks details:
  1. What do the structure variable ($x_s$) and child variables ($x_p$) actually represent during the experiments? It is unclear how these variables are defined in the context of graph generation, specifically what aspects of the graph they encode (e.g., adjacency matrix, node features, edge features). Without this information, it is difficult to assess the validity of the proposed approach.
  2. What does the models ($s_{\phi_i, t}$) approximate? The paper mentions that these models approximate the coupling between child and parent variables, but it lacks a precise definition of what this coupling represents mathematically. Is it a conditional probability, a gradient, or something else? The lack of clarity makes it difficult to understand the core mechanism of the proposed method.
  3. How is the training objective derived? Is it a straightforward extension of score matching objective? The paper states that the training objective is based on score matching, but it does not provide the explicit mathematical formulation. It is unclear how the forked diffusion processes are incorporated into the score matching objective, and whether any modifications are introduced to handle the conditional dependencies.

- Several claims made in the paper are not clear and requires justification:
  1. ( as explained in Intro) How does the parent process guide the childe processes? From what I have understood, the paraent process and child processes are dependent to each other rather than specific process guiding others, similar to the processes of GDSS. In particular, the proposed diffusion framework seems to be a system of multiple processes (parent and childs) with some dependency conditions given betwen the variables, and the score functions are dependent to all the variables including additional context. The paper claims that the parent process guides the child processes, but the mechanism for this guidance is not clearly explained. It is not evident how the parent process influences the reverse diffusion of the child processes, and whether this influence is different from the dependencies in existing methods like GDSS.
  2. Is the assumption on independence between child variables valid for the experiments? As what I have understood, the child variables represent some chemical properties, for which do not seem to be independent to each other. The assumption of independence between child variables is questionable, especially when these variables represent chemical properties that are often correlated. The paper needs to provide a more detailed justification for this assumption and discuss its potential impact on the results.
  3. (at the end of Sec. 3.4 and Tab. 1) What does the energy guidance mechanism indicate? Why is the additional influence of $s_{\phi_i}$ characterized as an energy guidance? The term 'energy guidance' is used without a clear definition. It is not clear how the additional influence of  $s_{\phi_i}$ relates to an energy function, and why this interpretation is appropriate.

- As FDP requires multiple score models (for the primary and child variables), I presume the number of model parameters required  for FDP would be quire large. Ablation study on number of model parameters could strengthen the effectiveness of the proposed framework.

- Important experimental details, for example, model architecture or what the variables actually represents, are not provided in the main paper. There seems to be some explanation in Appendix B, but not referenced by the main paper.

- The reason for superior performance on unconditional molecule generation (Sec. 4.4) is not clear. Especially, an important baseline, GDSS, seems to be missing in Tab. 6.

- Missed some previous works on conditional graph generation:
  - Vignac et al., DiGress: Discrete Denoising diffusion for graph generation, ICLR 2023
  - Lee et al., Exploring Chemical Space with Score-based Out-of-distribution Generation, ICML 2023

### Questions
- Please address the questions in the Weakeness section.

- Is the Wiener processes ($\\mathrm{d}\\textbf{w}$) in Eq. (2) independent?

- Recent works (e.g., DiGress) find that using Graph Transformer architecture (instead of GNN-based architecture of GDSS) shows improved generation performance. Does FDP show similar improvement over GDSS when using the Transfomer architecture?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes the forked diffusion process, featuring one parent process on graph structures and children processes for distinct properties. The method is assessed using the QM9 and ZINC250K datasets in comparison to baselines. While the concept sounds interesting, the current study does not support the authors' conclusion (quoted below) on the last page.

> Specifically, FDP demonstrates exceptional capabilities in the domains of conditional graph generation for molecular structures, inverse
molecule design tasks, and the generation of generic graphs, surpassing contemporary diffusionbased methods. 
>

### Strengths
1. The idea of incorporating forking into the diffusion process sounds reasonable.

2. The algorithm presented on page 6 is concise and aids in understanding the method.

### Weaknesses
W1: The paper lacks specific details on how the diffusion processes operate on graph structures and node features. Figure 1 illustrates the 3-D molecular structure; however, it remains unclear how, or if, these 3-D positions are integrated into the study. The description of how the diffusion process handles node features is also missing, specifically how the noise is added and removed from the node attributes. The paper should clarify whether the node features are discrete or continuous and how this affects the diffusion process.

W2: Some claims regarding contributions appear overstated. Recent research [1,2] indicates that achieving high levels of novelty, uniqueness, and validity on QM9 and ZINC250K is not particularly challenging; for instance, merely adding carbons can suffice. It's evident from recent studies [1,2] that both the genetic algorithm [3] and the reinvent method [5] serve as potent baselines. This paper should benchmark against a broader set of baselines to truly showcase its performance in molecular design tasks. Furthermore, molecular properties such as plogp and qed are often deemed impractical [1] and not truly beneficial for real-world inverse molecule design tasks. The paper should justify the choice of these properties or consider more relevant ones.

W3: In GDSS, node features and graph structures are treated as separate diffusion processes. The connection between this approach and the proposed method requires deeper exploration. It is unclear how the forking diffusion process integrates with the separate diffusion processes used in GDSS. The paper should clarify how the proposed method differs from simply running separate diffusion processes for each property and the graph structure.

W4: The assumption that "the properties are independent conditioned on the structure" in Equation 15 is unjustified and not reliable. This assumption needs to be supported by experimental evidence or a theoretical justification. The paper should discuss the limitations of this assumption and its potential impact on the results.

Other minor points:

W5: The pictures should be of higher resolution.

W6: There are several typos, such as the "}" symbol, in Figure 1.

W7: Definitions of the variables should be clarified. For instance, the dimension of the variable y is not clearly stated. It is also unclear if y is a vector or a scalar, and how it relates to the properties being modeled.

### Questions
1. Is it possible to include more baselines like the DiGress [1] for comparisons? 

2. Some molecular structures in Figure 2 do not appear reasonable. Could the authors provide further analysis?

Ref.

[1] DiGress: Discrete Denoising diffusion for graph generation. ICLR 2023.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair
