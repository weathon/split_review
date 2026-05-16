I have thoroughly read and verified the paper against all reviewer claims. Let me now produce the final consolidated review.

---

## Summary

iReVa proposes a method for traceable model editing by inserting explicit key-value adaptors into the MLP layers of Transformer models, where each edit is stored as an identifiable knowledge neuron. The method includes initialization of key-value pairs from cached hidden states, retrofitting with a multi-objective loss, and a max-pooling inference mechanism. Experiments on GPT2-XL (and several larger models) using zsRE-10K and PARAREL-10K benchmarks show iReVa achieving strong edit success and generalization with good specificity, plus a unique knowledge-withdrawal capability.

## Strengths

- **Novel traceable editing mechanism with explicit per-edit storage.** Unlike prior methods (ROME, MEMIT, MEND) that distribute edits across model weights in an untraceable manner, iReVa inserts one key-value neuron per edit, making it possible to identify, inspect, and selectively withdraw individual edits. This is demonstrated by the withdrawal test (Section 6.2, Table 2) where RS=100% and Con=98.8% on zsRE-10K.

- **Comprehensive ablation study validating each design component.** Table 3 systematically removes the activation function, max-pooling, reconstruction loss, and irrelevance loss, quantifying each component's contribution. Removing the activation function drops NS from 83.9 to 69.5; removing max-pooling drops ES from 99.6 to 88.5. These results confirm the method's design choices are individually meaningful.

- **Efficiency analysis with both theoretical and empirical backing.** Section 6.3 provides complexity analysis (O(l·d₁²·n) time) and shows 10K edits without fine-tuning takes 1.6 hours (vs. ROME's 9.16h, MEMIT's 5.4h) on a single A800 GPU, with only 0.08B additional parameters for 10K edits on a 1.5B model. This is competitive or faster than leading alternatives.

- **Robust generalization across layers, model sizes, and edit quantities.** The method is tested on GPT2-XL, GPT2-LARGE, GPT-Neo-2.7B, and GPT-J-6B (Table 4, Figure 2, Figure 3), showing consistent outperformance over baselines. Figure 3 shows iReVa maintains stable ES/PS/NS as edit count grows, while ROME's NS degrades sharply.

## Weaknesses

### Fatal

None.

### Major

- **Uncontrolled baseline comparison undermines claimed SOTA margins.** The paper acknowledges preprocessing edit data "differently from previous studies" (line 178) by decomposing multi-token targets into multiple data pairs. It states baselines were "re-implemented using the same configuration reported in existing studies" — but does *not* confirm that baselines were evaluated on the *same preprocessed data* under the *same evaluation conditions*. If baselines were run on standard (undecomposed) data while iReVa benefited from a different task formulation, the reported ~9%/6% improvements over SOTA (Table 1) cannot be reliably attributed to the method's design rather than to data differences. This is the paper's most significant weakness, as the central claim of SOTA performance rests on this comparison.

### Minor

- **No variance or multi-run statistics.** No standard deviations or results across random seeds are reported for any experiment. Given that some baselines (e.g., MEND) are known to be seed-sensitive, and iReVa's own results may vary with initialization, single-run reporting limits confidence in the numbers.

- **No hyperparameter sensitivity analysis.** Key hyperparameters — the margin θ (0.75 for zsRE, 0.65 for PARAREL) and scaling factor α (0.2) — are set without any analysis of how varying these values affects ES/PS/NS. Since the activation function and max-pooling mechanism's behavior depends critically on θ, its sensitivity should be characterized.

- **"Interpretability" claim conflated with traceability.** The paper claims "better interpretability" (abstract) but the evidence is limited to identifying which neuron encodes which edit (traceability). There is no analysis of whether the learned key vectors encode semantically meaningful patterns (e.g., whether similar edit inputs cluster in key space). The interpretability claim would be stronger with such analysis; in its absence, the framing overstates what is demonstrated.

- **Knowledge withdrawal novelty is slightly overstated.** The paper's withdrawal test is a meaningful validation of non-interference (Con=98.8% is informative), but RS=100% is expected by construction since each edit occupies its own neuron, and removing it necessarily changes the prediction. The framing as a "first attempt" and "breakthrough" could be tempered. Additionally, the paper does not test sequential edit/withdraw cycles or verify that withdrawal of one edit leaves other edits intact.

- **Limitations acknowledged but not quantified.** The paper notes (Section 7) that iReVa "performs poorly when the target prompt is a long sentence" and that ES/PS don't improve with model scale, but provides no quantitative characterization of when the method degrades or by how much.

### Trivial

- **Layer generalization analysis (Figure 2) could provide deeper insight.** The paper notes iReVa prefers higher layers but offers only a brief speculation ("LMs' final prediction primarily depends on the information retrieved from higher layers") without probing cached hidden states or analyzing why this pattern holds.

## Nice-to-Haves

- A controlled re-evaluation where all baselines are confirmed to use the same preprocessed data, base model checkpoint, and evaluation splits would resolve the most serious concern and is the single highest-priority improvement.
- An interpretability analysis showing nearest-neighbor structure among key vectors (e.g., do keys for similar edit inputs cluster?) would substantiate the interpretability claim.
- Testing on larger edit scales (e.g., 50K–100K) would strengthen claims about scalability beyond 10K.

## Removed Points

These points are flagged to be removed; treat them with caution:

1. **"Interaction between activation function and max-pooling is ambiguous during inference"** — The paper clearly specifies this in Section 4.3: the max-pooling selects the best-matching neuron (j = argmax_t(K̂_t^T i)), then the activation function with margin (GeLU(x−θ)) is applied to that neuron's score. This interaction is well-defined.

2. **"'w/o activation function' ablation unclear"** — The paper defines it: "w/o activation function denotes that we remove the activation function proposed in Equation 6." Equation 6 is g_act(x) = GeLU(x−θ). The description is sufficiently clear.

3. **"Other methods could also perform withdrawal"** — The paper explicitly states that other methods' edited parameters are untraceable (ROME/MEMIT distribute edits across weights; MELO trains batch-level adaptors). This claim is reasonable for the compared baselines.

4. **"10K edits is not large enough"** — 10K is the standard scale in model editing research (matching ROME, MEMIT, MELO evaluations). Demanding 50K–100K is scope creep.

5. **"Missing comparison to Memory Layers / Neural Turing Machines"** — The paper's baselines are the standard SOTA methods in model editing literature. Adding every possible memory-augmented architecture is not required.

6. **"Missing related work"** — The hard rules prohibit me from confirming this; the related work coverage is adequate for the paper's focused contribution.

7. **"The paper should discuss NS trade-off more"** — The paper presents all three metrics and uses average Score as summary. MEMIT's higher NS is evident from the table. The trade-off is implicitly acknowledged.

## Novel Insights

The reviews collectively surface a tension inherent in the paper: the method's defining strength (traceable per-edit storage) is also the source of its most debated weaknesses. The withdrawal test is simultaneously the strongest evidence of the method's novelty and the most criticized claim as "trivial by construction." The key insight that emerges is that *traceable storage* and *state-of-the-art performance* are orthogonal contributions — the paper could more cleanly separate them. If the method were presented primarily as "the first traceable editing approach enabling targeted withdrawal," with the SOTA comparison as secondary (and caveated) evidence, the contribution would be less vulnerable to the baseline-comparison concern. The ablation study further reveals that the activation margin is the critical component for specificity, not the multi-objective loss — which suggests the paper's design is more about careful initialization + gating than about the fine-tuning objectives, contrary to the emphasis in Section 4.2.

## Suggestions

1. **Controlled baseline re-evaluation**: Rerun all baselines on the exact same preprocessed data splits, same base model checkpoint, and report whether the numbers change. This single fix would resolve the most serious credibility threat.

2. **Multi-run reporting**: Report means and standard deviations over at least 3 random seeds for all experiments.

3. **Θ sensitivity analysis**: Vary θ from 0.5 to 1.0 in steps of 0.05 and report ES/PS/NS to characterize the method's robustness.

4. **Re-frame the contribution**: Separate the traceability/withdrawal capability (the unique contribution) from the SOTA claim (which requires controlled comparison). The paper is stronger if positioned as "a traceable editing method that achieves competitive performance" rather than "a method that outperforms SOTA by 9%."

5. **Quantify limitations**: Add a small experiment or analysis showing at what target length iReVa's performance degrades, to substantiate the acknowledged limitation.

## Score and Decision

This paper introduces a genuinely novel approach to model editing with traceable per-edit storage, and the core idea has clear merit. The ablation study and efficiency analysis are well-done. However, the central claim of SOTA performance rests on an uncontrolled baseline comparison where preprocessing differs and it is unclear whether baselines were run on equivalent data. Combined with missing variance reporting and sensitivity analysis, the experimental validation does not yet support acceptance at a top venue in its current form. The paper would benefit substantially from focused revisions.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>