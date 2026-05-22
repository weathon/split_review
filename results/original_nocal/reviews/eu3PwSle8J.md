Now I have all the information I need. Let me produce the consolidated review.

## Summary

This paper identifies a limitation in prior instruction-hierarchy (IH) defenses against prompt injection: they inject privilege signals exclusively at the input layer, causing the signal to degrade as it propagates through deeper decoder layers. The authors propose Augmented Intermediate Representations (AIR), which adds small trainable embedding tables to every decoder layer (plus the final layer before the logits) to continuously reinforce privilege information throughout the network. Evaluations across three model families (3B, 7B, 8B), two training paradigms (SFT, DPO), and multiple attack types show consistent and often large improvements in robustness against gradient-based attacks (1.6×–9.2× reduction in ASR) with minimal utility degradation (<2%).

## Strengths

- **Empirical demonstration of the input-only IH limitation (Fig. 3)**: The paper directly measures cosine similarity between hidden representations of tokens with different privilege levels across layers. For ISE, similarity rises from 0.55 to ~0.92 across layers, while AIR stays lower (~0.85), validating the motivating hypothesis that input-only injection causes privilege signal degradation.

- **Consistent and large robustness gains across diverse settings (Table 1, Fig. 7)**: AIR reduces ASR against GCG and Astra attacks by 1.6×–9.2× compared to the best prior method across all three model sizes and both SFT and DPO training. For example, on Llama-3.2-3B SFT vs. GCG: Delim=38%, ISE=48.1%, AIR=4.1%; on Qwen-2.5-7B DPO vs. Astra: Delim=19.9%, ISE=2.3%, AIR=0.9%.

- **Utility preservation (Fig. 6)**: Win rates on AlpacaEval after adversarial training with AIR remain within 2% of the non-adversarially-trained baseline (None) across all models and training methods.

- **Minimal parameter overhead**: AIR adds only ~0.4M parameters for Llama-3.1-8B (0.005% increase), quantified directly in Section 4, making the method practical.

- **Thorough evaluation scope**: Three model families (Llama-3.2-3B, Qwen-2.5-7B, Llama-3.1-8B), two training paradigms (SFT, DPO), five attack types (Naive, Ignore, Completion, Escape Separation, GCG, Astra), and two evaluation benchmarks (AlpacaFarm, SEP).

## Weaknesses

### Fatal
None.

### Major

- **Parameter count confound between AIR and ISE (Table 1)**. AIR adds (L+1)×K×d = ~0.4M IH-related parameters for Llama-8B (one embedding table per layer), while ISE adds only K×d = ~12K parameters (one input-level table). The paper attributes AIR's improvement to "per-layer injection," but the comparison does not control for the 33× difference in IH-related parameter count. An ablation that gives ISE equivalent additional capacity at the input layer (e.g., larger/multiple input embedding tables or a small linear projection) would cleanly isolate the effect of per-layer injection from increased encoding capacity. As presented, the hypothesis that "limiting injection to the input layer constrains efficacy" is supported, but the attribution to *where* rather than *how many* parameters is not fully disentangled.

  *Why this matters*: The paper's central claim is architectural (per-layer vs. input-only), not about capacity. While the absolute number of added parameters is tiny relative to model size (0.005%), the relative difference between AIR and ISE is large enough to warrant a controlled ablation. However, note that adding more capacity at the input layer would not fix the signal degradation problem shown in Fig. 3 (the input signal decays during propagation regardless of input capacity), so this is unlikely to overturn the main result—but it should be addressed for rigor.

### Minor

- **Gradient-based attack ASR uses logit likelihood rather than actual generation (Section 5.4)**. For GCG and Astra, ASR is measured from the log-probability of the target phrase "hacked!", not from whether the model's greedy/sampled output actually contains the phrase. While the paper is transparent about this choice and the attacker's loss curves (Fig. 7) serve as complementary evidence not subject to this concern, the headline ASR numbers could differ from generation-based ASR. Reporting generation-based ASR for gradient attacks would strengthen the main claims.

- **Asymmetric optimization steps between SFT (50) and DPO (200) models (Section 5.4)**. The number of GCG/Astra optimization steps differs by 4× (50 vs. 200) with no justification. If the attacks are stronger with more steps, the comparison between SFT and DPO robustness might conflate attack strength with defense quality. This should be justified or controlled.

- **Astra results variance not discussed (Table 1)**. The improvement from AIR over ISE against Astra varies dramatically between SFT (up to 145×) and DPO (up to 2.5×). This large discrepancy in relative improvement is not discussed, leaving open questions about when per-layer injection is most impactful.

### Trivial

- **Table 1 column labeling is ambiguous**: The first column "None" (no adversarial training) and the "None" subcolumn under SFT (adversarial training without IH signal) have the same label but represent different conditions. This could confuse readers.

## Nice-to-Haves

- An ablation controlling for parameter count (as described in the Major weakness above).
- Generation-based ASR for gradient-based attacks.
- A discussion of why the relative improvement over ISE varies so much between SFT and DPO for the Astra attack.
- Analysis of whether the per-layer embeddings learn distinct privilege information across layers or merely amplify the input-level signal (e.g., cosine similarity between S_j tables).

## Removed Points

These points were raised in the reviewer inputs but are removed with justification:

1. **"Adversarial dataset not described in the main text"** (Harsh Critic Issue 3) — REMOVED. The paper explicitly states "Details of the training datasets used for the two rounds are provided in Appendix B.1." The appendix was stripped by the PDF parser; this content exists in the original submission.

2. **"Delim similarity = 1.0 does not indicate signal degradation"** — REMOVED. The paper uses Fig. 3 to compare all three methods. Delim having similarity 1.0 is expected behavior (delimiter tokens don't carry a continuous privilege signal in the representation), and the key comparison is ISE vs. AIR. The framing is accurate: ISE's similarity rises from 0.55→0.92 while AIR stays at 0.55→0.85, showing AIR better maintains separation.

3. **Speculative fatal interpretation of the parameter confound** — REMOVED from Fatal classification. The harsh critic labels the parameter confound as a "structural issue" that "invalidates the paper's primary conclusion." This overstates the case: the absolute parameter difference is 0.4M vs 12K in an 8B model, and adding more input-only capacity would not solve the signal degradation mechanism shown in Fig. 3. The concern is valid but as a Major weakness requiring an ablation, not a fatal flaw.

4. **Generic "missing related work"** — REMOVED per instructions (cannot confirm from external sources).

5. **Formatting/style nitpicks** — REMOVED per instructions.

## Novel Insights

None beyond the paper's own contributions. The reviewers did not surface any novel analysis or connection not already present in the paper itself.

## Suggestions

1. **Add a controlled ablation**: Give ISE additional capacity at the input layer (e.g., expand the embedding table or add a small MLP) to match AIR's ~0.4M IH-related parameters, and show that per-layer injection still yields better robustness.
2. **Report generation-based ASR for GCG/Astra**: Compute the fraction of cases where greedy decoding actually outputs "hacked!" and compare against the logit-based metric.
3. **Justify or equalize the optimization steps**: Explain the 50 vs. 200 step asymmetry or run both settings for both SFT and DPO.
4. **Discuss the Astra variance**: Explain why AIR's relative improvement over ISE differs so much between SFT and DPO for the Astra attack.

## Score and Decision

The paper makes a clear, well-motivated contribution: identifying a genuine limitation in existing IH defenses and proposing a simple, effective fix. The experimental evaluation is thorough across models, training methods, and attacks, and the results are consistently positive. The main weakness (parameter count confound between AIR and ISE) is real but addressable and does not threaten the core claim — the signal degradation mechanism visualized in Fig. 3 would not be fixed by adding more input-only capacity. The paper is a solid empirical contribution that will be useful to the community working on LLM security.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>