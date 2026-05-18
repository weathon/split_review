Now I have all the evidence needed. Let me write the consolidated review.

## Summary

This paper addresses the problem of monitoring whether a deployed ML model's performance has deteriorated under distribution shift, without requiring labels on the deployment distribution. It formalizes "disagreement-based post-deployment deterioration" (D-PDD), proposes the D-PDDM algorithm that monitors whether well-performing auxiliary models disagree more with the deployed model on deployment data than on training data, proves finite-sample guarantees on false positive and true positive rates, and validates the method on synthetic data, CIFAR-10.1, and a large-scale healthcare dataset (GEMINI). A key practical advantage is that the algorithm decouples monitoring into a pre-training stage (which compresses training-data information) and a deployment stage that requires no access to training data.

## Strengths

1. **Principled problem formulation and theory.** The paper formalizes deterioration monitoring in a way that separates deteriorating from non-deteriorating shifts, provides sample-complexity bounds (Theorems 4.2, 4.4) that depend on the VC dimension of the auxiliary hypothesis class and the deterioration gap, and characterizes the failure regime (Regime 2, Theorem 4.5) where the FNR/FPR tradeoff occurs. This goes well beyond the typical shift-detection literature which flags all distribution changes.

2. **Training-data-free deployment monitoring.** The two-stage design (pre-training on labeled data → monitoring on unlabeled data without access to training data) is a genuinely useful practical property. The paper correctly identifies that many prior disagreement-based methods (Rosenfeld & Garg, Ginsberg et al., Chuang et al.) require training data during deployment, and D-PDDM is the first to provably drop this requirement. This is validated experimentally and supported by the algorithm design in Section 3.

3. **Real-world healthcare validation on GEMINI.** The paper evaluates on a large-scale hospital dataset with both a natural temporal shift (non-deteriorating, where D-PDDM achieves FPR consistently below α=0.05 while baselines exceed 0.1) and a manufactured age-based deteriorating shift (where D-PDDM matches or exceeds all baselines). This is a meaningful demonstration on a practically relevant high-stakes domain.

4. **Theoretical characterization of the failure regime and remedy.** Theorem 4.5 and the accompanying analysis (Section 4.3.1, Figure 3) identify the precise condition (ε_q ≤ ε_p despite deterioration) under which D-PDDM fails, and show that reducing the base classifier's training error ε_f can provably move the system from this failure regime into solvable regimes. This provides actionable guidance grounded in the theory, not a hand-wavy suggestion.

5. **Comprehensive baseline comparison.** D-PDDM is compared against six baselines (MMD-D, H-divergence, multiple f-divergences, BBSD, RMD) across three different data modalities (synthetic, vision, healthcare). The baselines are given advantages (oracle access to generating distributions, permutation testing) ensuring comparisons are not artificially tilted in D-PDDM's favor.

## Weaknesses

### Fatal

None.

### Major

1. **Theory-practice gap between the VC-theoretic framework and the Bayesian sampling implementation.** The paper defines H_p ⊆ H as the set of hypotheses with err(h; P_g) ≤ ε_f and grounds its guarantees in the VC dimension d_p of this set. In the implementation, however, H_p is approximated by sampling weights from a Bayesian neural network posterior and computing disagreement rates. The paper states (line 90) "one can view H_p as encoding the model's posterior parameter distribution" but provides no formal argument — not even a sketch — that the set of networks reachable via posterior sampling corresponds to H_p with a bounded VC dimension, or that the optimization over this sampled set respects the theoretical conditions. While using bounded-architecture neural networks (~32 hidden nodes, line 237) does constrain the VC dimension, the specific connection between what is optimized (posterior samples) and what the theory demands (H_p satisfying err(h; P_g) ≤ ε_f with known VC dimension) is never established. This leaves a gap between the "provable" claims in the title/abstract and what is actually verified in the experiments.

### Minor

2. **Equivalence assumptions (Lemma 2.1) are acknowledged but their real-world scope is not assessed.** Lemma 2.1 requires identical ground-truth labeling functions (g = g') and bounded TV distance between marginals. Concept drift (the labeling function itself changing) is explicitly excluded. The paper notes (line 56) that PDD monitoring is "impossible for any arbitrary g' ≠ g," but never discusses how often the g = g' condition actually holds in the claimed application domains (healthcare, vision). Without this characterization, it is unclear how often D-PDD (the problem being solved) corresponds to PDD (the problem that matters) in practice.

3. **Empirical scope is modest relative to the claimed generality.** The deterioration benchmarks consist of one synthetic setting, one vision dataset (CIFAR-10.1), and one manufactured healthcare shift (GEMINI age). The non-deterioration evaluation covers synthetic data and one real temporal split (GEMINI). There is no non-deteriorating vision shift (e.g., adding benign noise to CIFAR-10 without changing the decision boundary), and no evaluation on subpopulation-shift benchmarks (e.g., WILDS) where both stable and degrading splits exist within a single dataset. The paper's claims about robustness generalize beyond what the current evidence supports.

4. **Pre-training cost and sensitivity are not reported.** The paper mentions "500 pre-training steps" (line 239) but provides no wall-clock time, no analysis of how the number of rounds or the size of Φ affect the test's reliability, and no discussion of sensitivity to the error tolerance ε₀ or the constraint satisfaction in Algorithm 1. For practitioners evaluating deployability, these are important.

5. **The significance level α is used with dual interpretations across theorems.** In Theorem 4.2, α is the desired FPR. In Theorem 4.4, α is described as "1 minus the desired TPR" but still appears in the δ formula alongside β. The paper notes this distinction in passing but does not clearly disambiguate or explain the rationale for reusing the same symbol with different meanings. This is confusing.

6. **The condition γ ≤ α and the role of γ in Theorem 4.2 are unexplained.** γ appears as a free parameter with no practical guidance for its selection. The bound's condition γ ≤ α is stated but not motivated, and the reader is left unsure how to set γ or what it controls beyond tightening the bound.

7. **Missing experimental details for GEMINI.** The size of each temporal split, the number of features, and the number of patients are not reported. Without these, it is hard to assess whether the non-deterioration claim on the temporal split is credible or an artifact of small sample sizes.

### Trivial

8. Theorem statements (4.2, 4.4) contain some garbled notation (bars over variables, missing parentheses) that appear to be OCR artifacts from the parsed text. These should be cleaned up in the camera-ready version.

## Nice-to-Haves

- Characterize how often the g = g' assumption holds in real healthcare/vision deployments, or discuss extensions to concept drift.
- Add a non-deteriorating vision experiment (e.g., benign image perturbations on CIFAR-10) to directly demonstrate FPR control in vision.
- Include a formal argument (or at minimum a heuristic justification with empirical validation) connecting the Bayesian posterior sampling to the theoretical conditions on H_p.
- Discuss guidelines for choosing the error tolerance ε₀, the number of pre-training rounds, and the size of Φ in practice.
- Report wall-clock pre-training times and dataset statistics for GEMINI.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **Missing disagreement-based baselines (Rosenfeld & Garg, Ginsberg et al.)**: The critic claims these should be compared against. However, as the paper states (lines 16, 263), these methods require training data during deployment, which is one of D-PDDM's key advantages. The paper's Table 1 compares desiderata satisfaction, not TPR/FPR on identical experimental footing. Comparing against methods that violate the training-data-free desideratum would not be apples-to-apples. **Removed as factually misaligned.**

- **Section 4.3.1 is a non-falsifiable prescription**: The critic characterizes this as "train a better base classifier." In fact, the section provides a theoretical characterization (Theorem 4.5, Figure 3) showing that reducing ε_f provably moves from Regime 2 (failure) to Regime 1 (solvable) or to non-deteriorating. This is a meaningful theoretical insight, not vacuous advice. **Removed as strawman.**

- **Missing proof sketches / appendix content**: The parser strips appendices; these exist in the original submission. **Removed per hard rule.**

- **Image-based pseudocode not visible**: Parser artifact. **Removed per hard rule.**

- **WILDS benchmark suggestion**: The paper already covers 3+ datasets across different modalities. Adding WILDS is scope creep. **Removed per scope-creep rule.**

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Bridge the theory-practice gap.** Either (a) provide a formal argument that the Bayesian sampling procedure approximately respects the theoretical conditions on H_p (e.g., showing that posterior samples concentrate on low-error hypotheses with high probability, and that the VC dimension of the sampled set is bounded), or (b) adopt a simpler hypothesis class (e.g., linear models on top of frozen features) where the connection to VC theory is transparent, and validate the guarantees directly in a controlled experiment.

2. **Add a non-deteriorating vision experiment.** A simple experiment (e.g., adding Gaussian noise or applying a benign affine transformation to CIFAR-10 that does not change the decision boundary) would directly demonstrate D-PDDM's FPR control in a vision setting, complementing the synthetic and GEMINI temporal results.

3. **Disambiguate α and document γ.** Clearly separate the notation for FPR-related α (Theorem 4.2) from the TPR-related parameter in Theorem 4.4. Provide practical guidance for setting γ and explain the condition γ ≤ α.

4. **Report pre-training costs.** Add wall-clock time, number of optimization rounds, size of Φ, and sensitivity to ε₀ and the number of pre-training steps. Report GEMINI dataset statistics (split sizes, feature dimensions).

5. **Discuss the practical scope of Lemma 2.1's assumptions.** Add a paragraph assessing how often g = g' and bounded TV hold in the paper's target application domains, and how a practitioner might recognize violations.

## Score and Decision

The paper addresses a practically important problem, provides a novel theoretical framework and algorithm with sample-complexity guarantees, and validates on multiple datasets including a large-scale healthcare deployment. Its main weakness is a genuine gap between the VC-theoretic guarantees and the Bayesian sampling implementation — the provable claims are proven for an abstract algorithm whose practical instantiation is a heuristically motivated approximation. This does not invalidate the paper's contributions (the formal framework, the characterization of failure regimes, the training-data-free design, and the empirical demonstrations are all independently valuable) but it does mean the "provable" framing is overstated for what is actually implemented. The remaining weaknesses (limited empirical breadth, unclear notation, missing cost analysis) are addressable.

Given its novelty on an underexplored problem, the soundness of the core theory, and the practical relevance of the healthcare validation, the paper merits a borderline accept.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>