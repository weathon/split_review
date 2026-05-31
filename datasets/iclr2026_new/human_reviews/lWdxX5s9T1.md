## Human Reviewer 1

### Summary
This paper introduces RADAR, a scalable neural framework designed to address the limitation of existing neural solvers for Vehicle Routing Problems (VRPs) that primarily rely on symmetric Euclidean distances, which restricts their applicability to real-world scenarios with asymmetric distances (e.g., one-way streets, traffic congestion).  
RADAR tackles asymmetry from both static and dynamic perspectives: for static asymmetry, it uses Truncated Singular Value Decomposition (TSVD) on the asymmetric distance matrix to initialize compact, generalizable node embeddings that capture each node’s role as a source (outbound costs) and destination (inbound costs); for dynamic asymmetry, it replaces standard row-wise softmax normalization with Sinkhorn normalization, which jointly normalizes rows and columns of the attention matrix to enforce balanced bidirectional flow and capture global distance information from both interacting nodes.  
Extensive experiments on 17 synthetic VRP variants (e.g., ATSP, ACVRP) and 3 real-world datasets show that RADAR outperforms SOTA traditional and neural baselines.  
I regard the asymmetric vehicle routing problem as highly significant yet relatively underexplored in current research. The approach proposed in this paper is both novel and interesting; however, its experimental design and results are not very solid. Specifically, the selected baseline algorithms are not specifically tailored for asymmetric vehicle routing problems, limiting the validity of comparative analyses. Additionally, the experimental evaluations only cover out-of-distribution scenarios—where models are trained on instances of size 100 and tested on instances of other sizes—while failing to include in-distribution scenarios, i.e., training on instances across all sizes and subsequent testing on instances of all sizes. This omission undermines the comprehensiveness of the model’s performance verification.

### Strengths
1. The asymmetric vehicle routing problem is not well studied yet, this paper addresses a critical real-world gap by explicitly modeling asymmetric distances (e.g., one-way streets, traffic in vehicle routing problems (VRPs).
2. Features a dual-component design with strong theoretical grounding: Truncated Singular Value Decomposition (TSVD) initializes node embeddings to capture static asymmetry (distinguishing nodes as sources/destinations), while Sinkhorn normalization replaces softmax to model dynamic asymmetry via bidirectional global attention.
3. Demonstrates robust generalization across scenarios: it outperforms both traditional solvers (e.g., LKH3, HGS) and SOTA neural baselines (e.g., ReLD, MatNet) in synthetic multi-task (16 VRP variants) datesets and real-world datasets.
4. Well writing and easy to understand.

### Weaknesses
1. The ACVRP problem has been proposed for a long time, and there have been some dedicated efforts to solve this problem, including heuristic algorithms (e.g. Vigo D. A heuristic algorithm for the asymmetric capacitated vehicle routing problem[J]. European Journal of Operational Research, 1996, 89(1): 108-126.) and meta-heuristic algorithms (e.g. Leggieri V, Haouari M. A matheuristic for the asymmetric capacitated vehicle routing problem[J]. Discrete Applied Mathematics, 2018, 234: 139-150.). This paper does not discuss these previous works.
2. The selected baseline algorithms are not specifically tailored for asymmetric vehicle routing problems, limiting the validity of comparative analyses. 
3. The experimental evaluations only cover out-of-distribution scenarios—where models are trained on instances of size 100 and tested on instances of other sizes—while failing to include in-distribution scenarios, i.e., training on instances across all sizes and subsequent testing on instances of all sizes, weakening result comparability.
4. It lacks an online update mechanism to adapt to real-time dynamic changes (e.g., sudden traffic jams).
5. The results of the ACVRPTW problem in Table 3. The method presented in this paper is not the optimal one, but it is highlighted in bold.

### Questions
I like the asymmetric vehicle routing problem and the idea of this article, but the current experimental results cannot fully demonstrate the effectiveness of this idea. If the author could provide additional explanations regarding the effectiveness of the idea, I would be happy to raise my rating score.
1. It is suggested to conduct comparative experiments on algorithms specifically designed to solve the ACVRP problem(e.g. heuristics and meta-heuristics).
2. The experimental design should incorporate in-distribution scenarios, specifically involving training the model on instances spanning all node sizes and subsequently evaluating its performance on test instances of all sizes.
3. The results in Table 5 indicate that the existing baseline algorithms are designed for symmetric structure problems and its performance will deteriorate in the case of asymmetry. Therefore, maybe the authors could compare the experimental results of the algorithm proposed in this paper and the baseline algorithm in the symmetric structure scenario?
4. Regarding the ATSP and ACVRP problems, maybe the authors could add the experimental results of the HGS algorithm?

### Soundness
2

### Presentation
3

### Contribution
3

### Rating
4

### Confidence
3

---

## Human Reviewer 2

### Summary
The paper proposes RADAR, a neural framework for solving Vehicle Routing Problems (VRPs) with asymmetric distance matrices. RADAR addresses both static and dynamic asymmetries via two key components that learn asymmetry-aware embeddings. For static asymmetry, it applies Singular Value Decomposition (SVD) to the input distance matrix to obtain asymmetry-aware node embeddings. For dynamic asymmetry, i.e., asymmetries that emerge during encoder attention, RADAR replaces the standard softmax with Sinkhorn normalization within the attention mechanism.

### Strengths
1.	The SVD-based embedding is simple yet empirically effective. The motivation is clearly articulated and technically convincing.

2.	The paper presents extensive experiments across multiple datasets and VRP variants, providing solid empirical support for the method’s effectiveness.

### Weaknesses
While leveraging SVD to encode matrix asymmetry is a valuable idea, the current contribution is confined to routing problems. Asymmetric (Directed) edge structures widely exist in other graph-based combinatorial optimization tasks. This scope limitation reduces the broader impact and significance of the work. If the authors could extend the idea from routing distance asymmetry to general graph asymmetry and validate it on a more diverse set of problems, the contribution would be substantially strengthened.

### Questions
The proposed SVD-based embedding appears tailored to attention-based models. Although attention mechanisms are mainstream in many domains, it remains important to assess effectiveness under alternative network architectures. Such an analysis would clarify whether the observed gains are specific to certain architectures or are more generally applicable. Could the authors provide a discussion and, if possible, experiments on the choice of network architecture?

### Soundness
3

### Presentation
2

### Contribution
2

### Rating
6

### Confidence
3

---

## Human Reviewer 3

### Summary
The paper addresses the problem of learning to solve vehicle routing problem,
esp. with asymmetric distances. The authors propose a method with two 
aspects:
- i) to concatenate the left and right eigenvectors of the SVD of the distance
  matrix as customer features (replacing customer coordinates of the symmetric
  case), and
- ii) to make the attention matrix doubly stochastic with a Sinkhorn transform
  (instead of making it row stochastic by a softmax).

In experiments on synthetic and real TSP and CVRP problems they show
that their method outperforms existing neural routing methods, esp. 
for larger out-of-distribution instances, e.g., for ACVRP100 only by 0.3%,
but for ACVRP1000 by 38%

### Strengths
- s1. two simple ideas: using left and right eigenvectors for asymmetric distances and making attention
  doubly stochastic.
- s2. many experiments, also some on different problem variations.
- s3. well written.

### Weaknesses
- w1. ablation study and thus the attribution of improvement to the two ideas is not fully clear.
- w2. performance of OR heuristics is not fully clear.
- w3. why the performance improvements are so much larger for larger problems or 
  out of distribution problems is not investigated.
- w4. small methodological contribution: adding the eigenvectors is basically feature engineering the asymmetric
  distance matrix characteristics of the problem.

more details:

w1. ablation study and thus the attribution of improvement to the two ideas is not fully clear.
- You could add eigenvector features basically to any method with customer features.
- And you could use the Sinkhorn normalization with any method involving on attention.
- Which of the two contributions, 
  - i) using eigenvectors of the distance matrix as customer features and 
  - ii) making the attention matrix douvly stochastic 
  is contributing how much to the success of the method?
- The example you provide in fig. 5 is problematic:
  - You compare on ATSP100, but on ATSP100 lifts of your method are very small.
    It might be more convincing to also compare on ACVRP1000 where you have substantial lifts.
  - You report for your method RADAR w/o sinkhorn an objective value of ~1.5925,
    but in tab. 1 your closest baseline ReLD+ achieves an slightly even better objective:
	1.5900. So in this case, adding eigenvectors seems not to help?

w2. performance of OR heuristics is not fully clear.
- Why is the OR solver HGS not compared in tab. 1 and 3?
- Why do we not see runtimes in tab. 2? W/o. runtimes comparing VRP solvers is not so meaningful.

w3. why the performance improvements are so much larger for larger problems or 
out of distribution problems is not investigated.
- This is an odd phenomenon: on the problems you train for, ACVRP100, you see only
  a very small lift of 0.3%, but then on the larger out-of-distribution instances, e.g., 
  for ACVRP1000 the lift is a substantial 38%. Which aspect of your method 
  is responsible for this behavior?

w4. small methodological contribution: 
- adding the eigenvectors is basically feature engineering the asymmetric
  distance matrix characteristics of the problem.

Small points:
- p1. It would be helpful to show in tab. 1 which of the baselines have access to which problem 
  information such as the asymmetric distance matrix, the demands etc.

### Questions
- q1. Can you separate the effects of your two contributions i) and ii) clearly in an ablation study?
  Which of the baselines can be equipped with features i) or doubly stochastic attention scores ii)
  and how do they perform then?
- q2. How does HGS perform on problems in tab. 1 and 3? Do you really observe
  a lift over OR heuristics?
- q3. Your method performs better esp. in larger out-of-distribution settings. Can you explain or
  provide some first analysis why this happens?

### Soundness
3

### Presentation
3

### Contribution
2

### Rating
4

### Confidence
4

---

## Human Reviewer 4

### Summary
This paper addresses the challenge of solving asymmetric vehicle routing problems (AVRPs) with neural solvers. The authors propose RADAR, a framework that modifies existing neural solvers to handle asymmetric distance matrices. The contribution is twofold: (1) an SVD-based initialization to encode static asymmetry into compact node embedding, and (2) the use of Sinkhorn normalization in the attention mechanism. The authors validate RADAR on a wide range of synthetic and real-world asymmetric VRPs, showing superior performance and generalization compared to baselines.

### Strengths
1. The paper is well-written, and the methodology is explained clearly.

2. The conceptual framing of the problem into "static" and "dynamic" asymmetry is interesting, providing a new perspective for addressing asymmetric routing problems.  

3. The experimental evaluation is a major strength. It is comprehensive, rigorous, and includes a wide array of benchmarks

4. The empirical evaluation showcases the strong performance of the RADAR compared to the SOTA baseline, especially in out-of-distribution generalization to larger problem sizes.

### Weaknesses
1. The paper's contribution lies in the clever application of existing techniques rather than the development of fundamentally new methods. Both SVD and Sinkhorn normalization are standard, well-established algorithms. While the engineering is solid, the work feels more incremental than transformative from a methodological standpoint.

2. In Table 1, the authors state that all retrained baselines were evaluated using z-score normalization. However, the authors do not justify why this specific normalization was uniformly applied. Applying a non-native normalization may unfairly penalize baseline performance, making it unclear if the comparison was conducted under optimal conditions for all methods.

3. The paper uses different normalizations for different datasets. However, the paper provides no ablation study to compare the effect of z-score versus min-max (or no normalization) on the same dataset. It remains unclear whether the impressive performance gains are fully attributable to the proposed SVD and Sinkhorn modules or are partially an artifact of a specific, un-analyzed normalization choice. 

4.  The ablation study in Table 6 severely weakens the case for the SVD-based initialization as a standalone contribution. The RADAR-SVD performs very poorly on larger-scale problems, achieving a gap of over 20% on ATSP1000. This poor generalization suggests that the strong performance is critically dependent on the Sinkhorn operation.

5. Some critical hyperparameters' details are missing. For example, the number of iterations T for Sinkhorn normalization is not specified. It is unclear whether the increasing number of iterations significantly increases the computational load and performance of the model.

### Questions
1. To verify the necessity of the proposed SVD initialization, could you provide results for two models that keep all other settings unchanged (including z-score normalization) and combine Sinkhorn normalization with forward-only distance features (i.e., top-10 nearest outgoing neighbors) and bidirectional distance features (i.e., concatenating top-10 outgoing and top-10 incoming neighbor distances), respectively?

2. What is the number of iterations T used for Sinkhorn normalization?

While the empirical performance of RADAR is promising, I have concerns regarding its technical novelty and the true attribution of improvement to claimed components.

### Soundness
2

### Presentation
3

### Contribution
2

### Rating
4

### Confidence
4