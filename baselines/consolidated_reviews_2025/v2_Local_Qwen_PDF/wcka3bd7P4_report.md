## Summary
# Final Review Report

## Summary
This paper introduces FROND (FRactional-Order graph Neural Dynamical network), a continuous GNN framework that replaces integer-order differential equations with Caputo fractional derivatives ($D_t^\beta$) to model memory-dependent feature updating dynamics. The authors provide a non-Markovian random walk interpretation for the fractional diffusion process and theoretically prove that FROND exhibits a slow algebraic convergence rate ($\Theta(t^{-\beta})$), contrasting with the exponential convergence of traditional models. This property is leveraged to mitigate oversmoothing in deep GNNs. Empirically, the framework is validated by extending several integer-order continuous GNNs (e.g., GRAND, CDE), demonstrating consistent performance improvements, particularly on tree-structured and heterophilic datasets, without adding backbone parameters.

## Strengths
1. **Novel Theoretical Interpretation:** The paper provides a compelling non-Markovian random walk interpretation for fractional graph neural diffusion. Proving the algebraic convergence rate ($\Theta(t^{-\beta})$) versus the exponential rate of integer-order models offers a rigorous theoretical foundation for understanding memory effects in continuous GNNs.
2. **Effective Oversmoothing Mitigation:** By linking the slow algebraic convergence to practical oversmoothing mitigation, the authors address a critical challenge in deep GNNs. The empirical validation showing stable performance up to 128-256 layers is highly convincing and demonstrates the practical utility of the framework.
3. **Framework Compatibility and Generality:** FROND is designed as a drop-in extension for existing integer-order continuous GNNs (GRAND, CDE, GREAD, etc.). The experiments across diverse datasets (citation, tree-structured, heterophilic) consistently show performance gains without introducing additional trainable parameters to the backbone, highlighting the framework's efficiency and broad applicability.
4. **Insightful Parameter Analysis:** The ablation studies on the fractional order $\beta$ reveal meaningful insights, particularly the correlation between smaller $\beta$ values (stronger memory) and tree-structured/fractal datasets. This adds valuable interpretability to the method.

## Weaknesses
1. **Computational Complexity of Full Memory:** The non-local nature of fractional derivatives requires storing and computing over the entire history of feature updates, leading to $O(T^2)$ time and memory complexity for integration time $T$. While the short memory principle is mentioned, its impact on the theoretical convergence guarantees and practical performance trade-offs could be discussed more thoroughly in the main text.
2. **Limited Discussion on $\beta$ Optimization Strategy:** The optimal $\beta$ is determined via hyperparameter tuning. The paper does not discuss whether $\beta$ can be learned end-to-end or adapted per-node/per-layer, which could be a valuable extension. The current grid-search approach might be computationally expensive given the need to retrain the model for each $\beta$.
3. **Speculative Claims on Fractality:** The connection between the optimal $\beta$ and the fractal dimension of graph datasets is an interesting observation but remains somewhat speculative. The paper claims that $\beta$ can "unearth insights into the inherent fractality," but this is not rigorously validated as a generalizable metric across diverse graph types.
4. **Solver Variants Performance Variance:** The ablation on solver variants (Table 8) shows that the short memory solver with $K=10$ performs slightly worse on Cora. The paper does not deeply analyze why certain solvers or memory window sizes might degrade performance on specific topologies, leaving a gap in practical implementation guidance.

## Key Issues
1. **Computational Overhead vs. Performance Gain Trade-off:** The primary key issue is the computational cost of the full memory mechanism. For large integration times $T$, the $O(T^2)$ complexity can become a bottleneck. The paper relies on the short memory principle as a mitigation but does not provide a comprehensive analysis of how truncating memory affects the theoretical algebraic convergence rate or the practical oversmoothing mitigation capability.
2. **Lack of End-to-End $\beta$ Learning:** Treating $\beta$ as a fixed hyperparameter tuned via grid search limits the framework's adaptability. Different nodes or layers might benefit from different memory dependencies. The absence of a learnable $\beta$ mechanism is a missed opportunity to fully "unleash the potential" of fractional calculus in GNNs.
3. **Generalizability of Fractality Claims:** The claim that optimal $\beta$ correlates with graph fractality is intriguing but currently supported by limited datasets (Cora, Citeseer, Pubmed, Airport, Disease). Without broader validation across diverse graph topologies (e.g., random graphs, small-world networks), this claim risks being an overgeneralization from a small sample.

## Actionable Suggestions
1. **Introduce Learnable or Adaptive $\beta$:** Instead of fixing $\beta$ via grid search, consider making $\beta$ a learnable parameter (e.g., $\beta = \sigma(w_\beta)$) or node-adaptive (e.g., $\beta_i$ per node). This would allow the model to automatically adjust memory dependency based on local graph structure, potentially improving performance and reducing tuning overhead.
2. **Analyze Short Memory Impact on Convergence:** Provide a theoretical or empirical analysis of how the short memory principle (truncating history at window $K$) affects the algebraic convergence rate. Does a smaller $K$ reintroduce exponential-like smoothing? A plot showing convergence rate vs. $K$ would be highly informative.
3. **Expand Fractality Validation:** Validate the $\beta$-fractality correlation on a broader set of synthetic and real-world graphs with known fractal dimensions (e.g., Barabási-Albert, Watts-Strogatz). This would strengthen the claim that $\beta$ serves as a geometric lens for graph topology.
4. **Clarify Solver Selection Guidelines:** Provide clearer guidelines on when to use the basic predictor vs. predictor-corrector vs. short memory solvers. Discuss the trade-offs between numerical accuracy, task accuracy, and computational cost more explicitly to help practitioners choose the right solver for their use case.

## Storyline Options + Writing Outlines
### Abstract Outline (Complete)
- **S1 (Problem & Domain):** Graph Neural Networks (GNNs) based on integer-order differential equations suffer from Markovian limitations, capturing only local instantaneous changes and struggling with oversmoothing in deep architectures.
- **S2 (Significance/Challenge):** Modeling long-term memory dependencies is crucial for effective information propagation, especially on complex topologies like tree-structured or heterophilic graphs.
- **S3 (Prior Gap):** Existing continuous GNNs lack a mechanism to naturally incorporate historical feature states without explicit architectural modifications like residual connections.
- **S4 (Proposed Method):** We introduce FROND, a framework employing Caputo fractional derivatives ($D_t^\beta, \beta \in (0,1]$) to generalize continuous GNNs with memory-dependent dynamics.
- **S5 (Key Result & Implication):** Theoretically, we prove FROND exhibits slow algebraic convergence, mitigating oversmoothing. Empirically, FROND consistently enhances various continuous GNNs across diverse datasets without adding backbone parameters.

### Introduction Outline (Complete)
- **P1 (Big Picture):** GNNs excel in diverse domains, with continuous GNNs offering robustness and flexibility via differential equations.
- **P2 (Gap):** However, integer-order derivatives are inherently local (Markovian), limiting their ability to model long-term dependencies and leading to rapid feature smoothing (oversmoothing) in deep networks.
- **P3 (Solution Intuition):** Fractional calculus, widely used in physics for memory-dependent systems, offers a natural solution. By generalizing the derivative order to $\beta \in (0,1]$, we can embed historical memory into feature updates.
- **P4 (Method & Evidence):** We propose FROND, providing a non-Markovian random walk interpretation and proving algebraic convergence. Experiments on tree-structured and heterophilic graphs demonstrate significant performance gains and robustness to extreme depth.
- **P5 (Contributions):** (1) Generalized fractional continuous GNN framework. (2) Theoretical non-Markovian interpretation and oversmoothing mitigation proof. (3) Comprehensive empirical validation across multiple continuous GNN backbones.

## Priority Revision Plan
| Priority | Action Item | Expected Impact | Effort |
| :--- | :--- | :--- | :--- |
| **P0** | **Clarify Short Memory Impact:** Add a discussion or small experiment analyzing how the memory window size $K$ affects the algebraic convergence rate and oversmoothing mitigation. | Strengthens theoretical-practical alignment and addresses computational complexity concerns. | Low |
| **P0** | **Bound Fractality Claims:** Revise the introduction and conclusion to frame the $\beta$-fractality correlation as an exploratory observation rather than a proven generalizable metric. | Improves scientific rigor and prevents overclaiming. | Low |
| **P1** | **Introduce Learnable $\beta$ Experiment:** Add a small ablation study where $\beta$ is treated as a learnable parameter (e.g., $\beta = \sigma(w_\beta)$) to demonstrate potential performance gains and reduced tuning overhead. | Enhances framework adaptability and practical utility. | Medium |
| **P1** | **Expand Solver Guidelines:** Provide clearer recommendations on solver selection (predictor vs. corrector vs. short memory) based on dataset size and desired accuracy. | Improves reproducibility and practitioner guidance. | Low |
| **P2** | **Broaden Fractality Validation:** Validate the $\beta$-fractality trend on synthetic graphs (e.g., Barabási-Albert) to support the geometric interpretation. | Strengthens the interpretability narrative. | Medium |

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory
| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| E1 | F-GRAND improves node classification | Cora, Citeseer, Pubmed, Coauthor, Computer, Photo, ogbn-arxiv, Airport, Disease | Accuracy (%) | F-GRAND outperforms GRAND and baselines, especially on tree-structured graphs. | Framework compatibility & performance gain | Limited to specific continuous GNN backbones. |
| E2 | F-GRAND mitigates oversmoothing | Cora, Citeseer, Airport (fixed split) | Accuracy vs Depth (4-256 layers) | F-GRAND maintains performance at 128-256 layers; GRAND degrades rapidly. | Oversmoothing mitigation via algebraic convergence | Does not analyze memory window $K$ impact on convergence. |
| E3 | Optimal $\beta$ varies by topology | Cora, Airport | Accuracy vs $\beta$ | Larger $\beta$ for Cora, smaller $\beta$ for Airport. | $\beta$ tailored to dataset topology; fractality link | Fractality claim not rigorously validated across diverse graphs. |
| E4 | F-CDE enhances heterophilic performance | Roman-empire, Wiki-cooc, Minesweeper, Questions, Workers, Amazon-ratings | Accuracy (%) | F-CDE improves over CDE on most heterophilic datasets. | Framework generality to other continuous GNNs | Limited discussion on why $\beta$ helps heterophily. |

### Research-Theme Gap Diagnosis
The core research value lies in introducing memory-dependent dynamics to continuous GNNs. The current experiments strongly support performance gains and oversmoothing mitigation. However, the gap lies in **computational efficiency analysis** (impact of short memory $K$ on theoretical guarantees) and **adaptability** (fixed $\beta$ vs. learnable $\beta$).

### Proposed Research Experiments (P0/P1/P2)
| Target Claim | Hypothesis | Minimal Design | Controls/Baselines | Metrics | Success Criterion | Est. Cost | Expected Gain |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Short Memory Impact | Truncating memory at $K$ preserves algebraic convergence for sufficiently large $K$. | Vary $K \in \{5, 10, 20, 50\}$ on Cora/Airport; measure accuracy and feature variance at depth 128. | Full memory ($K=T$), GRAND-l | Accuracy, Feature Variance | Accuracy stable for $K \ge 20$; variance decay rate remains algebraic. | Low | Validates practical efficiency without theoretical compromise. |
| Learnable $\beta$ | End-to-end learning of $\beta$ adapts memory to local structure, improving performance. | Set $\beta = \sigma(w_\beta)$; train on Cora/Airport. | Fixed optimal $\beta$ (grid search) | Accuracy, Training Time | Learnable $\beta$ matches or exceeds fixed $\beta$ with less tuning. | Medium | Enhances framework adaptability and reduces hyperparameter search. |
| Fractality Validation | Optimal $\beta$ correlates negatively with graph fractal dimension. | Generate synthetic graphs (BA, WS) with known fractal dims; tune $\beta$. | None | Accuracy vs Fractal Dim | Clear negative correlation trend across synthetic graphs. | Medium | Strengthens geometric interpretability of $\beta$. |

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
Final Score: 7/10
Post-Revision Target: [8, 9]/10

**Justification:**
The paper presents a novel and theoretically grounded framework (FROND) that effectively addresses the oversmoothing problem in continuous GNNs through fractional calculus. The non-Markovian random walk interpretation and the proof of algebraic convergence are significant theoretical contributions. Empirically, the framework demonstrates consistent performance improvements across diverse datasets and backbones without adding trainable parameters, showcasing strong practical utility.

The score is held at 7 primarily due to the lack of deep analysis on the computational trade-offs of the short memory principle and the somewhat speculative nature of the fractality claims. Addressing the key issues—particularly by validating the impact of memory truncation on convergence and exploring learnable $\beta$—would significantly strengthen the paper's rigor and adaptability, justifying a post-revision target of 8-9.