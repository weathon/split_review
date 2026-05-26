Now let me run calibration searches to score the paper.Based on my reading of the paper and calibration analysis, I have enough information to write the review.

## Calibration Summary

**Round 1 anchors retrieved:**
- TYyzypZrgU.md (2.50, R1): Domain grounding NN — only loosely related
- 5x9kfRXhBd.md (3.00, R1): Spatial-temporal Graph Attention for forex — different domain
- fzZfju8y0g.md (3.40, R1): In-Context Neural PDE — different domain
- 2orBSi7pvi.md (3.00, R1): STDM spatio-temporal diffusion — different problem
- **FRzCIlkM7I.md (6.75, R1): EAC — Expand and Compress Continual STG Forecasting** — directly comparable; the predecessor of STBP
- URCfZ2NgaR.md (5.33, R1): SKI-CL Continual MTS — adjacent setting
- mkjKqeBXkt.md (5.67, R1): KITS — adjacent
- B1TnT6lUnU.md (4.40, R1): SKI-CL resubmission — adjacent
- fU8H4lzkIm.md (8.00, R1): PhyMPGN — different domain (PDEs)
- Cjz9Xhm7sI.md (8.00, R1): Radar nowcasting — different setting
- uKZdlihDDn.md (7.60, R1): Diffusion graph nets for fluids — different
- GRMfXcAAFh.md (8.00, R1): Oscillatory SSM — different

**Round 1 bracket:** 4.5–6.5, with EAC at 6.75 as the ceiling anchor (STBP extends it).

**Round 2 narrowing:**
- 4sJJixGIZX.md (5.00, R2): Online Continual Graph Learning — methodologically adjacent
- vXSCD3ToCS.md (4.60, R2): DynST dataset — adjacent
- rjuZyMfLSd.md (6.25, R2): Learning system dynamics without forgetting — CL, weaker similarity
- 4A9IdSa1ul.md (7.00, R2): FreDF frequency forecast — distant
- oANkBaVci5.md (6.75, R2): Simple MTS forecasting baseline — distant
- uiyljVIP0k.md (5.40, R2): S2GNN spectral spatio-temporal — close in topic
- V6uxd8MEqw.md (6.50, R2): MISA prompt-based CL — methodologically adjacent
- kVlfYvIqaK.md (6.00, R2): DyGPrompt node-time prompt dynamic graphs — methodologically adjacent

The closest comparators are EAC (6.75 accept, the direct predecessor) and S2GNN spectral STGNN (5.40 reject). STBP is methodologically more ambitious than S2GNN but has real clarity/evaluation gaps that EAC also had — yet EAC's central tuning principles were cleaner, while STBP's central CL claim (forgetting mitigation) is never directly measured. STBP's empirical gains are larger than EAC's on traffic data, but the AIR-Stream numbers and Table 1 bolding error pull credibility down. This places STBP modestly below EAC.

---

## Summary
This paper introduces STBP, a framework for continual spatio-temporal forecasting that pairs a new backbone (frequency-domain temporal filter "FreNet" plus dual-stream linear graph attention "DLGA") with a three-component, node-indexed "contextual pattern bank" (CPB) that is expanded for new nodes while the backbone is frozen after the first period. Experiments on PEMS-Stream, CA-Stream, and AIR-Stream show substantial MAE reductions on the two traffic datasets and modest improvement on AIR-Stream, plus an efficiency study supporting the linear-attention claim.

## Strengths
- **Large, consistent gains on PEMS-Stream and CA-Stream**: 21.44% and 21.93% average MAE reductions over the best baseline (Table 1, e.g. PEMS-Stream Avg MAE 12.31 vs. EAC 15.67), with standard deviations small enough to be meaningful.
- **Strong few-shot continual results**: With training set reduced to 10% in subsequent periods, STBP attains PEMS-Stream MAE 13.58 vs. EAC 16.13 and CA-Stream MAE 17.11 vs. EAC 20.94 (Table 2), supporting the stability/adaptability claim under data scarcity.
- **Efficiency story is empirically grounded**: Figure 8 directly shows the $O(N)$ DLGA variant uses substantially less GPU memory than the $O(N^2)$ ablation as node count grows on the toy dataset, while Figure 8's training-time scatter shows STBP at competitive cost to EAC despite the heavier backbone.
- **Case-study evidence the CPB encodes node structure**: Figures 3 and 6 show the pattern bank, trained only via the prediction loss, organizes nodes into clusters whose members share periodic/trend patterns, and that new-period nodes (e.g., PEMS-Stream 2017 additions) snap into existing clusters.

## Weaknesses

### Fatal
None.

### Major
- **The central catastrophic-forgetting claim is never directly measured.** Sec. 4.2 frames the CPB as the mechanism for forgetting mitigation, and Sec. 5.2/Table 1 report only "metrics averaged over all incremental periods." There is no per-period retrospective evaluation on earlier nodes, no average-forgetting (BWT) metric, and no forgetting-curve comparison against EAC/STRAP. The aggregate gain in Table 1 is fully consistent with simply having a stronger backbone plus more capacity from the CPB, with no evidence that older patterns are preserved better than in baselines. Given that "alleviating catastrophic forgetting" is challenge ❸ in the intro and a headline contribution, the absence of a forgetting-specific measurement is a substantive gap.
- **Internal inconsistency in the "frozen backbone, fine-tuned CPB" story.** Eq. 4 yields $P'_\tau \in \mathbb{R}^{N_\tau \times d}$, and the text immediately states "Only the expanded contextual pattern bank $P'_\tau \in \mathbb{R}^{N_\tau \times d}$ is fine-tuned during training" (Sec. 4.2, after Eq. 4). On the natural reading this means the entire bank — *including the rows for old nodes* — is updated every period. If true, then the claim that this strategy "ensures that the backbone retains previously acquired knowledge, while the contextual pattern bank continually adapts" elides that the node-indexed parameters that supposedly encode "relevance and heterogeneity" of historical nodes can themselves drift. The paper needs to clarify which rows are trainable and ideally ablate "fine-tune $\Delta P_\tau$ only" vs. "fine-tune all of $P'_\tau$" — both because the methodology is currently ambiguous and because this directly bears on the forgetting story.
- **AIR-Stream is incorrectly framed as a STBP win at longer horizons; Table 1 bolding appears wrong.** The paper's narrative claims STBP "outperforms all competing models" with a 2.35% AIR-Stream MAE reduction (Sec. 5.2, after Fig. 5). Inspecting the per-horizon AIR-Stream rows: RMSE h=6 is STBP 39.81 vs. EAC 39.63, and RMSE h=12 is STBP 44.97 vs. EAC 44.65 — EAC's numbers are lower, yet STBP is bolded as "best" in both rows (Table 1, AIR-Stream RMSE rows for h=6 and h=12). MAE h=12 is also a near-tie (28.28 vs. 28.52). At minimum the bolding is incorrect; more importantly, the headline framing should acknowledge that long-horizon air-quality forecasting essentially ties EAC. The current text averages this away.
- **DLGA formulation is unclear in the main text.** Eq. 9 writes attention as $\phi(Q)(\phi(K)^\top V + \phi(P_\tau^{(2)})^\top V)$, omitting the normalization denominator that linear attention (Katharopoulos et al. 2020) requires; the text then says "$\phi(\cdot)$ denotes a random feature mapping, with Softmax used for approximation in our implementation" (Sec. 4.3 after Eq. 9). Random features approximate softmax, not the reverse, so the wording is contradictory and leaves it ambiguous whether the implemented module is (a) softmax-normalized attention with a special pattern-bank key, (b) random-feature linear attention, or (c) a hybrid. The efficiency claim ("quadratic to linear") and the "dual-stream" novelty depend on which one is actually used, so this is a substantive clarity gap, not stylistic.

### Minor
- **No component-wise ablation of the three-stream CPB.** $P_\tau^{(0)}$ (gating bias), $P_\tau^{(1)}$ (gating scale), and $P_\tau^{(2)}$ (attention key) are described as serving distinct roles, but the ablation in Fig. 4 only removes the bank wholesale (via "w/o Backbone" or "Retrain/Online"). A $P^{(0)}/P^{(1)}/P^{(2)}$ leave-one-out would convert "we designed three streams" into "each stream matters."
- **FreNet's marginal contribution is not isolated.** "w/o DLGA" exists, but the only experiment that removes FreNet is "w/o Backbone," which simultaneously swaps both modules for CNN+GCN. The text in Sec. 5.3 states FreNet "makes a notable contribution," but no figure/table shows this.
- **The t-SNE evidence is illustrative, not validating.** Figures 3 and 6 show clusters in the learned bank, which is a generic outcome for any node-indexed trainable embedding optimized for forecasting. The clusters show structure but do not specifically validate the *continual-learning* function of the bank (i.e., that old-node patterns are preserved across $\tau$). The text in Sec. 4.2 should temper "validates" to "is consistent with."
- **Figure 4 axis values are reconstructed via parsing; the ablation chart itself appears to be a bar chart in the original.** This is fine evidentially, but it means the absolute reported numbers (e.g., "Our ~15") are approximate, which limits how precisely one can compare them to Table 1.

### Trivial
None worth listing.

## Nice-to-Haves
- Per-period forgetting evaluation on test data from earlier periods, plus a forgetting-curve comparison against EAC and STRAP.
- A "fine-tune $\Delta P_\tau$ only" vs. "fine-tune all of $P'_\tau$" comparison.
- An honest decomposition of AIR-Stream gains by horizon, with discussion of why the gap closes at longer horizons.
- A clean, normalized derivation of DLGA in either the random-feature or softmax-linearized form, with the main-text equation matching the appendix derivation.
- A FreNet-only ablation, distinct from the full backbone replacement.

## Removed Points
These points are flagged to be removed, treat them with caution.

- **Comparison-protocol asymmetry (retrain-from-scratch GWNet/STID vs. online-finetuned iTransformer).** The harsh critic flagged this, but the paper explicitly states this follows the protocol of prior work (Chen & Liang, 2025), and the asymmetry handicaps the conventional baselines, not STBP — i.e., the comparison against the relevant class of CSTF baselines (EAC, PECPM, STRAP) is fair. Per the hard rules, asymmetric setups that favor baselines should not be counted against the authors.
- **"The toy-dataset efficiency comparison should be repeated on PEMS-Stream/CA-Stream at scales where $O(N^2)$ is feasible."** Reasonable nice-to-have, but presentational rather than substantive; the toy dataset directly shows the asymptotic claim, and quadratic attention on full PEMS-Stream is impractical.
- Strength Finder's "Frozen backbone + pattern bank expansion outperforms full fine-tuning" — partially valid as a strength but the comparison against PECPM/TrafficStream is confounded by backbone differences; this overlaps with the empirical headline strength already kept.

## Novel Insights
None beyond the paper's own contributions. The combination of a frequency-domain temporal filter, linear graph attention, and a multi-stream pattern bank is a reasonable architectural recipe but does not surface a finding that reframes the CSTF problem beyond the EAC/STRAP/PECPM line of work.

## Suggestions
- Add explicit per-period retrospective evaluation (test on period-$\tau'$ test data using the model at period $\tau \geq \tau'$) plus a forgetting metric like average BWT, and report STBP vs. EAC and STRAP forgetting curves.
- Audit Table 1 bolding for AIR-Stream RMSE rows at h=6 and h=12 — both currently bold STBP despite EAC having the lower numerical value.
- Replace the "$\approx$ ... Softmax used for approximation" wording in DLGA with a clean derivation: pick one formulation, write the normalized form $\phi(Q)\bigl(\phi(K)^\top V + \phi(P_\tau^{(2)})^\top V\bigr) / \phi(Q)\bigl(\phi(K)^\top \mathbf{1} + \phi(P_\tau^{(2)})^\top \mathbf{1}\bigr)$ (or whichever is implemented), and align it with the appendix.
- Run a CPB component-wise leave-one-out across $P^{(0)}$, $P^{(1)}$, $P^{(2)}$ and a FreNet-only ablation.
- Reframe the AIR-Stream narrative: at h=3 the gain is large; at h=6 and h=12 it is essentially tied. Engage with *why* (low-frequency air-quality signals, long-horizon prediction difficulty).
- Specify clearly whether the entire $P'_\tau$ is fine-tuned each period or only $\Delta P_\tau$; if the former, justify why old-node prompts are allowed to drift.

---

### Axis-level appraisal
- **Originality:** Moderate. The components (FFT-based filter, linear attention, prompt bank) are individually well-known; the contribution is the specific combination and the three-stream CPB integrated with linear attention in a CSTF setting. This is a sensible extension of EAC/STRAP rather than a conceptually new approach.
- **Importance of question:** Solid. Continual forecasting on streaming graphs is a real, well-defined problem with practical motivation.
- **Are claims well supported:** Partially. The forecasting-accuracy and scalability claims are supported on PEMS-Stream/CA-Stream; the catastrophic-forgetting claim — explicitly listed as a core contribution — is not directly measured; the AIR-Stream "outperforms all" framing is at odds with the long-horizon table values.
- **Soundness of experiments:** Adequate on traffic; weaker on AIR-Stream framing; ablations are incomplete (no FreNet-only, no CPB-component-wise).
- **Clarity:** Mostly clear at the framework level. The DLGA formulation is the main exception and is significant.
- **Value to research community:** A reasonable next step in the CSTF line; would be more valuable with explicit forgetting metrics and a cleaner method exposition.

The paper is closer to EAC (6.75) in scope and contribution but somewhat below it in evidence quality (forgetting not measured, Table 1 bolding error, DLGA ambiguity, missing component ablations). Among round-2 anchors, it sits above S2GNN (5.40), Online Continual Graph Learning (5.00), and SKI-CL (5.33) — its empirical case is stronger and the problem is well-motivated — but below MISA (6.50) and DyGPrompt (6.00) in clarity and below EAC (6.75) in evidentiary support for its CL claim. That places it around 5.0–5.5.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>