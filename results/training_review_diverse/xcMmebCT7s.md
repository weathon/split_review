Now I have a thorough understanding of the paper and can verify reviewer claims systematically. Let me construct the final review.

---

## Summary

This paper addresses generalization in ML-based protein-protein interaction (PPI) design. The authors make three contributions: (1) **PPIRef**, the largest non-redundant dataset of 3D PPI interfaces (46K unique interfaces from 322K raw PDB entries), enabled by (2) **iDist**, a fast algorithm for PPI structural deduplication (480× faster than iAlign with 99% precision/97% recall); and (3) **PPIformer**, an SE(3)-equivariant transformer pre-trained on PPIRef via masked modeling and fine-tuned for ΔΔG prediction using a log-odds-ratio formulation. The model achieves strong performance on non-leaking splits of SKEMPI v2.0 and two independent case studies (SARS-CoV-2 antibody optimization and staphylokinase engineering).

---

## Strengths

1. **Largest non-redundant PPI dataset (PPIRef).** PPIRef50K contains 46K unique interfaces — roughly 5–10× more than DIPS (9K) or MaSIF-search (5K) — and demonstrably removes structural redundancy that plagued prior datasets. The 53–88% test-set leakage the authors identify in existing splits (Section 3.2) makes clear that earlier evaluations were optimistically biased. This is a substantial, independently useful resource.

2. **iDist: scalable PPI deduplication with validated accuracy.** iDist is 480× faster than the gold-standard iAlign while achieving 99% precision and 97% recall (Section 3.1). Without this efficiency gain, constructing a dataset the size of PPIRef with structural deduplication would be infeasible for academic groups. This is a well-engineered contribution in its own right.

3. **Log-odds-ratio fine-tuning with inherent antisymmetry.** Unlike prior ML methods that require two forward passes to enforce ΔΔG(wt→mut) = −ΔΔG(mut→wt) (e.g., RDE-Network), PPIformer's log-odds-ratio prediction satisfies this property by construction (Equation 4). This is a clean, principled design choice regardless of how strongly one interprets the thermodynamic motivation.

4. **Solid empirical results on non-leaking evaluations.** On five held-out PPIs from SKEMPI v2.0 with verified structural non-redundancy, PPIformer outperforms all ML baselines in 6 of 7 metrics (Spearman 0.44 vs. next-best GEMME 0.38, RDE-Network 0.24). The staphylokinase case study (Table 4) is notably strong: P@10% = 87.5% vs. next-best 62.5%.

5. **Coarse-grained representation with deliberate design rationale.** The choice of Cα positions and virtual Cβ directions (ignoring side-chain rotamers) is explicitly motivated by interface flexibility (Section 4.1). This avoids overfitting to static crystal-structure conformations and suits the mutation-prediction task.

---

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Miscalculated headline improvement.** Line 90 claims "a 183% relative improvement... compared to... RDE-Network, as measured by Spearman correlation." The correct calculation is (0.44 − 0.24) / 0.24 ≈ 83%. This is a 100-percentage-point overstatement of a headline number. While the method still outperforms RDE-Network, this error inflates the reported gain and should be corrected.

2. **Baseline retraining protocol not stated in main text.** The paper defers baseline training details to the appendix (Section 3, referenced as `\Cref{sec:baselines}`). Whether RDE-Network, GEMME, ESM-IF, and MSA Transformer were retrained on the same non-leaking training folds (or, for methods that cannot be retrained, evaluated in a way that accounts for data distribution shift) is a central methodological question. The main text should state this explicitly. The appendix almost certainly addresses it, but the omission from the main text makes the evaluation harder to assess at a glance. *(Note: this is a presentation concern, not a fatal flaw — see Removed Points for the related but overblown criticism.)*

3. **No limitations section.** The paper closes with a conclusion but includes no discussion of its own limitations. Important points to acknowledge include: (a) flex ddG still achieves higher correlation (0.55) than any ML method (Table 2); (b) the iDist recall of 97% means a small fraction of near-duplicates may persist between train and test; (c) the SARS-CoV-2 case study results are mixed — PPIformer detects 2/5 favorable mutations in the top-10% vs. 3/5 for some baselines. Adding a limitations paragraph would strengthen the paper's scientific rigor.

4. **Thermodynamic motivation is heuristic, not a derivation.** Equations 2–4 connect ΔΔG to log-probability ratios via the decomposition ΔΔG = RT(log K_wt − log K_mut). The paper then proposes to estimate log K_wt as Σ log p(ĉ_i = c_i | c_{\M}) and similarly for the mutant. While this is a plausible heuristic (and the log-odds ratio is a standard zero-shot scoring method in protein language modeling), equating masked-model probabilities to equilibrium constants is not thermodynamically justified — the derivation assumes a direct correspondence without argument. The paper hedges somewhat ("we reason that during pre-training PPIformer learns the correlates of ΔG values," line 163) but the abstract and introduction frame this as "thermodynamically motivated" more strongly than the derivation supports. This does not invalidate the method (it works empirically), but the framing should be dialed back to avoid overclaiming.

5. **Residual leakage risk from 97% iDist recall.** The paper reports 97% recall for iDist against iAlign, meaning ~3% of near-duplicates may go undetected. The authors do not quantify the minimum iDist distance between the five test PPIs and any training PPI, nor discuss whether any test PPI could be a near-duplicate below the threshold. Given that the paper's central evaluation claim rests on non-leaking splits, a brief empirical check would be reassuring. This is a minor oversight.

### Trivial

- None that survive filtering. Minor labeling conventions and presentation details are parser artifacts, not author errors.

---

## Nice-to-Haves

- **Ablation of pre-training data size.** An experiment showing performance with, e.g., 25%, 50%, and 100% of PPIRef (or without pre-training at all) would strengthen the claim that larger non-redundant data drives improvement.
- **Sensitivity of iDist threshold.** Showing how downstream ΔΔG prediction performance varies with stricter/looser deduplication thresholds would inform how much redundancy actually hurts generalization.
- **Full baseline retraining details in main text.** A one-sentence statement in Section 5.1 clarifying the retraining protocol would preempt the central objection without requiring readers to consult the appendix.

---

## Removed Points

These points were flagged for removal with justification:

1. **"Evaluation fairness — baselines might not have been retrained."** While the methodological concern is legitimate, the reviewer's framing that "Without explicit confirmation... the central claims... are unverifiable" is an overstatement that ignores the appendix (Section 3, referenced in the paper as `\Cref{sec:baselines}`). The paper defers baseline details to the appendix, which the parser strips. The concern is kept in Minor (point 2 above) but at reduced severity. The "fatal collapse" framing is removed as disproportionate.

2. **"SARS-CoV-2 results are less one-sided than claimed."** The paper already acknowledges this honestly: "Our model detects 2 out of 5 annotated mutations... The best among the other methods detect 3 out of 5 mutations. However... PPIformer achieves superior performance when considering the ranks of all 5 mutations collectively." The paper does not claim superiority on every metric. This criticism misreads what the paper actually states.

3. **"Table label `\label{fig:skempi_test}` despite being a table."** This is a LaTeX naming convention issue — pure formatting. Removed per instructions.

4. **"The 183% claim is miscomputed."** Kept in Minor — it is a real numerical error, not a formatting issue.

5. **Missing appendix content / missing related works.** Removed per instructions (parser strips appendix; we cannot confirm missing references).

---

## Novel Insights

Beyond the paper's own contributions, the most notable meta-insight is the quantification of data leakage in existing PPI splits: 53–88% of test examples have near-duplicates in training (Section 3.2). This finding, corroborated by the companion paper (Bushuiev et al., 2024), suggests that many published performance numbers in the PPI mutational prediction literature are optimistically biased, and that the gap between ML methods and physics-based simulators (flex ddG) may be smaller than previously believed when leakage is controlled for. The paper's own results (ML still lagging flex ddG on non-leaking splits) reinforce this sobering picture.

---

## Suggestions

1. **Correct the 183% → ~83% relative improvement.** This is a clear factual error in a headline number.
2. **Add a limitations paragraph** acknowledging (a) flex ddG outperforms ML methods on the non-leaking split, (b) iDist's 97% recall implies residual leakage risk, and (c) the SARS-CoV-2 results are mixed on the top-10% criterion.
3. **Move baseline retraining confirmation to the main text.** One sentence stating that all baselines were retrained on the same folds (or explaining the protocol for methods that cannot be retrained) would strengthen the evaluation.
4. **Dial back the thermodynamic framing.** Present the log-odds-ratio as a practical heuristic that naturally enforces antisymmetry, rather than a thermodynamically derived estimator. The method's empirical performance stands on its own without this framing.

---

## Score and Decision

**Originality:** 7/10 — iDist and PPIRef are genuinely useful resources; the PPIformer architecture adapts Equiformer with masked modeling to the PPI domain, which is novel in application though architecturally straightforward.

**Importance of research question:** 9/10 — Reliable PPI design is a central challenge in protein engineering and therapeutic development. The focus on generalization and non-leaking evaluation addresses a real and recognized problem.

**Claims supported:** 6.5/10 — The core empirical claims are broadly supported, but the miscalculated headline number (183% vs. 83%) and the absence of a limitations section weaken the presentation. The thermodynamic framing overclaims slightly.

**Soundness of experiments:** 7.5/10 — The non-leaking evaluation is carefully constructed. The case studies are appropriate. The baseline retraining protocol should be explicit in the main text, but is likely detailed in the appendix.

**Clarity of writing:** 7/10 — Generally clear and well-structured. The main weakness is the lack of a limitations section and the overconfident thermodynamic framing.

**Value to community:** 8/10 — PPIRef and iDist are immediately useful resources. The non-leaking evaluation protocol sets a higher standard for future work.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>