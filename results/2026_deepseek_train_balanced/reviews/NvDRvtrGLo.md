## Summary

TRENDy proposes combining the scattering transform with a parameter-conditioned neural ODE (NODE) to learn low-dimensional "effective dynamics" from PDE solution data, enabling bifurcation prediction in unseen parameter regimes. The core idea—using handcrafted multiscale scattering features as a regularized effective state, then modeling their temporal evolution with a parametric NODE—is well-motivated and clearly presented. The paper's strongest evidence comes from the Brusselator experiment, where TRENDy trained on data held at least \(\epsilon=0.15\) away from the Hopf manifold still recovered a qualitatively correct bifurcation curve via numerical continuation.

## Strengths

- **Novel, well-motivated synthesis of scattering features with parametric NODEs.** The paper identifies a genuine gap—prior work on effective dynamics of PDEs (e.g., Vlachas et al. 2022) does not handle parameter conditioning, preventing bifurcation prediction—and proposes a clean solution. The theoretical observation that any Fréchet-differentiable \(\Phi\) induces an ODE on the effective space (Eq.~\ref{eq:effective}, line 61) provides a principled foundation.

- **The Brusselator experiment demonstrates genuine bifurcation prediction with extrapolation.** Training data is explicitly held at distance \(\epsilon \geq 0.15\) from the true Hopf manifold (line 143), meaning TRENDy "never observed an actual bifurcation during training" (line 155). Numerical continuation on the learned model recovers a bifurcation curve that is "almost always concave up and is always monotonically increasing, matching the qualitative behavior of the true manifold" (line 157). This is the paper's most convincing result and directly supports its main claim.

- **Graceful degradation under controlled noise conditions.** Across clean, boundaries, and patches noise conditions, TRENDy with 10 scattering coefficients maintains accurate bifurcation detection while SINDyCP "degraded sharply with noise" (line 128, Fig. 2). The systematic comparison across three noise levels and five measurement types (T2, T5, T10, SG, FV) plus SINDyCP shows a clear trend.

- **Effective state supports pattern classification without a decoder.** In the Gray-Scott pattern classification experiment (Fig. 3, line 132), TRENDy's learned effective state enables 4-way SVM classification of patterning regimes (dense spots, homogeneity, sparse spots, stripes) with higher F1 than spatial gradient or Fourier features. This supports the claim that the scattering-based effective state is *interpretable*—the dynamics themselves can be decoded back to categorical spatial classes.

- **Application to real biological data.** The ocellated lizard experiment (lines 159-173) demonstrates TRENDy on a real-world dataset, achieving 95% SVM accuracy in predicting anatomical quadrant from learned dynamics. While the interpretive claim is debated below, the experiment itself shows the framework can handle real, noisy developmental video data.

## Weaknesses

### Fatal
None.

### Major

1. **Insufficient baselines for the claim of superior performance and noise robustness.** The paper compares against SINDyCP, spatial gradient (SG), and Fourier vector (FV) features. SINDyCP is a sparse regression method for *equation discovery*, not a method designed for learning effective dynamics under noise—its poor performance on the noise conditions is expected, not a revelation. SG and FV are different feature choices fed into the same NODE pipeline, not competing methods. The paper itself identifies Vlachas et al. (2022) as the closest prior work ("modeled effective dynamics of PDEs with multiscale features and recurrent neural networks," line 21) but never compares against it or any learned latent-dynamics baseline. A parameter-conditioned VAE + NODE or a grid of alternative recurrent latent-dynamics models would be needed to support the claim that TRENDy is "significantly more robust to noise compared to existing methods" (line 4). As it stands, the "existing methods" tested are either from a different paradigm (SINDyCP) or are variants of TRENDy's own feature engineering.

2. **Gray-Scott bifurcation test is interpolation, not extrapolation to unseen parameter regimes.** The training \(k\) range is \([0, 0.075]\) (line 118). The true Turing bifurcation is at \(k^* \approx 0.062\) (for \(F=0.054\)). Thus the training set contains data from **both below and above** the bifurcation within the same \(k\) interval. The heldout test data is a narrow rectangle "centered on the bifurcation value of \(k^*=.062\)" (Fig. 4 caption)—which falls entirely within the training \(k\) range. The model interpolates between training samples on either side of the bifurcation, which is less remarkable than predicting a bifurcation in genuinely unseen \(k\) territory. The paper's framing (e.g., "predict both Turing and Hopf bifurcations in unseen regions of parameter space," abstract) overstates this result. **Mitigation:** The Brusselator experiment uses a genuine holdout and does not suffer from this issue; the paper even acknowledges Gray-Scott's limitation ("only trained and evaluated in a narrow strip," line 135) before pivoting to the Brusselator. But the abstract and introduction do not caveat the Gray-Scott result.

3. **Lizard experiment interpretation outruns the evidence.** Patch coordinates (upper-left corner) are literally passed as parameters \(\theta\) to the NODE (line 169). It is therefore expected—by construction—that the learned dynamics differentiate by coordinate. The subsequent SVM achieving 95% accuracy on quadrant labels (line 173) primarily confirms the model used the coordinate information it was given; it does not, by itself, "highlight the potential influence of surface geometry on reaction-diffusion mechanisms" (line 173). To support such an interpretive leap, the experiment would need a proper null model (e.g., permuted coordinates, or withheld-region extrapolation) to establish that the clustering by quadrant is not a trivial consequence of the model design. Additionally, data comes from a single animal's video, so the quadrant distinction could reflect temporal artifacts, lighting gradients, or imaging non-uniformities rather than genuine biological geometry-dynamics coupling.

### Minor

1. **No uncertainty quantification for any quantitative claim.** The key numerical results—estimated \(k^* = 0.0624\) vs. \(0.0651\) (line 128), 95% accuracy (line 173), F1 scores (Fig. 3)—are reported as point estimates without variance, confidence intervals, or replication across random seeds. NODE training involves stochastic optimization, so variance is expected. Without knowing whether differences between conditions or methods are statistically significant, these results are anecdotal.

2. **Key design choices are stated without justification or ablation.** The NODE is a 4-layer MLP with 64 hidden units and ReLU activations (line 69), used in all experiments. The loss includes a derivative-matching term with weight \(\beta\) and a burn-in period \(\tau\) (Eq.~\ref{eq:loss}, line 74). No ablation or sensitivity analysis is provided for any of these choices. Whether the derivative term is necessary, whether ReLU is appropriate for a dynamical system (where smoothness matters for integration), and how \(\tau\) and \(\beta\) were selected are all unclear.

3. **Numerical continuation procedure is not described.** The paper states that numerical continuation was used to locate bifurcations from the learned NODE (lines 127, 155) but never specifies the numerical criterion for detecting a Hopf or Turing bifurcation. This is critical for reproducibility.

### Trivial
None.

## Nice-to-Haves

- **Add a learned latent-dynamics baseline.** A parameter-conditioned VAE + NODE (or an RNN on scattering features as in Vlachas et al. 2022) would directly test whether the handcrafted scattering features provide the advertised robustness advantage over learned representations.
- **Report uncertainty via multiple random seeds.** Run at least 5 seeds and report mean \(\pm\) std for \(k^*\) estimates, F1 scores, and forecasting errors.
- **Restructure the Gray-Scott experiment as a genuine extrapolation test.** Train on data from only one side of the bifurcation and test on the other, matching the Brusselator design.
- **Add a null model for the lizard experiment.** Compare against permuted coordinates or train on some anatomical regions and test on held-out regions.
- **Ablate loss components.** Remove the derivative-matching term (\(\beta=0\)) to isolate its contribution.
- **Report computational cost** (training time, inference time) relative to baselines.
- **Describe the numerical continuation criterion** used for Hopf/Turing bifurcation detection.

## Removed Points

These points from the inputs are flagged to be removed; treat them with caution:

- **Training details in appendix (Harsh Critic).** The critic noted that "training details are entirely in the excluded appendix." The parser strips all appendix material from the extracted text; the appendix exists in the original submission. Removed per hard rule.
- **Criticism about missing related works.** Removed per hard rule (no external sources to confirm/reject claims about missing citations).
- **"Reliance on true a(0) at test time limits practical usefulness" (Harsh Critic).** This is standard practice for NODE-based methods—the initial effective state is computed from observed data. In the noise experiments, a(0) is computed from noisy/masked spatial fields through the scattering transform, so it is NOT "clean." Removed: this criticism is factually incorrect about the experimental setup.
- **Formatting/style nitpicks and typo complaints.** Removed per hard rule; these are parser artifacts.
- **Strength: "Systematic benchmarking against multiple baselines" (Strength Finder).** The "baselines" are mostly different feature variants of TRENDy itself (T2, T5, T10, SG, FV), plus SINDyCP. Calling this a systematic benchmark against multiple *methods* overstates the comparison. Removed as overclaimed.
- **Strength: "Real biological data reveals geometry-dependent dynamics" (Strength Finder, as stated).** This conflicts with verified weakness #3 on the lizard experiment. The strength that TRENDy *can* model real data is kept above; the interpretive claim that the data *reveals* geometry-dynamics coupling is removed because the weakness (#3) demonstrates the evidence does not support that reading.

## Novel Insights

Beyond the paper's own contributions, the most interesting observation from the cross-review is the framing tension between the two experiments: the Gray-Scott experiment is presented as the headline result but its design (interpolation across the bifurcation) undercuts the paper's central claim of extrapolation, while the Brusselator experiment actually delivers on that claim but is presented as a secondary follow-up. Reordering and reframing these experiments in the paper would strengthen the narrative substantially—the Brusselator should lead, with Gray-Scott as a complementary demonstration. The review also surfaces an underappreciated virtue of the scattering transform choice: because it is fixed rather than learned, the effective state is forced to capture physically meaningful spatial statistics (multiscale energy distribution) rather than any arbitrary linear projection, which is likely why it outperforms spatial gradient and Fourier features on the pattern classification task.

## Suggestions

1. **Lead with the Brusselator experiment.** It is the strongest evidence for the paper's core claim and should be the primary result, not presented as an afterthought motivated by Gray-Scott's limitations.

2. **Restructure Gray-Scott as a genuine extrapolation test.** Train on data from only one side of the Turing bifurcation and test on the other side, matching the Brusselator design. This would directly substantiate the abstract's claim.

3. **Add at least one learned latent-dynamics baseline.** A parameter-conditioned VAE + NODE would be the most natural comparison and would directly test the claimed robustness advantage of scattering features over learned representations.

4. **Report means and standard deviations across multiple random seeds (≥5)** for all quantitative results. This is standard for deep learning papers and essential given stochastic NODE training.

5. **Add a null model for the lizard experiment.** Compare against a model trained on permuted coordinates or show that TRENDy can generalize to held-out anatomical regions, to support the interpretive claims about geometry-dynamics coupling.

6. **Describe the numerical continuation criterion** for Hopf/Turing bifurcation detection in the main text.

7. **Ablate the derivative matching term** in the loss function to clarify its contribution.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>