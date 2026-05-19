- Decision: Reject
- Avg Score: 2.00
- Scores: 3, 3, 1, 1
Now let me compile the final review after carefully verifying each claim against the paper.

## Summary

This paper introduces the "atypical" video dataset (5,486 videos spanning sci-fi, animation, unintentional actions, and abnormal events) and reports an exploratory study on using this data as outlier exposure (OE) to improve OOD detection in video action recognition. The central finding is that fine-tuning a ResNet3D-50 classifier with this small but diverse atypical dataset consistently improves OOD detection metrics on HMDB51 and MiT-v2 compared to using much larger conventional datasets (Kinetics400, Diving48) as OE sources. The paper further shows that increasing the categorical diversity of atypical samples yields progressively better OOD detection performance.

## Strengths
1. **Novel atypical video dataset** — The first dataset explicitly curated for studying atypical video content in open-world learning. The four-category design (sci-fi, animation, unintentional, abnormal) is well-motivated and fills a gap relative to standard action recognition datasets (Section 3, Table 1).

2. **Consistent empirical trend across multiple OOD benchmarks** — Table 2 shows that atypical OE improves AUROC over the baseline on all four OOD test sets (e.g., HMDB51 AUROC: baseline 83.40 → atypical 90.46; MiT-v2: baseline 78.48 → atypical 89.35) and surpasses Kinetics400 and Diving48 as OE sources. The improvements are directionally consistent, not cherry-picked from one favorable setting.

3. **Ablation evidence for categorical diversity** — Figures 4 and 5 and Table 3 demonstrate a clear monotonic trend: as more atypical categories are combined, OOD detection metrics improve (e.g., HMDB51 AUROC rising from ~86 with one category to ~90 with four). This directly supports the claim that diversity within the OE data is a key driver.

4. **Careful removal of category overlaps** — The paper explicitly removes overlapping action categories between UCF101 (ID), HMDB51 (OOD), MiT-v2 (OOD), and Kinetics400 (OE) (Section 4.2.3), preventing label leakage that could inflate OOD detection performance.

5. **Comparative evaluation across multiple OE baselines** — Five OE sources (Gaussian noise, Bernoulli noise, Diving48, Kinetics400, atypical) are evaluated under the same fine-tuning protocol (Table 2), providing a reasonably comprehensive benchmark.

## Weaknesses

### Fatal
None. The weaknesses below are significant but do not invalidate the paper's core thesis.

### Major
1. **No statistical confidence on any result** — Tables 2, 3 and Figures 4, 5 report single-run metrics with no error bars, standard deviations, or multiple seeds. The atypical dataset is small (5,486 videos), and several reported margins are thin (e.g., Table 3 shows <1 point AUROC differences between category combinations). Without at least 3 seeds, the reader cannot determine whether the headline gaps (atypical OE vs. Kinetics400 OE) are reliable or within random variation. This is the most consequential weakness because the paper's central claim rests on these numerical comparisons.

2. **Unexamined preprocessing asymmetry between OE datasets** — Section 3.2 describes aggressive manual curation of the atypical data: "manually reviewed to remove noninformative content," "temporally trimmed to retain action-rich segments," with selection "guided by the presence of clear and distinguishable targets." The paper does **not** state whether Kinetics400 or Diving48 received any analogous preprocessing. Since Kinetics400 clips are already sourced as ~10-second YouTube action clips, the asymmetry may be smaller than the critic suggests, but the lack of explicit clarification creates an uncontrolled confound: is the improvement due to *atypical content* or to *tighter temporal trimming*? This should be addressed by either confirming that all OE datasets were used in a comparable form or adding an ablation.

### Minor
3. **Fixed fine-tuning schedule may not equally serve all OE datasets** — All OE datasets are fine-tuned for exactly 5 epochs. The concern is that a larger dataset (Kinetics400: ~240k clips) may require more epochs to imprint its features compared to a small focused set (atypical: 5,486 clips). This is speculative—one could equally argue that Kinetics400 receives more total gradient updates per epoch—but the paper does not check whether the OE loss converges for each dataset, leaving the possibility that the comparison reflects training budget rather than data quality. An ablation with variable epochs or a convergence check would address this.

4. **Evaluation scope is narrow** — The study uses a single backbone (ResNet3D-50), a single ID dataset (UCF101), a single detection method (MSP), and only binary OOD detection. While this is acceptable for an exploratory study, the generality of the claims ("atypical data improves open-world learning") would be strengthened by testing at least one alternative backbone, another ID dataset, or an alternative scoring function (e.g., energy score).

### Trivial
5. **Synthetic vs. realistic OOD discussion is buried** — The paper correctly notes (Section 4.4) that noise OE inflates mean metrics by dominating on noise OOD tasks while hurting real OOD performance. This important caveat appears only in the prose and is not reflected in the table layout or a separate discussion, making it easy to miss.

## Nice-to-Haves
- Include a limitations section or explicit discussion of the study's boundaries (single backbone, single ID dataset, exploratory scope).
- Quantify feature-space separation between OE and OOD distributions (e.g., average pairwise distance or nearest-neighbor overlap) to complement the qualitative t-SNE visualization in Figure 6.

## Removed Points
*These points were flagged for removal; treat with caution.*

- **Dataset release status** (Harsh Critic #1, Critical Issues section): The critic notes "no information on whether the dataset will be released." Removed per hard rule: criticisms questioning release status/availability of cited resources must be removed.
- **"Harry Potter" title criticism**: The critic calls the title "an attention-getter" that is "not substantively integrated." This is a subjective presentation judgment, not a technical weakness.
- **Equation formatting nitpick** about `P(x|\mathbb{D})`: Removed per hard rule removing formatting/style nitpicks.
- **Missing related works**: Removed per hard rule (cannot verify existence of missing references without external sources).
- **Missing limitations section**: Not a standard requirement; removed as a format nitpick.
- **Suggestion that the paper should test open-set recognition or novel class discovery**: This asks the paper to address a task outside its stated scope (binary OOD detection). Scope creep.
- **Criticism about the "Unintentional" and "Abnormal" subsets being re-packaged**: The paper is already transparent about each subset's source (Section 3.1 explicitly names Oops Dataset, Ped2, CUHK Avenue, ShanghaiTech, UCF Crime). No misrepresentation.

## Novel Insights
None beyond the paper's own contributions. The reviews converge on the same core observation as the paper: that diverse atypical OE data improves OOD detection in video, but that the evidence base would benefit from statistical grounding.

## Suggestions
1. **Add error bars.** Run all main experiments (Tables 2, 3, Figures 4, 5) with at least 3 random seeds and report mean ± std. This is the single highest-leverage improvement.
2. **Clarify preprocessing for all OE datasets.** State explicitly whether Kinetics400 and Diving48 were used as-is or received any curation. Ideally, run an ablation where atypical data is used *without* aggressive trimming to test whether preprocessing explains the advantage.
3. **Add a convergence check for OE fine-tuning.** Report the OE loss after 5 epochs for each dataset, or run an ablation with more epochs for Kinetics400.
4. **Separate synthetic vs. realistic OOD results more clearly** in the table or add a dedicated paragraph to the results section.
5. **Include at least one additional detection method** (e.g., energy score) or one additional backbone to demonstrate generality.

**Evaluation axes:**
- *Originality*: Good — novel dataset and application of OE to video OOD detection.
- *Importance of research question*: Good — OOD detection in video is underexplored relative to images/text.
- *Claims well supported*: Moderate — consistent trends but no statistical confidence; potential confound from preprocessing asymmetry.
- *Soundness of experiments*: Moderate — reasonable setup and baselines, but missing error bars and convergence checks weaken rigor.
- *Clarity of writing*: Adequate — generally clear; organization is logical.
- *Value to community*: Good — the atypical dataset has reuse potential; the empirical findings are actionable.
