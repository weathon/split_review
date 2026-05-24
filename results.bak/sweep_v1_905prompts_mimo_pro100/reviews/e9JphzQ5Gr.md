Now I have all the information needed. Let me write the consolidated review.

## Summary

This paper proposes CaPT, an asymmetric-modalities co-training framework that integrates CLIP into semi-supervised learning by jointly training a fully fine-tuned vision-only network (UPM) with an adapter-tuned CLIP model (MPM), using entropy-weighted co-pseudo labels to facilitate bidirectional knowledge exchange. The paper identifies and theoretically formalizes the label-dependency problem in SSL, then demonstrates that CaPT achieves state-of-the-art performance across multiple benchmarks with minimal efficiency overhead (8% memory, 11% time increase over FreeMatch).

## Strengths

- **Strong empirical performance with large margins in extreme low-label regimes**: CaPT outperforms the second-best method by 21.38% on CIFAR-100 and 9.33% on ImageNet (10 labels/class). Importantly, when labeled samples per class drop from 2→1, FreeMatch collapses from 78.60%→61.13% and RegMixMatch from 80.74%→60.49%, while CaPT maintains 82.51% (Table 3), demonstrating genuine robustness to label scarcity rather than marginal improvement.

- **Minimal efficiency overhead**: Table 4 shows CaPT requires only 0.1044 sec/iter and 5050 MiB vs. FreeMatch's 0.0939 sec/iter and 4676 MiB—substantially less than RegMixMatch (0.1484 sec/iter, 6578 MiB) while achieving higher accuracy (84.83% vs. 80.74%). This makes the CLIP integration practical, not just theoretically interesting.

- **Cross-modal complementarity visually demonstrated**: Figure 3 provides concrete evidence that ViT(CLIP) attends to different object regions (e.g., comb vs. eye/beak on the rooster) compared to two differently-initialized pure-vision ViTs, which produce similar attention patterns. This directly supports the claim that asymmetric modalities avoid the pattern-homogeneity bottleneck of co-training identical architectures.

- **Well-structured ablation validating each design component**: Table 6 isolates contributions systematically—removing adapter-tuning (CaPT-Deb) causes −12.73% on EuroSAT; removing co-training to only MPM causes −16.51% on CIFAR-100; removing entropy weighting for equal weights loses 0.87%. Each ablation targets a specific design claim.

- **Adapter-tuning effectively mitigates CLIP's class bias**: Figure 5 shows raw CLIP predictions are highly skewed on EuroSAT (peak ~0.25 for one class), while adapter-tuned CLIP produces near-uniform distributions. This is reinforced by the CaPT-Deb ablation result, making it a validated design contribution.

## Weaknesses

### Fatal

None.

### Major

- **Missing critical baseline: CLIP pseudo-labels supervising the unimodal network without co-training** — The paper's core contribution is the co-training framework, but the only ablation removing co-training entirely is "only UPM" (which removes CLIP knowledge, not co-training) and "only MPM" (which removes the vision branch). A natural and critical baseline is: use CLIP's zero-shot or adapter-tuned predictions as pseudo labels to directly supervise the unimodal network, *without* bidirectional co-training. This would isolate whether the co-training mechanism provides value beyond simply having access to CLIP's predictions. The current ablations cannot distinguish "co-training helps" from "having CLIP's prior knowledge helps," which is the central claim the paper needs to establish. Without this baseline, the reader cannot assess the contribution of the co-training design itself. (Both reviewers flagged this concern; the harsh critic's point is valid and grounded in the experimental design.)

- **Comparison fairness concern with vision-only baselines in Tables 1–3** — All primary comparisons (FixMatch, FreeMatch, RegMixMatch, etc.) use vision-only models without access to CLIP. While the paper does include adapter-tuned CLIP and CLIP zero-shot as additional rows in Table 1 (e.g., adapter-tuned CLIP alone achieves 74.90% on CIFAR-100 with 2 labels), these are listed as supplementary information, not as competitive baselines. In Table 2 (ImageNet), Table 3 (one-label-per-class), no CLIP baselines are reported at all. The paper should acknowledge more prominently that some of CaPT's gains come from the sheer power of CLIP's pretrained representations, and that the comparison is not fully controlled. However, this is *not* a fatal flaw: the paper's explicit contribution *is* integrating CLIP into SSL, so comparing against non-CLIP methods is appropriate for showing the value of that integration—the issue is more about positioning and transparency than experimental validity.

### Minor

- **Theoretical contribution does not directly connect to the method mechanism** — Theorem 1.1 provides a clean bound on pseudo-label error as a function of labeled data quantity/quality (Equation 1). However, CaPT's solution is to import CLIP's representation space rather than to improve pseudo-labels within the same space that the theorem analyzes. The theorem motivates "use something other than the labeled data" but does not specifically motivate the asymmetric co-training architecture. This makes the theory a useful motivational observation rather than a direct justification of the design.

- **FGVCAircraft failure reveals domain-dependency limitation** — Table 5 shows CaPT loses to FreeMatch with 5 labels/class on FGVCAircraft (50.12% vs. 51.43%) while CLIP zero-shot achieves only 18.97%. The paper relegates this to an appendix, but it reveals that CaPT's effectiveness depends on CLIP having useful prior knowledge for the target domain. This is a significant practical limitation that deserves more prominent discussion, especially given that the conclusion claims a "future-proof framework."

- **Table 3 reports no standard deviations** — The one-label-per-class experiments (CIFAR-10, CIFAR-100, EuroSAT) report only point estimates, while Table 1 reports standard deviations for all methods. Given the extreme sensitivity of one-label settings to the specific labeled samples chosen (as the paper's own Figure 1a demonstrates with Set 0 vs. Set 2), omitting variance measures here is a notable gap.

### Trivial

None.

## Nice-to-Haves

- Showing actual weight trajectories (Γᵃ and Γᵇ) during training would transform the intuitive argument about "CLIP-early, UPM-later" into empirical evidence. This is currently stated but not demonstrated.
- The "portability" claim (contribution 2) would be stronger if tested with at least one other VLM or encoder size beyond ViT-B/32.
- A direct comparison with DebiasPL (which is described as a related approach but never quantitatively evaluated) would strengthen the positioning.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"Cherry-picking the 21.38% headline number"**: The abstract explicitly states this comes from "the one-label-per-class setting." This is disclosed, not cherry-picked. The number is real and the setting is specified.
- **"Missing DebiasPL quantitative comparison"**: While desirable, DebiasPL is a related-work reference, and the paper's ablation CaPT-Deb partially addresses the comparison by disabling adapter-tuning. This is a nice-to-have, not a critical gap.
- **"Feature-level Mixup not validated against input-level augmentation"**: The paper justifies this choice explicitly for efficiency (Section 3.2.2: "feature-level strong augmentation... avoids the need to construct another high-resolution version of the unlabeled image"). This is a reasonable design tradeoff, not an unvalidated assumption.
- **"Portability claim unsupported"**: The paper tests on multiple datasets spanning different domains (natural images, remote sensing, fine-grained recognition) with a single CLIP architecture, which is a reasonable scope for a single paper.
- **Style/formatting criticisms**: These are parser artifacts, not paper issues.

## Novel Insights

The paper provides a genuine empirical insight: existing SSL methods suffer a sharp phase transition when labeled data drops below a threshold (demonstrated in Figure 1a's performance cliff from 4→1 labels per class), and this is because the utility of unlabeled data is tightly coupled to labeled data quality (formalized in Theorem 1.1 and demonstrated in Figure 1c). The solution—importing prior knowledge from a vision-language model—is not surprising in hindsight, but the paper's value lies in clearly articulating the failure mode, providing theoretical backing, and engineering an efficient integration. The observation that cross-modal diversity (Figure 3) improves co-training over within-modal diversity is a genuine contribution to the co-training literature.

## Suggestions

- **Add the "CLIP pseudo labels → vision model" baseline** (no co-training). If CaPT beats this by a meaningful margin, the co-training design is justified. If the margin is small, reframe the contribution as "efficiently leveraging CLIP priors in SSL" rather than emphasizing the co-training mechanism.
- **Report standard deviations for Table 3** and discuss sensitivity to the specific labeled samples chosen.
- **Move the FGVCAircraft discussion from Appendix N to the main paper** and frame it as a known limitation alongside a discussion of when CLIP's prior is likely to be informative.
- **Soften the "break the label dependency" framing** to something like "leveraging vision-language pretraining to mitigate SSL's label dependency." This is more defensible and the paper's results are strong enough to stand on their own merits without overclaiming.

## Score and Decision

**Evaluation on axes:**
- **Originality**: Moderate. Co-training CLIP with a vision model for SSL is a reasonable but not groundbreaking idea. The asymmetric-modalities design and entropy-weighted fusion are well-crafted but incremental engineering contributions.
- **Importance of research question**: High. SSL in extreme low-label regimes is a practically important problem, and demonstrating that CLIP priors can unlock unlabeled data in this regime is valuable.
- **Claims well-supported**: Mostly. The empirical results are strong and well-reproduced, but the central claim that co-training (vs. simply having CLIP) is essential remains unverified due to the missing baseline.
- **Soundness of experiments**: Good. Extensive benchmarks, good ablations, efficiency analysis. The missing CLIP-pseudo-label baseline is the most significant gap.
- **Clarity of writing**: Good. Well-structured, clear motivation, informative figures.
- **Value to community**: Moderate-high. The framework and results are useful for practitioners integrating foundation models into SSL.

**Calibration report:**

*Round 1 anchors:*
- LLM2CLIP (HfJxXbXlYJ, avg 3.00, round 1): Rejected CLIP extension paper. CaPT is substantially stronger.
- Multi-Vision Multi-Prompt (j1FLTvgyAh, avg 2.50, round 1): Rejected few-shot CLIP paper. CaPT is much stronger.
- DIPS / Rethinking pseudo-labeling (eSO9quCgmz, avg 5.00, round 1): Rejected SSL paper with data-centric insights. CaPT has stronger empirical results and a more complete framework.
- SemiReward (dnqPvUjyRI, avg 6.00, round 1): Accepted SSL framework. Similar contribution level but CaPT has larger margins and addresses a more extreme setting.
- BOPL (AEi2wyAMyb, avg 5.33, round 1): Rejected bi-level optimization SSL paper. CaPT is substantially stronger.
- Interpreting CLIP (5Ca9sSzuDp, avg 8.00, round 1): Accepted CLIP analysis paper. More novel insights than CaPT.
- Compositional Entailment Learning (3i13Gev2hV, avg 8.00, round 1): Accepted VLM paper with strong novelty. Stronger contribution than CaPT.

*Round 1 bracket: 5.0–7.5*

*Round 2 anchors:*
- VITask (lja4JMesmC, avg 6.25, round 2): Rejected VLM adaptation paper. CaPT has stronger empirical results and a cleaner framework.
- MLL / VLM Selection (vG9dVXwXQV, avg 6.33, round 2): Rejected VLM selection paper. CaPT is more focused and empirically stronger.
- Concept Drift (b20VK2GnSs, avg 7.00, round 2): Accepted MLLM adaptation paper with new dataset and theoretical framework. More novel than CaPT but with more experimental concerns. CaPT is cleaner empirically but less novel conceptually.
- Dynamic Multimodal Evaluation (X1OfiRYCLn, avg 7.50, round 2): Accepted evaluation benchmark paper. More novel contribution.

*Round 2 bracket: 6.0–7.0*

**Positioning**: CaPT is clearly stronger than SemiReward (6.00) and the VLM adaptation papers (6.25, 6.33) due to its stronger empirical results, better ablations, and clearer contribution. It is slightly below Concept Drift (7.00) due to comparison fairness issues and the missing baseline that would establish co-training's contribution. The paper is a solid systems contribution with strong results, but the overclaimed framing and missing experiment prevent it from reaching the 7.0+ range.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>