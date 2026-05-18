Now I have all the information I need. Let me construct the final review.

## Summary

ADAPT proposes a method for achieving heterogeneous context lengths across layers in vision-language prompt tuning by iteratively pruning continuous prompt tokens based on saliency scores (Snip, gradient norm, l2-norm). The method is evaluated on CLIP across 11 downstream datasets, improving average accuracy from the best baseline's 79.83% to 81.70%, with per-dataset gains up to 9.63% (Aircraft). A key design choice is inserting prompts only into key/value (not query) computations, which naturally supports varying context lengths and maintains low FLOPs.

## Strengths

1. **Strong and consistent empirical gains across diverse datasets**: Table 1 (visible in text description) shows ADAPT improves over all baselines on 11 datasets, with the largest gains on fine-grained tasks (Aircraft +9.63%, EuroSAT +6.13%). The average improvement from 79.83% to 81.70% is credible and practically meaningful.

2. **Novel methodological contribution**: The paper is the first to apply iterative pruning of continuous prompts to automatically determine heterogeneous context lengths per layer and per branch (image vs. text). This removes the fixed-length constraint that limits prior deep prompting methods (VPT, MaPLe). The idea is clean and well-motivated.

3. **Parameter efficiency convincingly demonstrated**: Table 2 shows halving the total context budget (τ_target = 128 → 64) reduces trainable parameters by 52.37% with only 0.60% accuracy loss, and further reduction to 32 drops only 0.61%. This demonstrates that prompt redundancy is real and that pruning is an effective way to eliminate it.

4. **Robustness to scoring criterion**: Table 3 tests Snip, gradient norm, and l2-norm — even the simplest (l2-norm) achieves 81.48% vs. 81.70% for Snip, showing the method does not depend on a specific importance metric.

5. **Computational efficiency via K/V-only insertion**: Inserting prompts only for key/value (not query) naturally supports heterogeneous context lengths without altering attention output dimensions, yielding the second-lowest GFLOPs among compared methods.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Pruning procedure details are underspecified**: The accumulation period n_k and pruning rate r_p are named but their numerical values are not reported anywhere in the extracted text. The pruning frequency (every epoch? every N steps?) is also not stated. While the warmup duration (5 epochs) and termination condition (target budget reached) are specified, the missing values make it unnecessarily difficult to reproduce the exact pruning schedule. This is a concrete gap that should be addressed.

2. **No comparison to post-hoc (two-stage) pruning**: The method prunes tokens during training (after a warmup), which is a one-way process — pruned tokens are never reintroduced. The paper does not compare against a natural baseline: train with full prompts to convergence, then prune to the same budget post-hoc. Such a comparison would isolate whether the *dynamic* pruning schedule provides any benefit over static pruning after training, or whether the main value comes from the pruning itself regardless of timing. Without this control, the "adaptive" label is less strongly supported than it could be.

3. **No variance or error bars reported**: Results are reported as point estimates without standard deviations across runs. Given the few-shot setting (16-shot per the paper's context), accuracy can be noisy. Reporting variance would strengthen confidence in the reported gains.

### Trivial

1. **Text-equation inconsistency on prompt insertion**: Line 97 states "Adapt inserts continuous prompts only for **query and value**," but Equation (3) shows prompts inserted for K and V (key and value) while Q has no prompt. The text should say "key and value."

## Nice-to-Haves

- **Validate the motivating hypothesis directly**: The paper is motivated by surgical fine-tuning (different layers deviate differently depending on distribution shift type). It would strengthen the paper to check whether the learned pruning patterns (e.g., which layers retain more tokens) actually correlate with the predictions of surgical fine-tuning for specific dataset shift types — e.g., do input-level-shift datasets concentrate preserved tokens in early layers? This would turn the method from a black-box performance booster into an interpretable tool. However, this is not required for the paper's core claim (that heterogeneous lengths improve accuracy), which is already well-supported.

- **Seed sensitivity analysis for pruning patterns**: The paper could discuss whether different random seeds lead to different pruning patterns and whether final accuracy is robust to the specific pattern found.

## Removed Points

These points from the reviewers are flagged for removal; treat them with caution:

- **"Algorithm 1 referenced but not shown / pruning procedure is not specified enough"** (from Harsh Critic): The algorithm reference and experimental setup (Section 4.1) are stripped by the PDF parser. In the original submission these sections exist. The missing numerical values for n_k and r_p are retained as a Minor weakness above (verified from line 111), but the complaint about the algorithm being missing entirely is a parser artifact.

- **"Snip is usually applied at initialization, not during training"** (from Harsh Critic): This is an observation about Snip's typical usage, not a weakness of the paper. The paper addresses gradient noise via the accumulation period n_k.

- **"Why does omitting query prompts facilitate varying lengths?"** (from Harsh Critic): The paper explains this at lines 103-107 and line 130 — omitting prompts in Q means attention output sequence length is unchanged, naturally enabling heterogeneous input lengths.

- **"Missing experimental setup details (shots, epochs, LR)"** (from Harsh Critic): These details belong to Section 4.1 which is stripped by the parser. The paper states "following the setting of CoOp," which is standard practice.

- **"Per-dataset results not shown"** (from Harsh Critic): Table 1 exists in the original submission (stripped by parser).

- **"Strengths: addressed important problem / well-written"** (from Strength Finder): Generic/superficial strengths removed per filtering rules.

- **"Strengths: K/V-only prompt insertion reduces FLOPs"**: While factually correct, this is more of a design detail than an independent strength. The efficiency benefit is already reflected in the main strengths.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Provide numerical values for n_k (accumulation steps) and r_p (pruning rate), and state the pruning frequency explicitly (every epoch vs. every N steps) in a revision. This is the single most actionable fix.
2. Add a controlled experiment comparing ADAPT's dynamic pruning against a two-stage baseline (train full → prune post-hoc) to demonstrate the benefit of in-training pruning.
3. Report standard deviations over multiple seeds (3-5 runs) for the main results.
4. Correct the typo on line 97 ("query and value" → "key and value").
5. Consider adding an analysis (even brief) connecting the final pruning patterns to the distribution-shift type of each dataset, to deepen the link to the surgical fine-tuning motivation.

## Score and Decision

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>