- Decision: Reject
- Avg Score: 4.25
- Scores: 5, 1, 6, 5
Good, I've now thoroughly verified all claims against the paper. Here is my final consolidated review.

---

## Summary

The paper proposes a **peer evaluation framework (PRD)** for LLM-as-judge setups, comprising two components: **Peer Rank (PR)**, which aggregates pairwise judgments from multiple LLMs by iteratively reweighting reviewers based on their own performance as contestants, and **Peer Discussion (PD)**, where two LLMs engage in multi-turn discussion with explicit evaluation aspects to reach a mutual judgment. The framework is evaluated on LFQA and Vicuna80 datasets with human annotations. The strongest result is that the weighted PR scheme recovers the exact human global ranking (GPT-4 > Claude > Vicuna > GPT-3.5 > PaLM-2) on Vicuna80, while every individual reviewer, including GPT-4, deviates from this order.

---

## Strengths

1. **Weighted peer rank produces a global ranking that exactly matches human judgments and the Chatbot Arena leaderboard, outperforming every single-reviewer baseline.**  
   Table 2 (described in §4.2) shows that All (Weighted) yields the exact human ranking (GPT‑4 > Claude > Vicuna > GPT‑3.5 > PaLM‑2) and the closest Elo and win-rate numbers, whereas GPT‑4 alone (the strongest individual reviewer) mis-ranks GPT‑3.5 above Vicuna. This is a clean, compelling result that directly supports the PR contribution.

2. **PD demonstrably mitigates self-enhancement bias, especially for weaker models.**  
   Table 5 (§4.3) shows that GPT‑3.5 initially over-favors GPT‑3 answers by 13.79% (win rate 69.23% vs. human 55.44%); after PD with Claude, its win rate drops to 58.42%, closely matching the human reference. GPT‑4's already-close alignment remains stable after discussion, confirming the method does not degrade stronger reviewers.

3. **Both PR and PD reduce position bias, moving reviewer preferences toward human-level position indifference.**  
   Table 6 (§4.3) shows that after PD, all three LLM reviewers' win rates for GPT‑3 answers in different positions become nearly equal (e.g., GPT‑3.5: 60.53% vs. 57.89% in the two orders, down from a 15.79% gap), while Figure 3 shows global first/second-position preference converging toward the human baseline (50%).

4. **The paper identifies and quantifies a "discussion ordering effect": the LLM that leads the discussion is far less likely to change its opinion, and stronger models are more opinion-holding.**  
   Figure 4 (§5) reports that GPT‑4 holds its opinion in 174 discussions when leading versus only 76 for GPT‑3.5; all models show near-zero opinion-altering in the leader position. This provides empirical insight into multi-agent evaluation dynamics that goes beyond the paper's main claims.

5. **The iterative weight-update scheme in PR enables a group of LLMs to induce a self-ranking that aligns with external leaderboards, and the weights (GPT‑4 48.8%, Claude 37.7%, Bard ~0%) correspond to the known quality ordering.**  
   Figure 1 and Figure 2 (§4.2) confirm that weights converge meaningfully, and the method works under an anonymous setting where model identities are not revealed to reviewers.

---

## Weaknesses

### Fatal
None.

### Major

1. **The PD experimental design conflates multi-turn discussion with the introduction of a structured evaluation rubric, preventing clean attribution of accuracy gains to the discussion mechanism.**  
   The initial individual reviews use a generic prompt (Table 8), while the discussion prompt injects explicit evaluation aspects drawn from WebGPT guidelines (unsupported information, core information, coherence). The paper reports (lines 332–335) that switching from a *generic* discussion prompt to an *explicit-aspects* discussion prompt yields a 4% absolute gain (0.69 → 0.73 PDA). The paper does **not** include the necessary control: an initial individual judgment condition using the *same* explicit-aspects prompt as the discussion. Without this, we cannot determine whether the reported PD improvements over individual reviewers come from the multi-turn interaction, or simply from having a more detailed rubric.  

   *Why this matters:* The paper's title and framing emphasize "discussion" as the mechanism. The confound means the reader cannot attribute the improvement to discussion per se. This does **not** invalidate the combined approach (discussion + explicit rubric) — which does work, especially for weaker models — but it weakens the mechanistic claim. The paper partially addresses this by reporting generic-discussion results (0.69 PDA, which beats Claude alone but not GPT-4 alone), but the full ablation is missing.

   **Note for rebuttal:** This can be resolved by running initial judgments with the explicit-aspects prompt and comparing them to discussion with the same prompt.

2. **PR accuracy improvements are modest (3 percentage points over GPT-4) and lack statistical uncertainty quantification**, while the results for PD report standard deviations.  
   Table 1 (§4.2) reports PR achieving 67.3% accuracy vs. GPT-4's 64.3% on example-level pairwise comparisons, but no confidence intervals, standard deviations, or significance tests are provided. By contrast, PD results (§4.3) include standard deviations (e.g., 0.729±0.014), showing the authors know how to compute uncertainty. With a 3-point gap on a binary classification task, the improvement could lie within sampling noise. The global ranking result (Table 2) is more compelling, but the example-level accuracy claim is under-supported.

### Minor

3. **The core assumption of PR — that better contestants are better reviewers — is asserted rather than validated.**  
   The paper (§3.1) states this assumption, cites Walsh (2014) and Yuan et al. (2024), and reports that fixing self-weight at zero gave poorer performance (no numbers shown). The comparison between "All" (equal weights) and "All (Weighted)" (Table 2) provides *indirect* evidence, but additional ablations — e.g., weighting by an external capability metric (MMLU score), using random weights, or inverse weights — would strengthen the case that the *iterative weighting scheme* specifically drives the improvement, rather than simply aggregation of multiple reviewers.

4. **The paper does not test initial individual judgments with the same explicit-rubric prompt used in PD** (closely related to Point 1, but narrower: even without discussion, adding a structured rubric to an individual reviewer might yield similar gains). This is a specific missing control that would clarify the contribution of each component.

### Trivial

- No empirical convergence analysis for PR iterations is shown (Walsh 2014 is cited for convergence guarantee, but the paper does not plot convergence speed or verify it on this data).
- The anonymous setting is mentioned in the abstract but not elaborated in the PR setup description — the paper could clarify how model names are hidden during review to prevent name-based bias.

---

## Nice-to-Haves

- An error analysis examining cases where PR/PD disagrees with human judgments (e.g., are there systematic patterns related to question category, answer length, or required knowledge type?).
- Testing PD with explicit aspects given to initial reviewers individually as well, to fully isolate the discussion effect.
- Additional weighting ablations for PR (random weights, inverse weights, external-capability weights) to validate the iterative weighting mechanism.

---

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"SummEval results are mentioned but no numbers reported."** The paper references SummEval results in a bluenote (Table `tab:corr_summeval`), which was likely in the appendix — stripped by the parser, not absent from the submission. This is a parser artifact, not a paper weakness. Removed per Hard Rules.

- **"No mention of anonymity in the PR setup."** The paper explicitly mentions "anonymous setting" in the abstract (line 11). While details could be expanded, the claim of no mention is factually incorrect. Demoted to Trivial in the main review.

- **"The paper would benefit from error analysis."** This is a general suggestion for improvement, not a specific weakness. Moved to Nice-to-Haves.

- **"The paper could add more datasets."** The two datasets (LFQA and Vicuna80) are standard for this evaluation task. Requesting more without a specific gap is a generic scope-expansion criticism. Removed.

- **Criticisms about the confound framed as "fatal" or "structural."** The PD confound is genuine but not fatal — the paper provides partial controls (generic discussion comparison) and the combined approach (discussion + rubric) still shows meaningful gains, especially for weaker models. Demoted from Fatal to Major per verification.

---

## Novel Insights

The **discussion ordering effect** (the leader in a multi-LLM discussion is far less likely to change its opinion, and stronger models are more opinion-holding) is a genuinely novel behavioral finding that transcends the paper's primary evaluation contribution. It suggests practical design implications for multi-agent evaluation protocols: if the leader's opinion dominates, protocols should randomize leadership or run symmetric discussions and aggregate. This finding emerged from the further analysis in Section 5 and is not just a re-statement of the paper's main claims.

None beyond the paper's own contributions.

---

## Suggestions

1. **Add the missing control for PD:** Run individual initial judgments using the *same explicit-aspects prompt* that the discussion uses. Compare (a) individual + explicit rubric vs. (b) discussion + explicit rubric. This will cleanly isolate the effect of multi-turn interaction from the effect of a structured rubric.

2. **Report confidence intervals or bootstrap estimates for the PR example-level accuracy results** (Table 1). Even simple 95% bootstrap CIs would substantially strengthen confidence in the 3-point improvement over GPT-4.

3. **Add a weighting ablation for PR:** Compare the proposed iterative weighting against (a) equal-weight aggregation, (b) weighting by an external capability score (e.g., MMLU accuracy), and (c) random weights. This would validate that the iterative scheme specifically drives the improvement.

4. **Clarify the anonymity implementation** in the PR setup: are model names masked during review, and if so, how? This would address a natural reader concern about whether name-based bias is actually prevented.

---
