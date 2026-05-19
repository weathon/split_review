- Decision: Reject
- Avg Score: 3.75
- Scores: 3, 3, 3, 6
Now I have a thorough understanding of the paper and all reviewer claims. Let me produce the final consolidated review.

## Summary

This paper introduces QuickDrop, a federated unlearning method that generates compact synthetic datasets during FL training via gradient matching, then uses those synthetic datasets (just 1% of original data volume) for SGA-based unlearning and recovery. The approach is evaluated across three datasets and five baselines, demonstrating a 463× speedup in unlearning duration over retraining from scratch and 65–218× over existing FU methods while maintaining comparable accuracy.

## Strengths

- **Massive empirical speedup with competitive accuracy**: Table 2 shows QuickDrop achieves a 463.7× speedup over retraining and 65–218× over FedEraser, SGA, and FuMP on CIFAR-10 (10 clients, non-IID). The unlearning phase completes in 5.03 seconds (100 synthetic samples) vs 495.17 seconds for SGA on original data (5000 samples), with forget-set accuracy matching the oracle (0.82% vs 0.81%).

- **Novel integration of dataset distillation with FL for unlearning**: The core idea—generating compact synthetic datasets via gradient matching *during* FL training and reusing them for downstream SGA-based unlearning and recovery—is original and well-motivated. Algorithm 1 clearly describes the in-situ generation process where gradient matching (Eq. 6) runs concurrently with standard FL local updates, reusing gradients already computed for FL training.

- **Broad unlearning capability in a single framework**: Table 1 shows QuickDrop supports class-level, client-level, and relearning simultaneously, unlike FuMP (no client-level/relearn), SU (no class-level), and SGA (relearn possible but inefficient). Tables 3, 5, and 6 provide experimental validation across all three tasks.

- **Scalability demonstrated with 100 clients**: Table 4 reports a 326.69× speedup over retraining on SVHN with 100 clients (10% participation rate), with R-Set accuracy (84.96%) competitive with baselines (82.98–86.47%), showing the method works at realistic scale.

## Weaknesses

### Fatal
None.

### Major
None. The paper's central claims—that synthetic data can compress gradient information and enable fast federated unlearning—are well-supported by the empirical evidence.

### Minor

- **Heuristic link between gradient matching and SGA unlearning effectiveness**: The paper formulates DD for FU (Eq. 3) as: the generalization of the unlearned model using synthetic data should match that using original data. However, the actual optimization (gradient matching during FL training, Eq. 4) optimizes a different objective—matching gradients along the training trajectory. The paper provides only an intuitive justification ("the synthetic data absorbs the gradient information…") without a theoretical argument or small-scale verification that gradient-matching during training produces synthetic data that is specifically effective for SGA-based unlearning. While this is not fatal (many unlearning methods are heuristic), it weakens the scientific contribution. An ablation isolating the gradient-matching step (e.g., comparing against a variant using randomly sampled original data of the same size) would strengthen the design justification.

- **DD overhead amortization discussed only qualitatively**: The DD process adds 46–55% extra compute time during FL training (Table 7). The paper acknowledges this in Section 6 ("these compute costs are then amortized over the subsequent unlearning requests") but does not quantify the break-even point. A practitioner evaluating QuickDrop would benefit from knowing how many unlearning requests are needed to recoup the training-time investment. For instance, on CIFAR-10, the DD overhead is ~2948s; retraining from scratch costs ~7240s. The savings per unlearning request with QuickDrop is ~7224s. So the break-even is well under one request (since 2948 < 7224), but the paper never makes this calculation explicit. Including such an analysis would strengthen the practical argument.

- **QuickDrop's R-Set accuracy is consistently slightly below oracle**: In Table 2, QuickDrop achieves 70.48% R-Set vs oracle's 74.95% after recovery (without fine-tuning). In Table 5 (CIFAR-10, 20 clients), R-Set is 65.78% vs oracle's 71.48%. While the paper shows fine-tuning closes this gap (74.55% at F=200, Figure 3), the default configuration (F=0, used for all main experiments) leaves a 4–6% gap. The paper should be more explicit about this accuracy-efficiency trade-off when promoting the headline speedup numbers.

- **MIA results provide limited discriminative signal**: Figure 3 shows all methods (QuickDrop, baselines, and oracle) achieve near-0% F-Set MIA accuracy, making the metric uninformative for distinguishing unlearning quality among methods. The paper uses MIA as validation, but the results do not meaningfully differentiate QuickDrop from alternatives. This is not a flaw in QuickDrop but weakens the claim that MIA "further assess[es] the effectiveness of unlearning."

### Trivial

- **Client-level non-IID F-Set slightly higher than oracle**: In Table 3, QuickDrop achieves 11.57% F-Set vs oracle's 10.48% for non-IID client-level unlearning. Higher F-Set accuracy implies *less* effective forgetting than the oracle. The paper does not comment on this. The difference is small (~1%) and within variance, but worth noting.

- **Use of InstanceNorm without justification**: The paper uses ConvNet with InstanceNorm and ReLU (Section 4.1), while many FL works use BatchNorm. The choice is not justified; a brief mention of why InstanceNorm was selected (e.g., better handling of non-IID data where batch statistics vary across clients) would be helpful.

## Nice-to-Haves

- A quantitative break-even analysis showing the number of unlearning requests needed for QuickDrop's total cost (training + unlearning) to match retraining from scratch.
- An ablation comparing QuickDrop against a variant where synthetic data is simply a random subset of original data of the same size (no gradient matching), to isolate the benefit of the DD process.
- A discussion of how the synthetic data initialization (random selection from original data rather than Gaussian noise) affects the distillation quality and whether random selection already provides a strong baseline.

## Removed Points

These points are flagged to be removed; treat them with caution:

1. **"Simulation gap makes efficiency claims misleading" (Harsh Critic)**: The critic claims timing numbers are "essentially local computation times" and the speedup may not hold in real FL. This is standard practice in FL research—all baselines are evaluated on the same simulated setup. Additionally, QuickDrop uses *fewer* rounds (3) than retraining (30), so if communication overhead were included, QuickDrop's relative advantage would be *larger* or maintained, not smaller. The paper clearly states "All experiments are conducted on a machine equipped with an i5-10600K CPU and an RTX 2060 GPU," making the scope transparent. Removed because the criticism overstates the issue and the reasoning is partially backwards.

2. **"463× speedup is misleading without folding in DD overhead" (Harsh Critic)**: The critic calculates "2.7×" by adding DD overhead (~2700s) to unlearning time (15.61s). This conflates training costs with unlearning costs. The 463× speedup is for *unlearning duration*—the marginal cost of serving an unlearning request given a trained model—which is the standard metric in unlearning literature. Retraining from scratch also requires training the initial model (~2412s), which the critic's calculation omits. Even under a total-cost framing, QuickDrop (5360s training + 15.61s unlearning = 5375.61s) vs retrain (2412s training + 7239.58s retraining = 9651.58s) still shows a ~1.8× total cost advantage. The paper discusses amortization qualitatively in Section 6. Removed because the critic's comparison is non-standard and the claimed "misleading" framing is not supported by how the results are presented.

3. **"Time (s) measurements need clarification" (Harsh Critic)**: The paper explicitly states the hardware configuration. The comparison is relative—all methods run on the same machine. No clarification needed. Removed.

4. **"InstanceNorm should be justified" framing as a weakness (Harsh Critic)**: This is a trivial implementation detail. Moved to Trivial.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

- Add a brief break-even analysis quantifying how many unlearning requests amortize the DD overhead. As noted above, even a rough calculation (DD overhead ~2948s, savings per request ~7224s) shows the break-even is reached almost immediately; making this explicit would preempt concerns.
- Include an ablation comparing QuickDrop against a variant where synthetic data is a random subset of original data (no gradient matching) of the same size. This would isolate the benefit of the DD optimization.
- In the main results (Table 2), add a row for QuickDrop with fine-tuning (F=200) alongside the default (F=0) to show that accuracy parity with the oracle is achievable at moderate extra compute cost.
- Note the small F-Set elevation for client-level non-IID unlearning (11.57% vs oracle 10.48%) and explain why it occurs.
