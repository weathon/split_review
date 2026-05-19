## Summary
# Final Review Report

## Summary
This paper addresses the challenging problem of federated learning (FL) with local openset noisy labels, where clients observe disjoint subsets of the global label space and suffer from label noise. The authors argue that existing centralized noisy-label methods (e.g., loss correction, memorization-based approaches) fail in this setting due to incomplete transition matrix estimation and local overfitting. To mitigate this, they propose FedDPCont, a framework that shares differentially private (DP) contrastive labels across clients to regularize local training. The paper provides theoretical guarantees showing that FedDPCont calibrates distributed updates to match centralized peer loss expectations, and demonstrates empirical improvements over several baselines on synthetic and real-world benchmarks. While the problem formulation is practical and the DP-protected label communication is a creative solution, the manuscript requires stronger theoretical grounding for the contrastive loss, clearer experimental reproducibility details, and more rigorous positioning against recent FL noisy-label baselines.

## Strengths
1. **Practical Problem Formulation**: The paper identifies a highly relevant and underexplored setting in FL: openset noisy labels, where clients observe disjoint class subsets with noise. This combination of label space fragmentation and noise corruption is common in real-world multi-center scenarios (e.g., medical imaging, regional e-commerce) but lacks dedicated solutions.
2. **Creative DP-Protected Communication**: The proposal to share differentially private contrastive labels to regularize local training is innovative. It elegantly bypasses the need for explicit transition matrix estimation while preserving label privacy, addressing a key bottleneck in federated noisy-label learning.
3. **Theoretical Calibration Guarantee**: Theorem 2 provides a solid theoretical foundation by showing that the aggregated distributed updates match centralized peer loss expectations under asymptotic conditions. This bridges the gap between federated optimization and centralized robust learning theory.
4. **Comprehensive Empirical Validation**: The experiments cover multiple noise models (symmetric, random), varying noise rates, and both synthetic and real-world datasets (CIFAR-N, Clothing-1M). The consistent outperformance over strong baselines (FedAvg, FedProx, LC, Co-teaching) demonstrates the method's robustness and practical utility.

## Weaknesses
1. **Imprecise Motivation for Contrastive Loss**: The intuition behind Eq. (3) relies on the claim that a random private label is "likely to be a wrong label," which is mathematically imprecise. The core mechanism is actually that the second term acts as a regularizer derived from the global label distribution, pushing the model away from overfitting to local noisy patterns. Without explicitly connecting this to peer loss (Liu & Guo, 2020), the theoretical grounding appears weak.
2. **Missing Experimental Reproducibility Details**: The experimental setup omits crucial implementation details, including the number of clients, the exact strategy for generating openset partitions (e.g., Dirichlet concentration parameter or explicit class allocation probabilities), and the hyperparameter tuning protocol for baselines. This limits reproducibility and raises concerns about fair comparison.
3. **Implicit Theoretical Assumptions**: Theorem 2 claims that distributed updates match centralized expectations but implicitly assumes infinite data size and exact DP calibration. The finite-sample gap between FedDPCont and centralized training is acknowledged but not bounded or analyzed, leaving the practical impact of DP noise on convergence unclear.
4. **Weak Positioning Against Strongest Baselines**: The related work section reads as a list and does not explicitly contrast FedDPCont with the strongest direct competitors, such as FedCorr (Xu et al., 2022) or semi-supervised noisy label methods adapted to FL (e.g., DivideMix). The novelty claim would be stronger with a clear categorical comparison highlighting the openset gap in prior FL noisy-label works.
5. **Overclaiming in Abstract and Contributions**: The abstract states that both DP guarantee and effectiveness are "theoretically guaranteed," but the effectiveness guarantee is vague. Additionally, "efficiency" is used to describe accuracy improvements, which is a terminology mismatch. The contributions paragraph mixes theoretical and empirical claims without clear separation.

## Key Issues
1. **Lack of Explicit Peer Loss Connection**: The contrastive loss Eq. (3) is functionally equivalent to a federated adaptation of peer loss, but the manuscript does not explicitly state this. Without this connection, the regularization mechanism appears ad-hoc, and the theoretical robustness claims lack a clear lineage to established noisy-label literature.
2. **Insufficient Experimental Reproducibility**: The absence of client count, openset partition generation strategy, and baseline hyperparameter tuning details prevents independent verification of the results. Reviewers cannot assess whether the performance gains stem from the method or favorable tuning/partition choices.
3. **Unbounded Finite-Sample Theoretical Gap**: Theorem 2 provides an expectation-level guarantee but does not bound the deviation caused by DP noise and finite client participation. In practice, DP calibration introduces variance that could destabilize training, especially under high noise rates or small client subsets.
4. **Missing Comparison with Strongest FL Noisy-Label Baselines**: The evaluation omits recent methods like FedCorr (Xu et al., 2022) and DivideMix adaptations. Since these methods address noisy labels in FL, their exclusion weakens the claim that FedDPCont is the superior solution for openset noise.
5. **Terminology and Claim Overreach**: The abstract and contributions use imprecise terminology ("efficiency" for accuracy, "theoretically guaranteed" for empirical effectiveness) that overstates the current evidence. Tighter scoping is needed to maintain scientific credibility.

## Actionable Suggestions
1. **Explicitly Connect to Peer Loss**: Revise Section 3.2 to explicitly frame Eq. (3) as a federated adaptation of peer loss (Liu & Guo, 2020). Clarify that the second term acts as a regularizer derived from the global label distribution, which cancels out noise bias in expectation. This will strengthen the theoretical motivation and align the method with established robust learning theory.
2. **Enhance Experimental Reproducibility**: Add a dedicated subsection detailing the FL partition strategy (e.g., number of clients, Dirichlet concentration parameter or explicit openset allocation probabilities), baseline hyperparameter tuning protocol, and communication budget constraints. Ensure all baselines are evaluated under identical rounds $R$ and local epochs $E$.
3. **Bound the Finite-Sample Theoretical Gap**: Extend the discussion around Theorem 2 to explicitly state the assumptions (infinite data, exact DP calibration) and provide a brief analysis or empirical bound on the deviation caused by DP noise and finite client participation. This will address reviewer concerns about practical convergence stability.
4. **Include Strongest FL Noisy-Label Baselines**: Add comparisons with FedCorr (Xu et al., 2022) and a lightweight adaptation of DivideMix to the FL setting. If computational constraints prevent full DivideMix evaluation, include it in the appendix with a clear justification and discuss the trade-offs between accuracy and training time.
5. **Tighten Terminology and Claims**: Replace "efficiency" with "accuracy" or "robustness" in the abstract and contributions. Rephrase "theoretically guaranteed" to "theoretically calibrated" or "asymptotically consistent" to accurately reflect the expectation-level nature of Theorem 2. Split the contributions into clear theoretical, methodological, and empirical points.

## Storyline Options + Writing Outlines
### Abstract Outline (Complete)
- **S1 (Problem & Domain)**: Federated learning enables collaborative training while preserving privacy, yet practical deployments often suffer from heterogeneous and noisy local labels.
- **S2 (Challenge/Gap)**: When clients observe only a subset of the global label space (openset setting), existing centralized noisy-label solutions fail due to local overfitting and incomplete transition matrix estimation.
- **S3 (Proposed Method)**: We propose FedDPCont, a framework that shares differentially private (DP) contrastive labels across clients to regularize local training and mitigate openset noise.
- **S4 (Theoretical Guarantee)**: We theoretically prove that FedDPCont calibrates distributed updates to match centralized peer loss expectations while preserving label privacy.
- **S5 (Empirical Result)**: Extensive experiments on synthetic and real-world benchmarks demonstrate that FedDPCont consistently outperforms existing FL and noisy-label baselines in accuracy and robustness.

### Introduction Outline (Complete)
- **P1 (Big Picture & Motivation)**: Establish the prevalence of label space heterogeneity and noise in real-world multi-center FL (e.g., medical imaging, regional e-commerce). Replace the virus example with a direct openset scenario to immediately align reader intuition.
- **P2 (Problem Definition)**: Formally define the openset noisy label problem, highlighting why local clients cannot estimate the global noise transition matrix or rely on memorization effects due to small, imbalanced local datasets.
- **P3 (Failure of Prior Work)**: Categorize existing noisy-label methods into transition-matrix-dependent and memorization-based approaches, explicitly stating why each fails under openset FL assumptions.
- **P4 (Proposed Solution & Intuition)**: Introduce the core idea of sharing DP-protected contrastive labels to approximate the global label distribution. Explicitly connect the contrastive loss to peer loss regularization, clarifying how global sampling cancels noise bias.
- **P5 (Contributions)**: List four sharp contributions: (1) Problem formulation & failure analysis, (2) FedDPCont framework with DP communication, (3) Theoretical calibration guarantee, (4) Comprehensive empirical validation on synthetic and real-world benchmarks.

## Priority Revision Plan
| Priority | Action Item | Expected Impact | Effort |
|---|---|---|---|
| **P0** | Explicitly connect Eq. (3) to peer loss regularization and clarify the global sampling intuition. | Strengthens theoretical grounding and addresses core motivation gap. | Low |
| **P0** | Add experimental reproducibility details: client count, openset partition strategy, baseline tuning protocol. | Ensures fair comparison and enables independent verification. | Low |
| **P1** | Extend Theorem 2 discussion to explicitly state asymptotic assumptions and bound finite-sample DP noise impact. | Improves theoretical rigor and addresses convergence stability concerns. | Medium |
| **P1** | Include comparisons with FedCorr and a lightweight DivideMix adaptation (main text or appendix). | Positions method against strongest direct competitors. | Medium |
| **P2** | Tighten abstract/contributions terminology: replace "efficiency" with "accuracy", rephrase "theoretically guaranteed". | Improves scientific credibility and claim-evidence alignment. | Low |
| **P2** | Restructure Related Work into categorical taxonomy (FL non-IID, Centralized Noisy, FL Noisy) with gap statements. | Sharpens novelty positioning and improves readability. | Low |

**Execution Strategy**: Begin with P0 writing revisions (1-2 days), then implement P0 experimental detail additions (1 day). Proceed to P1 theoretical extension and baseline comparisons (3-5 days). Finally, polish P2 terminology and related work structure (1-2 days). This phased approach ensures high-impact validity fixes are completed before stylistic improvements.

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory
| Exp ID | Objective/Hypothesis | Setup (Data/Protocol/Baselines) | Metrics | Main Outcome | Claim Supported | Current Limitation |
|---|---|---|---|---|---|---|
| E1 | FedDPCont outperforms baselines under synthetic openset noise. | CIFAR-10/100, Symmetric/Random noise $\eta \in \{0.2, 0.4, 0.6, 0.8\}$, FedAvg/LC/FedProx/etc. | Best Accuracy | Consistent gains across noise rates. | Method effectiveness | Missing client count/partition details. |
| E2 | FedDPCont generalizes to real-world noisy datasets. | CIFAR-N, Clothing-1M, same baselines. | Best Accuracy | Outperforms baselines on natural noise. | Practical utility | Real-world noise not explicitly openset. |
| E3 | DP level $\epsilon$ has minimal impact on performance. | CIFAR-10, Random $\eta=0.4$, $\epsilon \in \{1, 2, 4, 8, 100, 3.58\}$. | Accuracy | Stable performance across $\epsilon$. | DP robustness | Limited to one dataset/noise setting. |
| E4 | FedDPCont is more efficient than DivideMix. | CIFAR-10/100, DivideMix vs FedDPCont. | Accuracy, Time (hr) | FedDPCont faster with competitive accuracy. | Efficiency claim | DivideMix not adapted to openset setting. |

### Research-Theme Gap Diagnosis
The current experiments validate accuracy gains but lack ablation studies isolating the contribution of the contrastive term vs. the DP calibration. Additionally, the real-world datasets (CIFAR-N, Clothing-1M) do not explicitly simulate openset label spaces, limiting the external validity of the "openset" claim.

### Proposed Research Experiments (P0/P1/P2)
| Target Claim | Hypothesis | Minimal Design | Controls/Baselines | Metrics | Success Criterion | Est. Cost | Expected Gain |
|---|---|---|---|---|---|---|---|
| Causal role of contrastive term | Removing the contrastive term degrades performance to FedAvg levels. | FedDPCont w/o contrastive term (only DP labels shared). | FedDPCont full, FedAvg. | Accuracy | Significant drop without contrastive term. | Low | Isolates mechanism contribution. |
| Openset generalization | FedDPCont maintains gains under extreme label space fragmentation. | Vary number of classes per client (e.g., 20% vs 80% overlap). | FedAvg, FedCorr. | Accuracy, Variance | Stable performance under high fragmentation. | Medium | Validates openset robustness. |
| Finite-sample DP impact | Higher DP noise ($\epsilon \to 0$) increases variance but maintains mean accuracy. | Multi-seed runs ($\ge 5$) across $\epsilon \in \{0.5, 1, 2, 4\}$. | FedDPCont, Centralized Peer Loss. | Mean±Std Accuracy | Variance bounded, mean consistent with theory. | Medium | Bounds theoretical gap empirically. |

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score**: 6/10

**Rationale**: The paper addresses a practical and underexplored problem (openset noisy labels in FL) and proposes a creative DP-protected contrastive learning framework with solid empirical results. However, the score is moderated by the imprecise theoretical motivation for the contrastive loss, missing experimental reproducibility details, and weak positioning against the strongest FL noisy-label baselines. The expectation-level theoretical guarantee is valuable but lacks finite-sample analysis, and the abstract/contributions overclaim effectiveness guarantees.

**Post-Revision Target**: [7, 8]/10

**Path to Target**: Explicitly connecting the method to peer loss regularization, adding comprehensive reproducibility details (client count, partition strategy, baseline tuning), and including comparisons with FedCorr/DivideMix would significantly strengthen the theoretical grounding and empirical credibility. Tightening the terminology and bounding the finite-sample theoretical gap would further improve scientific rigor, making the paper highly competitive for acceptance.