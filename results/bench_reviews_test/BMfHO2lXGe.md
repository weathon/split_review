## Summary
ProtMamba is a 107M-parameter, homology-aware but alignment-free protein language model built on the Mamba state-space architecture, trained on concatenated homologs with a fill-in-the-middle (FIM) objective. The paper claims competitive ProteinGym fitness prediction (ρ = 0.406, 0.432 with retrieval) at ~85–100× faster inference than PoET, and demonstrates conditional generation, inpainting, and activity prediction on the chorismate mutase family.

## Strengths
- **Real and substantial efficiency contribution.** ProtMamba scores all of ProteinGym in ~7–10 min vs. PoET's ~10h (single) and ~6 days (ensemble) on the same hardware (Table 1). For high-throughput variant scoring this is a practical, not just academic, win.
- **The FIM objective is genuinely useful and well-evaluated.** FIM scoring (ρ = 0.406) outperforms ProtMamba's own AR scoring (ρ = 0.367) on identical weights, and FIM scores all 19 single-site mutations in a single forward pass — a clean 20× reduction (Section 3.2).
- **Sequence-level positional embeddings inside Mamba** are a principled modification motivated by FIM's need to localize masked patches; the design enables controllable inpainting length (Section 2.2, Figure 1).
- **Long-context conditioning empirically helps.** Figure 2 shows FIM perplexity decreases monotonically with the number of homologs in context, with steeper gains for harder (longer) masked patches, and chorismate-mutase activity prediction plateaus around 75 context sequences (Table 2 right panel) — a meaningful sanity check on the long-context claim.
- **Chorismate mutase analysis** (Table 2) credibly shows that context choice (active-only vs any variant) materially changes predictions — a clean demonstration of prompt-style conditioning as an alternative to fine-tuning, beating DCA and logistic regression from Russ et al. 2020.

## Weaknesses

### Fatal
None.

### Major
- **Table 3 generation comparison is across non-matched protein families.** Section 3.4/Table 3 caption is explicit: ProtMamba's 250 sequences come from "different cluster[s] in our test set," while EvoDiff-MSA, MSA-Transformer, and Potts numbers are "retrieved from the Zenodo archive associated to the EvoDiff paper... generated each from a different cluster of the EvoDiff validation set." Natural-sequence pLDDT on ProtMamba's test clusters is 0.77, which is itself near ProtMamba's reported 0.75, suggesting the cluster-level confound is at least as large as any model-vs-model gap. Since this table is the principal evidence for the abstract's homolog-conditioned generation claims, the comparison as constructed does not establish state-of-the-art generation.
- **The most relevant baseline (PoET) is absent from the generation evaluation (Table 3) and from chorismate mutase (Table 2).** PoET is the direct architectural analogue (homology-aware, autoregressive over concatenated unaligned homologs) and is the paper's main comparator throughout Tables 1 and the discussion of FLOPs/speed. Omitting it from the conditional-generation comparison while including only alignment-based and older baselines leaves the most informative comparison unmade.
- **Figure 3 selects the 100 lowest-perplexity sequences out of 2500 generated (top 4%) and compares them to an unfiltered sample of 100 natural sequences.** Figure S15 itself shows that ProtMamba's perplexity correlates strongly (|r| > 0.57 avg) with HMMER, pLDDT, pTM, and Hamming distance — so top-k selection by perplexity mechanically inflates apparent quality on exactly those metrics. A fair version would (a) compare unfiltered generations to unfiltered naturals, (b) apply matched perplexity filtering to naturals, or (c) report a quality-vs-acceptance-rate curve.

### Minor
- **"ProtMamba outperforms ESM-2 150M" is not a controlled comparison.** ProtMamba sees ~200 homologs at inference time; ESM-2 sees only the wild-type. The relevant control would be ESM-2 with retrieval. The paper's framing in §3.2 is somewhat confounded; the comparison to MSA Transformer and Tranception is more apt.
- **Accuracy/speed trade-off vs. PoET should be stated explicitly.** ProtMamba is ~85× faster than PoET (single) but ~9% lower in Spearman (0.406 vs 0.447). The discussion frames this as Pareto-favorable; for many practical uses it is, but the accuracy gap should be acknowledged alongside the speed gain in the abstract/discussion rather than only in the limitations.
- **The §3.1 long-context narrative is somewhat undercut by Figure S5,** where per-sequence perplexity *rises* at 2¹⁷ tokens (the max training context). The authors attribute this to insufficient training, which is plausible, but the unbounded "very long context" framing should be tempered.
- **2020-era baselines on chorismate mutase.** Table 2 compares only to DCA energy and logistic regression from Russ et al. 2020. Adding PoET or an MSA Transformer baseline on this same dataset would make the comparison much more informative.

### Trivial
- The "10–60× speedup vs PoET" framing conflates ensemble (148h) and single (~10h) PoET timings; the actual factor against single-PoET is ~85×.
- Sequence-length warm-up "revert-to-checkpoint if loss doesn't drop in 10 steps" is an unusual training trick; quantifying how often it fired would help interpret the FLOP comparison to ESM3 ("8.5× more tokens per FLOP").

## Nice-to-Haves
- A per-family breakdown of Table 3 (and ideally regeneration of EvoDiff-MSA / MSA-Transformer on ProtMamba's test clusters, or vice versa) would directly resolve the cross-family concern.
- A perplexity-vs-quality curve for generated sequences across the full 2500 samples, rather than only the top decile.
- A direct held-out inpainting evaluation (e.g., recovery of masked patches in held-out natural sequences) — currently inpainting quality is inferred only indirectly through fitness prediction.
- ESM-2 with retrieval as a baseline to make the "homology helps" claim a controlled experiment.

## Removed Points
These points are flagged to be removed; treat them with caution.

- *"SLW callback FLOP accounting"* (harsh critic, §2.2): kept as a trivial nit only. The headline efficiency comparison is to ESM3 which is robust to small accounting differences; this is not a substantive concern.
- *Strength: "Practical training recipe on modest hardware."* This is real but somewhat generic and overlaps the efficiency strength. Demoted/merged rather than listed separately.

## Novel Insights
None beyond the paper's own contributions. The genuinely novel observations come from the paper itself: FIM applied to concatenated homologs in a Mamba backbone, and the FIM-vs-AR within-model comparison showing FIM scores better (0.406 vs 0.367) — an analysis most autoregressive PLM papers cannot do.

## Suggestions
- Rerun Table 3 with matched clusters (regenerate EvoDiff baselines on ProtMamba clusters, *or* generate ProtMamba sequences from EvoDiff clusters). This is the single most important fix.
- Add PoET to Table 3 and Table 2.
- Replace Figure 3 with either (a) unfiltered vs unfiltered or (b) perplexity-filter-matched comparisons; add a quality-vs-acceptance-rate plot.
- Soften the abstract/discussion claim of "outperforms state-of-the-art EvoDiff-MSA" pending the matched-cluster comparison. The fitness-prediction speed/accuracy story alone is a strong contribution.
- Acknowledge the ~9% Spearman gap vs PoET in the abstract alongside the speed gain.

---

**Evaluation on requested axes.** *Originality:* moderate-to-high — first Mamba-based homology-aware PLM with FIM training over concatenated homologs; the architectural recipe is novel. *Importance:* high — fast homology-aware variant scoring is a real practical need. *Claim support:* mixed — fitness-prediction claims are well-supported and honestly reported; generation claims (the abstract-level "outperforms" framing) are not adequately supported by Table 3 as designed. *Soundness:* fitness-side experiments are sound; generation-side has the cross-family confound and top-4% selection issue. *Clarity:* generally good; methods and ablations are well-explained. *Value to community:* substantive — speed gains plus the FIM scoring trick are immediately useful even setting the generation claims aside.

## Score and Decision

**Calibration anchors compared against:**
- `PSiijdQjNU.md` (avg 7.5) — protein family-conditioned generation that *did* compare to PoET/EvoDiff. ProtMamba is below this because its core generation comparison has the cross-family confound the high-scoring paper avoided.
- `E48QvQppIN.md` (avg 7.25) — evolutionary-aware protein generation; high mark for rigorous benchmarking. ProtMamba's fitness side approaches this rigor; generation side does not.
- `ua5MHdsbck.md` (avg 7.0) — protein design via preference optimization; well-supported claims. Comparable in ambition but more rigorous in evaluation.
- `OzUNDnpQyd.md` (avg 7.0) — structure language models. Not a tight topical match.
- `xuxYaBMd9F.md` (avg 5.4) — state-space transformer for long context, rejected for empirical gaps. ProtMamba is stronger: more concrete domain wins, better efficiency story.
- `HcY3fbVDqa.md` (avg 4.75) — state-space over alignments, rejected for limited experiments. ProtMamba clearly above this — wider eval and stronger headline efficiency.
- `LoXJlAW3gU.md` (avg 5.17) — protein-LM diffusion generation, rejected. Comparable to ProtMamba's generation half alone, but ProtMamba's fitness half lifts the overall paper.
- `jqx5XI4Yr3.md` (avg 3.4) — ProteinAdapter, rejected for limited scope. ProtMamba well above this.
- `8pYNdmwGAO.md` (avg 4.0) — homology-aware mutation effect prediction, rejected for narrow eval. ProtMamba above: broader ProteinGym coverage, more architectural novelty.
- `SFCHv2G33F.md` (avg 3.5) — narrow-application protein LM. Not comparable in scope.
- `wVmShpwtY0.md` (avg 4.0) — protein optimization paper rejected for limited eval. ProtMamba is substantially above.

ProtMamba is clearly above the low band and the weaker mid-band anchors, and clearly in the same league as — but somewhat below — the 7.0–7.5 anchors due to the Table 3 cross-family confound, the Figure 3 selection issue, and the missing PoET-on-generation baseline. The fitness-prediction half alone would justify acceptance; the generation half as evaluated would not. Net: borderline accept.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>