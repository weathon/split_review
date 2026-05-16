I now have all the verification I need. Let me produce the final consolidated review.

---

## Summary

This paper presents a theoretical framework connecting contrastive learning to formal semantic equivalence. It introduces the concept of semantic equivalence (Definition 2.1, two symbols are equivalent if swapping them leaves the label distribution unchanged), defines the Distributional Alignment Hypothesis (connecting downstream semantic equivalence to contrastive conditional equivalence), and proves that under this hypothesis optimal contrastive models encode semantic equivalence relations (Corollary 4.3). Experiments on a controlled modular addition task support the theoretical claims. The paper is primarily a theoretical contribution with a small synthetic experiment for validation.

## Strengths

- **Novel formal connection between contrastive learning and semantic equivalence.** The paper provides a clean theoretical framework (Theorems 3.1, 4.2, Corollary 4.3) showing that under the Distributional Alignment Hypothesis, optimal contrastive models encode formal semantic equivalence relations. This moves beyond empirical observations to a formal treatment, which prior work mostly lacked.

- **Distributional Alignment Hypothesis as a conceptual bridge.** Definition 4.1 formalizes the relationship between contrastive and downstream distributions by equating semantic equivalence (label-based) with conditional equivalence (contrastive covariate-based). While strong, this hypothesis provides a clear, testable condition that connects two disparate data distributions — a novel contribution relative to prior theoretical analyses that assume latent variable structures (e.g., HaoChen et al. 2021, Arora et al. 2019).

- **Controlled experiment supporting the theory.** The ModAdd/CModAdd setup is explicitly designed to satisfy all assumptions (alignment, conditional equivalence, basis condition). Figure 2a shows semantically equivalent symbols' embeddings converging during contrastive training while non-equivalent pairs remain separated, and Figure 2b shows accelerated downstream learning with pre-trained embeddings (5 seeds with 95% CI). This provides proof-of-concept empirical support.

- **Honest discussion of assumptions and limitations.** Section 7 (Threats to Validity) explicitly acknowledges the impracticality of verifying the alignment hypothesis in real scenarios, the strength of the conditional equivalence assumption, and the limited applicability to practice. This intellectual honesty strengthens the paper's credibility.

## Weaknesses

### Fatal

None.

### Major

- **Title and framing overclaim relative to what is actually analyzed.** The title "Contrastive Learners Are Semantic Learners" suggests a universal property of contrastive learning. However, the analysis is restricted to a specific **asymmetric SimCLR variant** with explicit symbol-context decomposition (Section 2.2), where one branch extracts symbols and the other extracts contexts via specialized, non-standard augmentations. Standard contrastive methods (SimCLR, MoCo, BYOL) use symmetric architectures and shared augmentation pipelines without such decomposition. The paper acknowledges this gap briefly in Section 7 but does not argue why its setup captures the essence of typical contrastive methods. The result is a mismatch between the general-sounding title and the narrow, engineered scenario analyzed. This is fixable by retitling and reframing.

- **The Distributional Alignment Hypothesis is very strong and effectively assumes the key connection.** Definition 4.1 states that downstream semantic equivalence (label-based) is equivalent to contrastive conditional equivalence (covariate-based). This is not derived from any more basic principle nor observable from data — it is a postulate that, together with Theorem 4.2, essentially builds the desired conclusion into the premise. The paper honestly acknowledges this ("verifying this hypothesis is impractical" in Section 7), but this acknowledgement does not mitigate the brittleness: the theory offers no guidance on when the hypothesis approximately holds, how to detect violations, or what happens when it is partially satisfied. For a paper whose core result depends on this hypothesis, the lack of analysis around partial alignment or robustness to violations is a significant gap.

### Minor

- **Experiments do not fully validate the theory's strongest predictions.** The theory predicts that optimal embeddings map semantically equivalent symbols to *identical* vectors. Figure 2a shows distances decreasing but not reaching zero; the paper attributes this to "loss becoming close to zero preventing noticeable movement" — a plausible but unverified heuristic. No direct test checks whether the learned embedding function ℰ is constant on semantic equivalence classes (i.e., that the bijection of Corollary 4.3 actually holds). The classification experiment (Figure 2b) shows pre-trained embeddings help, which is consistent with the theory but also consistent with many other explanations.

- **Only one synthetic task; no failure-case analysis.** The experiment uses a single synthetic task (modular addition) where all assumptions hold by construction. The paper does not test what happens when the alignment hypothesis is violated (e.g., misaligned contrastive tasks) or when conditional equivalence fails. Such experiments would substantially strengthen the causal interpretation.

- **Figure 2a does not report variance or number of seeds.** For Figure 2b, the caption states "mean and 95% confidence interval of 5 models," but no similar information is provided for Figure 2a. It is unclear whether the distance curves represent a single run or multiple seeds.

- **The basis condition argument is heuristic.** The paper argues that the set of configurations where E* vectors do not form a basis has Lebesgue measure zero, concluding that "slight perturbation… would establish a basis almost surely" (line 75). However, E* is the *optimal* (deterministic) encoder after training, not a random matrix. The argument that this holds for the specific solution found by optimization is suggestive but not rigorous.

### Trivial

- The notation for augmentation distributions (ˆτ, ˆτ|t) is introduced but lacks concrete examples connecting back to the symbol-context interpretation.
- Figure captions for Table 1 and Table 2 appear with garbled content (lines 126–134), though this may be a parser artifact.

## Nice-to-Haves

- A direct test of whether ℰ(u) = ℰ(v) if and only if u and v are semantically equivalent (intra-class vs. inter-class embedding variance), and a test of whether the basis condition holds empirically.
- An experiment where the alignment hypothesis is deliberately violated (e.g., using different k values for ModAdd and CModAdd) to show that the embeddings *fail* to capture semantics — which would strengthen the causal claim.
- A comparison table of assumptions relative to prior theoretical work (Arora et al. 2019, HaoChen et al. 2021, Saunshi et al. 2022, etc.) to clarify where the Distributional Alignment Hypothesis stands relative to latent variable or class-conditional independence assumptions.

## Removed Points

These points are flagged to be removed; treat them with caution.

- *"Missing proof sketches in the main text"* and *"missing appendix"* — Removed: The paper references appendix sections (superscript markers "2", "3", "6") that are stripped by the parser; they exist in the original submission.
- *"The paper does not discuss computational requirements, scalability, or batch size role in InfoNCE"* — Removed: This is scope creep beyond what a theoretical paper with a small experiment should be expected to cover.
- *"Condition 3 (basis) argument about measure zero... but E* is deterministic after optimization"* — Removed/weakened from what was originally a critical point to a minor one: the paper's argument is heuristic but reasonable, and the reviewer's framing suggests a fatal flaw where none exists.
- *"A brief comparison table or discussion would help"* regarding related work — Removed as a removed point: the request is for scope creep beyond the paper's contribution, and the related work section is already comprehensive.
- *"The paper does not provide new empirical evidence"* — Contradicts the paper's controlled experiment (Figures 2a, 2b). Removed.
- *"The label-aware setup seems unnatural because it assumes labels are available during pre-training"* — The paper explicitly presents Section 3 as a stepping stone to the unsupervised case, so this criticism misunderstands the pedagogical structure.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface any insight about the paper that the paper does not already state.

## Suggestions

1. **Reframe the paper's scope.** The title "Contrastive Learners Are Semantic Learners" overclaims. A more accurate title such as "When Contrastive Learners Learn Semantics: A Distributional Alignment Analysis" or "Understanding Semantic Learning in Contrastive Models" would align with the actual contribution. Similarly, the paper should explicitly state that the analysis covers a specific asymmetric variant of contrastive learning and discuss more concretely how standard practices (random crops in SimCLR, masked token prediction, etc.) could be mapped into the symbol-context formalism.

2. **Analyze robustness to approximate alignment.** The theory's key practical vulnerability is that the Distributional Alignment Hypothesis rarely holds exactly. The paper would be substantially strengthened by even a simple analysis — theoretical or empirical — of how violations affect the result. For instance, a Lipschitz-style bound showing that near-alignment yields near-equivalence would greatly increase practical relevance.

3. **Strengthen the experimental validation.** (a) Run at least one experiment where alignment is deliberately broken to show the embeddings fail to capture semantics. (b) Report variance for Figure 2a. (c) Directly verify the bijection between semantic equivalence and identical embeddings (e.g., clustering analysis or nearest-neighbor checks on equivalence classes).

4. **Include proof intuition in the main text.** A brief paragraph explaining why Theorems 3.1 and 4.2 hold (e.g., pointing out that optimal contrastive embeddings must satisfy an inner-product structure that forces equality under the stated conditions) would help readers assess the reasoning without needing the appendix.

## Score and Decision

The paper presents a clean theoretical framework and a novel formal connection between contrastive learning and semantic equivalence. The Distributional Alignment Hypothesis is a genuinely new way to think about the relationship between contrastive and downstream tasks. The paper is well-structured, mathematically clear, and honest about its limitations. However, the gap between the general-sounding title/framing and the narrow, assumption-laden analysis is significant. The experiment, while supporting, is minimal and does not fully validate the core predictions. The strong assumptions (especially the alignment hypothesis, which effectively assumes the conclusion) limit practical relevance without any analysis of partial violations. For these reasons, the paper in its current form does not meet the bar for acceptance at a top venue.

**MY FINAL SCORE:** <pineapple>5.0</pineapple>
**MY FINAL DECISION:** <orange>Reject</orange>