## Summary

This paper introduces **Alignment from Demonstrations (AfD)**, an approach for LLM alignment that uses demonstration data (response-output pairs) rather than preference pairs. The authors formalize AfD as an inverse RL problem, show theoretically that SFT corresponds to forward-KL trajectory distribution matching (explaining its mass-covering behavior), and propose a reward model training strategy—**Init-SFT**—that trains a discriminator between the SFT policy (positive) and the initial policy (negative) to avoid heterogeneity-induced reward hacking. Experiments on Anthropic HH-RLHF with GPT-2 and Gemma 2B show that Init-SFT + Best-of-N achieves golden-reward-model scores and GPT-4 win rates competitive with preference-based baselines.

---

## Strengths

1. **Clean theoretical connection between SFT and forward-KL trajectory matching.** Section 3.1 (Eq. 7–9) provides a precise analytic derivation showing that the SFT objective minimizes the forward KL divergence between the demonstration and policy trajectory distributions. This formally grounds the mass-covering behavior of SFT (an observation noted in prior work but lacking this derivation) and clearly distinguishes it from the mode-seeking behavior of reverse-KL methods.

2. **Principled Init-SFT reward model that avoids a key failure mode in AfD.** Section 3.2 identifies a concrete problem unique to AfD: using heterogeneous models (e.g., initial LLM vs. a stronger external demonstrator) as the two classes in discriminator training causes the reward model to latch onto irrelevant stylistic differences rather than alignment quality. The proposed remedy—using π_SFT (same architecture, fine-tuned from π_0) as positives instead of the original demonstrations—is well-motivated. Figure 5 empirically validates this design: Init-SFT RM outperforms both Init-Demo and SFT-Demo alternatives on golden reward model scores.

3. **Empirical evidence that AfD can be competitive without preference data.** On both Harmless and Helpful tasks, Init-SFT RM + BoN achieves golden-reward-model scores and GPT-4 win rates on par with the preference-based BT-RM baseline (Table 2, Figure 5), despite never seeing preference pairs. This directly supports the paper's central claim that AfD is a viable alternative to preference-based alignment in the settings tested.

4. **Clear conceptual distinction from DPO/SPIN on super-demonstration capability.** Section 3.3 and Figure 3 articulate a non-obvious difference: DPO's implicit reward is bounded by demonstration quality (demonstrations are always positive examples), whereas explicit IRL reward extrapolation can in principle surpass the demonstrator. This clarifies when the proposed approach offers a structural advantage over direct alignment methods applied to the same data.

---

## Weaknesses

### Major

1. **The validity of the Init-SFT reward model is asserted but not demonstrated.**  
The paper's core technical contribution is that training a discriminator between π_SFT (positive) and π_0 (negative) captures alignment-relevant signal. However, the paper provides **no analysis of what this discriminator actually learns**. There are no probing experiments, no correlation analysis with human judgments, no ablation controlling for surface-level features (response length, refusal templates, formality markers, specific phrasing patterns). The discriminator could be exploiting any artifact of the SFT fine-tuning process that has nothing to do with harmlessness or helpfulness.  

The BoN results (Figure 5, Table 2) are consistent with the paper's hypothesis, but they do not rule out a simpler explanation: the "best-of-N" effect improves quality regardless of the selection criterion, and the IRL-RM might merely correlate with quality without genuinely measuring it. A sanity check against BoN using trivial heuristics (e.g., response length) as a proxy reward is absent.  

**Why this matters:** The entire method hinges on the IRL-RM being a valid reward signal. Without evidence about what the discriminator captures, the method's apparent success could be brittle, dataset-specific, and may not transfer to settings where π_SFT and π_0 differ in ways orthogonal to alignment quality. This is a foundational evidential gap.

2. **The experimental design does not test the paper's own motivating advantages.**  
The paper motivates AfD with four claimed advantages over preference-based methods (lines 15–20): lower noise, lower cost, fewer assumptions, and privacy preservation. Yet the experiments use **GPT-4 API calls** to generate demonstration responses on the **HH-RLHF dataset** (a preference-annotation setting). This directly undermines several claims:
   - **Privacy**: Sending prompts to a third-party API (GPT-4) to generate demonstrations contradicts the paper's statement that AfD "can be applied to private dataset locally" (line 20) and its claim about privacy being a limitation of preference-based methods (line 18).
   - **Cost**: Generating 68K+ GPT-4 responses is not free; the paper provides no cost comparison against preference annotation.
   - **Noise/Quality**: Demonstrations come from GPT-4, not domain experts in the paper's claimed application areas (medical diagnostics, expert customer service—lines 25–26). Whether GPT-4 outputs in this setting are genuinely "high quality, low noise" is unknown.

The paper would need to demonstrate AfD in at least one setting where demonstrations come from an independent expert source to support its motivating claims. As submitted, the experiments stay within the preference-data paradigm the paper claims to supersede.

3. **No actual policy optimization is performed.**  
The paper evaluates the IRL-RM using Best-of-N (BoN), a *filtering* method that selects the best among fixed candidates rather than updating policy parameters. The paper frames its contribution as an "Inverse RL algorithm" (Section 3.2), but the final step—using the learned reward model to guide on-policy RL (PPO, REINFORCE, etc.)—is never executed. The paper justifies BoN by citing literature (Dong et al., 2023; Gao et al., 2023; Coste et al., 2023), but BoN is a diagnostic, not a substitute for RL. Whether the IRL-RM would succeed under the distribution shift inherent in on-policy optimization—where reward hacking can be far more severe—remains untested. For a method framed as Inverse RL, the absence of actual RL is a significant gap.

### Minor

4. **No error bars, confidence intervals, or significance tests on any result.** Figures 4, 5, and Table 2 report point estimates only. Given the modest scale (GPT-2, Gemma 2B), variance could be substantial. This is below the reporting standard expected at a top venue.

5. **No comparison to the full RLHF pipeline (PPO + learned reward model).** The paper compares against DPO variants but not against PPO with a preference-based reward model, which is the standard RLHF baseline. A comparison showing whether BoN+BT-RM matches PPO+BT-RM on these tasks would contextualize the BoN evaluation choice.

6. **No cost or compute analysis.** The paper claims cost advantages for AfD but does not report the GPU-hours for SFT training, reward model training, BoN inference, or the GPT-4 API cost for generating 68K+ demonstrations. Without this data, the claimed cost advantage is unverifiable.

7. **No limitations section.** Several limitations are apparent from the paper itself (small models, single dataset family, BoN instead of RL, no reward model analysis, GPT-4 as demonstrator, no privacy-preserving demonstration source), yet the paper ends with a conclusion that does not acknowledge any of them.

8. **The claim that SPIN is "upper-bounded by demonstration performance" (line 212) may be inaccurate.** Chen et al. (2024) report SPIN exceeding demonstration quality through iterative self-play. This cannot be fully verified from the paper alone, but the authoritative claim about SPIN's limitations should be checked against the original work.

---

## Nice-to-Haves

- **Analyze what the IRL-RM captures:** Probing experiments (e.g., correlation with human judgments, ablation controlling for response length/formatting) would directly address the most significant evidential gap.
- **Test with genuinely expert-curated demonstration data** in a domain where preference data is unavailable or privacy-sensitive (e.g., clinical notes, customer service transcripts), to actually validate the paper's motivating claims.
- **Demonstrate actual RL-based policy optimization** (PPO or equivalent) using the IRL-RM, and compare against PPO with preference-based reward models to complete the Inverse RL pipeline.

---

## Removed Points

The following points from the reviewers were removed with justification:

- **"Heterogeneity over-claimed; π_SFT and π_0 could differ substantially"** — The paper's claim is about *model-class* homogeneity (same architecture, same initialization, fine-tuned from the same base), not output distribution similarity. The critic conflated the two concepts; the paper's argument is sound on its own terms.
- **"SPIN comparison incomplete" raised as a structural/fatal concern** — The critic's claim about Chen et al. (2024) showing SPIN can exceed demonstrations depends on information external to the paper. Demoted to Minor (above).
- **"No cost or compute analysis" presented as a major weakness** — This is a legitimate omission but not central to the paper's contribution; kept as Minor.
- **"Section 2.1 state space is exponentially large"** — This is a standard observation about the MDP formulation and applies equally to all LLM-as-MDP formulations; it is not a specific weakness of this paper.

---

## Novel Insights

None beyond the paper's own contributions.

---

## Suggestions

1. Add a probing/analysis section examining what features the IRL-RM responds to—correlate its scores with human judgments, ablate for surface-level confounds (length, refusal keywords), and compare against BoN using simple heuristic proxies (e.g., response length).
2. Include at least one experiment where demonstration data comes from a genuinely independent source (not GPT-4 on a benchmark derived from preference data) to substantiate the claimed advantages.
3. Replace or supplement BoN evaluation with actual policy optimization (PPO or REINFORCE) using the IRL-RM, and compare against a PPO+BT-RM baseline.
4. Report error bars (standard deviations over seeds) for all quantitative results, and add a limitations section.
5. Provide a compute/cost breakdown to support the claimed cost advantages.

---

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>