- Decision: Reject
- Avg Score: 4.75
- Scores: 5, 6, 3, 5
I have thoroughly verified all claims against the paper. Here is my consolidated review.

---

## Summary

MAGNET adapts a decoder-only LLM (LLaMA‑2‑7B) by modifying its attention mask to blend bidirectional and causal attention, then fine-tunes with three self-supervised objectives (masked next token prediction for token representations, contrastive learning for sentence representations, and missing-span generation for infilling/generation) in a single training framework. The central claim is that this unified approach gives a decoder-only model robust encoding, infilling, and low-repetition generation capabilities that prior adaptation methods cannot simultaneously provide.

## Strengths

1. **Novel combined attention mechanism** — The paper introduces an attention mask (Section 3.1, Figure 2) that allows context tokens to attend bidirectionally while span tokens attend to all context tokens and maintain causal order among themselves. This design cleanly enables the three training objectives to operate within the same model, a clear departure from prior work that uses only one attention pattern.

2. **Superior representation learning over existing decoder adaptations** — On word-level tasks (Table 1: chunking, NER, POS) and sentence-level STS/clustering tasks (Tables 2–3), MAGNET outperforms LLM2Vec, LLM2Vec[MNTP], and Echo Embeddings when applied to the same LLaMA‑2‑7B base model. These are head-to-head, controlled comparisons that directly support the claim that joint multi-objective training provides an advantage over training representation objectives alone.

3. **Quantified and dramatic reduction in generation repetition** — The paper shows (Section 4.4, explicitly on line 197) that LLM2Vec makes LLaMA‑2‑7B 36.5× more likely to repeat sentences, while MAGNET raises repetition by only 2.7×. This identifies and solves a real failure mode of bidirectionalized decoders that prior work (including LLM2Vec) did not address.

4. **Demonstrated infilling improvement over the base model** — On infilling perplexity (Table 4) and human evaluation of contextual appropriateness (Table 5), MAGNET substantially outperforms the base LLaMA‑2‑7B and its zero-/few-shot variants, confirming that the attention modification and MSG objective effectively leverage future context.

5. **Disentangled token-level and sentence-level representations** — By using the last-token ([EOS]) embedding for sentence-level tasks and the preceding-token embedding for token-level tasks (Sections 3.2.2, 4.1), MAGNET avoids interference between the two representation objectives during joint training, a practical design choice justified by the architecture.

## Weaknesses

### Fatal
None.

### Major

1. **Overclaim in abstract conflating method with model scale** — The abstract states that MAGNET-adapted LLMs "can outperform state-of-the-art text encoders on token-level and sentence-level representation learning tasks." Table 1 includes comparisons against DeBERTa‑V3 and RoBERTa‑Large (hundreds of millions of parameters) using a 7B-parameter model. This conflates the adaptation *method* with model scale. The fair, controlled comparisons against LLM2Vec (same base model, Table 1) and Echo Embeddings (Tables 2–3) are the real evidence and are favorable. The abstract claim should be qualified to reflect that the primary comparison is against other *adaptation methods* applied to the same base model, not against all text encoders regardless of scale. This is a presentation issue, not a flaw in the method itself, but it misrepresents the contribution.

2. **No standard language-modeling perplexity evaluation for generation quality** — The paper claims that MAGNET "retains" generative capability (and the repetition analysis supports this claim for the repetition dimension), but it does not report perplexity on a held-out language modeling test set (e.g., Wikitext‑103) for the adapted model vs. the base LLaMA‑2‑7B. Without this, a reader cannot verify whether overall fluency or likelihood has degraded as a side effect of joint training. This is a straightforward evaluation to add and would directly substantiate a central claim of the paper.

### Minor

1. **No dedicated infilling baselines** — Tables 4 and 5 compare MAGNET only against the base LLaMA‑2‑7B and its variants. While the paper's scope is specifically about augmenting the *base LLM*, adding at least one strong dedicated infilling model (e.g., BART‑large or T5) would ground the practical value of the infilling capability. The absence does not invalidate the paper's claims (which are about the base model's improvement), but it leaves an open question about competitive significance.

2. **No statistical significance measures** — Results in Tables 1–5 are reported without error bars, confidence intervals, or significance tests. For large-scale benchmarks, single-run evaluation is common practice, and this alone does not undermine the results, but given the small gains on word-level tasks (0.2–0.6 points over LLM2Vec[MNTP]), significance information would increase confidence that the improvements are reliable.

### Trivial
None.

## Nice-to-Haves

- **Ablation of the three loss terms** — The claim that joint training is synergistic is supported only indirectly (MAGNET > LLM2Vec[MNTP]). An explicit ablation removing SSCL or MSG individually would directly demonstrate each component's contribution. Given computational cost, even a small-scale ablation would be informative.
- **Paraphrasing augmentation ablation** — Using only dropout as augmentation (standard SimCSE) would help verify that the paraphrasing augmentation (Damodaran, 2021) is necessary rather than just the contrastive objective being beneficial.

## Removed Points

The following points from the input reviews are removed per the consolidation rules:

- **Training details underspecified** (learning rate, batch size, optimizer, hardware, loss weights) — The reviewer acknowledges these may be in the appendix (which is stripped by the PDF parser). Per the hard rules: "REMOVE weaknesses about missing appendix, missing proofs in appendix, or absent references." Removed.
- **Table numbering confusion** (repetition table referenced as Table 5 conflicting with human evaluation Table 5) — This is a PDF-extraction artifact; the original submission has correct numbering. Removed.
- **Clustering table garbled / values unreadable** — PDF extraction artifact; the original table is legible. Removed.
- **Related work section absent from PDF** — Parser artifact; the section exists in the original submission. Removed.
- **"Text emphasizes comparison to LLM2Vec[MNTP] rather than full LLM2Vec"** — Misreading: the paper includes full LLM2Vec results in Table 1 and discusses them. Line 147 explicitly compares against "powerful encoder models and LLM2Vec." Removed.
- **Criticism about missing apparatus for MNTP augmentation** (dropout-only ablation) — Moved to Nice-to-Haves; not a weakness of the presented method.
- **Generic "could be a proxy" / "confounders" speculation** — These are area-of-concern sweeps without specific anchors in the paper. Removed.
- **Strength Finder generic strengths** (e.g., "addressed an important problem") — Removed for lacking concrete content or conflicting with verified weaknesses.

## Novel Insights

None beyond the paper's own contributions. The reviewers identified genuine weaknesses (overclaim, missing perplexity evaluation) and strengths (attention design, controlled comparison against LLM2Vec, repetition analysis) but did not surface observations about the method or findings that go beyond what the authors themselves articulate.

## Suggestions

1. **Qualify the abstract claim about "outperform[ing] state-of-the-art text encoders"** to clarify that the comparison is against other *adaptation methods* applied to the same base model (LLM2Vec, Echo Embeddings) rather than all text encoders regardless of scale. This would make the claim accurate and not misleading.

2. **Add a perplexity evaluation** on Wikitext‑103 test set (or an equivalent held-out LM benchmark) comparing MAGNET-adapted LLaMA‑2‑7B against the base model. This addresses the most significant evidence gap and directly supports the claim of retained generation capability.

3. **Report the loss weights λ₁, λ₂, λ₃** (and any hyperparameter tuning done for them). This is critical for reproducibility since these weights determine the trade-off among the three objectives. If these are in the appendix, ensure they are also in the main text.

4. **Run a small-scale ablation study** removing SSCL or MSG individually to demonstrate the synergy of joint training more directly.
