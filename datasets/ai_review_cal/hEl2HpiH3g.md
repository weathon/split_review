- Decision: Reject
- Avg Score: 4.75
- Scores: 5, 5, 6, 3
Now I have a thorough understanding of the paper. Let me consolidate my analysis and write the final review.

---

## Summary

FedJETs proposes a federated learning system combining multiple independent ResNet34 experts (Mixture-of-Experts), a frozen pretrained "common expert" used as a feature extractor, and a learned gating function to route each client's data to the most relevant experts. The goal is zero-shot personalization for unseen clients without fine-tuning. A key design element is "anchor clients" — pre-selected clients with distinct label distributions that are activated more often and assigned to specific experts to encourage specialization. Experiments on CIFAR10 and CIFAR100 report up to 95.7% and 78.6% accuracy respectively, outperforming FedAvg, FedProx, FedMix, and Average Ensembles.

## Strengths

1. **Large accuracy gains over baselines in zero-shot personalization.** In Table 1, FedJETs achieves 91.8% (CIFAR10, lower-bound common expert) and 75.7% (CIFAR100, lower-bound), exceeding the best baseline (FedProx) by 19.1 p.p. and 2.9 p.p. respectively. Under the average common-expert setting, margins are larger (95.7% vs 71.4% on CIFAR10). These gains directly support the paper's core claim.

2. **Anchor-client mechanism demonstrably enables expert specialization.** Figure 5 shows that without anchor clients (random sampling) FedJETs fails to improve beyond the common expert, whereas with anchor clients it surpasses the baseline and maintains stable performance. This validates the mechanism's central role in the method.

3. **Novel gating function that achieves dynamic, per-client expert selection using a frozen pretrained model.** The gating uses embeddings from a never-retrained common expert to route each client's data to top-K experts (Section 4). This design enables just-in-time personalization without any labeled data from unseen clients.

4. **Communication efficiency relative to prior MoE-FL work.** FedJETs sends only K=2 experts per client even when the total expert pool is M=5 or 10, while FedMix requires sending all M experts. This is a practical advantage over the most directly comparable method.

5. **Honest ablation identifying common-expert quality threshold.** Figures 3–4 characterize a breakpoint (~66% accuracy on CIFAR100) below which the gating cannot improve and experts stagnate. This identifies an important practical limitation of the method.

6. **Demonstrated robustness to expert initialization.** Table 2 shows that even when experts are initialized from the common expert (rather than randomly), FedJETs reaches 83.27% on CIFAR100 after 2000 rounds, outperforming all baselines (best baseline 74.10%).

## Weaknesses

### Fatal
None.

### Major

- **Ambiguous baseline initialization and potentially unfair comparison.** The paper states that Average Ensembles is "initialized from the common expert" (line 244), but it does not clarify whether FedAvg, FedProx, or FedMix receive the same initialization. Since the common expert is a pretrained ResNet34 achieving 73–93% on CIFAR10, whether baselines start from this checkpoint or random initialization makes a large difference. This ambiguity undermines the interpretation of the reported gaps. Additionally, even if baselines were initialized from the common expert, FedJETs has a routing advantage from the common expert's embeddings that baselines lack — a controlled experiment isolating the gating+MoE benefit from the pretrained routing signal is missing.

- **Anchor clients require privileged information about client data distributions.** The method pre-selects M clients with "roughly distinct local data distributions" and activates them every round (5 out of 10 active clients are always anchors). This requires knowing each client's label distribution a priori — unavailable in realistic FL deployments. The paper acknowledges "we assume we have some control over the activation of the clients during training" (line 337), but does not discuss this as a limitation or propose a practical discovery mechanism. The ablation (Figure 5) confirms that without anchor clients, FedJETs "shows difficulty improving performance," making this a core dependency rather than a nice-to-have.

- **Misleading claim about second-best baseline in the conclusion.** The conclusion states "the second best state of the art method achieves ~58% and ~74%" (line 355). On CIFAR10, FedProx achieves 71.4% (teal column) or 72.7% (violet) — both well above 58%. The paper cherry-picks FedAvg's 58.4% as "second best" to inflate the claimed improvement margin. The correct second-best on CIFAR10 (teal column) is FedProx at 71.4%, making the gap 95.7% vs 71.4%, not 95.7% vs 58%.

- **Missing details on test client construction.** The paper evaluates on "unseen test clients" (line 265) but does not describe how these test clients are generated — whether they are held-out clients from the same 100-client pool with their own non-i.i.d. partitions, or entirely new data splits. This makes it difficult to assess the validity of the zero-shot evaluation.

### Minor

- **Weak evidence that experts actually specialize on distinct class subsets.** The paper's only evidence for specialization is per-expert accuracy trajectories over rounds (Figure 4). These could reflect different convergence rates rather than specialization on different label subsets. The paper does not show per-class accuracy per expert, gating decisions across clients, or any diversity metric (e.g., agreement, gradient similarity). Since the entire motivation rests on meaningful specialization, stronger evidence would significantly strengthen the contribution.

- **Scaffold comparison presented as baseline failure without tuning discussion.** The paper states Scaffold "became unstable during training (10% for CIFAR10 / <5% for CIFAR100)" (line 274) but provides no hyperparameter search details. Scaffold's control variates require careful tuning; presenting this as a baseline failure without transparency is not a fair comparison.

- **No ablation comparing argmax vs. weighted averaging at test time.** The testing procedure uses the single highest-scoring expert per sample rather than standard MoE weighted averaging (line 214). The paper claims this "fully utilize[s] the specialization of the expert" but provides no ablation comparing the two strategies.

### Trivial

- Notation overload: $\mathbf{W}_s$ is used both for local model parameters (Section 2) and gating function parameters (Section 3), creating confusion.

## Nice-to-Haves

- An ablation varying the number of experts M (the paper uses M=5 for CIFAR10 and M=10 for CIFAR100 without justifying or varying this choice).
- A version of FedJETs where anchor clients are discovered dynamically (e.g., by clustering client embeddings during training) rather than pre-selected with knowledge of label distributions.
- A parameter count and communication cost comparison table across methods (FedJETs with 5–10 ResNet34 experts has substantially more total parameters than FedAvg's single model).

## Removed Points

- **Missing related work on personalized FL (pFedMe, Ditto, FedEM, etc.):** Removed per the rule against citing missing related works without external confirmation.
- **Incomplete algorithm pseudocode (missing \input{algo}):** Removed per the rule that appendix/supplementary material is stripped by the parser.
- **Incomplete sentence "FedJETs are able to dynamically select...":** Removed as a parser artifact, not an author error.
- **"The common expert alone achieves 73-93%... FedJETs inherits a strong head start":** Partially overblown — FedJETs' experts are randomly initialized (line 161), not initialized from the common expert. The common expert is used only as a frozen feature extractor for gating, so FedJETs does not directly "inherit" the common expert's classification performance. The concern about the routing advantage is real and is kept in Major weaknesses above.
- **"No evidence that experts actually specialize" treated as structural:** Downgraded to Minor. The per-expert accuracy trajectories in Figure 4 do provide some evidence; the reviewer's demand for per-class confusion matrices and diversity metrics is a reasonable strengthening request but not a fatal gap.
- **"Scaffold should not be presented as baseline failure":** Downgraded to Minor and kept. The point about missing tuning details is valid but the comparison is not central to the paper's claims.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Clarify baseline initialization.** State explicitly whether FedAvg, FedProx, and FedMix were initialized from the same pretrained ResNet34 checkpoint or from random initialization. If from random, run controlled experiments with same initialization to isolate the MoE+gating benefit.

2. **Fix the misleading conclusion.** Correct "~58%" to reflect the actual second-best baseline (FedProx at ~71.4% on CIFAR10) when reporting improvement margins.

3. **Describe test client generation.** Detail how unseen test clients are created — e.g., held-out portion of the 100 clients, or entirely new non-i.i.d. partitions.

4. **Provide stronger evidence of expert specialization.** Show per-class accuracy for each expert after training, or at minimum show that the gating function's top-1 selection matches the expert that actually performs best on that test sample.

5. **Acknowledge the anchor client limitation more prominently.** Discuss scenarios where such control over client selection is realistic, or propose a method for discovering anchor-like clients without prior knowledge of label distributions.

6. **Add ablation for test-time argmax vs. weighted averaging** to justify the design choice.
