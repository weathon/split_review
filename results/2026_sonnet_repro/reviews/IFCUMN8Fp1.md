Now let me perform the calibration search. I'll start with a bracketing pass on POMDP learning / spectral methods topics.Round 1 bracket: **4.5 – 6.5**. The paper is clearly above the 3.0-scoring papers (which had fundamental issues) and below the 8.0-scoring papers (which were highly polished theory papers). Let me read some mid-range anchors, then narrow.Now let me do Round 2, narrowing within the 4.5–6.5 bracket.Now I have sufficient calibration. Let me write the final synthesized review.

---

## Summary

This paper proposes a spectral algorithm to learn the explicit parameters of a discrete POMDP (transition and observation matrices) from action-observation sequences collected under random exploration. The central insight is to estimate the similarity transform *P* that relates a Predictive State Representation (PSR)—learnable via Hankel-matrix decomposition—to the original POMDP basis. Recovery is achieved up to a "full-rank observability partition": states sharing identical observation distributions across all full-rank actions are merged into a single recoverable unit. The core theoretical result (Theorem 1) guarantees existence of the algorithm's output in the infinite-data limit, and the joint-diagonalization step (Lemma 1) pools evidence across all full-rank actions to handle cases where individual per-action observation distributions are non-unique (e.g., Tiger). Experiments on Tiger, T-Maze, and Sense-Float-Reset show convergence to ground truth, and reward-specification experiments show that explicit likelihoods can distinguish ambiguous states that observation-only methods cannot.

---

## Strengths

- **Genuine conceptual contribution — full-rank observability partition and Theorem 1**: The paper introduces a precise, original notion of "full-rank observability partition" that characterizes exactly what can and cannot be recovered by the method. Theorem 1 provides a correct, well-stated guarantee in the infinite-data limit, and the worked illustration in Figure 2 (Sense-Float-Reset) makes the implications of the partition concept concrete.

- **Non-trivial joint diagonalization step (Lemma 1)**: The key algorithmic innovation is pooling all full-rank action-observation matrices jointly via a random weighted sum (Eq. 18) before eigendecomposition, rather than decomposing per-action as in prior tensor methods. Lemma 1 correctly characterizes when distinct eigenvalues are almost-surely guaranteed, directly addressing the failure mode of per-action approaches (repeated per-action observation likelihoods such as in Tiger). This is a well-motivated and non-trivial adaptation.

- **Empirical convergence to ground truth against a principled baseline**: Figure 3 demonstrates that the learned observation and partition-level transition matrices converge to ground truth as data increases, while EM consistently fails (local minima). The convergence is shown over 100 seeds with standard deviation bands, and planning performance matches both PSR and ground-truth models on all three domains.

- **Demonstrated practical advantage of explicit likelihoods**: The reward-specification experiments (Figure 4, noisy hallway domain) show a concrete case where state-based reward assignment—enabled by the learned observation matrices—outperforms observation-based assignment from PSRs. This substantiates the paper's stated motivation: explicit likelihoods enable downstream model manipulation that black-box PSRs cannot support.

---

## Weaknesses

### Fatal
None.

### Major

- **Missing experimental comparison with Azizzadenesheli et al. (2016) and Guo et al. (2016).** The paper's central empirical claim is that it handles POMDPs—such as Tiger—where prior per-action tensor methods fail because individual per-action observation distributions are not state-unique. This claim is articulated clearly in Section 1 and Section 4.2, but neither prior method appears as an experimental baseline. The comparison in Section 5 is against linear PSRs and EM—neither of which operates in the same regime as the proposed method or the cited tensor predecessors. Without this comparison, the most critical empirical test—whether the proposed method succeeds where Azizzadenesheli/Guo fail—is simply absent. This leaves the paper unable to empirically distinguish "strictly more general than prior tensor methods" from "a re-derivation of the same class." The theoretical argument for generality is sound, but verification on Tiger (where the prior methods should demonstrably fail) would be straightforward and would substantially strengthen the paper.

### Minor

- **Theorem 1 is an existence result with no finite-sample characterization.** The theorem states "there exists an algorithm" satisfying the recovery properties in the infinite-data limit, and the paper explicitly defers PAC-learning bounds to future work. While this is common for an initial theoretical contribution, the practical regime of validity is entirely uncharacterized analytically. The paper shows convergence curves in Figure 3 but does not analyze how error scales with sample size or problem size. Even an empirical scaling analysis—model error vs. data for increasing state counts—would substantially sharpen the practical story.

- **All experiments use very small domains (≤10 states, ≤4 actions, ≤2 observations).** The Hankel matrix approach has combinatorial cost in history/test length, and the paper acknowledges scalability as future work. However, the main body does not discuss where the method breaks down, what Hankel sizes or runtimes were used, or whether $10^6$ interactions (the x-axis maximum in Figure 3) is realistic for the stated motivating application (robot manipulation). The practical scope is effectively unquantified.

- **Selective truncation of transition error curves.** The Figure 3 caption explicitly states: "Trans. matrix error. This error is only measurable once the estimated number of states matches that of ground truth, which truncates the curves." This means the displayed transition errors are best-case estimates conditional on correct rank identification. Since T-Maze and Sense-Float-Reset show rank-estimation errors at low data regimes (Row 1), the transition error plots for those domains exclude the low-data regime where errors are presumably larger. This is honest disclosure but is never discussed as a distinct concern—the curves can give an overly optimistic impression of convergence speed.

### Trivial

- **Section 4.3's post-processing step (most algorithmically novel step) is under-explained in the main text.** The random block-diagonal rotation *R* and the final transform diag(R P'^{-1} m_∞) R P'^{-1} are introduced in three sentences and deferred entirely to Appendix A.5. For the paper's most novel algorithmic contribution, this brevity may leave readers unsure of why the construction is correct or what failure modes it guards against.

---

## Nice-to-Haves

- A toy variant of the Baum et al. (2017) cabinet-locking scenario—explicitly invoked in the introduction but never returned to—would make the case for explicit model learning more compelling than the hallway domains.
- An empirical scaling analysis (L1 model error vs. data size and number of states) would give readers a practical sense of where the method is usable.
- Clearer exposition in Section 6 of why EM fails systematically (non-convexity, local optima) vs. why the spectral approach avoids this; the distinction between EM-as-Baum-Welch and spectral-HMM learning could be made sharper.
- The Figure 4 legend label "PSR_obs" could be more descriptive (e.g., "PSR + obs-based reward") to avoid conflation of model type and reward specification strategy.

---

## Removed Points

*These points were flagged for removal; treat with caution.*

- **Conditioning of $(M^a)^{-1}$ in finite samples (Section 4.2).** The harsh critic notes that "for actions with transition matrices that are full-rank but poorly conditioned, this step will amplify noise substantially." While technically valid as a concern for any eigendecomposition-based method, the critic provides no specific evidence that it is a problem for the tested domains, and the paper does not present a case where this failure occurs. This is a general concern about numerical linear algebra, not a demonstrated flaw in this paper. REMOVED per filtering discipline (no concrete anchor in the paper).

- **Ergodicity with deterministic/near-deterministic transitions not discussed.** The critic suggests the memoryless uniform policy assumption fails for deterministic transitions. The paper does address this in Section 4.1.1 (discussing the role of passive sensing actions in breaking periodicity and ensuring irreducibility). While the discussion is brief, it is not absent. REMOVED as strawman.

- **"Post-hoc rationalization" of the noisy hallway result.** The critic characterizes the explanation of why observation-based rewards fail in the noisy domain as "post-hoc rationalization rather than a prior prediction." The paper's explanation—that a uniform belief and middle-state belief produce the same mixed observation distribution—is factually correct and genuinely explains the experimental result. The use of Figure 4 to demonstrate that the entropy-based state reward succeeds is confirmatory evidence. REMOVED as subjective.

- **Narrow use case for reward specification.** The critic argues the advantage of explicit likelihoods is demonstrated on a "narrow" use case. However, the paper is upfront that this is a targeted demonstration of the practical advantage of explicit likelihoods. The scope matches what the paper claims. REMOVED as scope-creep criticism.

---

## Novel Insights

The paper's most genuinely novel observation is that the joint diagonalization ambiguity in eigendecomposition—the standard failure mode of per-action tensor methods when observation distributions are non-unique—can be broken by pooling a random weighted sum across *all* full-rank actions simultaneously. This means that even when no single action distinguishes all states by its observation distribution, the aggregate weighted sum almost surely separates all states not in the same full-rank observability partition. The "full-rank observability partition" is a precise, original characterization of the limit of spectral POMDP recovery without per-action distinguishability—a concept that captures exactly which model structure is recoverable and which is not.

---

## Suggestions

1. Add Azizzadenesheli et al. (2016) and Guo et al. (2016) as baselines on the Tiger domain. This is a direct test of the paper's central claim and is highly likely to produce a definitive result (prior methods failing where the proposed method succeeds).
2. Provide at least an empirical scaling analysis: plot L1 model error as a function of dataset size *and* state count across several POMDP sizes (e.g., 2, 5, 10, 20 states). Even if 20 states proves intractable, the curve will characterize practical limits.
3. Expand Section 4.3 with an intuitive explanation of why the random block-diagonal rotation is needed and what goes wrong without it, before deferring the proof to the appendix.

---

## Score and Decision

**Calibration anchors:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| B5kAfAC7hO | 5.33 | R1 (mid) | "Provable Representation for POMDP RL" — Rejected for limited novelty over prior work (Ren et al.); paper under review is more original but weaker empirically |
| KrtGfTGaGe | 4.50 | R1 (mid) | POMDP belief update learning; weaker theory and broader scope than paper under review |
| Q00CO1Tm6M | 5.75 | R1 (mid) | POMDP tractability theory — stronger theory (PAC bounds, hardness), but narrower focus than paper under review |
| Qja5s0K3VX | 6.00 | R1 (mid) | POMDP OPE — accepted; cleaner theory, well-scoped contribution |
| GdTOzdAX5A | 5.75 | R2 | Switching dynamical system identifiability — criticized for results following directly from prior work, weaker experiments; paper under review has more original concepts but smaller experiments |
| wCUw8t63vH | 6.80 | R2 | Spectral learning for shared dynamics — rejected; solid method with real-data experiments, better validated empirically than paper under review |
| kyVzYpDxHg | 5.75 | R2 | Tensor equivariant learning; lower topical similarity |
| 8BAkNCqpGW | 8.00 | R1 (high) | Policy gradient for confounded POMDPs — clearly stronger (non-parametric identification + finite-sample bounds) |

**Round 1 bracket**: 4.5–6.5.

**Round 2 narrowing**: The two closest thematic anchors are GdTOzdAX5A (5.75, identifiability theory with small experiments, criticized for limited novelty) and wCUw8t63vH (6.80, spectral dynamics learning with stronger empirical validation). The paper under review is more novel than GdTOzdAX5A but less empirically complete; it is weaker empirically than wCUw8t63vH (which had real-data experiments, not just ≤10-state toy POMDPs, and did not miss its most important baseline comparison). The paper also lacks the finite-sample PAC bounds present in Q00CO1Tm6M (5.75) and the clean scope of the 6.0-accept Qja5s0K3VX. The missing critical baseline comparison is a genuine Major weakness that prevents the paper from delivering on its own central empirical claim.

**Final positioning**: Slightly below GdTOzdAX5A (5.75) and well below wCUw8t63vH (6.80). The paper is a genuine, sound theoretical contribution but is experimentally underdeveloped in its most important dimension. Score: **5.0**.

**Originality**: Moderate-high. The full-rank observability partition concept and joint diagonalization adaptation are original.
**Importance**: Moderate. Relaxing assumptions on per-action observation uniqueness is meaningful but the problem scope is narrow (discrete POMDPs, tiny domains).
**Support for claims**: Partial. The core theoretical claim is sound; the empirical claim of superiority over prior tensor methods is unverified.
**Soundness**: Good. No errors found in the theoretical argument.
**Clarity**: Good, with the exception of the key algorithmic step in Section 4.3.
**Value to the community**: Moderate. Provides a principled foundation, but practical applicability is undemonstrated beyond toy problems.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>