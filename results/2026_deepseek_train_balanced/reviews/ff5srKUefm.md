## Summary

This paper proposes "entropy voting," a non-iterative, information-theoretic routing procedure for capsule networks. The authors model capsules as log-normally distributed random variables and define a voting function \(f(\Psi,\Omega) = h(\Psi) + h(\Omega) - D_{KL}(\Psi\|\Omega)\) that maximizes marginal differential entropies while minimizing KL divergence between child and parent capsules. The method replaces the squash activation with softplus, constructs child capsules via 2D depthwise convolution and parent capsules via 3D transpose convolution, and reports inference speedups alongside competitive accuracy on MNIST, CIFAR10, SVHN, and smallNORB.

## Strengths

- **Novel information-theoretic framing of capsule routing.** The paper is the first to formalize capsule agreement as maximizing mutual information \(I(\Psi;\Omega)\) by showing that \(f(\Psi,\Omega) = h(\Psi) + I(\Psi;\Omega)\). This provides a cleaner theoretical lens than prior iterative routing heuristics or attention-based mechanisms (lines 118–119).

- **Substantial and consistently measured inference speedups.** Table 1 reports FPS improvements across all datasets (e.g., MNIST: 1806 FPS vs CapsNet's 1035 and Efficient-CapsNet's 1416, a ~75% gain over CapsNet). The advantage holds on CIFAR10 (1471 vs 781), SVHN (1567 vs 987), and smallNORB (1552 vs 862). These speedups are measured on the same hardware (V100), making within-experiment comparisons valid.

- **Architectural improvements that are clean and reproducible.** The use of 2D depthwise convolution for child capsules (line 77) and 3D transpose convolution for parent capsules (line 81) provides a principled mechanism for dimensionality changes between capsule layers (\(D \to D'\) and \(N \to N'\)) without ad-hoc matrix operations. The softplus activation (Eq. 1) is differentiable and avoids the near-singular behavior of the squash-based routing at the origin.

- **Controlled evaluation protocol controlling for augmentation confound.** The paper applies the same augmentation pipeline (simple affine transformations within \(\pm20\%\)) to all methods and reports results both with and without augmentation (lines 163–169). This is a genuine improvement over prior work that uses disparate, often extensive augmentation pipelines, and it isolates the method's performance under the conditions capsule networks were designed for.

## Weaknesses

### Major

- **Sign error in the core entropy formula (Eq. 3).** The paper gives the log-normal differential entropy as \(h(x) = \mu - \frac{1}{2}\ln(2\pi e\sigma^2)\) (line 98–99). The correct formula is \(h(x) = \mu + \frac{1}{2}\ln(2\pi e\sigma^2)\). The sign error on the \(\sigma^2\)-dependent term means that maximizing \(h(x)\) as written would drive \(\sigma^2 \to 0\), which is the *opposite* of the paper's stated objective: "maximizing differential entropy is basically the same as maximizing variance" (line 102). This is not a formatting artifact—the sign is wrong in the mathematical expression. Since the entropy voting function \(f(\Psi,\Omega)\) is the paper's central contribution (Eq. 2), an error this fundamental to the mathematical derivation undermines the claimed information-theoretic grounding. The authors must clarify whether the implementation uses the correct formula (in which case Eq. 3 is a typo) or the presented one (in which case the optimization does not do what is claimed).

- **Unvalidated baseline reimplementations invalidate the comparative claims.** The paper states explicitly that "none of the baseline implementations achieved performance similar to what was reported in their respective papers" (line 171). On MNIST, the authors' HVC-CapsNet reimplementation is substantially worse than the published results. Since Table 1—the paper's primary evidence—compares the proposed method against these weakened reimplementations, the claim that the method "outperforms all of the three baselines on every dataset" (line 151) is uninterpretable as evidence of superiority over the actual state-of-the-art capsule networks. The paper's own Table 2 shows that published methods (e.g., Byerly et al. at 0.28% error on MNIST with augmentation) match or exceed the proposed method's 0.26% when augmentation is used. The authors acknowledge this tension (lines 173–175) but do not resolve it: the central comparative evidence remains compromised.

- **Univariate information-theoretic framework applied to vector-valued capsules without explanation.** The KL divergence formula (Eq. 4) is explicitly stated as "for two univariate distributions" (line 108). However, child capsules have length 8 and parent capsules have length 16 (lines 79–81). The paper never explains how univariate entropy and KL divergence formulas extend to these multi-dimensional capsules—whether computed per-dimension and averaged, summed, or via some other reduction. The softplus activation (Eq. 1) operates element-wise, but the entropy and KL formulas are presented for scalar random variables. This is a structural gap between the mathematics as presented and the actual implementation.

### Minor

- **Training objective (loss function) is not specified.** The paper describes the entropy voting function \(f(\Psi,\Omega)\) and states that its output is passed through a sigmoid to obtain prediction probabilities (line 114). But it never states the loss function that is actually minimized during training. The reconstruction regularizer loss is described (lines 144–145), but the "overall loss" it is added to is never defined. Is it cross-entropy on the sigmoid outputs? A margin loss? The paper says the method learns "through discriminative learning" (line 195) but does not say what objective drives this learning. This makes the method partially irreproducible from the description alone.

- **Log-normal assumption lacks empirical support.** The justification for modeling capsules as log-normal is a hand-wavy appeal to the central limit theorem: "due to the central limit theorem, the internal activation of artificial neurons can often be regarded as an approximate Gaussian distribution" (line 67). Internal activations of a trained CNN are neither sums of i.i.d. variables nor approximately Gaussian in any verified sense. The paper provides no empirical verification (histograms, QQ plots, goodness-of-fit tests) that capsule activations follow a log-normal distribution. Combined with the softplus approximation (which does not produce a true log-normal from a Gaussian), this weakens the claimed theoretical foundation.

- **No ablation studies to isolate the contribution of entropy voting.** The method bundles: a specific CNN backbone design, depthwise child capsules, 3D transpose parent capsules, softplus activation, and the entropy voting mechanism. Without ablations, it is impossible to determine whether the empirical gains come from the entropy voting function specifically or from the architectural choices. This is particularly important given the sign error in Eq. 3—if the implementation uses the correct formula, the paper's mathematical contribution is correct in spirit but miswritten; if it uses the wrong formula, performance must come from the architecture alone.

### Trivial

None.

## Nice-to-Haves

- Ablation studies replacing entropy voting with a simple learned linear transformation or a single attention head, keeping the architecture fixed.
- Empirical verification of the log-normal assumption (e.g., distributional histograms of capsule activations).
- Specification of the main classification loss (e.g., "cross-entropy between sigmoid outputs and one-hot labels").

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Criticism that the squash function is differentiable (Critic's Section 2 note).** The paper calls the squash function "non-differentiable" (line 41). The squash function is differentiable everywhere except at the origin (where \(\|s\|=0\) creates a non-differentiable point). The paper's characterization is slightly overstated but not fundamentally wrong, and is not a core weakness.
- **FPS on V100 being uninformative.** The paper uses the same V100 GPU for all comparisons, making within-experiment FPS comparisons valid. Hardware specificity is standard practice.
- **Missing related works.** Cannot verify without external sources.
- **Formatting and style nitpicks.** Parser artifacts, not author errors.
- **"No discussion of loss function"** — kept as a Minor weakness above since it's valid; the reference to "missing" here was a duplicate.
- **Strength about "consistent accuracy improvements on all datasets"** — kept but qualified by the baseline reimplementation issue. The raw numbers in Table 1 are genuine; the interpretation is what's contested.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Fix the sign in Eq. 3** immediately. If the implementation uses the correct formula \((h = \mu + \frac{1}{2}\ln(2\pi e\sigma^2))\), correct the paper to match. If the implementation uses the formula as written, the optimization does not maximize variance—this must be explained or the method re-derived.

2. **Validate baseline reimplementations** by reproducing published results within reasonable tolerance, or reposition the paper as: (a) a comparison under equal augmentation (which is a valid contribution), while (b) explicitly stating the comparison is against self-reimplemented baselines using identical training conditions, and (c) toning down claims of outperforming "state-of-the-art."

3. **State the training loss explicitly.** One sentence specifying the loss function (e.g., "We minimize the cross-entropy between the sigmoid output of \(f(\Psi,\Omega)\) and the one-hot ground-truth labels") would resolve the irreproducibility.

4. **Add ablations** comparing entropy voting against a simpler scoring mechanism (e.g., dot-product agreement or a learned linear layer) while keeping the architecture fixed.

5. **Explain how univariate entropy/KL formulas are applied to vector capsules**—either per-dimension averaging or a vector-valued extension.

## Score and Decision

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>