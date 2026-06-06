## Summary

IterRef proposes a test-time scaling method for discrete diffusion models using iterative reward-guided noising-denoising transitions, formalized within a Multiple-Try Metropolis (MTM) framework. The method targets intermediate states *in situ*, progressively steering them toward a reward-aligned distribution, unlike prior sequential methods that advance in a single pass. Evaluated across MDLM, LLaDA-8B, and MaskGIT with five reward functions, IterRef consistently outperforms baselines (FK Steering, SVDD, SoP, BoN), achieving up to 8× speedup over FK on MDLM Toxicity and the highest CLIPScore at all compute budgets in image generation.

---

## Strengths

- **Consistent and large empirical gains across broad evaluation.** IterRef outperforms all tested baselines (FK Steering, SVDD, SoP, BoN) across three model backbones, two modalities, and five reward functions. On MDLM, IterRef at 2T NFEs exceeds all baselines at 32T NFEs on Sentiment, CoLA, and Perplexity (Section 4.2, Figure 2a). On image generation, IterRef achieves the highest CLIPScore at every compute budget from 1× to 16× (Table 1). The breadth of this evaluation strongly supports the paper's central claim.

- **Theoretical grounding via MTM.** The method is formally grounded in MTM (Proposition 1): by choosing the specific transition kernel and balancing function in Eq. 2, the importance weights collapse to uniform (w_n = 1/N) and the acceptance ratio reduces to a simple reward-difference test (Eq. 3). Proposition 1 states that the resulting Markov chain satisfies detailed balance and converges to p*(x_t), establishing that the iterative refinement is not heuristic.

- **Principled and quantified efficiency improvements.** Section 3.3 explains two concrete cost-reduction mechanisms: (1) the choice of balancing function eliminates backward proposals, halving per-iteration cost; (2) rejected pools are reused, further reducing overhead. The effective timestep set U allows refinement to be concentrated where it is most impactful.

- **Novel insight into discrete diffusion dynamics.** Table 2 shows that reward-guided refinement is most effective at later denoising stages (0.1T outperforms 0.9T substantially), which contrasts with continuous diffusion where early stages dominate. This finding constitutes a genuine empirical insight about discrete diffusion and has practical guidance value.

- **k-vs-N ablation reveals a non-obvious trade-off.** Table 3 on LLaDA shows that at fixed total compute, increasing iterations k yields larger gains than increasing candidates N. Peak performance at (k=8, N=4) versus degradation at (k=32, N=1) is a concrete result that motivates the specific design of IterRef over simple particle filtering.

---

## Weaknesses

### Fatal
None.

### Major

- **Theory-practice gap between Algorithm 2 and Section 3.3.** Algorithm 2 (Line 8) explicitly includes the step "Propose N-1 auxiliary samples {x_t''^(n)}_{n=1}^{N-1} ~ K(x_t', ·) and set x_t''^(N) = x_t," which are the backward proposals required for the MTM acceptance criterion. However, Section 3.3 directly states: "the practical implementation eliminates the resampling step and reduces the per-iteration cost by nearly half," claiming this is justified by the choice of balancing function in Eq. 2 while "still preserving the theoretical guarantees." These two accounts are contradictory as written. After the simplification, combined with uniform weights (w_n = 1/N), the actual running procedure becomes: draw N proposals, select one uniformly, accept via standard MH criterion, reuse pool on rejection — a substantially simpler procedure than full MTM. The paper does not show in the main body that this simplified procedure retains Proposition 1's convergence guarantee; it is merely asserted. Readers implementing IterRef must choose between the pseudocode and the prose, with no reconciliation. This should be resolved either by unifying the pseudocode with the actual implementation and showing the guarantee transfers, or by treating the full MTM as a theoretical framing and explicitly analyzing the simplified procedure as the deployed algorithm.

### Minor

- **NFE metric obscures efficiency claims for LLaDA-8B.** Section 3.3 explicitly acknowledges that "aggregating [diffusion model calls and reward model calls] into a single NFE value may obscure meaningful differences," noting that for LLaDA-8B the diffusion model dominates while for MDLM they are comparable. Nevertheless, all main figures (1b, 2, Table 1) use combined NFE. The "8×" speedup headline in Figure 1(b) is drawn on the combined NFE axis. For LLaDA-8B, a baselines at the same NFE may be using a very different actual FLOPs profile. The wall-clock analysis is deferred to Appendix C.4 with no representative summary in the main body. Since the paper itself flags this concern, it should surface the wall-clock comparison (even for one representative task and model) in the main body alongside the NFE plot.

- **Pool reuse after rejection: theoretical validity needs discussion.** Section 3.3 justifies reusing rejected proposal pools by noting "the candidates were already drawn i.i.d. from the same transition kernel." This is correct marginally, but the pool has already been conditioned on none of the N proposals being accepted — this technically changes the effective distribution of the reused pool. Whether this conditioning affects the MTM guarantees is not discussed. Even a brief argument in Section 3.3 or the appendix addressing this conditioning would strengthen the claim.

- **Absence of DSearch, DTS, PG-DLM as baselines.** Section 5 explicitly describes PG-DLM (Particle Gibbs on full trajectory), DSearch (beam search over denoising paths), and DTS (MCTS-based value backup) as related reward-guided generation methods for discrete diffusion. None appear in Figure 2 or Table 1. The paper does not explain whether these are excluded due to incompatible backbones, unavailable code, or different compute profiles. If any of these are applicable to the same tasks and models, their absence is a gap; if they are genuinely out of scope, a sentence explaining why would suffice.

### Trivial
None that warrant mention.

---

## Nice-to-Haves

- **Text quality beyond reward.** The paper motivates IterRef partly by preserving "naturalness of the samples" (Section 2), but experiments measure only the target reward. On Sentiment, Toxicity, and CoLA, the method could in principle reward-hack while producing degenerate outputs. Including at least one diversity or held-out perplexity metric for the non-Perplexity tasks would verify that naturalness is genuinely preserved.

- **Deeper analysis of non-monotonicity at k=32, N=1 in Table 3.** Table 3 shows degradation from (k=16, N=2) to (k=32, N=1) across all tasks, suggesting an optimum. Analyzing whether this corresponds to high rejection rates at N=1 or over-refinement at a single timestep would give the paper a sharper mechanistic story.

- **Ablation of BoN vs IterRef on CoLA/LLaDA.** Section 4.2 notes that BoN achieves larger gains on CoLA with LLaDA-8B, attributing this to LLaDA already generating well-formed text. Examining reward variance across LLaDA outputs on CoLA would test this explanation directly.

---

## Removed Points

*These points were removed; treat with caution.*

- **Figure 5 labeling inconsistency ("IterRef" vs "Ours" as separate curves).** The parsed text lists SLP, SR, SVTOD, IterRef, and Ours as five separate curves in Figure 5(a). Under the hard rules, this is a parser artifact, not a paper problem. Removed.

- **Introduction "novelty inflation" re: token correction.** The harsh critic contended the introduction presents re-masking as IterRef's exclusive invention. But the introduction presents the challenge ("incorrectly generated tokens cannot be corrected"), and the related work properly credits Wang et al. (2025) for the same idea. This is not inflation; it is a standard introduction/related-work split. Removed as a misread.

- **Critique of uniform w_n providing "no reward-weighting advantage."** The paper transparently explains that w_n = 1/N corresponds to uniform sampling and reward guidance flows entirely through the acceptance step β (Section 3.1, following Eq. 3). This is a design choice, not a flaw—the reward guidance is principled through β. Removed.

- **"Effective timestep finding is mechanically sensible"** (critique that the paper's Table 2 insight is not novel). This is a speculative standard argument — the paper provides empirical evidence for the discrete case and notes the contrast with continuous diffusion. The finding is genuine even if the direction is expected. Removed.

---

## Novel Insights

The most genuine novel insight from this review, beyond the paper's own contributions, is the implied tension between the MTM's theoretical elegance and its practical instantiation: by collapsing to uniform importance weights and eliminating backward proposals, IterRef in practice resembles a guided MH sampler with candidate reuse. Whether this collapse is theoretically innocent or whether it weakens the convergence guarantees in practice (e.g., due to rejection-conditioned pool reuse) is an open question that could illuminate broader relationships between MTM, MH, and reward-guided MCMC in discrete spaces. This analysis, if done, would make the theoretical contribution substantially more impactful than Proposition 1 currently stands.

---

## Suggestions

1. **Unify Algorithm 2 with the actual implementation.** Present a single "IterRef (deployed)" pseudocode that omits backward proposals and explicitly annotates where the MTM simplification is applied. Label Algorithm 2 (current) as the full theoretical MTM. Either add a corollary proving the simplified algorithm inherits Proposition 1's guarantees, or present a modified proposition for the simplified form.

2. **Surface wall-clock results in the main body.** Add a companion panel to Figure 2 or a table showing wall-clock time for at least LLaDA-8B Toxicity, since that is where the "8×" headline lives. This converts the headline from NFE-based to compute-verified.

3. **Address pool reuse conditioning.** Add a brief discussion (1–2 sentences) in Section 3.3 arguing why conditioning on rejection does not invalidate the i.i.d. characterization of the reused pool, or citing the relevant theoretical result.

4. **Explain absence of DSearch/DTS/PG-DLM baselines.** Add one sentence in Section 4.1 or the related work clarifying why these three methods are not compared (e.g., incompatible architecture, orthogonal compute profile, or code unavailability at submission time).

---

## Evaluation on Key Axes

- **Originality:** Moderate-high. Applying MTM with a specially designed noising-denoising kernel to discrete diffusion test-time scaling is a genuinely new combination. The simplification of the importance weights to uniform and the balancing function choice are non-obvious.
- **Importance of research question:** High. Test-time scaling for discrete diffusion is an under-explored but practically significant problem given growing use of discrete diffusion for language modeling.
- **Claims well-supported:** Mostly yes — the empirical case is broad and consistent. The main unsupported claim is that the simplified practical algorithm preserves the MTM convergence guarantee.
- **Soundness of experiments:** Strong. Three backbones, five reward functions, two modalities, consistent hyperparameter methodology following established baselines. NFE metric acknowledged as imperfect with appendix analysis.
- **Clarity of writing:** Good. The distinction between the theoretical and practical algorithm is the main clarity failure; the rest is clearly organized.
- **Value to research community:** High. Provides a practical and principled method for reward-guided generation in discrete diffusion with strong results; the k-vs-N analysis and effective timestep analysis have independent value.

---

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>4</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>4</soundness>
<clarity>3</clarity>
<community_value>4</community_value>
</subscores>