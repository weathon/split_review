Here is my consolidated review:

---

## Summary

This paper investigates how reasoning data should be allocated across pretraining and post-training (SFT, RL) stages of LLM development. Training four 8B models from scratch (1T tokens each) on different reasoning data blends and then crossing them with multiple SFT datasets, the authors find an **asymmetric allocation principle**: diversity and scale matter most during pretraining, while quality dominates SFT. They further claim that front-loading reasoning into pretraining yields compounding gains through post-training (a +19% lead after RL), that high-quality pretraining data has "latent effects" unlocked by SFT, and that naive SFT scaling can be harmful.

## Strengths

- **Large-scale, computationally ambitious study.** The paper trains 8B models from scratch for 1T tokens with controlled data blends—an experiment few academic labs can run. The fully factorial design (4 pretraining × 3 SFT conditions) yields a rich dataset of comparisons that collectively point to a consistent empirical pattern.

- **The asymmetric principle is practically relevant and intuitively grounded.** The finding that broad, diverse reasoning data helps pretraining while curated, high-quality data dominates SFT is an actionable heuristic that challenges simplistic "more is better" approaches. The supporting evidence in Tables 1 (pretraining) and 5 (SFT) shows a clear reversal across phases.

- **Multiple ablations strengthen internal consistency.** The catch-up test (Table 4), reasoning-ratio sensitivity (Tables 6–7), and SFT scaling analysis (Table 8) probe the robustness of the main findings and provide useful empirical data points beyond the headline claims.

- **RL-phase result is striking.** Table 3 shows \(\mathcal{M}_{\text{LMQ}} + \text{SFT}_{\text{SHQ}} + \text{RL}\) achieving 56.66% vs. 37.92% for the baseline on expert-level benchmarks, with a 39% absolute improvement on AIME—demonstrating that the pretraining advantage survives through the full pipeline.

## Weaknesses

### Major

- **No replication or uncertainty quantification.** Every claimed quantitative result—the 19% gain, the 11% diversity advantage, the 15% quality advantage, the 4% latent effect, the −5% harm from scaling SFT—rests on a single training run per condition. Without multiple seeds or any variance estimate, the paper cannot distinguish signal from noise. Many comparisons involve small differences (e.g., \(\mathcal{M}_{\text{LDQ}}\) vs. \(\mathcal{M}_{\text{LMQ}}\) at pretraining: 64.09 vs. 64.07 in Table 1; \(\mathcal{M}_{\text{LDQ}} + \text{SFT}_{\text{ALF}}\) vs. + \(\text{SFT}_{\text{ALF}}^*\): 42.66 vs. 43.04 in Table 8) where the reader cannot tell whether these are meaningful. This undermines the quantitative precision claimed in the abstract and Section 1. For large-scale pretraining, 2–3 seeds with different random initializations would be the standard to establish reliability.

- **Confounding of data factors prevents clean isolation of the asymmetric principle.** The three reasoning datasets differ simultaneously on multiple axes: \(\mathcal{D}_{\text{LDQ}}\) is large, diverse, mixed-quality; \(\mathcal{D}_{\text{SHQ}}\) is small, narrow, high-quality; \(\mathcal{D}_{\text{LMQ}}\) is their union. The paper attributes \(\mathcal{M}_{\text{LDQ}} > \mathcal{M}_{\text{SHQ}}\) at pretraining to "diversity and scale," but the comparison conflates scale, diversity, domain composition, and quality. Similarly, the SFT advantage of \(\mathcal{D}_{\text{SHQ}}\) is attributed to "quality," but \(\mathcal{D}_{\text{SHQ}}\) differs in size, length, and domain distribution. To causally establish the asymmetric principle, one needs at least one experiment that varies diversity while controlling for scale and quality (or vice versa). The current design does not provide such contrasts, so the central claim remains correlational rather than causal.

- **RL-phase evidence is too narrow to support global conclusions.** The RL experiment (Table 3) compares only two models: \(\mathcal{M}_{\text{base}} + \text{SFT}_{\text{SHQ}} + \text{RL}\) vs. \(\mathcal{M}_{\text{LMQ}} + \text{SFT}_{\text{SHQ}} + \text{RL}\). It does not test \(\mathcal{M}_{\text{SHQ}}\), \(\mathcal{M}_{\text{LDQ}}\), or other SFT variants from earlier tables, so it cannot speak to how diversity- vs. quality-based pretraining strategies compound differently through RL. The headline "19% average gain" comes from this single comparison, presented as if it generalizes across all pretraining strategies. A full RL sweep across all four base models with at least a common SFT recipe is needed to support the claimed generality.

### Minor

- **Ambiguous reporting of gains.** The abstract states "19% average gain" without specifying training stage or whether this is absolute or relative. In the body, 19% refers to the RL phase (18.57 percentage points absolute, Table 3), while the SFT-phase gain is 9.3 points (Table 2) and the pretraining gain is 8.35 points (Table 1). These are all absolute percentage-point differences, but the paper never clarifies this, making the headline claims imprecise.

- **The "catch-up" test is a limited operationalization.** The paper doubles SFT epochs for \(\mathcal{M}_{\text{base}}\) and finds it still cannot match reasoning-pretrained models. However, this tests only one axis of catch-up (more SFT epochs on the same data). Stronger tests—scaling SFT data volume, using a different SFT recipe, or adding a mid-training phase—are not conducted. The conclusion that SFT "cannot fully replicate" pretraining advantages is stronger than the evidence supports.

- **The "latent effect" claim (Table 4) has an alternative explanation.** \(\mathcal{M}_{\text{LMQ}}\) outperforms \(\mathcal{M}_{\text{LDQ}}\) by +4.25% after SFT on \(\mathcal{D}_{\text{SHQ}}\). Since \(\mathcal{M}_{\text{LMQ}}\) saw \(\mathcal{D}_{\text{SHQ}}\) during pretraining (as part of \(\mathcal{D}_{\text{LMQ}}\)), this advantage could partly reflect distribution alignment (the SFT data matches what was seen in pretraining) rather than any intrinsic "latent quality" of mixed data. The paper does not control for this.

- **The optimization framework in Eq. (2) is not operationalized.** The paper frames the problem as splitting a fixed budget \(\mathcal{B} = |\mathcal{D}_{\text{res}}^{\text{PT}}| + |\mathcal{D}_{\text{res}}^{\text{SFT}}|\) but never varies the split: pretraining always gets 80B reasoning tokens and SFT always gets 4.8M samples (~1B tokens). The budget framing is conceptually useful but does not correspond to the experiment design.

- **Reasoning data appears in the second half of pretraining (600B base-only → 400B mixed), which is closer to mid-training injection than "front-loading" in the strict sense.** While "front-loading" is meaningful relative to the full pipeline (pretraining vs. post-training), the title may overstate the earliness of injection within pretraining itself.

- **\(\mathcal{D}_{\text{ALF}}\) uses answer length >4096 tokens as a quality proxy**, which is at best a coarse heuristic. Longer answers can contain rambling, hallucinated, or otherwise low-quality reasoning. This does not invalidate the result but weakens the "high-quality" label.

### Trivial

- The paper uses percentage-point differences without the "%" vs. "pp" distinction, which could mislead readers about the scale of improvements.

## Nice-to-Haves

- Adding at least one experiment that varies data diversity while holding scale and quality fixed (e.g., a diverse subset of \(\mathcal{D}_{\text{LDQ}}\) matched to \(\mathcal{D}_{\text{SHQ}}\) in size) would substantially strengthen the causal interpretation of the asymmetric principle.
- Applying RL to all four base models (\(\mathcal{M}_{\text{base}}, \mathcal{M}_{\text{SHQ}}, \mathcal{M}_{\text{LDQ}}, \mathcal{M}_{\text{LMQ}}\)) would clarify whether the asymmetric principle holds at the RL stage.
- Reporting loss curves on held-out base data (e.g., C4 validation) would directly test the overfitting hypothesis the paper raises but addresses only indirectly.
- A per-task breakdown for the RL phase beyond the two-model comparison would help understand whether the advantage is concentrated in math or broad across domains.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Strength Finder's claim about "controlled experimental design isolates phase-specific effects"** — This conflicts with the verified weakness about confounding of data factors (see Major above). The factorial design is a strength, but the specific data comparisons are not cleanly isolating individual factors, so this claim is overstated.
- **"Missing appendix" / "missing proofs in appendix"** — The parser strips appendix content; these exist in the original submission.
- **General formatting/style nitpicks** — These are parser artifacts, not author errors.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a genuine tension: the paper's headline claims are framed with quantitative precision (19%, 11%, 15%, etc.) that the experimental design—with its confounded factors and single-run methodology—cannot support. The most useful insight from the review process is that the paper would benefit from repositioning itself as an exploratory, hypothesis-generating study rather than a causally conclusive one.

## Suggestions

1. **Add variance estimates.** Even 2–3 seeds for the central comparisons (or, minimally, bootstrapped confidence intervals from evaluation sampling) would dramatically increase confidence in the findings. Without this, the paper's quantitative precision claims are unsupported.

2. **Add at least one causally cleaner comparison.** Create a size-matched diverse subset of \(\mathcal{D}_{\text{LDQ}}\) to compare against \(\mathcal{D}_{\text{SHQ}}\) at pretraining, controlling for scale. This would directly test whether diversity or scale drives the pretraining advantage.

3. **Expand the RL sweep.** Apply RL to at least \(\mathcal{M}_{\text{LDQ}}\) and \(\mathcal{M}_{\text{SHQ}}\) in addition to \(\mathcal{M}_{\text{base}}\) and \(\mathcal{M}_{\text{LMQ}}\) to understand how different pretraining strategies compound through RL.

4. **Tone down the causal language.** Reframe the asymmetric principle as a consistent empirical pattern rather than a causally established law. This would make the paper honest about its limitations while preserving its contribution.

5. **Clarify whether reported gains are absolute or relative percentage points** throughout the paper, and specify which training stage each headline number refers to.

## Score and Decision

**Calibration Anchors (all paths in `/home/wg25r/review_agent/human_reviews_2026/`):**

| Path | Avg Score | Comparison |
|------|-----------|------------|
| `yKUbw7q1IA.md` (How to train data-efficient LLMs) | **6.80** | Stronger empirical methodology (hundreds of runs, multiple seeds). Current paper has a more ambitious question but weaker methodology. |
| `T5wkZJqzkz.md` (How LR Decay Wastes Your Best Data) | **6.00** | Cleaner experimental design with clear diagnosis. Current paper addresses a broader question but with less clean evidence. |
| `uLM3BfKo19.md` (Quagmires in SFT-RL) | **5.67** | More rigorous methodology (hundreds of models, >1M GPU hours, multiple seeds). Current paper's question is complementary but evidence is less definitive. |
| `MQ5gqRRHVN.md` (Facts in Stats) | **5.00** | Clean controlled experiments but limited to synthetic data. Current paper has more practical relevance but messier confounds. |
| `HwcwLBATQT.md` (Debunk the Myth of SFT Generalization) | **3.00** | Narrow evaluation scope, limited applicability. Current paper is stronger in scope and practical relevance. |
| `HNZfblGcKG.md` (Scheduling data improves fine-tuning) | **3.50** | Limited novelty, narrow evaluation. Current paper has clearer, more novel contributions. |
| `guUUlHPXRw.md` (Modelling Optimal Trade-Off CPT/SFT) | **2.00** | Fundamentally flawed experimental design. Current paper is substantially stronger. |
| `9gw03JpKK4.md` (Gaia2) | **8.00** | Clean benchmark contribution, comprehensive evaluation, strong novelty. Current paper is less polished methodologically. |

**Positioning:** The paper addresses an important question and produces a large-scale empirical study that few can replicate. Its core findings are intuitively plausible and practically relevant. However, compared to papers scoring 6+, its evidence is substantially weakened by the lack of replication/uncertainty quantification and by confounded data factors that prevent clean causal interpretation of the asymmetric principle. These are not minor nitpicks—they directly affect whether the central claims are supported at the level of precision the paper asserts. Relative to the anchors, the paper is clearly stronger than the 2–3.5 range but has deeper methodological issues than the 6+ papers. It is comparable in quality to the 5.0–5.5 range but with higher practical relevance.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>