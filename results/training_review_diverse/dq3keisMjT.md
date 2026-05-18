Now I have all the information I need. Let me produce the final consolidated review.

---

## Summary

This paper adapts statistical-physics methods for automated phase-transition detection to study LLM output distributions. The core idea is to measure changes in the output distribution via $f$-divergences (total variation distance, Jensen-Shannon divergence, and a linear dissimilarity) as a function of a control parameter — without requiring human-designed order parameters or access to model internals. The method is demonstrated on three fundamentally different scenarios: (1) an integer in the prompt, (2) the temperature hyperparameter, and (3) training epoch. The strongest findings are the detection of a tokenizer boundary at T≈2021 in Pythia models (a genuinely unexpected transition) and the mapping of three distinct temperature phases.

## Strengths

- **Versatility across diverse control parameters**: The method successfully detects distributional changes when varying three fundamentally different parameter types — prompt content (Sec. 3.1), temperature (Sec. 3.2), and training epoch (Sec. 3.3) — across multiple model families (Pythia, Mistral, Llama). This breadth convincingly demonstrates the method's generality.

- **Discovery of previously unrecognized transitions**: The method uncovers a sharp change in Pythia models' output distribution around integer 2021 and traces it to a tokenizer encoding change (Sec. 3.1, Fig. 2b). This is precisely the kind of discovery that justifies the approach — a transition not obvious from standard metrics and not anticipated by the authors.

- **Theoretical grounding and connection to Fisher information**: The approach is built on $f$-divergences and the linear dissimilarity measure $g(x)=2x-1$, which is bounded, has favorable convergence properties, and reduces to the Fisher information in the limit of closely spaced parameter values (Sec. 2.2). This provides a principled statistical foundation drawn from the physics literature on learning-by-confusion.

- **Black-box applicability**: The method requires only next-token probabilities, not weights or hidden activations, enabling interpretability studies of models where internals are inaccessible (demonstrated across Pythia, Mistral, Llama; Sec. 2.3, Sec. 3).

- **Robustness tuning via segment length $L$**: The paper explains how $L$ controls the scale of analysis — small $L$ approaches the Fisher information limit and highlights local changes, while larger $L$ averages out outliers (Sec. 3.3, Fig. 4). This flexibility is a genuine practical advantage.

## Weaknesses

### Fatal

None.

### Major

- **The heat capacity analysis is thermodynamically unsound and should not be used as validation.** The paper defines "energy" as $E(\bm{x}) = -\log P(\bm{x}|T=1)$ and computes a "heat capacity" $C(T) = d\langle E\rangle/dT$, then states that "the locations of peaks (i.e., dips) in these quantities are close to the critical points highlighted by our method" (line 167), implicitly using this as corroborating evidence. However, in the LLM setting, the actual sampling distribution at temperature $T$ is not a Boltzmann distribution over full sequences with energy $E(\bm{x}) = -\log P(\bm{x}|T=1)$. Rather, each token is drawn from $P(\text{token}_i|\text{context}, T) \propto \exp(z_i/T)$ where $z_i$ are logits. The paper's "energy" differs from the true negative logits by sequence-dependent normalization constants $\log Z$ that propagate through the derivative in uncontrolled ways. The paper acknowledges this mismatch in passing ("the text outputs are not truly sampled from a Boltzmann distribution," line 167), but this does not salvage the analysis — an acknowledged mismatch does not make the quantity meaningful. Moreover, the negative "heat capacity" is listed as a specific finding (line 31: "an LLM's 'heat capacity' with respect to the temperature can be negative"). The dissimilarity peaks in Fig. 2 stand on their own as evidence of distributional change; the heat capacity analysis neither supports nor refutes them and should be removed or replaced with a properly motivated comparison (e.g., showing generated text examples or n-gram statistics at each phase). This issue undermines the temperature section's secondary analysis but does **not** invalidate the core dissimilarity method, which is independent of the thermodynamic analogy.

### Minor

- **The method's "automated" nature is overstated.** The dissimilarity measure depends on human choices — the prompt, segment length $L$, grid resolution — and detected transitions are prompt-conditional rather than model-level (as the paper itself notes: "different prompts result in different transition times" at line 33). For the temperature scan, a single prompt is used; for the epoch scan, 20+7 prompts. The paper does not provide systematic guidelines for how to select these hyperparameters when ground truth is unknown, or how to aggregate across prompts to produce a model-level characterization. The abstract's claim of "objectively and automatically mapping out phase diagrams of generative models" implies a more global characterization than is demonstrated. A discussion of prompt aggregation strategies or heuristics for hyperparameter selection would strengthen the contribution.

- **The integer ordering example, while a useful sanity check, is a correctness boundary rather than an illuminating "phase transition."** The paper adopts a deliberately broad definition of phase transition (footnote, line 16), but the integer-ordering test (Sec. 3.1) essentially detects that the model knows "43 > 42" but not "41 > 42" — any reasonable accuracy metric would find the same discontinuity. The paper would benefit from a clearer discussion distinguishing trivial boundaries from transitions that reveal non-obvious structure (like the tokenizer change), and from acknowledging that the method's value lies in the latter.

- **No controlled ground-truth calibration experiment.** The paper does not evaluate its method against a synthetic benchmark with known, designed distributional shifts. The integer-ordering case provides one natural ground truth (correct answer flips at T=42), and the tokenizer transition is verified post-hoc, but a synthetic test (e.g., mixing two data distributions in known proportions) would calibrate whether the dissimilarity peaks reliably indicate genuine distributional changes versus noise. This would substantially strengthen the empirical case.

- **The epoch analysis does not quantify statistical significance of alignment.** The paper claims coincidence between weight-structure and output-distribution peaks around epoch 80K (Fig. 4a), but both curves have many peaks, and some alignment is expected by chance. A permutation test or similar null-model comparison would strengthen this claim.

### Trivial

- The computational cost of the approach (total forward passes per experiment) is not reported, making it hard for readers to assess practical feasibility.

## Nice-to-Haves

- A systematic investigation of how temperature transition points vary across a diverse set of prompts would turn a current limitation into a deeper result about how control parameters interact with prompt context.
- A synthetic benchmark with known transitions (e.g., a mixture model where the mixing weight is the control parameter) would calibrate the method.

## Removed Points

These points were raised by reviewers but are removed or downgraded per the filtering rules:

1. **"The heat capacity analysis undermines the entire temperature analysis"** — Retained but downgraded from Fatal to Major. The heat capacity analysis is problematic, but the dissimilarity peaks (the core method's output) stand independently and are not invalidated by the thermodynamic analogy's flaws. The heat-capacity-as-validation claim is undermined, but the temperature scan's main finding (three behavioral phases detected via dissimilarity) remains intact.

2. **"The paper does not adequately justify why this broad usage [of 'phase transition'] is informative"** — Kept in spirit but downgraded from Major to Minor. The paper explicitly defines its scope (footnote, line 16) and the integer-ordering example is presented as an introduction (line 118: "As an introduction, we start with the simplest case"). The paper is transparent about its definition; the issue is more about presentation clarity than a substantive flaw.

3. **Suggestions about missing statistical significance and computational cost** — Kept as Minor/Trivial. These are valid points but not central to the paper's contribution.

4. **Strength Finder's claim about "negative heat capacity" being a strength** — Removed. The heat capacity analysis has been identified as problematic; claiming it as a strength conflicts with a verified weakness. Per the rules, the weakness wins.

5. **Criticism that the integer ordering test "adds no insight"** — Partially removed. The integer ordering example is indeed simple, but the paper presents it as an introductory demonstration. The point about distinguishing trivial from non-trivial transitions is kept in Minor.

## Novel Insights

The reviews reveal an interesting tension: the paper's most compelling result (the tokenizer transition at T≈2021 in Pythia models) is precisely the kind of "surprising" discovery that the method is advertised to enable, yet it is also the simplest to explain post-hoc. This suggests the method's strongest use case is exploratory screening — generating hypotheses about model behavior changes that can then be investigated mechanistically. The reviews collectively highlight that the paper would benefit from reframing its contribution as a screening/detection tool rather than a full "phase diagram mapper," and from replacing its problematic thermodynamic validation with more direct characterizations of what changes at each detected transition.

## Suggestions

1. **Remove or substantially revise the heat capacity analysis.** The dissimilarity peaks in the temperature scan are independently interesting and well-supported. Replace the thermodynamic validation with a direct demonstration of qualitative differences across the three phases — for example, showing representative generated text, tracking n-gram diversity, or measuring perplexity — that does not rely on the problematic "heat capacity" quantity.

2. **Acknowledge and discuss prompt dependence explicitly.** The finding that transitions are prompt-conditional is itself interesting. Frame it as a feature rather than a limitation: the method can probe which aspects of behavior change at which parameter values. Provide practical heuristics for how to set $L$ and grid resolution when ground truth is unknown.

3. **Add a controlled calibration experiment.** Test the method on a synthetic setup where the transition location is known (e.g., mixing two output distributions with a known mixing weight as the control parameter) to establish that the dissimilarity peaks reliably indicate genuine distributional changes.

4. **Clarify the distinction between trivial and non-trivial transitions.** The paper would benefit from a brief discussion of what kinds of transitions the method is most valuable for (unexpected, non-obvious ones like tokenizer changes) versus simple sanity checks (like integer ordering). This would sharpen the framing.

## Score and Decision

**Originality:** Good. Adapting learning-by-confusion / $f$-divergence methods from statistical physics to LLM output analysis is a novel and well-motivated application.

**Importance of research question:** High. Automated detection of behavioral changes in LLMs is practically important for interpretability, safety, and training monitoring.

**Claims support:** Mostly well-supported, except the heat capacity analysis which is used as a secondary validation despite being thermodynamically unsound.

**Soundness of experiments:** The core dissimilarity experiments are sound and well-constructed. The heat capacity analysis needs revision.

**Clarity of writing:** Clear, well-structured, with appropriate mathematical exposition.

**Value to the community:** Moderate-to-high. The method is simple, theoretically grounded, and demonstrated on realistic scenarios. Once the heat capacity issues are addressed, it would be a useful tool.

The paper has a genuine core contribution (the dissimilarity-based detection method) that is well-motivated, theoretically grounded, and convincingly demonstrated across three distinct scenarios. The heat capacity analysis is the only serious weakness — it is a secondary analysis that is thermodynamically problematic, but removing it would not damage the core contribution. The other issues (overstated "automated" framing, need for clearer distinctions between transition types, missing calibration experiment) are addressable in revision. I recommend acceptance conditional on addressing the heat capacity issue and the framing concerns.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>