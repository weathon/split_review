## Summary

This paper proposes LoLoRA, a LoRA variant that replaces the frozen *A* matrix in LoRA-FA with online Hebbian PCA (HPCA) updates computed during the forward pass, eliminating the need to store activations for backpropagation through *A*. The authors derive a theoretical optimality condition for *A* under a random regression model (Theorem 4.4) and evaluate on GLUE, MathQA, multimodal LLaVA, and ablations on TinyLlama. The core idea — updating *A* locally without storing activations — is neat, and the theoretical characterization of the optimal *A* subspace is a legitimate contribution.

## Strengths

1. **Rigorous theoretical characterization of optimal A (Theorem 4.4).** The paper proves that, under a random regression model, the optimal frozen matrix *A* is any nonsingular linear transformation of the top *r* principal eigenvectors of the input covariance matrix. This provides a formal foundation for data-driven initialization methods (including EVA) that was previously lacking. The proof appears mathematically sound.

2. **Memory reduction is demonstrated across domains.** On LLaMA-3.1-8B MathQA (Table 3), LoLoRA reduces extra GPU memory from 30 GB (standard LoRA) to 26 GB while achieving the joint-highest accuracy (82.9%). Similar savings are reported on GLUE (up to 20% vs. standard LoRA, per Appendix D). The experiments cover NLU, reasoning, and multimodal settings, showing broad applicability.

3. **Comprehensive ablation study (Tables 5–6).** The paper compares 5 initializations (uniform, orthogonal, PiSSA, EVA) and 5 local update rules (HPCA variants, AE, SoftHebb) on TinyLlama. This allows the reader to isolate the effects of initialization vs. online adaptation. The results consistently show that HPCA-based methods perform nearly identically to EVA-initialized LoRA-FA.

## Weaknesses

### Major

1. **The central empirical claim — that LoLoRA's online adaptation adds value over a frozen PCA initialization — is unsupported by the data.** Across all experiments, LoLoRA (HPCA) is essentially tied with LoRA-FA (EVA), a simpler baseline that initializes *A* via PCA once and then freezes it. On GLUE (Tables 1–2), LoLoRA *underperforms* LoRA-FA (uniform) on 6 of 8 tasks. On MathQA (Table 3), LoLoRA ties LoRA-FA (EVA) at 82.9%. On LLaVA (Table 4), LoLoRA (2.93 perplexity) sits between LoRA-FA uniform (2.97) and LoRA-FA EVA (2.92). The ablations (Tables 5–6) confirm the pattern: at r=8, LoLoRA HPCA achieves 2.535 perplexity while LoRA-FA (EVA) achieves 2.536 — effectively identical. **If the supposed advantage of LoLoRA is online adaptation to distribution shifts, the paper should show a setting where online HPCA beats a single frozen PCA initialization. It does not.** This is the paper's most significant weakness because it calls into question whether the core innovation (online local updates) provides any practical benefit.

2. **The memory narrative conflates LoLoRA with LoRA-FA.** The abstract states that LoLoRA "further reduc[es] the memory required for fine-tuning," but the memory savings come from *not storing activations for A's backward pass* — which is exactly what LoRA-FA already achieves by freezing *A*. LoLoRA's memory footprint is essentially the same as LoRA-FA (Table 4: 24.1 GB vs. 23.9 GB; Table 3: both 26 GB). The paper should be clearer that LoLoRA matches LoRA-FA's memory efficiency while enabling *A* to be updated, not that it reduces memory beyond LoRA-FA.

3. **The local update rule is underspecified for reproducibility.** Algorithm 1 references `Opt_loc` and `LocalRule` but never states what optimizer is used for *A* (SGD? Adam? a specific HPCA solver?), the learning rate (or step size) for the HPCA update, or the hyperparameters beyond "smoothing factor 0.98" for the running mean. The paper cites Oja's SNL algorithm but does not give the precise update equations used in the experiments. For a method whose novelty is a specific local learning rule, this is a significant reproducibility gap. The appendix (stripped by the parser) may contain more details, but the main text should be self-contained on this point.

4. **The theory (Theorem 4.4) primarily justifies EVA, not LoLoRA's online contribution.** Theorem 4.4 shows that optimal *A* spans the top PCs of the input covariance — an insight that EVA (Paischer et al., 2024) already exploited empirically. LoLoRA's claimed addition is that HPCA can reach this subspace *online* without a separate PCA pre-pass. However, no experiment shows that online HPCA outperforms a single PCA initialization followed by freezing. The theory therefore does not provide evidence for the method's core claim; it is consistent with both LoLoRA and the simpler LoRA-FA (EVA) baseline. This disconnect between the theoretical framing and the experiments weakens the paper's narrative.

### Minor

5. **The paper overstates comparative results.** The conclusion claims that "HPCA consistently outperforms standard LoRA-FA in two out of three experimental setups." This is true as a factual statement (LoLoRA beats LoRA-FA uniform on MathQA and LLaVA), but the margin is tiny (0.3% on MathQA, ~0.04 perplexity on LLaVA) and within noise on many tasks. On GLUE — the largest benchmark — LoLoRA is *worse* than LoRA-FA (uniform). The claim is technically accurate but gives a misleading impression of the method's advantage.

6. **No analysis of how the PCA subspace evolves during training.** The method is motivated by "input distribution shifts," but the paper never measures whether the input covariance actually changes during fine-tuning, whether HPCA tracks it better than a static initialization, or whether the subspace found by HPCA matches the true top PCs. This makes the adaptation claim speculative rather than evidence-based.

7. **The comparison to standard LoRA on GLUE shows consistent degradation (0.2–1.1 points across tasks).** While "comparable" is a matter of interpretation and the memory savings are real, the paper should more explicitly acknowledge that on NLU tasks, LoLoRA sacrifices a small but consistent amount of performance relative to full LoRA — unlike LoRA-FA which sometimes matches or improves over LoRA (e.g., RTE, SST-2).

### Trivial

8. The paper references Appendix D for memory analysis but the appendix is stripped; the main text should report memory breakdowns more explicitly (activations vs. optimizer states vs. LoRA parameters).

## Nice-to-Haves

- **Evidence that online adaptation matters.** A direct comparison of LoLoRA (HPCA) vs. LoRA-FA (EVA) with a measure of how well the *A* subspace tracks the input covariance during training would validate the claimed motivation.
- **Statistical significance tests** for the comparative claims. Many differences are within one standard deviation.
- **Comparison to other low-memory PEFT methods** (VeRA, (IA)³, QLoRA) would help contextualize the method's memory/performance trade-off.
- **Specification of the HPCA learning rate and optimizer** in the main text.

## Removed Points

The following points from the harsh critic were checked against the paper and removed for the reasons stated:

- **"The central performance claim is not supported by the paper's own data" — the claim that LoLoRA is worse than standard LoRA on GLUE is true but the paper says "comparable" which is defensible given the small margins (≤1.1 points) and overlapping error bars. The critic overinterprets the GLUE results as contradicting the abstract; the abstract's "comparable" is not falsified by the data. The "two out of three" claim is factually accurate (MathQA and LLaVA show improvement over LoRA-FA uniform).** This point was downgraded from the critic's framing but its substance (weak empirical advantage) is retained in Major weakness #1 and Minor weakness #5 above.

- **"The theory does not translate into a practical advantage" — This is not a separate weakness from #1; it is the same evidential gap.** The critic's framing that the theory is "ornamental" is too harsh — Theorem 4.4 is a legitimate theoretical contribution that provides a unified justification for PCA-based initialization. The point is absorbed into Major weakness #4.

- **Criticisms about missing comparison to VeRA, (IA)³, QLoRA, and about FLOPs analysis** are nice-to-haves but not core flaws, downgraded to Nice-to-Haves.

- **Criticisms about missing appendix sections** are removed per the instruction that the parser strips appendix content.

## Novel Insights

None beyond the paper's own contributions. The key insight — that under a random regression model, optimal *A* is a transformation of the top input PCs — is the paper's own theoretical result, and the observation that HPCA can approximate this online is the paper's own method. No reviewers contributed an insight not present in the paper.

## Suggestions

1. **Reframe the contribution.** The paper should position LoLoRA as a way to *avoid a separate PCA pre-pass* while achieving similar performance to EVA-initialized LoRA-FA, not as a method that improves performance over LoRA-FA. This is a more honest and defensible claim, and it matches the data.
2. **Add an experiment that validates the adaptation claim.** Measure the cosine similarity between the HPCA subspace and the true top PCs at various training steps. If the subspace drifts during fine-tuning, show that HPCA tracks it better than a static PCA initialization.
3. **Specify the HPCA update rule and hyperparameters** (step size, optimizer) in the main paper. Without these, the method cannot be independently implemented.
4. **Provide a clearer memory breakdown** (activation memory vs. optimizer state vs. adapter parameters) for LoRA, LoRA-FA, and LoLoRA in all experimental settings.

---

## Score and Decision

### Anchor Comparison

| Anchor | Avg Score | Round / Query | Comparison to LoLoRA |
|--------|-----------|---------------|----------------------|
| ALLoRA (7X65yoKl3Y) | 3.33 | R1-topic-low | Weaker theory and experiments. LoLoRA is clearly better. |
| HoLoRA (igGeaxOiFM) | 3.00 | R1-topic-low | Similar weakness in empirical support. LoLoRA has stronger theory. |
| LoRA-FA (RbKThNNFxr) | 5.33 | R1-topic-mid / R1-weakness-memory | Closest baseline. LoRA-FA's claim (matching LoRA while saving memory) is better supported by its data than LoLoRA's claim. LoLoRA is weaker. |
| EVA (DM6Q45HWSk) | 4.75 | R1-weakness-EVA / R2 | Shares theoretical foundation. LoLoRA adds online updates but doesn't outperform EVA. Comparable strength. |
| EigenLoRA (KxGGZag9gW) | 5.00 | R2 | Similar pattern (eigendecomposition-based LoRA variant with mixed empirical results). LoLoRA is slightly weaker empirically. |
| DeLoRA (X1U74IwuxG) | 5.25 | R2 | Clearly demonstrated advantage (hyperparameter robustness). LoLoRA lacks such a clear demonstrated advantage. |
| ReLoRA (DLJznSp6X3) | 5.75 | R1-topic-mid | Stronger results in a complementary setting (pre-training). LoLoRA is weaker. |
| Forward Learning (My7lkRNnL9) | 6.50 | R1-weakness-local-hebbian | Stronger theoretical and empirical depth in a related (forward-only learning) subfield. LoLoRA is weaker. |
| "Activations Aren't Cheap" (3ylNuZXtMg) | 4.25 | R1-weakness-memory | Comparable range; both papers identify memory issues in LoRA. |
| GE-PEFT (NmiFwEP8K5) | 4.50 | R2 | Similar score range, also a PEFT variant with modest empirical support. |

**Round-1 bracket:** [3.5–5.5]. The paper sits above the ~3.0 band (ALLoRA, HoLoRA) due to sound theory and multi-domain experiments, but below the ~5.3+ band (LoRA-FA, ReLoRA) because its core empirical claim is not well-supported.

**Round-2 narrowing:** Focused on the 3.5–5.5 range. Zeroed in on EVA (4.75), EigenLoRA (5.00), and GE-PEFT (4.50) as the most comparable peers. LoLoRA's empirical weaknesses (online HPCA doesn't beat frozen PCA) are closer to the lower end of this range.

**What the low-band anchors failed at:** ALLoRA (3.33) and HoLoRA (3.00) failed because their theoretical reasoning was shaky and their empirical improvements were marginal or missing. LoLoRA partially shares the marginal-empirical-improvement failure but has genuinely sound theory, placing it above 3.3 but not near 5+.

**Final position:** The paper has a legitimate theoretical contribution and a reasonable idea, but the evidence does not demonstrate that the core innovation (online HPCA updates) provides practical value over the simpler LoRA-FA (EVA) baseline. The memory framing is also somewhat misleading. The paper is better than the weakest LoRA variants but falls short of the evidential standard set by papers in the 5+ range.

**MY FINAL SCORE: <score>4.5</score>**
**MY FINAL DECISION: <decision>Reject</decision>**