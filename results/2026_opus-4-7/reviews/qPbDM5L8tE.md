## Anchors retrieved

| Path | Avg | Round | Comparison |
|---|---|---|---|
| oyXoGJQlUf.md | 3.00 | R1 | LLM-PDDL induction; weaker contribution than CoRAL. |
| q1Cv7Hp52y.md | 3.00 | R1 | Skill discovery + symbolic planning; less mature than CoRAL. |
| I0To0G5J7g.md | 3.20 | R1 | Self-improvement for embodied FMs; not directly comparable. |
| zEhTnQZB3D.md | 2.33 | R1 | Language tips for continual RL; weaker. |
| WtHKqtHVXo.md | 4.00 | R1+R2 | LLM-generated policy code for contact-rich tasks; closest analog — similar fairness/baseline complaints; CoRAL has more ablations and a clearer modular story. |
| qGL6fE1lqd.md | 4.40 | R1+R2 | LLMPhy: LLM + world model for physics reasoning; comparable scoping concerns. |
| iTsHStJKcm.md | 5.25 | R1+R2 | Make-a-Donut: zero-shot LLM-guided deformable manipulation; more thorough experiments. |
| OI3RoHoWAN.md | 8.00 | R1 | GenSim; much broader contribution. |
| 7BLXhmWvwF.md | 8.00 | R1 | Geometry-aware RL; stronger empirical work. |
| KsUh8MMFKQ.md | 8.00 | R1 | Differentiable physics for thin shells; stronger. |
| pISLZG7ktL.md | 8.00 | R1 | Data scaling laws; broader. |
| NkYCuGM7E2.md | 3.75 | R2 | LLM for AD; weaker. |
| liuqDwmbQJ.md, O4LoPhRSfb.md, vbr1OKK19i.md, 2snKOc7TVp.md | 4.75–6.0 | R2 | VLM benchmarks; off-topic. |

Round-1 bracket: 3.5–5.5. Round-2 narrowing: the closest topical anchor (WtHKqtHVXo, 4.0) has very similar issues — fairness of comparisons, weak baselines, unclear which design decision drives the gains. CoRAL is somewhat more ambitious (online adaptation, memory unit, more ablations) but has the planner-equals-evaluator concern and OOD VLA comparison. I place CoRAL ≈ WtHKqtHVXo, marginally above, around 4.0.

## Summary
CoRAL is a modular neuro-symbolic stack for contact-rich manipulation: FoundationPose tracks 6-DoF object poses, GPT-4o (as VLM) infers physical parameters, an LLM formulates MPPI cost functions and symbolic contact strategies, and an outer LLM loop refines them online; a RAG memory stores successful episodes. It is evaluated in ROBOSUITE/MuJoCo on six tasks against two VLA baselines, two expert-cost baselines, and four ablations.

## Strengths
- The Unified-VLM ablation gives clear, falsifiable evidence that role separation matters: collapsing perception+reasoning into one VLM yields ≤2/10 on all complex tasks vs. 4–10/10 with the modular pipeline (Table 1).
- The LLM-guided contact strategy ablation on T6 is concrete and quantitative: 32 vs 199 planning steps (83.9% fewer) and 1.33 m vs 3.69 m EE path length (§4.1.4), showing the symbolic contact prior prunes the search space.
- The online parameter-adaptation demonstration (Fig. 4) shows LLM-driven model-based diagnosis (mass/friction correction from observed motion failures), which is a concrete explainability mechanism end-to-end VLAs cannot provide.

## Weaknesses

### Fatal
None — the closest call is the planner-equals-simulator concern, which is unresolved but not proved fatal from the page.

### Major
- **Planner appears to roll out in the evaluation simulator.** §4 states the "MPPI controller was integrated on top of the ROBOSUITE/MuJoCo environment," and §3.3 describes K=200 perturbed rollouts in a "Planning World" parameterized by VLM-supplied θ. The paper never describes a separate forward model, so the natural reading is that MPPI rolls out in the same MuJoCo instance used for evaluation with only θ swapped. If so, the Fig. 4 online-adaptation result reduces to recovering a single misset scalar in an otherwise ground-truth simulator — far weaker than the "zero-shot, unknown environments" framing. Clarification is necessary; if Planning World ≡ Evaluation World, generalization claims need to be tempered.
- **VLA baselines are evaluated out of distribution.** OpenVLA-OFT and π0.5 use LIBERO-OBJECT / LIBERO-GOAL checkpoints on custom tasks (push-with-constant-force, flip-with-wall, push-and-pick cutting board) they were never trained on. §4.1.1's conclusion that "even fine-tuning an end-to-end policy is insufficient for contact-rich tasks" generalizes far beyond the experiment. The fair comparison would either fine-tune the VLAs on the custom distribution or restrict CoRAL evaluation to LIBERO splits the VLAs cover.
- **No comparison against the nearest peer baselines (VLMPC, IMPACT).** Related work positions CoRAL as a strict upgrade over LLM/VLM-in-MPC and VLM-cost-map methods (§2), but neither is reproduced on the six tasks. All baselines are either a different paradigm (end-to-end VLAs) or oracles (hand-designed costs). The claim that LLM-formulated cost *structure* is the right level of abstraction is asserted, not demonstrated.
- **Key ablation differences sit inside binomial noise at n=10.** Memory yields 2/10→4/10 on T1 and 9/10→10/10 on T3 — the 95% CIs overlap heavily. These shifts drive the central "memory accelerates and improves" claim in §4.1.3. The flagship task T1 is still 4/10 even with the full system, well below the FSM expert (8/10), a fact the paper does not engage with.

### Minor
- The "Unified VLM" and "w/o Pose Tracking" ablations are weak controls: both compare against well-known failure modes (VLM as pose regressor; VLM as end-to-end planner). The 0/10 outcomes confirm "the most degenerate alternative is bad" but do not isolate which CoRAL design decision is load-bearing. Swapping one interface at a time (e.g., LLM-only weight tuning with a fixed cost template) would be more informative.
- Fig. 4 / §4.1.4 inconsistency: the text says the Evaluation World was initialized with mass 2.0 kg vs ground truth 0.1 kg, but Fig. 4 shows correction from 1.00 → 0.85 kg over 3 s. These numbers don't match; the two should be reconciled.
- The mapping between T1–T6 and the "two LIBERO tasks" mentioned in §4 is not explicit. If T2/T3 are the LIBERO tasks, the VLA gap on their *intended* benchmark is essentially tied, and the dramatic gap is entirely on the custom tasks — strengthening the OOD concern.
- The memory retrieval mechanism (Eq. 1) is under-specified: embedding space, similarity threshold, and what counts as "sufficiently similar" are not defined. With six tasks and few stored episodes, retrieval may be trivial.
- N_retry=15 is not operationalized: what counts as an inner-loop "failure" when there is no mid-execution success signal? How is parameter-update oscillation prevented?
- Eq. 5 reuses Eq. 2's illustrative running cost even though §3.2 disclaims this is only an example; the actual cost functions the LLM produced for the six tasks are never shown in the body — a gap for both reproducibility and the explainability claim.

### Trivial
- The explainability evidence in §4.1.4 ("Explainability and Automated Failure Recovery") rests on a single anecdotal LLM diagnosis; the abstract's "significantly enhances explainability" is over-claimed relative to that.

## Nice-to-Haves
- A real-robot validation, given the sim-to-real motivation and the force-feedback augmentation (Eq. 7).
- Show the actual LLM-generated per-task cost functions and contact strategies in the body.
- Stress-test MPPI on a perturbed dynamics model (different friction model, geometry noise) so the online-adaptation result demonstrates closing a real sim-to-sim gap.

## Removed Points
*These points are flagged to be removed; treat with caution.*
- "No real-robot experiments" → demoted to Nice-to-Have: the paper scopes itself to simulation and is consistent on that.
- Generic "thin evidence" without anchored figures → merged into the binomial-noise Major point rather than counted twice.
- Generic "important problem" strength from the strength finder → dropped as superficial.

## Novel Insights
None beyond the paper's own contributions. The merger-level observation that the Planning World may literally be the evaluation simulator is the sharpest synthesized concern, but it is verification of an existing worry rather than a new insight.

## Suggestions
- Clarify in §3 whether the Planning World is the evaluation simulator with only θ swapped or a separately maintained model.
- Add VLMPC and/or IMPACT (or a hand-coded cost template + LLM-weight-only variant) on the six tasks.
- Either fine-tune VLA baselines on the custom task distribution or evaluate CoRAL on LIBERO splits the VLAs cover.
- Increase per-cell trials to ≥20–30 or report bootstrap CIs for memory/refinement ablations.
- Reconcile the mass values in §4.1.4 vs Fig. 4 and include per-task LLM-generated cost functions in the body/appendix.

## Score and Decision
CoRAL is a reasonable system paper with several genuine wins (Unified-VLM ablation, contact-strategy planning-cost reduction) but four substantive concerns (OOD VLA comparison, missing peer baselines, planner-equals-simulator ambiguity, binomial-noise ablations) materially weaken the central claims. Comparable in scope and depth of issues to WtHKqtHVXo (4.0) and qGL6fE1lqd (4.4); below iTsHStJKcm (5.25).

MY FINAL SCORE: <score>4</score>
MY FINAL DECISION: <decision>Reject</decision>