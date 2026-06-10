Here is the final consolidated review:

## Summary

The paper proposes Model Swarms, applying Particle Swarm Optimization (PSO) to the weight space of LLM experts. Multiple expert models (particles) iteratively update their weights guided by personal best, global best, and global worst positions to optimize a utility function representing an adaptation objective. The method is evaluated across four settings (single-task, multi-task domain, reward model alignment, human interest) and consistently outperforms 12 model composition baselines. Additional analyses examine correctness emergence, the role of diversity, the "diamond in the rough" phenomenon, and computational efficiency.

## Strengths

- **Novel and well-specified PSO formulation for LLM weight-space search.** The adaptation of PSO to model weight spaces is clearly described in Algorithm 1 (lines 40–49), with explicit velocity components for inertia, cognitive search, social influence, and repulsion from the global worst. The method is tuning-free in the sense that it only requires a utility function and does not need supervised fine-tuning data or pre-existing compositional rules. This distinguishes it meaningfully from both learn-to-fuse approaches and static/dynamic model arithmetic.

- **Broad evaluation across four distinct adaptation objectives with consistent improvements.** The paper evaluates on single-task (9 datasets, Table 1), multi-task domain (8 tasks across 4 domains, Table 2), reward model alignment (Table 4), and human evaluation (16 topics, Table 3). Model Swarms outperforms all 12 baselines across all 9 single-task datasets and all 8 multi-task tasks, with up to 29.7% improvement on GSM8k. The breadth — going beyond standard benchmarks to multi-task domains, conflicting preference steerability, and human evaluation — is more extensive than most model composition papers.

- **Controlled diversity experiment providing causal evidence for the role of expert diversity.** The paper systematically varies the number of distinct initial experts (1×10, 2×5, 5×2, 10×1) while keeping total swarm size constant (Figure 4, line 108). This shows a monotonic 35.3% improvement from least to most diverse, providing controlled causal evidence (not just correlation) that diverse initial checkpoints drive success.

- **"Diamond in the Rough" and "Collaboration of Weak > Strong" analyses.** The paper shows that 56.9% of ending-best particles started in the bottom half of initial experts (Figure 3, line 98–106) and that removing the top-1 expert still yields a swarm that beats it by 35.4% on average (Figure 6, line 128). These are genuine, non-obvious findings that go beyond simple ablations and directly support the claim that the method produces new value from weak experts.

- **Practical efficiency analysis (Dropout-K/N).** The paper proposes and evaluates dropout strategies that skip utility evaluations, achieving up to 80% computational speedup with only 6.0% average performance drop (Figure 9, line 149). This provides practical guidance for deployment that most model merging papers lack.

- **Token Swarms extension for cross-architecture composition.** The prototype (Figure 5, lines 110–117) operates on token probability distributions rather than weights, enabling composition across different base architectures (GEMMA-7B and MISTRAL-7B). All 8 experts improved regardless of architecture, with global best increasing 5.7% and 11.9%.

## Weaknesses

### Fatal

None.

### Major

1. **Utility function data source is not disambiguated.** The paper optimizes a utility function *f* evaluated on data instances, repeatedly emphasizing that it works with "as few as 200 examples" (abstract, line 21). However, it never explicitly states whether these examples come from a held-out validation set or the test set. For the reward model setting, the paper separately mentions "validation and test set instructions" (line 70), suggesting proper separation exists. But for the single-task experiments (Table 1) — where the headline results of up to 29.7% improvement are reported — no such distinction is made. If *f* is evaluated on test examples during the search while baselines do not see the test distribution, the comparison would be fundamentally unfair. This is a critical missing detail that must be clarified for the core results to be interpretable.

2. **No comparison to standard fine-tuning (e.g., LoRA).** The paper compares against 12 model composition baselines but omits the most natural baseline for low-data LLM adaptation: fine-tuning the best starting expert on the same 200 examples (e.g., with LoRA). Model Swarms is more complex and computationally expensive than fine-tuning (it maintains and evaluates multiple full-size model copies across iterations). If fine-tuning on 200 examples matches or exceeds Model Swarms' performance, the practical value of the method is substantially diminished. This omission is especially conspicuous given the paper's framing as a "tuning-free model adaptation" approach (abstract).

3. **Human interest evaluation compares only to pre-swarm experts, not to baselines.** In the human evaluation (Table 3, lines 66, 83), post-swarm experts are compared only to their pre-swarm counterparts ("pre- and post-MODEL SWARMS"). A win rate of 70.8% against the *same model before optimization* is a weak comparison: any method that doesn't degrade performance could achieve this. A proper evaluation would compare against an independently fine-tuned model or a model merging baseline. Without this, the human evaluation does not differentiate Model Swarms from a trivial "do no harm" baseline.

### Minor

4. **The PPO/DPO comparison is asymmetric and should be reframed.** In the reward model experiments (Table 4, line 70), Model Swarms directly optimizes the reward model score (the evaluation metric) as its utility function *f*, while PPO and DPO optimize a different objective (preference likelihood). This means the evaluation metric *is* the optimization target for Model Swarms but not for PPO/DPO — a structural advantage. The paper acknowledges the "low-data regime" framing but does not discuss this asymmetry. The comparison would be more informative if presented as a demonstration of data efficiency rather than as head-to-head superiority over alignment methods.

5. **"Emergence" framing is overstated relative to the evidence.** The paper measures C-emerge (lines 90–96), showing that 36.0%–53.5% of previously unsolvable problems become solvable by at least one expert after Model Swarms — a genuine and interesting finding. However, the paper frames this as discovering "new capabilities and skills" and "previously unseen capabilities in initial checkpoints" (abstract, Figure 2 caption). The mechanism is iterative weight-space exploration and interpolation, which is related to model merging effects well-documented in the literature (model soups, Weighted Averaging, TIES-Merging, etc.). While the finding is noteworthy, the "new skills" language implies a stronger claim than the evidence supports.

6. **"Weak-to-strong" terminology is borrowed from a conceptually unrelated setting.** The paper cites Burns et al. (2024) and uses "weak-to-strong transition" (lines 106, 128, 165) to describe weak models collaborating via PSO to beat a strong one. Burns et al.'s weak-to-strong generalization concerns using a weak model's *supervision* to elicit a strong model's *capabilities* — a fundamentally different mechanism. The paper's finding (weak models can collectively outperform a stronger one through weight-space search) is independently interesting and does not benefit from the borrowed terminology, which may confuse readers about the connection.

7. **Statistical significance is absent from the main results tables.** Tables 1 and 2 report single numbers without variance, confidence intervals, or error bars. Figure 7 (line 123) does show variance across runs for one setting, reporting a 73% success rate against the best baseline — meaning the method *fails* to beat baselines 27% of the time, a caveat not discussed in the main results text. This practice should be extended to all main experimental results, especially since many claimed improvements are modest (e.g., 4.9% on knowledge tasks, 5.7% multi-task average).

8. **Absolute computational cost is not reported.** The dropout acceleration analysis (Figure 9, line 149) reports relative speedups but no absolute GPU-hours, wall-clock time, or FLOPs. Without this information, it is impossible to assess whether the method is practical for typical use cases. The method maintains and evaluates multiple full-size model copies across iterations, which could be substantially more expensive than simple model merging or fine-tuning.

### Trivial

None.

## Nice-to-Haves

- The paper's ***populate()* step** (line 43, "pairwise interpolation") could be specified more precisely: is it all pairs, random pairs, weighted or unweighted interpolation?
- The **velocity normalization** across layers with orders-of-magnitude differences in parameter values (e.g., embedding layers vs. late transformer layers) could be discussed.
- Disclosure of **specific hyperparameter values** chosen for the swarm (inertia, coefficients, step schedule) would aid reproducibility — these were likely in the stripped Section 3.

## Removed Points

These points were flagged by reviewers but are not included as weaknesses in the final review:

1. **Missing experimental setup (Section 3) / missing baseline list:** The paper references "Section 3" twice (lines 29, 108), and the extracted text lacks this section entirely. Given that the parser strips sections from all papers, this content likely exists in the original submission. The experimental details, baseline enumeration, and hyperparameter settings were presumably provided there. These are parser artifacts, not author omissions.

2. **"Any weight vector is a convex combination of initial experts' weights" (emergence criticism):** After the first iteration of Algorithm 1, particle positions are updated via velocity-corrected steps involving personal bests, global bests, and random factors. These are *not* simple convex combinations of initial expert weights — the iterative dynamics can explore outside the convex hull. The broader point about overstated framing is valid (see Minor #5), but the specific convex-combination claim is technically incorrect.

3. **Reproducibility nitpicks about undisclosed hyperparameters or implementation trivialia:** These details were likely in the stripped Section 3 and are not flagged as author omissions.

## Novel Insights

The most novel observation emerging from the reviews is the tension between the paper's strong empirical results and the incomplete specification of the utility function's data source. If it turns out that Model Swarms genuinely works with 200 *held-out validation* examples and generalizes to separate test sets, that would be a clean, strong finding. If the utility function inadvertently sees test data during search, the results collapse. This binary — which only the authors can resolve — is the single factor that determines whether this paper is a solid contribution or has an unrecoverable flaw. The diversity experiment and diamond-in-the-rough analysis are independently valuable regardless, as they provide insights applicable to any weight-space composition method.

## Suggestions

1. **Clarify the utility function data split immediately** — state explicitly for each experimental setting whether *f* is computed on held-out validation data or test data. If validation data is used, report test set performance separately and confirm that the test set was never accessed during search.

2. **Add a LoRA fine-tuning baseline** on the same 200 examples used for Model Swarms, comparing both performance and computational cost. This is the most natural alternative to the proposed method and its absence leaves a significant gap in the evaluation.

3. **Reframe the PPO/DPO comparison** as a demonstration of data efficiency rather than a head-to-head competition, and explicitly discuss the asymmetry (Model Swarms optimizes the same metric it is evaluated on).

4. **Tone down the "emergence" and "new capabilities" language** — the C-emerge finding is interesting without this strong framing. Replace "new skills and capabilities" with more precise descriptions (e.g., "solving previously unanswerable questions through weight-space exploration").

5. **Report statistical significance** (variance, confidence intervals, or run counts) for the main results in Tables 1 and 2, and discuss the 27% failure rate shown in Figure 7 in the main text.

6. **Include a human evaluation against at least one strong baseline** (e.g., the best model merging method from Table 1/2) rather than only against the pre-swarm model.

7. **Report absolute computational cost** in GPU-hours or wall-clock time for a typical run, alongside the relative speedup from dropout strategies.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Reject</decision>