- Decision: Reject
- Avg Score: 4.75
- Scores: 5, 6, 3, 5
Now I have all the information I need. Let me compose the consolidated review.

---

## Summary

This paper studies the effect of weight decay (L2 regularization) on token-level learning dynamics in language models. The authors show empirically, across four model variants (OpenELM 270M & 3B, Qwen2 0.5B & 1.5B) trained on IMDB/IMDB-xl with varying weight decay values, that increasing weight decay disproportionately increases loss on low-frequency tokens while leaving high-frequency tokens largely unaffected. Crucially, they demonstrate that this degradation is masked by the standard average training loss metric, but clearly visible in a token-balanced loss. A theoretical analysis using the unconstrained features model (UFM) with non-negative constraints shows the effect is structural (emerging at global minima), not merely a training artifact.

## Strengths

1. **Robust empirical demonstration across architectures and scales.** The core finding — that weight decay disproportionately harms low-frequency tokens — is replicated across two model families (OpenELM and Qwen2) at multiple sizes (270M–3B), on two dataset sizes (25K and 75K samples), with 5 random seeds each. The consistency of the pattern across these configurations makes it unlikely to be an artifact of a single architecture or training run.

2. **Token-balanced loss directly reveals the "silent" degradation.** Table 1 is the paper's most compelling evidence: the average training loss increases from 0.051 (λ=0.0) to 0.068 (λ=1.0) — a small absolute change — while the token-balanced loss jumps from 0.066 to 0.163 (a ~2.5× relative increase). This contrast cleanly demonstrates how a standard aggregate metric can hide a significant token-level bias, which is the paper's central claim.

3. **Theoretical grounding shows the phenomenon is structural, not a training artifact.** The analysis using the non-negative UFM framework (Section 5, building on Dang et al., 2024) derives that low-frequency tokens have larger per-token loss at any global minimum, and that this loss increases faster with weight decay for lower-frequency tokens. The claim that the effect would persist even with optimal training distinguishes the paper from purely empirical studies and explains why the problem is not easily fixable by better optimization.

4. **The per-token learning-speed metric provides orthogonal behavioral evidence.** The AUC-based learning-speed measure (Section 3, Figure 5b) confirms the loss-based findings using a distinct signal: the learning-speed gap between λ=0.1 and λ=1.0 widens for low-frequency tokens but narrows for high-frequency ones, corroborating the main result without relying on the same metric.

5. **Demonstrates the problem is amplified by growing vocabulary sizes.** Figure 2(b) shows that the proportion of low-frequency tokens (below the 95th percentile) increases with vocabulary size, converging to ~0.85 — directly linking the finding to the trend of expanding vocabularies in modern LLMs (LLaMA-3, Qwen2, Gemma-2).

## Weaknesses

### Fatal

None.

### Major

- **The experimental setup is far from representative of modern LLM training, undermining the generality of the claims.** The models are trained on IMDB (25K–75K samples, ≤75K training sequences) with a BPE tokenizer trained *on IMDB alone* (32K vocabulary), context lengths of 64–128 tokens, and only 10K training steps. The paper frames its findings as broadly about "LLM training" (citing LLaMA, GPT-3, Qwen2 as motivation), but provides no evidence that the same phenomenon occurs when training on trillions of tokens with general-domain vocabularies of 128K+. This gap does not invalidate the controlled finding, but it means the paper's central claim about LLM training is overstated relative to the evidence provided. Either validating the effect in a more realistic setting (e.g., fine-tuning a pretrained LLM on a general-domain corpus) or scaling back the claims to match the experimental scope is needed.

### Minor

- **The "silent" framing is slightly overstated.** The paper claims the average training loss remains "largely unchanged" (abstract, caption, conclusion). Table 1 shows it increases from 0.051→0.068 — a 33% relative increase. While the absolute change (0.017) is small in language modeling terms, and the contrast with the token-balanced loss (0.066→0.163) still supports the central point, a 33% relative increase is non-negligible. A more precise framing would acknowledge the average loss does shift measurably, but the *per-token imbalance* is far larger and entirely obscured by aggregation.

- **"Fairness across tokens" is invoked but never defined.** The abstract calls for "novel regularization techniques that ensure fairness across all available tokens" and the research question uses "fairness across tokens" (line 41), but the term is never formally defined or measured. The paper studies token-level loss degradation, not fairness in any standard sense (demographic parity, equal opportunity, etc.). This rhetorical choice risks overclaiming the societal implications.

- **The manuscript contains an incomplete placeholder.** Line 242 includes a visible annotation: `{\color{red}Add their first part of corollary 4.6}`. This indicates the theoretical discussion was not fully prepared at submission time and weakens reader confidence in the manuscript's completeness.

- **The contribution is incremental rather than revelatory.** The paper correctly cites prior work establishing that L2 regularization disproportionately harms minority classes in vision settings (Kang19, Cao19, balestriero2022effects, Dang et al. 2024). The finding that a similar effect holds for token-level prediction in language models is a natural domain extension rather than a surprising discovery. The paper would be stronger by presenting itself as a careful validation and characterization of this known effect in LLMs, rather than as a paradox or unexpected finding.

### Trivial

- The phrase "As weigth decay increases" contains a typo (Figure 1 caption, line 23).
- The paper could show accuracy specifically on low-frequency tokens (not just overall per-token accuracy), as Full-Table-1 gives only aggregate per-token accuracy (~98.8%), which the per-frequency-bin figures partly address but without numeric precision.

## Nice-to-Haves

- **Downstream evaluation.** The paper analyzes training loss exclusively. Demonstrating that the token-level degradation translates to practically meaningful harm (e.g., perplexity on rare-word subsets, generation quality on prompts involving rare tokens) would strengthen the practical relevance.
- **Comparison to alternative regularizers.** The paper does not test whether dropout, label smoothing, or spectral normalization exhibit similar or different token-frequency biases, which would contextualize whether the observed effect is unique to weight decay or a broader property of regularization.
- **Characterization of which tokens are harmed.** The paper does not analyze whether the degraded low-frequency tokens are domain-specific terms, valid subwords, or subword fragments. This matters for assessing practical severity (e.g., harming "mull" and "iss" may be less concerning than harming rare technical terminology).
- **Ablation at very small weight decay.** Testing whether even λ=0.01 already shows the pattern would help practitioners understand whether this is a threshold effect or a continuum.

## Removed Points

These points were flagged by the reviewers but removed after verification against the paper:

- *"The paper does not acknowledge the mismatch between UFM and the actual training setup."* — **Removed.** The paper explicitly states on line 225: "While the above formulation does not exactly match the practice (since H is a matrix of free parameters instead of the outputs of a neural network), this abstraction can help understand..." The mismatch is acknowledged. The derivative analysis with λ_W=λ_H=λ is a stated simplifying assumption, not an oversight.

- *"Low-frequency tokens may be garbled subwords — harming noise is not a concern."* — **Removed.** The paper provides concrete examples (Figure 2) of low-frequency tokens such as "mull", "ain", "iss" — these are legitimate subwords from English text, not garbled noise. The characterization is subjective and not supported by evidence in the review.

- *"Per-token accuracy should be reported separately for low-frequency tokens."* — **Removed.** The paper already provides per-token loss and accuracy by frequency bin in Figures 4(a) and 4(b), showing the breakdown the reviewer asks for.

- *"No evaluation on downstream tasks — loss alone doesn't demonstrate practical harm."* — **Moved to Nice-to-Haves.** This asks for additional experiments beyond the paper's stated scope (studying optimization dynamics). It is a reasonable suggestion for strengthening the paper but not a flaw in what is presented.

- *"The UFM theory would be more convincing if the paper derived a direct prediction..."* — **Moved to Nice-to-Haves.** This is a suggestion for strengthening, not a weakness.

- *"No discussion of whether the effect is monotonic beyond λ=1.0."* — **Moved to Nice-to-Haves.** This is a natural extension question.

## Novel Insights

The harsh critic and strength-finder mostly converge on the same evidence. The most interesting insight that emerges from combining the two is a calibration point: the paper's "silent" claim is simultaneously *well-supported* (the average-vs-balanced loss contrast in Table 1 is genuinely striking) and *slightly overplayed* (a 33% relative rise in average loss is not nothing). The meta-insight is that the paper's strongest single piece of evidence — the 2.5× gap between average and balanced loss trajectories — makes the central thesis robust even if one dials back the rhetorical framing. A second synthesis insight is that the paper's scope-gap problem (IMDB vs. trillion-token training) interacts with the incremental-novelty question in a non-trivial way: confirming a known effect in a more realistic LLM regime would have been a stronger contribution than confirming it in a narrow setting that does not resemble the regime the paper claims to speak about.

## Suggestions

1. **Scale the claims to match the evidence.** Replace sweeping references to "LLM training" with precise descriptions of the controlled setting (e.g., "small-scale language model training from scratch on a domain-specific corpus"). Either add experiments in a more realistic regime or caveat the generality clearly.

2. **Tighten the "silent" framing.** Acknowledge that the average loss does increase modestly (33% relative) while emphasizing that the token-balanced loss increases far more (~2.5× relative) — the key point is the *discrepancy* between the two metrics, not the absolute stability of the average.

3. **Define or remove "fairness."** If the paper intends to claim a fairness implication, it should define what notion of fairness is being violated and connect to the existing algorithmic fairness literature. Otherwise, replace "fairness" with more precise language (e.g., "token-level performance disparities").

4. **Clean up the incomplete annotation.** The placeholder text on line 242 should be completed before any publication.

5. **Add a per-frequency accuracy table or figure with numerical values.** The current figures show trends visually; adding a table with exact accuracy values for low-, medium-, and high-frequency token groups under each λ would strengthen the quantitative record.
