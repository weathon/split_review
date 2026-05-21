---
job_id: a6175985-451c-4eb1-b0f4-cacf0bf0cfe3
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: yBpzF8hp3J.pdf
paper: Missing Mass for Differentially Private Domain Discovery
main_score_norm: 0.8
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly in scope for ICLR, it studies differential privacy, learning-theoretic guarantees, and private data analysis algorithms with direct relevance to ML systems and private domain discovery.

## Minimum Quality
Pass ✅. The submission contains the expected scientific components, including abstract, introduction, related work, methodology, experiments, quantitative results, and concluding discussion; despite some technical and presentation issues, it clears the minimum bar for a full review rather than a desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find any hidden prompts, suspicious instructions to automated reviewers, or other manipulative content in the paper text provided.

# Expected Review Outcome:
## Summary
This paper studies differentially private domain discovery when the item universe is unknown, using missing mass as the main utility metric. The core result is that the Weighted Gaussian Mechanism (WGM), a simple thresholded noisy histogram method with contribution bounding, enjoys high-probability missing-mass guarantees, including an $\ell_1$ guarantee on Zipfian data and a distribution-free $\ell_\infty$ guarantee. The paper then uses WGM as a domain-discovery front end for unknown-domain private top-$k$ and $k$-hitting set, and reports experiments on six real datasets showing competitive or better performance than existing baselines.

## Strengths
1. **The paper addresses an important and under-theorized problem.**  
   Unknown-domain private analysis is a real bottleneck in practice, and the paper makes a persuasive case that set union, top-$k$, and $k$-hitting set can all be viewed through the lens of private domain discovery. Reframing set union utility in terms of missing mass in Section 2.3 is useful and more aligned with downstream utility than pure cardinality.

2. **The theoretical angle is substantive, not cosmetic.**  
   Theorems 3.3 and 3.6 give explicit utility bounds for WGM, and the lower bound in Theorem 3.5 provides nontrivial justification that the main dependence on $N$ and $\epsilon$ is not just an artifact of the analysis. I especially appreciate that the paper distinguishes the Zipfian $\ell_1$ result from the distribution-free $\ell_\infty$ result, rather than pretending one theorem covers all cases.

3. **The reduction-style use of WGM for downstream tasks is clean.**  
   Algorithm 2 is simple, but simplicity is a feature here. Using WGM as a precursor and then plugging in known-domain private algorithms is easy to understand and operationally appealing. The resulting guarantees in Theorems 4.3 and 4.5 are a meaningful extension of the set-union analysis.

4. **The experimental story is mostly coherent with the paper’s thesis.**  
   **Figure 1** is particularly helpful for the set union claim: across Reddit, Amazon Games, and Movie Reviews, WGM tracks the stronger policy-based baselines fairly closely as $\Delta_0$ varies, which supports the paper’s central practical message that a simple scalable mechanism can be competitive on missing mass even if prior work focused more on cardinality.  
   Likewise, **Figure 2** gives a fairly convincing empirical case for the top-$k$ pipeline, especially on the smaller datasets where the task is nontrivial. The widening gap as $k$ increases is consistent with the idea that domain discovery quality matters more when more items must be recovered.  
   **Figure 3** also conveys an interesting practical point: the WGM-based unknown-domain method can be competitive with, and sometimes even outperform, a known-domain private baseline, presumably because it shrinks the effective domain before the second-stage selection.

5. **The paper is generally well organized.**  
   The progression from set union to top-$k$ and then to $k$-hitting set is natural, and the definitions in Sections 2 and 4 are mostly clear. The abstract and introduction do a good job explaining why this matters.

6. **The dataset coverage is reasonably broad.**  
   Although the core evaluation is not enormous, the paper does test text, recommendation, and gaming-style datasets. **Table 1** usefully documents that these datasets span very different scales in numbers of users, items, and entries, which helps the reader interpret why some settings are “easy” for top-$k$ while others are more diagnostic.

## Weaknesses
1. **There appears to be a serious mathematical/presentation error in Corollary 3.4, and this is not a minor typo because it affects interpretability of the main bound.**  
   On **Page 5**, Corollary 3.4 states
   \[
   \mathrm{MM}(W,S)\leq\tilde{O}\left(\frac{C^{1/\epsilon}}{s-1}\left(\frac{\max_i |W_i|}{\epsilon N\sqrt{q^\star}}\right)^{(s-1)/\epsilon}\right).
   \]
   This does not look dimensionally or logically consistent with **Theorem 3.3** on **Page 4**, where the exponent is $(s-1)/s$, not something involving $1/\epsilon$. Substituting $\sigma,T=\tilde{\Theta}(1/\epsilon)$ into Theorem 3.3 should preserve the structural exponent $(s-1)/s$ and only inject $\epsilon$ into the multiplicative scale. As written, Corollary 3.4 suggests a much harsher and qualitatively different dependence on $\epsilon$, and also changes $C^{1/s}$ to $C^{1/\epsilon}$. This needs correction in the main text, because readers will naturally treat Corollary 3.4 as the ready-to-use takeaway.

2. **Several parameter choices and privacy-budget statements are underspecified in the main paper, and the hidden constants matter here.**  
   In **Section 4** on **Pages 5 to 7**, the paper says it spends half the privacy budget on WGM and half on the known-domain algorithm. But the theorem statements then specify
   \[
   \sigma=\Theta\!\left(\frac{1}{\epsilon}\sqrt{\log(1/\delta)}\right), \quad
   \lambda=\tilde{\Theta}\!\left(\frac{\sqrt{k}}{\epsilon}\right),
   \]
   while also claiming the composed algorithm is $(\epsilon,\delta)$-DP. Presumably the hidden constants absorb the factor-of-two allocation, but the paper should not make readers reverse-engineer this. For privacy-sensitive algorithms, “the constants are hidden in $\Theta(\cdot)$” is not very satisfying. This is especially relevant because the threshold $T$ in **Theorem 3.2** depends on the exact choice of $\sigma$, and the practical performance of WGM can be quite sensitive to threshold calibration.

3. **The empirical evaluation is good but not fully convincing against the strongest available baselines discussed in the paper itself.**  
   In **Section 1.1** and **Page 2**, the paper explicitly discusses Chen et al. (2025) as improving over WGM with adaptive weighting. Yet in **Section 5.1** the experiments compare only against Policy Gaussian and Policy Greedy. If the paper’s headline is “simple WGM has strong guarantees and competitive practice,” then omitting a directly relevant stronger weighting-based baseline that the paper itself cites weakens the empirical positioning. Maybe there are good reasons, but the authors should say so clearly in the main paper.

4. **The experiments mostly show averages, but uncertainty quantification is inconsistent and sometimes absent where it matters.**  
   In **Figure 1** and **Figure 2**, the paper reports average performance over 5 trials, but there are no error bars. In contrast, **Figure 3** includes standard errors. This asymmetry is unfortunate because the top-$k$ curves in Figure 2 are used to support a fairly strong comparative claim, namely that the proposed method “consistently obtains smaller top-$k$ MM than all limited-domain baselines.” With only 5 trials and no uncertainty shown, it is hard to judge how robust those differences are, especially when multiple baseline variants are close on some ranges of $k$.

5. **The theory-experiment connection is weaker than it could be.**  
   The theoretical story in Section 3 is driven by Zipf behavior, $s>1$, and the role of contribution bounds via $q^\star$. But the main experiments do not really test or visualize whether the observed trends follow the theorem’s predictions. For instance, **Figure 1** varies $\Delta_0$, which is exactly the quantity that should interact with the subsampling term in Theorem 3.3, yet the paper does not analyze whether the empirical curves track the predicted dependence on $\Delta_0$ or on user set sizes. The paper mentions that the datasets are Zipfian, and **Table 1** provides scale statistics, but the main text stops short of using these to validate the theory in a more targeted way.

6. **Some theorem statements are a bit too coarse for practical interpretation.**  
   **Theorem 4.3** on **Page 7** gives
   \[
   \mathrm{MM}^k(W,S)\leq \tilde{O}\left(\frac{k}{N}\left(\frac{\max_i |W_i|}{\epsilon\sqrt{q^\star}}+\frac{\sqrt{k}\log(M)}{\epsilon}\right)\right).
   \]
   This is fine as an upper bound, but the reader is left guessing which term dominates in realistic regimes, and how this compares to known-domain top-$k$ algorithms when the discovered domain is already small. The discussion after the theorem is brief and mostly lower-bound oriented. A sharper interpretation of the two terms would help, especially since the first comes from domain discovery and the second from the second-stage peeling mechanism.

7. **The exposition contains enough notation slips and local errors to reduce confidence, even if the overall ideas are sound.**  
   Examples include the inconsistent use of $p^\star$ versus $q^\star$ across the proofs, apparent typographical issues in Appendix derivations, and wording slips in the main text. More importantly for the main paper, there is at least one notable notation mistake on **Page 3**, where the hardness discussion writes
   \[
   \mathbb{E}_{S\sim \mathcal{A}(W)}[\mathrm{MM}(\mathcal{A},S)] \ge 1-\delta,
   \]
   which should presumably be $\mathrm{MM}(W,S)$, not $\mathrm{MM}(\mathcal{A},S)$. Individually these are fixable, but collectively they create friction in a paper whose main value is theoretical clarity.

8. **The top-$k$ and $k$-hitting-set experimental comparisons are somewhat asymmetric.**  
   For top-$k$, the paper compares to the limited-domain method of Durfee and Rogers with several hyperparameter settings, which is reasonable. For $k$-hitting set, however, the paper notes there is no unknown-domain private baseline and therefore compares against a non-private greedy method and a known-domain private method that assumes public knowledge of $\bigcup_i W_i$. This is acceptable as a sanity check, but it means the empirical claim in **Section 5.3** should be framed more cautiously. The method may well be strong, but the comparison is not apples-to-apples.

9. **The paper could do more to justify the practical choice of $\Delta_0$.**  
   This parameter is central in both the mechanism and the bounds, yet for top-$k$ and $k$-hitting set the experiments fix $\Delta_0=100$ in **Figures 2 and 3** with limited discussion of why that value is appropriate across all three small datasets. Since the paper repeatedly emphasizes the tradeoff introduced by subsampling, a short sensitivity study or a principled heuristic for setting $\Delta_0$ would make the method more usable.

## Questions
1. **Can the authors correct Corollary 3.4 in the main text?**  
   As written, the dependence on $\epsilon$ and $C$ seems inconsistent with Theorem 3.3. Please provide the corrected expression and confirm whether this is only a typographical issue or whether any downstream statements rely on the displayed formula.

2. **Please clarify the exact privacy-budget split and constants used in Sections 3 and 4.**  
   When the paper says WGM uses half the budget and the second-stage mechanism uses the other half, what are the exact parameter settings for $\sigma$, $T$, and $\lambda$ in terms of $(\epsilon/2,\delta/2)$? A precise statement would improve both reproducibility and confidence in the theorem calibration.

3. **Why is Chen et al. (2025) not included as an empirical baseline for set union?**  
   Since the related-work section explicitly presents it as a stronger variant of WGM, an explanation in the rebuttal would help. If implementation or scalability constraints prevented inclusion, please say so directly.

4. **Can the authors provide uncertainty estimates for Figures 1 and 2, not just Figure 3?**  
   Even simple standard errors or confidence intervals over the 5 trials would substantially strengthen the empirical claims.

5. **How sensitive are the top-$k$ and $k$-hitting set results to $\Delta_0$?**  
   The main paper fixes $\Delta_0=100$ in Figures 2 and 3. A brief explanation of how this was chosen, or whether nearby values behave similarly, would increase confidence that the improvements are not parameter-specific.

6. **Can the authors better connect the theory to the observed dataset structure?**  
   In particular, a short discussion relating dataset characteristics such as user set sizes and frequency concentration to the theorem terms, especially the $\max_i |W_i|/\sqrt{q^\star}$ dependence, would make the paper more informative.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
The work studies differentially private mechanisms and evaluates them on existing datasets. I did not identify specific ethics red flags in the main paper that would require additional ethics review.

## Soundness Rating
3: good. The main technical approach is solid and the claims are mostly supported, but the error in Corollary 3.4 and several underspecified constants/notation issues prevent an excellent soundness score.

## Presentation Rating
3: good. The paper is generally well structured and readable, but the exposition has enough notation slips and missing clarifications that it falls short of excellent.

## Contribution Rating
4: excellent. The paper makes a strong contribution on an important privacy problem by providing concrete utility guarantees for a simple practical mechanism and extending them to unknown-domain top-$k$ and $k$-hitting set.

## Overall Rating
8: Accept, good paper (poster). This is a strong and useful paper with meaningful theory and a credible empirical story. I do have real concerns about a mathematical error in Corollary 3.4, missing experimental comparisons, and some under-specification of parameter choices, but these issues look fixable and do not outweigh the paper’s overall value.

## Reviewer Confidence
4: confident. I am confident in the assessment and checked the main technical flow carefully, though some lower-level derivation details would still benefit from author clarification.