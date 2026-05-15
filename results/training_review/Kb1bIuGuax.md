Now I have a thorough verification of the paper's content against the reviewer claims. Let me produce the final review.

---

## Summary

This paper studies how weight decay (L₂ regularization) in LLM training affects token-level performance, focusing on the discrepancy between low-frequency and high-frequency tokens. Training OpenELM (270M, 3B) and Qwen2 (0.5B, 1.5B) models on IMDB movie reviews with varying weight decay, the authors show that increasing weight decay raises per-token cross-entropy loss more sharply for low-frequency tokens than for high-frequency ones, and that this effect is partially masked when monitoring only aggregate average training loss. A theoretical analysis using an unconstrained features model provides a mathematical framework for understanding this frequency-dependent bias.

## Strengths

- **Cross-architecture and multi-scale demonstration**: The paper shows the weight-decay-by-frequency interaction consistently across four model/dataset combinations (OpenELM 270M & 3B, Qwen2 0.5B & 1.5B, on IMDB and IMDB-xl), with results averaged over 5 random seeds with reported variance — good empirical practice within its chosen scope.

- **Introduction of token-level metrics that reveal hidden bias**: The token-balanced loss (averaging cross-entropy by token type rather than by occurrence) and the per-token learning speed metric (AUC-based) are well-motivated tools for detecting frequency-dependent effects that aggregate metrics obscure. Table 1 and Figure 3 demonstrate concretely that the token-balanced loss rises 2.5× (0.066 → 0.163) while average training loss rises only 33% (0.051 → 0.068) across λ ∈ [0.0, 1.0].

- **Clear motivation from token-frequency analysis**: Figure 2 quantifies the extreme imbalance in the IMDB dataset (95% of total tokens captured by the top 0.01% of the vocabulary), grounding the research question in a concrete measurement of the class-imbalance problem in language modeling.

- **Theoretical scaffolding from an established framework**: The paper adapts the Unconstrained Features Model (Dang et al., 2024) to derive closed-form expressions for per-token loss as a function of frequency and weight decay. While the theory's assumptions (d ≥ V) do not match the experimental setting, the qualitative predictions (low-frequency tokens have higher loss; this gap widens with λ) align with the empirical findings and provide a useful conceptual lens.

## Weaknesses

### Fatal
None. The paper's core observational claim — that weight decay disproportionately affects low-frequency tokens in this setup — is supported by the evidence presented. However, the following major issues severely limit the strength and generality of the conclusions that can be drawn.

### Major

1. **No held-out evaluation is presented anywhere in the paper.** All results (training loss, token-balanced loss, accuracy, perplexity, learning speed) are measured on the training set. For a paper whose central narrative is about *generalization* and about a regularization technique intended to *promote generalization*, the absence of validation/test loss or perplexity on held-out data is a fundamental omission. The models achieve per-token perplexities of 1.069–1.177 (Table 1), which are trivially low and indicate heavy overfitting/memorization. Without held-out evaluation, it is impossible to know whether the observed frequency-dependent degradation reflects a meaningful property of the loss landscape or merely the model's memorization dynamics on a small (25k–75k sample) dataset.

2. **The experimental scope is too narrow to support the paper's sweeping language-level claims.** Experiments are conducted on a single dataset (IMDB movie reviews) using a BPE tokenizer trained on that same 25k-document corpus. The token frequency distribution is therefore an artifact of a narrow domain and a corpus-specific tokenizer, not of "most languages" as stated in the abstract. Context lengths of only 64–128 tokens and 10,000 training steps are dramatically smaller than those used in practical LLM training. The paper's claims about implications for "real-world applications," "fairness," and "bias" (conclusion and broader impact) are extrapolated from a setup that shares little with production LLM training pipelines.

3. **The "silent" degradation claim is overstated.** Table 1 shows the average training loss increases from 0.051 to 0.068 — a 33% relative increase — as λ goes from 0.0 to 1.0. Calling this "largely unchanged" (Figure 1 caption, repeated in Figure 4 caption) downplays an observable shift. While the token-balanced loss increases much more (147%), the claim that practitioners "would not detect" the problem is unsupported: practitioners monitor validation perplexity, not just training loss, and the paper provides no evidence about validation metrics. The "silent" framing is a narrative device rather than a demonstrated empirical finding.

4. **The theoretical analysis operates in a regime that does not match the experiments.** The UFM analysis requires the feature dimension d ≥ V (vocabulary size, here 32,005). In all models studied, the hidden dimension is far smaller (d ~ 1024–3072 for the model sizes used). The paper acknowledges this is an "abstraction" (line 225) but then asserts that "these theoretical results emphasize that they are actually caused by a fundamental issue" (line 252). The theoretical results provide intuition but not proof for the experiments presented; the mismatch between the theory's premises and the experimental conditions is a logical gap.

### Minor

- **The paper does not propose or test any mitigation strategy.** The conclusion calls for "novel regularization techniques that ensure fairness across all tokens" but offers no suggestions or baselines. Without comparison to alternative approaches (e.g., token-frequency reweighting, no weight decay with early stopping, temperature scaling), the paper remains purely descriptive of a phenomenon already documented in the class-imbalance literature.

- **The token-balanced loss metric has high variance for very rare tokens.** Tokens appearing only once in the dataset contribute a single data point to their class's loss estimate, making the per-token loss for the rarest tokens unreliable. This is not discussed.

- **The theoretical derivation skips steps** (e.g., the derivative expression in line 250 is stated without showing how it follows from the earlier expressions), making it difficult to verify the claim that low-frequency token loss grows faster under weight decay.

- **Key claims about fairness and bias are not operationalized.** The broader impact statement mentions "fairness" and "bias" but the paper never defines these terms or measures them in any socially meaningful way. The leap from token frequencies in IMDB to fairness implications for population groups is unsupported.

### Trivial
- The y-axis ranges differ across panels in Figure 1, which slightly exaggerates the visual contrast between low- and high-frequency loss trajectories. A relative-change metric would be more informative.
- "weigth" typo in Figure 1 caption (line 23).

## Nice-to-Have Suggestions

- Validation/test evaluation on a held-out set (ideally from a different domain) to distinguish memorization from generalization effects.
- A controlled scaling experiment with realistic context lengths (512+) and a larger, more diverse dataset (e.g., C4 or The Pile) to test whether the observed effect persists at scale.
- Disentanglement of token frequency from other correlated properties (token length, subword boundary anomalies, semantic category).
- Comparison of weight decay against alternative regularization techniques or token-frequency reweighting.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"The paper largely replicates known class-imbalance effects..."** — The paper explicitly acknowledges this prior work (Section 2, "Training with Imbalanced Classes and Minority Collapse," and line 64–68), frames its contribution as extending it to language modeling, and shows the effect across multiple LLM architectures. Extending known phenomena to a new domain is a valid contribution, and the paper does not claim this is a novel discovery in classification.

- **"Figure 2 threshold is arbitrary"** — The 99th percentile is a standard statistical threshold and is clearly explained in the caption (line 33). The criticism that "true rare tokens (seen 1–5 times) are not highlighted" misunderstands the purpose of the visualization, which is to separate the bulk of the distribution.

- **"Binning by powers of 3 is arbitrary"** — This is a standard log-scale binning strategy for heavy-tailed distributions and is clearly documented in the paper (lines 205, 207).

- **"Figure 1 y-axis ranges differ"** — A presentation choice, not a substantive flaw. A more severe version of this point is retained under Trivial.

- **"Opening sentence is false"** — The paper's claim about "little is known about their training dynamics at the token level" is a general statement. The relevant prior work on token-level dynamics in LLMs (distinct from class-imbalance in vision) is not so well-established that this claim is false, and the paper's specific focus (weight-decay × token-frequency interaction) is indeed understudied in the LLM literature.

- **"Context lengths of 64-128 are absurdly short"** — While genuinely limiting (retained under Major weakness 2), the paper documents this choice and it is a design decision. The severity of this criticism as a standalone point is better subsumed under the broader scope-limitation weakness.

- **Proposition 1 "fragment"** — The restatable appears complete (lines 244–246). The \end{restatable} may have been stripped by the parser; this is not an author error.

## Novel Insights

The reviews do not surface a genuinely novel insight beyond the paper's own contribution. The key observation — that aggregate metrics can mask frequency-dependent degradation from regularization — is the paper's main finding, but the reviews primarily serve to identify the gap between the paper's ambitious claims and its limited evidence, rather than adding a new lens on the problem.

## Suggestions

1. **Add held-out evaluation as a matter of priority.** Without validation/test loss or perplexity, the paper cannot support claims about generalization. This is the single most important addition.

2. **Tone down the scope of claims.** Replace "most languages" with "the IMDB dataset," and reframe the contribution as a focused empirical study of token-frequency effects under weight decay in small-scale language modeling. Remove or substantially qualify the fairness/bias framing unless it is operationalized.

3. **Clarify what "silent" means precisely** (e.g., the ratio of token-balanced loss to average loss, or the correlation between average loss and per-token losses across λ). The current framing as "average loss remains largely unchanged" is contradicted by a 33% increase.

4. **Make the theoretical section's limitations explicit.** Acknowledge directly that the results require d ≥ V and global optimality, neither of which is satisfied in the experiments, and clarify that the theory provides qualitative intuition rather than a proof.

5. **At minimum, discuss or cite a mitigation strategy** so the paper offers more than a diagnosis of a problem without any path forward.

## Score and Decision

The paper identifies a real and important concern — that commonly used regularization may introduce frequency-dependent biases in LLM training that are partially hidden from aggregate metrics. The experiments are carefully run within their chosen setup (multiple architectures, seeds, confidence intervals). However, the paper's claims substantially outrun its evidence: no held-out evaluation, a single narrow-domain dataset with a corpus-specific tokenizer, unrealistic context lengths, an overstated "silent" narrative, and a theoretical analysis whose conditions are unmet. The contribution — confirming that class-imbalance effects documented in vision also appear in a small-scale language modeling setup — is modest and would need substantially stronger experimental support (diverse data, held-out evaluation, realistic training configurations) to merit acceptance at a top venue. As a descriptive finding in a limited setting, the paper could find a home at a workshop or a more applied venue, but in its current form it falls short of the bar for a major conference.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>