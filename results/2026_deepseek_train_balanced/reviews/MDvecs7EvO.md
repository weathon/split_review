Now let me produce the final review.

## Summary

This paper introduces SAE Match, a data-free method for aligning Sparse Autoencoder (SAE) features across layers of a neural network. The approach solves a linear assignment problem to find a permutation that minimizes MSE between SAE weights from different layers. A key technical contribution is "parameter folding"—absorbing the JumpReLU thresholds θ into the encoder/decoder weights via an exact transformation (Eq. 8) before matching. Experiments on Gemma 2 SAEs evaluate matching quality via MSE, LLM-judged semantic similarity of Neuronpedia descriptions, a "Matching Score," and a layer-pruning (encode-permute-decode) experiment that measures cross-entropy loss and explained variance when skipping a layer.

## Strengths

1. **Parameter folding is a novel, theoretically clean technique.** The folding operation (Eq. 8) exactly preserves the SAE output while incorporating the learned per-feature thresholds θ into the weight matrices. This is specific to the SAE/JumpReLU setting and has no direct analog in prior weight-matching work (Ainsworth et al., Git Re-Basin). The mathematical transformation is exact and well-motivated.

2. **The layer-pruning experiment (encode-permute-decode) provides functionally grounded validation.** Section 5.5 replaces a layer's computation by encoding at layer t, permuting features to match layer t+1, and decoding—effectively skipping the layer. Figure 8 shows that from layer 10 onward, the change in cross-entropy loss remains near zero and explained variance stays high. This tests whether matched features are functionally interchangeable in the actual forward pass, which is stronger evidence than MSE or LLM judgments alone.

3. **The data-free property is practically valuable.** Matching operates purely on SAE weights without requiring any input data at match time, which is a genuine advantage for studying feature dynamics without incurring the cost of running the model on large corpora.

4. **Composition of permutations is validated as a useful approximation.** Section 3.3 proposes composing permutations A→B and B→C to approximate A→C, and Section 5.4 shows this works well for nearby layers (especially later layers), reducing the number of expensive LAP solves needed.

5. **The analysis of early-layer polysemanticity uses a second metric to distinguish method failure from feature ambiguity.** Section 5.3 shows that the LLM evaluation yields near-zero "SAME" features in early layers, but the Matching Score (which does not rely on descriptions) does not drop to zero, suggesting the method retains predictive ability even when LLM descriptions fail. This nuanced diagnosis strengthens confidence in the method.

## Weaknesses

### Fatal
None.

### Major

1. **Missing critical baselines.** The paper compares SAE Match only against: (i) no permutation ("vanilla"), and (ii) unfolded matching (matching without folding). There is no comparison to (a) **random permutation**—to establish that the matching discovers structure beyond chance; (b) **cosine-similarity-based matching**—to test whether MSE (which is sensitive to norm differences) is the right similarity metric, or whether angular proximity suffices; or (c) **any data-dependent feature alignment**—to quantify what the "data-free" property costs. Without these anchors, the reader cannot assess whether the method is genuinely effective or merely better than doing nothing. The paper claims "improved feature matching quality" but provides no external reference point against which to measure that improvement.

2. **The layer-pruning experiment lacks controls necessary to attribute performance to matching quality.** The experiment (Section 5.5) shows that using matched features to skip a layer causes minimal loss increase from layer 10 onward. However, without controls such as (a) a random permutation instead of the learned one, (b) directly copying the hidden state of layer t to layer t+1, or (c) using the SAE reconstruction of layer t's own state as a proxy for layer t+1, the result could be explained by later layers being redundant or by the SAEs' reconstruction fidelity dominating regardless of permutation quality. The paper does not rule out these alternatives.

### Minor

1. **Folded vs. unfolded MSE comparison is confounded by evaluation design.** The caption of Figure 3 states: "In all cases, MSE is evaluated with folded parameters (i.e., for unfolded matching, parameters are first matched, then folded, and finally MSE is evaluated)." Folded matching minimizes MSE in the same space in which it is evaluated, while unfolded matching is optimized in a different space and then projected. This gives folded matching an inherent advantage in the MSE comparison. The paper does use an independent LLM evaluation to corroborate the folding benefit, which partly addresses this, but the MSE comparison alone cannot cleanly distinguish genuine improvement from evaluation bias.

2. **The LLM-based semantic similarity evaluation is uncalibrated and has acknowledged blind spots.** The pipeline uses GPT-4o-generated Neuronpedia descriptions as references and has an LLM judge them as SAME/MAYBE/DIFFERENT. The paper acknowledges (line 279) that "potential errors in Neuronpedia feature descriptions may affect the precise evaluation" and, in Figure 4's caption (line 166), notes that "folding thresholds results in an optimistic labeling." Despite these caveats, no human validation of even a subset of the LLM judgments is provided, so the actual accuracy of this evaluation signal is unknown. The paper simultaneously argues that early-layer features are more polysemantic and their descriptions incomplete (Section 5.3), yet relies on these same descriptions as ground truth for the evaluation.

3. **The claim that θ captures hidden state norm growth is asserted without quantitative evidence.** The paper states (line 100) that "the learned thresholds θ capture the growth of hidden state norms across layers" and cites Figure 1 (left) as evidence. However, no correlation coefficient, regression analysis, or any quantitative measure of this relationship is provided. This claim motivates the entire folding approach (Hypothesis 2) but rests on visual inspection alone.

4. **Several experimental details are underspecified.** (a) The paper states it uses "MSE from both decoder and encoder layers" (line 121) but does not clarify whether this is a combined objective function or separate matching per parameter type, nor how results are integrated. (b) The specific SAE width (e.g., 16k, 65k from GemmaScope) is not stated. (c) The "Matching Score" (line 135) is defined only as "the probability of paired feature activation between two matched layers" without specifying how this probability is estimated, over what data distribution, or what constitutes "paired feature activation." (d) Only 100 examples per dataset are used, yet no variance or confidence estimates are reported for any quantitative result.

### Trivial
None.

## Nice-to-Haves

- Adding a cosine-similarity matching baseline would clarify whether angular or Euclidean distance is more appropriate for this task.
- The folding comparison could be strengthened by evaluating both folded and unfolded matching on a metric that is equally fair to both (e.g., the layer-pruning ΔL, or human-judged feature similarity on a small subset).
- A simple correlation or regression analysis for the θ-vs.-hidden-state-norm relationship (Figure 1) would solidify the motivation.
- Providing error bars or variance estimates would help assess the reliability of results given the small (100-example) evaluation sets.

## Removed Points

- *Criticism about truncated Code dataset URL and missing appendix*: The truncated URL is a parser artifact; the appendix exists in the original submission but was stripped by the PDF parser. Per hard rules, these are removed.
- *Criticism that the paper "never specifies which was actually used" for encoder/decoder matching*: Line 121 states "MSE from both decoder and encoder layers," so the paper does specify this. However, the clarity issue about *how* both are combined is preserved as Minor weakness #4.
- *Criticism about "the Code dataset cannot be fully identified"*: Parser artifact; the URL was truncated during extraction. Removed.
- *Several generic sweep criticisms* that lacked specific textual anchors (e.g., speculation about what the appendix might contain, general claims about "limited generalization to one model" that the paper already acknowledges in its limitations) have been removed.

## Novel Insights

The key insight that is genuinely novel is that the JumpReLU thresholds θ, which control feature sparsity, can be "folded" into the encoder/decoder weights via an exact equivalence transformation (Eq. 8). This is specific to the SAE-with-JumpReLU setting and has no counterpart in earlier weight-matching literature (Ainsworth et al. dealt with networks without per-feature thresholds). The observation that folding θ into the weights prior to MSE-based matching yields different (and empirically better) permutations than matching on raw weights is a concrete methodological contribution. Beyond this, the finding that features in later layers are more stably matchable (with feature persistence spanning ~5 layers) and that composition of permutations works as an approximation for nearby layers are useful empirical observations, though they are validated with moderate evidentiary strength.

## Suggestions

1. **Add the missing baselines before any resubmission.** At minimum: (a) random permutation (to establish that the matching finds structure beyond chance), and (b) cosine-similarity-based matching in the same LAP framework (to test whether MSE or angular distance is the right metric). A data-dependent matching approach (e.g., based on activation co-occurrence) would further substantiate the data-free method's value.

2. **Add control conditions to the layer-pruning experiment.** Compare the learned permutation against (a) a random permutation, (b) direct state copying, and (c) SAE reconstruction without any permutation. This would clarify whether the good performance from layer 10 onward is attributable to matching quality or to confounding factors like layer redundancy.

3. **Clarify the experimental setup.** Specify: (a) whether encoder and decoder matching are performed jointly or separately, and if jointly, how the objective is combined; (b) the exact SAE width(s) used from GemmaScope; (c) a precise definition of the "Matching Score" including how "paired feature activation" is computed, over what data, and with what normalization.

4. **Quantify the θ/norm relationship** in Figure 1 with a simple correlation coefficient or regression analysis.

5. **Calibrate the LLM evaluation** by having at least one human annotator judge a sample of the matching labels, and report agreement rates.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>