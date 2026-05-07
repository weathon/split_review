Now I have read the entire paper and reviewed the calibration anchors. Let me synthesize the final review.

## Summary

This position paper argues that layerwise linear models (e.g., linear neural networks) should be prioritized over nonlinear activations as the primary theoretical tool for understanding dynamical phenomena in deep neural networks. The "dynamical feedback principle" — that layers mutually scale each other's gradient magnitudes — is proposed as a unifying mechanism that, under different conditions (small initialization, layer imbalance, weight-to-target ratios), produces emergence, neural collapse, lazy/rich regimes, and grokking. The paper reviews existing solvable models under this principle and contributes a novel toy model (Section 7) that unifies NTK initialization and target downscaling via the weight-to-target ratio $\Sigma_0/S$ and the quantity $\gamma_+$.

## Strengths

- **Clear, contestable position**: The stance — "prioritize layerwise structure dynamics over nonlinear activations until its limits are fully explored" — is clearly stated, specific enough to be debated, and genuinely counter-orthodox to a community that has focused heavily on nonlinearities. This invites productive disagreement.

- **Novel toy model unifying lazy regime methods (Section 7)**: The derivation showing that both NTK initialization and target downscaling are captured by the weight-to-target ratio $\Sigma_0/S$ via the quantity $\gamma_+$ is a genuine theoretical contribution that clarifies and unifies two previously separate explanations. Figure 7 provides intuitive illustration, and Figure 8 offers empirical support showing that reducing $\Sigma_0/S$ eliminates grokking delays in a 4-layer tanh MLP.

- **Effective pedagogical structure**: Figure 1's Principle → Conditions → Solvable Models → Phenomena template is followed consistently through Sections 4–7, making the unifying logic transparent. Each section pairs informal intuition with formal derivation, making the argument accessible while maintaining rigor.

- **Empirical validation of predictions in nonlinear networks**: Figure 4 shows the linear model's theoretical sigmoidal growth predictions (solid lines) matching empirical dynamics of a 2-layer ReLU network (dashed lines) for time, data, and parameter emergence. This provides concrete evidence that the linear model's predictions transfer beyond the linear regime.

- **Concrete research agenda (Section 10.1)**: The proposed directions — incorporating nonlinearity as perturbation, batch normalization as whitening/scaling, skip connections inducing differential multilinearity — are specific and grounded in the paper's framework.

## Weaknesses

### Fatal

None.

### Major

- **Thin engagement with the strongest counterarguments (Section 9)**: For a position paper, the "Alternative Views" section is the natural home for productive disagreement. Section 9 concedes only two points — models aren't used in practice and some phenomena may require nonlinearity — but never addresses the most serious objections: (1) that many complex DNN phenomena (attention mechanisms, in-context learning, tokenization effects in LLMs) appear to depend on specific nonlinear computational structures that layerwise linear models fundamentally cannot represent; and (2) that the paper's selection of phenomena (emergence, NC, lazy/rich, grokking) may be biased toward exactly those that admit linear analysis, while phenomena genuinely requiring nonlinearity (adversarial vulnerability, loss landscape geometry, mode connectivity) are systematically omitted. The position's force depends on showing layerwise structure explains *important* DNN phenomena, but the paper doesn't acknowledge the scope limitation this selection bias imposes. A position paper that stakes out a strong stance must engage the strongest counterarguments; this one does not.

- **Gap between "reproduces" and "explains"**: The paper provides phenomenological similarity — linear models produce sigmoidal growth, low-rank structure, lazy/rich transitions — but the central claim requires that the *mechanism* (dynamical feedback between layers) is the operative one in DNNs. Section 4.4 briefly argues that "stage-like training effectively decouples feature learning" in neural networks, but the argument is asserted rather than demonstrated. Section 5 claims "greedy dynamics toward minimal rank likely persist even with nonlinear activations" supported only by a citation to Jacot et al. (2024) and the word "likely." The paper acknowledges this limitation (Section 9: "Some phenomena may require non-linear activations for explanation") but treats it as a minor caveat rather than the central challenge it poses to the position. A principled argument for why nonlinearities should be perturbative corrections — analogous to physics where dimensionless ratios quantify perturbation magnitude — would significantly strengthen the claim, and its absence is a meaningful gap.

### Minor

- **High review-to-argument ratio**: Sections 4–7 primarily review existing work (Saxe et al., 2014; Nam et al., 2024; Mixon et al., 2020; Domine et al., 2025; Kunin et al., 2024; Kumar et al., 2024) with brief "intuition" paragraphs connecting each to the feedback principle. The position paper framing adds organization, but the ratio of original argumentation to reviewed content is lower than typical for a strong position paper. Section 7's toy model is the most original contribution but occupies a relatively small fraction of the text.

- **The "unification" claim overstates what is shared**: The paper claims the feedback principle "unifies" four phenomena, but each requires *different additional conditions* (small equal initialization, whitened input, λ-balanced initialization, weight-to-target ratio considerations). The conditions do much of the explanatory work, and they differ substantially across phenomena. The feedback principle is necessary but not sufficient for any individual phenomenon. The paper could more honestly represent what is and isn't unified.

### Trivial

- The "dynamical feedback principle" label for the observation that $\dot{a} \propto b$ and $\dot{b} \propto a$ in compositional parameterizations, while pedagogically useful, is a well-known property of gradient descent on products — naming it as a novel "principle" slightly overstates its novelty, though this is standard practice in physics-style exposition.

## Nice-to-Haves

- Mechanistic validation via intervention experiments (e.g., disrupting layerwise feedback in a DNN and showing the predicted change in training dynamics) would significantly strengthen the "explains, not just reproduces" argument, but is not required for the position to be clear and debatable.

- A more developed discussion of the perturbation theory analogy (Section 10.1 sketches this briefly) — showing under what specific conditions nonlinear corrections should be small — would strengthen the paper's central argument.

- Cataloging phenomena where layerwise linear models *fail* (not just succeed) would sharpen the position by honestly delineating its scope.

- Developing Section 9's alternative views with the strongest counterarguments would transform this from a well-organized review into a genuinely persuasive position paper.

## Removed Points

- **Harsh critic: "physics analogy undersells the challenge because minimalist models in physics must make accurate quantitative predictions"**: The paper actually *does* show quantitative predictions matching nonlinear networks (Figure 4: solid theoretical lines matching dashed empirical curves for a 2-layer ReLU network). This criticism is partially mistaken.

- **Harsh critic: "the dynamical feedback principle is simply the observation that gradient descent on products couples the parameters"**: While true at the level of the basic formula, the paper's contribution is organizing this observation into a systematic explanatory framework across four phenomena. This is analogous to how Le Chatelier's principle in thermodynamics names a well-known mathematical tendency but provides organizational value. Removed as too dismissive for a position paper that legitimately re-frames known material.

- **Harsh critic: "paper functions more as a literature review than a position paper"**: This is partially valid but overstates the case. The paper has a clear position statement, a unifying organizational framework (Figure 1), a novel theoretical contribution (Section 7), and concrete research directions. The review content is in service of the argument. This is retained as a minor weakness about the review-to-argument ratio.

- **Strength finder: "explicit engagement with limitations" (Section 9)**: Section 9 exists but is too thin to count as a strong engagement with limitations for a position paper. Downgraded to not count as a major strength.

- **Strength finder: "the dynamics of layerwise linear models are already non-linear making the simplification principled"**: While the paper makes this point, it's a well-known observation (Saxe et al., 2014). Retained as a minor conceptual point but not as a standalone strength.

## Novel Insights

The paper's most original insight is the $\gamma_+$ quantity (Section 7) and the weight-to-target ratio framework that unifies NTK initialization and target downscaling within a single analytical framework. The structural analogy to physics — where one identifies a first-order dynamical principle and then derives different phenomena under specific boundary/initial conditions — is cleanly executed, but the paper would be more compelling if it could articulate when the analogy breaks down (i.e., when nonlinearities become first-order rather than perturbative effects). The research direction of treating nonlinearity as a perturbation to layerwise dynamics (Section 10.1) remains underdeveloped and could be the paper's most productive extension.

## Suggestions

- Substantially expand Section 9 to address the strongest counterarguments: specifically, discuss which DNN phenomena genuinely appear to require nonlinear computation and why, and articulate a principled argument for when nonlinearities should be treated as perturbative versus first-order effects.

- Add a brief section or discussion identifying at least one class of DNN phenomena where the layerwise linear approach demonstrably fails, to honestly delineate the position's scope and demonstrate intellectual honesty.

- Rebalance the paper's content: Section 7's novel contribution deserves more space relative to the review content in Sections 4–6, or the review sections should be compressed to foreground the original argumentation.

## Score and Decision

**Calibration anchors:**
- **High**: yqKfMr0yvY (avg 7.67) — LLM-as-judges paper with principled measurement theory framework, comprehensive coverage, strong critique; BzFMBNqg7R (avg 7.0) — Model Atlas with clear unifying vision and formal grounding
- **Medium**: 816gaVGHgP (avg 5.33) — RL hyperparameter tuning paper with formal proof but narrow scope; a9eBWrd5Jg (avg 5.0) — compositionality critique with empirical evidence
- **Low**: U46jD48SJi (avg 4.33) — GNN over-smoothing position challenging framing with empirical weaknesses; R6TXwNF1SB (avg 3.0) — neuro-symbolic pillars paper criticized as summary of known ideas

This paper has a clearer mathematical framework and more novel contribution (Section 7) than the medium-low anchors, but is more review-heavy and has thinner counterargument engagement than the high-scoring anchors. It sits above 816gaVGHgP (which had narrower scope and less mathematical depth) but below yqKfMr0yvY (which had comprehensive critical engagement and a genuinely novel analytical framework). The thin alternative views section is the biggest gap relative to what makes a strong position paper.

MY FINAL SCORE: <pineapple>6</pineapple>
MY FINAL DECISION: <orange>Reject</orange>