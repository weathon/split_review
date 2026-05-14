Now I have a thorough understanding of the paper and anchor comparisons. Let me write the final consolidated review.

---

## Summary

This paper decouples the class label from the target concept in machine unlearning, formalizing three realistic mismatch scenarios (target mismatch, model mismatch, data mismatch) beyond the conventional all-matched setting. Through theoretical analysis showing that representation distance governs forgetting dynamics ("gravity effects") and empirical verification via t-SNE visualizations, the paper motivates a unified framework called TARF with three phases: target identification (via annealed gradient ascent), target separation (via simultaneous gradient ascent on forgetting data and gradient descent on identified false-retaining data), and retraining approximation. Across CIFAR-10/100, TinyImageNet, and ImageNet-1k, TARF dramatically outperforms existing methods on mismatched scenarios while remaining competitive on all-matched tasks.

## Strengths

- **Novel problem formulation with clear taxonomy**: The paper introduces and formalizes three label-domain mismatch scenarios (target, model, data mismatch) that systematically extend class-wise unlearning beyond the conventional all-matched setting. This conceptual framework is well-motivated (Section 3.1, Figure 1) and addresses a genuine gap: practical unlearning requests often violate pretraining taxonomy. The taxonomy is clean and likely to spur follow-up work.

- **Principled connection between representation geometry and forgetting dynamics**: Theorem 3.2 formally links the change in loss difference between two data subsets to their representation distance under gradient ascent, providing a theoretical basis for the "gravity effects" intuition. The empirical validation in Figure 3 (t-SNE visualizations + loss/accuracy trends on CIFAR-100) convincingly demonstrates the predicted entanglement (model mismatch) and under-entanglement (target/data mismatch) in learned representations, directly motivating the TARF design.

- **Effective unified framework with strong empirical results**: TARF achieves dramatic improvements across all mismatch scenarios. On CIFAR-100 target mismatch, TARF reduces the Gap metric to 0.21 vs. 8.86 for the best baseline (GA); on model mismatch, Gap drops from 2.45 (SCRUB) to 1.21; on data mismatch, from 2.43 (GA) to 1.17 (Table 3). TARF achieves near-perfect MIA (100.0) and near-zero UA in target/data mismatch where all baselines fail badly. These results directly support the claim that TARF approximates the retrained reference significantly better when label domains are mismatched.

- **Comprehensive evaluation breadth**: TARF is validated on CIFAR-10/100, TinyImageNet, and ImageNet-1k (Table 4), multiple architectures including ResNet-18, VGG-16, WideResNet-50 (Table 26), and extends to concept removal in Stable Diffusion (Figure 6, Tables 19-20) and LLM unlearning on TOFU with Llama 3.2 at 1B and 8B scales (Table 5). This breadth demonstrates the generality of the approach beyond standard classification setups.

- **Thorough ablation and sensitivity analysis**: The paper provides detailed studies on hyperparameters k, t₁, t₀ across all four settings (Figures 7, 17), ablation of β selection under varied false-retain sizes (Table 17), and analysis of the annealed vs. constant gradient ascent design choice. The computational overhead of target identification is shown to be minimal (0.18 min vs. 4.23 min total on CIFAR-10, Table 18).

## Weaknesses

### Fatal

None.

### Major

- **Reliance on known false-retain class count for β selection**: In target mismatch and data mismatch scenarios, TARF requires knowing how many classes/examples in the remaining set belong to the target concept to set the quantile threshold β (Section 2, line 229: "we assume that the number of classes in D_un belonging to the target concept is known"). The paper explicitly acknowledges this as a "task feasibility" assumption and draws an analogy to label-noise learning where noise rates are estimated as prior information (Appendix E.1). It also discusses alternatives in Appendix E.4 (pseudo-labels, model predictions). However, the paper does not evaluate TARF *without* this oracle information, and Table 17 shows performance degradation when the false-retain set is large and the quantile selection includes noise. This weakens the claim of practical applicability in deployment scenarios where the developer may not know the exact extent of the target concept. The paper would be strengthened by either (a) evaluating a heuristic β-setting strategy that does not use the ground-truth false-retain count, or (b) more thoroughly analyzing why the method's core mechanism (gravity-based ranking) might remain effective without this prior.

### Minor

- **LLM and diffusion experiments are preliminary**: The TOFU experiments (Table 5) report only QA probability on forget/retain sets, lacking standard unlearning metrics (accuracy, MIA equivalents). The diffusion case study (Tables 19-20) is anecdotal with only two prompts and a handful of generated images, without systematic quantitative evaluation (e.g., CLIP-score, FID) across a test set. These experiments are presented as case studies, and the paper honestly does not overclaim them—they are in the appendix—but the main-text language about "real-world applications" (Section 4.2) slightly overstates what the evidence supports.

- **Gap metric may mask trade-offs**: The Gap metric averages absolute deviations across UA, RA, TA, and MIA, which operate on different scales (percentages vs. MIA confidence). While this yields a convenient single number, it can obscure cases where a method achieves strong forgetting at severe utility cost. The paper does not present per-metric Pareto-style analysis or discuss metric dominance in the average.

- **No adapted baselines for mismatch settings**: All compared baselines (FT, GA, RL, BS, L1-sparse, SalUn, SCRUB) were designed for the all-matched scenario. While demonstrating their failure is a valid part of the paper's motivation, including even one simple adapted baseline (e.g., GA followed by quantile-based target selection + FT) would help isolate the contribution of TARF's joint optimization from the mere inclusion of a target-identification step. This is not essential for the paper's core argument but would strengthen the comparative analysis.

### Trivial

- The CIFAR-10 superclass grouping is manually constructed by the authors (line 786). The paper acknowledges this and cites prior work (Dhakad et al., 2024); the CIFAR-100 groups use official superclasses. This is a minor transparency point, not a flaw.
- The Gap metric is not fully explained in terms of per-component weighting; a brief note on this in the main text would improve clarity.

## Nice-to-Haves

- Evaluating TARF with a purely heuristic β (e.g., fixed top-5% rule without oracle knowledge of false-retain size) to quantify the practicality penalty.
- A simple two-stage baseline: run GA for a few epochs, select classes/samples with largest accuracy drop using the same quantile rule, then apply an existing method (e.g., SCRUB) on the union. This would isolate the contribution of TARF's joint optimization.
- Quantitative evaluation of target-identification quality (precision/recall of identified false-retain classes over t₁) to provide deeper insight into where the gravity-based identification succeeds or fails.
- Systematic concept removal evaluation for diffusion models using CLIP-score or FID across a held-out concept test set.

## Removed Points

These points are flagged to be removed, treat them with caution:

1. **Harsh critic's claim that β reliance makes the method impractical / "cannot operate autonomously"**: The paper explicitly states the assumption (line 229) as a "task feasibility" condition, discusses alternatives (Appendix E.4), and provides sensitivity analysis (Table 17). The assumption is analogous to knowing the noise rate in label-noise learning—a standard and accepted practice. The harsh critic overstates the severity. Demoted to Major (not Fatal).

2. **Harsh critic's claim that Theorem 3.2 is "decorative rather than foundational"**: The theorem provides formal grounding for the gravity effects intuition that drives the entire method design. While the Lipschitz assumption is standard, the theorem is not incorrect or misleading—it correctly characterizes how representation distance relates to differential loss changes under gradient ascent. The harsh critic's dismissal is too harsh.

3. **Harsh critic's complaint about t-SNE lacking quantitative metrics**: The paper provides quantitative loss/accuracy trends alongside t-SNE in Figure 3 and refers to additional cluster-wise distance and accuracy dynamics in Figure 9 (Appendix). The qualitative visualizations serve their explanatory purpose.

4. **Strength Finder's generic claims**: Dropped one strength about "practical considerations including computational cost" being framed as a major strength—the computational analysis (Table 18) is useful but standard, not a standout contribution.

5. **Harsh critic's "β estimated at single time point t₁" concern**: The paper explicitly designs β to be computed once at t₁ (end of Phase I) and kept fixed. Figure 17 sweeps t₁ showing stability. This is a design choice, not a flaw.

6. **Harsh critic's criticism about Appendix content**: The parser strips appendix sections; the original submission includes all proofs, ablations, and extended results mentioned in the paper.

## Novel Insights

The most genuinely novel insight emerging from this work—one that goes beyond the authors' own framing—is the realization that **forgetting dynamics themselves can serve as an implicit query mechanism for discovering the boundaries of an under-specified unlearning target**. Rather than requiring the developer to exhaustively enumerate all data belonging to a concept, TARF exploits the fact that gradient ascent on a partial forget set creates a measurable signal (accuracy/loss change) that propagates through the representation space according to semantic proximity. This "gravity-based" discovery mechanism is elegant because it repurposes the unlearning operation itself as an information-gathering tool, effectively turning a weakness of gradient ascent (collateral damage to nearby representations) into a strength (identification of semantically related data). This insight may generalize beyond the class-wise setting explored here.

## Suggestions

- Conduct and report an experiment where β is set heuristically (e.g., fixed top-ρ% rule without ground-truth false-retain count) to quantify how much performance degrades without the oracle assumption. This would directly address the major weakness.
- Present per-metric breakdowns alongside the Gap metric to make trade-offs transparent. A simple bar chart or radar plot would suffice.
- Clarify in the main text that the LLM and diffusion results are preliminary case studies, not full validation of generality, to avoid overclaiming.
- For the CIFAR-10 superclass grouping, briefly justify the semantic groupings or note that results on CIFAR-100 (official superclasses) serve as the primary validation.

---

**Calibration comparison:**

| Anchor | Avg Score | Comparison |
|--------|-----------|------------|
| `/home/wg25r/review_agent/human_reviews_2026/IPqUBL4R9x.md` (Distributional Unlearning) | 6.0 | Similar structure: novel problem framing + theory + algorithm. TARF has broader experimental coverage (ImageNet, diffusion, LLMs) and more dramatic improvements over baselines, but shares the "oracle assumption" weakness (beta vs. known p1/p2). Comparable quality. |
| `/home/wg25r/review_agent/human_reviews_2026/4WMBSHHJEr.md` (Retain-Forget Entanglement) | 5.5 | Both tackle related entanglement problems with two/three-phase optimization. TARF addresses four scenarios vs. one, has broader experiments, and a more elegant unified framework. TARF is slightly stronger. |
| `/home/wg25r/review_agent/human_reviews_2026/xG0mQ4Xsfm.md` (REM) | 5.0 | Similar approach: new taxonomy + universal method. TARF has substantially broader experiments (ImageNet vs. CIFAR-10/SVHN only) and more striking empirical results. TARF is clearly stronger. |
| `/home/wg25r/review_agent/human_reviews_2026/jROUUKq51K.md` (MaGA) | 4.0 | MaGA has high computational overhead, limited datasets, no theory. TARF is substantially stronger in all dimensions. |
| `/home/wg25r/review_agent/human_reviews_2026/o4dTaxZ1S9.md` (Multi-domain Benchmark) | 2.5 | Pure benchmark paper with limited novelty. TARF is a much stronger contribution. |
| `/home/wg25r/review_agent/human_reviews_2026/odMc2ZRGcw.md` (BLUR) | 2.5 | Another benchmark paper; TARF is clearly much stronger. |

The paper under review sits between the 5.5 and 6.0 anchors. It shares the structural strengths of the 6.0 paper (novel framing + theory + algorithm + solid experiments) but has the β oracle assumption that parallels the "known p1/p2" weakness in the distributional unlearning work. The broader experimental scope (ImageNet, multiple architectures, LLM, diffusion) and dramatically stronger improvements over baselines argue for placement at the upper end. I assign **5.5**, reflecting that the paper makes a genuine and well-validated contribution with one practical limitation that warrants further investigation but does not undermine the core claims.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>