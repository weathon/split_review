Now I have all the information I need. Let me compile the final review.

---

## Summary

This paper proposes a learnable three-channel Gray-Wyner Network (GWN) for separating common and private information between two vision tasks. It contributes (1) lossy common information bounds (Theorem 1) relating Wyner's and Gács–Körner common information to interaction information, (2) an optimization objective with a parameter β that controls the transmit–receive rate tradeoff, and (3) a "Shared" neural architecture with conditional entropy models. Experiments on a synthetic dataset, colored MNIST under three dependency structures, and two real-vision benchmarks (Cityscapes, COCO) demonstrate that the method outperforms independent coding and alternative architectures.

## Strengths

- **Novel theoretical bridge (Theorem 1)**: The paper extends Wyner's lossless result to the lossy case, establishing bounds that relate Wyner's and Gács–Körner common information through interaction information of optimal rate-distortion tuples (Section 3.1). This provides a principled information-theoretic characterization of the tradeoff the codec must navigate, and is a substantive theoretical contribution.

- **Well-designed controlled experiments**: The synthetic dataset with known mutual information (Section 4.1) and the three colored-MNIST PMFs (Dependent, Independent, Mixture; Section 4.2) provide clean, interpretable tests of the method's behavior. On synthetic data, the common channel rate aligns with empirical mutual information as expected: exceeds it when optimizing transmit rate (β=1) and falls below when optimizing receive rate (β=2). On colored MNIST, the codec allocates common-channel rate appropriately—dominant under full dependency, near zero under independence, and intermediate for the mixture case.

- **Architecture comparison with theoretical backing**: The Shared architecture consistently outperforms the Separated and Combined alternatives across all β values (Figure 3b, Appendix D). Appendix C provides a compatibility analysis based on Rademacher complexity, offering theoretical justification for why shared analysis transforms reduce the generalization burden of aligning representations.

- **Practical performance on real vision benchmarks**: On Cityscapes (segmentation + depth) and COCO (detection + keypoints), the proposed method substantially reduces receive rate compared to independent coding (e.g., from 4.409 BPP to 3.089 BPP on Cityscapes at comparable task accuracy; Figure 5), while approaching joint coding performance in transmit rate.

- **Clear connection to classical information theory**: The paper revives the Gray-Wyner network in a modern learned-compression context, offering a fresh perspective on multi-task representation learning that is distinct from standard variational or disentanglement approaches.

## Weaknesses

### Fatal
None.

### Major

- **Transmit–receive tradeoff not demonstrated on real vision tasks**: The β-controlled tradeoff between transmit and receive rates is a core contribution of the paper. However, on Cityscapes and COCO (Section 4.3), only β=1 is evaluated. The paper acknowledges in Appendix D.5 that "All experiments are trained with β=1, which, as previously discussed, due to the constraints of the auxiliary loss, does not necessarily optimize for the transmit rate." No results are reported for β=3/2 or β=2 on real tasks. The empirical tradeoff is demonstrated only on a synthetic toy dataset and colored MNIST. For practical computer vision settings, the claim that the method can navigate the Gray-Wyner achievable region is not substantiated. This significantly weakens the paper's central empirical contribution.

### Minor

- **Theoretical looseness between Theorem 2 and the Shared architecture**: Theorem 2 (Eq. 10) assumes Y₁ = f₁(X₁) and Y₂ = f₂(X₂)—that each private analysis transform depends only on its corresponding source. The Shared architecture (Section 3.3, Eq. 13) feeds both X₁ and X₂ into each analysis transform f₁, f₂. The paper notes this relaxes the Markov conditions of Eq. 1 ("This effectively removes the requirement for the conditions in 1"), but does not address the mismatch with Theorem 2's own assumptions. Consequently, the Lagrangian (Eq. 12) is derived under conditions that the trained architecture violates. While a more general architecture does not invalidate the Lagrangian as a reasonable optimization objective (more inputs can only help), the claimed tightness of the theory-to-practice mapping is weakened. The paper should discuss this gap explicitly rather than only addressing the Markov conditions.

- **Limited baseline comparisons**: The paper compares only against its own architectural variants (Joint, Independent, Separated, Combined). Multi-task learned compression methods exist and are cited (Chamain et al., 2021; Feng et al., 2022; Guo et al., 2024). The paper argues these use only common channels without private channels, making them conceptually equivalent to the Joint baseline—which is a reasonable argument. However, empirical comparison against at least one published multi-task codec would strengthen the claim of practical value and help contextualize the magnitude of the reported gains.

- **Common-information isolation not directly validated on real tasks**: On Cityscapes/COCO, there is no quantitative measurement (e.g., mutual information estimation between the common representation and task targets) or qualitative visualization of what the common channel captures. The evidence that the common channel distills task-relevant common information on real images is indirect—it relies on the observation that the receive rate is better than Independent coding. The synthetic and MNIST experiments provide stronger validation, but a direct probe on real tasks would ground the central claim more firmly.

- **β = 3/2 as "equal optimization" is heuristic**: The interpretation of β=3/2 as equally optimizing transmit and receive rates (Section 3.2) follows from the Lagrangian relaxation but lacks formal justification. The Lagrangian treats the common channel rate with weight β and private rates with weight 1; the claim that β=3/2 "equally optimizes for both" is intuitive but not rigorous. This is presented as fact rather than as a heuristic interpretation.

### Trivial

- The interaction between the auxiliary matching loss (γ, Eq. 15) and β is acknowledged as requiring compensation (reducing β when γ=1), but this interaction makes β a less clean knob than the theory suggests. This circularity could be discussed more transparently in the main text rather than only in Section 3.3.

## Nice-to-Haves

- Training and evaluating the Shared architecture under the strict assumptions of Theorem 2 (i.e., f₁ only sees X₁, f₂ only sees X₂) would quantify how much the architectural relaxation actually helps and test whether the theory's predictions hold under its intended conditions.

- Extending β ∈ {1, 3/2, 2} experiments to at least one real vision benchmark (Cityscapes or COCO) would substantially strengthen the paper's main empirical claim.

- Qualitative visualizations (reconstructions or feature maps) of what the common channel represents on Cityscapes/COCO—analogous to the MNIST per-channel reconstructions in Appendix D.4—would make the information-separation claim more tangible.

- A three-task experiment would test scalability, as the paper notes the exponential channel scaling makes this challenging.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Harsh Critic Section-by-Section claim that "the step 'an optimization over probability distributions … can be swapped by an optimization over a family of functions' needs more justification"**: The proof is deferred to Appendix B, which the parser stripped. The original submission contains this justification, so criticizing its absence is a parser artifact.

- **Harsh Critic claim that "the custom autodiff trick… is fragile and not commonly used in learned compression"**: Straight-through gradient estimation for quantization is standard in learned compression (used since Theis et al., 2017; Ballé et al., 2018). The element-wise matching operation with gradient flow (Eq. 14) is a design choice, not an inherent flaw. Calling it "fragile" is a value judgment rather than a verifiable criticism.

- **Harsh Critic claim that the reconstruction loss "turns the system into a form of human-and-machine coding, which is not the problem the paper set out to solve"**: The reconstruction loss is applied *before* the task models to improve rate-distortion performance when task models are frozen—a practical training strategy, not a scope violation. The paper acknowledges this limitation in Appendix D.5.

- **Harsh Critic claim about "-81.58% in transmit rate" being "ambiguous"**: The paper explicitly states this is "against single-task codecs" and the context (Section 5) summarizes results from Tables 7-8. The number is the BD-rate averaged across three experiments, not ambiguous.

- **"No qualitative visualizations of what the common channel contains" for Cityscapes/COCO**: Moved to Nice-to-Haves. The paper provides MNIST visualizations in the appendix. Missing them for real tasks is a limitation but not a flaw in the existing evidence.

- **"Missing Parts and Places to Improve" requesting an ablation enforcing Markov conditions, and mutual information estimation**: Moved to Nice-to-Haves. These would strengthen the paper but are methodological preferences rather than required validation.

## Novel Insights

The most genuinely novel insight emerging from this work is the explicit connection between lossy common information measures (Wyner's and Gács–Körner) and the interaction information of rate-distortion-optimal representations (Theorem 1). This gives a concrete, measurable interpretation to the transmit–receive tradeoff in the Gray-Wyner network: the gap between the two common information measures corresponds to how much interaction information differs between representations optimized for joint vs. marginal rate-distortion. The paper also makes the interesting observation that this gap is likely large in practice (Gács–Körner common information is zero for jointly Gaussian sources with any correlation less than 1), which motivates the practical importance of navigating the tradeoff rather than simply targeting one extreme.

## Suggestions

- Add an explicit discussion in Section 3.3 acknowledging that the Shared architecture relaxes not only the Markov conditions of Eq. 1 but also the per-source determinism assumptions of Theorem 2, and explain why the Lagrangian objective remains a reasonable choice despite this relaxation. This would preempt the most significant theoretical criticism.

- If compute permits, run β=2 (or at minimum β=3/2) on Cityscapes or COCO and add a brief note about the results. Even a single β-variation point on one real benchmark would substantially strengthen the paper.

- Clarify in the main text (not just the appendix) that the auxiliary loss (Eq. 15) interacts with β and that this is why β=1 on real tasks does not optimize purely for transmit rate. Currently this important caveat is buried in Appendix D.5.

## Score and Decision

**Anchor comparison:**

| Anchor | Score | Comparison |
|--------|-------|------------|
| mUIGdUTtk2 (Cross-Domain OT Compression) | 6.00 (Oral) | Similar theory-practice gap but more rigorous closed-form theory. Our paper has broader experiments but weaker theory-to-practice alignment. |
| YDRoTtmXu1 (CoTAM for MLLMs) | 6.00 (Poster) | Stronger empirical validation and clearer practical impact. Our paper has more theoretical depth but weaker real-task empirical claims. |
| lO6I66lweK (Hierarchical Coding + Spectral Reg.) | 5.50 (Poster) | Comparable technical depth. Our paper has a more novel problem framing but a bigger gap between claimed and demonstrated contributions. |
| isFHz8qf20 (Information Theory for Agentic Systems) | 5.00 (Poster) | Similar in bridging information theory with modern ML systems. Our paper has more extensive experiments. |
| YzHbFwYmE1 (R-D Limits Framework) | 4.00 (Reject) | Weaker theory, limited novelty. Our paper is significantly stronger in both theoretical and empirical contributions. |
| X54rAhS4Iz (R-D for Transformer Inference) | 3.00 (Reject) | Much weaker theory-practice connection and motivation. Our paper is clearly stronger. |
| brRjG5G9Qu (Combine-ICMH) | 2.50 (Reject) | Incremental work. Our paper is far more original. |

The paper under review makes genuine, novel contributions: the lossy common information bounds (Theorem 1), the β-controlled tradeoff framework, and the Shared GWN architecture. The controlled experiments are well-designed and support the core claims. However, the paper's central empirical claim about navigating the transmit–receive tradeoff is not demonstrated on real vision tasks, and there is a notable but not fatal gap between the theoretical assumptions of Theorem 2 and the actual architecture. Relative to the anchors, this paper is clearly stronger than the 3–4 range rejects (better theory and experiments than X54rAhS4Iz and YzHbFwYmE1), but does not reach the level of the 6.0 Oral paper (mUIGdUTtk2) which has tighter theory. It is comparable to the 5.0–5.5 poster-level papers.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>