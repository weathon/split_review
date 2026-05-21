---
job_id: 4e2bff38-e740-4f01-a57c-3a002d2f77f0
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: r5jxDjYeO4.pdf
paper: ASPD: Unlocking Adaptive Serial-Parallel Decoding by Exploring Intrinsic Parallelism in LLMs
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, focusing on efficient LLM inference, decoding algorithms, and architecture-level modifications for language generation.

## Minimum Quality
Pass ✅. The paper contains the expected components, including abstract, introduction, related work, methodology, experiments, quantitative results, and conclusion; despite several important technical and empirical weaknesses, it clears the minimum bar for full review rather than desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden instructions or manipulative text aimed at automated reviewing within the provided paper content.

# Expected Review Outcome:
## Summary
This paper proposes ASPD, an adaptive serial-parallel decoding framework for autoregressive LLMs that aims to exploit what the authors call intrinsic parallelism in model outputs. The method combines a data construction pipeline that rewrites and validates model responses into parallelizable branch structures, an internal masking and position-id scheme for parallel branch decoding within a single sequence, and a hybrid decoding engine that switches between serial and parallel modes while reusing KV cache. Experiments on dialogue, RAG, and mathematical reasoning benchmarks report improved speed-quality tradeoffs relative to several parallel decoding baselines.

## Strengths
The paper tackles an important systems-and-algorithms problem for LLM inference, namely how to reduce decoding latency without sacrificing output quality. This is relevant to the ICLR community, especially given the growing interest in inference-time efficiency beyond straightforward speculative decoding.

I appreciate that the paper does not stop at a high-level idea. It presents an end-to-end framework with three concrete components: data transformation, internal attention/positioning modifications, and inference engine design. Even if some parts need sharper justification, the overall system story is coherent.

The main empirical takeaway is practically appealing. In **Table 1** on MT Bench and Vicuna Bench, V-ASPD is clearly stronger than V-APAR and SoT on judged quality, while **Figure 4(a,b,c)** indicates a favorable speed-quality tradeoff relative to those baselines. In particular, on Vicuna Bench, the paper reports V-ASPD at 7.74 versus 7.62 for V-APAR* and 5.93 for SoT, while retaining strong speedup. That is the kind of tradeoff this line of work needs to demonstrate.

The paper also makes a good effort to evaluate beyond a single task family. The inclusion of RAG and math-style reasoning is useful, and **Table 2** suggests that the approach is not confined to chat-style itemization. The result on GPQA, where ASPD exceeds Seq (65.66 vs 61.11), is especially interesting because it hints that the parallelization recipe may occasionally act as a useful structural prior rather than merely a latency trick.

The visualizations help communicate the intended mechanism. **Figure 2** is useful in positioning ASPD against APAR and PASTA at the mechanism level, especially around the claimed handling of branch visibility and positional continuity. **Figure 3(b)** is also helpful in conveying the serial-to-parallel switching behavior and the intended role of title generation and branch prefixes in the hybrid engine. This makes the core idea easier to follow than if it had been described only textually.

The ablation section is directionally helpful. **Table 4** tries to separate the effects of data pipeline choices, attention masking, and position-id strategies, which is the right instinct for a paper whose contribution is a combination of multiple interacting design decisions.

## Weaknesses
1. **The paper’s central novelty claim is weaker than the framing suggests, and the positioning against recent related work is incomplete.**  
   The paper presents ASPD as a broad framework for discovering parallelizable structure and decoding it within one sequence. However, much of the contribution appears to be an integration of already active ideas in this area: branch decomposition from outputs, hidden-branch decoding, custom masking, position-id manipulation, and KV-cache reuse. The paper discusses APAR, PASTA, APR, PDOS, and Multiverse, but it does not do enough to isolate what is fundamentally new versus what is an engineering refinement or a better-trained variant. This matters because for an ICLR main-track paper, the contribution should be more sharply distinguished than “we do the same general thing, but more carefully.” The manuscript would be stronger if Section 2 and Section 3 explicitly decomposed novelty into: data extraction novelty, masking novelty, position-id novelty, and engine novelty, with a precise statement of which parts are absent from prior work.

2. **The mathematical specification in Section 3.2 is underspecified and partially inconsistent, which is serious because the masking and positioning equations are the core technical contribution.**  
   In **Equation (2)**, the attention mask is defined by
   \[
   M_{i,j}=\begin{cases}
   0 & \text{if } \mathcal{S}(b(i),b(j))=1 \text{ and } \text{pos}(i)>\text{pos}(j)\\
   -\infty & \text{otherwise}
   \end{cases}
   \]
   but this omits the usual allowance for self-attention or equality, unless the implementation implicitly shifts indices. If self-attention is disallowed by design, that should be stated and justified. If not, the strict inequality should likely be \(\text{pos}(i)\ge \text{pos}(j)\) or there should be a separate diagonal treatment. As written, the mask definition is not fully standard and can materially affect reproducibility.

   **Equation (3)** is even more problematic. The piecewise definition of \(\mathcal{S}(b(i),b(j))\) is malformed in the text:
   \[
   \mathcal{S}(b(i),b(j))=\begin{cases}
   1&\text{if }b(i)\text{ in main branch}\\
   1&-b(i),b(j)>\text{ in same parallel branch}\\
   1&-b(i),b(j)>\text{ in different stage}\\
   0&\text{otherwise}
   \end{cases}
   \]
   This is not just cosmetic, it leaves ambiguity about exactly when branch tokens can attend across branches and across stages. Given that the masking logic is the whole point of the architecture, the paper needs a formally correct definition, ideally with Boolean predicates such as
   \[
   \mathcal{S}(i,j)=\mathbf{1}\!\left[\text{Main}(i)\ \lor\ \big(\text{Stage}(i)\neq \text{Stage}(j)\big)\ \lor\ \big(\text{Branch}(i)=\text{Branch}(j)\big)\right].
   \]
   Without this, it is hard to verify the claim that branch decoding is “behaviorally consistent with native serial decoding from each branch’s perspective.”

   **Equation (4)** also raises questions. For main-branch tokens,
   \[
   \text{pos}(i)=\sum_{t=1}^{i-1}P_t+1
   \]
   but \(i\) is previously used as a token index, not a time index. This makes the expression hard to interpret, because \(P_t\) is defined as the number of tokens decoded simultaneously at time \(t\). The paper needs consistent indexing over tokens versus timestamps. Right now, the formalism mixes token-level and time-step-level quantities in a way that is not mathematically clean.

3. **The claims of “lossless”, “no information loss”, and preserving native autoregressive behavior are stronger than what the paper actually establishes.**  
   On **Page 2**, the paper claims that switching back to the primary branch incurs “no information loss and recomputation overhead.” On **Page 6**, it says each branch maintains “the same generation pattern as native autoregressive models from its own perspective.” These are strong claims. However, there is no theorem, proposition, or even a careful equivalence argument showing that the joint hidden states under branch-shared positions and branch-invisible masking are functionally equivalent to serial generation over a corresponding linearized sequence. In fact, shared position ids across different branches can easily create aliasing relative to standard AR position semantics, and branch prefixes such as `"<branch> T_i:"` alter the actual conditioning context. This matters because the entire conceptual pitch is that the method achieves acceleration without changing behavior in any meaningful way. The current evidence is empirical only, and even there the quality is not perfectly preserved.

4. **The empirical comparisons are narrower and less fair than the paper suggests, especially for a paper making strong efficiency claims.**  
   The strongest baselines are mostly from the same semantic-parallelism family, such as APAR and SoT. That is reasonable, but for a paper centered on practical LLM inference efficiency, the lack of comparison to stronger token-level acceleration baselines in a unified setup is noticeable. Since the paper argues for practical latency benefits, it should at minimum discuss how ASPD relates to and complements speculative decoding in actual serving systems, not just in the related work paragraph. This is particularly important because the reported speedups, while meaningful, are not so dominant that one can ignore other acceleration paradigms.

   More concretely, the reported main comparisons rely heavily on Vicuna-7B and Qwen2.5-7B, with batch size 1 and a custom engine. That setup may favor the proposed mechanism. A stronger experimental case would include more realistic serving conditions, or at least clarify hardware, kernel efficiency, memory overhead, and branch-management overhead in more detail. **Figure 4** presents a speed-quality frontier, but the axes alone do not establish whether the system would remain favorable in production stacks where scheduling, memory fragmentation, and framework-level optimizations matter.

5. **The paper’s main quantitative story depends heavily on LLM-as-judge scores, while direct task-grounded evaluation is limited.**  
   In **Section 4.1**, the primary effectiveness metric for MT Bench and Vicuna Bench is LLM-as-judge using Qwen3-235B-A22B. That is standard in this literature, but the paper leans on very small differences. For example, in **Table 1**, V-Seq is 7.70 and V-ASPD is 7.74 on Vicuna Bench, while Q-Seq is 9.11 and Q-ASPD is 9.03. These are tiny margins. The paper repeatedly interprets them as evidence of quality preservation or improvement, but without confidence intervals, run-to-run variance, or test-retest robustness, it is hard to know which differences are meaningful. This matters because the selling point is “maintaining quality while accelerating decoding.” When the gains are near the noise floor of judge-based evaluation, stronger statistical treatment is needed.

6. **Several result tables contain formatting or interpretability issues that make important claims harder to trust.**  
   **Table 3** is especially problematic. Entries such as “27.141.17x” and “43.031.86x” appear to merge raw TPS with speedup multipliers in the same cell without clear formatting. Similar issues occur for other rows. This makes it unnecessarily difficult to parse whether the table reports absolute throughput, multiplicative gain, or both. Since efficiency is a central contribution, this kind of sloppiness in the efficiency table is not minor.

   **Table 4** is also confusing. The subsection text in **Section 4.4.2** says “Shared masks consistently outperform Indep masks across both Seq and Max position id configurations,” but the table entries under “Attention Mask” do not straightforwardly support the subsequent sentence “This empirical finding strongly validates our design decision to maintain strict branch isolation.” In fact, if “Shared” outperforms “Indep”, that would seem to cut against strict branch invisibility, unless the authors are using “Indep” to denote their favored choice and the prose is flipped. Right now, either the table labels or the interpretation is inconsistent. This is not a superficial nit, it directly affects the claimed rationale for the proposed masking design.

7. **The data construction pipeline is powerful but introduces a substantial hidden source of supervision and potential bias that is under-analyzed.**  
   In **Section 3.1**, the pipeline repeatedly uses an external LLM to rewrite, verify independence, verify integrity, and verify answer correctness, all with majority voting. This is effectively a strong teacher pipeline. The paper calls it “non-invasive,” but that description is a little too flattering. The distribution of the resulting data is shaped by the prompting behavior, judgment tendencies, and inductive biases of the verifier model. There is also a selection effect in Step 4, where candidates with higher DP and ABN are preferred. That means the training corpus is explicitly optimized toward easy-to-parallelize structures. This matters scientifically because the reported performance may partly reflect a strong data curation and distillation pipeline rather than the intrinsic merit of the decoding architecture itself. The paper should better disentangle “better data created by a large teacher model” from “better decoding mechanism.”

8. **The paper does not sufficiently analyze failure cases, despite the method being highly dependent on detecting valid branch independence.**  
   The paper acknowledges that semantic dependencies are tricky, but the experiments focus mostly on average-case wins. There is very little analysis of when the pipeline misidentifies a branchgroup, when branch titles are ambiguous, when parallel branches subtly depend on each other, or when the hybrid engine triggers parallel mode inappropriately. This is exactly where the method could break in realistic use. **Figure 1** is used to motivate the existence of parallelizable structure across domains, and **Figure 5** in the appendix shows qualitative parallelization patterns, but neither figure probes failure or brittleness. For a method whose correctness depends on semantic decomposition, the lack of error taxonomy is a major omission.

9. **The claim of broad cross-domain generalization is overstated relative to the evidence.**  
   The paper reports results on general chat, RAG, and math, which is good coverage, but the models, data pipelines, and even training corpora differ substantially across settings. For the reasoning experiments in **Section 4.3**, the setup shifts to Qwen2.5-32B-Instruct and OpenR1-Math-220K, trained for 9 epochs with different context lengths and batch sizes. This is understandable, but it weakens the claim that one unified ASPD recipe broadly generalizes. A reader cannot tell whether the gains stem from the architecture, the task-specific data transformation pipeline, the stronger backbone, or the specialized training corpus.

10. **Some of the strongest figures support the paper’s motivation, but they also expose missing analysis that the authors should address.**  
   **Figure 1** is visually effective in motivating “data intrinsic parallelism” and “model internal parallelism,” but it remains largely descriptive. The upper panel reports PPD, DP, and ABN across datasets, yet the paper never rigorously explains how these statistics are estimated before training, after training, or under which model outputs. Since this figure underpins the entire premise that there is substantial exploitable intrinsic parallelism, the methodology for computing these quantities should be in the main paper, not only referenced abstractly. Similarly, **Figure 3(a)** makes the data pipeline look clean and deterministic, but the actual process depends on multiple prompting and majority-vote decisions from an external LLM. The figure slightly oversells stability relative to the textual description.

11. **There are presentation issues in the main paper that hinder technical confidence.**  
   Beyond the malformed equations, there are multiple grammatical slips and contradictions, for example “We introduces” on **Page 2**, and several places where the paper overstates empirical findings. The writing is usually understandable, but not polished enough for a method paper whose correctness rests on careful masking and positional definitions. The appendix prompt section also contains malformed tags and examples, which may not affect the core contribution directly, but it reinforces the impression that the technical details were not checked as carefully as they should have been.

## Questions
1. The most important clarification is the exact formal definition of the visibility function in **Equation (3)** and the indexing semantics in **Equation (4)**. Please rewrite these equations cleanly and specify whether self-attention on the diagonal is allowed in **Equation (2)**. A precise pseudocode block for mask and position-id construction would materially increase my confidence.

2. Can you provide a stronger argument, empirical or formal, for the claim that branch decoding preserves native autoregressive behavior “from each branch’s perspective”? For example, under what assumptions would the logits for a branch token in ASPD match those from a serially decoded branch-conditioned sequence?

3. In **Table 4**, the text in Section 4.4.2 appears inconsistent with the reported attention-mask ablation. Which masking strategy is actually preferred by the results, Shared or Indep? Please reconcile the table, the terminology, and the conclusion.

4. How much of the gain comes from the data pipeline versus the decoding architecture? A useful rebuttal would separate:  
   (a) training only on parallel-rewritten data but decoding serially,  
   (b) architecture changes without the LLM-verified rewriting pipeline, and  
   (c) the full system.  
   The paper hints at this through Seq and ASPD, but not cleanly enough to isolate the effect of teacher-driven data curation.

5. Since many quality differences in **Table 1** are small, can you provide variance estimates, repeated runs, or confidence intervals for judge scores and throughput? This is especially important for claims of “within 1% difference” or slight gains over Seq.

6. Please clarify how PPD, DP, and ABN in **Figure 1** are computed. Are these statistics measured on rewritten training data, on model generations, or on benchmark outputs after fine-tuning? The current figure is central to the paper’s motivation, but the measurement protocol is not explicit enough.

7. What are the main failure cases of the pipeline and the hybrid engine? I would be particularly interested in examples where independence verification passes but the final merged answer becomes incoherent, or where branch-title conditioning causes mode-triggering errors.

8. Can you comment on serving overhead beyond TPS, for example memory use, branch scheduling costs, and implementation complexity in mainstream inference stacks? **Table 5** provides wall-clock latency, which is useful, but deployment realism would be better supported by a clearer accounting of overheads.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics concerns are apparent from the main paper. The work is about inference acceleration for language models and does not introduce a new dataset involving sensitive human subjects in the main text.

## Soundness Rating
2: fair. The core idea is plausible and partially supported by experiments, but the masking/positioning formalization has important ambiguities, and several central claims are stronger than the evidence provided.

## Presentation Rating
2: fair. The paper is generally readable and the figures are helpful, but there are notable issues in the equations, table formatting, and consistency between some experimental claims and reported results.

## Contribution Rating
2: fair. The paper has practical engineering value and some empirical merit, but the conceptual advance over closely related parallel decoding work is not sharply established, and the evidence does not fully support the strength of the claims.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The paper is interesting and potentially useful, but in its current form it overclaims relative to its mathematical precision, novelty positioning, and experimental rigor. With cleaner formalization, stronger ablations, and better analysis of failure modes and deployment realism, I could see this moving into positive territory.

## Reviewer Confidence
4: confident. I am confident in this assessment, though not absolutely certain. The paper is in an area I know well, and I checked the main technical and empirical claims carefully, but some implementation details remain ambiguous from the manuscript.