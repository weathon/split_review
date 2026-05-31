## Summary
This paper introduces **BIRD-INTERACT**, an interactive, executable **text-to-SQL benchmark + environment** intended to better reflect real NLIDB usage by requiring multi-turn clarification, tool use, and error recovery. It couples each database with a **hierarchical knowledge base (HKB), metadata files, an executable DB environment, and a function-driven user simulator**, and evaluates models in two regimes: a scripted protocol (**c-Interact**) and a more agentic setting (**a-Interact**) (Abstract; Sec. 1 contributions paragraph around “A High-Fidelity Interactive Environment”).

## Strengths
- **Concrete benchmark/environment design beyond static multi-turn context**: The abstract explicitly specifies the coupled environment (HKB + metadata + executable DB + function-driven user simulator) and the intended capabilities (clarification, knowledge retrieval, execution-error recovery) rather than only providing dialog histories (Abstract; Sec. 1 “A High-Fidelity Interactive Environment” contribution statement).
- **Two evaluation regimes that plausibly test different deployment styles**: The benchmark defines both **c-Interact** (predefined conversational protocol) and **a-Interact** (agent autonomously decides when to query user simulator / explore DB) (Abstract).
- **Executable evaluation with CRUD coverage (in claim and framing)**: The task suite is stated to cover the “full CRUD spectrum … guarded by executable test cases” (Abstract). If implemented as described, this is a meaningful step beyond SELECT-only evaluation.

## Weaknesses

### Fatal
None.

### Major
- **Insufficient on-paper validation that the user simulator measures “realistic interaction” rather than “simulator-following”**. The paper’s core positioning is that it “restores … missing realism” via a “function-driven user simulator” (Abstract), and Sec. 1 emphasizes the simulator as “most critically” part of the environment and that it “can respond to clarification questions, provide feedback on proposed actions, and guide the model…” (Sec. 1 contributions paragraph). However, in the provided text extraction there is no clearly described *validation study* demonstrating robustness to simulator phrasing/policy changes, nor evidence that success cannot be achieved by exploiting simulator-specific regularities. For a benchmark whose key novelty is dynamic interaction mediated by a simulator, this missing validation directly weakens the central realism claim.
- **Ambiguity/inconsistency in benchmark scale reporting undermines confidence in the dataset specification**. The abstract states the suite is organized into **600 FULL** and **300 LITE** tasks (total 900) (Abstract), while the conclusion states “**totally 900 challenging tasks**” (Conclusion) and earlier repeatedly centers “600 tasks … up to 11,796 interactions” (Abstract). This is likely reconcilable (FULL+LITE=900), but the paper should be explicit about what counts as the benchmark total and how sets relate (disjoint vs overlapping, evaluation split usage). As written, the benchmark definition feels underspecified at a key “what exactly is being benchmarked?” level.

### Minor
- **The a-Interact setting is explicitly framed as “stress-mode” with strict budget constraints, and the paper defers “free-mode” as future work**. The limitations/future work section states: “our current *a*-Interact setting imposes strict budget constraints that create a stress-mode evaluation… we will conduct experiments in a free-mode setting without the budget-constrained awareness testing” (Sec. 8). This is a reasonable scope choice, but it should temper any broad conclusions about “agentic interaction” in general, since the reported a-Interact results may partially reflect performance under an intentionally constrained regime rather than typical agent behavior.

### Trivial
None.

## Nice-to-Haves
- Add explicit dataset/environment “specification tables” in the main text: e.g., distribution of interaction lengths per task (not just the “up to 11,796 interactions” aggregate), proportions of ambiguity types, and what fraction of tasks require user interaction vs can be solved without it. This would strengthen interpretability of what “interactive” means in practice for BIRD-INTERACT.

## Removed Points
These points are flagged to be removed, treat them with caution.
- **CRUD execution/statefulness pitfalls (reset semantics, equivalence classes, safety constraints)**: The abstract claims CRUD + executable test cases, but the provided extracted text does not include the detailed evaluation harness description needed to verify whether these pitfalls actually occur. Without concrete anchors (e.g., a section defining transaction boundaries/reset/isolation), this remains speculative in this extraction and is therefore removed rather than asserted as a weakness.
- **c-Interact vs a-Interact confounded comparison (token budgets/tools/stopping criteria)**: The abstract reports different success rates (8.67% vs 17.00%), but the extracted text available here does not include the full protocol definitions needed to verify confounds. Kept as a “watch item” but removed as a claimed weakness due to lack of verifiable on-page evidence in the provided text.

## Novel Insights
None beyond the paper’s own contributions.

## Suggestions
- Provide a **simulator robustness/validity** section in the main paper: at minimum, show (i) alternative simulator policies or paraphrase perturbations and (ii) whether model rankings/performance are stable; additionally report whether models can succeed by asking the simulator for overly-direct hints and what constraints prevent that (directly tied to the simulator’s central role described in Abstract and Sec. 1).
- Clarify the **benchmark cardinalities and splits** precisely (FULL vs LITE relationship, overlap/disjointness, and which set is used for headline reporting), to eliminate ambiguity between the abstract’s (600+300) and the conclusion’s “900 tasks”.

## Score and Decision
**Originality:** High for an interactive executable text-to-SQL benchmark centered on dynamic interaction.  
**Importance:** High—interactive NLIDB evaluation is a real gap beyond single-turn text-to-SQL.  
**Claims support:** Moderately supported in high-level description, but the key “restores realism” claim is not convincingly validated in the provided text.  
**Experimental soundness:** Hard to fully assess from this extraction; headline results suggest difficulty, but protocol/harness details and simulator validation are the main missing pieces.  
**Clarity:** Generally clear at the abstract/conceptual level; some dataset-size/specification ambiguity remains.  
**Community value:** Potentially high if simulator validity and benchmark specification are made airtight.

MY FINAL SCORE: <score>6.0</score>  
MY FINAL DECISION: <decision>Reject</decision>