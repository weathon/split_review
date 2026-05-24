## Summary

DaVinci introduces a two-stage framework (supervised fine-tuning followed by GRPO reinforcement learning) for parsing scientific diagram images into compilable TikZ code. The paper contributes: (1) TiKZ30K, a curated dataset with reordered drawing sequences and comment-based planning scaffolds; (2) a hybrid reward function that leverages vectorized PDF representations to extract text and geometric primitives for precise reward signals; and (3) strong empirical results—DaVinci-7B achieves 97.6% compile rate on DATiKZv3, surpassing GPT-5, Claude-Sonnet-4, and all open-source baselines, with human evaluation confirming these improvements.

## Strengths

- **Near-perfect compile rate through RL post-training.** DaVinci-7B achieves 97.60% Pass@1 compile rate, far exceeding the SFT-only variant (84.50%) and all baselines including Claude-Sonnet-4-Thinking (86.90%) and GPT-5-Default (72.88%) (Table 1). This directly validates the core claim that RL refines structural relationships.
- **Code reordering and comment injection are causally validated.** The ablation (Table 4) shows reordering alone increases Pass@1 by 9.04% over the raw dataset, and adding comment annotations yields a further 5.72% gain — direct causal evidence that these underexplored data features are critical for diagram parsing.
- **Hybrid reward function with vectorized PDF extraction improves text and geometry metrics.** The reward ablation (Table 5) shows adding the spatio-textual reward lifts the textual match score from 37.23 to 41.58, and adding the geometric reward raises the geometry score from 41.44 to 44.10. Using PyMuPDF to extract elements from the PDF vector representation (rather than OCR on rasterized images) is well-motivated and avoids well-known OCR failure modes for diagrams.
- **Rigorous human evaluation with quantified inter-annotator agreement.** The Best-Worst Scaling study (Section 4.4) uses six evaluators and reports split-half reliability of 0.7227 and 0.7878 — stronger than many studies that report only pairwise agreement or none.
- **Nuanced analysis of code-level vs. visual-level metrics.** The paper observes that DaVinci-7B's cBLEU decreases after RL while all visual metrics improve, and correctly explains that "strict code-level similarity is neither necessary nor always desirable" — a genuine insight for evaluation methodology in code-generation tasks.
- **Legally compliant dataset release.** The paper explicitly addresses data licensing by releasing diff files and reproducible scripts for restricted-license sources, enabling full reproducibility without violating source licenses.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Prompt details for proprietary baselines are not disclosed.** The paper shows a prompt template in Figure 3 ("This is a picture of a scientific figure. Generate LaTeX code that draws this scientific figure using TikZ...") but does not explicitly state whether the identical prompt format was used for GPT-5, Claude-Sonnet-4, and Gemini-2.5-Pro, or whether these models received any task-specific system instructions. While it is standard practice to use comparable prompts, omitting this detail prevents the reader from assessing whether the comparison is fully apples-to-apples. The authors should disclose the exact prompt strings for all baselines.

2. **The "surpasses leading proprietary models" framing is imprecise given Gemini's performance.** On several metrics (DreamSim, SSIM, LPIPS, SigLIP) and in human evaluation (Table 3: Gemini scores 0.50, DaVinci scores -0.01), Gemini-2.5-Pro-Thinking outperforms DaVinci. The paper acknowledges this in the text (Section 4.3: "Gemini-2.5-Pro presents better performance than DaVinci-7B regarding certain metrics") but the abstract and conclusion state that DaVinci "surpasses leading proprietary models like GPT-5 and Claude-Sonnet-4" without mentioning Gemini as an exception. The claims about GPT-5 and Claude-Sonnet-4 are accurate; the framing should simply acknowledge Gemini's stronger perceptual performance to avoid overclaiming.

3. **Implementation details of the matching algorithms are underspecified.** The text matching uses a "Levenshtein distance with an adaptive threshold" and the geometric matching uses a "weighted sum of differences" in attributes with a "scaling constant k" — none of these are specified. The adaptive threshold selection method, the specific weights in the geometric cost function, and the value of k are not reported. While these details affect the reliability of the reward signal, they primarily impact reproducibility rather than the validity of the paper's conclusions (since the ablation study consistently shows improvements from adding each reward component).

4. **The "error-free" terminology could be read too broadly.** The paper claims extraction from PDF vectorized representations is "error-free," which is technically correct for the *extraction* step (PDF metadata contains exact text and geometry). However, the subsequent matching algorithm (Levenshtein matching, bipartite matching with cost functions) is not error-free and could introduce mismatches. The paper would benefit from a brief clarification that "error-free" refers to extraction (bypassing OCR) rather than the full matching pipeline.

### Trivial

- The compile failure analysis is limited to one sentence ("mainly dense visualizations like scatter plots, where the model over-produces data points, leading the output to exceed the context limit"); a brief breakdown of failure types would be helpful.
- The equal-weight design of the hybrid reward components (Eq. 2) could benefit from a brief justification or sensitivity note.

## Nice-to-Haves

- An ablation of the SFT stage (running RL directly on the base model without SFT) would quantify the importance of cold-start data.
- Applying the same pipeline to a different base MLLM (e.g., LLaVA-NeXT) would show the method is not idiosyncratic to Qwen2.5-VL-7B.
- A correlation analysis between the reward components (text, geometry) and human judgment on the 100 human-evaluation samples would strengthen the case that the proxy rewards are well-designed.
- A sensitivity study varying the relative weights of the reward components would test the robustness of the equal-weight choice.

## Removed Points

- **Claim that baseline comparison is unfair due to prompt engineering asymmetry (from Harsh Critic, Weakness 1):** This is speculative. The paper shows the prompt template in Figure 3, and standard practice in the field is to use comparable inputs. There is no evidence of deliberate unfair prompting. However, the specific prompts *should* be disclosed, which is retained as Minor weakness 1.
- **Claim that "error-free" characterization is overstated because matching can produce mismatches (from Harsh Critic, Weakness 2):** The paper uses "error-free" to describe the *extraction* step (bypassing OCR via vectorized PDF), not the matching step. This is technically correct. The missing implementation details are a separate concern, retained as Minor weakness 3.
- **Claim about inconsistency in "no special weights for each reward component" (from Section-by-Section Notes):** The paper means equal weighting; this is a clear statement, not an inconsistency.
- **Request for RL-only without SFT ablation, generalization to other backbones, and reward-human correlation analysis (from Harsh Critic, "Missing Parts"):** These are nice-to-have extensions beyond the paper's stated scope.
- **All pure formatting/style nitpicks and missing-appendix complaints:** These are parser artifacts.
- **Several strengths from Strength Finder removed as generic or unsupported:** "Scalable and legally compliant dataset release" kept; "Outperforms proprietary models on multiple metrics" collapsed into the broader strength framing.

## Novel Insights

The paper's key insight that *drawing order normalization* in diagram code is a critical but overlooked data feature for autoregressive models is genuinely novel and well-supported by ablations. Most prior work treats code ordering as irrelevant for rendering-based languages (SVG, TikZ), but this paper correctly identifies that training autoregressive models on arbitrarily ordered code sequences is detrimental. The second insight—that inline comments can serve as *planning scaffolds* during SFT, effectively injecting structural decomposition into the training data without requiring explicit reasoning traces—is a practical contribution that could transfer to other code-generation tasks. The observation that enabling explicit reasoning ("thinking" modes) does not consistently improve diagram parsing (and sometimes degrades it) is a useful counterpoint to the prevailing trend of adding chain-of-thought to everything.

## Suggestions

1. **Disclose the exact prompt template(s) used for every baseline model** — both the system instructions and the user prompt. If the same template was used for all, state this explicitly.
2. **Reframe the abstract/conclusion** to say "surpasses GPT-5 and Claude-Sonnet-4" (which is accurate) and briefly acknowledge Gemini-2.5-Pro as a stronger competitor on perceptual metrics, noting this as an interesting direction for future work.
3. **Specify the missing implementation details** in the appendix: the adaptive threshold algorithm for Levenshtein matching, the weights in the geometric cost function, and the scaling constant k.
4. **Clarify that "error-free" refers to the extraction from vectorized PDFs** (bypassing OCR), not the matching pipeline.
5. **Add a brief failure-type breakdown** for the 2.4% compile failures — even a simple categorical count would help users understand practical limitations.

## Score and Decision

**Bracketing pass (Round 1):** The paper was compared against three score bands. For the weak band (avg < 3.5), typical papers at scores 3.0–3.4 have either limited methodological contribution or weak empirical support — DaVinci is clearly far above this. For the middle band (3.5–7.5), comparable diagram-generation papers (AutomaTikZ at 6.50, Sketch2Diagram at 6.25) have simpler methods (SFT-only, no RL) and tackle easier problem formulations. For the strong band (7.5+), papers like AnalogGenie (7.50) have high domain novelty but comparable technical depth. Initial bracket: **6.0–8.0**.

**Narrowing pass (Round 2):** Retrieved CraftRTL (7.00), Diffusion on Syntax Trees (7.20), Articulate-Anything (6.20), and AutomaTikZ (6.50). DaVinci is stronger than AutomaTikZ (6.50) and Articulate-Anything (6.20) due to more sophisticated methodology and more rigorous evaluation. Compared to CraftRTL (7.00) — which has similar thoroughness in evaluation and data curation but targets a different domain — DaVinci has comparable technical depth with the addition of RL post-training. Compared to Diffusion on Syntax Trees (7.20), DaVinci has stronger practical contributions (dataset release, human evaluation) but less fundamental algorithmic novelty. The paper sits between these anchors.

**Final score: 7.0.** This reflects a strong paper with clear, well-validated contributions in methodology, dataset construction, and empirical results. The weaknesses are minor and addressable; none threaten the core claims.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>