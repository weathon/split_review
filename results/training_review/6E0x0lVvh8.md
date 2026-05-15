Now I have a thorough understanding of the paper. Let me compose the final consolidated review.

## Summary

This paper presents an extensive benchmark of how language models internally represent mental states (beliefs of self and others) across model size, fine-tuning, prompt variations, and activation steering. Building on Zhu et al. (2024), the authors probe residual stream activations from two model families (Pythia 70M–12B, Llama-2 7B–70B, including instruction-tuned/RLHF variants) and report that (1) probing accuracy for protagonist beliefs improves with scale and, more dramatically, with fine-tuning (up to +29%); (2) prompt variations affect internal representations, with the "Initial Belief" variant helping and "Time Specification" unexpectedly not; and (3) Contrastive Activation Addition (CAA) improves downstream ToM performance without training any probe, and generalises across tasks.

---

## Strengths

- **Systematic multi-factor benchmarking of internal belief representations.** The paper probes residual stream activations across two model families spanning 70M–70B parameters and three fine-tuning conditions (base, chat/instruct, RLHF). Figure 2 shows clear scaling trends (e.g., +29% for Llama‑2‑7B‑chat over its base version), and the authors quantify scaling relationships (logarithmic for base models, R²=0.98; linear for fine-tuned, R=1.0 in Figure 5). This goes substantially beyond the single-model, single-size analysis in prior work.

- **First systematic study of prompt-variation effects on internal belief representations.** The paper defines four conceptually controlled prompt variants (Random, Misleading, Time Specification, Initial Belief) and measures their effect on probe accuracy. Figure 3 shows that even variations expected to help (Time Specification) unexpectedly degrade performance, while Initial Belief consistently helps. Prior work on prompt robustness focused on model outputs, not internal representations, making this a novel contribution.

- **Demonstration that CAA improves ToM reasoning without training probes and transfers across tasks.** Using steering vectors computed from Forward Belief, CAA yields consistent accuracy gains over both no intervention and ITI across three BigToM tasks (e.g., +56 points for Llama‑2‑13B‑chat on Backward Belief; 70B models reach ~91% on Both). This is the first application of CAA to ToM and shows cross-task transfer without retraining, which probe-based ITI in prior work did not demonstrate.

---

## Weaknesses

### Fatal
None.

### Major

- **Single-dataset design limits generalisability.** All experiments use BigToM, a single GPT-4-generated synthetic benchmark. The authors acknowledge this limitation (Section 5), but it means all conclusions about scaling, prompting, and CAA effectiveness are conditional on the quirks of BigToM's specific story templates and generation process. Without replication on other ToM benchmarks (e.g., ToMi, FANToM, OpenToM), it is unclear whether reported patterns reflect genuine properties of mental-state representations or artifacts of the specific dataset.

- **The scaling-law fits (R², R values) are based on very few data points and may overstate predictive power.** For Llama-2 base, the logarithmic fit uses only 3 model sizes (7B, 13B, 70B), yielding R²=0.98. For Llama-2 chat, the linear fit also uses 3 points, yielding R=1.0. With 3 data points, a near-perfect fit can occur by chance or because any curve passing through 3 points is trivially well-fitted. The Pythia fit (5 sizes, R²=0.96) is more meaningful. The paper should acknowledge the limited inferential power of these fits.

### Minor

- **No explicit train/test split is described for the probing experiments.** The paper defines probing datasets D^P (Section 3.4) and describes training probes, but never states whether reported accuracies are on held-out test data, via cross-validation, or on the training set. While it is standard practice in probing to use held-out evaluation (and the paper's formal definition on line 126 distinguishes training from evaluation), the omission of an explicit statement leaves a gap for readers concerned about overfitting. The PCA analysis (Section 4.3) partially addresses memorisation concerns but does not substitute for a clear description of the evaluation protocol.

- **The PCA-based memorisation check is suggestive but not a standard memorisation test.** Projecting activations onto top-k principal components and retraining probes shows that belief information is concentrated in a low-rank subspace (Figure 4). This is reasonable evidence against memorisation (a genuinely memorising probe would rely on high-dim specific patterns), but it is not the most direct test. Standard approaches such as comparing train vs. test accuracy curves, training on scrambled labels, or cross-validation would provide stronger evidence. The paper's claim that this "eliminates any possible memorisation issue" (line 47) is overstated.

- **Why does Time Specification not help?** The paper notes this unexpected finding (Section 4.2) but offers no analysis or hypothesis for why models fail to benefit from temporal disambiguation. Since this contradicts the authors' own stated expectation, some discussion (e.g., probing the wording's effectiveness, checking whether models lack time-sensitivity in their representations) would deepen the contribution.

- **No exploration of the relationship between probing accuracy and CAA improvement.** The paper studies both probing (internal representations) and CAA (downstream behaviour) but never examines whether models with better probe accuracy also benefit more from CAA. Bridging these two halves could provide a more unified understanding of the mechanisms involved.

### Trivial
None.

---

## Nice-to-Haves

- Evaluate on additional ToM benchmarks (e.g., ToMi, FANToM, OpenToM) to test whether the observed patterns generalise beyond BigToM.
- Probe attention heads as well (following Zhu et al.) and compare with residual stream probing to identify where belief representations localise.
- Test CAA steering vectors on non-ToM tasks (e.g., factual reasoning) to verify specificity.
- Include a figure showing CAA performance vs. steering coefficient α for at least one model to demonstrate sensitivity to the intervention strength.

---

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **Missing CAA results table (Harsh Critic point #1).** The critic claims the CAA table is absent and the third contribution is unverifiable. The paper includes `\input{sections/table}` (line 196) and `\Cref{tab:caa_results}` (line 293) — the table exists in the original submission but was not captured in the text extraction. Per the formatting-artifact rule, this criticism is removed.

2. **Original prompt not shown in main text (Harsh Critic point #4).** The paper states that examples are reported in `\Cref{app:prompts}` (line 216). The appendix is stripped by the parser. Per the missing-appendix rule, this criticism is removed.

3. **Strength Finder's claim that PCA "rules out probe overfitting."** This phrasing overstates the evidence. The PCA analysis is a reasonable check but does not definitively rule out memorisation. Rephrased as a minor weakness above.

4. **Strength Finder's claim of "predictive understanding" from scaling laws.** With only 2–5 data points per fit, the predictive power is limited. This is now reflected as a major weakness.

---

## Novel Insights

The most interesting finding to emerge from the reviews is the asymmetry between the paper's probing and CAA results: probing reveals that models' internal representations of protagonist beliefs are surprisingly fragile under prompt variations (even beneficial-sounding ones like Time Specification hurt), yet CAA steering — which operates on the same residual stream — can lift downstream task performance substantially (+56 points on the hardest task). If the internal representations are so prompt-sensitive, why does adding a steering vector (essentially a different kind of prompt-level intervention) work so well? This tension between the brittleness of probed representations and the robustness of steering-based improvements is not addressed in the paper and suggests a more complex relationship between linear separability of belief features and their functional utilisability for generation than the current framing assumes.

---

## Suggestions

1. **Explicitly state the train/test split protocol for probing** (or confirm it is standard held-out evaluation). This single sentence would resolve the most persistent reviewer concern.
2. **Acknowledge the limited inferential power of scaling-law fits with few data points**, and consider reframing them as descriptive trends rather than predictive laws.
3. **Add a short discussion of why the Time Specification prompt variant might have failed** — even a speculative paragraph would turn an unexplained negative result into a useful insight.
4. **Make the CAA results table and the original prompt example visible** (they are present in the original submission, so this is just a presentation matter).
5. **Include a standard memorisation check** (e.g., train/test accuracy comparison) alongside the PCA analysis to strengthen the defense against overfitting concerns.

---

## Score and Decision

The paper makes solid, multi-faceted empirical contributions: it extends prior work across more models, fine-tuning regimes, prompt designs, and a new activation-steering method. The core findings — that fine-tuning dramatically improves belief representations, that these representations are prompt-sensitive, and that CAA can improve ToM performance without probe training — are well-supported by the evidence presented (figures, trends, and verbal descriptions of the CAA results). The weaknesses are about scope limitations (single dataset), overclaimed precision (scaling-law fits), and omitted procedural details (train/test split) — none of which invalidate the core claims. This is a useful benchmarking paper that the community will reference.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>