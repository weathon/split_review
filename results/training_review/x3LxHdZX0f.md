Now I have thoroughly verified all claims. Let me produce the final consolidated review.

---

## Summary

PUMA presents an MPC-based secure inference framework for Transformer models under a three-party replicated secret-sharing setting. The paper designs high-quality polynomial approximations for GeLU and Softmax, implements faithful secure Embedding and LayerNorm protocols, and demonstrates that pre-trained models can be evaluated under MPC without retraining or architectural modification. Empirically, PUMA achieves 1.4–2.4× speedup over the open-source baseline MPCFormer while maintaining accuracy within ≤0.011 Matthews correlation / ≤0.02 perplexity of plaintext, and reports the first MPC-based inference of LLaMA-7B (~200 seconds per output token).

## Strengths

- **First MPC inference of a 7B-parameter model (LLaMA-7B).** The paper demonstrates secure evaluation of LLaMA-7B with an 8-token input generating one output token in ~200 seconds (1.794 GB communication). This is a genuine scaling milestone — no prior MPC work has operated at this parameter count (lines 6, 224–231).

- **Accuracy parity with plaintext without retraining or architectural modification.** On three BERT-family models across three GLUE tasks, PUMA's Matthews correlation / accuracy differs from plaintext by at most 0.011; on GPT-2 models, perplexity differs by ≤0.02 (Table references at lines 177–179). This cleanly addresses a key limitation of prior work (e.g., MPCFormer's BatchNorm substitution caused a CoLA drop from 0.616 to −0.020, line 149 footnote).

- **Consistent and substantial speedup over the leading open-source baseline.** Across BERT models, PUMA is 1.375–1.916× faster than MPCFormer; across GPT-2 models, 2.250–2.414× faster (line 188). Communication reductions of up to 1.88× are also reported. These improvements hold across varying input lengths and output lengths (Section 5.3).

- **Clean end-to-end design with a share-invariant across all layers.** The paper maintains replicated secret shares throughout every layer (Section 4.1), enabling arbitrary-depth Transformers to be composed securely. The faithful implementation of Embedding and LayerNorm — layers that prior work modified or omitted — allows loading any HuggingFace pre-trained model without retraining (lines 35–40).

- **Practical engineering contributions disclosed.** The detection and resolution of serialization size limits (Protobuf/FlatBuffers 2 GB cap) via automatic chunking is a concrete, useful contribution for the community building on SecretFlow-SPU (lines 227–228).

## Weaknesses

### Fatal

None. The core technical content (approximation protocols for GeLU, Softmax, Embedding, LayerNorm) is referenced via `\input{}` directives that the parser stripped; the original submission would contain these sections. The remaining weaknesses do not invalidate the paper's central claims.

### Major

None. The weaknesses below are addressable and do not threaten the core contributions.

### Minor

- **Inconsistent and potentially misleading framing of the LLaMA-7B result.** The abstract and introduction claim "evaluate LLaMA-7B in around 5 minutes" (lines 6, 37), while Section 5.4 reports ~200 seconds (~3.3 minutes, line 231) for *one token*. These are inconsistent with each other. More importantly, the title "Secure Inference of LLaMA-7B in Five Minutes" creates the impression of full end-to-end inference; generating a meaningful response (e.g., 100 tokens) would scale to hours. While the paper is transparent that this is a per-token measurement, the headline framing overstates the practical capability.

- **The efficiency comparison to MPCFormer is informative but incomplete.** The paper compares PUMA's full system against MPCFormer *without* its Quad approximations (line 151), justified by the fact that Quad requires retraining and PUMA does not. However, this conflates two separable questions: (1) does PUMA's no-retraining requirement buy something? and (2) is PUMA's per-token cost lower even controlling for approximation quality? A side-by-side accuracy *and* cost comparison against MPCFormer-with-Quad (retrained) would cleanly separate these factors. The paper's single plaintext experiment showing that MPCFormer's BatchNorm replacement drops CoLA from 0.616 to −0.020 (line 149 footnote) is suggestive but does not directly measure MPCFormer's retrained accuracy.

- **No variance reporting.** Accuracy, perplexity, and runtime numbers are reported without standard deviations, confidence intervals, or number of runs. While single-run evaluation is common in MPC systems papers, the claim that PUMA "matches plaintext accuracy" would be strengthened by showing, over multiple trials, that the fixed-point and truncation noise does not meaningfully affect results.

### Trivial

- **Internal numerical inconsistency:** The abstract says "around 5 minutes" for LLaMA-7B; the experiment section reports "around 200 seconds" (3.33 minutes). These should be reconciled.
- **The "about 2× faster" claim** (abstract) is a slight rounding up of the observed range: BERT models achieve 1.375–1.916×, GPT-2 models achieve 2.250–2.414× (line 188). This is defensible as a summary but tilts toward the upper end.

## Nice-to-Haves

- An ablation study showing the impact on accuracy and runtime of replacing each approximation (GeLU-polynomial, Softmax-polynomial, secure Embedding, secure LayerNorm) with the exact protocol would help quantify the source of each gain.
- A per-layer cost breakdown for LLaMA-7B (attention v. FFN v. norm) would help the community identify bottlenecks for future optimization.
- Demonstrating generation of a short multi-token sequence (e.g., 3–5 tokens) under MPC would strengthen the claim of practical viability beyond single-token generation.

## Removed Points

These points are flagged to be removed, treat them with caution:

1. **"Missing core technical content — the protocols are in separate included files."** The `\input{Protocols/Gelu}`, `\input{Protocols/Softmax}`, etc. directives at lines 130–133 are LaTeX includes that the PDF parser stripped. In the original submission, these files are present. This is a parser artifact, not an author omission. *Reason: Hard Rule — parser-stripped sections exist in the original submission.*

2. **"The paper does not discuss why prior works could not scale to LLaMA-7B."** The paper identifies three specific limitations of prior work: high inference cost, need for retraining, and incompatible architectures (lines 18–28). These are the reasons prior work could not handle models at LLaMA-7B scale. *Reason: Factually incorrect — the paper does discuss this.*

3. **"The paper does not test whether specific drawbacks of prior work are resolved."** The experiments directly test accuracy parity (lines 177–179) and speedup over MPCFormer (line 188), which are the claimed resolutions of the identified drawbacks. *Reason: Factually incorrect.*

4. **"Should compare to PrivTransformer and Iron."** The paper explicitly states MPCFormer is "the only one that have been open-sourced" (line 54) and justifies focusing on it. *Reason: Scope creep — the paper is not obligated to benchmark against non-open-sourced baselines that it cannot run.*

5. **"Does not report communication round count."** Round count is not a standard reporting requirement for MPC inference papers of this type; runtime and communication volume are the standard metrics. *Reason: Nitpick — standard practice in the field.*

## Novel Insights

The most interesting observation that emerges from the reviews is the tension between PUMA's two headline claims: "no retraining" and "2× faster." The efficiency comparison against MPCFormer-without-Quad leaves open the question of whether the speedup is driven by better approximations or simply by choosing a slower baseline variant. A reviewer who is aware of the Quad approximations in MPCFormer would naturally ask: does PUMA beat MPCFormer-with-Quad on both speed *and* accuracy, or only on accuracy? The paper's design choice — to compare against the no-retraining variant of MPCFormer — is methodologically consistent with PUMA's own ethos, but it means the 2× claim rests partly on the fact that MPCFormer pays an additional cost (retraining) that PUMA avoids. This is a real advantage, but it is an advantage of the *system design*, not of the approximation technique per se. Disentangling these two contributions would sharpen the paper's technical narrative.

## Suggestions

1. Reconcile the "5 minutes" / "200 seconds" discrepancy and reframe the LLaMA-7B claim more precisely — e.g., "Secure inference of LLaMA-7B at ~200 seconds per output token."
2. Add a supplemental comparison: run MPCFormer with Quad+retraining on a comparable task (or cite existing accuracy numbers from the MPCFormer paper) and report the accuracy and cost, even if the comparison is imperfect.
3. Add standard deviation or min/max ranges for at least the runtime numbers over 3 runs; this is inexpensive and significantly improves rigor.
4. If the protocol files (`Protocols/Gelu`, `Protocols/Softmax`, etc.) were inadvertently omitted from the review text, ensure they are present in the camera-ready submission and accessible to reviewers.
5. Include a footnote clarifying that the "five minutes" title refers to per-token cost for LLaMA-7B and that autoregressive generation would scale linearly.

## Score and Decision

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>