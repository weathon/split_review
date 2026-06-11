Now I have a clear picture from the calibration. Let me synthesize everything and write the final review.

**Calibration summary:**

Round 1 bracketing placed this paper between ~4.0–6.5. Round 2 narrowed with anchors at:
- **D2O (5.80, Accept)**: Dynamic KV cache allocation, limited novelty but solid empirical results
- **HeadKV (6.50, Accept)**: Head-level KV compression, novel granularity, good results, some practical concerns
- **ChunkKV (5.25, Reject)**: Chunk-based KV compression, incremental, missing latency numbers
- **Identify Critical KV Cache (5.75, Reject)**: Output perturbation perspective, real theoretical work, incremental contribution

QubitCache is more novel than ChunkKV and has more comprehensive evaluation, but its overclaiming (missing proof, overstated relational preservation, quantum compression advantage) is more significant than the issues in comparable papers. It sits below HeadKV (6.50) and D2O (5.80), and is comparable to or slightly below Identify Critical KV Cache (5.75). I'll score it at **5.0**.

---

## Summary

QubitCache proposes a KV-cache compression method that uses quantum-inspired amplitude encoding to preserve a distribution over evicted tokens' attention importance. The method partitions tokens into anchor, recent, critical (collectively ~15%), and non-critical (~85%) sets. Non-critical tokens are replaced by a 9-qubit quantum state encoding per-token aggregate attention weights as amplitudes; during inference, measurement probabilities from this state weight interpolated value vectors in a hybrid hard/soft attention mechanism (Eq. 7). The paper claims 7× memory reduction while retaining 92–97% of baseline performance across five models and multiple benchmarks.

## Strengths

- **Comprehensive empirical evaluation across diverse settings**: Table 1 reports results across five model families (Mistral-7B, Qwen2-7B, Phi-4-mini, DeepSeek-Coder-7B, Llama-8B) and seven benchmarks spanning both short-context (PG19, PIQA) and long-context (HotpotQA, TriviaQA, GovReport, Contract, SummScreen) tasks. QubitCache outperforms all baselines (ScissorHand, H2O, StreamingLLM, GEAR) on a large majority of model×task combinations, providing robust evidence for its effectiveness.

- **Evidence that attention-based token selection is decisive**: Table 4's ablation shows that removing critical tokens (selected by accumulated attention scores) causes a 20.4% performance drop (0.491 → 0.391), whereas removing position-based heuristics (anchor/recent tokens) degrades performance by only ~0.6% each. Random selection at comparable retention yields substantially worse performance (0.335), directly validating the importance of attention-guided selection. This is the paper's strongest empirical argument.

- **Well-specified hybrid attention mechanism (Eq. 7)**: The formulation `Attention(Q_t) = λ Σ_{i∈I_p} α_i V_i + (1-λ) Σ_{j∈I_c} p_j(ψ) Ṽ_j` cleanly separates hard attention over preserved tokens from soft attention over probabilistically reconstructed ones, with the balancing coefficient `λ = √(|I_p|/N)` providing a principled interpolation. This moves beyond the binary keep/drop paradigm of prior methods (H2O, ScissorHands, StreamingLLM).

- **Scalability evidence to large models**: Table 2 extends evaluation to 30B and 70B parameter models (Qwen-30B, Llama-70B), showing QubitCache retains 96.9% and 89.0% of baseline F1 respectively on NarrativeQA.

- **Practical segment-wise encoding design**: Segmenting the sequence into 512-token blocks and encoding per-segment attention distributions into 9-qubit states avoids the exponential gate cost of preparing arbitrary 2^n-amplitude states, grounding the method in NISQ-era feasibility constraints.

## Weaknesses

### Fatal

None.

### Major

- **Overclaimed framing: "relational structure preservation" vs. per-token importance encoding**: The paper's central thesis — stated in the abstract, introduction, and throughout — is that the method preserves "relational structure" and "attention patterns between tokens." However, Equations (3)–(5) compute a single scalar per token (aggregate attention received, averaged across all layers and heads), and encode the normalized distribution of these scalars into quantum amplitudes. This preserves which tokens were important as attention targets (a marginal distribution), not the pairwise relational structure of the attention matrix. The method genuinely departs from binary keep/drop decisions by using soft, probabilistically weighted reconstruction, but the framing as "relational preservation" significantly overstates what the mechanism actually does.

- **Claimed theoretical guarantee is absent from the paper body**: The abstract states "We prove QubitCache preserves rank r attention structure with bounded reconstruction error" and the introduction repeats this claim. No theorem statement, formal error bound, or proof sketch appears in the paper body. Even if a full proof exists in an appendix, the paper body contains no theorem statement that would allow a reader to assess what is being claimed.

- **Quantum compression advantage is overstated**: The paper claims "logarithmic compression beyond classical information-theoretic limits." On classical simulation (which is how the method is implemented and evaluated, line 100), a 9-qubit state vector is a 512-element complex array — storing the same order of information as storing 512 scalar attention weights directly. The 7× compression ratio in Table 3 (0.55 GB vs. 0.59 GB for GEAR) comes almost entirely from retaining only 15% of tokens classically, not from the quantum encoding. GEAR achieves 6.7× compression through quantization alone; QubitCache's margin over GEAR is marginal (~7%). The claim of a quantum-driven compression breakthrough is not supported by the classical-simulation implementation used.

### Minor

- **Ablation study (Table 4) does not specify the task or dataset**: A single "F1 Score" column is shown with no indication of which benchmark was used, making the ablation results unverifiable and incomparable to Table 1.

- **PG19 metric labeling is confusing**: PG19 is described as "for language modeling" (Section 4.1.2) but Table 1 reports PG19 results as "F1" with scores around 0.12–0.19. Language modeling is conventionally evaluated with perplexity; what F1 measures on PG19 here is unclear.

- **Figure 3 uses different F1 ranges without explanation**: Plot (a) (qubit count) has F1 in 0.50–0.56 while Plot (b) (circuit depth) has F1 in 0.70–0.85. These appear to be from different experimental setups, but the figure does not specify what task each plot corresponds to.

- **Ablation retention ratio discrepancy**: The ablation text states that the random baseline "preserves the same 49.8% of tokens" while the main paper uses 15% retention. Comparing QubitCache at one retention ratio against random selection at a different ratio makes the quantitative comparison ambiguous, even though the qualitative conclusion (attention-based selection matters) remains supported.

- **No latency or throughput measurements**: The paper reports only memory consumption. For an inference optimization method, the computational overhead of quantum circuit simulation per segment is a first-order concern. The paper mentions "minimal latency overhead" (line 216) but provides no timing data.

### Trivial

- Figure 3(b) caption claims "achieving 103% of baseline performance" — unclear what baseline this refers to (presumably some compressed baseline rather than the uncompressed model).
- Section 4.1.2 describes LAMBADA as a benchmark but it does not appear in Table 1, while HotpotQA, TriviaQA, GovReport, Contract, and SummScreen appear in the table without individual description in the setup.

## Nice-to-Haves

- A comparison against the simplest attention-based baseline — retain 15% of tokens by accumulated attention score and use inverse-distance-weighted value interpolation for the rest, without any quantum encoding — would isolate the contribution of the quantum component. The "No Quantum" ablation (0.472 vs. 0.491 in Table 4) already provides some evidence here, but a standalone baseline would strengthen the case.
- Clarify how a single quantum state per segment serves all layers and heads given that the KV cache is per-layer and per-head, while the encoding collapses across layers and heads (Eq. 4).

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Harsh Critic claim that "Figure 3 is internally inconsistent"**: The two plots show different experiments (varying qubits vs. varying depth) and can legitimately have different F1 ranges. The lack of task specification is a presentation issue, not an internal inconsistency. Moved to Minor.
- **Harsh Critic claim that PG19 F1 reporting is "nonsensical"**: While unusual, F1 could be computed on a derived task from PG19. The real issue is unclear labeling, not impossibility. Moved to Minor.
- **Harsh Critic claim about "the 15% vs 50% retention claim is misleading" as a separate credibility problem**: This is a presentation clarity issue, not a fatal experimental flaw. Moved to Minor.
- **Strength Finder claim about "quantum encoding provides a 3.9% performance improvement" being a strong independent contribution**: Table 4 shows this, but the "Random + Quantum" vs. "Random No Quantum" comparison shows essentially no gain (0.335 vs. 0.334), suggesting the quantum component only helps when combined with attention-based selection. The gain is real but modest.
- **Harsh Critic claim that the method "could be stated and evaluated without any quantum language"**: While true, the quantum formalism provides a specific encoding scheme. This is more a matter of presentation preference than a weakness.

## Novel Insights

The key tension in this paper is between its ambitious conceptual framing and the more modest mechanism it actually implements. The idea of using soft, probabilistic reconstruction weights for evicted tokens (rather than binary keep/drop) is a genuine conceptual advance over prior work — it allows evicted tokens to retain some influence on generation through their attention-derived importance weights. However, the paper's claim that it preserves "relational structure" collapses under scrutiny: what's preserved is a marginal distribution of per-token importance (who was attended to), not pairwise attention relationships (who attended to whom). The quantum encoding formalism is largely orthogonal to the core idea — any distribution over tokens could be stored and sampled classically with comparable cost. The hybrid attention mechanism (Eq. 7) is the paper's most concrete and valuable contribution, and could be evaluated independently of the quantum framing.

## Suggestions

- Either provide the claimed theorem statement and proof of bounded reconstruction error, or retract the claim from the abstract and introduction.
- Add latency/throughput measurements to make the case for practical deployment.
- Specify what task/dataset Table 4's ablation was run on.
- Add an ablation that isolates the quantum component: compare "attention-based token selection + value interpolation" with and without the quantum encoding, at matched retention ratios.
- Temper the relational-structure-preservation language to accurately reflect what's encoded (per-token importance distributions).
- Clarify the PG19 evaluation — if it's language modeling, report perplexity; if it's a derived task, specify what task and why F1 is the appropriate metric.

## Anchor Comparison

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| IntelLLM | 3.00 | R1 | Weaker — narrower evaluation, less novelty |
| MixAttention | 2.00 | R1 | Weaker — simpler approach, less evaluation |
| PrefixQuant | 3.00 | R1 | Weaker — different sub-area (quantization) |
| LSH-E | 3.83 | R1 | Weaker — less comprehensive evaluation |
| Running Huge Context Windows | 4.67 | R1 | Slightly weaker — simpler top-k approach |
| ChunkKV | 5.25 | R1 | Comparable — similar evaluation breadth, different weaknesses |
| Identify Critical KV Cache | 5.75 | R1/R2 | Slightly stronger — has actual theoretical derivations |
| D2O | 5.80 | R2 | Slightly stronger — more thorough ablation, throughput data |
| Locret | 5.80 | R2 | Slightly stronger — trained approach with retaining heads |
| HeadKV | 6.50 | R2 | Stronger — tighter contribution, fewer overclaiming issues |
| SharedContextBench | 6.50 | R2 | Stronger — benchmark contribution with clear methodology |
| FlexPrefill | 8.00 | R1 | Much stronger — clear methodology, strong results |
| Scaling Laws for Precision | 8.00 | R1 | Much stronger — foundational contribution |

Round 1 bracket: 4.0–6.5. Round 2 narrowed to 5.0–5.5. The paper has genuine strengths (comprehensive evaluation, well-specified hybrid attention mechanism, evidence for attention-based selection) but is held back by significant overclaiming: the missing proof claim in the abstract, the overstated "relational structure preservation" framing, and the overstated quantum compression advantage. Among KV-cache compression papers, it is more novel and better-evaluated than the 3–4 range papers, but falls short of the 5.75–6.50 range due to the overclaiming issues. Final score: **5.0**.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>