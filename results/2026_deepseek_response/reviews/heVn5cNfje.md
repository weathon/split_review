Now let me finalize my assessment with calibration comparisons.

**Round 1 Bracket:** The paper sits comfortably above the weak-band papers (2.0-3.0) and clearly below the 8.0 strong-band papers. My initial bracket is **5.5–7.0**.

**Round 2 Anchors (5.5–7.5):** Comparing against the key anchors:
- **DELIFT (6.00, Accept):** Similar scope (data selection across paradigms), similar strength (70% pruning). This paper's HES metric is arguably more principled than DELIFT's ICL-based utility, and the SFT-20% matching full-dataset is more impressive. I'd rate this paper *slightly better* than DELIFT in evidence strength, but the lack of variance reporting in RFT/RL is a real gap. Approximately **6.0–6.5**.
- **CoT through Information Theory (6.40, mixed):** Different framing but similar information-theoretic approach. Its score distribution (5,6,8,5,8) shows polarization. The current paper has more consistent evidence across experiments. About **6.0**.
- **Rule-Based Rating (5.75, Reject) and 3DS (5.75, Reject):** These are weaker — limited novelty or insufficient baselines. This paper is stronger.

The paper's SFT results are its strongest pillar and alone justify acceptance. The RFT/RL weaknesses (small margins, no variance) are real but fixable. The paper is clearly above the average reject-level paper at 5.75 and comparable to DELIFT at 6.00 (which was accepted). I'll set the score at **6.0**.

---

## Summary

This paper introduces High-Entropy Sum (HES), a training-free metric that sums the entropy of only the top 0.5% highest-entropy tokens in a reasoning response, rather than averaging across all tokens. The authors argue this better captures critical "forking points" in long-CoT reasoning. They validate HES-guided data selection across three training paradigms: SFT, RFT, and RL, showing consistent gains over baselines like length, difficulty, and other entropy-based metrics.

## Strengths

1. **HES provides markedly better separation of correct vs incorrect reasoning samples than global entropy metrics.** Figure 1 quantitatively shows that normalized mean HES for incorrect samples (0.68) is substantially higher than for correct samples (0.29), whereas average entropy yields nearly overlapping means (0.53 vs 0.52). This directly supports the paper's core claim that focusing on the highest-entropy tokens reveals discriminative signal hidden by averaging.

2. **HES-guided SFT consistently achieves performance matching or exceeding full-dataset training with only 20% of the data, and pruning the lowest-20% boosts results above full-dataset.** Table 1 shows Highest-HES-20% at 31.14% (approaching full-dataset 32.61%) and Highest-HES-80% at 35.36%, surpassing full-dataset. This pattern replicates on DeepSeek-R1-Distilled-7B (Table 2) and across code (Table 3) and STEM (Table 4) domains, demonstrating robustness.

3. **Small-to-large transfer using a 0.6B proxy model achieves performance (32.12%) comparable to 8B self-selection (31.14%), establishing cost-effective scalability.** The paper shows that HES captures data-intrinsic properties rather than model-specific artifacts, enabling practical large-scale data curation with a tiny scoring model.

4. **The asymmetric RL sampling strategy (Pos-High, Neg-Rand) outperforms both random downsampling (21.30% vs 19.88%) and the full-batch baseline (20.63%) using half the positive rollouts per update.** Table 6 shows HES is the only training-free metric to surpass the full-batch baseline in RL, with a controlled ablation demonstrating the importance of negative sample diversity.

5. **Comprehensive evaluation across 7 benchmarks, multiple baseline methods (length, difficulty, multiple entropy variants), two model families, and three training paradigms.** This breadth strengthens confidence in the findings.

## Weaknesses

### Major

1. **No statistical significance or variance reporting in RFT and RL experiments.** The paper reports single-run results throughout. In RFT (Table 5), the average advantage of Highest-HES over Random is +1.01, +1.69, and +0.97 points for k=2,4,8 in the per-query setting — differences small enough that run-to-run variation could account for them. In RL (Table 6), the headline gain of Pos-High, Neg-Rand over Full-Batch is +0.67 points. Without confidence intervals, multiple seeds, or variance measures, the reader cannot assess whether the RFT and RL improvements are statistically reliable. The SFT results (larger margins) partially mitigate this, but the paper's claim that HES works "across SFT, RFT, and RL" is only fully supported for SFT without proper uncertainty quantification.

2. **Confound in the SFT full-dataset baseline: differential number of training steps.** All SFT experiments train for three epochs. Since the full dataset (~100k examples) is ~5× larger than the 20% subsets (~20k), the full-dataset model receives ~5× more gradient updates. If the full-dataset model is undertrained (3 epochs on 100k for a 7B/8B model may be insufficient for convergence) or overtrained, the claim that "top-20% matches full-dataset performance" is confounded by unequal optimizer steps. This does not invalidate comparisons between HES and other methods at the *same* ratio (e.g., Highest-HES-20% vs Random-20%), but it weakens the strongest headline claim about matching full-dataset performance.

### Minor

3. **Computational cost of HES is not quantified.** The paper calls HES "training-free," which is technically correct (no separate model training), but computing token-level entropies for long-CoT responses (~8k tokens) requires a forward pass per candidate. The small-to-large transfer experiment partially addresses cost, but the paper never reports actual compute (FLOPs or wall time) of HES scoring relative to baselines like length (free) or difficulty (requires multiple sampling runs). Quantifying this trade-off would strengthen the practical contribution.

4. **The conceptual link between "forking tokens" and HES-guided SFT needs sharper reasoning.** In SFT, HES is computed on *external correct demonstrations* using the base model's entropy. The paper never explicitly argues why a correct demonstration that the base model finds *uncertain* is a good training example — it relies entirely on downstream performance to justify it. The "forking tokens" intuition (from Wang et al. 2025) applies most naturally to the model's own generations (as in RFT/RL). A brief conceptual justification would help.

5. **Mild overclaim in the sensitivity analysis.** Section 4.4 states "smaller, more targeted ratios of 0.005 and below consistently deliver the best performance," but only four ratios were tested (0.005, 0.05, 0.5, 1.0). No ratios below 0.005 were evaluated, so the "and below" claim is unsupported. The statement should be limited to "0.005 delivers the best performance among tested values."

### Trivial

None.

## Nice-to-Haves

- Add qualitative examples showing high-HES and low-HES tokens highlighted in reasoning paths to substantiate the "forking tokens" intuition visually.
- Analyze what Lowest-HES samples actually look like (trivially easy, short, template-based?) to strengthen the finding that pruning them boosts performance.
- Discuss settings where HES might fail (e.g., overconfident errors where the model is confident on an incorrect reasoning path, yielding low HES despite being incorrect).
- Mention why the per-query setting in RFT outperforms global-pool selection beyond the diversity hypothesis (e.g., is it partly due to better representation of harder queries with fewer correct responses?).

## Removed Points

These points from the input reviews are removed with justification:

- *"Figure 1 does not explain why HES separates better — incorrect samples have higher HES than correct, so high-HES correct responses are most similar to incorrect ones"* — **Removed.** The paper's logic is that within the set of correct responses, higher HES indicates "successful navigation of more difficult forks" and thus more informative training data. The cross-group comparison (correct vs incorrect means) is a sanity check showing HES captures uncertainty, not a contradiction of the within-group selection logic. The "similar to incorrect" framing is not a valid criticism since the paper selects correct responses, not incorrect ones.
- *"Computational cost roughly equals generation cost"* — **Removed.** This is speculative quantification. The small-to-large transfer experiment (0.6B proxy) directly addresses practical cost concerns by showing orders-of-magnitude cheaper scoring is viable.
- *"Missing reproducibility details (which checkpoint, forward pass question)"* — **Removed.** The paper states the base model is used, and HES is clearly computed from the model's token-level probabilities, which implies a single forward pass.
- *"Missing related work"* — **Removed per instructions:** I cannot verify existence of missing related works.
- *Style/formatting nitpicks* — **Removed per instructions.**
- **Strength Finder generic strengths:** Several strengths were removed because they were generic ("the paper targets an important problem," "the paper is well-written") or duplicative of kept strengths.

## Novel Insights

The insight that averaging entropy across all tokens (standard practice) dilutes the signal from critical forking tokens, and that summing the entropy of only the top percentile of tokens reverses this, is the paper's own contribution. The finding that removing the 20% *lowest*-HES samples consistently boosts performance over full-dataset training (Tables 1-4) is a striking demonstration that low-quality data acts as training noise even in curated datasets. The asymmetric RL strategy insight — that constraining negative samples harms performance while targeting high-HES positive samples helps — is a non-obvious finding about the interaction between data selection and policy learning.

## Suggestions

1. **Run RFT and RL experiments with 3–5 random seeds** and report means and standard deviations. This is the single highest-leverage improvement: if the gains hold with proper variance, the paper's claims are strongly supported; if they collapse, the claims should be revised downward.
2. **Clarify or control for the SFT training-step confound.** Either train the full dataset to convergence (e.g., with early stopping on a held-out set) or compare at matched numbers of gradient steps. A brief discussion of why three epochs was chosen would also help.
3. **Quantify the compute cost of HES scoring** (FLOPs per response, total wall time for data curation) relative to baselines like length (free) and difficulty (requires multiple samples).
4. **Add a brief conceptual justification** for why a correct demonstration with high HES is a good SFT training example, connecting the "forking tokens" intuition to the model's learning dynamics.
5. **Correct the sensitivity overclaim** — replace "0.005 and below" with "0.005 among tested values."

## Score and Decision

**Calibration procedure:**

**Round 1 — Bracketing** (3 queries, topic "data selection for LLM reasoning"):
- Weak band (avg ≤ 3.5): 2.00–3.00 — papers with poor experimental design or minimal contribution. This paper is clearly above.
- Middle band (3.5–7.5): 4.40–6.00 — papers with solid contributions but identifiable weaknesses.
- Strong band (≥7.5 avg): 8.00 — top-tier papers. This paper is below these.
- **Initial bracket: 5.0–7.0**

**Round 2 — Narrowing** (3 queries, score range 5.5–7.5):
- DELIFT (avg 6.00, Accept): Similar scope (data selection for fine-tuning). Comparable strength of SFT results. This paper arguably has stronger SFT results (matching full dataset with 20%) but weaker variance reporting. **Comparable, ~6.0.**
- CoT through Information Theory (avg 6.40, mixed decision): More theoretical framing, less empirical breadth. This paper has broader validation (SFT+RFT+RL vs one paradigm). **Slightly below this anchor for the paper as currently presented, ~6.0.**
- Rule-Based Rating (avg 5.75, Reject), 3DS (5.75, Reject), Best of Both Worlds (6.0, Reject), DSDS (5.75, Accept): This paper's SFT evidence is stronger than these anchors. **Above 5.75–6.0.**

**Final calibrated score: 6.0** — The paper sits comfortably in the 6.0 band. The SFT results alone are strong enough to warrant acceptance, but the lack of variance reporting in RFT/RL prevents a higher score. The paper is comparable to DELIFT (6.0, Accept) in overall strength, with slightly stronger empirical breadth and slightly weaker statistical rigor.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>