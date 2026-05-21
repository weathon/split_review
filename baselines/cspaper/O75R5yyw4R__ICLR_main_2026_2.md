---
job_id: 76c81b31-e539-407e-9f65-45caed80b95c
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: O75R5yyw4R.pdf
paper: Effective Test-Time Scaling of Discrete Diffusion through Iterative Refinement
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, focusing on generative models, discrete diffusion, MCMC-based test-time sampling, and alignment/safety-oriented generation across language and image domains.

## Minimum Quality
Pass ✅. The submission contains the expected scientific components, including abstract, introduction, related work, methodology, experiments, quantitative/qualitative results, and conclusion. While I found several serious technical and presentation issues that affect the rating, they do not rise to the level of an immediate desk rejection based on the provided text alone.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, reviewer-targeted instructions, or other manipulative content in the provided paper text.

# Expected Review Outcome:
## Summary
This paper proposes IterRef, a test-time scaling method for discrete diffusion models that performs iterative reward-guided refinement of intermediate states via a Multiple-Try Metropolis (MTM) procedure. The method uses a noising-denoising transition kernel to revisit and improve intermediate samples rather than only guiding the next step, and the paper claims convergence to a reward-aligned target distribution under stated assumptions. Experiments on text generation with MDLM and LLaDA-8B, and image generation with MaskGIT, show improved reward-guided generation compared with several inference-time baselines across multiple reward functions and compute budgets.

## Strengths
The paper tackles a meaningful problem. Test-time scaling for discrete diffusion is much less developed than for autoregressive models or continuous diffusion, and the paper is trying to address a genuine limitation of prior one-pass particle methods, namely the inability to correct poor intermediate states once sampling has moved on.

The high-level idea is intuitive and, at least conceptually, well matched to discrete diffusion. Revisiting an intermediate state through a noising-denoising proposal mechanism is a natural way to recover some of the correction ability that discrete samplers otherwise lack. I found the conceptual contrast in **Figure 1(a)** useful: it clearly conveys the paper’s central claim that IS/SMC-style approaches move forward along a single denoising frontier, whereas IterRef performs local refinement around the current state. Even though the theory and implementation details have issues, the figure does a good job of communicating what the authors believe is structurally different about their method.

The empirical coverage is broader than many papers in this area. The method is tested on two language backbones and one image backbone, and across several rewards, including Toxicity, Sentiment, CoLA, Perplexity, and CLIPScore. That breadth makes the paper more relevant to the ICLR audience than a single-task result would.

Some of the empirical trends are promising. In **Figure 2(a)** and **Figure 2(b)**, IterRef generally improves faster than the baselines as compute increases, particularly on Toxicity and Perplexity. Even without exact numeric tables for the language plots, the trend that IterRef is often better at low to moderate budgets is visible. Likewise, **Table 1** shows consistent gains for MaskGIT under CLIPScore guidance at every budget above 1, for example \(33.7\) vs \(32.1\) at cost 2 and \(35.8\) vs \(34.8\) for the strongest baseline at cost 16. This is a clean and easy-to-read result table.

The ablation studying iterations versus particles is directionally informative. **Figure 4** and **Table 3** both support the claim that spending compute on iterative refinement can be more effective than merely increasing the number of proposals. In **Table 3**, moving from \((k,N)=(1,32)\) to \((8,4)\) substantially improves all three rewards on LLaDA, which is consistent with the paper’s main narrative that iteration matters more than breadth alone.

The paper also includes qualitative examples. **Figure 3** suggests that the image samples from IterRef are often more semantically aligned and visually coherent than those from the baselines, at least in the selected examples. **Figure 5(b)** is also useful in illustrating the detoxification case study, though it raises separate questions about semantic preservation.

## Weaknesses
I have substantial concerns about the technical correctness and internal consistency of the MTM formulation as presented in the main paper. These are not cosmetic issues, because the claimed theoretical guarantee is one of the headline contributions.

1. **Equation 3 and the MTM weight derivation appear mathematically inconsistent, and in one place plainly incorrect.**  
   On **Page 4**, the paper states that with the proposed \(K\) and \(\lambda\), the importance weights are \(w_n = N^{-1}\) and the acceptance probability is
   \[
   \beta=\min(1,\exp((r(x_t')-r(x_t})/\alpha)).
   \]
   Setting aside the parenthesis typo, the appendix derivation in **D.2, Page 22** does not support the claim \(w_n = 1/N\). The derivation first simplifies the weights to
   \[
   w_n = \frac{\exp(r(x_t^{\prime(n)})/\alpha)}{\sum_j \exp(r(x_t^{\prime(j)})/\alpha)},
   \]
   and then suddenly asserts this equals \(1/N\). That only holds if all rewards are equal, which is obviously not the general case. This is a direct contradiction inside the derivation itself, not a matter of interpretation. Since candidate selection in MTM depends critically on these weights, this undermines both Algorithm 1 and Algorithm 2 as written.

2. **The sign of the acceptance ratio is inconsistent between the main text and the appendix, and one version appears to prefer lower-reward moves.**  
   In the main text on **Page 4**, Equation 3 gives an acceptance probability proportional to \(\exp((r(x_t')-r(x_t))/\alpha)\), which would favor higher-reward proposals. But in **Appendix D.2, Page 22**, the acceptance ratio is derived as
   \[
   \beta=\min\left(1,\exp\left(\frac{r(x_t)-r(x_t')}{\alpha}\right)\right),
   \]
   which does the opposite. These two formulas cannot both be correct. For a reward-guided sampler, the sign matters enormously. This is not a typo-level concern because it changes the direction of the Markov chain bias.

3. **Algorithm 1 is not written correctly enough to verify the MTM procedure.**  
   On **Page 4**, the selection step samples \(x_t'\) from a multinomial over candidates, but the formula uses \(\lambda(x_t',x_t)\) inside the probability mass for every candidate rather than \(\lambda(x_t^{\prime(n)},x_t)\). Similarly, the acceptance numerator sums over \(i\) but repeatedly uses the same \(p^*(x_t')K(x_t',x_t)\lambda(x_t',x_t)\) term rather than candidate-specific terms. These expressions are not just sloppy notation; they obscure what is actually being summed and make the algorithm impossible to check rigorously from the main paper.

4. **The convergence claim in Proposition 1 depends on assumptions that are very strong and not justified for the actual models used.**  
   **Proposition 1 on Page 5** assumes that \(q\) and \(p_\theta\) form a reversible Markov kernel. That is a major assumption. For learned reverse kernels in large discrete diffusion models such as MDLM or LLaDA-8B, reversibility is not something I would take for granted. The paper does not explain when this assumption is expected to hold, whether it approximately holds for the evaluated models, or how violations affect the claimed convergence. A theorem whose key assumption is both strong and disconnected from the practical models only weakly supports the empirical method.

5. **The theoretical target and balancing function depend on quantities that are not clearly tractable, and the paper sidesteps this gap too quickly.**  
   The balancing function in **Equation 2 on Page 4** is
   \[
   \lambda(x_t,x_t')=\frac{1}{p(x_t)K(x_t,x_t')\exp((r(x_t)+r(x_t'))/\alpha)}.
   \]
   This involves \(p(x_t)\), the intermediate marginal under the diffusion process, and the proposal kernel \(K\), which itself sums over all \(x_s \in \mathcal{X}_s\). In realistic discrete spaces, neither quantity is obviously tractable. The paper then says in **Section 3.3, Page 5** that with the chosen balancing function, backward resampling can be eliminated “while still preserving the theoretical guarantees.” That is a very strong claim, but the main paper gives no derivation for why the practical implementation, which differs from textbook MTM, still leaves the same target invariant. Right now the theory appears to justify one chain, while the implementation uses another.

6. **The practical speed/computation story is internally inconsistent.**  
   In **Section 3.3, Page 6**, the authors argue that aggregating reward-model calls and generative-model calls into a single NFE can be misleading, especially because in LLaDA-8B the generative calls dominate. However, in **Section 4.1, Page 6**, the main experiments explicitly compare methods under equal NFE while “treat[ing] the reward model and the generative model on equal footing.” Those two statements are in tension. If the paper itself argues that equal-weight NFEs obscure meaningful differences, then the main headline scaling comparisons in **Figure 2** become harder to interpret. This matters because a central claim of the paper is faster scaling under low compute budgets.

7. **The empirical evaluation is promising but still thinner than the claims suggest.**  
   The language experiments use only 15 prompts with 20 samples each, as stated in **Section 4.1, Page 6**. For broad claims about scaling behavior across tasks and models, this is a fairly small evaluation. The main paper provides curves in **Figure 2**, but not the underlying numerical values, confidence intervals, or statistical tests there. The appendix later gives standard deviations, but the decision should not depend on supplementary material. Since the paper repeatedly uses phrases like “consistently demonstrates” and “far surpassing,” the main paper should carry stronger uncertainty reporting.

8. **Several baseline choices and exclusions need better justification.**  
   In **Appendix B.4, Page 17**, the paper says PG was reimplemented but excluded because results deviated significantly from the literature. That is understandable operationally, but from a reviewer perspective it weakens the empirical positioning, because the paper is making strong comparative claims in a rapidly moving area while excluding at least one relevant baseline. In the main paper, the baseline section on **Page 6** also states that hyperparameters are “favorably configured” following original papers, but there is limited evidence that the methods were retuned appropriately for the current tasks and cost accounting.

9. **The presentation has many writing and notation issues that materially hurt confidence.**  
   There are numerous typos and malformed statements, for example “Intermediate rewards \(r(x_t)\) can approximate” on **Page 4**, “The Multiple-Try Metropolis” as a dangling subsection header on **Page 4**, inconsistent notation around \(x_t^{\mathrm{can}}\) vs \(x_t'\) in **Algorithm 2, Page 5**, and several grammatical problems throughout Sections 3 and 4. Normally I would not dwell on copyediting, but here the notation errors directly affect the core method, making it genuinely hard to verify what algorithm was run and what theorem was proved.

10. **Some empirical claims drawn from figures are stronger than what the figures cleanly support.**  
   **Figure 1(b)** advertises up to \(8\times\) faster scaling for safety alignment on LLaDA-8B, but the axes and exact numbers are not easy to read from the figure alone, and the paper’s compute metric has the NFE ambiguity discussed above. Likewise, in **Figure 5(a)**, the detoxification improvement is plausible, but the case study relies on only 300 generations total from the 15 most toxic prompts. This is useful as a case study, not yet conclusive enough to support strong safety claims.

11. **The paper’s differentiation from nearby iterative refinement work could be sharper.**  
   The related work section discusses remasking, search, and particle-based methods, but the paper’s central idea, reward-guided iterative refinement via noising-denoising transitions, is close in spirit to other iterative refinement approaches in diffusion. The current discussion in **Sections 1 and 5** does not fully convince me that the methodological jump is as large as the framing suggests. Even if the exact MTM instantiation is different, the paper should be more precise about what is fundamentally new: the MCMC target, the proposal design, the practical sampler, or the empirical test-time scaling recipe.

## Questions
1. Please clarify the exact MTM equations in the main paper. In particular, what is the correct expression for the candidate weight \(w_n\), and what is the correct sign in the acceptance probability \(\beta\)? Right now **Equation 3** and **Appendix D.2** disagree. A precise correction here would materially affect my confidence.

2. Does the practical implementation used in experiments still sample from the same stationary distribution as the theoretical MTM chain? In **Section 3.3**, you remove backward resampling and reuse proposal pools after rejection. Please explain, in the main-paper terms, whether this is exactly equivalent to the original MTM kernel or an approximation. If it is approximate, what part of Proposition 1 still applies?

3. How should readers interpret the reversibility assumption in **Proposition 1** for learned discrete diffusion models like MDLM and LLaDA-8B? Is this assumption believed to hold exactly, approximately, or only as a proof device? A sharper discussion of when the theorem is relevant to the experiments would help.

4. Can you provide the exact numerical values corresponding to **Figure 2** in the main paper, ideally with confidence intervals? The curves look encouraging, but the paper makes fairly strong consistency claims and the current presentation makes it hard to judge effect sizes rigorously.

5. Since **Section 3.3** argues that equal-weight NFEs can be misleading, can you provide a main-paper comparison under separate accounting of model calls and reward calls, at least for LLaDA-8B? This would help verify the core “effective test-time scaling” claim.

6. In **Table 2**, the “Evenly” schedule is best for Toxicity, Sentiment, and Perplexity, while \(0.1T\) is best for CoLA. Can you explain mechanistically why CoLA behaves differently? This analysis is interesting and could become a stronger insight if connected more explicitly to the structure of discrete denoising.

7. For the detoxification examples in **Figure 5(b)**, can you quantify semantic preservation or task relevance in the main paper, not only in the appendix? Some outputs appear less toxic partly because they drift far from the prompt intent.

## Flag For Ethics Review
- Yes, Privacy, security and safety  
- Yes, Potentially harmful insights, methodologies and applications

## Details Of Ethics Concerns
The paper explicitly studies reward-guided generation for toxicity-related objectives and states in the ethics section on **Page 10** that it includes experiments that increase toxicity in generated text for stress-testing. I understand the research motivation, and the work also includes detoxification experiments, but techniques for stronger reward-guided control over toxic generation can be dual use. The selected prompts from RealToxicityPrompts in **Section 4.5, Page 9** and toxicity-guided generation setup in **Section 4.1, Page 6** therefore raise safety considerations. I do not view this as misconduct, but it is an area where careful release practices and framing matter.

## Soundness Rating
2: fair. The empirical results are encouraging, but the central MTM derivation has multiple inconsistencies, and the link between the proved chain and the implemented sampler is not sufficiently established in the main paper.

## Presentation Rating
2: fair. The high-level idea is understandable and the figures are helpful, but notation mistakes, equation inconsistencies, and writing issues materially hinder verification.

## Contribution Rating
2: fair. The problem is important and the empirical direction is interesting, but the current paper does not yet make a sufficiently reliable contribution because the technical foundation and positioning need tightening.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The idea is promising and the experiments suggest there may be something useful here, but the paper asks the reader to trust a theoretical story that is currently too shaky. The MTM formulation needs to be corrected and the practical sampler-theory connection needs to be made much more precise before I would be comfortable supporting acceptance.

## Reviewer Confidence
4: confident. I am familiar with diffusion sampling, MCMC-style inference, and reward-guided generation, and I checked the main equations and algorithmic claims carefully.