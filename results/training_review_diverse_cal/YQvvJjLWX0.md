Now I have a thorough understanding of the paper and the reviews. Let me construct the final consolidated review.

## Summary

The paper proposes Semantic Entropy Probes (SEPs), linear logistic regression classifiers trained on LLM hidden states to predict binarized semantic entropy. SEPs combine the cost efficiency of probing (operating on a single generation at test time) with the superior generalization properties of semantic uncertainty as a supervisory signal. Across 5 models, 4 QA datasets, and both short- and long-form generation settings, the paper shows that SEPs generalize out-of-distribution significantly better than accuracy probes (2.2–10.5 AUROC points improvement), while approaching but not matching the performance of 10× costlier sampling-based methods. A counterfactual context-addition experiment confirms that SEPs capture genuine model uncertainty rather than spurious correlations.

## Strengths

- **Clear practical contribution with strong empirical support.** SEPs reduce the test-time cost of semantic uncertainty quantification to a single forward pass, eliminating the 5–10× overhead of sampling-based SE. This addresses a genuine barrier to adoption. The OOD generalization advantage over accuracy probes is consistently demonstrated across 6 model/task combinations (Table 2, Fig. 6), with the largest gaps on Mistral-7B (10.5 ± 3.5) and Phi-3 (9.9 ± 2.9).

- **SE can be predicted before any tokens are generated (TBG).** Figure 4 shows that SEPs achieve strong AUROC values (consistently 0.7–0.9+) from the token-before-generation position across models and datasets, enabling uncertainty quantification in a single forward pass without any generation. This is a novel capability not shown in prior probing work.

- **Counterfactual intervention provides strong causal evidence.** The context-addition experiment (Fig. 5) shows that adding context to TriviaQA questions causes SEP-predicted probabilities of high SE to shift from ≈0.9 to ≈0.5, mirroring the ground-truth SE drop from 1.84 to 0.50. This establishes that SEPs capture intrinsic model uncertainty rather than shallow dataset correlations.

- **Thorough ablation study across layers, token positions, and model scales.** Results span Llama-2 7B/70B, Mistral-7B, Phi-3, and Llama-3-70B, covering both short-form (~15 char) and long-form (~100 char) generations, with consistent patterns across layers (peaking in mid-to-late layers).

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Layer selection procedure for aggregated results is underspecified.** The paper reports results "for a representative set of high-performing layers" (lines 374, 385) but does not specify in the main text which layers were chosen, how many, or whether the same layers were used for SEPs and accuracy probes. If different layers were selected for each probe type, the comparison could be biased in favor of one method. The appendix presumably contains these details, but the main text should state the selection criterion explicitly (e.g., "top-3 layers by validation AUROC per probe type") and include a fixed-layer comparison as a robustness check.

- **In-distribution results show high variance in the long-form setting.** Table 1 reports a ΔAUROC of −1.9 ± 7.5 for Llama-2-70B long-form generations. While the paper's conclusion that SEPs and accuracy probes perform similarly in-distribution is reasonable, error bars of ±7.5 AUROC points mean the comparison is not stable and could flip direction depending on the split or seed. This does not affect the OOD claims (which are the paper's main contribution), but it limits confidence in the in-distribution comparison.

### Trivial

- **The paper describes SEPs as "directly approximating SE"** (abstract, line 8) when the probes are actually trained on a binarized version of SE (threshold minimizing within-group variance, Eq. 1). Section 4 transparently describes the binarization, so this is not misleading to a careful reader, but the abstract could add one clarifying word (e.g., "binarized SE"). Similarly, describing SEPs as "unsupervised" (line 378) is correct in that no ground-truth accuracy labels are needed, but could be misinterpreted as requiring no upfront cost — the paper is transparent about needing SE computation on training data.

## Nice-to-Haves

- **Quantitative cost comparison.** The paper emphasizes the cost savings of SEPs over sampling-based methods but provides no concrete numbers (FLOPs, wall-clock time, or forward passes). A simple table comparing inference cost of SEPs, accuracy probes, SE, and p(True) would make the efficiency contribution more concrete and easier to evaluate.

- **Mechanistic analysis of why SE generalizes better.** The Discussion section (lines 446–458) offers plausible speculation (SE is more model-internal, accuracy labels are noisy and task-specific) but no direct evidence. Expanding the analysis of which hidden dimensions are used by SEPs vs. accuracy probes, or testing generalization on a qualitatively different distribution (e.g., instruction following or summarization), would strengthen the mechanistic claim.

## Removed Points

These points from the reviews were considered but removed or downgraded with justification:
- **"Binarization is a methodological concern"** — The paper fully and transparently describes binarization in Section 4 (lines 185–207) and evaluates against binarized SE gold labels (line 254). Predicting binarized SE for a binary hallucination detection task is a sensible design choice, and the paper never claims to predict continuous SE values. This is a presentation nitpick, not a substantive weakness.
- **"Compare against non-QA tasks"** — This would expand the paper's scope beyond its stated domain. A useful future direction but not a weakness of the current paper, which covers 4 diverse QA datasets and two generation lengths.

## Novel Insights

The reviews collectively surface an interesting tension: SEPs consistently outperform accuracy probes on OOD generalization (their headline result), but the in-distribution comparison is noisier and occasionally favors accuracy probes. This asymmetry — better OOD, comparable/slightly worse ID — actually strengthens the paper's central argument that SE is a more transferable supervisory signal than accuracy, since accuracy probes can exploit task-specific shortcuts that do not generalize. The counterfactual context experiment provides unusually direct causal evidence for this interpretation, which is rare in the probing literature where most claims about "what probes capture" rely on correlation rather than intervention.

## Suggestions

- In the main text, specify the layer selection criterion explicitly (e.g., "top-3 layers by held-out validation AUROC, selected separately for each probe type") and report results for fixed layers as a sanity check.

## Score and Decision

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>