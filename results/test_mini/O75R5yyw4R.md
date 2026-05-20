Now I have sufficient calibration data. Let me write the final consolidated review.

## Summary

This paper proposes IterRef, a test-time scaling method for discrete diffusion models that applies Multiple-Try Metropolis (MTM) based iterative refinement to intermediate states during denoising. The key idea is to use noising-denoising transitions within an MCMC framework to progressively steer intermediate states toward the reward-aligned distribution. The paper provides a convergence guarantee (Proposition 1) via a carefully designed balancing function that simplifies the MTM acceptance rate, and demonstrates results across text (MDLM, LLaDA-8B) and image (MaskGIT) domains on tasks including toxicity reduction, sentiment control, and CLIPScore optimization.

## Strengths

1. **Theoretical convergence guarantee with a clever balancing function**: Proposition 1 proves convergence to the optimal reward-aligned distribution under the assumption of a reversible Markov kernel. The choice of balancing function λ in Equation 2 is the key technical insight — it reduces the MTM acceptance rate to the simple form β = min(1, exp((r(x_t') − r(x_t))/α)), eliminating the need for backward proposals while (as claimed) preserving detailed balance. This is a non-trivial adaptation of MTM to the discrete diffusion setting.

2. **Strong empirical results at low compute budgets**: Figure 2(a) shows that on MDLM, IterRef with 2T NFEs outperforms all baselines (FK, SVDD, SoP, BoN) at 32T NFEs on Sentiment, CoLA, and Perplexity. On Toxicity, IterRef at 4T NFEs matches FK at 32T NFEs. These results support the paper's central claim of effective test-time scaling.

3. **Cross-modal and cross-backbone generalization**: Table 1 shows IterRef on MaskGIT achieving CLIPScore 33.7 at 2 NFEs vs. 32.1 for FK, with consistent advantages across all compute budgets. Qualitative results in Figure 3 corroborate. This demonstrates the method is not language-specific.

4. **Useful ablations providing insight into discrete diffusion dynamics**: Table 2 identifies that later denoising stages (0.1T) are most effective for IterRef, contrasting with continuous diffusion where early steps dominate — a novel empirical finding. Table 3 and Figure 4 demonstrate that increasing iterations k is more effective than increasing particles N, validating the iterative-refinement design choice.

## Weaknesses

### Fatal
None.

### Major

1. **Opaque NFE accounting weakens empirical comparisons (key concern)**: The paper acknowledges that "aggregating these into a single NFE value may obscure meaningful differences" and that "it is preferable to report generative-model calls and reward-model calls separately" (line 178), yet the main results (Figures 2, Table 1) use only blended NFE. No itemized breakdown of generative vs. reward-model calls per method is provided in the main paper. The claimed appendix (C.4) with wall-clock analysis is stripped, so this cannot be verified. For methods with fundamentally different cost structures (IterRef's per-refinement-step cost vs. BoN's full-trajectory sampling cost vs. FK's particle propagation), the reader cannot determine whether IterRef's advantage comes from the refinement mechanism itself or from more favorable compute accounting. This concern affects every quantitative claim in the paper.

2. **Convergence guarantee relies on an unexamined strong assumption**: Proposition 1 requires that "q and p_θ form a reversible Markov kernel." For a learned denoiser p_θ that only approximates the true reverse process, this condition is almost never exactly satisfied. The paper provides no empirical diagnostics (e.g., acceptance rates over refinement iterations, convergence checks on the chain's stationary distribution, or analysis of how violations affect the target distribution). The theory is presented as clean but lives in an idealized regime whose practical validity is not assessed.

### Minor

1. **Detoxification evaluation lacks fluency/quality metrics**: The safety case study (Section 4.5, Figure 5) measures only toxicity reduction. A method that reduces toxicity by producing incoherent or off-topic text would trivially succeed on this metric. Perplexity, semantic similarity, or human evaluation of the detoxified outputs is needed to show that the method preserves quality while reducing toxicity.

2. **No statistical uncertainty reported**: All results are point estimates. With 15 prompts × 20 samples = 300 generations per experiment, variance is expected. Error bars or confidence intervals would strengthen the evidence considerably.

3. **Pool reuse heuristic upon rejection not covered by theory**: The paper states that when a proposal is rejected, the previously generated pool is reused (Section 3.3, line 172). This practical optimization breaks the i.i.d. proposal assumption of the MTM framework, and the paper does not analyze how this affects the convergence guarantee. The theoretical analysis only covers the idealized algorithm.

4. **Large CLIPScore jump at 2 NFEs (Table 1) warrants explanation**: IterRef goes from 30.5 (base model, 1 NFE) to 33.7 at 2 NFEs, while baselines reach 30.7–32.1. This is a remarkable jump for a single NFE of additional compute. The paper attributes this to efficiency of its compute allocation, but a more detailed analysis (e.g., how much of the gain comes from the first refinement step vs. from the specific timestep selection) would build confidence that the comparison is not driven by asymmetric NFE counting.

5. **No analysis of reward over-optimization**: For a method that explicitly maximizes a learned reward at inference time, there is no secondary quality metric (e.g., perplexity for text, FID for images) tracked alongside the primary reward to detect reward hacking.

### Trivial

1. **Ethics statement contains an inaccurate claim**: The statement says the work "intentionally includes experiments that increase the toxicity of generated text" (line 375), but the paper's experiments uniformly aim to *reduce* toxicity (detoxification) or steer toward positive sentiment. No toxicity-increasing experiment is described in the paper.

2. **Algorithm 2 pseudocode formatting is ambiguous**: The denoising step (Line 10) appears inside the `if` block in the pseudocode structure, though the text clarifies it happens after the refinement loop. A clearer structural separation would help readability.

## Nice-to-Haves
- Report generative-model calls and reward-model calls separately, as the paper itself suggests.
- Include a controlled ablation comparing IterRef against a version of FK or SVDD that also selectively applies guidance only at a subset of timesteps, to isolate the benefit of the refinement mechanism from the compute-allocation advantage.
- Analyze empirical acceptance rates over refinement iterations to build confidence that the practical algorithm behaves like an MCMC method.
- Include ImageReward scores (promised in Appendix C.1) in the main paper.
- A small human evaluation study for the detoxification case study.

## Removed Points
These points were flagged by the reviewers but are removed with justification:

- **"Practical algorithm decoupled from theoretical guarantee"** (Harsh Critic Weakness #2): The paper explicitly designs the balancing function λ (Eq. 2) such that the acceptance rate can be evaluated without backward proposals *while still preserving theoretical guarantees*. The claim is stated in line 168. The critic asserts without evidence that this cannot be true. This is the paper's core theoretical contribution, and without verification of the proof (in the stripped appendix) to the contrary, this criticism is unsupported.
- **"2T vs 2 NFE axis confusion"**: The paper consistently uses "2T NFEs" in text. The critic's claim about figure axis tick values {2,4,8,16,32} cannot be verified from the text and contradicts the paper's consistent notation.
- **"Asymmetric cost structure"** : The critic argues that IterRef's design efficiencies (pool reuse, selective timesteps, free noising) create an unfair comparison. These are genuine algorithmic efficiencies, not accounting tricks. The paper explicitly counts NFEs to include all operations for all methods. An asymmetry that favors the proposed method is expected and valid.
- **"Missing related works"**: Removed per instructions.
- **"Missing appendix content"**: Removed per instructions (appendix stripped by parser).
- **"Formatting/style nitpicks"**: Removed per instructions.
- **Generic/sweeping concerns** about evaluation rigor, evidence strength, and scope — the critic raised these as area-of-concern probes without concrete anchors. They are removed under the filtering discipline.

## Novel Insights

A genuinely novel observation emerges from cross-referencing the harsh critic and strength finder: the paper's central tension is that its strongest practical claim (dramatic compute efficiency) and its strongest theoretical claim (MTM convergence) operate on two different versions of the algorithm. The convergence proof applies to an idealized procedure with full backward proposals and fresh i.i.d. proposals at every iteration, while the efficiency advantage comes from the practical shortcuts (no backward proposals, pool reuse on rejection). The paper does not bridge this gap, and the community would benefit from understanding whether the shortcuts preserve convergence (the paper asserts yes for the balancing function, but no for pool reuse) and whether the efficiency would survive a fully rigorous implementation. The ablations on k vs. N (Table 3) and on timestep selection (Table 2) are the paper's most solid empirical contributions because they are internal comparisons not subject to the cross-method NFE accounting concern.

## Suggestions
1. Provide a transparent, itemized table showing exactly how many generative model calls and reward model calls each method uses at each compute level. Include wall-clock time measurements for all methods.
2. Add empirical acceptance rate analysis over refinement iterations to bridge the theory-practice gap.
3. Include statistical uncertainty (error bars/confidence intervals) for all main results.
4. Add a secondary quality metric (perplexity for text, FID or ImageReward for images) alongside the primary reward to monitor for over-optimization.
5. Add fluency/quality metrics to the detoxification evaluation.

## Score and Decision

**Calibration anchors:**

| Paper | Path | Avg Score | Round | Comparison |
|---|---|---|---|---|
| Deterministic Discrete Denoising | CHtLFyDbZp | 2.50 | R1 | Weaker; no reward guidance, no iterative refinement |
| Sketch First, Scale Fast | pr68D2Bo42 | 3.00 | R1 | Weaker; different problem (image generation only) |
| Discrete Guidance Matching | N1RYhOg6ib | 4.50 | R1 | Comparably narrow experiments, stronger theory claims but weaker empirical support |
| PG-DLM (Particle Gibbs) | je6FN2TuWf | 4.67 | R2 | Most directly comparable; similar task and backbones but IterRef has cross-modal results and more novel mechanism; IterRef is stronger |
| Improving CFG in Masked Diffusion | mMK9pvQJxf | 5.00 | R1 | Different problem (CFG, not reward-guided generation). Comparable quality of analysis |
| **IterRef** | **O75R5yyw4R** | **5.5** | — | **Current paper** |
| SMC for Discrete Diffusion | 7wbrFQvfdH | 6.00 | R2 | Similar scope; SMC paper has cleaner evaluation but IterRef's MTM mechanism is more novel |
| DriftLite | l01eG3Qikl | 6.00 | R2 | Continuous diffusion; stronger theory but different setting |
| Classical Search for Diffusion | b7Ftp6U78i | 6.00 | R2 | Continuous diffusion primarily; similar inference-time scaling theme |
| Duality Ψ-Samplers | RSIoYWIzaP | 7.00 | R2 | Different focus (sampler design, not reward guidance) |

**Round 1 bracket**: 3.5–7.5 (the paper is clearly stronger than the weak anchors in [2.5, 3.5] and clearly weaker than the strong anchors at 8.0+)

**Round 2 narrowing**: Compared against PG-DLM (4.67, Reject), SMC for Discrete Diffusion (6.0, Accept), and Classical Search (6.0, Accept), the paper sits between them. It is stronger than PG-DLM (more novel mechanism, cross-modal evidence, no unfair comparison issues) but weaker than the SMC paper on evaluation transparency. The NFE accounting concern is the primary factor preventing a higher score.

**Final score**: 5.5. The paper makes a genuine contribution to the discrete diffusion test-time scaling literature with a novel MTM-based refinement mechanism and strong initial evidence. However, the opacity of the NFE accounting weakens the empirical claims, and the theory-practice gap around the reversibility assumption and practical heuristics requires more analysis. The weaknesses are addressable in revision.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>