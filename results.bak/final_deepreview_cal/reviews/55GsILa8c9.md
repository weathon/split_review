Now I have all the information I need. Let me compile the final review.

## My Round-1 Bracket Assessment

Based on the calibration anchors:
- **Weak band (< 3.5)**: Papers scoring 2-3 — weak bio/cheminformatics papers with fundamental flaws. CausalNovo is clearly above this.
- **Middle band (3.5–7.5)**: Papers scoring 4-6 — causal representation learning papers with limited empirical validation (Causal IB at 6.0, SIT at 5.67, LSCM at 4.0). Also similar de novo papers (ReNovo at 6.5 accepted, RankNovo at 5.5 rejected). CausalNovo sits in this band.
- **Strong band (> 7.5)**: Papers scoring 8 — full accept, very strong contributions. CausalNovo is not at this level due to the methodological concerns.

**Initial bracket: 5.5 – 7.0**

## Narrowing (Round 2)

After inspecting anchors within the bracket:
- **ReNovo (6.5, accept)**: Most comparable — same field, similar empirical rigor. CausalNovo has more methodological novelty (causal framework vs RAG) and shows larger improvements. However, CausalNovo has the circular evaluation concern that ReNovo doesn't.
- **RankNovo (5.5, reject)**: Smaller improvements, more computational concerns. CausalNovo is clearly stronger.
- **Causal IB (6.0, reject)**: More theoretical but limited to synthetic experiments. CausalNovo has much stronger empirical validation.
- **NCG (6.25, accept)**: Causal graph for classification. Similar causal+neural integration.

**Final score: 6.5** — Comparable to ReNovo in overall strength, with more methodological novelty but some additional methodological concerns that bring it slightly below the strongest 7+ level.

---

## Summary

CausalNovo introduces a causality-informed framework for *de novo* peptide sequencing that learns to disentangle causal signal peaks from spurious noise in the latent space. It grounds the task in a Structural Causal Model (SCM), derives independence and sufficiency principles, and operationalizes them through a Causality Extraction Module (CEM) with information-theoretic objectives and a causal intervention that replaces noise peaks. The framework is model-agnostic and is evaluated across three strong autoregressive baselines (CasaNovo, AdaNovo, π-HelixNovo) on three public datasets.

## Strengths

- **Principled causal framework anchored in domain knowledge.** The paper formalizes de novo peptide sequencing via an SCM (Figure 2A) with explicit causal factors C and non-causal factors S, from which two actionable principles (independence, sufficiency) are derived. This goes beyond purely statistical approaches by providing a principled reason to learn noise-invariant representations, and the intervention design (replacing noise peaks identified from the theoretical spectrum) makes effective use of established domain knowledge in mass spectrometry.

- **Consistent and substantial empirical gains across all baselines and datasets.** Tables 1–2 show CausalNovo improves amino acid precision, peptide precision, and PTM precision across every baseline and dataset. Examples: CasaNovo AA precision goes from 0.525→0.635 on HC-PT (+11.0% relative), π-HelixNovo from 0.465→0.536 on Seven-species. In PTM precision on Seven-species, CausalNovo improves π-HelixNovo by +15.1% (0.362→0.513). These margins substantially exceed typical incremental gains in the field.

- **Cross-species validation confirms generalization to unseen biological domains.** Table 3 reports leave-one-out experiments on Nine-species: CausalNovo+CasaNovo outperforms CasaNovo for every single species, with average peptide precision improvement from 0.550→0.574 (+2.4pp). This is a clean test of out-of-distribution generalization.

- **Interpretable attention analysis directly ties improvements to causal focus.** Table 7 shows the proportion of predictions where all three top-attended peaks are causal rises from 19.26% (baseline) to 32.87% (CausalNovo), while the proportion ignoring causal peaks drops from 12.73% to 10.76%. This provides direct evidence linking the method's success to increased attention on signal ions.

- **Well-structured ablation isolating each component's contribution.** Table 4 cleanly validates the independence principle (+1.2pp AA precision), purification objective (+0.8pp), and symmetric training (+0.4pp). Table 5 ablates the causal intervention design, showing replace+enhance is the effective combination while random drop does not help.

## Weaknesses

### Major

- **Vulnerability evaluation partially mirrors the training intervention, weakening the headline robustness claim.** The training intervention (Sec 3.4.1) replaces noise peaks identified via the theoretical spectrum; the vulnerability evaluation (Figures 1, 3) also replaces noise peaks identified by the same method. While this is not fully circular — the evaluation varies the m/z tolerance threshold, replaces *all* noise peaks (not a fraction α), and crucially, Table 6 uses a completely different 18-ion-type identification scheme and still shows improvement — the closest analog to "robustness to unseen noise structures" is not tested with a fundamentally different perturbation type (e.g., additive Gaussian noise, intensity jitter). The cross-species validation and NSR generalization provide independent support, but the primary vulnerability analysis would be stronger with an additional, truly out-of-distribution noise perturbation.

### Minor

- **The purification objective $\max I(z_s; Y)$ has an unclear theoretical justification.** The paper states that maximizing mutual information between the non-causal representation $z_s$ and the label $Y$ "can indirectly lead to the purification of $z_c$" but does not provide a satisfactory mechanism. Standard causal disentanglement would minimize $I(z_s; Y)$ to push noise information away from the label; the paper does the opposite. While the ablation (Table 4) shows it provides a small empirical gain (+0.8pp AA precision), the paper's explanation is insufficient and potentially contradictory. A clearer justification — e.g., that the combination of independence constraint on $z_c$ and shared decoder forces genuinely causal information into $z_c$ — would strengthen the paper's theoretical foundation.

- **The intervention replacement fraction α is not reported.** Section 3.4.1 introduces "a fraction α of peaks in x_non-causal" for the replace-based perturbation, but the value of α is never specified in the main text, nor is its impact ablated. (The ablation in Table 5 uses 20% for the unrelated "drop" operation only.) This is a nontrivial hyperparameter that likely affects intervention strength and should be reported.

- **No variance or statistical significance reporting.** All results are reported as point estimates without standard deviations, confidence intervals, or multiple-seed runs. Given that many improvements (e.g., +1.4% peptide precision over SearchNovo on Nine-species) are moderate, it would be helpful to know whether these differences are statistically reliable.

### Trivial

- The attention analysis (Table 7) shows improvements, but the "0 causal peaks" rate only drops from 12.73% to 10.76% — a modest absolute improvement relative to the large shift in full-attention (19.26%→32.87%). This is not a problem, but the paper might overstate the former.

## Nice-to-Haves

- Integrating CausalNovo with a non-autoregressive architecture (e.g., π-PrimeNovo) would further strengthen the model-agnosticity claim beyond the three autoregressive baselines tested.
- A breakdown of the 2.3× training overhead (which component contributes most: the dual forward pass, contrastive loss, or both) would help practitioners assess the cost-benefit trade-off.
- An ablation of the α replacement fraction (e.g., 0.1, 0.2, 0.5) would provide useful insight into how intervention strength affects results.

## Removed Points

These points are flagged for removal — treat with caution:

- **Criticism about SearchNovo comparison being unfair** (from harsh critic). REMOVED: The paper uses published numbers from the NovoBench benchmark, which applies a consistent evaluation protocol. All methods are compared on the same benchmark. There is no evidence of different splits or pre-processing. Speculation about "slightly different splits" does not constitute a verified weakness.
- **Criticism that model-agnosticity requires more architectures** (from harsh critic). REMOVED: Showing model-agnosticity across three different autoregressive models (CasaNovo, AdaNovo, π-HelixNovo) from different labs with different design choices is sufficient evidence for the claim as stated. Extending to non-autoregressive models is a nice-to-have, not a required demonstration.
- **Strength about vulnerability analysis being primary evidence** (from strength finder, softened). REMOVED from strengths list as the vulnerability analysis has the circularity concern; the other evidence (cross-species, NSR, attention analysis) independently supports the claim.

## Novel Insights

None beyond the paper's own contributions. The reviews did not surface an observation about the paper that the paper itself does not make.

## Suggestions

1. Report the value of α used for noise peak replacement, and ideally ablate it (e.g., 0.1, 0.2, 0.5).
2. Add at least one additional robustness perturbation that is structurally different from the training intervention (e.g., adding random Gaussian noise to all peaks, or randomly masking a fraction of peaks) to demonstrate that robustness generalizes beyond the trained perturbation type.
3. Clarify the theoretical justification for $\max I(z_s; Y)$ — either provide a gradient-based or toy-example explanation of why this objective aids disentanglement rather than blurring it.
4. Report results from multiple random seeds (at least 3) with standard deviations for the main comparisons.
5. Include a discussion of the tolerance threshold γ and, if feasible, a sensitivity analysis over this parameter.

## Score and Decision

**Calibration anchors (all rounds):**

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|-----------|
| G536mmC2HL | TorSeq | 3.00 | R1 | Much weaker — molecular conformer generation, limited empirical validation |
| IZiKBis0AA | AI Derivation of Antibiotic Spaces | 3.00 | R1 | Much weaker — in silico analysis, limited novelty |
| B6B6EhC1bW | High-Order Substructure Assoc. | 2.50 | R1 | Much weaker — limited improvement, methodological concerns |
| ZyAwBqJ9aP | CypST | 2.00 | R1 | Much weaker — narrow task, limited novelty |
| qac43AwuL9 | Causal Information Bottleneck | 6.00 | R1 | Comparable — similar causal representation learning approach; CIB more theoretical with only synthetic experiments, CausalNovo stronger empirically |
| lWXedJyLuL | Causal View of Instruction Tuning | 5.67 | R1 | Slightly weaker — theoretical flaws identified, smaller-scale experiments |
| 0sO2euxhUQ | Learning Latent SCMs | 4.00 | R1 | Weaker — only synthetic experiments, no identifiability guarantees |
| tlH4vDii0E | Fine-tuning PLMs for Causal Rep. | 5.60 | R1 | Slightly weaker — NLP domain, limited novelty |
| 3cuJwmPxXj | Intervention Extrapolation | 8.00 | R1 | Stronger — theoretical identifiability, rigorous proofs, accepted paper |
| uQnvYP7yX9 | ReNovo | 6.50 | R2 | Comparable — same field, similar empirical quality; ReNovo has retrieval augmentation novelty while CausalNovo has causal framework novelty |
| 87B3zDRMjv | RankNovo | 5.50 | R2 | Weaker — more modest improvements, higher computational overhead |
| nmvmPIi185 | Neural Causal Graph | 6.25 | R2 | Comparable — causal graph for classification, similar causal+neural integration |
| 3n4RY25UWP | Disentangled SSL | 6.25 | R2 | Comparable — different domain, similar information-theoretic approach |

**Round-1 bracket: 5.5 – 7.0**  
**Round-2 narrowing:** The ReNovo anchor (6.5, accepted) is the closest comparator — same field, accepted, similar empirical quality. CausalNovo contributes greater methodological novelty (causal framework vs. retrieval) but has a more significant methodological concern (circular evaluation). This places CausalNovo at the same level as ReNovo. It is clearly stronger than RankNovo (5.5, rejected) and the causal representation learning papers with only synthetic experiments (4-6).

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>