Now I have sufficient calibration. Let me compile my final review.

**Bracket analysis:** Round 1 suggested this paper sits between the weak anchors (avg 1.4–3.0) and the middle anchors (avg 3.75–6.67). Round 2 narrowed the comparison to papers scoring 2.5–4.4. The papers at 2.5–3.0 had similarly shallow methodology but often stronger empirical results (93% ASR on language game attacks). The paper at 4.25 (jailbreak detection) had a more thorough evaluation with clear methodology. The current paper is weaker than the 3.75 anchor and comparable to the 2.5–3.0 anchors. I'll place it at 3.0.

---

## Summary

This paper studies the trade-off between jailbreakability and stealthiness in Vision-Language Models. It contributes: (1) an intra-entropy gap detection algorithm for non-stealthy jailbreak attacks, (2) a diffusion-model-based stealthy attack pipeline, and (3) an information-theoretic framing via Fano's inequality linking attack success and stealthiness. The core idea — that there is a trade-off between how detectable an attack is and how successful it can be — is sound and worth studying. However, the execution across all three pillars is substantially below the bar for acceptance.

## Strengths

- **The proposed attack is genuinely stealthy against the entropy-gap detector.** Table 1 shows near-random AUROC (0.45–0.62) across five scenarios for the authors' own attack, while prior attacks (Li et al., 2024; Liu et al., 2024b) are easily detected (AUROC ≥0.79). This directly supports the claim that the diffusion-based attack embeds malicious content in a way that does not create an entropy imbalance.

- **The detection algorithm catches known non-stealthy attacks.** Algorithm 1 combined with logistic regression achieves AUROC of 0.79–0.99 on the attacks from Li et al. (2024) and Liu et al. (2024b). While these attacks make minimal effort to hide, the method provides a concrete baseline defense.

- **Evaluation across multiple VLMs and settings.** The paper tests on LLaVA, MiniGPT-4, InstructBLIP (white-box), and Gemini and ChatGPT 4o (black-box), showing consistent patterns in the results.

- **Interesting open observation about imperceptible typography.** Figure 6 and the discussion in Section 6 raise an intriguing question ("Do VLMs perceive typography imperceptible to humans?") that connects VLM jailbreaking to broader AIGC detection challenges.

## Weaknesses

### Fatal
None. The paper's claims are not invalidated by a single fatal error; rather they are undermined by a collection of major issues.

### Major

- **The theory section (Section 4.3) is decorative and does not contribute meaningful insight.** Theorem 1 is a direct restatement of Fano's inequality with no adaptation to the jailbreak setting — the paper itself acknowledges this ("The result is derived directly from Fano's inequality"). The Markov chains defined are technically contradictory: the paper writes both $X \to Y_1 \to \hat{X}$ and $X \to Y_2 \to \hat{X}$, but then states that $\hat{X}$ "relies on both the text and image data $Y_1$ and $Y_2$," which neither chain structure alone can represent. Corollary 2 claims that minimizing squared entropy gaps minimizes mutual information $I(X;Y_1,Y_2)$, but this is stated without proof and the connection between entropy gaps of random partitions and mutual information with $X$ is not established. Figures 4 and 5 merely plot the textbook Fano bound numerically under different parameter choices — they contain no empirical measurements of entropies, mutual information, or actual attack data. The Remark lists three implications, two of which are trivial (more modalities → higher success rate; larger blacklist → lower success rate), while the third (entropy gap as a detection feature) is not connected back to any theorem or experiment. The theory section adds no value that a citation to Fano's inequality would not provide.

- **The detection algorithm is evaluated without any baselines.** The paper compares the entropy-gap feature against no alternative detection method — not a simple threshold on raw image entropy, not a pre-trained ViT-based outlier detector, not a frequency-domain analysis, not perplexity-based text detection, and not any prior defense method from the literature (e.g., SmoothLLM, self-reminders, or moderation APIs). Without baselines, there is no evidence that the entropy-gap feature is useful relative to trivial alternatives, and the reader cannot assess whether the reported AUROC values (0.79–0.99 on non-stealthy attacks) represent a meaningful advance or simply the fact that these attacks are trivially detectable by any reasonable method.

- **The attack's success rate is too marginal to demonstrate a meaningful trade-off.** In white-box evaluation on LLaVA (Table 2), the authors' attack achieves an average ASR of 0.39 — only 0.02 above Gong et al. (2023) and 0.05 above "No Attack" (0.34). On several categories (Financial Advice, Health Consultation), the attack shows zero improvement. On black-box models (Table 5), the attack's ASR is *lower* than Li et al. (2024) in 4 out of 5 scenarios on Gemini, and both methods achieve an average of 0.01 on ChatGPT 4o. These results do not demonstrate that the attack is practically threatening or that the trade-off curve is meaningful — they show that a weak attack happens to also be hard to detect. Without an ablation study that isolates each pipeline component (keyword extraction, story generation, typography, diffusion model), the attack is a black box whose design choices cannot be attributed to the claimed trade-off.

- **No ablation studies are conducted anywhere in the paper.** The attack pipeline has four components and the detection algorithm has multiple design choices (partitioning method, number of trials K), yet none of these are ablated. The paper mentions that "detailed comparisons" between diffusion and watermark blending are in Appendix C (which is missing), and that RAKE and LLM keyword extraction "exhibit a high degree of similarity" without quantitative support. The lack of ablations makes it impossible to attribute any empirical observation to specific design decisions.

- **No confidence intervals or statistical testing on key results.** Table 2 (ASR), Table 1 (detection AUROC/F1), and Tables 3–4 (toxicity scores) report point estimates without confidence intervals. Given the small differences being claimed (e.g., ASR of 0.39 vs 0.34 for "No Attack"), this is essential for assessing whether observed differences are meaningful or within noise.

### Minor

- **The LLM-as-judge evaluation metric is not validated.** The paper uses an LLM to assign an "unsafe score" with a threshold of 0.5, but reports no agreement rate with human judgment, no calibration analysis, and no comparison with alternative evaluation protocols (e.g., HarmBench's trained classifier or existing benchmarks like SafeBench's evaluation procedure).

- **The relationship between the entropy-gap feature and human-perceptible stealthiness is unexamined.** The paper uses entropy gap as a proxy for stealthiness but never validates that low entropy-gap images are actually harder for humans to distinguish from natural images. No human study or perceptual metric is included.

- **No discussion of failure cases.** When does the detection fail? When does the attack fail? Understanding failure modes would significantly strengthen the empirical contribution.

### Trivial
None worth noting beyond what is covered above.

## Nice-to-Haves

- A human evaluation study to validate the entropy gap as a proxy for perceptual stealthiness.
- An ablation study isolating each attack component's contribution to success rate and detectability.
- An empirical information-theoretic analysis where mutual information is actually estimated from data (e.g., between image features and harmfulness labels), replacing the current decorative theory section.
- Comparison to perplexity-based text detectors and basic image statistics as detection baselines.

## Removed Points

These points are flagged to be removed; treat with caution:

1. **"The two central claims are at cross-purposes"** — The harsh critic argues the detection and attack framing is incoherent, but the paper explicitly studies a trade-off between jailbreakability and stealthiness, which is internally consistent. Removed as subjective framing, not a verified weakness.

2. **"The detection algorithm is evaluated only against attacks that are trivially detectable"** — The paper states "Our detection method primarily addresses recent jailbreak attacks (Li et al., 2024; Liu et al., 2024b)". This is acknowledged scope, not a flaw per se. However, the *lack of baselines* (retained above) is the real issue.

3. **"First information-theoretic characterization" strength** — Overclaimed. Fano's inequality is a standard textbook result directly restated. While this is the first application to VLM jailbreaking, the adaptation adds no new theoretical machinery. Demoted from strength to non-contribution.

4. **"Figures 4 and 5 validate the bound numerically" strength** — These figures merely plot the formula; they are not an empirical validation. Removed as misleading framing.

5. Various formatting, reproducibility, and appendix-related nitpicks from the harsh critic (missing appendix content that was stripped by the parser). Removed per parsing rules.

## Novel Insights

None beyond the paper's own contributions. The observation that diffusion-embedded typography can jailbreak GPT-4o even when text is nearly invisible (Figure 6) is genuinely interesting, but it is stated as an open question without quantitative backing. The core empirical analysis — that the entropy-gap detector catches non-stealthy attacks and misses the authors' own — is predictable from design and does not reveal an unexpected phenomenon.

## Suggestions

1. Drop the theory section entirely, or replace it with an empirical analysis where information-theoretic quantities are actually measured from data and related to experimental outcomes. The current Fano inequality framing adds nothing and introduces definitional errors.

2. Add at least two detection baselines (e.g., threshold on raw image entropy, off-the-shelf anomaly detector) to Table 1. Without baselines, the detection results are uninterpretable.

3. Conduct an ablation study that varies each attack component independently and measures both ASR and detection AUROC, to attribute the trade-off to specific design choices.

4. Report confidence intervals or standard deviations over multiple runs for all key metrics — especially the ASR results where the claimed improvements are 0.02–0.05 above baseline.

5. Validate the LLM-as-judge evaluation by reporting agreement rates with human annotators on a sample of outputs, or by using a standardized evaluation framework (e.g., HarmBench).

6. If the goal is to demonstrate a fundamental trade-off, sweep a continuous control knob (e.g., diffusion strength, typography opacity) and plot ASR vs. detection AUROC as a Pareto frontier. This would be far more informative than comparing a single operating point against baselines.

## Score and Decision

**Calibration anchors used:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| MV5j4Qpq7N.md (System-Prompt Attention) | 2.33 | R1 | Weaker than present paper |
| 5kMwiMnUip.md (NEMESIS Chain-of-Thought) | 1.40 | R1 | Much weaker, no proper evaluation |
| BeOEmnmyFu.md (Language Game) | 2.50 | R1 | Similar weakness profile but stronger empirical ASR |
| KyKTjRtyNG.md (Incremental Exploits) | 3.00 | R1 | Comparable; both have methodological issues |
| KAWlH5pfQu.md (Detecting Adversarial Examples) | 3.00 | R1 | Comparable |
| wvFnqVVUhN.md (Transferable VLM Jailbreaks) | 6.25 | R1 | Much stronger — comprehensive empirical study |
| RC5x3OkywQ.md (LLM Jailbreak Detection Free) | 4.25 | R1/R2 | Stronger — has clear detection method with baselines |
| JwoCs9O3QL.md (VLMGuard) | 5.00 | R1 | Much stronger — complete framework with ablations |
| x9gCQC3rVA.md (AdvWeb) | 4.40 | R2 | Stronger — well-structured black-box attack |
| w0b7fCX2nN.md (Multi-Round Jailbreaking) | 3.75 | R2 | Stronger — attack achieves 80-90%+ ASR |
| Nazzz5GJ4g.md (Weak-to-Strong Jailbreaking) | 5.40 | R2 | Much stronger — >99% misalignment rate |

**Round-1 bracket:** Between 3.0 and 6.25.

**Round-2 narrowing:** The paper sits below the 3.75 anchor (Multi-Round jailbreaking) and is comparable to the 2.50–3.00 anchors. The paper attempts three contributions but each has fundamental flaws. The 3.75 anchor paper at least demonstrated a working attack with high ASR. The present paper's attack achieves marginal ASR improvement (0.39 vs 0.34 baseline), its detection contribution lacks any baselines, and its theory section is decorative. I place it in the 3.0 range.

**Final score rationale:** The paper tackles an important problem and takes an ambitious three-pillar approach (theory, detection, attack). However, the theory section is a textbook restatement with contradictory definitions, the detection evaluation lacks any baselines, the attack succeeds only marginally above no-attack, and no ablation studies or confidence intervals are provided. The stealthiness evidence (Table 1) and the interesting typography observation (Figure 6) are genuine positives, but they cannot compensate for the structural weaknesses across all three contributions.

MY FINAL SCORE: <score>3.0</score>
MY FINAL DECISION: <decision>Reject</decision>