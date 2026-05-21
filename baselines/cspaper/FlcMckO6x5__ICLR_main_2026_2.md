---
job_id: 5320cafd-d090-4332-9aea-b77bff40905c
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: FlcMckO6x5.pdf
paper: Separable Neural Networks: Approximation Theory, NTK Regime, and Preconditioned Gradient Descent
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, combining learning theory, kernel/NTK analysis, optimization, and applications to INRs and PINNs.

## Minimum Quality
Pass ✅. The paper contains the expected core components, including abstract, introduction, technical development, experiments with quantitative/qualitative results, and conclusions; while I found substantial issues in rigor and exposition, they do not rise to the level of an immediate desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find any hidden prompts, suspicious instructions to automated reviewers, or other manipulative content in the provided paper text.

# Expected Review Outcome:
## Summary
This paper studies separable neural networks (SepNNs), focusing on three aspects: approximation theory, NTK behavior, and optimization. The authors prove a universal approximation result for CP, TT, and Tucker-style separable architectures, derive NTK limits for CP SepNNs in infinite-width/infinite-rank and infinite-width/fixed-rank regimes, and propose a separable preconditioned gradient descent method, SepPGD, aimed at reducing spectral bias while preserving the computational advantages of separable models on grid-structured data.

## Strengths
The paper tackles a timely and practically relevant model family. SepNNs are increasingly used in coordinate-based modeling, especially INRs and PINNs, and a consolidated treatment of their approximation properties, NTK regime, and optimization behavior is useful for the community.

The approximation result in **Theorem 1** is a meaningful contribution. While the high-level conclusion, universal approximation for separable architectures with sufficient rank, is not shocking, the paper gives a unified treatment across **CP, TT, and Tucker** constructions rather than only the bivariate CP case. The proof strategy via Stone-Weierstrass plus univariate neural approximation is conceptually natural and, despite presentation issues, it gives a clean lens on why these architectures are expressive.

The NTK decomposition in **Lemma 1**, especially the form in **Equation (4)**, is one of the more useful technical parts of the paper. It makes explicit how the SepNN NTK decomposes into factor-level NTKs weighted by products of the other factors. This is the right object to analyze if one wants to reason about training dynamics in overparameterized separable models.

I appreciated that the paper does not stop at asymptotic theory and includes empirical checks of the NTK story. In **Figure 1(a,b,c)**, the qualitative trends are aligned with the intended claims: fixed rank does not appear to wash out randomness with width alone, while joint increase of width and rank stabilizes the NTK and makes it more nearly constant through training. **Figure 1(d)** is also helpful in visually motivating the spectral-bias discussion by showing a sharply decaying eigen-spectrum.

The proposed optimization angle is interesting. The core motivation behind **SepPGD**, namely replacing a huge preconditioner over \(n^D\) grid samples by factor-wise objects over \(n\)-sized axes, is sensible and matches the structural advantage of separable models. Even if I am not fully convinced by the current theory, the direction is worthwhile.

The empirical section is broad. The paper includes KRR, INR image fitting, 3D surface representation, and PINN experiments. **Figure 2** is particularly useful because it reports convergence against execution time rather than iteration count, which is the correct axis if the main claim is computational efficiency. In both **Figure 2(a)** and **Figure 2(b)**, SepPGD appears to improve wall-clock convergence over the SepNN baseline.

The qualitative examples in **Figure 3** and **Figure 4** are visually consistent with the narrative. In **Figure 3**, the SepPGD reconstructions retain more image detail and slightly better 3D surface quality than plain SepNN at the same iteration budget. In **Figure 4**, the separable PINN with SepPGD looks closer to the ground truth than the unpreconditioned separable PINN.

## Weaknesses
My main concern is that the paper overstates what is actually proved about SepPGD. The abstract and introduction repeatedly claim that SepPGD “provably adjusts” the NTK spectrum and alleviates spectral bias. However, in the main paper this is not established with a theorem of the same caliber as the NTK results. The core formal result for the optimizer is **Lemma 2** on **Page 9**, and that lemma only shows equivalence, in the **bivariate case \(D=2\)**, to a classical NTK-based PGD with a specific Kronecker-structured preconditioner. The subsequent spectral-improvement argument is explicitly heuristic: the paper says “Suppose that \(\hat K\) is close to the true NTK matrix \(K\)” and “We can ultimately show that \(K\hat S\) has better spectrum than \(K\),” but this is not actually turned into a theorem with assumptions, bounds, or proof in the main paper. That gap matters because the optimizer is one of the headline contributions.

Relatedly, the jump from the bivariate analysis to the general multivariate algorithm is too loose. The method is defined for general \(D\) in **Definition 1**, but the main theoretical bridge to classical PGD is only shown for \(D=2\) in **Lemma 2**. On **Page 9**, the paper says the result “is believed” to extend readily to \(D>2\). That is not enough for a paper whose central claims are theoretical. If the general-\(D\) case is essential to the method and to the complexity claims, it should either be proved in the main paper or the claims should be narrowed accordingly.

There are several mathematical and notational inconsistencies that make careful verification harder than it should be. A few examples:
1. In the definition of the separable function class \(\mathcal A\) on **Page 4**, the function is written as \(g(x_1,\cdots,x_N)\) although the paper uses \(D\) dimensions elsewhere.
2. In **Corollary 1** on **Page 6**, the expression for \(V_d(\mathbf x,\mathbf x')\) contains an index \(r'\) that is never defined:
   \[
   V_d(\mathbf x,\mathbf x')=\frac{1}{R}\sum_{r=1}^R \prod_{d'\neq d} (f_{\Theta_{d'}}(x_{d'}))_r (f_{\Theta_{d'}}(x'_{d'}))_{r'}.
   \]
   This should presumably use the same \(r\), but as written it is incorrect.
3. In **Theorem 1** on **Page 4**, the Tucker part ends with a malformed sentence, “\(R_{d+1}\times\cdots\times R_{d-1}\times R_{d+1}\times\cdots\times R_D\) denotes the mode-\(d\) specific product...”, which appears to be a corrupted statement.
4. In the proof sketch of **Theorem 1**, the paper says the approximation error is bounded via the “Cauchy-Schwarz inequality,” but the displayed inequality is actually a product-difference telescoping bound, not Cauchy-Schwarz. This is not a fatal issue, but it reflects a pattern of imprecise exposition around the math.

The complexity discussion is sloppy to the point of being misleading in places. **Table 1** on **Page 8** is the most obvious problem. The row for “Modified NTK spectrum (Geifman et al., 2024)” lists complexity \(O(nD)\) for \(n^D\) training samples, even though the surrounding text in **Section 4** says the classical NTK-based preconditioner scales as \(O(n^D)\) to apply on \(n^D\)-dimensional residuals. Likewise, the row for the mini-batch version says \(O(nD/p)\), whereas the text above says \(O(n^D/p)\). These are not cosmetic typos because the paper’s efficiency story is a major selling point. There is also a notation mismatch in **Remark 4**: it says SepPGD scales as \(O(nD)\) by multiplying \(D\) \(n\times n\) preconditioning matrices \(\{M_d\}\), but **Equation (8)** defines \(M_d\in\mathbb R^{R\times n}\), not \(n\times n\). Presumably the intended \(n\times n\) matrices are \(\{S_d\}\). Again, this is exactly the part that should be airtight.

The experimental evidence is promising but not strong enough to fully support the broad claims. The main paper relies heavily on convergence curves and qualitative images, while many of the quantitative ablations are pushed to the appendix. For example, the sensitivity to \(k\), rank, width, update frequency, and noise robustness all appear only in appendix tables. Given that SepPGD introduces nontrivial design choices, at least one main-paper ablation would have been appropriate. Also, many comparisons to the classical NTK-based preconditioner are limited to small/downsampled problems because of memory issues. I understand the practical reason, but it weakens the claim that SepPGD is decisively superior on the intended large-scale settings.

The presentation around the figures is weaker than it could be. **Figure 1** is useful, but the paper mainly gives qualitative interpretations without quantifying rates or connecting the observed trends back to the specific asymptotic statements. For instance, **Figure 1(b)** is supposed to support convergence to a deterministic kernel as both width and rank increase, but the paper does not discuss how sensitive this is to activation choice, data distribution, or finite-rank effects. Similarly, **Figure 2** presents time-based convergence, which is the right metric, but the lack of accompanying summary statistics in the main text makes it hard to judge robustness. A results table summarizing final metrics and runtime tradeoffs would have helped substantially.

The claims about “generalization not being affected” are too casual for the evidence provided. On **Page 10**, the paper states that SepPGD accelerates convergence “without affecting the model’s generalization (in most cases improving generalization),” but this is supported mainly by appendix qualitative inpainting examples and a few task-specific observations. Since preconditioning changes optimization trajectories and can amplify high frequencies, this is exactly the sort of claim that needs more careful empirical qualification.

The theoretical scope is narrower than the headline presentation suggests. The universal approximation theorem covers CP, TT, and Tucker SepNNs, but the NTK and optimization analysis are essentially only for **CP SepNNs**. That is acceptable if framed clearly, but the paper often speaks broadly about “SepNNs” as a whole. For a paper emphasizing a unified theory of separable neural networks, the disconnect between approximation theory on three architectures and NTK/optimization theory on one architecture is noticeable.

Finally, the paper has many writing and bibliographic issues that reduce confidence in the level of polish. There are malformed references, duplicated or corrupted author listings, inconsistent citation years, and several grammatical mistakes. These do not by themselves determine acceptance, but in a theory-heavy paper they matter because they make the work feel less carefully checked than it should be.

## Questions
1. The paper repeatedly claims that SepPGD “provably adjusts” the NTK spectrum and alleviates spectral bias. Can the authors point to a precise theorem in the main paper that establishes this for the proposed method in the general \(D\)-dimensional case, not only the \(D=2\) equivalence in **Lemma 2**? If such a theorem is missing, I strongly suggest toning down the claim.

2. Can the authors clarify the complexity statements in **Table 1** and **Remark 4**? As written, the table appears inconsistent with the surrounding text, and \(M_d\) is not an \(n\times n\) preconditioner according to **Equation (8)**. A corrected and carefully dimension-checked version would increase my confidence.

3. In **Corollary 1**, is the definition of \(V_d(\mathbf x,\mathbf x')\) intended to use the same output index \(r\) on both factors, rather than \(r\) and \(r'\)? Please correct the expression and state whether this affects any downstream claims.

4. For **Figure 1**, can the authors provide more quantitative detail on how the reported NTK differences are measured? For example, what matrix norm is used, and how sensitive are the trends to dataset choice or activation function? Right now the figure is suggestive, but a bit too qualitative.

5. The method is presented as broadly useful for INRs and PINNs. Could the authors include, at least in rebuttal, one compact quantitative table in the style of final error plus runtime for the main tasks, rather than only curves and qualitative images? This would help evaluate the practical tradeoff more cleanly.

6. For the claim that SepPGD does not hurt generalization, what exact evidence should I use from the main paper? If this is meant as a claim beyond anecdotal examples, I would like to see a clearer evaluation protocol and summary metric.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No ethics concerns identified from the main paper.

## Soundness Rating
2: fair. The paper contains several technically interesting ideas and some plausible theory, but key claims around SepPGD’s guarantees are not fully supported in the main paper, and there are enough mathematical and complexity inconsistencies to limit confidence.

## Presentation Rating
2: fair. The high-level structure is understandable, but notation errors, dimension mismatches, malformed statements, and an especially problematic complexity table hurt clarity and make the technical parts harder to trust.

## Contribution Rating
2: fair. The topic is important and the combination of approximation theory, NTK analysis, and separable preconditioning is potentially valuable, but the optimizer contribution is not established as cleanly as the paper claims, and the empirical evidence is not yet strong enough to fully compensate.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The paper has real ideas and some useful results, especially the approximation theorem and the NTK decomposition, but the SepPGD contribution is oversold relative to what is actually proved, and the technical/presentation issues around equations and complexity claims are too substantial for me to support acceptance in its current form.

## Reviewer Confidence
4: confident. I am comfortable assessing the learning-theory/NTK/optimization aspects and checked the main equations and claims with care, though some details would benefit from clarification by the authors.