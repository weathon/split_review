Now I have enough information to write the review. Let me compose it.

## Summary
The paper introduces Distributed Neural Architectures (DNAs), a framework where each token follows a learned, content-dependent path through a collection of modules (transformers, MLPs, attention blocks). Routers at each step select which modules process each token. The paper shows DNAs are trainable and competitive with dense baselines in both vision (ImageNet classification, within ~1% of ViT-small) and language (zero-shot benchmarks, Top-2 DNA outperforms GPT-2 medium on 6/7 tasks). It further analyzes emergent properties: path distributions follow power laws, modules develop specialization, and compute can be allocated dynamically based on input complexity.

## Strengths

1. **Novel architecture concept validated in two domains.** The paper demonstrates that a non-feedforward architecture with per-token learned routing is trainable at practical scale (ViT-small and GPT-2-medium scales). This is a nontrivial feasibility result that opens a new design axis beyond fixed-depth models. The Top-2 vision DNA (18M params) achieves 78.8% on ImageNet vs 79.8% for ViT-small (22M params), and the Top-2 language DNA outperforms GPT-2 medium on 6/7 zero-shot benchmarks (Table 3).

2. **Power-law path distribution as a quantitative organizing principle.** The finding that path frequencies follow a power law (exponent ≈ −1.2 for trained language, −1 for random) is a concrete, falsifiable observation about routing behavior that provides a baseline for future work in this area.

3. **Learnable, input-dependent compute allocation shown to correlate with semantic content.** Using identity modules and a bias-based objective (Eq. 2–3), DNAs learn to skip computation per token. In vision, the model allocates less compute to background-dominated images and more to boundary-rich images (Fig. 5). In language, low-compute documents correspond to HTML, bibliographies, or unfamiliar scripts (Sec. 4.3). The correlation between compute and content is demonstrated qualitatively with visualizations.

4. **Honest reporting of negative results.** The paper acknowledges that language-domain module reuse appears random (Sec. 4.3), that random initializations also show power-law path structure (Fig. 1c–d), and that the final Deep-Dream reconstructions are not classified correctly (Fig. 4). This transparency strengthens the credibility of the positive findings.

## Weaknesses

### Major

1. **Dense baselines are matched on active parameters but not total parameters, making it unclear whether performance comes from routing or extra static capacity.** Top-1 DNA vision: 34M total params vs ViT-small's 22M (+55%). Top-1 DNA language: 583M total vs GPT-2 medium's 406M (+44%). The Top-2 language DNA has both more total params (603M vs 406M) AND more active params (433M vs 406M). Without a dense baseline matched on total parameter count, the claim that DNA routing provides benefit over simply having more static capacity is not directly supported. (The Top-2 vision DNA at 18M total params vs ViT-small's 22M is a cleaner comparison but receives less emphasis in the paper's narrative.)

2. **The "emergent specialization" claim is partially undercut by the paper's own random-model baseline, and the distinction is not quantified.** The paper reports that random DNA models also exhibit power-law path distributions and can cluster patches by similarity (Fig. 1c–d, Sec. 3.2). The paper says the random model uses "a very different similarity measure" leading to clustering based on "superficial features," but this is a qualitative statement without a quantitative metric. Without measuring how much training *adds* to the structure already present in the architectural prior (e.g., mutual information between path identity and token class, or cluster purity for trained vs. random routing), the central interpretive claims about "emergence" rest on an unquantified distinction.

### Minor

3. **Router gradient estimation is under-specified.** The paper states that routing uses "hard top-k sampling" (Sec. 2.2) and combines module outputs via Eq. 1 using softmax probabilities ρ as weights. The softmax weights are differentiable, which provides a gradient signal to the router—this is the standard approach in MoE and is implicit in the formulation. However, the paper does not explicitly state whether gradients flow through the softmax weights, whether a straight-through estimator is used, or how the discrete top-k selection interacts with backpropagation. This detail affects reproducibility and should be clarified in the main text.

4. **Interpretability analyses are qualitative and would benefit from quantitative backing.** The language-domain claim that "early routers group similar tokens" (Sec. 4.2) is illustrated on two examples. The vision specialization analysis (Fig. 3) is a qualitative clustering visualization. Given that token embeddings already cluster by part-of-speech and semantics in the input space, a simple baseline (e.g., k-means on token embeddings compared to router assignments) would clarify whether the router learns structure beyond what is already present in the embedding layer. The paper would be strengthened by quantitative metrics for path specialization.

### Trivial

5. **"Any token can traverse any series of modules in any order"** (Abstract) slightly overstates the architecture: the forward pass is organized as a fixed sequence of routing steps (s = 1, 2, …, s_max), so tokens cannot go backward or visit modules in an arbitrary DAG order. This is clarified in Sec. 2, but the abstract framing could mislead.

## Nice-to-Haves
- A dense baseline matched on total parameter count (not just active parameters) would directly resolve whether routing adds value over extra static capacity. This is the single experiment that would most directly validate the paper's framing.
- A quantitative metric for path specialization (e.g., mutual information between path identity and token class, or cluster purity for trained vs. random models) would substantiate the "emergence" claim beyond qualitative comparison.
- A k-means clustering baseline on token embeddings for the language router analysis would clarify whether the router learns something beyond the trivial structure of the embedding space.

## Removed Points
These points were considered but removed per the filtering rules (they are included for reference but should be treated with caution):
- *"Deep-Dream reconstructions are classified wrong (bell pepper → spotlight)"* — The paper acknowledges and explains this; the paper is transparent about limitations, not spinning them.
- *"Module reuse in language appears random, contradicting vision findings"* — The authors honestly report this negative result. Reporting a domain difference is a feature, not a bug.
- *"References Roberts et al. 2022 and Doshi et al. 2023 relate to signal propagation, not gradient estimation"* — True but irrelevant: those references are cited for the form of Eq. 1 (residual signal propagation), not for router gradient estimation. The criticism conflates two separate parts of the method.
- *"Missing appendix details"* — Appendices are stripped by the PDF parser; they exist in the original submission.
- *"Missing related work"* — Cannot verify without external sources; per hard rules this is removed.
- *Formatting/style nitpicks* — Removed per hard rules.

## Novel Insights
The most striking observation, not fully articulated by the paper itself, is that **the power-law path distribution provides a natural compression principle for DNAs**: most tokens take few paths, meaning inference could be heavily cached or specialized for a small set of "frequent paths" without affecting most tokens. This turns a descriptive finding into a potential efficiency mechanism. Additionally, the fact that language-domain module reuse is random while vision-domain module reuse is structured (particularly the observation that high-reuse images lack distinct objects, and that two vision models agree on which images have high reuse) suggests that **parameter sharing emerges from perceptual invariances** (uniform backgrounds → same modules), a property that may not transfer to domains where token identity is highly contextual.

## Suggestions
1. Add a dense baseline matched on total parameter count (not just active parameters) for both vision and language. This directly addresses the most critical evaluation concern.
2. Add a quantitative comparison of trained vs. random routing behavior — e.g., compute k-means purity of path-based token clusters, or mutual information between path identity and token class — to substantiate the "emergence" framing.
3. Explicitly state the gradient estimation mechanism for the hard top-k routers (Sec. 2.2).
4. For the language router analysis (Sec. 4.2), add a baseline comparing router assignments to k-means on token embeddings to show the router learns nontrivial structure.

## Score and Decision

**Calibration anchors used:**

| Anchor | Avg Score | Query Bucket | Comparison to Paper Under Review |
|--------|-----------|-------------|----------------------------------|
| QHzzAU7Qf9 (SMEAR) | 6.00 | topic-mid | Routing method for MoE with cleaner experiments and proper baselines but less novel architecture concept. DNA paper is less rigorous but more novel. |
| z1mLNhWFyY (Gradient Routing) | 5.25 | topic-mid | Similar quality band — interesting method with evaluation limitations. DNA has broader scope but similar strength of evidence. |
| RQz7szbVDs (Initialisation's Impact on Specialisation) | 6.00 | topic-mid | Theory paper on specialization with rigorous analysis. DNA is more empirical and less rigorous. |
| XVHXVdoV11 (Collective Model Intelligence) | 3.40 | topic-low | Weak paper on model merging with unclear contribution. DNA is substantially stronger. |
| nyuaoVnVCa (Emergence of Language Agents) | 2.33 | weakness-emergent-claim | Poorly executed emergence paper with unclear contribution. DNA is far better executed. |
| 1gqR7yEqnP (Pan for Gold) | 2.20 | weakness-unsupported-claim | Paper with unsupported central claims. DNA has more grounded evidence. |
| Pu3c0209cx (Tight Clusters) | 7.00 | topic-high | Strong MoE routing paper with theory + large-scale experiments. DNA is less rigorous and less well-evidenced. |

**What the low-band anchors failed at, and does this paper share those failures?** The low-band anchors (XVHXVdoV11, nyuaoVnVCa, 1gqR7yEqnP) failed due to: (a) central claims not supported by evidence, (b) unclear or unoriginal contributions, and (c) poor execution/writing. The DNA paper does NOT share failures (b) or (c) — its contribution is clear and the paper is well-written. However, it partially shares failure (a): the "emergent specialization" claim is not fully supported because the paper's own data shows random models also produce structured routing, and the trained-vs-random distinction is not quantified. The parameter count confound also means the "competitive" claim rests on favorable comparison conditions. These issues are less severe than the low-band anchors' problems but are real and prevent the paper from reaching the quality level of the mid/high anchors.

**Score**: 5.0  
**Decision**: Reject

The paper introduces a genuinely novel architecture concept and provides interesting exploratory analysis across two domains. However, the evaluation is weakened by a parameter-count confound in the dense baseline comparison (total params differ substantially, making it unclear whether routing provides benefit over extra static capacity), and the central "emergent specialization" narrative is partially undercut by the paper's own random-model results without quantitative comparison. These issues are addressable, and with tighter claims and fairer evaluation the paper could become a strong contribution. In its current form, the evidence does not fully rise to the level of the claims.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>