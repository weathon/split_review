## Human Reviewer 1

### Summary
The authors propose FedSGM, a unified framework for federated constrained optimization that addresses four challenges in federated learning: functional constraints, bidirectional communication compression, multi-step local updates, and partial client participation. Building on the Switching Gradient Method (SGM), FedSGM performs primal-only, projection-free updates that alternate between minimizing the objective and the constraint, enabling feasibility without dual variables. The authors derive convergence guarantees for both hard and soft switching regimes, proving an optimal $\mathcal{O}(1/\sqrt{T})$ rate even with biased compression (via error feedback) and random client sampling. Extensive theoretical analysis covers convex functional constraints, communication noise, and participation variance. Empirical results on Neyman–Pearson classification and constrained MDP tasks demonstrate that FedSGM achieves constraint satisfaction and stable convergence under heterogeneous and lossy federated settings.

### Strengths
- This work tackles a challenge: federated optimization with constraints (such as fairness or safety requirements) in realistic federated learning (FL) conditions, which involve limited communication and sporadic client participation. Previous FL methods primarily address either heterogeneity (FedAvg variants) or constraints (e.g., FedAvg with projection) or compression. 

- By building on the Switching Gradient Method, FedSGM avoids expensive projections or dual updates needed in prior constrained FL approaches (e.g., penalty/ADMM methods).

- The paper provides a rigorous theoretical analysis covering multiple challenging aspects equally. It proves convergence for both hard and soft switching regimes under a broad range of settings (full or partial client participation, with or without compression, and multiple local steps).

- The paper is generally well-written and structured.

### Weaknesses
- The theoretical guarantees rely on the convexity of both the objective and constraint functions (Assumption 1), along with bounded Lipschitz constants and sub-Gaussian noise assumptions. This is a standard assumption for proving $O(1/\sqrt{T})$ rates, but it limits the immediate applicability to realistic federated learning settings (most real federated tasks, such as deep neural network training, are nonconvex).

- Combining constraints, compression, local updates, and partial clients in a single framework is beneficial, but the technical novelty of each component may appear incremental compared to prior art. FedSGM essentially merges well-known techniques, such as switching gradient updates for constraints, error-feedback compression, and multi-step local SGDs (similar to FedAvg), and extends existing analyses to their combined application.

- Although the two case studies are relevant, the experiments are somewhat limited in diversity and scale.

### Questions
- In practice, how does FedSGM handle non-convex objectives? While the theory assumes convex $f_i$ and $g_i$, the experiments involve neural networks and reinforcement learning (both non-convex). Does the algorithm still converge reliably in these settings? 

- Could the authors provide guidance or intuition on selecting the soft switching parameters (such as the smoothing coefficient $\beta$ or threshold $\epsilon$ in the sigmoid function)? How sensitive is FedSGM’s performance to this choice? 

- How does FedSGM compare against simpler baseline approaches for constrained federated learning? For instance, one could run FedAvg with a penalty for constraint violation or project the global model onto the constraint set each round (if feasible).

- The analysis introduces the factor $\Gamma(q,q_0)$ to capture compression in presence of local steps. Could the authors elaborate on how error feedback interacts with multiple local SGD steps?

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
6

### Confidence
3

---

## Human Reviewer 2

### Summary
The paper proposes FEDSGM, a unified framework for federated constrained optimization that simultaneously handles four major challenges: (1) functional constraints, (2) bi-directional communication compression, (3) multiple local updates per round, and (4) partial client participation. Built upon the Switching Gradient Method, FEDSGM adopts a projection-free, primal-only update scheme that avoids dual variable tuning and inner-loop projections. The framework incorporates error-feedback mechanisms to correct compression bias and establishes an $O(1/\sqrt{T})$ convergence rate under convex objectives. Experiments on Neyman–Pearson classification and constrained MDPs demonstrate convergence and constraint satisfaction.

### Strengths
1. The work is the first to combine constraint handling, compression, multiple local steps, and partial participation in a single theoretical framework.
2. The convergence proof carefully separates optimization and sampling errors and analyzes the bias introduced by compression and local drift. Both hard and soft switching variants are theoretically justified.
3. FEDSGM avoids inner projections and dual updates, leading to a lightweight and practical approach for resource-constrained federated systems.
4. Experiments on Neyman–Pearson classification and CMDP tasks confirm the feasibility and stability of the proposed method.

### Weaknesses
1. The theory assumes convex objectives and constraints, which restricts applicability to deep federated learning scenarios. The extension to nonconvex settings is not discussed.
2. Experiments are restricted to small datasets and tabular RL tasks. Results on large-scale or nonconvex benchmarks (e.g., image classification or language models) would greatly strengthen the empirical claims.
3. The experimental section lacks strong comparisons with recent constrained FL baselines (e.g., primal-dual or penalty-based methods), making it difficult to evaluate relative performance.
4. No experiments under heterogeneous data distributions.

### Questions
See weaknesses above.

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
4

### Confidence
3

---

## Human Reviewer 3

### Summary
The paper proposes a unified theoretical framework for federated learning optimization that jointly captures several key aspects: constraints, partial participation, local computation, and bidirectional communication compression with error feedback. The framework generalizes many existing FL methods and, if it indeed recovers their best-known convergence rates across all settings (as claimed), it would constitute a strong theoretical contribution. The paper centers on the functional constraints and considers both hard and soft switching for satisfying them.

### Strengths
- The unification of these aspects of federated learning (local steps, communication compression \& error feedback, partial participation) under one framework is meaningful and relevant. If the framework recovers the best-known convergence rates for all covered scenarios of literature (as claimed), it is worth publishing on its own.

- The authors provide high-probability convergence guarantees for both hard and soft switching.

### Weaknesses
**Constraint formulation**: The novelty and significance of the constraint formulation seem to be overstated. Assumption 3 restricts the generality of the framework, limiting the scope of the unification.
Hard and soft switching closely resemble well-known approaches for minimizing an unconstrained regularized objective, with the regularizer R chosen as: R(w)=0 if G(w)<=\eps and \infty otherwise (see the formulation [1]). In this viewpoint, the literature review seems to be inadequate.

> [1] Condat, Laurent, and Peter Richtárik. "Murana: A generic framework for stochastic variance-reduced optimization." Mathematical and Scientific Machine Learning. PMLR, 2022.

**Practical relevance:**
Practical relevance of the unified framework is unclear: FL is a diverse field, and it is not evident which real-world FL setups require all of the newly-enabled components simultaneously.

**Experimental comparison:**
Experiments are limited and mostly illustrative. I think that there is a lot of missed potential. Having the unified framework, one can also compare the different aspects of the framework to answer fundamental questions of federated learning -- what is more important: to have more clients in partial participation, or to have more bits in the compresion schemes, or to do more local steps?

**Presentation issues:** The paper needs a major revision before considering publishing.  There are missing definitions (convexity, Lipschitz continuity), a lack of formal rigor, and a disjointed and difficult-to-follow narrative.

### Questions
- How is the proposed notion of hard/soft constraint switching connected to projection (or inexact projection) onto the feasible set {w:G(w)<= \eps}?

- Is there a practically significant configuration (e.g., combination of compression, partial participation, local steps, and constraints) that is new and not covered by prior FL works?

- Can the authors provide insights (both theoretical and empirical) on the relative importance of **i)** number of clients in partial participation, **ii)** number of bits in compression, and **iii)*** number of local updates?

### Soundness
3

### Presentation
1

### Contribution
3

### Rating
2

### Confidence
3

---

## Human Reviewer 4

### Summary
This paper introduces FEDSGM, a unified framework for federated constrained optimization designed to simultaneously address four major challenges: functional constraints, communication bottlenecks, multiple local updates, and partial client participation. Proposed approach is built on the Switching Gradient Method (SGM). FEDSGM provides projection-free, primal-only updates, avoiding the need for expensive dual-variable tuning. To manage communication limits, it incorporates bidirectional error feedback to correct bias from compression, and its theoretical analysis explicitly models the interaction between this compression noise and the client drift from multiple local steps. The authors derive convergence guarantees showing the averaged iterate achieves the canonical $\mathcal{O}(1/\sqrt{T})$ rate, with high-probability bounds that isolate the sampling noise from partial participation. Additionally, a "soft switching" variant is proposed to stabilize updates near the feasibility boundary. The framework's efficacy is validated empirically on Neyman-Pearson classification and constrained Markov decision process (CMDP) tasks.

### Strengths
1. The paper provides a rigorous and extensive theoretical analysis of its framework.
2. Well-motivated problems and applications.

### Weaknesses
1. Lack of Empirical Validation: The authors have not compared their proposed method with the state-of-the-art. The experiments (Section 4) only compare FEDSGM against a "Centralized" (i.e., non-federated) version of itself which is an ablation study.
 
2. It demonstrates that the federated setting introduces a performance cost (which is expected) but tells us nothing about whether FEDSGM is better than any other existing method.

3. Communication Efficiency:  In this paper, the authors does not propose a new communication-efficient technique. It merely "incorporates" standard  methods like Top-K compression and Error Feedback. Moreover, their method added new communication overhead. Algorithm 1 explicitly requires a "Constraint query" (lines 3-4) where all clients send their constraint value $g_j(w_t)$ to the server, which then aggregates and broadcasts the switching decision. This is a full, separate communication round-trip that must happen before the main gradient/model update. This added synchronisation step directly contradicts the goal of reducing communication bottlenecks.

### Questions
1. I want to see a detailed comparative analysis with SOTA (e.g., Federated Frank-Wolfe, and other projection-free methods ) to prove the superiority of the proposed approach.

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
4

### Confidence
3

---

## Human Reviewer 5

### Summary
The paper introduces a federated algorithm for IV analysis (FEDIV) via federated GMM (FEDGMM). It formulates FEDGMM as a federated zero-sum game defined by a non-convex non-concave minimax optimization problem. It also shows that the solutions to the federated game satisfies Stackelberg equilibrium satisfying client-local equilibria up to a heterogeneity bias. The work is the first work on federated IV using federated GMM.

### Strengths
1. The work is the first work formulating federated IV via federated GMM. 
2. The solid theoretical results strengthen the work. 
3. The experimental results shows that the federated IV analysis framework is efficient in recovering the GMM estimators.

### Weaknesses
The experimental results in the main body of the paper are limited. The authors could move some of the results from the appendix for the final version of the draft.

### Questions
In Table 1, when using GDA, Fed-DeepGMM performs closer to the DeepGMM compared to when SGDA is used for both. Is there an intuitive reason behind this observation?

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
6

### Confidence
3