Now I have all the information needed. Let me produce the consolidated final review.

## Summary

This paper proves a "law of balance" for SGD under rescaling symmetries: the norm difference $\|u\|^2-\|w\|^2$ decays deterministically under SGD noise, establishing an $O(1)$ non-perturbative gap between SGD and gradient flow stationary solutions. It then derives the first closed-form stationary distribution of SGD for diagonal linear networks of arbitrary depth and width. The resulting distribution exhibits phase transitions (critical learning rate for learnability), a depth-dependent power-law tail, broken ergodicity, and fluctuation inversion — phenomena claimed to distinguish deep from shallow models. An extended scaling law linking depth, width, learning rate, and batch size is also obtained in the infinite-depth limit.

## Strengths

1. **Non-perturbative law of balance (Theorem 1).** The paper proves that for any loss with the rescaling symmetry $\ell(u,w,x)=\ell(\lambda u, w/\lambda, x)$, the quantity $\|u\|^2-\|w\|^2$ evolves under a deterministic decay equation driven by the SGD noise covariance, with the stationary ratio $\|u\|^2/\|w\|^2$ bounded between data-dependent eigenvalue bounds. This cleanly demonstrates that even infinitesimal SGD noise produces an $O(1)$ change relative to gradient flow — a genuinely non-perturbative result. Evidence: Theorem 1, the eigenvalue bounds (lines 60–67), and the explicit two-layer linear network example (lines 78–90).

2. **First exact stationary distribution for a deep nonlinear network.** The paper derives a closed-form stationary distribution (Eq.~\ref{eq: stationary distribution}) for a diagonal linear network of arbitrary depth $D$ and width $d_0$, going well beyond prior local approximations (Mandt et al., Mori et al.) that assumed convexity or proximity to a minimum. The distribution is explicit enough to analyze phase transitions, tail behavior, and mode structure. Evidence: Eqs.~(stationary distribution), (P_w_i^2) for depth-1 specialization, and the explicit critical threshold $T_c = (\beta_2-\gamma)/\alpha_3$ (line 172).

3. **Depth-dependent power-law tail independent of data.** The paper shows that for $D\ge1$, the tail of the stationary distribution scales as $v^{-5+3/(D+1)}$, depending only on depth — not on the dataset, learning rate, or batch size. For depth-1 this gives exponent $-7/2$; infinite depth gives $-5$. This explains why deeper networks avoid divergent training loss. Evidence: Section 3.3, scaling analysis leading to $v^{-5+3/(D+1)}$ (line 211), and Figure 3 (left panel) showing agreement with experiments on linear nets.

4. **Extended scaling law linking architecture and optimization.** In the infinite-depth limit, the combination $(d/D)\cdot(S/\eta)$ appears as an effective noise strength, implying that depth, width, learning rate, and batch size can be traded off. This yields a concrete prediction for network design. Evidence: Section 3.4, Eq.~(multi-layer-3), and the discussion of the three regimes $d=o(D)$, $d=c_0D$, $d=\Omega(D)$ (lines 224–231).

## Weaknesses

### Fatal

None.

### Major

1. **Experimental validation partially mismatches the theory's model class.** The theory is derived for diagonal linear networks and more generally for models with the rescaling symmetry $\ell(u,w,x)=\ell(\lambda u, w/\lambda, x)$ (which holds for ReLU but NOT for tanh). Yet several experiments use tanh networks: Figure 2 (right panel, tanh distribution of $v$), Figure 3 (mid, training loss of a tanh network; right, tanh nets on MNIST). Since tanh is not positively homogeneous, the rescaling symmetry does not hold, and these experiments are at best qualitative analogies rather than tests of the theory. The only experiment on the correct model class is the power-law tail check on deep linear nets (Figure 3 left). The paper would be substantially stronger by replacing the tanh experiments with ReLU-based experiments or with direct tests on diagonal linear networks (e.g., measuring the empirical distribution of $v$ and comparing to Eq.~\ref{eq: stationary distribution}). *Severity: The core theoretical results stand on their own, but the experimental section over-promises by presenting tanh results as supporting evidence.*

2. **Theorem 2 (multi-layer net dynamics reduction) is stated without proof or derivation sketch in the main text.** While some derivation may reside in the appendix (which is stripped by the parser), the main text provides no reasoning for why the conditions in Theorem 2 hold at stationarity or how $|v_i|^2-|v_j|^2=0$ for $D>1$ follows from the dynamics. Since this theorem is the crucial step that reduces the multi-dimensional process to a one-dimensional one (the basis for the stationary distribution), the reader cannot verify correctness from the main text alone. *Severity: The paper should at minimum provide a sketch of the Fokker-Planck or SDE argument that yields these conditions.*

3. **The edge-of-stability discussion is only loosely connected to the derived theory.** The paper claims (line 213) that "neural networks with at least one hidden layer will never have a divergent training loss" and that this "directly explains the puzzling observation of the edge-of-stability phenomenon." However, edge of stability is a discrete-time phenomenon observed with full-batch GD near the stability threshold, whereas the paper's theory is continuous-time SGD for diagonal linear networks. The leap from a power-law tail in a stylized model to explaining a discrete-time phenomenon in general networks is speculative and not supported by the experiments shown. This paragraph should be heavily qualified. *Severity: Overclaiming the explanatory reach of the theory.*

### Minor

1. **The per-coordinate balance equation for the two-layer linear network is stated with looser justification than ideal.** The paper writes "Applying the law of balance, we obtain" (line 78) and then gives a per-coordinate equation $d/dt(u_i^2-w_i^2) = -4[T(\alpha_1 v^2-2\alpha_2 v+\alpha_3)+\gamma](u_i^2-w_i^2)$. This equation can be verified by direct computation for the specific diagonal linear network (because $\partial\tilde\ell/\partial(u_i w_k)$ is independent of $i,k$ in this model), but referring to it as simply an "application" of Theorem 1 without explaining why the per-coordinate factorization holds may mislead readers into thinking the general theorem directly licenses per-coordinate decay. The paper would benefit from a brief note clarifying that the specific structure of the diagonal network (the $u_i,w_i$ pairs factor through a single product $v=\sum_i u_i w_i$) enables the per-coordinate reduction. *Severity: Does not affect correctness but impacts clarity.*

2. **The conditional nature of the stationary distribution on the effective width $d$ could be discussed more clearly.** The paper states that the effective width $d\le d_0$ depends on initialization and can be arbitrary (line 146), and the derived distribution (Eq.~\ref{eq: stationary distribution}) is parameterized by $d$. However, the paper does not discuss whether the process can transition between different $d$ values, whether the full stationary measure is a mixture over $d$, or which $d$ values are reachable from typical random initializations. The repeated use of "the stationary distribution" (singular) throughout the paper risks implying uniqueness. Adding a brief qualification about the conditional nature would tighten the framing. *Severity: Presentation clarity, not a technical flaw.*

3. **The infinite-depth scaling law $d/D \cdot S/\eta = \text{const}$ is derived in the $D\to\infty$ limit of a formula whose intermediate steps are not fully shown.** The derivation depends on the stationary distribution (Eq.~\ref{eq: stationary distribution}) whose own derivation is deferred. This makes the scaling law less self-contained than it could be. Including the key intermediate algebraic steps or citing a specific appendix equation would improve verifiability. *Severity: Addressable with additional exposition.*

### Trivial

1. Line 49: The paper defines $T = \eta/T$, which appears to contain a typo (should be $T = \eta/S$ based on usage and the standard SGD literature); the intended meaning is clear from context.
2. Line 67: The phrase "the stationary dynamics of the parameters $u,w$ is constrained in a bounded subspace of the unbounded degenerate local minimum valley" is somewhat overwrought — a simpler statement about bounded ratios would suffice.
3. Figure 3 caption refers to "upper ($-7/2$) and lower ($-5$) bound" of the tail exponent, but $-7/2 = -3.5$ and $-5$ is more negative, so "upper" and "lower" could be misinterpreted.

## Nice-to-Haves

- Direct experiments on diagonal linear networks comparing the empirical stationary distribution of $v$ against the predicted form (Eq.~\ref{eq: stationary distribution}) for various $d$, $D$, and $T$ values would ground the theory's main claim.
- A discussion of whether and how the effective width $d$ can change during training (e.g., can a zero $v_i$ become non-zero?) would clarify the ergodic properties of the process.
- Experiments with ReLU networks (which do satisfy the rescaling symmetry) would better bridge the gap between the toy model and practical architectures.
- The paper notes that weight decay shifts $T_c$ (line 172) but does not extend the analysis to deep networks with weight decay; extending even the depth-1 analysis to depth > 1 with weight decay would strengthen applicability.

## Removed Points

- **Per-coordinate law of balance as a "structural/fatal" flaw.** The harsh critic claimed that the derivation "collapses" because the law of balance (Theorem 1) only constrains global norms, not per-coordinate differences. However, the per-coordinate equation for the diagonal linear network (Eq.~\ref{u^2-w^2}) is verifiable by direct computation for this specific model: because $\partial\tilde\ell/\partial(u_i w_k)$ is $i$-independent, the factor $(u_i^2-w_i^2)$ factors out of each coordinate's dynamics. Critic's conclusion that the central result collapses is not supported by the paper as written — the per-coordinate equation is a model-specific consequence, not an unjustified application of the general theorem. This is downgraded to a minor clarity concern.

- **"Stationary distribution is not unique" as an evidential gap.** The paper clearly states that $d$ depends on initialization (line 146: "We stress that the effective width $d\le d_0$ depends on the initialization and can be arbitrary") and the distribution is conditional on $d$. The critic's claim that "the paper does not discuss whether these components are reachable" is a fair question but not a fatal omission — every initial-condition-dependent invariant measure in a non-ergodic system has this character. Downgraded to minor.

- **Opaque derivation — references to missing appendix content.** Critic's point that Theorem 2 is stated without proof is noted, but the rule against penalizing missing appendix content applies. The paper references an appendix (Section~\ref{app sec: theory}) and a table (~\ref{tab:double_layer}) that are stripped by the parser. The concern about derivation opacity in the main text is retained as Major point 2 above, but the claim that the derivation cannot be verified at all is removed.

- **Scaling law described as "chain of speculation."** The scaling law follows algebraically from the infinite-depth limit of the derived stationary distribution. It is not a heuristic — it is a mathematical consequence of the formula the authors derive. The critic's characterization is too harsh and is removed.

- **Missing related works / "stationary distribution is unknown until today" too strong.** The critic's objection about prior stationary distributions for quadratic settings is noted, but the paper largely acknowledges this context (line 19–20 mentions Mandt et al. and Mori et al.). The claim is qualified as applying to nonlinear, highly-dimensional, nonconvex settings. Not a weakness.

- **Formatting/presentation nitpicks** (notation $C_1$, $C_2$ not defined, eigenvalue bounds not static — these are standard mathematical descriptions) are removed.

## Novel Insights

The harsh critic's observation about the non-uniqueness of the invariant measure (multiple components parameterized by the effective width $d$) is worth emphasizing beyond what the paper itself signals. The paper acknowledges that $d$ depends on initialization, but does not discuss whether the Markov chain is irreducible across $d$-values, whether mixing between components is possible, or whether the stationary distribution should be understood as a mixture. This is a genuine structural nuance: the "stationary distribution" is actually a family of conditional distributions indexed by the number of non-zero subnetworks. For a paper that titles itself "Stationary Distribution of SGD" (singular), this multiplicity deserves explicit treatment — particularly when drawing conclusions about phase transitions and fluctuation inversion that are derived from one component. The strength finder's identification of the non-perturbative law of balance as the paper's most important single contribution is correct and deserves emphasis: Theorem 1 is elegant, independent of the subsequent diagonal-network analysis, and could have broader impact beyond the stationary distribution application studied here.

## Suggestions

1. **Add experiments on the correct model class.** Replace or supplement the tanh experiments with tests on diagonal linear networks (matching the theory) and/or ReLU networks (which respect the rescaling symmetry). At minimum, measure the empirical stationary distribution of $v$ for diagonal linear networks at various $D$, $d$, and $T$ values and compare to Eq.~\ref{eq: stationary distribution}.

2. **Provide a derivation sketch for Theorem 2 in the main text.** Even a short paragraph explaining the SDE or Fokker-Planck argument that leads to the $|v_i|^2-|v_j|^2=0$ condition for $D>1$ would substantially improve verifiability.

3. **Clarify the conditional nature of the stationary distribution.** Add a sentence explicitly stating that Eq.~\ref{eq: stationary distribution} is conditional on the effective width $d$, which is set by initialization, and that the full stationary measure may be a mixture over $d$ values.

4. **Discuss the per-coordinate derivation for the diagonal linear network more carefully.** Briefly note that for the specific diagonal structure, the coupling between coordinates only enters through the scalar $v$, enabling the per-coordinate factorization shown in Eq.~\ref{u^2-w^2}.

5. **Tone down the edge-of-stability claims.** Acknowledge that edge-of-stability is a discrete-time, full-batch phenomenon and that the continuous-time SGD theory provides a suggestive scaling argument, not a proof.

## Score and Decision

**Originality:** High — the law of balance is a novel symmetry-based principle for SGD, and the stationary distribution for diagonal linear networks is the first exact result for a nonlinear deep model.  

**Importance of research question:** High — understanding the stationary distribution of SGD is a central open problem in deep learning theory.  

**Claims supported:** Moderately well for the theory on its own terms; experiments partially mismatch the theory's assumptions.  

**Soundness of experiments:** Moderate — power-law tail results on linear nets are clean, but tanh experiments do not satisfy the symmetry the theory relies on.  

**Clarity of writing:** Good for the theoretical sections; the experimental framing could be more precise about what constitutes a test vs. an analogy.  

**Value to the community:** High theoretical contribution that could inspire further work on symmetry-based analyses of SGD.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>