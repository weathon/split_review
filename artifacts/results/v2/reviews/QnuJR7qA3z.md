## Summary

The paper introduces HARA, a framework that replaces all non-linear operators in Transformers (GELU, SiLU, Softmax, LayerNorm, RMSNorm) with a unified canonical architecture built from a single-hidden-layer ReLU network plus basic arithmetic. The core algorithmic contribution is a DP-based initialization pipeline that computes near-optimal PWL approximations of target functions, then analytically converts them to ReLU network parameters. The paper validates on four architectures (BERT, Swin, LLaMA, Stable Diffusion), reporting <0.1% accuracy change under 8-bit post-training quantization and projecting >60% area and >51% power savings from synthesis estimations.

## Strengths

1. **DP-based initialization yields large and consistent accuracy improvements at the operator level.**  
   Across all tested operators and hidden dimensions, HARA achieves MSEs several orders of magnitude lower than NN-LUT and RI-LUT (Table 3), and the ablation (Table 4) confirms the DP stage alone reduces error by 3–5 orders over naive training. This provides clear evidence that the principled optimization pipeline, not just the network architecture, drives the fidelity gains.

2. **Analytical PWL-to-ReLU conversion provides a clean, automated initialization procedure.**  
   Algorithm 1 gives a closed-form mapping from optimal PWL breakpoints to the weights and biases of a single-hidden-layer ReLU network, avoiding the instability of direct training. The approach is principled and reproducible.

3. **Principled handling of infinite-domain activation functions via symmetry decomposition.**  
   HARA exploits the even/odd symmetries and asymptotic decay of functions like GELU and SiLU to decompose them into a linear (ReLU) part and a finite-domain nonlinear correction (Table 1, Figure 3). This ensures the approximation generalizes beyond the training interval — a failure mode demonstrated for naive approaches.

4. **Broad evaluation across diverse architectures and tasks.**  
   Validation spans BERT (NLU), Swin (vision), LLaMA (language generation), and Stable Diffusion (text-to-image), giving reasonable confidence that the framework generalizes beyond a single domain.

## Weaknesses

### Major

- **End-to-end quantization claim rests on a confounded comparison.**  
  Table 6 compares HARA+INT8 against a FP32 baseline. To support the claim that the approximation is "fully compatible with 8-bit quantization," the proper control is the original model *also quantized to 8-bit*. Without this, the reader cannot separate the effect of operator replacement from the effect of quantization itself. If the original model degrades significantly under INT8, the HARA numbers might actually be worse than a quantized baseline, or the apparent preservation could be coincidental. This does not invalidate the core DP algorithm, but it means one of the paper's headline claims is not supported by the presented data.

- **The hardware baseline for the projected 62.3% savings is insufficiently documented.**  
  Table 5 compares HARA's URN against "BL Specialized Units" (Softmax: Log(LUT)/Div(LUT), LayerNorm: Sqrt(LUT)/Div(LUT), GELU: Polynomial Approx.(LUT)) with no references, no description of optimization level, and no sensitivity analysis. A realistic accelerator design could share arithmetic blocks (e.g., an exponent unit) between the specialized units, which would reduce the apparent fragmentation and narrow the savings gap. The estimates are presented to 4–5 significant figures (e.g., 6,890.24 µm²), creating a misleading impression of precision. The paper acknowledges these are synthesis estimates, but the absence of baseline detail is a significant gap given that the hardware savings are a central advertised result.

### Minor

- **Error propagation in the Softmax/LayerNorm decomposition is not separately analyzed.**  
  Equations (2)–(3) decompose these operators into Pow2/Log2 primitives plus arithmetic chaining. The reported operator-level MSE (Table 3) aggregates the full function, but the paper does not isolate the error contributed by the ReLU nets for Pow2/Log2 from the error introduced by the arithmetic composition. Given the extremely low claimed MSE (e.g., 10⁻¹⁴ for Softmax at HD=16), a stability analysis for typical input distributions would strengthen the evidence.

- **No confidence intervals or variance reported for end-to-end results.**  
  Table 6 reports a single value per metric. Even a confidence interval from bootstrap on the test set (or ideally multiple seeds) would help assess the reliability of the <0.1% difference claims.

- **Fine-tuning hyperparameters (Stage 3) are not specified.**  
  The paper mentions a "brief fine-tuning stage using the Adam optimizer" (Section 3.2) but gives no learning rate, number of iterations, or whether fine-tuning is per-operator or global. This affects reproducibility.

- **The ablation study (Table 4) does not compare against other initialization strategies.**  
  The "Naive" baseline is a randomly initialized ReLU network, which is a weak comparator. Results against Xavier/He initialization or knowledge distillation from the original function would better isolate the value of the DP approach. The gap is large enough that the main conclusion likely holds, but this limits the granularity of the analysis.

- **The LayerNorm decomposition (Eq. 3) omits the epsilon term** typically added for numerical stability (the small constant added to σ² before the reciprocal square root). While likely negligible, this should be clarified.

### Trivial

None.

## Nice-to-Haves

- A discussion of the parameter overhead introduced by HARA approximators (how many parameters per operator, how this compares to the model's total parameter count) would strengthen the hardware narrative.
- Comparison with alternative *unified* approximator designs (e.g., a single shared LUT with reconfigurable entries under the same area budget) would further validate the ReLU-network architecture choice.
- A brief note on the sensitivity of the DP approach to the discretization density and the number of segments N would be useful.

## Removed Points

These points were raised in the inputs but are removed for the reasons stated:

- **No comparison with other unified approximators (scope creep):** The paper's contribution is the specific HARA framework (ReLU network + DP initialization), not a claim that ReLU networks are the universally optimal approximator. The comparison against NN-LUT and RI-LUT covers the relevant function-specific baselines. Asking for comparison against piecewise-polynomial or shared-LUT alternatives is a reasonable extension but not a required baseline. *(Removed: scope creep beyond the paper's stated contribution.)*

- **"HD" meaning ambiguous:** The paper explicitly says "hidden dimension" (Section 4.2.1). For a single-hidden-layer ReLU network, HD clearly refers to the number of hidden neurons/segments. *(Removed: the paper is clear on this.)*

- **Hardware numbers too precise (form/style nitpick):** Reporting synthesis results to sub-µm² precision is normal practice in the EDA community. *(Removed: standard reporting format, not a weakness.)*

- **"Naive" baseline not specified:** Section 4.2.2 states it is "a Naive direct training approach." While additional initialization baselines would be informative (noted under Minor), the Naive baseline is adequately described for an ablation. *(Downgraded to Minor as a more granular comparison would strengthen the study.)*

- **"HARA (8,8,8)" unexplained:** The paper states "using an efficient configuration (hidden dimension 8)" — (8,8,8) is clearly the HD for three operator groups. *(Removed: sufficiently explained.)*

- **b₂ handling not mentioned / second-layer bias:** The algorithm returns first-layer weights n, second-layer weights m, and first-layer biases B. The second-layer bias b₂ is handled in the full derivation referenced to Appendix A.1 (stripped by parser). This is a detail deferred to the appendix, not a missing element. *(Removed: appendix contains the derivation.)*

- **gGELU notation unclear:** The paper defines g(x) as "the approximation function that closely matches the original function for x < 0." The notation is consistent. *(Removed: the paper adequately explains it.)*

- **Related work doesn't explain why LUT methods can't be unified:** The paper positions NN-LUT and RI-LUT as function-specific methods — this is stated. The claim is not that they *cannot* be unified, but that existing work does not pursue unification. *(Removed: the paper's characterization is accurate.)*

## Novel Insights

None beyond the paper's own contributions. The harsh reviewer and strength finder largely agree on the paper's content; no novel synthesis emerged from the meta-review beyond what the paper itself states.

## Suggestions

1. **Add the quantized baseline.** Report the original model quantized to INT8 (using standard post-training quantization) alongside HARA+INT8 in Table 6. This directly isolates the effect of operator replacement from quantization and would make the "fully compatible with 8-bit quantization" claim supportable.

2. **Document the hardware baseline in detail.** Describe the RTL design, optimization flags, cell library version, and synthesis tool for each baseline unit. Include a sensitivity analysis showing how the savings change if the baseline uses shared arithmetic blocks (e.g., a common exponent unit). This is necessary to make the 62.3% claim credible.

3. **Report error bars or confidence intervals** for the end-to-end results, at minimum via bootstrap on the test set.

4. **Provide hyperparameter details** for the fine-tuning stage (learning rate, schedule, iterations) in the main paper or a clearly referenced appendix section.

## Score and Decision

**Score:** 5.0  
**Decision:** Reject

### Calibration Anchors

| Anchor Path | Avg Score | Round / Source | Comparison to this paper |
|---|---|---|---|
| q541p2YLt2 | 2.50 | R1-topic-low | Lower quality; paper had fundamental flaws in attention stability analysis |
| 5dDYhvt6dY | 3.00 | R1-topic-low | Very limited (single translation task, 10 epochs), much weaker than HARA |
| E4Fk3YuG56 | 8.50 | R1-topic-high | Strong, top-venue work on memory-efficient loss computation; substantially more rigorous |
| wYVP4g8Low | 3.00 | R1-topic-low | Marginal proposal about per-node activation functions; no hardware analysis |
| AEvu2ifH1r (PTNQ) | 3.67 | R1-topic-mid | Similar domain (post-training quantization); also had missing baseline comparisons. HARA has stronger algorithmic contribution but similar evaluation gaps |
| osoWxY8q2E (ReLU Strikes Back) | 7.33 | R1-topic-mid | Very strong empirical work on ReLU in LLMs; thorough evaluation. HARA is weaker in evaluation rigor |
| LlE61BEYpB (FLARE) | 4.00 | R1-topic-mid | Similar domain (hardware-efficient transformer ops); also had evaluation limitations. HARA has stronger algorithmic novelty (DP initialization vs. combining existing ideas) |
| wWhZ2RFAxF (PowerSoftmax) | 3.75 | R1-topic-mid | HE-friendly attention; narrower scope. HARA has broader architecture coverage |
| d8w0pmvXbZ | 8.00 | R1-topic-high | Strong theoretical+empirical work on training instabilities; much more rigorous |
| STUGfUz8ob | 7.60 | R1-topic-high | Strong theoretical work on transformer reasoning |
| wg1PCg3CUP | 8.00 | R1-topic-high | Precision-aware scaling laws; thorough and rigorous |
| S4wo3MnlTr | 4.25 | R1-weakness, R2 | ReLU network initialization paper, rejected; only synthetic experiments. HARA has broader real-model validation |
| Mhu9iNGKqP | 4.50 | R1-weakness, R2 | Dynamic programming for polynomial approximation in HE; narrower application |
| vVCHWVBsLH | 7.25 | R1-weakness | Theoretical CPWL decomposition; different type of contribution |
| zA0oW4Q4ly | 6.00 | R1-weakness, R2 | ReLU network linear regions; strong theory but mixed reviews (3,8,8,5) |
| F9JZiGradI (MLP-KAN) | 5.25 | R2 | Unified representation+function learning; rejected with mixed scores. Comparable in quality to HARA — both have genuine contributions but evaluation gaps |
| gbrHZq07mq | 5.60 | R2 | Accepted but with mixed scores (6,3,3,8,8). HARA's evaluation gaps are more significant |

**Round 1 Bracket:** The paper sits between the mid-band (3.5–7.5) anchors, closer to the lower end. The topic-anchored mid-band produced FLARE (4.00) and PTNQ (3.67) — both rejected with evaluation weaknesses similar to HARA's. The weakness-anchored queries confirmed that papers with missing baselines or poorly-documented hardware analyses consistently score below 5.0.

**Round 2 Narrowing:** The 4.5–6.0 bracket produced anchors including MLP-KAN (5.25, rejected) and other papers in the 5-range. HARA is comparable to these: it has a stronger operator-level validation than MLP-KAN, but MLP-KAN's evaluation covers more ground. The narrowing confirms 5.0 as the appropriate score — the paper's algorithmic contribution is genuine, but the evaluation gaps (especially the missing quantized baseline) prevent it from being a clear accept at a top venue.

**What the low-band anchors failed at:** Poor experimental design, missing baselines, insufficient evaluation breadth, or marginal contributions. HARA shares with these the problem of a confounded comparison (quantized baseline) and insufficiently documented hardware claims. It distinguishes itself through a genuinely novel algorithmic contribution (DP initialization) and strong operator-level validation, which pushes it into the mid-range rather than the low range.