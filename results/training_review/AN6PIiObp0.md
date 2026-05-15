Now I have a thorough understanding of the paper and all the reviews. Let me compile the final consolidated review, carefully cross-checking every criticism against the actual paper text.

---

## Summary

SALSA replaces the standard single-SFT reference model in PPO-based RLHF with a weight-space average (model soup) of two independently fine-tuned SFT models. The motivation is that the soup sits in a "higher-reward" region of parameter space, allowing the KL penalty to target a better reference and thus enabling broader exploration during policy optimization. Experiments on Llama2-7B, Mistral-7B, and Gemma-2B across MT-Bench, Arena-Hard, and UltraFeedback show directionally positive win rates over PPO (50.68%–57.19%), and ablations support the mechanistic story.

## Strengths

- **Novel observation of reward geometry near model soups.** Section 4.2 demonstrates (before any RLHF) that reward-model scores peak at the midpoint of two SFT models and that the interior of a 3-SFT simplex has higher reward than the vertices. This observation goes beyond the accuracy/loss improvements shown in the original model soup literature and directly motivates the method.

- **Clean ablations that support the proposed mechanism.** The α-ablation (Figure 4a) shows win rate peaks at α=0.5 (the uniform soup), while using π\_other alone yields only 43.07%. The MKL ablation (Figure 4b) shows that averaging two separate KL divergences does not outperform PPO, whereas SALSA does — ruling out the alternative explanation that any multi-reference signal suffices.

- **Directionally consistent results across 9 experimental conditions.** SALSA achieves win rates >50% over PPO on all 3 models × 3 benchmarks (Table 1). The scaling experiment (more SFTs → higher win rate, Figure 5) further corroborates the approach.

- **Evaluation breadth.** Three LLM families (Llama2-7B, Mistral-7B, Gemma-2B) and three instruction-following benchmarks (MT-Bench, Arena-Hard, UltraFeedback) with GPT-4-Turbo judging provide reasonable coverage for an empirical RLHF paper.

## Weaknesses

### Fatal
None. The core claims are not invalidated, though some are weaker than advertised.

### Major

- **No confidence intervals or significance testing for the headline win rates.** Table 1 reports point estimates (e.g., 50.75%, 50.68%, 52.50%) without any error bars, p-values, or bootstrap estimates. MT-Bench has only 80 questions, Arena-Hard has 500. On these sizes, a win rate of 52.5% or 50.7% is within the noise band of the evaluation. The paper repeatedly claims SALSA "consistently outperforms" PPO, but the reader cannot assess whether individual comparisons reflect genuine improvement or chance variation. While the consistency *across* 9 comparisons is encouraging, the evidence for individual benchmarks is weaker than the paper asserts.

### Minor

- **"Adjusted Win Rates" is never defined.** The Table 1 caption and the ablation section use this term, but the paper never specifies how pairwise GPT-4 judgments are converted to an "adjusted" win rate (e.g., how ties are handled, whether 50% represents chance or tied performance). This is a basic reporting gap that prevents proper interpretation of every numerical result in the paper.

- **Out-of-distribution robustness is claimed but not tested.** The abstract and conclusion assert OOD improvements, and line 228 says "SALSA's robustness to out-of-distribution data … delivers improvements." But all three evaluation benchmarks (MT-Bench, Arena-Hard, UltraFeedback test) are standard in-distribution instruction-following sets. No explicit OOD evaluation (e.g., domain shift, task shift) is conducted. The OOD claim is inherited from the model soup literature without independent verification in this setting.

- **PPO tuning details underspecified.** The paper states (line 139) that "For both PPO and SALSA, we use the KL coefficient β that achieves the highest win rate" but does not report the β search range, the values tried, the criterion for "highest win rate" (evaluated on which dataset?), or the final β values used per model/dataset. While both methods are tuned symmetrically, the lack of detail makes it difficult to assess the fairness of the comparison or reproduce the results.

- **"PPO tends to find solutions near the vertices" (line 194) is stated without evidence.** The paper asserts this as part of the reward-plane analysis but provides no measurements of PPO-trained parameters to support the claim. This is a reasonable intuition (PPO starts from π\_ref and the KL penalty anchors it), but it is left as an unverified assumption.

- **Reward analysis (Section 4.2) uses the same reward model employed for PPO training.** The analysis showing higher rewards near the soup uses the reward model trained on UltraFeedback — the same model that provides the reward signal during PPO. This limits the strength of the motivational evidence: the soup may be exploiting idiosyncrasies of that particular reward model rather than reflecting a genuinely better region. However, this does not affect the main results, which rely on GPT-4-Turbo judgments. This is a concern for the *motivational* analysis but not for the core empirical claim.

### Trivial

- **Model inconsistency in the reward analysis.** The reward interpolation experiments (Figures 4a–b, Section 4.2) use "Gemma-7B" (line 191, line 152) while the main experimental setup (line 139) and all main results (Table 1) use Gemma-2B. If a different model size was used for the analysis, this should be explained. As written, it creates confusion.

## Nice-to-Haves

- A comparison with the dynamic reference model of Gorbatovski et al. (2024) — already discussed in related work — would contextualize SALSA among existing solutions to the same limitation.
- Reporting observed KL divergences during training (if not already in the appendix, which was stripped by the parser) would directly support the claim that SALSA allows broader exploration.
- A small-scale human evaluation would strengthen the claim of better alignment beyond automated GPT-4 judging.

## Removed Points

These points were raised by reviewers but are removed with justification:

- **"PPO baseline might be unusually weak"** — The paper states both methods use the β achieving the highest win rate (line 139). The observation that "a basic version of PPO does not significantly outperform SFT" (line 228) is a well-known finding in the literature, not evidence of poor tuning. **Removed (strawman).**

- **"Missing KL divergence measurement"** — The paper references `\ref{sec:kl-divergence}` and `\ref{tab:app:mean_kl}` (lines 255, 261), indicating this analysis exists in the original submission. The parser strips appendix content from all papers. **Removed (artifact of parsing).**

- **"Improvement in reward is a newly observed phenomenon" is misleading** — Model soup papers (Wortsman et al.) showed accuracy/loss improvements on classification. Showing reward-model score improvement (before RLHF) on LLM responses is genuinely new and complementary. **Removed (not factually incorrect).**

- **"Comparison with Gorbatovski et al. is missing"** — This is a nice-to-have extension, not a required baseline. The paper already cites and discusses this work. **Removed (scope creep).**

- **"Human evaluation is missing"** — Standard practice in the RLHF literature is automated evaluation with GPT-4 judging. A human study is nice but not required. **Moved to Nice-to-Haves.**

- **"Policy initialization may cause instability or large KL spikes"** — A valid theoretical observation but belongs as an analysis extension, not a weakness of the presented results. No evidence that instability occurred is provided by the reviewer. **Removed (speculative concern).**

## Novel Insights

The interaction between the two reviews reveals an interesting tension: the Harsh Critic's strongest point (no confidence intervals) is genuinely important, yet the strength of the paper lies not in any single win-rate number but in the *consistency* of the pattern across 9 conditions combined with the ablations (α=0.5 optimal, MKL fails, more SFTs help). The reward-geometry analysis — while dependent on a single reward model — provides an explanation for *why* the soup works that goes beyond what a pure win-rate table can show. This dual structure (mechanistic analysis + consistent directional results) partially compensates for the lack of per-comparison significance testing, but the paper would be substantially strengthened by explicitly making this consistency argument and by providing error bars or bootstrap intervals.

## Suggestions

1. **Define the evaluation protocol.** Clarify what "Adjusted Win Rate" means — how are ties counted? Is the adjustment splitting ties? Report this clearly alongside each number.
2. **Add confidence intervals or bootstrap estimates** for the win rates in Table 1. At minimum, report approximate standard errors given the benchmark sizes (N=80 for MT-Bench, N=500 for Arena-Hard). If computational cost permits, run multiple seeds.
3. **Remove or substantiate the OOD claim.** Either add an explicit out-of-distribution evaluation (e.g., a different domain or task distribution) or temper the language to match what was actually tested.
4. **Report the β search details.** Include the search range, the evaluation criterion, and the final β values per model/dataset.
5. **Explain the Gemma-7B vs Gemma-2B discrepancy** in the reward analysis, or unify the model choices.

## Score and Decision

**Originality:** 6/10 — Model soup as a reference in PPO is a straightforward but underexplored combination. The reward-geometry finding is the most novel part.

**Importance of research question:** 7/10 — Improving RLHF exploration is a well-recognized problem; the paper targets a real limitation.

**Claims support:** 4/10 — The main claim of "consistently outperforms" is weakened by the absence of confidence intervals, undefined win-rate adjustment, and untested OOD claims.

**Soundness of experiments:** 5/10 — Reasonable breadth and good ablations, but the lack of statistical reporting and underspecified tuning details undermine confidence.

**Clarity of writing:** 6/10 — The method is clearly described. The main presentation gap is the undefined "Adjusted Win Rates" and the model inconsistency.

**Value to community:** 6/10 — Simple, implementable idea with plausible empirical support. Would benefit from stronger statistical validation.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>