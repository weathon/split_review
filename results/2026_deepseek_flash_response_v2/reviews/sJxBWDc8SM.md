## Summary

This paper empirically compares modern SSMs (Mamba, Hyena, Mamba2, DeltaNet) with Transformers on the multi-query associative recall (MQAR) and copying tasks. It finds that SSMs exhibit extreme sensitivity to learning rate—their success is confined to a narrow window that can be missed by standard hyperparameter grids—while Transformers are broadly robust. It uncovers opposing scaling behaviors (SSMs benefit from width, Transformers from depth), traces Mamba's single-layer expressivity advantage to its 1D convolution via clean ablation, and identifies DeltaNet as a more optimization-stable architecture. The paper argues that optimization instability, not just expressivity, fundamentally separates these architectures.

## Strengths

1. **Systematic demonstration of a narrow learning-rate window in SSMs across two tasks (Figures 1 & 5):** The contrast between Attention's broad LR plateau and Mamba/Hyena's sharp peaks is visually striking and practically important. The dashed vertical lines marking the grid used by Arora et al. (2023) fall outside the optimal windows, concretely showing how standard tuning grids can produce misleading conclusions about SSM capabilities.

2. **Clean ablation isolating the 1D convolution as the source of Mamba's single-layer advantage (Table 2):** Removing the 1D convolution from a 1-layer Mamba drops accuracy from 99% to 2% (matching the 1-layer Transformer's failure), while adding a convolution before QKV in a 1-layer Attention model boosts accuracy from 2% to 99%. This is a precise causal intervention that pinpoints the responsible architectural component, rather than speculating about broad architectural families.

3. **Contrasting scaling strategies (width vs. depth) with concrete evidence (Table 1, Figures 3-4):** Table 1 is especially telling: a deeper but narrower Mamba (24 layers, 150M params) achieves only 16% accuracy on copying, while a shallower but wider Mamba (12 layers, 150M params) achieves 100%. This directly challenges the common practice of comparing architectures at equal parameter counts without considering their preferred scaling axis.

4. **Observation that a 1-layer Transformer exhibits induction-head-like dynamics despite failing the task (Figure 6):** This provides a novel dissection of why single-layer comparisons can be misleading—the Transformer attempts the right circuit but lacks the depth to complete it.

5. **Identification of DeltaNet as more optimization-stable with a hypothesized mechanism (Figure 7, Section 7):** DeltaNet maintains high accuracy across a wide LR range, and the paper connects this to Householder-based updates avoiding the vanishing-gradient problem from Mamba's A-matrix decay parameter.

## Weaknesses

### Fatal
None.

### Major

1. **Central thesis stated more strongly than the evidence supports.** Line 39 states: *"Transformers differ from SSMs not in terms of expressive power but mainly because of their optimization dynamics."* The evidence shows optimization is an important and neglected confound, but it does not cleanly separate expressivity from learnability to support "mainly." The paper itself acknowledges "a sizable gap with Transformers can still be observed at low widths (e.g. Hyena)" (line 140), and the memory bottleneck hypothesis (Jelassi et al., 2024) about expressivity limits tied to hidden state size is neither disproven nor directly tested. The abstract's more measured phrasing (*"a crucial differentiator lies not just in their expressivity but in their fundamental learnability"*) is well-supported and should replace the stronger thesis throughout the paper.

2. **Statistical characterization is thin for the instability claims being made.** Results are reported throughout as "mean and relative max-min errors using 5 seeds" (lines 25, 101, 127, 231). Five seeds is a limited basis for claims about "critical instability" and "narrow window," especially when the central finding is about *variability* across learning rates. The "relative max-min" metric is unusual and less informative than standard deviations or confidence intervals. For Figure 1, the paper's most prominent result, readers need to see how much of the apparent "narrow window" is due to variance across runs—if at the optimal LR all 5 seeds succeed but at adjacent LRs only 1/5 succeeds, the visual story changes meaningfully.

3. **Table 1 reports no variance despite the paper's focus on instability.** Table 1 (copy task scaling) shows single-configuration results without error bars, even though the paper elsewhere uses 5 seeds. The key finding—24-layer Mamba at 150M params achieves only 16% vs. 12-layer wider Mamba at 150M params achieving 100%—would benefit from variance characterization.

### Minor

1. **Bridge from synthetic benchmarks to real-world LM comparisons is crossed too quickly.** The paper motivates its tasks by citing correlation with LM performance, then makes claims that directly bear on real-world model comparisons (line 43: "prior empirical expressivity comparisons may have been confounded by suboptimal tuning," citing Waleffe et al. 2024 on actual pretrained LMs). The scaling findings are demonstrated at toy scales (dimensions 64–512, sequence lengths 64–512). The paper acknowledges this limitation in the discussion (line 235), which is good, but the introduction framing understates the gap between the evidence and the real-world conclusions.

2. **DeltaNet stability result is limited by scale.** Figure 7 shows DeltaNet achieving Transformer-like LR robustness only up to model dimension 256—the maximum supported by the implementation. The claim that "Transformer-level robustness is only achieved by DeltaNet" (line 221) cannot be verified at the scales where SSMs are practically deployed. The paper acknowledges this, but it limits how far the conclusion travels.

3. **The 1-layer induction head observation rests on visual similarity without mechanistic confirmation.** The paper notes a loss bump "resembling" induction head formation (Section 6) and hypothesizes that the Attention mechanism "attempts" to form such heads. The evidence is visual similarity alone; no attention-map analysis or probing confirms that an induction-head circuit is actually being formed. The paper uses appropriately hedged language, so this is a minor concern.

### Trivial
None.

## Nice-to-Haves

- Report individual seed trajectories or the fraction of seeds succeeding at each learning rate for the core Figure 1 result, rather than just "mean and relative max-min."
- The convolution ablation (adding convolution to Attention solves MQAR in 1 layer) could be unpacked mechanistically: does it act as a short-term memory buffer, extend the effective context window, or both?
- A controlled experiment within the Mamba family testing whether removing A-matrix decay improves stability (rather than switching to DeltaNet) would more directly validate the mechanistic hypothesis about what drives instability.

## Removed Points

These points were flagged for removal from the inputs; they are listed here with justification in case they prove useful:

- *"The paper frames the 1-layer Transformer's failure as a novel discovery, but prior work already established that induction heads require 2+ layers"* — **Removed** because the paper does not claim novelty here and cites Sanford et al. (2024) in the same discussion (line 145).
- *"The 'overlooked' framing risks overstating the case"* — **Removed** because this is a judgment about tone rather than a factual error; prior work (Arora et al., 2023) did miss the optimal LRs for SSMs.
- *"Limited model set (no RWKV, no Griffin, no H3)"* — **Removed** because the paper already covers the most prominent SSMs (Mamba, Hyena, Mamba2, DeltaNet), which is a reasonable selection.
- *"Only Adam is used"* — **Removed** because using a single optimizer is standard practice and not a meaningful weakness for this paper.
- *"No analysis of what happens inside the narrow window"* — **Removed** because this asks for additional analysis beyond the paper's stated scope.
- *Generic strengths from Strength Finder about "important problem"* — **Removed** as superficial.

## Novel Insights

The merger of the two reviews highlights a tension the paper does not fully resolve. The convolution ablation (Table 2) is the paper's most incisive result: it shows that the *expressivity* difference between a 1-layer Mamba and 1-layer Transformer is entirely attributable to a single architectural component (the 1D convolution). Yet the narrow LR window persists even with the convolution—meaning that expressivity and optimization stability are at least partially orthogonal issues, not that one reduces to the other. The paper's thesis conflates these two axes: it shows that SSMs are *more expressive* than previously appreciated (they can solve MQAR with good tuning) and that they are *harder to optimize* (narrow LR window), but it does not show that the latter fully explains the former. This distinction is the key nuance that the paper's strong thesis language obscures, and it represents a genuinely more interesting conclusion than "it's mainly optimization."

## Suggestions

1. **Soften the central thesis** to match the evidence. Replace line 39 ("not in terms of expressive power but mainly because of their optimization dynamics") with language consistent with the abstract ("a crucial differentiator lies not just in their expressivity but in their fundamental learnability").
2. **Improve variance characterization** of the core LR-sensitivity results: report confidence intervals, standard deviations, or the fraction of seeds succeeding at each learning rate for Figures 1 and 5.
3. **Add variance bars** to Table 1.
4. **More carefully delimit** how far synthetic-task conclusions generalize to real-world LM comparisons in the abstract and introduction.

## Score and Decision

**Calibration Anchors (all rounds):**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| `/home/.../q541p2YLt2.md` (Transformer Training Instability) | 2.50 | R1 | Much weaker; rejected paper |
| `/home/.../4dtwyV7XyW.md` (Principled Transformers for KT) | 3.00 | R1 | Much weaker |
| `/home/.../iVy7aRMb0K.md` (Mimetic Initialization) | 4.50 | R1 | Similar topic, our paper is clearly stronger (cleaner experiments, more important findings) |
| `/home/.../b5lXUwZiD3.md` (Limitation of Transformer for HMMs) | 5.25 | R1 | Comparable topic, our paper slightly stronger |
| `/home/.../QFgbJOYJSE.md` (SSMs Provably Comparable to Transformers) | 5.75 | R2/R3 | Similar empirical+synthetic style; our paper slightly stronger on experimental design |
| `/home/.../pymXpl4qvi.md` (Understanding Bottlenecks of SSMs) | 6.00 | R1 | Most directly comparable anchor; similar contribution scope and limitations |
| `/home/.../sZJNkorXMk.md` (Autocorrelation Matters for SSMs) | 6.67 | R2 | Has stronger theoretical component our paper lacks; our empirical experiments are cleaner |
| `/home/.../DjeQ39QoLQ.md` (Robustifying SSMs) | 6.50 | R2 | Stronger theoretical contribution; our paper more empirically focused |
| `/home/.../d8w0pmvXbZ.md` (Small-scale proxies) | 8.00 | R1 | Clearly stronger; more thorough ablations and practical insights |

**Round 1 bracket**: 5.0–7.0
**Round 2 narrowing**: Compared against anchors at 6.0 (Understanding Bottlenecks) and 6.67 (Autocorrelation), our paper sits closest to the 6.0 anchor with slightly weaker statistical rigor but cleaner causal experiments.

**Final assessment**: This is a solid empirical study with genuinely useful findings (the narrow LR window demonstration, the convolution ablation, the width-vs-depth scaling evidence). The main weaknesses—an overclaimed thesis statement and thin variance reporting—are bounded and addressable. The paper makes a clear contribution to the ongoing debate about SSM vs. Transformer capabilities.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>