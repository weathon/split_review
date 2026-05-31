## Summary
The paper performs an empirical comparison of three neural network architectures — a plain MLP, a "U-Net-style residual network," and a "DeepONet-inspired model" — for surrogate modeling of a thermal explosion ODE system (H₂-O₂-air, 11 species). Using 70,000 samples generated from a stiff ODE solver, the authors train all three networks on identical 13-dimensional input/output vectors and report that their U-Net variant achieves an MSE ~14× lower than both competitors, concluding that architecture selection is crucial for combustion surrogate modeling.

---

## Strengths
- **Practically motivated problem**: Accelerating stiff chemical ODE integration via neural surrogates is a legitimate and active research challenge, and the paper targets a concrete combustion system with realistic initial-condition ranges (T ∈ [250, 5000] K, p ∈ [10⁴, 2×10⁷] Pa).
- **Multi-step training loss**: The use of a recursively-unrolled multi-step prediction loss (Eq. 4) to penalize error accumulation is a sensible design choice that encourages temporal stability, and it is applied uniformly across all architectures, ensuring fair training objectives.

---

## Weaknesses

### Fatal
- **The DeepONet is fundamentally misapplied.** The canonical DeepONet maps an *input function* (evaluated at sensor points) to an *output function*; its branch network encodes a function, and its trunk network evaluates that function at a query coordinate. Here, the task is a point-to-point regression: given a 13-dimensional state vector and a scalar Δt, predict the next state. The 12 chemical species playing the role of "branch input" are not a sampled function, and Δt as the sole "trunk input" does not represent a spatial or temporal query location. The "DeepONet-style" model described is structurally a multiplicative gating network. Calling it DeepONet inflates the scope of the comparison and attributes performance differences to operator-learning paradigms when the architecture is simply ill-suited to the task by design.

### Major
- **No parameter-count or FLOP-controlled comparison.** The three networks have different layer widths, depths, and skip-connection counts; the paper does not report total trainable parameters for any model. Without this, the conclusion "architecture matters" is confounded with "parameter count matters." A deeper plain MLP with the same parameter budget as the U-Net could be informative.
- **The "U-Net" is not a U-Net.** A U-Net has an encoder that progressively downsamples spatial resolution and a decoder that upsamples it, with skip connections bridging corresponding resolution levels. The architecture described (13→100→120→120→100→13, plus a global input skip) is a residual MLP — there is no downsampling, no upsampling, and no multi-resolution feature hierarchy. Labeling it "U-Net" is architecturally misleading and overstates the contribution.
- **Inference time is not reported.** The entire motivation for replacing a stiff ODE solver with a neural network is computational speed. The paper never measures inference latency or speedup over the solver, rendering the practical case for the approach unsubstantiated.
- **Single-problem, single-seed evaluation.** All conclusions rest on one combustion mechanism, one equivalence-ratio/dilution assumption, and apparently one training run (no ensemble or multiple seeds reported). Performance rankings among modestly-differing architectures can be unstable across random seeds, especially when MSE standard deviations (0.02–0.07) are an order of magnitude larger than the mean MSE differences being ranked.
- **No physical constraint verification.** The paper does not evaluate whether predictions satisfy physical constraints such as mass conservation, species-concentration positivity, or thermodynamic consistency. These are necessary checks for any combustion surrogate; large MSE spread in Table 1 suggests some predictions may be physically inadmissible.

### Minor
- **Weighting in the multi-step loss is unexplained.** Equation 4 weights step k by 1/k, penalizing short-horizon errors more heavily than later steps. This is unconventional; the opposite weighting (larger penalty for accumulated later errors) is more standard. No ablation or justification is given.
- **70,000 total samples is modest, not "large."** For a smooth 13-dimensional ODE system sampled i.i.d. in a box, this sampling density is sparse. The self-described "fairly large dataset" claim is not calibrated against prior work.
- **Self-contradictory conclusion.** The abstract explicitly states "Despite testing various architectures and using a fairly large dataset, the problem remains unresolved," yet the conclusions section claims the U-Net provides "stable and physically meaningful approximations." These statements are not reconciled.

### Trivial
- Figure captions repeat the alt-text block verbatim, creating duplication in the text.

---

## Nice-to-Haves
- An ablation isolating the contribution of the local skip connection versus the global input skip (residual) would clarify which structural element drives the gain.
- Including a recurrent baseline (GRU or LSTM) would be natural given the time-series nature of the task.
- A parity plot or distribution of relative errors per species (especially for minor radicals like OH and H where concentrations vary by orders of magnitude) would better reveal model behavior than aggregate MSE.

---

## Novel Insights
None beyond the paper's own contributions. The observation that residual/skip connections improve surrogate accuracy for stiff ODE systems has been established previously in the chemical kinetics ML literature (e.g., KiNet-style networks). The paper does not provide theoretical grounding for why this architecture class should be preferred, nor does it generalize across mechanisms or fuels.

---

## Suggestions
- Replace the "DeepONet-inspired" baseline with a proper operator-learning setup (e.g., feeding a short state trajectory as branch input and querying future times as trunk input) or relabel it as a "gated/multiplicative MLP" to avoid misleading comparisons.
- Report model size (parameters), training wall-clock time, and inference throughput (states/second) against the reference ODE solver for all three architectures.
- Extend the evaluation to at least one additional kinetic mechanism or fuel to assess whether the U-Net advantage is task-specific.

---

## Score and Decision

The paper's core experimental comparison is built on an improperly adapted DeepONet baseline and an "architecture" label ("U-Net") that does not match the described network. The absence of parameter-controlled comparisons, inference speed measurements, and physical constraint checks leaves the central claims inadequately supported. The scope is narrow (one dataset, one problem, no generalization), and the contribution — residual connections help for this ODE — is incremental relative to existing literature. These are not minor presentation issues; they concern the validity of the comparison itself.

MY FINAL SCORE: <score>2</score>
MY FINAL DECISION: <decision>Reject</decision>