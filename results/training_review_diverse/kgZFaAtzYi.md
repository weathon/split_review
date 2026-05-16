Now I have a thorough understanding of the paper and can construct the final consolidated review. Let me synthesize everything.

---

## Summary

This paper studies whether an attacker who can access (and compute gradients on) a single agent in a multi-agent LLM system can craft an adversarial suffix that manipulates the entire system's collective decision. The authors propose M-Spoiler, which simulates a multi-turn debate between a normal agent and a "stubborn" adversary during training, weighing gradients across turns with exponential decay to produce adversarial suffixes via GCG-style optimization. Experiments across six models, three tasks, and three attack backbones show that M-Spoiler consistently outperforms the single-agent GCG baseline.

## Strengths

- **Timely and well-motivated research question.** The paper identifies a realistic vulnerability scenario — an attacker with gray-box access to one agent in a multi-agent system — that is distinct from prior black-box/white-box characterizations. This gap is real and the problem is practically important as multi-agent LLM systems gain adoption.

- **Consistent empirical outperformance across diverse settings.** M-Spoiler achieves higher ASR than the single-agent GCG baseline in nearly every reported condition: targeted/untargeted attacks (Table 1), six different model pairs (Table 2, all 8 comparisons), three tasks (Table 3, all 9 comparisons), varying agent counts (Table 4), and different suffix lengths (Table 6, 5/6 comparisons). The margins are often substantial (e.g., 64.2% vs. 41.7% targeted attack, Table 1).

- **Broad evaluation scope.** The paper tests six models (Llama2/3, Vicuna, Guanaco, Mistral, Qwen2), three datasets (AdvBench, SST-2, CoLA), three attack backbones (GCG, I-GCG, AutoDAN), and agent counts ranging from 2 to 15. This breadth strengthens generalizability claims.

- **Ablation on chat rounds and suffix length provides practical insight.** The analysis in Section 4.6 shows that more rounds improve ASR but slow convergence (Figure 3), and longer suffix lengths generally boost performance — useful guidance for practitioners.

## Weaknesses

### Fatal
None.

### Major

1. **Multi-turn gradient computation is under-specified (reproducibility gap).** The paper states that gradients are "obtained from the Normal Agent" at each turn, weighted, and used for GCG-style token replacement. However, GCG was designed for single forward passes. Extending it to multi-turn conversations where the suffix influences hidden states at each turn, and later turns depend on *generated* tokens from earlier turns, raises non-trivial questions: Are gradients back-propagated through the entire unrolled conversation (requiring a full computational graph across generated tokens)? Is teacher forcing used? Are gradients truncated/detached at generated token boundaries? The paper does not address any of these. Without this specification, the core training procedure cannot be reproduced or verified. (Lines 73–79 describe the weighting but not the gradient computation mechanics.)

2. **Core design choice (stubborn adversary) is not isolated by ablation.** The paper claims the key contribution is simulating a "stubborn adversary" during training, but the only experimental comparison is against a baseline that trains on a *single agent with no multi-turn simulation at all*. This comparison conflates two factors: (a) the multi-turn simulation itself, and (b) the specific choice of a stubborn adversary. A control condition that replaces the stubborn agent with a second normal agent (same model, same flexibility) is needed to determine whether the benefit stems from multi-turn training or from the adversary's fixed opinion. The paper's ablations on chat rounds and suffix length do not address this.

### Minor

3. **No statistical uncertainty reported.** All ASR results appear to come from a single run per condition. No confidence intervals, standard deviations, or multiple seeds are provided. For a metric that can vary with random initialization, sampling, and optimization stochasticity, this makes it impossible to assess whether observed differences between methods are meaningful.

4. **No-attack baseline issue on CoLA is not properly addressed.** In Table 3, the "No Attack" condition shows non-negligible ASR on CoLA (e.g., 27.50% for Mistral, 7.50% for combined system). This means the un-attacked multi-agent system itself is unreliable on this task, and the reported ASR for attacks may conflate attack success with the system's inherent error rate. The paper acknowledges the issue briefly ("in some cases, no attack performs best") but does not adjust the metric (e.g., measuring improvement over the no-attack baseline) or discuss why the system is error-prone on this task.

5. **The decay constant α is not reported.** The exponential decay function is defined as $f(\lambda) = \alpha^{\lambda/t}$ with $t=1$, but the value of $\alpha$ is never specified. This is a hyperparameter that affects the relative importance of early vs. late turns and is needed for reproducibility. (Line 73.)

6. **Untargeted attack definition conflates two distinct failure modes.** The paper defines untargeted attack success as "the final output is incorrect or agents fail to reach an agreement." This merges two qualitatively different outcomes: (a) agents unanimously converging on a wrong answer vs. (b) agents failing to converge at all. Reporting a single ASR masks which mechanism drives the result.

7. **Interpretation of "infectious" propagation with more agents is premature.** The paper observes that ASR increases with more agents (2 → 3 → 15, Table 4) and attributes this to "infectious" propagation. However, with more agents, the likelihood that a single compromised agent is in the majority increases mechanically, even without propagation. The experiment does not control for this confound.

8. **Defense analysis is thin for the strength of the claim it supports.** The paper concludes that "existing defense mechanisms are inadequate against these attacks" based on testing only two defenses (introspection, self-perplexity filtering), with the latter tested only on a subset of systems. The introspection defense shows a non-trivial ASR reduction, and the self-perplexity filter is tested only against GCG and AutoDAN backbones. This is insufficient to support a blanket conclusion about the inadequacy of all existing defenses.

### Trivial

- The game-theoretic framing ("game with incomplete information") is used to motivate the problem but is never formalized — no equilibrium, strategy, or game-theoretic analysis is derived. This is not a flaw in the method, but it over-promises slightly.
- The Byzantine Fault analogy is mentioned but not developed beyond the initial analogy.

## Nice-to-Haves

- Running the main experiments with 3–5 random seeds and reporting mean/variance would substantially increase confidence in the results.
- A discussion of computational overhead (wall-clock time per iteration compared to baseline GCG) would help practitioners assess practical feasibility.
- For the CoLA task where no-attack ASR is high, reporting the *increase* over the no-attack baseline would provide a cleaner measure of attack effectiveness.

## Removed Points

- Concern about the GCG candidate sampling hyperparameters (top-k, batch size) being unreported: These are standard GCG implementation details that a practitioner would supply from the original paper.
- Question about why the initial suffix is "!" repeated 20 times: This is standard practice in GCG-based attacks and does not warrant a weakness.
- Criticism that the Related Work does not clearly state why existing work does not cover the scenario: The paper explicitly distinguishes the gray-box scenario from prior black-box/white-box treatments. While this could be expanded, it is not absent.
- Concern about the paper not specifying exact prompts controlling the stubborn agent: The paper describes the stubborn agent's behavior in sufficient functional detail (lines 71–72).

## Novel Insights

The reviews surface one genuinely novel perspective beyond the paper's own contributions: the insight that the paper cannot distinguish whether its gains come from multi-turn simulation or from the stubborn-adversary design. This is not just a missing ablation but a structural ambiguity about what the method *is* contributing. If the benefit comes entirely from multi-turn simulation, then the "stubborn" framing is decorative; if it comes specifically from the fixed opinion, the paper should say so explicitly and explain the mechanism. Either way, this point reframes what the paper needs to establish.

## Suggestions

1. Provide a precise algorithmic description (pseudocode or explicit text) of how gradients are computed across turns in the multi-turn debate — specifically addressing whether generated tokens are treated as fixed or part of the computational graph.
2. Add an ablation comparing M-Spoiler against a variant where both agents are normal (no stubborn adversary) to isolate the effect of the stubborn design.
3. Report main results with multiple seeds (e.g., 5 runs) and include confidence intervals or standard deviations.
4. For tasks where the no-attack ASR is high, report the attack's marginal improvement over the no-attack baseline, and discuss why the un-attacked system is unreliable on that task.

## Score and Decision

The paper addresses a timely and practically important problem, proposes a reasonable approach, and provides broad empirical evaluation. The core result — that a gray-box attack on a single agent can manipulate multi-agent collective decisions — is convincingly demonstrated in its broad strokes. However, two significant issues prevent acceptance in the current form: (1) the multi-turn gradient computation is under-specified enough to harm reproducibility, and (2) the central design claim (stubborn adversary) is not isolated by a proper ablation, leaving ambiguity about what drives the improvement. These are addressable in revision but are non-trivial gaps. The statistical reporting and the CoLA no-attack issue are also concerns, though less severe.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>