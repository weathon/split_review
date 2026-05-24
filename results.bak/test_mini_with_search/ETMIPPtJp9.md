Now I have enough calibration data. Let me write the consolidated review.

## Summary

This paper proposes FiDeLiS, a training-free retrieval-augmented reasoning method for Knowledge Graph Question Answering (KGQA). It combines two components: (1) Path-RAG, a keyword-enhanced retrieval mechanism that fetches entities and relations from a vector-based KG index, and (2) Deductive-Verification Guided Beam Search (DVBS), which uses LLM-based deductive reasoning as a scoring and termination criterion during beam search. Experiments on WebQSP, CWQ, and CR-LT show competitive results, outperforming the training-free baseline ToG with the same LLM backbone and approaching/beating finetuning methods when using GPT-4-turbo.

## Strengths

- **High-recall retrieval demonstrated via coverage ratio.** Figures 3a-b show Path-RAG achieves higher coverage of ground-truth reasoning paths compared to a vanilla retriever across all depths on both CWQ and WebQSP, directly supporting the claim that keyword-enhanced retrieval improves recall (Section 4.3).

- **Deductive verification yields more precise termination.** Table 5 reports that FiDeLiS produces reasoning path depths (2.4, 2.8, 4.6) much closer to ground-truth depths (2.3, 3.2, 4.7) than ToG (3.1, 4.1, 5.2) across all three datasets. This provides evidence that the deductive verification criterion meaningfully signals when to cease reasoning (Section 4.3).

- **Ablation confirms each component's role.** Table 2 quantifies the impact of removing beam search (18.97% Hits@1 drop on WebQSP), deductive verifier (5.19% drop), and Path-RAG (6.97% drop), showing each component is necessary for the overall result (Section 4.2).

- **Efficiency gains over the training-free baseline.** Table 6 shows FiDeLiS reduces average runtime per question to 43.83s on WebQSP (vs. 74.26s for the ToG-based retrieval variant) and 74.59s on CWQ (vs. 132.59s), with lower token usage (2,452 vs. 6,437 on WebQSP). This supports the claim of lower computational cost (Section 4.4).

- **Robustness across different embedding backbones.** Table 3 shows Path-RAG outperforms a vanilla retriever consistently across BM25, SentenceBert, E5, and OpenAI-Embedding backbones, e.g., with E5 achieving 77.93% vs. 68.42% on WebQSP. This demonstrates the retrieval design is generally beneficial, not tied to a specific embedding model (Section 4.3).

## Weaknesses

### Fatal
None.

### Major

- **The paper's central claim about "faithful reasoning" is not directly evaluated on the proposed method.** The paper is titled "Faithful Reasoning" and repeatedly emphasizes that FiDeLiS produces verifiable, KG-grounded paths. However, the only explicit validity ratio (VR) evaluation is conducted on the baseline RoG (Figure 3c: 67% valid steps), not on FiDeLiS. The paper defines VR as the ratio of steps that exist in the KG but never reports it for its own method. While the method *constructs* paths from KG candidates (so each step should exist in the KG by design), the absence of direct empirical validation of the headline claim is a meaningful gap. The authors should compute and report the validity ratio for FiDeLiS (and ideally compare it to ToG and RoG) to substantiate the faithfulness claim.

- **The deductive verification component is underspecified.** The criterion \(C(q', s^t, s^{1:t-1})\) in Equation (5) is defined abstractly as "1 if q' can be deduced from s^t and s^{1:t-1}, 0 otherwise," but: (1) \(q'\) is introduced without definition (it is presumably a simplified or decomposed form of the query, but the paper never clarifies); (2) no prompt template is provided for how the LLM is instructed to perform this deduction; (3) it is not specified whether verification uses the same or a different LLM. Additionally, \( \mathcal{K} = \text{LM}(\text{prompt}_p, q) \) references a prompt that is never shown. These omissions hinder reproducibility, as the performance gains could depend significantly on prompt engineering choices.

- **The comparison with finetuning baselines is confounded by LLM capacity.** In Table 1, FiDeLiS with GPT-4-turbo outperforms finetuning methods (DeCAF, RoG) that use smaller backbone models (RoBERTa, BART). However, with GPT-3.5-turbo, FiDeLiS (79.32% Hits@1 on WebQSP) *underperforms* DeCAF (82.1%) and RoG (83.15%), indicating that the advantage over finetuning methods is partially attributable to the stronger LLM backbone. The paper should acknowledge this nuance more clearly. The fair comparison (FiDeLiS vs. ToG with matching backbones) is valid and favorable, but the framing "outperforms established strong baselines" without qualification overstates the evidence for the method's intrinsic superiority.

### Minor

- **The \( \alpha \) parameter in the Path-RAG scoring function (Equation 4) is introduced but never reported or ablated.** The paper describes \( \alpha \) as balancing short-term vs. long-term outcomes but does not state its default value or study its sensitivity. Given the scoring function is central to Path-RAG, this is a noticeable omission.

- **The "w/o beam-search" ablation is underspecified.** Table 2 shows a large drop (18.97% on WebQSP) when beam search is removed, but the paper does not describe what selection mechanism replaces it. Without this detail, it is unclear whether the drop reflects the importance of beam search specifically or a strawman replacement.

- **No statistical significance or variance reporting.** All results are reported as single point estimates without confidence intervals or significance tests, making it difficult to assess whether improvements over ToG (e.g., 84.39% vs. 81.84% with GPT-4-turbo on WebQSP) are robust.

### Trivial

- **Sections 2 (Preliminary) and 3 (Method) contain near-verbatim duplicate definitions** (reasoning step, reasoning path, validity). This is redundant and wastes space.

- **The case study in Table 7 is illustrative but single-example evidence.** While it effectively demonstrates the method, a small table of success/failure types would strengthen the qualitative analysis.

## Nice-to-Haves

- A limitations section discussing reliance on LLM keyword-generation quality, embedding model quality, KG pre-indexing scalability for very large KGs (e.g., Wikidata), and potential LLM biases in the deductive verification step would strengthen the paper.
- Providing the prompt templates used for keyword generation, planning, step selection, and deductive verification would aid reproducibility.
- Ablating the value of \( \alpha \) in Equation (4) would help understand the scoring function's behavior.

## Removed Points

- *Criticism about unfair comparison with finetuning methods being "fatal":* Demoted to Major. The paper does present FiDeLiS vs. ToG with the same LLM backbone as a fair comparison, and the GPT-3.5-turbo results are transparently reported. The issue is about framing, not data integrity.
- *Criticism about the paper missing related works:* Removed per instruction — I do not have external sources to confirm whether these works exist and should not assume the paper missed them.
- *Formatting/style nitpicks (color shading in table, font sizes):* Removed as pure formatting issues unrelated to scientific content.
- *Speculation about GPT-4 log-probability accessibility:* Removed. The paper does not specify how probabilities are obtained, but this is covered under the general underspecification weakness.
- *Generic concern about "comparison not being apples-to-apples":* Merged with the Major weakness about the LLM backbone confound rather than kept as a separate, vaguer point.
- *Strength: "Concrete case study illustrating complex query handling":* Kept but this is illustrative evidence, not a core strength. It supports the method's plausibility.
- *Strength: "Error analysis motivating approach":* Kept but noted that it only evaluates RoG, which is also a weakness of the paper itself.
- *"Missing appendix/table for open-source model results":* Removed. The parser strips appendix sections from all papers; they exist in the original submission.

## Novel Insights

None beyond the paper's own contributions. The reviewer analyses do not surface a perspective that the paper itself does not present.

## Suggestions

1. **Directly measure faithfulness.** Compute and report the validity ratio (percentage of reasoning steps that exist in the KG) for FiDeLiS's own generated paths across all three datasets, and compare it to ToG and RoG. This single addition would substantiate the paper's central claim.

2. **Provide prompts and define \( q' \).** Include the prompt templates for keyword generation, planning, step selection, and deductive verification in the appendix. Clarify what \( q' \) represents (a sub-question? a simplified query?) and whether the verifier is a separate LLM call or part of the same prompt.

3. **Nuance the comparison with finetuning baselines.** Acknowledge that the advantage over DeCAF/RoG is partly attributable to the stronger LLM backbone. Report FiDeLiS with a weaker backbone (e.g., Llama-3) against finetuning methods to isolate the method's contribution.

4. **Report the default value of \( \alpha \)** and consider a brief sensitivity analysis. This is a small addition that would close a noticeable gap.

5. **Describe the replacement for beam search in the "w/o beam-search" ablation** to clarify what is being compared.

## Score and Decision

**Round 1 bracket:** Based on initial anchors, I estimated the paper falls between 4.5 and 6.5. The weak anchor at 3.00 (KGQA-Star, withdrawn) was clearly below this paper. The mid-range anchors at 5.00 (CoD, poster) and 6.00 (DAMR, poster) were much more representative. The high-range anchors (8.00) were on unrelated topics and not useful for direct comparison.

**Round 2 narrowing:** I pulled anchors inside the 4.5–7.0 range, yielding: KG-Infused RAG (4.50, reject), FREESON (4.50, reject), EoG (5.50, poster), VoG (5.50, poster), and DAMR (6.00, poster). Reading EoG and VoG in full showed papers with similar contribution levels to FiDeLiS — all accepted as posters with clear methodology, solid experiments, and some reproducibility gaps.

**Final score analysis relative to anchors:** FiDeLiS is comparable to VoG (5.50) and EoG (5.50) in overall quality. Like VoG, it has a clean method, good experimental validation, and some underspecified components. It is weaker than DAMR (6.00) which had more comprehensive experiments and stronger efficiency claims, but stronger than CoD (5.00) which had presentation issues and less thorough analysis. I position FiDeLiS at 5.5: above CoD due to better ablation/efficiency analysis and training-free status, but below DAMR due to the significant gap of not directly evaluating its central faithfulness claim on its own outputs.

**Anchor comparison table:**

| Anchor Paper | Path | Avg Score | Round | Comparison |
|---|---|---|---|---|
| KGQA-Star | wBU6aBTcPF | 3.00 | R1 | Much weaker: complex RL method with limited novelty; FiDeLiS is clearly stronger |
| SEAL-RAG | QqjUfdPkkb | 2.50 | R1 | Much weaker: different sub-area (corpus RAG), less relevant |
| GRAPE | QIN5GrCB7d | 2.50 | R1 | Much weaker: different approach |
| MA-RAG | Yc9LTfD7DY | 3.00 | R1 | Much weaker: multi-agent RAG, less relevant |
| Chain-of-Decomposition (CoD) | 4vfEo07rmv | 5.00 | R1/R2 | Weaker: similar KGQA area but with presentation issues and less thorough analysis; FiDeLiS is stronger |
| DAMR | mUx7WLC8q6 | 6.00 | R1/R2 | Slightly stronger: more comprehensive experiments, though has reproducibility gaps; comparable but FiDeLiS lags on the faithfulness evaluation gap |
| Verifier-Guided Beam Search | ZN1fL8jLfr | 4.40 | R1 | Different focus (math reasoning scaling flaws) |
| CtrlHGen | oTgJg0M9kY | 5.50 | R1 | Different sub-area (abductive reasoning) |
| KG-Infused RAG | vhDOprq9Hf | 4.50 | R2 | Weaker: corpus-based RAG with KG infusion |
| FREESON | au9aGVAaTJ | 4.50 | R2 | Weaker: retriever-free RAG using MCTS |
| FaithCoT-Bench | lN3yKqqzF1 | 6.50 | R2 | Different focus (benchmark for CoT faithfulness) |
| Explore-on-Graph (EoG) | NfuBj8jleE | 5.50 | R2 | Very similar in quality: both KG+LLM reasoning papers, accepted as poster; comparable contribution level |
| VoG | 0RdAmwfVku | 5.50 | R2 | Very similar in quality: both stepwise verification on KGs, comparable contribution and weakness profile |

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>