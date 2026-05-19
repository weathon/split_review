- Decision: Reject
- Avg Score: 3.00
- Scores: 3, 3, 3
Now I have a thorough understanding of the paper and all the review inputs. Let me craft the final consolidated review.

---

## Summary

This paper addresses the problem of providing multi-step algorithmic recourse paths to individuals who receive negative decisions from ML classifiers. The authors propose a framework that (1) learns an optimal distance function and threshold from feasibility-labeled transition data, with PAC guarantees, and (2) augments the dataset with new points to ensure a recourse path exists for every negatively-classified individual. Experiments on synthetic and three real datasets show that the method achieves validity=1 (everyone gets a path satisfying the learned constraints), while baselines (FACE, counterfactual explanations) fail to provide paths for some individuals.

## Strengths

- **PAC learnability results for the distance-and-threshold hypothesis class**: The paper proves (Theorem 2.2) a bounded VC-dimension when the set of candidate distance functions is finite, and (Theorem 2.5) a VC-dimension of at most 2n+1 for the more flexible additive-form distance functions. Algorithm 1 provides an efficient exact ERM. These are concrete theoretical contributions that directly support the claim that a near-optimal feasibility classifier can be learned from data.

- **Data augmentation algorithm with a formal convergence guarantee**: Theorem 2.8 specifies conditions under which Algorithm 2 (augmentation) always converges to a positive outcome. This is a novel formal guarantee for an augmentation-based recourse method that explicitly aims to fill gaps where the original data does not contain a path.

- **Model-agnostic design with practical advantages**: The method requires only the classifier's continuous prediction probabilities (not gradients, causal graphs, or model internals). This is demonstrated with logistic regression and is a genuine practical advantage over methods that require differentiability or causal structure.

- **Incorporation of directional and monotonicity constraints**: For the Adult and HELOC datasets, the distance functions encode domain-appropriate constraints (e.g., age and education must increase; returns ∞ if monotonicity is violated). This is a concrete improvement over purely proximity-based approaches and shows the framework can incorporate domain knowledge.

- **Honest ablation on the λ hyperparameter**: Figure 3 systematically varies λ and reports path length, validity, average distance, and weight, showing the trade-off between path ease and convergence speed. The paper honestly reports a case where large λ leads to non-convergence for some individuals (validity < 1), providing useful practical guidance.

## Weaknesses

### Fatal
None.

### Major

- **The ground-truth feasibility labels are synthetic and their external validity is unestablished**. The paper constructs \(h^*\) using hand-defined rules (e.g., L1 distance per feature below one standard deviation; monotonicity constraints on age, education, etc.) with no justification that these rules approximate real-world feasibility. While the paper acknowledges this limitation (Conclusion: "future directions will include using human annotators for labeling transitions"), the core evaluation—learning distance/threshold and augmenting—is demonstrated against these self-defined standards. The claim that the method learns "feasible recourse" is therefore only as strong as the connection between these labeling rules and actual feasibility, which is not established.

- **Evaluation of recourse paths is self-referential**. Validity (VAL) is defined as \(d(z,w) \leq \tau\) for consecutive steps, where \(d\) and \(\tau\) are the *learned* distance and threshold. The augmentation algorithm constructs paths precisely to satisfy \(d(x',y) \leq \tau\). Thus VAL=1 is largely guaranteed by construction when the algorithm converges. The paper would be stronger with independent path validation—e.g., verifying paths against the original \(h^*\) labels (hold-out), or against a separate gold standard. Table 1 does show low 0-1 error of the learned classifier against \(h^*\), which partially mitigates this, but the path evaluation itself remains circular and the headline result ("our method finds feasible recourse for all") is less impressive than it first appears.

- **Augmented points are not assessed for realism**. When no feasible transition exists in \(V \cup U\), Algorithm 2 generates a new point \(q \notin V \cup U\) constrained only by the learned \(d\) and \(\tau\). The paper provides no evaluation of whether these generated points correspond to plausible real-world states—e.g., distance to nearest real data point, featurewise plausibility checks (do generated capital gains violate legal limits?), or domain-expert assessment. Without this, the guarantee of "recourse for all" may produce mathematically valid paths that are practically unrealistic.

### Minor

- **Limited baseline comparisons**: Only two baselines are compared (FACE and nearest-neighbor CE). The paper mentions StEP in related work but does not compare against it. While the paper states this is because only these implementations were available, the absence of comparisons to other path-based and causally-aware methods limits the evidence for the method's relative effectiveness. (Note: using the same learned \(d,\tau\) for FACE as for the proposed method is a reasonable experimental choice, not unfair—it gives FACE the best available feasibility parameters.)

- **No error bars in Figure 2**: Recourse path evaluation uses 50 random samples per dataset, but Figure 2 shows only point estimates without error bars or confidence intervals. Given stochasticity in the Bayesian optimization-based augmentation, variability should be reported.

- **No systematic analysis of failure modes**: The paper reports one case (λ=0.01 on PIMA) where the algorithm was killed due to slow convergence, but does not systematically characterize when the algorithm fails—e.g., for points far from all positive points, in low-density regions, or with certain classifier geometries.

- **Convergence guarantee relies on strong assumptions**: Theorem 2.8 requires that "for all \(x\) there exists \(y\) with \(f(y)-f(x) > \lambda / \min_{a,b} w(a,b)\)" and that "the algorithm only chooses fresh points." The paper acknowledges this is idealized, and Figure 3 empirically shows convergence failures in practice, but the gap between guarantee and practice could be discussed more explicitly.

- **Bayesian optimization without global optimality guarantee**: The augmentation solver uses Bayesian optimization with a fixed budget; there is no guarantee of finding the global maximum, meaning the algorithm could fail to find a feasible extension even if one exists.

- **No discussion of computational cost or scalability**: Runtime is only reported for λ-variation experiments on two datasets (PIMA and synthetic). Practical scalability to large datasets or many negatively-classified individuals is not discussed.

### Trivial

- The density estimation method for the weight function \(f_\rho\) (used in \(w(x,y) = d(x,y) / f_\rho((x+y)/2)\)) is not specified—e.g., KDE kernel and bandwidth selection are not mentioned.
- Label generation for the synthetic dataset is described only as "using a causal graph" without further detail on how the causal graph was used to derive feasibility labels.

## Nice-to-Haves

- Replace or supplement the synthetic labeling with a more grounded experiment (e.g., using actionability constraints from Ustun et al.'s actionability catalog, or human-annotated labels).
- Ablate the learning component by comparing to a fixed \(d\) (e.g., L2) and fixed \(\tau\) (tuned by cross-validation) to isolate the value of the learning pipeline.
- Assess augmented point realism by reporting minimum distance to nearest real point, featurewise plausibility bounds, or a small domain-expert evaluation.
- Add confidence intervals to Figure 2 and report results across multiple random seeds for the augmentation.

## Removed Points

These points were flagged by the reviewers but are removed from the main weaknesses for the reasons stated. Treat them with caution if considering them:

- **"Comparison to FACE is unfair because FACE is given the learned d,τ"**: Removed. Using the same learned d,τ for both methods is a reasonable and fair comparison—it gives FACE the best available estimate of feasibility. If anything, this asymmetry favors the baseline rather than the proposed method.
- **"Training set size makes the sample complexity bounds easily satisfied"**: Removed. Having sufficient data to satisfy theoretical bounds is a positive property, not a weakness.
- **"Abstract/Introduction overstates the landscape"**: Removed. The paper says "most" methods provide single-step CFEs, which is accurate, and it explicitly cites FACE as a multi-step method whose limitations motivate the work.
- **"No code or data release mentioned"**: Removed per instructions—cannot question release status of cited entities.
- **"Misspecification (h* not in hypothesis class) not discussed"**: Removed based on closer reading—the paper acknowledges this in the Conclusion ("we can study more expressive feasibility functions"), and misspecification is a standard assumption in PAC learning that applies to nearly all such work.
- **Formatting, style, and grammar nitpicks**: Removed per instructions (these are parser artifacts, not author errors).

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Break the circular evaluation**: Validate paths against a held-out portion of the original h* labels, or better yet, against an independently constructed feasibility standard. This would separate the quality of the learned d,τ from the construction of paths that satisfy those constraints.
2. **Assess augmented point plausibility**: Report at minimum the distance from each augmented point to its nearest real training point, and perform featurewise sanity checks (e.g., do generated values fall within plausible real-world ranges?).
3. **Add error bars to Figure 2**: Report mean and standard deviation across multiple runs for all metrics, especially given the stochastic nature of Bayesian optimization.
4. **Characterize failure modes systematically**: Beyond the λ=0.01 case, analyze conditions under which the algorithm does not converge or generates implausible points.
5. **Expand baseline comparisons**: Where implementations are available, compare to StEP (Hamer et al., 2023) and causally-aware methods on the synthetic causal dataset where causal structure is available.
