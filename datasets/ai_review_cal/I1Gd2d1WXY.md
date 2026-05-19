- Decision: Reject
- Avg Score: 3.75
- Scores: 6, 3, 3, 3
Now I have all the information I need. Let me synthesize the final consolidated review.

---

## Summary

This paper introduces Adaptive Resolution Residual Networks (ARRNs), which structure residual networks using insights from Laplacian pyramids. **Laplacian residuals** enable a single network to be "rediscretized" to lower resolutions by simply evaluating fewer residuals — skipping inner architectural blocks and replacing them with a precomputed linear projection — while **Laplacian dropout** trains the network to be robust at low resolutions by randomly gating early residuals during training. The paper provides a theoretical derivation showing that, under ideal bandlimited signal conditions and perfect filters, the skipped residuals produce exactly the same output as the full network. Experiments on CIFAR10/100, TinyImageNet, and STL10 compare ARRN against fixed-resolution CNNs (ResNet, WideResNet, MobileNetV3, EfficientNetV2) and demonstrate that ARRN with Laplacian dropout maintains accuracy across resolutions whereas baselines degrade.

## Strengths

- **Novel theoretical guarantee for computation reduction**: Equations 12–15 formally derive that, under the assumption of bandlimited inputs and ideal filters, each Laplacian residual whose input spectrum lies within the lowpass filter passband collapses to a linear projection, skipping all nested architectural blocks. This gives a principled foundation for the claim that lower-resolution inputs require fewer residuals for the same output — a property absent in prior adaptive-resolution methods that require continuous-operator equivalence across all resolutions (Section 4.1, lines 122–132).

- **Laplacian dropout yields clear empirical robustness improvements**: Section 5.1 and Figure 5 show that ARRNs trained with Laplacian dropout maintain accuracy across decreasing resolutions, while ARRNs without dropout and all four fixed-resolution baselines degrade significantly. The paper also notes that EfficientNetV2's residual dropout (Huang et al., 2016) does not produce similar robustness, distinguishing Laplacian dropout as a bandwidth-targeted augmentation (lines 171, 178).

- **Negligible adaptation overhead**: Figure 7 shows that the precomputation for rediscretization (computing the chained linear projection) takes under 750 microseconds, making resolution adaptation effectively instantaneous — a practical advantage over methods requiring retraining or fine-tuning (Section 5.4, lines 189–192).

- **Flexible architectural compatibility**: The only constraint on inner blocks \(b_n\) is \(b_n(0) = \text{constant}\), which is satisfied by convolutions, normalizations, transformers, and their compositions (Section 4.1, line 92). This is a genuine advantage over neural operators and implicit neural representations, which require continuous-operator equivalence or atypical signal representations.

- **Consistent evaluation across four datasets and four strong baselines**: Experiments span CIFAR10, CIFAR100, TinyImageNet, and STL10, comparing against ResNet, WideResNetV2, MobileNetV3, and EfficientNetV2 — covering diverse dataset sizes and model families (Section 5, lines 162–164).

## Weaknesses

### Fatal
None.

### Major
- **The paper's framing promises comparison against adaptive-resolution methods that experiments do not deliver.** The Introduction states that ARRNs "combine the best features of both approaches" — fixed-resolution methods and adaptive methods (neural operators, implicit neural representations). Section 2 discusses these adaptive methods in detail and positions ARRN as a type of neural operator that "escapes the burden of maintaining the equivalence between continuous functions and discrete functions." However, every baseline in the experiments is a fixed-resolution CNN. No neural operator (e.g., FNO-type) or implicit representation method is included. While the paper correctly notes that these methods are "much more challenging to use in classification tasks" (line 29), the framing nonetheless sets up an expectation of comparison that goes unfulfilled. This does not invalidate the paper's core contribution — the fixed-resolution comparisons already demonstrate the value of single-network multi-resolution adaptation — but the rhetorical framing overreaches relative to the experimental evidence.

### Minor
- **Accuracy results from a single run with no error bars.** The paper states "All models are trained once" (line 162). For a method involving stochastic gating (Laplacian dropout uses Bernoulli random variables; line 155), the absence of multiple seeds or error bars weakens confidence that the reported accuracy curves are representative, especially for the fine-grained claim that rediscretized performance is "identical or better" (line 178). Timing measurements use 10 runs with median picking, but accuracy does not.

- **"Exact computation" claim is not qualified up front.** The abstract and introduction state that "lower resolution signals require a lower number of Laplacian residuals for exact computation" without immediate qualification that this holds under the ideal conditions of bandlimited signals and perfect (Whittaker-Shannon) filters. The practical implementation uses Kaiser-windowed approximations (Section 4.1, line 134), and Section 5.2 acknowledges that approximate filters cause "bleed-through" that prevents exactness in practice. The gap is disclosed in Section 5.2 but the abstract and introduction would benefit from upfront qualification (e.g., "exact under ideal conditions" or "theoretically exact").

- **Laplacian dropout probabilities \(p_n\) are not specified.** The gating mechanism is defined with Bernoulli random variables having probabilities \(p_n\) (Equation 20, line 155), but the main text never states what these values are or how they are set (e.g., constant across residuals, tuned, scheduled). This information may reside in the (parser-stripped) appendix, but the main text should state it.

### Trivial
- None.

## Nice-to-Haves
- Ablation studies varying the number of Laplacian residuals (depth) and comparing different lowpass filter designs (e.g., Gaussian vs. Whittaker-Shannon approximations) would strengthen the understanding of which design choices drive performance.
- A limitations section discussing when rediscretization may fail (e.g., when the input spectrum is not bandlimited or filter approximations cause significant leakage) and the extension to 1D/3D signals would improve the paper's completeness.
- Additional comparisons: training baselines directly at lower resolutions to compare against the single-network approach, and comparing inference-time compute savings more directly (e.g., FLOPs vs. accuracy curves).

## Removed Points

The following points from the inputs were removed with justification:

- **Experimental design ambiguity (Harsh Critic #2):** The paper is sufficiently explicit about the input protocol ("images are rediscretized to the lower resolutions, then rediscretized back to the native dataset resolution during evaluation... all methods have access to the same information in a fair manner," line 162). The critic's concern about whether ARRN receives direct low-res input or upsampled input is resolved by this statement — all models receive the same preprocessed input. Removed as misunderstanding.

- **Underspecification of inner blocks (Harsh Critic #3, part 1):** The paper states "subsection A.1 explains the architecture design in detail" (line 164). The appendix exists in the original submission but was stripped by the PDF parser. Per policy, parser-stripped content cannot be flagged as missing. Removed.

- **Zero-blocking filter confusion (Harsh Critic #3, part 2):** The paper defines \(\phi^{\text{zero}}\) as a filter that "subtracts the mean" shown in convolution form (lines 111–113). In signal processing this is a standard DC-blocking filter expressed as a convolution kernel. The critic's confusion about whether this is a global or local operation does not reflect a paper deficiency. Removed.

- **Missing related works:** Not flagged by any reviewer as missing specific citations; per policy, missing related works claims are removed as unverifiable without external sources.

- **Pure formatting/style nitpicks and claims about parser artifacts:** Removed per policy.

- **Generic concern about theoretical idealizations being "papered over" (part of Harsh Critic #3, part 3):** The paper explicitly acknowledges the theory-practice gap in Section 5.2 (line 178: "likely a result of the approximate filters used by the implementation, which allow a small quantity of information to bleed through"). The "papered over" characterization is inaccurate. However, the related concern about the abstract not qualifying "exact" is retained as a Minor weakness above.

- **Strength Finder generic strengths (importance of problem, etc.):** Removed as they are generic, superficial, or sycophantic. Only concrete, evidence-grounded strengths are retained.

## Novel Insights

None beyond the paper's own contributions. The two reviews identify a common gap (lack of adaptive-resolution baselines and statistical rigor) but do not surface any insight about the method's theory or design that the paper itself misses.

## Suggestions

1. **Qualify "exact" in the abstract and introduction** with a brief caveat (e.g., "under ideal bandlimited conditions") so readers are not misled about the practical implementation's faithfulness.
2. **Add error bars or multi-seed reporting** for all accuracy experiments — this is standard practice for classification benchmarks and is especially important given the stochastic training augmentation.
3. **Specify the Laplacian dropout probabilities \(p_n\)** in the main text, or at minimum state the design choice (e.g., constant, decreasing, tuned).
4. **Tone down the "best of both worlds" framing** or add a brief discussion explaining why adaptive-resolution baselines (neural operators, implicit representations) are not directly comparable on image classification tasks, since the paper already notes they are difficult to apply to classification (line 29). Alternatively, include one simplified adaptive baseline if feasible.
5. **Add a Limitations subsection** discussing conditions under which rediscretization may not preserve accuracy (e.g., filter approximation leakage, non-bandlimited real-world signals) and generalization to other signal types/dimensions.
