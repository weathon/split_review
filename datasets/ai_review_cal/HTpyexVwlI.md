- Decision: Reject
- Avg Score: 3.50
- Scores: 5, 3, 3, 3
Now I have all the information I need. Let me construct the final consolidated review.

## Summary

The paper introduces V-TIFA, a method that uses pretrained vision-language models (VLMs) as direct evaluative feedback providers to train instruction-following agents via reinforcement learning, eliminating the need for handcrafted reward functions, human demonstrations, or environment-specific code. The core idea is to query a VLM to rate entire agent trajectories based on language instructions, using these ratings as reward signals for off-policy RL. Experiments on the ALFRED benchmark across four household environments (80 instructions) show V-TIFA outperforms prior VLM-based reward methods (CLIP, R3M, RoboCLIP) and approaches ground-truth reward performance.

## Strengths

1. **Consistent outperformance of prior VLM-based reward methods under the same conditions**: Figure 4 shows V-TIFA achieves higher success rates than CLIP Reward, R3M Reward, and RoboCLIP Reward across all four ALFRED environments, often substantially closing the gap to ground-truth reward training. This is concretely supported by the training curves and text discussion.

2. **Eliminates reliance on human data and environment access**: Section 4 describes how V-TIFA uses a pretrained VLM to directly output ratings from trajectories and instructions, requiring no human demonstrations, no human feedback, and no access to environment code or ground-truth state. This is a clear practical advance over inverse RL and code-based reward methods.

3. **Ablation identifies actions as the critical design element**: Section 5.3 ablates prompt components and shows that including actions in the summary prompt yields the largest performance gain. This provides actionable insight into why VLM-based evaluation works — the VLM's reasoning about action-driven state changes matters more than visual similarity.

4. **Evaluative feedback is shown to outperform comparative feedback with a concrete explanation**: Section 6 demonstrates that comparative (pairwise) feedback yields worse alignment than evaluative feedback, and manual inspection reveals VLMs bias toward shorter trajectories in comparisons. This supports V-TIFA's design choice of direct ratings over preferences and contributes a documented limitation of comparative feedback.

5. **Offline VLM comparison provides practical guidance**: Section 5.3 compares five VLMs (Gemini Flash/Pro, GPT-4o Mini/4o, Qwen2-VL) on offline trajectory alignment, showing larger models achieve better agreement with ground-truth rewards. This helps practitioners choose a cost-performance trade-off, even though only Gemini 1.5 Pro was used for actual training.

## Weaknesses

### Fatal
None.

### Major

1. **Missing variance/error bars in the main training results (Figure 4).** The paper reports training curves "across three runs" but plots only single lines with no error bars, confidence intervals, or discussion of run-to-run variability. Given that RL training in ALFRED is known to be noisy (the authors report collected trajectories with averaged returns of 0.6–0.7 from GT agents), the reader cannot assess whether the reported advantages over baselines are robust or within noise. This does not invalidate the contribution, but it substantially weakens the confidence one can place in the headline claims. The paper states "Success rates are measured every 100 epochs, averaged over 500 episodes" — this is evaluation averaging, not run-level variance.

2. **Only one VLM (Gemini 1.5 Pro) is used for actual agent training.** The method is evaluated with a single VLM in the online RL loop. Section 5.3 tests other VLMs (GPT-4o, Qwen2-VL, Gemini Flash, GPT-4o Mini) on offline collected trajectories, but this is only an alignment check — we do not know whether these VLMs would similarly succeed when used to train policies online. Since the method's generality across VLMs is part of its claimed contribution, this is an evidential gap. Training with at least one additional VLM (e.g., GPT-4o or Qwen2-VL) and comparing final performance would substantially strengthen the claims.

### Minor

1. **Missing IQL hyperparameters and policy architecture details.** The paper specifies using "a variant of Implicit Q-Learning (IQL)" but provides no hyperparameters (learning rates, batch size, network architecture, target update rate, etc.). This harms reproducibility and makes it difficult for other researchers to build on the work.

2. **Representation of actions in the prompt is underspecified.** The paper discusses including actions in the summary prompt (Section 5.3) but does not specify how actions are represented textually (e.g., as raw action names like "MoveAhead, Pickup", as natural language descriptions, or otherwise). This is a small but unnecessary ambiguity for reproduction.

3. **The "across three runs" claim for Figure 4 is text-only.** While the paper mentions three runs, there is no textual summary of final mean/s.d. success rates across runs (e.g., in a table). Even without plotted error bars, a table showing mean ± s.d. for each method in each environment would improve evidential strength.

### Trivial
- Figure 2 (the prompt template) is referenced but appears to be an embedded image with text that cannot be fully verified from the text-only extract. The textual description of the prompt is otherwise clear.

## Nice-to-Haves

- **Binary success/failure VLM baseline**: Training an agent with a VLM that directly outputs binary success/failure (instead of multi-level ratings) would isolate the benefit of the multi-level rating scheme itself. The paper already analyzes this in the GT alignment setting (thresholded ratings) but does not train with it.
- **Prompt sensitivity analysis**: The paper uses a single prompt template. A brief discussion or ablation of prompt phrasing would help assess robustness.
- **Computational cost of baselines**: The paper reports V-TIFA's training time (~1.5 days) but not the cost of baselines, which would be useful for comparison.
- **Segmentation details**: Whether trajectory segments overlap and how partial final segments are handled is not specified.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Overclaiming: 'V-TIFA does not require manually crafted task specifications'"**: The critic interprets "task specifications" as the instructions themselves, but the paper contrasts with CLIP-based methods that require specially crafted text descriptions for reward computation (e.g., "a clean kitchen"). V-TIFA uses the natural instructions directly. The paper's wording is clear in context. **Removed: misreading of the paper.**

- **"Limited task diversity and environment scope (only ALFRED)"**: ALFRED is a standard, challenging benchmark for instruction following with realistic visuals and crowd-sourced language. Claiming the paper should also run experiments on R2R or mobile manipulation is scope creep beyond the paper's stated focus. **Removed: scope creep.**

- **"Rating levels not specified in the method section"**: Rating levels and their labels ("very bad" through "very good") are explicitly defined in Section 3 (Preliminaries), which is the natural location for this definition. **Removed: factually incorrect — the information is in the paper.**

- **"Using same VLM for summarization and rating could introduce bias"**: This is speculative concern without supporting evidence or any concrete analysis showing such bias manifests. **Removed: speculative.**

- **"Grammatical error in abstract"**: Parser artifact rule applies. **Removed: formatting/grammar nitpick.**

- **"Overclaiming about outperforming 'existing reward generation methods'"**: The critic acknowledges the comparison to code-based methods is "fair given the scope." The paper explicitly compares to VLM-based reward methods, which is appropriate. **Removed: acknowledged as fair by the critic themselves.**

- **"Clarify number of checkpoints for offline dataset"**: The paper states ~500 trajectories from 40 per checkpoint, which implies ~12-13 checkpoints. The math is self-consistent. **Removed: the information is sufficient.**

## Novel Insights

The reviews do not surface insights that go beyond the paper's own contributions. The observation that evaluative feedback outperforms comparative feedback in this setting (Section 6) is part of the paper's own analysis. The key takeaway — that zero-shot VLM trajectory ratings can effectively train instruction-following agents in a multi-step embodied setting — is already clearly stated.

## Suggestions

1. **Add error bars or shaded intervals to Figure 4** and report final success rates with standard deviations across seeds in a table. This is the single highest-leverage improvement.
2. **Train an agent with at least one additional VLM** (e.g., GPT-4o or Qwen2-VL) and report comparison results to demonstrate generality beyond Gemini 1.5 Pro.
3. **Provide IQL hyperparameters and policy network architecture details** in the main paper or appendix (noting that missing appendix content is a parser artifact, but the main paper should at minimum reference where hyperparameters can be found).
4. **Specify how actions are represented textually in the summary prompt** (raw action names, descriptions, etc.).
5. **Slightly clarify the claim about "not requiring manually crafted task specifications"** to read "not requiring manually crafted reward specifications" to avoid ambiguity.
