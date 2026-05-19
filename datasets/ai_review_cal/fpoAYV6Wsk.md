- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 6, 8
Now I have a thorough understanding of the paper and the reviews. Let me construct the consolidated review.

## Summary
The paper investigates whether circuits discovered for the Indirect Object Identification (IOI) task are reused by GPT2-Medium for the seemingly different Colored Objects task. The authors report that ~78% of the top 2% most important attention heads are shared between the two circuits, and demonstrate that artificially activating inhibition heads and the negative mover head (to behave as they do in IOI) boosts Colored Objects accuracy from 49.6% to 93.7%, with predicted downstream effects on mover heads. This is an empirical study providing evidence for circuit-level reuse across tasks.

## Strengths

1. **Causal intervention with predicted downstream effects is compelling and internally consistent.** The paper does not just report an accuracy boost — it shows that forcing three inhibition heads and one negative mover head to attend to incorrect color tokens causes downstream mover heads to decrease attention to wrong colors (avg −8.7%) and increase logit attribution (~3×). The Spearman correlation of 0.69 (p<0.01) between logit attribution change and original mover-head importance provides strong evidence that the intervention activates the same functional subcircuit observed in IOI (Section 5, lines 141–148).

2. **Quantified overlap figure, though improvable, directly addresses the core question.** The finding that 25/32 heads are shared between the two circuits (Section 4, Figure 3 caption, line 79) gives a concrete, falsifiable number to the "are circuits reused?" question rather than relying on qualitative similarity claims. The paper rightfully acknowledges that perfect quantification is difficult (footnote, line 14).

3. **Diagnosis of *why* the existing circuit components fail on the new task.** Rather than simply reporting overlap, the paper explains that inhibition heads are present in Colored Objects but receive an unfocused signal (attending to all color tokens rather than specifically wrong ones), and the negative mover head is essentially "parked" (Section 4.4, lines 119–124). This provides a principled basis for the intervention rather than trial-and-error.

4. **Control experiment for content gatherer heads is well-designed.** Blocking attention from content gatherer heads to question tokens reduces accuracy to 35% (chance), with a random-head control at 49.9%±1.0 (line 91). This validates the claimed role of these heads in the Colored Objects circuit.

5. **Refined understanding of negative mover heads.** The paper identifies that in GPT2-Medium, negative mover head 19.1 attends specifically to the S2 token (not all names as in GPT2-Small) and functions as the most important head for logit difference, suggesting more sophisticated behavior at larger scale (Section 3.1, lines 58–59).

## Weaknesses

### Fatal
None. The paper's core claims are supported by the evidence presented, and the methodology is sound for an exploratory empirical study.

### Major
None. The identified issues are about clarity and precision, not about fundamental flaws that would invalidate the results.

### Minor

1. **The derivation of the 78% overlap figure is not fully transparent.** The paper states "thresholding at the 2% most important heads (per path patching stage)" (Figure 3 caption), yielding 32 heads total (lines 79–80). However, it never specifies: (a) how many path-patching stages there are, (b) how many heads are selected per stage (2% of what population — all heads, or heads implicated at that stage?), or (c) how sensitive the overlap percentage is to the 2% threshold. The paper honestly notes that "quantifying overlap is a difficult problem" (footnote, line 14), but a headline number in the abstract requires clearer derivation. This does not invalidate the qualitative finding of substantial overlap (which is visually supported by Figure 3), but it limits the precision readers can assign to the "78%" figure.

2. **The cross-model reproduction claim is under-quantified.** The paper states it "replicates" the IOI circuit on GPT2-Medium (lines 53–54), but then reports that the negative mover head (19.1) behaves differently from GPT2-Small (attending only to S2 rather than all names, and being the *most* important head vs. a hedging mechanism). The paper provides no quantitative comparison (e.g., correlation of path-patching importance scores across model sizes) or systematic list of which heads are shared between the two model sizes. Since the reproduction is a prerequisite for the main experiment, the claim could be strengthened with more rigor, but this does not undermine the cross-task comparison which is the paper's main contribution.

3. **No confidence intervals on the primary accuracy numbers.** The main intervention result (49.6% → 93.7%) is reported without confidence intervals or standard errors, though error bars are shown in Figure 5 and standard errors are reported for the random-head control (49.9%±1.0, line 91). Reporting uncertainty on the headline results would strengthen the quantitative claims.

4. **The term "reuse" in the title and framing could be clarified.** The paper's intervention is externally guided — it forces attention patterns rather than showing the model naturally activates these heads on Colored Objects. The paper is transparent about this (calling it a "proof-of-concept intervention" and noting the heads "are receiving incorrect biases" at lines 115–127), but the broader framing ("Circuit Component Reuse Across Tasks") risks implying natural reuse. The evidence shows the *subcircuit* is functionally invariant when externally triggered, which is a meaningful but more nuanced claim.

### Trivial
None.

## Nice-to-Haves

- A control intervention that forces the same heads to attend to random tokens (rather than specifically the incorrect colors) would strengthen the claim that the specific inhibition pattern drives the improvement.
- Showing the overlap percentage across multiple thresholds (1%, 2%, 5%, 10%) would demonstrate robustness of the 78% figure.
- Reproducing the key intervention on another model (e.g., GPT2-Small if it can handle the task, or Pythia) would strengthen generality claims, though this is scope for future work.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"The intervention experiment supports a weaker claim than the paper seems to make"** — The paper repeatedly calls this a "proof-of-concept intervention" (lines 20, 115, 161) and explicitly states the heads are "receiving incorrect biases" and "not active" (lines 124–127, 135). The paper does not claim the model naturally uses this subcircuit; it claims the subcircuit itself is functionally invariant when triggered. The reviewer's concern conflates the paper's actual claims with a potential over-reading by readers. Removed as a misunderstanding of the paper's scoping.

- **"Dataset and code release are not mentioned"** — The rules instruct removing criticisms about existence/release status of cited entities. The paper cites existing datasets (IOI from Wang et al., Colored Objects from BIG-Bench) and the generated dataset is a simple systematic variation. Code release is a standard request but not a weakness of the scientific contribution. Removed per hard rules.

- **Reviewer's specific erroneous calculations about GPT2-Medium architecture** (assuming 24 heads/layer → 576 total) — GPT2-Medium has 16 heads/layer (384 total). The reviewer's numbers are factually wrong. Removed.

- **"Comparison of path-patching scores" as a missing comparison** — The paper shows this visually in Figure 3 (left panel shows "difference of path patching importance scores between each task"). The reviewer missed this figure. Removed as factually incorrect.

- **Several generic "Strengthening the Paper" suggestions** (testing on GPT2-Small/Large) — Requests to do additional experiments beyond the paper's stated scope. The paper is scoped as a proof-of-concept on GPT2-Medium, which is appropriate. Moved to nice-to-have.

## Novel Insights

The reviews surface a useful nuance that the paper itself acknowledges but could foreground more: the 78% overlap figure comes with nontrivial methodological caveats (threshold sensitivity, stage-dependent head selection), and the intervention results prove *capability* for reuse rather than *natural* reuse. Neither of these is a fatal weakness, but together they suggest the paper's contribution is best understood as: (1) providing strong prima facie evidence that circuit-level structures can be shared across tasks in ways that support targeted interventions, and (2) demonstrating that even when head-level overlap is imperfect, the algorithmic structure (duplication detection → signal to mover heads → token copying) is preserved. The Spearman correlation result (0.69) between intervention-induced logit attribution changes and original mover-head importance is a particularly clean piece of evidence that was not exaggerated by any reviewer.

## Suggestions

1. **Clarify the overlap quantification in full detail.** Specify: number of path-patching stages, how "top 2%" is computed per stage (from what candidate set), the breakdown of the 32 heads (how many from each stage), and a sensitivity analysis showing overlap at 1%, 2%, 5%, 10% thresholds.

2. **State the total number of attention heads in GPT2-Medium** (24 layers × 16 heads = 384) explicitly in the experimental setup section.

3. **Add confidence intervals** (e.g., bootstrapped 95% CI) for the main accuracy numbers (49.6% and 93.7%).

4. **Add a sentence clarifying the intervention vs. natural reuse distinction** in the abstract or conclusion. The current framing uses "reuse" broadly; acknowledge upfront that the intervention demonstrates the subcircuit's functional invariance when externally guided, which is a step toward but not identical to demonstrating natural reuse.

5. **Add a small table comparing GPT2-Small vs. GPT2-Medium IOI heads and their roles** to make the reproduction claim concrete.
