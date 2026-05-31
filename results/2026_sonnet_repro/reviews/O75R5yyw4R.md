Now let me do the calibration searches.Round 1 bracket: **5.5–7.5**. DDPP (6.25) and the discrete guidance paper (6.5) are the most topically relevant anchors. IterRef seems at least comparable or stronger. Now narrowing.Now I have sufficient calibration data. Let me write the final review.

**Summary of calibration:**
- Round 1 bracket: 5.5–7.5
- Most relevant anchors in range: DDPP (6.25), Discrete Guidance (6.5), GenARM (6.5), DAS (7.25)
- IterRef is stronger than DDPP (training-free, more backbones, no secondary model), comparable to DAS (training-free SMC for reward-aligned diffusion, but DAS is for continuous diffusion), and stronger than Discrete Guidance (6.5) due to its breadth and convergence guarantee.
- The algorithm presentation gap (Algorithm 2 vs. Section 3.3) and NFE conflation are real but not fatal; the core empirical contributions are solid.
- Final score: **6.5**

---

## Summary

IterRef is a training-free test-time scaling method for discrete diffusion models that applies reward-guided iterative refinement at fixed intermediate denoising states via Multiple-Try Metropolis (MTM). It formalizes a noising-denoising transition kernel and a matching balancing function that yields uniform proposal weights and a simple reward-ratio acceptance criterion, proving convergence to the optimal reward-aligned distribution. Extensive experiments across MDLM, LLaDA-8B, and MaskGIT on language (Toxicity, Sentiment, CoLA, Perplexity) and image (CLIPScore) tasks show consistent and often large improvements over FK Steering, SVDD, SoP, and Best-of-N.

---

## Strengths

- **Consistent and large empirical gains across diverse settings.** IterRef outperforms all tested baselines across four language-generation tasks with two backbones (MDLM, LLaDA-8B) and one image-generation model (MaskGIT). On MDLM with Sentiment, CoLA, and Perplexity, IterRef with **2T NFEs** exceeds all baselines at **32T NFEs** (Section 4.2, Figure 2a); on Toxicity it matches FK Steering at 4T versus FK's 32T, an 8× speedup. MaskGIT results show IterRef as best at every compute budget in Table 1. This breadth makes the core empirical claim hard to dismiss.

- **Principled MTM framework with convergence guarantee.** The specific choice of kernel $K$ and balancing function $\lambda$ in Equation 2 yields uniform importance weights ($w_n = 1/N$) and a simple reward-ratio acceptance probability ($\beta = \min(1, \exp((r(x_t') - r(x_t))/\alpha))$ (Eq. 3), with Proposition 1 proving that the resulting Markov chain converges asymptotically to $p^*(x_t)$. This is a genuine theoretical contribution over prior heuristic particle-reweighting methods.

- **Training-free design with explicit compute knobs.** IterRef requires no fine-tuning, no secondary model training, and works plug-and-play with any reward function (differentiable or not). The effective timestep set $\mathcal{U}$ and the $k$-vs-$N$ tradeoff (Table 3, Figure 4) give practitioners direct control over the compute/quality budget — a practically valuable contribution.

- **Novel insight on discrete diffusion dynamics.** Table 2 establishes that reward guidance is most effective at later denoising stages ($0.1T$) for discrete diffusion, in contrast to continuous diffusion where early steps dominate content. The finding that "Evenly" dominates for most tasks while $0.1T$ alone wins on CoLA is a concrete and actionable insight for practitioners.

- **Iteration over particles.** Table 3 shows that increasing iteration count $k$ at fixed total compute consistently dominates increasing particle count $N$, confirming that iterative distribution-shifting is more powerful than i.i.d. over-sampling at the same cost. This is a well-supported analytic contribution.

---

## Weaknesses

### Fatal

None.

### Major

- **Disconnect between Algorithm 2 and the practical implementation in Section 3.3.** Algorithm 2 (Line 8) specifies generating $N-1$ backward auxiliary proposals from $K(x_t', \cdot)$, which is the full MTM procedure. Section 3.3 then states: *"Through an appropriate choice of the balancing function in Equation 2, the acceptance rate can be evaluated without the need for resampled proposals $x_t''$, while still preserving the theoretical guarantees of the MTM framework. Consequently, the practical implementation eliminates the resampling step and reduces the per-iteration cost by nearly half."* These two descriptions are directly inconsistent as presented: a reader following Algorithm 2 will implement something different from the method that was actually run in experiments. The math showing why the specific $\lambda$ in Equation 2 cancels the backward proposals is deferred to Appendix D.2. As a result it is unclear from the main text (i) what was actually run, (ii) whether Proposition 1 applies to the simplified procedure, and (iii) how to reproduce the results. The paper should either provide a simplified pseudocode that reflects the deployed method or explicitly label Algorithm 2 as the formal MTM procedure and present a separate "IterRef-practical" algorithm that shows the simplified version and explains its equivalence.

- **NFE-based efficiency claims are not fully grounded.** Section 3.3 itself flags that *"aggregating these into a single NFE value may obscure meaningful differences"* and notes that for LLaDA-8B the diffusion model calls dominate while for MDLM reward and generative model calls have comparable costs. Yet Figures 1(b), 2, 4, 5, and Table 1 all use combined NFE, and the headline "8× faster" (Figure 1(b)) is drawn on the NFE axis. Whether this advantage holds in wall-clock time — which the paper promises in Appendix C.4 — is essential to substantiate. A result that looks 8× faster in NFE but much less so in wall-clock time would substantially weaken the efficiency claim.

### Minor

- **The CoLA anomaly (LLaDA-8B) is post-hoc unexplained.** Section 4.2 notes that on CoLA with LLaDA-8B, BoN achieves "larger gains" than IterRef, attributed to LLaDA already generating linguistically well-formed text. This explanation is plausible but untested. Reporting the variance of reward scores across LLaDA outputs on CoLA would either validate (low variance → reward signal is weak → BoN and IterRef are comparable) or undercut (high variance → something else is going on) this interpretation.

- **Text quality / naturalness not directly measured.** The paper's stated objective (Section 2 background) is "to preserve the naturalness of the samples while maximizing the given reward." For Toxicity, Sentiment, and CoLA experiments, reward-hacking via fluent-but-degenerate text is possible. At minimum, reporting generation diversity or a complementary quality metric (e.g., perplexity from a held-out model for the non-perplexity tasks) would characterize whether IterRef genuinely shifts the distribution or narrowly optimizes the metric.

- **Non-monotonicity at $k=32$, $N=1$ in Table 3 is unexplained.** Table 3 (LLaDA) shows that $k=8, N=4$ dominates $k=32, N=1$ on all three tasks, and $k=32, N=1$ underperforms $k=16, N=2$. This is noted in passing as "diminishing returns" but not analyzed. The likely cause (very high rejection rate at $N=1$, causing the chain to stall) is a direct consequence of how MTM operates, and understanding this would sharpen the paper's story about the mechanism.

### Trivial

None beyond the parser-artifact formatting issues noted in reviews.

---

## Nice-to-Haves

- A unified pseudocode that directly reflects the deployed simplified procedure, with theoretical-MTM Algorithm 2 labeled as the formal derivation. This would resolve the reproducibility concern at no cost to the contribution.
- Reporting wall-clock efficiency alongside NFE in at least one representative setting (e.g., LLaDA-8B Toxicity), moving Appendix C.4 material into the main paper.
- An analysis of whether the "Evenly" strategy's superiority in Table 2 is explained by its coverage of later timesteps (since $0.1T$ individually performs best) or by independent contributions of early timesteps — this would deepen the insight.
- Evaluating DSearch (Li et al., 2025), DTS (Jain et al., 2025), or PG-DLM (Dang et al., 2025) as baselines or explaining why they are excluded (e.g., different backbone requirements, training-time overhead). The paper clearly distinguishes IterRef's trajectory-free approach from their trajectory-search designs, but quantitative comparison would strengthen the positioning.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

1. **Figure 5 labeling inconsistency ("IterRef" vs "Ours" as separate curves)** — The harsh critic flagged this but also noted it is almost certainly a parser artifact. The parser-extracted figure caption conflates baseline labels. REMOVED per the hard rule against formatting artifacts from PDF parsing.

2. **Effectiveness of uniform weights $w_n = 1/N$** — The harsh critic raised this as a concern about whether MTM provides reward-weighting advantage during proposal selection. However, the paper is explicit in Equation 3 and the surrounding discussion that the uniform weight follows *directly* from the designed $\lambda$ (Eq. 2), and that reward guidance is deferred to the acceptance step. This is a design choice, not an unexplained omission. REMOVED as a strawman — the paper addresses it.

3. **Pool reuse violates MTM theoretical requirements** — The harsh critic questions whether the rejected pool's distribution changes after conditioning on rejection. The paper's claim that "the candidates were already drawn i.i.d. from the same transition kernel" and hence the pool "remains a valid proposal set" is a standard argument in MCMC (the pool was generated before observing the rejection event under MTM's sequential independence). DEMOTED to editorial/minor-clarity concern at most; not retained as a weakness.

4. **Missing related-work baselines (DSearch, DTS, PG-DLM)** — Moved to Nice-to-Haves per the hard rule against missing-related-work criticisms as main weaknesses; the paper clearly explains why these methods are architecturally distinct.

5. **Introduction does not credit Wang et al. (2025) for re-masking idea** — The introduction presents the corrective re-masking mechanism as a challenge context, and Related Works (Section 5) does cite Wang et al. (2025) for re-masking. The harsh critic's assertion that the introduction should acknowledge this connection is a minor presentation note already addressed. REMOVED.

---

## Novel Insights

The most genuinely novel observation in IterRef is that test-time reward-guidance in *discrete* diffusion is most effective at later denoising stages — directly inverting the conventional wisdom from continuous diffusion, where early high-noise steps dominate content formation. This matters because it implies that compute budgets for discrete diffusion guidance should be concentrated near $t \approx 0$ rather than spread uniformly, which is a practically actionable difference in how one deploys test-time scaling for masked language models. The MTM instantiation (uniform proposals + reward-ratio acceptance) that makes this computationally tractable is also a clean and reusable theoretical contribution: any future masked diffusion refinement method can adopt the same kernel-balancing function pair and inherit the convergence guarantee.

---

## Suggestions

1. **Unify the algorithm.** Present a "IterRef-simplified" pseudocode reflecting the actual deployed method (uniform selection, MH acceptance, no backward proposals). Label Algorithm 2 as the formal MTM proof vehicle. This single change removes the most significant reproducibility concern.

2. **Report wall-clock time prominently.** Move the Appendix C.4 wall-clock comparison to the main text, at minimum for LLaDA-8B Toxicity (the "8× faster" headline case). If the advantage persists in wall-clock, the efficiency claim becomes much stronger; if it shrinks, the discussion should be honest about it.

3. **Add a simple generation quality metric.** For the language tasks, report perplexity (from a held-out GPT-2) for all tasks other than Perplexity itself, or n-gram diversity. This directly addresses whether IterRef preserves naturalness or narrows to reward-hacking outputs.

4. **Analyze the $k=32$, $N=1$ failure mode.** Track the acceptance rate $\beta$ as $N$ decreases and $k$ increases. If the chain stalls at $N=1$ (acceptance rate near 0), this would explain the non-monotonicity in Table 3 and give a concrete lower bound on $N$ for practical deployment.

---

## Score and Decision

**Anchor papers and comparison:**
- Round 1: DDPP (6.25), Discrete Guidance (6.5), DAS (7.25), SVDD-related (3.8)
- Round 2: Scaling MDMs on Text (6.5), GenARM (6.5), Energy-based DLM (6.75), DAS (7.25)

IterRef is clearly stronger than DDPP (6.25): it is training-free, uses simpler infrastructure, covers more backbones, and has a cleaner theoretical derivation. It is comparable to GenARM (6.5) and Energy-based DLM (6.75): these also make solid empirical contributions with theoretical backing, but IterRef's breadth across modalities and models is an advantage. It is somewhat below DAS (7.25) in overall polish (DAS has more complete main-text efficiency analysis and no algorithm-description gap), but DAS addresses continuous diffusion, which is technically easier than discrete.

The Algorithm 2 vs. Section 3.3 discrepancy is a real and not merely cosmetic flaw — it affects what is actually run and whether the convergence guarantee applies — but it is recoverable in revision. The NFE conflation is partially mitigated by the paper's own acknowledgment and the promised appendix, but would need to be moved into the main text. Neither is fatal. The core contributions (MTM formulation, convergence proof, consistent empirical gains, effective-timestep insight) are solid and well-supported.

**Final bracket narrowed to 6.0–7.0; paper sits closer to the upper end at 6.5**, between DDPP/GenARM and DAS.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>