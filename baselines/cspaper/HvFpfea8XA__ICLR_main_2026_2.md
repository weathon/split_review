---
job_id: 1a33fd28-da27-498f-80ed-f3e11dc98898
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: HvFpfea8XA.pdf
paper: Dynamic Context Adaptation for Consistent Role-Playing Agents with Retrieval-Augmented Generations
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, focusing on retrieval-augmented generation, role-playing LLM agents, and a benchmark dataset for evaluating persona-consistent language modeling.

## Minimum Quality
Pass ✅. The submission includes the expected scientific components, namely abstract, introduction, related work, methodology, experiments, quantitative results, and conclusion. While there are notable weaknesses in rigor and presentation, the paper is sufficiently complete and research-oriented to merit full review rather than desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find any hidden prompts, reviewer-directed instructions, or suspicious manipulative text in the provided paper content.

# Expected Review Outcome:
## Summary
This paper studies retrieval-augmented role-playing agents and argues that standard RAG pipelines struggle when users ask questions that are not explicitly answered in a character’s persona document. To address this, the authors propose AMADEUS, a training-free framework with three components, ACTS for persona chunking with hierarchical context, GS for LLM-guided chunk selection, and AE for extracting higher-level character attributes from retrieved chunks. The paper also introduces CharacterRAG, a manually constructed dataset of 15 fictional characters with persona documents and 450 QA pairs, and evaluates the method on in-knowledge QA as well as personality-oriented interview settings based on MBTI and BFI.

## Strengths
The paper tackles a reasonably well-motivated problem. The gap it identifies, namely that RAG-based role-playing can fail badly on out-of-knowledge questions even when the desired behavior should still remain persona-consistent, is real and relevant for agent-style applications.

The overall pipeline is easy to understand at a high level. **Figure 3** is helpful here, because it makes the intended division of labor among ACTS, GS, and AE concrete: ACTS prepares persona chunks, GS filters for inferable evidence, and AE turns those chunks into explicit attribute-level conditioning. Even though some implementation details remain underspecified, the architecture diagram does a good job of communicating the intended workflow.

The paper contributes a new dataset, CharacterRAG, and the dataset construction effort appears nontrivial. The examples and statistics in **Figure 2** help clarify what the persona documents look like and how the benchmark is structured. In particular, the example persona page in **Figure 2(b)** makes it easier to see why hierarchical headings could matter for retrieval, since narrative episodes are nested under broader sections.

The empirical results do suggest that the proposed method improves over the specific baselines included in the paper. In **Table 4**, AMADEUS modestly but consistently improves over Naive RAG on CharacterRAG across GPT-4.1, Gemma3-27B, and Qwen3-32B, with the strongest gains showing up in hallucination score for Qwen3-32B and small gains in ACC / \(ACC_L\). These are not huge jumps, but they are directionally consistent.

The results on personality-style evaluations are more substantial within the paper’s chosen setup. In **Table 1**, AMADEUS improves MBTI accuracy from 65.00 to 85.00 and BFI accuracy from 72.00 or 76.00 to 81.33, depending on baseline, under the GPT-4.1 setting. If one accepts MBTI/BFI agreement as a proxy for persona consistency, that table supports the claim that the method helps on questions outside explicit persona knowledge.

I also appreciated that the paper did not only report end-task numbers but tried to inspect retrieval behavior. **Figure 1** is a useful diagnostic figure: the claim is that chunk usage becomes more uniform under the proposed method for out-of-knowledge MBTI questions, which aligns with the intuition that the model should not keep collapsing onto a small set of repeatedly reused chunks.

## Weaknesses
1. **The main empirical gains are difficult to attribute cleanly because the method is not compared under a controlled ablation ladder.**  
   The method has three distinct components, ACTS, GS, and AE, but the main end-task comparisons in **Table 4** and **Table 1** are primarily against external baselines such as Naive RAG, CRAG, and LightRAG, not against strong internal ablations like ACTS-only, ACTS+GS, GS-only, AE-only, or ACTS+AE without GS. This matters because the paper’s central claim is not simply that “some pipeline works,” but that each component addresses a specific failure mode. Right now, the evidence for those claims is fragmented: **Table 2** speaks to chunking, **Table 3** speaks to attribute extraction reasonableness, and **Table 1/4** speak to end-task outcomes, but the paper never really closes the loop. Without a full component-wise ablation on the final tasks, it is hard to know whether AE is genuinely necessary, whether GS is doing most of the work, or whether ACTS alone already explains most of the gains.

2. **Several parts of the mathematical and algorithmic formulation are too loose to support the level of certainty in the claims.**  
   In Section 4.1, **Equation (4)** defines \(l_{\max} = \varphi(p_1,\dots,p_l)\), where \(\varphi\) is merely “a length-calculating function.” That is not really a mathematical definition; from the text it appears to mean the maximum paragraph length, but this should be stated explicitly as something like \(l_{\max} = \max_j \varphi(p_j)\). As written, the equation is ambiguous.  
   Likewise, **Equation (3)** is not properly typed. \(\text{TopK}(\{\text{sim}(u,c_i)\}_{i=1}^n)\) returns scores or indices, but \(\mathcal{C}^*\) is later treated as a set of chunks. The intended object is presumably \(\mathcal{C}^* = \{c_i : i \in \text{TopKIndices}(\text{sim}(u,c_i))\}\). This seems minor, but it matters because retrieval formulations should be precise about whether one is selecting chunks, scores, or ranked positions.  
   The presentation around **Equations (5) and (6)** is also underspecified. If \(\hat c_i = [c_i; \mathcal H_i]\), then the embedding and retrieval are performed over augmented text containing both content and headers. This may help, but it also changes token distribution and similarity structure. The paper never formalizes whether \(\text{sim}(u,\hat c_i)\) is actually used during retrieval, even though that is the obvious implication. That missing link weakens the methodological clarity.

3. **Algorithm 1 is underspecified in a way that directly affects reproducibility and validity.**  
   The key decision step in GS, line 8 of **Algorithm 1**, says: “With an LLM, determine if chunk \(c\) contains information from which the character’s attributes can be inferred regarding \(u\).” This is the heart of the method, yet the decision rule is left almost entirely informal. What prompt is used? Is the LLM producing a binary label, a score, a chain-of-thought-style rationale, or structured JSON? Is the inference decision deterministic? Are there any few-shot examples? How is contradiction handled if a chunk suggests one trait and another chunk suggests the opposite? These details are not cosmetic. They determine whether GS is a stable retrieval policy or a brittle prompting trick.  
   There is also a likely typo or conceptual inconsistency in line 15: if \(|S|=0\), then the algorithm sets \(S \leftarrow\) “Top-\(K+1\) chunks from \(C_{\text{sorted}}\).” Why \(K+1\)? The rest of the paper uses top-\(K\) retrieval, and I could not find a principled reason for this off-by-one change. This should be clarified because it affects fairness of comparison with Naive RAG.

4. **The experimental design creates a confound because GS and AE are always implemented with GPT-4.1, even when the generator is Gemma3-27B or Qwen3-32B.**  
   Section 5.1 states that GS and AE use GPT-4.1 for all settings. This means that the proposed pipeline is not purely a retrieval wrapper around the evaluated backbone; it includes a stronger external model inside the inference loop. This is a serious issue for fair comparison. If Gemma3-27B + AMADEUS uses GPT-4.1 to select evidence and extract attributes, while Gemma3-27B + Naive RAG does not, then part of the gain may come from outsourcing key reasoning steps to a more capable model, not from the retrieval design itself. The same concern applies to Qwen3-32B.  
   This matters scientifically because the paper frames AMADEUS as a training-free framework, but in practice it is also a model-assisted framework whose quality partly depends on a powerful proprietary controller. The contribution would be much stronger if the paper showed same-backbone GS/AE, or at least a sensitivity analysis where GS/AE are run with weaker models.

5. **The claims about personality consistency are stronger than what the evaluation actually establishes.**  
   A large portion of the paper’s headline story rests on MBTI and BFI interview-style evaluations. However, matching externally assigned personality types is at best an indirect proxy for persona consistency. A character can answer MBTI-style prompts in a way that matches a community-voted label while still being unfaithful to speech style, social relationships, narrative constraints, or factual backstory.  
   This issue is especially important because the paper sometimes generalizes from these tests to broad statements like maintaining persona consistency “even when answering out-of-knowledge questions.” That is too sweeping. The evaluation mainly shows better alignment with a narrow psychological trait lens, not comprehensive persona faithfulness. The six-attribute taxonomy in Section 2.2 is broader than what AE actually models, since Section 4.3 only extracts Belief and Value plus Psychological Traits. There is a mismatch between the breadth of persona claimed and the narrowness of the explicit control signal.

6. **The evidence against competing RAG methods is not fully convincing, and some conclusions are overdrawn.**  
   The paper repeatedly argues that graph-based RAG and web-search-based RAG are unsuitable for role-playing. That is a much stronger statement than the experiments justify. The comparisons are limited to CRAG and LightRAG, both adapted to this setting, and even there it is not clear how much tuning effort was spent to make them competitive. Concluding that an entire class of methods is unsuitable based on these specific implementations feels overstated.  
   This problem is visible around the discussion of **Table 1** and **Table 4** on Pages 8-9. For example, LightRAG performs poorly in some settings, but the paper then expands this into a fairly broad methodological dismissal. That leap is not warranted without stronger baselines, more careful adaptation, or analysis of failure cases beyond a few anecdotal statements.

7. **The retrieval analysis in Table 2 and Figure 4 is statistically thin and not obviously tied to downstream quality.**  
   In **Table 2**, the paper reports sums of means and variances of similarity scores across chunking methods, but the construction of these aggregated statistics is not clearly explained. Why are \(\sum \mu\) and \(\sum \sigma^2\) the right summaries? Over what exact random variables are these computed, and why does a higher sum of similarity means necessarily imply better role-playing performance?  
   The subsequent argument around **Figure 4** is also shaky. The figure shows ridgelines based on a normality assumption using  
   \[
   \log f\big(x\mid \sum \mu,\sum \sigma^2\big)
   \]
   but this is more of a stylized visualization than a rigorous validation of the overlap coefficient \(\alpha\). The logic seems to be: choose \(\alpha=2\) because it maximizes mean similarity and minimizes variance under an assumed Gaussian model. That is not a strong basis for claiming an “optimal” overlap. A direct downstream ablation on QA and persona-consistency metrics would be more convincing than this detour through fitted score distributions.

8. **There are presentation issues, inconsistencies, and likely errors in the tables that reduce confidence in the results.**  
   The paper has multiple typographical and formatting problems that go beyond mere polish. Examples include “three folds” on Page 2, “prposed” on Page 6, “Attributer Extractor” in Section 4.3, and duplicated/garbled captions for **Table 4** on Page 9. The second “Table 4” appears to refer to CRAG/MBTI/BFI hallucination results but is mislabeled and not integrated cleanly with the surrounding text.  
   More concerning, **Table 1** includes several suspicious labels such as “INFI” and character names like “Frieten,” “Mão Mão,” and “Tanjiro Kainado,” which may be simple typos but still suggest insufficient proofreading in a paper where per-character labels are central. When tables contain obvious label errors, it becomes harder to trust the rest of the bookkeeping.

9. **The dataset is potentially useful, but its scale and evaluation protocol limit the strength of the benchmark contribution.**  
   CharacterRAG contains 15 characters and 450 QA pairs, which is a good start but still quite small for drawing broad conclusions about RAG-based role-playing. Because the benchmark uses a narrow set of fictional characters and manually curated personas, it is difficult to know whether the findings transfer to less structured personas, multilingual settings, original characters, or interactive multi-turn conversations.  
   This matters because the paper sometimes presents CharacterRAG as a general-purpose foundation for RAG-based RPAs. In reality, it looks more like a promising pilot benchmark than a definitive one. I would have liked to see stronger discussion of scope and limitations.

10. **Human evaluation is only partially informative.**  
    **Table 3** reports Likert judgments for whether the attributes extracted by AE from GS-selected chunks are reasonable. That is useful, but it evaluates an intermediate representation rather than final role-play quality. A mean near 4.0 with decent Cronbach’s alpha shows annotator agreement that the extracted attributes are plausible, not that responses generated from them are actually more faithful, vivid, or less hallucinatory in final dialogue. Since the paper’s real claim is about end-user-facing role-playing behavior, the human study stops one step short of the most important question.

## Questions
1. Can the authors provide a full end-to-end ablation on the final tasks, ideally including Naive RAG + ACTS, Naive RAG + ACTS + GS, Naive RAG + ACTS + AE, and the full ACTS + GS + AE pipeline? This would substantially improve confidence about where the gains in **Table 1** and **Table 4** actually come from.

2. Please clarify the exact implementation of GS in **Algorithm 1**. What is the prompt template used for the True/False decision, what output format is expected, and how do you ensure consistency across questions and characters? If there is any thresholding or post-processing, it should be stated explicitly.

3. Why does line 15 of **Algorithm 1** return “Top-\(K+1\)” chunks instead of top-\(K\)? Is this a typo, or an intentional design decision? If intentional, please explain why this does not make the fallback setting incomparable to the baseline in Section 3.

4. Can the authors disambiguate the mathematical definitions in **Equations (3)-(6)**? In particular, please define whether retrieval scores are computed over \(c_i\) or \(\hat c_i\), and rewrite **Equation (3)** so that \(\mathcal C^*\) is explicitly a set of chunks rather than an implicit set of top similarity values.

5. How much of the gain remains if GS and AE are implemented using the same model as the generator, rather than GPT-4.1? This is important for fair attribution of improvements, especially in the Gemma and Qwen settings.

6. Could the authors provide stronger evidence that the overlap coefficient choice in **Figure 4** improves downstream role-playing, not just similarity-score statistics? A direct ablation on CharacterRAG accuracy and hallucination would be much more convincing.

7. For the benchmark contribution, can the authors clarify how the 450 QA pairs are split across attributes and characters, and whether any validation set was used for tuning chunking or retrieval hyperparameters? This would help assess the risk of benchmark-specific tuning.

## Flag For Ethics Review
- Yes, Legal compliance (e.g., GDPR, copyright, terms of use)  
- Yes, Responsible research practice (e.g., human subjects, data release)

## Details Of Ethics Concerns
The ethics statement on **Page 10** says the dataset was obtained from Namuwiki and “adhered to applicable usage permissions,” but the paper does not provide enough detail in the main text about licensing, redistribution terms, or what exactly will be released when the code and dataset are made public. Since the benchmark is a paper contribution, the legal basis for releasing reconstructed persona documents should be stated more clearly.

The paper also reports human evaluation with 14 evaluators in Section 5.3, and the ethics statement says participants were informed and free to withdraw. That is good, but the main paper does not describe compensation, recruitment, or review/approval procedures. I am not flagging this as a major ethics violation, but the responsible-research details are too sparse for a benchmark paper involving human annotation and human evaluation.

## Soundness Rating
2: fair. The paper has a plausible core idea and some supporting experiments, but important parts of the method are underspecified, attribution of gains is incomplete, and some conclusions are stronger than the evidence supports.

## Presentation Rating
2: fair. The overall structure is readable, and several figures are useful, but the paper has enough notation issues, typos, table inconsistencies, and underexplained algorithmic details to noticeably hinder confidence.

## Contribution Rating
2: fair. The problem is relevant and the dataset/framework are potentially useful, but the methodological advance feels moderate, and the empirical validation is not yet strong enough to support the broader claims made in the paper.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The paper addresses an interesting problem and has some promising ingredients, especially the benchmark and the intuition of attribute-guided retrieval, but too many methodological and evaluation gaps remain for me to recommend acceptance at ICLR in its current form.

## Reviewer Confidence
4: confident. I am confident in this assessment, though not absolutely certain. The paper is in an area I know well, and I checked the main methodological and experimental details carefully, but some implementation details are missing from the paper and limit certainty.