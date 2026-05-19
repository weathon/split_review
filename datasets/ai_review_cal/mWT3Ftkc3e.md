- Decision: Reject
- Avg Score: 6.50
- Scores: 8, 6, 6, 6
Now I have a thorough understanding of the paper. Let me produce the consolidated review.

## Summary

This paper provides the first convergence guarantee for Consistency Models (CMs). Under \(L^2\)-accurate score estimation and consistency errors (Assumptions 3–4), Lipschitz smoothness of the score and the learned consistency model (Assumptions 2, 5), and finite second moment of the data distribution (Assumption 1), the authors prove that one-step CM generation achieves \(\varepsilon\)-accuracy in Wasserstein-2 distance with polynomial complexity (Corollary 4). They further show that multistep consistency sampling reduces the linear-in-\(T\) dependence to logarithmic (Corollary 6), extend the theory to bounded-support distributions (Section 3.4), and provide TV-error guarantees via OU smoothing or Langevin correctors (Corollaries 9–10).

## Strengths

1. **First convergence guarantee for Consistency Models.** The paper delivers on its central claim: this is the first work to establish a systematic, non-asymptotic convergence analysis of CMs (line 49: *"this is the first work to establish a systematical analysis of the convergence property of CMs"*). Prior work (Song et al. 2023) only provided asymptotic analysis, leaving the finite-sample regime open.

2. **Assumptions are realistic and weaker than comparable analyses.** The results hold under \(L^2\)-accurate score and consistency errors rather than the stronger \(L^\infty\) assumption, and do not require log-Sobolev inequalities, convexity, or dissipativity (Section 3.1, lines 185–186). This class of assumptions is aligned with the best available SGM guarantees and covers highly non-log-concave, multimodal distributions.

3. **Polynomial scaling in all parameters.** The W\(_2\) bounds in Corollary 4 and the discretization complexity \(N = O(L_f L_s^{3/2} d^{1/2} / \varepsilon^2)\) show polynomial dependence on dimension, Lipschitz constants, and accuracy — matching the functional form of ODE-type SGM complexity (line 234).

4. **Multistep consistency sampling provably reduces error.** Corollary 6 shows that recursion with exponential contraction removes the linear-in-\(T\) dependence present in the one-step bound, requiring only \(T \geq \max(\log(2L_f)+\delta, L_s^{-1})\) (Remark 1). This provides the first theoretical justification for the multistep procedure proposed by Song et al. (2023).

5. **Extension to bounded-support and low-dimensional manifold data.** Lemma 7 and Corollary 8 handle the case where the data distribution is compactly supported or supported on a lower-dimensional submanifold, using early stopping to control the score Lipschitz constant. This generalizes the theory beyond smooth-density settings.

## Weaknesses

### Fatal

None.

### Major

1. **The Lipschitz assumption on the learned consistency model (Assumption 5) is a significant gap between theory and practice.** The paper requires \(f_\theta(\cdot, t_n)\) to be Lipschitz with constant \(L_f > 1\) (line 197), but this is an assumption about a learned neural network that is not guaranteed by any training procedure. The sole justification (line 195: *"has been used in prior work (Song et al. (2023), Theorem 1)"*) merely notes prior usage without showing why a trained network would satisfy this condition or how \(L_f\) could be controlled. While the paper honestly acknowledges this as a limitation (Section 4, line 347: *"somehow unrealistic"*), the gap remains structural: \(L_f\) appears in every bound, and without a mechanism to enforce or bound it, the practical relevance of the guarantees is undermined. The natural fix — proving that the *exact* consistency function \(f^{\text{ex}}\) is Lipschitz under Assumptions 1–2 and then only requiring the learned model to approximate it in \(L^2\) — is mentioned as future work but not addressed here.

### Minor

2. **The claim of "matching" state-of-the-art SGM convergence guarantees is slightly overstated.** The abstract (line 4) and the discussion after Corollary 4 (line 234) claim the results "match" SGM guarantees. However, the bounds include an extra \(L_f\) factor (e.g., \(L_f e^{-T}\), \(L_f \varepsilon_{\text{sc}}\), \(L_f L_s^{3/2} d^{1/2} h\) in Corollary 4). In comparable SGM bounds (Chen et al. 2022, 2023a; Lee et al. 2022b) the analogous constants are \(O(1)\) or depend only on the data distribution and dimension. While the *functional form* and *polynomial scaling* are similar, the extra \(L_f\) dependence means the bounds are not exactly "matching." The claim should be qualified.

3. **The TV-error guarantees come at the cost of the one-step advantage that motivates CMs.** The paper provides two routes to TV bounds: forward OU smoothing (Corollary 9) and Langevin correctors (Corollary 10). The smoothing route compares a *smoothed* generated distribution to the *original* data distribution — a non-standard guarantee. The Langevin route requires \(O(\sqrt{d}/\varepsilon)\) extra evaluation steps (line 335), effectively turning the one-step generator into a multi-step procedure. While the paper acknowledges this as a limitation (Section 4, line 347–348), it weakens a central motivation of CMs (fast one-step generation). A clearer discussion of whether this is a fundamental limitation or an artifact of the analysis would strengthen the paper.

### Trivial

4. **Notational issue in Corollary 8.** The bound for \(h\) reads \(R^3(R^6 \setminus d^3)\) (line 282); the "\(\setminus\)" symbol is a formatting error and should likely be "\(\vee\)" (denoting max). This makes the bound difficult to parse. (This is a presentation issue in the parsed text; the original submission may render correctly.)

## Nice-to-Haves

- **Proof sketches in the main text.** The theorems and corollaries are stated with only references to the appendix. Brief sketches of the key ideas (e.g., the Grönwall chain, how the consistency error enters the bound) would improve readability for the theory audience.
- **Explicit discussion of whether the Consistency Distillation / Consistency Training objectives actually minimize the \(L^2\) error assumed in Assumption 4.** The paper asserts this connection is "nature and realistic" (line 193), but a brief technical comment would be helpful.
- **A simpler illustrative case of the multistep schedule.** Showing that \(k \approx \log T\) steps suffice to match one-step quality (rather than the general recursion in Corollary 6) would make the practical message more immediate.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"Assumption 6 description is garbled (bound on h_1 illegible), figure missing."** The critic correctly notes these as *parsing artifacts* from PDF extraction. The original submission does not have these issues. Removed per parser-error rule.

2. **"Lack of proof sketches in the main text."** This was listed as a "Missing Parts" point by the harsh critic. It is a reasonable suggestion but not a weakness of the paper's technical content; moved to Nice-to-Haves above.

3. **"Figure 1 not described in the text."** The parsed text strips the figure but the caption is present (line 205); the paper references the figure in the text (line 206). Parser artifact.

## Novel Insights

The most interesting observation to emerge from the intersection of the two reviews is that the Lipschitz-on-\(f_\theta\) problem (Weakness 1) and the TV-guarantee limitation (Weakness 3) are connected: both stem from the fact that current CM theory fundamentally relies on ODE-based arguments (the probability flow ODE), inheriting their strengths (smooth trajectories, W\(_2\) guarantees) and weaknesses (inability to bound TV without extra steps). The multistep analysis (Corollary 6) is a genuine non-obvious insight — showing that the exponential contraction in the recursion removes the linear-in-\(T\) dependence is the kind of result that could guide practitioners in choosing step counts. However, the key open question — whether the exact consistency function inherits Lipschitz structure from the score regularity (Assumption 2) — is briefly raised by the authors as future work but deserves more prominence as the central bottleneck limiting the theory's impact.

## Suggestions

1. **Address the Lipschitz gap.** Either prove that \(f^{\text{ex}}\) is Lipschitz under Assumptions 1–2 (with constant depending on \(L_s\) and \(T\) via Grönwall on the true ODE), then relax Assumption 5 to an \(L^2\) approximation condition; or provide heuristic justification (e.g., that the exponential integrator's Jacobian can be bounded in terms of \(L_s\)).
2. **Qualify the "matching SGM" claim.** Replace "match" with "achieve the same functional form as" or "recover analogous polynomial dependence to," and explicitly note the extra \(L_f\) factor.
3. **Fix the \(\setminus\)→\(\vee\) typesetting error in Corollary 8** and clean up any similar formatting issues.
4. **Add brief proof sketches** (2–3 sentences per theorem) in the main text to help readers follow the argument structure without consulting the appendix.
