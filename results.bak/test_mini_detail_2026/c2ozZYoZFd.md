Now I have a good understanding of the calibration landscape. Let me write the final review.

## Summary

This paper provides a detailed case-study re-analysis of the ICLR 2025 Oral paper on min-p sampling. It systematically examines all four lines of evidence presented in the original paper — human evaluations, NLP benchmarks, LLM-as-a-Judge evaluations, and community adoption claims — and shows that each fails to support the original conclusions when properly analyzed. The paper makes a methodological contribution (Best-of-N analysis for controlling hyperparameter volume in comparisons) and derives a set of general lessons for rigorous empirical ML research. The evidence is substantial: correct statistical re-analysis of omitted human data, a 6000 A100-hour controlled sweep on GSM8K, documentation of selective reporting, and verification that community-adoption claims were retracted.

## Strengths

1. **Discovery of omitted data and correct statistical re-analysis of human evaluations (Section 2).** The paper shows that the original study omitted 1/3 of human evaluation data (scores for basic sampling) without justification. When all data are included and 12 one-sided t-tests are performed with Bonferroni correction (Table 1), only 1 of 12 comparisons reaches significance at α=0.05. The Intersection-Union Test further confirms that the claim of "consistent" superiority is unsupported. This is the strongest section of the paper — the evidence chain is complete, verifiable from the original paper's own published data.

2. **Novel "Best-of-N" methodology for controlled hyperparameter comparison (Section 3.1, Figures 4-5).** The paper develops an analysis that equalizes the number of hyperparameters searched per method, then measures how maximum performance improves as the hyperparameter budget grows. This is a genuine methodological contribution that addresses a common confound in empirical ML (unequal hyperparameter tuning). The sweep covers 9 models × 31 temperatures × 6 hyperparameters per sampler × 3 seeds, totaling ~6000 A100-hours, and convincingly shows min-p is indistinguishable from baselines when hyperparameter volume is controlled.

3. **Systematic exposure of selective reporting in LLM-as-a-Judge evaluations (Section 4.3).** The paper documents that the original paper reported the higher of two win rates for min-p (52.01 at p=0.05 vs. 50.14 at p=0.01) but the lower for top-p (50.07 at p=0.9 vs. 50.43 at p=0.98). Combined with the finding that min-p received 2–10× more hyperparameter tuning than baselines (Figure 6), this is concrete evidence of asymmetric evaluation favoring the proposed method.

4. **Verification and subsequent retraction of unsubstantiated community-adoption claims (Section 5).** The paper independently shows that the claimed 54,000 repositories and 1.1 million stars could not be substantiated (summing stars of major LM repositories gives ~453k), and that these claims were retracted from the camera-ready version. The finding that 3 of 4 reviewers and the Area Chair cited these numbers as justification for acceptance demonstrates the real-world impact of unverified claims on peer review.

## Weaknesses

### Fatal
None.

### Major

- **The NLP benchmark re-analysis is limited to GSM8K, but the abstract and framing use plural "benchmarks."** The original paper evaluated min-p on both GSM8K and GPQA. The present re-analysis, due to compute constraints (6000 A100-hours), only covers GSM8K. The abstract states "Extensive hyperparameter sweeps on NLP benchmarks show min-p's claimed superiority vanishes" — this is technically accurate for the single benchmark analyzed, but the plural phrasing ("benchmarks," and Section 3 title "Extending Min-p's NLP Benchmark Evaluations") overstates the scope. The authors acknowledge this only implicitly in the discussion. This does not invalidate the GSM8K results — which are thorough and convincing on their own — but the paper's framing should align with its actual scope.

### Minor

- **The selective reporting claim in Section 4.3 relies on a single Telegram link as the primary evidence.** The paper states that the first author shared a Telegram link showing that higher win rates were reported for min-p and lower for top-p. For a serious allegation of selective reporting, this evidence chain is thin. The claim is likely true (it is consistent with the asymmetric hyperparameter tuning documented in Section 4.2), but the paper would be stronger with a screenshot, a table of the raw data, or a more transparent description of the Telegram data. As written, the evidence is credible but falls short of the standard set by the rest of the paper's analysis.

- **The human evaluation re-analysis (Section 2) focuses on the "high diversity" setting and excludes the "low diversity" setting.** The authors provide reasonable justifications for this choice (authors' guidance, poorly chosen top-p hyperparameter in low diversity), and the original claim as stated ("across all settings") is invalidated even within the high-diversity setting alone. However, the paper should state this scope decision more explicitly early in Section 2 to avoid any ambiguity about the coverage of the re-analysis relative to the original claims.

### Trivial
None worth listing — the paper is well-written and the parser artifacts (image captions, page breaks) are not author errors.

## Nice-to-Haves

- **A brief discussion of statistical power** for the human evaluation study (53 participants) would strengthen the methodological lessons in Section 6. The paper demonstrates the original claims are unsupported, but a comment on whether the study had sufficient power to detect meaningful effect sizes if they existed would be informative.
- **A brief discussion of the assumptions of the Best-of-N analysis** (e.g., that hyperparameters are independently sampled uniformly; in practice researchers may tune more strategically) would strengthen Section 3.

## Removed Points

These points from the inputs were removed or demoted for the following reasons:

1. **Harsh Critic's concern about the Telegram link being "unverifiable"** — Removed as a formal weakness (per hard rules, cited references/tools exist if the paper cites them). However, I retained the substance as a Minor weakness because the evidence chain is thin for a serious accusation, not because the link doesn't exist.

2. **Harsh Critic's "Missing/Places to Improve" items: "Statistical power," "Non-parametric tests," "Reproducibility," "Best-of-N assumptions"** — Moved to Nice-to-Haves or removed. These are suggestions that would strengthen the paper but are not flaws. The paper already meets community standards for a critique paper.

3. **Strength Finder's generic strengths** — Some strengths were generic ("the paper addresses an important problem"). Removed those and kept only specific, evidence-grounded strengths.

4. **Harsh Critic's suggestion about "add a GPQA replication"** — Moved to implicit in the Major weakness about scope. It's the flip side of the same issue.

5. **Harsh Critic's note about "make scope explicit" for human evaluation re-analysis** — Integrated into the Minor weakness about low-diversity setting scope.

6. **Harsh Critic's "community adoption" point in Strengthening the Paper on Its Own Terms (point 3)** — This was already well-argued in the paper and is not missing. Demoted from its status as a needed improvement.

## Novel Insights

None beyond the paper's own contributions. The paper is a straightforward and well-executed re-analysis case study; the reviewers' analyses do not surface observations that the paper's authors haven't already made.

## Suggestions

1. In the abstract and Section 3 title, qualify "NLP benchmarks" to "on GSM8K" or add a sentence noting the scope. This is a small change that would eliminate the overclaiming concern.
2. In Section 4.3, add a screenshot of the Telegram data or a tabular rendering of the two win rates per hyperparameter to strengthen the selective reporting evidence. Even a sentence describing the raw numbers more transparently would help.
3. Add an explicit sentence in Section 2 clarifying that the re-analysis covers the high-diversity setting (with justification), and that this alone suffices to show the original claim fails because it relied on a flawed low-diversity condition.

## Score and Decision

### Calibration

**Round 1 — Bracketing:** I queried for meta-analysis/reproducibility critique papers in three bands.

*Low band (avg < 3.5):* Anchors included papers with scores 0–2.8 (e.g., "TabPalooza" at 1.20, "Reliable Detection of ASD" at 0.00, "EEG confound" at 2.00). These are fundamentally flawed or incomplete papers with little valid evidence. **The current paper is far above this band.**

*Middle band (3.5–7.5):* Anchors included "Is Memorization Actually Necessary for Generalization" (4.00, Rejected) — a critique paper that had limited experiments (50 models), no code release, and insufficient evidence to overturn its target claim. Also "On the (In)Significance of Feature Selection" (4.67, Rejected) — which had highly polarized reviews (2,2,10) and significant methodological concerns. **The current paper is clearly stronger than both** — it has more extensive experiments, released code and data, a novel methodological contribution, and more convincingly supports its claims.

*High band (avg > 7.5):* Anchors included papers at 8.00 (e.g., "Multilevel Control Functional," "LLMs Get Lost in Multi-Turn Conversation"). These are papers proposing new methods/theory with strong execution and evaluations. **The current paper, as a meta-analysis, is not at this level because it is critiquing another work rather than proposing a fundamentally new method.**

**Round 1 bracket: 4.0–7.5**

**Round 2 — Narrowing (4.5–7.5):** I queried for critique/evaluation papers in the upper-middle range.

*Anchors examined in full:*
- **"How NOT to benchmark your SITE metric"** (6.00, Poster, scores 6,4,8,6) — Critique of evaluation practices. Weakness: didn't implement the fixes it recommended. **The current paper is stronger** — it not only identifies flaws but provides new experiments and a novel methodology.
- **"Curse of Slicing"** (6.50, Poster, scores 6,8,4,8) — Critique of SMI with theoretical analysis. **Comparable** — both have strong evidence for their critiques, but the current paper has broader implications and larger-scale experiments.
- **"Dropping Just a Handful of Preferences"** (7.33, Poster, scores 8,6,8) — Clean, impactful findings about LLM ranking fragility. **The current paper is slightly weaker** — the 7.33 anchor had stronger novelty in its findings and tighter execution; the current paper's scope limitation (one NLP benchmark) and thin evidence for the selective reporting claim prevent it from reaching this level.

**Final score: 6.5/10.** The paper is a well-executed, thorough re-analysis with genuine contributions (Best-of-N methodology, concrete lessons for rigorous science). It is not fatally flawed — the weaknesses are scope limitations and one thin evidence chain, not fundamental errors. It is stronger than the typical 4–5 range critique papers that lack experiments or fail to produce new evidence. However, the scope limitation (GSM8K-only) and the Telegram-link evidence prevent it from reaching the top of the bracket.

**Decision: Accept** as a Poster. The paper's contribution — a rigorous, high-quality case study that demonstrates methodological best practices — is valuable for the community. The weaknesses are fixable with minor revisions.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>