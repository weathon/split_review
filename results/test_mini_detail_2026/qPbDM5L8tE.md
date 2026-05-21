Now I have a clear picture of the calibration landscape. Let me write the final review.

**Round 1 bracket:** Based on my first calibration search, the paper sits in the (3.5, 7.5) band. It's clearly stronger than the weak-band papers (avg 3.0-3.33, which are incremental/poorly-executed works) and clearly weaker than the strong-band papers (avg 8.0, which have definitive contributions and very strong execution). **Plausible range: 4.5–6.5.**

**Round 2 narrowing:** I examined papers at 5.00 (Semantic World Models, Reject), 5.33 (BiNoMaP, Reject), 5.50 (PDDLLM, Accept; VLBiMan, Accept), 5.60 (RoboTwin 2.0, Reject), and 6.00 (Ctrl-World, Accept; Sim2Real-VLA, Accept). CoRAL's architecture is more novel than most, and its ablations are thorough. However, the Figure 4 discrepancy is a concrete evidential flaw that none of these anchors share, and the simulation-only evaluation with small trial counts limits the strength. CoRAL sits below the 5.5-6.0 accepted papers (which have real-robot validation or cleaner evidence chains) and above the truly weak 3.0-3.33 papers. **Final score: 5.0**, comparable to Semantic World Models — novel architecture with clear potential, but significant evidential issues that need resolution before acceptance.

---

## Summary

CoRAL proposes a modular, neuro-symbolic framework for zero-shot contact-rich robotic manipulation. It separates perception (VLM estimates mass, friction, pose) from reasoning (LLM generates cost functions and contact strategies for an MPPI controller), with nested feedback loops for online adaptation and a memory unit for experience reuse. Evaluated on six challenging simulated manipulation tasks, CoRAL outperforms end-to-end VLA baselines (OpenVLA-OFT, π₀.₅) on contact-rich tasks and ablated variants demonstrate the importance of each component.

## Strengths

1. **Genuinely novel architecture validated by ablation.** The key design choice — separating VLM (perception/physical parameter estimation) from LLM (cost function generation and strategy formulation) — is directly tested via the *CoRAL (Unified VLM)* ablation, which collapses both into a single model and catastrophically fails (0/10 on 4 of 6 tasks). This is concrete evidence that the modular separation is critical, not decorative. Table 1 provides clean, interpretable evidence.

2. **LLM-generated cost functions and contact strategies for MPPI are a fresh contribution.** Rather than using the LLM to select subgoals or waypoints (as in prior decoupled-reasoning works), CoRAL has the LLM directly formulate the *mathematical structure* of the optimization objective (Equation 2) and propose focused contact surfaces (Equation 3). The quantitative analysis for the "Flip with Wall" task (83.9% fewer planning steps, 63.9% shorter path) demonstrates that this symbolic guidance meaningfully prunes the MPPI search space.

3. **Zero-shot outperformance of VLA baselines on demanding tasks is clearly demonstrated.** In Table 1, CoRAL achieves 7/10 on T6 (Flip with Wall) and 4/10 on T1 (Push+Pick Board), while OpenVLA-OFT and π₀.₅ score 0/10 on both. This provides credible evidence that the neuro-symbolic approach addresses a genuine limitation of imitation-learned policies on contact-rich scenarios.

4. **Thorough ablation study isolates each component's contribution.** Removing pose tracking (0/10 on most tasks), removing refinement (drops T1 from 4/10→0/10), removing memory (e.g., T6 from 7/10→5/10) — each ablation cleanly tests a specific design claim. This is stronger ablation evidence than many papers in this space.

## Weaknesses

### Major

1. **Figure 4 contradicts the text it is supposed to support — undermines the core adaptation claim.** The text (Section 4.1.4) describes an experiment with an initial belief of 2.0 kg and a true mass of 0.1 kg, claiming convergence "remarkably close to their true values." However, the Figure 4 caption describes a y-axis spanning only 0.75–1.00 kg, an "Initial Mass" line constant at 1.0 kg, and a "Corrected Mass" line dropping from 1.0 kg to approximately 0.85 kg — neither matching the 2.0 kg initial belief nor approaching 0.1 kg. The text also mentions friction correction (0.9→0.5) but Figure 4 only plots mass. This is not a minor axis-labeling issue; the central quantitative evidence for the online adaptation claim does not match the described experiment. The adaptation concept may still be sound (the *w/o Refinement* ablation provides supporting evidence), but as presented, this figure cannot be used to support the dramatic convergence claim the paper makes.

### Minor

2. **Simulation-only evaluation limits the practical claims.** Every experiment runs in MuJoCo via Robosuite, where the "planning world" and "evaluation world" share the same physics engine. The reactive feedback term (Eq. 7) is intended to address sim-to-real gaps, but is never tested under real sensor noise, calibration errors, or unmodeled dynamics. The authors acknowledge this as a limitation (Section 5), but the paper's title claims of "Contact-Rich Adaptive … Control for Robotic Manipulation" and the real-world framing in the introduction are broader than the evidence supports. A single real-robot experiment on one task would substantially strengthen confidence.

3. **Small trial count (10 per condition) with overclaimed significance.** Going from 2/10 to 4/10 (T1 memory benefit) or 5/10 to 7/10 (T6) is described as "significantly" boosting performance (Section 4.1.3). With only 10 trials, the binomial 95% confidence intervals for 2/10 and 4/10 overlap substantially (≈3–44% vs. ≈12–74%), and the difference is not statistically significant. The paper should include confidence intervals or bootstrap estimates for all success-rate comparisons, and avoid claiming "significance" without a proper test.

4. **Critical implementation details are underspecified.** The prompts used for the VLM (physical parameter estimation), the LLM (Task Formulation), the LLM (Online Adaptation), and the RAG memory retrieval are not provided. The dynamics of the "planning world" are described only as the world model constructed from estimated parameters θ — it is unclear whether this is a separate lower-fidelity model or the same MuJoCo simulator with perturbed parameters. The MPPI wall-clock time per control cycle and the actual control frequency are not reported, making it difficult to assess real-time feasibility. These details are important for reproducibility.

### Trivial

5. The limitations paragraph (Section 5) is only two sentences and defers discussion to an appendix that is not accessible in this format. The main body would benefit from a more substantive limitations discussion.

## Nice-to-Have

- The grounding of the memory unit via RAG with LLM-based retrieval is described at a high level. A concrete example of what is stored, how similarity is computed, and how the retrieved plan differs from the initial plan would strengthen this component.
- The adaptive term in Eq. (7) is a proportional feedback on pose error. In contact-rich tasks, force feedback would be more directly relevant; a brief justification of the pose-based choice (or a comparison) would be informative.

## Removed Points

- **"Method dependence on GPT-4o is a fatal reproducibility concern"** — The harsh critic notes that prompts are not specified. This is a valid minor concern (moved to weakness 4 above), but it is standard practice in the field to use proprietary VLMs/LLMs without full prompt disclosure, and this alone is not a fatal or even major weakness for an ICLR paper proposing a systems architecture.
- **"Comparison with OpenVLA-OFT/π₀.₅ is unfair"** — The critic acknowledges this isn't necessarily a flaw. The asymmetry (baselines fine-tuned on LIBERO, CoRAL uses a foundation model) favors the baselines if anything, not the proposed method. Removed.
- **"Unfair baseline comparison" inverted** — Following the rule that asymmetry favoring baselines is not a valid weakness. Removed.
- **"Missing related work"** — General rule prohibits mentioning missing related works as you cannot verify their existence. Removed.
- **Some formatting/style nitpicks and speculative concerns** — Removed per hard rules.
- **Strength Finder's generic strengths** — Claims like "this paper addressed an important problem" and generic framing of the contribution as desirable are removed. Only concrete, evidence-backed strengths are retained above.

## Novel Insights

None beyond the paper's own contributions. The key insight — that an LLM can structure the cost function and contact strategy of an MPPI controller to make contact-rich manipulation zero-shot — is the paper's own, and the reviews do not add a dimension of analysis that reframes or deepens this contribution.

## Suggestions

1. **Fix Figure 4.** Align the figure content with the text. Either plot the actual 2.0 kg → 0.1 kg correction described, or adjust the text to describe what Figure 4 actually shows (a milder correction from 1.0 kg → 0.85 kg). Add the friction correction plot alongside mass on the same axes.
2. **Add statistical rigor.** Report bootstrapped 95% confidence intervals on all success-rate entries in Table 1. Remove or qualify the word "significantly" when the data do not support it.
3. **Include one real-robot experiment.** Even a single task (e.g., Push with Constant Force, which directly tests the reactive feedback of Eq. 7) on real hardware would substantially strengthen the paper's claims about real-world applicability.
4. **Release prompts and planning-world specification.** The prompts for the VLM parameter estimation, LLM Task Formulation, LLM Online Adaptation, and memory RAG should be included.

## Score and Decision

**Round 1 bracket:** 4.5–6.5 (between papers averaging ~3.0 and those averaging ~8.0).

**Round 2 narrowing anchors:**
- **Semantic World Models (5.00, Reject)** — Similar score level. Novel framing but privileged-state requirement and simulation-only evaluation. CoRAL's architecture is comparably novel, but Figure 4 issue is an evidential problem that SWM doesn't have.
- **BiNoMaP (5.33, Reject)** — RL-free bimanual pipeline with limited novelty. CoRAL has stronger architectural novelty and cleaner ablations but weaker evaluation.
- **PDDLLM (5.50, Accept)** — LLM-based planning domain derivation with real-robot experiments. CoRAL is more architecturally novel but lacks real-robot validation that PDDLLM has.
- **VLBiMan (5.50, Accept)** — One-shot bimanual with extensive real-robot experiments. CoRAL is more novel architecturally but massively outmatched in evaluation depth.
- **Ctrl-World (6.00, Accept)** — Well-executed world model with real-robot experiments. CoRAL has more novel architecture but weaker execution and evidential issues.
- **Sim2Real-VLA (6.00, Accept)** — Real-robot zero-shot transfer with thorough evaluation. CoRAL's architecture is more novel but lacks real experiments and has the Figure 4 problem.

**Final score:** 5.0. The paper has a genuinely novel architecture and strong ablations, placing it above the 3.0–4.0 range of clearly weak papers. However, the Figure 4 discrepancy is a concrete evidential flaw in the primary adaptation claim, the simulation-only evaluation limits the scope of the practical claims, and the statistical basis (10 trials, no confidence intervals) is thin. These issues are fixable — the core idea is promising — but in the current form the paper does not meet the evidence standard for a top venue.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>