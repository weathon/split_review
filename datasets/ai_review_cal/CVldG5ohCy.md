- Decision: Reject
- Avg Score: 4.00
- Scores: 6, 3, 6, 1
Now I have a thorough understanding of the paper and all the reviewer inputs. Let me produce the final consolidated review.

## Summary

The paper proposes AdamQLR, an optimizer that applies K-FAC's Levenberg-Marquardt damping and quadratic-model learning rate selection to Adam's update direction. The core idea is to keep Adam's well-established update direction $\mathbf{d}_t$ but replace its manually-tuned learning rate with one computed from a local second-order model using the Fisher information matrix, while also adapting the damping parameter to maintain model trustworthiness. Experiments span MLPs on UCI regression tasks, Fashion-MNIST, and ResNet-18 on SVHN/CIFAR-10, comparing against SGD, Adam, and K-FAC.

## Strengths

1. **Well-designed sensitivity study demonstrates robustness to hyperparameters**: Section 4.7 (Figure 3) systematically varies initial damping, learning rate rescaling, batch size, and clipping threshold. The key finding — that scaling the automatically-selected learning rate by $k \neq 1$ does not improve test error and that initial damping choice is largely irrelevant — directly supports the claim that AdamQLR can be used without extensive tuning. This is the paper's strongest empirical contribution.

2. **Untuned variant achieves competitive performance on multiple tasks**: On UCI Protein (Section 4.3), the untuned version is "clearly superior to tuned SGD" and competitive with tuned Adam. On Fashion-MNIST (Section 4.4) and SVHN (Section 4.5), the untuned variant performs within a small margin of the best methods despite using fixed default hyperparameters. This demonstrates genuine practical value — reducing tuning burden while maintaining performance.

3. **SVHN results show a clear case where AdamQLR outperforms both Adam and K-FAC**: On the ResNet-18/SVHN benchmark (Section 4.5, Figure 2d), AdamQLR reaches lower test loss than tuned Adam and avoids the severe overfitting that plagues K-FAC, while remaining more stable. This provides a concrete success case that aligns with the paper's motivation (combining second-order stability heuristics with a first-order direction).

4. **Well-motivated framing and clear exposition**: The paper articulates a clear research question — whether second-order methods' success is driven by their curvature model or by their stabilising heuristics — and proposes a natural experiment (Section 3.1). The method is described as a wrapper around Adam (Section 3.4), making the contribution easy to understand and implement.

## Weaknesses

### Fatal
None.

### Major

1. **No wall-clock runtime comparison, despite the method adding per-iteration cost**: AdamQLR requires an additional forward pass (to compute $M(\theta_t)$) and a Fisher-vector product (one additional backward pass per product), as acknowledged in Section 3.4. The paper claims these "turn out not to impede performance in our experimental results" (line 106) but provides zero quantitative evidence — no time-per-iteration figures, no time-to-target-loss curves, no runtime overhead percentages. All loss plots use epochs on the x-axis, which is uninformative when comparing methods with different per-iteration costs. For a paper whose practical appeal is central to its contribution, this is a significant evidential gap. A practitioner cannot evaluate whether the moderate improvement in convergence quality justifies the extra compute.

2. **Improvements over Adam are modest on most benchmarks, weakening the core claim**: The paper's central narrative is that borrowing second-order heuristics improves Adam. Examining the results:
   - **UCI Energy**: SGD Full outperforms all methods; AdamQLR is competitive with but not clearly better than Adam (Section 4.2).
   - **UCI Protein**: K-FAC is "clearly the best-performing algorithm"; tuned AdamQLR outperforms Adam, but the gap is modest (Section 4.3).
   - **Fashion-MNIST**: AdamQLR is "the most performant algorithm by a very small margin" (Section 4.4, emphasis added).
   - **CIFAR-10**: All methods reach similar test loss; the main difference is convergence speed, not final performance (Section 4.6).
   
   Only on SVHN does AdamQLR show a clear and substantial advantage. The paper's claim that AdamQLR "competes strongly with tuned commonly-used optimisers" is fair, but the stronger implicit claim — that the second-order heuristics materially improve Adam — is only weakly supported.

### Minor

3. **Limited theoretical insight into why the combination works**: The paper acknowledges (citing Kunstner et al. 2019) that Adam's curvature estimate (the empirical Fisher with a square root) and the true Fisher used for the quadratic model have known mismatches, but does not analyze when or why AdamQLR's learning rate selection should be expected to help or harm. This limits the contribution to an empirical recipe rather than a principled advance. A study of the reduction ratio $\rho$ over training, or of settings where the quadratic model is a poor fit, would strengthen the paper.

4. **No comparison to other adaptive learning rate methods in related work**: The paper cites hypergradient-based methods (Franceschi et al. 2017, Clarke et al. 2022) and other quadratic-model approaches (Kwatra et al. 2023, Zhang et al. 2019) in related work but does not compare against any of them empirically. Even a single comparison would help position the contribution and address the natural question: "does adding second-order LR selection to Adam work better than simpler LR adaptation schemes?"

5. **K-FAC baseline comparison details are underspecified**: The paper states K-FAC has "tuned initial damping" (line 128) but does not specify what other K-FAC hyperparameters (e.g., momentum, Kronecker update frequency, weight decay) were used or whether they were tuned. Given K-FAC's known sensitivity to its many interacting hyperparameters, this lack of detail makes it harder to assess whether the comparison is fair. The absence of wall-clock time also matters here, as K-FAC's factor updates have non-trivial cost.

### Trivial
None.

## Nice-to-Haves

- **Plot the damping and learning rate trajectories over training** to show how $\lambda$ and $\alpha$ evolve, which would give insight into the method's behavior and when the quadratic model is trusted.
- **Add an ablation isolating the learning rate selection from the damping** — e.g., Adam with damping alone but default LR, and Adam with QLR alone but no damping. This would disambiguate which component drives improvements.
- **Compare untuned AdamQLR against untuned Adam (default hyperparameters)** to show the tuning-effort benefit directly, rather than only comparing against tuned baselines.

## Removed Points

These points are flagged to be removed — treat them with caution:

- **"The paper's contribution is more incremental than its framing suggests" / "straightforward engineering hybrid"**: This is a general judgment about novelty, not a specific verifiable weakness. The paper explicitly claims "first use of damping and second-order approximations to select learning rates in Adam," which is a specific, falsifiable novelty claim. The critic provides no evidence that this exact combination exists in prior work. While the components are individually standard, the specific combination is unrefuted. Removed as an uninformed judgment rather than a verifiable weakness.

- **"The paper does not provide standard deviations or confidence intervals for the final numerical results (Table 5)"**: Table 5 likely exists in the original submission (it is referenced at lines 132 and 164) but is not visible due to PDF extraction. The paper does show variance via standard deviation bands in all loss-evolution figures. Removed due to extraction artifact.

- **"K-FAC's reported overfitting may be a tuning artifact rather than a structural advantage of AdamQLR"**: This is purely speculative. The paper attributes K-FAC's overfitting to a known issue cited in the K-FAC literature (Martens et al., 2018). The critic provides no evidence that better K-FAC tuning would eliminate overfitting. Removed as speculation.

- **"The untuned variant should be compared against Adam with its default hyperparameters"**: The paper's claim is that untuned AdamQLR "competes with methods using tuned hyperparameters." Comparing against Adam with defaults would be a different claim. The existing comparison against tuned Adam is the harder test and arguably stronger evidence. Removed as a misunderstanding of the paper's framing.

- **"Algorithm 2 is missing" / "the extracted text lacks pseudocode"**: Image-based algorithms are routinely stripped by PDF extraction. The paper clearly describes the method's operation in Section 3.3-3.4. Removed as an extraction artifact.

- **"Missing related works"**: Per the hard rules, I cannot mention missing related works as I have no external sources to confirm their existence.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface any observation about the paper that the paper itself does not already convey or imply.

## Suggestions

1. **Add wall-clock time curves** to at least one benchmark (e.g., SVHN or Fashion-MNIST) showing loss vs. time for AdamQLR, Adam, SGD, and K-FAC. This is the single most important piece of missing evidence for a practical optimizer paper.

2. **Provide an ablation of QLR vs. damping**: Run AdamQLR with (a) learning rate selection only (fixed $\lambda$), (b) damping only (fixed $\alpha$), and (c) both, to isolate contributions. The sensitivity study (Section 4.7) already shows the learning rate is near-optimal ($k\approx 1$); showing damping's contribution separately would complete the picture.

3. **Add a study of the reduction ratio $\rho$** over training on one or two benchmarks to show when the quadratic model is trusted or rejected. This would provide the theoretical insight the paper currently lacks.

4. **Include at least one empirical comparison to an adaptive LR method** from the related work (e.g., hypergradient descent or Kwatra et al. 2023) to better position the contribution within the adaptive learning rate literature.
