Now I have a thorough understanding of the paper and the reviewer claims. Let me produce the final consolidated review.

---

## Summary

This paper empirically studies two paradigms for using LLMs in reinforcement learning: (1) **direct policy modeling**, where the LLM generates actions, and (2) **indirect policy modeling**, where the LLM first generates a reward function (via AI feedback preferences, direct scalar output, reward-as-code, or embedding similarity) that is then optimized by a standard RL algorithm. Across four diverse domains (MiniWob, Wordle, NetHack, MetaWorld), the paper finds that AI-feedback-based reward modeling is the most generally applicable zero-shot approach, analyzes how AI feedback improves credit assignment and exploration, and explores fine-tuning strategies that preserve prior knowledge while improving downstream RL performance.

---

## Strengths

1. **Comprehensive comparison of LLM-based reward modeling methods across diverse domains.**  
   Figure 1 (indirect_comparison) systematically evaluates four distinct approaches (Direct Scalar, AI Feedback, Reward as Code, Embedding-based) on four environments spanning natural-language web interaction, reasoning, open-ended exploration, and continuous control. AI Feedback is the only method that succeeds across all domains, providing clear evidence that among LLM-derived reward methods, preference-based elicitation is the most robust.

2. **Empirical diagnosis of why LLMs fail as direct policies.**  
   The binary prediction experiment (Figure 2b) shows that GPT-4o performs near chance (≈50%) at distinguishing ground-truth next observations from random ones and ground-truth actions from random ones. This directly tests—and supports—the hypothesis that LLMs' limited understanding of environment dynamics and action spaces underlies their poor direct-policy performance, a diagnosis that goes beyond simply observing failures.

3. **Prompt engineering can replace hand-crafted exploration mechanisms.**  
   The NetHack exploration experiment (Figure 5) demonstrates that modifying the AI feedback prompt to favor diverse (non-repetitive) observations achieves performance comparable to adding a separate count-based exploration bonus (Eq. 3), eliminating the need for explicit counting functions. This cleanly shows how the flexibility of natural language can absorb algorithmic components.

4. **Evidence that AI-feedback rewards correlate with high-quality value functions.**  
   The correlation analysis (Figure 4) shows that AI-feedback-derived reward models increasingly align with the value function of an improving RL agent across three domains. The Wordle experiment is particularly clean: a code-generated near-optimal policy's Monte Carlo value function correlates almost perfectly with the LLM-derived reward, providing independent (non-circular) evidence that these rewards encode structure relevant to optimal behavior.

5. **Fine-tuning for reward modeling can improve RL performance while largely preserving prior knowledge.**  
   The fine-tuning experiments (Figure 6) show that fine-tuning PaliGemma on ~100 synthetic image-caption pairs for AI feedback yields substantial RL gains on the sweep-into task, with minimal degradation on standard multimodal benchmarks (POPE, GQA, AI2D, MMMU)—and even improvement on AI2D. This is a practically useful observation regardless of the comparison to direct fine-tuning.

---

## Weaknesses

### Fatal
None.

### Major

1. **Confounded comparison between direct and indirect policy modeling (different models, different prompting budgets).**  
   The direct LLM Policy method uses GPT-4o (a stronger, closed-source model) with a full suite of prompting techniques (Chain of Thought + In-Context Learning + RCI self-refinement). The indirect AI Feedback method uses Llama 3 / PaliGemma (weaker, open-source models) with only Chain of Thought prompting. The paper states this asymmetry explicitly (lines 77, 148, 163) and frames it as a strength ("despite the more capable model and richer prompts, direct still loses"). However, this design means the headline claim—that *indirect modeling more-readily solves RL tasks*—cannot be cleanly attributed to the *direct vs. indirect paradigm*. The observed gap could be driven by model capability, prompting budget, or both. A fair comparison holding the LLM fixed (e.g., using GPT-4o for both, or testing both methods with the same model family) would be needed to support the central claim as stated.

2. **Confounded fine-tuning comparison between direct and indirect policy modeling.**  
   The fine-tuning experiments compare two fundamentally different procedures: (a) **Indirect**: fine-tune PaliGemma on image-caption pairs (standard supervised learning with a language head), vs. (b) **Direct**: fine-tune via behavior cloning with a VQ-VAE token-overwriting scheme (RT-2 style) that directly modifies the model's vocabulary. These differ not only in the objective (reward prediction vs. action selection) but also in the invasiveness of the architectural modification. The finding that direct fine-tuning causes more catastrophic forgetting is therefore expected from the specific *procedure* chosen—aggressive token overwriting vs. standard cross-entropy on captions—and not attributable to "direct vs. indirect modeling" per se. The conclusion about forgetting (lines 279, 292–293) is not well-supported by this confounded comparison.

### Minor

1. **Credit assignment analysis has some circularity.**  
   The quantitative correlation analysis (Figure 4) computes the correlation between the AI-feedback reward model and the value function of an agent *trained on that same reward model*. A high correlation is partly expected by construction—the RL algorithm optimizes toward that reward, so the value function will naturally align with it. The Wordle experiment (independent near-optimal policy, near-perfect correlation) partially redeems this, but it is a single domain. The gridworld qualitative example (Figure 3/doorkey) is illustrative but not tested across multiple seeds or domains. The claim that AI feedback "shortens the horizon over which credit must be propagated" is plausible but the evidence would be stronger with comparisons to other dense reward shaping baselines (e.g., potential-based shaping).

2. **No non-LLM baselines.**  
   The paper compares only among LLM-derived methods. Claims that LLMs "excel at reward modeling" or that AI Feedback yields "the most generally applicable approach" are relative to other LLM methods; no comparisons to standard RL algorithms (PPO, SAC) with hand-crafted or learned rewards are provided. This limits the reader's ability to calibrate what "good performance" means in absolute terms. (The paper's scope is evaluating LLM-based methods, so this is not fatal, but it weakens the strength of the generality claims.)

3. **Final RL success rate after fine-tuning not reported numerically.**  
   The paper reports the initial zero-shot success rate (15% on sweep-into) and states "significant gains" after fine-tuning, but does not state the final numerical success rate in the text. The figure presumably shows it, but the number should be in the text for clarity.

4. **Exploration prompt modification not fully described.**  
   The description of the modified exploration prompt is cut short (line 243–244: "The prompt was also modified to steer the LLM towards avoiding low entropy sequences, i.e."), leaving the exact prompt modification unspecified. For reproducibility and understanding, this detail should be provided.

5. **No ablation of prompting complexity for direct policy.**  
   The paper states that combining all prompting techniques worked best for LLM Policy (line 77) but does not ablate individual components. Without this, the reader cannot assess whether direct policy failure is due to suboptimal prompting or inherent limitation.

### Trivial
- The final RL success rate after fine-tuning should be reported numerically in the text rather than only in a figure.

---

## Nice-to-Haves

- **Statistical significance tests.** The paper reports error bars (standard error over 10 seeds), which is standard, but formal significance tests (e.g., bootstrap hypothesis tests) on the main comparisons would strengthen confidence in the results.
- **Non-LLM baselines** to calibrate absolute performance levels (e.g., PPO with a dense hand-crafted reward, or RND for exploration).
- **Fairer fine-tuning comparison** using the same training objective architecture (e.g., both via language-head cross-entropy) to isolate the effect of direct vs. indirect modeling from the effect of fine-tuning procedure.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"Prompts not provided in the paper / missing prompting details."** The parser strips appendix material from all papers; prompts would be in the original appendix. Removed per hard rule about missing appendix content.
- **"Wordle RL results not clearly reported / not in Figure 2a."** Figure 2a (actor_comparison) explicitly compares LLM Policy vs. AI Feedback across domains including Wordle. The critic appears to have missed this. Removed as factually incorrect.
- **"No error bars or significance tests"** framed as a critical omission. Error bars (standard error, 10 seeds) are present. Significance tests are a nice-to-have, not a requirement. Demoted to Nice-to-Haves.
- **"Global criticism about missing non-LLM baselines as an evidential gap for the 'excelling' claim."** This is partially valid but the paper's scope is explicitly comparison of LLM-based methods. Demoted to Minor and re-framed.
- **Strength Finder claim that "fine-tuning results directly support the claim that indirect modeling mitigates forgetting"** without caveat. The confounded comparison weakens this attribution. Strength retained but is reported with the caveat in this review.

---

## Novel Insights

Beyond the paper's own contributions, a notable emergent insight is the asymmetry in what types of knowledge LLMs encode well: they encode *reward-relevant knowledge* (what outcomes are desirable, which states represent progress) far better than *transition-relevant knowledge* (what action leads to what next state). The binary prediction experiment (Figure 2b) shows near-chance performance on dynamics prediction, while the AI Feedback results show strong reward model quality. This suggests that LLMs' pretraining data contains more signal about "what is good" than "what happens next," which has implications beyond this specific RL setting—for example, explaining why LLM-based reward learning often succeeds while LLM-based world modeling struggles.

---

## Suggestions

1. **Fix the core confound in the direct vs. indirect comparison.** Run both methods using the **same underlying LLM** (e.g., GPT-4o for direct policy and GPT-4o for preference labeling for AI Feedback). This single change would dramatically strengthen the central claim.
2. **Deconfound the credit assignment analysis.** Show that AI-feedback rewards correlate with value functions from an *independently trained* optimal policy (as done for Wordle) on at least one additional domain.
3. **Use a comparable fine-tuning procedure** for both direct and indirect methods. Fine-tune both via language-head cross-entropy (reward prediction vs. action prediction) rather than using an invasive VQ-VAE scheme for the direct method, so the comparison isolates the paradigm rather than the procedure.
4. **Report the final success rate** after fine-tuning numerically in the text.
5. **Consider adding at least one non-LLM baseline** (e.g., PPO with a simple shaped reward) to provide an absolute performance anchor.

---

## Score and Decision

This paper tackles an important question and contributes useful empirical observations: the systematic comparison of LLM-based reward methods across diverse domains, the diagnosis of LLMs' poor dynamics understanding, the exploration-through-prompting finding, and the encouraging result that fine-tuning for reward modeling can preserve prior knowledge while improving RL performance. However, the two headline claims—that indirect policy modeling is superior and that fine-tuning for reward modeling mitigates forgetting better than fine-tuning for direct policy—rest on confounded comparisons (different models/prompting budgets, different fine-tuning procedures). These confounds are acknowledged but not resolved; they weaken the paper's strongest conclusions. The paper is transparent and the individual observations have value, but the central argument is not as cleanly supported as it should be. With revisions addressing the comparison fairness, this could be a solid contribution.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>