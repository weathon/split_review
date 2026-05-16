Now I have all the evidence I need. Let me produce the final consolidated review.

## Summary

This paper proposes Variable Forward regularization (-kF), which extends Forward regularization (-F) by introducing a tunable penalty factor \(k\) for online linear regression, and an adaptive variant (-kF-Bayes) that adjusts \(k\) online. The paper provides closed-form recursive updates, derives a relative regret bound for -kF, and evaluates the methods on numerical simulations, tabular continual learning benchmarks, and CIFAR-100 with randomized neural network backbones. The goal is to address practical failures of -F (fixed penalty, vulnerability to non-i.i.d. data) and improve over both -R and -F.

## Strengths

- **Generalization of forward regularization with closed-form updates**: The paper extends -F to a more general form (-kF) that subsumes -R (\(k=0\)) and -F (\(k=1\)) as special cases (Remark 1). The recursive closed-form updates for \(\theta_{t+1}\) and \(\eta_{t+1}\) (Theorem 3) are clearly specified and maintain the non-replay property, which is algorithmically sound.

- **Adaptive -kF-Bayes eliminates manual tuning of \(k\)**: The -kF-Bayes variant adapts \(k\) online (\(k_t = x_t^T \eta_t x_t\)), removing the need for expensive hyperparameter search. Experimental results (Figures 1d, 3, 4b, 5, 6) show that -kF-Bayes achieves competitive or superior performance across numerical, tabular, and image benchmarks without requiring SMAC3 tuning, which is a practical advantage.

- **Broad empirical evaluation across diverse continual learning scenarios**: The methods are tested in numerical simulation (Section 4.1), tabular CIL/OTCIL (Section 4.2), and CIFAR-100 image classification (Section 4.3). The comparison includes EWC, CRNet, DYSON, RanPAC, NICE, GEM, and GSS — a substantial set of baselines. Results consistently show edRVFL-kF-Bayes performing competitively.

## Weaknesses

### Fatal

None.

### Major

- **The adversarial claim is unsupported by the proof technique**: The abstract states that -kF has "a tighter upper bound than -F in adversarial settings." However, Remark 3 reveals that the proof relies on an i.i.d. Gaussian distribution assumption (\( \mathbb{E}[x_{t+1}^T \eta_t x_t] = 0 \)). The -R and -F bounds (equations 4, 5) are deterministic adversarial bounds that make no distributional assumptions. The -kF bound is an expectation under a distributional approximation. This is a fundamental asymmetry: the paper claims adversarial superiority but proves it under a stochastic assumption that the baselines do not require. The paper does not explain how the Gaussian approximation is valid in an adversarial environment, nor does it quantify the approximation error. This gap substantially undermines the claimed theoretical advantage.

- **The -kF-Bayes algorithm (Theorem 6) lacks any theoretical grounding**: The update \(k_{t+1}=k_{t}=x_t^T\eta_t x_t\) is presented as a fact without derivation from Bayesian principles — no prior, posterior, likelihood, or evidence is specified. No regret bound is provided for -kF-Bayes, and the paper does not explain why this specific form mitigates non-i.i.d. effects. Since -kF-Bayes is the main practical contribution (the adaptive method that "curbs unstable penalties" and eliminates tuning), the absence of theoretical justification leaves it as an unverified heuristic. The paper should either derive it properly or present it as a heuristic with a clear caveat.

- **The regret bound in Theorem 5 is written as an equality (\(=\)) rather than an inequality (\(\leq\))**: The text introduces it as "The upper bound of the learner using -kF," which implies an inequality, but equation (16) uses "=". This is a significant formal issue. Regret bounds are upper bounds and should be expressed as \(\leq\). The paper must clarify whether this is a formatting corruption or a mathematical error. Additionally, the bound is in expectation (\(\mathbb{E}[\cdot]\)), while the -R and -F baselines (eq. 4, 5) are deterministic — this difference is not discussed.

### Minor

- **The -kF bound (16) has a denominator \(\lambda + (k-1)X_m^2\) that can become negative for \(k<1\) when \((1-k)X_m^2 > \lambda\)**, which would make the logarithm's argument negative and the bound invalid. The paper states \(k>0\) but does not discuss this validity condition. Since the recommended range is \(0<k<1\) (Remark 4), this condition matters for whether the bound is actually meaningful.

- **Confusing notation in Theorem 6**: The line \(k_{t+1}=k_t=x_t^T\eta_t x_t\) suggests both that \(k\) is constant (\(k_{t+1}=k_t\)) and that it varies with \(t\) (defined via \(x_t,\eta_t\)). This appears to be a writing error that needs clarification — likely the intended meaning is that \(k_t\) is defined as \(x_t^T\eta_t x_t\) and used at the next step.

- **Growth-rate analysis does not prove tighter full bound**: Remark 4 compares growth rates (derivatives w.r.t. \(t\)) of the -R and -kF bounds, concluding \(0<k<1\) gives a better growth rate. As the paper itself acknowledges, comparing growth rates is not equivalent to comparing the full cumulative bounds at finite \(T\). The claim that "-kF have a tighter regret bound than -F's" (line 173) is weaker than the analysis supports — it should say "better growth rate."

- **The experimental evaluation uses randomized neural networks (edRVFL) rather than linear regression**: The paper's theoretical framework is developed for online linear regression, but the main experiments (Sections 4.2, 4.3) use edRVFL — a randomized neural network — as the base learner. The paper does not explain how the -kF update translates to this setting, what \(x_t\) and \(y_t\) correspond to in the neural network context, or whether any regret guarantees are preserved. While extending to NNs is a reasonable application, the primary evaluation should at least include linear regression results to directly validate the theory.

### Trivial

- The \(\eta_{t+1}^\dagger\) update in Theorem 3 (line 109) appears to have a typographical error: the first term is \(\eta_{t}^\dagger\) (as expected from the matrix inversion lemma) but the line shows an overline \(\overline{\eta_t^\dagger}\) in the -kF-Bayes version (line 192).

## Nice-to-Haves

- Provide a condition on \(\lambda\) and \(X_m\) ensuring the denominator \(\lambda + (k-1)X_m^2 > 0\) for the recommended range \(0<k<1\).
- Include a linear regression experiment (without NNs) on a real dataset to directly validate the theoretical claims within the stated scope.
- Discuss the computational overhead of the matrix updates in -kF and -kF-Bayes compared to -R and -F.
- Add a limitations section explicitly acknowledging that the -kF-Bayes update lacks regret guarantees and that the adversarial bound relies on a distributional approximation.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Critical Issue 1 from harsh reviewer ("regret bound for -kF is inconsistent with the claimed degeneration to -R")**: The paper states \(k>0\) in Theorem 5 (line 155), so the bound is not claimed to cover \(k=0\). Remark 1 says the *algorithm* degenerates to -R at \(k=0\), not the bound. There is no inconsistency — the reviewer conflated algorithm degeneration with bound degeneration. *Removed because factually wrong about what the paper claims.*

- **Missing Table 1 and numerical results**: The table is absent from the parsed text. Per the instructions, the parser strips tables and appendices; they exist in the original submission. *Removed because this is a parser artifact, not an author error.*

- **Strength Finder's claim of "Rigorous theoretical regret bound derivation"**: This conflicts with the verified weakness about the proof using a Gaussian distributional approximation under an adversarial claim. *Removed because the weakness (adversarial claim vs. Gaussian proof) is verified and contradicts this strength.*

- **Complaint that -F "fails to -R" is not convincingly demonstrated**: The paper does provide motivation in Section 4.1 with empirical comparisons. The claim is about "even possibly failing to -R" (line 14, emphasis mine), not a blanket failure. The synthetic experiments do compare -F and -R across multiple \(\lambda\) values. *Removed because the paper's claim is more modest than the reviewer asserts.*

- **Criticism that the bound for -kF cannot be compared with -F because the growth rate doesn't prove full bound tightness is a fatal issue**: The growth-rate analysis is presented as what it is — a comparison of asymptotic rates, with the paper acknowledging the full comparison is "complicated" (Remark 4). This is a reasonable analysis, not a fatal flaw. *Downgraded to minor.*

- **Complaint about limited \(k\) values (0.2, 0.4, 0.6, 0.8)**: Ablating 4 values of \(k\) is sufficient for a proof-of-concept in a paper that also proposes an adaptive variant. *Removed as overly demanding for the paper's scope.*

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Clarify the adversarial vs. stochastic setting**: Either (a) prove the bound without the Gaussian approximation (truly adversarial), or (b) clearly state that the -kF bound is in-expectation under a stochastic data assumption, and explain why the comparison to the adversarial -F/-R bounds is still meaningful. The abstract's phrasing should match whatever is actually proven.

2. **Derive or caveat -kF-Bayes**: Either provide a proper derivation showing why \(k_t = x_t^T \eta_t x_t\) follows from Bayesian principles, or explicitly state that -kF-Bayes is a heuristic motivated by Bayesian considerations, with no regret guarantee.

3. **Fix the bound inequality**: Ensure equation (16) uses \(\leq\) not \(=\), consistent with the "upper bound" language in the text.

4. **Add a simple linear regression experiment** on a real dataset (not NNs) to directly validate the theoretical framework without the confounding factors of neural network approximations.

5. **Discuss the denominator condition**: State when \(\lambda + (k-1)X_m^2 > 0\) holds and what happens when it doesn't.

6. **Fix the notation in Theorem 6**: The line \(k_{t+1}=k_t=x_t^T\eta_t x_t\) should be corrected to avoid the implication that \(k\) is constant.

## Score and Decision

This paper presents a clear and well-motivated algorithmic extension of forward regularization, with substantial empirical evaluation across multiple continual learning settings. However, the theoretical contribution has serious issues: the adversarial claim is unsupported because the proof uses an i.i.d. Gaussian approximation, the main practical algorithm (-kF-Bayes) has no theoretical justification or regret analysis, and the regret bound equation has a formal issue (equality vs. inequality). These gaps prevent acceptance in the current form but are addressable with significant revision.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>