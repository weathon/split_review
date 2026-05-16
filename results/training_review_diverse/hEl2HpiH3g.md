Now I have all the information I need to produce the final consolidated review. Let me compose it.

## Summary

The paper proposes FedJETs, a federated learning system that combines a Mixture-of-Experts (MoE) framework with a pretrained "common expert" feature extractor and a learned gating function to achieve zero-shot (just-in-time) personalization for unseen clients. The key ideas are: (1) using a frozen pretrained model's embeddings to route client data to the most relevant experts, (2) an "anchor clients" mechanism that pre-selects clients with distinct distributions to stabilize expert specialization, and (3) sparse expert selection (K ≪ M) for communication efficiency. Experiments on CIFAR-10 and CIFAR-100 show strong accuracy figures (91.8–95.7% on CIFAR-10, 75.7–78.6% on CIFAR-100) with ablations characterizing the required quality threshold of the common expert and the anchor client ratio.

## Strengths

- **Novel combination of frozen common expert embeddings + learned gating for FL personalization**: The gating function uses a pretrained model as a fixed feature extractor to route samples to the most relevant experts (Section 4, lines 165–176). This design is architecturally agnostic and avoids retraining the large common expert. The ablation in Figures 2–3 demonstrates a clear accuracy threshold (~66% on CIFAR-100) below which routing collapses and above which the system improves — a valuable diagnostic for practitioners.

- **Significant zero-shot personalization accuracy on standard benchmarks**: FedJETs achieves 91.8%/95.7% on CIFAR-10 and 75.7%/78.6% on CIFAR-100 under two common expert regimes (Table 1). These figures are substantially above the baselines tested in the paper. The paper correctly identifies this as a challenging just-in-time (no fine-tuning) scenario.

- **Anchor clients mechanism with clear ablation evidence**: The idea of pre-selecting M clients with distinct distributions to anchor each expert is principled. The ablation in Figure 5 (referred to as Figure \ref{fig:cifar10_sampling}) shows that removing anchor clients causes the method to collapse to the common expert baseline, while a 30–50% anchor ratio yields stable gains. This gives the community a concrete mechanism to study.

- **Communication efficiency via sparse expert selection**: Unlike FedMix which transmits all M experts to every client, FedJETs sends only K=2 experts per round (Table 1 uses M=5 or 10, K=2). This is a practical advantage for bandwidth-limited FL deployments.

- **Comprehensive ablation on common expert quality threshold**: The paper identifies a "phase-transition" baseline accuracy (~66%) below which the gating function fails (Figures 2–4). This sensitivity analysis is more informative than typical single-point evaluations and helps practitioners assess whether the method is applicable to their setting.

## Weaknesses

### Fatal
None.

### Major

- **Asymmetric baseline comparison inflates the claimed gains.** The common expert (ResNet-34 pretrained on the full CIFAR dataset, achieving 93% on CIFAR-10) is a centrally trained model with access to all data — it is never trained under FL constraints. FedJETs uses this model's embeddings for free in its gating function. The baselines (FedAvg, FedProx, FedMix) are trained entirely from scratch under the FL protocol without access to any such pretrained model. This is not a head-to-head comparison of the MoE routing mechanism; it conflates the method's contribution with the advantage of having a strong centralized pretrained feature extractor. The paper partially addresses this with Table 2 (initializing all experts from the common expert), but even there FedJETs uniquely benefits from the common expert's embeddings in the gating function while the baselines do not. **The claimed "up to 18% improvement"** (abstract) and the conclusion's statement that "the second best state of the art method achieves ~58%" on CIFAR-10 are misleading: FedProx achieves 71.4% (teal column, Table 1) on CIFAR-10, which is substantially better than the 58.4% of FedAvg that the conclusion apparently references. The gap shrinks from the implied 37 points to ~24 points when compared against the actual best competitor, and neither comparison controls for access to the pretrained common expert.

- **FedMix baseline is surprisingly weak with no explanation.** FedMix achieves only 31.3% on CIFAR-10 (Table 1), which is barely above random (10%) on a 10-class problem. Since FedMix is the most directly comparable MoE-based FL baseline, this anomalous result casts doubt on whether the hyperparameters were properly tuned. The paper concedes difficulty tuning Scaffold (line 274) but offers no similar admission or analysis for FedMix. Because the main comparison table is the paper's central quantitative evidence, this unaddressed discrepancy undermines the reliability of the reported margins.

- **Conclusion overstates the relative improvement over the strongest competitor.** In the conclusion (line 355), the paper claims "the second best state of the art method achieves ~58% and ~74%, respectively." On CIFAR-10 (teal column), the actual second-best method is FedProx at 71.4%, not FedAvg at 58.4%. This misrepresentation inflates the apparent margin of FedJETs (95.7% vs. 71.4% = 24.3 points, not 95% vs. 58% = 37 points). While 24 points is still substantial, the paper should report this accurately.

### Minor

- **No statistical variability reported.** No standard deviations, confidence intervals, or multiple-seed runs are reported for any experiment. Given the stochasticity in client sampling, expert selection, and model initialization, a single run per configuration is insufficient to establish that the observed gains are significant. This is a standard expectation for empirical ML papers.

- **Anchor client assumption limits generality.** The method requires pre-identifying M clients with "roughly distinct" distributions and controlling their participation frequency. The ablation shows the method fails without anchor clients (Figure \ref{fig:cifar10_sampling}). In many real-world FL deployments, client participation is uncontrolled, distributions shift over time, and identifying representative anchor clients a priori may be impractical. The paper acknowledges "we assume we have some control over the activation of the clients" (line 337) but does not discuss how anchor clients would be selected in practice or whether the method is robust to misspecified anchors.

- **No quantitative communication or computation cost analysis.** The paper qualitatively claims communication efficiency (sending K=2 rather than all M experts) but provides no wall-clock time, parameter count comparisons, or FLOPs measurements. Since each expert is a full ResNet-34, sending K=2 experts per client implies roughly 2× the downstream communication of a standard FL round, plus the gating MLP. A quantitative breakdown would strengthen the efficiency claim.

### Trivial

- Figure 3 (ranker breakpoint) y-axis is labeled "Accuracy" but it is unclear whether this is expert accuracy, gating accuracy, or overall zero-shot personalization accuracy. The caption says "Zero-shot personalization accuracy per expert" (line 321), but the top panel's y-axis label should match.

## Nice-to-Haves

- A breakdown of per-client accuracy (e.g., histogram) would show whether the improvement is systematic or driven by a few favorable clients.
- Reporting global test accuracy (on the full held-out test set) in addition to zero-shot personalization would help assess whether personalization comes at the cost of overall performance.
- A sensitivity analysis of anchor client selection (e.g., randomly sampling different sets of M clients as anchors, reporting variance) would strengthen claims about robustness.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"Figure 1 (problem setting) is referenced but not included in the text"** — The paper contains `\input{ICLR/fig_1}` (line 118). The figure is included in the original submission; the extracted text does not render figures. This is a parser artifact.
- **"The caption's violet/teal colors are not defined"** — The caption of Table 1 (lines 265–266) explicitly defines the colors: "a) The violet lower bound model... b) The teal average model." The reviewer missed this.
- **"Missing appendix / missing proofs"** — The parser strips appendix content from all papers. No such criticism is valid.
- **"No discussion of how many classes per client"** — The paper states "partition the data samples by classes to turn full datasets into non-i.i.d. subsets" (line 89) and "In the CIFAR10 scenario, each client has fewer classes" (line 272). This is adequately described.
- **Various formatting/typo nitpicks** — These are parser artifacts, not author errors.
- **"M=5 experts for CIFAR-10 with 10 classes" as a weakness** — Having fewer experts than classes is a design choice, not a flaw. The method is not required to have one expert per class.
- **Strength Finder strength about "communication efficiency" is kept** as it is specific and backed by the paper's design (K=2 vs all M experts).
- **Strength Finder's generic strengths** (e.g., "this paper addressed an important problem") are removed as they lack specific content.

## Novel Insights

The reviews converge on a central tension: the paper's core technical contribution (learned gating using frozen common-expert embeddings + anchor clients for expert specialization) is genuinely novel and well-motivated, but the experimental validation conflates this contribution with the advantage of having a centrally pretrained feature extractor. The most revealing observation across the reviews is that the ablation in Table 2 (initializing all experts from the common expert) narrows the FedJETs advantage to ~9 points on CIFAR-100 (83.27% vs. 74.10%), which is more attributable to the routing mechanism itself — but this table is buried in the ablation section rather than presented as a controlled comparison. The existence of a phase-transition threshold (~66% common-expert accuracy) below which the method fails is an insightful finding that the paper should foreground more prominently, as it both bounds applicability and provides a practical diagnostic.

## Suggestions

1. **Redesign the main comparison table to control for the pretrained common expert.** Either: (a) initialize all baselines from the common expert (as in Table 2) and report that as the primary comparison, or (b) add a transfer-learning baseline (FedAvg fine-tuned from the common expert) to isolate the benefit of the routing mechanism. The current Table 1 should be supplementary, and the conclusions should reflect the controlled comparison.

2. **Report statistical variability.** Run each experiment with at least 3 different seeds and report mean ± std. This is especially important given the stochastic client selection and the surprising FedMix result.

3. **Explain or fix the FedMix baseline.** Either tune FedMix properly to reach competitive performance, cite published results that show competitive numbers under similar non-i.i.d. partitions, or at minimum acknowledge the discrepancy and explain the likely cause (e.g., extreme non-i.i.d. partition that particularly harms ensemble/MoE methods with too few experts).

4. **Correct the conclusion's claim about "second best" accuracy.** The 58% figure on CIFAR-10 corresponds to FedAvg, not the actual second-best method (FedProx at 71.4%). Report the gap to the strongest competitor honestly.

5. **Discuss the practical feasibility of anchor clients.** Provide guidance on how anchor clients would be identified in realistic FL deployments (e.g., using metadata, clustering of common-expert embeddings, or random assignment with verification) and what happens when the anchor assumption is misspecified.

## Score and Decision

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>