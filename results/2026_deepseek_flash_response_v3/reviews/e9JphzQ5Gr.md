Now let me write the final consolidated review.

## Summary

CaPT proposes an asymmetric-modalities co-training framework that integrates CLIP into semi-supervised learning. It jointly trains an adapter-tuned multimodal CLIP model and a fully fine-tuned unimodal vision network, fusing their predictions via entropy-weighted co-pseudo labels. The method is evaluated across an extensive set of benchmarks including USB, ImageNet, extreme low-label regimes, and fine-grained datasets.

## Strengths

1. **Well-motivated asymmetric-modalities design (Figure 3, lines 43-51):** The paper provides concrete evidence (attention maps on eight images) that two unimodal ViTs with different initializations still converge to similar attention patterns (the "pattern-homogeneity bottleneck"), while CLIP attends to semantically distinct regions. This directly motivates why cross-modal co-training is more beneficial than the standard two-ViT co-training used in prior work (e.g., CLS).

2. **Extensive and rigorous evaluation (Tables 1-6):** The paper evaluates across 12 SSL baselines on USB benchmark (CIFAR-100, STL-10, EuroSAT), ImageNet (10 and 100 labels/class), extreme one-label-per-class settings, and 6 fine-grained datasets. The ablation study (Table 6) systematically isolates six design choices, cleanly showing each component's contribution. The inclusion of fine-grained datasets (FGVCAircraft, Flowers102, StanfordCars, SUN397, DTD, SVHN) preempts the concern that results are driven purely by CLIP's training-data overlap.

3. **Practical efficiency (Table 4, lines 242-248):** CaPT adds only +8% memory (5050 vs 4676 MiB) and +11% training time (0.1044 vs 0.0939 sec/iter) over the FreeMatch baseline while improving accuracy by +6.23%. Compared to RegMixMatch, CaPT is both cheaper (5050 vs 6578 MiB; 0.1044 vs 0.1484 sec/iter) and more accurate. This directly rebuts the concern that adding a dual-encoder model would be prohibitively expensive.

4. **Strong results in extreme low-label settings (Table 3, lines 234-240):** With one label per class on CIFAR-100, CaPT achieves 82.51% vs 61.13% (FreeMatch) and 60.49% (RegMixMatch). The margin is large and the method's robustness to label scarcity is convincingly demonstrated across multiple datasets.

## Weaknesses

### Major

1. **STL-10 anomaly: Adapter-tuned CLIP alone outperforms the full CaPT framework, and this is not discussed.** From Table 1 (line 193): on STL-10 with 4 labels, adapter-tuned CLIP achieves 96.86% vs CaPT's 96.07%; with 10 labels, 97.15% vs 96.34%. CLIP zero-shot (97.18%) also exceeds CaPT. The paper claims CaPT "leads by 6.18%" on STL-10 (line 210), but this is relative to another SSL method (RegMixMatch, 89.89%), not relative to the simpler baseline of just using adapter-tuned CLIP. The framework's value proposition is that the co-training mechanism is essential — but on STL-10, the simplest possible approach (adapter-tuned CLIP with no SSL pipeline) performs *better*. This directly undercuts the narrative and is not addressed anywhere in the paper.

2. **Gain decomposition is not separated from CLIP's prior.** The headline results (e.g., +21.38% on CIFAR-100 one-shot, +6.18% on STL-10) compare against purely unimodal SSL methods without access to CLIP. While the paper shows "Adapter-tuned CLIP" baselines at the bottom of Table 1, it does not include comparisons against other CLIP-integrated approaches (DebiasPL, CLS) in the main tables, and does not systematically decompose how much of the gain comes from CLIP's prior vs. the specific co-training framework. This makes it difficult to assess the marginal contribution of the framework itself, as distinct from the advantage of simply having CLIP available.

### Minor

3. **Theoretical bound (Theorem 1.1, Eq. 1) is presented with overstated claims.** The bound contains a multiplicative factor of $2^{d/2}$ where $d$ is the input dimension. For any realistic image dimension, this factor is astronomically large. While such bounds are common in GMM analysis and can be meaningful when inter-class distances also scale, the paper does not discuss this limitation, and the claim in Contribution 1 ("theoretically establish the label dependency that constrains SSL") overstates what the bound accomplishes. It is a motivating conceptual illustration, not a substantive theoretical establishment.

4. **CaPT-Uni ablation shows modest bidirectionality gains (Table 6, line 291).** Removing the vision-model→CLIP flow (CaPT-Uni) drops performance by only 0.88% on CIFAR-100 and 1.49% on EuroSAT. The paper emphasizes "bidirectional information exchange" and "richer cross-model information exchange" as key aspects, but the ablation shows the bulk of the benefit is unidirectional (CLIP→vision). This does not invalidate the method, but the framing should be adjusted.

5. **"only MPM" vs "Adapter-tuned CLIP" discrepancy (Table 6: 68.32% vs Table 1: 74.90%).** On CIFAR-100 2-shot, the "only MPM" ablation (removing the unimodal network) gives 68.32%, while the standalone "Adapter-tuned CLIP" reported in Table 1 gives 74.90%. If these represent similar training setups, the 6.58% gap is unexplained. The paper likely uses different training paradigms (SSL consistency loss vs. standard supervised fine-tuning), but this is not clarified.

### Trivial

None.

## Nice-to-Haves

- **Sample-level analysis of co-training dynamics:** The paper uses batch-level entropy weighting but does not show sample-level behavior when the two modules disagree. A per-sample analysis would illuminate when and why the fusion mechanism is valuable.
- **Analysis of why CLIP alone beats CaPT on STL-10:** Understanding this failure mode could sharpen the paper's claims about when the framework is beneficial.
- **Clarify "only MPM" vs "Adapter-tuned CLIP" training differences.**

## Removed Points

These points were flagged during review but are not included as weaknesses in the final assessment:

- *"The comparison is unfair because baselines lack CLIP"* — This is standard practice: comparing a new pipeline against existing pipelines. The paper does show adapter-tuned CLIP baselines. The specific, actionable concern (STL-10 anomaly) is kept as a Major weakness.
- *"Feature-level Mixup asymmetry not discussed"* — The paper explicitly addresses this at lines 135-143, explaining it as a resource-saving choice. 
- *"Entropy-based weighting could allow one module to dominate"* — This is a design feature, not a flaw; the intention is that more confident modules should dominate.
- *"Standard deviations are remarkably small, warranting explanation"* — This is a positive finding of robustness; not a weakness.
- *"Missing related work on co-training"* — Hard rule against flagging missing references.

## Novel Insights

None beyond the paper's own contributions. The review surfaces one observation the paper overlooks: the STL-10 results (adapter-tuned CLIP alone outperforms CaPT) are a natural experiment that could reveal when co-training is not beneficial — which would strengthen the paper if analyzed rather than omitted.

## Suggestions

1. **Address the STL-10 anomaly directly.** Analyze why adapter-tuned CLIP alone outperforms the full CaPT framework on this dataset. Is the unimodal network adding noise? Is the SSL training loop hurting CLIP's representations? This analysis would strengthen rather than weaken the paper by clarifying the boundary conditions of the framework's value.

2. **Include DebiasPL and CLS baselines in the main tables** to enable a fairer comparison against other CLIP-integrated SSL approaches.

3. **Reframe the theoretical contribution** as a motivating conceptual illustration rather than a theoretical establishment, and discuss the bound's limitations (the $2^{d/2}$ factor and the gap between the GMM model and actual SSL practice).

4. **Adjust the framing of bidirectional co-training** to reflect that the primary benefit is CLIP providing a prior to the unimodal network, with more modest additional gains from the reverse direction.

## Calibration Report

**Round 1 (Bracketing):** Retrieved anchors from five score bands (0-2.5, 2.5-4.5, 4.5-6.1, 6.0-7.5, 7.5+). Key anchors:
- SelfPrompt (3.50) — VLM+SSL, rejected. CaPT is clearly stronger.
- LIST (4.00) — Self-training for multimodal alignment, rejected. CaPT is stronger.
- BOPL (5.33) — SSL pseudo-labeling, rejected. CaPT is slightly stronger.
- DIPS (5.00) — SSL data-centric, rejected. CaPT is comparable.
- SemiCLIP (5.80) — CLIP+SSL, accepted. CaPT is slightly weaker due to comparison fairness issues.
- SemiReward (6.00) — SSL reward model, accepted. CaPT has more significant comparison issues.

**Round 1 bracket:** 4.5–6.0

**Round 2 (Narrowing):** Queried inside (4.5, 6.5) with CLIP+SSL focused query. Retained SemiCLIP (5.80) as the closest topical anchor.

**Final score determination:** Compared to SemiCLIP (5.80, accepted), CaPT has stronger technical novelty (asymmetric co-training framework is more novel than concept mining + trapezoidal consistency) and broader evaluation (12 baselines, ImageNet, fine-grained). However, CaPT has the significant STL-10 anomaly and comparison fairness concerns that SemiCLIP does not share. Compared to BOPL (5.33, rejected) and DIPS (5.00, rejected), CaPT has stronger empirical results but similar levels of framing/interpretation issues. **Score: 5.0** — the STL-10 oversight and lack of gain decomposition prevent it from being a clear accept, but the framework novelty and extensive evaluation prevent it from being a strong reject.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>