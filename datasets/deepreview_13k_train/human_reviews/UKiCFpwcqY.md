# SenseFlow: A Physics-Informed and Self-Ensembling Iterative Framework for Power Flow Estimation

- Decision: Reject
- Scores: 3, 6, 6, 5

## Abstract
Power flow estimation plays a vital role in ensuring the stability and reliability of electrical power systems, particularly in the context of growing network complexities and renewable energy integration. However, existing studies often fail to adequately address the unique characteristics of power systems, such as the sparsity of network connections and the critical importance of the unique Slack node, which poses significant challenges in achieving high-accuracy estimations. In this paper, we present SenseFlow, a novel Physics-Informed and Self-Ensembling Iterative Framework that integrates two main designs, the Physics-Informed Power Flow Network (FlowNet) and Self-Ensembling Iterative Estimation (SeIter), to carefully address the unique properties of the power system and thereby enhance the power flow estimation. Specifically, SenseFlow enforces the FlowNet to gradually predict high-precision voltage magnitudes and phase angles through the iterative SeIter process. On the one hand, FlowNet employs the Virtual Node Attention and Slack-Gated Feed-Forward modules to facilitate efficient global-local communication in the face of network sparsity and amplify the influence of the Slack node on angle predictions, respectively. On the other hand, SeIter maintains an exponential moving average of FlowNet’s parameters to create a robust ensemble model that refines power state predictions throughout the iterative fitting process. Experimental results demonstrate that SenseFlow outperforms existing methods, providing a promising solution for high-accuracy power flow estimation across diverse grid configurations.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper aims to solve the powerflow equations for phase and voltage using a version of graph neural network designed to include the global influence of the slack node. Inspired by the historical solution methodology of classical Gauss-Seidel and Newton-Raphson based nonlinear solvers, the approach adopts a iterative solution methodology to refine solution estimates to reduce solution residual. Performance is compared to various alternative convolutional graph neural network solutions to the problem.

### Strengths
The paper adapts some concepts from the classical iterative solution of the powerflow equations to attain higher performance than competitive network based solution. There is a recognition that the global solution requires global communication despite the local connectivity pattern of the graph.

### Weaknesses
The paper doesn’t appear to compare performance to classical solution methodologies, stress test the methodology in scenarios where the classical solution nonlinearly diverges due to fractal solution basin, or scale to problem sizes incompatible with classical solution methodologies. Once in the basin of convergence, the iterative methods have characterized convergence properties. It is not clear this is the case with this method as it is not shown how hard the randomized test conditions and small topology changes without demonstrating failure with classical methods. The classical methods also seem quite old. Slow convergence of local iterative solvers has been a known issue for a long time which has spurred development of scalable solver technologies. Compared to such work as in more recent algebraic multigrid solution methods as in “Nonlinear Algebraic Multigrid for the Power Flow Equations”, LLNL-JRNL-717563 (2017) running up to 2,383 node networks. The fact that Fig 4(a) is a linear-linear convergence plot rather than semilog as in Fig.1 of that reference highlights that there isn’t a good apples-apples comparison vs. traditional solution methodologies. However, the multigrid solver shows 1e-6 residuals in 16 iterations with the IEEE 300-Bus Network which does not inspire confidence that the comparison includes SoA classical methods for reference. Comparing FLOPs or wall clock of a modern classical solver vs. iterating with a 21.844M parameter network would also be important. Further, comparing scaling into large networks with O(n)/iteration computational cost with n^.3 nonlinear iteration growth is a critical component since a 300 node network does not represent a particular challenge for modern scalable classical solvers.

While I do not have high familiarity with the other referenced NN-based solution methodologies, the sheear number of assorted graph/convolutional NN approaches to this powerflow problem suggest that methods like algebraic multigrid do not perform well by comparison. The test cases chosen just do not provide a compelling case that the proposed methodology overcomes the perceived challenges of very old classical solution methods. This problem seems to be exactly the type of problem such scalable methods were designed to overcome and they show nothing like scaling to 2^14 or node network sizes or beyond, and so it’s just not clear this method would even successfully scale up and train for realistic problem sizes of the type indicated as the problem motivation.

### Questions
How does the proposed methodology scale to large problems relative to modern scalable solvers?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposed a physics-informed and self-ensembling framework, SesneFlow to estimate the state of power systems variables. Particularly, this framework considers different properties of power system nodes, such as PV bus, PQ bus and slack bus, as well as the power balance equations in their fomulation. For the framework, it is consisted of two components, FlowNet and SeIter. From the case studies, it shows great improvement of using SeIter with previous GNN or GCN framework for the same type of problems.

### Strengths
1. It considers different charateristics of power systems, nodes type and power balance equations, with GCN to more accurately and reasonably estimate power flows.
2. The SeIter seems can stand alone to improve the accuracy of power flow estimation with other methods.
3. The effectiveness of proposed SenseFlow is well investigated and compared with different cases.

### Weaknesses
I cannot find some convincing statement or description of how the SensFlow can handle the limitations of existing methods for solving power flow problems, which I detailed in the questions section below.

I could not find the detailed settings and parameters of their framework for the case studies, such as how many layers of VNA and SGF they have, how long does the training take, etc.

### Questions
1. My background is more on power systems, so I don't think the limitation of estimating power flows is mentioned as sparse connectiveity limiting information exchange (line 80-83). I do agree with the authors that the expansion of power networks and integration of renewable energy sources can influence the power system analyses, but there seems not much detailed explanation about it and how SenseFlow can handle it (line 44-46).

2. The input for SenseFlow is not clear to me. Do you only need the node information and features (voltage, power injection) or also include edge information (resistance and reactance) to compute the power balancing over the system? If so, how to incorporate this information with FlowNet and/or SeIter?

3. From equation (7)-(9), it seems like you already know the node type and input data of the case. However, for different types of bus, PV, PQ, and Slack, their states/variables are different, how do you contact the node features? Normalize the data and them use node attention, Pooling, and cross attention? Could you please give more details of how to replicate your framework?

4. For equation (7)-(12), could you please explain more about them? Maybe include the explaination of them in appendix, like the purpose of F_fuse, what is Concat function, Linear function, AvgPool, MaxPool etc.

5. I didn't find some information, such as how many layers of VNA and SGF you used in your FlowNet for your case study (paramter K), how long does it take to train, and the requirement/parameters of SeIter to stop power flow estimation. Could you please include them in the paper or appendix? For the supplementary file, I only find code but no appendix. And the dataset folder doesn't have the case information/file.

6. Some typos, page 5, line 232; page 6 line 308, I believe you want to use PQ node instead of PV node as example.

### Soundness
3

### Presentation
2

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
This paper tries to design a power flow estimation framework that effectively handles both the unique structural characteristics of power systems (sparse connectivity and the special role of the Slack node) while maintaining high accuracy through iterative refinement. Accurate and reliable power flow estimation in power systems is important to power system stability and reliable operation. Changes in buses in the system can impact overall system balance and thus power flow calculations need to be performed timely and frequently. But modern grid complexity, network sparsity and slack node make this estimation challenging. For example, existing GNN based methods heavily rely on graph connections which is lacking in power system topology and therefore struggle with the sparsity in the power system networks.

The authors proposed a novel framework, SensFlow, with two key components to address the challenges. FlowNet uses Virtual Node Attention (VNA) and Slack-Gated Feed-Forward (SGF) to handle network sparsity while enabling global information flow and enhance slack node's influence on predictions. FlowNet addresses the challenges GNN faces with domain knowledge in power systems (physics-informed). The second key component is SeIter uses iterative self-ensembling mechanism to improve accuracy through iterative refinement.

The solution is evaluated on 3 datasets and outperforms baselines in most cases. The effectiveness of each components is evaluated through an ablation study.

### Strengths
- The paper is well motivated and addresses an important issue: reliable and accurate power flow estimation in electrical power systems
- The proposed solution addresses each challenge with a reasonable design. FlowNet with VNA for network sparsity and SGF for slack node importance. SeIter for accuracy requirement through self-ensembling iterative estimation.
- The paper is well organized and presented.
- The proposed solution shows good performance in the evaluation.

### Weaknesses
- The authors mentioned "This makes power flow estimation not only essential but also highly frequent in operational contexts", but did not clearly show the requirements. What's the timing and accuracy requirements for such estimation? Without such information, it's hard to assess if the proposed solution is practical. The iterative approach may help with the prediction accuracy but could increase the inference time compared to traditional or end-to-end methods. A discussion of the timing and accuracy requirement as well as a discussion of the computation overhead of the proposed solution may be needed.
- What's the convergence properties and criterion for SeIter?
- The design decisions, while seemingly reasonable, appear to lack some comparison and justification with alternative designs. Could you use other global information sharing mechanism? Any other ways to incorporate slack node influence? Why EMA for self-ensembling?

### Questions
- Could you describe the timing and accuracy requirements for the estimation?
- Could you describe the computation overhead of the proposed solution?
- What's the convergence criterion and properties? E.g., does it always converge?
- Have you explored alternative designs and how did you arrive at VNA and SGF?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper tackles the challenge of accurately estimating power flow in electrical systems, especially given the increasing complexity of modern grids and the integration of renewable energy sources. It proposes a novel approach, SenseFlow, that incorporates the unique characteristics of power systems, including network sparsity and the critical role of the slack node. SenseFlow combines physics-informed modeling with self-ensembling iterative estimation for enhanced power flow analysis. To address the distinct features of power systems, it introduces specialized components such as Virtual Node Attention and Slack-Gated Feed-Forward modules, designed to capture these key elements effectively.

### Strengths
•	Novel integration of physics-informed modeling and self-ensembling for power flow estimation

•	Attention to unique characteristics of power systems (network sparsity, Slack node importance)

•	Potential for high-accuracy power flow estimation across diverse grid configurations

### Weaknesses
Major:

•	“With the recent expansion of power networks in scale and complexity, particularly with the integration of renewable energy sources, these conventional methods fail to provide timely and accurate solutions” lacks a proper reference to support this claim.

•	Key Reference Missing: The paper omits an important comparison with Donon et al.'s work on "Neural networks for power flow: Graph neural solver." This reference should be incorporated, along with a comparative analysis, to position SenseFlow more effectively within the field.

•	The 'Related Work' section at the end of the paper should appear in the introduction, as at the end of the paper, it makes it difficult to understand the novelty and unique contributions of the proposed approach.

•	It is only in section 2.2 that it becomes clear that the aim is to solve the AC power flow equations; this critical point should be addressed earlier in the paper.

•	The paper only compares GNN models without providing key details such as hyperparameters or specifying the loss function used in the experiments.

•	There is a lack of comparison with traditional power flow methods like Newton-Raphson and Gauss-Seidel, which could provide valuable context for evaluating the model's performance.
•	The paper does not include a section dedicated to discussing its limitations.

Minor:
•	The manuscript exceeds the recommended length of 9 pages.

•	Several typos are present, such as ‘physic’ instead of ‘physics’, extra brackets in section 2.1 when listing variables, and mistakes like ‘giving’ instead of ‘given’ and unclear formatting in section 3.4 (loop ¿).

•	The term ‘pure student’ in Figure 4 should be clarified in the figure caption to avoid confusion.

### Questions
How do the distinctive characteristics of power systems, such as network sparsity and the critical role of the slack node, benefit from SenseFlow compared to other methods? Could you provide more explicit results or analyses to support the claim that incorporating these features improves performance? I found the statement: *“However, none of these studies thoroughly examine the distinctive characteristics of power systems, such as network sparsity and the critical role of the slack node. Differently, we explore these features and deliberately incorporate them into our network designs.”* to be unsupported by a thorough analysis of these distinctive characteristics. Clearer evidence demonstrating their impact on SenseFlow's effectiveness would strengthen the argument.

### Soundness
2

### Presentation
1

### Contribution
2
