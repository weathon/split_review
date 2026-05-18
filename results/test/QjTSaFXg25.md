Now I have all the information I need. Let me write the consolidated review.

## Summary

This paper investigates the theoretical foundations of the reparameterization trick in prefix-tuning. The authors observe that reparameterization encodes a *shared structure* between prefix key and value vectors (both are functions of the same latent prompt), and they connect prefix-tuning to a mixture-of-experts (MoE) framework. Their theoretical analysis compares convergence rates of prompt estimation under shared vs. non-shared structures, claiming that shared structure yields parametric or near-parametric rates of \(O_P(\sqrt{\log n/n})\) while non-shared alternatives can degrade to \(O(1/\log n)\). Empirically, they show across vision (FGVC, VTAB-1K) and language (E2E, WebNLG, XSUM) benchmarks that Deep-share (with reparameterization) substantially outperforms No-share (without).

## Strengths

- **Consistent large-margin empirical gains across vision and language.** The empirical results are clear and striking: Deep-share consistently and substantially outperforms No-share across most tasks (e.g., +16.8% on Stanford Cars, Table 1; +5.76 ROUGE-1 on XSUM, Table 2). These results are reported over five independent runs and across multiple backbones (ViT-B/16, GPT2, BART), making a convincing case that the reparameterization matters in practice. *Supported by Tables 1–2 and Figure 2 in the paper.*

- **Principled connection to mixture-of-experts framework.** The paper formally connects prefix-tuning to MoE models via the work of Le et al. (2024), showing that prefix key vectors correspond to parameters in score functions and value vectors to expert parameters (Section 2.2, Equation 6). This framing provides a clean theoretical language for analyzing prompt estimation and is a genuine conceptual contribution. *Supported by Section 2.2 and Figure 1.*

- **Identification of shared structure in prompt-tuning.** The paper observes that prompt-tuning (K=V=prompt) is a special case of the shared structure, linking it theoretically to prefix-tuning's reparameterization (Section 3). This insight extends the paper's contribution beyond prefix-tuning alone and offers partial theoretical grounding for why prompt-tuning works. *Supported by Section 3, paragraphs "Shared structure in prompt-tuning."*

## Weaknesses

### Fatal
None.

### Major

- **The theoretical comparison between shared and non-shared structures is not valid as presented.** This is the paper's central theoretical claim, and it has two problems:

  **Problem (a): Lower bound vs. upper bound, different loss functions.** Theorem 1 provides a minimax *lower bound* of \(\gtrsim n^{-1/2}\) on loss \(\mathcal{D}_{1,r}\) for the non-shared case. Theorems 2 and 3 provide *upper bounds* of \(O_P(\sqrt{\log n/n})\) on the different losses \(\mathcal{D}_2\) and \(\mathcal{D}_3\) for the shared case. Comparing a lower bound for one loss to an upper bound for a different loss does not constitute a valid rate comparison. A proper comparison would require either (i) an upper bound for the non-shared case under the same model to establish its actual (not just worst-case) rate, or (ii) a matching minimax lower bound for the shared case to show the upper bound is tight. Without this, the paper's claim that shared structure "substantially improves sample efficiency" relative to non-shared is not rigorously supported by the theory.

  **Problem (b): The \(O(1/\log n)\) claim is not derived from Theorem 1.** The paper states that non-shared prompt estimation rates "could be as significantly slow as \(O(1/\log(n))\)." This does not follow from Theorem 1: the lower bound of \(n^{-1/2}\) on the *sum* of bias and prompt terms does not force prompt-error rates to be as slow as \(1/\log n\). The bias term in the Voronoi loss could dominate the lower bound, leaving the prompt terms to converge arbitrarily faster. The \(1/\log n\) figure appears speculative.

  These issues together mean the paper's central theoretical contribution — a rigorous proof that reparameterization accelerates convergence — is not yet established. *Supported by Theorem 1 (line 450), the interpretation on line 454, and Theorems 2–3 (lines 487–493, 534–539). The O(1/log n) claim is on line 454.*

- **The paper overstates its theoretical conclusions relative to what the analysis actually supports.** The abstract and introduction claim that reparameterization "is grounded in deep theoretical foundations" and that the theory shows "faster convergence rates compared to non-shared alternatives." Given the issues above, these claims go beyond what the theoretical results can currently justify. The empirical finding that reparameterization helps in practice is valuable on its own, but the theory-as-explanation is the paper's claimed novelty, and that part is not yet convincing.

### Minor

- **The experimental comparison between Deep-share and No-share does not control for parameter count or model capacity.** Deep-share uses a smaller latent prompt space + an MLP, while No-share learns K and V independently. These differ not only in whether the structure is shared, but also in total parameter count, optimization landscape, and the implicit regularization from the bottleneck. The Simple-share baseline partially addresses this (K=V has a different structure with fewer parameters but still helps), but an ablation that matches total parameter count between shared and non-shared conditions would strengthen the attribution of the performance gap to shared structure per se.

- **The one-layer neural network setting (Section 4.2.2) relies on assumptions (A.1) and (A.2) that, while standard in MoE theory, are non-trivial and not validated for the MLP architectures actually used in prefix-tuning practice.** The paper provides tanh as an example satisfying these assumptions, but the reparameterization MLP \(g_\theta\) in real prefix-tuning can have multiple layers and different nonlinearities. The gap between the simplified setting and actual practice is acknowledged (Section 4.2.2), but its implications for the applicability of the theoretical rates are not discussed.

### Trivial
None.

## Nice-to-Haves

- A matching upper bound for the non-shared case under the same regression model would transform the theoretical comparison from suggestive to rigorous.
- Reporting standard deviations alongside the mean accuracies in the main tables would improve reproducibility assessment.
- A brief discussion of hyperparameter tuning for the compared conditions (Deep-share vs. No-share) would address the concern that No-share might simply be poorly tuned.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Strength Finder point 1 ("Theoretical proof of accelerated convergence")** — Removed because it conflicts with the verified weakness that the theoretical comparison is flawed. The paper presents a framework and attempt, but a valid proof of accelerated convergence is not yet established.

- **Harsh critic point 2's sub-claim about Theorem 3 only bounding W₁p/W₂p, not actual prompts** — Partially removed/weakened because the paper explicitly addresses this: Lipschitz continuity of activation functions (lines 541–545) transfers the rates to the actual prompt vectors K and V. The critic overlooked this passage.

- **Harsh critic's point about the paper not discussing how results extrapolate to multi-head attention** — This is a scope demand beyond what the paper claims to do; the paper explicitly states it simplifies to a single head and row (line 409). Such simplification is standard in theoretical work.

## Novel Insights

None beyond the paper's own contributions. The reviews surface no fundamentally new perspective on the work that the paper itself does not already articulate.

## Suggestions

1. **Fix the theoretical comparison.** The paper should either provide an upper bound for the non-shared case under the same regression model (showing it indeed converges more slowly) or a matching lower bound for the shared case (showing the obtained upper bound is optimal). Without this, the theory should be repositioned as establishing a *framework* for analysis and deriving rates for the shared case, with the comparison to the non-shared case presented as a conjecture or empirical observation rather than a proven result.

2. **Remove or carefully qualify the \(O(1/\log n)\) rate.** This claim cannot be derived from Theorem 1 and should either be derived from a proper analysis or removed.

3. **Control for parameter count in ablation.** Adding a baseline where K and V are generated from separate (non-shared) latent vectors through an MLP of matched capacity would isolate the effect of sharing from the regularization effect of the bottleneck.

## Score and Decision

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>