Now I have all the information needed. Let me produce the final consolidated review.

## Summary

This paper presents Musketeer, a vision-language model with fully shared parameters trained jointly on heterogeneous tasks (visual grounding, VQA, captioning, visual entailment, classification, detection, and text summarization). The core technical contribution is Task Explanation Prompts (TEPs)—structured natural-language descriptions (data description, I/O format, output description, instance prompt) that are appended to the model input to reduce task interference. Experiments show that a single Musketeer model achieves results competitive with single-task OFA specialists and substantially outperforms multi-task models using standard (BaseP) or one-hot prompts, while also enabling positive transfer in few-shot and zero-shot settings.

## Strengths

- **Fully-shared multi-task model matches or exceeds single-task specialists.** Table 1 shows Musketeer_Large on Subset$_{\text{caption}}$ outperforms the single-task OFA_Large on visual grounding (90.8 vs. 90.1 val; 93.1 vs. 92.9 test-A; 87.6 vs. 85.3 test-B) and achieves comparable caption B@4 (42.5 vs. 42.4) and CIDEr (140.2 vs. 142.2), using a single model with no task-specific heads or fine-tuning.

- **TEP consistently outperforms shorter prompts across all tasks and data scales.** Table 2 shows TEP outperforms both BaseP and one-hot prompts on all six evaluated tasks at all three dataset scales. On Subset$_{\text{small}}$: VG val 87.5 (TEP) vs. 85.8 (BaseP) vs. 84.2 (one-hot); VE test 84.5 vs. 83.5; VQA test-dev 70.6 vs. 69.2.

- **Adding more tasks improves TEP-trained models but degrades BaseP models.** Table 5 shows that as the number of training tasks increases from 1 to 7, TEP models improve on most metrics (VG val 86.4→87.5, CIDEr 128.9→130.3), while BaseP models decline substantially (VG val 88.6→85.8, CIDEr 138.2→125.5, VE test 89.2→83.5). This demonstrates TEP's core claim: structured descriptions enable positive transfer rather than interference.

- **TEP enables strong few-shot and zero-shot transfer.** Table 3 shows TEP outperforms BaseP by ~3–4% in few-shot VG (e.g., 100 VG samples: TEP 79.2 vs. BaseP 75.1). Table 6 shows zero-shot VE accuracy of 49.1% (TEP) vs. 38.6% (BaseP) on an unseen task. Table 7 shows zero-shot summarization on unseen datasets where TEP substantially beats BaseP (R-1: 40.2 vs. 33.3 on news-summary).

- **Ablation confirms every TEP subprompt contributes positively.** Table 8 shows each subprompt removal hurts performance; full TEP achieves the highest VG val (87.5), VE test (84.5), and caption CIDEr (130.3) compared to any partial version.

- **Competitive with much larger multi-task models.** Table 4 shows Musketeer_Base (182M) outperforms Unified-IO_Large (776M) on VE test (89.1 vs. 86.1) and caption CIDEr (137.2 vs. —), and Musketeer_Large (472M) achieves 75.0 VQA vs. Unified-IO_XLarge (2.9B) 77.9 while using only 44% of VQAv2 data.

## Weaknesses

### Fatal
None.

### Major

- **The structural decomposition claim is not separated from prompt length/informativeness.** The paper compares TEP only against BaseP (a single sentence) and one-hot vectors. Both are far shorter than TEP. The paper mentions "Task Description (ChatGPT)" and "Task Description (Wiki)" in the similarity analysis (Fig. 4) but does not report quantitative multi-task performance for either. The central claim that TEP's *explicit decomposition* into subprompts (Data Description, I/O Format, etc.) drives the improvement—rather than simply providing more tokens or more informative text—cannot be assessed without a length-controlled baseline: a long, informative, but unstructured paragraph covering the same information as TEP without the formal subcomponent tags. The ablation in Table 8 shows removing subprompts hurts, but this does not test whether a single cohesive paragraph would achieve comparable or better results. While this does not invalidate the paper's empirical findings (TEP > BaseP/one-hot), it leaves a significant gap in the mechanistic argument.

### Minor

- **"Consistently improves" overstates the pattern in Table 5.** The paper states "the TEP-trained model consistently improves" as more tasks are added. However, Table 5 shows a non-monotonic pattern: from 1→3 tasks, TEP's VG val drops from 86.4 to 86.0, Caption CIDEr drops from 128.9 to 123.9, before recovering at 5 and 7 tasks. While the overall trend from 1→7 is positive (and sharply contrasts with BaseP's steady decline), calling it "consistently improves" is imprecise. The dip at 3 tasks and the absence of error bars make it unclear whether this is noise or a genuine effect of task-composition.

- **TEP underperforms BaseP at #Task=1—uncommented.** In Table 5, at #Task=1, TEP scores *lower* than BaseP on all metrics (VG val 86.4 vs. 88.6, VE test 84.2 vs. 89.2, CIDEr 128.9 vs. 138.2). This is consistent with TEP being designed for interference reduction (which is unnecessary with one task), but the paper does not acknowledge this important boundary condition. Discussing when TEP is and is not beneficial would strengthen the paper's credibility.

- **No error bars or multiple runs for key tables.** Tables 4, 5, and 6 report single-run results. Many differences between methods are small (0.1–0.5 points for some metrics). Without variance estimates, it is impossible to assess which differences are meaningful versus noise. This is a standard practice gap that should be addressed.

- **Object detection results are described but not reported.** The paper states that OFA-based models have low baseline performance on detection and "we follow OFA and choose not to present object detection task as our main results," adding that Musketeer "still outperform[s] specialist OFA" on detection. If claims about detection performance exist, the actual numbers should be reported so readers can assess trade-offs. Excluding them—especially while including a purely language task (text summarization)—weakens the full-task picture.

### Trivial
None.

## Nice-to-Haves

- **Add a long, informative, unstructured paragraph baseline** (ideal content: same information as TEP but as a single cohesive paragraph without subcomponent tags) to the main multi-task comparison. This would directly test whether TEP's decomposition is what drives the benefit, or whether any long informative prompt suffices.

- **The similarity matrices (Fig. 4)** provide an interesting qualitative motivation, but the paper would benefit from a simple correlational analysis linking matrix properties (e.g., inter-task separation) to observed multi-task accuracy.

- **Add "Task Description (ChatGPT)" and "Task Description (Wiki)" as prompt baselines** in the main performance table, not just in the similarity analysis. These are natural baselines that bridge the gap between BaseP and TEP.

- **Brief discussion of computational cost** (training compute comparison between Musketeer and N specialists) would help ground the practical claims. The paper mentions 10–15% inference latency increase but does not discuss training cost.

- **Error bars or multiple seeds** for the key ablation results (Tables 4, 5, 6) would greatly increase confidence in the reported patterns.

- **Provide a lower-bound baseline** (e.g., majority-class prediction) for the zero-shot VE experiment, to contextualize the 49.1% accuracy.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Zero-shot VE near chance"** — Removed as factually inaccurate. 49.1% is 16 points above random chance (33.3%) on a 3-class task and represents a 10.5-point absolute gain over BaseP (38.6%). This is a meaningful result, not "near chance." The paper appropriately presents it as a significant improvement.

- **"Prompt construction details missing"** — Removed because the parser strips appendix/supplementary material from all papers. The exact prompts likely exist in the original submission's supplementary.

- **"Clarity on initialization"** — Removed. The paper is explicit: "initialize weights of Musketeer from pretrained model in wang2022ofa" (Section 4.2). This is standard and clearly stated.

- **""Joint training/inference" phrasing confusion"** — Removed as a style nitpick.

## Novel Insights

The reviews collectively highlight a key gap in the paper's argumentation: the paper convincingly demonstrates that TEP (structured, long) outperforms BaseP (short, flat) and one-hot (minimal), but it does not isolate *which* property of TEP drives the benefit. Is it the decomposition into subcomponents, the sheer length/informativeness, or the specific natural-language content? The similarity analysis (Fig. 4) attempts to motivate the structural claim but stops short of quantitative validation. This is a common pattern in prompt-engineering papers and points to a broader methodological challenge: how to control for informativeness when comparing prompts of different lengths and structures. The paper's core empirical finding—that a fully-shared model with TEP approaches specialist performance—is well-supported and valuable regardless of the resolution of this mechanistic question.

## Suggestions

1. **Add a long unstructured paragraph baseline** to the main multi-task evaluation (Tables 2 and 5). This is the single most impactful experiment the authors could add. If the unstructured paragraph performs similarly to TEP, the paper's contribution should be reframed around "long informative prompts" rather than "structured prompts." If TEP outperforms it, the structural claim is strongly validated.

2. **Correct the language on line 494:** replace "consistently improves" with "improves overall" or "shows a positive trend" and note the non-monotonic pattern at 3 tasks in the discussion.

3. **Report object detection results** in a supplementary table or a footnote, even if they are low, to allow full transparency.

4. **Add a brief discussion** of the #Task=1 case where TEP underperforms BaseP, clarifying the boundary conditions of TEP's utility.

5. **Include error bars** or at minimum note that results are from single runs and which conclusions are robust despite this.

## Score and Decision

The paper presents a clean, well-executed idea with strong empirical support. The core contribution—that structured task descriptions enable a fully-shared multi-task model to compete with specialists—is clearly demonstrated across multiple tasks, data scales, model sizes, and few/zero-shot settings. The main weakness (lack of a length-controlled baseline for the structural claim) is significant but does not invalidate the paper's key results; it primarily limits the strength of the mechanistic story. The overstatement about "consistent improvement" and the omission of detection numbers are easy to fix. The paper makes a genuine contribution to multi-task vision-language modeling.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>