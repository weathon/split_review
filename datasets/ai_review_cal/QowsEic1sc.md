- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6
Now I have all the information I need. Let me compile the final consolidated review.

## Summary

This paper proposes LCSC (Linear Combination of Saved Checkpoints), a method that uses evolutionary search to find optimal linear combinations of saved weight checkpoints from diffusion/consistency model training. The key innovation is allowing coefficients to be negative (going outside the convex hull of checkpoints), which standard averaging methods like EMA cannot do. The paper demonstrates two use cases: (1) reducing training cost by training fewer iterations or with smaller batch sizes and then combining checkpoints to match fully-trained model quality, and (2) enhancing pre-trained models to improve quality or reduce inference steps. Results include 23× training speedup on CIFAR-10 CD and reducing DM inference from 15 to 9 NFE while maintaining quality.

## Strengths

- **Impressive and well-documented training speedups**: Table 1 (CIFAR-10 CD) shows LCSC with 100K iterations and batch size 128 achieves FID 3.34 vs. 3.65 for the fully trained 800K/512 model, a 23× speedup that includes search cost. Similar 15× speedup is shown on ImageNet-64 CD. These are substantial, practically meaningful results.

- **Landscape analysis demonstrating sub-optimality of EMA**: Figure 2 visualizes the 2D metric landscape spanned by three training checkpoints, showing that optimal model weights lie outside the convex hull. The analysis extends to three EMA checkpoints, showing that even the best EMA rate cannot replicate the combination of multiple EMA checkpoints. This is a clean, compelling visual motivation for the method.

- **Generalization across multiple metrics, settings, and model types**: Improvements are consistent across FID, IS, Precision, and Recall (Tables 1–3), and the method works for both CD and CT variants of CMs as well as DMs on both CIFAR-10 and ImageNet-64. This demonstrates the technique is not overfitted to a single metric or setting.

- **Gradient-free optimization of a non-differentiable objective**: The evolutionary search directly optimizes FID, which cannot be minimized via backpropagation. The hyperparameter study (Table 4) shows that increasing search iterations and sample size monotonically improves FID, demonstrating algorithmic reliability.

## Weaknesses

### Fatal

None.

### Major

- **Missing comparison to simpler averaging baselines (SWA, uniform averaging)**: The paper compares LCSC against EMA and a grid-searched EMA*, but does not include Stochastic Weight Averaging (Izmailov et al., 2018) or uniform averaging of the same set of checkpoints — both of which are mentioned in the related work (Section 2.3). While LCSC's advantage over EMA* (which already optimizes the EMA rate) provides strong evidence that going outside the convex hull helps, the missing comparison makes it harder to assess whether the *evolutionary search itself* is the source of improvement, or whether any more thoughtful averaging strategy would suffice. This does not threaten the core claim (negative coefficients are meaningfully beneficial), but it is the most significant gap in the experimental evaluation.

### Minor

- **Search cost not broken down in the main paper**: The paper states that "reported speedup results have been adjusted to include the search cost" and refers to \cref{app:exp_cost} (Section 5.2). However, no breakdown of training time vs. search time is provided in the main body. The headline speedup factors (e.g., 23×, 15×) would be more transparent and easier to evaluate if the main text included at least an approximate breakdown (e.g., "X hours training + Y hours search, compared to Z hours baseline").

- **FID overfitting concern partially but not fully addressed**: The search optimizes FID computed on a fixed set of 5K–10K samples with a fixed initial noise. While the paper uses a different noise set for final 50K evaluation and reports multiple metrics (IS, Precision, Recall), it does not analyze variance across different search noise seeds or sample sets. Given the known variance of FID estimates at small sample sizes, some quantification of search stability would strengthen the results.

- **Limited theoretical insight into why negative coefficients work**: The paper shows empirically that optimal combinations include negative coefficients (Section 6, Figure 5), but offers only speculative reasoning (high gradient variance, small basins) and explicitly defers a "more comprehensive theoretical investigation to future studies." This is transparent and acceptable for an empirical methods paper, but it limits the scientific contribution beyond the empirical results themselves.

### Trivial

None.

## Nice-to-Haves

- Compare against SWA or uniform averaging of checkpoints as an additional baseline, to more cleanly isolate the benefit of the evolutionary search procedure itself.
- Provide a brief wall-clock time breakdown in the main paper (training vs. search).
- Include variance analysis of the search across different random seeds or initialization noise.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"SGD cannot reach these basins is a conjecture"** — The paper provides a specific, testable 2D landscape visualization (Figure 2) showing optimal basins outside the convex hull of checkpoints. The claim is appropriately scoped (these regions "cannot be reliably reached" by SGD) and is supported by the empirical observation that the optimal points in the 2D slice are not visited by the training trajectory. The criticism overstates what is a reasonable empirical observation.

2. **"The claim about reducing NFE from 15 to 9 is not well supported"** — Table 3 (CIFAR-10 DM) shows LCSC at NFE=9 achieves FID 3.97 vs. EMA* at NFE=15 achieving FID 3.96 — essentially identical. The paper's claim of "maintaining generation quality" is accurate. The criticism was an overly precise reading of a 0.01 FID difference.

3. **"Missing ablation on window size"** — The paper states in Section 5.3 that "a more comprehensive study of the hyperparameters is provided in \cref{app:exp_hyper}." The main paper ablates interval, search iterations, and sample size. Window size is likely addressed in the (stripped) appendix.

4. **"Reproducibility details missing for population size, crossover/mutation rates"** — These are standard implementation details that belong in the appendix, not the main paper. The algorithm is clearly described (Algorithm 1) with its key hyperparameters (Epoch, M_CP, Iter) listed.

5. **"The comparison to gradient-based methods is speculative"** — The paper frames this as a discussion ("we offer some insights... defer a more comprehensive theoretical investigation to future studies," Section 6), not as a rigorous claim. The reviewer's framing treats the discussion as a weakness, but the paper is appropriately transparent about the limits of its analysis.

## Novel Insights

The most interesting observation from the reviews that extends beyond the paper's own contributions is the question of whether the found LCSC coefficients could be used to initialize continued training. If the model is trained further from the LCSC-found combination, does SGD maintain or even improve the FID? The paper discusses why SGD might not reach these basins (high gradient variance, small basins), but it does not test whether SGD *starting from* the basin can stay there. A positive result would strengthen the "SGD cannot reach these regions" claim; a negative result (SGD immediately leaves the basin) would deepen the mystery and point to interesting future work on optimization dynamics in DM/CM training.

## Suggestions

1. Add a comparison to SWA or uniform averaging of checkpoints as a baseline. Even a single experiment demonstrating that LCSC significantly outperforms these simpler averaging methods would strengthen the paper considerably.
2. Include a brief cost breakdown in the main text, e.g., "Search required X GPU-hours, bringing total cost to Y vs. baseline Z."
3. Run the search with 3–5 different random seeds to report mean and std of final FID, addressing the metric overfitting concern.
4. Consider adding an experiment where the LCSC-found combination is used as initialization for further training, to test whether SGD can maintain the found basin.

---
