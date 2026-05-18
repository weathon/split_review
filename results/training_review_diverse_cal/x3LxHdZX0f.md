Now I have a thorough understanding of the paper. Let me construct the final consolidated review.

---

## Summary

This paper presents PUMA, a secure multi-party computation (MPC) framework for Transformer model inference. It proposes new polynomial approximations for GeLU and Softmax, together with faithful secure implementations of Embedding and LayerNorm, enabling end-to-end secure inference of pre-trained Transformer models *without* retraining or architecture modifications. Experiments on seven models (BERT-Base/Large, RoBERTa-Base, GPT2-Base/Medium/Large, LLaMA-7B) show that PUMA matches plaintext accuracy (≤0.011 MCC difference, ≤0.02 perplexity difference) while achieving ~1.4–2.4× speedup over MPCFormer (ICLR 2023). The paper also reports the first MPC-based evaluation of LLaMA-7B (~200 seconds per token).

## Strengths

- **Plaintext-matching accuracy without retraining.** Across BERT/RoBERTa models on GLUE tasks and GPT2 models on Wikitext-103, PUMA's secure inference accuracy deviates from plaintext by at most 0.011 Matthews correlation coefficient and 0.02 perplexity (Section 4.1). This directly addresses a key limitation of prior work (e.g., MPCFormer) that required fine-tuning to recover from approximation losses.

- **Significant and consistent speedup over the state-of-the-art.** PUMA achieves 1.375–1.916× faster runtime on BERT models and 2.250–2.414× faster on GPT2 models compared to MPCFormer (Tables 2–3, Section 4.2), with communication improvements of 1.079–1.884×. The efficiency gains increase with model size, supporting the claim that the specialized approximations are more effective at scale.

- **Faithful end-to-end framework compatible with pre-trained models.** PUMA designs secure Embedding and LayerNorm protocols that exactly replicate plaintext functionality, allowing direct loading of Hugging Face pre-trained models. This contrasts with MPCFormer, which replaces LayerNorm with BatchNorm (causing a catastrophic drop from 0.616 to –0.020 MCC on CoLA, Section 4) and cannot load pre-trained weights faithfully.

- **First MPC evaluation of LLaMA-7B.** The paper demonstrates secure inference of a 7B-parameter language model under MPC with 8-token input, producing one output token in ~200 seconds with 1.794 GB communication (Section 4.4). This represents a meaningful scaling milestone for the field.

- **Broad evaluation across model families and tasks.** Seven models (BERT, RoBERTa, GPT2, LLaMA-7B) across four benchmarks (CoLA, RTE, QNLI, Wikitext-103), with ablations on input length, output length, and batch size (Section 4.3), demonstrating that the approximations generalize across architectures.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **Minor inconsistency in headline runtime claim.** The title and abstract state "around 5 minutes" for LLaMA-7B token generation, but Section 4.4 reports ~200 seconds (~3.3 minutes) for one output token from an 8-token input. While both numbers are impressive, the ~50% overstatement in the title/abstract should be corrected for accuracy. The runtime also lacks a breakdown by layer (e.g., attention vs. FFN vs. embedding), which would help readers understand where the costs concentrate and where future optimization could focus.

- **Accuracy advantage over MPCFormer is argued indirectly.** The paper convincingly shows that MPCFormer's architecture modifications (BatchNorm replacing LayerNorm) cause catastrophic accuracy loss on pre-trained models, and that PUMA matches plaintext accuracy. However, the central claim that "MPCFormer does not achieve similar precision as PUMA" would be strengthened by a more direct comparison: e.g., approximating MPCFormer's Quad-based GeLU on a pre-trained model and measuring the accuracy drop before retraining. The current evidence (a plaintext BatchNorm-vs-LayerNorm ablation) supports the claim about architectural incompatibility but does not directly measure the impact of MPCFormer's GeLU/Softmax approximations. The argument is logically sound given that MPCFormer cannot load pre-trained models, but the claim is phrased as a precision comparison rather than an architectural-compatibility limitation.

- **Communication cost breakdown is not provided.** The paper reports total communication costs but does not break down which layers or operations dominate. Providing this would help other researchers understand where PUMA's efficiency gains come from and identify further optimization targets.

### Trivial

- The title phrase "in Five Minutes" is imprecise given the reported ~200 seconds (~3.3 minutes).
- The paper uses `\input{}` to include protocol and table files, which makes the extracted manuscript appear to have missing content. This is a formatting/packaging issue rather than a scientific one, but future versions should ensure that the core technical content (at minimum the approximation forms and coefficients) appears directly in the main paper or appendix.

## Nice-to-Haves

- A brief security argument sketch (e.g., why the composed protocols maintain the invariant that all intermediate values remain secret-shared) would be helpful for readers unfamiliar with the replicated secret-sharing setting.
- An analysis of how the one-hot embedding cost scales with vocabulary size and how it might be optimized would be useful.
- Reporting LLaMA-7B runtime with longer output sequences would further demonstrate scalability.

## Removed Points

These points were flagged by reviewers but are excluded from the main assessment for the reasons below:

1. **"The core technical content (approximations for GeLU and Softmax) is absent"** — The paper uses `\input{Protocols/Gelu}`, `\input{Protocols/Softmax}`, etc. to include protocol details from separate files. These files are part of the original submission; the PDF parser did not extract them. Per the review guidelines, parser-based omissions are not author errors and should not be counted as weaknesses. The protocol content exists in the original submission.

2. **"Missing batch input table"** — The batch input results are mentioned in the text and the table is included via `\input{Table/CostBatch}`, which the parser did not extract. Same parser artifact.

3. **"No security proof or verification is provided"** — The paper specifies the threat model (semi-honest, honest-majority, ≤1 corrupted party) and notes that all intermediate values remain secret-shared throughout (Section 3.1). This level of security argument is standard for systems papers in this area (MPCFormer, Iron, etc., use the same approach). A full formal security proof would be beyond scope for a systems/conference paper of this type.

4. **Weaknesses about missing appendix, proofs, or references** — All such concerns stem from parser-stripped content and are removed per guidelines.

5. **Criticism that MPCFormer's Quad approximations "could still achieve reasonable accuracy after retraining" and that this was not compared** — PUMA's core claim is about *faithful inference of pre-trained models without retraining*. MPCFormer's Quad approach requires retraining by design, making it an apples-to-oranges comparison on that axis. The paper provides a plaintext experiment showing that MPCFormer's architectural changes (BatchNorm) cause catastrophic accuracy loss (0.616→–0.020), supporting the claim that MPCFormer cannot match PUMA's accuracy on pre-trained models as-is.

## Novel Insights

None beyond the paper's own contributions. The two key technical insights — that GeLU and Softmax can be approximated with low-degree polynomials accurate enough to preserve model accuracy without retraining, and that one-hot embedding and LayerNorm can be faithfully implemented in MPC — are clearly stated and supported by the paper's experiments. The reviews did not surface any unexpected implications beyond what the paper already discusses.

## Suggestions

1. **Correct the title/abstract to match the reported LLaMA-7B runtime.** "In Five Minutes" should be adjusted to "in ~3.3 Minutes" or "in Minutes" to avoid overstatement.
2. **Provide a breakdown of LLaMA-7B runtime** by layer type (embedding, attention, FFN, LayerNorm) to help the community understand where optimization would be most impactful.
3. **Consider adding an explicit comparison** against MPCFormer's Quad GeLU approximation applied to a pre-trained model (without retraining) to directly demonstrate the accuracy degradation.
4. **Include the polynomial coefficients and error bounds** for the GeLU and Softmax approximations directly in the main paper body, not only in separately-included files, to improve accessibility.

## Score and Decision

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>