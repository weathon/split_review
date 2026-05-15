Now I have all the information I need. Let me compose the final consolidated review.

## Summary

This paper proposes Causal Transfer Learning (CTL), a method that leverages pre-trained language model (PLM) representations from two stages (pre-trained vs. fine-tuned) as paired environments to identify invariant causal features via the von Kügelgen et al. (2021) framework, then applies a front-door-inspired adjustment using token-level local features to improve OOD generalization under a single-domain scenario. The method is evaluated on semi-synthetic and real-world sentiment analysis benchmarks.

## Strengths

- **Novel use of PLM stages as natural paired environments for causal feature learning**: The paper exploits the pre-training and fine-tuning stages of PLMs to obtain two representations (R₀, R₁) of the same input, treating them as two views that share causal content C but differ in spurious factors S (Assumption 2). This bridges causal representation learning (von Kügelgen et al.) with practical NLP fine-tuning and allows identifying invariant features without requiring multiple observed domains.

- **Consistent and substantial OOD gains across benchmarks**: In semi-synthetic experiments (Table 1), CTL outperforms SFT by 9–13% F1 on the strongest OOD splits (e.g., Yelp OOD 10%: CTL 58.40 vs. SFT 49.24; Amazon OOD 10%: CTL 56.40 vs. SFT 49.33). In the real-world experiment (Table 2), CTL achieves 49.22 F1 at OOD 10% vs. SFT 37.78 and SWA 47.41. The gains are consistent across multiple OOD severity levels.

- **Informative ablation studies**: The ablations (CTL-N without front-door adjustment, CTL-C using only causal features, CTL-Φ using only spurious features) provide meaningful isolation of components. CTL-Φ's performance correlates strongly with spurious distribution shifts (dropping to 12.40 at OOD 10% on Amazon), confirming that Φ captures spurious information. CTL-N is consistently worse than CTL, supporting the role of the do(x) adjustment.

- **Single-domain applicability**: Unlike many domain generalization approaches that require multiple observed domains (e.g., IRM), the method works with a single supervised dataset plus a pre-trained model, which is a practical advantage for real-world deployment.

## Weaknesses

### Fatal

None. The paper's empirical contributions are real and the core research direction is interesting. However, the theoretical framing has serious issues described below.

### Major

1. **Inconsistency between the Decomposition Assumption and the causal graph (Fig. 1c)**: Assumption 1 states that X can be decomposed as X = f(S, C), meaning C and S are generative components of X (C → X, S → X in generative direction). Yet the graph (Fig. 1c) shows Φ → C (where Φ is derived from X), reversing the causal direction. The caption states that "X is broken and abstracted into vectors R⁰, R¹ and Φ," but the graph places C downstream of X's features rather than as a generative parent. The do-calculus derivation in Theorem 2 operates on this graph, and if the graph does not encode the true generative process, the derived identification formula lacks a valid causal foundation. The paper does not clarify whether Fig. 1c depicts computational dependencies among learned representations or true generative causal structure — and for do-calculus, it must be the latter.

2. **Insufficiently justified do-calculus derivation in Theorem 2**: The proof of Theorem 2 contains steps that are not properly justified against the graph:
   - **Step 1**: \(P(y \mid do(x)) = P(y \mid do(s,c))\) assumes that intervening on X is equivalent to intervening on (S, C) jointly under the decomposition X = f(S, C). This relationship is not standard do-calculus and requires additional justification about the functional form of f.
   - **Step 2**: \(P(y \mid do(s,c)) = P(y \mid do(c))\) via Rule 3. This requires verifying that Y is d-separated from S in the graph where incoming edges to S and C are removed. Given the bidirected edges R₁ ↔ Φ and Φ ↔ Y in the graph, there is a plausible active path S₁ → R₁ ↔ Φ ↔ Y that is not blocked, making this application of Rule 3 unverified. The paper checks none of these conditions.
   - **Step 3**: The front-door step \(\sum_{\Phi'} P(y \mid \Phi', c) P(\Phi')\) is presented without verifying the standard front-door criterion conditions against the graph, which includes the bidirected edge Φ ↔ Y (a likely unblocked backdoor path from the mediator to Y). The formula conditions on c (which may block this path), but this deviates from the standard front-door framework and is not formally justified.

   Because the paper's central claim is providing a *principled causal identification* result, these gaps in the derivation are serious.

3. **The "front-door" label overstates what is established**: The paper claims to apply a "front-door adjustment" (appearing in the title's framing, abstract, and main text). However, the actual formula used — \(P(y \mid do(x)) = \sum_{\Phi', x'} P(y \mid \Phi', c) P(\Phi' \mid x') P(x')\) — conditions on the learned causal features c, which is not the standard front-door formula. The relationship between this formula and the standard front-door criterion is unclear, and the required conditions (mediator intercepts all paths, no backdoor from X to mediator, backdoor from mediator to Y blocked by X) are neither stated nor verified.

### Minor

1. **CTL-C performs nearly as well as full CTL, raising questions about what drives gains**: In Table 1, CTL-C (using only causal features C) is often within 1–3 F1 points of the full CTL on OOD splits (e.g., Yelp OOD 10%: CTL 58.40 vs. CTL-C 57.75; Amazon OOD 30%: CTL 65.24 vs. CTL-C 63.01). If C captures invariant causal features, the front-door adjustment through Φ adds relatively little. This suggests the main source of robustness may come from the invariant feature identification (via the paired representations) rather than the causal adjustment procedure itself. This does not invalidate the results but makes the claimed central role of the front-door adjustment harder to justify.

2. **Assumption 2 (Paired Representations) is asserted without evidence**: The claim that R₀ (pre-trained) and R₁ (fine-tuned) share the same causal factors C but differ only in spurious factors S is critical for identifying C via Theorem 1 (citing von Kügelgen et al., Theorem 4.4). The paper provides no empirical evidence or theoretical argument that PLM representations satisfy this property, nor does it test what happens when fine-tuning also shifts causal features. While assumptions are necessary in causal work, this one is both strong and central — the paper would benefit from validation on synthetic data with known causal/spurious splits.

3. **The sampling procedure in Algorithm 1 is underspecified**: Step 2 reads "Sample \(\tilde{x}_i\) and \(\bar{x}_i\) from \(\mathcal{D}\) which have the same label as \(y_i\)." The paper does not specify how these samples are selected (uniform? weighted? with replacement?) or how this affects the training distribution. This makes reproduction unnecessarily difficult.

4. **The shuffling of Φ to approximate \(P(\Phi')\) is a heuristic without theoretical justification**: Steps 7–8 in Algorithm 1 and Step 4 in Algorithm 2 shuffle Φ within a mini-batch to obtain samples from \(P(\Phi)\). This approximates the marginal distribution of Φ but relies on the assumption that Φ values are exchangeable across examples within a batch, which is not justified. If Φ is correlated with the label (as the experiments suggest it is), the shuffled samples may provide a biased estimate of the true marginal.

### Trivial

None that survive the filtering rules — the formatting and presentation issues are parser artifacts.

## Nice-to-Haves

- A baseline matching model capacity (adding a similarly-sized MLP to SFT without the causal adjustment) would help isolate whether gains come from the causal estimator or simply from additional parameters.
- A controlled experiment on synthetic text data with known causal/spurious generative factors would validate whether Assumption 2 holds in practice and whether the method correctly recovers the causal effect.
- Sensitivity analysis of the inference sample size K (mentioned in the paper but figures stripped by the parser — if included in the original, this point is moot).
- Qualitative analysis of what the learned causal features C actually capture (e.g., attention visualization, counterfactual nearest neighbors).

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Criticism about missing results for different K (inference sample size)**: The paper states it conducted this analysis (Section 6, "Further Analysis" point 3) and references figures. The parser strips figures; this analysis exists in the original submission.
- **Criticism that Proposition 3 declares non-identifiability then Section 4 claims identifiability**: This merely describes the paper's logical flow (problem → assumptions → solution) and is not a genuine weakness.
- **"No variance shown in main table"**: Variance is shown in boxplots (Figs. 4 and 6), which is an appropriate and standard way to display variance across runs.

## Novel Insights

The reviews surface an interesting tension: the paper's empirical results are consistently positive across multiple benchmarks and ablations, suggesting the method genuinely improves OOD robustness. Yet the causal derivation that the paper frames as its core contribution is not rigorously supported. This raises the question of whether the method's success can be attributed to the causal adjustment per se, or whether the paired-environment invariance learning (from von Kügelgen et al.) combined with the local feature shuffling heuristic is doing the work — potentially through a mechanism that has a different (perhaps simpler) explanation. A cleaner framing that separates the empirically validated algorithm from the causal narrative would better serve the contribution.

## Suggestions

1. **Clarify the causal graph**: Distinguish between the generative level (where X = f(S, C) and C → X) and the representation level (where features are extracted from X). Provide a single coherent graph that supports the do-calculus derivation, or remove the claim of rigorous causal identification and reframe the method as causally-inspired.

2. **Formally justify or correct the do-calculus derivation**: Either (a) provide a correct derivation with explicit verification of each d-separation condition against the graph, or (b) drop the pretense of formal causal identification and present the method as an empirically-motivated algorithm with intuitive causal motivation.

3. **Validate Assumption 2** with a controlled experiment where ground-truth causal/spurious factors are known, even on a small synthetic dataset, to establish that R₀ and R₁ indeed share C but differ in S.

4. **Provide clearer justification for why CTL-C performs nearly as well as CTL** — this could be framed as a feature rather than a weakness if the paper positions the paired-representation invariance learning as the primary contribution.

5. **Specify the sampling procedure** in Algorithm 1 unambiguously to support reproduction.

## Score and Decision

This paper tackles an important problem (OOD generalization for finetuned PLMs) with a creative and practically-motivated approach. The empirical results are solid and the ablation design is thoughtful. However, the paper's central claim — providing a *principled causal identification* via front-door adjustment — is not adequately supported. The causal graph is inconsistent with the stated assumptions, the do-calculus derivation has unverified steps, and the front-door conditions are not checked. Since the theoretical framing is the paper's advertised primary contribution, these issues are significant. The empirical findings are interesting enough to warrant future exploration, but the paper in its current form overstates its theoretical grounding.

MY FINAL SCORE: <pineapple>4.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>