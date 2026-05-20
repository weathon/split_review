Now I'll write the final consolidated review.

## Summary

This paper re-evaluates claims from prior work (Verma et al. 2018, Trivedi et al. 2021, Inala et al. 2020) that programmatic policies generalize better than neural policies in RL. Across three benchmarks (TORCS, KAREL, PARKING), the authors show that neural policies with appropriate modifications—a cautious reward function in TORCS and adding the previous action to the observation in KAREL—can match or exceed programmatic policies in OOD generalization. They propose an expressivity/discoverability framework to explain these results and identify a class of problems (those requiring instance-scaling memory) where programmatic representations have an inherent theoretical advantage, supported by a proof-of-concept using LLM-based program synthesis.

## Strengths

1. **Important re-evaluation that identifies specific confounds in influential prior work.** The paper demonstrates that in TORCS, reducing the speed-weighting coefficient β from 1.0 to 0.5 allows neural DRL to generalize to OOD tracks (76% success on G-TRACK-2, 69% on E-ROAD, Table 1), whereas prior work reported 0% with neural policies. In KAREL, augmenting the observation with the previous action enables a simple feedforward network to generalize to 100×100 grids where ConvNets and LSTMs fail (Table 2). These experiments pinpoint concrete experimental factors—reward shaping and observation design—that explain much of the reported programmatic advantage.

2. **Expressivity/discoverability framework (Definitions 2 and 3) that provides a principled lens for interpreting results.** The paper formalizes the conditions under which a representation enables OOD generalization: (i) the policy space must contain a generalizing solution (expressivity), and (ii) the search algorithm must be able to find it (discoverability). This framework cleanly explains the re-evaluation results (both representations are expressive, but discoverability was not equally controlled) and provides a vocabulary for discussing why certain problems require programmatic representations.

3. **Theoretically grounded identification of a problem class where programmatic representations have an inherent advantage.** The paper argues convincingly that tasks requiring working memory growing with input size (general pathfinding, nested subproblems) cannot be solved by fixed-capacity neural architectures because indexing |V| vertices already requires Ω(log|V|) bits. This provides a concrete, principled criterion beyond simple empirical comparison.

4. **Honest reporting of limitations.** The PARKING results (Table 3) are presented with balanced interpretation—the paper acknowledges the evidence is mixed and that neither representation reliably solves this domain.

## Weaknesses

### Major

- **Asymmetric comparison in the KAREL re-evaluation limits the discoverability claim.** The paper shows that PPO with a_{t-1} (last action added to observation) achieves perfect generalization on 100×100 STAIRCLIMBER, MAZE, TOPOFF, and FOURCORNER. However, it does not test whether LEAPS would also benefit from the same observation augmentation. The claim that the gap was due to "discoverability" rather than "expressivity" is a plausible hypothesis, but the experiment only shows that *some* neural baseline can close the gap—not that programmatic methods wouldn't also improve with better information. A symmetric test (LEAPS with and without a_{t-1}) would substantially strengthen this conclusion.

- **The constructive proof-of-concept does not connect to the programmatic RL methods being re-evaluated.** The paper argues that tasks requiring instance-scaling memory provide an inherent advantage for programmatic representations, and demonstrates this via FUNSEARCH (Romera-Paredes et al., 2024) with Qwen 3-Coder synthesizing a BFS implementation. However, FUNSEARCH is an LLM-based program synthesis system operating on Python, not the same restricted-DSL programmatic RL methods (NDPS, LEAPS, PSM) that were re-evaluated. The paper provides no evidence that NDPS, LEAPS, or PSM could discover BFS on a wall-sparse maze within their constrained search budgets and DSLs. This creates a disconnect between the critical and constructive halves of the paper: the re-evaluation shows that neural networks are sufficient for the existing benchmarks, and the constructive argument says other benchmarks would favor programmatic methods, but those benchmarks are not tested with the methods in question.

### Minor

- **The TORCS reward comparison is not fully controlled.** The paper changes β from 1.0 to 0.5 for the neural DRL agent and compares against NDPS results from the original paper (trained with β=1.0). The paper argues this is acceptable because β controls an *intrinsic* reward used during learning, not the evaluation metric (lap time). While this argument has merit—the evaluation is on lap time and crash rate, not the reward itself—the comparison is asymmetric: we do not know what NDPS would achieve with β=0.5 (it might generalize even better, or its advantage might persist). The claim that the programmatic advantage was "caused by" the reward function would be stronger if both methods were tested at both β settings. As presented, the experiment shows that neural policies *can* generalize with a cautious reward, but does not fully isolate the causal mechanism.

- **Seed filtering in TORCS creates a mild asymmetry.** The paper reports results for DRL (β=0.5) only for seeds that learned to complete laps (13/30 for G-TRACK-1, 4/15 for AALBORG). The NDPS results are over 3 seeds that "always worked" from the original paper. While the fractions are reported (Table 1 caption), the filtering makes the comparison less clean—particularly the 4/15 success rate on AALBORG, which means the test generalization results (100%) are based on a small, selected subset.

- **The PARKING results are largely inconclusive for distinguishing representations.** PSM has lower test success rate (0.16 vs 0.18 for DQN) but a smaller train-test gap (0.10 vs 0.68). The paper honestly acknowledges this, but the resulting lack of a clear signal means this benchmark does not add much weight to either side of the argument.

### Trivial

- None of note.

## Nice-to-Haves

- **A controlled TORCS experiment testing NDPS with β=0.5** (or, alternatively, neural DRL with β=1.0 but constrained to lower speed) would strengthen the causal claim about the reward function.
- **Analysis of what the neural policies actually learn in KAREL**—e.g., does the "PPO with a_{t-1}" policy implement wall-following or some other strategy? This would strengthen the discoverability argument.
- **An RL experiment using NDPS/LEAPS/PSM on a task requiring instance-scaling memory** (e.g., a simple pathfinding domain with sparse walls where wall-following fails) would connect the constructive half to the re-evaluated methods. This would substantially elevate the paper's contribution.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"The paper does not show the benchmarks require instance-scaling memory"** (Critic Issue 3): This misunderstands the paper. The entire point of the re-evaluation is that the existing benchmarks *do not* require such memory, which is precisely why neural policies can match programmatic ones. The paper then separately argues about problems that *do* require such memory. This criticism reflects a misreading.

- **"No variance estimates or statistical tests for TORCS"**: The paper reports average lap times and success fractions with the number of seeds, which is standard practice for this setting. The NDPS results are taken from the original paper (3 seeds). While more seeds would be better, the practice is not a weakness unique to this paper.

- **"No discussion of FUNSEARCH computational cost"**: This is a reasonable suggestion but not a weakness—FUNSEARCH is presented as a proof-of-concept, not a practical RL method.

- **Formatting/style nitpicks and missing related work references**: Removed per policy.

## Novel Insights

The most novel insight from the reviews is that the paper's two halves (re-evaluation and constructive) operate at different levels of analysis: the re-evaluation uses the same methods as prior work and finds they under-deliver on their promises, while the constructive argument shifts to a different technology (LLM synthesis) to make a theoretical point about expressivity. This structural gap means the paper tells a convincing story about what *doesn't* make programmatic policies special (expressivity on constant-memory tasks) but a less convincing story about what *does* (expressivity on growing-memory tasks). The intersection of these two narratives—the class of problems where existing programmatic RL methods would succeed and existing neural methods would provably fail—remains empirically unpopulated.

## Suggestions

1. **Run a controlled TORCS experiment training NDPS with β=0.5** (reusing the original codebase). This is the single highest-leverage addition: if the gap closes, the reward-confound claim is validated; if NDPS still generalizes better, the paper needs a different explanation.

2. **Test LEAPS with the a_{t-1} augmentation on KAREL** to make the comparison symmetric. If LEAPS also benefits, the discoverability claim weakens; if LEAPS does not benefit (or if its performance drops), the claim strengthens.

3. **Either remove the FUNSEARCH proof-of-concept or connect it concretely to programmatic RL.** Option A: State clearly that the proof-of-concept uses a different technology and is not intended to validate NDPS/LEAPS/PSM. Option B: Test one of these methods on the wall-sparse KAREL maze to show whether the theoretical expressivity advantage translates to a practical one within the programmatic RL paradigm.

## Calibration Anchors

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| RL Grokking Recipe | CJJ8VxOWbG.md | 5.20 (8,8,2,4,4) | 1, 2 | Similar tier — both have clear contributions and some experimental concerns. Current paper is more focused on identifying confounds in prior work. |
| MLES | OHFNJoNtjW.md | 4.00 (6,4,4,2) | 1 | Current paper is stronger — broader scope (3 benchmarks + theory vs 2 environments) and more novel contribution. |
| BYOL-γ | FkeURAdA0h.md | 4.50 (4,6,4,4) | 2 | Current paper has more clearly defined contribution and less theoretical confusion. |
| TD Stitching | LMD8ndMqs0.md | 5.50 (6,4,6,6) | 2 | Rejected due to experimental methodology concerns. Current paper has cleaner experiments but a similar level of methodological concern about asymmetric comparisons. |
| EXPO | aFjSjkB6CV.md | 6.50 (6,4,8,8) | 2 | Stronger empirical validation (12 tasks, comprehensive ablations). Current paper has less comprehensive experiments. |
| Debunk SFT Generalization | HwcwLBATQT.md | 3.00 (4,2,4,2) | 1 | Weaker — less empirical grounding and narrower scope. Current paper is clearly better. |
| LLM Policy Diffusion | eM8Db7ukSB.md | 2.50 (2,4,2,2) | 1 | Weaker — limited experimental support. Current paper is substantially stronger. |

**Round 1 bracket**: Between 3.5 and 7.5 (clearly above weak anchors at 2.5–3.3, clearly below strong anchors at 8.0).  
**Round 2 narrowing**: Compared against anchors at 4.00–6.50. The paper sits near the 5.0–5.5 range: its contribution is clearer than the 4.00/4.50 papers but its experimental evidence is less comprehensive than the 6.50 paper. The methodological concerns (asymmetric comparisons) are real but not fatal, placing it below the rejected 5.50 paper on methodological rigor but above it on contribution clarity.

**Final Score**: 5.0 — The paper makes a genuine contribution by identifying confounds in influential prior work and providing a useful theoretical framework. However, the re-evaluation experiments have asymmetric comparisons that limit the strength of the causal claims, and the constructive half does not connect to the same programmatic RL methods. The paper would be significantly stronger with controlled comparisons and an RL experiment on a memory-scaling task.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>