Now I have a thorough understanding of the paper and all review inputs. Let me construct the final consolidated review.

## Summary

The paper identifies a previously unreported training instability affecting shifted ReLU and soft-thresholding activations at Edge-of-Chaos (EoC) initialization: their variance maps have \(V'(q^*)=1\) with positive second derivative, causing exponentially growing variance and training failure. The authors propose magnitude-clipped variants (CReLU, CST) that decouple the EoC condition from variance instability (\(V'(q^*)<1\) while \(\chi_{1,\phi}=1\)). Proof-of-concept experiments on 100-layer DNNs (MNIST) and 50-layer CNNs (CIFAR-10) show the clipped activations train successfully at sparsity levels up to 85%, while the unclipped counterparts fail even at 50–60% sparsity.

## Strengths

1. **Identification of a genuine, previously unrecognized instability.** The paper theoretically proves that for \(\text{ReLU}_\tau\) and soft thresholding, the variance map satisfies \(V'(q^*) = \chi_{1,\phi} = 1\) at the edge of chaos, with \(V''(q^*) > 0\) for \(\tau > 0\). This creates a fragile fixed point that is stable only from the left, causing variance to diverge under finite-width stochasticity. The derivation in Section 2 and Table 1 (equations) are clear and correct.

2. **A principled, simple fix.** Magnitude clipping (CReLU, CST) yields \(\chi_{1,\phi} > V'_\phi(q^*)\), so the EoC condition \(\chi_{1,\phi}=1\) now forces \(V'_\phi(q^*) < 1\), restoring local stability. The analysis of how \(m\) controls \(V'\) and \(V''\) (Section 3.1) provides concrete guidance for choosing the clipping threshold, supported by Figure 3.

3. **Experimental validation of the core theory.** DNNs with CReLU/CST achieve 92–94% test accuracy on MNIST at 85% sparsity — matching the ReLU baseline — while unclipped versions collapse at sparsity as low as 50–60%. The gradient-norm plots (Figure 4) directly confirm that exploding gradients are the failure mechanism for large \(m\), and that clipping prevents this.

4. **Identification of two distinct failure modes.** The paper distinguishes between catastrophic failure from excessive \(m\) (exploding gradients due to variance-map bifurcation) and a plateau failure from too-small \(m\) (reduced expressivity despite stable gradients). This provides useful practical guidance for tuning \(m\).

## Weaknesses

### Fatal
None.

### Major

1. **CNN experiments lack reproducibility and statistical strength.** The paper reports single-run CNN results with no standard deviations, while DNN experiments use 5 seeds. CNN architecture details (kernel sizes, stride, padding, pooling, batch normalization usage) are not specified — only "depth 50" and "300 channels in each layer" are stated. The paper explicitly acknowledges the single-run design (Table 1 caption), but this weakens the "full accuracy retained at 70% sparsity" claim for CNNs. Combined with the fact that even the ReLU CNN baseline (70% accuracy on CIFAR-10) is quite low, the reader cannot assess whether the 66–70% range for clipped activations represents genuine parity or merely noise in a low-accuracy regime.

2. **Missing optimizer hyperparameters.** The paper specifies only SGD with learning rate (\(10^{-4}\) for DNN, \(10^{-3}\) for CNN) and 200 epochs. Batch size, momentum, weight decay, and learning rate schedule are not reported. This hinders reproducibility, especially for the CNN experiments where training dynamics are less well-understood.

### Minor

1. **Second failure mode lacks mechanistic explanation in the main text.** The paper notes that at \(s=0.85\) with small \(m\), accuracy plateaus at \(\approx 78\%\) despite stable gradients, then defers the explanation to the appendix ("discussed further in App. \ref{sec: loss function}"). The main text provides no intuition — is this a capacity bottleneck, an optimization landscape issue, or something else? Since this occurs at the paper's highest sparsity level, the reader deserves at least a hypothesis in the body. (The paper's own conclusions section lists this as future work, which honestly acknowledges the gap but does not fill it.)

2. **"Full accuracy" claim is slightly overstated for CNNs.** The ReLU baseline (τ=0, s=0.50) achieves 70% on CIFAR-10. CReLU at \(s=0.70\) achieves 0.68–0.70 across three \(m\) values. While close, the claim of "full accuracy" would be more precise as "approximately full accuracy" or "near-full accuracy." At \(s=0.85\), accuracy drops to 65–66%, which is further from parity. This is a small overclaim but worth correcting.

3. **No training dynamics for sparsity.** The paper claims "the starting sparsity level is maintained throughout training" but provides no curves showing sparsity evolution over training steps. For a paper about sparsity-inducing activations, this verification would be valuable.

### Trivial
None.

## Nice-to-Haves

- A curve of activation sparsity over training steps would strengthen the claim that sparsity is maintained throughout training.
- Rough estimates of theoretical FLOP reduction from 85% activation sparsity (assuming efficient sparse operations) would better motivate the practical relevance.
- Explaining why the second failure mode occurs (even a brief hypothesis in the main text) would improve self-containedness.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Missing baseline accuracy in Table 1"** — This criticism is factually incorrect. The \( \text{ReLU}_\tau \) row with \(\tau=0.00\) and \(s=0.50\) (first row of Table 1) IS the ReLU baseline: \(\text{ReLU}_\tau(x)=\max(0,x-\tau)\), and with \(\tau=0\) this is the standard ReLU. It shows DNN accuracy 94% and CNN accuracy 70%, against which the clipped results should be compared. The baseline is in the table.
- **"Equation typo \(V'_{CST}(q) = 2 V'_{CST}(q)\)"** — The harsh critic flagged this as a likely parser artifact. Per the parsing instructions, formatting/rendering artifacts should not be treated as author errors. The intended equation is \(V'_{CST}(q) = 2 V'_{CReLU}(q)\), consistent with the pattern in Table 1 and equation (161).

## Novel Insights

None beyond the paper's own contributions. The most interesting cross-review observation is that both reviewers correctly identified the CNN reproducibility gap as the paper's main empirical weakness, while the harsh critic's flagship complaint (missing baseline) was factually wrong — a reminder that even careful reviewers can miss data sitting in plain sight.

## Suggestions

1. **Report the CNN experiments with at least 3–5 seeds** and include standard deviations for both test accuracy and test sparsity, at least for the key sparsity levels (70% and 85% with best \(m\)).
2. **Disclose complete CNN architecture** (kernel sizes, stride, pooling, padding, batch normalization) and all optimizer hyperparameters (batch size, momentum, weight decay, learning rate schedule).
3. **Add one sentence of intuition for the second failure mode** in Section 4 (e.g., "low \(m\) limits the range of activation values, reducing the network's effective capacity independent of gradient stability").
4. **Tone down "full accuracy" to "near-full accuracy"** for the CNN 70% sparsity case and acknowledge the \(\sim 4\%\) relative drop at 85% sparsity more explicitly.

## Score and Decision

The paper makes a genuine theoretical contribution (identifying and fixing a non-obvious initialization instability), proposes a simple and effective remedy, and validates it with proof-of-concept experiments. The weaknesses are real but addressable: the CNN experiments need better statistical rigor and full architectural disclosure, and a few claims need minor calibration. No fatal methodological flaw is present. With reasonable revisions, the paper's core claims are well-supported.

**Score:** 6.0

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>