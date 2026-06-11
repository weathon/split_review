## Summary
This paper identifies a novel "priming vulnerability" specific to Masked Diffusion Language Models (MDLMs): affirmative tokens appearing at intermediate denoising steps can steer generation toward harmful responses even in safety-aligned models. The authors (1) quantify this via an anchoring attack, (2) derive a theoretical lower bound enabling a practical First-Step GCG attack, and (3) propose Recovery Alignment (RA), which trains models to generate safe responses from intentionally contaminated intermediate states. Experiments across three MDLMs show significant robustness improvements with minimal utility degradation on 11 benchmarks.

## Strengths
- **Novel, well-identified vulnerability with clean empirical evidence**: The anchoring attack (Section 4.1) demonstrates that injecting even a single token at step 1/128 raises ASR from 2% to 21% on LLaDA Instruct (Figure 2). This minimal perturbation with outsized safety impact convincingly demonstrates the vulnerability is real, severe, and MDLM-specific.
- **Theoretically grounded attack with practical impact**: Theorem 4.1 provides a lower bound on the full denoising log-likelihood using only the first-step mask predictor, yielding First-Step GCG (Equation 4) which is ~20× faster and up to ~3× more effective than Monte Carlo GCG (Table 1: 58.0% vs 20.0% on LLaDA Instruct).
- **Dramatic ASR reductions on well-aligned models**: On LLaDA Instruct, RA reduces ASR under anchoring attack from 17.3% to 0.0% at t_inter=1 (Table 2). The RA w/o inter ablation cleanly confirms contaminated-state training is critical (e.g., at t_inter=4: RA w/o inter 22.0% vs. RA 1.3%).
- **Preserved general capability across 11 benchmarks**: Table 4 shows negligible degradation (LLaDA average: 52.2→52.6; LLaDA 1.5: 52.7→52.8), with TruthfulQA and MBPP even improving.
- **Well-designed ablations**: The comparison of scheduling strategies (linear vs. uniform vs. constant) in Figure 3b isolates curriculum design contribution; the RA w/o inter ablation separates contaminated-state training from generic RLHF.
- **Comprehensive threat model coverage**: Both intervention-based attacks (anchoring, PAD, DiJA) and non-intervention attacks (First-Step GCG, PAIR, ReNeLLM, Crescendo) are evaluated — broader than concurrent works.

## Weaknesses

### Fatal
None.

### Major
- **MMaDA results partially conflate generic alignment with recovery training**: MMaDA MixCoT achieves 79.7% ASR under no attack (Table 2), indicating it is essentially unaligned. The RA w/o inter ablation already reduces this to 2.0%, nearly matching RA (3.3%). While on LLaDA models the contaminated-state training clearly adds significant value (e.g., at t_inter=4: RA w/o inter 22.0% vs. RA 1.3%), the MMaDA improvements are harder to attribute specifically to the novel recovery mechanism. The paper should more explicitly discuss this distinction, as the headline MMaDA results may overstate RA's unique contribution.

- **Claim about conventional jailbreak robustness is overstated for MMaDA**: The paper claims RA "improves robustness against conventional jailbreak attacks" as a general finding. For MMaDA in Table 3, ReNeLLM ASR is essentially unchanged (79.3% → 81.7%) and Crescendo remains at 55.3% after RA. The claim should be qualified to acknowledge that for weakly-aligned models, RA provides only partial improvement against strong conventional attacks.

### Minor
- **Single reward model without ablation**: DeBERTaV3 is used without fine-tuning as the sole reward signal (Section 6.1). While practical, the paper does not ablate reward model choice or report its agreement rate with GPT-4o (the evaluation judge). Even a brief comparison or agreement analysis would strengthen confidence that RA's effectiveness is not an artifact of DeBERTaV3's specific biases.

- **Theoretical bound looseness deserves more transparent framing in main text**: The bound in Theorem 4.1 includes a 1/T factor (T=128), making it quite loose. The paper acknowledges this implicitly ("this effect helps compensate for the looseness," Section 4.2) but should more explicitly frame the theorem as motivation for the surrogate objective rather than a tight analytical result. The method's success is primarily empirical.

### Trivial
None.

## Nice-to-Haves
- Disentangling generic RLHF benefits from contaminated-state training more rigorously (e.g., training from contaminated states but initialized from fully-masked-safe-only data).
- Discussion of why MMaDA remains more vulnerable than LLaDA variants even after RA — is this a fundamental limitation for weakly-aligned models or specific to architecture/training?

## Removed Points
These points are flagged to be removed, treat them with caution:
- **Multi-evaluator results deferred to appendix**: The paper explicitly states it uses GPT-4o, LLaMA Guard 3, and keyword matching (Section 6), with supplementary results in Appendix C. Standard practice given space constraints.
- **Monotonicity assumption scrutiny**: The assumption is stated upfront in Theorem 4.1, acknowledged as empirically validated in Appendix C.2, and the bound's looseness is discussed. Appropriately handled.
- **Harmful responses generated by non-safety-aligned model in anchoring attack**: Reasonable methodology for controlled vulnerability evaluation; source acknowledged in Appendix D.
- **Generation length L vulnerability scaling**: Paper notes L=T=128 and addresses length impact in Appendix C.5.
- **Formatting/style issues**: All parser artifacts, not paper issues.

## Novel Insights
The paper provides a genuinely novel structural insight: MDLMs' iterative denoising mechanism creates a fundamentally different safety vulnerability from ARMs — the training distribution never covers contaminated intermediate states. This observation (formalized in Equations 5–6) cleanly explains why standard alignment methods fail and directly motivates the contaminated-state training approach. The analogy to shallow safety alignment in ARMs is illuminating: in MDLMs, alignment only applies to trajectories starting from fully-masked states, leaving a parallel structural gap that conventional safety alignment cannot address.

## Suggestions
- Explicitly separate MMaDA results discussion from LLaDA results in Section 6.2, noting that improvements on MMaDA are largely driven by generic alignment rather than the novel recovery mechanism.
- Add a brief reward model ablation or at minimum report agreement rates between DeBERTaV3 and GPT-4o.
- Qualify the conventional jailbreak robustness claim to acknowledge incomplete defense on weakly-aligned models.

## Calibration Report

**All anchors retrieved:**

Round 1:
| Path | Avg Score | How it compares |
|------|-----------|-----------------|
| 5kMwiMnUip.md | 1.40 | Weak survey of jailbreak methods, no novelty — far below our paper |
| 8QTpYC4smR.md | 1.00 | Generic LLM review, rejected — unrelated quality level |
| BeOEmnmyFu.md | 2.50 | Language game jailbreak, limited novelty — below our paper |
| KyKTjRtyNG.md | 3.00 | Multi-round jailbreak, limited — below our paper |
| 6Mxhg9PtDE.md | 9.50 | "Safety Alignment Should be More Than a Few Tokens Deep" — identifies shallow alignment in ARMs, proposes mitigation. Very analogous but much more comprehensive and broadly applicable |
| u08UxVNdIo.md | 4.75 | "Diffusion Attacker" — uses diffusion for prompt rewriting, rejected |
| hXA8wqRdyV.md | 6.14 | "Jailbreaking Leading Safety-Aligned LLMs" — attack-only, no defense contribution |
| xP1radUi32.md | 6.25 | "Endless Jailbreaks with Bijection Learning" — attack-only |
| plmBsXHxgR.md | 6.25 | "Jailbreak in pieces" — VLM compositional attacks |
| Bo62NeU6VF.md | 8.00 | "Backtracking Improves Generation Safety" — recovery from unsafe generation via [RESET] token, all 8s, broadly applicable |
| tyEyYT267x.md | 8.00 | "Interpolating AR and Discrete Denoising Diffusion LMs" — architecture paper, safety not focus |

Round 2:
| Path | Avg Score | How it compares |
|------|-----------|-----------------|
| r42tSSCHPh.md | 7.00 | "Catastrophic Jailbreak via Exploiting Generation" — attack + defense on 11 models, our paper has cleaner theory and ablations |
| sULAwlAWc1.md | 7.00 | "One Model Transfer to All" — robust jailbreak against defended LLMs |
| uhaLuZcCjH.md | 7.00 | "Functional Homotopy" — optimization-based jailbreak, no defense |
| aSy2nYwiZ2.md | 6.67 | "Injecting Universal Jailbreak Backdoors" — backdoor attacks |
| 0VZP2Dr9KX.md | 5.25 | "Baseline Defenses" — defense baselines, rejected |
| YzxMu1asQi.md | 6.50 | "Scaling Laws for Adversarial Attacks" — activation attacks |
| V01FPV3SNY.md | 5.33 | "Defending Against Alignment-Breaking" — RA-LLM defense, rejected |

**Round 1 bracket: 6.0 – 8.5.** The paper is clearly above the 6.14 attack-only paper (hXA8wqRdyV) since it provides both attack analysis and effective defense. It is comparable to the 7.00 "Catastrophic Jailbreak" paper (r42tSSCHPh) which also has attack + defense, but our paper has cleaner theory, better ablations, and addresses a novel model class. It does not reach the 8.00 "Backtracking" paper (Bo62NeU6VF) which achieved all 8s with a clean, broadly applicable method — our paper has MMaDA noise and a narrower model class. It does not reach 9.50 "Safety Alignment" (6Mxhg9PtDE) which unified multiple attack types under a single structural insight across the ARM ecosystem.

**Round 2 narrowing: 7.0 – 7.5.** The 7.00 papers have comparable scope (attack + defense) but our paper has stronger theoretical grounding and cleaner ablations. However, the MMaDA results partially conflate generic alignment with the novel mechanism, and the conventional jailbreak claim is overstated for that model.

**Final score: 7.0.** The paper makes a genuine, well-executed contribution identifying and mitigating a real vulnerability in an emerging model class. The LLaDA results are compelling and the theory-practice connection is clean. The MMaDA concerns and single reward model prevent a higher score but do not undermine the core contribution.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>