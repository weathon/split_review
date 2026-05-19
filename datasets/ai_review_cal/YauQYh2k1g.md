- Decision: Accept
- Avg Score: 6.25
- Scores: 8, 5, 6, 6
Now I have all the evidence I need. Let me compose the final consolidated review.

## Summary

This paper studies the adversarial robustness of multimodal LM agents in a realistic web environment (VisualWebArena). The authors curate VWA-Adv, a benchmark of 200 targeted adversarial tasks, and propose the Agent Robustness Evaluation (ARE) framework, which decomposes agent systems into directed graphs with edge weights quantifying adversarial influence. The central empirical finding is that state-of-the-art agents (GPT-4V, GPT-4o) are highly vulnerable to imperceptible perturbations to a single product image (≤5% of page pixels), achieving up to 67% attack success rate. Further, adding commonly-used components (evaluators, value functions) that improve benign performance can *increase* vulnerability when those components are themselves attacked.

## Strengths

1. **Realistic and well-constrained threat model.** The attacker can only modify their own product image within a tight $L_\infty$ bound of $\epsilon=16/256$ (≤5% of page pixels) or add one piece of text (Sections 3.1, 4.2). This is far more realistic than the full-input-control or white-box assumptions common in prior work, and directly supports the claim that even minimal, imperceptible changes can hijack agents.

2. **Systematic decomposition of adversarial influence via agent graphs.** The ARE framework (Section 3.2–3.3, Figure 2) models agents as directed graphs with formal edge weights $\lambda(e)$. This goes beyond end-to-end ASR to attribute vulnerability to specific components and connections. The paper demonstrates reusability of edge weights across configurations (e.g., the self-captioning edge weight $\lambda=0.38$ from Figure 4 is reused in the defense analysis of Section 5.4).

3. **Counterintuitive finding that new components can harm robustness.** The paper shows (Sections 5.2–5.3, Figures 5–6) that adding an evaluator (reflexion) or value function (tree search) increases ASR when those components are attacked: from 31% (base) to 36% (reflexion) and 38% (tree search). This result — that components designed to improve benign performance open new attack surfaces — is well-supported and has clear practical implications.

4. **Multiple attack modalities with transferability.** The paper implements three distinct attack types — prompt injection (text access), white-box PGD on captioners, and black-box CLIP-based attacks (Section 4.3). The CLIP attack transfers to black-box LMs, achieving 19% ASR on self-captioning agents and even 10% on base agents without captions (Figure 4C–D), demonstrating breadth across access levels.

5. **Honest defense evaluation showing limited gains.** The paper evaluates four defenses (system prompts, paraphrase, consistency check, instruction hierarchy) in Section 5.4. The consistency check reduces captioner-attack ASR to near-zero but is expensive (many API calls) and itself vulnerable to CLIP attacks (38% ASR bound). This provides a realistic, sobering assessment rather than overclaiming a solution.

6. **Robustness-utility trade-off analysis.** Figure 4 (right) quantitatively compares different LMs, showing a positive correlation between benign SR and ASR, with GPT-4o offering the best trade-off — a practical guide for model selection.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **No confidence intervals for ASR comparisons.** ASR values are reported as point estimates from 200 tasks, but binomial confidence intervals are not provided. Several of the paper's comparative claims hinge on differences of 5–7 percentage points (e.g., 31% base → 36% reflexion, 31% → 38% tree search). With 200 trials, a 95% CI for 31% is approximately ±6.4pp; the difference between 31% and 36% falls within this range. The comparisons remain directionally plausible and the overall trend is robust, but the lack of uncertainty intervals weakens the precision of the claim that "new components harm robustness" at the specific numerical values reported. Fixable with a straightforward addition.

2. **No dedicated limitations section.** While the paper is transparent about its methodology (e.g., explicitly stating in Section 5.2 that it "simulates" the unattacked-component scenario by providing clean/adversarial captions), it would benefit from a dedicated limitations section discussing: (a) the simulated nature of the uncompromised-component experiments relative to the full threat model, (b) reliance on a single environment suite (VisualWebArena), (c) selection bias toward tasks the agent can already solve, and (d) dependence on specific API model versions. This is a presentation gap, not a correctness gap.

3. **Operationalization of AdvIn(c) is task-specific rather than fully general.** The formal definition of $\operatorname{AdvIn}(c)$ as the "tightest upper bound" on downstream ASR suggests a component-independent quantity. In practice, it is determined by checking whether an intermediate output (e.g., a caption) contains adversarial goal text or leads to an adversarial action (Table 1). This is a reasonable operationalization for the paper's experiments, where adversarial goals are well-defined, but it is more heuristic than the formal framing implies. The reusability claim ("only need to be computed once," Section 3.3) is conditional on upstream design remaining fixed, which the paper states, though this condition limits the scope of reusability in practice.

### Trivial
None.

## Nice-to-Haves

- **Automating edge weight computation.** Currently AdvIn(c) is determined by checking whether an intermediate output contains adversarial goal text. Using an automated judge (e.g., an LLM prompted to check alignment with the adversarial goal) and validating a sample would make the framework more operational and reproducible by others.
- **Direct evaluation of the evaluator/value function on full screenshots.** The current approach attacks the evaluator via adversarial captions rather than by modifying the environment screenshot directly. An experiment where the LLM-based evaluator takes the (adversarial) screenshot as input would further strengthen ecological validity for the "evaluator attacked" scenario, though this is a secondary question given the paper's focus on component-level isolation.

## Novel Insights

The most striking insight from combining both reviews is that the ARE framework's diagnostic power lies precisely in the tension it reveals: components that "block" adversarial influence when uncompromised (reducing ASR) simultaneously provide new, concentrated attack surfaces when compromised (increasing ASR beyond the base agent). The harsh critic correctly notes that the "unattacked component" scenario is a simulation, not a natural configuration — but this is precisely the point. The paper's value is in making this tension visible and measurable via edge weights, not in claiming that unattacked components are the realistic default. The finding that attack success can be decomposed into *where in the graph* influence enters versus where it is blocked, and that this decomposition generalizes across reflexion and tree-search architectures, is a genuinely novel methodological contribution that neither review fully captured.

## Suggestions

1. **Add 95% binomial confidence intervals** to all reported ASR and Benign SR values. This is a low-effort change that would substantially strengthen the empirical claims, particularly the comparative ones (base vs. reflexion vs. tree search).
2. **Add a brief limitations paragraph** covering the simulated nature of the unattacked-component experiments, the single-environment scope, and the API-version dependence. This would preempt the most common methodological concerns.
3. **Clarify the edge-weight reusability claim** by explicitly stating the conditional ("if upstream design remains fixed") earlier in the framework introduction, rather than only in the technical definition.
