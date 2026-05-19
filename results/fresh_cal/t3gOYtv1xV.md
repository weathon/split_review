Now I have all the information needed. Let me write the final consolidated review.

## Summary

This paper reverse-engineers how small encoder-only transformers implement the carrying-over algorithm for integer addition. Using attention pattern analysis, ablation studies, PCA of residual streams, and neuron-level dissection, it demonstrates that two-layer models allocate each algorithmic step to a distinct architectural component: the first layer adds digits and detects sums ≥10, a second-layer attention head decides where a carried one is needed, and the final MLP physically adds the carried one. The paper also provides a method to identify the exact subset of MLP neurons responsible for carrying, discusses a phase transition in one-layer models, examines length generalization through priming/finetuning, and provides suggestive evidence for similar patterns in 7B LLMs.

## Strengths

1. **Multi-evidence mechanistic decomposition of the carrying over algorithm.** The paper shows that in two-layer encoder-only transformers, each step of the algorithm maps to a specific architectural component. This is supported by convergent evidence from ablations (Table 1: ablating the decision head leaves the model unsure about non-carry sums, ablating the final MLP makes the model unable to carry), attention patterns (Figure 2: staircase patterns in layer 0, information transfer from previous sum in head 1:0), and PCA of the residual stream (Figure 3: layer 0 separates by ≥10 vs <10; layer 1 separates by whether a carried one is needed). This goes beyond prior attention-only analysis by causally identifying the role of each architectural block.

2. **Precise neuron-level identification of the carry operation.** The paper provides two complementary methods (Section 5) to isolate the subset of MLP neurons responsible for carrying: activation-based ablation (removing ~86 neurons whose activations on carry tasks exceed the maximum NC activation causes total inability to carry while non-carry sums remain perfect) and SVD of the pre-activation weights identifying a "carry axis." This is a concrete, reproducible dissection technique.

3. **Fine-grained task decomposition as an analytic tool.** The five natural subsets of the addition dataset (NC, C@1, C@2, C all, C all con.) defined in Section 2 are used throughout all analyses, enabling precise diagnosis of which component handles which algorithmic step. This is a clear improvement over overall accuracy metrics.

4. **Length generalization with a mechanistic rationale.** The paper demonstrates (Section 6) that models trained on 3-digit addition can generalize to 6-digit addition when primed with only 100 longer examples or finetuned on 500 examples, and argues (referencing the appendix) that this works because the early-trained carry components are leveraged rather than relearned.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Incomplete variance reporting in the core ablation table.** Table 1 reports accuracies "averaged over six runs" but only mentions variance for one specific case ("whenever it is unsure, the variation between runs is large (~0.38)"). While the qualitative pattern in Table 1 is stark enough that variance is unlikely to change the conclusions (e.g., 0.52 vs 0.31 vs 1.0 for decision head ablation, or near-0 vs near-1 for MLP ablation), providing standard deviations for all entries would allow readers to assess robustness. The paper does report standard deviations elsewhere (e.g., the squashing metric and skip-connection ablation), making this omission inconsistent.

2. **One-layer phase transition analysis is thin for a listed contribution.** Contribution 4 claims a "novel phase transition" in one-layer models, but the evidence is limited to one loss/weight-norm plot from a single run (Figure 1) and attention patterns at three epochs. No quantitative measure of transition sharpness, no analysis of variance across the six runs mentioned in Section 2, and no detailed comparison to prior work on phase transitions in attention (e.g., the induction head phase change from Olsson et al. that the paper cites). The one-layer models themselves are acknowledged to be imperfect (~80-90% accuracy), further weakening what can be claimed.

3. **LLM evidence is thin but appropriately caveated.** The LLM analysis (Section 6) provides suggestive evidence: staircase attention patterns, an ablation showing accuracy drop when "addition heads" are removed, and a PCA snapshot at one layer of Llemma. The paper's own framing ("suggestive evidence," "potentially suggest") is honest, but contribution 2 lists this as a main finding. The analysis would be strengthened by (a) clearer description of what is ablated and how ablation was verified, (b) analysis across more layers showing the transition from sum-separation to carry-need separation in LLMs, and (c) stronger caveats about the correlational nature of the residual stream evidence.

4. **Length generalization "forgetting" claim is asserted without main-text evidence.** The paper claims (Section 6) that "all the parts of the carrying over algorithm are in place around epoch 500... but after this time the model starts to forget this" — but no supporting plot or quantitative evidence is shown in the main text; it is deferred to the appendix. For a listed contribution (item 3), this evidence belongs in the main text.

5. **Neuron ablation threshold is underspecified.** The threshold for identifying carry neurons is stated as "ablating those neurons whose activations satisfy $z_i > z_{\texttt{NC}}$" (Section 5), but it is not made explicit whether $z_{\texttt{NC}}$ is the maximum activation over NC examples, a percentile, or something else. The appendix likely clarifies this, but the main text is ambiguous.

### Trivial

- The phrase "hidde states" appears in Figure 4's caption (parser artifact or typo).
- The claim that the ablated model is "very confident where to add a one when it indeed should" (p. 4) is accurate but the evidence shows 1.0 accuracy for carry tasks in the decision-head ablated case, while the model fails at non-carry tasks — this is better described as "the model always adds a one at carry-requiring positions when the head is ablated," which the corrected-accuracy rows confirm.

## Nice-to-Haves

- Reporting standard deviations for all entries in Table 1.
- Including one plot showing the "forgetting" phenomenon in the main text for the length generalization experiment.
- A brief clarification of how $z_{\texttt{NC}}$ is defined for the neuron activation threshold.
- More explicit distinction in the one-layer section between this phase transition and known grokking/induction-head phase transitions.

## Removed Points

**"Position 9 never needs a carried one is incorrect"** — REMOVED (factually wrong). The paper counts positions from the left (0–9). Position 9 is the rightmost = sign, corresponding to the least significant (units) digit of the output. The units digit can generate a carry but never receives one, so the claim is correct. The harsh critic mistakenly labeled it the "most significant digit."

**"No causal intervention on LLMs"** — REMOVED (contradicted by the paper). Table 2 reports "ablated acc." after removing identified "addition heads," and a footnote states the ablation did not damage generation ability. The analysis is thin but does include causal intervention.

**"PCA trinary labeling system unclear"** — REMOVED (incorrect). The paper explains the trinary system clearly: "0 means <9 at this position, 1 means ≥10, 2 means equal to 9 (if previous sum was ≥10)."

**"Position numbering is confusing"** — REMOVED (not the paper's error). The paper states "count the positions of the digits from the left" and consistently uses this scheme. The harsh critic's confusion about which positions correspond to which digits is a reader-side issue, not a paper error.

**"Missing related works"** — REMOVED per instructions (no external sources to verify).

**"Pure formatting/style nitpicks" and "typos/grammar"** — REMOVED per instructions (parser artifacts, not author errors).

## Novel Insights

None beyond the paper's own contributions. The reviewers' comments do not surface a novel observation about the paper that the paper itself does not already make.

## Suggestions

1. Add standard deviations (or at least the range) for all entries in Table 1 to allow readers to assess robustness across random seeds.
2. Either move the length-generalization forgetting curve into the main text or clearly state in Section 6 that the details are in the appendix and summarize the key quantitative finding.
3. Clarify the neuron identification threshold: is $z_{\texttt{NC}}$ the maximum, the 95th percentile, or something else?
4. Strengthen the one-layer phase transition analysis with at least one additional run and a quantitative measure (e.g., sharpness, epoch of transition across seeds), or downgrade its status from a listed contribution to an observation.
5. In the LLM section, provide a clearer description of what "ablated acc." means (which heads, how many, verification of intact generation) and add explicit caveats about the correlational nature of the residual stream evidence beyond the single layer analyzed.

## Score and Decision

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>