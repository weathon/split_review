I have enough content to verify the major claims. Let me compose the final review.

## Summary
The paper proposes **codebook features**: a sparse, discrete vector-quantization bottleneck inserted after attention heads and/or MLP sublayers of transformers, trained via finetuning with a straight-through estimator. The authors argue that the resulting discrete codes (i) preserve language-modeling performance with mild degradation, (ii) mitigate superposition by assigning distinct codes to FSM states beyond the neuron count, and (iii) enable causal steering by activating topic-relevant codes at inference time. Experiments span a synthetic TokFSM task and TinyStories / WikiText-103 language models up to 410M parameters.

## Strengths
- **Well-controlled TokFSM testbed with clean causal evidence.** With known ground-truth states, the interchange-intervention result (Fig. 2 / JSD plots) shows that swapping a single MLP code shifts next-token distributions toward the target state, providing genuinely *causal* (not merely correlational) evidence inside the model (§3.2).
- **Disentanglement beyond neuron count is concretely demonstrated.** In layers of width 128, the codebooks recover identifiable codes for all 100 FSM states and 686 state-plus-digit combinations, with 97.1% average classification precision vs. 70.5% for the best matched-recall neuron (Fig. 2a). This is exactly the kind of evidence the superposition framing demands.
- **Non-trivial engineering result.** Training straight-through-quantized bottlenecks at every layer of a 24-layer 410M-parameter transformer without collapse is a useful empirical finding, and the inference-speed analysis using MIPS is a practical addition.
- **Clear two-phase protocol (hypothesize-then-intervene).** The methodology in §2.2 is explicit and reproducible at the conceptual level.

## Weaknesses

### Fatal
None.

### Major
- **"Modest degradation" understates the cost on the analyzed configurations.** The model the paper explicitly says it analyzes for TokFSM (Attn+MLP, k=1, C=10k; daggered in Table 1) has State Acc 63.65 vs. 96.77 baseline — a 33-point drop on the metric that measures whether the FSM was learned. Likewise, the daggered WikiText model (Attn k=8) is 2.74 / 46.68 vs. 2.41 / 50.52 base — roughly equivalent to a 160M finetuned model rather than the 410M base. The abstract/intro's "only modest degradation" framing is at odds with the headline numbers for the *very models the analysis is run on*. This matters because interpretability claims should hold on models that actually solve the task.
- **Steering evaluation is methodologically circular and lacks baselines.** Topic codes are *selected* by inspecting activating tokens and manually filtering those that "appear to activate frequently on other examples related to that topic" (§4.1), and success is then measured with "a simple word-based classifier" over the same lexical surface. There is no held-out code-selection split, no human or LM-judged fluency/coherence evaluation, no null baseline (e.g., random codes activated at matched rates), and no comparison to the inference-time steering baselines the paper itself cites (activation addition, prompting). The 65–100% topic-hit numbers therefore do not isolate the contribution of codebooks from selection effects + a lexical metric.
- **No empirical comparison to concurrent sparse-feature work (SAEs / dictionary learning).** The paper acknowledges Bricken et al. 2023, Cunningham et al. 2023, and Sharkey in related work, but never compares against them despite pursuing the same goal — sparse, more monosemantic features — at lower cost (no finetuning, no performance hit). The central practical question — "is paying a performance cost to bake discreteness into the network better than post-hoc sparse decomposition?" — is left unresolved.

### Minor
- **Codes-vs-best-neuron comparison is structurally asymmetric.** A discrete top-1 indicator over a 10k-entry codebook is, by design, more localized than a single coordinate of a 128-dim distributed representation. A stronger comparison would be against a linear probe or sparse-feature dictionary of comparable cardinality. The result still indicates codebooks are more localized than neurons, but does not by itself settle the "superposition" framing against other sparse-feature methods.
- **JSD-normalized-to-1.** Fig. 2 reports normalized Jensen–Shannon divergence with the "None" baseline normalized to 1, which obscures absolute residual divergence after intervention. Reporting raw JSD would let readers judge how complete the swap is.
- **TokFSM regime is small (N=100 states, 128-dim, 4 layers).** Generalizing "codebooks overcome superposition" from this controlled setting to language models requires more than the regex-probe experiment provided.
- **Selection bookkeeping for topic codes is missing.** The paper does not report how many candidate codes were inspected and discarded per topic, which is the true human-cost of the interpretability protocol.
- **λ=1 is asserted without a sensitivity analysis** in the main text; sensitivity to the reconstruction-loss coefficient would strengthen the method section.

### Trivial
- "Code 2543 in MLP layer 2 activates on the 0 in state 40" is anecdotal; per-code precision/recall for the state-plus-digit family would be more informative than the single example.
- Limitations omit the most consequential one: the method requires finetuning and accepts performance loss, foreclosing application to frozen pretrained models — the dominant setting for interpretability work.

## Nice-to-Haves
- Apply codebooks via adapter-style insertion that better preserves base behavior, or evaluate on a frozen pretrained model.
- Pareto plot of perplexity vs. k vs. C across a denser sweep, not just a few configurations.
- Compositionality test: do codes for distinct concepts compose predictably when co-activated?
- Distributional analysis of steered generations (perplexity under base model, human-rated coherence), not just topic-hit rate.

## Removed Points
These points are flagged to be removed, treat them with caution.
- *Strength Finder*: "Preservation of model performance under extreme discretization" framed as a top strength — partly retained, but the specific claim that the analyzed configurations (daggered rows) preserve performance conflicts with a verified major weakness; the weakness wins.
- *Strength Finder*: "Interpretable concepts emerge without explicit supervision" — partially true but rests on cherry-picked exemplars and a manual filter step, so it is not strong evidence on its own and is downgraded.
- *Harsh critic*: "No comparison to currently available systems" framing is fine; we keep the SAE comparison ask but not as an existence/reproducibility doubt.
- *Harsh critic*: Anecdotal "code 2543" criticism — kept as Trivial only; doesn't undermine the precision/recall numbers in Fig. 2a.

## Novel Insights
None beyond the paper's own contributions. The most genuinely new observation — that VQ-style bottlenecks can be inserted at every layer of a 24-layer LM without collapse, and that the resulting codes admit clean interchange interventions in a controlled FSM setting — is the paper's own.

## Suggestions
- Restate the performance cost honestly in the abstract: distinguish "comparable with enough k/C" from "the analyzed configuration takes a 33-point hit on State Acc / a 5-point LM accuracy hit."
- Run a head-to-head against a sparse autoencoder trained on the same base model's activations: regex-probe precision at matched recall, plus topic-steering effectiveness on the same topic list.
- Make the steering evaluation non-circular: select topic codes on a held-out activation split, and evaluate hit-rate with both a lexical classifier and an LM-judge for fluency; include a random-code null and an activation-addition baseline.
- Report absolute JSD alongside the normalized values; report per-code precision/recall distributions for the state-plus-digit family.
- Add a λ sensitivity table and a denser k×C sweep.

---

**Evaluation in plain language.** *Originality*: moderate — VQ bottlenecks are standard; per-layer placement plus the interpretability framing is the new piece. *Importance*: the research question (sparse, discrete, causally manipulable features) is central to mechanistic interpretability. *Claims vs. evidence*: the FSM causal evidence is solid; the "modest degradation" and "overcomes superposition vs. alternatives" claims are overstated relative to the headline numbers and missing baselines. *Soundness*: FSM interventions are sound; LM steering is methodologically circular. *Clarity*: generally clear and well-organized. *Value to community*: a useful methodological proposal and engineering datapoint, but its position relative to concurrent SAE work is undefined.

## Score and Decision
The paper presents real, novel empirical content (clean interchange interventions in a controlled setting, working VQ bottlenecks at scale), but two of its three headline claims — "only modest degradation" and steering effectiveness — are evidentially weaker than the abstract suggests, and the most natural comparison (SAEs) is absent. Borderline; leans slightly negative for a top venue but salvageable with the right revisions.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>