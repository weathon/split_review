## Summary

INFO-SEDD is a novel mutual information (MI) and entropy estimator for high-dimensional discrete data, built on the continuous-time Markov chain (CTMC) / discrete diffusion framework. The central contribution is the application of Dynkin's formula to the log-ratio of two evolving distributions, yielding a tractable KL divergence estimator (Equation 5). A key architectural insight—exploiting absorbing noise so that a single score model trained on the joint distribution can also compute marginal scores (Equation 6)—eliminates the need for a second model. The method yields two variants (INFO-SEDD-J and INFO-SEDD-C) and is validated on synthetic benchmarks, text summarization, and genomics.

---

## Strengths

- **Rigorous CTMC-based formulation with error decomposition.** Section 3 (Equation 7) provides an explicit bound on the estimation error: it decomposes into an estimation error scaling linearly with the score approximation error and a truncation bias that vanishes exponentially as the absorbing state probability approaches 1. This establishes consistency of the estimator and is a meaningful theoretical guarantee.

- **Strong empirical accuracy on high-MI, high-dimensional synthetic data.** Table 1 shows INFO-SEDD-J recovering ground-truth MI up to 50 nats (e.g., 47.77 ± 1.18 at MI=50, D=50) while all competing methods collapse (e.g., GAN-DIME drops to 17.27, MINE/NWJ/KL-DIME plateau near 6–7 nats). This directly validates the paper's core claim of robustness where existing estimators fail.

- **Efficient single-model design via absorbing noise.** Equation 6 is a non-obvious mathematical result: when absorbing transition matrices are used, the marginal score ratios are recoverable from the joint score model by conditioning on the absorbing state. This reduces the training overhead from two models to one and is the practical backbone of INFO-SEDD-J's scalability.

- **Consistent MI estimation on real text summarization data.** Figure 1 shows INFO-SEDD variants tracking the expected linear growth with ρ across 0–1, matching the empirical entropy-rate range of 256–303 nats derived from prior work, while variational baselines (HD-DIME, KL-DIME, SMILE) either underestimate severely or exhibit non-monotonic behavior.

- **Genomics domain consistency and motif discovery.** In Figure 4, INFO-SEDD-C closely tracks the classifier-based MI reference across all ρ values on a DNA classification task. In Figure 5, INFO-SEDD correctly localizes the TATA-box motif in *Arabidopsis thaliana* promoter sequences with a clean MI profile, exploiting the method's ability to estimate MI over subsets without retraining.

---

## Weaknesses

### Fatal
None.

### Major

- **INFO-SEDD-J exhibits a substantial positive bias at ρ = 0 in the text consistency test, and the paper's guidance on when to use each variant is insufficient.** From Figure 1, at ρ = 0 (randomly paired text–summary, so true MI ≈ 0), INFO-SEDD-J estimates approximately 10² nats. The paper acknowledges this in a single sentence ("Note that INFO-SEDD-C obtains MI estimates closer to zero than the joint variant, when ρ = 0.0") but provides no diagnosis. The most plausible explanation—that both X and Y are drawn from overlapping English text distributions, so the joint score model cannot distinguish random pairing from shared distributional structure—is never discussed. This has a direct impact on Table 2: INFO-SEDD-J achieves a Pearson correlation of 0.550 with consistency vs. INFO-SEDD-C's 0.740, but if INFO-SEDD-J's estimates carry a large distributional-similarity offset, the 0.550 figure may reflect that artifact rather than genuine MI. The paper presents both variants as co-equal options without adequately warning practitioners against INFO-SEDD-J in domains where X and Y share the same distributional family.

### Minor

- **The synthetic benchmark is constructed exclusively in the regime MI = D (one nat per dimension), which is favorable to INFO-SEDD's per-token factorized structure.** Every row in Table 1 satisfies MI = D (MI=10/D=10, MI=20/D=20, …, MI=50/D=50), meaning MI is uniformly distributed one nat per position pair—precisely where the sparse rate matrix factorization is optimal by construction. The case of concentrated MI (e.g., MI=40, D=10) is never tested in the main paper. The real-world experiments partially compensate for this (text and DNA involve complex dependencies), but Table 1 alone cannot be taken as evidence of robustness to non-factorized MI structures. This should be noted clearly.

- **The motif discovery result (Figure 5) lacks any competitor comparison.** The paper justifies this by noting that "other MI estimators would need different training runs for each window, whereas INFO-SEDD natively supports MI estimation between subsets." This is a legitimate and practically important advantage. However, it does not establish whether a competitor—given per-window retraining—would also localize the TATA-box, which is the implicit claim. The motif discovery result is presented purely descriptively for INFO-SEDD alone.

### Trivial

- Section 2.2 states "We omit the term E[log(p₀/q₀)(X₀)], as both p₀ and q₀ converge to π." Strictly speaking, this term vanishes only approximately (bounded by the truncation bias in Equation 7), not exactly. The Equation 7 error bound is self-consistent, but the phrasing in the main text is slightly imprecise.

---

## Nice-to-Haves

- A targeted synthetic experiment with concentrated MI (e.g., MI=40 with D=10 where correlation is non-factorized) would test whether the absorbing CTMC approximation degrades gracefully or catastrophically outside the MI=D regime.
- A direct investigation and explicit discussion of the INFO-SEDD-J positive-bias mechanism for text would sharpen practitioner guidance. If the bias is systematic, the authors should recommend INFO-SEDD-C as the default for domains where X and Y are from the same distributional family.
- The Ising model entropy experiments in the appendix (which offer rare exact ground-truth validation) would strengthen the main paper's case if even a summary were included in the main body.
- Clearer guidance in Section 3 or a practical discussion on when to prefer INFO-SEDD-C vs. INFO-SEDD-J, given the materially different behavior observed in Figure 1 and Table 2.

---

## Removed Points

*These points are flagged to be removed — treat them with caution.*

- **Harsh Critic: "The training protocol for consistency tests is underspecified (whether a single model or ρ-specific models are used)."** The paper states the backbone is MDLM-SMALL and describes training in Section 4.2 and Appendix C.2. The natural reading is that one model is trained and evaluated at all ρ via test-time pairing, which is standard. The confound the critic raises (that ρ=1 training would fail to score ρ=0 pairs correctly) is speculative rather than verified from the paper. Removed as speculative-fatal.

- **Harsh Critic: "The genomics advantage may reflect how poorly embedding-based continuous estimators interact with CADUCEUS's output space rather than a general advantage."** The paper explicitly states "we use a pretrained CADUCEUS model for the backbone of all methods" ensuring a level playing field. The critic's observation is a general epistemological caution, not an identified flaw. Removed as generic.

- **Harsh Critic: "Section 5's extension to mixed continuous/discrete data understates technical challenges."** This is a forward-looking remark in the Conclusion; the paper explicitly frames it as future work. Removed as scope creep.

- **Harsh Critic: "No empirical validation of the D|χ| bound's tightness is offered."** The paper provides empirical sample complexity results (Appendix C.1.5) and the bound is standard in the style of the CTMC literature. Demanding tightness experiments for a theoretical bound in an empirical systems paper is beyond the community norm. Demoted and removed.

- **Strength Finder strengths about "important problem" and broad applicability** — removed as generic per filtering rules. Kept only the concrete evidence-backed strengths above.

---

## Novel Insights

The most genuinely novel observation synthesized across both reviewers is the absorbing-noise marginal extraction trick (Equation 6) and its practical consequence: discrete-native MI estimation can achieve what neither continuous embeddings nor per-model training can do simultaneously—scale to high MI while leveraging a single pretrained model for both joint and marginal scores. The INFO-SEDD-J calibration bias at ρ=0 in text reveals a subtle but important limitation: when both variables are drawn from the same distributional family (English text), the joint score model cannot cleanly separate MI from distributional overlap, suggesting that INFO-SEDD-J is best reserved for settings where the marginals are structurally dissimilar (e.g., DNA sequence vs. binary label), while INFO-SEDD-C is the preferred and more robust variant for homogeneous-domain pairs.

---

## Suggestions

1. **Add a non-factorized synthetic experiment**: Test at least one configuration where MI > D (e.g., MI=20, D=5, so 4 nats/dimension with cross-dimensional correlations) to characterize how INFO-SEDD behaves outside the MI=D regime.
2. **Diagnose and communicate the INFO-SEDD-J bias**: Add a short paragraph in Section 4.2 or the Discussion explaining why INFO-SEDD-J has a non-zero intercept at ρ=0, and add a practical recommendation (e.g., "Use INFO-SEDD-C when X and Y are drawn from the same domain").
3. **Motif discovery framing**: Add a brief discussion of what a competitor with per-window retraining would theoretically require, to contextualise INFO-SEDD's practical uniqueness in that application.
4. **Move Ising model entropy results to main body**: Even a single-row summary table of entropy estimates vs. exact values would provide an important independent verification of the estimator under ground truth.

---

## Axes Evaluation

- **Originality**: High. The application of Dynkin's formula to CTMC-based KL divergence for discrete MI estimation, and especially the absorbing-noise marginal extraction, are non-obvious and original within the MI estimation literature.
- **Importance of research question**: High. Scalable MI estimation for discrete, high-dimensional data is a genuine bottleneck in genomics, NLP, and neuroscience.
- **Claims supported**: Mostly well-supported. The core claim (INFO-SEDD outperforms embedding-based alternatives) is strongly backed by Table 1, Figures 1 and 4. The INFO-SEDD-J bias and the non-factorized regime gap are real but do not undermine INFO-SEDD-C's validity.
- **Soundness of experiments**: Good. Multiple settings, real-world domains, and explicit baselines. Weakened slightly by the synthetic benchmark's MI=D design and the absence of a competitor curve in Figure 5.
- **Clarity of writing**: Good overall; the methods and derivations are clearly presented.
- **Value to the research community**: High. INFO-SEDD-C is a practical tool with clear advantages, and the codebase integration with pretrained models (MDLM, CADUCEUS) lowers the barrier to adoption.

---

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>4</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>4</soundness>
<clarity>4</clarity>
<community_value>4</community_value>
</subscores>