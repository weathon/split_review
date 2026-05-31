Now let me do the calibration search to establish the score.**Round 1 Bracket: approximately 4.5–6.0.** The paper is clearly stronger than FLARE (4.0) but the non-competitive hardware baseline and absence of latency analysis put it below AERO (6.0). Now let me narrow within this bracket.Let me read the two most topically similar anchors to sharpen the comparison.I now have enough to write the full review. Let me synthesize everything.

---

## Summary

HARA introduces a unified hardware-software co-design framework for transformer inference on edge devices, replacing diverse non-linear operators (GELU, SiLU, Softmax, LayerNorm, RMSNorm) with a single reconfigurable Unified ReLU Network (URN) block. The core algorithmic contribution is a three-stage parameter initialization pipeline using dynamic programming to find optimal piecewise-linear breakpoints, which are then analytically converted to ReLU network weights and fine-tuned. The framework is validated end-to-end across BERT, Swin, LLaMA 3.2-3B, and Stable Diffusion 3.5, achieving <0.1% accuracy degradation while projecting >62% silicon area savings over a baseline using separate specialized hardware units.

---

## Strengths

- **DP initialization yields orders-of-magnitude lower approximation MSE than competing methods.** Table 3 shows HARA's GELU MSE at HD=2 is 2.36e-05 versus NN-LUT's 2.07e-03; at HD=16 it is 3.20e-08 vs. RI-LUT's 4.48e-05. The ablation in Table 4 isolates the DP stage: naive training gives MSE ≈1.38e-03, DP alone drops it to 1.34e-06, and DP+fine-tuning reaches 1.89e-07. The improvement is systematic and scales predictably with hidden dimension, unlike baseline methods that stagnate or behave erratically.

- **Comprehensive end-to-end validation across four architecturally diverse transformers with negligible accuracy degradation.** Table 6 reports BERT EM drop of only 0.018 (80.038→80.020), Swin Top-1 drop of 0.012 (81.182→81.170), LLaMA perplexity increase of only 0.005 (7.814→7.819), and essentially unchanged HPSv2 for DiT (0.2724→0.2731), all under 8-bit quantization. This is a strong empirical result spanning NLP, vision, generation, and diffusion.

- **Systematic decomposition of complex operators into two hardware-friendly primitives.** Equations (2) and (3) restructure Softmax and LayerNorm entirely around Pow2 and Log2, eliminating exp, sqrt, and div hardware. The finite-domain approximation targets ([0,1] for Pow2, [1,2] for Log2) are small and well-conditioned, and MSE values in Table 4 reach 2.88e-13 and 5.74e-08 for these primitives. This is a clean, principled decomposition.

- **Exploitation of symmetry and asymptotic structure for activation functions.** Table 1 characterizes each activation by its symmetry and boundary behavior, enabling GELU and SiLU to be transformed into even, decaying functions on a finite domain. Figure 3 demonstrates that this approach correctly extrapolates (GELU(x) ≈ -3.99e-14 at x=8, HARA ≈ 1) while a naive ReLU net diverges to -0.8213, a concrete demonstration of methodological superiority.

---

## Weaknesses

### Fatal

None.

### Major

- **Hardware baseline is non-competitive, making the headline 62.3% area reduction an unreliable quantitative claim.** Table 5 compares HARA's single URN against three *fully independent and unshared* specialized LUT units: a Log/Div LUT for Softmax (6,890 µm²), a Sqrt/Div LUT for LayerNorm (6,817 µm²), and a Polynomial LUT for GELU (6,349 µm²). A hardware designer building the same system would naturally share resources—the Div unit appears in both Softmax and LayerNorm; an exponential/log LUT can serve both Softmax and GELU. The paper makes no attempt to share these primitives in the baseline. The actual area advantage of unification over a resource-sharing baseline is unknown and could be substantially smaller than 62.3%. Since the hardware efficiency claim is the paper's primary motivation (stated first in abstract and introduction), a non-competitive baseline undermines the central quantitative contribution.

- **Latency and throughput are entirely absent from the hardware analysis.** Table 5 reports area and power only. Figure 2 shows a controller, scheduling mechanism, and two parallel URN groups (G1, G2), but the paper provides no throughput, latency, or cycles-per-operator figures. A unified reconfigurable architecture by design requires time-multiplexing: when a transformer layer requires Softmax, LayerNorm, and GELU in the same forward pass, they must be serialized through the shared URN (or the URN must be replicated, recovering area costs). Area savings that come with a latency penalty are a genuine engineering trade-off central to the edge deployment use case—and the paper leaves it completely uncharacterized.

- **No model-level comparison against competing approximation methods.** Table 6 compares HARA-approximated models only against the FP32 baseline. This establishes negligible degradation relative to the original model, but does not answer whether HARA produces better end-to-end accuracy than I-BERT, NN-LUT, or integer-arithmetic softmax designs when deployed under comparable hardware budgets. The operator-level MSE advantage in Table 3 is compelling, but approximation MSE and downstream task performance are only weakly correlated when errors are already small. A head-to-head model-level comparison against at least one competing full-model approximation approach is missing.

- **Hardware results are pre-layout synthesis estimates only.** The paper acknowledges in Section 5 that "our hardware benefits are based on synthesis estimations rather than a full physical implementation and post-layout analysis." Synthesis estimates do not capture routing, interconnect overhead, controller costs (visible in Figure 2 but not in Table 5), or local buffer area. The reproducibility statement says synthesis documentation "will be provided"—its absence at submission time leaves the core hardware claim externally unverifiable. This limitation is self-acknowledged but still substantive given that hardware efficiency is the primary contribution.

### Minor

- **Ablation study (Table 4) tests DP only against the weakest possible baseline.** The "Naive" baseline is random initialization with unconstrained gradient descent. Systematic alternatives—uniform-spacing PWL with segment-wise least squares, Chebyshev polynomial fitting converted to ReLU form—would more rigorously establish DP as the correct choice. The phenomenon that DP finds globally better breakpoints than random initialization is real and important, but the magnitude of DP's advantage over *all* systematic methods is not established.

- **The binary constraint on second-layer weights (m_j = sign(n_j) ∈ {-1, +1}) is never ablated.** Algorithm 1 line 13 hard-constrains the output-layer weights to ±1 for hardware reasons (eliminating multipliers). This constraint is maintained through fine-tuning. The approximation cost of this restriction relative to unconstrained real-valued second-layer weights is never measured. It is both an uncharacterized hardware-accuracy trade-off and a missing ablation.

- **No model-level accuracy sweep over hidden dimension.** The paper uses a single HARA(8,8,8) configuration for Table 6 and shows operator-level MSE vs. HD (HD∈{2,4,8,16}) in Table 3, but does not link these to model-level accuracy. Whether HD=4 (smaller hardware footprint) would cause negligible model degradation for BERT or Swin is left uncharacterized—an important question for deployment where the hardware configuration and model accuracy jointly determine the design point.

### Trivial

None.

---

## Nice-to-Haves

- Design a resource-sharing baseline for Table 5 (shared Div unit between Softmax and LayerNorm; shared exponential block between Softmax and GELU) and show HARA area savings relative to this fairer comparator. Even if the savings are smaller, demonstrating they exist against a thoughtful baseline would substantially strengthen the hardware claim.
- Add a simplified cycles-per-layer or latency estimate using the controller scheduling logic already shown in Figure 2, comparing pipelined specialized units against the time-multiplexed URN. Even a conservative analytical estimate would anchor the area savings in a performance context.
- An end-to-end comparison against one competing full-model approximation method (NN-LUT or I-BERT) on at least one of the four architectures would validate that HARA's MSE advantage in Table 3 translates to practical model benefits.

---

## Removed Points

*These points are flagged to be removed, treat them with caution.*

- **Equation 3 LayerNorm denominator uses Σxⱼ² not Σx̄ⱼ²**: The harsh critic claims the formula as written is only correct when μ=0. The paper defines x̄ = Mx − Σxⱼ in line 150, and the denominator in Eq. 3 appears to use xⱼ without the bar. However, given (a) the parser strips formatting including overbars from variable names, (b) the end-to-end experiments work correctly across all tested models, and (c) the mathematical derivation is in Appendix A.2 which was stripped by the parser, this is almost certainly a parser artifact. Per hard rules, formatting/symbol-stripping artifacts are removed.

- **Figure 3 "overstates" naive method failure**: The harsh critic argues that clamping or extending the training domain could fix the naive method's extrapolation problem. This is speculative about what a "naive" method could do with modifications; the comparison shown is valid between HARA and unconstrained naive training. REMOVED as speculative.

- **DP for optimal PWL fitting is a classical tool**: The critic implies lack of novelty in using DP for piecewise linear fitting. Without external sources to confirm the originality claim, this is removed per hard rules against missing related works claims.

- **LUT address-bit-width not stated (baseline comparison)**: A minor implementation detail. Removed per rules on reproducibility nitpicks about trivial implementation details.

- **Strength about hardware savings being the "direct result of co-design"**: Weakened (hardware baseline is non-competitive), so this strength is moved here—the projected savings are real but inflated by an uncharacteristic baseline.

---

## Novel Insights

The most genuinely novel observation across these reviews is that the DP-based breakpoint optimization provides a *global* optimum for piecewise linear approximation rather than a local one, and this can be analytically converted (not just initialized) into ReLU network weights via closed-form expressions. This decouples the approximation quality problem from the gradient-based training problem entirely. The symmetric decomposition strategy in Table 1—which transforms infinite-domain activation functions into finite-domain even functions—is also a clean insight with hardware consequences: it means the same URN block parameterized over [0, D] can serve all covered activations, rather than requiring separate per-function domain handling.

---

## Suggestions

1. Rebuild the hardware baseline in Table 5 with resource sharing (one Div unit shared across Softmax and LayerNorm, one Log/Exp unit for both Softmax and GELU). Report the area of this shared baseline alongside HARA's URN. This single change would make the hardware contribution defensible.
2. Use the controller logic in Figure 2 to estimate per-operator cycles for a time-multiplexed URN vs. parallel specialized units, and report latency per transformer layer for a representative model. This is feasible without a full chip layout.
3. Replace all non-linear operators in one model (e.g., BERT) with NN-LUT and report its SQuAD EM/F1 in Table 6 as a competing approximation baseline. The operator-level MSE advantage (Table 3) needs a model-level validation to be fully convincing.
4. Add an HD sensitivity analysis at the model level: report BERT EM and Swin Top-1 accuracy for HD ∈ {2, 4, 8, 16} to help practitioners choose the hardware configuration with the best accuracy/area trade-off.

---

## Score and Decision

**Calibration anchors retrieved:**

| Paper | Path | Avg Human Score | Round | Comparison |
|-------|------|----------------|-------|------------|
| Optimizing Attention | vnp2LtLlQg.md | 3.00 | R1 | Much weaker—single-architecture, no principled method |
| On-Device Transfer Learning | eqKHuxIpp5.md | 2.50 | R1 | Much weaker—narrow scope |
| FiRST (router transformers) | ulGwcj1egv.md | 3.00 | R1 | Different problem, less methodological depth |
| PTNQ (post-training non-linear quant) | AEvu2ifH1r.md | 3.67 | R1 | Less comprehensive, fewer architectures |
| Edge AI inference (QAT) | NLfWQfy5zp.md | 3.75 | R1 | Less principled algorithm, weaker contribution |
| FLARE (ReLU-enhanced attention) | LlE61BEYpB.md | 4.00 | R1 | Weaker—only GPT-2, less principled, poor presentation |
| AERO (Softmax-only PI) | CPBdBmnkA5.md | 6.00 | R1 | Similar topic; compares vs SOTA at model level, has latency numbers—slightly stronger hardware evidence |
| ReLU Approximation Manifold | S4wo3MnlTr.md | 4.25 | R2 | Related algorithm but only synthetic experiments; weaker empirical grounding |
| Super Floating-Point (SuFP) | tth2qXY7RU.md | 4.67 | R2 | Hardware co-design for quantization, similar quality tier |
| I-LLM (integer-only quantization) | 44pbCtAdLx.md | 5.00 | R2 | Most directly comparable—addresses non-linear ops in LLMs, multi-model eval, comparable novelty level |
| Pyramid VQ for LLMs | ZBlfjXubgG.md | 5.00 | R2 | Different method, similar quality |
| NeuralFuse | Qvoe4wXWFi.md | 5.75 | R2 | Hardware-aware edge DNN, synthesis estimates, slightly stronger baseline |
| BNN+SNN | lGUyAuuTYZ.md | 5.67 | R2 | Hardware efficiency, multiple comparisons vs baselines |
| CoreInfer (sparse activation) | s3003xWtfd.md | 6.25 | R2 | Broader eval, compared against SOTA |
| Intermittent DNN Training | SFNqrHQTEP.md | 6.00 | R2 | Edge deployment, but different focus |

**Round 1 bracket: 4.5–6.0**

**Round 2 narrowing:**

The two closest anchors are I-LLM (5.0) and AERO (6.0). HARA is:

- *Better than I-LLM (5.0)* in: algorithmic originality (DP initialization is a principled, novel contribution, not extension of known techniques), breadth of evaluation (4 architectures spanning NLP/vision/generation/diffusion vs. LLM-only), and cleaner unified design principle.
- *Weaker than AERO (6.0)* in: AERO includes concrete latency measurements and compares against SOTA baselines at the model level; HARA's hardware evaluation lacks latency and uses a non-competitive baseline.

HARA is also clearly above S4wo3MnlTr (4.25—only synthetic experiments, no real-world validation) and SuFP (4.67—similar hardware co-design concept but less systematic). The comparison with NeuralFuse (5.75) is close: NeuralFuse has a cleaner hardware result (actual bit-flip model) but narrower algorithmic contribution. HARA's lack of a fair hardware comparison tips it below 5.75.

HARA sits between I-LLM (5.0) and AERO (6.0), closer to I-LLM given the major hardware evaluation gaps. The software contribution justifies above 5.0, but not reaching 6.0 without a fair hardware comparison. **Final score: 5.0.**

**Axis evaluation:**
- *Originality*: Moderate-to-good. DP-based parameter initialization for unified hardware approximation is novel; the decomposition of operators is systematic and original.
- *Importance of research question*: High. Efficient non-linear hardware for edge transformers is a real bottleneck.
- *Claims well-supported*: Mixed. Software claims are very well-supported; hardware claims rest on an inflated baseline.
- *Soundness of experiments*: Good for the software side; weak for the hardware side (no latency, no fair baseline).
- *Clarity of writing*: Good. The paper is organized and the methodology is clearly described.
- *Value to research community*: Moderate-to-good. The DP initialization technique and the unified decomposition are reusable contributions; the hardware numbers need to be revisited.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>