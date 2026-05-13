## Summary
The paper studies federated learning under simultaneously occurring label, feature, and concept shifts. It proposes a "clustering principle" (separate clients with concept shifts; keep clients with only label/feature shifts together), shows existing clustered FL methods (IFCA, FeSEM, FedEM, FedSoft) violate it, and introduces FedRC, a soft-clustering algorithm with a label-marginal-normalized objective $\tilde{\mathcal{I}}(x,y;\theta_k)=\exp(-f(x,y,\theta_k))/C_{y,k}$, an EM-style optimization, and an $O(1/T)$ convergence result. Experiments on FashionMNIST/CIFAR10/CIFAR100/Tiny-ImageNet report large global-accuracy gains over baselines.

## Strengths
- **Concrete clustering principle plus diagnostic experiment.** Section 3 / Fig. 3 cleanly visualize that IFCA, FeSEM, FedEM, and FedSoft fail to separate clients by concept in the constructed multi-shift scenario; this diagnostic is useful independent of the proposed method.
- **Well-motivated objective.** Normalizing by $C_{y,k}\approx P(y;\theta_k)$ to remove label-frequency confounding (Eq. 2 and surrounding text) is a clean idea that aligns with the stated principle in a way most clustered-FL objectives do not, and FedRC's own clustering visualizations show diagonal concept structure (Fig. 4b/d).
- **Substantial reported gains with standard deviations.** Table 1 reports both local and global accuracy with $\pm$ across three datasets/architectures (e.g., CIFAR10/MobileNetV2 global 63.83 vs. FedEM 43.35), and the improvements persist after fine-tuning (FedRC-FT) and under hard clustering (Fig. 4c).
- **Convergence guarantee.** Theorem 1 gives an $O(1/T)$ rate for the $\Theta$ update under standard smoothness + bounded-gradient assumptions.

## Weaknesses

### Fatal
None.

### Major
- **Concept shift is operationalized as a single symmetric class permutation $y\mapsto C-y$ with only three concepts.** Section 5.1 and the experiment description (lines ~412) confirm this is the only $P(y|x)$ change studied in the main tables. This is a structured, globally consistent permutation that (i) produces maximally large losses under the "wrong" cluster, making the clustering signal trivially strong, and (ii) symmetrically permutes label marginals, mechanically breaking the label-frequency confound the proposed $C_{y,k}$ normalizer is designed to counter. The central empirical claim ("decouples concept shifts from label/feature shifts") is therefore only tested in the regime most favorable to the proposed mechanism — partial relabelings or covariate-dependent $P(y|x)$ changes are never evaluated.
- **$K$ is set to the ground-truth number of concepts in essentially all main results.** Section 5.2 explicitly initializes $K=3$ "which is the same as the number of concepts" for all clustered methods. Fig. 4a does sweep $K$, but only on CIFAR10/100 clients (a different configuration than the main tables), so the headline Table 1/2 numbers benefit from oracle access to a quantity that is unobservable in practice. A mis-specified-$K$ sweep on the main 300-client benchmarks is needed to support the deployment claim.
- **The "decouples feature shift" claim does not transfer to the practical objective.** The interpretation under Eq. 1 leans on $P(x;\theta_k)$ being small to absorb feature shift (bullet on line ~230), but Section 4.2 explicitly drops the $P(x;\theta_k)$ branch and only approximates $P(y|x)/P(y)$. The feature-shift decoupling argument in its current form therefore applies to an objective that is not actually optimized.

### Minor
- **Global-accuracy evaluation protocol for nonparticipating clients is under-specified.** Section 5.1 says nonparticipating clients' labels are swapped "in the same manner as the participating clients for each concept," but the paper does not state how $\omega_{i;k}$ is set or how the soft ensemble $\sum_k\omega_{i;k}P(y|x;\theta_k)$ is formed on a held-out client with no training data. Whether $\omega$ is inferred from labeled test data, set uniformly, or matched to the known concept materially affects how to read the global-accuracy numbers, and the paper should state this explicitly.
- **Approximation $C_{y,k}\approx P(y;\theta_k)$ is hand-waved.** $C_{y,k}$ as defined (Eq. after line 260) is the empirical label frequency in the cluster's soft-assigned data, which equals $P(y;\theta_k)$ only when $\gamma$ is the true posterior — i.e., the quantity being estimated. The interpretive bullet glosses this circularity.
- **Convergence statement covers only $\Theta$.** Theorem 1 bounds $\|\nabla_{\theta_k}\mathcal{L}\|^2$ averaged over $T$ but says nothing about stationarity in $\Omega$ for the bi-level problem the paper actually solves.
- **Table 2 (ResNet18) has no standard deviations**, while Table 1 does; significance is not addressed despite some Table 1 std devs being large (e.g., FedRC FashionMNIST global 59.00 ± 4.91).
- **No ablation isolating the $C_{y,k}$ normalizer.** Plugging the same label-frequency normalization into FedEM's objective would show whether gains come from the new objective form or from the normalizer alone.

### Trivial
- Fig. 4d only tests {1, 3, 5} concepts with $K$ matched, so it inherits the oracle-$K$ issue.

## Nice-to-Haves
- A non-symmetric concept shift (subsets of classes relabeled, spurious-feature-induced conditional shifts, or natural concept shift from a real distributed dataset) to test whether the gains generalize beyond class permutation.
- A test client whose label permutation is *not* one of the three training concepts, to probe whether FedRC learns shared decision boundaries or memorizes the three permutations.
- A case study tracing $\omega_{i;k}$ over training for a single nonparticipating client to make the evaluation protocol concrete.

## Removed Points
These points are flagged to be removed; treat them with caution.
- **Harsh critic's "novelty overstated" comment on Sec. 1** (Jothimurugesan, Ke already evaluate clustering under shifts): borderline missing-related-work / framing nitpick; not substantive enough to keep.
- **"Global > local in Table 1 means protocols are not comparable" (Fig. 2b critique):** The setup explicitly uses balanced global distributions per concept while participating clients have LDA-skewed labels, so global > local is mechanically possible and not by itself evidence of a measurement problem; the critic's framing is unsupported.
- **Strength Finder's "fair and comprehensive experimental protocol"** and **"the objective function is well-justified and directly targets the clustering principle"**: generic and partially in tension with the verified major weakness that the feature-shift decoupling claim does not transfer to the practical objective.
- **Strength Finder's "statistically robust" claim:** Table 1 has std devs but Table 2 does not, and no significance tests are reported; "statistically robust" overstates the evidence.

## Novel Insights
None beyond the paper's own contributions. The most useful idea is the paper's own: dividing the log-likelihood by an estimated label marginal $C_{y,k}$ so that label-frequency similarity stops dominating cluster assignment.

## Suggestions
- Replace (or augment) $y\mapsto C-y$ with at least one asymmetric/partial concept shift on CIFAR10 and Tiny-ImageNet using the main 300-client setup, and re-run the cluster-quality plots of Fig. 3.
- Sweep $K\in\{2,3,5,8\}$ on the main benchmarks (not just CIFAR10/100 clients) and report Tables 1–2 numbers under mis-specified $K$.
- Specify, with equations, how $\omega_{i;k}$ is set for nonparticipating test clients and how the ensemble is formed; if $\omega$ uses labeled test data, state that this is the protocol and discuss its implications.
- Either re-derive the feature-shift decoupling argument for the practical $\tilde{\mathcal{I}}$ (which drops $P(x;\theta_k)$) or soften that claim.
- Add an ablation that plugs $C_{y,k}$-normalization into FedEM to isolate the normalizer's contribution.
- Extend Theorem 1 (or state explicitly) to address stationarity in $\Omega$, and add standard deviations / significance to Table 2.

## Assessment
- **Originality:** Moderate. The label-marginal normalizer is a sensible new twist on EM-style clustered FL.
- **Importance:** The problem (concurrent shifts in FL) is legitimately under-explored.
- **Soundness of claims:** Partially supported. The clustering-principle diagnostic is convincing; the "robust to diverse shifts" claim is weakened by the narrow concept-shift simulator, oracle $K$, and the feature-shift gap between the idealized and practical objectives.
- **Experiments:** Multiple datasets/architectures with std devs on Table 1, but the central scenario is one structured permutation regime with oracle cluster count.
- **Clarity:** Generally clear; the nonparticipating-client evaluation protocol and the $C_{y,k}\!\approx\! P(y;\theta_k)$ identification are the main exposition gaps.
- **Value to community:** The diagnostic visualizations and the normalizer idea are useful; the paper would be substantially stronger after addressing the major points above.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>