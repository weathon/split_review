Now I have a thorough understanding of the paper and all reviewer claims. Let me produce the consolidated review.

## Summary

This paper identifies and formalizes an "interpretability illusion" specific to subspace activation patching in transformers: a 1-dimensional subspace found by optimization (e.g., DAS) can appear to mediate a feature by leveraging a *causally disconnected* component (in the kernel of the MLP's down-projection \(W_{out}\)) to activate a *dormant* pathway, rather than faithfully representing the feature. The authors demonstrate this mathematically with a toy model, empirically in GPT-2 Small on the IOI task (layer 8 MLP), and in GPT-2 XL for factual recall, and show an approximate equivalence to ROME-style rank-1 edits. They also provide a validated counterexample (residual stream subspaces for IOI) to show the method is not intrinsically flawed.

## Strengths

1. **Formal identification of a novel interpretability failure mode.** The paper provides a precise, mathematically grounded mechanism (Section 3.2) showing how a subspace patch can succeed by combining a causally disconnected direction (\(\ker W_{out}\)) with a dormant direction. This is not merely a theoretical possibility — the decomposition into \(\mathbf{v}_{\text{null}} + \mathbf{v}_{\text{row}}\) is concrete and testable.

2. **Clear empirical demonstration in a real transformer (IOI, GPT-2 Small).** Table 1 is the paper's strongest piece of evidence: patching \(\mathbf{v}_{\text{MLP}}\) gives 46.7% FLDD, but removing the nullspace component drops it to 13.5%, and removing the rowspace component gives 0%. This directly confirms the illusion's mechanics in a real model, and the contrast with the residual stream directions (140.7% / 127.5%) is compelling.

3. **Provides a validated success case (residual stream for IOI) that serves as a controlled contrast.** The paper does not merely show the illusion exists — it also shows what a *faithful* subspace looks like under the same tests. The high cosine similarity (0.78) between \(\mathbf{v}_{\text{resid}}\) and the gradient direction \(\mathbf{v}_{\text{grad}}\), and the fact that removing the nullspace component does not diminish the effect, validate that DAS can find meaningful subspaces when used in the right locations.

4. **Extends the illusion to factual recall and connects to rank-1 editing (ROME).** The paper shows that DAS finds similar illusory subspaces in GPT-2 XL for factual recall (Figure 5), and derives an approximate equivalence between 1-dimensional subspace interventions and ROME-style rank-1 edits (Section 6.3–6.4). This provides a mechanistic explanation for the prior observation (Hase et al.) that ROME "works" even in layers where the fact is not stored — a genuinely useful reframing.

5. **Introduces practical diagnostic tests and makes concrete recommendations.** The paper proposes a clear methodology for detecting the illusion (Section 3.4): compare patch strength after removing the nullspace component, and check how dormant the rowspace component is. The recommendation to favor residual-stream bottlenecks and perform validations beyond end-to-end causal effect is actionable for practitioners.

## Weaknesses

### Fatal

None.

### Major

None. The core contribution is well-supported, and no identified weakness undermines the central claims.

### Minor

- **Absence of uncertainty estimates for key metrics.** Table 1 and Figures 3–5 report FLDD, interchange accuracy, and rewrite scores as point estimates without confidence intervals or standard errors. Given that the argument relies on comparing numerical values (e.g., 46.7% vs 13.5% vs 0%, or rewrite scores across layers), the reader cannot assess whether these differences are reliably outside noise. The effect sizes are large enough that the qualitative story is likely robust, but the paper would be stronger with bootstrap confidence intervals or standard errors. This is the paper's most significant methodological gap.

- **The prevalence claim is theoretically argued but empirically narrow.** Section 7 (Prevalent) is convincingly reasoned but relies on only two empirical demonstrations (IOI at layer 8 of GPT-2 Small, factual recall at layers 20–35 of GPT-2 XL). The paper acknowledges this indirectly and frames it as an argument rather than a proven claim, but the gap between the prose ("should be prevalent") and the evidence is noticeable. Adding a negative control (e.g., MLP layers *outside* the IOI circuit, or a different model architecture) would substantially strengthen this section. As is, this is a limitation rather than a flaw.

- **The 13.5% FLDD for \(\mathbf{v}_{\text{MLP}}\) rowspace is not fully discussed.** The paper states "the effect is greatly diminished" (from 46.7% to 13.5%), which is true, but 13.5% is non-zero. The paper should more explicitly quantify whether this residual effect is within noise or constitutes a meaningful dormant contribution. The paper mentions this in passing but the offhand framing undersells the caveat. With error bars, the reader could assess whether 13.5% is reliably above zero.

- **The connection to ROME is indirectly demonstrated.** The paper derives an approximate equivalence and shows that the subspace interventions have a large nullspace component (Figure 5, right), but does not directly check whether ROME edits themselves rely on the nullspace component. The paper provides circumstantial evidence that is sufficient for its main argument but leaves a natural experiment (ablate the nullspace component from the ROME key vector and check if the edit still works) unexplored. This is not a weakness of the paper's core claims but a missed opportunity for stronger evidence.

### Trivial

- The paper refers to "Section 7" for the prevalence argument, but the discussion section (Section 8 / \ref{sec:discussion}) is where some key summary statements appear; Section 7 / \ref{sec:prevalent} is the main prevalence section. Minor cross-reference confusion.

## Nice-to-Haves

- **Negative control for the MLP illusion:** Test whether a random 1-dimensional subspace of MLP activations (or a DAS subspace trained on an irrelevant task) shows any FLDD. This would calibrate how meaningful a 13.5% effect is relative to noise.
- **Direct nullspace ablation of ROME edits:** Decompose the ROME key vector into nullspace/rowspace components and test whether the edit retains its effect after removing the nullspace component. This would directly confirm the proposed mechanism.
- **Additional model/task for prevalence support:** A spot-check on a different model (e.g., Pythia, LLaMA) or a different task would significantly strengthen the prevalence argument without requiring exhaustive evaluation.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Harsh Critic Point 3 ("causally-disconnected subspace for residual stream defined by proxy — paper does not report this test"):** Removed because it is factually incorrect. The paper *does* report this test in Table 1: \(\mathbf{v}_{\text{resid}}\) nullspace FLDD = 13.9%. The test was run. The residual stream's nullspace definition is indeed a proxy (using only Name Mover head query matrices), and the paper honestly acknowledges this limitation. The reviewer's confusion about the table format does not constitute a valid weakness.
- **Hidden Critic's style/formatting nitpicks:** Various minor phrasing suggestions that do not affect the paper's technical correctness have been removed per Hard Rules.
- **Generic or dropped strengths from Strength Finder:** Several strengths were generic ("this paper addressed an important problem") and have been dropped. Remaining strengths in the main review are those with specific, citable evidence.

## Novel Insights

The primary novel insight from this review is that the paper's analysis incidentally provides a mechanistic lens for understanding *when* a method like DAS will succeed versus fail: DAS finds faithful subspaces in activation bottlenecks (residual stream) where the causally disconnected subspace is small or nonexistent, but finds illusory subspaces in MLP activations where \(\ker W_{out}\) provides a high-dimensional "free variable" that can be exploited. This suggests a deeper principle: optimization-based subspace search methods are prone to finding solutions that exploit any available degrees of freedom disconnected from the output, and the degree of illusion is predictable from the nullspace dimension. None beyond the paper's own contributions.

## Suggestions

1. Add bootstrap confidence intervals or standard errors to all averaged metrics (FLDD, interchange accuracy, rewrite scores). This is the single most impactful improvement.
2. Explicitly quantify and discuss the 13.5% residual FLDD for \(\mathbf{v}_{\text{MLP}}\) rowspace — is it meaningfully above zero, or within noise?
3. Add a negative control experiment (random subspaces, or DAS on irrelevant tasks) to calibrate the FLDD metric.
4. Consider a direct nullspace-ablation experiment for ROME edits to tighten the mechanistic link.
5. Tone down the prevalence language slightly ("likely occurs" rather than "should be prevalent") or add one additional empirical spot-check.

## Score and Decision

**Originality:** 8/10 — The illusion is genuinely novel and clearly distinct from prior interpretability failure modes (e.g., saliency map fragility, backup circuits).
**Importance of research question:** 9/10 — Subspace activation patching is increasingly used, and a clear cautionary demonstration is valuable to the community.
**Claims well-supported:** 7/10 — The main claims are well-supported empirically; prevalence claims are less so, but not central.
**Soundness of experiments:** 7/10 — Well-designed experiments; main gap is absence of uncertainty quantification.
**Clarity of writing:** 8/10 — Generally clear; mathematical exposition is precise, and the narrative arc is well-structured.
**Value to community:** 9/10 — Provides methodology (diagnostic tests) and a cautionary example that will influence how practitioners validate subspace interventions.

The paper makes a real and important contribution. The weaknesses are real but minor and addressable. No weakness undermines the core claim. The paper should be accepted.

MY FINAL SCORE: <pineapple>8.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>