Now I have enough anchors calibrated. Let me write the final review.

---

## Summary
This paper conducts a systematic empirical study of how reasoning data—varying in scale, diversity, and quality—affects LLM performance when introduced at different training stages (pretraining vs. SFT). The authors train multiple 8B models from scratch under a fully-crossed design, varying pretraining data among four configurations (no reasoning, diverse-only, quality-only, mixed) and SFT data among three types. Key findings: (1) front-loading reasoning into pretraining yields durable gains that intensive SFT cannot match, (2) the optimal data strategy is asymmetric—diversity dominates pretraining while quality dominates SFT, (3) high-quality data added to diverse pretraining mixtures shows a "latent" effect unlocked by SFT, and (4) naively scaling SFT data can be harmful.

## Strengths
- **Fully-crossed experimental design training from scratch.** Unlike prior studies that explore mid-training/continued-pretraining or post-training in isolation, the authors train multiple 8B models from scratch (Section 2.3, Section 3.1), systematically varying data diversity, scale, and quality across *both* pretraining and SFT under a fixed token budget (Eq. 2). This methodological rigor—controlling for budget while isolating phase-specific data effects—is largely absent in earlier proprietary or mid-training-focused work and enables direct measurement of cross-phase synergy.
- **Empirical validation of an asymmetric data allocation principle.** Table 1 shows that large-scale diverse data ($\mathcal{D}_{\text{LDQ}}$) outperforms smaller high-quality data ($\mathcal{D}_{\text{SHQ}}$) by +9.09% average accuracy at the pretraining stage, while Table 5 reverses this relationship at SFT, with quality outperforming diversity by +13.45%. This directly challenges uniform "quality-first" or "quantity-first" heuristics and provides an actionable, stage-dependent heuristic.
- **Rigorous refutation of the "catch-up" hypothesis via controlled ablation.** Table 4 demonstrates that doubling SFT epochs on the baseline ($\mathcal{M}_{\text{base}} + \text{SFT}_{\text{SHQ}}(2\times)$) gains only 4.09% and still trails the weakest reasoning-pretrained model $\mathcal{M}_{\text{SHQ}}$ by 3.32%. This provides concrete, quantified evidence that pretraining establishes foundational reasoning priors that cannot be replicated by intensifying SFT.
- **Actionable sensitivity analysis on ratios and scaling.** Tables 6 and 8 provide direct empirical guidance: increasing the pretraining reasoning ratio from 20% to 40% monotonically improves math (72.37%→79.63%, Table 6), while naively doubling mixed-quality SFT data actively harms math by -4.92% (Table 8). These move beyond qualitative claims to quantify concrete trade-offs.

## Weaknesses
### Fatal
None.

### Major
- **Repetition confound in the diversity-vs-quality comparison (Section 2.3).** The paper states: "When a reasoning dataset is small, it is repeated so that the model still observes the same total volume of reasoning tokens." $\mathcal{D}_{\text{SHQ}}$ (1.2M samples) must be repeated ~200× to fill the 80B reasoning token budget, while $\mathcal{D}_{\text{LDQ}}$ (268M samples) requires ~1× repetition. The performance gap attributed to "diversity" (LDQ beating SHQ by +9.09% in Table 1) could partially arise from effects of extreme repetition—overfitting to narrow reasoning patterns—rather than structural diversity per se. The paper cannot disentangle whether LDQ's advantage comes from seeing diverse reasoning patterns or from avoiding the degradation caused by repeating a small dataset hundreds of times. This is a structural limitation. The comparison is still informative, but the claim that "diversity drives gains" overstates what the experiment isolates.
  
- **The +19% RL gain claim is not fully supported by the evidence.** The abstract and introduction prominently state "front-loading reasoning data into pretraining is critical (19% average gain)," but Table 3—the only table reporting RL results—presents only *two* configurations: $\mathcal{M}_{\text{base}}+\text{SFT}_{\text{SHQ}}+\text{RL}$ vs. $\mathcal{M}_{\text{LMQ}}+\text{SFT}_{\text{SHQ}}+\text{RL}$. The paper's wider claim that RL compounding benefits all reasoning-pretrained models is not empirically demonstrated. If RL amplifies or diminishes specific configurations differently, the aggregate figure is unjustified. The directional claim (RL preserves the gap) is plausible, but the magnitude is extrapolated from a single comparison.

### Minor
- **Overconfident prose for correlational findings.** The paper uses language like "proving that SFT cannot compensate" (Introduction), "This provides conclusive evidence" (Section 4), and "deterministic impact" for findings that are fundamentally empirical and correlational. These phrases overstate the evidence.

- **No statistical variance or multiple-seed results.** Across all tables, single-run values are reported without confidence intervals or seed-averages. Given that model performance can vary by 1-3% across seeds, this undermines confidence in small reported differences (e.g., the +4.25% latent effect in Table 4, or the +3.32% gap in the catch-up refutation).

- **GPR ceiling effect limits the overfitting rebuttal.** The paper claims its GPR results "refute the overfitting hypothesis" (Section 4), but all models score 75-77% on GPR—suggesting a ceiling effect. These tasks may be too easy to detect generalization degradation on non-reasoning capabilities. Harder general-purpose benchmarks would provide a more convincing refutation.

- **Latent effect framing overstates the evidence.** Table 4 shows $\mathcal{M}_{\text{LMQ}}$ gains +4.25% over $\mathcal{M}_{\text{LDQ}}$ after SFT. The paper frames this as revealing "a deeper synergy where pretraining can instill a latent potential in the model that is only activated during alignment." However, $\mathcal{D}_{\text{LMQ}}$ is simply $\mathcal{D}_{\text{LDQ}} + \mathcal{D}_{\text{SHQ}}$ (Section 2.2)—269.2M samples versus 268M. The improvement could partially reflect the marginal benefit of additional high-quality signal in the mix. The "latent potential" narrative is compelling but goes beyond what the experimental isolation supports.

### Trivial
None significant.

## Nice-to-Haves
- **Acknowledge the repetition confound explicitly.** Even if the computational cost of an equal-diversity experiment is prohibitive, the authors should discuss this as a structural limitation and hypothesize how repetition may inflate LDQ's measured advantage over SHQ.
- **Expand RL reporting.** Even a subset of the full 4×3 grid under RL (e.g., at least $\mathcal{M}_{\text{SHQ}}+\text{SFT}_{\text{SHQ}}+\text{RL}$ alongside the existing two) would substantially strengthen the compounding advantage narrative.
- **Report multiple seeds.** At minimum, reporting 3-seed averages/variance for the most critical comparisons (Table 1 pretraining stage, Table 4 catch-up ablation) would add confidence to the small but important differences.

## Removed Points
- **Reviewer's claim that "the first systematic study" is overclaimed.** *Removed.* The paper's comparison to mid-training literature (Section 6) is sufficiently differentiated—the authors explicitly note mid-training operates on existing checkpoints, whereas this work varies data injection during *end-to-end pretraining from scratch*. This distinction is valid.
- **"Token counting needs clarification" as a substantive weakness.** *Removed.* The 80B reasoning token budget and the 80/20 ratio on the final 400B tokens (Section 2.3) are clearly stated. The effective diversity question is interesting but would be scope-creep for the paper's core contribution.
- **Generic claim that "the evaluation lacks rigor."** *Removed.* This was an area-sweep from the harsh critic without a concrete anchor. The evaluation covers math, science, code, and instruction-following across multiple benchmark tiers (including AIME competition-level tasks).
- **Strength finder's "rigorous refutation" strength.** *Retained but noted the overconfident framing in weaknesses (#3).* The evidence is real; the prose just overstates it.
- **Any criticism about missing related works.** *Removed per policy.*
- **Any criticism about missing appendices/proofs.** *Removed per policy* (parser strips these sections).

## Novel Insights
The most genuinely novel observation emerging jointly from the paper and reviews is the identification of a *latent activation* phenomenon: adding a small fraction of high-quality data to a large diverse pretraining mixture (LMQ = LDQ + SHQ) yields indistinguishable results at the pretraining checkpoint (64.07% vs. 64.09% in Table 1) but reveals a +4.25% gap *only after SFT*. This suggests that some properties of early data exposure—perhaps related to the model's capacity to learn and generalize from high-quality reasoning traces—remain dormant until activated by high-quality downstream alignment. This cross-phase dormancy effect is absent from prior isolated-stage analyses and offers a new lens on how pretraining and post-training interact in reasoning model development.

## Suggestions
- Reframe the "latent effect" as "a marginal benefit from mixing high-quality samples into diverse pretraining data, which becomes more visible after SFT" to be more conservatively aligned with what the experiment isolates.
- Add a paragraph in the discussion explicitly acknowledging the repetition confound and its implications for interpreting the LDQ vs. SHQ comparison.
- Include a small RL expansion (even one additional configuration) to substantiate the "+19% average gain" claim.

## Score and Decision

**Round 1 — Bracketing:**
- *Weak anchor (score <3.5):* `SaOxhcDCM3.md` (3.20, self-consuming training loop; more speculative), `E4hK8t7Fts.md` (3.00, math fine-tuning methods; narrow), `pXIbcRPxWR.md` (2.50, supervised CoT; rejected). These are all rejected papers with more speculative or narrower scope than the current paper.
- *Middle anchor (3.5-7.5):* `1hQKHHUsMx.md` (6.75, influence function analysis of pretraining data's role in reasoning; well-executed but narrow scope, only 80 queries), `GtpubstM1D.md` (5.71, math reasoning via CPT/SFT; solid but not training from scratch). 
- *Strong anchor (7.5+):* `KIPJKST4gw.md` (7.25, code data at different training stages; similar topic, systematic 2×2 design with pretraining and instruction-tuning but only 2.6B model, 6 tasks), `NGKQoaqLpo.md` (7.50, new data's impact on LLM knowledge; strong but different topic: knowledge editing/priming).

**Initial bracket: 6.5–7.5.** The paper's fully-crossed design with models trained from scratch at 8B scale is materially stronger than the mid-training-focused `GtpubstM1D.md` (5.71) and the influence-function analysis `1hQKHHUsMx.md` (6.75). It competes with `KIPJKST4gw.md` (7.25) but that paper had a cleaner experimental design (no repetition confound), though at smaller scale (2.6B).

**Round 2 — Narrowing within the bracket:**
- `GtpubstM1D.md` (5.71): Uses continued pretraining on existing models, not training from scratch. Less systematic cross-phase design. The current paper is stronger.
- `cijO0f8u35.md` (5.25): Single-dataset (GSM8K only) scaling study. Reject. The current paper is substantially stronger (multi-domain, from-scratch training).
- `KIPJKST4gw.md` (7.25): Best topical match at 7.25. Code data at pretraining vs. instruction-tuning. Systematic 2×2 design, 6 reasoning tasks, 5 domains. More limited model size (2.6B), smaller benchmarks, some token-counting inconsistency flagged by reviewers. The current paper matches/exceeds it on scale and benchmark breadth but has its own issues (repetition confound, overclaimed RL result).
- `1hQKHHUsMx.md` (6.75): Influence function study, very different methodology. Current paper is stronger on experimental design.

**Comparison:** Against `KIPJKST4gw.md` (7.25), the current paper has larger-scale training (8B vs. 2.6B), more diverse benchmarks, and a more complete pipeline (PT + SFT + RL). However, it carries a real confound (repetition) and overclaims the RL result, whereas the code paper had cleaner isolation despite smaller scale. The current paper is slightly below or at parity with the 7.25 anchor, but clearly above the 6.75 anchor.

**Final score: 6.5.** The paper is a solid, practically useful empirical contribution with a genuine methodological advantage (training from scratch with fully crossed design). The repetition confound is a real structural limitation but not fatal—the comparison remains informative. The overclaimed RL magnitude is a presentational issue. The work is worth accepting but does not reach the strongest tier.

All anchors retrieved:
| Path | Avg Score | Round | Comparison |
|---|---|---|---|
| `SaOxhcDCM3.md` | 3.20 | R1 | More speculative, rejected; paper is stronger |
| `E4hK8t7Fts.md` | 3.00 | R1 | Narrow scope, rejected; paper is stronger |
| `pXIbcRPxWR.md` | 2.50 | R1 | Rejected; paper is stronger |
| `GtpubstM1D.md` | 5.71 | R1/R2 | CPT-based, not from scratch; paper is stronger |
| `cijO0f8u35.md` | 5.25 | R2 | Single-dataset, limited; paper is stronger |
| `1hQKHHUsMx.md` | 6.75 | R1/R2 | Influence function study, different method; paper is stronger on experimental design |
| `KIPJKST4gw.md` | 7.25 | R1/R2 | Closest match; paper is larger scale but has repetition confound; roughly comparable |
| `NGKQoaqLpo.md` | 7.50 | R2 | Different topic (knowledge editing); not directly comparable |

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>