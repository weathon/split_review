Now let me produce the final consolidated review.

## Summary

InfoBatch proposes a dynamic data pruning framework that combines three components — soft random pruning of low-loss samples, gradient rescaling by $1/(1-r)$ to maintain unbiased gradient expectation, and annealing (full dataset in the final epochs) — to accelerate training while approximately preserving performance. The method achieves $O(1)$ per-sample time complexity (versus $O(\log N)$ for prior dynamic methods), is architecture-agnostic, and is validated across classification, semantic segmentation, diffusion, and instruction fine-tuning tasks.

## Strengths

- **Theoretical grounding for unbiased gradient expectation.** The derivation (Eqns. 6–11) shows that rescaling gradients by $\gamma_t(z)=1/(1-\mathcal{P}_t(z))$ makes the training objective a constant-rescaled version of the original objective. This formalizes a guarantee that prior dynamic pruning methods (UCB, $\epsilon$-greedy) lack, and connects directly to why InfoBatch maintains performance at moderate pruning ratios.

- **$O(1)$ per-sample complexity with concrete efficiency evidence.** By using the mean score as a pruning threshold instead of sorting, InfoBatch reduces dynamic pruning overhead from $O(\log N)$ to $O(1)$ per sample. The empirical evidence — 10 seconds overhead for 90 epochs of pruning on ImageNet-1K vs. substantially more for UCB — makes this practical advantage tangible.

- **Unusually broad task coverage.** The method is evaluated on classification (CIFAR-10/100, ImageNet-1K), semantic segmentation (ADE20K with 60% iterations), latent diffusion (FFHQ, 27% cost savings), and instruction fine-tuning (LLaMA, 20% cost savings). This breadth is rare among data pruning papers and genuinely supports the claim of architecture/task agnosticism.

- **Component-wise ablation validating each design choice.** The ablation (Tab. abl_res_anneal) isolates soft pruning, rescaling, and annealing, showing that rescaling provides the primary bias correction while annealing stabilizes variance. This decomposition directly supports the theoretical claims and demonstrates that all three components contribute.

- **Demonstrated compatibility with orthogonal acceleration methods.** InfoBatch combines with mixed-precision training, CutMix/MixUp, and large-batch optimizers (LARS/LAMB), achieving 1.67× further speedup when combined with large-batch training. This "plug-and-play" compatibility is rarely validated in data pruning papers.

## Weaknesses

### Major

- **The "lossless" claim is not operationally defined and lacks statistical support.** The paper uses "lossless" as its headline claim (appearing 10+ times throughout) without ever defining what threshold qualifies as lossless, and without reporting any error bars, standard deviations, or multi-seed repetitions. On ADE20K, InfoBatch achieves mIoU 41.12% vs. the full-data baseline 40.7% — i.e., it *outperforms* full-data training. On FFHQ diffusion, FID is 7.70 vs. 7.83 — again better. These small differences are well within the range of random seed variation, but the paper presents them as straightforward "lossless" results. Without knowing the variance of the baseline or the method, the reader cannot assess whether the central claim is meaningful. This is the single most impactful weakness: the paper's core contribution cannot be properly evaluated.

### Minor

- **Score staleness may create a self-reinforcing pruning pattern.** Under the score update rule (Eqn. 4), pruned samples retain their old scores while only kept samples are updated to the current loss. Since low-loss samples are more likely to be pruned, their scores can become stale — staying artificially low because they are not updated — making them more likely to be pruned again. The annealing phase partially addresses this, but the paper does not analyze what fraction of samples are systematically pruned across epochs or whether the annealing is sufficient to overcome this feedback loop. This is a structural concern that would benefit from empirical investigation (e.g., tracking pruning overlap across epochs).

- **Ambiguous hyperparameter description for key datasets.** Line 210 states: "On CIFAR100, ImageNet-1K and ADE20K, a more aggressive r (0.75) is utilized for smaller loss samples (20%)." It is unclear whether this means 20% of the dataset receives a higher pruning probability, or the bottom 20% of low-loss samples get $r=0.75$, or something else. Since ImageNet-1K and ADE20K are two of the three main datasets where the headline results are demonstrated, and the paper also claims "With the same hyperparameters in most cases" (line 55), this ambiguity weakens confidence in the reported results.

- **Occasional outperformance of the full-data baseline is not discussed.** On ADE20K and FFHQ, InfoBatch numerically exceeds the full-data baseline. A data pruning method that improves over full training is either (a) within noise (requiring error bars to determine) or (b) a genuine phenomenon that merits explanation (e.g., rescaling low-loss samples acts as a form of importance weighting that improves learning on hard examples). The paper does neither — it simply presents these results as "lossless," which is uninformative in either case.

- **Variance introduced by gradient rescaling is acknowledged but not analyzed.** The theoretical derivation shows unbiasedness in expectation, but the gradient rescaling (amplifying updates from low-loss samples by $1/(1-r)$) increases per-step variance. The paper notes this qualitatively (lines 173, 252, 261) but does not bound or measure it. Since variance is the primary practical concern with such corrections, a formal or empirical analysis would strengthen the paper substantially.

### Trivial

None.

## Nice-to-Haves

- Multi-seed experiments (3–5 seeds) with error bars across all main results, plus an explicit operational threshold for "lossless" (e.g., "within one standard deviation of the baseline"). This is the single most impactful improvement the authors could make.
- An empirical analysis of which samples are pruned across epochs (overlap distribution), to address the staleness concern directly.
- A measurement or bound on gradient variance (e.g., plot of gradient norm variance over time for InfoBatch vs. full-data training).

## Removed Points

These points were considered but removed during consolidation:
- **"Gradient rescaling is standard importance sampling presented as novel"**: The paper presents the rescaling as part of its framework justification, not as a novel invention. The novelty lies in the combination (soft pruning + rescaling + annealing + O(1) threshold) and the overall system. Removed as a misreading.
- **"Criticism of Eqns. 9–10 transition"** and **"O(1) vs O(log N) complexity scaling"**: These are implementation details adequately justified for an empirical paper. Removed as overly technical nitpicks.
- **Speculative fatal claims about staleness**: The critic framed this as potentially fatal, but the paper has annealing and the claim depends on information not present. Demoted to Minor.
- **Several generic formatting-style criticisms**: Removed as parser artifacts or style nitpicks.

## Novel Insights

None beyond the paper's own contributions. The reviews primarily recapitulate what the paper states rather than revealing hidden strengths or overlooked implications. The interaction between score staleness (Eqn. 4) and the annealing phase is a tension worth exploring empirically, but neither the paper nor the reviews do so.

## Suggestions

1. **Operationalize "lossless."** Run all main experiments with at least 3 random seeds, report means and standard deviations, and pre-specify what difference counts as lossless (e.g., accuracy within one standard deviation of the full-data baseline). This is the minimum bar for a paper whose headline claim hinges on equivalence.
2. **Clarify the hyperparameter on line 210.** Rewrite the sentence to specify exactly what "a more aggressive r (0.75) is utilized for smaller loss samples (20%)" means — e.g., "Among the bottom 50% of samples below the mean loss, the bottom 20% are pruned with probability $r=0.75$ while the remainder are pruned with $r=0.5$."
3. **Discuss the outperformance cases.** If the ADE20K/FFHQ improvements are within noise, say so explicitly and provide variance estimates. If they are real, offer a hypothesis.
4. **Analyze the staleness loop.** Track the overlap of pruned samples across epochs and report whether the method systematically under-trains any subset.
5. **Replace the "lossless" framing** with a more precise descriptor such as "performance-preserving" or "approximately lossless," unless the above statistical evidence justifies the stronger term.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>