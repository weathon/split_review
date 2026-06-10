Here is my final consolidated review.

---

## Summary

PUMA proposes an MPC framework for secure Transformer inference with novel polynomial approximations for GELU and Softmax, faithful LayerNorm and Embedding protocols in MPC, and end-to-end compatibility with pre-trained plaintext models without retraining. The paper demonstrates accuracy within 0.011 of plaintext across multiple BERT/GPT2 models and reports the first MPC evaluation of LLaMA-7B (~200 seconds per token). The technical contributions are genuine, but the paper overstates its efficiency advantage through a selectively chosen baseline and an aspirational title/abstract.

## Strengths

- **Accuracy preservation within 0.011 of plaintext without retraining.** Across Bert-Base, Roberta-base, and Bert-Large on CoLA, RTE, and QNLI, PUMA's accuracy differs from plaintext by at most 0.011; GPT2 perplexity differences are ≤0.02 (Section 5.1, lines 177–179). This is a concrete, measured improvement over prior MPC approaches that required fine-tuning and still could not match plaintext accuracy.

- **First MPC evaluation of a 7B-parameter model (LLaMA-7B).** Section 5.4 (lines 229–231) reports the first successful MPC inference of LLaMA-7B at ~200 seconds per token with 1.794 GB communication. This is a genuine scalability advance over prior work limited to much smaller models.

- **Empirical demonstration that faithful LayerNorm matters.** Footnote on line 149 shows that replacing LayerNorm with BatchNorm (as MPCFormer does) collapses the CoLA MCC score from 0.616 to −0.020, while PUMA achieves 0.613. This directly validates the need for PUMA's LayerNorm protocol.

- **Practical engineering contribution addressing the 2GB serialization limit.** Lines 227–228 describe a workaround for the Protobuf/FlatBuffers 2GB trunk limit that would otherwise prevent distributing LLaMA-7B's secret-shared weights.

## Weaknesses

### Fatal

None.

### Major

- **The headline efficiency claim rests on a selectively chosen baseline.** The paper compares PUMA's runtime against MPCFormer *without* its Quad approximations (the slower variant), reporting ~2× speedup. The justification is that Quad requires retraining, which PUMA does not. However, the abstract and title claim "2× faster than the state-of-the-art framework MPCFormer" without this qualification. A reader reasonably expects "state-of-the-art" to include the fastest available configuration. The paper never reports how PUMA compares to MPCFormer+Quad (which, if faster, would invert the comparison). This makes the headline speedup claim difficult to interpret. The paper should either compare against MPCFormer+Quad with a full accounting of the accuracy–retraining–speed trade-off, or clearly qualify the claim in the abstract and title.

- **Title and abstract over-promise on the LLaMA-7B result.** The title "Secure Inference of LLaMA-7B in Five Minutes" is unqualified. The body clarifies this means ~200 seconds for generating *one token* from an 8-token input on 3 extremely expensive servers (128 vCPUs, 1TB RAM each, 20GB bandwidth). Generating 32 tokens would take ~107 minutes. While the paper is honest about the raw numbers, the framing implies a level of practicality that the system does not deliver. The contribution (first LLaMA-7B MPC evaluation) is real and should be presented as a feasibility milestone, not as a practically deployable capability.

### Minor

- **No component-level cost breakdown for LLaMA-7B inference.** The 200-second single-token latency is reported as a monolithic number (Section 5.4). Breaking it down into attention, FFN, embedding, LayerNorm, and communication costs would help identify bottlenecks for future work and give readers a clearer picture of where the time goes.

- **One-hot embedding overhead acknowledged but never quantified.** The paper notes that one-hot computation in MPC adds overhead (lines 201, 214–215) and causes efficiency gains to decrease with larger batches and longer sequences. However, it never reports what fraction of total runtime this accounts for, making it hard to assess the cost of the "plaintext-compatible design choice."

### Trivial

None.

## Nice-to-Haves

- A direct comparison against MPCFormer with Quad approximations (including the accuracy after retraining) would be the single most informative addition. It would either confirm PUMA's advantage (if PUMA is comparably fast with better accuracy and no retraining) or reveal the true trade-offs.
- A cost projection for multi-token generation with LLaMA-7B (e.g., 32 or 128 tokens) would help readers understand the practical cost structure.
- An ablation isolating the contribution of each approximation (GELU vs. Softmax vs. Embedding vs. LayerNorm) to latency and accuracy would strengthen the evidence for the design choices.

## Removed Points

These points were flagged in the reviews but are not valid weaknesses of the paper:

- **"Core protocols inaccessible in extracted text"** (Harsh Critic #3) — The protocols are in separate files (`\input{Protocols/Gelu}`, etc.) that are part of the submission. Parser extraction limitations do not reflect an author error.
- **"No variance or statistical analysis"** — MPC protocols are deterministic given fixed inputs and network conditions; single-run evaluation is standard in this community.
- **"No discussion of GELU/Softmax approximation form"** — The main text states the approach is "based on the specialized properties of these non-linear functions" (line 35); specific forms are detailed in the protocol files which are part of the submission.
- **Strength Finder claim that is generic/overly broad** — None found; all identified strengths are concrete and evidence-grounded.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **In the abstract and title, qualify the efficiency and LLaMA-7B claims.** E.g., "PUMA is ~2× faster than MPCFormer (without Quad approximations)" and "Secure Inference of LLaMA-7B Under MPC" would be more precise. Alternatively, add the MPCFormer+Quad comparison to justify the unqualified statement.
2. **Provide a component-level latency breakdown** for the LLaMA-7B run so readers can see where the 200 seconds are spent.
3. **Quantify the one-hot embedding overhead** explicitly (e.g., "X% of total runtime is spent on one-hot embedding") so the cost of plaintext compatibility is transparent.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>