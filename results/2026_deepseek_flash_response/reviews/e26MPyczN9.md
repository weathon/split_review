## Summary

This paper re-evaluates prior claims that programmatic policies generalize better than neural policies in RL, revisiting three benchmarks (TORCS, KAREL, PARKING). The authors demonstrate that the reported gaps can be largely attributed to identifiable confounds: in TORCS, the neural policy's superior speed optimization caused worse generalization on OOD tracks (adjusting the reward function closes the gap); in KAREL, a simple feedforward network augmented with the last action matches programmatic generalization on all tasks. The paper proposes an expressivity/discoverability framework to reason about these findings and identifies a class of problems (those requiring instance-growing working memory) where fixed-capacity neural networks provably cannot express generalizing solutions.

## Strengths

- **Causal identification of the speed-optimization confound in TORCS.** The paper manipulates a single term (β in Equation 2) while keeping everything else fixed. Table 1 shows DRL with β=1.0 crashes on all OOD tracks, while DRL with β=0.5 achieves 76% generalization to G-TRACK-2 and 69% to E-ROAD. This directly demonstrates that the reported generalization gap was driven by the neural policy over-optimizing speed on the training track, not by representational superiority of programs.

- **A simple feedforward network with last-action augmentation matches programmatic policies on KAREL OOD generalization.** Table 2 shows "PPO with a_{t-1}" achieves return 1.00 (0.00 standard deviation) on 100×100 grids for STAIRCLIMBER, MAZE, TOPOFF, and FOURCORNER — identical to LEAPS's top scores — while the LSTM and ConvNet baselines from prior work all collapse to near-zero. This is a striking result: prior programmatic advantages in KAREL stemmed from poor discoverability of the baselines, not representational inexpressivity.

- **The expressivity/discoverability framework (Definitions 2–3) provides a principled vocabulary** for decomposing OOD generalization failures into the existence of a generalizing policy in the policy space vs. the ability of a search algorithm to find it. Section 5 uses this framework to coherently explain both the TORCS and KAREL findings as discoverability problems rather than expressivity failures.

- **The theoretical argument about fixed-capacity neural limits (Section 5) is rigorous and well-motivated.** Indexing among |𝒱| vertices requires Ω(log |𝒱|) bits, so constant-memory models (feedforward and fixed-state recurrent networks) provably cannot represent general pathfinding solutions. The paper correctly identifies this as a genuine expressivity ceiling where programmatic representations can provide an inherent advantage.

## Weaknesses

### Fatal
None.

### Major

- **The FUNSEARCH proof-of-concept is critically underspecified for the weight it carries.** The paper's climactic demonstration that programmatic representations can overcome the expressivity ceiling consists of: "Three runs of FUNSEARCH returned a correct implementation of breadth-first search, which generalizes to any pathfinding problem" (lines 308–309). There are no quantitative results — no success rates, no comparison to any neural baseline on the wall-sparse maze, no analysis of failure cases, no computational cost, and no description of how the wall-sparse maze differs from the original (Figure 7 is referenced but not described). Moreover, FUNSEARCH itself uses Qwen 3-Coder (30B), a large language model, as its backbone — the "programmatic representation" here is heavily mediated by a neural component. Given that the paper's title and abstract prominently identify when programmatic representations provide an inherent OOD generalization advantage, a proof-of-concept this thin is insufficient. The paper should either present quantitative results with neural baselines (which are predicted to fail) or significantly scale back the claims made on this basis.

### Minor

- **The "uncontrolled experimental factors" framing is somewhat overstated for TORCS.** The prior work (Verma et al., 2018) used the same reward function (β=1.0) for both the neural DRL agent and the NDPS programmatic agent — the experiment was controlled in the traditional sense. The issue is that the programmatic policies' *worse* optimization capability accidentally helped OOD generalization, making it appear that the representation itself was superior. This is a genuine finding about confounded *interpretation* rather than an uncontrolled experimental *design*. The paper would be more accurate framing this as a disentanglement of representation from optimization behavior.

- **Selection asymmetry in TORCS evaluation.** The paper reports OOD results only for the 13/30 DRL β=0.5 models that successfully learned G-TRACK-1 (4/15 for AALBORG). While excluding models that cannot solve the training task is natural, the paper does not discuss whether the 43% (G-TRACK-1) and 73% (AALBORG) failure rates of the neural approach are themselves meaningful disadvantages. The NDPS baseline succeeded on 3/3 seeds. Cross-condition seed counts also differ (30 vs. 3), making direct statistical comparison difficult.

- **PARKING results do not cleanly support the thesis.** DQN achieves higher absolute test success (0.18) than PSM (0.16), while PSM shows a smaller train-test gap (0.10 vs. 0.68). The paper presents both metrics transparently, but this domain neither confirms nor refutes the confound narrative. The paper's honest admission that PARKING is challenging for both representations (line 266) is the most accurate characterization.

- **The theory-experiment gap is not fully bridged.** The paper argues that neural networks cannot represent solutions requiring instance-growing memory but does not empirically demonstrate this failure on any task where it actually matters. The KAREL benchmarks used are all solvable by constant-memory wall-following (as the paper acknowledges), and the wall-sparse maze demonstration lacks neural baselines. The theoretical argument is sound, but the experimental support for the paper's central claim about when programmatic representations have an inherent advantage remains incomplete.

- **Missing experimental details.** The paper does not describe network architectures (number of layers, hidden sizes), learning rates, training steps, or hyperparameter tuning for the neural models. Given that the paper's thesis is that "a few modifications" enable neural policies to match programmatic ones, these details are important for reproducibility.

### Trivial
None.

## Nice-to-Haves
- Adding confidence intervals or statistical significance tests for the TORCS and KAREL comparisons.
- A direct neural baseline on the wall-sparse maze to complete the experiment-theory connection.
- An explicit discussion of whether the TORCS β=0.5 training failure rate (43% on G-TRACK-1) itself constitutes a practical disadvantage of neural training.

## Removed Points
These points from the inputs were removed with justification:
- **Expressivity/discoverability framework is "circular" (Harsh Critic):** The paper does not claim the framework is predictive; it is used as a post-hoc conceptual vocabulary, which is a legitimate and common use of such definitions in ML. Removed as overreach.
- **Missing Figure 7 / appendix content:** Parser artifacts from PDF extraction, not author errors.
- **Definition 1 too strong vs. evaluation:** The paper explicitly acknowledges this gap (lines 45–46). Removed as already addressed.
- **Strength Finder's generic claims about the problem being "important":** These add no information. Removed.
- **Speculation about other works' confounds (Qiu & Zhu, etc.):** The paper is appropriately cautious ("Although a careful investigation is needed"). Removed as the critic's concern about speculation is not a valid weakness.

## Novel Insights

The paper's most valuable meta-insight — not fully captured by either input — is that the representational *equivalence* of programmatic and neural spaces on existing benchmarks (both can express the same generalizing solutions) forces the conclusion that observed generalization gaps must be attributed to the *search process* (discoverability), not the representation itself. This reframes the debate from "which representation is better?" to "how do we design search processes that find generalizing solutions in expressive spaces?" — a productive reframing with implications beyond the specific domains studied. The paper also correctly identifies that the genuine differentiator is problems requiring instance-growing memory, where the expressivity ceiling bites.

## Suggestions

1. **Expand the FUNSEARCH proof-of-concept substantially.** Run multiple seeds, report success/failure rates, compare against neural baselines on the wall-sparse maze (which are predicted to fail), and describe the wall-sparse maze construction. Without this, the climactic claim of the paper is unsupported.
2. **Reframe the TORCS finding** as a disentanglement of representation from optimization capability rather than an "uncontrolled experimental factor."
3. **Address the selection asymmetry in TORCS explicitly** — report OOD results for all 30 seeds, including those that failed the training track, or at minimum discuss the asymmetry.
4. **Add network architecture and hyperparameter details** for all neural models in the main text or appendix.

## Score and Decision

**Score: 6.0**

**Decision: Accept**

**Calibration Report:**

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| Reclaiming the Source of Programmatic Policies | `NGVljI6HkR.md` | 3.67 | 1 | Weaker — narrower scope, less surprising findings |
| GRAM: Generalization in Deep RL | `UfczlMudN6.md` | 6.00 | 1 | Comparable quality — well-executed but limited scope |
| Addressing Long-Horizon Tasks (POMPs) | `lUWf41nR4v.md` | 4.50 | 1 | Weaker — incomplete methodology, less rigorous evaluation |
| How the Level Sampling Process impacts ZSG | `X1p0eNzTGH.md` | 5.67 | 2 | Weaker — mixed reviews, limited evaluation scope |
| The Generalization Gap in Offline RL | `3w6xuXDOdY.md` | 6.50 | 2 | Similar genre, comparable quality — thorough experiments but less conceptual novelty |
| ExeDec: Execution Decomposition | `oTRwljRgiv.md` | 7.00 | 2 | Stronger — more thorough experiments, but different problem setting |
| OMNI-EPIC | `Y1XkzMJpPd.md` | 6.75 | 2 | Stronger overall execution |

**Round 1 bracket:** [5.5, 7.0]. The paper is stronger than the 3.67 and 4.50 programmatic RL papers and roughly comparable to the 5.67–6.50 generalization-in-RL papers.

**Round 2 narrowing:** The paper sits between the 6.00 GRAM paper (comparable quality but our paper has broader scope and conceptual novelty) and the 6.50 Generalization Gap paper (similar re-evaluation genre with more thorough experiments). The 7.00 ExeDec paper is stronger in experimental execution but addresses a different problem. The FUNSEARCH thinness prevents a higher score.

**Final score:** 6.0. Core contributions (TORCS/KAREL re-evaluations, expressivity/discoverability framework, memory-limitation theory) are solid and well-supported. The paper is held back primarily by the critically underspecified FUNSEARCH proof-of-concept, which is the climactic demonstration of the paper's central thesis about when programmatic representations provide an inherent advantage.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>