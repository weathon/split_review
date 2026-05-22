Now I'll write the final consolidated review.

## Summary

This paper introduces DelRec, a surrogate-gradient-based method for learning axonal or synaptic delays in recurrent connections of spiking neural networks. The method employs a differentiable triangle interpolation over real-valued delay parameters with progressive σ annealing during training, then rounds to integer delays at inference. Experiments on SSC, PS-MNIST, and SHD show that DelRec with simple LIF neurons achieves new state-of-the-art on SSC (82.58%) and PS-MNIST (96.21%), and a functional study demonstrates that learned recurrent delays provide a stronger accuracy/parameter trade-off than learned feedforward delays in low-parameter regimes.

## Strengths

- **First SGL-based method for continuous-valued recurrent delay learning.** The paper correctly identifies that prior work either does not learn recurrent delays (DCLS, cAdLIF) or uses non-SGL approaches (EventProp). Xu et al.'s softmax-based discrete delay selection is the closest prior art, but DelRec's continuous real-valued delays with differentiable interpolation is a genuine methodological advance. Code is provided.

- **New SOTA on two benchmarks with simple LIF neurons.** Table 1 shows DelRec (only recurrent delays) achieves 82.58% on SSC and 96.21% on PS-MNIST, surpassing prior models that rely on more complex neurons (adaptive LIF, multi-compartment, attention). This directly supports the claim that recurrent delays are a critical mechanism for temporal processing that can substitute for neuron-model complexity.

- **Thoroughly designed functional study (Section 3.2, Figure 3).** The ablation comparing vanilla SNN, vanilla RSNN, feedforward delays, fixed random recurrent delays, learned recurrent delays, and combined delays across a range of parameter counts provides strong, granular evidence for the benefit of learning recurrent delays. The finding that recurrent delays outperform feedforward delays under low-parameter constraints (Figure 3C) is the paper's most convincing experimental result.

- **Sound technical approach with clear motivation.** The triangle interpolation with σ annealing (Section 2.2) is well-specified and connected to both biological motivation (myelin plasticity) and theoretical benefits (Izhikevich's dynamical systems work, gradient mitigation via temporal skip connections shown in Figure 1B).

## Weaknesses

### Major

None.

### Minor

1. **The combined (recurrent + feedforward) delay model underperforms the recurrent-only model on SSC, and this is not discussed.** In Table 1, DelRec (Rec. and Ff. delays) achieves 82.19±0.16% with 0.55M parameters, while DelRec (only Rec. delays) achieves 82.58±0.08% with 0.37M parameters — a statistically meaningful difference. The conclusion mentions "better combining DelRec with feedforward delays" as future work, but the paper does not analyze why adding feedforward delays *hurts* performance on SSC specifically. A brief discussion (overfitting, optimization conflict, redundancy, or hyperparameter sensitivity) would turn this puzzle into a useful insight for readers.

2. **PS-MNIST results are reported from a single seed.** The paper's justification ("only test one seed as all the previous state-of-the-art models on the dataset") does not make this practice correct. The claimed SOTA improvement over Xu et al. (96.21% vs. 95.77%) is less than 0.5 percentage points. Without variance estimates, the reader cannot assess whether this gap is meaningful. This is especially important since the paper criticizes Chen et al. (2024) for using one seed — the same criticism applies here.

3. **The σ annealing schedule is not specified in the main text.** The paper states "we decrease σ throughout training down to 0" but does not describe the schedule (per epoch? per iteration? linear? exponential?). Equation (10) uses σ_epoch, suggesting an epoch-level schedule, but the actual reduction rule is absent from the main text. Since σ controls both gradient behavior and the interpolation precision that defines the learned delays, this is a meaningful reproducibility gap (though code is available).

4. **"Fixed random delays" baseline is underspecified.** The functional study uses a "RSNN with fixed random delays in recurrent connections" but does not describe how these delays were sampled (distribution, range, procedure). This baseline is important for interpreting the benefit of *learning* delays — without knowing the random configuration, a reader cannot reproduce or assess whether the comparison is fair.

### Trivial

- The claim "first SGL-based method" (Abstract, line 13) should be qualified to note that Xu et al. also use backpropagation (i.e., SGL) with a softmax over discrete delays. The paper's actual contribution — continuous delays with differentiable interpolation — is genuine and does not need an overly broad "first" claim to stand. The paper already states the more precise distinction on line 94: "first method to train...using surrogate gradient learning **and backpropagation**" — but even this is technically true of Xu et al. Recommend: "first continuous SGL-based method for per-neuron delays in recurrent connections."

## Nice-to-Haves

- A brief analysis of why the combined delay model underperforms on SSC (e.g., showing learned delay distributions, or a control where feedforward delays are frozen after pretraining).
- Multi-seed results for PS-MNIST (even 3 seeds with mean and std would substantially strengthen the claim).
- Training time comparison with vanilla RSNN to help assess the overhead of the scheduling buffer.

## Removed Points

The following points from the reviewer inputs were removed for the indicated reasons:

- *Harsh Critic's point about "Eq. (13) approximation justification"*: The paper does justify that non-negative delays make the lower bound ignorable (it's the second sentence after Eq. 13). The reviewer's question is reasonable but the paper addresses it adequately.
- *Harsh Critic's point about selective criticism of Chen et al. using test set as validation*: The paper applies this criticism to exactly one model that explicitly did this, and does not level it at any other baseline. This is factually correct and appropriate.
- *Harsh Critic's complaint about missing limitations section*: The parser strips appendix content. The paper may well have this in the appendix.
- *Harsh Critic's point about why random recurrent delays help and gradient comparison*: Interesting but speculative — requesting additional analyses that go beyond what the paper set out to demonstrate.
- *Several generic strengths from the Strength Finder*: Statements like "addresses an important problem" are generic and not specific enough to the paper's concrete contributions.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Add 3–5 seed results with mean and std for PS-MNIST. Even if prior work did not, setting a better standard strengthens the paper.
2. Briefly discuss the SSC combined-delay result — even a one-paragraph conjecture (overfitting, optimization conflict, or redundancy with recurrent delays) would address the reader's natural curiosity.
3. Specify the σ annealing schedule (e.g., "linear decay from σ=5 to σ=0 over E epochs, applied after each epoch") in the main text or a table in the main body.
4. Clarify the "first SGL-based" claim to reference the continuous/per-neuron aspect that differentiates DelRec from Xu et al.'s discrete per-layer approach.

## Score and Decision

**Anchors used for calibration:**

| Anchor ID | Avg Score | Round | Paper Topic | Comparison to DelRec |
|-----------|-----------|-------|-------------|---------------------|
| pIJR9uPjy3 | 4.50 | R1 | Delay Neural Networks (DeNN) | Weaker — poor exposition, technical issues, limited evaluation |
| drPDukdY3t | 6.25 | R1 | DeepTAGE (SNN gradient enhancement) | Similar — both accepted-quality, DelRec has stronger novelty/ablation |
| eN4g4cjFX1 | 5.75 | R2 | ST-DANO (neuron optimization for temporal deps.) | Weaker — rejected due to incomplete comparisons |
| 9HsfTgflT7 | 6.20 | R2 | Temporal Flexibility in SNNs | Similar — both accepted, DelRec has cleaner contribution |
| FlH6VB5sJN | 5.20 | R2 | Multi-compartment spiking neurons | Weaker — rejected, limited novelty, narrow scope |

**Round 1 bracket:** 5.5–7.5. **Round 2 narrowing:** DelRec is clearly stronger than all rejected anchors (DeNN at 4.50, ST-DANO at 5.75, PMSN at 5.20) and comparable to or slightly stronger than accepted anchors (DeepTAGE at 6.25, Temporal Flexibility at 6.20). The paper's main weaknesses (σ schedule, PS-MNIST single seed, combined delay discussion) are addressable and do not threaten the core contribution.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>