Now I have sufficient calibration. Let me produce the final review.

---

## Summary

This paper conducts the first systematic empirical study of how reasoning data—varying in scale, diversity, and quality—affects LLM performance when introduced at different training stages (pretraining vs. SFT). Using from-scratch pretraining of an 8B hybrid Mamba-Attention model on 1T tokens, the authors show that (1) front-loading reasoning data into pretraining creates a durable advantage that persists through SFT and RL, (2) the optimal allocation strategy is asymmetric—diverse data helps pretraining while high-quality data dominates SFT, (3) naive scaling of SFT data harms math reasoning, and (4) high-quality pretraining data can have latent effects that only emerge after SFT. The study is the first to jointly control reasoning data across both pretraining and post-training at this scale.

## Strengths

- **Systematic from-scratch pretraining study.** The paper pretrains 8B models from scratch for 1T tokens, varying reasoning data in scale (1.2M → 269.2M unique samples), diversity, and quality, and evaluates through SFT and RL. This is substantially more controlled than mid-training or continued-pretraining studies and provides clean causal evidence that the *timing* of reasoning data matters.

- **Front-loading finding is robustly supported.** Tables 1–3 show that any reasoning-pretrained model outperforms the baseline at every stage: +8.35% after pretraining (Table 1), +9.3% after SFT (Table 2), and +18.57% after RL (Table 3). The RL gap on AIME is +39.32 percentage points (Table 3). This finding is independent of the repetition confound and is the paper's most solid contribution.

- **SFT quality-over-diversity finding is clean and well-controlled.** Table 5 shows that models finetuned on the small, high-quality D_SHQ outperform those finetuned on the large, diverse D_LDQ (44.99% vs 31.54% average). Table 8 shows that doubling mixed-quality SFT data harms math (−4.92%) while a targeted 0.4% addition of high-quality data (D_ALF') yields consistent gains. These comparisons are not confounded by repetition and provide strong evidence for the SFT half of the asymmetric principle.

- **Ratio sensitivity analysis (Tables 6–7).** Varying the reasoning proportion from 10% → 20% → 40% in pretraining shows monotonic improvement on reasoning benchmarks with minimal degradation on general tasks, providing actionable guidance.

- **Three-phase evaluation pipeline (pretraining → SFT → RL).** The RL results (Table 3) demonstrate that the pretraining advantage compounds rather than diminishes through later training stages, directly refuting the overfitting hypothesis.

## Weaknesses

### Major

- **The M_LDQ vs. M_SHQ comparison conflates diversity with data repetition, weakening the "diversity in pretraining" claim.** The paper compares M_LDQ (268M unique samples, diverse, mixed quality) against M_SHQ (1.2M unique samples, high quality, less diverse). To reach the fixed 80B token budget, M_SHQ's data is repeated ~60–80× (estimated from paper's numbers) while M_LDQ's data is not substantially repeated. This confound means the observed +9.09% advantage of M_LDQ over M_SHQ at pretraining (Table 1) cannot be cleanly attributed to "diversity vs. quality"—it could partly reflect overfitting or reduced gradient diversity from extreme repetition in M_SHQ. The paper acknowledges the repetition mechanism ("When a reasoning dataset is small, it is repeated…") but never quantifies the repetition rates, reports validation loss curves, or analyzes whether M_SHQ exhibits memorization. This weakness specifically affects the pretraining leg of the headline "asymmetric principle"; the SFT leg (quality > diversity) remains well-supported.

    *However, the M_LDQ vs. M_LMQ comparison (64.09 vs. 64.07, Table 1) is not affected by this confound (both have ~269M unique samples) and shows that adding high-quality narrow data to a diverse corpus provides no pretraining benefit. This provides partial, indirect support for the diversity-over-quality direction, though it tests whether quality *adds* to existing diversity rather than directly comparing diversity vs. quality.*

- **The "catch-up" test uses a weak intervention.** The paper refutes the catch-up hypothesis by showing that doubling SFT epochs for M_base does not match reasoning-pretrained models (Table 4). While the result is informative, the conclusion is stated too broadly: "SFT cannot compensate for a weak pretraining foundation." Doubling epochs on the same narrow SFT dataset is a limited test; a stronger test would involve scaling SFT data *variety*, using curated multi-stage SFT, or adding an intermediate continued-pretraining phase. The narrow test risks overfitting M_base further, which actually favors the paper's narrative.

### Minor

- **Proxy for reasoning complexity in D_ALF is unvalidated.** The paper uses answer length > 4096 tokens as a proxy for "reasoning complexity" (Section 2.2) to create D_ALF. Long answers can be verbose or repetitive rather than containing deeper reasoning. While D_ALF is used only in secondary ablations (Table 8), the claims about "qualitative expansion vs. quantity-driven scaling" would be stronger with validation that longer answers correlate with reasoning quality (e.g., human judgments or task difficulty).

- **"Latent effect" claim rests on a small delta.** The claim that high-quality pretraining data has "latent effects activated only after SFT" is based on M_LMQ + SFT_SHQ achieving +4.25% over M_LDQ + SFT_SHQ (Table 4). This is a small margin, and an alternative explanation is that M_LMQ contains D_SHQ (1.2M high-quality samples) as 0.4% of its pretraining mix, and the SFT phase reinforces these same high-quality traces—a data overlap effect rather than a genuine "latent" capability. The narrative oversells a modest and ambiguous finding.

- **Proprietary data limits external scrutiny.** The reliance on NVIDIA's internal datasets (D_base, D_LDQ, Nemotron-Pretraining-SFT-v1) is understandable for an industry lab, but the confounding repetition issue is exacerbated by the lack of transparency on exact token counts, per-dataset repetition epochs, and pretraining loss trajectories for each variant. Reporting these would substantially strengthen reproducibility.

### Trivial

- None beyond the formatting artifacts introduced by PDF extraction.

## Nice-to-Haves

- A control experiment where D_LDQ is subsampled to the same size as D_SHQ (1.2M unique samples) and repeated to match its repetition rate would cleanly isolate the diversity effect. Alternatively, a control where D_SHQ is augmented with synthetic diversity to match D_LDQ's coverage would also be informative.
- Quantifying the exact repetition rates and reporting validation-set loss curves for each pretrained model would help assess whether M_SHQ's performance is degraded by overfitting.
- A stronger catch-up experiment using a larger, more diverse SFT corpus (rather than just 2× epochs) would strengthen the claim that post-training cannot compensate for weak pretraining.

## Removed Points

The following points from the inputs are removed with justification:

1. *"Cherry-picked numbers in abstract"* (Harsh Critic) — REMOVED. The 19% gain (Table 3) is the overall average across all RL tasks, and the 11% gain approximates the M_LDQ vs. M_SHQ gap. Neither is selectively chosen from the widest gaps; both are standard comparisons reported in the paper's tables.
2. *"Fatal structural flaw invalidates the asymmetric principle"* (Harsh Critic) — DEMOTED to Major. The confound is real, but the M_LDQ vs. M_LMQ comparison (unconfounded) provides partial support, and the SFT leg of the principle is independently supported. The paper's central finding (front-loading helps) is unaffected.
3. *"Catch-up hypothesis test is a straw man"* (Harsh Critic) — DEMOTED to Minor. The test is limited but not a straw man; it is a straightforward, interpretable intervention. The conclusion merely needs to be scoped more precisely.
4. *"Reproducibility concerns about unreleased data"* (Harsh Critic) — MODIFIED/REMOVED per policy. The paper cites released resources; concerns about data transparency are kept but softened.
5. Various generic strength statements from the Strength Finder (e.g., "important problem," "well-written") — REMOVED as they lack specific evidence anchors or are too generic.

## Novel Insights

The most interesting insight that emerges from the reviews is that the paper's own data provides *two* independent tests of the "diversity over quality in pretraining" claim—one confounded (M_LDQ vs. M_SHQ) and one clean (M_LDQ vs. M_LMQ). The fact that both point in the same direction suggests the diversity finding is likely real but needs tighter experimental verification. The review process also surfaces a tension that the authors could productively address: the paper's strongest contributions (front-loading is beneficial; SFT quality matters more than quantity) are somewhat decoupled from its most novel claim (the asymmetric principle), and the paper would be more robust if it explicitly separated these contributions and acknowledged the limitations of the evidence for each.

## Suggestions

1. **Redesign or reframe the diversity comparison.** Either (a) run a control where D_LDQ is subsampled to 1.2M unique samples and repeated to match D_SHQ's repetition rate, then compare M_(LDQ-subsampled) vs. M_SHQ to isolate diversity from repetition; or (b) explicitly frame the pretraining finding as "scale and diversity" rather than "diversity vs. quality," and acknowledge the confound transparently.

2. **Quantify repetition effects.** Report the exact repetition epochs for each dataset, and provide validation loss curves or overfitting metrics for M_SHQ to demonstrate whether extreme repetition caused memorization.

3. **Scope the catch-up conclusion.** Replace "SFT cannot compensate" with "SFT with more epochs on the same narrow data cannot compensate"—the current framing overstates what one intervention can support.

4. **Validate the D_ALF proxy.** Show that answer length > 4096 correlates with reasoning quality (e.g., human ratings, task difficulty, or number of reasoning steps) on a sample of the corpus.

5. **Soften the "latent effect" narrative.** The 4.25% delta for M_LMQ over M_LDQ after SFT could plausibly reflect data overlap rather than a general latent capability. Frame it as "preliminary evidence consistent with a latent effect" rather than a confirmed finding.

## Score and Decision

**Calibration summary:**

| Anchor | Score | Decision | Round | Comparison |
|--------|-------|----------|-------|------------|
| mfTM4UdYnC (LogicJitter) | 2.50 | Reject | R1 | Much weaker; unserious methodology |
| qgLyKwXVDs (FreeLM) | 2.00 | Reject | R1 | Much weaker |
| EVa5OIYBoG (Expanding the Web) | 3.67 | Reject | R1 | Weaker; narrower scope, less rigorous |
| 8uXkyWFVum (Amuro and Char) | 4.20 | Reject | R1 | Weaker; smaller scale, less controlled |
| aP3OBwf8dk (Plan Early) | 6.00 | Reject | R1 | Comparable score but rejected for different reasons (limited novelty) |
| GtpubstM1D (Advancing Math Reasoning) | 5.71 | Accept | R2 | Slightly weaker; narrower math focus, wider score spread |
| 1hQKHHUsMx (What Kind of Pretraining Data) | 6.75 | Accept | R1 | Different methodology (influence functions), similar overall quality |
| KIPJKST4gw (At Which Training Stage Code Data) | 7.25 | Accept | R1 | Slightly stronger; cleaner experimental design, but smaller model |
| 5HCnKDeTws (When Scaling Meets Finetuning) | 6.75 | Accept | R2 | Comparable; similar thoroughness, different topic |
| 3OyaXFQuDl (Smaller Weaker Yet Better) | 7.00 | Accept | R2 | Stronger experimental design but narrower scope |

**Round 1 bracket:** The paper sits well above the 2–4 range (weak rejects) and below the 8.0 range (exceptional accepts). Initial bracket: (5.0, 7.5).

**Round 2 narrowing:** Comparing against the most topically similar anchor—"At Which Training Stage Does Code Data Help LLMs Reasoning?" (7.25)—the paper is slightly weaker due to the repetition confound, which is more central to the claims. Compared to "Advancing Mathematical Reasoning" (5.71), the paper is substantially more comprehensive. The confound is real but does not invalidate the paper's overall contribution, as the front-loading finding and SFT findings are independently supported. Final score anchored between the 5.71 and 7.25 anchors, closer to the former because the confound affects the headline contribution.

**Final position:** 6.0. The paper makes a solid empirical contribution through its systematic from-scratch pretraining study, confirming that front-loading reasoning data creates a durable advantage. The asymmetric principle is a compelling hypothesis but is weakened by the confound in the pretraining diversity comparison. The SFT-side evidence is clean and valuable. The paper would benefit from a revision that addresses the confound and softens the strongest claims.

<score>6.0</score>
<decision>Accept</decision>