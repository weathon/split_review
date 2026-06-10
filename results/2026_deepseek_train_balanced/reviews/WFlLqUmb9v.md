## Summary

This paper proposes FIA-Net, a time-series forecasting architecture that aggregates information across STFT windows in the frequency domain using two MLP backbones: a window-mixing MLP (WM-MLP) that mixes adjacent windows, and a hyper-complex MLP (HC-MLP) that treats p STFT windows as a single hyper-complex vector and processes them via octonion algebra. The paper claims consistent improvements over seven baselines across six benchmarks, with parameter efficiency gains from both frequency compression and the HC-MLP structure.

## Strengths

- **Novel use of hyper-complex algebra for STFT window aggregation**: The HC-MLP (Section 4.2, Eq. 1–2) provides a principled and parameter-efficient way to combine information from all STFT windows simultaneously. Using octonion multiplication, this requires only p weight matrices for p=4 windows, which is a concrete architectural innovation over prior STFT-based models (FreTS, FREQTSF, FRETS) that process windows independently. The equations and parameterization are clearly presented for the p=4 case.

- **Empirical finding of complex-component redundancy**: Section 5.3.3 (Table 3) reports that masking either the real or imaginary component of inputs or weights does not significantly degrade accuracy. While the Kramers-Kronig explanation is acknowledged as a conjecture, this observation is non-obvious and could motivate simpler architectures. This is a genuine empirical discovery, properly scoped.

- **Frequency compression analysis**: Section 5.3.1 (Figure 5) demonstrates that selecting only the top-M frequency components (often M=4) improves accuracy over using all components, with a cogent explanation about reducing NN class complexity. This provides practical guidance for deployment.

## Weaknesses

### Fatal

- **The WM-MLP architecture — one of the paper's two main contributions — is never formally defined.** Section 3 ("PROPOSED MODEL: FIA-NET") states that it will describe the model but contains only a motivation paragraph and two conceptual figures. No equations, tensor operations, weight structure, or mixing rule for the WM-MLP are specified anywhere in the paper. The paper claims it as a contribution ("We construct the FIA-Net with the WM-MLP backbone," line 19), references it throughout the experimental discussion, and even states it requires "3p-2 weight matrices" (line 91), but never specifies what those matrices do or how they combine adjacent windows. A new-method paper that does not define one of its two primary architectural innovations cannot be evaluated, reproduced, or built upon. This is a structural flaw: the contribution as presented is incomplete.

### Major

- **HC-MLP is formulated and evaluated only for p=4, while the WM-MLP comparison is asymmetric.** Section 4.2 explicitly restricts the HC-MLP to p=4. The main results (Table 1) compare a WM-MLP optimized over different p values against an HC-MLP locked at p=4. Although Table 2 attempts a "fair" comparison at p=4 for both, the HC-MLP's generalization to other p values is not discussed. The claim of "three times fewer parameters" (line 5, line 91) is only asserted for this specific configuration and depends on an architecture (WM-MLP) that is not defined.

- **The baseline set is outdated and omits the most relevant competitors.** The paper compares against FedFormer, Reformer, Informer, Autoformer, FreTS, PatchTST, and LSTF-Linear (line 105). Missing from this set are DLinear and NLinear (from the same line of work as LSTF-Linear), TimesNet, TiDE, and — most importantly — FREQTSF and FRETS, which are the STFT-based methods discussed in the related work (line 39) and are the most natural comparators. This makes the claimed state-of-the-art results difficult to trust, as the evaluation stack is tilted toward older or less competitive methods.

- **The lookback window ablation makes unsupported claims about competing models.** Section 5.3.2 states that "many models exhibit parabolic behavior, where performance deteriorates after a certain point... In contrast, our model maintains stable performance." However, Figure 6 plots only FIA-Net's own performance. No curves for any other model are shown or referenced, so the claim about other models' behavior is an assertion without evidence within this paper.

### Minor

- **All three main result tables are embedded as bitmap images.** Tables 1, 2, and 3 are inaccessible as numerical data. The textual summaries ("average improvement of 5.4% in MAE," "up to 20% improvement") cannot be verified against per-dataset, per-horizon numbers. This makes the evidential basis for the paper's central accuracy claims opaque.

- **The Kramers-Kronig explanation for complex-component redundancy is acknowledged as speculative but presented with a misleading degree of certainty.** Section 5.3.3 says "This phenomenon can be explained through the Kramers-Kronig relation" before conceding it is a "conjecture." The KKR applies to analytic complex functions, and no argument is given that discrete STFT representations satisfy analyticity. This is an interesting observation, not a supported explanation.

- **The forward-pass complexity claim (O(L log L / p), line 19) is stated without derivation.** The actual complexity of STFT with overlapping windows of a given size does not straightforwardly reduce to O(L log L / p) without specifying the FFT size per window and the overlap ratio.

### Trivial

- None beyond those already listed as minor.

## Nice-to-Haves

- Include FREQTSF and FRETS as direct baselines since they share the STFT-based approach and are discussed in the related work.
- Provide a derivation or reference for the O(L log L / p) complexity claim.
- Extend the HC-MLP formulation to other values of p, or at minimum discuss the generalization pathway.

## Removed Points

The following points from the harsh critic or strength finder were removed or downgraded with justification:

- **"Tables are images means evidence is inaccessible"** — Kept as a Minor weakness because the textual summaries of results are still present; the tables being images prevents per-detail verification but does not make evidence wholly absent.
- **"KKR explanation is mis-sold"** — Downgraded from harsh critic's "methodological gap" to Minor because the paper explicitly uses the word "conjecture" and defers a complete study to future work. The criticism overstates the paper's assertiveness.
- **"Missing appendix details (hyperparameters, epochs)"** — Removed per instructions: the parser strips appendix content from all papers; these details exist in the original submission.
- **Strength: "Robustness to lookback window size"** — Removed because the paper only plots FIA-Net's own performance and makes an unsupported claim about other models. The evidence does not support the strength as stated.
- **Strength: "Consistent accuracy improvement"** — Kept as stated in Strengths but paired with weaknesses about unverifiable tables and outdated baselines.
- **"HC-MLP uses three times fewer parameters" as stated** — The parameter count claim depends on the undefined WM-MLP architecture and only holds for p=4. This is reflected in the weaknesses rather than presented as an unqualified strength.
- **Criticism about questionable model/model existence/release** — None raised.
- **Formatting/style nitpicks, typos, grammar** — Removed per instructions.
- **Missing related works** — Removed per instructions.

## Novel Insights

The most interesting observation to emerge from the reviews is that the paper's claimed contribution structure is misaligned with its actual content. The WM-MLP is presented as a primary contribution in the title, abstract, and contributions list, yet the paper only provides a meaningful mathematical specification for the HC-MLP. This creates a fundamental disconnect between what the paper promises and what it delivers. A secondary insight is that the Kramers-Kronig finding — if the redundancy observation holds more broadly — could lead to radical parameter reduction in frequency-domain models, but the paper's current evidence (one dataset, one setting) is far too thin to support this direction.

## Suggestions

1. **Formally define the WM-MLP architecture.** Provide equations for how adjacent STFT windows are mixed, the weight matrix structure, and how p determines the parameterization. Without this, the paper is incomplete as a methods contribution.
2. **Add the most relevant baselines**, particularly FREQTSF and FRETS (discussed in related work but not compared against), as well as DLinear and NLinear. Report honestly whether the improvements hold or diminish against these methods.
3. **Make all result tables readable as text** so that per-dataset, per-horizon numbers can be inspected, and report standard deviations or confidence intervals where feasible.
4. **In the lookback ablation (Section 5.3.2), either include comparison curves for other models** or remove the unsupported claims about their "parabolic" behavior.
5. **Scope the HC-MLP contribution accurately**: state clearly that it is currently formulated only for p=4 and discuss how it might generalize.

## Score and Decision

MY FINAL SCORE: <score>3.0</score>
MY FINAL DECISION: <decision>Reject</decision>