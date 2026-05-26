Now I have a thorough understanding of the paper. Let me write the consolidated review.

## Summary

This paper proposes IterRef, a test-time scaling method for discrete diffusion models that applies iterative refinement through Multiple-Try Metropolis (MTM) sampling. The key idea is to use noising-denoising transition kernels within an MCMC framework to progressively correct intermediate states during the reverse diffusion process, rather than relying on one-shot guidance that cannot fix errors mid-trajectory. Experiments across language (MDLM, LLaDA-8B) and image (MaskGIT) domains with multiple reward functions show generally consistent improvements over existing guidance methods.

## Strengths

1. **Novel and well-motivated approach.** The paper identifies a genuine limitation of existing guidance methods for discrete diffusion — their inability to correct intermediate states once generated — and proposes an iterative refinement mechanism to address it. The noising-denoising transition kernel is a natural fit for discrete diffusion and is clearly connected to the predictor-corrector paradigm.

2. **Theoretical convergence guarantee.** Proposition 1 provides a formal convergence result showing that the MTM-based iterative refinement asymptotically converges to the optimal reward-aligned distribution \(p^*(x_t)\), assuming the idealized kernel and balancing function. This principled foundation distinguishes IterRef from purely heuristic guidance methods.

3. **Consistent empirical improvements across settings.** Across two language model backbones and four guidance tasks, IterRef generally outperforms baselines (FK, SVDD, SoP, BoN) at most compute budgets. The advantage is often substantial — e.g., on MDLM toxicity control, IterRef at 4T NFEs matches FK at 32T NFEs (Section 4.2). The method also transfers to image generation (MaskGIT) with clear improvements over baselines at low compute budgets (Table 1).

4. **Insightful analysis of scaling dynamics.** The analysis of iteration count vs. particle count (Table 3, Figure 4) cleanly demonstrates that iterative refinement is more effective than simply increasing the number of parallel proposals. The effective timestep analysis (Table 2) revealing that later denoising stages matter more for discrete diffusion (in contrast to continuous diffusion) is a useful finding.

## Weaknesses

### Fatal
None.

### Major

1. **No error bars or confidence intervals anywhere in the paper.** All reported results (Figure 2, Table 1, Table 2, Table 3, Figure 5) are point estimates with no measures of variability. This is a critical gap for an empirical paper claiming "consistent improvements" — especially when the advantage over baselines is sometimes modest (e.g., CLIPScore 35.8 vs 34.8 at NFE=16 in Table 1). Without error bars, the reader cannot assess whether the reported improvements are statistically reliable. This undermines the paper's central quantitative claim.

2. **CLIPScore used as both reward objective and primary evaluation metric for image generation.** MaskGIT results (Table 1) report CLIPScore — the same metric being optimized by the reward-guided process. This creates a circular evaluation: the method that better optimizes CLIPScore will naturally score higher on it, but this does not guarantee better generation quality. The paper mentions ImageReward results in Appendix C.1, but the main results table presents only the circular metric. Without FID, Inception Score, diversity metrics (recall), or human evaluation, the image generation claims are not convincingly supported.

3. **No diversity or quality-preservation analysis.** Reward-guided generation risks mode collapse or reward hacking (e.g., repetitive text for sentiment, CLIPScore-inflating artifacts in images). The paper provides no analysis of whether IterRef maintains generation diversity — no self-BLEU, distinct-n, or recall metrics for language, and no diversity metrics for images. The perplexity results (Figure 2) are a partial proxy for quality but do not address diversity. Without this analysis, it is impossible to rule out the possibility that IterRef achieves higher reward by collapsing to a narrow set of high-reward outputs.

4. **Significant gap between theoretical guarantees and practical implementation.** The convergence guarantee (Proposition 1) applies to the idealized MTM procedure, but the practical implementation deviates in ways that are not adequately analyzed:
   - **Approximate reward.** The theoretically required intermediate reward \(r(x_t) = \alpha \log \mathbb{E}_{x_0 \sim p_\theta(\cdot|x_t)}[\exp(r(x_0)/\alpha)]\) is replaced by a point estimate "by evaluating the reward function on the diffusion model's prediction of \(x_0\)" (Section 3.1). The convergence guarantee requires the exact \(r(x_t)\), so the practical chain targets a different distribution.
   - **Backward proposal elimination.** Section 3.3 claims the balancing function eliminates the need for resampled backward proposals "while still preserving the theoretical guarantees," but this is asserted rather than argued in the main text. The acceptance ratio in Equation (3) takes the form of a simple Metropolis-Hastings ratio rather than the standard MTM ratio, and the justification that the theoretical guarantees "still hold" under this modification is deferred entirely to the appendix.
   - **Pool reuse.** When a proposal is rejected, the paper states they "simply reuse the previously generated sampling pool" (Section 3.3). Standard MCMC would generate fresh proposals; reusing the same pool introduces autocorrelation and could bias the stationary distribution. No analysis of this effect is provided.
   
   The paper would benefit from either (a) providing guarantees that account for these practical modifications, or (b) clearly stating that the theory applies only to an idealized version and the practical algorithm is a heuristic supported by empirical evidence.

### Minor

1. **"8× faster" claim is imprecise and partially mismatched with evidence.** The claim is well-supported for one specific setting (MDLM on Toxicity, Section 4.2). However, Figure 1(b) labels "8× faster" for LLaDA-8B with safety reward, but the described data shows IterRef achieving higher reward at the same compute (not the same reward at 8× less compute). The abstract and Figure 1 caption use "up to 8× faster," which could be read as a general property. The claim should be precisely scoped to the setting where it holds.

2. **Small prompt set.** Language experiments use 15 prompts (Section 4.1), yielding 300 generations per condition (with an additional 3 seeds per the stated "3 seed" setup). While this aligns with conventions in some prior work, results on such a small prompt set could shift meaningfully with a different selection. This is a recognized limitation that should be explicitly discussed.

3. **No ablation on the reward strength \(\alpha\).** The temperature parameter \(\alpha\) controls the reward-KL trade-off and is central to the method's behavior, yet no sensitivity analysis or ablation is provided. Its value is never even stated for the main experiments.

4. **Choice of the noising distance \(s\) is not discussed in the main text.** The transition kernel \(K(x_t, x_t')\) involves a noising step to \(s > t\) followed by denoising back to \(t\), costing \((s-t)\) model calls per candidate. The value of \(s\) (or how it is chosen) is never mentioned in the main paper, making it impossible for the reader to assess the proposal cost.

5. **BoN outperforms IterRef on LLaDA for the CoLA task (Figure 2(b)),** yet the paper's framing emphasizes "consistently outperforms" without consistently qualifying this exception. The paper does acknowledge it in the LLaDA Results paragraph, but the abstract and introduction do not reflect this caveat.

### Trivial
- The pseudocode (Algorithm 2) mentions drawing backward auxiliary samples (Line 8), but Section 3.3 states this step is eliminated in practice — the pseudocode and text could be better aligned.
- "Evenly" in Table 2 is not clearly defined (it presumably means applying IterRef at every timestep with adjusted per-step compute to keep total budget fixed).

## Nice-to-Haves
- An ablation on \(\alpha\) (reward strength) would help understand the method's sensitivity to this key hyperparameter.
- Reporting wall-clock time alongside NFEs in the main paper (rather than delegating it entirely to Appendix C.4) would give a more complete picture of computational cost, especially given the sequential nature of IterRef.
- A limitations paragraph explicitly discussing the risk of reward over-optimization, the dependence on tuning \(\mathcal{U}\), and the gap between theory and practice would improve the paper's completeness.

## Removed Points

The following points from the reviewers were identified as noise or invalid and moved here:

1. **Harsh critic's claim that the acceptance ratio is "a standard Metropolis-Hastings ratio, not the MTM ratio" implying the algorithm is not actually MTM.** This misunderstands the design: the specific choices of \(K\) and \(\lambda\) in Equation (2) are crafted precisely to simplify the MTM acceptance ratio to the form in Equation (3). The derivation is in Appendix D.2 (not available in the extracted text). The paper's claim that this preserves the MTM framework is plausible and should be evaluated against the proof, not dismissed on stylistic grounds. *Demoted from potential fatal to removed.*

2. **Criticism that "The derivation of Equation (3) from the chosen K and λ is presented as a result with only a reference to Appendix D.2. The main paper should at least sketch the derivation."** Deferring detailed derivations to the appendix is standard practice. The main paper clearly states the key outcome (uniform proposal weights, simple acceptance ratio). *Removed as a presentation nitpick.*

3. **"Algorithm 2... the pseudocode does not make this cost visible."** Pseudocode is not expected to include computational cost annotations. *Removed as a presentation nitpick.*

4. **Strength Finder's claim about "Practical efficiency design" as a strength.** While the balancing function and selective refinement are genuinely useful design choices, the claim that they "preserve theoretical guarantees" is precisely what is contested above. I have kept this as a qualified strength but note it should be treated with caution given the theory-practice gap.

## Novel Insights

None beyond the paper's own contributions. The key insight — that iterative MCMC refinement via noising-denoising transitions is an effective test-time scaling strategy for discrete diffusion — is the paper's own contribution. The reviewer inputs did not surface any genuinely novel observation beyond what the paper already provides.

## Suggestions

1. **Add error bars or confidence intervals** (e.g., bootstrapped over prompts or seeds) to all quantitative results. This is essential for the reader to assess the statistical reliability of the claimed improvements, especially where margins are small.

2. **Report diversity metrics** alongside reward scores. For language: self-BLEU or distinct-n-grams. For images: FID-50k on ImageNet and recall (diversity) metrics. This is necessary to rule out reward hacking and to show that the reward improvement reflects genuine quality gains.

3. **For image generation, report at least one non-circular evaluation metric in the main paper.** Move the ImageReward results (currently in Appendix C.1) to the main table, or add FID. CLIPScore as both objective and metric is insufficient.

4. **Clarify the relationship between theory and practice.** Either provide convergence guarantees that account for the approximate reward, eliminated backward proposals, and pool reuse, or explicitly mark the practical algorithm as a heuristic inspired by the theoretical framework and discuss the gap.

5. **Scope the "8× faster" claim precisely.** Specify the exact setting (model, task, compute levels) where this holds and ensure all figure labels and captions match the evidence. Remove or qualify the annotation on Figure 1(b) if the data does not support 8× for LLaDA.

6. **Add ablations for \(\alpha\) and for the noising distance \(s\).** These are key hyperparameters in the method and understanding their effect would strengthen the paper.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>