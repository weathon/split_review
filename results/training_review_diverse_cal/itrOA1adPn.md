Here is my consolidated review:

---

## Summary

This paper introduces a deep RL framework for studying visual ecology, where agents navigate a 3D environment (ViZDoom) and must forage for food to survive, with reward = current satiety. The authors systematically evaluate five "brain" architectures (linear, feedforward, feedforward+input satiety, recurrent, recurrent+input satiety) across four tasks of increasing visual complexity (apples, Gabors, MNIST, CIFAR-10). The main findings are: (1) vision model complexity scales with task difficulty in the survival context, (2) recurrence is critical for exploiting complex vision models on the hardest task (CIFAR-10), and (3) different architectures learn distinct representations and behavioral strategies (e.g., input satiety agents avoid overeating). The paper contributes a reproducible benchmark and demonstrates how representations and behavior emerge from a simple survival objective.

## Strengths

- **Systematic scaling analysis across vision model complexity and task difficulty**: The paper varies vision model parameters (n_BC, n_LGN) and shows that on CIFAR-10—the most visually demanding task—recurrent (RNN) agents exhibit a clear positive correlation between vision model complexity and lifespan (Figure 2d–e), while feedforward agents plateau near baseline regardless of vision model size. This directly supports the claim that required visual complexity is task-dependent.

- **Recurrence demonstrated as critical for exploiting complex vision models in an RL context**: On CIFAR-10, RNN and RNN-IS agents achieve lifespans of ~800–1000 frames while all feedforward architectures (linear, FF, FF-IS) remain near the 200-frame baseline (Figure 2c). The discrimination analysis (Figure 3d) further isolates the mechanism: only RNN agents maintain above-chance nourishment pickup frequencies on CIFAR-10, while FF agents perform near chance. This shows the gap is not solely about smarter behavior but about object recognition.

- **Multi-faceted analysis linking architecture to representations to behavior**: The paper uses integrated gradients (Figure 1b), value function regression (Figure 4), and behavioral analysis (Figure 5) to connect architectural choices to internal representations and ultimately to distinct foraging strategies. Notably, input-satiety agents waste 2–3× less food than non-IS agents (Figure 5b) and adopt distinct velocity policies (Figure 5a), demonstrating that representation differences translate to quantifiable behavioral consequences.

- **Comprehensive benchmarks with strong experimental design**: The paper evaluates five architectures across four tasks with three replicates each, consistent training conditions (8×10^9 frames, PPO), and a significant compute investment (~2 months on 18 A100 GPUs). This provides a structured benchmark suite that future work can build on.

## Weaknesses

### Fatal
None.

### Major

- **Capacity confound in the FF–RNN comparison (Sections 3.1–3.2, Figure 2c–f)**: The default feedforward model uses n_FC=32 while the default recurrent model uses n_FC=128 (line 84). This means the central claim—that "a recurrent network architecture is necessary" to exploit complex vision models on CIFAR-10—is tested with a confound between architecture and capacity. The paper argues that FF lifespan is insensitive to n_FC (Figure 2f), but the evidence is weakened by a floor effect: on CIFAR-10, FF agents barely survive (~200 frames, the no-action baseline) regardless of n_FC, so any capacity-driven improvement might be invisible on the scale used. The claim of insensitivity would be stronger if the paper explicitly showed that an FF agent with n_FC=128 (matched to the RNN's default capacity) still cannot exceed a few hundred frames on CIFAR-10, or if the discrimination analysis (Figure 3d) were repeated with capacity-matched models. As it stands, the strongest claim is somewhat overreaching for the evidence provided. *Note: This does not invalidate the paper—the discrimination analysis provides converging evidence—but the "necessity" language should be softened to "RNNs provide a large qualitative improvement" unless the confound is resolved.*

- **Value function regression uses future information as a regressor (Section 3.3, Figure 4)**: Regressing the agent's estimated value V̂ on "food countdown" (time until next food pickup) uses information that is not causally available to the agent at the time of estimation—it is a retrospective label. The paper interprets the results as though V̂ tracks food countdown, but the correlation could equally arise from a third variable (e.g., proximity to food correlating with both V̂ and future pickup times). Additionally, the "intrinsic noise" upper bound is computed with an arbitrary 20-frame smoothing window whose width directly affects the bound, and no justification is given for this choice. The analysis is suggestive but not rigorous enough to support the stronger interpretive claims about what the agent "represents." The paper should either reframe the analysis as purely correlational/descriptive, or use only causally available features as regressors.

### Minor

- **The CIFAR-10 convergence issue:** The learning curves (Figure 2b) show that CIFAR-10 has not converged at 8×10^9 frames. The paper mentions a 20% improvement from fivefold training (4×10^10 frames) but does not show these results (line 97). Since the relative performance differences between architectures (FF vs RNN) are large (~200 vs ~800–1000 frames), the convergence gap is unlikely to change the main conclusions, but presenting the extended training data would strengthen confidence in the reported comparisons.

- **Food countdown regression interpretation could be clearer:** The paper concludes that RNN value functions are "driven by additional task-relevant latent variables" because satiety and food countdown leave more variance unexplained for RNNs than for FF-IS agents. However, since the food countdown regressor uses future (non-causal) information, the residual analysis conflates genuine latent variables with the noise from using a mismatched regressor. A cleaner approach would be to decode task-relevant variables directly from the GRU hidden state (as the paper itself suggests in the discussion, line 154).

### Trivial

- The "survival" framing in the abstract and introduction slightly oversells ecological realism for what is essentially a foraging task with a decaying satiety signal. The paper acknowledges this in the discussion (line 152–158), but the framing could be aligned more precisely up front.

- The vision model is described using biological terminology (photoreceptor, bipolar, RGC, LGN, V1) but no biological validation (tuning curves, etc.) is provided. The paper should either explicitly state that this is a loose architectural analogy (not a model of a specific animal) or provide such validation.

## Nice-to-Haves

- A direct analysis of the GRU hidden state (e.g., dimensionality reduction, decoding of task-relevant variables) would substantially strengthen the claim that RNNs "capture features of the environment beyond the immediate presence of food" (line 130), complementing the value function analysis.
- Reporting the effective visual resolution at which CIFAR-10/MNIST images are rendered in the viewport would help readers calibrate expectations about what the vision model must process.
- The n_FC sensitivity results (Figure 2f) would benefit from being broken out per-task to more clearly show the floor effect on CIFAR-10.

## Removed Points

- **Criticism about reward = satiety being an unusual design:** The reviewer questioned the reward design, suggesting that a stationary agent collects reward. However, this is a standard and well-motivated design for a foraging/survival task—the agent must act to maintain satiety or it dies. The paper explicitly provides the no-action baseline (200 frames), showing the design is understood and accounted for. **Removed: not a valid weakness.**
- **Criticism about missing biological validation:** The reviewer noted the biological language creates unfulfilled expectations. The paper frames the vision model as "modeled after" (not validated against) the visual system. This is a presentation choice, not a flaw. **Moved to Trivial.**
- **Criticism that "the paper should also cover Y / domain Z / additional tasks":** The reviewer suggests controlling for number of object classes and image resolution effects more extensively. These are scope-creep demands for what would be a different paper. **Removed.**
- **Criticism about learning curves not having converged / 20% improvement not being shown:** The paper explicitly acknowledges the convergence issue and reports the 20% improvement from fivefold training (line 97). The results are described but not shown—this is a presentation choice in an already long paper. The main conclusions are robust to this because the architectural differences are large. **Moved to Minor.**
- **Strength Finder strengths about biologically grounded vision model and integrated gradients:** These are retained as genuine but belong in the supporting category. The integrated gradients analysis is indeed a nice methodological touch.

## Novel Insights

The most interesting observation emerging from the reviews is the unresolved tension between capacity-driven explanations versus architecture-driven explanations in the FF vs RNN comparison. The paper's evidence for the "necessity of recurrence" is confounded by a 4× parameter count difference in the FC/latent layers. However, the discrimination analysis provides an independent line of evidence that RNNs excel at object recognition on CIFAR-10 while FFs fail, suggesting that even if the capacity confound were resolved, the architecture matters. This tension—capacity vs. architecture—is itself an interesting question for future work that the paper does not fully engage with. A controlled experiment (matching capacity while varying architecture, and vice versa) would cleanly separate these factors and could reveal whether the RNN advantage is about parameter efficiency, temporal integration, or both.

## Suggestions

1. **Resolve the capacity confound on CIFAR-10**: Run FF agents with n_FC=128 (matched to the RNN default) and compare lifespan directly. If FF still cannot exceed ~300 frames, the necessity claim is substantially strengthened. If FF reaches 400–500 frames, soften the claim to "RNNs provide a large improvement" rather than "necessity."

2. **Reframe or redesign the food countdown regression**: Either (a) clarify that this is a purely correlational/descriptive analysis showing environmental statistics that correlate with V̂, not evidence about the agent's internal model, or (b) replace the future-information regressor with causally available features (e.g., recent movement history, distance to nearest visible food).

3. **Strengthen the latent state analysis**: Decode task-relevant variables directly from the GRU hidden state rather than relying on residual variance in V̂. This would directly support the claim that RNNs "capture additional task-relevant latent variables" (line 130) and is already flagged as future work (line 154)—moving some of it into the current paper would strengthen the contribution.

4. **Soften the "necessary" / "required" language** for the recurrence claim (abstract, line 21, line 117) unless the capacity confound is resolved. The evidence supports a strong advantage, not strict necessity.

## Score and Decision

The paper makes a genuine contribution: it provides a well-motivated framework, a systematic multi-task benchmark, and converging behavioral/representational analyses that connect architectural choices to emergent strategies. The main empirical results (vision model complexity scales with task difficulty; RNNs dramatically outperform FFs on CIFAR-10; input satiety reduces food waste) are well-supported. The primary weakness is a capacity confound that tempers—but does not invalidate—the paper's strongest interpretive claim about the necessity of recurrence. The value function analysis is creative but methodologically imperfect. These issues are addressable and do not undermine the paper's core contributions.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>