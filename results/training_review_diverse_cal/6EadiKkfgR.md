Now I have all the information I need. Let me write the final consolidated review.

## Summary

This paper formalizes the connection between contrastive learning and semantic equivalence. It defines semantic equivalence (Definition 2.1) in a distributional sense — two symbols are equivalent if substituting one for the other never changes the output distribution given any context. The paper proves two main theorems: Theorem 3.1 shows that, under conditional equivalence and a basis condition, an optimal InfoNCE-style model maps semantically equivalent symbols to identical embeddings when labels are available. Theorem 4.2 extends this to the label-free setting. The Distributional Alignment Hypothesis (Definition 4.1) then bridges contrastive and downstream distributions: if conditional equivalence in the contrastive data coincides with semantic equivalence in the downstream data, Corollary 4.3 establishes a bidirectional correspondence between embedding equality and semantic equivalence. Experiments on a synthetic modular addition task illustrate the theory.

## Strengths

- **Formal grounding of semantic equivalence for contrastive learning.** The paper adopts a precise, task-agnostic definition of semantic equivalence (Definition 2.1) grounded in distributional invariance, allowing it to state and prove theorems linking contrastive objectives to the encoding of equivalence relations. This is a step beyond prior empirical observations.

- **Theorem 3.1 and Theorem 4.2 provide clean necessary conditions for optimal encoders.** Theorem 3.1 shows that when labels are available, an optimal solution to the contrastive loss forces embeddings of semantically equivalent symbols to be identical (under the stated conditions). Theorem 4.2 extends this to the label-free setting, requiring only conditional equivalence of context distributions. These results directly support the paper's central claim within its assumed setting.

- **The Distributional Alignment Hypothesis (Definition 4.1) formalizes when a contrastive distribution is useful for a downstream task.** The hypothesis connects conditional equivalence in contrastive data to semantic equivalence in downstream data. Corollary 4.3 then shows that under alignment, the optimal contrastive solution recovers downstream semantic structure exactly — a clean theoretical answer to the paper's research question.

- **Controlled experimental validation in a synthetic domain where all assumptions hold.** The ModAdd / CModAdd setup is designed so that conditional equivalence, alignment, and the basis condition are exactly satisfied. Figure 2a shows semantically equivalent pairs converging during training while non-equivalent pairs do not, directly illustrating Theorem 4.2. Figure 2b shows that pre-trained embeddings accelerate downstream learning, confirming practical benefit.

- **Candid discussion of limitations.** Section 7 openly acknowledges that the conditional equivalence assumption is "often too strong for practical applications" and that the alignment hypothesis is "quite strong" and impractical to verify in realistic scenarios. This transparency clarifies the scope of the contribution.

## Weaknesses

### Fatal
None.

### Major

1. **The key assumptions (conditional equivalence, distributional alignment) are very strong and limit the theory's applicability to real contrastive learning.**  
   Theorems 3.1 and 4.2 both require ∀ρ: p(ρ|u) = p(ρ|v) (conditional equivalence) alongside semantic equivalence or as sole premise. The paper concedes this is "often too strong for practical applications" (Section 7). The Distributional Alignment Hypothesis is itself a strong, untestable condition — it equates semantic equivalence under the *unknown* downstream distribution with conditional equivalence under the contrastive distribution. As the paper notes (Section 7), "in most realistic scenarios, verifying this hypothesis is impractical." These assumptions mean the theorems characterize an idealized regime rather than providing actionable guarantees for practical contrastive learning setups. The contribution is a consistency check on a clean mathematical setting, not a substantive characterization of how contrastive learners behave with real data and augmentations.

2. **The experimental validation is confined to a single synthetic task where all assumptions are exactly satisfied, providing no evidence the claims extend to realistic settings.**  
   The ModAdd / CModAdd setup (N=16, k=8, d=8) is a carefully constructed testbed where equivalence classes are known a priori, conditional equivalence holds deterministically, alignment is built in by design, and the embedding dimension matches the number of equivalence classes (8 residue classes, d=8). The paper acknowledges this is a "small controlled experiment" where hypotheses are "easily tested," but this is the minimum bar. No experiments probe robustness to violations of the assumptions (partial alignment, inexact conditional equivalence, finite-sample effects, or suboptimal optimization) — even though the paper itself notes that real contrastive learners succeed despite such violations. This leaves a gap between the paper's theoretical claims and any claim about "actual" contrastive learners.

3. **The title and central claim ("Contrastive Learners Are Semantic Learners") are broader than what is actually shown.**  
   The paper studies a specific asymmetric variant of InfoNCE applied to a particular symbol-context decomposition. It does not analyze other popular contrastive objectives (BYOL, SwAV, Barlow Twins, MoCo) or standard augmentation pipelines (stochastic crops, color jitter, etc.). The paper mentions these methods in the introduction but the theory only covers the narrow asymmetric SimCLR variant with symbol-extraction and context-extraction augmentations. A more precise title (e.g., "Optimal InfoNCE Models Encode Formal Semantic Equivalence Under Idealized Conditions") would better reflect the scope of the contribution.

### Minor

1. **The embedding dimension (d=8) was chosen to match the number of equivalence classes (k=8).**  
   This makes the basis condition trivially satisfiable and the learning problem artificially easy. Real tasks have orders of magnitude more semantic classes than embedding dimensions, and the paper does not discuss how the theory would apply when d is much smaller than the number of equivalence classes.

2. **The paper relates to optimal solutions, but trained neural networks rarely reach global optima on non-convex objectives.**  
   The theorems characterize a property of the loss landscape's optimum. The paper is clear about this ("optimal model"), but the experiments show distances approaching but not reaching zero, and the paper offers only a brief speculation ("likely due to the loss becoming close to zero preventing noticeable movement"). A brief discussion or probe of how close trained solutions come to the theoretical ideal would help calibrate practical relevance.

3. **The Distributional Alignment Hypothesis is not constructive — it defines what alignment *is* without guidance on how to achieve or verify it.**  
   The hypothesis is a definition, not a testable or designable condition. The paper acknowledges this ("verifying this hypothesis is impractical"), but this means the central condition for the main result cannot be checked in any real application. This limits the theory's utility as a design guide.

### Trivial
None.

## Nice-to-Haves

- A simple experiment where the conditional equivalence assumption is partially violated (e.g., perturbed symbol frequencies in ModAdd) would strengthen the paper by showing how the theory degrades gracefully.
- An empirical check of whether backward direction of Corollary 4.3 holds (i.e., that distinctly embedded symbols correspond to distinct semantic classes) on the synthetic task.
- A discussion connecting the paper's framework to existing theoretical analyses (Arora et al., HaoChen et al., Wang & Isola) more concretely, e.g., by showing whether their assumptions imply or are implied by the alignment hypothesis.

## Removed Points

- **Harsh Critic Issue 4 (backward direction inadequately justified):** The reviewer criticizes that the backward direction of Corollary 4.3 is not justified in the main text and refers to Proposition A.4. Per the meta-review rules, criticisms about proofs deferred to the appendix are removed since the parser strips appendices from all papers; the full proof exists in the original submission. The substance about the "immediate" claim being slightly misleading in the main text is noted but does not rise to a weakness since the formal proof is present.
- **"Distributional alignment hypothesis is a tautology":** This characterization is an overstatement. The hypothesis states an equivalence between two conditions on two different distributions — this is a substantive, contingent condition, not a tautology. The paper is clear that this is a strong assumption that cannot be verified in practice.
- **Strength Finder generic strengths filtered:** Some generic strengths (e.g., "this paper addressed an important problem") were dropped as they lack specific content tied to the paper.

## Novel Insights

The main novel insight from the review process is that the paper's formal framework, while clean, faces a fundamental tension: the conditions that make the theory work (exact conditional equivalence, perfect alignment) are precisely the conditions that ensure the problem statement itself is almost tautologically solved. The paper shows that under the assumption that the contrastive data perfectly mirrors the downstream semantic structure, contrastive learning recovers that structure — which is mathematically sound but leaves unanswered the harder question of *why* standard augmentations (which do not guarantee these conditions) nonetheless induce useful semantic structure in practice. The paper's most valuable contribution may be in providing a precise vocabulary (semantic equivalence, conditional equivalence, alignment) for discussing these questions, even if the answers it provides are limited to idealized settings.

## Suggestions

1. **Scope the claims more precisely.** Either temper the title to reflect the specific setup analyzed (asymmetric InfoNCE variant, symbol-context decomposition) or add a brief argument for why the results should generalize to other contrastive objectives.
2. **Add at least one experiment probing robustness to assumption violations.** For example, a version of ModAdd where symbol frequencies are not uniform across equivalence classes would test how the theory degrades when conditional equivalence is violated. Even a simple synthetic relaxation would substantially strengthen the empirical support.
3. **Provide constructive guidance on checking or achieving alignment.** Even an illustrative example showing when alignment approximately holds (or fails) on a small real dataset (e.g., CIFAR-10 with defined "symbols" as image patches) would make the theory more practically useful.
4. **Note explicitly in the main text that the backward direction of Corollary 4.3 requires a nontrivial argument** (provided in the appendix) rather than claiming the proof is "immediate," to avoid misleading readers.

## Score and Decision

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>