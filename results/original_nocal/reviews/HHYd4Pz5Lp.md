Now I have all the information needed to produce the consolidated review.

## Summary

This paper introduces DelRec, a method for learning per-neuron axonal/synaptic delays in the recurrent connections of spiking neural networks via surrogate gradient learning (SGL). The approach uses differentiable triangle-function interpolation that relaxes integer delays to continuous values during training, with σ annealed to zero so delays round to integers at inference. The authors achieve new state-of-the-art results on Spiking Speech Commands (82.58%) and Permuted Sequential MNIST (96.21%) using only simple LIF neurons, and match SOTA on SHD. A functional study compares recurrent versus feedforward delays under low-parameter constraints, showing that learned recurrent delays are particularly beneficial for temporal processing.

## Strengths

1. **New SOTA on two challenging temporal datasets using only LIF neurons.**  
   Table 1 shows DelRec (recurrent delays only) achieving 82.58±0.08% on SSC (surpassing the previous best of 81.54%) and 96.21% on PS-MNIST (surpassing 95.77%), with comparable or fewer parameters than the baselines. This is a clean empirical result.

2. **Principled and well-described differentiable delay interpolation.**  
   The triangle-function spread with σ annealing (Section 2.2, Eq. 9–11, Fig. 2C) is clearly motivated, avoids ad-hoc rounding heuristics, and provides well-defined gradients throughout training. The scheduling matrix and buffer mechanism (Eq. 8, 13, Algorithm 1) are concrete implementation details that make the method reproducible.

3. **Clean ablation isolating learning from architecture.**  
   The comparison of learned recurrent delays vs. fixed random recurrent delays (Fig. 3B, ~82% vs. ~78% on SHD at 10k params) cleanly shows that *learning* the delays matters beyond simply having them. This directly supports the claim that optimization of delays is beneficial.

4. **Parameter-efficient SOTA.**  
   On SSC, DelRec (recurrent-only) uses 0.37M parameters, fewer than DCLS (2.5M), SE-adLIF (1.6M), and RadLIF (3.9M), while achieving higher accuracy. This demonstrates the contribution comes from the method, not from added capacity.

## Weaknesses

### Fatal
None.

### Major

- **The "first SGL-based method" claim is imprecisely bounded relative to prior work described in the paper itself.**  
  The paper states "DelRec, the first SGL-based method to train axonal or synaptic delays in recurrent spiking layers" (Abstract, line 13; Section 1, line 94), yet also describes Xu et al. as using "backpropagation" (i.e., SGL) to learn "a single recurrent delay parameter per layer" with "a softmax function with a decreasing temperature" (lines 88–89). Since backpropagation with surrogate gradients is precisely what defines SGL, the claim is contradicted by the paper's own description of Xu et al. The paper should have been more precise: DelRec is the first method to learn *per-neuron* recurrent delays via *continuous differentiable optimization* (rather than discrete selection from a fixed set), or the first to *combine* feedforward and recurrent delay learning. The current framing risks overclaiming. **Why it matters:** The paper's central novelty assertion is ambiguously stated relative to work the authors themselves cite.

### Minor

- **The combined-delay result on SSC is unexplained.**  
  In Table 1, DelRec with both recurrent and feedforward delays (82.19±0.16%, 0.55M params) performs *worse* than DelRec with only recurrent delays (82.58±0.08%, 0.37M params). The paper discusses this phenomenon for small SHD models (line 273: "we found no advantage in using both types of delays in these small configurations") but does not address it on SSC, where the model is not small. Adding both delay types increases parameters by ~50% *and* reduces accuracy. Whether this is an optimization difficulty, overfitting, or a genuine interaction effect deserves at least a brief comment.

- **The comparison between recurrent and feedforward delays is architecturally confounded.**  
  Section 3.2 compares a recurrent network with learned recurrent delays against a *feedforward* network with learned feedforward delays (Fig. 3A–C). These differ in two ways simultaneously: presence/absence of recurrent connections and type of learned delay. The conclusion "recurrent delays outperform feedforward delays" conflates the effect of delay type with the effect of recurrent connectivity itself. This is partially mitigated by other controls in the study (random fixed recurrent delays vs. learned recurrent delays), but the headline comparison remains confounded. A cleaner design would compare a recurrent network with learned recurrent delays against the *same* recurrent network but with learned feedforward delays on the incoming weights (keeping architecture fixed).

- **The "critical" claim in the Conclusion (line 291) is stronger than the evidence warrants.**  
  The paper concludes that "recurrent delays are critical for temporal processing in SNNs." The ablation shows learned recurrent delays substantially improve performance over no-delay baselines, which is strong evidence that they are *beneficial* and *useful*. However, the word "critical" implies indispensability, and the paper does not demonstrate that no alternative mechanism (e.g., larger networks, adaptive neurons, longer time constants) could achieve comparable temporal processing without recurrent delays. A more measured claim ("highly beneficial" or "powerful") would better match the evidence.

### Trivial
None.

## Nice-to-Haves

- **Memory and compute profiling.** The buffer size depends on the maximum learned delay (Eq. 13), but the paper does not report how large delays actually grow during training or what the memory/runtime overhead is. For a method motivated by neuromorphic deployment, a brief profiling table (buffer size, FLOPs, wall-clock time for a typical SSC/SHD run) would strengthen the practical contribution.
- **Learned delay distributions.** Histograms of final learned delay values would reveal whether the available delay range is fully utilized or whether delays converge to a small subset of values. This would inform whether the "unbounded" design choice is actually exploited.
- **Additional temporal benchmarks.** Validation on Speech Commands v2 or DVS Gesture would strengthen generalization claims beyond the three datasets used.

## Removed Points

These were flagged by the harsh critic but are removed after verification against the paper:

- **"Combined-delay degradation invalidates the claimed advantage of recurrent delays"** — Removed. The SSC result is unexplained but not contradictory. The core claim is that recurrent delays are beneficial, which is supported by recurrent-only outperforming all no-delay baselines. Adding feedforward delays on top could introduce optimization challenges; the paper's overall evidence for recurrent delays remains intact. This is a minor unexplained observation, not a fatal contradiction.
- **"Novelty claim is unverifiable due to missing citation"** — Removed. The paper explicitly cites Xu et al. multiple times (lines 88, 190, 224, Tables 1–2) and describes their work. The full bibliographic entry may be in the appendix/references section truncated by the parser (line 312: "Rest of paper (reference and Appendix) is removed"). Per hard rules, missing reference text due to parser truncation is not an author error.
- **"Xu et al. is ignored when claiming only Mészáros et al. proposed a method for recurrent delays"** — Removed. The paper mentions Xu et al. on the same line as the Mészáros claim (line 88: "For instance, Xu et al. achieved state-of-the-art results..."). The Mészáros claim is about an algorithm "specifically designed to learn optimal delays in recurrent connections," which is arguably different from Xu et al.'s single-per-layer discrete selection. The paper does not ignore Xu et al.
- **"SiLIF inclusion violates exclusion criteria"** — Removed. The exclusion criteria (line 190) applies to models *left out* of the table. SiLIF is included *in* the table as a baseline. There is no inconsistency.
- **"ASRC-SNN footnote has no code URL / missing citation"** — Removed. The parser truncates the appendix and reference list. The code URL and full citation may be in the truncated portion.
- **"Figure 3C conclusion is misleading about energy efficiency"** — Removed. The paper explicitly acknowledges the trade-off (lines 273–285: "feedforward delays can provide a more energy-efficient alternative when computational efficiency is preferred over performance"). The critic's claim that the paper "downplays" this is factually incorrect.
- **"Unbounded delay buffer"** — Removed. Eq. 13 provides a finite bound: buffer size = ⌈1 + max d_j + (1+σ)⌉. The buffer is mathematically bounded, not unbounded.
- **"Vague and unreferenced claim about theoretical works"** — Removed. The paper cites Izhikevich (line 80) and provides specific theoretical motivation for recurrent delays (lines 77–81).
- **"New SOTA without qualifier"** — Removed. The claim is clearly qualified by dataset (SSC and PS-MNIST) and neuron type (LIF) in both the abstract and conclusion.

## Novel Insights

None beyond the paper's own contributions. The reviews surface no insight that the paper itself does not already articulates.

## Suggestions

1. **Sharpen the novelty claim.** Replace "first SGL-based method" with a more precise formulation such as "first method to learn *per-neuron* recurrent delays via *continuous differentiable optimization* (as opposed to discrete selection from a fixed set)" to distinguish from Xu et al. without contradiction.
2. **Discuss the SSC combined-delay result.** Even a brief sentence acknowledging the degradation and offering a hypothesis (optimization difficulty, interaction effects, statistical fluctuation) would remove a source of reader concern.
3. **Add an architecture-controlled comparison on SHD.** Compare (a) a recurrent network with learned recurrent delays, (b) the same recurrent network with learned feedforward delays on incoming weights (removing recurrent delays), to isolate the effect of delay *type* from architecture. Alternatively, explicitly acknowledge the confound and adjust the conclusion language accordingly.
4. **Tone down "critical"** to "highly beneficial" or "substantially improve temporal processing" to match the evidence level.

## Score and Decision

This paper presents a well-motivated method with clear algorithmic contributions and strong empirical results (new SOTA on two benchmarks). The weaknesses are addressable and do not undermine the core contributions. The major issue is a framing/positioning imprecision that can be fixed in revision. The experimental evidence is solid, the methodology is reproducible, and the ablations are informative.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>