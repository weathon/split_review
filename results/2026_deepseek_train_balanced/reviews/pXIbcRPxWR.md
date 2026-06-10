Here is the consolidated final review:

---

## Summary

This paper proposes a conceptual decomposition of Chain-of-Thought (CoT) reasoning into two distinct search problems — "prompt space" (finding the correct step template / algorithm) and "answer space" (searching for the solution given that template). The authors argue that task-specific human supervision is essential for correctly navigating the prompt space, and present experiments on structured reasoning tasks (Regular, Context-Free, Context-Sensitive) to demonstrate the impact of step-template quality on CoT performance.

## Strengths

- **Novel conceptual decomposition of CoT search into prompt space and answer space (Section 3).** This goes beyond prior theoretical work on CoT's computability (Li et al., 2024; Zhang et al., 2024) by partitioning the solution process into two components and explicitly distinguishing the problem of finding the right algorithm (step template) from the problem of executing it. This framing provides a useful vocabulary for discussing why methods that only improve answer-space navigation (ToT, GoT) cannot fix a wrong step template.

- **Controlled experiments that isolate step-template quality as an independent variable (Table 1).** The contrast between correct supervision (CR), incorrect supervision (IN), and unsupervised CoT across 10 tasks cleanly demonstrates that incorrect step templates can degrade performance to near-zero on several tasks (e.g., Stack Manipulation: 0.96 → 0.00; Odds First: 0.92 → 0.00; Addition: 0.88 → 0.00). This provides controlled evidence for the causal role of template selection quality.

- **Empirical evidence that ToT and GoT cannot fully compensate for template errors (Table 2).** Even with Tree-of-Thought or Graph-of-Thought, unsupervised CoT underperforms correctly supervised CoT on most tasks (e.g., Stack Manipulation: ToT 0.36, GoT 0.72 vs Supervised CoT 0.96; Sorting: ToT 0.66, GoT 0.80 vs Supervised CoT 0.90). This concretely supports the claim that answer-space search methods address a different bottleneck.

- **Clear mechanistic exposition of how CoT enables recurrence in Transformers (Section 2).** The h_t → (o_1,...,o_k) → h_{t+1} cycle is well-explained with the chess simulation example, bridging prior theoretical results with the practical point that discretization can only extract partial information — motivating why step-template selection matters.

## Weaknesses

### Major

1. **The combinatorial formalism C(m,s) = m!/(s!(m−s)!) (line 81) is decorative, not operationalized.** The paper defines m as information bits in the hidden state (suggesting m ∝ d, the hidden dimension) and s as bits extracted per step, but never attempts to measure or estimate these quantities in any experiment. No task's search space size is computed, the formula is never used to predict or explain any empirical result, and the paper itself acknowledges (line 86) that "step template search is not entirely random" and uses heuristics "which significantly reduces the search complexity." The framework would lose nothing of substance if this formula were removed. This matters because the appearance of formal rigor (the C(m,s) formula) is not backed by any actual measurement or prediction.

2. **Missing critical baselines weaken the experimental evaluation.** (a) No comparison with few-shot CoT — the paper's "unsupervised" baseline is the bare prompt "think step by step" (zero-shot CoT), but standard practice already uses task-specific few-shot examples that implicitly define step templates. Few-shot CoT would be a more informative and fairer baseline. (b) No supervised variants of ToT or GoT are tested in Table 2 — the comparison pits correctly-supervised CoT against *unsupervised* ToT/GoT, making the comparison asymmetric. Without testing whether adding supervision to ToT/GoT further improves them, the claim that these methods "cannot compensate" for template errors is incomplete.

3. **Experimental methodology lacks sufficient detail for reproducibility or full evaluation.** The paper does not specify the number of test instances per task, the temperature setting for GPT-4-o, the exact evaluation metric (exact match? rubric-based?), or the methodology used to compute the "hit ratio" in Figure 4 — specifically, what constitutes "deriving the correct step template" and how this was judged. These omissions prevent independent verification and full interpretation of the results.

### Minor

4. **The paper overclaims novelty.** The statement "Our work is the first of its kind to focus on prompt space exploration" (line 32) is overstated given the extensive literature on prompt optimization, automated prompt search (e.g., Gao et al., Zhou et al., Pryzant et al.), and structured prompt engineering for reasoning tasks. The paper's specific angle (decomposing search into prompt vs answer space) is novel, but "prompt space exploration" broadly construed is not new.

5. **Unsupervised CoT performs fairly well on most tasks, tempering the "essential" narrative.** In Table 1, unsupervised CoT achieves 0.78–0.96 on 8 of 10 tasks (all except Multiplication at 0.14 and Sorting at 0.36). The improvement from unsupervised to correctly supervised CoT ranges from 0.04 (Modular Arithmetic, Parity, Addition) to 0.54 (Sorting), with most gaps being small to moderate. The paper acknowledges this (line 212: "the model makes mistakes in finding the optimal step template less frequently") but does not fully reconcile this with the strong claim in the abstract that "task-specific supervision is essential" — the data suggest it is helpful but far from essential on simpler tasks.

6. **The "one-prompt-for-all" characterization of CoT variants is reductive.** The paper frames vanilla CoT, ToT, and GoT as using a generic "think step by step" prompt. In practice, few-shot CoT already provides task-specific examples that implicitly define the step template, and prompt engineering for reasoning tasks routinely involves task-specific step design. The paper does not engage with these existing practices.

### Trivial

- The paper uses "discritization" (line 63) instead of "discretization" (appears in the h_t → (o_1,...,o_k) → h_{t+1} diagram description).

## Nice-to-Haves

- An analysis of *why* Multiplication (0.14 unsupervised) and Sorting (0.36 unsupervised) are specifically hard for unsupervised CoT — comparing the model's self-generated template to the correct one would provide much stronger evidence for the paper's thesis than the CR vs IN comparison alone.
- A more systematic discussion of when to supervise vs. when to trust the model's heuristics, beyond the brief guidance in Section 6.2.

## Removed Points

These points appeared in the input reviews but are removed from the main assessment with justification:

- **"IN Supervised condition is a tautology"** — Removed. The paper explicitly states (line 212) that it introduced this condition because the natural gap was hard to observe, making it a legitimate controlled experiment to isolate the effects of template errors. Demonstrating that bad templates cause bad performance is a valid sanity check, not a tautology.
- **"Paper does not discuss the cost of supervision"** — Removed. Line 257 explicitly states "this supervision adds a substantial workload."
- **"Advice on 'when to supervise' contradicts the paper's thesis"** — Removed. The advice to "avoid providing supervision unless you are reasonably confident" is nuanced practical guidance, not a contradiction. The paper's thesis is that supervision is *important*, not that it should always be used.
- **"Theoretical framework does not connect to TC⁰/computability argument"** — Removed. The paper explicitly positions the computability discussion (Section 1) as background motivation, stating that "the gap between 'can solve in principle' and 'actually solves in practice' is real" (paraphrased from the paper's own framing). The theoretical apparatus is used to motivate *why* template selection matters (limited information extraction from h), not to prove the need for supervision.
- **Formatting, style, and trivial reproducibility nitpicks** — Removed per filtering rules. Specific requests about undisclosed hyperparameters, training logs, or parser artifacts are not author errors.
- **"Claim about ToT providing little benefit is inconsistent with Table 2"** — Weakened. The paper's statement that "ToT provides little benefit, as the tasks typically have only one path to the solution" is a reasonable characterization — ToT improves on 4-5 tasks, harms performance on several others (e.g., Stack Manipulation: 0.36 vs 0.92), and generally doesn't match supervised CoT performance. The statement is defensible when read in context.

## Novel Insights

The most distinctive observation in the reviews is the disconnect between the paper's theoretical framing and experimental design: the paper's strongest evidence comes from the IN Supervised condition (deliberately chosen incorrect templates), but the claim most readers would care about — whether and when the model *naturally* selects suboptimal templates that supervision can fix — is only weakly supported by the unsupervised CoT results, which show fairly strong performance on most tasks. This gap between "can bad templates hurt?" (clearly yes) and "does the model pick bad templates?" (sometimes, mostly on harder tasks) is not squarely addressed.

## Suggestions

1. Add a few-shot CoT baseline (with 2-3 task-specific examples but no explicit step-by-step instructions) to contextualize the "unsupervised vs. supervised" comparison.
2. Test supervised variants of ToT and GoT to determine whether the benefits of supervision and improved answer-space search are additive.
3. Either operationalize the C(m,s) formalism (e.g., estimate m and s for specific tasks and show that search space size correlates with performance) or drop the formula and treat the framework as purely conceptual.
4. Provide the methodological details needed for reproducibility: number of instances per task, temperature, evaluation metric, and the hit-ratio computation methodology.
5. Conduct a qualitative error analysis of the Multiplication and Sorting cases — show the model's self-generated template, explain what information it extracts incorrectly, and demonstrate how supervision corrects it.

## Score and Decision

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>