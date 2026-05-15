Now I have all the information I need from my earlier reads of the full paper. Let me synthesize the final review.

---

## Summary

FedJETs proposes a federated mixture-of-experts system for zero-shot personalization. The system maintains a pool of expert models on the server and uses a pretrained "common expert" as a feature extractor to drive a learned gating function that routes only K=2 out of M=5-10 experts to each client per round. A separate "anchor client" mechanism dedicates certain clients to specific experts via a one-to-one mapping and auxiliary loss to encourage specialization. On CIFAR10 and CIFAR100, FedJETs reports accuracy improvements over baselines, with the largest gains on CIFAR10.

## Strengths

- **Notable accuracy gains in a challenging setting**: Table 1 shows FedJETs achieving 91.8% on CIFAR10 (violet condition) versus the next best baseline (FedProx at 72.7%), a ~19 percentage point improvement. On CIFAR100, FedJETs reaches 75.7% vs 74.0% for FedAvg/FedProx. These numbers, if verified under fair conditions, represent a meaningful advance in zero-shot FL personalization — the paper's stated goal.

- **Conceptually novel integration of MoE with FL**: The idea of using non-i.i.d. client distributions as a *source* of expert specialization (rather than just a problem to overcome) is well-motivated. The combination of a frozen pretrained feature extractor (common expert) with a learned gating function that routes a subset of experts is a creative and non-obvious design.

- **Informative ablation studies**: Figures 3-5 diagnose when the method works. The "breakpoint" analysis (Figure 4) showing that a common expert below ~67% accuracy causes routing collapse is useful operational guidance. The ablation on anchor-client ratio (Figure 5) convincingly shows that the mechanism is essential — random client sampling without anchors causes performance to stagnate.

- **Clear problem framing**: The paper carefully distinguishes zero-shot personalization (goal iii) from other FL goals and motivates why fine-tuning is not always feasible (privacy, resource constraints on fresh clients).

## Weaknesses

### Fatal
None. No single flaw invalidates the paper's core claims beyond repair, though several serious issues require attention.

### Major

- **Two accuracy columns in Table 1 differ for methods that do not use the common expert, without explanation.**  
  The table presents two "Acc." columns per dataset, corresponding to two different common experts (violet = lower bound, teal = average). For methods like FedAvg and FedProx that do not use the common expert, both columns should be identical if all other experimental conditions are the same. Yet on CIFAR10, FedAvg reports 31.2% (violet) and 58.4% (teal) — a 27-point gap. FedProx reports 72.7% vs 71.4%. These discrepancies strongly suggest that the two columns come from *different experimental conditions* (different partitions, seeds, or hyperparameters), not just different common experts. The paper provides no explanation for this, making it impossible to determine which comparison is fair and whether the reported gains are consistent across runs. *(Verified directly from Table 1 and its caption.)*

- **The anchor-client mechanism assumes distributional knowledge that standard FL protocols do not provide.**  
  The paper states "we pre-select M special clients, with roughly distinct local data distributions, as anchor clients" (line 179) and establishes a "one-to-one mapping between these clients and the experts, corresponding to each group of labels" (line 235). Without the server knowing each client's label distribution — information FL is explicitly designed to protect — it is unclear how anchor clients would be identified in practice. Figure 5 confirms that performance collapses without anchor clients. While the paper acknowledges "some control over the activation of clients," it never discusses how this selection would be done without violating privacy or requiring labeled metadata from clients. This limits applicability to settings where client data distributions are already known (e.g., cross-silo FL with known institutional specialties), a scope the paper does not discuss. *(Verified: lines 179–183, 234–236, and Figure 5.)*

- **Absence of data partition parameters undermines reproducibility and fairness assessment.**  
  The paper describes only: "we partition the data samples by classes to turn full datasets into non-i.i.d. subsets" (line 89). No Dirichlet concentration parameter (α), no number of classes per client, and no target heterogeneity level are reported. Since the paper itself attributes FedAvg's poor CIFAR10 performance (31.2%) to "the number of classes each client holds" and "amplif[ied] model drift" (line 272), the reader cannot verify whether this is a natural outcome of a realistic partition or an artifact of an extreme partition that disproportionately harms baselines. *(Verified: lines 89, 233–235, 272.)*

### Minor

- **No comparison against random gating, despite this being the paper's central motivation.**  
  The paper's motivation (Section 1) cites Zuo et al. (2021) showing that random gating in MoEs performs comparably to learned gating, and claims FedJETs overcomes this. Yet no experiment replaces the learned gating function with a random (frozen) gating network to demonstrate that the learned routing actually provides a benefit. This is the most directly relevant ablation for the paper's core claim of "true expert specialization" (line 138). *(Verified: lines 31–33, 138.)*

- **No communication cost measurements despite repeated efficiency claims.**  
  The paper claims FedJETs "scale[s] more efficiently" (abstract) and "reduces communication cost" (line 187, line 270), but provides zero empirical measurements of communication volume (MB per round), computation time, or wall-clock training cost. Sending M full ResNet-34 experts (once) plus K experts per round plus gating-network parameters is non-trivial. Without measurements, these efficiency claims are unsubstantiated. *(Verified: abstract, lines 187, 270.)*

- **No variance estimates or multiple seeds.**  
  All results in Table 1, Table 2, and Figures 3-5 are presented as point estimates with no standard deviations, confidence intervals, or indication of how many seeds were run. This is a concern given the apparent instability of the method near the breakpoint (Figure 4) and the wide variation in baseline numbers across conditions. *(Verified: entire Section 5.)*

- **FedMix baseline uses fewer experts (M=2) than FedJETs (M=5 or M=10), conflating method comparison with capacity.**  
  FedMix sends all M=2 experts to each client (M=K by design), while FedJETs uses M=5–10 and selects K=2. The paper explains this as a feature of FedMix's design limitation, but it means the comparison simultaneously varies both the method *and* the total expert pool size. An apples-to-apples comparison would use equal M for both methods, or compare FedJETs with M=2. *(Verified: Table 1, line 270.)*

### Trivial
None.

## Nice-to-Haves

- An experiment varying K (number of selected experts) beyond K=2 would reveal how the gating function's routing quality scales.
- Quantifying expert specialization (e.g., per-expert test accuracy on disjoint label groups, or activation frequency per client type) would strengthen the claim of "true expert specialization."
- A discussion of how the "breakpoint" (67%) relates to the number of classes or the difficulty of the routing problem would help practitioners apply the method.

## Removed Points

These points were flagged by the reviewers but removed after verification against the paper:

- *"FedAvg's 72.9% on CIFAR100 surpasses the lower-bound common expert (67%), creating an internal inconsistency"* — FedAvg does not use the common expert; there is no inconsistency between a pretrained model's accuracy and a separately trained FL model's accuracy.
- *"Testing with the highest-ranked expert per sample introduces high variance"* — This is an explicit design choice, and the paper does not claim low variance as a benefit of this decision.
- *"The anchor-client loss is explicit supervision, not emergent specialization"* — The paper never claims "emergent" specialization; the loss is explicitly designed to guide the gating function.
- *"The paper overstates consistency"* — Both columns of Table 1 are presented, allowing readers to see both lower-bound and average conditions.
- Several parser-artifact issues, formatting complaints, and missing-appendix concerns that reflect PDF extraction artifacts, not author errors.

## Novel Insights

The reviews converge on a structural tension that the paper does not resolve: FedJETs's best results come from precisely the conditions where it deviates farthest from standard FL assumptions — namely, knowing per-client label distributions to select anchor clients. This raises a deeper question about whether FL methods that work by exploiting known heterogeneity should be evaluated against baselines that are not allowed to exploit the same knowledge, or whether the method is better understood as operating in a distinct regime (partially known client distributions) that FL research typically avoids. The paper would benefit from explicitly stating which FL assumptions it relaxes, and then comparing against methods that also relax those same assumptions.

## Suggestions

1. **Clarify Table 1**: Explain why the two "Acc." columns differ for methods that do not use the common expert. If they come from different seeds, partitions, or hyperparameter choices, state this explicitly and report means+variances. If they are from the same experimental conditions, the numbers should be reconciled.

2. **Address anchor client feasibility**: Either (a) provide a concrete, privacy-preserving procedure for identifying anchor clients (e.g., based on metadata already available in cross-silo FL), (b) acknowledge this as a limitation and scope the method accordingly, or (c) demonstrate a variant that works without anchor clients.

3. **Report partition details**: Publish the exact data partition procedure (Dirichlet α, number of classes per client, or the specific assignment) to enable reproducibility.

4. **Add a random gating baseline**: Replace the learned gating function with a randomly initialized, frozen gating network to directly test whether FedJETs achieves meaningful routing.

5. **Report communication costs**: Provide MB/round for FedJETs and baselines, including the one-time common expert broadcast.

6. **Run multiple seeds**: Report means and standard deviations over at least 3 seeds.

## Score and Decision

This paper tackles a well-motivated and underexplored problem (zero-shot personalization in FL via MoE-style specialization) with a creative architectural proposal. The accuracy numbers, particularly on CIFAR10, are striking. However, the experimental evaluation has several issues that must be addressed before the core claims can be accepted: the unexplained discrepancy in Table 1's two accuracy columns for methods that do not use the common expert undermines trust in the baseline comparisons; the anchor-client mechanism's reliance on distributional knowledge that standard FL does not provide is not scoped or justified; and key controls (random gating baseline, communication cost measurements, variance estimates) are missing. The paper's contributions are promising but the evidence as presented is not yet fully convincing.

**Score**: 5.5/10 (borderline reject; major revisions needed)

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>