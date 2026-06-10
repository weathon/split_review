## Summary

DRDO (Direct Reward Distillation and policy-Optimization) proposes combining two training signals into a single preference optimization loss: (1) squared-error regression of the student policy's implicit reward differences onto an Oracle reward model's reward differences, and (2) a focal-softened contrastive log-unlikelihood term that upweights gradient updates when the policy is uncertain about the preference label. The method is motivated by an analysis arguing that DPO and e-DPO produce degenerate policies on non-deterministic (ambiguous) preference pairs.

## Strengths

1. **Novel adaptive-weighting preference loss** (Eq. 7). The focal-softened term $(1-p_w)^\gamma$ is a clean, well-motivated mechanism. When the policy is uncertain ($p_w \approx 0.5$), the gradient is amplified; when confident ($p_w \approx 1$), it is tempered. This directly operationalizes the paper's stated goal of handling diverse preference strengths, and is a genuine addition beyond DPO's fixed $\beta$.

2. **Consistent multi-benchmark evaluation with independent judges on two of three benchmarks.** The TL;DR summarization results (Table 1, GPT-4o judge) and AlpacaEval results (Table 3, GPT-4 Turbo judge) both use judges that are independent of DRDO's training objective. Across all TL;DR training splits, DRDO achieves ~79–81% win rates against DPO and e-DPO, providing credible non-circular evidence that DRDO produces preferred outputs.

3. **Creative experimental design for non-deterministic preferences.** The construction of $\mathcal{D}_{hc,he}$ and $\mathcal{D}_{\ell c,\ell e}$ splits based on labeler confidence and edit distance is a reasonable proxy for isolating deterministic vs. non-deterministic preference pairs, and evaluating on OOD CNN Daily articles is a sensible stress test.

4. **Reference-model-free training.** Unlike DPO and e-DPO, DRDO does not require loading a separate $\pi_{\text{ref}}$ during training, which reduces memory footprint.

5. **Candid limitations section.** The paper honestly acknowledges dependence on Oracle quality, the strictness of theoretical assumptions, and the proxy nature of the non-determinism operationalization.

## Weaknesses

### Major

1. **Ultrafeedback evaluation uses the Oracle as judge — a circularity that inflates the headline results.** Table 2 caption states win rates are "computed with DRDO's Oracle reward model." DRDO's loss (Eq. 7) includes a term that explicitly regresses the student's reward differences onto this same Oracle's reward differences. Evaluating DRDO vs. baselines (DPO, e-DPO) with this Oracle is therefore measuring how well the student mimicked the teacher, not whether it learned better general preferences. The "88% win rate against DPO with Phi-3" is the paper's most striking numerical claim, but it is uninformative as evidence of superior alignment. The TL;DR and AlpacaEval results use independent judges and are not affected, but their margins are more modest (~62% on AlpacaEval). This remains the paper's most significant evidential weakness.

2. **No ablation studies isolating loss components or hyperparameters.** The DRDO loss (Eq. 7) has two distinct terms (reward difference regression + focal contrastive loss) and two hyperparameters ($\alpha$ and $\gamma$). The Oracle loss (Eq. 6) has its own $\alpha$. None of these are ablated. The reader cannot tell:
   - What DRDO achieves with only the reward distillation term (no preference loss) or only the preference loss (no distillation).
   - How performance varies with $\gamma$ — the core adaptive mechanism.
   - Whether both components interact positively or one dominates.
   Without ablations, the paper cannot attribute gains to the proposed mechanism over simpler alternatives.

### Minor

3. **Missing comparison against IPO, the most directly relevant baseline.** IPO (Azar et al., 2023) is discussed in related work and uses a regression-based objective specifically designed to address DPO's handling of preference strength — the exact problem DRDO targets. Its absence from the experimental comparison is a significant gap. Comparing only against DPO and e-DPO sets a low bar for the paper's central claim.

4. **Consistent margins across all TL;DR splits undercut the specific mechanistic claim.** If DRDO's advantage were specifically about handling non-deterministic preferences, one would expect a larger margin on the $\mathcal{D}_{\ell c,\ell e}$ ("hard") split than on $\mathcal{D}_{hc,he}$ ("easy"). In Table 1, the win rates are nearly uniform: DRDO vs. DPO ranges from 79.11% (easy) to 79.79% (hard), and DRDO vs. e-DPO ranges from 80.92% (easy) to 79.01% (hard). The uniformity across splits suggests DRDO may simply be better overall rather than specifically addressing non-deterministic preferences as theorized.

5. **Proposition 1 and the lemmas are weaker than claimed.** Proposition 1 states that for non-deterministic preferences $P(y \succ y'|x) \approx 1/2$, the Bradley-Terry model assigns $\Delta r = 0$. This is a direct consequence of the BT definition $p = \sigma(\Delta r)$, not a finding. Lemma 1 and Lemma 2 make non-trivial claims about DPO/e-DPO optimal policies on finite data, but the main text provides only the claims without derivations. The paper's claim of "thorough theoretical grounding" (contribution 2) overstates what is demonstrated on the page.

6. **Oracle training loss asymmetry is unexplained.** The language-generation regularization term in Eq. 6 only models the log-likelihood of the *winning* response $y_w$, not both $y_w$ and $y_l$. This asymmetry could bias the Oracle toward assigning higher rewards to responses that resemble the preferred data distribution — a confound that is not discussed.

7. **Cherry-picked qualitative examples.** The qualitative example in Table 4 shows a competitor response containing "If you disagree, you're wrong, and you should go back to English class" — a clearly and obviously bad output. Demonstrating improvement over such a low bar is uninformative for assessing genuine performance differences.

### Trivial

- The cross-references to ``\Cref{sec:hyperparameters}'' and ``\Cref{app:*}'', and the struck-through large block (\iffalse ... \fi, lines 86–121 and 387–453) indicate placeholder sections that were presumably filled in the full submission; they appear as vestigial artifacts in the extracted text.

## Nice-to-Haves

- Ablations isolating the two loss components and sweeping $\gamma$ values would substantially strengthen the paper.
- Adding variance estimates (e.g., 3 random seeds with win-rate ranges) for the TL;DR and AlpacaEval results would improve evidential quality.
- Analyzing the Oracle's reward accuracy (e.g., agreement with held-out human judgments or RewardBench) would help readers assess whether the distillation target is worth emulating.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"Gold vs. DRDO comparison shows DPO is closer to human summaries"** (harsh critic). The critic reversed the numbers. Gold beats DPO 58.54% of the time and beats DRDO 52.82% of the time. This means DRDO summaries are *closer* to human quality than DPO summaries, consistent with the paper's claims. Removed as factually wrong.
- **"No hyperparameter values reported."** The paper states hyperparameters are in \Cref{sec:hyperparameters} (stripped appendix). Hard rule: remove criticisms about missing appendix content.
- **"Theoretical analysis incomplete without proofs."** The proofs are in the appendix (stripped). Hard rule: remove. However, the criticism of what IS in the main text (Proposition 1 being a tautology) is retained as Minor weakness 5.
- **"Statistical significance / variance not reported."** Single-run GPT-judge evaluations without confidence intervals are standard practice at this venue. The point is demoted to a Nice-to-Have rather than a weakness.
- **"Missing related works"** and **"Reproducibility concerns about undisclosed hyperparameters"**: Removed per hard rules.
- **"Formatting/style nitpicks"**: Removed per hard rule.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Re-evaluate Ultrafeedback using an independent judge** (GPT-4, or held-out human evaluations) or at minimum clearly flag the circularity and separate those results from claims about general superiority.
2. **Add ablation studies** isolating the reward distillation term, the focal contrastive term, and sweeping $\gamma$ (e.g., $\gamma \in \{0, 0.5, 1.0, 2.0, 5.0\}$).
3. **Add IPO as a baseline**, since it is the most directly relevant regression-based preference optimization method targeting the same limitation.
4. **Acknowledge the uniform margins across splits** in the discussion and address what this means for the specific mechanism claim.
5. **Report win rates with confidence intervals** (e.g., bootstrap CIs) for the TL;DR and AlpacaEval results.

## Score and Decision

The paper proposes a well-motivated method and provides some non-circular evidence (TL;DR with GPT-4o, AlpacaEval with GPT-4 Turbo) that DRDO outperforms DPO and e-DPO. However, the headline Ultrafeedback results are compromised by a circular evaluation, the absence of ablations makes it impossible to attribute improvements to the proposed mechanism, and a key directly-relevant baseline (IPO) is missing. These are major but addressable weaknesses. The method is clearly presented and the core idea is sound.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>