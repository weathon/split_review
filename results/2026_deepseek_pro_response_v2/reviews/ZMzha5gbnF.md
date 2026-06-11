Now I have enough context. Let me finalize. Here are my comparisons:

- **Safe RLHF (7.50):** Decoupled helpfulness/harmlessness RLHF. Some reviewers noted incremental contribution and missing baselines. Our paper has more novelty (new vulnerability class + defense), broader evaluation, and a theoretical contribution — slightly stronger overall.
- **Catastrophic Jailbreak (7.00):** Attack-focused, narrower evaluation, open-source only. Our paper is clearly stronger.
- **Backtracking (8.00):** Similar "recovery" concept, clean method, all 8s. Our paper has more breadth but slightly less precise framing. Comparable but marginally below.
- **Shallow Safety Alignment (9.50):** Unifying framework — clearly above our paper.

**Final score: 7.5 — Accept.**

Now let me write the complete review.

---

## Final Answer

## Summary

This paper identifies a "priming vulnerability" in Masked Diffusion Language Models (MDLMs): tokens from harmful responses appearing at intermediate denoising steps can steer aligned models toward harmful outputs. The authors demonstrate this via a controlled anchoring attack and a theoretically-grounded First-Step GCG, then propose Recovery Alignment (RA), an RLHF-style method that trains MDLMs to generate safe responses from deliberately contaminated intermediate states. Experiments on three MDLMs show RA substantially reduces attack success rates while preserving general capability across eleven benchmarks.

## Strengths

- **Clean empirical demonstration of the vulnerability (Figure 2, Table 2).** The anchoring attack shows that injecting ~1 token at the first denoising step raises ASR from 2% to 21% on LLaDA Instruct — a crisp, controlled experiment isolating the mechanism from confounding factors.

- **Theoretically motivated attack (Theorem 4.1, Table 1).** First-Step GCG is tractable, ~20× faster, and 2–4× more effective than Monte Carlo GCG. This is both a practical contribution and validation that the vulnerability is exploitable without denoising-process access.

- **RA substantially mitigates the vulnerability while preserving utility.** Table 2: RA reduces anchoring ASR (t_inter=1) from 17.3% to 0.0% on LLaDA and First-Step GCG from 58.0% to 11.3%. Table 4 confirms no degradation across 11 benchmarks (52.2% → 52.6% average).

- **Well-designed ablations validate design choices.** Figure 3b confirms linear curriculum scheduling outperforms uniform and constant scheduling. The RA w/o inter ablation (Table 2) directly validates that training from contaminated intermediate states — not just RLHF — is the causal factor.

- **Comprehensive evaluation.** Three MDLM architectures, two benchmarks, three evaluators, seven attack methods (both intervention-based and black-box), and four baselines including the prior MDLM-specific MOSA. This breadth makes findings robust across model, dataset, and metric choices.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **"Affirmative token" framing overstates specificity.** The paper defines the priming vulnerability around "affirmative tokens, which endorse or advance a harmful intent" (line 84). However, the anchoring attack injects the entire harmful response at t_inter then applies masking — the surviving token at t_inter=1 is a uniformly random token from the response, which could be a content word (e.g., "bomb") rather than an affirmative token (e.g., "Sure"). The paper never decomposes affirmative-token from content-token effects. The vulnerability is real, but the evidence supports a general "intermediate-state contamination" problem rather than specifically an affirmative-token phenomenon. The authors should either provide a token-type decomposition or soften the "affirmative token" language.

- **RA's variable effectiveness against attacks with different contamination patterns deserves deeper analysis.** Table 2 shows RA is very strong against Anchoring (1.3% at t_inter=4 on LLaDA) and PAD (1.0%) but substantially weaker against DiJA (35.7%), and Table 3 shows ReNeLLM ASR remains at 72.3%. The paper acknowledges the ReNeLLM limitation (line 244) but does not analyze whether the performance gap stems from a mismatch between the contamination distribution used during training (full harmful responses) and the different contamination patterns of DiJA/ReNeLLM. A brief categorization of attacks by contamination pattern, correlated with RA effectiveness, would strengthen the analysis of the method's scope and limitations.

### Trivial

- **Algorithm 1 variable name bug.** Lines 5–6 (page 6) use `t_min` instead of `t_inter` (computed in line 2). Line 6's comment says "Denoise from t_inter to T" while the code uses `t_min`. This would confuse readers trying to reimplement. (The paper references Algorithm 2 in the appendix for the detailed procedure, which likely has the correct version.)

- **Table 2 header uses `t_min` for anchoring attack columns** where `t_inter` would be the correct variable name, creating a minor notational inconsistency with the text.

## Nice-to-Haves

- A controlled experiment injecting only affirmative tokens (e.g., "Sure," "Certainly") vs. only content tokens (e.g., "bomb," "explosive") at intermediate steps would clarify whether the vulnerability is specifically about affirmativeness or general semantic biasing.
- An MDLM-vs-ARM comparison injecting the same prefix into both architectures would empirically substantiate the claimed mechanistic distinction from ARM prefilling.
- Reporting which specific tokens survive masking at t_inter=1 in the anchoring attack would improve interpretability.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Harsh Critic #2: "The claimed distinction from ARM prefilling vulnerabilities is asserted but not empirically substantiated."** WEAKENED and REMOVED as a standalone weakness. The ARM contrast is contextual positioning, not a core claim. The paper's contribution does not depend on proving MDLMs differ from ARMs — it identifies a vulnerability in MDLMs and proposes a defense. The contrast helps motivate the work but empirical substantiation is not required for the main contribution to stand.

- **Harsh Critic #3: "The theoretical connection between the priming vulnerability and First-Step GCG is tenuous."** REMOVED. The paper provides Theorem 4.1 (with proof in the appendix), empirically validates the monotonicity assumption (Appendix C.2), and the anchoring attack results directly show that early-step contamination steers generation. The chain from vulnerability → first-step surrogate is coherent. The critic's requested ablation (disentangling "better surrogate" from "priming effect") is a distinction without a practical difference — both explanations imply the method works for the same underlying reason.

- **"GPT-4o-only ASR in main text weakens confidence."** REMOVED. The paper explicitly states (line 200) that remaining results for LLaMA Guard 3 and keyword matching are in Appendix C. This is standard ICLR practice.

- **"Figure 2 data table only goes to step 10/128 but text mentions step 16."** REMOVED. At step 10/128 the ASR is already 100% for aligned models, so step 16 exceeding 80% is trivially true. No actual inconsistency.

- **Strength Finder: "Generalization to broader jailbreak attacks."** KEPT but noted with the ReNeLLM qualification (72.3% vs. original 92.7% is an improvement but still high).

## Novel Insights

The paper's key insight — that MDLM safety alignment trained only from fully-masked initial states creates a blind spot at contaminated intermediate states, and that explicitly training recovery from those states addresses it — is genuinely novel and well-motivated. This reframes MDLM safety from "train to refuse harmful queries" to "train to recover from any state where harmful tokens have emerged," which generalizes beyond the specific priming attack to broader jailbreak robustness. The connection between this vulnerability and the First-Step GCG lower bound is also a nice theoretical contribution.

## Suggestions

- Soften the "affirmative token" language throughout (abstract, introduction, vulnerability definition) to "intermediate-state contamination" or clarify that the vulnerability is about any harmful-response token, not specifically affirmative ones — unless providing a token-type decomposition experiment.
- Fix Algorithm 1 to use `t_inter` consistently in lines 5–6.
- Add a paragraph in Section 6.2 analyzing why RA effectiveness varies across attack types (DiJA vs. Anchoring vs. ReNeLLM) — even a qualitative categorization of contamination patterns would help.
- Hedge the ARM-vs-MDLM contrast in Section 1 (e.g., "we hypothesize this differs from ARM prefilling") unless empirical evidence is provided.

## Calibration Anchors

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| NEMESIS Jailbreaking (5kMwiMnUip) | 1.40 | R1 | Clearly weaker — simple jailbreak survey |
| Safety Alignment More Than Few Tokens (6Mxhg9PtDE) | 9.50 | R1 | Clearly stronger — unifying framework paper |
| Incremental Exploits MRCJ (KyKTjRtyNG) | 3.00 | R1 | Weaker — narrower contribution |
| Diffusion Attacker (u08UxVNdIo) | 4.75 | R1 | Weaker — attack-only, less comprehensive |
| IDEATOR Jailbreaking VLMs (JnRvQ8CxLx) | 4.00 | R1 | Weaker — narrower scope |
| Injecting Universal Jailbreak Backdoors (aSy2nYwiZ2) | 6.67 | R2 | Weaker — attack-focused, narrower eval |
| Catastrophic Jailbreak (r42tSSCHPh) | 7.00 | R2 | Weaker — attack-focused, open-source only |
| One Model Transfer to All (sULAwlAWc1) | 7.00 | R2 | Weaker — attack-only |
| Safe RLHF (TyFrPOKYXw) | 7.50 | R2 | Comparable — similar quality, our paper has more novelty in domain |
| Backtracking (Bo62NeU6VF) | 8.00 | R1 | Slightly stronger — cleaner framing, similar concept |
| Booster (tTPHgb0EtV) | 8.00 | R1 | Slightly stronger — cleaner contribution |

**Round 1 bracket:** 7.0–8.0. **Round 2 narrowed to:** 7.0–7.5. The paper is comparable to Safe RLHF (7.50) in overall quality — it has more novelty (new vulnerability class in an underexplored domain, theoretical contribution) but slightly less precise framing. It is stronger than the attack-focused 7.0 papers but not quite at the cleaner 8.0 level of Backtracking. **Final: 7.5.**

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>