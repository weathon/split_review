Now I have enough data to make a final calibration. Let me write the final review.

**Round 1 bracket**: Based on bracketing, MoRE sits clearly above the rejected unlearning papers (SUN at 4.0, Deep Unlearning at 5.25) and above the accepted LAF at 6.0. My initial bracket: 6.5-8.0.

**Round 2 narrowing**: Comparing against anchors in the 6.0-8.0 range:
- MoRE is clearly stronger than "Jogging the Memory of Unlearned LLMs" (6.75, accepted) which is an attack paper
- MoRE is comparable to "Proactive Privacy Amnesia" (7.00, accepted) — MoRE has a more novel method and more striking results but with acknowledged fragility
- MoRE is comparable to "Utility and Complexity of Machine Unlearning" (6.60, accepted) — different strengths (MoRE is more empirical, that paper more theoretical)

**Final score: 7.0** — A strong contribution with novel methodology, striking empirical results surpassing the retrain gold standard, and efficiency. The target-class sensitivity and single-attack evaluation are real but partially mitigated limitations.

---

## Summary
This paper proposes MoRE (Mixture of Remapping Experts), a training-free framework for feature-level machine unlearning that combines prototype-orthogonal (PO) projection with remapping of forget prototypes to multiple remain prototypes via a mixture-of-experts architecture. Experiments across CIFAR-10, CIFAR-100, Tiny-ImageNet, and Stable Diffusion concept erasure demonstrate that MoRE achieves superior irreversibility (surpassing the retrain-from-scratch gold standard) while maintaining remain-set accuracy and training-free efficiency.

## Strengths
- **PO projection solves a concrete, empirically-verified problem.** Fig. 3 shows forget/remain prototype cosine similarities averaging ~0.5 (max 0.77 on CIFAR-10). Table 3 ablation cleanly isolates PO's role: without PO, erase achieves only 13.47% forget accuracy; with PO, 99.90%. Remap without PO drops remain accuracy to 79.64%; with PO, 99.87%.
- **MoRE surpasses the retrain gold standard on irreversibility.** Table 1 KR results: MoRE D_f = 0.11% on CIFAR-10 and 0.07% on CIFAR-100, vs. retrain 72.62% and 57.20% respectively. This is a striking and unusual result that demonstrates feature-level scattering as more effective than parameter-space forgetting.
- **Thorough ablation isolates each component's contribution.** Table 3 systematically tests Erase vs Remap with/without PO across standard and KR settings. Table 6 compares stochastic vs conditional routing (MoRE-P, MoRE-P-T-B). Fig. 7 demonstrates robustness across expert counts.
- **Training-free efficiency.** Fig. 5: MoRE completes unlearning in ~9.5s on CIFAR-10 with ~540MB GPU memory, competitive with ESC (21.5s, 491MB). O(Nd) time and O(dk) space complexity for prototype collection.
- **Cross-domain generalization to diffusion models without adaptation.** Table 2: MoRE achieves best LPIPS_d tradeoff (0.25 Van Gogh, 0.26 Kelly McKernan) among training-free methods. Fig. 4 qualitatively demonstrates removal of Van Gogh style with faithful prompt adherence.
- **Multi-expert design addresses single-expert fragility.** Table 3: MoRE with 8 experts reduces KR recovery from 33.20 (single-expert remap) to 9.01, demonstrating that scattering across multiple remain prototypes is substantially more robust than single-target remapping.

## Weaknesses

### Fatal
None.

### Major
- **Target-class sensitivity for single-expert remapping is larger than acknowledged.** Table 5 (KR setting, lr=0.1) shows single-expert Remap D_f ranges from 33.20 (target 0) to 89.95 (target 9) — a 2.7× spread, where 89.95 approaches the pre-unlearning level of 99.88. The paper describes this as "some yield slightly better results, suggesting mild preference" (line 334), which significantly understates the variation. While MoRE's multi-expert design mitigates this (Table 3: 9.01 with 8 experts), Table 5 only reports single-expert results, so robustness across targets with multi-expert routing is not empirically verified. The irreversibility claim depends on the multi-expert mitigation holding across all targets, which is plausible but not demonstrated.
- **Irreversibility evaluation relies on a single attack configuration.** The entire KR evaluation uses only fine-tuning with lr=0.1. The paper does not specify in the main text what parameters are fine-tuned, for how many epochs, or what data the attacker accesses. A title-level claim of "irreversible" unlearning should be validated against diverse adversarial strategies. The paper's strong irreversibility results may be specific to this configuration.

### Minor
- **Random data forgetting experiment (Table 4) omits MoRE.** The table shows "Remap" but not the multi-expert MoRE variant, yet the text (line 360) claims "MoRE achieves comparable or superior performance." Remap's MIA score (79.31) is worse than Retrain (74.64) and substantially worse than RL (27.99), complicating the "comparable or superior" framing.
- **Diffusion extension reports results for only 2 of 10 artists.** The evaluation set includes 10 artists (line 274), but Table 2 only reports Van Gogh and Kelly McKernan. The method is applied out-of-the-box, which is a strength, but partial reporting limits confidence in generalization.

### Trivial
None.

## Nice-to-Haves
- Report KR results across multiple attack configurations (varying learning rates, fine-tuning durations, nonlinear probes).
- Verify multi-expert robustness by reporting MoRE (not just single-expert Remap) across different target classes in Table 5.
- Include MoRE variant in the random data forgetting experiment (Table 4).
- Report diffusion results on all 10 artists.
- Discuss limitations of using class-wise activation means as prototypes (multimodal distributions).

## Removed Points
These points are flagged to be removed, treat them with caution:
- **"Table 1 parsing issues"** — This is a PDF parser artifact, not a paper problem. The paper's tables are properly formatted in the original submission.
- **"Linearity assumption limits effectiveness for nonlinear boundaries"** — The paper scopes to class-wise unlearning where linear operations on prototypes are appropriate. This is scope creep.
- **Missing related works** — Cannot verify external claims about missing citations.

## Novel Insights
The paper's most striking empirical finding is that MoRE surpasses the retrain-from-scratch gold standard on irreversibility (Table 1 KR: D_f = 0.11% vs retrain 72.62% on CIFAR-10). This inverts the conventional assumption that retraining provides the strongest unlearning guarantee, suggesting that feature-space scattering can be fundamentally more effective than parameter-space forgetting for preventing recovery. Additionally, the paper reveals that the fragility of single-target remapping (Table 5: D_f ranging 33-90%) highlights an important underexplored dimension in feature-level unlearning: the geometric relationship between forget and remain concepts in feature space determines irreversibility, not just the method itself.

## Suggestions
- Acknowledge the target-class sensitivity honestly (not as "mild preference") and provide a principled target selection heuristic or systematic multi-class remapping strategy.
- Expand KR evaluation to multiple attack configurations to strengthen the irreversibility claim.
- Report Table 5 with MoRE (multi-expert) to demonstrate that the multi-expert design closes the target-class gap.
- Include MoRE in Table 4 for completeness.
- Report diffusion results on the full 10-artist evaluation set.

## Anchor Papers Retrieved

**Round 1 (bracketing):**
| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| Xagys9QD3T (PPU) | 3.00 | 1 | Weak unlearning method, limited results. MoRE clearly stronger. |
| BJfIDS5LsS (MASIMU) | 2.50 | 1 | Weak multi-agent unlearning. MoRE far stronger. |
| hwXUmwJAq5 (UGradSL) | 3.00 | 1 | Simple gradient-based method. MoRE far stronger. |
| 85X9awoVtv (Auditing) | 2.50 | 1 | Different scope (audit verification). Not comparable. |
| p7mgNvOD9Q (SUN) | 4.00 | 1 | Training-free subspace unlearning. MoRE clearly superior (PO projection, remapping, MoE). |
| pUOesbrlw4 (Deep Unlearning) | 5.25 | 1 | SVD-based class unlearning. Similar motivation but MoRE is more sophisticated and achieves better results. |
| SIZWiya7FE (LAF) | 6.00 | 1 | Accepted unlearning paper. MoRE has stronger results and more novel method. |
| 7tpMhoPXrL (Forget Vectors) | 4.80 | 1 | Input perturbation approach. Different methodology, MoRE stronger. |
| Tzh6xAJSll | 7.60 | 1 | Scaling laws for associative memories. Topically distant. |
| DzGe40glxs | 8.00 | 1 | RL interpretability. Topically distant. |
| SPS6HzVzyt | 8.00 | 1 | Instruction finetuning analysis. Topically distant. |
| 84n3UwkH7b | 8.00 | 1 | Diffusion memorization detection. Topically distant but MoRE's contribution is narrower. |

**Round 2 (narrowing):**
| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| UstOpZCESc | 6.25 | 2 | Privacy-aware lifelong learning. MoRE stronger contribution. |
| HVFMooKrHX | 6.60 | 2 | Theoretical unlearning analysis. Different strengths; MoRE more practical. |
| fMNRYBvcQN | 6.75 | 2 | Relearning attacks on LLM unlearning. Attack paper, different niche. |
| oe51Q5Uo37 | 6.75 | 2 | Exact unlearning with PEFT. MoRE addresses a harder problem (feature-level irreversibility). |
| io8uRPYktn | 7.00 | 2 | PII protection in LLMs. Comparable accept quality; MoRE has more novel method. |

**Round 1 bracket: 6.5–8.0.** Round 2 narrowed to 7.0: MoRE clearly surpasses 6.75 anchors and is comparable to the 7.00 anchor, but target-class sensitivity and single-attack evaluation prevent scoring higher.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>