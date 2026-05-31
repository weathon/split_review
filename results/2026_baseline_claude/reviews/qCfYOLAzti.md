## Summary
This paper identifies a failure mode called the "squeezing effect" in gradient ascent (GA)-based LLM unlearning: suppressing a target response forces probability mass to redistribute into semantically related high-likelihood regions, causing models to generate paraphrases of the supposedly forgotten content—what the authors term "spurious unlearning." To address this, the paper proposes a bootstrapping (BS) framework that incorporates the model's own high-confidence predictions ("model beliefs") as additional unlearning targets. Two instantiations are introduced: BS-T (token-level soft targets that penalize the top-k neighborhood) and BS-S (sequence-level augmentation with high-confidence samples), along with theoretical analysis under the AKG learning dynamics framework and experiments on TOFU, MUSE, and WMDP.

---

## Strengths

- **Identifies a genuine and underexplored failure mode.** The squeezing effect is a real phenomenon rooted in softmax normalization. The paper supports it with two complementary lines of evidence: qualitative case studies (Cases 1–2) where classical metrics declare success while the model still leaks sensitive knowledge, and mechanistic log-probability dynamics (Fig. 2) showing that GA/NPO consistently amplify high-likelihood neighbors when suppressing targets.

- **Principled and well-motivated solution.** The bootstrapping idea cleanly follows from the diagnosis: if mass shifts to high-confidence regions, suppress those regions too. Both BS-T (soft label mixing) and BS-S (data augmentation from model samples) are natural operationalizations. The two variants are complementary in scope (local token vs. global sequence) and both can be composed with existing objectives (NPO, WGA, GradDiff).

- **Non-trivial theoretical support.** Theorem 5.2 shows formally that the GA residual reallocates mass to neighboring tokens while the BS-T residual distributes repulsion across both the target and top-k alternatives, directly connecting the theory to the squeezing effect diagnosis. Theorem 5.3 extends this cleanly to off-policy BS-S.

- **Broad empirical coverage.** Three benchmarks (TOFU, MUSE, WMDP), three model families (Llama 2, Llama 3, Zephyr), and multiple forget percentages are covered. BS-S delivers the best aggregate score on TOFU across 1B/3B/8B scales and achieves a better forget/retain trade-off on WMDP. Integration into OpenUnlearning signals practical utility.

- **Better evaluation methodology.** The paper raises a valid critique of ROUGE/probability metrics and introduces LaaJ evaluation measuring Naturalness and Similarity, which is shown to better capture spurious unlearning (Fig. 4c). This meta-contribution benefits the wider community.

---

## Weaknesses

### Fatal
None.

### Major

- **Squeezing effect analysis is validated in a narrow setting.** Figure 2's mechanistic analysis (log-probability dynamics, semantic similarity across likelihood bands) is shown for a single benchmark (TOFU) and model (Llama 3.2 1B). The paper asserts that spurious unlearning and the squeezing effect are systematic phenomena, but Fig. 2 only shows NPO vs. retrain in one configuration. Demonstrating this across at least one other benchmark (e.g., WMDP, which involves hazardous knowledge with qualitatively different structure) and one larger model would significantly strengthen the foundational claim.

- **BS-S design is underspecified and computationally opaque.** The paper mentions "temperature-controlled decoding" and both off-policy and on-policy variants of BS-S, but does not specify what temperature is used, how N (number of generated sequences) is chosen, or when to prefer on-policy over off-policy sampling. The computational cost of generating N sequences per forget sample per step is not analyzed or reported. Given that practitioners will need this information to reproduce and deploy BS-S, the omission is a meaningful gap.

- **LaaJ evaluation lacks validation at scale.** The paper correctly critiques classical metrics and introduces LaaJ as a better alternative, demonstrating its usefulness in a handful of qualitative cases. However, the systematic LaaJ comparison in Fig. 4c covers only TOFU. The claimed advantage of LaaJ over ROUGE/probability is not quantified across MUSE and WMDP, making it hard to assess whether the gains reported in Tables 1–3 correspond to genuine rather than spurious unlearning in those settings.

### Minor

- **Hyperparameter sensitivity is unaddressed.** BS-T introduces λ_BST and k (top-k), while BS-S introduces λ_BSS and N. The paper does not include an ablation over these parameters. Even a small grid study on TOFU would clarify robustness and guide practitioners.

- **On-policy vs. off-policy BS-S.** The off-policy variant is theoretically analyzed (Theorem 5.3), but it is not clear whether the reported experiments use off-policy or on-policy sampling, or whether both are evaluated. This distinction matters practically (cost) and theoretically (distributional shift during training).

### Trivial
- The semantic similarity analysis in §3.2 partially defines "high-likelihood regions" through the same mechanism being attributed to the squeezing effect, creating mild circularity in the argument. A small additional probe (e.g., embedding-space nearest-neighbor analysis) would make the claim more independent.

---

## Nice-to-Haves
- An explicit wall-clock or flop comparison of BS-S vs. baselines would help readers understand the efficiency trade-off.
- Showing failure cases of BS-S (prompts where even sequence-level bootstrapping fails) would clarify the remaining limitations.
- The MUSE table appears to be missing from the parsed version; ensuring those results are clearly discussed in the main text would round out the experimental story.

---

## Novel Insights
The central insight—that LLM unlearning can be systematically defeated by softmax-induced mass redistribution, and that the model's own high-confidence outputs precisely locate the regions into which this mass escapes—is a clean and actionable observation. The "bootstrapping" framing, where the model's beliefs are turned against itself as unlearning targets, offers a self-correcting loop absent from prior GA variants. While the individual components (soft labels, data augmentation, learning dynamics analysis) are individually known, their synthesis specifically for the unlearning squeezing problem is original. The theoretical connection between the AKG residual structure and the squeezing phenomenon (Theorem 5.2) provides a transparent formal account that can guide future unlearning objectives.

---

## Suggestions
- Add squeezing-effect analysis (Fig. 2–style dynamics) for at least one non-TOFU benchmark to establish the generality of the core claim.
- Report wall-clock training time for BS-S and specify whether experiments use on-policy or off-policy sampling with explicit N and temperature.
- Include a hyperparameter sensitivity table for λ_BST, λ_BSS, k, and N on TOFU to guide reproducibility.
- Extend LaaJ evaluation to MUSE and WMDP to validate that the gains in classical metrics also correspond to genuine unlearning in those settings.

---

## Score and Decision

The paper makes a genuine and well-supported contribution to LLM unlearning: the squeezing effect diagnosis is convincing, the bootstrapping solution is principled and practically integrated, the theory is nontrivial, and the empirical coverage is broad. The main gaps—narrow mechanistic validation, underspecified BS-S, and limited LaaJ evaluation—are resolvable and do not undermine the core claims, but they reduce confidence in the full scope of the contribution.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>