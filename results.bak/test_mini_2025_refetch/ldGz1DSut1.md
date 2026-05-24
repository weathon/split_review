Now I have all the data needed. Here is my final consolidated review.

---

## Summary

This paper presents the first systematic study of whether multiple deep image watermarking methods can coexist in the same image (i.e., both be decoded accurately) and proposes using coexistence to ensemble watermarks as a post-hoc tool for adjusting capacity–accuracy–robustness–quality trade-offs without retraining. The core empirical finding—that watermarks from different methods often do not overwrite each other—is counterintuitive and practically relevant.

## Strengths

- **First systematic study of deep watermark coexistence:** Table 1 shows that for most method pairs (e.g., DwtDct followed by DwtDctSvd, HiDDeN followed by SSL), the first watermark's accuracy remains high (often close to its solo accuracy) after the second watermark is applied. This contradicts the intuitive expectation that the second watermark would overwrite the first and fills a genuine gap in the literature.

- **Coexistence persists even after controlling for quality degradation:** Figure 3 shows that after clipping watermark strengths to 0.5 (equating the final PSNR to the mean of the individual methods' PSNRs), many method pairs still retain ≥25% accuracy for both watermarks. This controls for the trivial explanation that coexistence is merely a byproduct of extra capacity at lower quality.

- **Ensembling enables capacity increase and new trade-offs without retraining:** Figure 5A demonstrates that ensembling TrustMark B (100 bits) and SSL (100 bits) yields an effective capacity of 200 bits, which is impossible with strength clipping or ECC alone. Figure 6C shows ensembles of RoSteALS and HiDDeN dominating the base models in accuracy–quality space.

- **Parallel vs. series ensembling provides a practical design knob:** Figure 7 shows that parallel ensembling (averaging residuals) yields a PSNR distribution shifted to higher quality (up to 45 dB) compared to series ensembling, which concentrates below 40 dB.

- **Honest evaluation against ECC+strength clipping baselines:** Figure 8 shows that applying ECC alone to a strong base method (TrustMark Q with LC[100,32,25]) outperforms all ensembles of RivaGAN+TrustMark Q. The paper does not overclaim and clearly communicates when ensembling is beneficial versus when it is not.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **No uncertainty quantification for accuracy/robustness estimates.** All results are point estimates (over 1020 images) without confidence intervals, standard errors, or statistical tests. For claims that hinge on small differences (e.g., "only minor impact on decoding robustness"), the absence of error bars makes it impossible to judge whether observed differences are meaningful or sampling noise. While single-run evaluation on large test sets is common in the watermarking community, adding CIs or bootstrap estimates would substantially strengthen the paper's empirical claims.

- **The "controlling for quality" experiment (Fig. 3) could be better motivated.** The paper clips strength to 0.5 so that the final PSNR approximates the *mean* of the individual methods' PSNRs — a reasonable center-point choice. However, the paper does not check whether the coexistence pattern is sensitive to this specific target. A robustness check across multiple target PSNRs would clarify whether the observed pattern is robust or specific to this quality level.

- **Systematic ensembling comparison is limited to a few hand-picked examples.** The ensembling experiments (Figs. 5, 6) focus on a handful of method pairs. While the paper is honest about this being illustrative, a more systematic evaluation (e.g., a heatmap across all 8×8 pairs with a consistent ECC and strength-clipping setup) would significantly strengthen the practical guidance about when ensembling is beneficial.

### Trivial
None.

## Nice-to-Haves

- **Comparison against a retrained model with equivalent capacity.** The paper's framing is "without retraining," but it would be informative to compare the ensemble against a model retrained to match the same total capacity. This would establish how large the gap is between ensembling and a purpose-built solution (the paper acknowledges this gap but does not quantify it).

- **Analysis of how coexistence varies with image content, secret length, or strength.** For example, do high-capacity watermarks overwrite each other more? Does coexistence degrade for low-texture images? This would deepen the empirical contribution.

- **Security implications.** If multiple watermarks can coexist, an adversary could adversarially embed an extra watermark to disrupt the intended one. A brief discussion would be valuable, though it is outside the paper's stated scope.

## Removed Points

These points are flagged to be removed; treat them with caution:

1. **"Underspecified experimental conditions"** (re dataset/anonymization): The paper states "1020 samples from Anon. dataset," giving the dataset size. "Anon. dataset" is a standard double-blind review placeholder. The robustness augmentation details were referenced to App. D, which existed in the original submission but was stripped by the parser. Per the hard rules, criticisms about missing appendix content and dataset anonymization during blind review are removed.

2. **"Robustness evaluation not comparable across methods"**: The paper references App. D for augmentation parameters. This criticism falls under the rule about missing appendix content stripped by the parser. Removed.

3. **"Arbitrary strength choice" framing**: The paper justifies strength=0.5 by stating it makes the final PSNR approximate the mean of individual methods' PSNRs. This is a principled choice (the mean is a natural center point), not arbitrary. This criticism is weakened to the minor note above.

## Novel Insights

None beyond the paper's own contributions. The reviews did not surface a synthesis that goes deeper than what the paper already provides.

## Suggestions

1. Add 95% confidence intervals (bootstrap) for all accuracy and robustness numbers.
2. For the "controlling for quality" experiment (Fig. 3), show results across a small grid of target PSNRs (e.g., mean ± a few dB) to demonstrate robustness of the coexistence finding.
3. Provide a systematic heatmap or table showing which method pairs respond well to ensembling across all 8 methods, using a consistent ECC and strength-clipping setup.
4. De-anonymize the dataset (e.g., COCO or similar standard benchmark) in the final version.

## Score and Decision

**Calibration anchors (all rounds):**

| Paper | Avg Score | Round | Comparison to this paper |
|---|---|---|---|
| FStega [bGv9kWeBcw] | 2.80 | R1 | Much weaker — significant methodological flaws |
| Hybrid Defense Strategy [ns8qw9q19b] | 3.00 | R1 | Much weaker — conceptually unrelated |
| From Forgery to Authenticity [hYEV8QmaOt] | 3.40 | R1 | Much weaker — submitted/withdrawn |
| Quantifying Likeness [9zKm3TytBG] | 2.50 | R1 | Much weaker — limited contribution |
| A Recipe for Watermarking DMs [HexshmBu0P] | 5.33 | R1, R2 | Weaker — limited novelty, straightforward application |
| Who Leaked the Model? [WNSjteBJd9] | 5.33 | R1 | Differently scoped (FL) — not directly comparable |
| Safe & Robust Watermark Inj. [PCm1oT8pZI] | 5.75 | R1, R2 | Similar overall quality; our paper has more novel findings |
| Codable Watermarking for LLMs [JYu5Flqm9D] | 5.75 | R2 | Similar framing ("first systematic study"); our empirical findings are more surprising |
| Multi-bit Watermark for LLMs [KOTsHW6mBI] | 5.20 | R2 | Weaker — withdrawn/rejected |
| Semantic-aware Spec. Sampling [LdIlnsePNt] | 6.00 | R2 | Comparably scored but rejected due to serious rigor issues; our paper is more coherent |
| Transfer Attack to Watermarks [UchRjcf4z7] | 6.50 | R1, R2 | Stronger on experimental rigor; our paper has more novel contribution |
| Lightweight Deep Watermarking [j7b4mm7Ec9] | 7.60 | R1 | Stronger individual scores but rejected; our paper has more conceptual novelty |
| Dataset Bias Decade Battle [SctfBCLmWo] | 8.00 | R1 | Different class of contribution (Oral) |

**Round 1 bracket:** Between ~4.5 and ~7.0 (clearly above weak anchors at 2.5–3.4, below top-tier work at 7.5+).

**Round 2 narrowing:** Within (5.5, 7.5), the paper sits closest to JYu5Flqm9D (5.75, Accept) and PCm1oT8pZI (5.75, Accept) — both accepted. Our paper has a more genuinely surprising empirical finding (coexistence) than those papers, but lacks some experimental rigor (no error bars, limited systematic comparison). It is slightly weaker on rigor than UchRjcf4z7 (6.50, Accept) but has a more novel contribution.

**Final score: 6.0.** The paper has a genuinely novel and surprising core finding, clear motivation, thorough coverage of 8 methods, and honest assessment of limitations. The weaknesses are real but addressable and do not invalidate the central contribution.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>