Now let me do calibration search to score this paper.Round-1 bracket: **5.5–7.5**. The paper is above basic (3-4 range) due to clear novelty, cross-model validation, and functional ablations. It's below the exemplary (8+) papers because functional experiments are limited to one model and the frequency confound is unaddressed. Let me narrow.Now I have enough information to write the final review. Let me synthesize everything.

---

## Summary
This paper introduces a weight-based cosine-similarity method for classifying gated MLP neurons in transformer LLMs into "read-write" (RW) functional classes — notably *weakening* neurons whose output weights point anti-parallel to their input-reading direction. Applying this method to 12 LLMs, the authors document a consistent structural pattern: conditional strengthening neurons dominate early-to-middle layers while weakening neurons concentrate in late layers. Ablation experiments on OLMo-7B show that the small class of ~243 weakening neurons has an outsized functional impact on both attribute rate and next-token entropy, with a novel finding that this impact is partly driven by activations where the gate value is *negative* — previously assumed to be functionally inert.

---

## Strengths

- **Novel weight-based taxonomy of read-write functionality for gated neurons (Section 4.2, Table 1).** The cosine-similarity classification scheme (strengthening, weakening, conditional variants, etc.) is a principled and transparent method that captures the relationship between what a neuron reads and what it writes. Validated against random baselines via significance tests (Section 4.3, Figure 2), it provides a clean operationalization of a question that prior work (Gurnee et al., 2024) computed but never interpreted.

- **Striking cross-model structural universality across 12 LLMs (Figure 1a, 1b, Section 5).** The strengthening-to-weakening layer-wise trend — with median cos(w_in, w_out) positive in early-middle layers and turning negative in late layers — is consistent across nine models ranging from 0.5B to 9B parameters and two architectures (SwiGLU and GEGLU). This is a strong, data-driven finding that is robust to scale and family.

- **Ablation experiments demonstrate outsize functional influence of weakening neurons (Figure 3a, Section 6.1).** Zero-ablating only 243 weakening neurons in OLMo-7B causes a large drop in attribute rate (from layer ≈10 onward), while ablating the same number of random neurons from the same layers has no effect. The entropy sharpening finding is similarly specific to this class (Figure 3b).

- **Novel conditional ablation method and discovery of negative-gate-value mechanism (Section 6.2).** By conditioning ablations on the signs of x_gate and x_in, the authors isolate that case (iii) — gate < 0, x_in < 0, leading to x_post > 0 — accounts for a substantial portion of weakening neurons' entropy effects. This is the first demonstration that the small-negative portion of the Swish/SwiGLU activation function encodes genuine functional mechanisms, not merely training dynamics artifacts. The paper appropriately notes concurrent work (Kong et al., 2025) on a related but distinct phenomenon.

- **Use of publicly available training data (Dolma) for OLMo-7B experiments (Section 6).** This allows the ablation results to be reproduced against exactly the same data distribution used during training, a practical strength over work relying on closed data.

---

## Weaknesses

### Fatal
None.

### Major

- **Activation-frequency confound in ablation comparison (Sections 6.1, 7).** Section 7 reports that weakening neurons activate very frequently — correlation r ≈ −0.97 between cos(w_in, w_out) and activation frequency at layer 15 (Figure 4). The ablation baselines in Section 6 use random neurons sampled from the same *layers*, but there is no indication that these baseline neurons are matched on activation frequency. Since weakening neurons fire far more often than typical neurons in those layers, the outsize ablation effect could be partly or substantially explained by differential activation rates rather than by the RW class per se. The paper notes (Section 7) that "activation frequencies do not fully explain their effect, since we found that even their negative gate values are influential," but this does not address the comparison with the random baseline. A frequency-matched ablation experiment is the natural remedy. As currently presented, this is the weakest link in the paper's central evidential chain.

- **Functional significance is demonstrated only for OLMo-7B; universal framing in abstract and conclusion is not fully supported (Abstract, Section 9).** The abstract states that weakening neurons "have a large influence on model behavior" universally, and the conclusion says "we have discovered that they have an outsize impact on model behavior" without model qualification. However, ablation experiments are run exclusively on OLMo-7B. The structural universality (Figure 1a, 1b) is well-supported across 12 models, but this is a different claim from functional universality. Even a lightweight replication — e.g., running the attribute-rate ablation on Llama-3.2-3B, which is already analyzed structurally — would substantially strengthen the functional claims.

### Minor

- **The early-layer effect in the attribute-rate ablation is unexplained (Figure 3a, Section 6.1).** The paper notes that "the effect is most visible in layers ≈10 and onward, even though weakening neurons are few and mostly in late layers," but offers no mechanism. How does ablating ~243 mostly-late-layer neurons affect residual-stream predictions at layer 10? This is an interesting empirical puzzle that is flagged and dropped; at minimum, an acknowledgment of possible causes (e.g., early-appearing weakening neurons are disproportionately powerful, or late-layer ablation alters residual-stream trajectories that are measured via logit lens) would strengthen the paper.

- **The weight-preprocessing step (Section 3.2) receives no main-text intuition.** The step — multiplying w_in and w_out by sign(cos(w_gate, w_in)) — determines which neurons end up classified as weakening vs. strengthening. Deferring all justification to Appendix C leaves readers unable to evaluate the core classification without consulting supplementary material. A one-sentence functional motivation in the main text would suffice.

### Trivial

- **Section 6.3 case study is selected at the maximum-effect extreme without stating this context upfront.** The paper says "we study a particular text example, namely where the entropy reduction by case (iii) activations of weakening neurons was most extreme." This is transparent but should be more explicitly framed as an extreme-case illustration rather than a representative example, to avoid misleading readers about typical behavior.

---

## Nice-to-Haves

- A frequency-matched baseline experiment would transform the activation-frequency point from a major weakness into a confirmed strength, and would sharpen the claim that RW class per se is mechanistically important.
- A quantitative decomposition of the negative-gate contribution — e.g., "case (iii) activations represent X% of all weakening-neuron activations but account for Y% of total entropy reduction" — would make the finding much more precise than the current qualitative framing ("similar to those of weakening neurons as a whole").
- Extending the functional ablation to even one additional model (e.g., Llama-3.2-3B) would make the universality framing scientifically defensible.
- Systematic descriptive statistics over all top-activating examples for the weakening neuron case study (Section 8) would strengthen the conclusion that weakening neurons are inherently harder to interpret.

---

## Removed Points

*These points are flagged as removed — treat with caution.*

- **Harsh critic's concern about the negative-gate histograms being "centered around 0" invalidating the finding.** The figure parser's automated description says all six histograms in Figure 3(b) are "centered around 0." However, the paper's own caption explicitly states: "in ≈10^6 next-token predictions, weakening neurons decrease the entropy by about 10 nats, whereas they increase it much more rarely." This text is more authoritative than a parser artifact. The qualitative finding (case iii dominates) is internally consistent in the paper and is corroborated by the case study in Section 6.3. **Removed as a parser artifact.**

- **Harsh critic's concern about the preprocessing step changing neuron classification "arbitrarily."** The paper explains the preprocessing preserves model behavior and gives the functional rationale for the sign normalization (Appendix C). That justification exists; removing it to the appendix is a presentation choice, not a methodological flaw. **Downgraded to Minor.**

- **Strength Finder claim that OLMo-7B's use of Dolma "sets the study apart from work relying on closed or unreleased data."** This is a contextually true but generic benefit of using an open-weights model; it does not constitute a genuine technical strength that distinguishes the methodology. **Removed as generic.**

---

## Novel Insights

The most genuinely novel observation in this paper — one that goes beyond repackaging known facts — is the discovery that **negative gate values in SwiGLU/GEGLU neurons have real functional significance**, rather than being a training-dynamics artifact reducible to ReLU. The conditional ablation method (Section 6.2) reveals that case (iii) activations (gate < 0, x_in < 0, x_post > 0) account for a disproportionate share of weakening neurons' entropy effects. This effectively shows that the Swish function's below-zero "leak" is not vestigial — it encodes a distinct computational case in which a weakening neuron acts as a *conditional strengthener* that activates on the *absence* of the concept in the gate direction, rather than its presence. This has direct implications for interpretability methodology: SwiGLU neurons cannot be analyzed with a ReLU-approximation assumption.

---

## Suggestions

1. Run the ablation experiment with a baseline that matches weakening neurons' activation frequency (e.g., sample baseline neurons stratified by activation frequency). This single experiment would either confirm or substantially qualify the headline claim about outsize influence.
2. Add one sentence of main-text motivation for the w_in/w_out sign preprocessing (Section 3.2) before pointing to Appendix C.
3. Report the quantitative contribution of case-iii activations to total entropy change (as a fraction of the full-weakening ablation effect).
4. Frame the case study in Section 6.3 explicitly as the maximum-effect example, and note how it compares to the median or typical effect magnitude.
5. Replicate the attribute-rate ablation on at least one additional model (structurally representative candidates are already identified in Section 5) to support functional universality claims.

---

## Score and Decision

**Calibration anchors:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| 9L9j5bQPIY.md (Metanetwork interp) | 2.50 | R1 | Much weaker — no compelling finding, no cross-model evidence |
| fSbPwHjdDG.md (Llamas think in English) | 3.00 | R1 | Weaker — a single causal intervention claim, smaller scope |
| 89wVrywsIy.md (Sparse Circuits) | 3.40 | R1 | Weaker — circuit tracing without structural universality |
| CN2bmVVpOh.md (Frontostriatal gating) | 4.33 | R1 | Weaker — speculative cross-domain analogy without strong functional validation |
| aN4Jf6Cx69.md (Mechanistic basis ICL) | 4.50 | R1 | Weaker — single model, smaller contribution |
| A0HKeKl4Nl.md (Mechanistic fine-tuning) | 6.67 | R1 | Comparable — similar depth of experimental work across multiple conditions |
| rIx1YXVWZb.md (Understanding Addition) | 5.50 | R1 | Weaker — single toy task, single model |
| EytBpUGB1Z.md (Retrieval Heads) | 8.00 | R1 | Stronger — functional universality demonstrated across many models, very clean methodology |
| STUGfUz8ob.md (Transformer relational reasoning) | 7.60 | R1 | Stronger — theoretical + empirical, broader impact |
| 2J18i8T0oI.md (Universality cross-architecture) | 6.50 | R2 | Comparable — cross-model structural universality, weaker on functional depth |
| rLX7Vyyzus.md (Systematic Outliers) | 6.00 | R2 | Similar in style — discovers specific functional class with outsized influence, experiments mostly on one model class |
| f6r1mYwM1g.md (Capability Localization) | 5.75 | R2 | Slightly weaker — narrower finding, less robust methodology |
| GdbQyFOUlJ.md (NeurFlow) | 6.50 | R2 | Comparable — neuron group analysis framework, but more incremental |
| yR47RmND1m.md (Safety Neurons) | 6.20 | R2 | Similar — identifies small set of functional neurons via ablation, one model class |

**Round 1 bracket:** 5.5–7.5

**Round 2 narrowing:** The most relevant anchors at 6.0–6.5 are "Systematic Outliers" (6.0) and "Towards Universality" (6.5). The paper under review:
- Has *more* novel structural findings than "Systematic Outliers" (12 models vs. primarily GPT-2), and a cleaner taxonomic contribution
- Has *weaker* functional validation than "Systematic Outliers" (no architectural fix proposed, frequency confound unaddressed)
- Has broadly comparable scope to "Towards Universality" but stronger functional evidence (ablations with clear baselines vs. SAE feature similarity metrics)
- Falls short of the 6.67 fine-tuning paper, which has multiple experimental settings with strong controls

**Axis summary:**
- *Originality*: High — novel taxonomy, new neuron class, first negative-gate mechanism finding
- *Importance of research question*: High — MLP neurons in modern gated LLMs are understudied from an interpretability perspective
- *Claims well supported*: Partially — structural claims are very well supported; functional/universal claims are supported for OLMo-7B but extrapolated to all models without cross-model replication
- *Soundness of experiments*: Good but with one genuine methodological gap (frequency confound in ablation baseline)
- *Clarity of writing*: High — well-structured, clear framing, accessible taxonomy
- *Value to research community*: High — the method, negative-gate finding, and layer-wise pattern are immediately useful

The paper is positioned at **6.0** — clearly above the 5.75 and 5.50 anchors due to stronger novelty and cross-model evidence, comparable to or slightly above the 6.0 "Systematic Outliers" paper in novelty, but held back from 6.5 by the single-model functional validation and the unaddressed frequency confound in the ablation comparison.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>