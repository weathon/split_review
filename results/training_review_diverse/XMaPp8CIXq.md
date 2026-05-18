I have read and verified the paper thoroughly. Let me now construct the final consolidated review.

---

## Summary

The paper proposes Guided Stochastic Exploration (GSE), a dynamic sparse training algorithm that never materializes dense weights or computes dense gradients. GSE samples a random subset of inactive connections (size proportional to the active set), computes gradients only for that subset, and grows the connections with the largest gradient magnitudes. This hybrid of stochastic exploration and greedy selection is shown to match or modestly exceed the accuracy of RigL (which requires periodic dense gradient computation) while reducing computational cost. Experiments on CIFAR-10/100 and ImageNet across ResNet, VGG, and ViT models at sparsities of 90%–98% are presented against a broad set of baselines.

## Strengths

1. **Genuinely always-sparse training that matches/slightly exceeds RigL's accuracy at high sparsity.**  
   On CIFAR-100 at 98% sparsity with ResNet-56, GSE (62.1%) outperforms RigL (60.8%) and SET (56.0%); on VGG-16, GSE (69.6%) vs RigL (68.8%). On ImageNet with ResNet-50 at 90% sparsity, GSE achieves 75.82% vs RigL's 75.01% (Table 2). These results are consistently in GSE's favor, especially at extreme sparsity where differences between methods are most meaningful. Unlike RigL, GSE achieves these results without ever materializing dense weights or computing dense gradients.

2. **Simple, well-motivated method with a clean ablation of the exploration strategy.**  
   The core idea — sample a random subset of inactive connections, then greedily select the best from that subset — is intuitive and easy to implement. Section 4.2 thoroughly compares three sampling distributions (uniform, GraBo, GraEst) and shows that uniform sampling works as well or better than the biased alternatives. The finding that uniform + greedy selection is both simplest and most effective is a genuine insight that simplifies the method considerably.

3. **Comprehensive empirical evaluation.**  
   The paper covers 3 datasets (CIFAR-10, CIFAR-100, ImageNet), 3 architectures (ResNet-56, VGG-16, ViT), 3 sparsity levels (90%, 95%, 98%), and compares against 9+ baseline methods spanning pruning-before-training (SNIP, GraSP, SynFlow), gradual pruning, and dynamic sparse training (SET, RigL, Top-KAST, DSR, SNFS). The comparison is wider than many papers in this area.

4. **Always-sparse property is a meaningful differentiator from RigL.**  
   As Section 2 correctly notes, RigL "requires periodically computing the dense gradients." GSE removes this requirement entirely. The paper clearly states (Section 3): "at no point is the dense model materialized, all forward passes use sparse weights, and it exclusively calculates sparse gradients."

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **The accuracy improvement over RigL is modest and the framing slightly overstates it.**  
   The abstract claims GSE "improves the accuracy over previous methods." While this is technically true — GSE consistently achieves higher accuracy than RigL in the reported experiments — the margins are small on ImageNet (~0.8 percentage points at 90% sparsity). On CIFAR at lower sparsities (90%), differences are also small. The contribution is strongest at extreme sparsity (98%). The paper would be more accurate and compelling if it framed its main contribution as *"always-sparse training that matches or modestly exceeds RigL's accuracy at lower computational cost"* rather than leading with an accuracy improvement claim. This is a framing issue, not a result invalidation.

2. **The time complexity analysis (O(n) vs O(n²)) lacks necessary precision.**  
   The paper states "improves the training time complexity of RigL from O(n²) to O(n)" (Introduction) but never explicitly derives either complexity. Section 3.2 shows that GSE's sampling, gradient computation for the subset, and top-k selection each run in O(n) time, and that the Erdős–Rényi initialization ensures |A| = O(n). This is correct per update step. However, the paper never explains where RigL's O(n²) cost comes from (computing gradients for all O(n²) inactive connections each grow step) or discusses how RigL's periodicity T affects the *amortized* cost per training step. A proper comparison would clarify: (a) the per-grow-step cost of computing O(n²) vs O(n) gradients, and (b) how the amortized cost changes when T is large. Without this, the complexity advantage is directionally correct but imprecisely argued.

3. **The choice of γ=2 on ImageNet is used without justification.**  
   On CIFAR, γ=1 suffices to match/exceed RigL. On ImageNet (Section 4.4), the paper uses γ=2 with no explanation. The FLOPs comparison in Section 4.6 uses γ=1, creating a disconnect between the efficiency analysis and the ImageNet accuracy results. If γ=1 was tried on ImageNet and failed, that should be reported and explained. If it was not tried, the missing ablation raises questions about whether the efficiency advantage holds at scale. This is a straightforward missing experiment.

4. **Variability reporting with only 3 runs is insufficient.**  
   The paper reports the mean and "plot[s] the 95th percentile" from 3 random seeds (Section 4.1). With only 3 samples, the 95th percentile is not a statistically meaningful dispersion measure — it essentially reports the maximum. Standard deviation or individual run values would be more informative, especially given the small accuracy differences between methods (many in the 0.2–1.3 percentage point range).

5. **Source of baseline numbers is not always clearly distinguished.**  
   Section 4.4 states that Table 2's baseline results "were obtained from prior publications" but it is not stated whether Table 1's baselines were rerun by the authors or drawn from prior work. Section 4.1 says the authors "adopt the implementation of the baselines based on their available code," suggesting Table 1 baselines are rerun. This should be stated explicitly for each table to avoid confusion about comparability.

### Trivial

- **Figure numbering reference error (Section 4.5):** The text refers to Figure 3 for the model scaling experiment but also mentions ViT accuracy "plateaus at 62" with a sentence fragment that appears garbled — likely a parser artifact.

## Nice-to-Haves

- A brief sensitivity study of γ on ImageNet (γ=1 vs γ=2 at 90% sparsity) would settle whether the efficiency advantage holds at scale.
- Reporting actual (or simulated) wall-clock time, even with the mask-simulation acknowledged limitation, would ground the FLOPs analysis.
- The model scaling experiment (Figure 3) is interesting but tangential to the core GSE-vs-baseline comparison; it could be moved to an appendix to sharpen the paper's focus.

## Removed Points

- **"0.01% gap (77.43 vs 77.42) on ImageNet"** — These numbers do not appear in the paper text. The paper reports different values (GSE 75.82% vs RigL 75.01% per the experiment description and table caption). The harsh critic's specific numerical claim cannot be verified from the readable text and appears to be an error. *Removed as factually unverifiable/incorrect.*

- **"Figure 2 shows accuracy plateaus at the level of RigL"** — The paper states GSE "consistently matched, or even surpassed" RigL at γ=1, not merely plateaued. The critic's phrasing misrepresents the paper's own description of its results. *Removed as a misreading.*

- **"The model scaling experiment does not directly support the main contribution"** — The paper frames it as an exploration of the method's utility for training wider sparse models, which is a reasonable secondary contribution. This is a presentation preference, not a weakness. *Removed as a scope/style nitpick.*

## Novel Insights

Beyond the paper's own contributions, the reviews surface an interesting observation: GSE's success with uniform + greedy selection suggests that in dynamic sparse training, the *exploration* phase (sampling which inactive connections to evaluate) and the *exploitation* phase (selecting the best among those evaluated) can be decoupled productively. The uniform distribution handles exploration cheaply, while gradient-magnitude selection handles exploitation — and neither requires the complexity of biased distributions like GraBo/GraEst. This insight has practical implications: future DST methods can focus engineering effort on novel selection criteria rather than sophisticated sampling distributions. The fact that γ=1 (subset size = active set size) is sufficient also suggests an "uncertainty principle" for DST: it is not necessary to examine all inactive connections to make good growing decisions — examining as many as are already active suffices, a finding that could guide theoretical analysis of sparse training dynamics.

## Suggestions

1. **Reframe the contribution** around "always-sparse training that matches/exceeds RigL's accuracy at reduced cost" rather than leading with accuracy improvement alone. This is both more accurate and still compelling.

2. **Provide a brief derivation** of both GSE's O(n) and RigL's O(n²) per-grow-step complexity in Section 3.2, and add a sentence contextualizing the amortized cost over training (accounting for RigL's periodicity T).

3. **Include a γ ablation on ImageNet** (at least one sparsity level) and justify the γ=2 choice — or report γ=1 results if they are comparable.

4. **Replace the 95th percentile** with standard deviation or report individual run values for the main CIFAR experiments.

5. **State explicitly** which baselines in each table are from the authors' runs vs. prior publications.

## Score & Decision

The paper proposes a clean, well-motivated always-sparse training algorithm with a simple and effective design. The core contribution — matching RigL's accuracy while being genuinely always-sparse with a cheaper update step — is real and valuable. The weaknesses are manageable (imprecise complexity analysis, missing γ-justification on ImageNet, suboptimal variability reporting) and addressable in revision. The overclaim about accuracy improvement is a framing issue rather than a factual error. Overall, this is a solid contribution to the dynamic sparse training literature.

**MY FINAL SCORE:** <pineapple>7.0</pineapple>
**MY FINAL DECISION:** <orange>Accept</orange>