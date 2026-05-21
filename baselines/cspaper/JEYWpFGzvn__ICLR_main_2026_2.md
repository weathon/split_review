---
job_id: 35262355-8230-404f-92bb-4e334616099e
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: JEYWpFGzvn.pdf
paper: INFOTOK: Adaptive Discrete Video Tokenizer via Information-Theoretic Compression
main_score_norm: 0.8
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, focusing on representation learning, generative modeling, variational objectives, and video tokenization.

## Minimum Quality
Pass ✅. The paper contains the expected scientific components, including abstract, introduction, method, experiments, results, related work, discussion, and conclusion; despite several concerns about theory precision and evaluation scope, it clears the bar for full review rather than desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, reviewer-targeting instructions, or other obvious manipulation attempts in the provided paper content.

# Expected Review Outcome:
## Summary
This paper studies adaptive discrete video tokenization, with the goal of assigning fewer tokens to easier videos and more tokens to information-rich ones. The authors argue, via an information-theoretic framing, that fixed-length tokenization and data-agnostic adaptive training are suboptimal, then propose INFOTOK, which uses an ELBO-based router to choose token lengths and a transformer-based adaptive compressor to prune tokens based on estimated information content. Experiments on TokenBench and DAVIS show better reconstruction-quality-versus-compression tradeoffs than ElasticTok and competitive quality relative to a strong fixed tokenizer while using fewer average tokens.

## Strengths
1. The paper tackles an important problem. As video tokenizers become upstream components for long-context video models, fixed-rate tokenization is clearly wasteful on easy content and brittle on hard content. The motivation is well aligned with current bottlenecks in scalable video modeling.

2. The overall method is easy to understand at a systems level, and **Figure 1** is genuinely helpful here. It clearly separates the roles of the encoder/decoder inherited from the base tokenizer, the router that decides \(N_{\mathbf{x}}\), and the adaptive compressor/decompressor that implements the variable-length bottleneck. This figure does real explanatory work rather than decorative work.

3. The empirical results are strong and fairly consistent in the main paper. In **Table 1**, INFOTOK and INFOTOK-Flex substantially outperform ElasticTok at the matched compression settings \( \mathrm{BPP}_{16}=0.81 \) and \(0.56\) on both TokenBench and DAVIS. The gap is not limited to one metric: PSNR, LPIPS, and especially FVD all improve materially. The result that INFOTOK at \(0.56\) is competitive with or better than ElasticTok at \(0.81\) is particularly compelling, since that is the kind of tradeoff this paper is supposed to deliver.

4. The paper does a good job showing the compression-quality frontier rather than cherry-picking a single operating point. **Figure 4(a-f)** is one of the stronger parts of the submission. The curves show that INFOTOK-Flex and INFOTOK mostly dominate ElasticTok across a range of compression levels, not just at one handpicked threshold. **Figure 4(g)** is also important, because it supports the claim that the proposed routing mechanism is not only better in reconstruction quality but also much cheaper at inference than threshold-search-based adaptive baselines.

5. The ablation against an oracle-like routing strategy is useful. **Table 2** shows that the ELBO-based router is quite close to the “Optimal” search-based strategy, at least on the discretized compression grid they consider. This directly addresses the core question of whether the router is a reasonable surrogate for brute-force allocation.

6. The qualitative examples are sensible. In **Figure 2**, the proposed method appears to preserve detail better than ElasticTok at similar compression, and retain quality close to Cosmos-DV with lower token usage. **Figure 3** also makes the degradation pattern under more aggressive compression easy to inspect. These figures support the claim that the method tends to preserve coarse structure first and lose fine details gradually, which is the behavior one would want from a practical tokenizer.

7. The method is modular. Building on top of an existing fixed tokenizer, instead of requiring a completely new tokenizer from scratch, makes the framework easier to adopt and easier to benefit from future backbone improvements.

## Weaknesses
1. The theoretical claims are stated more strongly than the main-paper derivations really support. The paper repeatedly suggests that existing fixed-rate or data-agnostic adaptive methods are “biased” and that INFOTOK is near-optimal, but the actual results rely on highly idealized assumptions that are much narrower than the rhetoric. For example, **Theorem 2.1** on **Page 3** is a restatement of source coding for perfect reconstruction under a distribution \(p(\mathbf{x})\), and **Theorem 2.2** on **Pages 4-5** depends on a very specific uniform router and a stylized generate-then-mask/prefix-tree view. That is not the same object as a practical neural video tokenizer with quantization error, imperfect reconstruction, finite capacity, and architecture-induced biases. The gap matters because the paper uses the theorem as a conceptual hammer against prior methods, but the theorem mostly tells us what happens in an ideal source-coding abstraction, not necessarily what happens in realistic training regimes.

2. **Equation 4** on **Page 5** is underspecified in a way that affects reproducibility and interpretation:
   \[
   r_{\beta}(N_{\mathbf{x}}|\mathbf{x})=\delta\!\left(\beta\cdot\frac{\mathrm{ELBO}(\mathbf{x})}{\mathbb{E}[\mathrm{ELBO}(\mathbf{x})]}\right).
   \]
   Here \(N_{\mathbf{x}}\) is supposed to be a token count, hence an integer in \(\mathbb{N}^+\), but the expression inside \(\delta(\cdot)\) is a real number. The main paper does not define how this is converted to an integer, whether by rounding, floor, stochastic rounding, clipping, or some constrained projection to \([1,N_{\max}]\). This is not a cosmetic omission. Small changes in rounding and clipping can change average token usage, especially near low-budget regimes. The appendix later mentions clipping to \(1/16\) of maximal length, but this implementation detail is absent from the main formulation even though it directly changes the router definition and the practical operating range.

3. There is a noticeable mismatch between the theory and what is actually used in practice. On **Page 5**, the router is justified using the ELBO in **Equation 3**, including the KL term,
   \[
   \mathrm{ELBO}(\mathbf{x})=\mathbb{E}_{q_{\phi}(\mathbf{z}|\mathbf{x})}[\log p_{\theta}(\mathbf{x}|\mathbf{z})]-D_{\mathrm{KL}}[q_{\phi}(\mathbf{z}|\mathbf{x})\|p(\mathbf{z})].
   \]
   But on **Page 6**, the authors state that in practice they use “the reconstruction error itself (without the KL term)” because the KL term is approximately proportional. That may be a perfectly reasonable engineering shortcut, but then the theoretical story is no longer the one being experimentally validated. Theorems about ELBO-based routing do not automatically transfer to a reconstruction-error-only router. This matters because a central selling point of the paper is that the routing mechanism is principled rather than heuristic; once the main practical version drops the KL term, the distinction becomes blurrier.

4. The proof sketch for **Theorem 3.1** is too loose for the strength of the claim. The theorem on **Page 5** claims a near-optimal expected length guarantee, but the proof in **Appendix B.2, Page 21** is extremely terse and appears to skip crucial steps. In particular, the line “the minimizer of the adaptive loss has \(N_{\mathbf{x}}\le -l_{\mathbf{x}}\) with \(N\ge -l_{\mathbf{x}}\)” is asserted rather than derived, and the bound mixes \(H_C(\mathbb{D})\) with \(\mathbb{E}[-\log p(\mathbf{x})]\) in a way that obscures log-base consistency. Since \(H_C(\mathbb{D})=\mathbb{E}[-\log_C p(\mathbf{x})]\), the relationship to \(\mathbb{E}[-\log p(\mathbf{x})]\) should be written carefully with the base-conversion factor made explicit. As written, the result reads more like an intuition than a fully checked theorem.

5. The token-selection mechanism itself is described somewhat ambiguously. On **Page 6**, the text says the compressor computes a binary mask where the “\(N_{\mathbf{x}}\) tokens with the lowest ELBO values are 1 and the remaining are 0.” If 1 means preserved, this would keep the lowest-information tokens, which contradicts the stated goal. The sentence is likely intended to mean that low-information tokens are masked out, but the wording is backwards enough to cause confusion. The appendix on **Page 22** then says they “remove tokens with the highest log-likelihoods, corresponding to the lowest information content,” which is more sensible. This inconsistency should be cleaned up in the main paper because the compressor is one of the two core contributions.

6. The experimental evidence is strong for reconstruction, but narrower than the paper’s framing suggests. The introduction motivates adaptive tokenization as crucial for long-video understanding and generation, yet **Section 4** only evaluates reconstruction metrics. The paper explicitly says downstream generation is beyond scope, which is fair, but then the broader impact claims should be toned down. A tokenizer can look good under PSNR/SSIM/LPIPS/FVD and still be a poor interface for downstream autoregressive modeling, retrieval, or action understanding. Without any downstream experiment, the paper demonstrates a better adaptive reconstructor, not yet a clearly better foundation for long-video models.

7. The baseline set is somewhat limited for a paper making broad claims about adaptive tokenization. In the adaptive category, the main comparison is essentially against ElasticTok. That is an important baseline, but the literature positioning feels incomplete, especially relative to other recent variable-length or adaptive tokenization approaches. The related-work discussion on **Pages 9-10** is not terrible, but it reads a bit too much like “everyone else is heuristic, we are principled,” without enough direct empirical confrontation against a wider set of alternatives. This weakens the novelty and significance case.

8. The fairness of the data setup is mixed. On **Page 6**, all evaluations are restricted to square 256px crops because ElasticTok only supports \(256\times256\) inputs. That makes the head-to-head comparison fair with ElasticTok, but it also reduces the realism of the evaluation for a video tokenizer paper, especially because variable resolution is one of the practical reasons a content-adaptive method might matter. The appendix does include additional resolution results, but the main paper’s claims would be stronger if some of that evidence were brought into the main results rather than outsourced.

9. The paper leans heavily on a very strong base tokenizer, Cosmos, and the improvements over the fixed baseline are meaningful but not huge at the top operating point. In **Table 1**, INFOTOK at \( \mathrm{BPP}_{16}=0.81 \) is very close to Cosmos-DV at \(1.00\), which is a nice token-saving result, but the absolute gains over the base tokenizer are mostly in efficiency rather than raw quality. That is not a flaw per se, but it means the contribution is more “better routing and compression on top of an already strong tokenizer” than a wholesale advance in video tokenization. The paper would benefit from clearer framing on this point.

10. There are a few quantitative inconsistencies and missing details that should not be hand-waved away. On **Page 6**, the mask overhead is described as “approximately \(5\%\),” while the inference formula on **Page 7** and the appendix effectively use an overhead of \(1/16=6.25\%\). This is minor numerically, but it is symptomatic of the paper being a bit casual in places where exact accounting matters. Likewise, the dependence of \(\mathbb{E}[\mathrm{ELBO}(\mathbf{x})]\) on training EMA versus evaluation-set averaging is scattered between **Page 7** and **Appendix C.3**, and should be specified more cleanly in the main method.

## Questions
1. Please clarify the exact operational definition of the router in **Equation 4**. How is the real-valued quantity converted into an integer token count, and what clipping constraints are applied in the main experiments? A precise formula would materially increase confidence in reproducibility.

2. The theory is built around ELBO, but the practical implementation on **Page 6** says the KL term is dropped and reconstruction error alone is used. How much of the empirical gain survives if one uses the true ELBO router exactly as defined in **Equation 3**? A direct comparison would help verify whether the information-theoretic argument is central or mostly motivational.

3. For **Theorem 3.1**, can the authors provide a more rigorous derivation of the stated bound, including explicit log-base handling and a clearer justification of the step asserting \(N_{\mathbf{x}}\le -l_{\mathbf{x}}\)? Right now this theorem is one of the main intellectual selling points, but the proof in the appendix feels too compressed.

4. In **Section 3.2**, please clarify the masking semantics. Does the binary mask mark preserved tokens or discarded tokens? The wording on **Page 6** appears inconsistent with the appendix. This should be unambiguous.

5. In **Table 2**, the ELBO-based router is close to the “Optimal” search-based strategy on the tested compression grid. Could the authors report how sensitive this is to the granularity of the grid and to the choice of evaluation set used for estimating the average ELBO? This would help assess how robust the routing policy is.

6. Since the method is motivated as a better representation for long-video models, do the authors have even a lightweight downstream proxy, for example autoregressive perplexity on token streams, retrieval, or action classification using frozen tokens? Even a small-scale study would substantially strengthen the significance claim.

7. Can the authors broaden the empirical comparison to additional recent variable-length or adaptive tokenizers, or at least discuss more explicitly where INFOTOK differs from prior approaches that also allow non-fixed token counts? The current empirical story is convincing against ElasticTok, but narrower than the conceptual claims.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
The paper discusses general misuse risks of video generation and deepfakes in the ethics statement, but I do not see an ethics issue that requires special review beyond standard conference handling. The work is a tokenizer/compression method and does not introduce a new human-subjects dataset or a sensitive deployment setting in the main paper.

## Soundness Rating
3: good. The method is empirically well supported for reconstruction, but several theoretical claims and mathematical details, especially around **Equation 4** and **Theorem 3.1**, need tighter justification.

## Presentation Rating
3: good. The paper is generally readable and the main figures are useful, but there are important ambiguities in notation, routing details, and compressor masking semantics.

## Contribution Rating
3: good. The adaptive-tokenization problem is important, the method is practically effective, and the empirical gains are meaningful, though the contribution is somewhat narrowed by limited downstream evaluation and a theory-to-practice gap.

## Overall Rating
8: Accept, good paper (poster). This is a strong paper with a clear practical win over prior adaptive tokenization baselines and a useful modular design, even though I am not fully convinced by the strongest theoretical framing and I would like tighter mathematical exposition and broader validation.

## Reviewer Confidence
4: confident. I am confident in the assessment and checked the main equations, tables, figures, and the high-level logic of the theoretical claims, though some proof details would benefit from author clarification.