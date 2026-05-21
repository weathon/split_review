---
job_id: f7874960-1118-4450-9857-335421efca5e
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: yEpE0QPpf8.pdf
paper: Grounding-IQA: Grounding Multimodal Language Model for Image Quality Assessment
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, it studies multimodal learning for image quality assessment, introduces a new task formulation, and contributes a dataset and benchmark for grounded multimodal evaluation.

## Minimum Quality
Pass ✅. The paper contains the expected scientific structure, including abstract, introduction, related work, method, experiments, quantitative/qualitative results, and conclusion; the work is coherent and empirically supported enough to merit full review, even though several methodological details remain insufficiently justified.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find any hidden instructions, suspicious embedded prompts, or other manipulative content targeting automated review systems in the provided paper text or figures.

# Expected Review Outcome:
## Summary
This paper introduces **Grounding-IQA**, a new multimodal image quality assessment paradigm that combines IQA with referring and grounding. The paper defines two subtasks, **GIQA-DES** for grounded quality description and **GIQA-VQA** for region-aware quality question answering, and builds a corresponding instruction-tuning dataset, **GIQA-160K**, plus a manually curated benchmark, **GIQA-Bench**. The authors also propose an automated annotation pipeline for generating grounded IQA data from existing descriptive IQA datasets, and show that fine-tuning several MLLMs on this data improves performance on the proposed benchmark.

## Strengths
1. **The problem formulation is meaningful and well motivated.** The paper identifies a genuine limitation of current MLLM-based IQA, namely that purely textual quality descriptions are often too coarse when quality defects are spatially localized. The move from “describe quality” to “describe quality and where it is” is sensible, and the split into GIQA-DES and GIQA-VQA is easy to understand.

2. **The paper contributes both a dataset and a benchmark, not just a training recipe.** GIQA-160K and GIQA-Bench are potentially useful resources for the community. In particular, the benchmark covers three distinct aspects, description quality, VQA accuracy, and grounding precision, which is a better evaluation design than reporting only language metrics.

3. **The automated annotation pipeline is reasonably structured and clearly illustrated.** **Figure 3** is one of the stronger parts of the paper. It makes the four-stage GIQA-DES pipeline and the derived GIQA-VQA generation process easy to follow, and helps justify how the authors turn existing descriptive IQA data into grounded supervision. Likewise, **Figure 4** gives a concrete intuition for why using a description phrase \( \mathcal{T}_r \) rather than a category name can improve localization quality.

4. **The empirical gains on the proposed benchmark are consistent.** In **Table 5**, the fine-tuned models improve substantially over general MLLMs and often over task-specific baselines. For example, Grounding-IQA (mPLUG-Owl2-7B) reaches the best or near-best numbers across several axes, including GIQA-DES BLEU@4, LLM-Score, and GIQA-VQA Acc(Y)/Acc(W), while also providing nontrivial grounding metrics. Even if one debates the benchmark design, the trend is fairly consistent.

5. **The ablations are directionally useful.** **Table 2** suggests that the proposed box refinement procedure is not cosmetic, since Ref-Box improves both grounding metrics and text metrics over Raw-Box. **Table 3** is also informative, showing that the two subtasks provide complementary supervision, with joint training improving GIQA-VQA grounding and accuracy relative to single-task variants.

6. **The qualitative examples are aligned with the paper’s main claim.** **Figure 7** is effective in showing the intended behavior: the model is not merely naming quality issues, but tying them to localized regions. This helps support the practical intuition behind the proposed task better than the scalar metrics alone.

## Weaknesses
1. **The benchmark is too small to support broad claims about a “new IQA paradigm”.**  
   The paper repeatedly positions grounding-IQA as an extension of IQA more broadly, but **GIQA-Bench contains only 100 images and 250 total samples** according to **Table 1** and **Section 3.4**. That is extremely limited for supporting strong claims about generality across image quality phenomena, domains, and spatial reasoning cases. With such a small benchmark, variance can be high, coverage can be narrow, and gains may reflect the annotation style of the benchmark rather than robust capability. This matters because the central contribution is not merely a model, it is a task definition and benchmark. If the benchmark is narrow, the claimed paradigm shift is correspondingly narrow.

2. **The automated data construction pipeline may bake teacher/model biases directly into the supervision, and the paper does not quantify annotation quality carefully enough in the main paper.**  
   The whole dataset hinges on a chain of model-generated annotations: Llama3 extracts tags, Grounding DINO proposes boxes, Q-Instruct filters boxes, and Llama3 generates VQA from descriptions, as described in **Section 3.2** and **Figure 3**. This is efficient, but it creates a strong risk that the resulting data reflects the quirks and blind spots of these upstream models rather than the underlying task. The paper states that GIQA-Bench is expert-annotated, but it does **not** provide a direct main-paper estimate of the precision/recall or agreement of the automatically constructed GIQA-160K annotations against human reference labels. Without such validation, it is hard to know whether the improvements come from learning a meaningful grounded IQA capability or simply adapting to a synthetic annotation style.

3. **Several evaluation components rely on LLM-as-a-judge scoring, but the protocol is underspecified and potentially unstable.**  
   In **Section 3.4**, both description quality and open-ended VQA accuracy use Llama3 scoring. However, the exact evaluation prompt, sampling settings, number of judge runs, and robustness to paraphrases are not specified in the main paper. This matters because the reported margins are not always large. For instance, in **Table 5**, differences in GIQA-DES LLM-Score among the stronger methods are often a few points, and Acc(W) gains are modest. Without a clearer scoring protocol, it is difficult to assess whether these are meaningful improvements or judge noise. Using BLEU@4 alongside LLM scoring partially helps, but BLEU is also a poor fit for open-ended quality descriptions.

4. **The mathematical specification of the coordinate discretization is unclear and appears inconsistent.**  
   In **Equation (1)**, the paper defines
   \[
   \mathrm{idx}_l = y_1 \cdot m \cdot n + x_1 \cdot n,\quad \mathrm{idx}_r = y_2 \cdot m \cdot n + x_2 \cdot n.
   \]
   If \(x_1,y_1,x_2,y_2\) are normalized continuous coordinates, this expression does not by itself produce a valid discrete grid index unless an explicit quantization operator such as floor/round is applied. More importantly, standard row-major indexing for an \(m \times n\) grid would usually look like \( \lfloor y m \rfloor \cdot n + \lfloor x n \rfloor \), not \( y \cdot m \cdot n + x \cdot n \) as written. Then in **Equation (2)**, the inverse mapping uses
   \[
   x_1' = (\mathrm{idx}_l \% n + 0.5)/n,\quad y_1' = (\mathrm{idx}_l / n + 0.5)/m,
   \]
   but the division should presumably be integer division or floor, which is not specified. As written, the discretization/inversion scheme is underspecified. This is not a cosmetic issue, because the representation of coordinates is central to the method and to the comparison in **Table 2(b)**.

5. **Algorithm 1 is underdefined, and some design choices seem heuristic without enough justification.**  
   In **Algorithm 1**, the filtering step asks Q-Instruct whether a cropped patch has quality \(<\mathcal{T}_q>\), but the mapping from free-form quality labels \( \mathcal{T}_q \) to a yes/no question is unclear. For example, if \( \mathcal{T}_q = \) “clear” or “medium”, what exact semantics does the binary question encode? Also, the merge condition on line 13,
   \[
   \text{area}(\mathcal{R}[i]) < T_a \ \text{and is-touch}(\mathcal{R}[i],\mathcal{R}[j]) \ \text{or coverage-ratio}(\mathcal{R}[i],\mathcal{R}[j]) > T_o,
   \]
   lacks parentheses, so operator precedence is ambiguous. The choice \(T_a=0.256\) and \(T_o=95\%\) is also not justified in the main paper. Since **Table 2(a)** shows only moderate gains from Raw-Box to Ref-Box, the paper should be more transparent about how sensitive these results are to these thresholds.

6. **The baseline comparison is useful but still incomplete in a way that affects the central claim.**  
   The paper compares against general MLLMs, grounding models, and IQA-oriented models in **Table 5**, which is good. However, some of the strongest “Ground” models were not trained for IQA, and some of the strongest “IQA” models were not trained for grounding. That means the paper is partly comparing specialized single-capability systems against a jointly fine-tuned multitask system on a new benchmark specifically designed for the joint task. This is not unfair per se, but it makes it harder to determine whether the improvement comes from the novelty of the task formulation or simply from adding in-domain supervision for the exact benchmark format. A stronger comparison would include controlled baselines trained on matched amounts of supervision without the authors’ particular pipeline, or simpler multitask formulations without the full grounding-IQA design.

7. **The gains on open-ended VQA are relatively modest, which weakens the claim of a substantial advance in fine-grained reasoning.**  
   In **Table 5**, the biggest gains are on Acc(Y), while **Acc(W)** improvements are much smaller. For example, Grounding-IQA (mPLUG-Owl2-7B) gets 0.5875 on Acc(W), only moderately above several baselines. This suggests the method may be learning strong pattern matching for localized yes/no questions more than deeper quality reasoning. Since GIQA-VQA is presented as a key component of the paradigm, the paper should be more candid about where the gains are concentrated.

8. **The claimed grounding precision may be inflated by benchmark/task design, and Tag-Recall is not described rigorously enough.**  
   In **Section 3.4**, Tag-Recall is said to require both IoU and object-name similarity exceeding 0.5, but the object-name similarity metric is unspecified in the main paper. Is it exact matching, embedding similarity, edit similarity, or judged by an LLM? Small wording changes can substantially alter this metric, especially since the outputs are natural language. Since Tag-Recall is a headline grounding metric in **Tables 2, 3, 4, and 5**, the lack of a precise definition is a real reproducibility issue.

9. **The paper’s scope is presented too broadly relative to the demonstrated cases.**  
   Many examples in **Figures 2, 5, and 7** involve salient local objects or regions, such as people, horses, hands, shadows, blur on foreground subjects, and so on. These are intuitive and visually compelling, but they do not convincingly establish coverage of more global or diffuse quality factors, such as mild compression, color cast, banding, overall exposure mismatch, or subtle background artifacts. This matters because image quality assessment is not only about local salient regions. The current evidence supports a useful local grounded-IQA setting, but not yet the full breadth of IQA suggested by the framing.

10. **Presentation is generally decent, but there are several notation and referencing inconsistencies that matter.**  
    A few examples: in **Section 3.1**, the text refers to “Fig. 5a” and “Fig. 5b” when describing the task definitions, but these are clearly conceptual examples shown earlier in **Figure 2**, while **Figure 5** contains dataset instances. In **Section 3.2**, the notation alternates between \( \mathcal{T}_r \) and \( \mathcal{T}r \), and the phrasing around coordinate tokens and token counts is loose. These are not fatal issues, but they contribute to a sense that the paper is strong on motivation and system building, yet less careful in the formal details.

## Questions
1. **Can the authors provide a direct human validation of the automatically generated GIQA-160K annotations in the main rebuttal?**  
   In particular, I would like to see estimated precision for extracted object tags, bounding boxes after refinement, and GIQA-VQA question-answer correctness, ideally on a random held-out subset. This would materially increase my confidence in the dataset contribution.

2. **Please clarify the exact coordinate discretization mathematically.**  
   For **Equation (1)**, what are the quantization operators applied to \(x_1,y_1,x_2,y_2\)? Are \(x\) and \(y\) first mapped to cell indices by floor, round, or nearest-center assignment? In **Equation (2)**, is \( \mathrm{idx}/n \) integer division? A corrected formulation would help a lot.

3. **Please fully specify Tag-Recall.**  
   What exact function is used for “object name similarity”? How are multiple predicted tags/boxes matched to multiple references? Is there one-to-one matching, greedy matching, or Hungarian matching? Since this metric appears throughout the tables, a precise definition is important.

4. **How robust are the LLM-judge metrics?**  
   Please report the exact evaluation prompt, decoding settings, and whether scores are averaged across multiple runs. If possible, providing inter-run variance or agreement with human preference on a subset would substantially strengthen the empirical claims.

5. **Can the authors break down GIQA-Bench by distortion type and spatial scope?**  
   A split between local-object-centered degradations versus more global degradations would help determine whether the method truly advances IQA broadly or mainly improves localized defect reasoning.

6. **How much of the gain comes from grounded supervision versus simply more IQA instruction data?**  
   A useful control would be to train on the same generated descriptions and QA but remove coordinates, or randomize coordinates, to test whether the grounding signal itself is responsible for the improvement.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics concerns stood out from the main paper. The work is primarily about dataset construction and evaluation for image quality assessment. Standard dataset provenance and licensing questions remain relevant for reused public datasets, but nothing in the main paper suggests an ethics flag beyond ordinary diligence.

## Soundness Rating
**2: fair.** The paper is technically plausible and empirically supported to a reasonable extent, but several core pieces, especially the coordinate formulation, metric definitions, and automated annotation validation, are not specified rigorously enough for a higher soundness score.

## Presentation Rating
**3: good.** The paper is generally readable, well organized, and supported by useful figures and tables, but there are enough notation inconsistencies and underspecified details that it falls short of excellent.

## Contribution Rating
**3: good.** The task formulation, dataset, and benchmark are valuable and likely useful to the community, though the novelty is more in problem framing and resource construction than in a fundamentally new learning method, and the empirical scope is still somewhat narrow.

## Overall Rating
**6: Marginally above the acceptance threshold. But would not mind if paper is rejected.**  
I lean positive because the paper introduces a sensible and useful task formulation, provides nontrivial resources, and shows consistent gains on its benchmark. That said, the paper is not as airtight as the framing suggests: the benchmark is small, several metrics and equations are underspecified, and the main-paper validation of the automated pipeline is thinner than I would like. So this is a positive but cautious recommendation.

## Reviewer Confidence
**4: confident.** I am confident in the overall assessment and familiar with the relevant MLLM/IQA landscape, though a few implementation details are underspecified enough that I cannot verify every technical choice fully from the main paper alone.