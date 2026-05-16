Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

---

## Summary

This paper proposes a post-training compression method that merges adjacent feed-forward sublayers in Transformers by: (1) permuting neurons via correlation-based alignment to match activations across sublayers, (2) averaging the aligned weight matrices, and (3) tying the merged parameters so only one copy is stored. The method is evaluated on GPT-2 (language modeling), ViT (image classification), and an OPUS-MT translation model, showing that merging one-third of FF sublayers preserves near-original performance while removing over 21% of total parameters in ViT.

## Strengths

- **Effective across diverse architectures and modalities**: The method is tested on decoder-only (GPT-2), encoder-only (ViT), and encoder–decoder (OPUS-MT) Transformers, covering two modalities (text and vision). Across all three, merging 1/3 of FF sublayers retains near-original performance (ViT loses ~1% accuracy, GPT-2 incurs ~1 PPL increase). This breadth is the paper's strongest evidence that the approach generalizes.

- **Outperforms a strong structured-pruning baseline**: At comparable compression ratios, the proposed merging method consistently matches or exceeds a layer-dropping baseline (Figure 3). The layer-dropping baseline is itself strong — it uses the same sliding-window selection and fine-tuning protocol, making the comparison fair and favorable.

- **Robust to design choices**: Ablations show that the method is insensitive to which specific sublayers are merged (Table 2) and which anchor layer is used for permutation alignment (Table 3), with all variants achieving similar post-fine-tuning performance. This substantially strengthens the practical reliability of the approach.

- **Orthogonal to quantization**: Combining the method with LLM.int8() quantization (Table 4) yields further compression with negligible additional degradation (e.g., ViT accuracy drops only 0.1% from 84.1% to 84.0%), demonstrating practical compatibility with other compression techniques.

## Weaknesses

### Fatal

None.

### Major

None. The weaknesses below are substantive but addressable; none invalidate the paper's core claims.

### Minor

- **"Quick fine-tuning" claim is not quantitatively supported**: The paper describes the fine-tuning as "a small amount" that "quickly" restores performance, but reports up to 100k steps for GPT-2 (batch size 2) and the translation model, and 50k steps for ViT (batch size 128). No learning curves, step-wise performance trajectories, or ablations over fine-tuning length (e.g., 1k, 5k, 10k steps) are provided, so the reader cannot assess how much fine-tuning is actually needed. This does not weaken the compression results themselves, but it does mean the characterization of efficiency is unsubstantiated.

- **No variance or statistical error reporting**: All results (perplexity, accuracy, BLEU) are presented as single numbers with no standard deviations, confidence intervals, or multiple-seed runs. Given that the differences between Permute FF Merge and Vanilla FF Merge are modest at 1/3 removal for some settings, and that fine-tuning involves randomness from data order and initialization, the reliability of fine-grained comparisons (e.g., which window is best before tuning) is unclear. While single-run evaluation is not uncommon in this space, the absence of variance reporting weakens the precision of the claims.

- **Incomplete model specifications**: The ViT variant (e.g., base vs. large) is not identified by hidden dimension or total parameter count — only resolution (224×224) and patch size (16×16) are given. The OPUS-MT model's hidden size, FF dimension, and total parameters are also unspecified. Hyperparameters such as learning rate, optimizer, schedule, warmup steps, and weight decay are absent. These omissions hinder reproducibility and should be added.

- **Mapping from "1/3 of FF sublayers removed" to concrete merge configurations is not explicitly stated**: The paper describes merging k adjacent sublayers into one (removing k−1 sublayers), and reports results at "1/3 of FF sublayers removed." The actual k values used for each model (e.g., k=13 for GPT-2 with 36 layers to remove 12 sublayers) can be inferred but are never stated. The number of merges performed (one merge of size k, or multiple) is also not clarified. This makes the experimental setup less reproducible than it should be.

- **CKA similarity analysis is not empirically linked to mergeability**: Section 5.5 identifies regions of high CKA similarity between FF sublayer outputs, and the paper suggests this may explain why merging works. However, a direct, quantitative link is missing: does the best-performing sliding window correspond to the region of highest CKA similarity? Without this connection, the CKA analysis remains an interesting observation rather than evidence for the method's rationale. Plotting pairwise CKA against post-fine-tuning performance per window would substantiate the claimed explanatory value.

- **Adjacent-only merging is not motivated**: The method only merges adjacent sublayers. The paper acknowledges non-adjacent merging as future work, but never discusses why adjacency is a reasonable constraint (e.g., whether CKA similarity is higher between adjacent sublayers than distant ones, as hinted by Figure 5). A brief justification would help the reader understand the design choice.

### Trivial

- The phrase "pack batches to the context length of 1024 after tokenization" (Section 4.1) is slightly ambiguous — it likely means sequences are concatenated/packed to fill the context window rather than truncated, but this could be clarified in one sentence.

## Nice-to-Haves

- **Additional compression baselines**: The paper compares only against layer pruning. While the paper's justification (structured pruning is the most comparable family) is defensible, comparisons to other post-training methods — e.g., neuron-level structured pruning with recovery, or other parameter-sharing approaches — would better contextualize the contribution. This is a desideratum, not a flaw.

- **Fine-tuning length ablation**: Adding an ablation that varies fine-tuning steps (e.g., 1k, 5k, 10k, 25k, 50k) with performance curves would substantiate or refine the "quick" recovery claim.

- **Discussion of overfitting to alignment data**: The permutation alignment uses validation data; a brief note on whether this risks overfitting to the alignment sample would strengthen methodological rigor.

## Removed Points

These points were flagged for removal and should be treated with caution; they reflect reviewer knowledge gaps, scope mismatches, or misinterpretations:

1. **"Thin comparison to other compression methods"** — The paper explicitly explains why it focuses on structured pruning (unstructured pruning requires specialized sparse libraries for actual memory savings; distillation and quantization are orthogonal families). Asking for more baselines beyond the most directly comparable one is scope creep; the paper's choice is defensible.

2. **"Pack batches" clarity concern** — This is a minor phrasing ambiguity that does not affect the paper's contributions or reproducibility in any meaningful way.

3. **Questions about random selection procedure in Table 2** — The paper says "we randomly select 3 sets of k consecutive layers" which is sufficiently clear. The reviewer's concern about whether these were "truly random or sampled from the some-are-good distribution after the fact" is not grounded in any evidence that the paper was misleading.

4. **Figures missing from parsed text** — The reviewer acknowledges this is a parser issue. The original submission contains the figures.

5. **Criticism about GPT-2 variant confirmation** — The paper states "36 layers and a feed-forward dimension of 5120," which unambiguously identifies GPT-2 large. The reviewer's query about this is resolved by the paper's own text.

## Novel Insights

The reviews surface a useful meta-point: the paper's CKA analysis is interesting but currently stands as a separate observation rather than an integrated part of the method's evidence. A natural follow-up — correlating pairwise CKA within each candidate window against post-fine-tuning performance — would transform this section from an interesting aside into direct mechanistic support. The reviewers also correctly note that the method's "quick fine-tuning" framing would benefit from concrete evidence, and that the experimental reporting would be strengthened by variance estimates. None of these points challenge the validity of the core contribution; they identify where the evidence could be tightened.

## Suggestions

1. Add a table reporting ViT variant (hidden dim, FF dim, total params), OPUS-MT architecture details, and all fine-tuning hyperparameters (learning rate, optimizer, schedule, warmup, weight decay).
2. Include a fine-tuning steps ablation with performance curves (e.g., 1k, 5k, 10k, 25k, 50k, 100k) to substantiate the "quick recovery" claim.
3. State explicitly the k values used for each compression ratio and model (e.g., "for GPT-2 with 36 layers, merging 13 FF sublayers into 1 removes 12/36 = 1/3 of FF sublayers").
4. Add a plot correlating pairwise CKA similarity within each candidate window against post-fine-tuning performance to connect the CKA analysis to mergeability.
5. Report results from at least 3 seeds with mean ± std for the main comparisons (Figures 2 and 3), especially for conditions where the Permute vs. Vanilla gap is small.

## Score and Decision

This paper presents a conceptually clean compression method that is novel (borrowing model-merging ideas for within-model compression), tested across a genuinely diverse set of architectures and tasks, and supported by reasonable ablations. The results are promising and the method is practical. The weaknesses are real but addressable — they concern the strength of claims and completeness of reporting rather than the validity of the core contribution. The paper would benefit from addressing the fine-tuning evidence gap, variance reporting, and specification completeness, but these are not structural flaws.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>