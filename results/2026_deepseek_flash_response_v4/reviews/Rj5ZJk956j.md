## Summary

This paper introduces a weight-based method for classifying gated MLP neurons by read-write (RW) functionality, computing cosine similarities among w_gate, w_in, and w_out. Applying this to 12 LLMs reveals a cross-model universal pattern: early-middle layers are dominated by (conditional) strengthening neurons, while a numerically rare class of "weakening neurons" appears mostly in late layers. The paper further demonstrates through ablation experiments on OLMo-7B that these weakening neurons have a disproportionately large effect on attribute rate and output entropy, and that part of this effect is driven by a mechanism involving negative gate values in Swish—a regime previously assumed to be only relevant for training dynamics.

## Strengths

1. **Novel RW taxonomy for gated neurons (Table 1, Section 4.2):** The paper systematically classifies gated neurons into six prototypical RW functionalities based on three weight-vector cosine similarities. Prior work analyzed activation contexts (Voita et al., 2024) or output weights alone (Gurnee et al., 2024); this is the first joint analysis of all three weight vectors (w_gate, w_in, w_out) for gated neurons.

2. **Cross-model universality demonstrated across 12 LLMs (Figure 1(a), Section 5):** The paper shows that the strengthening-then-weakening pattern—median cos(w_in, w_out) positive in early layers and negative in late layers—holds across 12 LLMs spanning multiple families (Llama, Gemma, OLMo, Mistral, Qwen2.5, Yi) and sizes (0.5B–9B), providing strong evidence that the finding is not an artifact of a single architecture.

3. **Controlled ablation experiments with layer-matched baselines (Figure 3(a), Section 6.1):** Zero-ablating all 243 weakening neurons produces a clear, sustained drop in attribute rate from layer ~10 onward, while ablating the same number of random neurons from the same layers produces no effect. This isolates the effect of the RW class from the effect of layer position. Other RW classes are reported as indistinguishable from the clean run (appendix figures 14–16).

4. **Conditional ablation method revealing a negative-gate mechanism (Section 6.2):** The paper introduces conditional ablation—ablating only activations meeting specific sign conditions on x_gate and x_in—and shows that the entropy-sharpening effect of weakening neurons is largely attributable to the (x_gate < 0, x_in < 0) case. This challenges the common assumption that negative Swish values are functionally irrelevant for model mechanisms (not just training dynamics).

5. **Activation frequency analysis with strong correlation (Figure 4, Section 7):** The paper reports a near-linear negative correlation between cos(w_in, w_out) and activation frequency (r = −0.97, p < 0.01) in Layer 15 of OLMo-7B, with correlations at least −0.71 in most layers, extending Gurnee et al. (2024)'s finding from GELU to gated activation functions.

## Weaknesses

### Fatal
None.

### Major

- **Causal evidence for weakening neuron influence is limited to a single model (OLMo-7B).** Sections 6–8—which contain the causal claims that weakening neurons have "outsize influence," activate often, and that negative gate values drive important behavior—are all conducted on OLMo-7B alone (explicitly acknowledged on line 188: "to save resources, we focus on a single model"). The weight-cosine correlational patterns (Section 5) generalize convincingly across 12 models, but the paper's headline causal claims about influence and mechanisms each rest on experiments from one architecture. Since the paper presents the weakening neuron phenomenon as a general discovery about transformer models, the causal experiments need to be replicated on at least one additional model (e.g., a Llama or Gemma variant) to establish that the observed behavior is not OLMo-7B-specific. This is the single largest gap in the evidence.

### Minor

- **The evidence for the negative-gate mechanism, while suggestive, is based on limited data.** The conditional ablation analysis (Section 6.2) uses one model and one metric (entropy). The case study in Section 6.3 is a single text example ("Omicron"), and the paper honestly notes that no single neuron's output weight is similar to "mic," meaning the mechanism is distributed rather than attributable to a single neuron. The qualitative neuron analysis (Section 8) provides converging evidence but on a single additional neuron (31.9634). For the paper's most novel claim—that negative Swish values play an active functional role—the evidence would be strengthened by more examples, ideally across multiple models.

- **The taxonomy threshold (τ = ±0.5) is acknowledged as arbitrary but no sensitivity analysis is provided.** The paper states (line 129) that "many cosines will not be close to 0 or ±1" and offers three granularity options, including threshold-free scatter plots. However, quantitative claims such as "25% of all neurons are input manipulators" and the distributional percentages of RW classes depend on the threshold choice. A sensitivity analysis showing how the class distribution varies with τ ∈ {0.3, 0.4, 0.5, 0.6, 0.7} would demonstrate robustness.

- **The activation frequency correlation statistics are not explicitly tied to a specific model.** Section 7 states that correlations are "at least −0.71 in all layers except the last two" but does not specify whether this applies to OLMo-7B alone or to multiple models. Given that the paper emphasizes cross-model consistency in Section 5, this ambiguity makes it impossible to tell whether the activation frequency pattern also generalizes.

### Trivial

- **Inconsistency between abstract/intro (9 LLMs) and body (12 LLMs).** The abstract and introduction refer to "nine different LLMs" (lines 9, 19), while Section 5 lists 12 models (line 170). The body clarifies that Figure 1(a) shows the "nine larger models" (line 172), so the full corpus is 12, but the abstract is imprecise.

- **The preprocessing step (sign-flipping based on cos(w_gate, w_in)) is deferred to the appendix (Section C).** Since this preprocessing directly affects the sign of cos(w_in, w_out) and therefore which neurons are classified as strengthening vs. weakening, a brief justification in the main text would improve accessibility.

## Nice-to-Haves
- Replication of ablation experiments on additional models (e.g., Llama-3.2-3B, Gemma-2-2B) to confirm the generality of the causal claims.
- Statistical uncertainty measures (e.g., repeated runs or confidence intervals) for the ablation results, which would strengthen the quantitative claims.
- Connecting the neuron-level analysis to SAE latents, as the paper itself suggests as future work.

## Removed Points
- **"Entropy histogram descriptions are contradictory":** The parser-generated figure description says all six histograms are "centered around 0," which a reviewer interpreted as contradicting the paper's claim of a ~10 nat decrease. However, these are auto-generated figure descriptions from the PDF parser (not the paper's own text). The paper's own caption (line 209) clearly states the effect size. Without the actual figure, the contradiction cannot be verified and may be a parser artifact.
- **"Preprocessing should be in main text":** This is a presentation preference, not a scientific weakness. Demoted to a trivial note.
- **"No statistical uncertainty / error bars":** Single-run ablation experiments are standard in mechanistic interpretability; moved to nice-to-have.
- **"First to observe such a mechanism" conflicts with concurrent work:** The paper explicitly cites Kong et al. (2025) and bounds the claim ("concurrently with Kong et al. (2025) who focus on a different phenomenon"), which is appropriate scholarly practice.
- **Generic criticisms about missing related work, formatting, or reproducibility:** These are either factually incorrect, parser artifacts, or not substantive concerns for this type of paper.

## Novel Insights

The reviews surface one observation not foregrounded by the paper itself: the striking asymmetry between the strength of the correlational evidence (12 models, universal pattern) and the causal evidence (1 model, specific analyses). This gap is not a flaw per se—it is a natural consequence of resource constraints—but it defines the paper's evidential profile precisely. The weight-cosine discovery is robust and general; the specific mechanism claims (negative gate values, outsize influence) are plausibly general but only directly tested in one architecture. Making this asymmetry explicit in the paper's framing would help readers calibrate confidence appropriately.

## Suggestions
1. **Replicate the ablation and conditional-ablation experiments on at least one additional model** (e.g., Llama-3.2-3B or Gemma-2-2B) to confirm that the causal influence of weakening neurons and the negative-gate mechanism are not OLMo-7B-specific. This is the highest-impact improvement.
2. **Add a sensitivity analysis for the cosine threshold τ** (e.g., τ ∈ {0.3, 0.4, 0.5, 0.6, 0.7}) to demonstrate which distributional claims are robust to the arbitrary threshold choice.
3. **Explicitly state which model(s) the activation frequency statistics (Section 7) refer to.**
4. **Correct the "nine LLMs" / "12 LLMs" inconsistency** in the abstract and introduction.

## Score and Decision

**Calibration anchors (all rounds):**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/KdR88Qskmw.md` | 3.00 | 1 | Pooling contraction paper; substantially weaker, no mechanistic interpretability contribution |
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/9L9j5bQPIY.md` | 2.50 | 1 | Metanetwork paper; much weaker, different paradigm |
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/hbon6Jbp9Q.md` | 2.33 | 1 | Neurobiological semantics paper; much weaker, different domain |
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/bBUhlynfRX.md` | 3.00 | 1 | Brain-inspired regularizer; much weaker, different topic |
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/rfSfDSFrRL.md` | 5.50 | 1 | Gated RNNs discover attention; weaker—more theoretical but less comprehensive experiments |
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/CN2bmVVpOh.md` | 4.33 | 1 | Transformer frontostriatal gating; weaker, more speculative |
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/wnT8bfJCDx.md` | 6.25 | 1 | Gated-linear RNNs unified view; comparable, both propose analysis frameworks |
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/52UtL8uA35.md` | 6.75 | 1 | Deep networks learn features; stronger, more rigorous theory |
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/kbjJ9ZOakb.md` | 8.00 | 1 | Single-neuron invariance manifolds; stronger, more comprehensive |
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/aWXnKanInf.md` | 8.00 | 1 | TopoLM brain-like organization; stronger, more ambitious |
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/I4e82CIDxv.md` | 8.00 | 1 | Sparse Feature Circuits; substantially stronger—complete pipeline with circuit discovery and editing |
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/d8w0pmvXbZ.md` | 8.00 | 1 | Training instability proxies; stronger, more rigorous |
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/MbX0t1rUlp.md` | 6.20 | 2 | MLPs learn in-context; comparable in quality, different topic |
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/WQQyJbr5Lh.md` | 6.00 | 2 | Influential neuron paths in ViTs; comparable, but our paper has stronger cross-model evidence |
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/y3CdSwREZl.md` | 4.80 | 2 | MINER modality-specific neurons; weaker, less rigorous |
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/cif0JVXJ3b.md` | 5.25 | 2 | Knowledge neurons; weaker, more speculative |
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/XBHoaHlGQM.md` | 6.60 | 2 | DOCS weight similarity; stronger—more mathematically grounded and broader analysis, though our paper has more surprising causal findings |
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/vVxeFSR4fU.md` | 6.50 | 2 | Tracing representation progression; stronger on layer-wise analysis rigor |
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/2J18i8T0oI.md` | 6.50 | 2 | Towards Universality; comparable—both study cross-model patterns, but our paper has more surprising findings |
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/ih3BJmIZbC.md` | 6.80 | 2 | RSVC visual concept similarity; stronger, more rigorous evaluation |

**Round 1 bracket:** The paper clearly beats the sub-3.5 band and falls short of the 8.0 band. Initial bracket: 5.0–7.0.

**Round 2 narrowing:** Against the DOCS anchor (6.60, pure analysis paper), our paper is slightly weaker because the causal experiments are single-model. Against MLPs Learn In-Context (6.20) and Influential Neuron Path (6.00), our paper is comparable or slightly stronger. Against Towards Universality (6.50), our paper is comparable—both study cross-model patterns, but our paper's single-model limitation for causal claims prevents it from reaching the 6.5+ tier.

**Final calibrated score: 6.0**

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>