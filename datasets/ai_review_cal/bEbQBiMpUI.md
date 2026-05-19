- Decision: Reject
- Avg Score: 5.40
- Scores: 3, 8, 3, 8, 5
Now I have a thorough understanding of the paper. Let me synthesize the final consolidated review.

## Summary

This paper studies intrinsic self-correction in LLMs, demonstrating empirically that performance, model uncertainty, calibration error, and latent concept activations converge over multiple rounds of self-correction. The main contributions are: (1) showing convergence across six diverse tasks (both text-only and multi-modal), (2) jointly tracking uncertainty reduction and calibration improvement across rounds, (3) analyzing how activated latent concepts evolve (convergence and instruction-dependence properties), and (4) a simulation task linking concept shifts to uncertainty changes with 83% accuracy. The paper proposes a causal chain: instructions → concept activation → reduced uncertainty → lower calibration error → converged performance.

---

## Strengths

- **Empirical demonstration of convergence across diverse tasks (Section 3, Figure 3):** The paper convincingly shows that intrinsic self-correction performance improves and plateaus over rounds in six tasks spanning multi-choice QA, text generation, and vision-language settings. This goes beyond prior single-round self-correction analyses and provides the first systematic multi-round characterization.

- **Joint tracking of uncertainty, calibration, and concepts (Sections 4–5, Figures 4–5):** The paper simultaneously tracks model uncertainty (semantic entropy/ECE), calibration error (ECE/RCE), and latent concept scores across rounds. This joint perspective is novel and reveals that uncertainty decreases monotonically and calibration converges at roughly the same point as performance, establishing correlated trends among these variables.

- **Simulation task linking concept change to uncertainty change (Section 6.1):** Using logistic regression on concept difference vectors to predict whether uncertainty will increase or decrease achieves 83.18% accuracy (variance 0.00024). This provides empirical evidence of a strong dependence between activated concepts and model uncertainty, beyond simple correlation.

- **Extension to multi-modal settings:** Including visual grounding and visual VQA tasks (using GPT-4) shows the convergence phenomenon holds beyond pure-text settings, broadening generality.

---

## Weaknesses

### Fatal
None. The paper's empirical core — that intrinsic self-correction performance, uncertainty, and latent concepts converge over rounds — is supported by the experiments and stands independently of the theoretical derivation.

### Major

1. **The theoretical derivation in Section 6.2 is mathematically flawed and does not provide a valid explanation.** 
   - The Bayesian derivation of p(C_p|q_k) contains algebraic errors: the normalizing constant is inconsistently applied. For q_0 the formula is p(C_p|q_0)=c_x c_i/c_p, but for q_1 the correct denominator should be c_p³, not c_p (as used in the paper). The error compounds with each round.
   - The final claimed expression p(C_p|q_k) = (c_i c_y)^(t-1)·p(C_p|q_0) does not follow cleanly from the provided equations, and the claim that p(C_p|q_k) > p(C_n|q_k) is "guaranteed" by the irreversibility property is asserted without formal justification.
   - The derivation does not account for how c_y (the positive concept probability of each output) itself changes across rounds in a way that depends on the full history, making the assumption that c_y is constant questionable.
   - **Why it matters:** The paper frames this as part of its contribution ("a mathematical formulation" — abstract, line 7; "convergence guarantee" — line 20). An invalid theoretical section weakens the paper's analytical contribution. The authors should either correct the derivation to a rigorous standard or remove it, as the empirical findings are interesting on their own.

2. **Causal claims exceed what the evidence supports.**
   - The paper states it "empirically validates the strong causal relationship between concept and uncertainty" (Section 6.1, line 118) and calls the concept "a strong driving force" (line 120). The evidence is a logistic regression achieving 83% accuracy at predicting the direction of uncertainty change from concept change — this shows strong correlation/dependence, not causation.
   - The overall framework (Figure 2) posits a causal chain (instructions → concepts → uncertainty → calibration → performance), but each link is supported only by correlational or co-occurrence evidence. Alternative causal directions (e.g., uncertainty reduction driving concept change, or a third factor driving both) are not discussed.
   - **Why it matters:** The paper's central explanatory narrative is framed in causal terms that the experiments cannot support. The conclusions should be tempered to describe the findings as a proposed mechanism consistent with the data, not a proven causal chain.

### Minor

1. **The "irreversibility" property is imprecisely defined and the evidence is ambiguous.**
   - The paper claims that once a concept is activated in a particular direction (positive or negative), it "cannot be revertable" (line 53) and exhibits "irreversibility" (Section 5). However, the intervention experiments show that injecting immoral instructions at specific rounds immediately shifts the concept toward toxicity. If the concept can flip when instructions change, "irreversibility" is a misnomer — the concept is instruction-dependent, not irreversible.
   - The plotted red line in Figure 5(b) appears to decrease between immoral injection rounds (rounds 2→5, 5→8), suggesting the concept may partially revert toward non-toxicity when moral instructions resume. The paper does not provide a quantitative analysis of this behavior.
   - **Why it matters:** The theoretical analysis (Section 6.2) relies on the irreversibility claim to guarantee p(C_p|q_k) > p(C_n|q_k). If the concept can revert when instructions change, this guarantee is not unconditional. The paper should clarify the definition and provide quantitative evidence for what "irreversibility" means.

2. **Single base LLM for text experiments limits generality.**
   - All text experiments use only zephyr-7b-sft-full (a single 7B instruction-tuned model). While GPT-4 is used for vision tasks, the core convergence analysis on text tasks lacks model diversity. Demonstrating the same patterns on a second model (e.g., a different family or scale) would substantially strengthen the claim that convergence is a general property of intrinsic self-correction.

3. **"Convergence guarantee" language is stronger than the evidence supports.**
   - The paper uses "convergence guarantee" (lines 20, 31, 64), but the evidence is empirical saturation on six tasks, not a formal guarantee. This is a common rhetorical pattern in ML papers but still overstates what is demonstrated. The authors should use "empirical convergence" or "stable convergence" rather than "guarantee."

### Trivial
- The paper does not report statistical significance or confidence intervals for the performance improvements and convergence plateaus. Adding variance estimates across random seeds would strengthen reliability.

---

## Nice-to-Haves
- A control experiment that recycles the same instruction without any self-correction intent (e.g., asking the model to "repeat" or "re-read" rather than "correct") would help rule out the alternative explanation that uncertainty reduction is driven by familiarity/repeated exposure to similar prompts rather than concept activation.
- Discussion of whether the same convergence pattern holds for reasoning tasks (excluded due to ongoing debate) would provide a more complete picture.

---

## Removed Points
These points are flagged to be removed; treat them with caution.

1. **From Harsh Critic — "Irreversibility" as a fundamental flaw:** The critic claims the experiment does not cleanly support the claim. However, the paper defines irreversibility as the concept maintaining its direction under consistent instructions — the intervention experiments intentionally show that changing instructions changes the concept, which is consistent with the definition (the concept follows the instruction). The critic's framing casts irreversibility as a crisp property failure but the ambiguity is about definitional clarity, not a fundamental contradiction. Downgraded from "undermines the core claim" to Minor.

2. **From Harsh Critic — Missing prompt templates as reproducibility gap:** "The prompt templates and exact instructions... may be in the appendix, which is stripped." Per instructions, appendix content is assumed to exist in the original submission. Removed as an artifact of the parsing process.

3. **From Strength Finder — "Mathematical formulation linking concepts to convergence":** Claims the derivation "formally explains why uncertainty and performance converge" and is "absent in earlier empirical analyses." The derivation is flawed (see Major weakness #1) and does not constitute a valid formal explanation. Removed.

4. **From Strength Finder — "Irreversibility of activated concepts":** Claims this "essential property" is supported by intervention experiments. Given the definitional ambiguity and lack of quantitative analysis, this claimed strength is overstated. Removed.

5. **From Strength Finder — "Simulation task establishing causal dependence":** Phrases the logistic regression result as "directly confirming the causal chain." The experiment shows correlation/dependence, not causation. Rephrased as a dependence result in the strengths section above.

6. **From Harsh Critic — Various section-by-section style notes:** "Abstract/Introduction: The phrase 'convergence guarantee'...", "Section 3: only one LLM..." etc. These are presented as observations rather than specific identified weaknesses. The substantive concerns have been folded into the appropriate weakness tiers above; the rest are editorial suggestions rather than reviewable weaknesses.

7. **From Harsh Critic — "Number of rounds is fixed rather than determined by a convergence criterion":** The paper acknowledges this choice (line 60: "Following the setting in Huang et al. (2023a), we set the number of self-correction rounds as a constant"). This is a standard design choice, not a weakness.

---

## Novel Insights
None beyond the paper's own contributions. The two reviews offer complementary perspectives (the harsh critic identifying mathematical issues and overclaiming, the strength finder noting the empirical contributions) but do not surface observations about the paper's content that go beyond what the authors themselves present.

---

## Suggestions
1. **Either fix or remove Section 6.2.** The derivation's algebraic errors undermine its credibility. If a correct derivation exists, provide it with rigorous normalization and clearly stated assumptions. Otherwise, drop the theoretical section entirely — the empirical findings are valuable on their own.
2. **Tone down causal language throughout.** Replace "causal relationship," "strong driving force," and "convergence guarantee" with "strong dependence," "is associated with," and "empirical convergence" / "stable convergence."
3. **Clarify the "irreversibility" definition.** State clearly that the concept follows the direction of the most recent instruction (not that it is immutable), and provide quantitative analysis of whether the concept partially reverts between intervention rounds in Figure 5(b).
4. **Repeat the core convergence analysis on at least one additional LLM** (different family or size) to strengthen generality claims.
5. **Add confidence intervals or variance estimates** to the performance and uncertainty curves across multiple seeds or prompt templates.

---
