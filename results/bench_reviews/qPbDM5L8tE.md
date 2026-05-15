Now I have all the information I need. Let me compose the final consolidated review.

## Summary

The paper proposes CoRAL, a modular neuro-symbolic framework for zero-shot contact-rich robotic manipulation. It separates perception (FoundationPose + VLM for pose tracking and physical parameter estimation) from reasoning (LLM for generating MPPI cost functions, contact strategies, and online adaptation). A memory unit enables experience reuse. Experiments on six simulated contact-rich tasks show CoRAL succeeds where end-to-end VLA baselines (OpenVLA, π₀.₅) completely fail, and ablations validate the architectural choices.

## Strengths

- **LLM-driven cost function and contact strategy generation for MPPI is a genuine contribution.** Rather than using the LLM to identify sub-goals or objects (as in prior LLM+planner work), CoRAL has the LLM formulate the mathematical structure and weights of the MPPI cost function itself (Eq. 2) and propose symbolic contact regions that bias sampling (Eq. 3). This grounds high-level reasoning directly into the optimal control problem.

- **Role separation between VLM (perception) and LLM (reasoning) is empirically validated.** The Unified VLM ablation, which merges both functions into a single multimodal prompt, collapses to 0/10 on T1, T3, T5, T6, while the separated architecture achieves non-zero success on those same tasks (Table 1). The paper also shows that removing FoundationPose (w/o Pose Tracking) causes catastrophic failure, confirming that a dedicated pose estimator is critical.

- **Zero-shot success on contact-rich tasks where fine-tuned VLA models completely fail.** On T1, T4, T5, T6, OpenVLA-OFT and π₀.₅ achieve 0/10 on three of four tasks, while CoRAL obtains 4/10, 9/10, 9/10, and 7/10 respectively without any task-specific fine-tuning (Table 1). This demonstrates a real capability gap that the modular approach addresses.

- **LLM-generated contact strategy dramatically prunes the planning search space.** In the "Flip with Wall" task, the LLM-guided strategy requires 83.9% fewer planning steps (32 vs. 199) and 63.9% shorter end-effector travel (1.33 m vs. 3.69 m) compared to an unguided variant (Section 4.1.4). This shows that symbolic reasoning makes long-horizon contact planning tractable.

- **Memory unit provides measurable improvement.** Adding memory boosts success from 2/10 to 4/10 on T1 and from 9/10 to 10/10 on T3, while also reducing completion times (Table 1). This demonstrates the value of experience reuse in this setting.

## Weaknesses

### Fatal
None.

### Major

1. **Figure 4 contradicts the text's claim about online parameter adaptation — this undermines a core experimental demonstration.** The text states the evaluation world was initialized with mass 2.0 kg (ground truth 0.1 kg) and that after adaptation "the agent's belief about both mass and friction converged remarkably close to their true values." However, the figure caption describes a y-axis ranging from 0.75 to 1.00 kg, with the corrected mass starting at 1.0 kg and converging to approximately 0.85 kg — neither close to the stated ground truth of 0.1 kg nor showing 2.0 kg on the axis. The OCR may be imperfect, but the paper text itself asserts convergence to 0.1 kg while the figure as described shows nothing of the sort. This is a critical inconsistency in the paper's headline demonstration of online physical parameter correction. The authors must clarify what Figure 4 actually shows and reconcile it with the text, or the claim of successful parameter adaptation to ground-truth values is unsupported.

2. **The paper does not compare against the most relevant baselines (IMPACT, VLMPC).** The Related Work (Section 2) discusses IMPACT and VLMPC as closely related prior work that integrates foundation models with motion planners, and claims CoRAL "significantly advances this paradigm." Yet the experimental comparison includes only end-to-end VLA models (OpenVLA, π₀.₅) and human-designed cost functions. The failure of end-to-end VLAs on contact-rich tasks is expected given their training data biases and tells us little about improvement over the LLM+planner family. Without at least one comparison to IMPACT, VLMPC, or a similar system, the paper cannot substantiate its claim of advancing the state of the art in its own paradigm. The human expert baselines provide upper bounds but do not substitute for direct comparison with prior methods in the same family.

### Minor

3. **The memory evaluation protocol is unclear.** The paper reports that CoRAL with memory outperforms CoRAL without memory (e.g., 4/10 vs. 2/10 on T1) but does not specify whether memory is populated from earlier trials within the same evaluation or from a separate prior set. The text mentions "after just a single successful completion, the system can store the entire successful interaction context," suggesting within-evaluation accumulation. If memory grows during the reported 10 trials, the comparison is not between equivalent conditions — the "with memory" condition has access to more data. The authors should clarify the protocol and, if memory accumulates during evaluation, acknowledge this directly rather than presenting it as a straightforward ablation.

4. **No statistical variance is reported.** Results are given as success counts (x/10) and average completion time over successful trials, with no confidence intervals, standard deviations, or statistical tests. Given the stochasticity from MPPI sampling, LLM generation, and randomized object parameters (mass, friction, dimensions), 10 trials per condition is thin. The average completion time is computed over differing numbers of successful trials (sometimes as few as 2-4), making cross-condition time comparisons unreliable.

5. **The reactive control augmentation (Eq. 7) is never ablated.** The paper mentions a feedback term for robustness but provides no evaluation of its contribution. Given that force feedback is central to contact-rich task performance, an ablation with and without this term would help clarify which components drive the reported results.

### Trivial
- The term "zero-shot" is used alongside a memory unit that stores and retrieves past experiences, which creates some terminological tension. Clarifying the distinction (zero-shot w.r.t. task-specific fine-tuning vs. within-task experience reuse) would help.

## Nice-to-Haves
- The evaluation is simulation-only. Contact-rich manipulation is highly sensitive to sim-to-real gaps (e.g., friction, compliance, sensing noise). Real-robot validation would significantly strengthen the claims, particularly for the online adaptation mechanism.
- The system uses GPT-4o for both VLM and LLM roles. Demonstrating the approach with a smaller, open-source model would improve reproducibility and show generality.
- Showing prompts used for LLM cost function generation and online adaptation (likely in the appendix, stripped by the parser) would help reproducibility.

## Removed Points

These points were flagged by reviewers but are removed from the main review with justification:

- **"Unified VLM confounded because it likely discards FoundationPose"** — REMOVED. The paper clearly separates these as two distinct ablations (lines 243, 324). "CoRAL (w/o Pose Tracking)" explicitly removes FoundationPose and gets different results (9/10 on T2) from "CoRAL (Unified VLM)" (2/10 on T2). The Unified VLM merges VLM (perception of physical parameters) and LLM (planning) roles while presumably retaining FoundationPose. The critic's claim is factually incorrect.

- **"Missing implementation details (prompts, output parsing, etc.)"** — REMOVED per hard rules about missing appendix content stripped by the parser.

- **"Explainability claim unverifiable"** — REMOVED per hard rules about missing appendix content stripped by the parser.

- **"Zero-shot claim contradictory with memory"** — REMOVED. The paper uses "zero-shot" to mean no task-specific fine-tuning, which is standard usage. Memory is for cross-episode experience reuse.

- **"Missing comparison to ThinkAct"** — REMOVED. The paper mentions ThinkAct in Related Work but this is a different paradigm (LLM generates reasoning steps for a learned policy, not for a controller). The paper's scope is LLM+planner integration, which it already benchmarks against human-designed cost functions.

- **"Simulation only"** — MOVED to Nice-to-Haves. Simulation evaluation is standard for the initial presentation of a new framework, but real-robot validation would strengthen the claims.

- **"Formatting/style nitpicks and typo concerns"** — REMOVED per hard rules.

## Novel Insights

Beyond the paper's own contributions, the most informative pattern across the reviews is that the paper's claimed strength (modular role separation) and its main weakness (experimental gaps) stem from the same architectural choice: by decomposing perception, reasoning, and control into distinct modules, the paper enables clean ablations that clearly identify which components matter, but this same modularity makes the system especially sensitive to any single module's failure (as seen in the Unified VLM and w/o Pose Tracking ablations both crashing performance). This suggests a fundamental tension in the neuro-symbolic approach: modularity buys explainability and targeted debuggability at the cost of brittleness and a larger hypothesis space to validate. The second interesting observation is that the LLM-as-cost-function-designer approach has a natural advantage over end-to-end VLAs on contact-rich tasks that involve simple-but-force-sensitive physics (pushing, flipping) — but the advantage comes at the cost of high variance (2/10 to 4/10 on T1) even within a single task configuration, suggesting the method is not yet reliable enough for deployment.

## Suggestions

1. Resolve the Figure 4 discrepancy immediately. Clarify what the figure shows (planning world estimates vs. evaluation world values), reconcile the axis labels with the text's stated ground truth of 0.1 kg, and provide a corrected figure or text. If the adaptation did not actually converge close to 0.1 kg, revise the claim accordingly.

2. Add at least one comparison to IMPACT or VLMPC — even if implemented approximately in the same simulation environment — or clearly justify why such a comparison is infeasible.

3. Clarify the memory evaluation protocol: are the "with memory" results from a sequential run where memory accumulates during evaluation? If so, report the per-trial progression or use a pre-populated memory from a held-out set.

4. Report confidence intervals or standard deviations across trials, or at minimum provide per-trial data.

5. Provide the LLM prompts used for cost function generation, contact strategy formulation, and online adaptation (either in the main text or appendix).

## Score and Decision

### Calibration Anchors

| Anchor | Avg Score | Comparison |
|--------|-----------|------------|
| NavFoM (kkBOIsrCXh.md) | 8.00 (Accept Poster) | Stronger paper with real-world deployment, more baselines, cleaner empirical story. CoRAL is comparable in novelty but weaker in execution. |
| VLM4VLA (tc2UsBeODW.md) | 7.00 (Accept Poster) | Cleaner experimental methodology with broader model coverage. CoRAL has more novel contribution (LLM cost function design) but weaker validation. |
| Semantic World Models (KfaZaYYCvt.md) | 5.00 (Reject) | Both have novel framing but simulation-only evaluation and missing baselines. CoRAL's practical contribution to contact-rich tasks is stronger, but SWM's framing is cleaner. |
| VLA-in-the-Loop (aT4LG8c6DE.md) | 5.00 (Reject) | Similar tier: interesting idea with execution gaps. CoRAL has better ablations but worse flagship experiment issue (Figure 4). |
| BiNoMaP (4jcnded6fA.md) | 5.33 (Reject) | Contact-rich manipulation paper. CoRAL has more novel architecture but similar simulation-only limitation. |
| LLM-guided MIP (zHexNab8uH.md) | 2.50 (Reject) | Much weaker: toy tasks, overclaimed novelty. CoRAL's experimental validation, while imperfect, is substantially stronger. |
| GRACE (SESeW4EvPd.md) | 1.50 (Reject) | Over-engineered pipeline with hand-crafted components. CoRAL's LLM-driven approach is more flexible and scalable. |

### Score Rationale

The paper presents a genuinely novel contribution — LLM-generated cost functions and contact strategies for MPPI — and provides meaningful ablations that validate the architectural choices. On the hardest contact-rich tasks, CoRAL succeeds where fine-tuned VLA baselines completely fail. However, the experimental validation has two serious issues. First, the Figure 4 parameter adaptation demonstration contradicts its own text: the claim of convergence to the true mass (0.1 kg) is unsupported by the figure as described, which undermines a core claim of the paper. Second, the most relevant prior work (IMPACT, VLMPC) is discussed but never compared against, making it impossible to assess the paper's contribution relative to its own paradigm. Combined with the unclear memory evaluation protocol and lack of statistical variance, these issues prevent acceptance in the current form.

The core ideas warrant further development, but the experimental presentation needs substantial revision before the paper can be evaluated fairly.

MY FINAL SCORE: <pineapple>4.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>